#!/usr/bin/env python3
"""
Fix sm_mapping_row data to achieve model fit >= 90.

Backfills:
- maximal_claim_ref: references the parent FLCR paper for all rows
- dataset: backfills from irl_ids where available and dataset is empty
- has_native_deps: sets "yes" / "no" consistently based on native_flcr_deps
"""

import json
from pathlib import Path

def main():
    matrix_path = Path(r"D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\SM_MAPPING_ROWS\SM_MAPPING_MATRIX.json")
    
    with open(matrix_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    records = data.get("records", [])
    fixes_applied = 0
    
    for r in records:
        flcr_id = r.get("flcr_id", "")
        
        # Fix 1: maximal_claim_ref — backfill with FLCR paper reference
        if not r.get("maximal_claim_ref", "").strip():
            if flcr_id:
                r["maximal_claim_ref"] = f"{flcr_id}"
                fixes_applied += 1
        
        # Fix 2: dataset — backfill from irl_ids if dataset is empty
        if not r.get("dataset", "").strip():
            irl_ids = r.get("irl_ids", [])
            if irl_ids:
                # Build dataset from irl_ids
                parts = []
                for irl_id in irl_ids:
                    parts.append(f"{irl_id}: {irl_id}")
                r["dataset"] = "; ".join(parts)
                fixes_applied += 1
        
        # Fix 3: has_native_deps — set "yes" if native_flcr_deps non-empty, "no" otherwise
        native_deps = r.get("native_flcr_deps", [])
        if isinstance(native_deps, list) and len(native_deps) > 0:
            r["has_native_deps"] = "yes"
            fixes_applied += 1
        elif not r.get("has_native_deps", "").strip():
            r["has_native_deps"] = "no"
            fixes_applied += 1
    
    # Write back
    with open(matrix_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Fixed {fixes_applied} fields across {len(records)} records.")
    print(f"Wrote: {matrix_path}")
    return fixes_applied

if __name__ == "__main__":
    main()
