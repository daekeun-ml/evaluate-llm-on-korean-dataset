"""MuSR(Ko) benchmark evaluation"""
import os
import sys
import time
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
from dotenv import load_dotenv
from datasets import load_dataset
from tqdm import tqdm

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.question_templates import get_question_template
from core.evaluator import MuSRKoEvaluator
from core.logger import logger
from util.custom_parser import BaseMultipleChoiceParser
from util.common_helper import str2bool, format_timespan, get_provider_name, check_existing_csv_in_debug, skip_completed_samples
from util.evaluate_helper import evaluate

SUBSETS = ["murder_mysteries", "object_placements", "team_allocation"]


def get_prompt(x):
    """프롬프트 생성 (narrative를 context로, 선택지 수는 서브셋마다 고정)"""
    num_choices = len(x["choices"])
    template = get_question_template(num_choices=num_choices, with_context=True)

    format_dict = {"CONTEXT": x["narrative"], "QUESTION": x["question"]}
    for i, choice in enumerate(x["choices"]):
        format_dict[chr(65 + i)] = choice

    return template.format(**format_dict)


def get_answer(x):
    """정답 추출 (0-based 인덱스를 알파벳으로 변환)"""
    return chr(65 + int(x["answer"]))


def make_parser_class(num_choices):
    """선택지 개수에 맞는 파서 클래스를 동적으로 생성"""
    choices = [chr(65 + i) for i in range(num_choices)]

    class _Parser(BaseMultipleChoiceParser):
        def __init__(self):
            super().__init__(choices)

    return _Parser


def process_chunk(chunk_info):
    """데이터 청크 처리 (서브셋별로 나눠서 처리, 서브셋마다 선택지 수가 다름)"""
    chunk_id, data_chunk, model_config, template_type, csv_path, model_name = chunk_info

    logger.info(f"[{model_name}] Processing chunk {chunk_id} with {len(data_chunk)} samples")

    try:
        evaluator = MuSRKoEvaluator(model_config, template_type)

        by_subset = {}
        for item in data_chunk:
            by_subset.setdefault(item["subset"], []).append(item)

        for subset, sub_data in by_subset.items():
            num_choices = sub_data[0]["num_choices"]
            parser_class = make_parser_class(num_choices)
            evaluator.process_batch(
                sub_data, parser_class, num_choices=num_choices, csv_path=csv_path, chunk_id=chunk_id
            )

        logger.info(f"✅ [{model_name}] Completed chunk {chunk_id}")
        return chunk_id, "completed"

    except Exception as e:
        logger.error(f"❌ Error processing chunk {chunk_id}: {e}")
        return chunk_id, f"error: {str(e)}"


def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--is_debug", type=str2bool, default=True)
    parser.add_argument("--num_debug_samples", type=int, default=5)
    parser.add_argument("--model_provider", type=str, default="azureopenai")
    parser.add_argument("--hf_model_id", type=str, default="mistralai/Mistral-7B-Instruct-v0.2")
    parser.add_argument("--batch_size", type=int, default=10)
    parser.add_argument("--max_retries", type=int, default=3)
    parser.add_argument("--max_tokens", type=int, default=256)
    parser.add_argument("--temperature", type=float, default=0.01)
    parser.add_argument("--template_type", type=str, default="basic")
    parser.add_argument("--wait_time", type=float, default=float(os.getenv("WAIT_TIME", "30.0")))
    parser.add_argument("--subsets", nargs="+", default=None, help="Filter by subset (murder_mysteries object_placements team_allocation)")
    parser.add_argument("--num_workers", type=int, default=4)
    args = parser.parse_args()

    load_dotenv(os.getenv('DOTENV_PATH', '.env'), override=True)

    model_provider = os.getenv("MODEL_PROVIDER", args.model_provider)
    logger.info(f"Using {get_provider_name(model_provider)} as model provider.")

    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
    model_version = os.getenv("MODEL_VERSION", "2024-07-18")

    model_config = {
        'provider': model_provider,
        'hf_model_id': args.hf_model_id,
        'batch_size': args.batch_size,
        'max_tokens': args.max_tokens,
        'temperature': args.temperature,
        'max_retries': args.max_retries,
        'wait_time': args.wait_time,
    }

    os.makedirs("results", exist_ok=True)
    csv_path = f"results/[MuSR-Ko] {model_name}-{model_version}.csv"

    if check_existing_csv_in_debug(csv_path, args.is_debug):
        evaluate(csv_path, dataset="MuSR-Ko", verbose=True)
        return

    all_subsets = args.subsets if args.subsets else SUBSETS
    invalid = [s for s in all_subsets if s not in SUBSETS]
    if invalid:
        logger.error(f"Invalid subsets: {invalid}")
        return

    logger.info("Loading all data...")
    all_data = []
    for subset in all_subsets:
        ds = load_dataset("thunder-research-group/SNU_Ko-MuSR", subset)["test"]
        for idx, item in enumerate(ds):
            all_data.append({
                "qid": f"{subset}-{idx}",
                "subset": subset,
                "num_choices": len(item["choices"]),
                "question": get_prompt(item),
                "answer": get_answer(item),
            })

    if args.is_debug:
        all_data = all_data[:args.num_debug_samples]

    # Re-answer only the samples that previously failed or came back empty
    all_data = skip_completed_samples(all_data, csv_path)

    if not all_data:
        logger.info("✅ All data completed!")
        evaluate(csv_path, dataset="MuSR-Ko", verbose=True)
        return

    logger.info(f"🚀 [{model_name}] Processing {len(all_data)} samples with {args.num_workers} workers")

    chunk_size = (len(all_data) + args.num_workers - 1) // args.num_workers
    chunks = [
        (i, all_data[i*chunk_size:(i+1)*chunk_size], model_config, args.template_type, csv_path, model_name)
        for i in range(args.num_workers)
        if i*chunk_size < len(all_data)
    ]

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=args.num_workers) as executor:
        futures = {executor.submit(process_chunk, chunk): i for i, chunk in enumerate(chunks)}

        with tqdm(total=len(all_data), desc="Processing samples", unit="samples") as pbar:
            for future in as_completed(futures):
                chunk_idx = futures[future]
                chunk_size = len(chunks[chunk_idx][1])
                pbar.update(chunk_size)
                pbar.set_postfix({"chunk": f"{sum(1 for f in futures if f.done())}/{len(chunks)}"})

        results = [future.result() for future in futures]

    elapsed = time.time() - start_time
    logger.info(f"\n{'='*50}")
    logger.info(f"✅ [{model_name}] Evaluation completed in {format_timespan(elapsed)}")
    logger.info(f"Results saved to: {csv_path}")

    for chunk_id, status in results:
        logger.info(f"  Chunk {chunk_id}: {status}")

    logger.info(f"\n{'='*50}")
    logger.info("Calculating accuracy...")
    evaluate(csv_path, dataset="MuSR-Ko", verbose=True)


if __name__ == "__main__":
    main()
