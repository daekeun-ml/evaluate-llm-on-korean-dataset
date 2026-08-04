import re
import json
import os
import numpy as np
import pandas as pd

# def convert_to_pascal_case(category):
#     exceptions = {'and'}
#     return '-'.join(word.capitalize() if word.lower() not in exceptions else word.lower() for word in category.split('-'))


def convert_to_pascal_case(category):
    # 카테고리 이름 정규화 (대소문자, 공백, 하이픈 처리)
    if pd.isna(category):
        return category
    
    # 문자열로 변환하고 공백 제거
    category = str(category).strip()
    
    # 이미 올바른 형식인지 확인 (하이픈으로 구분된 Pascal Case)
    if "-" in category and category.replace("-", "").replace("and", "").isalpha():
        # 각 단어의 첫 글자를 대문자로, 나머지는 소문자로
        words = category.split("-")
        normalized_words = []
        for word in words:
            if word.lower() == "and":
                normalized_words.append("and")
            else:
                normalized_words.append(word.capitalize())
        return "-".join(normalized_words)
    
    # 언더스코어로 구분된 경우 하이픈으로 변환
    if "_" in category:
        words = category.split("_")
        normalized_words = []
        for word in words:
            if word.lower() == "and":
                normalized_words.append("and")
            else:
                normalized_words.append(word.capitalize())
        return "-".join(normalized_words)
    
    # 공백으로 구분된 경우 하이픈으로 변환
    if " " in category:
        words = category.split()
        normalized_words = []
        for word in words:
            if word.lower() == "and":
                normalized_words.append("and")
            else:
                normalized_words.append(word.capitalize())
        return "-".join(normalized_words)
    
    # 단일 단어인 경우 첫 글자만 대문자로
    return category.capitalize()


def extract_single_alphabet_answer(row):
    pred = row["pred"]

    if (
        isinstance(pred, float)
        and np.isnan(pred)
        or (isinstance(pred, str) and len(pred.strip()) == 0)
    ):
        match = re.search(r"정답(?: \(Answer\))?: (\w)", row["response"])
        return match.group(1) if match else None
    else:
        return pred


def evaluate(csv_path, dataset="CLIcK", subset=None, verbose=False):

    valid_datasets = ["CLIcK", "KMMLU", "KMMLU-HARD", "HAERAE", "hrm8k", "KoBALT", "KorMedMCQA"]
    assert (
        dataset in valid_datasets
    ), f"Invalid 'dataset' value. Please choose from {valid_datasets}."

    result = pd.read_csv(csv_path)
    
    # FAILED 응답 필터링 및 로깅
    original_count = len(result)
    failed_count = len(result[result["pred"] == "FAILED"])
    if failed_count > 0:
        print(f"Warning: Found {failed_count} FAILED responses out of {original_count} total responses")
        print(f"Excluding FAILED responses from accuracy calculation")
        result = result[result["pred"] != "FAILED"]
        print(f"Evaluating on {len(result)} valid responses")

    if dataset == "CLIcK":
        mapping_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "mapping", "id_to_category.json")
        with open(mapping_path, "r") as json_file:
            id_to_category = json.load(json_file)

        if "id" in result.columns:
            result["category"] = result["id"].map(id_to_category)
            
            # 매핑되지 않은 ID들 확인 및 제거
            missing_ids = result[result["category"].isna()]["id"].unique()
            if len(missing_ids) > 0:
                print(f"Warning: Found IDs without category mapping: {missing_ids[:10]}...")
                print(f"Total missing IDs: {len(missing_ids)}")
                result = result.dropna(subset=["category"])
        elif "category" not in result.columns:
            raise ValueError("CLIcK dataset requires either 'id' or 'category' column")
        
        result["supercategory"] = result["category"].apply(
            lambda x: (
                "Culture"
                if x in [
                    "Economy", "Geography", "History", "Law", "Politics", 
                    "Society", "Tradition", "Pop Culture",  # "Popular" → "Pop Culture"로 수정
                ]
                else "Language" if x in ["Functional", "Textual", "Grammar"] else "Other"
            )
        )
    elif dataset in ["KMMLU", "KMMLU-HARD"]:
        mapping_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "mapping", "kmmlu_category.json")
        with open(mapping_path, "r") as json_file:
            category_to_supercategory = json.load(json_file)
        
        result["category"] = result["category"].map(convert_to_pascal_case)
        result["supercategory"] = result["category"].map(category_to_supercategory)
    elif dataset == "hrm8k":
        if "subset" not in result.columns:
            result["subset"] = subset if subset else "Unknown"
        result["category"] = result["subset"]
    
    # For hrm8k, correct column is already calculated during evaluation
    if dataset != "hrm8k":
        result["correct"] = result["answer"] == result["pred"]
    
    overall_acc = round(result["correct"].mean() * 100, 2)

    if dataset == "KoBALT":
        # Level별 정확도
        level_names = {1: "Easy", 2: "Moderate", 3: "Hard"}
        result["level_name"] = result["level"].map(level_names)
        
        category_acc = (
            result.groupby(["level", "level_name"])
            .agg(
                accuracy=("correct", "mean"),
            )
            .reset_index()
            .sort_values("level")
        )
        category_acc = category_acc[["level_name", "accuracy"]]
        category_acc.columns = ["category", "accuracy"]
        category_acc["accuracy"] = pd.to_numeric(category_acc["accuracy"], errors="coerce").multiply(100).round(2)
        supercategory_acc = None
    elif dataset in ["HAERAE", "hrm8k", "KorMedMCQA"]:
        category_acc = (
            result.groupby(["category"])
            .agg(
                accuracy=("correct", "mean"),
            )
            .reset_index()
        )
        category_acc["accuracy"] = pd.to_numeric(category_acc["accuracy"], errors="coerce").multiply(100).round(2)
        supercategory_acc = None
    else:
        category_acc = (
            result.groupby(["supercategory", "category"])
            .agg(
                accuracy=("correct", "mean"),
            )
            .reset_index()
        )
        category_acc["accuracy"] = pd.to_numeric(category_acc["accuracy"], errors="coerce").multiply(100).round(2)

        supercategory_acc = (
            result.groupby("supercategory")
            .agg(
                accuracy=("correct", "mean"),
            )
            .reset_index()
        )
        supercategory_acc["accuracy"] = (
            pd.to_numeric(supercategory_acc["accuracy"], errors="coerce").multiply(100).round(2)
        )

    if verbose:
        print("Overall Accuracy:", overall_acc)
        print(category_acc)
        if supercategory_acc is not None:
            print(supercategory_acc)

    return overall_acc, category_acc, supercategory_acc


def get_markdown_accuracy(exp_group, *dfs):
    exp_group = exp_group[: len(dfs)]
    
    # 모든 DataFrame에서 가능한 모든 카테고리와 supercategory 조합 수집
    all_combinations = set()
    
    for df in dfs:
        if 'supercategory' in df.columns:
            # supercategory가 있는 경우 (KMMLU, CLIcK)
            all_combinations.update(zip(df['supercategory'], df['category']))
        else:
            # supercategory가 없는 경우 (HAERAE)
            all_combinations.update([(None, cat) for cat in df['category'].tolist()])
    
    # 각 DataFrame을 전체 카테고리 리스트에 맞춰 보완
    filled_dfs = []
    for i, df in enumerate(dfs):
        if 'supercategory' in df.columns:
            # supercategory가 있는 경우 (KMMLU, CLIcK)
            current_combinations = set(zip(df['supercategory'], df['category']))
            missing_combinations = all_combinations - current_combinations
            missing_rows = []
            for supercat, cat in missing_combinations:
                missing_rows.append({
                    'supercategory': supercat,
                    'category': cat,
                    'accuracy': None  # 누락된 카테고리는 None으로 표시 (0이 아닌)
                })
            
            if missing_rows:
                missing_df = pd.DataFrame(missing_rows)
                df_filled = pd.concat([df, missing_df], ignore_index=True)
                df_filled = df_filled.sort_values(['supercategory', 'category'])
            else:
                df_filled = df.copy()
        else:
            # supercategory가 없는 경우 (HAERAE)
            current_categories = set(df['category'].tolist())
            all_categories = set([cat for _, cat in all_combinations])
            missing_categories = all_categories - current_categories
            missing_rows = []
            for cat in missing_categories:
                missing_rows.append({
                    'category': cat,
                    'accuracy': None  # 누락된 카테고리는 None으로 표시
                })
            
            if missing_rows:
                missing_df = pd.DataFrame(missing_rows)
                df_filled = pd.concat([df, missing_df], ignore_index=True)
                df_filled = df_filled.sort_values(['category'])
            else:
                df_filled = df.copy()
        
        filled_dfs.append(df_filled)
    
    # 기존 로직으로 병합
    renamed_dfs = [
        df.rename(columns={"accuracy": exp_group[i]}) for i, df in enumerate(filled_dfs)
    ]

    merged_df = renamed_dfs[0]
    for df in renamed_dfs[1:]:
        merged_df = pd.concat([merged_df, df[[df.columns[-1]]]], axis=1)

    # NaN 값을 '-' 또는 'N/A'로 대체하여 명시적으로 표시
    merged_df = merged_df.fillna('-')

    md = merged_df.to_markdown(index=False)
    return md


def get_markdown_accuracy_with_overall(exp_group, *dfs, overall_acc):
    exp_group = exp_group[: len(dfs)]

    # 각 DataFrame에서 누락된 카테고리를 None으로 처리한 후 병합
    renamed_dfs = []
    for i, df in enumerate(dfs):
        renamed_df = df.rename(columns={"accuracy": exp_group[i]})
        renamed_dfs.append(renamed_df)

    merged_df = renamed_dfs[0]
    for df in renamed_dfs[1:]:
        merged_df = pd.concat([merged_df, df[[df.columns[-1]]]], axis=1)

    # NaN 값을 '-'로 대체
    merged_df = merged_df.fillna('-')

    overall_row = pd.DataFrame(
        [["**Overall**"] + overall_acc], columns=merged_df.columns
    )
    merged_df = pd.concat([merged_df, overall_row], ignore_index=True)

    md = merged_df.to_markdown(index=False)
    return md


def get_experiments_md(dataset, csv_path_dict, postfix=None):
    exp_group = list(csv_path_dict.keys())
    overall_acc = [None] * len(csv_path_dict)
    category_acc = [None] * len(csv_path_dict)
    supercategory_acc = [None] * len(csv_path_dict)

    for idx, (k, csv_path) in enumerate(csv_path_dict.items()):
        overall_acc[idx], category_acc[idx], supercategory_acc[idx] = evaluate(
            csv_path_dict[k], dataset
        )

    if postfix is None:
        title = f"### {dataset}\n\n"
    else:
        title = f"### {dataset} ({postfix})\n\n"

    if dataset in ("HAERAE", "KoBALT"):
        category_acc_md = get_markdown_accuracy_with_overall(
            exp_group, *category_acc, overall_acc=overall_acc
        )
        str_md = title
        str_md += f"#### Accuracy by category\n" + category_acc_md
    else:
        category_acc_md = get_markdown_accuracy(exp_group, *category_acc)
        supercategory_acc_md = get_markdown_accuracy_with_overall(
            exp_group, *supercategory_acc, overall_acc=overall_acc
        )
        str_md = title
        str_md += f"#### Accuracy by supercategory\n" + supercategory_acc_md + "\n\n"
        str_md += f"#### Accuracy by category\n" + category_acc_md

    return str_md
