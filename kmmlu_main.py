import os
import json
import time
import argparse

import openai
from openai import RateLimitError
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from datasets import Dataset, load_dataset

from prompts import TYPE_1, TYPE_2, TYPE_3, TYPE_4, TYPE_MMLU_FEW_SHOT
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_community.llms.azureml_endpoint import AzureMLOnlineEndpoint
from util.phi3_formatter import CustomPhi3ContentFormatter
from util.common_helper import str2bool
from logger import logger


def format_timespan(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = seconds - hours*3600 - minutes*60
    timespan = f"{hours} hours {minutes} minutes {remaining_seconds:.4f} seconds."
    return timespan


class CustomStrOutputParser(StrOutputParser):
    def parse(self, text: str) -> str:
        response = text.strip().replace('"', "").replace("'", "")
        if response.startswith("A"):
            pred = "A"
        elif response.startswith("B"):
            pred = "B"
        elif response.startswith("C"):
            pred = "C"
        elif response.startswith("D"):
            pred = "D"
        else:
            pred = ""  # Wrong answer

        return pred, response


def generate_few_shots_prompt(data):
    prompt = ""
    for i, row in enumerate(data):
        #prompt += f"## Example {i+1}:\n"
        prompt += f"질문 (Question): {row['question']}\n"
        prompt += f"보기 (Options)\nA: {row['A']}, B: {row['B']}, C: {row['C']}, D: {row['D']}\n"
        prompt += f"정답 (Answer): {row['answer']}\n\n"
    return prompt


def get_prompt(x, few_shots=None) -> str:
    if few_shots is None:
        return TYPE_2.format(
            QUESTION=x["question"],
            A=x["A"],
            B=x["B"],
            C=x["C"],
            D=x["D"],
        )        
    else:
        return TYPE_MMLU_FEW_SHOT.format(
            FEW_SHOTS=few_shots,
            QUESTION=x["question"],
            A=x["A"],
            B=x["B"],
            C=x["C"],
            D=x["D"],
        )

def get_answer(x) -> str:
    return x["answer"].upper().strip()


def map_answer(answer):
    answer_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    return answer_mapping[answer]


def convert_to_pascal_case(category):
    return '-'.join(word.capitalize() for word in category.split('_'))


def get_prompt_template(template_type):
    
    if template_type == "basic":
        prompt = PromptTemplate.from_template("{question}")
    elif template_type == "chat":
        system_prompt = """You are an AI assistant who reads a given question and solves multiple choice questions.
        You don't need to write a detailed explanation of your answer in sentences. Just answer in one word."""
        system_message_template = SystemMessagePromptTemplate.from_template(system_prompt)
        human_prompt = [
            {
                "type": "text",
                "text": "{question}"
            },
        ]
        human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

        prompt = ChatPromptTemplate.from_messages(
            [
                system_message_template,
                human_message_template
            ]
        )        
    else:
        raise Exception("Invalid 'template_type' value. Please choose from ['basic', 'chat']")
    return prompt


def benchmark(args):

    IS_DEBUG = args.is_debug
    MAX_RETRIES = args.max_retries
    DELAY_INCREMENT = 30
    MODEL_VERSION = None
    FEW_SHOTS = "5shot" if args.use_few_shots else "0shot"

    num_debug_samples = args.num_debug_samples
    batch_size = args.batch_size
    max_tokens = args.max_tokens
    temperature = args.temperature

    if args.is_hard:
        hf_dataset_id = "HAERAE-HUB/KMMLU-HARD"
        dataset_name = "KMMLU-HARD"
        kmmlu_category = [
            'accounting', 'agricultural_sciences', 'aviation_engineering_and_maintenance', 'biology', 'chemical_engineering', 'chemistry', 
            'civil_engineering', 'computer_science', 'construction', 'criminal_law', 'ecology', 'economics', 'education', 
            'electrical_engineering', 'electronics_engineering', 'energy_management', 'environmental_science', 'fashion', 
            'food_processing', 'gas_technology_and_engineering', 'geomatics', 'health', 'industrial_engineer', 'information_technology', 
            'interior_architecture_and_design', 'korean_history', 'law', 'machine_design_and_manufacturing', 'management', 
            'maritime_engineering', 'marketing', 'materials_engineering', 'math', 'mechanical_engineering', 'nondestructive_testing', 
            'patent', 'political_science_and_sociology', 'psychology', 'public_safety', 'railway_and_automotive_engineering', 
            'real_estate', 'refrigerating_machinery', 'social_welfare', 'taxation', 'telecommunications_and_wireless_technology'
        ]
    
    else:
        hf_dataset_id = "HAERAE-HUB/KMMLU"
        dataset_name = "KMMLU"
        kmmlu_category = [
            'Accounting', 'Agricultural-Sciences', 'Aviation-Engineering-and-Maintenance', 'Biology', 'Chemical-Engineering', 'Chemistry', 
            'Civil-Engineering', 'Computer-Science', 'Construction', 'Criminal-Law', 'Ecology', 'Economics', 'Education', 
            'Electrical-Engineering', 'Electronics-Engineering', 'Energy-Management', 'Environmental-Science', 'Fashion', 
            'Food-Processing', 'Gas-Technology-and-Engineering', 'Geomatics', 'Health', 'Industrial-Engineer', 'Information-Technology', 
            'Interior-Architecture-and-Design', 'Korean-History', 'Law', 'Machine-Design-and-Manufacturing', 'Management', 
            'Maritime-Engineering', 'Marketing', 'Materials-Engineering', 'Math', 'Mechanical-Engineering', 'Nondestructive-Testing', 
            'Patent', 'Political-Science-and-Sociology', 'Psychology', 'Public-Safety', 'Railway-and-Automotive-Engineering', 
            'Real-Estate', 'Refrigerating-Machinery', 'Social-Welfare', 'Taxation', 'Telecommunications-and-Wireless-Technology'
        ]        

    if args.model_provider == "azureopenai":
        logger.info("Using Azure OpenAI model provider.")
        MODEL_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
        MODEL_VERSION = os.getenv("OPENAI_MODEL_VERSION")
        llm = AzureChatOpenAI(
            azure_deployment=MODEL_NAME,
            openai_api_version=API_VERSION,
            temperature=temperature, 
            max_tokens=max_tokens,
            max_retries=MAX_RETRIES     
        ) 
    elif args.model_provider == "openai":
        logger.info("Using OpenAI model provider.")
        MODEL_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
        llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=temperature,
            max_tokens=max_tokens,
            max_retries=MAX_RETRIES
        )
    elif args.model_provider == "huggingface":
        if temperature == 0.0: # in case of not supporting 0.0 for some SLM, set to 0.01
            temperature = 0.01 
        MODEL_NAME = args.hf_model_id.split("/")[-1]
        logger.info("Using Hugging Face model provider.")
        llm = HuggingFaceEndpoint(
            repo_id=args.hf_model_id,
            temperature=temperature,
            max_new_tokens=max_tokens,
            huggingfacehub_api_token=os.getenv("HF_API_TOKEN")
        )

    elif args.model_provider == "azureml":
        logger.info("Using Azure ML endpoint as model provider.")
        MODEL_NAME = os.getenv("AZURE_ML_DEPLOYMENT_NAME")
        AZURE_ML_ENDPOINT_URL = os.getenv("AZURE_ML_ENDPOINT_URL")
        AZURE_ML_ENDPOINT_TYPE = os.getenv("AZURE_ML_ENDPOINT_TYPE") # https://python.langchain.com/v0.2/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType
        AZURE_ML_API_KEY = os.getenv("AZURE_ML_API_KEY")
        
        llm = AzureMLOnlineEndpoint(
            endpoint_url=AZURE_ML_ENDPOINT_URL,
            endpoint_api_type=AZURE_ML_ENDPOINT_TYPE,
            endpoint_api_key=AZURE_ML_API_KEY,
            content_formatter=CustomPhi3ContentFormatter(),
            model_kwargs={"temperature": temperature, "max_new_tokens": max_tokens
            }              
        )

    logger.info(f"====== [START] Generate answers to questions given by LLM. =====")
    if args.use_few_shots:
        logger.info(f"===== Use Few-shots Prompt.")
    else:
        logger.info(f"===== Use Zero-shot Prompt.") 
    logger.info(f"====== deployment name: {MODEL_NAME}, model version: {MODEL_VERSION} =====")
    responses = []
    
    # Load the datasets and append to the list with their respective categories
    for c in kmmlu_category:
        logger.info(f"##### Category [{c}] Processing...") 
        ds_dict = load_dataset(hf_dataset_id, c)

        # For few-shot prompts, we need to generate a prompt with examples
        ds_dev = ds_dict["dev"]
        ds_dev = ds_dev.map(lambda x: {'answer': map_answer(x['answer'])})
        if args.is_hard:        
            ds_dev = ds_dev.map(lambda x: {'category': convert_to_pascal_case(x['category'])})                
        else:
            ds_dev = ds_dev.rename_column("Category", "category")

        ds = ds_dict["test"]
        ds = ds.map(lambda x: {'answer': map_answer(x['answer'])})
        if args.is_hard:
            ds = ds.map(lambda x: {'category': convert_to_pascal_case(x['category'])})                   
        else:
            ds = ds.rename_column("Category", "category")    
    
        if IS_DEBUG:
            ds = ds.select(range(num_debug_samples))

        if args.use_few_shots:
            few_shots = generate_few_shots_prompt(ds_dev)
        else:
            few_shots = None

        #all_batch = [{"category": x["category"], "question": get_prompt(x, few_shots), "answer": get_answer(x)} for x in tqdm(ds)]   
        all_batch = [{"category": c, "question": get_prompt(x, few_shots), "answer": get_answer(x)} for x in tqdm(ds)]   

        prompt_template = get_prompt_template(args.template_type)
        chain = prompt_template | llm | CustomStrOutputParser()

        t0 = time.time()

        with tqdm(total=len(all_batch), desc="Processing Answers") as pbar:

            for i in range(0, len(all_batch), batch_size):
                mini_batch = all_batch[i:i+batch_size]
                retries = 0
                
                while retries <= MAX_RETRIES:
                    try:
                        preds = chain.batch(mini_batch, {"max_concurrency": batch_size})
                        # If no exception, add questions and answers to all_answers
                        for qna, pred in zip(mini_batch, preds):
                            responses.append({"category": qna["category"], "answer": qna["answer"], "pred": pred[0], "response": pred[1]})
                        break  # Exit the retry loop once successful
                    except RateLimitError as rate_limit_error:
                        delay = (retries + 1) * DELAY_INCREMENT
                        logger.warning(f"{rate_limit_error}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                        retries += 1

                        if retries > MAX_RETRIES:
                            logger.error(f"Max retries reached this batch. Skipping to next batch.")
                            break
                    except openai.BadRequestError as e:
                        logger.error(f"BadRequestError: {e}. Skipping this batch.")
                        logger.info(f"Question: {qna['question']}")
                        break
                    except Exception as e:
                        logger.error(f"Error in process_inputs: {e}")
                        break            
                
                pbar.set_postfix({"current_batch": f"{i//batch_size + 1}/{(len(all_batch) + (batch_size-1))//batch_size}"})
                pbar.update(len(mini_batch))

        t1 = time.time()
        acc = evaluate_each_category(responses, c)
        timespan = format_timespan(t1 - t0)
        logger.info(f"##### Category [{c}] accuracy: {acc}") 
        logger.info(f"##### Generating Answers for Category [{c}] took {timespan}")

    logger.info("====== [DONE] Completed Generating Answers to Questions given by LLM. =====")
    df = pd.DataFrame(responses)
    os.makedirs("results", exist_ok=True)
    csv_path = f"results/[{dataset_name}] {MODEL_NAME}-{MODEL_VERSION}-{FEW_SHOTS}.csv"
    logger.info(f"====== Generated CSV file - CSV_PATH: {csv_path} =====")
    df.to_csv(csv_path, index=False)

    logger.info(f"====== [START] Evaluation start - CSV_PATH: {csv_path} =====")
    evaluate(csv_path)
    logger.info(f"====== [START] Evaluation end =====")


def evaluate_each_category(responses, category):
    df = pd.DataFrame(responses)
    df = df[df["category"] == category]
    df["correct"] = df["answer"] == df["pred"]
    acc = round(df["correct"].mean()*100, 2)
    return acc


def evaluate(csv_path):

    result = pd.read_csv(csv_path)
    result["correct"] = result["answer"] == result["pred"]

    category_avg = result.groupby(['category']).agg(
        correct_mean=('correct', 'mean'),
        correct_count=('correct', 'size')
    ).reset_index()
    print(category_avg)
    overall_avg = category_avg["correct_mean"].mean()
    print(f"Overall Average: {overall_avg}")

    os.makedirs("evals", exist_ok=True)
    filename = csv_path.split("/")[-1].split(".")[0]
    category_avg.to_csv(f"evals/{filename}-eval.csv", index=False)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Options')

    parser.add_argument("--is_debug", type=str2bool, default=False)
    parser.add_argument("--num_debug_samples", type=int, default=10)
    parser.add_argument("--model_provider", type=str, default="azureopenai")
    parser.add_argument("--hf_model_id", type=str, default="microsoft/Phi-3.5-mini-instruct")
    parser.add_argument("--batch_size", type=int, default=20)
    parser.add_argument("--max_retries", type=int, default=3)
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--temperature", type=float, default=0.01)
    parser.add_argument("--template_type", type=str, default="basic")
    parser.add_argument("--is_hard", type=str2bool, default=True)
    parser.add_argument("--use_few_shots", type=str2bool, default=True)    

    args = parser.parse_args()

    valid_providers = ["azureopenai", "openai", "azureml", "huggingface"]
    assert args.model_provider in valid_providers, f"Invalid 'model_provider' value. Please choose from {valid_providers}."
    
    valid_template_types = ["basic", "chat"]
    assert args.template_type in valid_template_types, f"Invalid 'template_type' value. Please choose from {valid_template_types}."

    logger.info(args)
    benchmark(args)