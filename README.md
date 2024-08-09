# Korean language proficiency evaluation for LLM/SLM models using CLIcK and HAE-RAE dataset

## Overview

With the continuous emergence of various LLM/SLM models, there is a need for robust evaluation datasets for non-English languages such as Korean. CLIcK (Cultural and Linguistic Intelligence in Korean) and HAE_RAE_BENCH 1.0 fill this gap by providing a rich, well-categorized dataset that focuses on cultural and linguistic aspects, enabling detailed evaluation of Korean language models. This code performs benchmarking on two datasets with minimal time and effort.

### CLIcK (Cultural and Linguistic Intelligence in Korean)
This dataset assesses Korean language proficiency in the subject areas of Korean Culture (History, Geography, Law, Politics, Society, Tradition, Economy, Pop culture) and Korean Language (Textual, Functional, Grammar). There are a total of 1,995 sample data in 11 categories.

- [Paper](https://arxiv.org/abs/2403.06412), [GitHub](https://github.com/rladmstn1714/CLIcK), [Hugging Face](https://huggingface.co/datasets/EunsuKim/CLIcK)

### HAE_RAE_BENCH 1.0
This dataset evaluates Korean language proficiency in the following 6 categories (General Knowledge, History, Loan Words, Rare Words, Reading Comprehension, Standard Nomenclature). Similar to CLiCK, the task is to solve multiple-choice questions. There are a total of 1,538 sample data in 6 categories.

- [Paper](https://arxiv.org/abs/2309.02706), [GitHub](https://github.com/HAE-RAE/HAE-RAE-BENCH), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0)

## Implementation

The code skeleton is based on https://github.com/corca-ai/evaluating-gpt-4o-on-CLIcK, but a lot of parts have changed. 

In particular, we modified the code to run on Azure OpenAI & Hugging Face and added logic for parallel processing, content filtering (400 error), and max request error (429 error) exception handling. 

## Results

### CLIcK

| LLM             |             | GPT-4o-mini (2024-07-18) |       | GPT-4o (2024-05-13) |       | GPT-4 (turbo-2024-04-09) |       |
|-----------------|-------------|--------------------------|-------|---------------------|-------|--------------------------------|-------|
| Subject Area    | Subject     | mean                     | count | mean                | count | mean                           | count |
| Korean Culture  | History     | 0.472                    | 250   | 0.656               | 250   | 0.384                          | 250   |
|                 | Geography   | 0.778626                 | 131   | 0.816794            | 131   | 0.763359                       | 131   |
|                 | Law         | 0.552511                 | 219   | 0.675799            | 219   | 0.579909                       | 219   |
|                 | Politics    | 0.833333                 | 84    | 0.880952            | 84    | 0.880952                       | 84    |
|                 | Society     | 0.864078                 | 309   | 0.915858            | 309   | 0.841424                       | 309   |
|                 | Tradition   | 0.716216                 | 222   | 0.873874            | 222   | 0.761261                       | 222   |
|                 | Economy     | 0.830508                 | 59    | 0.949153            | 59    | 0.864407                       | 59    |
|                 | Pop culture | 0.853659                 | 41    | 0.97561             | 41    | 0.878049                       | 41    |
|                 | **Average**     | **0.738**                    |       | **0.843**               |       | **0.744**                          |       |
| Korean Language | Textual     | 0.803509                 | 285   | 0.912281            | 285   | 0.859649                       | 285   |
|                 | Functional  | 0.64                     | 125   | 0.848               | 125   | 0.728                          | 125   |
|                 | Grammar     | 0.454167                 | 240   | 0.5875              | 240   | 0.3                            | 240   |
|                 | **Average**     | **0.633**                    |       | **0.783**               |       | **0.629**                          |       |

### HAE_RAE_BENCH 1.0

GPT-4o-mini (2024-07-18)
| Category                 | Correct Mean | Correct Count |
|--------------------------|--------------|---------------|
| General Knowledge        | 0.556818     | 176           |
| History                  | 0.856383     | 188           |
| Loan Words               | 0.775148     | 169           |
| Rare Words               | 0.819753     | 405           |
| Reading Comprehension    | 0.771812     | 447           |
| Standard Nomenclature    | 0.764706     | 153           |

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