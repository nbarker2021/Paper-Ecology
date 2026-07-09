"""Fix maximal manuscript index to match CMPLX-Standards model contract.

The MAXIMAL_FLCR_INDEX.json was generated with field names that don't match
the cmplx.maximal_manuscript model. This script reads each manuscript .md,
checks for required sections, and rebuilds the index with correct fields.
"""

import json
import re
from pathlib import Path

MAXIMAL_DIR = Path(r"D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\MAXIMAL_FLCR_MANUSCRIPTS")
INDEX_PATH = MAXIMAL_DIR / "MAXIMAL_FLCR_INDEX.json"

def check_sections(md_text: str) -> dict[str, bool]:
    """Check for required sections in manuscript markdown."""
    lines = md_text.split('\n')
    headers = [line.lower() for line in lines if line.startswith('## ')]
    headers_text = '\n'.join(headers)
    
    return {
        "has_abstract": "## abstract" in headers_text,
        "has_main_results": "## main results" in headers_text,
        "has_construction": bool(re.search(r'## \d*\.?\s*construction', headers_text)),
        "has_downstream_program": bool(re.search(r'## \d*\.?\s*dependencies and downstream', headers_text)),
        "has_active_channels": "## active research channels" in headers_text,
        "has_methods_note": bool(re.search(r'## \d*\.?\s*(methods|source routing|paper.specific development)', headers_text)),
        "has_evidence_appendix": bool(re.search(r'## \d*\.?\s*evidence and receipts', headers_text)),
        "has_assembled_link": False,  # Will be set from index entry
    }

def fix_product(product: dict) -> dict:
    """Update product record to match CMPLX-Standards model."""
    # Read the manuscript file
    md_path = Path(product.get("path", ""))
    if not md_path.exists():
        md_path = MAXIMAL_DIR / md_path.name
    
    sections = {}
    if md_path.exists():
        md_text = md_path.read_text(encoding="utf-8")
        sections = check_sections(md_text)
    
    # Build corrected record
    fixed = {
        "paper_id": product.get("paper_id", ""),
        "title": product.get("title", ""),
        "prose_tier": product.get("prose_tier", "maximal_publication"),
        "has_abstract": sections.get("has_abstract", False),
        "has_main_results": sections.get("has_main_results", False),
        "has_construction": product.get("has_construction", sections.get("has_construction", False)),
        "has_downstream_program": product.get("has_downstream", sections.get("has_downstream_program", False)),
        "has_active_channels": sections.get("has_active_channels", False),
        "has_methods_note": sections.get("has_methods_note", False),
        "has_evidence_appendix": sections.get("has_evidence_appendix", False),
        "has_assembled_link": bool(product.get("assembled_link")),
        "claim_count": product.get("claim_count", 0),
        "receipt_count": product.get("receipt_count", 0),
    }
    return fixed

def main():
    print("=== Fixing Maximal Manuscript Index ===")
    
    # Load existing index
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    products = index.get("products", [])
    print(f"Found {len(products)} products in index")
    
    # Fix each product
    fixed_records = []
    for product in products:
        fixed = fix_product(product)
        fixed_records.append(fixed)
        print(f"  {fixed['paper_id']}: abstract={fixed['has_abstract']}, main_results={fixed['has_main_results']}, "
              f"construction={fixed['has_construction']}, downstream={fixed['has_downstream_program']}, "
              f"channels={fixed['has_active_channels']}, methods={fixed['has_methods_note']}, "
              f"evidence={fixed['has_evidence_appendix']}, assembled={fixed['has_assembled_link']}")
    
    # Build payload
    payload = {
        "schema": "cmplx_standards_maximal_manuscript_payload.v1",
        "source_dir": str(MAXIMAL_DIR),
        "record_count": len(fixed_records),
        "records": fixed_records,
    }
    
    # Save payload
    payload_path = MAXIMAL_DIR / "MAXIMAL_FLCR_INDEX_FIXED.json"
    with open(payload_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
    
    print(f"\nFixed payload saved: {payload_path}")
    print(f"Records: {len(fixed_records)}")
    
    # Also save as the standard index format (with products array)
    index["products"] = fixed_records
    index["fixed_at"] = "2026-07-03T19:30:00+00:00"
    index["fix_reason"] = "Aligned field names with CMPLX-Standards maximal_manuscript_model.json"
    
    fixed_index_path = MAXIMAL_DIR / "MAXIMAL_FLCR_INDEX.json"
    # Backup original
    backup_path = MAXIMAL_DIR / "MAXIMAL_FLCR_INDEX.json.bak"
    if not backup_path.exists():
        import shutil
        shutil.copy(fixed_index_path, backup_path)
        print(f"Original backed up to: {backup_path}")
    
    with open(fixed_index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    
    print(f"Index updated: {fixed_index_path}")
    
    # Quick stats
    perfect = sum(1 for r in fixed_records if all([
        r["has_abstract"], r["has_main_results"], r["has_construction"],
        r["has_downstream_program"], r["has_active_channels"],
        r["has_evidence_appendix"], r["has_assembled_link"]
    ]))
    print(f"\nRecords with all key sections: {perfect}/{len(fixed_records)}")

if __name__ == '__main__':
    main()
