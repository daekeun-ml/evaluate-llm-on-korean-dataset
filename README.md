# Korean language proficiency evaluation for LLM/SLM models using CLIcK and HAE-RAE dataset

## Overview

With the continuous emergence of various LLM/SLM models, there is a need for robust evaluation datasets for non-English languages such as Korean. CLIcK (Cultural and Linguistic Intelligence in Korean) and HAE_RAE_BENCH 1.0 fill this gap by providing a rich, well-categorized dataset that focuses on cultural and linguistic aspects, enabling detailed evaluation of Korean language models. This code performs benchmarking on two datasets with minimal time and effort.
- unit: correct_mean; Only the second decimal place was used. For exact results, please refer to the results folder.

### CLIcK (Cultural and Linguistic Intelligence in Korean)
This dataset assesses Korean language proficiency in the subject areas of Korean Culture (History, Geography, Law, Politics, Society, Tradition, Economy, Pop culture) and Korean Language (Textual, Functional, Grammar). There are a total of 1,995 sample data in 11 categories. This dataset presents 4- or 5-choice multiple choice questions. Depending on the question, additional context is given.

- [Paper](https://arxiv.org/abs/2403.06412), [GitHub](https://github.com/rladmstn1714/CLIcK), [Hugging Face](https://huggingface.co/datasets/EunsuKim/CLIcK)

### HAE_RAE_BENCH 1.0
This dataset evaluates Korean language proficiency in the following 6 categories (General Knowledge, History, Loan Words, Rare Words, Reading Comprehension, Standard Nomenclature). Similar to CLiCK, the task is to solve multiple-choice questions, but no additional context. There are a total of 1,538 sample data in 6 categories.

- [Paper](https://arxiv.org/abs/2309.02706), [GitHub](https://github.com/HAE-RAE/HAE-RAE-BENCH), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0)

### KMMLU
The KMMLU (Korean Massive Multi-task Language Understanding) dataset is a large-scale multi-task language understanding evaluation dataset in Korean. It is not a simple translation of the MMLU dataset, but rather data generated from Korean text, allowing us to evaluate how well LLM/SLM works in Korean. It consists of a total of 45 categories and 4 super categories, such as STEM, Appliced ​​Science, HUMSS, and Other.

- [Paper](https://arxiv.org/abs/2402.11548), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KMMLU)

### KMMLU-HARD
This dataset is an extended version of the KMMLU dataset, with more challenging questions. It is designed to further evaluate the limits of Korean NLP models and contains questions that require a particularly high level of comprehension and reasoning skills.

- [Paper](https://arxiv.org/abs/2402.11548), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KMMLU-HARD)


## Implementation

The code skeleton is based on https://github.com/corca-ai/evaluating-gpt-4o-on-CLIcK, but a lot of parts have changed. 

In particular, we modified the code to run on Azure OpenAI & Hugging Face and added logic for parallel processing, content filtering (400 error), and max request error (429 error) exception handling. 

## Results
🔥 Aug 25, 2024: Added experimental results for KMMLU and KMMLU-HARD benchmark datasets.

🔥 Aug 22, 2024: Added **Phi-3-5-mini-instruct** and **Phi-3.5-MoE-instruct** benchmark results. Phi-3.5 is Microsoft's latest open source model that has begun to properly support multiple languages, and its Korean performance has been greatly improved, as shown in the benchmark results below.

🔥 Aug 22, 2024: Added **Llama-3-1-8B-instruct** benchmark results. Of course, fine-tuned Llama-3.1 with Korean dataset may perform better, but we only compared it with the vanilla model.

🔥 Aug 9, 2024: Added Azure OpenAI **GPT-3.5-turbo (2023-06-13)**, **GPT-4-turbo (2024-04-09)**, **GPT-4o (2024-05-13)**, and **GPT-4o-mini (2024-07-18)** benchmark results.

### Notes
The prompt is the same as the CLIcK paper prompt. The experimental results may vary depending on the system prompt, context, and parameters. The experimental results below were given with max_tokens=512, temperature=0.01 without using few-shot, context, or system prompt.

Since most of them are ChatCompletion or instruction fine-tuned models, the variation may be large compared to the results of other group's experiments. However, our experimental results show that the trend follows similarly under the same experimental conditions. (e.g., GPT-4o: 70.57/GPT-4o-mini: 60.31 in Experimental Condition 1; GPT-4o: 67.76/GPT-4o-mini: 57.53 in Experimental Condition 2).

### CLIcK

#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Culture         |                  58.44 |                   43.77 |                   51.15 |    81.89 |         53.38 |         70.95 |           73.61 |
| Language        |                  52.31 |                   41.38 |                   40.92 |    77.54 |         46    |         63.54 |           71.23 |
| **Overall**     |                  56.44 |                   42.99 |                   47.82 |    80.46 |         50.98 |         68.5  |           72.82 |

#### Accuracy by category
| supercategory   | category    |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Culture         | Economy     |                  77.97 |                   61.02 |                   66.1  |    94.92 |         64.41 |         83.05 |           89.83 |
| Culture         | Geography   |                  60.31 |                   45.8  |                   54.2  |    80.15 |         53.44 |         77.86 |           82.44 |
| Culture         | History     |                  33.93 |                   26.15 |                   29.64 |    66.92 |         31.79 |         48.4  |           46.4  |
| Culture         | Law         |                  52.51 |                   32.42 |                   44.29 |    70.78 |         41.55 |         57.53 |           61.19 |
| Culture         | Politics    |                  70.24 |                   54.76 |                   59.52 |    88.1  |         65.48 |         83.33 |           89.29 |
| Culture         | Pop Culture |                  80.49 |                   60.98 |                   60.98 |    97.56 |         75.61 |         85.37 |           92.68 |
| Culture         | Society     |                  74.43 |                   54.37 |                   65.05 |    92.88 |         71.2  |         85.44 |           86.73 |
| Culture         | Tradition   |                  58.11 |                   47.75 |                   54.95 |    87.39 |         55.86 |         74.77 |           79.28 |
| Language        | Functional  |                  48    |                   37.6  |                   32.8  |    84.8  |         40    |         64.8  |           80    |
| Language        | Grammar     |                  29.58 |                   27.5  |                   22.92 |    57.08 |         30    |         42.5  |           47.5  |
| Language        | Textual     |                  73.33 |                   54.74 |                   59.65 |    91.58 |         62.11 |         80.7  |           87.37 |

### HAE_RAE_BENCH 1.0

#### Accuracy by category
| category              |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| General Knowledge     |                  39.77 |                   31.25 |                   34.66 |    77.27 |         40.91 |         53.41 |           66.48 |
| History               |                  60.64 |                   32.45 |                   44.15 |    92.02 |         30.32 |         84.57 |           78.72 |
| Loan Words            |                  70.41 |                   47.93 |                   63.31 |    79.88 |         59.17 |         76.33 |           78.11 |
| Rare Words            |                  63.95 |                   55.06 |                   63.21 |    87.9  |         61.23 |         81.98 |           79.01 |
| Reading Comprehension |                  64.43 |                   42.95 |                   51.9  |    85.46 |         56.15 |         77.18 |           80.09 |
| Standard Nomenclature |                  66.01 |                   44.44 |                   58.82 |    88.89 |         53.59 |         75.82 |           79.08 |
| **Overall**           |                  61.83 |                   44.21 |                   53.9  |    85.7  |         52.67 |         76.4  |           77.76 |

### KMMLU

#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  45.15 |                   35.8  |                   37.03 |    61.35 |         38.47 |         49.19 |           55.97 |
| HUMSS           |                  49.75 |                   31.56 |                   37.27 |    69.28 |         40.9  |         56.37 |           63    |
| Other           |                  47.24 |                   35.45 |                   39.15 |    63.64 |         40.19 |         52.32 |           57.51 |
| STEM            |                  49.08 |                   38.54 |                   40.42 |    65.03 |         42.23 |         54.64 |           60.83 |
| **Overall**     |                  47.43 |                   35.87 |                   38.54 |    64.1  |         40.3  |         52.53 |           58.74 |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  47.9  |                   34.9  |                   36.6  |    69.7  |         39    |         50.3  |           61.82 |
| Applied Science | Electronics-Engineering                    |                  55.4  |                   42.7  |                   42.9  |    72.8  |         47.1  |         64.3  |           70.2  |
| Applied Science | Energy-Management                          |                  35.7  |                   27.4  |                   29.6  |    49.9  |         33.9  |         39.5  |           43.6  |
| Applied Science | Environmental-Science                      |                  36    |                   33.8  |                   30.2  |    45.41 |         30.51 |         36.5  |           42.7  |
| Applied Science | Gas-Technology-and-Engineering             |                  39.7  |                   31.7  |                   31.7  |    50.6  |         35    |         44.3  |           48.3  |
| Applied Science | Geomatics                                  |                  42.7  |                   37.5  |                   36.1  |    56.3  |         35.7  |         43.7  |           47.3  |
| Applied Science | Industrial-Engineer                        |                  48.6  |                   40.5  |                   41.9  |    61.6  |         41.12 |         53.1  |           57    |
| Applied Science | Machine-Design-and-Manufacturing           |                  46.2  |                   34.6  |                   35.5  |    68.3  |         37.9  |         52.9  |           61    |
| Applied Science | Maritime-Engineering                       |                  48    |                   34.67 |                   40    |    67    |         42.67 |         52.5  |           60.17 |
| Applied Science | Nondestructive-Testing                     |                  48.5  |                   34.7  |                   39.2  |    65.2  |         35.8  |         47.9  |           59.7  |
| Applied Science | Railway-and-Automotive-Engineering         |                  37.8  |                   30.3  |                   33.2  |    53.6  |         32.5  |         40.5  |           48.6  |
| Applied Science | Telecommunications-and-Wireless-Technology |                  56.4  |                   46.4  |                   48.7  |    77.8  |         52.24 |         66.1  |           73    |
| HUMSS           | Accounting                                 |                  47    |                   34    |                   32    |    72    |         30    |         48    |           59    |
| HUMSS           | Criminal-Law                               |                  31.5  |                   25    |                   30    |    52.5  |         40.5  |         36.5  |           46.5  |
| HUMSS           | Economics                                  |                  53.08 |                   31.54 |                   31.54 |    74.62 |         43.85 |         64.62 |           65.38 |
| HUMSS           | Education                                  |                  64    |                   37    |                   44    |    83    |         43    |         70    |           69    |
| HUMSS           | Korean-History                             |                  32    |                   33    |                   34    |    56    |         26    |         29    |           41    |
| HUMSS           | Law                                        |                  43.4  |                   32.7  |                   36    |    65.8  |         38.23 |         50.6  |           56.7  |
| HUMSS           | Management                                 |                  57    |                   34.2  |                   39.7  |    73.7  |         47.9  |         64.2  |           70.7  |
| HUMSS           | Political-Science-and-Sociology            |                  58.33 |                   36.67 |                   43.33 |    79.67 |         46.67 |         61.67 |           72.67 |
| HUMSS           | Psychology                                 |                  44.7  |                   27.6  |                   35    |    66.4  |         32.8  |         50.3  |           57.3  |
| HUMSS           | Social-Welfare                             |                  58.5  |                   31.8  |                   40.2  |    74.1  |         46.4  |         67.3  |           73.2  |
| HUMSS           | Taxation                                   |                  33    |                   25.5  |                   31    |    51    |         33.5  |         39.5  |           44    |
| Other           | Agricultural-Sciences                      |                  37.8  |                   32.3  |                   31.4  |    53.9  |         30.1  |         41.8  |           47.58 |
| Other           | Construction                               |                  37.5  |                   33.8  |                   32.4  |    50.6  |         33.2  |         41.8  |           46    |
| Other           | Fashion                                    |                  47.4  |                   35    |                   41.5  |    65.8  |         39.7  |         51.1  |           58.28 |
| Other           | Food-Processing                            |                  45.8  |                   31.7  |                   39.2  |    64.9  |         37.3  |         51.6  |           57.4  |
| Other           | Health                                     |                  58    |                   44    |                   44    |    80    |         50    |         69    |           70    |
| Other           | Interior-Architecture-and-Design           |                  58    |                   40.9  |                   44    |    77.5  |         48.2  |         64    |           71.1  |
| Other           | Marketing                                  |                  73    |                   48.7  |                   63.3  |    88.9  |         63.6  |         83.1  |           86.26 |
| Other           | Patent                                     |                  45    |                   24    |                   26    |    52    |         40    |         33    |           46    |
| Other           | Public-Safety                              |                  41.2  |                   33.2  |                   34.2  |    53    |         36.2  |         44.2  |           48.2  |
| Other           | Real-Estate                                |                  47    |                   31    |                   32.5  |    64.5  |         38    |         49    |           56.5  |
| Other           | Refrigerating-Machinery                    |                  36.4  |                   29.2  |                   29.4  |    53.9  |         32.7  |         41.9  |           45.6  |
| STEM            | Biology                                    |                  39.9  |                   29.6  |                   34    |    63.1  |         31.84 |         45.5  |           52.83 |
| STEM            | Chemical-Engineering                       |                  46.9  |                   36.3  |                   35.7  |    65    |         38.5  |         55.6  |           62.6  |
| STEM            | Chemistry                                  |                  51.17 |                   36.83 |                   36.17 |    68.67 |         39.67 |         57.33 |           64.33 |
| STEM            | Civil-Engineering                          |                  43.1  |                   33.7  |                   36    |    53.7  |         38.3  |         46.9  |           50.3  |
| STEM            | Computer-Science                           |                  73.8  |                   56.9  |                   60.4  |    88.2  |         65.7  |         80.1  |           84.8  |
| STEM            | Ecology                                    |                  48.8  |                   41.6  |                   41.6  |    64.4  |         42.9  |         54.3  |           60    |
| STEM            | Electrical-Engineering                     |                  39    |                   32.6  |                   32.1  |    45.9  |         31.7  |         38.5  |           44.1  |
| STEM            | Information-Technology                     |                  66.1  |                   52.1  |                   57.1  |    83.6  |         63.78 |         78.2  |           81.2  |
| STEM            | Materials-Engineering                      |                  46.9  |                   34.6  |                   37.1  |    69.4  |         39.69 |         52.1  |           64.55 |
| STEM            | Math                                       |                  26.33 |                   29    |                   23.33 |    32.67 |         26    |         28.33 |           28.33 |
| STEM            | Mechanical-Engineering                     |                  42.8  |                   33.3  |                   37.5  |    59.5  |         34.2  |         46.8  |           54.7  |

### KMMLU-HARD

#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  25.83 |                   27.08 |                   26.25 |    36.86 |         21.07 |         22.17 |           29.17 |
| HUMSS           |                  21.52 |                   20.21 |                   20.21 |    41.97 |         19.44 |         23.07 |           31.51 |
| Other           |                  24.82 |                   23.05 |                   23.88 |    40.29 |         22.22 |         26.48 |           29.59 |
| STEM            |                  28.18 |                   24.36 |                   24.64 |    39.55 |         20.91 |         26.27 |           32.18 |
| **Overall**     |                  25.34 |                   24    |                   24.03 |    39.45 |         20.97 |         24.46 |           30.56 |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  22    |                   29    |                   25    |    45    |         25    |         25    |           32    |
| Applied Science | Electronics-Engineering                    |                  34    |                   31    |                   26    |    42    |         22    |         29    |           41    |
| Applied Science | Energy-Management                          |                  23    |                   30    |                   27    |    38    |         22.45 |         27    |           37    |
| Applied Science | Environmental-Science                      |                  28    |                   26    |                   30    |    26.25 |         31.25 |         20    |           24    |
| Applied Science | Gas-Technology-and-Engineering             |                  30    |                   28    |                   23    |    35    |         13    |         23    |           28    |
| Applied Science | Geomatics                                  |                  23    |                   23    |                   29    |    34    |         22    |         22    |           24    |
| Applied Science | Industrial-Engineer                        |                  28    |                   30    |                   25    |    32    |         25    |         19    |           26    |
| Applied Science | Machine-Design-and-Manufacturing           |                  27    |                   24    |                   24    |    45    |         16.25 |         17    |           27    |
| Applied Science | Maritime-Engineering                       |                  26    |                   27    |                   28    |    32    |         21    |         19    |           26    |
| Applied Science | Nondestructive-Testing                     |                  26    |                   31    |                   25    |    36    |         14    |         22    |           23    |
| Applied Science | Railway-and-Automotive-Engineering         |                  20    |                   25    |                   26    |    32    |         18    |         17    |           24    |
| Applied Science | Telecommunications-and-Wireless-Technology |                  23    |                   21    |                   27    |    43    |         24    |         26    |           38    |
| HUMSS           | Accounting                                 |                  19.57 |                    8.7  |                   23.91 |    50    |         13.04 |         21.74 |           21.74 |
| HUMSS           | Criminal-Law                               |                  22    |                   20    |                   16    |    31    |         27    |         16    |           22    |
| HUMSS           | Economics                                  |                  21.43 |                   23.81 |                   14.29 |    52.38 |         26.19 |         26.19 |           38.1  |
| HUMSS           | Education                                  |                  21.74 |                   30.43 |                   21.74 |    56.52 |         17.39 |         43.48 |           34.78 |
| HUMSS           | Korean-History                             |                  15.91 |                   13.64 |                   27.27 |    40.91 |         18.18 |         18.18 |           27.27 |
| HUMSS           | Law                                        |                  29    |                   18    |                   17    |    40    |         15.85 |         20    |           28    |
| HUMSS           | Management                                 |                  22    |                   27    |                   28    |    42    |         22    |         26    |           38    |
| HUMSS           | Political-Science-and-Sociology            |                  22.22 |                   20    |                   14.44 |    53.33 |         23.33 |         25.56 |           38.89 |
| HUMSS           | Psychology                                 |                  15    |                   22    |                   19    |    44    |          7    |         20    |           32    |
| HUMSS           | Social-Welfare                             |                  27    |                   23    |                   17    |    45    |         24    |         32    |           47    |
| HUMSS           | Taxation                                   |                  16.67 |                   15.62 |                   27.08 |    28.12 |         17.71 |         18.75 |           17.71 |
| Other           | Agricultural-Sciences                      |                  27    |                   21    |                   18    |    38    |         17    |         23    |           28    |
| Other           | Construction                               |                  29    |                   23    |                   24    |    34    |         23    |         28    |           27    |
| Other           | Fashion                                    |                  21    |                   26    |                   28    |    31    |         29    |         23    |           20    |
| Other           | Food-Processing                            |                  24    |                   19    |                   19    |    38    |         19    |         21    |           26    |
| Other           | Health                                     |                   8.7  |                   13.04 |                   34.78 |    39.13 |         17.39 |         34.78 |           34.78 |
| Other           | Interior-Architecture-and-Design           |                  30    |                   28    |                   26    |    49    |         25    |         29    |           36.67 |
| Other           | Marketing                                  |                  32    |                   26    |                   32    |    54    |         22    |         39    |           46    |
| Other           | Patent                                     |                  15.69 |                   23.53 |                   17.65 |    47.06 |         37.25 |         25.49 |           25.49 |
| Other           | Public-Safety                              |                  24    |                   21    |                   26    |    31    |         17    |         19    |           25    |
| Other           | Real-Estate                                |                  23.6  |                   23.6  |                   26.97 |    39.33 |         19.1  |         20.22 |           32.58 |
| Other           | Refrigerating-Machinery                    |                  21    |                   22    |                   16    |    45    |         22    |         34    |           27    |
| STEM            | Biology                                    |                  22    |                   21    |                   24    |    46    |         13    |         27    |           26    |
| STEM            | Chemical-Engineering                       |                  32    |                   25    |                   23    |    37    |         20    |         21    |           34    |
| STEM            | Chemistry                                  |                  28    |                   30    |                   22    |    50    |         27    |         35    |           45    |
| STEM            | Civil-Engineering                          |                  19    |                   28    |                   22    |    38    |         13    |         23    |           29    |
| STEM            | Computer-Science                           |                  38    |                   26    |                   29    |    47    |         26    |         31    |           36    |
| STEM            | Ecology                                    |                  28    |                   15    |                   26    |    39    |         19    |         26    |           25    |
| STEM            | Electrical-Engineering                     |                  27    |                   27    |                   26    |    34    |         16    |         19    |           24    |
| STEM            | Information-Technology                     |                  29    |                   28    |                   27    |    43    |         28    |         35    |           44    |
| STEM            | Materials-Engineering                      |                  33    |                   23    |                   29    |    43    |         24    |         25    |           33    |
| STEM            | Math                                       |                  23    |                   15    |                   20    |    23    |         22    |         25    |           22    |
| STEM            | Mechanical-Engineering                     |                  31    |                   30    |                   23    |    35    |         22    |         22    |           36    |

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
   
```bash
python click_main.py

python haerae_main.py

python kmmlu_main.py
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