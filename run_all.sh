#!/bin/bash


env_files=(.env_*) 

echo "Found the following .env files:"
for env_file in "${env_files[@]}"; do
    echo "$env_file"
done

for env_file in "${env_files[@]}"; do
    echo "Using environment file: $env_file"
    cp "$env_file" .env

    python3 click_main.py \
        --model_provider azureml \
        --batch_size 20 \
        --max_tokens 512 \
        --temperature 0.01 \
        --template_type basic

    python3 haerae_main.py \
        --model_provider azureml \
        --batch_size 20 \
        --max_tokens 512 \
        --temperature 0.01 \
        --template_type basic
done