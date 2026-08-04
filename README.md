# Korean LLM/SLM Evaluation Suite

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

### KMMLU-Pro
KMMLU-Pro is a professional-licensure benchmark comprising 2,822 problems from official Korean National Professional Licensure (KNPL) exams, covering 15 licenses (e.g. lawyer, doctor, CPA, tax accountant) across 4 domains (Law, Tax & Accounting, Value Estimation, Medicine) and 63 subjects. Questions have 4 or 5 choices depending on the source exam.

- [Paper](https://arxiv.org/abs/2507.08924), [Hugging Face](https://huggingface.co/datasets/LGAI-EXAONE/KMMLU-Pro) (gated — requires accepting the dataset conditions)

### MuSR(Ko)
MuSR(Ko) is a Korean adaptation of MuSR (Multistep Soft Reasoning), evaluating multi-step reasoning over long synthetic narratives across 3 task types: murder mysteries (2-choice, 250 samples), object placements (4-choice, 250 samples), and team allocation (3-choice, 250 samples), for 750 samples total.

- [Hugging Face](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-MuSR) (gated — requires accepting the dataset conditions)

## 🆕 What's New

- Aug 4, 2026: Added **KMMLU-Pro** (2,822 professional-licensure questions across 14 licenses) and **MuSR(Ko)** (750 multi-step reasoning questions across murder mysteries / object placements / team allocation) benchmark datasets, with results for **GPT-5.6 (Sol/Terra/Luna)**, **Claude Sonnet 5**, **Claude Opus 5**, and **DeepSeek-V4-Flash-0731** (reasoning=none and reasoning=high). **Claude Opus 5** leads both: 95.11% on KMMLU-Pro and 86.53% on MuSR(Ko).

- Aug 4, 2026: Added **GPT-5.6 (Sol/Terra/Luna)**, **Claude Sonnet 5**, **Claude Opus 5** (all Amazon Bedrock, reasoning_effort=medium) and **DeepSeek-V4-Flash-0731** (self-hosted via vLLM, tested at both reasoning=none and reasoning=high) benchmark results on CLIcK, HAE-RAE, KoBALT-700, and KMMLU-HARD. **Claude Opus 5** leads on CLIcK (95.84%), HAE-RAE (95.84%), and KMMLU-HARD (87.79%); **GPT-5.6 Sol** leads on KoBALT-700 (84.29%). DeepSeek-V4-Flash-0731 improves substantially with reasoning enabled (e.g. KoBALT-700: 48.86% → 50.43%, KMMLU-HARD: 56.92% → 67.91%) but still trails the frontier reasoning models. Older per-model results (GPT-5.2, GPT-5.1, Nova 2, GPT-4.1, Phi, Llama, etc.) have moved to [PREVIOUS_RESULTS.md](PREVIOUS_RESULTS.md).

<details>
<summary>Older updates</summary>

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

</details>

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

Charts below compare the current model round: GPT-5.6 (Sol/Terra/Luna), Claude Sonnet 5, Claude Opus 5, and DeepSeek-V4-Flash-0731 (reasoning=high).

| CLIcK Performance by Category | HAERAE Performance by Category |
|:---:|:---:|
| <img src="./charts/CLIcK_radar_chart.png" width="650"> | <img src="./charts/HAERAE_radar_chart.png" width="650">  |

| KoBALT-700 Performance by Difficulty | KMMLU-Hard Performance by Supercategory |
|:---:|:---:|
| <img src="./charts/KoBALT_radar_chart.png" width="650"> | <img src="./charts/KMMLU-HARD_radar_chart.png" width="650"> |

| KMMLU-Pro Performance by License | MuSR(Ko) Performance by Task Type |
|:---:|:---:|
| <img src="./charts/KMMLU-Pro_radar_chart.png" width="650"> | <img src="./charts/MuSR-Ko_radar_chart.png" width="650"> |

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
- DeepSeek-V4-Flash-0731 (reasoning=high): DeepSeek-V4-Flash-0731, self-hosted via vLLM (chat_template_kwargs thinking=True, reasoning_effort="high" — the model only supports low/high/max, no "medium")
- DeepSeek-V4-Flash-0731 (reasoning=none): DeepSeek-V4-Flash-0731, self-hosted via vLLM (non-reasoning mode)
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
| supercategory   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
|:----------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Culture         |                              95.02 |                                92.12 |                            94.76 |                              91.45 |                             91.3  |                                85.87 |                                80.37 |
| Language        |                              97.54 |                                90.31 |                            97.04 |                              93.85 |                             92    |                                84.62 |                                80    |
| **Overall**     |                              95.84 |                                91.53 |                            95.5  |                              92.24 |                             91.53 |                                85.46 |                                80.25 |


<details>
<summary>Click to view Accuracy by category</summary>

##### Accuracy by category
| supercategory   | category    |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
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
| category              |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
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
| category    |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
|:------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Easy        |                              97.8  |                                95.05 |                            98.9  |                              97.8  |                             97.25 |                                79.12 |                                85.16 |
| Moderate    |                              92.27 |                                77.27 |                            90.45 |                              89.09 |                             87.73 |                                61.82 |                                50.91 |
| Hard        |                              68.79 |                                43.29 |                            70.81 |                              54.36 |                             56.71 |                                24.5  |                                25.17 |
| **Overall** |                              83.71 |                                67.43 |                            84.29 |                              76.57 |                             77    |                                50.43 |                                48.86 |

### KMMLU-HARD (0-shot)

#### Accuracy by supercategory
| supercategory   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
|:----------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|-------------------------------------:|-------------------------------------:|
| Applied Science |                              88.42 |                                76    |                            85.56 |                              78.37 |                             76.08 |                                72.67 |                                59.5  |
| HUMSS           |                              89.54 |                                77.41 |                            87.27 |                              76.81 |                             75.74 |                                59.1  |                                55.41 |
| Other           |                              83.49 |                                72.27 |                            81.05 |                              74.14 |                             71.65 |                                59.71 |                                50.88 |
| STEM            |                              89.55 |                                81    |                            86.27 |                              81.41 |                             79    |                                76.64 |                                60.55 |
| **Overall**     |                              87.79 |                                76.75 |                            85.04 |                              77.86 |                             75.76 |                                67.91 |                                56.92 |


<details>
<summary>Click to view Accuracy by category</summary>

##### Accuracy by category
| supercategory   | category                                   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
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


### KMMLU-Pro

#### Accuracy by supercategory
| supercategory   |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
|:----------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|------------------------------------------:|------------------------------------------:|
| 감정평가사      |                              96.43 |                                91.33 |                            95.93 |                              87.76 |                             87.76 |                                     68.88 |                                     57.65 |
| 공인노무사      |                              93.72 |                                82.01 |                            93.07 |                              82.01 |                             85.36 |                                     62.34 |                                     59.83 |
| 공인회계사      |                              97.6  |                                80.77 |                            95.67 |                              85.1  |                             86.06 |                                     67.31 |                                     50.96 |
| 관세사          |                              94.97 |                                85.53 |                            92.05 |                              81.76 |                             83.65 |                                     64.78 |                                     61.01 |
| 법무사          |                              87.88 |                                67.68 |                            83.33 |                              61.11 |                             64.14 |                                     31.82 |                                     41.92 |
| 변리사          |                              97.25 |                                82.57 |                            91.74 |                              69.72 |                             80.73 |                                     47.71 |                                     55.96 |
| 변호사          |                              90.67 |                                68    |                            88    |                              69.33 |                             61.33 |                                     30    |                                     52    |
| 세무사          |                              95.38 |                                78.57 |                            92.02 |                              79.83 |                             79.83 |                                     55.46 |                                     51.26 |
| 손해사정사      |                              95.83 |                                85.83 |                            88.39 |                              77.5  |                             78.33 |                                     57.5  |                                     62.5  |
| 약사            |                              98.15 |                                94.46 |                            98.15 |                              96.68 |                             95.94 |                                     93.36 |                                     89.67 |
| 의사            |                              98.67 |                                98    |                            98    |                              95.33 |                             99.33 |                                     90.67 |                                     84    |
| 치과의사        |                              93.65 |                                86.11 |                            95.08 |                              90.08 |                             91.67 |                                     82.54 |                                     75.4  |
| 한약사          |                              98.36 |                                96.72 |                            97.95 |                              97.95 |                             97.13 |                                     95.49 |                                     91.39 |
| 한의사          |                              93.4  |                                90.97 |                            94.79 |                              87.85 |                             89.58 |                                     82.99 |                                     72.22 |
| **Overall**     |                              95.11 |                                85.51 |                            93.64 |                              84.44 |                             85.54 |                                     69.35 |                                     66.19 |


<details>
<summary>Click to view Accuracy by category (63 subjects)</summary>

##### Accuracy by category
| supercategory   | category                         |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
|:----------------|:---------------------------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|------------------------------------------:|------------------------------------------:|
| 감정평가사      | 감정평가관계법규                 |                              85    |                                80    |                            87.5  |                              77.5  |                             85    |                                     42.5  |                                     57.5  |
| 감정평가사      | 경제학원론                       |                             100    |                               100    |                           100    |                             100    |                             97.37 |                                     97.37 |                                     68.42 |
| 감정평가사      | 민법                             |                             100    |                                87.5  |                           100    |                              72.5  |                             75    |                                     42.5  |                                     50    |
| 감정평가사      | 부동산학원론                     |                             100    |                                95    |                            95    |                              95    |                             92.5  |                                     77.5  |                                     65    |
| 감정평가사      | 회계학                           |                              97.37 |                                94.74 |                            96.67 |                              94.74 |                             89.47 |                                     86.84 |                                     47.37 |
| 공인노무사      | 경영학개론                       |                             100    |                               100    |                           100    |                             100    |                            100    |                                     95    |                                     95    |
| 공인노무사      | 경제학원론                       |                             100    |                                97.5  |                            97.5  |                              95    |                             97.5  |                                     95    |                                     65    |
| 공인노무사      | 노동법1                          |                              97.5  |                                85    |                            97.5  |                              85    |                             95    |                                     57.5  |                                     52.5  |
| 공인노무사      | 노동법2                          |                              82.05 |                                66.67 |                            82.05 |                              64.1  |                             61.54 |                                     41.03 |                                     48.72 |
| 공인노무사      | 민법                             |                              95    |                                75    |                            96.88 |                              82.5  |                             77.5  |                                     42.5  |                                     55    |
| 공인노무사      | 사회보험법                       |                              87.5  |                                67.5  |                            85    |                              65    |                             80    |                                     42.5  |                                     42.5  |
| 공인회계사      | 경영학                           |                             100    |                                95    |                           100    |                              95    |                             97.5  |                                     92.5  |                                     77.5  |
| 공인회계사      | 경제원론                         |                              97.37 |                               100    |                            97.37 |                             100    |                             97.37 |                                    100    |                                     50    |
| 공인회계사      | 상법                             |                             100    |                                85    |                            95    |                              87.5  |                             82.5  |                                     55    |                                     57.5  |
| 공인회계사      | 세법개론                         |                              90    |                                40    |                            87.5  |                              47.5  |                             62.5  |                                     10    |                                     32.5  |
| 공인회계사      | 회계학                           |                             100    |                                84    |                            98    |                              94    |                             90    |                                     78    |                                     40    |
| 관세사          | 관세법개론                       |                              92.5  |                                70    |                            90    |                              72.5  |                             80    |                                     40    |                                     52.5  |
| 관세사          | 내국소비세법                     |                              95    |                                85    |                            87.5  |                              75    |                             77.5  |                                     55    |                                     57.5  |
| 관세사          | 무역영어                         |                              95    |                                92.5  |                            95    |                              90    |                             85    |                                     80    |                                     75    |
| 관세사          | 회계학                           |                              97.44 |                                94.87 |                            94.87 |                              89.74 |                             92.31 |                                     84.62 |                                     58.97 |
| 법무사          | 가족관계의등록등에관한법률       |                              70    |                                70    |                            80    |                              50    |                             80    |                                      0    |                                     40    |
| 법무사          | 공탁법                           |                              80    |                                70    |                            55    |                              55    |                             70    |                                     40    |                                     50    |
| 법무사          | 민법                             |                              97.5  |                                75    |                            95    |                              75    |                             77.5  |                                     42.5  |                                     45    |
| 법무사          | 민사집행법                       |                              80    |                                60    |                            88.57 |                              54.29 |                             60    |                                     34.29 |                                     31.43 |
| 법무사          | 부동산등기법                     |                              75.86 |                                37.93 |                            68.97 |                              51.72 |                             37.93 |                                     13.79 |                                     34.48 |
| 법무사          | 상법                             |                             100    |                                96.55 |                            93.1  |                              58.62 |                             75.86 |                                     51.72 |                                     65.52 |
| 법무사          | 상업등기법및비송사건절차법       |                             100    |                                60    |                            86.67 |                              66.67 |                             46.67 |                                     13.33 |                                     33.33 |
| 법무사          | 헌법                             |                              90    |                                70    |                            85    |                              70    |                             65    |                                     25    |                                     30    |
| 변리사          | 민법개론                         |                             100    |                                82.5  |                            90    |                              62.5  |                             85    |                                     25    |                                     47.5  |
| 변리사          | 산업재산권법                     |                              94.87 |                                71.79 |                            87.18 |                              61.54 |                             64.1  |                                     33.33 |                                     51.28 |
| 변리사          | 자연과학개론                     |                              96.67 |                                96.67 |                           100    |                              90    |                             96.67 |                                     96.67 |                                     73.33 |
| 변호사          | 공법                             |                              97.5  |                                90    |                            97.5  |                              80    |                             65    |                                     35    |                                     50    |
| 변호사          | 민사법                           |                              85.71 |                                57.14 |                            78.57 |                              65.71 |                             62.86 |                                     27.14 |                                     48.57 |
| 변호사          | 형사법                           |                              92.5  |                                65    |                            95    |                              65    |                             55    |                                     30    |                                     60    |
| 세무사          | 민법                             |                              97.5  |                                95    |                            92.5  |                              85    |                             85    |                                     60    |                                     57.5  |
| 세무사          | 상법                             |                             100    |                                84.62 |                            97.44 |                              84.62 |                             87.18 |                                     46.15 |                                     56.41 |
| 세무사          | 세법학개론                       |                              82.5  |                                37.5  |                            85    |                              55    |                             62.5  |                                     22.5  |                                     45    |
| 세무사          | 재정학                           |                             100    |                                97.44 |                           100    |                              97.44 |                             94.87 |                                     97.44 |                                     69.23 |
| 세무사          | 행정소송법                       |                             100    |                                77.5  |                            87.5  |                              75    |                             70    |                                     32.5  |                                     42.5  |
| 세무사          | 회계학개론                       |                              92.5  |                                80    |                            90    |                              82.5  |                             80    |                                     75    |                                     37.5  |
| 손해사정사      | 보험계약법                       |                              97.5  |                                90    |                            87.5  |                              70    |                             75    |                                     47.5  |                                     65    |
| 손해사정사      | 보험업법                         |                              92.5  |                                80    |                            84.38 |                              70    |                             70    |                                     42.5  |                                     47.5  |
| 손해사정사      | 손해사정이론                     |                              97.5  |                                87.5  |                            92.5  |                              92.5  |                             90    |                                     82.5  |                                     75    |
| 약사            | 보건의약관계법규                 |                              85    |                                50    |                            85    |                              65    |                             65    |                                     55    |                                     65    |
| 약사            | 산업약학                         |                              96.67 |                                96.67 |                            96.67 |                              96.67 |                             95    |                                     96.67 |                                     86.67 |
| 약사            | 생명약학                         |                             100    |                                98.84 |                           100    |                             100    |                            100    |                                     98.84 |                                     97.67 |
| 약사            | 임상실무약학                     |                             100    |                                98.1  |                           100    |                             100    |                             99.05 |                                     94.29 |                                     89.52 |
| 의사            | 보건의약관계법규                 |                             100    |                                95    |                           100    |                              85    |                            100    |                                     85    |                                     70    |
| 의사            | 의학각론                         |                              98.94 |                                98.94 |                            97.87 |                              96.81 |                            100    |                                     93.62 |                                     86.17 |
| 의사            | 의학총론                         |                              97.22 |                                97.22 |                            97.22 |                              97.22 |                             97.22 |                                     86.11 |                                     86.11 |
| 치과의사        | 구강악안면외과학                 |                              96.55 |                                86.21 |                            96.55 |                              96.55 |                             96.55 |                                     86.21 |                                     86.21 |
| 치과의사        | 보건의약관계법규                 |                              95    |                                80    |                            95    |                              80    |                             90    |                                     65    |                                     65    |
| 치과의사        | 소아치과학/치과교정학            |                              84.85 |                                81.82 |                            87.88 |                              90.91 |                             87.88 |                                     78.79 |                                     69.7  |
| 치과의사        | 영상치의학/구강내과학/구강병리학 |                              95    |                                95    |                           100    |                              95    |                             95    |                                     90    |                                     85    |
| 치과의사        | 치과보존학                       |                              96.77 |                                87.1  |                           100    |                              93.55 |                             93.55 |                                     87.1  |                                     87.1  |
| 치과의사        | 치과보철학                       |                              87.1  |                                74.19 |                            90.32 |                              77.42 |                             80.65 |                                     74.19 |                                     61.29 |
| 치과의사        | 치과재료학/구강생물학            |                             100    |                               100    |                           100    |                             100    |                             98.08 |                                    100    |                                     82.69 |
| 치과의사        | 치주과학/구강보건학              |                              91.67 |                                77.78 |                            91.67 |                              80.56 |                             88.89 |                                     66.67 |                                     63.89 |
| 한약사          | 보건의약관계법규                 |                              93.1  |                                79.31 |                            89.66 |                              86.21 |                             82.76 |                                     68.97 |                                     65.52 |
| 한약사          | 한약학 응용                      |                              99.06 |                                98.11 |                            99.06 |                              99.06 |                             98.11 |                                     98.11 |                                     95.28 |
| 한약사          | 한약학기초                       |                              99.08 |                               100    |                            99.08 |                             100    |                            100    |                                    100    |                                     94.5  |
| 한의사          | 내과학1                          |                              97.14 |                                94.29 |                            97.14 |                              94.29 |                             97.14 |                                     85.71 |                                     80    |
| 한의사          | 내과학2                          |                              84.38 |                                71.88 |                            90.62 |                              71.88 |                             68.75 |                                     62.5  |                                     21.88 |
| 한의사          | 보건의약관계법규                 |                              95    |                                85    |                            95    |                              80    |                             90    |                                     80    |                                     65    |
| 한의사          | 본초학                           |                             100    |                               100    |                            91.67 |                              83.33 |                             91.67 |                                     91.67 |                                     83.33 |
| 한의사          | 부인과학                         |                              90    |                                90    |                            93.33 |                              86.67 |                             86.67 |                                     83.33 |                                     73.33 |
| 한의사          | 소아과학                         |                              90.91 |                                90.91 |                           100    |                              90.91 |                             86.36 |                                     77.27 |                                     63.64 |
| 한의사          | 신경정신과학                     |                              92.86 |                               100    |                            92.86 |                              85.71 |                             85.71 |                                     92.86 |                                     85.71 |
| 한의사          | 안이비인후과학                   |                              85.71 |                                85.71 |                           100    |                              85.71 |                            100    |                                     85.71 |                                     71.43 |
| 한의사          | 예방의학                         |                             100    |                               100    |                           100    |                             100    |                            100    |                                    100    |                                     90.48 |
| 한의사          | 외과학                           |                             100    |                                75    |                           100    |                             100    |                            100    |                                    100    |                                    100    |
| 한의사          | 침구학                           |                              92.5  |                                95    |                            90    |                              82.5  |                             87.5  |                                     82.5  |                                     80    |
| 한의사          | 한방생리학                       |                              93.75 |                                93.75 |                            93.75 |                             100    |                             93.75 |                                     81.25 |                                     87.5  |
</details>

### MuSR-Ko

#### Accuracy by category
| category          |   Claude Opus 5 (reasoning=medium) |   Claude Sonnet 5 (reasoning=medium) |   GPT-5.6 Sol (reasoning=medium) |   GPT-5.6 Terra (reasoning=medium) |   GPT-5.6 Luna (reasoning=medium) |   DeepSeek-V4-Flash-0731 (reasoning=high) |   DeepSeek-V4-Flash-0731 (reasoning=none) |
|:------------------|-----------------------------------:|-------------------------------------:|---------------------------------:|-----------------------------------:|----------------------------------:|------------------------------------------:|------------------------------------------:|
| murder_mysteries  |                              78    |                                 68.4 |                            76.45 |                              72    |                             66.4  |                                     61.6  |                                     57.2  |
| object_placements |                              94.4  |                                 92.8 |                            96.4  |                              95.87 |                             74.8  |                                     61.2  |                                     44.8  |
| team_allocation   |                              87.2  |                                 83.6 |                            82.8  |                              82    |                             73.2  |                                     73.2  |                                     70    |
| **Overall**       |                              86.53 |                                 81.6 |                            85.31 |                              83.15 |                             71.47 |                                     65.33 |                                     57.33 |

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

Create a `.env` file (or multiple files under `env/` for parallel multi-model runs — see
`./run.sh`) with `MODEL_PROVIDER` plus that provider's credentials. Supported providers:
Azure OpenAI, Azure AI Foundry, Amazon Bedrock (including Claude Sonnet/Opus 5 and Bedrock-hosted
OpenAI models like GPT-5.6), OpenAI (including self-hosted OpenAI-compatible endpoints such as
vLLM), Azure ML, and Hugging Face.

**Full provider reference and `.env` examples: [CONFIGURATION.md](CONFIGURATION.md)**

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

@article{hong2025kmmlupro,
      title={From KMMLU-Redux to KMMLU-Pro: A Professional Korean Benchmark Suite for LLM Evaluation},
      author={Hong, Seokhee and Kim, Sunkyoung and Son, Guijin and Kim, Soyeon and Hong, Yeonjung and Lee, Jinsik},
      journal={arXiv preprint arXiv:2507.08924},
      year={2025}
}

@inproceedings{sprague2024musr,
      title={MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning},
      author={Sprague, Zayne and Ye, Xi and Bostrom, Kaj and Chaudhuri, Swarat and Durrett, Greg},
      booktitle={ICLR},
      year={2024},
      note={MuSR(Ko) is the Korean adaptation used in this repo: \url{https://huggingface.co/datasets/thunder-research-group/SNU_Ko-MuSR}}
}
```
</details>