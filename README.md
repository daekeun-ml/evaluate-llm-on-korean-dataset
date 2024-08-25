# Korean language proficiency evaluation for LLM/SLM models using KMMLU, CLIcK, and HAE-RAE dataset

## Overview

With the continuous emergence of various LLM/SLM models, there is a need for robust evaluation datasets for non-English languages such as Korean. KMMLU (Korean Massive Multi-task Language Understanding), CLIcK (Cultural and Linguistic Intelligence in Korean) and HAE_RAE_BENCH 1.0 fill this gap by providing a rich, well-categorized dataset that focuses on cultural and linguistic aspects, enabling detailed evaluation of Korean language models. This code performs benchmarking on two datasets with minimal time and effort.

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


## Implementation

The code skeleton is based on https://github.com/corca-ai/evaluating-gpt-4o-on-CLIcK, but a lot of parts have changed. 

In particular, we modified the code to run on Azure OpenAI & Hugging Face and added logic for parallel processing, content filtering (400 error), and max request error (429 error) exception handling. 

## Results
🔥 Aug 25, 2024: Added experimental results for **KMMLU** and **KMMLU-HARD** benchmark datasets. Added **Phi-3-mini-128K-instruct (June version)** benchmark results.

🔥 Aug 22, 2024: Added **Phi-3-5-mini-instruct** and **Phi-3.5-MoE-instruct** benchmark results. Phi-3.5 is Microsoft's latest open source model that has begun to properly support multiple languages, and its Korean performance has been greatly improved, as shown in the benchmark results below.

🔥 Aug 22, 2024: Added **Llama-3-1-8B-instruct** benchmark results. Of course, fine-tuned Llama-3.1 with Korean dataset may perform better, but we only compared it with the vanilla model.

🔥 Aug 9, 2024: Added Azure OpenAI **GPT-3.5-turbo (2023-06-13)**, **GPT-4-turbo (2024-04-09)**, **GPT-4o (2024-05-13)**, and **GPT-4o-mini (2024-07-18)** benchmark results.

### Notes
The numbers in the table below are the average accuracy (%). For Azure OpenAI models, a few questions are filtered out due to the content filtering feature, but this only happens between 1-5 samples in the entire dataset, so the impact is not significant. 

The prompt is the same as the CLIcK paper prompt. The experimental results may vary depending on the system prompt, context, and parameters. The experimental results below were given with max_tokens=512, temperature=0.01 without using few-shot, context, or system prompt.

Since most of them are ChatCompletion or instruction fine-tuned models, the variation may be large compared to the results of other group's experiments. However, our experimental results show that the trend follows similarly under the same experimental conditions. (e.g., GPT-4o: 70.57/GPT-4o-mini: 60.31 in Experimental Condition 1; GPT-4o: 67.76/GPT-4o-mini: 57.53 in Experimental Condition 2).

- GPT-4o: 2024-05-13 version
- GPT-4o-mini: 2024-07-18 version
- GPT-4-turbo: 2024-04-09 version
- GPT-3.5-turbo: 2023-06-13 version

### CLIcK
#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Culture         |                  58.44 |                   43.77 |                           29.74 |                   51.15 |    81.89 |         70.95 |         73.61 |           53.38 |
| Language        |                  52.31 |                   41.38 |                           27.85 |                   40.92 |    77.54 |         63.54 |         71.23 |           46    |
| **Overall**     |                  56.44 |                   42.99 |                           29.12 |                   47.82 |    80.46 |         68.5  |         72.82 |           50.98 |

#### Accuracy by category
| supercategory   | category    |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Culture         | Economy     |                  77.97 |                   61.02 |                           28.81 |                   66.1  |    94.92 |         83.05 |         89.83 |           64.41 |
| Culture         | Geography   |                  60.31 |                   45.8  |                           29.01 |                   54.2  |    80.15 |         77.86 |         82.44 |           53.44 |
| Culture         | History     |                  33.93 |                   26.15 |                           30    |                   29.64 |    66.92 |         48.4  |         46.4  |           31.79 |
| Culture         | Law         |                  52.51 |                   32.42 |                           22.83 |                   44.29 |    70.78 |         57.53 |         61.19 |           41.55 |
| Culture         | Politics    |                  70.24 |                   54.76 |                           33.33 |                   59.52 |    88.1  |         83.33 |         89.29 |           65.48 |
| Culture         | Pop Culture |                  80.49 |                   60.98 |                           34.15 |                   60.98 |    97.56 |         85.37 |         92.68 |           75.61 |
| Culture         | Society     |                  74.43 |                   54.37 |                           31.72 |                   65.05 |    92.88 |         85.44 |         86.73 |           71.2  |
| Culture         | Tradition   |                  58.11 |                   47.75 |                           31.98 |                   54.95 |    87.39 |         74.77 |         79.28 |           55.86 |
| Language        | Functional  |                  48    |                   37.6  |                           24    |                   32.8  |    84.8  |         64.8  |         80    |           40    |
| Language        | Grammar     |                  29.58 |                   27.5  |                           23.33 |                   22.92 |    57.08 |         42.5  |         47.5  |           30    |
| Language        | Textual     |                  73.33 |                   54.74 |                           33.33 |                   59.65 |    91.58 |         80.7  |         87.37 |           62.11 |

### HAE_RAE_BENCH 1.0

#### Accuracy by category
| category              |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| General Knowledge     |                  39.77 |                   31.25 |                           28.41 |                   34.66 |    77.27 |         53.41 |         66.48 |           40.91 |
| History               |                  60.64 |                   32.45 |                           22.34 |                   44.15 |    92.02 |         84.57 |         78.72 |           30.32 |
| Loan Words            |                  70.41 |                   47.93 |                           35.5  |                   63.31 |    79.88 |         76.33 |         78.11 |           59.17 |
| Rare Words            |                  63.95 |                   55.06 |                           42.96 |                   63.21 |    87.9  |         81.98 |         79.01 |           61.23 |
| Reading Comprehension |                  64.43 |                   42.95 |                           41.16 |                   51.9  |    85.46 |         77.18 |         80.09 |           56.15 |
| Standard Nomenclature |                  66.01 |                   44.44 |                           32.68 |                   58.82 |    88.89 |         75.82 |         79.08 |           53.59 |
| **Overall**           |                  61.83 |                   44.21 |                           36.41 |                   53.9  |    85.7  |         76.4  |         77.76 |           52.67 |

### KMMLU
#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  45.15 |                   35.8  |                           31.68 |                   37.03 |    61.35 |         49.19 |         55.97 |           38.47 |
| HUMSS           |                  49.75 |                   31.56 |                           26.47 |                   37.27 |    69.28 |         56.37 |         63    |           40.9  |
| Other           |                  47.24 |                   35.45 |                           31.01 |                   39.15 |    63.64 |         52.32 |         57.51 |           40.19 |
| STEM            |                  49.08 |                   38.54 |                           31.9  |                   40.42 |    65.03 |         54.64 |         60.83 |           42.23 |
| **Overall**     |                  47.43 |                   35.87 |                           30.82 |                   38.54 |    64.1  |         52.53 |         58.74 |           40.3  |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  47.9  |                   34.9  |                           30.1  |                   36.6  |    69.7  |         50.3  |         61.82 |           39    |
| Applied Science | Electronics-Engineering                    |                  55.4  |                   42.7  |                           33.9  |                   42.9  |    72.8  |         64.3  |         70.2  |           47.1  |
| Applied Science | Energy-Management                          |                  35.7  |                   27.4  |                           26.9  |                   29.6  |    49.9  |         39.5  |         43.6  |           33.9  |
| Applied Science | Environmental-Science                      |                  36    |                   33.8  |                           30.1  |                   30.2  |    45.41 |         36.5  |         42.7  |           30.51 |
| Applied Science | Gas-Technology-and-Engineering             |                  39.7  |                   31.7  |                           30.8  |                   31.7  |    50.6  |         44.3  |         48.3  |           35    |
| Applied Science | Geomatics                                  |                  42.7  |                   37.5  |                           33.6  |                   36.1  |    56.3  |         43.7  |         47.3  |           35.7  |
| Applied Science | Industrial-Engineer                        |                  48.6  |                   40.5  |                           32.7  |                   41.9  |    61.6  |         53.1  |         57    |           41.12 |
| Applied Science | Machine-Design-and-Manufacturing           |                  46.2  |                   34.6  |                           29.5  |                   35.5  |    68.3  |         52.9  |         61    |           37.9  |
| Applied Science | Maritime-Engineering                       |                  48    |                   34.67 |                           30.67 |                   40    |    67    |         52.5  |         60.17 |           42.67 |
| Applied Science | Nondestructive-Testing                     |                  48.5  |                   34.7  |                           31.3  |                   39.2  |    65.2  |         47.9  |         59.7  |           35.8  |
| Applied Science | Railway-and-Automotive-Engineering         |                  37.8  |                   30.3  |                           31.3  |                   33.2  |    53.6  |         40.5  |         48.6  |           32.5  |
| Applied Science | Telecommunications-and-Wireless-Technology |                  56.4  |                   46.4  |                           38.9  |                   48.7  |    77.8  |         66.1  |         73    |           52.24 |
| HUMSS           | Accounting                                 |                  47    |                   34    |                           22    |                   32    |    72    |         48    |         59    |           30    |
| HUMSS           | Criminal-Law                               |                  31.5  |                   25    |                           18.5  |                   30    |    52.5  |         36.5  |         46.5  |           40.5  |
| HUMSS           | Economics                                  |                  53.08 |                   31.54 |                           24.62 |                   31.54 |    74.62 |         64.62 |         65.38 |           43.85 |
| HUMSS           | Education                                  |                  64    |                   37    |                           31    |                   44    |    83    |         70    |         69    |           43    |
| HUMSS           | Korean-History                             |                  32    |                   33    |                           16    |                   34    |    56    |         29    |         41    |           26    |
| HUMSS           | Law                                        |                  43.4  |                   32.7  |                           26.6  |                   36    |    65.8  |         50.6  |         56.7  |           38.23 |
| HUMSS           | Management                                 |                  57    |                   34.2  |                           28.3  |                   39.7  |    73.7  |         64.2  |         70.7  |           47.9  |
| HUMSS           | Political-Science-and-Sociology            |                  58.33 |                   36.67 |                           26.33 |                   43.33 |    79.67 |         61.67 |         72.67 |           46.67 |
| HUMSS           | Psychology                                 |                  44.7  |                   27.6  |                           23.7  |                   35    |    66.4  |         50.3  |         57.3  |           32.8  |
| HUMSS           | Social-Welfare                             |                  58.5  |                   31.8  |                           29.6  |                   40.2  |    74.1  |         67.3  |         73.2  |           46.4  |
| HUMSS           | Taxation                                   |                  33    |                   25.5  |                           29.5  |                   31    |    51    |         39.5  |         44    |           33.5  |
| Other           | Agricultural-Sciences                      |                  37.8  |                   32.3  |                           30.6  |                   31.4  |    53.9  |         41.8  |         47.58 |           30.1  |
| Other           | Construction                               |                  37.5  |                   33.8  |                           32.4  |                   32.4  |    50.6  |         41.8  |         46    |           33.2  |
| Other           | Fashion                                    |                  47.4  |                   35    |                           30.8  |                   41.5  |    65.8  |         51.1  |         58.28 |           39.7  |
| Other           | Food-Processing                            |                  45.8  |                   31.7  |                           30.9  |                   39.2  |    64.9  |         51.6  |         57.4  |           37.3  |
| Other           | Health                                     |                  58    |                   44    |                           29    |                   44    |    80    |         69    |         70    |           50    |
| Other           | Interior-Architecture-and-Design           |                  58    |                   40.9  |                           34.3  |                   44    |    77.5  |         64    |         71.1  |           48.2  |
| Other           | Marketing                                  |                  73    |                   48.7  |                           31.3  |                   63.3  |    88.9  |         83.1  |         86.26 |           63.6  |
| Other           | Patent                                     |                  45    |                   24    |                           25    |                   26    |    52    |         33    |         46    |           40    |
| Other           | Public-Safety                              |                  41.2  |                   33.2  |                           32    |                   34.2  |    53    |         44.2  |         48.2  |           36.2  |
| Other           | Real-Estate                                |                  47    |                   31    |                           23    |                   32.5  |    64.5  |         49    |         56.5  |           38    |
| Other           | Refrigerating-Machinery                    |                  36.4  |                   29.2  |                           28.2  |                   29.4  |    53.9  |         41.9  |         45.6  |           32.7  |
| STEM            | Biology                                    |                  39.9  |                   29.6  |                           27.2  |                   34    |    63.1  |         45.5  |         52.83 |           31.84 |
| STEM            | Chemical-Engineering                       |                  46.9  |                   36.3  |                           29    |                   35.7  |    65    |         55.6  |         62.6  |           38.5  |
| STEM            | Chemistry                                  |                  51.17 |                   36.83 |                           28.33 |                   36.17 |    68.67 |         57.33 |         64.33 |           39.67 |
| STEM            | Civil-Engineering                          |                  43.1  |                   33.7  |                           32.1  |                   36    |    53.7  |         46.9  |         50.3  |           38.3  |
| STEM            | Computer-Science                           |                  73.8  |                   56.9  |                           40.7  |                   60.4  |    88.2  |         80.1  |         84.8  |           65.7  |
| STEM            | Ecology                                    |                  48.8  |                   41.6  |                           33.9  |                   41.6  |    64.4  |         54.3  |         60    |           42.9  |
| STEM            | Electrical-Engineering                     |                  39    |                   32.6  |                           31    |                   32.1  |    45.9  |         38.5  |         44.1  |           31.7  |
| STEM            | Information-Technology                     |                  66.1  |                   52.1  |                           39.4  |                   57.1  |    83.6  |         78.2  |         81.2  |           63.78 |
| STEM            | Materials-Engineering                      |                  46.9  |                   34.6  |                           29.2  |                   37.1  |    69.4  |         52.1  |         64.55 |           39.69 |
| STEM            | Math                                       |                  26.33 |                   29    |                           25.67 |                   23.33 |    32.67 |         28.33 |         28.33 |           26    |
| STEM            | Mechanical-Engineering                     |                  42.8  |                   33.3  |                           28.6  |                   37.5  |    59.5  |         46.8  |         54.7  |           34.2  |

### KMMLU-HARD
#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  25.83 |                   27.08 |                           26.17 |                   26.25 |    36.86 |         22.17 |         29.17 |           21.07 |
| HUMSS           |                  21.52 |                   20.21 |                           24.38 |                   20.21 |    41.97 |         23.07 |         31.51 |           19.44 |
| Other           |                  24.82 |                   23.05 |                           24.82 |                   23.88 |    40.29 |         26.48 |         29.59 |           22.22 |
| STEM            |                  28.18 |                   24.36 |                           26.91 |                   24.64 |    39.55 |         26.27 |         32.18 |           20.91 |
| **Overall**     |                  25.34 |                   24    |                           25.68 |                   24.03 |    39.45 |         24.46 |         30.56 |           20.97 |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  22    |                   29    |                           24    |                   25    |    45    |         25    |         32    |           25    |
| Applied Science | Electronics-Engineering                    |                  34    |                   31    |                           23    |                   26    |    42    |         29    |         41    |           22    |
| Applied Science | Energy-Management                          |                  23    |                   30    |                           22    |                   27    |    38    |         27    |         37    |           22.45 |
| Applied Science | Environmental-Science                      |                  28    |                   26    |                           36    |                   30    |    26.25 |         20    |         24    |           31.25 |
| Applied Science | Gas-Technology-and-Engineering             |                  30    |                   28    |                           24    |                   23    |    35    |         23    |         28    |           13    |
| Applied Science | Geomatics                                  |                  23    |                   23    |                           31    |                   29    |    34    |         22    |         24    |           22    |
| Applied Science | Industrial-Engineer                        |                  28    |                   30    |                           32    |                   25    |    32    |         19    |         26    |           25    |
| Applied Science | Machine-Design-and-Manufacturing           |                  27    |                   24    |                           23    |                   24    |    45    |         17    |         27    |           16.25 |
| Applied Science | Maritime-Engineering                       |                  26    |                   27    |                           25    |                   28    |    32    |         19    |         26    |           21    |
| Applied Science | Nondestructive-Testing                     |                  26    |                   31    |                           19    |                   25    |    36    |         22    |         23    |           14    |
| Applied Science | Railway-and-Automotive-Engineering         |                  20    |                   25    |                           28    |                   26    |    32    |         17    |         24    |           18    |
| Applied Science | Telecommunications-and-Wireless-Technology |                  23    |                   21    |                           27    |                   27    |    43    |         26    |         38    |           24    |
| HUMSS           | Accounting                                 |                  19.57 |                    8.7  |                           17.39 |                   23.91 |    50    |         21.74 |         21.74 |           13.04 |
| HUMSS           | Criminal-Law                               |                  22    |                   20    |                           24    |                   16    |    31    |         16    |         22    |           27    |
| HUMSS           | Economics                                  |                  21.43 |                   23.81 |                           26.19 |                   14.29 |    52.38 |         26.19 |         38.1  |           26.19 |
| HUMSS           | Education                                  |                  21.74 |                   30.43 |                           39.13 |                   21.74 |    56.52 |         43.48 |         34.78 |           17.39 |
| HUMSS           | Korean-History                             |                  15.91 |                   13.64 |                           15.91 |                   27.27 |    40.91 |         18.18 |         27.27 |           18.18 |
| HUMSS           | Law                                        |                  29    |                   18    |                           27    |                   17    |    40    |         20    |         28    |           15.85 |
| HUMSS           | Management                                 |                  22    |                   27    |                           20    |                   28    |    42    |         26    |         38    |           22    |
| HUMSS           | Political-Science-and-Sociology            |                  22.22 |                   20    |                           21.11 |                   14.44 |    53.33 |         25.56 |         38.89 |           23.33 |
| HUMSS           | Psychology                                 |                  15    |                   22    |                           22    |                   19    |    44    |         20    |         32    |            7    |
| HUMSS           | Social-Welfare                             |                  27    |                   23    |                           29    |                   17    |    45    |         32    |         47    |           24    |
| HUMSS           | Taxation                                   |                  16.67 |                   15.62 |                           30.21 |                   27.08 |    28.12 |         18.75 |         17.71 |           17.71 |
| Other           | Agricultural-Sciences                      |                  27    |                   21    |                           28    |                   18    |    38    |         23    |         28    |           17    |
| Other           | Construction                               |                  29    |                   23    |                           28    |                   24    |    34    |         28    |         27    |           23    |
| Other           | Fashion                                    |                  21    |                   26    |                           22    |                   28    |    31    |         23    |         20    |           29    |
| Other           | Food-Processing                            |                  24    |                   19    |                           26    |                   19    |    38    |         21    |         26    |           19    |
| Other           | Health                                     |                   8.7  |                   13.04 |                           17.39 |                   34.78 |    39.13 |         34.78 |         34.78 |           17.39 |
| Other           | Interior-Architecture-and-Design           |                  30    |                   28    |                           32    |                   26    |    49    |         29    |         36.67 |           25    |
| Other           | Marketing                                  |                  32    |                   26    |                           25    |                   32    |    54    |         39    |         46    |           22    |
| Other           | Patent                                     |                  15.69 |                   23.53 |                           19.61 |                   17.65 |    47.06 |         25.49 |         25.49 |           37.25 |
| Other           | Public-Safety                              |                  24    |                   21    |                           20    |                   26    |    31    |         19    |         25    |           17    |
| Other           | Real-Estate                                |                  23.6  |                   23.6  |                           23.6  |                   26.97 |    39.33 |         20.22 |         32.58 |           19.1  |
| Other           | Refrigerating-Machinery                    |                  21    |                   22    |                           23    |                   16    |    45    |         34    |         27    |           22    |
| STEM            | Biology                                    |                  22    |                   21    |                           23    |                   24    |    46    |         27    |         26    |           13    |
| STEM            | Chemical-Engineering                       |                  32    |                   25    |                           38    |                   23    |    37    |         21    |         34    |           20    |
| STEM            | Chemistry                                  |                  28    |                   30    |                           26    |                   22    |    50    |         35    |         45    |           27    |
| STEM            | Civil-Engineering                          |                  19    |                   28    |                           25    |                   22    |    38    |         23    |         29    |           13    |
| STEM            | Computer-Science                           |                  38    |                   26    |                           27    |                   29    |    47    |         31    |         36    |           26    |
| STEM            | Ecology                                    |                  28    |                   15    |                           26    |                   26    |    39    |         26    |         25    |           19    |
| STEM            | Electrical-Engineering                     |                  27    |                   27    |                           31    |                   26    |    34    |         19    |         24    |           16    |
| STEM            | Information-Technology                     |                  29    |                   28    |                           24    |                   27    |    43    |         35    |         44    |           28    |
| STEM            | Materials-Engineering                      |                  33    |                   23    |                           27    |                   29    |    43    |         25    |         33    |           24    |
| STEM            | Math                                       |                  23    |                   15    |                           22    |                   20    |    23    |         25    |         22    |           22    |
| STEM            | Mechanical-Engineering                     |                  31    |                   30    |                           27    |                   23    |    35    |         22    |         36    |           22    |

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
AZURE_OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME> (e.g., gpt-4o-mini)
OPENAI_MODEL_VERSION=<YOUR_OPENAI_MODEL_VERSION> (e.g., 2024-07-18)>
```

### OpenAI
```ini
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
OPENAI_DEPLOYMENT_NAME=<YOUR_OPENAI_API_VERSION>
OPENAI_MODEL_VERSION=<YOUR_OPENAI_MODEL_VERSION> (e.g., 2024-07-18)
```

### Azure ML
You can create endpoints by provisioning a managed compute host or using the serverless option.
For Phi-3.5, if you do not have a managed GPU compute quota, you can temporarily use Microsoft's shared quota for 168 hours. For more information, please refer to these links: [Phi-3.5 deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python), [Azure ML deployment](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-deploy-model)
```ini
AZURE_ML_DEPLOYMENT_NAME=<YOUR_ML_DEPLOYMENT_NAME>
AZURE_ML_ENDPOINT_URL=<YOUR_ML_ENDPOINT_URL>
AZURE_ML_ENDPOINT_TYPE=<YOUR_ML_ENDPOINT_TYPE> (dedicated or serverless)
AZURE_ML_API_KEY=<YOUR_ML_API_KEY>
```

### Hugging Face
Please refer to [this guide](https://huggingface.co/docs/hub/security-tokens) to generate a Hugging Face token.
```ini
HF_API_TOKEN=<YOUR_HF_API_TOKEN>
```

Execute the command to perform the evaluation. (The evaluation results are saved in the `./results` folder and `./evals`.)
Below is an example.
   
```bash
#!/bin/bash
model_provider="azureopenai"

# CLIcK
python3 click_main.py \
      --model_provider "$model_provider" \
      --batch_size 20 \
      --max_tokens 512 \
      --temperature 0.01 \
      --template_type basic

# HAERAE
python3 haerae_main.py \
      --model_provider "$model_provider" \
      --batch_size 20 \
      --max_tokens 512 \
      --temperature 0.01 \
      --template_type basic

# KMMLU
python3 kmmlu_main.py \
      --model_provider "$model_provider" \
      --batch_size 20 \
      --max_tokens 512 \
      --temperature 0.01 \
      --template_type basic \
      --is_hard False
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
parser.add_argument("--template_type", type=str, default="basic")
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

@misc{son2024kmmlumeasuringmassivemultitask,
      title={KMMLU: Measuring Massive Multitask Language Understanding in Korean}, 
      author={Guijin Son and Hanwool Lee and Sungdong Kim and Seungone Kim and Niklas Muennighoff and Taekyoon Choi and Cheonbok Park and Kang Min Yoo and Stella Biderman},
      year={2024},
      eprint={2402.11548},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.11548}, 
}
```