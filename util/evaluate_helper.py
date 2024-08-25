import os
import json
import argparse
import pandas as pd

def convert_to_pascal_case(category):
    exceptions = {'and'} 
    return '-'.join(word.capitalize() if word.lower() not in exceptions else word.lower() for word in category.split('-'))

def evaluate(csv_path, dataset="CLIcK", verbose=False):
    
    valid_datasets = ["CLIcK", "KMMLU", "KMMLU-HARD", "HAERAE"]
    assert dataset in valid_datasets, f"Invalid 'dataset' value. Please choose from {valid_datasets}."
        
    result = pd.read_csv(csv_path)
    
    if dataset == "CLIcK":
        with open('id_to_category.json', 'r') as json_file:
            id_to_category = json.load(json_file)

        result["category"] = result["id"].map(id_to_category)
        result['supercategory'] = result['category'].apply(
            lambda x: 'Culture' if x in ['Economy', 'Geography', 'History', 'Law', 'Politics', 'Popular', 'Society', 'Tradition', 'Pop Culture'] else 
                    ('Language' if x in ['Functional', 'Textual', 'Grammar'] else 'Other')
        )
    elif dataset in ["KMMLU", "KMMLU-HARD"]:
        with open('kmmlu_category.json', 'r') as json_file:
            category_to_supercategory = json.load(json_file)
        result["category"] = result["category"].map(convert_to_pascal_case)    
        result["supercategory"] = result["category"].map(category_to_supercategory)
    
    result["correct"] = result["answer"] == result["pred"]
    overall_acc= round(result['correct'].mean() * 100, 2)

    if dataset == "HAERAE":
        category_acc = result.groupby(['category']).agg(
            accuracy=('correct', 'mean'),
        ).reset_index()
        category_acc['accuracy'] = category_acc['accuracy'].multiply(100).round(2)
        supercategory_acc = None
    else:
        category_acc = result.groupby(['supercategory', 'category']).agg(
            accuracy=('correct', 'mean'),
        ).reset_index()
        category_acc['accuracy'] = category_acc['accuracy'].multiply(100).round(2)
        
        supercategory_acc = result.groupby('supercategory').agg(
            accuracy=('correct', 'mean'),
        ).reset_index()
        supercategory_acc['accuracy'] = supercategory_acc['accuracy'].multiply(100).round(2)
        
    if verbose:
        print("Overall Accuracy:", overall_acc)
        print(category_acc)
        print(supercategory_acc)
    
    return overall_acc, category_acc, supercategory_acc

def get_markdown_accuracy(exp_group, *dfs):
    exp_group = exp_group[:len(dfs)]
    renamed_dfs = [df.rename(columns={'accuracy': exp_group[i]}) for i, df in enumerate(dfs)]
    
    merged_df = renamed_dfs[0]
    for df in renamed_dfs[1:]:
        merged_df = pd.concat([merged_df, df[[df.columns[-1]]]], axis=1)
    
    md = merged_df.to_markdown(index=False)
    return md

def get_markdown_accuracy_with_overall(exp_group, *dfs, overall_acc):
    exp_group = exp_group[:len(dfs)]
    
    renamed_dfs = [df.rename(columns={'accuracy': exp_group[i]}) for i, df in enumerate(dfs)]
    
    merged_df = renamed_dfs[0]
    for df in renamed_dfs[1:]:
        merged_df = pd.concat([merged_df, df[[df.columns[-1]]]], axis=1)
        
    overall_row = pd.DataFrame([['**Overall**'] + overall_acc], columns=merged_df.columns)
    merged_df = pd.concat([merged_df, overall_row], ignore_index=True)        
    
    md = merged_df.to_markdown(index=False)
    return md


def print_experiments(dataset, csv_path_dict):
    exp_group = list(csv_path_dict.keys())
    overall_acc = [None]*len(csv_path_dict)
    category_acc = [None]*len(csv_path_dict)
    supercategory_acc = [None]*len(csv_path_dict)
    
    for idx, (k, csv_path) in enumerate(csv_path_dict.items()):
        overall_acc[idx], category_acc[idx], supercategory_acc[idx] = evaluate(csv_path_dict[k], dataset)

        
    if dataset == "HAERAE":
        category_acc_md = get_markdown_accuracy_with_overall(
            exp_group, *category_acc, overall_acc=overall_acc
        )
        str_md = f"### {dataset}\n\n" 
        str_md += f"#### Accuracy by category\n" + category_acc_md         
    else:
        category_acc_md = get_markdown_accuracy(exp_group, *category_acc)
        supercategory_acc_md = get_markdown_accuracy_with_overall(
            exp_group, *supercategory_acc, overall_acc=overall_acc
        )
        str_md = f"### {dataset}\n\n" 
        str_md += f"#### Accuracy by supercategory\n" + supercategory_acc_md + "\n\n"
        str_md += f"#### Accuracy by category\n" + category_acc_md

    print(str_md)