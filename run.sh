#!/bin/bash

# Get project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$PROJECT_ROOT"

# 동적으로 env 폴더에서 .env 파일들 찾기
env_files=(env/.env*)
if [ ! -e "${env_files[0]}" ]; then
    echo "Error: env 폴더에 .env 파일이 없습니다."
    echo "env 폴더를 만들고 .env 파일들을 추가해주세요."
    echo "예: mkdir env && cp .env.sample env/.env.model1"
    exit 1
fi

### Parallel execution version of run_all.sh with resume capability

# Ask user for dataset selection
read -p "[Q1] 평가할 데이터셋을 선택하세요 (1:CLIcK, 2:HAE-RAE, 3:KMMLU, 4:KMMLU-HARD, 5:HRM8K, 6:KoBALT, 7:KorMedMCQA, 8:KMMLU-Pro, 9:MuSR-Ko, 기본값: 1): " dataset_choice
dataset_choice=${dataset_choice:-1}

case "$dataset_choice" in
    1) benchmark="click" ;;
    2) benchmark="haerae" ;;
    3) benchmark="kmmlu" ;;
    4) benchmark="kmmlu-hard" ;;
    5) benchmark="hrm8k" ;;
    6) benchmark="kobalt" ;;
    7) benchmark="kormedmcqa" ;;
    8) benchmark="kmmlu-pro" ;;
    9) benchmark="musr-ko" ;;
    *)
        echo "잘못된 선택입니다. 기본값(CLIcK)으로 실행합니다."
        benchmark="click"
        ;;
esac

# Ask user for debug mode
read -p "[Q2] 디버그 모드로 실행하시겠습니까? (y/n, 기본값: y): " debug_choice
debug_choice=${debug_choice:-y}
if [[ "$debug_choice" =~ ^[Yy]$ ]]; then
    is_debug=True
    num_debug_samples=20
else
    is_debug=False
    num_debug_samples=0
fi

# Ask user for batch size
read -p "[Q3] Batch size를 입력하세요 (기본값: 4): " batch_input
batch_size=${batch_input:-4}

# Ask user for max tokens
read -p "[Q4] Max tokens를 입력하세요 (기본값: 128): " tokens_input
max_tokens=${tokens_input:-128}

# Ask user for temperature
read -p "[Q5] Temperature를 입력하세요 (기본값: 0.01): " temp_input
temperature=${temp_input:-0.01}

# Ask user for num workers
read -p "[Q6] Num workers를 입력하세요 (기본값: 10): " workers_input
num_workers=${workers_input:-10}

# 파일 개수에 따라 max_parallel_jobs 설정
max_parallel_jobs=${#env_files[@]}
template_type=chat
categories=""  #별도로 실행할 카테고리를 넣으려면 여기에 카테고리명 입력, 기존의 데이터는 삭제되므로 주의 필요

echo "Found the following .env files:"
for env_file in "${env_files[@]}"; do
    echo "$env_file"
done

# 함수: 단일 모델의 모든 벤치마크 실행
run_model() {
    local env_file=$1
    echo "Starting evaluation for $env_file"
    
    # 공통 arguments 구성
    local common_args="--is_debug $is_debug --batch_size $batch_size --max_tokens $max_tokens --temperature $temperature --template_type basic --num_debug_samples $num_debug_samples --num_workers $num_workers"
    [[ -n "$categories" ]] && common_args="$common_args --categories $categories"
    
    case "$benchmark" in
        click)
            DOTENV_PATH="$env_file" uv run python benchmarks/click_main.py $common_args
            ;;
        haerae)
            DOTENV_PATH="$env_file" uv run python benchmarks/haerae_main.py $common_args
            ;;
        kmmlu)
            DOTENV_PATH="$env_file" uv run python benchmarks/kmmlu_main.py $common_args --is_hard False --num_shots 0
            ;;
        kmmlu-hard)
            DOTENV_PATH="$env_file" uv run python benchmarks/kmmlu_main.py $common_args --is_hard True --num_shots 0
            ;;
        hrm8k)
            DOTENV_PATH="$env_file" uv run python benchmarks/hrm8k_main.py $common_args
            ;;
        kobalt)
            DOTENV_PATH="$env_file" uv run python benchmarks/kobalt_main.py $common_args
            ;;
        kormedmcqa)
            DOTENV_PATH="$env_file" uv run python benchmarks/kormedmcqa_main.py $common_args
            ;;
        kmmlu-pro)
            DOTENV_PATH="$env_file" uv run python benchmarks/kmmlu_pro_main.py $common_args
            ;;
        musr-ko)
            DOTENV_PATH="$env_file" uv run python benchmarks/musr_ko_main.py $common_args
            ;;
        *)
            echo "Invalid benchmark: $benchmark"
            echo "Usage: ./scripts/run_debug.sh [click|haerae|kmmlu|kmmlu-hard|hrm8k|kobalt|kormedmcqa|kmmlu-pro|musr-ko]"
            exit 1
            ;;
    esac
    
    echo "Completed evaluation for $env_file"
}

# 재시작 기능 안내
if [[ -n "$start_category" ]]; then
    echo "Resuming from category: $start_category"
else
    echo "Starting from the beginning (or skipping completed categories)"
fi

# 병렬 실행 관리
job_count=0
for env_file in "${env_files[@]}"; do
    # 백그라운드에서 실행
    run_model "$env_file" &
    
    ((job_count++))
    
    # 최대 병렬 작업 수에 도달하면 일부 작업이 완료될 때까지 대기
    if (( job_count >= max_parallel_jobs )); then
        wait -n  # 하나의 작업이 완료될 때까지 대기
        ((job_count--))
    fi
done

wait  # 모든 작업 완료 대기
echo "All evaluations completed!"