import sys
import re
import os

def cleanup_file(filepath):
    print(f"Cleaning: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Answer Quick Reference and Distribution Statistics
    # Matches "## 答案速查表" until the next separator (---) or end of file
    content = re.sub(r'## 答案速查表[\s\S]*?(?=\n---|$)', '', content)
    content = re.sub(r'## 答案總覽[\s\S]*?(?=\n---|$)', '', content)
    
    # Matches "**題目分佈統計**" until the next separator (---) or end of file
    content = re.sub(r'\*\*題目分佈統計\*\*[\s\S]*?(?=\n---|$)', '', content)

    # 2. Remove (X題) from section headers
    content = re.sub(r'\((\d+)題\)', '', content)

    # 3. Clean up the title line - remove " - 精選實戰題庫" or count
    content = re.sub(r'# (.*?) - .*', r'# \1', content)
    
    # 4. Remove extra separators if they are now consecutive
    content = re.sub(r'\n---\n\s*\n---', '\n---', content)
    
    # 5. Final trim
    content = content.strip() + "\n"

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # 6. Rename file
    # Example: L21101_自然語言_100題.md -> L21101_自然語言.md
    new_filename = re.sub(r'_(\d+)題', '', os.path.basename(filepath))
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
    
    if filepath != new_filepath:
        if os.path.exists(new_filepath):
            os.remove(new_filepath)
        os.rename(filepath, new_filepath)
        print(f"Renamed: {os.path.basename(filepath)} -> {new_filename}")
    else:
        print(f"File naming remains: {os.path.basename(filepath)}")

if __name__ == "__main__":
    files = [
        "/Users/tsai/AI-Planner-Medium/題庫/L21101_自然語言_100題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21102_電腦視覺_100題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21103_生成式AI_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21104_多模態AI_70題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21201_AI導入評估_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21202_AI導入規劃_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21203_AI風險管理_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21301_數據準備與模型選擇_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L21302_AI技術系統集成與部署_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22101_敘述性統計與資料摘要技術_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22102_機率分佈與資料分佈模型_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22103_假設檢定與統計推論_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22201_數據收集與清理_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22202_數據儲存與管理_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22203_數據處理技術與工具_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22301_統計學在大數據中的應用_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22302_常見的大數據分析方法_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22303_數據可視化工具_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22401_大數據與機器學習_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22402_大數據在鑑別式AI中的應用_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22403_大數據在生成式AI中的應用_80題.md",
        "/Users/tsai/AI-Planner-Medium/題庫/L22404_大數據隱私保護、安全與合規_80題.md"
    ]
    for f in files:
        if os.path.exists(f):
            cleanup_file(f)
        else:
            print(f"Skipping (not found): {f}")
