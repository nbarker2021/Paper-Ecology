#!/usr/bin/env python3
"""
CMPLX Paper Variant Discovery Script
====================================
Scans all source directories across D drive for paper variants,
groups them by paper number, and produces a structured report
for consolidation workflow.

Usage:
    python variant_discovery.py --block 0    # Papers 0-2
    python variant_discovery.py --block 1    # Papers 3-5
    python variant_discovery.py --block 2    # Papers 6-8
    python variant_discovery.py --paper 3  # All variants of Paper 3
    python variant_discovery.py --all      # Full report (0-100)

Output:
    D:\PaperLib\scripts\output\variant_report_block_N.json
    D:\PaperLib\scripts\output\variant_report_block_N.md
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Configuration: directories to scan for paper variants
# ---------------------------------------------------------------------------
SCAN_ROOTS = [
    Path("D:/CQE_CMPLX/papers/UFT0-100"),
    Path("D:/CQE_CMPLX/CQECMPLX-Production/papers"),
    Path("D:/CQE_CMPLX/CQE-CMPLX-1T-Production/src/papers/source_backup"),
    Path("D:/CQE_CMPLX/CQECMPLX-Formal-Suite"),
    Path("D:/CQE_CMPLX/CQECMPLX-AirLock/forgefactory-v0.3-lineage-read/ForgeFactory_v0_3"),
    Path("D:/CQE_CMPLX/CMPLX-PartsFactory-main/papers"),
    Path("D:/CQE_CMPLX/papers"),
    Path("D:/PaperLib"),
]

OUTPUT_DIR = Path("D:/PaperLib/scripts/output")

# Regex patterns for paper number extraction
PAPER_PATTERNS = [
    # paper_03, paper_3, paper03, paper3
    re.compile(r'paper[_\-]?(\d+)', re.IGNORECASE),
    # uft_04, uft04
    re.compile(r'uft[_\-]?(\d+)', re.IGNORECASE),
    # 04__d4_j3o, 4__d4_j3o
    re.compile(r'^(\d{1,3})__', re.IGNORECASE),
    # P4_, P04_, p4_, p04_
    re.compile(r'[pP](\d{1,3})[_\-]', re.IGNORECASE),
    # 04_d4, 4_d4 (leading digits with separator)
    re.compile(r'^(\d{1,3})[_\-][a-zA-Z]', re.IGNORECASE),
]

PRIORITY_KEYWORDS = {
    'unified': 10,
    'final': 9,
    'verified': 8,
    'receipt': 7,
    'complete': 6,
    'consolidated': 5,
    'source_backup': 4,
    'production': 3,
    'uft': 2,
    'draft': 1,
    'old': 0,
    'archive': 0,
    'stale': -1,
}


def extract_paper_number(filename: str) -> Optional[int]:
    """Extract paper number (0-100) from filename."""
    base = Path(filename).stem
    for pattern in PAPER_PATTERNS:
        match = pattern.search(base)
        if match:
            num = int(match.group(1))
            if 0 <= num <= 100:
                return num
    return None


def score_variant(file_path: Path, content: Optional[str] = None) -> int:
    """Score a variant file by quality heuristics. Higher = better."""
    score = 0
    name_lower = file_path.name.lower()
    
    # Priority keywords in filename
    for keyword, value in PRIORITY_KEYWORDS.items():
        if keyword in name_lower:
            score += value
    
    # File size (larger papers tend to be more complete)
    try:
        size = file_path.stat().st_size
        if size > 100_000:
            score += 5
        elif size > 50_000:
            score += 3
        elif size > 20_000:
            score += 1
        elif size < 1000:
            score -= 2
    except OSError:
        pass
    
    # Extension preference
    if name_lower.endswith('.md'):
        score += 2
    elif name_lower.endswith('.txt'):
        score += 1
    elif name_lower.endswith('.py'):
        score -= 1  # Code files are not the paper itself
    
    # Content quality indicators (if content available)
    if content:
        if 'Abstract' in content or 'ABSTRACT' in content:
            score += 2
        if 'Theorem' in content:
            score += 2
        if '## ' in content or '# ' in content:
            score += 1
        if 'Proof.' in content:
            score += 1
        if 'QED' in content or '∎' in content:
            score += 1
    
    return score


def scan_directory(root: Path) -> Dict[int, List[dict]]:
    """Scan a directory tree and group files by paper number."""
    variants: Dict[int, List[dict]] = {}
    
    if not root.exists():
        return variants
    
    for file_path in root.rglob('*'):
        if not file_path.is_file():
            continue
        
        # Skip non-text files and build artifacts
        if file_path.suffix.lower() not in ('.md', '.txt', '.rst', '.tex', '.html'):
            continue
        
        # Skip very small files (likely stubs)
        try:
            if file_path.stat().st_size < 200:
                continue
        except OSError:
            continue
        
        paper_num = extract_paper_number(file_path.name)
        if paper_num is None:
            continue
        
        # Read first 2KB for content scoring
        content = None
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')[:2048]
        except Exception:
            pass
        
        score = score_variant(file_path, content)
        
        variant = {
            'path': str(file_path),
            'filename': file_path.name,
            'size': file_path.stat().st_size,
            'score': score,
            'source_dir': str(root),
        }
        
        variants.setdefault(paper_num, []).append(variant)
    
    return variants


def merge_variants(all_scans: List[Dict[int, List[dict]]]) -> Dict[int, List[dict]]:
    """Merge variant dictionaries from multiple scans."""
    merged: Dict[int, List[dict]] = {}
    for scan in all_scans:
        for num, variants in scan.items():
            merged.setdefault(num, []).extend(variants)
    
    # Sort each paper's variants by score descending
    for num in merged:
        merged[num].sort(key=lambda v: v['score'], reverse=True)
        # Deduplicate by path
        seen = set()
        deduped = []
        for v in merged[num]:
            if v['path'] not in seen:
                seen.add(v['path'])
                deduped.append(v)
        merged[num] = deduped
    
    return merged


def generate_report(merged: Dict[int, List[dict]], block: Optional[int] = None) -> Tuple[str, str]:
    """Generate JSON and Markdown reports."""
    
    if block is not None:
        start, end = block * 3, block * 3 + 2
        papers = {k: v for k, v in merged.items() if start <= k <= end}
        report_name = f"block_{block}"
    else:
        papers = merged
        report_name = "full"
    
    # JSON report
    json_path = OUTPUT_DIR / f"variant_report_{report_name}.json"
    json_path.write_text(json.dumps({
        'generated': datetime.now().isoformat(),
        'scan_roots': [str(r) for r in SCAN_ROOTS],
        'paper_count': len(papers),
        'variant_count': sum(len(v) for v in papers.values()),
        'papers': {
            str(k): {
                'variant_count': len(v),
                'top_variants': v[:5],  # Top 5 by score
                'best_guess': v[0]['path'] if v else None,
            }
            for k, v in sorted(papers.items())
        }
    }, indent=2, default=str), encoding='utf-8')
    
    # Markdown report
    md_lines = [
        f"# CMPLX Variant Discovery Report: {report_name.upper().replace('_', ' ')}",
        f"**Generated:** {datetime.now().isoformat()}",
        f"**Scan Roots:** {len(SCAN_ROOTS)} directories",
        f"**Papers Found:** {len(papers)} | **Total Variants:** {sum(len(v) for v in papers.values())}",
        "",
        "---",
        "",
    ]
    
    for num in sorted(papers.keys()):
        variants = papers[num]
        md_lines.extend([
            f"## Paper {num}",
            f"**Variants:** {len(variants)} | **Best Guess:** `{variants[0]['filename'] if variants else 'N/A'}`",
            "",
            "| Rank | Filename | Source | Size | Score |",
            "|------|----------|--------|------|-------|",
        ])
        for i, v in enumerate(variants[:10], 1):
            src = Path(v['source_dir']).name
            md_lines.append(f"| {i} | `{v['filename']}` | {src} | {v['size']:,} | {v['score']} |")
        if len(variants) > 10:
            md_lines.append(f"| ... | *({len(variants) - 10} more variants)* | | | |")
        md_lines.append("")
    
    md_path = OUTPUT_DIR / f"variant_report_{report_name}.md"
    md_path.write_text('\n'.join(md_lines), encoding='utf-8')
    
    return str(json_path), str(md_path)


def main():
    parser = argparse.ArgumentParser(description='CMPLX Paper Variant Discovery')
    parser.add_argument('--block', type=int, help='Process block N (papers N*3 to N*3+2)')
    parser.add_argument('--paper', type=int, help='Process single paper number')
    parser.add_argument('--all', action='store_true', help='Process all papers 0-100')
    parser.add_argument('--scan', action='store_true', help='Run scan and save full cache')
    args = parser.parse_args()
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Full scan
    print("Scanning for paper variants across all source directories...")
    all_scans = []
    for root in SCAN_ROOTS:
        if root.exists():
            variants = scan_directory(root)
            if variants:
                print(f"  {root}: {len(variants)} papers, {sum(len(v) for v in variants.values())} variants")
                all_scans.append(variants)
        else:
            print(f"  {root}: [MISSING — skipped]")
    
    merged = merge_variants(all_scans)
    print(f"\nTotal: {len(merged)} papers, {sum(len(v) for v in merged.values())} variants")
    
    # Save full cache
    cache_path = OUTPUT_DIR / "variant_cache.json"
    cache_path.write_text(json.dumps({
        'generated': datetime.now().isoformat(),
        'papers': {
            str(k): v for k, v in sorted(merged.items())
        }
    }, indent=2, default=str), encoding='utf-8')
    print(f"Full cache saved: {cache_path}")
    
    # Generate reports
    if args.paper is not None:
        if args.paper in merged:
            papers = {args.paper: merged[args.paper]}
            json_path, md_path = generate_report(papers)
            print(f"\nPaper {args.paper} report:")
            print(f"  JSON: {json_path}")
            print(f"  MD:   {md_path}")
            print(f"  Variants: {len(merged[args.paper])}")
            for v in merged[args.paper][:5]:
                print(f"    - {v['filename']} ({v['size']:,} bytes, score {v['score']})")
        else:
            print(f"Paper {args.paper} not found in any scanned directory.")
            sys.exit(1)
    
    elif args.block is not None:
        start, end = args.block * 3, args.block * 3 + 2
        papers = {k: v for k, v in merged.items() if start <= k <= end}
        json_path, md_path = generate_report(papers, block=args.block)
        print(f"\nBlock {args.block} (Papers {start}-{end}) report:")
        print(f"  JSON: {json_path}")
        print(f"  MD:   {md_path}")
        for k in sorted(papers.keys()):
            print(f"  Paper {k}: {len(papers[k])} variants")
    
    elif args.all:
        json_path, md_path = generate_report(merged)
        print(f"\nFull report (0-100):")
        print(f"  JSON: {json_path}")
        print(f"  MD:   {md_path}")
    
    else:
        # Default: show summary
        print("\nUsage: python variant_discovery.py --block N | --paper N | --all")
        print("\nTop papers by variant count:")
        sorted_papers = sorted(merged.items(), key=lambda x: len(x[1]), reverse=True)
        for num, variants in sorted_papers[:20]:
            best = variants[0]
            print(f"  Paper {num:3d}: {len(variants):3d} variants — best: {best['filename']} ({best['size']:,} bytes)")


if __name__ == '__main__':
    main()
