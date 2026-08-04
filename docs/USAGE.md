# Usage

See [../README.md](../README.md) for the one-command quick start. This file covers local setup
details, manual per-benchmark CLI usage, all script arguments, and output format.

## Local Setup

Install the required packages via uv:

```bash
uv sync
```

To use Jupyter Notebook in VS Code or Cursor, choose one of the two methods below:
1. Click **Select Kernel** - **Python Environments**, and then select **.venv**.
<img src="../imgs/quick-start-01.png" width="100%"/>
<img src="../imgs/quick-start-02.png" width="50%"/>

2. Click **Python: Select Interpreter** with the shortcut **Ctrl + Shift + P (Windows/Linux)**, **Cmd + Shift + P (macOS)**, and then select **.venv**.
<img src="../imgs/quick-start-03.png" width="100%"/>

### GitHub Codespace
Start a new project by connecting to the Codespace. The environment required for hands-on work is
automatically configured through devcontainer, so you only need to run a Jupyter notebook.

## Configuration

Create a `.env` file (or multiple files under `env/` for parallel multi-model runs — see
`./run.sh`) with `MODEL_PROVIDER` plus that provider's credentials. Full provider reference and
`.env` examples: **[CONFIGURATION.md](CONFIGURATION.md)**.

## Running Evaluations

### Interactive Mode (Recommended)
Run the interactive script that guides you through the evaluation process. It runs one benchmark
across every `.env` file under `env/` in parallel:

```bash
./run.sh
```

The script will ask you to:
1. Select dataset (`1:CLIcK`, `2:HAE-RAE`, `3:KMMLU`, `4:KMMLU-HARD`, `5:HRM8K`, `6:KoBALT`, `7:KorMedMCQA`, `8:KMMLU-Pro`, `9:MuSR-Ko`)
2. Choose debug mode (`y/n`)
3. Set batch size (default: `4`)
4. Set max tokens (default: `128`)
5. Set temperature (default: `0.01`)
6. Set number of workers (default: `10`)

### Manual Mode
Run individual benchmarks directly against a single `.env` (or `DOTENV_PATH`):

```bash
# Example: CLIcK benchmark
DOTENV_PATH=env/.env.claude-opus-5 uv run python benchmarks/click_main.py \
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
# benchmarks/kmmlu_main.py       # --is_hard True for KMMLU-HARD, --num_shots for few-shot
# benchmarks/hrm8k_main.py       # --subset GSM8K|MATH|OMNI_MATH|MMMLU|KSM
# benchmarks/kobalt_main.py      # --levels 1 2 3
# benchmarks/kormedmcqa_main.py
# benchmarks/kmmlu_pro_main.py   # --licenses 변호사 의사 ...
# benchmarks/musr_ko_main.py     # --subsets murder_mysteries object_placements team_allocation
```

## Available Parameters

Common to every benchmark script:
```python
--is_debug              # Enable debug mode (default: True)
--num_debug_samples     # Number of samples in debug mode (default varies by script, usually 5-20)
--model_provider        # Provider: azureopenai, bedrock, bedrock_openai, openai, azureml, azureaifoundry, huggingface
--batch_size            # Batch size for processing (default: 10)
--max_retries           # Maximum retry attempts (default: 3)
--max_tokens            # Maximum tokens in response (default varies by script)
--temperature           # Sampling temperature (default: 0.01)
--template_type         # Prompt template type (default: basic)
--wait_time             # Wait time between requests on throttling (default: from WAIT_TIME env var)
--num_workers           # Number of parallel workers for processing (default: 4)
```

Benchmark-specific filters:
```python
--num_shots             # kmmlu_main.py: number of few-shot examples (default: 0)
--is_hard               # kmmlu_main.py: use KMMLU-HARD instead of KMMLU (default: False)
--categories            # click_main.py / kmmlu_main.py / haerae_main.py: filter by category
--subset                # hrm8k_main.py: GSM8K, MATH, OMNI_MATH, MMMLU, KSM
--levels                # kobalt_main.py: filter by difficulty (1, 2, 3)
--licenses              # kmmlu_pro_main.py: filter by license_name (e.g. 변호사 의사)
--subsets               # musr_ko_main.py: filter by subset (murder_mysteries, object_placements, team_allocation)
```

Reasoning is controlled via `.env` (not CLI flags) — see [CONFIGURATION.md](CONFIGURATION.md):
```ini
REASONING_ENABLED=true
REASONING_EFFORT=medium   # exact accepted values vary by provider — see CONFIGURATION.md
```

## Output

Evaluation results are saved as `results/[<Benchmark>] <MODEL_NAME>-<MODEL_VERSION>.csv`, with one
row per question (`answer`, `pred`, `response`, plus benchmark-specific category columns). Re-run
`evaluate.ipynb` / `evaluate-all.ipynb` (or `util/evaluate_helper.get_experiments_md`) to regenerate
the markdown leaderboard tables shown in [RESULTS.md](RESULTS.md).
