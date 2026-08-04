import os
import argparse
import boto3
import time
from functools import wraps
from typing import Any, Dict, List, Optional

from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import BaseMessage
from langchain_core.callbacks import CallbackManagerForLLMRun

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.runnables import RunnableLambda
from langchain_community.llms.azureml_endpoint import AzureMLOnlineEndpoint
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from .phi3_formatter import CustomPhi3ContentFormatter
from config.prompts import get_system_prompt


def str2bool(v):
    """Convert string to boolean value."""
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def check_existing_csv_in_debug(csv_path, is_debug):
    """Check if CSV exists in debug mode and ask user whether to reuse it."""
    if not is_debug or not os.path.exists(csv_path):
        return False
    
    print(f"\n✅ 기존 결과 파일이 존재합니다. 자동으로 사용합니다: {csv_path}\n")
    return True


def format_timespan(seconds):
    """Format seconds into human-readable timespan."""
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    timespan = f"{hours} hours {minutes} minutes {remaining_seconds:.4f} seconds."
    return timespan


def get_prompt_template(template_type, model_provider=None, num_choices=5, use_math_prompt=False):
    """Get prompt template based on the template type.
    
    Args:
        template_type: Type of template ('basic' or 'chat')
        model_provider: Model provider name
        num_choices: Number of answer choices (default: 5)
        use_math_prompt: Use math-specific system prompt (default: False)
    
    Returns:
        tuple: (prompt_template, system_prompt_text or None)
    """
    
    if use_math_prompt:
        from config.prompts import get_math_system_prompt
        system_prompt_text = get_math_system_prompt()
    else:
        system_prompt_text = get_system_prompt(num_choices=num_choices)
    
    if template_type == "basic":
        prompt = PromptTemplate.from_template("{question}")
    elif template_type == "chat":
        system_message_template = SystemMessagePromptTemplate.from_template(
            f"System:\n\n{system_prompt_text}"
        )
        human_prompt = [
            {"type": "text", "text": "{question}"},
        ]
        human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

        prompt = ChatPromptTemplate.from_messages(
            [system_message_template, human_message_template]
        )
    else:
        raise ValueError(
            "Invalid 'template_type' value. Please choose from ['basic', 'chat']"
        )
    return prompt, system_prompt_text


def get_provider_name(model_provider):
    """Get human-readable provider name"""
    provider_names = {
        "azureopenai": "Azure OpenAI",
        "openai": "OpenAI",
        "bedrock": "AWS Bedrock",
        "huggingface": "Hugging Face",
        "azureml": "Azure ML endpoint",
        "azureai": "Azure AI Foundry endpoint",
        "bedrock_openai": "AWS Bedrock (OpenAI models)",
    }
    return provider_names.get(model_provider, model_provider)


def get_llm_client(
    model_provider, hf_model_id=None, temperature=0.01, max_tokens=256, max_retries=3, wait_time=None, system_prompt=None
):
    """Get LLM client"""
    
    # Use environment variable for wait_time if not provided
    if wait_time is None:
        wait_time = float(os.getenv("WAIT_TIME", "30.0"))

    if model_provider == "azureopenai":

        model_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        reasoning_effort = os.getenv("REASONING_EFFORT")
        reasoning_enabled = os.getenv("REASONING_ENABLED", "false").lower() == "true"

        # GPT-5.1 계열 모델들 (reasoning_effort 지원)
        if model_name in ["gpt-5.1", "gpt-5.1-chat", "gpt-5.1(medium)","gpt-5.2","gpt-5.2(medium)"]:
            model_kwargs = {}
            if reasoning_enabled and reasoning_effort:
                model_kwargs["reasoning_effort"] = reasoning_effort
            
            llm = AzureChatOpenAI(
                azure_deployment=model_name,
                openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                max_retries=max_retries,
                **model_kwargs,
            )
        # GPT-5 계열 모델들 (gpt-5-chat 추가)
        elif model_name in ["gpt-5-mini", "gpt-5-nano", "gpt-5-chat"]:
            llm = AzureChatOpenAI(
                azure_deployment=model_name,
                openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                max_retries=max_retries,
            )
        elif model_name in ["gpt-oss-120b", "gpt-oss-20b"]:
            llm = AzureChatOpenAI(
                azure_deployment=model_name,
                openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                max_retries=max_retries,
                temperature=temperature,
                stop=["\n"]
            )
        else:
            llm = AzureChatOpenAI(
                azure_deployment=model_name,
                openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                temperature=temperature,
                max_tokens=max_tokens,
                max_retries=max_retries,
            )
    elif model_provider == "openai":

        model_name = os.getenv("OPENAI_DEPLOYMENT_NAME")
        openai_api_base = os.getenv("OPENAI_API_BASE")
        llm_kwargs = {
            "model": model_name,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "max_retries": max_retries,
        }
        # OpenAI-compatible 커스텀 엔드포인트(예: 자체 서빙 vLLM)를 가리킬 때 사용
        if openai_api_base:
            llm_kwargs["openai_api_base"] = openai_api_base
            llm_kwargs["openai_api_key"] = os.getenv("OPENAI_API_KEY", "EMPTY")
        llm = ChatOpenAI(**llm_kwargs)
    elif model_provider == "bedrock_openai":
        # Bedrock에 올라간 OpenAI 모델(GPT-5.6 등)은 bedrock-runtime(Converse)이 아니라
        # bedrock-mantle 엔드포인트의 OpenAI Responses API로만 서빙됨.
        # 이 모델들은 reasoning 모델이라 temperature 파라미터를 지원하지 않음(400 에러).
        model_name = os.getenv("BEDROCK_OPENAI_MODEL_ID")
        region = os.getenv("AWS_REGION", "us-east-1")
        bearer_token = os.getenv("AWS_BEARER_TOKEN_BEDROCK")

        reasoning_enabled = os.getenv("REASONING_ENABLED", "false").lower() == "true"
        reasoning_effort = os.getenv("REASONING_EFFORT", "medium")

        llm = ChatOpenAI(
            model=model_name,
            openai_api_base=f"https://bedrock-mantle.{region}.api.aws/openai/v1",
            openai_api_key=bearer_token,
            use_responses_api=True,
            max_retries=max_retries,
            reasoning_effort=reasoning_effort if reasoning_enabled else None,
        )
    elif model_provider == "huggingface":
        if (
            temperature == 0.0
        ):  # in case of not supporting 0.0 for some SLM, set to 0.01
            temperature = 0.01
        model_name = hf_model_id.split("/")[-1]

        llm = HuggingFaceEndpoint(
            repo_id=hf_model_id,
            temperature=temperature,
            max_new_tokens=max_tokens,
            huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
        )
    elif model_provider == "azureml":

        model_name = os.getenv("AZURE_ML_DEPLOYMENT_NAME")

        llm = AzureMLOnlineEndpoint(
            endpoint_url=os.getenv("AZURE_ML_ENDPOINT_URL"),
            endpoint_api_type=os.getenv("AZURE_ML_ENDPOINT_TYPE"),
            endpoint_api_key=os.getenv("AZURE_ML_API_KEY"),
            content_formatter=CustomPhi3ContentFormatter(),
            model_kwargs={"temperature": temperature, "max_new_tokens": max_tokens},
        )

    elif model_provider == "azureai":

        model_name = os.getenv("AZURE_AI_DEPLOYMENT_NAME")

        llm = AzureAIChatCompletionsModel(
            endpoint=os.getenv("AZURE_AI_INFERENCE_ENDPOINT"),
            credential=os.getenv("AZURE_AI_INFERENCE_KEY"),
            model_name=model_name,
        )
    elif model_provider == "bedrock":

        model_name = os.getenv("BEDROCK_MODEL_ID")
        
        # Build additional_model_request_fields
        additional_fields = {}
        
        # Reasoning config - only for Nova models
        reasoning_enabled = os.getenv("REASONING_ENABLED", "false").lower() == "true"
        is_nova_model = "nova" in model_name.lower()
        
        if reasoning_enabled and is_nova_model:
            reasoning_effort = os.getenv("REASONING_EFFORT", "high")
            additional_fields["reasoningConfig"] = {
                "type": "enabled",
                "maxReasoningEffort": reasoning_effort
            }
        
        # Prepare system prompt
        system_messages = None
        if system_prompt:
            system_messages = [system_prompt] if isinstance(system_prompt, str) else system_prompt
        
        # When reasoning is enabled with high effort, temperature and max_tokens must be unset
        bedrock_kwargs = {
            "model": model_name,
            "region_name": os.getenv("AWS_REGION"),
            "system": system_messages,
            "additional_model_request_fields": additional_fields if additional_fields else None
        }
        
        if not (reasoning_enabled and is_nova_model and reasoning_effort == "high"):
            bedrock_kwargs["temperature"] = temperature
            bedrock_kwargs["max_tokens"] = max_tokens
        
        llm = ChatBedrockConverse(**bedrock_kwargs)
    else:
        raise ValueError(
            "Invalid 'model_provider' value. Please choose from ['azureopenai', 'openai', 'huggingface', 'azureml', 'azureai', 'bedrock', 'bedrock_openai']"
        )

    return llm, model_name
