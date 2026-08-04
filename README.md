# Korean LLM/SLM Evaluation Suite

Benchmark LLMs/SLMs on Korean-language proficiency, reasoning, and professional-domain knowledge
with minimal setup — multi-provider (Azure OpenAI, Amazon Bedrock, OpenAI-compatible/self-hosted,
Azure ML, Hugging Face), parallel batch evaluation, and ready-made leaderboard tables.

## 📋 Benchmarks

| Benchmark | What it tests | Size |
|---|---|---|
| [CLIcK](https://huggingface.co/datasets/EunsuKim/CLIcK) | Korean culture & language, 11 categories | 1,995 |
| [HAE-RAE Bench 1.0](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0) | Korean knowledge, 6 categories | 1,538 |
| [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) | Massive multitask understanding, 45 categories | — |
| [KMMLU-HARD](https://huggingface.co/datasets/HAERAE-HUB/KMMLU-HARD) | Harder KMMLU subset | — |
| [HRM8K](https://huggingface.co/datasets/HAERAE-HUB/HRM8K) | Bilingual (Ko/En) math reasoning | 8,011 |
| [KoBALT-700](https://huggingface.co/datasets/snunlp/KoBALT-700) | Advanced Korean linguistic phenomena, 3 difficulty levels | 700 |
| [KorMedMCQA](https://huggingface.co/datasets/sean0042/KorMedMCQA) | Medical licensing exams (doctor/nurse/pharmacist/dentist) | 7,469 |
| [KMMLU-Pro](https://huggingface.co/datasets/LGAI-EXAONE/KMMLU-Pro) (gated) | 14 professional-licensure exams (lawyer, CPA, doctor, ...) | 2,822 |
| [MuSR(Ko)](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-MuSR) (gated) | Multi-step reasoning over long narratives, 3 task types | 750 |

Full dataset descriptions and paper links: [docs/DATASETS.md](docs/DATASETS.md).

## 🚀 Quick Start

```bash
uv sync
cp .env.sample .env   # fill in MODEL_PROVIDER + that provider's credentials
./run.sh              # interactive: pick a benchmark, runs every env/.env* file in parallel
```

- Full provider setup (Azure OpenAI, Bedrock incl. Claude Sonnet/Opus 5 and GPT-5.6, self-hosted
  vLLM, etc.): **[docs/CONFIGURATION.md](docs/CONFIGURATION.md)**
- Manual per-benchmark CLI usage, all script arguments, output format: **[docs/USAGE.md](docs/USAGE.md)**
- GitHub Codespaces: connect to this repo's Codespace — the devcontainer sets up everything, then
  just open a notebook.

## 📈 Results

**Current round** (Aug 2026): GPT-5.6 Sol/Terra/Luna, Claude Sonnet 5, Claude Opus 5 (all
reasoning=medium), and DeepSeek-V4-Flash-0731 (self-hosted, reasoning=none and reasoning=high).

| Benchmark | Claude Opus 5 | Claude Sonnet 5 | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna | DeepSeek-V4-Flash-0731 (high) | DeepSeek-V4-Flash-0731 (none) |
|---|---:|---:|---:|---:|---:|---:|---:|
| CLIcK | **95.84** | 91.53 | 95.50 | 92.24 | 91.53 | 85.46 | 80.25 |
| HAE-RAE | **95.84** | 92.00 | 94.64 | 92.85 | 93.17 | 89.66 | 84.92 |
| KoBALT-700 | 83.71 | 67.43 | **84.29** | 76.57 | 77.00 | 50.43 | 48.86 |
| KMMLU-HARD | **87.79** | 76.75 | 85.04 | 77.86 | 75.76 | 67.91 | 56.92 |
| KMMLU-Pro | **95.11** | 85.51 | 93.64 | 84.44 | 85.54 | 69.35 | 66.19 |
| MuSR(Ko) | **86.53** | 81.60 | 85.31 | 83.15 | 71.47 | 65.33 | 57.33 |

Claude Opus 5 leads 5 of 6 benchmarks; GPT-5.6 Sol leads KoBALT-700. DeepSeek-V4-Flash-0731
improves substantially with reasoning enabled but still trails the frontier reasoning models.

- Full per-category/per-supercategory breakdowns, radar charts, and model-version details:
  **[docs/RESULTS.md](docs/RESULTS.md)**
- Older benchmark rounds (GPT-5.2, GPT-5.1, Nova 2, GPT-4.1, Phi, Llama, etc.):
  **[docs/PREVIOUS_RESULTS.md](docs/PREVIOUS_RESULTS.md)** and **[docs/DETAILED_RESULTS.md](docs/DETAILED_RESULTS.md)**
- Changelog: **[docs/CHANGELOG.md](docs/CHANGELOG.md)**

## ⚙️ Implementation

The code skeleton is based on https://github.com/corca-ai/evaluating-gpt-4o-on-CLIcK, with:

- **Multi-provider support**: Azure OpenAI, AWS Bedrock (native + Bedrock-hosted OpenAI models),
  OpenAI (incl. self-hosted OpenAI-compatible endpoints such as vLLM), Azure ML, Azure AI Foundry,
  Hugging Face
- **Parallel processing**: chunk-based multiprocessing with configurable concurrency
- **Robust error handling**: content filtering, rate limiting, throttling retries
- **Reasoning-aware prompts and parsing**: configurable effort levels per provider, parsers that
  strip reasoning/thinking content before extracting the final answer

## 📚 References

BibTeX citations for every benchmark dataset: **[docs/REFERENCES.md](docs/REFERENCES.md)**
