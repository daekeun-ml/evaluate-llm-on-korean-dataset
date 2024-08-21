# Korean language proficiency evaluation for LLM/SLM models using CLIcK and HAE-RAE dataset

## Overview

With the continuous emergence of various LLM/SLM models, there is a need for robust evaluation datasets for non-English languages such as Korean. CLIcK (Cultural and Linguistic Intelligence in Korean) and HAE_RAE_BENCH 1.0 fill this gap by providing a rich, well-categorized dataset that focuses on cultural and linguistic aspects, enabling detailed evaluation of Korean language models. This code performs benchmarking on two datasets with minimal time and effort.

### CLIcK (Cultural and Linguistic Intelligence in Korean)
This dataset assesses Korean language proficiency in the subject areas of Korean Culture (History, Geography, Law, Politics, Society, Tradition, Economy, Pop culture) and Korean Language (Textual, Functional, Grammar). There are a total of 1,995 sample data in 11 categories. This dataset presents 4- or 5-choice multiple choice questions. Depending on the question, additional context is given.

- [Paper](https://arxiv.org/abs/2403.06412), [GitHub](https://github.com/rladmstn1714/CLIcK), [Hugging Face](https://huggingface.co/datasets/EunsuKim/CLIcK)

### HAE_RAE_BENCH 1.0
This dataset evaluates Korean language proficiency in the following 6 categories (General Knowledge, History, Loan Words, Rare Words, Reading Comprehension, Standard Nomenclature). Similar to CLiCK, the task is to solve multiple-choice questions, but no additional context. There are a total of 1,538 sample data in 6 categories.

- [Paper](https://arxiv.org/abs/2309.02706), [GitHub](https://github.com/HAE-RAE/HAE-RAE-BENCH), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0)

## Implementation

The code skeleton is based on https://github.com/corca-ai/evaluating-gpt-4o-on-CLIcK, but a lot of parts have changed. 

In particular, we modified the code to run on Azure OpenAI & Hugging Face and added logic for parallel processing, content filtering (400 error), and max request error (429 error) exception handling. 

## Results

### CLIcK

|               |                  |              |                  |                    |               |unit: correct_mean   |               |
|---------------------|------------------------|--------------------|------------------------|--------------------------|---------------------|---------------------|---------------------|
|category_big         |category                |GPT-4o-mini (2024-07-18)|GPT-4o  (2024-05-13)    |GPT-4 (turbo-2024-04-09)  |GPT-3.5-turbo (2023-06-13)|Llama-3.1-8B-Instruct|Phi-3-5-mini-instruct|
|Culture              |Economy                 |0.81                |0.95                    |0.90                      |0.64                 |0.42                 |0.61                 |
|Culture              |Geography               |0.78                |0.82                    |0.82                      |0.53                 |0.34                 |0.46                 |
|Culture              |History                 |0.48                |0.68                    |0.46                      |0.33                 |0.23                 |0.26                 |
|Culture              |Law                     |0.58                |0.71                    |0.61                      |0.42                 |0.32                 |0.32                 |
|Culture              |Politics                |0.83                |0.89                    |0.89                      |0.65                 |0.39                 |0.55                 |
|Culture              |Pop Culure              |0.85                |0.98                    |0.93                      |0.73                 |0.39                 |0.61                 |
|Culture              |Society                 |0.86                |0.92                    |0.87                      |0.72                 |0.44                 |0.54                 |
|Culture              |Tradition               |0.73                |0.88                    |0.79                      |0.56                 |0.37                 |0.48                 |
|Language             |Functional              |0.65                |0.84                    |0.80                      |0.39                 |0.13                 |0.38                 |
|Language             |Grammar                 |0.43                |0.57                    |0.48                      |0.30                 |0.22                 |0.28                 |
|Language             |Textual                 |0.81                |0.91                    |0.87                      |0.62                 |0.22                 |0.55                 |
|category_big average:|                        |                    |                        |                          |                     |                     |                     |
|Culture              |                        |**0.71**                |**0.82**                    |**0.74**                      |**0.54**                 |**0.35**                 |**0.44**                 |
|Language             |                        |**0.64**                |**0.77**                    |**0.71**                      |**0.46**                 |**0.20**                 |**0.41**                 |


### HAE_RAE_BENCH 1.0

|               |                  |              |                  |                    |unit: correct_mean   |               |
|---------------------|------------------------|--------------------|------------------------|--------------------------|---------------------|---------------------|
|category             |GPT-4o-mini<br>(2024-07-18)|GPT-4o<br>(2024-05-13)|GPT-4<br>(turbo-2024-04-09)|GPT-3.5-turbo<br>(2023-06-13)|Llama-3.1<br>8B-Instruct|Phi-3-5<br>mini-instruct|
|General Knowledge    |0.53                    |0.77                |0.66                    |0.41                      |0.18                 |0.31                 |
|History              |0.85                    |0.92                |0.79                    |0.30                      |0.15                 |0.32                 |
|Loan Words           |0.76                    |0.80                |0.78                    |0.59                      |0.21                 |0.48                 |
|Rare Words           |0.82                    |0.88                |0.79                    |0.60                      |0.20                 |0.55                 |
|Reading Comprehension|0.77                    |0.85                |0.80                    |0.56                      |0.23                 |0.43                 |
|Standard Nomenclature|0.76                    |0.89                |0.79                    |0.54                      |0.19                 |0.44                 |
|overall average:     |                        |                    |                        |                          |                     |                     |
|                     |**0.75**                    |**0.85**                |**0.77**                    |**0.50**                      |**0.19**                 |**0.42**                 |



## Quick Start

### GitHub Codespace
Please start a new project by connecting to Codespace Project. The environment required for hands-on is automatically configured through devcontainer, so you only need to run a Jupyter notebook.

### Your Local PC
Please start by installing the required packages on your local PC with

```bash
pip install -r requirements.txt
```

Please do not forget to modify the .env file to match your account. Rename `.env.sample` to `.env` or copy and use it

### Modify your .env

#### Azure OpenAI
```ini
AZURE_OPENAI_ENDPOINT=<YOUR_OPEN_ENDPOINT>
AZURE_OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
AZURE_OPENAI_API_VERSION=<YOUR_OPENAI_API_VERSION>
AZURE_OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME> (e.g., gpt-4o-mini)>
OPENAI_MODEL_VERSION=<YOUR_OPENAI_MODEL_VERSION> (e.g., 2024-07-18)>
```

### OpenAI
```ini
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
OPENAI_DEPLOYMENT_NAME=<YOUR_OPENAI_API_VERSION>
OPENAI_MODEL_VERSION=<YOUR_OPENAI_MODEL_VERSION> (e.g., 2024-07-18)>
```

### Hugging Face
```ini
HF_API_TOKEN=<YOUR_HF_API_TOKEN>
```

Execute the command to perform the evaluation. (The evaluation results are saved in the `./results` folder and `./evals`.)
   
```bash
python click_main.py

python haerae_main.py

```

### Tunable parameters
```python
parser.add_argument("--is_debug", type=bool, default=True)
parser.add_argument("--num_debug_samples", type=int, default=20)
parser.add_argument("--model_provider", type=str, default="azureopenai")
parser.add_argument("--hf_model_id", type=str, default="mistralai/Mistral-7B-Instruct-v0.2")
parser.add_argument("--batch_size", type=int, default=10)
parser.add_argument("--max_retries", type=int, default=3)
parser.add_argument("--max_tokens", type=int, default=256)
parser.add_argument("--temperature", type=float, default=0.01)
```

azure-gpt-4o-mini Benchmark results (temperature=0.0)
```bash
   category_big     category   correct
0       Culture      Economy  0.830508
1       Culture    Geography  0.778626
2       Culture      History  0.484000
3       Culture          Law  0.575342
4       Culture     Politics  0.833333
5       Culture  Pop Culture  0.853659
6       Culture      Society  0.857605
7       Culture    Tradition  0.743243
8      Language   Functional  0.648000
9      Language      Grammar  0.425000
10     Language      Textual  0.807018
```


## References

```bibtex
@misc{kim2024click,
      title={CLIcK: A Benchmark Dataset of Cultural and Linguistic Intelligence in Korean}, 
      author={Eunsu Kim and Juyoung Suk and Philhoon Oh and Haneul Yoo and James Thorne and Alice Oh},
      year={2024},
      eprint={2403.06412},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@misc{son2024haeraebenchevaluationkorean,
      title={HAE-RAE Bench: Evaluation of Korean Knowledge in Language Models}, 
      author={Guijin Son and Hanwool Lee and Suwan Kim and Huiseo Kim and Jaecheol Lee and Je Won Yeom and Jihyu Jung and Jung Woo Kim and Songseong Kim},
      year={2024},
      eprint={2309.02706},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2309.02706}, 
}
```