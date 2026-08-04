# Configuration

Full reference for `.env` provider configuration. See [README.md](README.md#-quick-start) for the
general setup flow — this file covers per-provider options in detail.

## Multiple Models Setup
For testing multiple models simultaneously, create separate configuration files in the `env/` folder:

```bash
mkdir env
cp .env.sample env/.env.gpt4
cp .env.sample env/.env.claude
cp .env.sample env/.env.nova
```

Each file should have different model configurations:

**env/.env.gpt4:**
```ini
MODEL_NAME=gpt-4o
MODEL_VERSION=2024-05-13
AZURE_OPENAI_ENDPOINT=<YOUR_ENDPOINT>
AZURE_OPENAI_API_KEY=<YOUR_API_KEY>
```

**env/.env.claude:**
```ini
MODEL_NAME=claude-4-5
MODEL_VERSION=2025-12-05
BEDROCK_MODEL_ID=anthropic.claude-3-5-sonnet-20241022-v2:0
AWS_REGION=us-west-2
```

**env/.env.nova:**
```ini
MODEL_NAME=nova-2-lite
MODEL_VERSION=2025-12-05
BEDROCK_MODEL_ID=us.amazon.nova-2-lite-v1:0
AWS_REGION=us-west-2
```

The `./run.sh` script will automatically detect all `.env` files in the `env/` folder and run evaluations in parallel.

## Configuration Options

```ini
# Basic info
MODEL_NAME=<YOUR_MODEL_NAME>
MODEL_VERSION=<YOUR_MODEL_VERSION>

# Reasoning Configuration (applies to all providers)
REASONING_ENABLED=true  # Enable reasoning mode for system prompts
REASONING_EFFORT=medium  # none, minimal, low, medium, high

# Wait time between requests (seconds) - helps avoid throttling
WAIT_TIME=30  # Default: 30 seconds, only used when throttling errors occur
```

## Azure OpenAI
```ini
AZURE_OPENAI_ENDPOINT=<YOUR_ENDPOINT>
AZURE_OPENAI_API_KEY=<YOUR_API_KEY>
AZURE_OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
AZURE_OPENAI_API_VERSION=2025-04-01-preview
```

## Azure AI Foundry
```ini
AZURE_AI_INFERENCE_KEY=<YOUR_API_KEY>
AZURE_AI_INFERENCE_ENDPOINT=<YOUR_ENDPOINT>
AZURE_AI_DEPLOYMENT_NAME=Phi-4
```

## Amazon Bedrock
```ini
BEDROCK_MODEL_ID=us.amazon.nova-2-lite-v1:0
AWS_REGION=us-west-2
```

Claude Sonnet 5 / Opus 5 only support the newer adaptive-thinking API
(`thinking.type=adaptive` + `output_config.effort`), not the older
`thinking.type=enabled` + `budget_tokens` scheme used by Claude 4.x. This is
handled automatically when `REASONING_ENABLED=true` and `BEDROCK_MODEL_ID`
contains `sonnet-5` or `opus-5`:
```ini
MODEL_PROVIDER=bedrock
BEDROCK_MODEL_ID=global.anthropic.claude-opus-5  # or global.anthropic.claude-sonnet-5
AWS_REGION=us-east-1
REASONING_ENABLED=true
REASONING_EFFORT=medium
```

## Amazon Bedrock (OpenAI models, e.g. GPT-5.6)
OpenAI models on Bedrock (GPT-5.6 Sol/Terra/Luna, etc.) are served only through the
`bedrock-mantle` endpoint's Responses API, not the regular `bedrock-runtime` Converse API.
Use `MODEL_PROVIDER=bedrock_openai` for these models:
```ini
MODEL_PROVIDER=bedrock_openai
BEDROCK_OPENAI_MODEL_ID=openai.gpt-5.6-sol  # or openai.gpt-5.6-terra, openai.gpt-5.6-luna
AWS_REGION=us-east-1
# AWS_BEARER_TOKEN_BEDROCK must be set in the shell environment (not the .env file)
```

## OpenAI
```ini
OPENAI_API_KEY=<YOUR_API_KEY>
OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
```

## OpenAI-compatible self-hosted endpoint (e.g. vLLM)
To evaluate a self-hosted, OpenAI-compatible server (such as a vLLM deployment), set
`OPENAI_API_BASE` under the `openai` provider:
```ini
MODEL_PROVIDER=openai
OPENAI_DEPLOYMENT_NAME=deepseek-v4-flash
OPENAI_API_BASE=http://localhost:8000/v1
OPENAI_API_KEY=EMPTY
```

To enable thinking mode on a self-hosted reasoning model (e.g. DeepSeek-V4-Flash-0731, which
only supports `reasoning_effort` values `low`/`high`/`max` — no `medium`), set
`REASONING_ENABLED=true`; this is forwarded to vLLM as `chat_template_kwargs`:
```ini
MODEL_PROVIDER=openai
OPENAI_DEPLOYMENT_NAME=deepseek-v4-flash
OPENAI_API_BASE=http://localhost:8000/v1
OPENAI_API_KEY=EMPTY
REASONING_ENABLED=true
REASONING_EFFORT=high
```

## Azure ML
```ini
AZURE_ML_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
AZURE_ML_ENDPOINT_URL=<YOUR_ENDPOINT_URL>
AZURE_ML_ENDPOINT_TYPE=<dedicated or serverless>
AZURE_ML_API_KEY=<YOUR_API_KEY>
```

## Hugging Face
```ini
HF_API_TOKEN=<YOUR_HF_API_TOKEN>
```

