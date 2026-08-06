import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from math import pi
import glob
import os

# 한글 카테고리 레이블(예: KMMLU-Pro의 license_name)이 깨지지 않도록 나눔고딕 폰트를 사용
for _font_path in [
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf",
]:
    if os.path.exists(_font_path):
        fm.fontManager.addfont(_font_path)
        plt.rcParams["font.family"] = fm.FontProperties(fname=_font_path).get_name()
        break

class RadarChartGenerator:
    def __init__(self, results_dir="./results"):
        self.results_dir = results_dir
        
    def read_dataset_results(self, dataset_name, model_filter=None):
        """Read all CSV files for a specific dataset.

        model_filter: optional list of model name substrings to include (e.g. only the
        4 models being compared in this round) instead of every CSV under results_dir.
        """
        if dataset_name == "KMMLU":
            # KMMLU-HARD/KMMLU-Pro를 제외하고 KMMLU만 선택
            pattern = os.path.join(self.results_dir, f"*{dataset_name}*.csv")
            files = [f for f in glob.glob(pattern) if "KMMLU-HARD" not in f and "KMMLU-Pro" not in f]
        else:
            pattern = os.path.join(self.results_dir, f"*{dataset_name}*.csv")
            files = glob.glob(pattern)

        results = {}
        for file in files:
            model_name = os.path.basename(file).replace(f"[{dataset_name}] ", "").replace(".csv", "")
            if model_filter and not any(m in model_name for m in model_filter):
                continue
            df = pd.read_csv(file)
            # Calculate accuracy
            if 'answer' in df.columns and 'pred' in df.columns:
                df['correct'] = (df['answer'] == df['pred']).astype(int)
            results[model_name] = df

        return results
    
    def create_radar_chart(self, data_dict, title, save_path=None, top_n=None):
        """Create radar chart from dictionary of model results"""
        if not data_dict:
            print(f"No data found for {title}")
            return
            
        # Sort models by average performance (descending)
        sorted_models = sorted(data_dict.items(), 
                             key=lambda x: sum(x[1].values()) / len(x[1].values()), 
                             reverse=True)
        
        # Select top N models if specified
        if top_n:
            sorted_models = sorted_models[:top_n]
            title += f" (Top {top_n})"
        
        # Get categories from first model
        categories = list(sorted_models[0][1].keys())
        
        # Number of variables
        N = len(categories)
        
        # Compute angle for each axis
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]  # Complete the circle
        
        # Initialize plot with better styling
        plt.style.use('seaborn-v0_8-whitegrid')
        if "NanumGothic" in [f.name for f in fm.fontManager.ttflist]:
            plt.rcParams["font.family"] = "NanumGothic"
        plt.rcParams["axes.unicode_minus"] = False
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        fig.patch.set_facecolor('white')
        
        # Enhanced color palette
        colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6', 
                 '#1ABC9C', '#E67E22', '#34495E', '#E91E63', '#FF5722']
        
        # Plot data for each model (sorted by performance)
        for i, (model_name, scores) in enumerate(sorted_models):
            values = [scores.get(cat, 0) for cat in categories]
            values += values[:1]  # Complete the circle
            
            color = colors[i % len(colors)]
            
            # Plot line with enhanced styling
            ax.plot(angles, values, 'o-', linewidth=1.5, label=model_name, 
                   color=color, markersize=4, alpha=0.8)
            ax.fill(angles, values, alpha=0.05, color=color)
        
        # Enhanced category labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
        
        # Enhanced y-axis
        ax.set_ylim(0, 100)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], 
                          fontsize=10, alpha=0.7)
        
        # Enhanced grid
        ax.grid(True, alpha=0.3, linewidth=1)
        ax.set_facecolor('#FAFAFA')
        
        # Enhanced title and legend
        plt.title(title, size=16, fontweight='bold', pad=30, color='#2C3E50')
        
        # Better legend positioning and styling
        legend = plt.legend(loc='center left', bbox_to_anchor=(1.15, 0.5), 
                           fontsize=10, frameon=True, fancybox=True, shadow=True)
        legend.get_frame().set_facecolor('white')
        legend.get_frame().set_alpha(0.9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
        
        plt.show()
    
    def process_click_results(self, results):
        """Process CLIcK results by category"""
        processed = {}

        for model_name, df in results.items():
            if 'correct' not in df.columns:
                continue
            if 'category' in df.columns:
                # CSV already carries the accurate category column
                category_scores = df.groupby('category')['correct'].mean() * 100
            elif 'id' in df.columns:
                # Fallback: extract category from id (e.g., "KIIP_economy_1" -> "economy")
                df['category'] = df['id'].str.extract(r'_([a-zA-Z]+)_')[0].fillna('other')
                category_scores = df.groupby('category')['correct'].mean() * 100
            else:
                continue
            processed[model_name] = category_scores.to_dict()

        return processed

    def process_kobalt_results(self, results):
        """Process KoBALT results by difficulty level"""
        processed = {}
        level_names = {1: "Easy", 2: "Moderate", 3: "Hard"}

        for model_name, df in results.items():
            if 'correct' in df.columns and 'level' in df.columns:
                df['level_name'] = df['level'].map(level_names)
                category_scores = df.groupby('level_name')['correct'].mean() * 100
                processed[model_name] = category_scores.to_dict()

        return processed
    
    def get_kmmlu_supercategory(self, category):
        """Map KMMLU category to supercategory with flexible matching"""
        category_lower = category.lower().replace('-', '').replace('_', '')
        
        # STEM categories
        stem_keywords = ['biology', 'chemical', 'chemistry', 'civil', 'computer', 'ecology', 
                        'electrical', 'information', 'materials', 'math', 'mechanical']
        
        # Applied Science categories  
        applied_keywords = ['aviation', 'electronics', 'energy', 'environmental', 'gas', 
                           'geomatics', 'industrial', 'machine', 'maritime', 'nondestructive',
                           'railway', 'automotive', 'telecommunications', 'wireless']
        
        # HUMSS categories
        humss_keywords = ['accounting', 'criminal', 'law', 'economics', 'education', 
                         'korean', 'history', 'management', 'political', 'sociology',
                         'psychology', 'social', 'welfare', 'taxation']
        
        # Check matches
        for keyword in stem_keywords:
            if keyword in category_lower:
                return 'STEM'
                
        for keyword in applied_keywords:
            if keyword in category_lower:
                return 'Applied Science'
                
        for keyword in humss_keywords:
            if keyword in category_lower:
                return 'HUMSS'
        
        # Default to Other
        return 'Other'
    
    def process_kmmlu_results(self, results):
        """Process KMMLU results by supercategory"""
        processed = {}
        
        for model_name, df in results.items():
            if 'correct' in df.columns and 'category' in df.columns:
                # Map categories to supercategories
                df['supercategory'] = df['category'].apply(self.get_kmmlu_supercategory)
                category_scores = df.groupby('supercategory')['correct'].mean() * 100
                processed[model_name] = category_scores.to_dict()
        
        return processed
    
    def process_haerae_results(self, results):
        """Process HAE-RAE results by category"""
        processed = {}

        for model_name, df in results.items():
            if 'correct' in df.columns and 'category' in df.columns:
                category_scores = df.groupby('category')['correct'].mean() * 100
                processed[model_name] = category_scores.to_dict()

        return processed

    def process_kmmlu_pro_results(self, results):
        """Process KMMLU-Pro results by license_name (supercategory)"""
        processed = {}

        for model_name, df in results.items():
            if 'correct' in df.columns and 'license_name' in df.columns:
                category_scores = df.groupby('license_name')['correct'].mean() * 100
                processed[model_name] = category_scores.to_dict()

        return processed

    def process_musr_results(self, results):
        """Process MuSR-Ko results by subset"""
        processed = {}

        for model_name, df in results.items():
            if 'correct' in df.columns and 'subset' in df.columns:
                category_scores = df.groupby('subset')['correct'].mean() * 100
                processed[model_name] = category_scores.to_dict()

        return processed

    def generate_all_charts(self, datasets=['CLIcK', 'KMMLU', 'HAERAE', 'HRM8K', 'KoBALT', 'KorMedMCQA'], top_n=None, model_filter=None):
        """Generate radar charts for all specified datasets.

        model_filter: optional list of model name substrings to restrict the comparison to
        (e.g. only the current round's models instead of every model ever benchmarked).
        """

        for dataset in datasets:
            print(f"Processing {dataset}...")

            # Read results
            results = self.read_dataset_results(dataset, model_filter=model_filter)

            if not results:
                print(f"No results found for {dataset}")
                continue

            # Process based on dataset type
            if dataset == 'CLIcK':
                processed_data = self.process_click_results(results)
            elif dataset in ['KMMLU', 'KMMLU-HARD']:
                processed_data = self.process_kmmlu_results(results)
            elif dataset == 'HAERAE':
                processed_data = self.process_haerae_results(results)
            elif dataset == 'KoBALT':
                processed_data = self.process_kobalt_results(results)
            elif dataset == 'KMMLU-Pro':
                processed_data = self.process_kmmlu_pro_results(results)
            elif dataset == 'MuSR-Ko':
                processed_data = self.process_musr_results(results)
            else:
                # Generic processing for other datasets
                processed_data = {}
                for model_name, df in results.items():
                    if 'correct' in df.columns:
                        if 'category' in df.columns:
                            category_scores = df.groupby('category')['correct'].mean() * 100
                        elif 'id' in df.columns:
                            # Try to extract category from id
                            df['category'] = df['id'].str.split('_').str[0]
                            category_scores = df.groupby('category')['correct'].mean() * 100
                        else:
                            continue
                        processed_data[model_name] = category_scores.to_dict()
            
            if processed_data:
                title = f"{dataset} Performance by Category"
                save_path = f"./charts/{dataset}_radar_chart.png"
                os.makedirs("./charts", exist_ok=True)
                self.create_radar_chart(processed_data, title, save_path, top_n=top_n)
            else:
                print(f"Could not process data for {dataset}")

if __name__ == "__main__":
    generator = RadarChartGenerator()
    generator.generate_all_charts()
