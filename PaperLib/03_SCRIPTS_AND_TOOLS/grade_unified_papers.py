import os
import re
import sys
import json
import sqlite3
from pathlib import Path

# Add CMPLX-Standards to path
STANDARDS_DIR = r"D:\CQE_CMPLX\CMPLX-Standards"
if STANDARDS_DIR not in sys.path:
    sys.path.insert(0, STANDARDS_DIR)

from cmplx_standards import grade_payload, load_json

PAPERLIB = r"D:\PaperLib"

def build_paper_payload():
    """Build payload from unified papers for CMPLX-Standards grading."""
    papers = []
    
    for f in os.listdir(PAPERLIB):
        if not f.endswith('.md') or not f.startswith('paper-'):
            continue
        m = re.match(r'paper-(\d{2,3})__', f)
        if not m:
            continue
        num = int(m.group(1))
        path = os.path.join(PAPERLIB, f)
        
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        
        # Extract band
        band = "Unknown"
        band_match = re.search(r'\*\*Band\*\*:\s*(.+)', content)
        if band_match:
            band = band_match.group(1).strip()
        
        # Check for required sections
        has_header = bool(re.search(r'#{1,3}\s+.*Header', content, re.IGNORECASE))
        has_claim_ledger = 'Claim Ledger' in content
        has_definitions = 'Definitions' in content
        has_theorems = 'Theorems' in content or 'Theorem' in content
        has_hand_reconstruction = 'Hand Reconstruction' in content
        has_rejected_claims = 'Rejected Claims' in content
        has_relation = 'Relation to Later Papers' in content
        has_open_obligations = 'Open Obligations' in content
        has_bibliography = 'Bibliography' in content
        has_dix = 'Data vs. Interpretation' in content or 'Data vs Interpretation' in content
        has_python_verifiers = '```python' in content or 'def verify_' in content
        has_unified_refs = 'Paper 4' in content and 'Paper 5' in content
        
        # Check for SM-specific content
        has_lattice = 'lattice code chain' in content.lower() or '1→3→7→8→24→72' in content
        has_triality = 'triality' in content.lower() or 'D4' in content
        has_sm_sector = 'SU(3)' in content or 'SU(2)' in content or 'U(1)' in content
        has_gauge = 'gauge group' in content.lower() or 'gauge boson' in content.lower()
        has_millennium = 'Millennium Prize' in content or 'Clay Mathematics' in content
        has_bounded = 'closed-now' in content or 'bounded' in content.lower()
        
        paper_record = {
            "canonical_id": f"Paper {num}",
            "paper_number": num,
            "title": content.split('\n')[0].strip('# '),
            "band": band,
            "header": has_header,
            "claim_ledger": has_claim_ledger,
            "definitions": has_definitions,
            "theorems": has_theorems,
            "hand_reconstruction": has_hand_reconstruction,
            "rejected_claims": has_rejected_claims,
            "relation_to_later_papers": has_relation,
            "open_obligations": has_open_obligations,
            "bibliography": has_bibliography,
            "data_vs_interpretation": has_dix,
            "python_verifiers": has_python_verifiers,
            "cross_references_unified": has_unified_refs,
            "lattice_code_chain": has_lattice,
            "triality_surface": has_triality,
            "standard_model_sector": has_sm_sector,
            "gauge_group": has_gauge,
            "millennium_prize_status": has_millennium,
            "bounded_validation": has_bounded
        }
        papers.append(paper_record)
    
    return {
        "schema": "cmplx_standards_unified_paper_payload.v1",
        "source_dir": PAPERLIB,
        "record_count": len(papers),
        "papers": papers
    }

def main():
    print("=== Building Unified Paper Payload ===")
    payload = build_paper_payload()
    
    # Save payload
    payload_path = os.path.join(PAPERLIB, "unified_paper_payload.json")
    with open(payload_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
    print(f"Payload saved: {payload_path}")
    print(f"Records: {payload['record_count']}")
    
    # Load model
    model_path = os.path.join(PAPERLIB, "models", "unified_paper_model.json")
    model = load_json(Path(model_path))
    
    # Grade
    print("\n=== Grading Against CMPLX-Standards ===")
    report = grade_payload(payload, model)
    
    # Save report
    report_path = os.path.join(PAPERLIB, "CMPLX_STANDARDS_UNIFIED_PAPER_REPORT.json")
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    summary = report["summary"]
    print(f"\n{'='*60}")
    print(f"CMPLX-Standards Unified Paper Report")
    print(f"{'='*60}")
    print(f"Records: {summary['record_count']}")
    print(f"Average fit: {summary['average_fit_score']:.2f}")
    print(f"Average distance to perfect: {summary['average_distance_to_perfect']:.4f}")
    print(f"\nInclusion Bands:")
    for band, count in summary['bands'].items():
        print(f"  {band}: {count}")
    
    # Show lowest-fit papers
    print(f"\nLowest-Fit Papers (need attention):")
    for grade in sorted(report['grades'], key=lambda x: x['fit_score'])[:10]:
        print(f"  {grade['record_id']}: fit={grade['fit_score']:.2f}, band={grade['inclusion_band']}, missing={len(grade['missing_fields'])}")
    
    print(f"\nReport saved: {report_path}")
    return {"status": "complete", "report_path": report_path}

if __name__ == '__main__':
    main()
