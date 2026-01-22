"""HAERAE-VISION benchmark evaluation for Vision Language Models"""
import os
import sys
import time
import base64
import argparse
import json
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from datasets import load_dataset
from tqdm import tqdm
import pandas as pd
import boto3
from PIL import Image

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.logger import logger
from util.common_helper import str2bool, format_timespan, check_existing_csv_in_debug


# Supported models configuration
# Model IDs from AWS documentation: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
# Cross-region inference profile IDs use prefixes like 'us.', 'eu.', 'apac.', or 'global.'
SUPPORTED_MODELS = {
    # Claude 4.5 models (Cross-region inference profiles only)
    "claude-sonnet-4-5": {
        "model_id": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
        "display_name": "Claude 4.5 Sonnet",
        "supports_vision": True,
    },
    "claude-opus-4-5": {
        "model_id": "us.anthropic.claude-opus-4-5-20251101-v1:0",
        "display_name": "Claude 4.5 Opus",
        "supports_vision": True,
    },
    "claude-haiku-4-5": {
        "model_id": "us.anthropic.claude-haiku-4-5-20251001-v1:0",
        "display_name": "Claude 4.5 Haiku",
        "supports_vision": True,
    },
    # Nova v1 models (Single-region and Cross-region support)
    "nova-pro-v1": {
        "model_id": "us.amazon.nova-pro-v1:0",
        "display_name": "Nova Pro v1",
        "supports_vision": True,
    },
    "nova-lite-v1": {
        "model_id": "us.amazon.nova-lite-v1:0",
        "display_name": "Nova Lite v1",
        "supports_vision": True,
    },
    # Nova v2 models (Cross-region inference profiles only)
    "nova-pro-v2": {
        "model_id": "us.amazon.nova-2-pro-preview-20251202-v1:0",
        "display_name": "Nova 2 Pro",
        "supports_vision": True,
    },
    "nova-lite-v2": {
        "model_id": "us.amazon.nova-2-lite-v1:0",
        "display_name": "Nova 2 Lite",
        "supports_vision": True,
    },
}

# Default judge model
DEFAULT_JUDGE_MODEL = "claude-sonnet-4-5"


def get_model_id(model_name):
    """Get the full model ID from short name"""
    if model_name in SUPPORTED_MODELS:
        return SUPPORTED_MODELS[model_name]["model_id"]
    # If full model ID is provided directly
    return model_name


def get_display_name(model_name):
    """Get display name for a model"""
    if model_name in SUPPORTED_MODELS:
        return SUPPORTED_MODELS[model_name]["display_name"]
    return model_name


def encode_image_to_base64(image):
    """PIL Image를 base64로 인코딩"""
    if image is None:
        return None

    buffered = BytesIO()
    # RGB로 변환 (RGBA인 경우)
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image.save(buffered, format="JPEG", quality=85)
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def get_vision_response_bedrock(client, model_id, images, question, max_tokens=1024, temperature=0.01):
    """AWS Bedrock Converse API를 사용하여 비전 모델 응답 생성"""

    # 이미지 컨텐츠 구성
    content = []
    for idx, img in enumerate(images):
        if img is not None:
            img_base64 = encode_image_to_base64(img)
            if img_base64:
                content.append({
                    "image": {
                        "format": "jpeg",
                        "source": {
                            "bytes": base64.b64decode(img_base64)
                        }
                    }
                })

    # 텍스트 질문 추가
    content.append({
        "text": question
    })

    messages = [
        {
            "role": "user",
            "content": content
        }
    ]

    system_prompt = [{"text": "당신은 이미지를 분석하고 질문에 정확하게 답변하는 AI 어시스턴트입니다. 한국어로 답변해주세요."}]

    try:
        response = client.converse(
            modelId=model_id,
            messages=messages,
            system=system_prompt,
            inferenceConfig={
                "maxTokens": max_tokens,
                "temperature": temperature,
            }
        )

        output_message = response.get("output", {}).get("message", {})
        content_blocks = output_message.get("content", [])

        response_text = ""
        for block in content_blocks:
            if "text" in block:
                response_text += block["text"]

        return response_text

    except Exception as e:
        logger.error(f"Bedrock API error: {e}")
        return f"ERROR: {str(e)}"


def get_judge_score(judge_client, model_id, question, response, checklist, max_tokens=512):
    """GPT 모델로 응답 채점"""

    checklist_str = "\n".join(checklist) if isinstance(checklist, list) else checklist

    prompt = f"""다음은 사용자의 질문과 AI 모델의 응답입니다. 평가 기준(checklist)에 따라 응답의 품질을 평가해주세요.

[질문]
{question}

[AI 응답]
{response}

[평가 기준]
{checklist_str}

위 평가 기준을 바탕으로 AI 응답의 품질을 0.0에서 1.0 사이의 점수로 평가해주세요.
- 1.0: 모든 평가 기준을 완벽하게 충족
- 0.75: 대부분의 기준을 충족
- 0.5: 일부 기준을 충족
- 0.25: 소수의 기준만 충족
- 0.0: 평가 기준을 전혀 충족하지 못함

반드시 다음 형식으로 답변해주세요:
SCORE: [점수]
REASON: [평가 이유]"""

    messages = [
        {
            "role": "user",
            "content": [{"text": prompt}]
        }
    ]

    try:
        response = judge_client.converse(
            modelId=model_id,
            messages=messages,
            inferenceConfig={
                "maxTokens": max_tokens,
                "temperature": 0.01,
            }
        )

        output_message = response.get("output", {}).get("message", {})
        content_blocks = output_message.get("content", [])

        judge_response = ""
        for block in content_blocks:
            if "text" in block:
                judge_response += block["text"]

        return judge_response

    except Exception as e:
        logger.error(f"Judge API error: {e}")
        return f"ERROR: {str(e)}"


def parse_score(judge_response):
    """판정 응답에서 점수 추출"""
    try:
        if "SCORE:" in judge_response:
            score_line = judge_response.split("SCORE:")[1].split("\n")[0].strip()
            score = float(score_line)
            return min(max(score, 0.0), 1.0)  # 0.0~1.0 범위로 클램핑
    except:
        pass
    return None


def process_sample(sample, client, model_id, question_type, max_tokens, temperature, max_retries=3, wait_time=1.0):
    """단일 샘플 처리 (재시도 로직 포함)"""
    images = sample.get("images", [])

    # 질문 유형 선택
    if question_type == "original":
        question = sample.get("question_original", "")
    else:
        question = sample.get("question_explicit", "")

    # 재시도 로직
    for retry in range(max_retries):
        response = get_vision_response_bedrock(
            client, model_id, images, question, max_tokens, temperature
        )

        # 에러가 아니면 성공
        if not response.startswith("ERROR:"):
            break

        # 에러 발생 시 대기 후 재시도
        if retry < max_retries - 1:
            sleep_time = wait_time * (retry + 1)
            logger.warning(f"Retry {retry + 1}/{max_retries} after {sleep_time}s for sample {sample.get('question_idx')}")
            time.sleep(sleep_time)

    return {
        "question_idx": sample.get("question_idx"),
        "source": sample.get("source"),
        "category": sample.get("category"),
        "question_type": question_type,
        "question": question,
        "checklist": sample.get("checklist"),
        "response": response,
    }


def save_result_to_csv(result, csv_path, chunk_id=None):
    """결과를 CSV 파일에 저장 (중복 방지 로직 포함)"""
    import fcntl

    # checklist를 JSON 문자열로 변환
    result_copy = result.copy()
    if isinstance(result_copy.get('checklist'), list):
        result_copy['checklist'] = json.dumps(result_copy['checklist'], ensure_ascii=False)

    question_idx = result_copy.get('question_idx')

    if os.path.exists(csv_path):
        # 기존 파일에서 중복 체크
        try:
            existing_df = pd.read_csv(csv_path)
            if question_idx in existing_df['question_idx'].values:
                # 이미 존재하면 업데이트 (에러였던 것을 성공으로 덮어쓰기)
                existing_response = existing_df.loc[existing_df['question_idx'] == question_idx, 'response'].iloc[0]
                new_response = result_copy.get('response', '')

                # 기존이 에러이고 새 것이 정상이면 업데이트
                if str(existing_response).startswith('ERROR:') and not str(new_response).startswith('ERROR:'):
                    existing_df.loc[existing_df['question_idx'] == question_idx] = pd.DataFrame([result_copy]).iloc[0]
                    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                        existing_df.to_csv(f, header=True, index=False)
                # 그 외의 경우는 중복 저장 방지
                return
        except Exception as e:
            logger.warning(f"Error checking duplicates: {e}")

    df_new = pd.DataFrame([result_copy])

    if os.path.exists(csv_path):
        with open(csv_path, 'a', newline='', encoding='utf-8') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            df_new.to_csv(f, header=False, index=False)
    else:
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            df_new.to_csv(f, header=True, index=False)


def get_processed_indices(csv_path):
    """이미 처리된 샘플의 question_idx 목록 반환"""
    if not os.path.exists(csv_path):
        return set()

    try:
        df = pd.read_csv(csv_path)
        # 에러가 아닌 성공한 샘플만 반환
        success_df = df[~df['response'].str.startswith('ERROR:', na=False)]
        return set(success_df['question_idx'].tolist())
    except Exception as e:
        logger.warning(f"Error reading processed indices: {e}")
        return set()


def evaluate_responses(csv_path, judge_model_id, region, output_path=None, wait_time=1.0, max_retries=3):
    """저장된 응답을 judge 모델로 채점 (재시도 로직 포함)"""
    logger.info("Starting evaluation with judge model...")

    df = pd.read_csv(csv_path)

    # 중복 제거 (question_idx 기준으로 첫 번째 행만 유지)
    original_len = len(df)
    df = df.drop_duplicates(subset=['question_idx'], keep='first')
    if len(df) < original_len:
        logger.warning(f"Removed {original_len - len(df)} duplicate rows")

    # 이미 채점된 결과가 있으면 건너뛰기
    if 'score' in df.columns and df['score'].notna().all():
        logger.info("All responses already scored. Skipping evaluation.")
        return df

    client = boto3.client('bedrock-runtime', region_name=region)

    scores = []
    judge_responses = []

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Judging responses"):
        # 이미 채점된 경우 건너뛰기
        if 'score' in df.columns and pd.notna(row.get('score')):
            scores.append(row['score'])
            judge_responses.append(row.get('judge_response', ''))
            continue

        # 에러 응답은 0점 처리
        if str(row['response']).startswith('ERROR:'):
            scores.append(0.0)
            judge_responses.append("ERROR_RESPONSE")
            continue

        checklist = row['checklist']
        if isinstance(checklist, str):
            try:
                checklist = json.loads(checklist)
            except:
                checklist = [checklist]

        # 재시도 로직 추가
        score = None
        judge_response = None
        for retry in range(max_retries):
            judge_response = get_judge_score(
                client, judge_model_id,
                row['question'], row['response'], checklist
            )

            # 에러가 아니면 점수 파싱 시도
            if not str(judge_response).startswith('ERROR:'):
                score = parse_score(judge_response)
                if score is not None:
                    break

            # 재시도 전 대기
            if retry < max_retries - 1:
                sleep_time = wait_time * (retry + 2)
                logger.warning(f"Judge retry {retry + 1}/{max_retries} for question_idx {row.get('question_idx')}, waiting {sleep_time}s")
                time.sleep(sleep_time)

        # 모든 재시도 실패 시 0점 처리
        if score is None:
            logger.warning(f"Failed to score question_idx {row.get('question_idx')} after {max_retries} retries, assigning 0.0")
            score = 0.0

        scores.append(score)
        judge_responses.append(judge_response)

        time.sleep(wait_time)  # 쓰로틀링 방지

    df['judge_response'] = judge_responses
    df['score'] = scores

    # 결과 저장
    if output_path is None:
        output_path = csv_path.replace('.csv', '_scored.csv')

    df.to_csv(output_path, index=False)
    logger.info(f"Scored results saved to: {output_path}")

    return df


def calculate_metrics(df):
    """평가 결과 메트릭 계산"""
    # 유효한 점수만 필터링
    valid_df = df[df['score'].notna()]

    if len(valid_df) == 0:
        logger.warning("No valid scores found")
        return {}

    metrics = {
        'overall': {
            'mean_score': valid_df['score'].mean(),
            'std_score': valid_df['score'].std(),
            'total_samples': len(valid_df),
        }
    }

    # 카테고리별 점수
    if 'category' in valid_df.columns:
        category_scores = valid_df.groupby('category')['score'].agg(['mean', 'std', 'count'])
        metrics['by_category'] = category_scores.to_dict('index')

    # 소스별 점수
    if 'source' in valid_df.columns:
        source_scores = valid_df.groupby('source')['score'].agg(['mean', 'std', 'count'])
        metrics['by_source'] = source_scores.to_dict('index')

    # 질문 유형별 점수
    if 'question_type' in valid_df.columns:
        qtype_scores = valid_df.groupby('question_type')['score'].agg(['mean', 'std', 'count'])
        metrics['by_question_type'] = qtype_scores.to_dict('index')

    return metrics


def print_metrics(metrics, model_name=""):
    """메트릭 출력"""
    print("\n" + "="*60)
    print(f"HAERAE-VISION Evaluation Results - {model_name}")
    print("="*60)

    overall = metrics.get('overall', {})
    print(f"\n📊 Overall Score: {overall.get('mean_score', 0):.4f} (±{overall.get('std_score', 0):.4f})")
    print(f"   Total Samples: {overall.get('total_samples', 0)}")

    if 'by_category' in metrics:
        print("\n📂 Scores by Category:")
        for cat, scores in sorted(metrics['by_category'].items(), key=lambda x: x[1]['mean'], reverse=True):
            print(f"   {cat}: {scores['mean']:.4f} (±{scores['std']:.4f}) [n={int(scores['count'])}]")

    if 'by_source' in metrics:
        print("\n📰 Scores by Source:")
        for src, scores in sorted(metrics['by_source'].items(), key=lambda x: x[1]['mean'], reverse=True):
            print(f"   {src}: {scores['mean']:.4f} (±{scores['std']:.4f}) [n={int(scores['count'])}]")

    if 'by_question_type' in metrics:
        print("\n❓ Scores by Question Type:")
        for qtype, scores in sorted(metrics['by_question_type'].items()):
            print(f"   {qtype}: {scores['mean']:.4f} (±{scores['std']:.4f}) [n={int(scores['count'])}]")

    print("\n" + "="*60)


def run_inference(args, model_name, model_id, region, all_data, csv_path):
    """모델 추론 실행"""
    # 이미 처리된 샘플 확인
    processed_indices = get_processed_indices(csv_path)
    remaining_data = [d for d in all_data if d.get('question_idx') not in processed_indices]

    if not remaining_data:
        logger.info(f"All {len(all_data)} samples already processed for {model_name}")
        return

    logger.info(f"🚀 [{model_name}] Processing {len(remaining_data)} samples ({len(processed_indices)} already done)")

    client = boto3.client('bedrock-runtime', region_name=region)

    for sample in tqdm(remaining_data, desc=f"Processing [{model_name}]"):
        try:
            result = process_sample(
                sample, client, model_id, args.question_type,
                args.max_tokens, args.temperature,
                max_retries=args.max_retries, wait_time=args.wait_time
            )
            save_result_to_csv(result, csv_path)
            time.sleep(args.wait_time)
        except Exception as e:
            logger.error(f"Error processing sample {sample.get('question_idx')}: {e}")
            error_result = {
                "question_idx": sample.get("question_idx"),
                "source": sample.get("source"),
                "category": sample.get("category"),
                "question_type": args.question_type,
                "question": sample.get(f"question_{args.question_type}", ""),
                "checklist": sample.get("checklist"),
                "response": f"ERROR: {str(e)}",
            }
            save_result_to_csv(error_result, csv_path)


def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description="HAERAE-VISION Benchmark Evaluation")
    parser.add_argument("--is_debug", type=str2bool, default=False)
    parser.add_argument("--num_debug_samples", type=int, default=5)
    parser.add_argument("--model", type=str, default="nova-lite-v1",
                        choices=list(SUPPORTED_MODELS.keys()),
                        help=f"Model to evaluate. Choices: {list(SUPPORTED_MODELS.keys())}")
    parser.add_argument("--all_models", type=str2bool, default=False,
                        help="Run evaluation on all supported models")
    parser.add_argument("--question_type", type=str, default="original",
                        choices=["original", "explicit"],
                        help="Question type: 'original' (under-specified) or 'explicit' (clarified)")
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--temperature", type=float, default=0.01)
    parser.add_argument("--wait_time", type=float, default=float(os.getenv("WAIT_TIME", "1.0")))
    parser.add_argument("--max_retries", type=int, default=3)
    parser.add_argument("--skip_inference", type=str2bool, default=False,
                        help="Skip inference and only run evaluation on existing results")
    parser.add_argument("--skip_evaluation", type=str2bool, default=False,
                        help="Skip evaluation (judging) step")
    parser.add_argument("--judge_model", type=str, default=DEFAULT_JUDGE_MODEL,
                        help=f"Model for judging (default: {DEFAULT_JUDGE_MODEL})")
    parser.add_argument("--region", type=str, default=None,
                        help="AWS region (default: from env or us-west-2)")
    args = parser.parse_args()

    load_dotenv(os.getenv('DOTENV_PATH', '.env'), override=True)

    # Region 설정
    region = args.region or os.getenv("AWS_REGION", "us-west-2")

    # 평가할 모델 목록 결정
    if args.all_models:
        models_to_eval = list(SUPPORTED_MODELS.keys())
    else:
        models_to_eval = [args.model]

    # 데이터셋 로드
    logger.info("Loading HAERAE-VISION dataset...")
    ds = load_dataset("HAERAE-HUB/HAERAE-VISION", split="train")
    all_data = [item for item in ds]
    logger.info(f"Loaded {len(all_data)} samples")

    # 디버그 모드
    if args.is_debug:
        all_data = all_data[:args.num_debug_samples]
        logger.info(f"Debug mode: using {len(all_data)} samples")

    if not all_data:
        logger.info("No data to process!")
        return

    os.makedirs("results", exist_ok=True)

    # Judge 모델 ID
    judge_model_id = get_model_id(args.judge_model)

    # 각 모델에 대해 평가 실행
    all_results = {}

    for model_name in models_to_eval:
        model_config = SUPPORTED_MODELS[model_name]
        model_id = model_config["model_id"]
        display_name = model_config["display_name"]

        logger.info(f"\n{'='*60}")
        logger.info(f"Evaluating: {display_name} ({model_id})")
        logger.info(f"Region: {region}")
        logger.info(f"Question type: {args.question_type}")
        logger.info(f"{'='*60}")

        # CSV 경로
        csv_path = f"results/[HAERAE-VISION] {model_name}_{args.question_type}.csv"
        scored_csv_path = csv_path.replace('.csv', '_scored.csv')

        # 추론 단계
        if not args.skip_inference:
            start_time = time.time()
            run_inference(args, display_name, model_id, region, all_data, csv_path)
            elapsed = time.time() - start_time
            logger.info(f"✅ [{display_name}] Inference completed in {format_timespan(elapsed)}")
            logger.info(f"Results saved to: {csv_path}")

        # 평가 (Judging) 단계
        if not args.skip_evaluation and os.path.exists(csv_path):
            logger.info(f"\nStarting evaluation with judge model: {args.judge_model}")

            df = evaluate_responses(csv_path, judge_model_id, region, scored_csv_path, args.wait_time)

            # 메트릭 계산 및 출력
            metrics = calculate_metrics(df)
            print_metrics(metrics, display_name)

            # 메트릭을 JSON으로 저장
            metrics_path = scored_csv_path.replace('.csv', '_metrics.json')
            with open(metrics_path, 'w', encoding='utf-8') as f:
                json.dump(metrics, f, ensure_ascii=False, indent=2, default=str)
            logger.info(f"Metrics saved to: {metrics_path}")

            all_results[model_name] = {
                'display_name': display_name,
                'metrics': metrics,
                'csv_path': scored_csv_path,
            }

    # 모든 모델 결과 요약 (여러 모델 평가 시)
    if len(all_results) > 1:
        print("\n" + "="*70)
        print("SUMMARY: All Models Comparison")
        print("="*70)
        print(f"\n{'Model':<25} {'Score':<12} {'Std':<12} {'Samples':<10}")
        print("-"*60)

        sorted_results = sorted(all_results.items(),
                               key=lambda x: x[1]['metrics'].get('overall', {}).get('mean_score', 0),
                               reverse=True)

        for model_name, result in sorted_results:
            overall = result['metrics'].get('overall', {})
            print(f"{result['display_name']:<25} {overall.get('mean_score', 0):.4f}       "
                  f"{overall.get('std_score', 0):.4f}       {overall.get('total_samples', 0)}")

        print("="*70)


if __name__ == "__main__":
    main()
