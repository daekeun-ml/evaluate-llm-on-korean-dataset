#!/bin/bash

### To run experiments on multiple models at once, create multiple env files as follows:
# .env_gpt4
# .env_gpt4o
# .env_gpt4o-mini
# .env_gpt35
# .env_phi35-mini
# .env_phi35-moe
# .env_llama31-8b

env_files=(.env_*) 
is_debug=True
batch_size=20
max_tokens=512
temperature=0.01

echo "Found the following .env files:"
for env_file in "${env_files[@]}"; do
    echo "$env_file"
done

for env_file in "${env_files[@]}"; do
    if [[ "$env_file" == .env_gpt* ]]; then
        model_provider="azureopenai"
    else
        model_provider="azureml"
    fi

    echo "Using environment file: $env_file with model_provider: $model_provider"
    cp "$env_file" .env

    ### CLIcK
    python click_main.py \
        --is_debug "$is_debug" \
        --model_provider "$model_provider" \
        --batch_size "$batch_size" \
        --max_tokens "$max_tokens" \
        --temperature "$temperature" \
        --template_type basic \

    ### HAERAE 1.0
    python haerae_main.py \
        --is_debug "$is_debug" \
        --model_provider "$model_provider" \
        --batch_size "$batch_size" \
        --max_tokens "$max_tokens" \
        --temperature "$temperature" \
        --template_type basic

    ### KMMLU
    # python kmmlu_main.py \
    #     --is_debug "$is_debug" \
    #     --model_provider "$model_provider" \
    #     --batch_size "$batch_size" \
    #     --max_tokens "$max_tokens" \
    #     --temperature "$temperature" \
    #     --template_type basic \
    #     --is_hard False

    # ### KMMLU-HARD
    # python kmmlu_main.py \
    #     --is_debug "$is_debug" \
    #     --model_provider "$model_provider" \
    #     --batch_size "$batch_size" \
    #     --max_tokens "$max_tokens" \
    #     --temperature "$temperature" \
    #     --template_type basic \
    #     --is_hard True    
done