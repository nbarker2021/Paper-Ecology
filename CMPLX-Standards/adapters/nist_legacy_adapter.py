"""Wrap legacy NIST review suite output into CMPLX-Standards grade records (diff-only)."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

CMPLX_ROOT = Path(__file__).resolve().parents[2]
TOOLS = CMPLX_ROOT / "tools"
AUDIT_OUT = CMPLX_ROOT / "_drive-audit/output"
NIST_SCRIPT = TOOLS / "run_flcr_nist_review_suite.py"
SERIES_CANDIDATES = [
    CMPLX_ROOT
    / "papers/active-rework/publication_series/Formalizing_LCR_Unifying_Standard_Models",
    Path(r"D:\Paper Reworks/publication_series/Formalizing_LCR_Unifying_Standard_Models"),
]
SERIES = next((path for path in SERIES_CANDIDATES if path.exists()), SERIES_CANDIDATES[0])
DEFAULT_NIST_REPORT = SERIES / "FLCR_NIST_AND_REVIEW_SUITE_REPORT.json"


def load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def run_nist_suite_if_stale(report_path: Path) -> None:
    if not NIST_SCRIPT.exists():
        return
    if report_path.exists() and NIST_SCRIPT.exists():
        if report_path.stat().st_mtime >= NIST_SCRIPT.stat().st_mtime:
            return
    subprocess.run([sys.executable, str(NIST_SCRIPT)], cwd=str(TOOLS), check=False)


def _fit_from_nist_verdict(verdict: str) -> float:
    if verdict == "PASS":
        return 100.0
    if verdict == "OPEN":
        return 55.0
    if verdict == "FAIL":
        return 10.0
    return 25.0


def _band_from_fit(fit: float) -> str:
    if fit >= 100.0:
        return "perfect_fit"
    if fit >= 90.0:
        return "model_inclusive"
    if fit >= 65.0:
        return "partial_inclusive"
    if fit >= 35.0:
        return "weak_inclusive"
    return "non_inclusive"


def nist_paper_to_grade_record(paper: dict[str, Any]) -> dict[str, Any]:
    verdict = str(paper.get("nist_verdict", "OPEN"))
    fit = _fit_from_nist_verdict(verdict)
    standards = paper.get("standards") or []
    failed = [row for row in standards if row.get("status") not in {"PASS", "NOT_APPLICABLE"}]
    return {
        "record_id": paper.get("publication_id", "unknown"),
        "legacy_source": "flcr_nist_review_suite",
        "legacy_adapter": "nist_legacy_adapter.v1",
        "nist_verdict": verdict,
        "fit_score": fit,
        "distance_to_perfect": round(1.0 - fit / 100.0, 6),
        "inclusion_band": _band_from_fit(fit),
        "claim_count": paper.get("claim_count", 0),
        "receipt_count": paper.get("receipt_count", 0),
        "open_obligation_count": paper.get("open_obligation_count", 0),
        "standards_fail_count": len(failed),
        "standards": standards,
        "peer_recommendation": paper.get("peer_recommendation", "not_run"),
        "apply_next": paper.get("apply_next", []),
        "provenance_label": "nist_legacy_adapter",
    }


def adapt_nist_report(report: dict[str, Any]) -> dict[str, Any]:
    papers = report.get("papers") or []
    grades = [nist_paper_to_grade_record(paper) for paper in papers]
    avg_fit = sum(g["fit_score"] for g in grades) / len(grades) if grades else 0.0
    return {
        "schema": "cmplx_standards_legacy_adapter_report.v1",
        "adapter_id": "nist_legacy_adapter",
        "purpose": "diff-only — not a forward gate",
        "legacy_source_schema": report.get("schema", "flcr_nist_and_review_suite_report.v1"),
        "legacy_generated_at": report.get("generated_at"),
        "record_count": len(grades),
        "average_fit_score": round(avg_fit, 6),
        "grades": grades,
        "note": "Compare against CMPLX_STANDARDS_SUITE_REPORT.json for drift detection.",
    }


def load_adapted_nist_report(report_path: Path | None = None) -> dict[str, Any]:
    path = report_path or DEFAULT_NIST_REPORT
    run_nist_suite_if_stale(path)
    report = load_json(path)
    if not isinstance(report, dict):
        return {
            "schema": "cmplx_standards_legacy_adapter_report.v1",
            "adapter_id": "nist_legacy_adapter",
            "record_count": 0,
            "average_fit_score": 0.0,
            "grades": [],
            "error": f"missing_or_invalid_report:{path}",
        }
    return adapt_nist_report(report)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adapt legacy NIST suite report to CMPLX-Standards grades")
    parser.add_argument("--input", default=str(DEFAULT_NIST_REPORT))
    parser.add_argument("-o", "--output", default=str(AUDIT_OUT / "NIST_LEGACY_DIFF_REPORT.json"))
    args = parser.parse_args(argv)
    adapted = load_adapted_nist_report(Path(args.input))
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(adapted, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(out),
                "record_count": adapted.get("record_count", 0),
                "average_fit_score": adapted.get("average_fit_score", 0),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
