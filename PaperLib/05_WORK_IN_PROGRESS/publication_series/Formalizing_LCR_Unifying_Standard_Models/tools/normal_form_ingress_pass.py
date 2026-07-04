#!/usr/bin/env python3
"""Build the normal-form ingress matrix for non-receipt-bound obligations.

This pass is intentionally conservative. It does not promote any obligation to
ASSEMBLE. It creates the missing review surface between open/citation/CAM/
calibration obligations and the CMPLX-Standards validation layer: a generalized
normal form, a paper-local normal form, an advanced form, and an explicit FLCR
conversion rule for each row that is not already receipt-bound.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
OBLIGATION_PATH = SERIES_ROOT / "OBLIGATION_ROWS.json"
OUT_JSON = SERIES_ROOT / "NORMAL_FORM_INGRESS_MATRIX.json"
OUT_MD = SERIES_ROOT / "NORMAL_FORM_INGRESS_MATRIX.md"
PROTOCOL_MD = SERIES_ROOT / "NORMAL_FORM_INGRESS_PROTOCOL.md"


LANE_FAMILIES = {
    "receipt_bound_internal_result": "receipt_replay",
    "standard_theorem_citation_bound_result": "standard_import",
    "cam_crystal_reapplication_result": "cam_reapplication",
    "normal_form_result": "normal_form_derivation",
    "external_calibration_result": "external_calibration",
    "grand_synthesis_claim": "cross_paper_synthesis",
    "falsifier_or_open_obligation": "residue_falsifier",
    "ledger_action": "ledger_action",
}


ADVANCED_FORM_BY_FAMILY = {
    "standard_import": "citation-conservative-extension form",
    "cam_reapplication": "memory-route replay form",
    "normal_form_derivation": "Kimi window/tower normal form",
    "external_calibration": "unit-bearing comparator form",
    "cross_paper_synthesis": "dependency-braided synthesis form",
    "residue_falsifier": "negative-space falsifier form",
    "ledger_action": "obligation-ledger action form",
}


GATE_BY_FAMILY = {
    "standard_import": "citation target, object mapping, and conservative-extension boundary",
    "receipt_replay": "receipt path, verifier name, replay scope, and content-address check",
    "cam_reapplication": "CAM/crystal source, routing path, replay data, and boundary",
    "normal_form_derivation": "standard normal form, paper normal form, conversion rule, and falsifier",
    "external_calibration": "dataset, units, uncertainty/comparator, and pass/fail criteria",
    "cross_paper_synthesis": "dependency papers, dependency lanes, residual obligations, and falsifier",
    "residue_falsifier": "explicit failure condition, next binding action, and owner surface",
    "ledger_action": "ledger row type, import/export rule, affected obligation ids, and validator receipt",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def slug(text: str, limit: int = 40) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").upper()
    return value[:limit] or "ROW"


def paper_title(flcr_id: str) -> str:
    formal = SERIES_ROOT / flcr_id / "formal.md"
    if not formal.exists():
        return flcr_id
    for line in formal.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return flcr_id


def normalize_claim_text(text: str) -> str:
    return " ".join(text.strip().split())


def build_entry(row: dict[str, Any]) -> dict[str, Any]:
    flcr_id = row["flcr_id"]
    evidence = row.get("evidence_type_needed", "unknown")
    family = LANE_FAMILIES.get(evidence, "unclassified")
    deps = row.get("prior_paper_deps", [])
    claim_text = normalize_claim_text(row.get("claim_text", ""))
    oid = row["obligation_id"]
    title = paper_title(flcr_id)
    source_section = row.get("source_section", "unspecified")
    gate_material = GATE_BY_FAMILY.get(family, "validator-defined gate")

    standard_form = {
        "id": f"KNF-GENERAL-{family.upper()}",
        "name": "generalized Kimi normal form",
        "tuple": [
            "source_identity",
            "typed_object",
            "operation_or_relation",
            "evidence_lane",
            "dependency_set",
            "scope_boundary",
            "falsifier_or_residue",
            "validator_gate",
        ],
        "acceptance_rule": (
            "The row is reviewable only when all tuple fields are explicit and "
            "the validator gate can reject the conversion without interpreting prose."
        ),
    }

    paper_form = {
        "id": f"KNF-{flcr_id}-{slug(oid)}",
        "name": "paper-specific Kimi normal form",
        "paper": flcr_id,
        "paper_title": title,
        "source_section": source_section,
        "typed_object": title.split(" - ", 1)[-1],
        "statement": claim_text,
        "dependencies": deps,
        "local_boundary": (
            "The claim is paper-local until the conversion rule and validator gate "
            "show what downstream papers may import."
        ),
    }

    advanced_form = {
        "id": f"ANF-{flcr_id}-{slug(oid)}",
        "name": ADVANCED_FORM_BY_FAMILY.get(family, "validator-specific advanced form"),
        "window_form": {
            "left_context": deps or [flcr_id],
            "center_claim": claim_text,
            "right_residue": gate_material,
        },
        "octad_review_vector": {
            "source": source_section,
            "object": title,
            "operation": family,
            "lane": evidence,
            "dependencies": deps,
            "boundary": "no physical or cross-paper promotion without this gate",
            "falsifier": gate_material,
            "validator": "paper.normal_form_conversion",
        },
    }

    conversion_rule = {
        "id": f"FLCR-CONVERT-{flcr_id}-{slug(oid)}",
        "source_language": "paper prose / obligation row",
        "target_language": "FLCR algebra and claim-lane formal language",
        "steps": [
            "parse claim into source_identity, typed_object, operation_or_relation, and evidence_lane",
            "build the paper-specific Kimi normal form from the paper object and source section",
            "lift the paper-specific form into the generalized Kimi normal form tuple",
            "assign FLCR algebra: L=source/provenance/dependencies, C=typed claim operator, R=residue/falsifier/validator gate",
            "emit a validator-readable claim envelope with scope boundary and rejection condition",
        ],
        "flcr_algebra": {
            "L": {
                "meaning": "left/source/provenance side",
                "value": {"paper": flcr_id, "source_section": source_section, "dependencies": deps},
            },
            "C": {
                "meaning": "center/carrier claim operator",
                "value": {"family": family, "lane": evidence, "statement": claim_text},
            },
            "R": {
                "meaning": "right/residue/falsifier side",
                "value": {"gate": gate_material, "status": row.get("status", "unknown")},
            },
        },
    }

    standards_gate = {
        "standard_id": "paper.normal_form_conversion",
        "status": "PENDING",
        "required_material": gate_material,
        "promotion_rule": (
            "A PASS permits movement into the appropriate receipt/citation/CAM/"
            "calibration review queue. It does not by itself grant ASSEMBLE."
        ),
        "failure_rule": "A FAIL or missing field keeps the obligation staged_open.",
    }

    return {
        "obligation_id": oid,
        "flcr_id": flcr_id,
        "source_status": row.get("status", "unknown"),
        "evidence_type_needed": evidence,
        "claim_family": family,
        "claim_text": claim_text,
        "standard_normal_form": standard_form,
        "paper_specific_normal_form": paper_form,
        "advanced_normal_form": advanced_form,
        "flcr_conversion_rule": conversion_rule,
        "cmplx_standards_gate": standards_gate,
        "nist_nsit_validator_gate": standards_gate,
        "promotion_status": "blocked_until_normal_form_review",
    }


def build_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Normal Form Ingress Matrix")
    lines.append("")
    lines.append(f"Generated: `{payload['generated_utc']}`")
    lines.append("")
    lines.append("Scope: every row in `OBLIGATION_ROWS.json` that is not `receipt_bound`.")
    lines.append("")
    lines.append("This pass does not promote rows to ASSEMBLE. It creates the missing")
    lines.append("validator surface for rows that need normal-form conversion before any")
    lines.append("receipt, citation, CAM, calibration, synthesis, or falsifier closure.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    s = payload["summary"]
    lines.append(f"- Total obligation rows: `{s['total_obligation_rows']}`")
    lines.append(f"- Receipt-bound rows excluded: `{s['receipt_bound_rows_excluded']}`")
    lines.append(f"- Normal-form ingress rows: `{s['normal_form_ingress_rows']}`")
    lines.append(f"- Papers represented: `{s['papers_represented']}`")
    lines.append("")
    lines.append("### Rows By Claim Family")
    lines.append("")
    lines.append("| Claim family | Rows |")
    lines.append("|---|---:|")
    for family, count in sorted(s["rows_by_claim_family"].items()):
        lines.append(f"| `{family}` | {count} |")
    lines.append("")
    lines.append("### Rows By FLCR")
    lines.append("")
    lines.append("| FLCR | Rows | Dominant family |")
    lines.append("|---|---:|---|")
    for flcr, row in sorted(s["rows_by_flcr"].items()):
        lines.append(f"| `{flcr}` | {row['count']} | `{row['dominant_family']}` |")
    lines.append("")
    lines.append("## Validator Contract")
    lines.append("")
    lines.append("The CMPLX-Standards layer needs a new standard named")
    lines.append("`paper.normal_form_conversion`. A row passes that standard only when it has:")
    lines.append("")
    lines.append("1. A generalized Kimi normal form.")
    lines.append("2. A paper-specific Kimi normal form.")
    lines.append("3. An advanced form appropriate to its evidence family.")
    lines.append("4. An explicit FLCR conversion rule.")
    lines.append("5. A falsifier, residue, citation target, dataset/comparator, or replay gate.")
    lines.append("")
    lines.append("A pass through this standard moves a row into the next evidence queue. It")
    lines.append("does not directly grant ASSEMBLE.")
    lines.append("")
    lines.append("## First Rows")
    lines.append("")
    lines.append("| Obligation | Family | Gate |")
    lines.append("|---|---|---|")
    for entry in payload["entries"][:40]:
        gate = entry["cmplx_standards_gate"]["required_material"]
        lines.append(f"| `{entry['obligation_id']}` | `{entry['claim_family']}` | {gate} |")
    lines.append("")
    lines.append("Full machine-readable rows are in `NORMAL_FORM_INGRESS_MATRIX.json`.")
    lines.append("")
    return "\n".join(lines)


def build_protocol() -> str:
    return """# Normal Form Ingress Protocol

Status: active gate for non-receipt-bound obligations.

Purpose: make every non-receipt-bound paper obligation validator-readable before
it can become an FLCR claim. This is the missing layer between open prose and
CMPLX-Standards validation.

## Required Forms

Each obligation must carry all four forms below.

1. Generalized Kimi normal form: the standard tuple used across the whole
   series: source identity, typed object, operation or relation, evidence lane,
   dependency set, scope boundary, falsifier or residue, and validator gate.
2. Paper-specific Kimi normal form: the same claim expressed in the local paper's
   object language, section, dependencies, and import boundary.
3. Advanced normal form: the lane-specific refinement. Examples include
   citation-conservative-extension form, memory-route replay form, unit-bearing
   comparator form, dependency-braided synthesis form, and negative-space
   falsifier form.
4. FLCR conversion rule: the explicit conversion into FLCR algebra:
   L=source/provenance/dependencies, C=typed claim operator, and
   R=residue/falsifier/validator gate.

## CMPLX-Standards Standard To Add

`paper.normal_form_conversion`

PASS means the conversion is explicit enough that a validator can reject it
without interpreting free prose. PASS does not grant ASSEMBLE; it routes the row
to the next evidence queue.

FAIL means the row remains `staged_open`.

OPEN means the row has not yet been supplied with one or more of the required
forms.

## Promotion Discipline

Normal-form review is not a substitute for receipts, citations, calibration
data, or falsifiers. It is the legal ingress that decides which of those
evidence paths is actually required and makes the conversion auditable.
"""


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Build normal-form ingress matrix.")
    parser.add_argument(
        "--top-batch",
        type=int,
        default=0,
        help="Limit output entries to top N rows (0 = all non-receipt-bound rows)",
    )
    args = parser.parse_args()

    obligations = load_json(OBLIGATION_PATH)
    rows = obligations["rows"]
    entries = [build_entry(row) for row in rows if row.get("status") != "receipt_bound"]
    if args.top_batch > 0:
        entries = entries[: args.top_batch]

    by_family = Counter(entry["claim_family"] for entry in entries)
    by_flcr_entries: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        by_flcr_entries[entry["flcr_id"]].append(entry)

    rows_by_flcr = {}
    for flcr, items in by_flcr_entries.items():
        family_counter = Counter(item["claim_family"] for item in items)
        rows_by_flcr[flcr] = {
            "count": len(items),
            "dominant_family": family_counter.most_common(1)[0][0],
            "families": dict(sorted(family_counter.items())),
        }

    payload = {
        "schema": "flcr_normal_form_ingress_matrix.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "source": str(OBLIGATION_PATH.relative_to(SERIES_ROOT)),
        "summary": {
            "total_obligation_rows": len(rows),
            "receipt_bound_rows_excluded": len(rows) - len(entries),
            "normal_form_ingress_rows": len(entries),
            "top_batch_limit": args.top_batch if args.top_batch > 0 else None,
            "papers_represented": len(rows_by_flcr),
            "rows_by_claim_family": dict(sorted(by_family.items())),
            "rows_by_flcr": dict(sorted(rows_by_flcr.items())),
        },
        "validator_standard_to_add": {
            "standard_id": "paper.normal_form_conversion",
            "owner_suite": "CMPLX-Standards",
            "status": "required_not_yet_executed",
            "effect": "routes non-receipt-bound obligations into their lawful evidence queues",
        },
        "entries": entries,
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    PROTOCOL_MD.write_text(build_protocol(), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"wrote {PROTOCOL_MD}")


if __name__ == "__main__":
    main()
