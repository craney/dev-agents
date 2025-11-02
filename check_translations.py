#!/usr/bin/env python3
"""
批量检查翻译文件完整性的脚本
"""

import os
import re
from pathlib import Path

def count_lines(file_path):
    """统计文件行数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except:
        return 0

def count_words(file_path):
    """统计文件单词数（中英文都算）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 简单统计：按空格和标点分割
            words = re.findall(r'\b\w+\b', content)
            return len(words)
    except:
        return 0

def extract_frontmatter(file_path):
    """提取文件的frontmatter部分"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                end = content.find('---', 3)
                if end != -1:
                    return content[:end+3]
        return ""
    except:
        return ""

def main():
    en_dir = Path('/Users/zhaohe/Documents/workspace/dev-agents/en')
    cn_dir = Path('/Users/zhaohe/Documents/workspace/dev-agents/cn')
    
    # 指定顺序的文件列表
    file_order = [
        "README.md", "ai-engineer.md", "api-documenter.md", "architect-review.md",
        "backend-architect.md", "backend-security-coder.md", "blockchain-developer.md",
        "business-analyst.md", "c-pro.md", "cloud-architect.md", "code-reviewer.md",
        "content-marketer.md", "context-manager.md", "cpp-pro.md", "csharp-pro.md",
        "customer-support.md", "data-engineer.md", "data-scientist.md",
        "database-admin.md", "database-architect.md", "database-optimizer.md",
        "debugger.md", "deployment-engineer.md", "devops-troubleshooter.md",
        "django-pro.md", "docs-architect.md", "dx-optimizer.md", "elixir-pro.md",
        "error-detective.md", "fastapi-pro.md", "flutter-expert.md",
        "frontend-developer.md", "frontend-security-coder.md", "golang-pro.md",
        "graphql-architect.md", "hr-pro.md", "hybrid-cloud-architect.md",
        "incident-responder.md", "ios-developer.md", "java-pro.md",
        "javascript-pro.md", "kubernetes-architect.md", "legacy-modernizer.md",
        "legal-advisor.md", "mermaid-expert.md", "minecraft-bukkit-pro.md",
        "ml-engineer.md", "mlops-engineer.md", "mobile-developer.md",
        "mobile-security-coder.md", "network-engineer.md", "observability-engineer.md",
        "payment-integration.md", "performance-engineer.md", "php-pro.md",
        "prompt-engineer.md", "python-pro.md", "quant-analyst.md",
        "reference-builder.md", "risk-manager.md", "ruby-pro.md", "rust-pro.md",
        "sales-automator.md", "scala-pro.md", "search-specialist.md",
        "security-auditor.md", "seo-authority-builder.md", "seo-cannibalization-detector.md",
        "seo-content-auditor.md", "seo-content-planner.md", "seo-content-refresher.md",
        "seo-content-writer.md", "seo-keyword-strategist.md", "seo-meta-optimizer.md",
        "seo-snippet-hunter.md", "seo-structure-architect.md", "sql-pro.md",
        "tdd-orchestrator.md", "terraform-specialist.md", "test-automator.md",
        "tutorial-engineer.md", "typescript-pro.md", "ui-ux-designer.md",
        "ui-visual-validator.md", "unity-developer.md"
    ]
    
    print("翻译文件检查报告")
    print("=" * 80)
    print(f"{'文件名':<30} {'英文行数':<10} {'中文行数':<10} {'英文词数':<10} {'中文词数':<10} {'状态':<15}")
    print("-" * 80)
    
    total_files = 0
    complete_files = 0
    issues_found = []
    
    for filename in file_order:
        en_file = en_dir / filename
        cn_file = cn_dir / filename
        
        if not en_file.exists():
            print(f"{filename:<30} 英文文件不存在")
            continue
            
        if not cn_file.exists():
            print(f"{filename:<30} 中文文件缺失")
            issues_found.append(f"{filename}: 中文文件缺失")
            continue
        
        total_files += 1
        
        # 统计行数和词数
        en_lines = count_lines(en_file)
        cn_lines = count_lines(cn_file)
        en_words = count_words(en_file)
        cn_words = count_words(cn_file)
        
        # 检查frontmatter
        en_fm = extract_frontmatter(en_file)
        cn_fm = extract_frontmatter(cn_file)
        
        # 判断翻译状态
        status = "完整"
        if cn_lines < en_lines * 0.8:  # 如果中文行数明显少于英文，可能不完整
            status = "可能不完整"
            issues_found.append(f"{filename}: 内容可能不完整")
        elif "name:" not in cn_fm:
            status = "格式问题"
            issues_found.append(f"{filename}: frontmatter格式问题")
        elif cn_words < en_words * 0.6:  # 如果中文词数明显少于英文
            status = "可能不完整"
            issues_found.append(f"{filename}: 内容可能不完整")
        else:
            complete_files += 1
        
        print(f"{filename:<30} {en_lines:<10} {cn_lines:<10} {en_words:<10} {cn_words:<10} {status:<15}")
    
    print("-" * 80)
    print(f"总计检查文件: {total_files}")
    print(f"完整翻译文件: {complete_files}")
    print(f"有问题的文件: {len(issues_found)}")
    
    if issues_found:
        print("\n问题详情:")
        for issue in issues_found:
            print(f"  - {issue}")

if __name__ == "__main__":
    main()