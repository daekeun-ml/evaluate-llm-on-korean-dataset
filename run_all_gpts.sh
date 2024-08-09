#!/bin/bash

# Copy specific environment file to .env
cp .env_gpt-4 .env

# Run the korean evaluations
python3 click_main.py
python3 haerae_main.py

# gpt-4o
cp .env_gpt-4o .env

python3 click_main.py
python3 haerae_main.py

# gpt-4o-mini
cp .env_gpt-4o-mini .env

python3 click_main.py
python3 haerae_main.py
