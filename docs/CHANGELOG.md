# Changelog

- Aug 4, 2026: Added **KMMLU-Pro** (2,822 professional-licensure questions across 14 licenses) and **MuSR(Ko)** (750 multi-step reasoning questions across murder mysteries / object placements / team allocation) benchmark datasets, with results for **GPT-5.6 (Sol/Terra/Luna)**, **Claude Sonnet 5**, **Claude Opus 5**, and **DeepSeek-V4-Flash-0731** (reasoning=none and reasoning=high). **Claude Opus 5** leads both: 95.11% on KMMLU-Pro and 86.53% on MuSR(Ko).

- Aug 4, 2026: Added **GPT-5.6 (Sol/Terra/Luna)**, **Claude Sonnet 5**, **Claude Opus 5** (all Amazon Bedrock, reasoning_effort=medium) and **DeepSeek-V4-Flash-0731** (self-hosted via vLLM, tested at both reasoning=none and reasoning=high) benchmark results on CLIcK, HAE-RAE, KoBALT-700, and KMMLU-HARD. **Claude Opus 5** leads on CLIcK (95.84%), HAE-RAE (95.84%), and KMMLU-HARD (87.79%); **GPT-5.6 Sol** leads on KoBALT-700 (84.29%). DeepSeek-V4-Flash-0731 improves substantially with reasoning enabled (e.g. KoBALT-700: 48.86% → 50.43%, KMMLU-HARD: 56.92% → 67.91%) but still trails the frontier reasoning models. Older per-model results (GPT-5.2, GPT-5.1, Nova 2, GPT-4.1, Phi, Llama, etc.) have moved to [PREVIOUS_RESULTS.md](PREVIOUS_RESULTS.md).

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
