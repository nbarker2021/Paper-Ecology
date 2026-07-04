#!/usr/bin/env python3
"""Audit what can honestly reach ASSEMBLE from current FLCR/Cursor state."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
ASSEMBLY_PATH = SERIES_ROOT / "PAPER_ASSEMBLY_AUDIT_PASS.json"
OBLIGATION_PATH = SERIES_ROOT / "OBLIGATION_ROWS.json"
CMPLX_REPORT_PATH = SERIES_ROOT / "CMPLX_STANDARDS_NORMAL_FORM_INGRESS_REPORT.json"
NORMAL_FORM_PATH = SERIES_ROOT / "NORMAL_FORM_INGRESS_MATRIX.json"
OUT_JSON = SERIES_ROOT / "ASSEMBLE_CANDIDATE_AUDIT.json"
OUT_MD = SERIES_ROOT / "ASSEMBLE_CANDIDATE_AUDIT.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def md(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def bucket_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "count": len(rows),
        "by_nist_status": dict(Counter(str(row.get("nist_status", "")) for row in rows)),
        "by_validation_status": dict(Counter(str(row.get("validation_status", "")) for row in rows)),
        "by_integration_status": dict(Counter(str(row.get("integration_status", "")) for row in rows)),
        "with_external_pair_and_correlation": sum(
            1 for row in rows if row.get("external_paper_title") and row.get("correlation")
        ),
    }


def top_blocked(rows: list[dict[str, Any]], limit: int = 25) -> list[dict[str, Any]]:
    ranked = sorted(
        rows,
        key=lambda row: (
            row.get("score_notebook", {}).get("assembly_score", 0),
            row.get("score_notebook", {}).get("source_identity_score", 0),
        ),
        reverse=True,
    )
    out: list[dict[str, Any]] = []
    for row in ranked[:limit]:
        score = row.get("score_notebook", {})
        missing = []
        if not row.get("external_paper_title"):
            missing.append("external_paper_title")
        if not row.get("correlation"):
            missing.append("correlation")
        if row.get("nist_status") != "PASS":
            missing.append("PASS validation status")
        if row.get("validation_status") not in {"READY_FOR_PAPER_ROUTING", "ASSEMBLY_READY"}:
            missing.append("assembly validation status")
        if row.get("record_type") != "pairwise_external_evidence_package":
            missing.append("pairwise_external_evidence_package type")
        out.append(
            {
                "record_id": row.get("record_id"),
                "title": row.get("title"),
                "assembly_score": score.get("assembly_score"),
                "decision": score.get("decision"),
                "integration_status": row.get("integration_status"),
                "nist_status": row.get("nist_status"),
                "validation_status": row.get("validation_status"),
                "declared_routes": row.get("declared_routes", []),
                "missing_for_assemble": missing,
            }
        )
    return out


def build_payload() -> dict[str, Any]:
    assembly = load_json(ASSEMBLY_PATH)
    obligations = load_json(OBLIGATION_PATH)
    cmplx_report = load_json(CMPLX_REPORT_PATH)
    normal_form = load_json(NORMAL_FORM_PATH)

    assemble_now = assembly.get("assemble_now", [])
    reroute_or_repair = assembly.get("reroute_or_repair", [])
    discovery_queue = assembly.get("discovery_queue", [])
    obligation_rows = obligations.get("rows", [])

    receipt_bound_rows = [row for row in obligation_rows if row.get("status") == "receipt_bound"]
    pending_receipt_rows = [
        row for row in obligation_rows if row.get("status") == "derived_pending_receipt"
    ]

    cmplx_bands = Counter(row["inclusion_band"] for row in cmplx_report.get("grades", []))
    normal_form_by_flcr: dict[str, Counter[str]] = defaultdict(Counter)
    for grade in cmplx_report.get("grades", []):
        flcr = str(grade.get("record_id", ""))[:7]
        normal_form_by_flcr[flcr][grade["inclusion_band"]] += 1

    receipt_by_flcr: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in receipt_bound_rows:
        receipt_by_flcr[row["flcr_id"]].append(row)

    immediate_new_assemble: list[dict[str, Any]] = []
    for row in reroute_or_repair + discovery_queue:
        score = row.get("score_notebook", {})
        if score.get("decision") == "ASSEMBLE":
            immediate_new_assemble.append(row)

    return {
        "schema": "flcr.assemble_candidate_audit.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "sources": {
            "assembly": str(ASSEMBLY_PATH.name),
            "obligations": str(OBLIGATION_PATH.name),
            "cmplx_standards": str(CMPLX_REPORT_PATH.name),
            "normal_form": str(NORMAL_FORM_PATH.name),
        },
        "hard_rule": assembly.get("assembly_rule"),
        "summary": {
            "already_assemble": len(assemble_now),
            "new_immediate_assemble_from_current_nonassemble_buckets": len(immediate_new_assemble),
            "receipt_bound_support_rows": len(receipt_bound_rows),
            "pending_receipt_rows": len(pending_receipt_rows),
            "cmplx_perfect_fit_normal_form_rows": cmplx_bands.get("perfect_fit", 0),
            "cmplx_model_inclusive_normal_form_rows": cmplx_bands.get("model_inclusive", 0),
            "cursor_timeline_reroute_records": sum(
                1
                for row in reroute_or_repair
                if row.get("integration_status") == "timeline_provenance_wired"
            ),
            "reroute_records_with_external_pair": bucket_rows(reroute_or_repair)[
                "with_external_pair_and_correlation"
            ],
        },
        "assemble_now": assemble_now,
        "immediate_new_assemble": immediate_new_assemble,
        "receipt_bound_support_rows": receipt_bound_rows,
        "receipt_bound_by_flcr": {
            flcr: [
                {
                    "obligation_id": row["obligation_id"],
                    "receipt_path": row.get("receipt_path"),
                    "receipt_verifier": row.get("receipt_verifier"),
                }
                for row in rows
            ]
            for flcr, rows in sorted(receipt_by_flcr.items())
        },
        "bucket_readout": {
            "assemble_now": bucket_rows(assemble_now),
            "reroute_or_repair": bucket_rows(reroute_or_repair),
            "discovery_queue": bucket_rows(discovery_queue),
        },
        "cmplx_standards_by_flcr": {
            flcr: dict(counter) for flcr, counter in sorted(normal_form_by_flcr.items())
        },
        "normal_form_summary": normal_form.get("summary", {}),
        "closest_blocked_records": top_blocked(reroute_or_repair + discovery_queue),
        "decision": (
            "Current current-state promotion count remains 28. The 9 receipt-bound "
            "obligation rows are attachable support rows, not new ASSEMBLE records, "
            "until OBLIGATION_ROWS is wired into scoring and paper-local holds clear."
        ),
    }


def write_markdown(payload: dict[str, Any]) -> None:
    lines: list[str] = []
    summary = payload["summary"]
    lines.append("# Assemble Candidate Audit")
    lines.append("")
    lines.append(f"Generated: `{payload['generated_utc']}`")
    lines.append("")
    lines.append("## Bottom Line")
    lines.append("")
    lines.append(f"- Already ASSEMBLE: `{summary['already_assemble']}`")
    lines.append(
        "- New immediate ASSEMBLE from current non-assemble buckets: "
        f"`{summary['new_immediate_assemble_from_current_nonassemble_buckets']}`"
    )
    lines.append(f"- Receipt-bound support rows: `{summary['receipt_bound_support_rows']}`")
    lines.append(f"- Pending receipt rows: `{summary['pending_receipt_rows']}`")
    lines.append(
        "- CMPLX-Standards normal-form rows: "
        f"`{summary['cmplx_perfect_fit_normal_form_rows']}` perfect, "
        f"`{summary['cmplx_model_inclusive_normal_form_rows']}` model-inclusive"
    )
    lines.append(
        f"- Cursor timeline reroute records: `{summary['cursor_timeline_reroute_records']}`"
    )
    lines.append("")
    lines.append(payload["decision"])
    lines.append("")
    lines.append("## Existing ASSEMBLE Items")
    lines.append("")
    lines.append("| Record | Score | Primary title |")
    lines.append("|---|---:|---|")
    for row in payload["assemble_now"]:
        lines.append(
            f"| `{row.get('record_id')}` | {row.get('score_notebook', {}).get('assembly_score')} | "
            f"{md(row.get('title'))} |"
        )
    lines.append("")
    lines.append("## Receipt-Bound Support Rows")
    lines.append("")
    lines.append("| FLCR | Obligation | Receipt | Verifier |")
    lines.append("|---|---|---|---|")
    for row in payload["receipt_bound_support_rows"]:
        lines.append(
            f"| `{row.get('flcr_id')}` | `{row.get('obligation_id')}` | "
            f"{md(row.get('receipt_path'))} | `{md(row.get('receipt_verifier'))}` |"
        )
    lines.append("")
    lines.append("## Closest Blocked Records")
    lines.append("")
    lines.append("| Record | Score | Status | Missing | Title |")
    lines.append("|---|---:|---|---|---|")
    for row in payload["closest_blocked_records"][:20]:
        lines.append(
            f"| `{row['record_id']}` | {row['assembly_score']} | "
            f"`{row.get('integration_status')}` | {md(', '.join(row['missing_for_assemble']))} | "
            f"{md(row.get('title'))} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "The shortest honest path to more ASSEMBLE is not normal-form scoring alone. "
        "It is either: bind the 51 pending receipt rows to real receipts and clear "
        "paper holds, or pair the 50 timeline-rerouted local artifacts with external "
        "papers and rerun validation as pairwise external evidence packages."
    )
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    payload = build_payload()
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    write_markdown(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
