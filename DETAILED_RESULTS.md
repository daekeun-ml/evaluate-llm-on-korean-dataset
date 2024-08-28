## Detailed Results

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

### HAERAE

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
| Applied Science |                  45.15 |                   35.8  |                           31.68 |                   37.03 |    61.52 |         49.29 |         55.98 |           38.47 |
| HUMSS           |                  49.75 |                   31.56 |                           26.47 |                   37.29 |    69.45 |         56.59 |         63    |           40.9  |
| Other           |                  47.24 |                   35.45 |                           31.01 |                   39.15 |    63.79 |         52.35 |         57.53 |           40.19 |
| STEM            |                  49.08 |                   38.54 |                           31.9  |                   40.42 |    65.16 |         54.74 |         60.84 |           42.24 |
| **Overall**     |                  47.43 |                   35.87 |                           30.82 |                   38.54 |    64.26 |         52.63 |         58.75 |           40.3  |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  47.9  |                   34.9  |                           30.1  |                   36.6  |    69.8  |         50.4  |         61.92 |           39    |
| Applied Science | Electronics-Engineering                    |                  55.4  |                   42.7  |                           33.9  |                   42.9  |    73.2  |         64.5  |         70.2  |           47.1  |
| Applied Science | Energy-Management                          |                  35.7  |                   27.4  |                           26.9  |                   29.6  |    50.3  |         39.5  |         43.6  |           33.9  |
| Applied Science | Environmental-Science                      |                  36    |                   33.8  |                           30.1  |                   30.2  |    45.82 |         36.5  |         42.7  |           30.51 |
| Applied Science | Gas-Technology-and-Engineering             |                  39.7  |                   31.7  |                           30.8  |                   31.7  |    50.7  |         44.6  |         48.3  |           35    |
| Applied Science | Geomatics                                  |                  42.7  |                   37.5  |                           33.6  |                   36.1  |    56.4  |         43.7  |         47.3  |           35.7  |
| Applied Science | Industrial-Engineer                        |                  48.6  |                   40.5  |                           32.7  |                   41.9  |    61.7  |         53.1  |         57    |           41.12 |
| Applied Science | Machine-Design-and-Manufacturing           |                  46.2  |                   34.6  |                           29.5  |                   35.5  |    68.4  |         53    |         61    |           37.9  |
| Applied Science | Maritime-Engineering                       |                  48    |                   34.67 |                           30.67 |                   40    |    67    |         52.5  |         60.17 |           42.67 |
| Applied Science | Nondestructive-Testing                     |                  48.5  |                   34.7  |                           31.3  |                   39.2  |    65.2  |         48    |         59.7  |           35.8  |
| Applied Science | Railway-and-Automotive-Engineering         |                  37.8  |                   30.3  |                           31.3  |                   33.2  |    53.9  |         40.9  |         48.6  |           32.5  |
| Applied Science | Telecommunications-and-Wireless-Technology |                  56.4  |                   46.4  |                           38.9  |                   48.7  |    77.8  |         66.1  |         73    |           52.24 |
| HUMSS           | Accounting                                 |                  47    |                   34    |                           22    |                   32    |    72    |         48    |         59    |           30    |
| HUMSS           | Criminal-Law                               |                  31.5  |                   25    |                           18.5  |                   30    |    52.5  |         37    |         46.5  |           40.5  |
| HUMSS           | Economics                                  |                  53.08 |                   31.54 |                           24.62 |                   31.54 |    74.62 |         64.62 |         65.38 |           43.85 |
| HUMSS           | Education                                  |                  64    |                   37    |                           31    |                   44    |    83    |         70    |         69    |           43    |
| HUMSS           | Korean-History                             |                  32    |                   33    |                           16    |                   34    |    56    |         32    |         41    |           26    |
| HUMSS           | Law                                        |                  43.4  |                   32.7  |                           26.6  |                   36    |    65.8  |         50.6  |         56.7  |           38.23 |
| HUMSS           | Management                                 |                  57    |                   34.2  |                           28.3  |                   39.7  |    74.2  |         64.2  |         70.7  |           47.9  |
| HUMSS           | Political-Science-and-Sociology            |                  58.33 |                   36.67 |                           26.33 |                   43.33 |    79.67 |         62.33 |         72.67 |           46.67 |
| HUMSS           | Psychology                                 |                  44.7  |                   27.6  |                           23.7  |                   35    |    66.4  |         50.4  |         57.3  |           32.8  |
| HUMSS           | Social-Welfare                             |                  58.5  |                   31.8  |                           29.6  |                   40.3  |    74.5  |         67.7  |         73.2  |           46.4  |
| HUMSS           | Taxation                                   |                  33    |                   25.5  |                           29.5  |                   31    |    51    |         39.5  |         44    |           33.5  |
| Other           | Agricultural-Sciences                      |                  37.8  |                   32.3  |                           30.6  |                   31.4  |    53.9  |         41.8  |         47.58 |           30.1  |
| Other           | Construction                               |                  37.5  |                   33.8  |                           32.4  |                   32.4  |    50.7  |         41.8  |         46    |           33.2  |
| Other           | Fashion                                    |                  47.4  |                   35    |                           30.8  |                   41.5  |    65.8  |         51.1  |         58.28 |           39.7  |
| Other           | Food-Processing                            |                  45.8  |                   31.7  |                           30.9  |                   39.2  |    64.9  |         51.7  |         57.4  |           37.3  |
| Other           | Health                                     |                  58    |                   44    |                           29    |                   44    |    80    |         69    |         70    |           50    |
| Other           | Interior-Architecture-and-Design           |                  58    |                   40.9  |                           34.3  |                   44    |    77.6  |         64    |         71.1  |           48.2  |
| Other           | Marketing                                  |                  73    |                   48.7  |                           31.3  |                   63.3  |    88.9  |         83.1  |         86.26 |           63.6  |
| Other           | Patent                                     |                  45    |                   24    |                           25    |                   26    |    52    |         33    |         46    |           40    |
| Other           | Public-Safety                              |                  41.2  |                   33.2  |                           32    |                   34.2  |    53.2  |         44.3  |         48.2  |           36.2  |
| Other           | Real-Estate                                |                  47    |                   31    |                           23    |                   32.5  |    64.5  |         49    |         56.5  |           38    |
| Other           | Refrigerating-Machinery                    |                  36.4  |                   29.2  |                           28.2  |                   29.4  |    54.7  |         41.9  |         45.7  |           32.7  |
| STEM            | Biology                                    |                  39.9  |                   29.6  |                           27.2  |                   34    |    63.1  |         45.5  |         52.83 |           31.84 |
| STEM            | Chemical-Engineering                       |                  46.9  |                   36.3  |                           29    |                   35.7  |    65.1  |         55.8  |         62.6  |           38.5  |
| STEM            | Chemistry                                  |                  51.17 |                   36.83 |                           28.33 |                   36.17 |    68.67 |         57.33 |         64.33 |           39.67 |
| STEM            | Civil-Engineering                          |                  43.1  |                   33.7  |                           32.1  |                   36    |    54.3  |         46.9  |         50.3  |           38.3  |
| STEM            | Computer-Science                           |                  73.8  |                   56.9  |                           40.7  |                   60.4  |    88.2  |         80.1  |         84.8  |           65.7  |
| STEM            | Ecology                                    |                  48.8  |                   41.6  |                           33.9  |                   41.6  |    64.4  |         54.3  |         60    |           42.9  |
| STEM            | Electrical-Engineering                     |                  39    |                   32.6  |                           31    |                   32.1  |    46    |         38.5  |         44.1  |           31.7  |
| STEM            | Information-Technology                     |                  66.1  |                   52.1  |                           39.4  |                   57.1  |    83.6  |         78.4  |         81.2  |           63.78 |
| STEM            | Materials-Engineering                      |                  46.9  |                   34.6  |                           29.2  |                   37.1  |    69.4  |         52.1  |         64.55 |           39.69 |
| STEM            | Math                                       |                  26.33 |                   29    |                           25.67 |                   23.33 |    32.67 |         30    |         28.67 |           26.33 |
| STEM            | Mechanical-Engineering                     |                  42.8  |                   33.3  |                           28.6  |                   37.5  |    60    |         46.9  |         54.7  |           34.2  |

### KMMLU (5shot)

#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  45.9  |                   37.42 |                           29.98 |                   19.24 |    61.47 |         48.66 |         56.85 |           40.22 |
| HUMSS           |                  49.18 |                   34.72 |                           27.27 |                   22.5  |    68.79 |         55.95 |         63.68 |           43.35 |
| Other           |                  48.43 |                   37.04 |                           30.76 |                   20.95 |    64.21 |         51.1  |         57.85 |           41.92 |
| STEM            |                  49.21 |                   38.9  |                           30.73 |                   19.55 |    65.28 |         53.29 |         61.08 |           44.43 |
| **Overall**     |                  47.92 |                   37.35 |                           29.98 |                   20.21 |    64.28 |         51.62 |         59.29 |           42.28 |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  46.6  |                   34.3  |                           33.8  |                   17.4  |    70.8  |         50.6  |         61.9  |           40.1  |
| Applied Science | Electronics-Engineering                    |                  53.1  |                   46.9  |                           37.3  |                   18.6  |    72.3  |         63.5  |         72.7  |           50.6  |
| Applied Science | Energy-Management                          |                  34.7  |                   29.4  |                           25.3  |                   21.2  |    52.2  |         38.4  |         44.8  |           32.3  |
| Applied Science | Environmental-Science                      |                  34.6  |                   33.3  |                           22.7  |                   11.2  |    48.2  |         36.5  |         40.9  |           32.8  |
| Applied Science | Gas-Technology-and-Engineering             |                  40.4  |                   30.3  |                           31.9  |                   15.5  |    49.9  |         37.9  |         47.6  |           34.4  |
| Applied Science | Geomatics                                  |                  46.9  |                   37.3  |                           33.3  |                   23    |    48.8  |         39.9  |         49.7  |           37.6  |
| Applied Science | Industrial-Engineer                        |                  48.5  |                   41.2  |                           35.4  |                    4.3  |    64    |         52.5  |         55.5  |           39.5  |
| Applied Science | Machine-Design-and-Manufacturing           |                  48.9  |                   37.5  |                           29.9  |                   22.1  |    68.4  |         54.4  |         64    |           44.3  |
| Applied Science | Maritime-Engineering                       |                  47.67 |                   36.5  |                           27.33 |                   16.83 |    69.5  |         53.33 |         65.17 |           46.33 |
| Applied Science | Nondestructive-Testing                     |                  50.1  |                   40.7  |                           22.6  |                   26.7  |    64.7  |         51.4  |         59.9  |           41.1  |
| Applied Science | Railway-and-Automotive-Engineering         |                  40.2  |                   32.8  |                           27.1  |                   19.1  |    55.4  |         42.2  |         49.2  |           35.5  |
| Applied Science | Telecommunications-and-Wireless-Technology |                  59.8  |                   48.5  |                           32.1  |                   34    |    76.7  |         65.2  |         74.2  |           50.5  |
| HUMSS           | Accounting                                 |                  51    |                   36    |                           25    |                   15    |    67    |         46    |         63    |           37    |
| HUMSS           | Criminal-Law                               |                  28.5  |                   25    |                           26.5  |                   14    |    51.5  |         37.5  |         46    |           38.5  |
| HUMSS           | Economics                                  |                  51.54 |                   37.69 |                           29.23 |                   23.08 |    83.08 |         61.54 |         72.31 |           39.23 |
| HUMSS           | Education                                  |                  58    |                   38    |                           26    |                   20    |    86    |         69    |         76    |           48    |
| HUMSS           | Korean-History                             |                  30    |                   33    |                           29    |                   12    |    50    |         31    |         33    |           34    |
| HUMSS           | Law                                        |                  43.6  |                   32.9  |                           26    |                   20.9  |    64.7  |         51    |         55.1  |           40.6  |
| HUMSS           | Management                                 |                  54.6  |                   36.6  |                           27.2  |                   26.9  |    70.1  |         61.9  |         71.8  |           50.5  |
| HUMSS           | Political-Science-and-Sociology            |                  50.67 |                   30.67 |                           29.67 |                   15.33 |    76.67 |         59.67 |         72.33 |           46.67 |
| HUMSS           | Psychology                                 |                  46.2  |                   33.2  |                           24.7  |                   19.4  |    66.9  |         51.2  |         57.3  |           36    |
| HUMSS           | Social-Welfare                             |                  60.8  |                   39.4  |                           31.1  |                   27.9  |    77.4  |         67.4  |         76    |           49.9  |
| HUMSS           | Taxation                                   |                  28    |                   31    |                           24.5  |                   26    |    47    |         37.5  |         45    |           33.5  |
| Other           | Agricultural-Sciences                      |                  38.1  |                   32.9  |                           25.1  |                   16.7  |    56.7  |         41.4  |         48.1  |           33.8  |
| Other           | Construction                               |                  38.5  |                   31.7  |                           33    |                    7.7  |    50.4  |         39.2  |         45    |           32.8  |
| Other           | Fashion                                    |                  49.4  |                   37.1  |                           31.5  |                   16.7  |    68.2  |         52.9  |         60.7  |           41.8  |
| Other           | Food-Processing                            |                  47.1  |                   34.7  |                           32.3  |                   24.3  |    64    |         47.8  |         57.5  |           38.3  |
| Other           | Health                                     |                  54    |                   43    |                           31    |                    2    |    80    |         68    |         73    |           53    |
| Other           | Interior-Architecture-and-Design           |                  57.9  |                   43    |                           34.9  |                   26.6  |    78.8  |         64.5  |         72.3  |           50.8  |
| Other           | Marketing                                  |                  76.4  |                   58.9  |                           32.9  |                   22.2  |    89.2  |         83.7  |         86.5  |           70.2  |
| Other           | Patent                                     |                  32    |                   32    |                           24    |                    6    |    51    |         33    |         47    |           34    |
| Other           | Public-Safety                              |                  43.1  |                   32.6  |                           28.4  |                   30.8  |    53.2  |         41.5  |         46.6  |           35.2  |
| Other           | Real-Estate                                |                  42    |                   34    |                           24.5  |                   26    |    66    |         43.5  |         54    |           40    |
| Other           | Refrigerating-Machinery                    |                  39.3  |                   25.9  |                           29.9  |                   25    |    52.6  |         39.4  |         46.4  |           32.5  |
| STEM            | Biology                                    |                  40.2  |                   31.3  |                           26.8  |                   13.9  |    63.6  |         43.9  |         54.4  |           32.1  |
| STEM            | Chemical-Engineering                       |                  44.6  |                   37.6  |                           24.4  |                   20.2  |    66.3  |         54.1  |         63.5  |           43.1  |
| STEM            | Chemistry                                  |                  49.33 |                   33.5  |                           30    |                    9.67 |    69.17 |         57.33 |         64.83 |           41.5  |
| STEM            | Civil-Engineering                          |                  45.1  |                   34.6  |                           22.2  |                    9.1  |    53.7  |         44.8  |         51.3  |           39.5  |
| STEM            | Computer-Science                           |                  67.6  |                   56.7  |                           42.7  |                   29.3  |    88.1  |         77.5  |         83.3  |           66.6  |
| STEM            | Ecology                                    |                  52    |                   41.9  |                           31.3  |                    8    |    58.1  |         52.8  |         57.7  |           45.8  |
| STEM            | Electrical-Engineering                     |                  40.3  |                   33.3  |                           32.2  |                   21.8  |    45.4  |         35.7  |         43.5  |           33.7  |
| STEM            | Information-Technology                     |                  68.3  |                   52.7  |                           38.1  |                   28.2  |    84.4  |         77.3  |         82.3  |           66.2  |
| STEM            | Materials-Engineering                      |                  48.5  |                   33.7  |                           30.7  |                   28.3  |    72.7  |         53.2  |         64.4  |           42    |
| STEM            | Math                                       |                  25.33 |                   28.33 |                           26.33 |                   26.67 |    30    |         27.67 |         34.67 |           25.33 |
| STEM            | Mechanical-Engineering                     |                  43.4  |                   34.7  |                           29.9  |                   20.9  |    63.5  |         45.6  |         55    |           38.4  |

### KMMLU-HARD

#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  25.83 |                   27.08 |                           26.17 |                   26.25 |    37.12 |         22.25 |         29.17 |           21.07 |
| HUMSS           |                  21.52 |                   20.21 |                           24.38 |                   20.21 |    41.97 |         23.31 |         31.51 |           19.44 |
| Other           |                  24.82 |                   23.05 |                           24.82 |                   23.88 |    40.39 |         26.48 |         29.59 |           22.22 |
| STEM            |                  28.18 |                   24.36 |                           26.91 |                   24.64 |    39.82 |         26.36 |         32.18 |           20.91 |
| **Overall**     |                  25.34 |                   24    |                           25.68 |                   24.03 |    39.62 |         24.56 |         30.56 |           20.97 |

#### Accuracy by category
| supercategory   | category                                   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------------------------------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Aviation-Engineering-and-Maintenance       |                  22    |                   29    |                           24    |                   25    |    45    |         25    |         32    |           25    |
| Applied Science | Electronics-Engineering                    |                  34    |                   31    |                           23    |                   26    |    42    |         29    |         41    |           22    |
| Applied Science | Energy-Management                          |                  23    |                   30    |                           22    |                   27    |    40    |         27    |         37    |           22.45 |
| Applied Science | Environmental-Science                      |                  28    |                   26    |                           36    |                   30    |    27.5  |         20    |         24    |           31.25 |
| Applied Science | Gas-Technology-and-Engineering             |                  30    |                   28    |                           24    |                   23    |    35    |         23    |         28    |           13    |
| Applied Science | Geomatics                                  |                  23    |                   23    |                           31    |                   29    |    34    |         22    |         24    |           22    |
| Applied Science | Industrial-Engineer                        |                  28    |                   30    |                           32    |                   25    |    32    |         19    |         26    |           25    |
| Applied Science | Machine-Design-and-Manufacturing           |                  27    |                   24    |                           23    |                   24    |    45    |         17    |         27    |           16.25 |
| Applied Science | Maritime-Engineering                       |                  26    |                   27    |                           25    |                   28    |    32    |         19    |         26    |           21    |
| Applied Science | Nondestructive-Testing                     |                  26    |                   31    |                           19    |                   25    |    36    |         23    |         23    |           14    |
| Applied Science | Railway-and-Automotive-Engineering         |                  20    |                   25    |                           28    |                   26    |    32    |         17    |         24    |           18    |
| Applied Science | Telecommunications-and-Wireless-Technology |                  23    |                   21    |                           27    |                   27    |    43    |         26    |         38    |           24    |
| HUMSS           | Accounting                                 |                  19.57 |                    8.7  |                           17.39 |                   23.91 |    50    |         21.74 |         21.74 |           13.04 |
| HUMSS           | Criminal-Law                               |                  22    |                   20    |                           24    |                   16    |    31    |         16    |         22    |           27    |
| HUMSS           | Economics                                  |                  21.43 |                   23.81 |                           26.19 |                   14.29 |    52.38 |         26.19 |         38.1  |           26.19 |
| HUMSS           | Education                                  |                  21.74 |                   30.43 |                           39.13 |                   21.74 |    56.52 |         43.48 |         34.78 |           17.39 |
| HUMSS           | Korean-History                             |                  15.91 |                   13.64 |                           15.91 |                   27.27 |    40.91 |         18.18 |         27.27 |           18.18 |
| HUMSS           | Law                                        |                  29    |                   18    |                           27    |                   17    |    40    |         20    |         28    |           15.85 |
| HUMSS           | Management                                 |                  22    |                   27    |                           20    |                   28    |    42    |         26    |         38    |           22    |
| HUMSS           | Political-Science-and-Sociology            |                  22.22 |                   20    |                           21.11 |                   14.44 |    53.33 |         27.78 |         38.89 |           23.33 |
| HUMSS           | Psychology                                 |                  15    |                   22    |                           22    |                   19    |    44    |         20    |         32    |            7    |
| HUMSS           | Social-Welfare                             |                  27    |                   23    |                           29    |                   17    |    45    |         32    |         47    |           24    |
| HUMSS           | Taxation                                   |                  16.67 |                   15.62 |                           30.21 |                   27.08 |    28.12 |         18.75 |         17.71 |           17.71 |
| Other           | Agricultural-Sciences                      |                  27    |                   21    |                           28    |                   18    |    38    |         23    |         28    |           17    |
| Other           | Construction                               |                  29    |                   23    |                           28    |                   24    |    35    |         28    |         27    |           23    |
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
| STEM            | Chemical-Engineering                       |                  32    |                   25    |                           38    |                   23    |    38    |         21    |         34    |           20    |
| STEM            | Chemistry                                  |                  28    |                   30    |                           26    |                   22    |    50    |         35    |         45    |           27    |
| STEM            | Civil-Engineering                          |                  19    |                   28    |                           25    |                   22    |    38    |         23    |         29    |           13    |
| STEM            | Computer-Science                           |                  38    |                   26    |                           27    |                   29    |    47    |         31    |         36    |           26    |
| STEM            | Ecology                                    |                  28    |                   15    |                           26    |                   26    |    39    |         26    |         25    |           19    |
| STEM            | Electrical-Engineering                     |                  27    |                   27    |                           31    |                   26    |    34    |         19    |         24    |           16    |
| STEM            | Information-Technology                     |                  29    |                   28    |                           24    |                   27    |    43    |         35    |         44    |           28    |
| STEM            | Materials-Engineering                      |                  33    |                   23    |                           27    |                   29    |    43    |         25    |         33    |           24    |
| STEM            | Math                                       |                  23    |                   15    |                           22    |                   20    |    23    |         26    |         22    |           22    |
| STEM            | Mechanical-Engineering                     |                  31    |                   30    |                           27    |                   23    |    37    |         22    |         36    |           22    |

### KMMLU-HARD (5shot)

#### Accuracy by supercategory
| supercategory   |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science |                  21    |                   25    |                           29    |                   12    |    31    |         21    |         25    |           20    |
| HUMSS           |                  22.88 |                   21.89 |                           19.92 |                   14    |    43.98 |         23.47 |         33.53 |           19.53 |
| Other           |                  25.13 |                   23.26 |                           27.27 |                   12.83 |    39.84 |         28.34 |         29.68 |           23.22 |
| STEM            |                  21.75 |                   20.5  |                           25.25 |                   12.75 |    40.25 |         23.25 |         27.25 |           19.75 |
| **Overall**     |                  25.66 |                   24.76 |                           25.73 |                   15.81 |    40.94 |         24.63 |         31.12 |           21.19 |

#### Accuracy by category
| supercategory   | category     |   Phi-3.5-MoE-instruct |   Phi-3.5-mini-instruct |   Phi-3-mini-128k-instruct-June |   Llama-3.1-8B-Instruct |   GPT-4o |   GPT-4o-mini |   GPT-4-turbo |   GPT-3.5-turbo |
|:----------------|:-------------|-----------------------:|------------------------:|--------------------------------:|------------------------:|---------:|--------------:|--------------:|----------------:|
| Applied Science | Geomatics    |                  21    |                   25    |                           29    |                   12    |    31    |         21    |         25    |           20    |
| HUMSS           | Accounting   |                  21.74 |                   15.22 |                           10.87 |                   13.04 |    52.17 |         23.91 |         45.65 |           19.57 |
| HUMSS           | Economics    |                  21.43 |                   26.19 |                           26.19 |                   30.95 |    57.14 |         23.81 |         45.24 |           23.81 |
| HUMSS           | Education    |                  17.39 |                   13.04 |                           26.09 |                    8.7  |    60.87 |         30.43 |         39.13 |           21.74 |
| HUMSS           | Law          |                  23    |                   24    |                           20    |                    6    |    41    |         26    |         28    |           20    |
| HUMSS           | Management   |                  21    |                   31    |                           20    |                   15    |    47    |         29    |         41    |           26    |
| HUMSS           | Psychology   |                  24    |                   21    |                           13    |                   15    |    46    |         19    |         36    |           13    |
| HUMSS           | Taxation     |                  26.04 |                   14.58 |                           27.08 |                   14.58 |    28.12 |         17.71 |         16.67 |           16.67 |
| Other           | Construction |                  20    |                   18    |                           31    |                   15    |    30    |         26    |         26    |           17    |
| Other           | Fashion      |                  30    |                   28    |                           30    |                   11    |    36    |         26    |         23    |           26    |
| Other           | Health       |                   8.7  |                    4.35 |                           26.09 |                    0    |    47.83 |         39.13 |         39.13 |           21.74 |
| Other           | Marketing    |                  29    |                   32    |                           23    |                   15    |    53    |         34    |         43    |           27    |
| Other           | Patent       |                  25.49 |                   15.69 |                           23.53 |                   13.73 |    37.25 |         21.57 |         19.61 |           14    |
| STEM            | Biology      |                  20    |                   23    |                           23    |                   11    |    49    |         22    |         27    |           31    |
| STEM            | Chemistry    |                  23    |                   23    |                           26    |                   12    |    54    |         36    |         43    |           14    |
| STEM            | Ecology      |                  23    |                   23    |                           37    |                    7    |    30    |         23    |         15    |           20    |
| STEM            | Math         |                  21    |                   13    |                           15    |                   21    |    28    |         12    |         24    |          nan    |