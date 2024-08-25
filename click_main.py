import os
import json
import time
import argparse

import openai
from openai import RateLimitError
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from datasets import load_dataset

from prompts import TYPE_1, TYPE_2, TYPE_3, TYPE_4
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_community.llms.azureml_endpoint import AzureMLOnlineEndpoint
from util.phi3_formatter import CustomPhi3ContentFormatter

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
        elif response.startswith("E"):
            pred = "E"
        else:
            pred = ""  # Wrong answer

        return pred, response

def get_prompt(x) -> str:
    num_choices = len(x["choices"])
    if num_choices == 4:
        if x["paragraph"] != "":  # Use Type 1 Prompt
            return TYPE_1.format(
                CONTEXT=x["paragraph"],
                QUESTION=x["question"],
                A=x["choices"][0],
                B=x["choices"][1],
                C=x["choices"][2],
                D=x["choices"][3],
            )
        else:
            return TYPE_2.format(
                QUESTION=x["question"],
                A=x["choices"][0],
                B=x["choices"][1],
                C=x["choices"][2],
                D=x["choices"][3],
            )
    elif num_choices == 5:
        if x["paragraph"] != "":
            return TYPE_3.format(
                CONTEXT=x["paragraph"],
                QUESTION=x["question"],
                A=x["choices"][0],
                B=x["choices"][1],
                C=x["choices"][2],
                D=x["choices"][3],
                E=x["choices"][4],
            )
        else:
            return TYPE_4.format(
                QUESTION=x["question"],
                A=x["choices"][0],
                B=x["choices"][1],
                C=x["choices"][2],
                D=x["choices"][3],
                E=x["choices"][4],
            )
    else:
        raise ValueError(f"Invalid number of choices: {num_choices} (ID: {x['id']})")


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


def get_answer(x) -> str:
    answer_idx = [xx.strip() for xx in x["choices"]].index(x["answer"].strip())
    if answer_idx == -1:
        raise ValueError(f"Answer not found in choices: {x['answer']} (ID: {x['id']})")
    return chr(0x41 + answer_idx)  # answer_idx = 0 -> answer = "A"


def benchmark(args):

    IS_DEBUG = args.is_debug
    MAX_RETRIES = args.max_retries
    DELAY_INCREMENT = 30
    MODEL_VERSION = None

    num_debug_samples = args.num_debug_samples
    batch_size = args.batch_size
    max_tokens = args.max_tokens
    temperature = args.temperature

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
        AZURE_ML_ENDPOINT_TYPE = os.getenv("AZURE_ML_ENDPOINT_TYPE") # "serverless" or "dedicated"
        AZURE_ML_API_KEY = os.getenv("AZURE_ML_API_KEY")
        
        llm = AzureMLOnlineEndpoint(
            endpoint_url=AZURE_ML_ENDPOINT_URL,
            endpoint_api_type=AZURE_ML_ENDPOINT_TYPE,
            endpoint_api_key=AZURE_ML_API_KEY,
            content_formatter=CustomPhi3ContentFormatter(),
            model_kwargs={"temperature": temperature, "max_new_tokens": max_tokens}              
        )

    click_ds = load_dataset("EunsuKim/CLIcK")["train"]

    if IS_DEBUG:
        click_ds = click_ds.select(range(num_debug_samples))

    all_batch = [{"id": x["id"], "question": get_prompt(x), "answer": get_answer(x)} for x in tqdm(click_ds)]
    responses = []
    prompt_template = get_prompt_template(args.template_type)
    chain = prompt_template | llm | CustomStrOutputParser()

    logger.info(f"====== [START] Generate answers to questions given by LLM. =====")
    logger.info(f"====== deployment name: {MODEL_NAME}, model version: {MODEL_VERSION} =====")
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
                        responses.append({"id": qna["id"], "trial": 0, "answer": qna["answer"], "pred": pred[0], "response": pred[1]})
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
    timespan = format_timespan(t1 - t0)
    logger.info(f"===== [DONE] Generating Answer dataset took {timespan}")

    df = pd.DataFrame(responses)
    os.makedirs("results", exist_ok=True)
    csv_path = f"results/[CLIcK] {MODEL_NAME}-{MODEL_VERSION}.csv"
    logger.info(f"====== Generated CSV file - CSV_PATH: {csv_path} =====")
    df.to_csv(csv_path, index=False)

    logger.info(f"====== [START] Evaluation start - CSV_PATH: {csv_path} =====")
    evaluate(csv_path)
    logger.info(f"====== [START] Evaluation end =====")


def evaluate(csv_path):
    result = pd.read_csv(csv_path)
    with open('id_to_category.json', 'r') as json_file:
        id_to_category = json.load(json_file)

    result["category"] = result["id"].map(id_to_category)
    result["correct"] = result["answer"] == result["pred"]
    result['category_big'] = result['category'].apply(
        lambda x: 'Culture' if x in ['Economy', 'Geography', 'History', 'Law', 'Politics', 'Popular', 'Society', 'Tradition', 'Pop Culture'] else 
                ('Language' if x in ['Functional', 'Textual', 'Grammar'] else 'Other')
    )

    category_avg = result.groupby(['category_big', 'category']).agg(
        correct_mean=('correct', 'mean'),
        correct_count=('correct', 'size')
    ).reset_index()
    print(category_avg)

    category_big_avg = result.groupby('category_big').agg(
        correct_mean=('correct', 'mean'),
        correct_count=('correct', 'size')
    ).reset_index()
    print(category_big_avg)

    os.makedirs("evals", exist_ok=True)
    filename = csv_path.split("/")[-1].split(".")[0]
    category_avg.to_csv(f"evals/{filename}-eval.csv", index=False)
    category_big_avg.to_csv(f"evals/{filename}-eval-avg.csv", index=False)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Options')

    parser.add_argument("--is_debug", type=bool, default=True)
    parser.add_argument("--num_debug_samples", type=int, default=20)
    parser.add_argument("--model_provider", type=str, default="azureopenai")
    parser.add_argument("--hf_model_id", type=str, default="microsoft/Phi-3.5-MoE-instruct")
    parser.add_argument("--batch_size", type=int, default=10)
    parser.add_argument("--max_retries", type=int, default=3)
    parser.add_argument("--max_tokens", type=int, default=256)
    parser.add_argument("--temperature", type=float, default=0.01)
    parser.add_argument("--template_type", type=str, default="basic")   

    args = parser.parse_args()
    valid_providers = ["azureopenai", "openai", "azureml", "huggingface"]
    assert args.model_provider in valid_providers, f"Invalid 'model_provider' value. Please choose from {valid_providers}."
    
    valid_template_types = ["basic", "chat"]
    assert args.template_type in valid_template_types, f"Invalid 'template_type' value. Please choose from {valid_template_types}."

    logger.info(args)
    benchmark(args)