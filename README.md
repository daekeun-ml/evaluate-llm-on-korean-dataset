# Korean language proficiency evaluation for LLM/SLM models using KMMLU, CLIcK, HAE-RAE, HRM8K, KoBALT, and KorMedMCQA dataset

## 📋 Overview

With the continuous emergence of various LLM/SLM models, there is a need for robust evaluation datasets for non-English languages such as Korean. KMMLU (Korean Massive Multi-task Language Understanding), CLIcK (Cultural and Linguistic Intelligence in Korean), HAE_RAE_BENCH 1.0, HRM8K, KoBALT, and KorMedMCQA fill this gap by providing rich, well-categorized datasets that focus on cultural, linguistic, mathematical reasoning, advanced linguistic phenomena, and medical knowledge, enabling detailed evaluation of Korean language models. This code performs benchmarking on these datasets with minimal time and effort.

### CLIcK (Cultural and Linguistic Intelligence in Korean)
This dataset assesses Korean language proficiency in the subject areas of Korean Culture (History, Geography, Law, Politics, Society, Tradition, Economy, Pop culture) and Korean Language (Textual, Functional, Grammar). There are a total of 1,995 sample data in 11 categories. This dataset presents 4- or 5-choice multiple choice questions. Depending on the question, additional context is given.

- [Paper](https://arxiv.org/abs/2403.06412), [GitHub](https://github.com/rladmstn1714/CLIcK), [Hugging Face](https://huggingface.co/datasets/EunsuKim/CLIcK)

### HAE_RAE_BENCH 1.0
This dataset evaluates Korean language proficiency in the following 6 categories (General Knowledge, History, Loan Words, Rare Words, Reading Comprehension, Standard Nomenclature). Similar to CLiCK, the task is to solve multiple-choice questions, but no additional context. There are a total of 1,538 sample data in 6 categories.

- [Paper](https://arxiv.org/abs/2309.02706), [GitHub](https://github.com/HAE-RAE/HAE-RAE-BENCH), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0)

### KMMLU
The KMMLU dataset is a large-scale multi-task language understanding evaluation dataset in Korean. It is not a simple translation of the MMLU dataset, but rather data generated from Korean text, allowing us to evaluate how well LLM/SLM works in Korean. It consists of a total of 45 categories and 4 super categories, such as STEM, Appliced ​​Science, HUMSS, and Other.

- [Paper](https://arxiv.org/abs/2402.11548), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KMMLU)

### KMMLU-HARD
This dataset is an extended version of the KMMLU dataset, with more challenging questions. It is designed to further evaluate the limits of Korean NLP models and contains questions that require a particularly high level of comprehension and reasoning skills.

- [Paper](https://arxiv.org/abs/2402.11548), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KMMLU-HARD)

### HRM8K
HRM8K (HAE-RAE Math 8K) is a bilingual math reasoning benchmark for Korean and English, comprising 8,011 instances. It includes Korean School Math (KSM) with 1,428 challenging problems from Korean Olympiad and competition-level exams, and Prior Sets with 6,583 problems from existing English benchmarks (GSM8K, MATH, Omni-MATH, MMMLU). This dataset evaluates mathematical reasoning capabilities in both languages.

- [Paper](https://arxiv.org/abs/2501.02448), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HRM8K)

### KoBALT-700
KoBALT (Korean Benchmark for Advanced Linguistic Tasks) is designed to evaluate LLMs on Korean linguistic phenomena. It consists of 700 expert-written multiple-choice questions (A-J, 10 choices) covering 24 fine-grained linguistic phenomena across 5 core domains: Syntax (300), Semantics (215), Pragmatics (81), Phonetics/Phonology (62), and Morphology (42). Questions are categorized into 3 difficulty levels (1: easy, 2: moderate, 3: hard).

- [Paper](https://arxiv.org/abs/2505.16125), [GitHub](https://github.com/snunlp/KoBALT), [Hugging Face](https://huggingface.co/datasets/snunlp/KoBALT-700)

### KorMedMCQA
KorMedMCQA is a Korean Medical Multiple-Choice Question Answering benchmark derived from professional healthcare licensing examinations conducted in Korea between 2012 and 2024. The dataset contains 7,469 questions from examinations for doctor (2,489 questions), nurse (1,751 questions), pharmacist (1,817 questions), and dentist (1,412 questions), covering a wide range of medical disciplines. This dataset presents 5-choice multiple choice questions with answers numbered 1-5.

- [Paper](https://arxiv.org/abs/2403.01469), [Hugging Face](https://huggingface.co/datasets/sean0042/KorMedMCQA)

## 🆕 What's New

- Aug 4, 2026: Added **GPT-5.6 (Sol/Terra/Luna)**, **Claude Sonnet 5**, **Claude Opus 5** (all Amazon Bedrock, reasoning_effort=medium) and **DeepSeek-V4-Flash** (self-hosted via vLLM, tested at both reasoning=none and reasoning=high) benchmark results on CLIcK, HAE-RAE, KoBALT-700, and KMMLU-HARD. **Claude Opus 5** leads on CLIcK (95.84%), HAE-RAE (95.84%), and KMMLU-HARD (87.79%); **GPT-5.6 Sol** leads on KoBALT-700 (84.29%). DeepSeek-V4-Flash improves substantially with reasoning enabled (e.g. KoBALT-700: 48.86% → 50.43%, KMMLU-HARD: 56.92% → 67.91%) but still trails the frontier reasoning models. Older per-model results (GPT-5.2, GPT-5.1, Nova 2, GPT-4.1, Phi, Llama, etc.) have moved to [PREVIOUS_RESULTS.md](PREVIOUS_RESULTS.md).

- Dec 26, 2025: Added **Radar Chart Visualization** for Korean LLM evaluation results with interactive charts showing performance by category/supercategory.

- Dec 15, 2025: Added **GPT-5.2** GPT-5.2 (medium) achieved the highest KMMLU-Hard score with 74.63% accuracy (0-shot).

- Dec 6, 2025: Added **HRM8K, KoBALT, and KorMedMCQA** benchmark datasets. Added **AWS Nova 2.0 Lite** (launched at re:Invent 2025) KMMLU benchmark results. Notably, Nova 2.0 Lite, despite being a lightweight model, outperforms GPT-4.1 on KMMLU with 67.02% accuracy (0-shot) compared to GPT-4.1's 65.49%.

- Nov 21, 2025: Added **GPT-5.1, GPT-5.1-chat** benchmark results. GPT-5.1 now supports reasoning_effort="none", while other 5.x models introduce a new "minimal" setting, transforming GPT-5.1 into a flexible spectrum rather than a single fixed-intelligence model. In our benchmark, GPT-5.1 (medium) achieved the highest KMMLU score with 83.65% accuracy (0-shot), whereas GPT-5.1 with the default none setting recorded a score that was approximately 20 percentage points lower, at 62.14% (0-shot).

- Aug 11, 2025: Added **GPT-5** family benchmark results. What is very impressive is the KMMLU score (0-shot 78.53% accuracy) and KMMLU-Hard score of GPT-5-mini (0-shot 61.68% accuracy). For KMMLU-Hard, many open-source models struggle to even surpass 30% accuracy.

- Apr 17, 2025: Added **GPT-4.1** family benchmark results. GPT-4.1-mini is an improvement over GPT-4o-mini and is closer to GPT-4o. GPT-4.1 outperforms GPT-4o.

- Feb 28, 2025: Added **Phi-4-mini-instruct** benchmark results.

- Feb 2, 2025: Added **Phi-4** benchmark results / Added Azure AI Foundry deployment options. Phi-4 outperforms Phi-3.5-MoE in some metrics, such as CLIcK and KMMLU.

- Aug 29, 2024: Added 5-shot experiments for **KMMLU** and **KMMLU-HARD** benchmark datasets. For Llama-3.1-8B-Instruct, adding an example with 5-shot does not give a proper answer based on Korean language. The results may vary depending on the experimental environment, but it seems that an appropriate system prompt is needed. (Please note that we did not use any system prompt.)

- Aug 25, 2024: Added experimental results for **KMMLU** and **KMMLU-HARD** benchmark datasets. Added **Phi-3-mini-128K-instruct (June version)** benchmark results.

- Aug 22, 2024: Added **Phi-3-5-mini-instruct** and **Phi-3.5-MoE-instruct** benchmark results. Phi-3.5 is Microsoft's latest open source model that has begun to properly support multiple languages, and its Korean performance has been greatly improved, as shown in the benchmark results below.

- Aug 22, 2024: Added **Llama-3-1-8B-instruct** benchmark results. Of course, fine-tuned Llama-3.1 with Korean dataset may perform better, but we only compared it with the vanilla model.

- Aug 9, 2024: Added Azure OpenAI **GPT-3.5-turbo (2023-06-13)**, **GPT-4-turbo (2024-04-09)**, **GPT-4o (2024-05-13)**, and **GPT-4o-mini (2024-07-18)** benchmark results.

## ⚙️ Implementation

The code skeleton is based on https://github.com/corca-ai/evaluating-gpt-4o-on-CLIcK, but significant improvements have been made:

- **Multi-provider support**: Azure OpenAI, AWS Bedrock, OpenAI, Azure ML, Azure AI Foundry, and Hugging Face
- **Parallel processing**: Efficient batch processing with configurable concurrency and chunk-based file merging
- **Robust error handling**: Content filtering, rate limiting, and throttling exception handling with configurable wait times
- **Advanced parsing**: Custom output parsers supporting reasoning models with multiple response format detection
- **Adaptive prompts**: Reasoning-aware system prompts with configurable effort levels (none/minimal/low/medium/high)
- **Comprehensive logging**: Debug mode with detailed request/response logging for troubleshooting 

## 📊 Visualization

### Radar Chart Generator

```bash
# Creating a radar chart
uv run python -c "
from utils.radar_chart_generator import RadarChartGenerator
generator = RadarChartGenerator()
generator.generate_all_charts(['CLIcK', 'KMMLU', 'HAERAE'], top_n=10)
"

# Or use a juputer notebook
jupyter notebook radar_chart_visualization.ipynb
```

### Radar Charts

Charts below compare the current model round: GPT-5.6 (Sol/Terra/Luna), Claude Sonnet 5, Claude Opus 5, and DeepSeek-V4-Flash (reasoning=high).

| CLIcK Performance by Category | HAERAE Performance by Category |
|:---:|:---:|
| <img src="./charts/CLIcK_radar_chart.png" width="650"> | <img src="./charts/HAERAE_radar_chart.png" width="650">  |

| KoBALT-700 Performance by Difficulty | KMMLU-Hard Performance by Supercategory |
|:---:|:---:|
| <img src="./charts/KoBALT_radar_chart.png" width="650"> | <img src="./charts/KMMLU-HARD_radar_chart.png" width="650"> |

## 📈 Results

### Notes
The numbers in the table below are the average accuracy (%). For Azure OpenAI models, a few questions are filtered out due to the content filtering feature, but this only happens between 1-5 samples in the entire dataset, so the impact is not significant. 

The prompt is the same as the CLIcK paper prompt. The experimental results may vary depending on the system prompt, context, and parameters. The experimental results below were given with max_tokens=512, temperature=0.01 without using few-shot, context, or system prompt.

**Important for HRM8K (especially OMNI_MATH subset):**
- OMNI_MATH problems are extremely complex and require significantly more tokens
- Recommended settings: `--max_tokens 5000` or higher
- For reasoning models (e.g., Nova with reasoning), consider using lower reasoning effort to reduce token consumption
- If you encounter `stopReason: 'max_tokens'`, increase the token limit further

**Reasoning Configuration:**
- `REASONING_ENABLED=true` enables reasoning mode for system prompts across all providers
- `REASONING_EFFORT` levels: none (minimal reasoning), minimal (1-2 sentences), low (2-3 sentences), medium (3-4 sentences), high (4-6 sentences)
- For Bedrock Nova models, reasoning config is also applied to the model's native reasoning capability
- For other providers, reasoning is handled through enhanced system prompts

**Throttling Protection:**
- `WAIT_TIME` environment variable controls delay when throttling errors occur (default: 30 seconds)
- Only activates on `ThrottlingException`, `Too many requests`, or similar throttling errors
- Normal processing continues without delays

Since most of them are ChatCompletion or instruction fine-tuned models, the variation may be large compared to the results of other group's experiments. However, our experimental results show that the trend follows similarly under the same experimental conditions. (e.g., GPT-4o: 70.57/GPT-4o-mini: 60.31 in Experimental Condition 1; GPT-4o: 67.76/GPT-4o-mini: 57.53 in Experimental Condition 2).

### Model Version
<details>
<summary>Click to view model versions</summary>

- Claude Opus 5 (reasoning=medium): global.anthropic.claude-opus-5 on Amazon Bedrock, 2026-08-04 model version (thinking.type=adaptive, output_config.effort="medium")
- Claude Sonnet 5 (reasoning=medium): global.anthropic.claude-sonnet-5 on Amazon Bedrock, 2026-08-04 model version (thinking.type=adaptive, output_config.effort="medium")
- GPT-5.6 Sol (reasoning=medium): openai.gpt-5.6-sol on Amazon Bedrock, 2026-07-13 model version (reasoning_effort="medium")
- GPT-5.6 Terra (reasoning=medium): openai.gpt-5.6-terra on Amazon Bedrock, 2026-07-13 model version (reasoning_effort="medium")
- GPT-5.6 Luna (reasoning=medium): openai.gpt-5.6-luna on Amazon Bedrock, 2026-07-13 model version (reasoning_effort="medium")
- DeepSeek-V4-Flash (reasoning=high): DeepSeek-V4-Flash-0731, self-hosted via vLLM (chat_template_kwargs thinking=True, reasoning_effort="high" — the model only supports low/high/max, no "medium")
- DeepSeek-V4-Flash (reasoning=none): DeepSeek-V4-Flash-0731, self-hosted via vLLM (non-reasoning mode)
- GPT-5.2 (medium): 2025-12-11 model version (reasoning_effort="medium")
- GPT-5.2: 2025-12-11 model version (reasoning_effort="none" as default)
- Nova 2.0 Lite: us.amazon.nova-2-lite-v1:0 model (reasoning mode: medium)
- GPT-5.1 (medium): 2025-11-13 model version (reasoning_effort="medium")
- GPT-5.1: 2025-11-13 model version (reasoning_effort="none" as default)
- GPT-5.1-chat: 2025-11-13 model version 
- GPT-5-chat: 2025-08-08 model version 
- GPT-5-mini: 2025-08-08 model version (reasoning_effort="medium" as default)
- GPT-5-nano: 2025-08-08 model version (reasoning_effort="medium" as default)
- GPT-4.1: 2025-04-14 model version
- GPT-4.1-mini: 2025-04-14 model version
- GPT-4.1-nano: 2025-04-14 model version
- GPT-4o: 2024-05-13 model version
- GPT-4o-mini: 2024-07-18 model version
- GPT-4-turbo: 2024-04-09 model version
- GPT-3.5-turbo: 2023-06-13 model version

</details>

### CLIcK

#### Accuracy by supercategory
| supercategory   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash (reasoning=high) |   DeepSeek-V4-Flash (reasoning=none) |
|:----------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Culture         |                              95.02 |                                92.12 |                            94.76 |                              91.45 |                             91.3  |                                85.87 |                                80.37 |
| Language        |                              97.54 |                                90.31 |                            97.04 |                              93.85 |                             92    |                                84.62 |                                80    |
| **Overall**     |                              95.84 |                                91.53 |                            95.5  |                              92.24 |                             91.53 |                                85.46 |                                80.25 |


<details>
<summary>Click to view Accuracy by category</summary>

##### Accuracy by category
| supercategory   | category    |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash (reasoning=high) |   DeepSeek-V4-Flash (reasoning=none) |
|:----------------|:------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Culture         | Economy     |                             100    |                                94.92 |                           100    |                              98.31 |                            100    |                                96.61 |                                94.92 |
| Culture         | Geography   |                              94.66 |                                95.42 |                            96.18 |                              92.37 |                             93.13 |                                90.08 |                                83.97 |
| Culture         | History     |                              90.36 |                                89.29 |                            89.29 |                              85    |                             87.14 |                                76.79 |                                63.57 |
| Culture         | Law         |                              99.54 |                                89.95 |                            98.58 |                              90.41 |                             91.32 |                                74.89 |                                69.41 |
| Culture         | Politics    |                              92.86 |                                89.29 |                            90.48 |                              92.21 |                             86.9  |                                90.48 |                                86.9  |
| Culture         | Pop Culture |                             100    |                                97.56 |                            97.56 |                              97.5  |                            100    |                                97.56 |                                90.24 |
| Culture         | Society     |                              96.12 |                                94.82 |                            96.12 |                              95.22 |                             94.17 |                                93.53 |                                91.26 |
| Culture         | Tradition   |                              93.69 |                                91.44 |                            95.05 |                              91.89 |                             89.19 |                                88.29 |                                86.94 |
| Language        | Functional  |                              98.4  |                                93.6  |                            98.4  |                              96.8  |                             92    |                                88    |                                88    |
| Language        | Grammar     |                              98.33 |                                85.42 |                            96.98 |                              89.58 |                             90    |                                76.25 |                                62.08 |
| Language        | Textual     |                              96.49 |                                92.98 |                            96.49 |                              96.14 |                             93.68 |                                90.18 |                                91.58 |
</details>

### HAERAE

#### Accuracy by category
| category              |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash (reasoning=high) |   DeepSeek-V4-Flash (reasoning=none) |
|:----------------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| General Knowledge     |                              88.64 |                                80.11 |                            94.32 |                              91.48 |                             89.2  |                                82.95 |                                72.16 |
| History               |                              98.4  |                                96.81 |                            96.81 |                              96.28 |                             96.28 |                                96.81 |                                92.55 |
| Loan Words            |                              97.63 |                                88.76 |                            95.27 |                              91.72 |                             92.9  |                                89.35 |                                77.51 |
| Rare Words            |                              98.52 |                                97.28 |                            94.96 |                              93.09 |                             95.56 |                                88.89 |                                90.12 |
| Reading Comprehension |                              94.41 |                                91.05 |                            92.84 |                              91.72 |                             90.83 |                                89.71 |                                85.91 |
| Standard Nomenclature |                              96.08 |                                92.16 |                            96.08 |                              94.12 |                             94.77 |                                90.85 |                                81.7  |
| **Overall**           |                              95.84 |                                92    |                            94.64 |                              92.85 |                             93.17 |                                89.66 |                                84.92 |

### KoBALT

#### Accuracy by category
| category    |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash (reasoning=high) |   DeepSeek-V4-Flash (reasoning=none) |
|:------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Easy        |                              97.8  |                                95.05 |                            98.9  |                              97.8  |                             97.25 |                                79.12 |                                85.16 |
| Moderate    |                              92.27 |                                77.27 |                            90.45 |                              89.09 |                             87.73 |                                61.82 |                                50.91 |
| Hard        |                              68.79 |                                43.29 |                            70.81 |                              54.36 |                             56.71 |                                24.5  |                                25.17 |
| **Overall** |                              83.71 |                                67.43 |                            84.29 |                              76.57 |                             77    |                                50.43 |                                48.86 |

### KMMLU-HARD (0-shot)

#### Accuracy by supercategory
| supercategory   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash (reasoning=high) |   DeepSeek-V4-Flash (reasoning=none) |
|:----------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Applied Science |                              88.42 |                                76    |                            85.56 |                              78.37 |                             76.08 |                                72.67 |                                59.5  |
| HUMSS           |                              89.54 |                                77.41 |                            87.27 |                              76.81 |                             75.74 |                                59.1  |                                55.41 |
| Other           |                              83.49 |                                72.27 |                            81.05 |                              74.14 |                             71.65 |                                59.71 |                                50.88 |
| STEM            |                              89.55 |                                81    |                            86.27 |                              81.41 |                             79    |                                76.64 |                                60.55 |
| **Overall**     |                              87.79 |                                76.75 |                            85.04 |                              77.86 |                             75.76 |                                67.91 |                                56.92 |


<details>
<summary>Click to view Accuracy by category</summary>

##### Accuracy by category
| supercategory   | category                                   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash (reasoning=high) |   DeepSeek-V4-Flash (reasoning=none) |
|:----------------|:-------------------------------------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                              94    |                                75    |                            85    |                              82.61 |                             77    |                                75    |                                65    |
| Applied Science | Electronics-Engineering                    |                              95    |                                89    |                            95    |                              90    |                             85    |                                87    |                                80    |
| Applied Science | Energy-Management                          |                              94    |                                77    |                            89    |                              83    |                             79    |                                72    |                                54    |
| Applied Science | Environmental-Science                      |                              89    |                                70    |                            87    |                              74    |                             72    |                                66    |                                49    |
| Applied Science | Gas-Technology-and-Engineering             |                              89    |                                76    |                            83.7  |                              78    |                             77    |                                67    |                                51    |
| Applied Science | Geomatics                                  |                              97    |                                84    |                            90    |                              85.06 |                             86    |                                79    |                                61    |
| Applied Science | Industrial-Engineer                        |                              74    |                                61    |                            69    |                              62    |                             60    |                                56    |                                44    |
| Applied Science | Machine-Design-and-Manufacturing           |                              93    |                                79    |                            88    |                              81    |                             77    |                                77    |                                62    |
| Applied Science | Maritime-Engineering                       |                              92    |                                84    |                            91    |                              82    |                             82    |                                80    |                                65    |
| Applied Science | Nondestructive-Testing                     |                              76    |                                65    |                            76    |                              66    |                             69    |                                63    |                                61    |
| Applied Science | Railway-and-Automotive-Engineering         |                              85    |                                76    |                            88    |                              80    |                             76    |                                73    |                                59    |
| Applied Science | Telecommunications-and-Wireless-Technology |                              83    |                                76    |                            84.78 |                              78    |                             73    |                                77    |                                63    |
| HUMSS           | Accounting                                 |                             100    |                                89.13 |                            97.83 |                              95.65 |                             89.13 |                                80.43 |                                73.91 |
| HUMSS           | Criminal-Law                               |                              87    |                                68    |                            82.61 |                              57    |                             62    |                                42    |                                47    |
| HUMSS           | Economics                                  |                              97.62 |                                92.86 |                            95.24 |                              90.48 |                             80.95 |                                73.81 |                                64.29 |
| HUMSS           | Education                                  |                             100    |                                95.65 |                           100    |                              95.65 |                             95.65 |                                78.26 |                                78.26 |
| HUMSS           | Korean-History                             |                              84.09 |                                84.09 |                            84.09 |                              72.73 |                             75    |                                59.09 |                                40.91 |
| HUMSS           | Law                                        |                              84    |                                67    |                            78    |                              70    |                             68    |                                47    |                                48    |
| HUMSS           | Management                                 |                              88    |                                77    |                            90    |                              80    |                             74    |                                70    |                                62    |
| HUMSS           | Political-Science-and-Sociology            |                              91.11 |                                85.56 |                            87.78 |                              83.33 |                             86.67 |                                63.33 |                                60    |
| HUMSS           | Psychology                                 |                              92    |                                78    |                            92    |                              86    |                             76    |                                56    |                                55    |
| HUMSS           | Social-Welfare                             |                              90    |                                83    |                            84    |                              82    |                             78    |                                80    |                                65    |
| HUMSS           | Taxation                                   |                              86.46 |                                64.58 |                            86.46 |                              62.5  |                             73.96 |                                34.38 |                                39.58 |
| Other           | Agricultural-Sciences                      |                              81    |                                66    |                            76    |                              73    |                             68    |                                58    |                                48    |
| Other           | Construction                               |                              86    |                                72    |                            81    |                              72    |                             73    |                                59    |                                52    |
| Other           | Fashion                                    |                              68    |                                54    |                            67    |                              58    |                             52    |                                41    |                                32    |
| Other           | Food-Processing                            |                              81    |                                66    |                            75    |                              74    |                             64    |                                59    |                                50    |
| Other           | Health                                     |                             100    |                                91.3  |                            86.96 |                              91.3  |                             86.96 |                                60.87 |                                65.22 |
| Other           | Interior-Architecture-and-Design           |                              88    |                                83    |                            88    |                              77    |                             82    |                                76    |                                64    |
| Other           | Marketing                                  |                              77    |                                69    |                            75    |                              72.83 |                             66    |                                62    |                                56    |
| Other           | Patent                                     |                              90.2  |                                78.43 |                            92.16 |                              74.51 |                             70.59 |                                45.1  |                                31.37 |
| Other           | Public-Safety                              |                              80    |                                72    |                            78    |                              68    |                             75    |                                61    |                                49    |
| Other           | Real-Estate                                |                              91.01 |                                68.54 |                            93.26 |                              76.4  |                             78.65 |                                42.7  |                                44.94 |
| Other           | Refrigerating-Machinery                    |                              93    |                                92    |                            91.3  |                              92    |                             84    |                                84    |                                68    |
| STEM            | Biology                                    |                              87    |                                75    |                            87    |                              79    |                             77    |                                72    |                                50    |
| STEM            | Chemical-Engineering                       |                              89    |                                81    |                            88    |                              85    |                             84    |                                86    |                                61    |
| STEM            | Chemistry                                  |                              98    |                                88    |                            94    |                              90    |                             91    |                                89    |                                77    |
| STEM            | Civil-Engineering                          |                              82    |                                74    |                            78    |                              73    |                             71    |                                68    |                                56    |
| STEM            | Computer-Science                           |                              84    |                                80    |                            81    |                              78.26 |                             73    |                                73    |                                69    |
| STEM            | Ecology                                    |                              84    |                                70    |                            77    |                              69    |                             70    |                                52    |                                53    |
| STEM            | Electrical-Engineering                     |                              93    |                                84    |                            85    |                              73    |                             75    |                                73    |                                55    |
| STEM            | Information-Technology                     |                              91    |                                82    |                            91    |                              87.63 |                             78    |                                82    |                                75    |
| STEM            | Materials-Engineering                      |                              92    |                                82    |                            88    |                              84.78 |                             81    |                                75    |                                64    |
| STEM            | Math                                       |                              92    |                                91    |                            89    |                              91    |                             88    |                                89    |                                39    |
| STEM            | Mechanical-Engineering                     |                              93    |                                84    |                            91    |                              85    |                             81    |                                84    |                                67    |
</details>

> **Looking for older model results (GPT-5.2, GPT-5.1, Nova 2, GPT-4.1, Phi, Llama, etc.)?**
> See [PREVIOUS_RESULTS.md](PREVIOUS_RESULTS.md) for full CLIcK/HAE-RAE/KMMLU/KMMLU-HARD tables from earlier benchmark rounds.

## 🚀 Quick Start

### GitHub Codespace
Please start a new project by connecting to Codespace Project. The environment required for hands-on is automatically configured through devcontainer, so you only need to run a Jupyter notebook.

### Your Local PC
Please start by installing the required packages on your local PC through uv.

```bash
uv sync
```

To use Jupyter Notebook in VS Code or Cursor, choose one of the two methods below:
1. Click **Select Kernel** - **Python Environments**, and then select **.venv**.
<img src="./imgs/quick-start-01.png" width="100%"/>
<img src="./imgs/quick-start-02.png" width="50%"/>

2. Click **Python: Select Interpreter** with the shortcut **Ctrl + Shift + P (Windows/Linux)**, **Cmd + Shift + P (macOS)**, and then select **.venv**.
<img src="./imgs/quick-start-03.png" width="100%"/>

### Configuration

#### Multiple Models Setup
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

#### Configuration Options

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

#### Azure OpenAI
```ini
AZURE_OPENAI_ENDPOINT=<YOUR_ENDPOINT>
AZURE_OPENAI_API_KEY=<YOUR_API_KEY>
AZURE_OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
AZURE_OPENAI_API_VERSION=2025-04-01-preview
```

#### Azure AI Foundry
```ini
AZURE_AI_INFERENCE_KEY=<YOUR_API_KEY>
AZURE_AI_INFERENCE_ENDPOINT=<YOUR_ENDPOINT>
AZURE_AI_DEPLOYMENT_NAME=Phi-4
```

#### Amazon Bedrock
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

#### Amazon Bedrock (OpenAI models, e.g. GPT-5.6)
OpenAI models on Bedrock (GPT-5.6 Sol/Terra/Luna, etc.) are served only through the
`bedrock-mantle` endpoint's Responses API, not the regular `bedrock-runtime` Converse API.
Use `MODEL_PROVIDER=bedrock_openai` for these models:
```ini
MODEL_PROVIDER=bedrock_openai
BEDROCK_OPENAI_MODEL_ID=openai.gpt-5.6-sol  # or openai.gpt-5.6-terra, openai.gpt-5.6-luna
AWS_REGION=us-east-1
# AWS_BEARER_TOKEN_BEDROCK must be set in the shell environment (not the .env file)
```

#### OpenAI
```ini
OPENAI_API_KEY=<YOUR_API_KEY>
OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
```

#### OpenAI-compatible self-hosted endpoint (e.g. vLLM)
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

#### Azure ML
```ini
AZURE_ML_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
AZURE_ML_ENDPOINT_URL=<YOUR_ENDPOINT_URL>
AZURE_ML_ENDPOINT_TYPE=<dedicated or serverless>
AZURE_ML_API_KEY=<YOUR_API_KEY>
```

#### Hugging Face
```ini
HF_API_TOKEN=<YOUR_HF_API_TOKEN>
```

### Running Evaluations

#### Interactive Mode (Recommended)
Run the interactive script that guides you through the evaluation process:

```bash
./run.sh
```

The script will ask you to:
1. Select dataset (`CLIcK`, `HAE-RAE`, `KMMLU`, `KMMLU-HARD`, `HRM8K`, `KoBALT`, `KorMedMCQA`)
2. Choose debug mode (`y/n`)
3. Set batch size (default: `10`)
4. Set max tokens (default: `1500`)
5. Set temperature (default: `0.01`)
6. Set number of workers (default: `4`)

#### Manual Mode
Run individual benchmarks directly:

```bash
# Example: CLIcK benchmark
uv run python benchmarks/click_main.py \
    --model_provider bedrock \
    --batch_size 4 \
    --is_debug true \
    --num_debug_samples 20 \
    --num_workers 5 \
    --max_tokens 512 \
    --temperature 0.01

# Available benchmark scripts:
# benchmarks/click_main.py
# benchmarks/haerae_main.py  
# benchmarks/kmmlu_main.py
# benchmarks/hrm8k_main.py
# benchmarks/kobalt_main.py
# benchmarks/kormedmcqa_main.py
```

### Available Parameters

```python
--is_debug              # Enable debug mode (default: True)
--num_debug_samples     # Number of samples in debug mode (default: 20)
--model_provider        # Provider: azureopenai, bedrock, openai, azureml, azureaifoundry, huggingface
--batch_size            # Batch size for processing (default: 10)
--max_retries           # Maximum retry attempts (default: 3)
--max_tokens            # Maximum tokens in response (default: 256)
--temperature           # Sampling temperature (default: 0.01)
--template_type         # Prompt template type (default: basic)
--wait_time             # Wait time between requests (default: 1.0)
--num_workers           # Number of parallel workers for processing (default: 4)
--num_shots             # Number of few-shot examples for KMMLU (default: 0)
--is_hard               # Use KMMLU-HARD dataset (default: False)
--subset                # HRM8K subset: GSM8K, MATH, OMNI_MATH, MMMLU, KSM (default: GSM8K)
--categories            # Specific categories to evaluate (optional)
```

### Output

Evaluation results are saved in:
- `./results/` - Detailed CSV results for each model and dataset
- `./evals/` - Aggregated evaluation metrics

## 📚 References

<details>
<summary>Expand...</summary>

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

@misc{son2024kmmlumeasuringmassivemultitask,
      title={KMMLU: Measuring Massive Multitask Language Understanding in Korean}, 
      author={Guijin Son and Hanwool Lee and Sungdong Kim and Seungone Kim and Niklas Muennighoff and Taekyoon Choi and Cheonbok Park and Kang Min Yoo and Stella Biderman},
      year={2024},
      eprint={2402.11548},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.11548}, 
}

@misc{ko2025hrm8k,
      title={HRM8K: A Bilingual Math Reasoning Benchmark for Korean and English}, 
      author={Hyunwoo Ko and Guijin Son and Dasol Choi},
      year={2025},
      eprint={2501.02448},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.02448}, 
}

@misc{lee2025kobalt,
      title={KoBALT: A Benchmark for Evaluating Korean Linguistic Phenomena in Large Language Models}, 
      author={Dohyun Lee and Seunghyun Hwang and Seungtaek Choi and Hwisang Jeon and Sohyun Park and Sungjoon Park and Yungi Kim},
      year={2025},
      eprint={2505.16125},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.16125}, 
}

@misc{kweon2024kormedmcqa,
      title={KorMedMCQA: Multi-Choice Question Answering Benchmark for Korean Healthcare Professional Licensing Examinations}, 
      author={Sunjun Kweon and Jiyoun Kim and Sujeong Im and Eunbyeol Cho and Seongsu Bae and Jungwoo Oh and Gyubok Lee and Jong Hak Moon and Seng Chan You and Seungjin Baek and Chang Hoon Han and Yoon Bin Jung and Yohan Jo and Edward Choi},
      year={2024},
      eprint={2403.01469},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2403.01469}, 
}
```
</details>