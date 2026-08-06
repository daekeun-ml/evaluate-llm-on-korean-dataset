# Korean LLM Benchmark Suite

Benchmark LLMs/SLMs on Korean-language proficiency, reasoning, and professional-domain knowledge
with minimal setup — multi-provider (Azure OpenAI, Amazon Bedrock, OpenAI-compatible/self-hosted,
Azure ML, Hugging Face), parallel batch evaluation, and ready-made leaderboard tables.

## 📋 Benchmarks

| Benchmark | What it tests | Size |
|---|---|---|
| [CLIcK](https://huggingface.co/datasets/EunsuKim/CLIcK) | Korean culture & language, 11 categories | 1,995 |
| [HAE-RAE Bench 1.0](https://huggingface.co/datasets/HAERAE-HUB/HAE_RAE_BENCH_1.0) | Korean knowledge, 6 categories | 1,538 |
| [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) | Massive multitask understanding, 45 categories | 35,030 |
| [KMMLU-HARD](https://huggingface.co/datasets/HAERAE-HUB/KMMLU-HARD) | Harder KMMLU subset | 4,104 |
| [KMMLU-Pro](https://huggingface.co/datasets/LGAI-EXAONE/KMMLU-Pro) | 14 professional-licensure exams (lawyer, CPA, doctor, ...) | 2,822 |
| [HRM8K](https://huggingface.co/datasets/HAERAE-HUB/HRM8K) | Bilingual (Ko/En) math reasoning | 8,011 |
| [KoBALT-700](https://huggingface.co/datasets/snunlp/KoBALT-700) | Advanced Korean linguistic phenomena, 3 difficulty levels | 700 |
| [KorMedMCQA](https://huggingface.co/datasets/sean0042/KorMedMCQA) | Medical licensing exams (doctor/nurse/pharmacist/dentist) | 7,469 |
| [MuSR(Ko)](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-MuSR) | Multi-step reasoning over long narratives, 3 task types | 750 |

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

## 🆕 What's New

- Aug 5, 2026: Added a **reasoning=max** column for **DeepSeek-V4-Flash-0731**, so the self-hosted
  model is now measured across all three of its reasoning levels (none / high / max). Its `high`
  and `max` levels land within about a point of each other on most benchmarks, so the extra
  deliberation `max` spends buys little here.

- Aug 4, 2026: Added **KMMLU-Pro** (2,822 professional-licensure questions across 14 licenses) and
  **MuSR(Ko)** (750 multi-step reasoning questions across murder mysteries / object placements /
  team allocation) benchmark datasets, with results for **GPT-5.6 (Sol/Terra/Luna)**,
  **Claude Sonnet 5**, **Claude Opus 5**, and **DeepSeek-V4-Flash-0731**.

Earlier updates: **[docs/CHANGELOG.md](docs/CHANGELOG.md)**

## 📈 Results

**Current round** (Aug 2026): GPT-5.6 Sol/Terra/Luna, Claude Sonnet 5, Claude Opus 5 (all
reasoning=medium), and DeepSeek-V4-Flash-0731 (self-hosted, reasoning=none/high/max — this model
exposes `low`/`high`/`max` only, with no `medium` level).

| Benchmark | Claude Opus 5 | Claude Sonnet 5 | GPT-5.6 Sol | GPT-5.6 Terra | GPT-5.6 Luna | DeepSeek-V4-Flash-0731 (max) | DeepSeek-V4-Flash-0731 (high) | DeepSeek-V4-Flash-0731 (none) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CLIcK | 95.84 | 92.08 | 95.50 | 92.24 | 91.53 | 90.78 | 90.63 | 80.25 |
| HAE-RAE | 95.84 | 92.00 | 94.64 | 92.85 | 93.17 | 92.98 | 91.87 | 84.92 |
| KoBALT-700 | 88.14 | 76.14 | 84.29 | 76.57 | 77.00 | 73.43 | 73.29 | 48.86 |
| KMMLU-HARD | 88.40 | 77.44 | 85.04 | 77.86 | 75.76 | 74.00 | 74.20 | 56.92 |
| KMMLU-Pro | 95.64 | 85.83 | 93.64 | 84.44 | 85.54 | 78.42 | 79.20 | 66.19 |
| MuSR(Ko) | 86.53 | 81.60 | 85.31 | 83.15 | 71.47 | 82.40 | 81.20 | 57.33 |

Reasoning models can exhaust their token budget mid-thought and return an empty response, which
silently drops those items from the accuracy denominator. Every number above is measured with a
budget large enough to avoid that (see [docs/RESULTS.md](docs/RESULTS.md) for details).

### ⚠️ Disclaimer

> These are personal benchmark runs, **not official results** from any model vendor. Treat them as a
> rough reference only.
>
> Scores vary with the system prompt, token budget, temperature, parsing rules, and provider-side
> model updates, so they will not match vendor-published numbers or other groups' evaluations.
> Single-run results also carry sampling noise, and multiple-choice parsing can misread an otherwise
> correct answer. Do not use these numbers for procurement decisions or published claims without
> reproducing them yourself.
>
> This repository is a personal side project. It is not affiliated with, endorsed by, or
> representative of the views of the author's employer or any model vendor.

- Full per-category/per-supercategory breakdowns, radar charts, and model-version details:
  **[docs/RESULTS.md](docs/RESULTS.md)**
- Older benchmark rounds (GPT-5.2, GPT-5.1, Nova 2, GPT-4.1, Phi, Llama, etc.):
  **[docs/PREVIOUS_RESULTS.md](docs/PREVIOUS_RESULTS.md)**
- Changelog: **[docs/CHANGELOG.md](docs/CHANGELOG.md)**

## 📚 References

BibTeX citations for every benchmark dataset: **[docs/REFERENCES.md](docs/REFERENCES.md)**
