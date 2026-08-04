# Datasets

Full descriptions and paper/repo links for every benchmark supported by this suite. See
[../README.md](../README.md) for the quick summary table.

### CLIcK (Cultural and Linguistic Intelligence in Korean)
This dataset assesses Korean language proficiency in the subject areas of Korean Culture (History, Geography, Law, Politics, Society, Tradition, Economy, Pop culture) and Korean Language (Textual, Functional, Grammar). There are a total of 1,995 sample data in 11 categories. This dataset presents 4- or 5-choice multiple choice questions. Depending on the question, additional context is given.

- [Paper](https://arxiv.org/abs/2403.06412), [GitHub](https://github.com/rladmstn1714/CLIcK), [Hugging Face](https://huggingface.co/datasets/EunsuKim/CLIcK)

### HAE_RAE_BENCH 1.0
This dataset evaluates Korean language proficiency in the following 6 categories (General Knowledge, History, Loan Words, Rare Words, Reading Comprehension, Standard Nomenclature). Similar to CLiCK, the task is to solve multiple-choice questions, but no additional context. There are a total of 1,538 sample data in 6 categories.

- [Paper](https://arxiv.org/abs/2309.02706), [GitHub](https://github.com/HAE-RAE/HAE-RAE-BENCH), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0)

### KMMLU
The KMMLU dataset is a large-scale multi-task language understanding evaluation dataset in Korean. It is not a simple translation of the MMLU dataset, but rather data generated from Korean text, allowing us to evaluate how well LLM/SLM works in Korean. It consists of a total of 45 categories and 4 super categories, such as STEM, Applied Science, HUMSS, and Other. There are 35,030 test samples across the 45 categories.

- [Paper](https://arxiv.org/abs/2402.11548), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KMMLU)

### KMMLU-HARD
This dataset is an extended version of the KMMLU dataset, with more challenging questions. It is designed to further evaluate the limits of Korean NLP models and contains questions that require a particularly high level of comprehension and reasoning skills. There are 4,104 test samples (plus 225 dev samples used for few-shot prompting) across the same 45 categories.

- [Paper](https://arxiv.org/abs/2402.11548), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/KMMLU-HARD)

### KMMLU-Pro
KMMLU-Pro is a professional-licensure benchmark comprising 2,822 problems from official Korean National Professional Licensure (KNPL) exams, covering 15 licenses (e.g. lawyer, doctor, CPA, tax accountant) across 4 domains (Law, Tax & Accounting, Value Estimation, Medicine) and 63 subjects. Questions have 4 or 5 choices depending on the source exam.

- [Paper](https://arxiv.org/abs/2507.08924), [Hugging Face](https://huggingface.co/datasets/LGAI-EXAONE/KMMLU-Pro)

### HRM8K
HRM8K (HAE-RAE Math 8K) is a bilingual math reasoning benchmark for Korean and English, comprising 8,011 instances. It includes Korean School Math (KSM) with 1,428 challenging problems from Korean Olympiad and competition-level exams, and Prior Sets with 6,583 problems from existing English benchmarks (GSM8K, MATH, Omni-MATH, MMMLU). This dataset evaluates mathematical reasoning capabilities in both languages.

- [Paper](https://arxiv.org/abs/2501.02448), [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HRM8K)

### KoBALT-700
KoBALT (Korean Benchmark for Advanced Linguistic Tasks) is designed to evaluate LLMs on Korean linguistic phenomena. It consists of 700 expert-written multiple-choice questions (A-J, 10 choices) covering 24 fine-grained linguistic phenomena across 5 core domains: Syntax (300), Semantics (215), Pragmatics (81), Phonetics/Phonology (62), and Morphology (42). Questions are categorized into 3 difficulty levels (1: easy, 2: moderate, 3: hard).

- [Paper](https://arxiv.org/abs/2505.16125), [GitHub](https://github.com/snunlp/KoBALT), [Hugging Face](https://huggingface.co/datasets/snunlp/KoBALT-700)

### KorMedMCQA
KorMedMCQA is a Korean Medical Multiple-Choice Question Answering benchmark derived from professional healthcare licensing examinations conducted in Korea between 2012 and 2024. The dataset contains 7,469 questions from examinations for doctor (2,489 questions), nurse (1,751 questions), pharmacist (1,817 questions), and dentist (1,412 questions), covering a wide range of medical disciplines. This dataset presents 5-choice multiple choice questions with answers numbered 1-5.

- [Paper](https://arxiv.org/abs/2403.01469), [Hugging Face](https://huggingface.co/datasets/sean0042/KorMedMCQA)

### MuSR(Ko)
MuSR(Ko) is a Korean adaptation of MuSR (Multistep Soft Reasoning), evaluating multi-step reasoning over long synthetic narratives across 3 task types: murder mysteries (2-choice, 250 samples), object placements (4-choice, 250 samples), and team allocation (3-choice, 250 samples), for 750 samples total.

- [Hugging Face](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-MuSR)
