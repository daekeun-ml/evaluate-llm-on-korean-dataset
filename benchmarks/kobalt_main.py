"""KoBALT benchmark evaluation"""
import os
import sys
import time
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
from dotenv import load_dotenv
from datasets import load_dataset
from tqdm import tqdm

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.evaluator import KoBALTEvaluator
from core.logger import logger
from util.evaluate_helper import evaluate
from util.common_helper import check_existing_csv_in_debug, get_provider_name, str2bool, format_timespan, skip_completed_samples
from util.custom_parser import MultipleChoicesTenParser

def process_chunk(chunk_info):
    """데이터 청크 처리"""
    chunk_id, data_chunk, model_config, template_type, csv_path, model_name = chunk_info
    
    logger.info(f"[{model_name}] Processing chunk {chunk_id} with {len(data_chunk)} samples")
    
    try:
        evaluator = KoBALTEvaluator(model_config, template_type)
        results = evaluator.process_batch(data_chunk, MultipleChoicesTenParser, num_choices=10, csv_path=csv_path, chunk_id=chunk_id)
        # save_results는 process_batch 내에서 이미 호출됨
        
        logger.info(f"✅ [{model_name}] Completed chunk {chunk_id}")
        return chunk_id, "completed"
        
    except Exception as e:
        logger.error(f"❌ Error processing chunk {chunk_id}: {e}")
        return chunk_id, f"error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="KoBALT Benchmark Evaluation")
    parser.add_argument("--is_debug", type=str2bool, default=True)
    parser.add_argument("--num_debug_samples", type=int, default=5)
    parser.add_argument("--model_provider", type=str, default="azureopenai")
    parser.add_argument("--batch_size", type=int, default=10)
    parser.add_argument("--max_retries", type=int, default=3)
    parser.add_argument("--max_tokens", type=int, default=256)
    parser.add_argument("--temperature", type=float, default=0.01)
    parser.add_argument("--template_type", type=str, default="basic")
    parser.add_argument("--wait_time", type=float, default=float(os.getenv("WAIT_TIME", "30.0")))
    parser.add_argument("--levels", nargs="+", type=int, default=None, help="Filter by levels (1, 2, 3)")
    parser.add_argument("--num_workers", type=int, default=4)
    args = parser.parse_args()
    
    load_dotenv(os.getenv('DOTENV_PATH', '.env'), override=True)
    
    model_provider = os.getenv("MODEL_PROVIDER", args.model_provider)
    logger.info(f"Using {get_provider_name(model_provider)} as model provider.")
    
    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
    model_version = os.getenv("MODEL_VERSION", "2024-07-18")
    
    model_config = {
        'provider': model_provider,
        'batch_size': args.batch_size,
        'max_tokens': args.max_tokens,
        'temperature': args.temperature,
        'max_retries': args.max_retries,
        'wait_time': args.wait_time,
    }
    
    os.makedirs("results", exist_ok=True)
    csv_path = f"results/[KoBALT] {model_name}-{model_version}.csv"
    
    if check_existing_csv_in_debug(csv_path, args.is_debug):
        evaluate(csv_path, dataset="KoBALT", verbose=True)
        return
    
    all_levels = [1, 2, 3]
    
    if args.levels:
        invalid = [l for l in args.levels if l not in all_levels]
        if invalid:
            logger.error(f"Invalid levels: {invalid}")
            return
        all_levels = args.levels
    
    # 전체 데이터 로드
    logger.info("Loading all data...")
    dataset = load_dataset("snunlp/KoBALT-700", "kobalt_v1", split="raw")
    
    all_data = []
    for idx, item in enumerate(dataset):
        if item["Level"] in all_levels:
            all_data.append({
                "qid": str(idx),
                "category": item["Class"],
                "subcategory": item.get("Subclass"),
                "level": item.get("Level"),
                "question": item["Question"],
                "answer": item["Answer"],
            })

    # 디버그 모드
    if args.is_debug:
        logger.info(f"🔍 Debug mode: requested {args.num_debug_samples} samples, available {len(all_data)} samples")
        all_data = all_data[:args.num_debug_samples]
        logger.info(f"🔍 Using {len(all_data)} samples for evaluation")

    # Re-answer only the samples that previously failed or came back empty
    all_data = skip_completed_samples(all_data, csv_path)

    if not all_data:
        logger.info("✅ All data completed!")
        evaluate(csv_path, dataset="KoBALT", verbose=True)
        return
    
    logger.info(f"🚀 [{model_name}] Processing {len(all_data)} samples with {args.num_workers} workers")
    
    # 데이터를 worker 수만큼 균등 분할
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
    evaluate(csv_path, dataset="KoBALT", verbose=True)


if __name__ == "__main__":
    main()
