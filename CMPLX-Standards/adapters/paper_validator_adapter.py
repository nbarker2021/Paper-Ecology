"""Bridge verify_*.json receipts and paper validator patterns into CMPLX-Standards inputs."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CMPLX_ROOT = Path(__file__).resolve().parents[2]
AUDIT_OUT = CMPLX_ROOT / "_drive-audit/output"

PASS_STATUSES = frozenset(
    {
        "PASS",
        "pass",
        "pass_with_open_gaps",
        "pass_with_open_low_energy_running",
        "pass_with_open_numeric_projection_gaps",
        "pass_with_open_obligations",
        "pass_estimate_with_physical_boundary",
        "pass_with_threshold_residuals",
        "pass_with_open_numeric_gaps",
        "pass_with_open_majorana_absolute_mass_and_no_fit_gaps",
        "pass_with_open_residual_weight_law",
        "pass_with_located_deephole_klein_sources_open_executable_binding",
        "pass_with_open_normalization_gaps",
    }
)

DEFAULT_RECEIPT_ROOTS = [
    CMPLX_ROOT / "CQECMPLX-Formal-Suite/lib/lattice_forge/receipts",
    CMPLX_ROOT / "papers/active-rework/publication_series/Formalizing_LCR_Unifying_Standard_Models",
    CMPLX_ROOT / "_drive-audit/output",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def normalize_status(raw: Any) -> str:
    text = str(raw or "").strip()
    if not text:
        return "unknown"
    lowered = text.lower()
    if lowered in {s.lower() for s in PASS_STATUSES}:
        return text
    if lowered in {"fail", "failed", "error"}:
        return "FAIL"
    if lowered in {"open", "deferred", "unknown"}:
        return "OPEN"
    return text


def is_pass_status(normalized: str) -> bool:
    return normalized.lower() in {s.lower() for s in PASS_STATUSES}


def discover_verify_receipt_paths(
    roots: list[Path] | None = None,
    *,
    max_files: int | None = None,
) -> list[Path]:
    found: list[Path] = []
    seen: set[str] = set()
    for root in roots or DEFAULT_RECEIPT_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("verify_*.json")):
            if any(part in path.parts for part in (".git", "node_modules", "archive_history")):
                continue
            key = str(path.resolve()).lower()
            if key in seen:
                continue
            seen.add(key)
            found.append(path)
            if max_files is not None and len(found) >= max_files:
                return found
    return found


def receipt_path_to_record(path: Path) -> dict[str, Any] | None:
    data = load_json(path)
    if not isinstance(data, dict):
        return None
    normalized = normalize_status(data.get("status"))
    checks = data.get("checks")
    if checks is None and isinstance(data.get("projection"), dict):
        checks = data["projection"]
    boundary = data.get("honesty_boundary") or data.get("boundary")
    verifier_pass = is_pass_status(normalized)
    return {
        "receipt_id": path.stem,
        "verifier": data.get("verifier") or path.stem,
        "path": str(path),
        "status": data.get("status"),
        "normalized_status": normalized,
        "verifier_pass": "yes" if verifier_pass else "no",
        "schema": data.get("schema"),
        "checks": checks,
        "honesty_boundary": boundary,
        "closed_now": data.get("closed_now"),
        "boundary": data.get("boundary"),
        "provenance_label": "paper_validator_adapter",
    }


def discover_verify_receipts(
    roots: list[Path] | None = None,
    *,
    max_files: int | None = None,
    pass_only: bool = False,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in discover_verify_receipt_paths(roots, max_files=max_files):
        record = receipt_path_to_record(path)
        if record is None:
            continue
        if pass_only and record.get("verifier_pass") != "yes":
            continue
        records.append(record)
    return records


def build_receipt_payload(
    roots: list[Path] | None = None,
    *,
    max_files: int | None = None,
    pass_only: bool = False,
) -> dict[str, Any]:
    receipts = discover_verify_receipts(roots, max_files=max_files, pass_only=pass_only)
    pass_count = sum(1 for row in receipts if row.get("verifier_pass") == "yes")
    return {
        "schema": "cmplx_standards_verifier_receipt_payload.v1",
        "adapter_id": "paper_validator_adapter",
        "receipt_count": len(receipts),
        "pass_count": pass_count,
        "roots": [str(root) for root in (roots or DEFAULT_RECEIPT_ROOTS)],
        "receipts": receipts,
    }


def adapt_paper_payloads(payloads: dict[str, Any]) -> list[dict[str, Any]]:
    grades: list[dict[str, Any]] = []
    slots = payloads.get("slots") or []
    if isinstance(slots, list):
        for doc in slots:
            if not isinstance(doc, dict):
                continue
            slot = doc.get("paper_id") or doc.get("slot_id") or "unknown"
            tier = doc.get("standards_grade") or {}
            grades.append(
                {
                    "record_id": slot,
                    "fit_score": tier.get("fit_score", 0),
                    "inclusion_band": tier.get("inclusion_band", "pending"),
                    "adapter": "paper_validator",
                }
            )
    return grades


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Paper validator / verify receipt adapter")
    parser.add_argument(
        "--mode",
        choices=("receipts", "paper_payloads"),
        default="receipts",
    )
    parser.add_argument("--input", default=str(AUDIT_OUT / "PAPER_REVIEW_PAYLOADS.json"))
    parser.add_argument("-o", "--output", default=str(AUDIT_OUT / "PAPER_VALIDATOR_ADAPTER_REPORT.json"))
    args = parser.parse_args(argv)

    if args.mode == "receipts":
        report = build_receipt_payload()
    else:
        payloads = load_json(Path(args.input)) or {}
        grades = adapt_paper_payloads(payloads if isinstance(payloads, dict) else {})
        report = {
            "schema": "cmplx_standards_adapter_report.v1",
            "generated_utc": utc_now(),
            "adapter": "paper_validator",
            "grade_count": len(grades),
            "grades": grades,
        }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(out), "mode": args.mode}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
