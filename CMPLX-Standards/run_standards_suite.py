"""CMPLX-Standards suite orchestrator — single forward validation surface."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STANDARDS_DIR = Path(__file__).resolve().parent
CMPLX_ROOT = STANDARDS_DIR.parent
if str(STANDARDS_DIR) not in sys.path:
    sys.path.insert(0, str(STANDARDS_DIR))

from cmplx_standards import grade_payload, load_json  # noqa: E402
from adapters.application_validator_adapter import build_application_validation_payload  # noqa: E402
from adapters.flcr80_repo_slot_adapter import build_flcr80_repo_slot_payload  # noqa: E402
from adapters.forge_runtime_adapter import build_forge_runtime_payload  # noqa: E402
from adapters.legacy_repo_port_adapter import build_legacy_repo_port_payload  # noqa: E402
from adapters.nist_legacy_adapter import load_adapted_nist_report  # noqa: E402
from adapters.paper_validator_adapter import build_receipt_payload  # noqa: E402

SERIES_CANDIDATES = [
    CMPLX_ROOT
    / "papers/active-rework/publication_series/Formalizing_LCR_Unifying_Standard_Models",
    Path(r"D:\Paper Reworks/publication_series/Formalizing_LCR_Unifying_Standard_Models"),
]
SERIES = next((path for path in SERIES_CANDIDATES if path.exists()), SERIES_CANDIDATES[0])
AUDIT_OUT = CMPLX_ROOT / "_drive-audit/output"
ASSEMBLED_DIR = SERIES / "ASSEMBLED_FLCR_PRODUCTS"
MAXIMAL_DIR = SERIES / "MAXIMAL_FLCR_MANUSCRIPTS"
SM_MAPPING_DIR = SERIES / "SM_MAPPING_ROWS"
DEFAULT_OUTPUT = AUDIT_OUT / "CMPLX_STANDARDS_SUITE_REPORT.json"

DATE_POLICIES = frozenset({"prefer_2025", "any_peer_reviewed"})

MODEL_REGISTRY: dict[str, dict[str, Any]] = {
    "normal_form": {
        "model_file": "normal_form_ingress_model.json",
        "input": SERIES / "NORMAL_FORM_INGRESS_MATRIX.json",
    },
    "normal_form_ingress": {
        "model_file": "normal_form_ingress_model.json",
        "input": SERIES / "NORMAL_FORM_INGRESS_MATRIX.json",
    },
    "assembled_paper": {
        "model_file": "assembled_paper_model.json",
        "loader": "assembled_paper",
    },
    "maximal_manuscript": {
        "model_file": "maximal_manuscript_model.json",
        "loader": "maximal_manuscript",
    },
    "sm_mapping_row": {
        "model_file": "sm_mapping_row_model.json",
        "loader": "sm_mapping",
    },
    "external_pair": {
        "model_file": "external_pair_model.json",
        "loader": "external_pair",
    },
    "ability_seed": {
        "model_file": "ability_seed_model.json",
        "loader": "ability_seed",
    },
    "verifier_receipt": {
        "model_file": "verifier_receipt_model.json",
        "loader": "verifier_receipt",
    },
    "forge_runtime": {
        "model_file": "forge_runtime_model.json",
        "loader": "forge_runtime",
    },
    "application_validation": {
        "model_file": "application_validation_model.json",
        "loader": "application_validation",
    },
    "legacy_repo_port": {
        "model_file": "legacy_repo_port_model.json",
        "loader": "legacy_repo_port",
    },
    "flcr80_repo_slot": {
        "model_file": "flcr80_repo_slot_model.json",
        "loader": "flcr80_repo_slot",
    },
}

FULL_MODEL_SET = [
    "normal_form",
    "assembled_paper",
    "maximal_manuscript",
    "sm_mapping_row",
    "external_pair",
    "ability_seed",
    "verifier_receipt",
    "forge_runtime",
    "application_validation",
    "legacy_repo_port",
    "flcr80_repo_slot",
]


def _section_flags(intake: dict[str, Any]) -> dict[str, Any]:
    formal = intake.get("formal_sections") or {}
    receipts = intake.get("receipts") or []
    obligations = (intake.get("required_direct") or {}).get("open_obligations") or []
    external = intake.get("external_candidates") or {}
    gaps = (intake.get("required_direct") or {}).get("assembly_audit_falsifier_gaps") or []
    meta = intake.get("meta") or {}
    flags = {
        "has_proof_receipt_index": "yes" if receipts else "",
        "has_obligation_crosswalk": "yes" if obligations else "",
        "has_external_calibration": "yes"
        if external.get("nist_readiness_by_doi") or external.get("candidate_dois_from_seeds")
        else "",
        "has_falsifiers_section": "yes" if gaps else "",
        "has_honesty_boundary": "yes" if meta.get("epistemology") else "",
    }
    section_count = sum(1 for value in flags.values() if value == "yes")
    section_count += sum(
        1
        for key in ("abstract", "keywords", "claims")
        if (formal.get(key) or "").strip()
    )
    section_count += 5
    flags["assembled_section_count"] = section_count
    return flags


def _date_gate(package: dict[str, Any], date_policy: str) -> dict[str, Any]:
    paper = package.get("external_paper") or {}
    peer_ok = paper.get("peer_review_status") == "peer_reviewed_journal_article"
    year = int(paper.get("year", 0) or 0)
    if date_policy == "any_peer_reviewed":
        date_gate_pass = peer_ok
        date_gate_check = "peer_review_only"
    else:
        date_gate_pass = peer_ok and year >= 2025
        date_gate_check = "prefer_2025_window"
    return {
        "date_policy": date_policy,
        "peer_review_gate_pass": "yes" if peer_ok else "",
        "date_gate_pass": "yes" if date_gate_pass else "",
        "date_gate_check": date_gate_check,
    }


def load_maximal_manuscript_payload() -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    index_path = MAXIMAL_DIR / "MAXIMAL_FLCR_INDEX.json"
    if index_path.exists():
        index = load_json(index_path)
        if isinstance(index, dict):
            for product in index.get("products") or []:
                if isinstance(product, dict):
                    records.append(dict(product))
    return {
        "schema": "cmplx_standards_maximal_manuscript_payload.v1",
        "source_dir": str(MAXIMAL_DIR),
        "record_count": len(records),
        "records": records,
    }


def load_sm_mapping_payload() -> dict[str, Any]:
    matrix_path = SM_MAPPING_DIR / "SM_MAPPING_MATRIX.json"
    payload = load_json(matrix_path)
    if not isinstance(payload, dict):
        return {
            "schema": "cmplx_standards_sm_mapping_payload.v1",
            "source": str(matrix_path),
            "record_count": 0,
            "records": [],
            "error": f"missing_or_invalid_input:{matrix_path}",
        }
    records = [dict(row) for row in (payload.get("records") or []) if isinstance(row, dict)]
    return {
        "schema": "cmplx_standards_sm_mapping_payload.v1",
        "source": str(matrix_path),
        "record_count": len(records),
        "records": records,
    }


def load_assembled_paper_payload() -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    if ASSEMBLED_DIR.exists():
        for path in sorted(ASSEMBLED_DIR.glob("FLCR-*__intake.json")):
            intake = load_json(path)
            if not isinstance(intake, dict):
                continue
            row = dict(intake)
            row.update(_section_flags(intake))
            records.append(row)
    return {
        "schema": "cmplx_standards_assembled_paper_payload.v1",
        "source_dir": str(ASSEMBLED_DIR),
        "record_count": len(records),
        "records": records,
    }


def load_external_pair_payload(date_policy: str) -> dict[str, Any]:
    index_path = SERIES / "PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_INDEX.json"
    index = load_json(index_path)
    packages: list[dict[str, Any]] = []
    if isinstance(index, dict):
        for package in index.get("packages") or []:
            if not isinstance(package, dict):
                continue
            row = dict(package)
            row.update(_date_gate(package, date_policy))
            packages.append(row)
    return {
        "schema": "cmplx_standards_external_pair_payload.v1",
        "source": str(index_path),
        "date_policy": date_policy,
        "package_count": len(packages),
        "packages": packages,
    }


def load_ability_seed_payload() -> dict[str, Any]:
    seeds: list[dict[str, Any]] = []
    for rel in ("LOCAL_ABILITY_SEED_QUEUE.json", "LEGACY_REPO_ABILITY_SEED_QUEUE.json"):
        path = AUDIT_OUT / rel
        doc = load_json(path)
        if isinstance(doc, dict):
            seeds.extend(row for row in (doc.get("seeds") or []) if isinstance(row, dict))
    return {
        "schema": "cmplx_standards_ability_seed_payload.v1",
        "seed_count": len(seeds),
        "seeds": seeds,
    }


def load_verifier_receipt_payload() -> dict[str, Any]:
    return build_receipt_payload(pass_only=False)


def resolve_payload(model_name: str, date_policy: str) -> dict[str, Any]:
    spec = MODEL_REGISTRY[model_name]
    loader = spec.get("loader")
    if loader == "assembled_paper":
        return load_assembled_paper_payload()
    if loader == "maximal_manuscript":
        return load_maximal_manuscript_payload()
    if loader == "sm_mapping":
        return load_sm_mapping_payload()
    if loader == "external_pair":
        return load_external_pair_payload(date_policy)
    if loader == "ability_seed":
        return load_ability_seed_payload()
    if loader == "verifier_receipt":
        return load_verifier_receipt_payload()
    if loader == "forge_runtime":
        return build_forge_runtime_payload()
    if loader == "application_validation":
        return build_application_validation_payload()
    if loader == "legacy_repo_port":
        return build_legacy_repo_port_payload()
    if loader == "flcr80_repo_slot":
        return build_flcr80_repo_slot_payload()
    input_path = spec.get("input")
    if input_path is None:
        raise ValueError(f"no input configured for model {model_name}")
    payload = load_json(Path(input_path))
    if not isinstance(payload, dict):
        return {"records": [], "error": f"missing_or_invalid_input:{input_path}"}
    return payload


def run_model(model_name: str, date_policy: str) -> dict[str, Any]:
    spec = MODEL_REGISTRY[model_name]
    model_path = STANDARDS_DIR / "models" / spec["model_file"]
    model = load_json(model_path)
    payload = resolve_payload(model_name, date_policy)
    report = grade_payload(payload, model)
    report["suite_model_name"] = model_name
    report["input_summary"] = {
        key: payload.get(key)
        for key in (
            "record_count",
            "package_count",
            "seed_count",
            "receipt_count",
            "source",
            "source_dir",
            "date_policy",
            "error",
        )
        if key in payload
    }
    return report


def parse_models(raw: str | None, full: bool) -> list[str]:
    if full:
        return list(FULL_MODEL_SET)
    if not raw or raw == "all":
        return ["normal_form", "ability_seed"]
    names = [part.strip() for part in raw.split(",") if part.strip()]
    resolved: list[str] = []
    for name in names:
        if name not in MODEL_REGISTRY:
            known = ", ".join(sorted(MODEL_REGISTRY))
            raise ValueError(f"unknown model {name!r}; known: {known}")
        canonical = "normal_form" if name == "normal_form_ingress" else name
        if canonical not in resolved:
            resolved.append(canonical)
    return resolved


def aggregate_suite_report(
    model_reports: dict[str, dict[str, Any]],
    *,
    legacy_nist: dict[str, Any] | None,
    date_policy: str,
) -> dict[str, Any]:
    total_records = sum(report["summary"]["record_count"] for report in model_reports.values())
    avg_fit = (
        sum(report["summary"]["average_fit_score"] for report in model_reports.values())
        / len(model_reports)
        if model_reports
        else 0.0
    )
    return {
        "schema": "cmplx_standards_suite_report.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "tool": "CMPLX-Standards/run_standards_suite.py",
        "primary_gate": "CMPLX-Standards",
        "date_policy": date_policy,
        "model_count": len(model_reports),
        "summary": {
            "total_records_graded": total_records,
            "average_model_fit_score": round(avg_fit, 6),
            "models_run": sorted(model_reports),
        },
        "models": model_reports,
        "legacy_adapters": {
            "nist_legacy": legacy_nist,
        },
        "epistemology": (
            "CMPLX-Standards measures model fit only. "
            "Loosened date_policy widens comparator candidacy, not ASSEMBLE promotion."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="run-standards-suite",
        description="Run CMPLX-Standards models against current artifacts.",
    )
    parser.add_argument(
        "--models",
        default="normal_form,ability_seed",
        help="Comma-separated model keys, 'all', or default subset",
    )
    parser.add_argument("--full", action="store_true", help="Run all registered models")
    parser.add_argument(
        "--date-policy",
        choices=sorted(DATE_POLICIES),
        default="prefer_2025",
        help="External-pair date gate policy (default: prefer_2025)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=str(DEFAULT_OUTPUT),
        help="Write CMPLX_STANDARDS_SUITE_REPORT.json here",
    )
    parser.add_argument(
        "--legacy-nist-diff",
        "--nist-diff",
        action="store_true",
        dest="legacy_nist_diff",
        help="Attach legacy NIST adapter diff report (not a forward gate)",
    )
    args = parser.parse_args(argv)

    model_names = parse_models(None if args.full else args.models, args.full)
    model_reports = {name: run_model(name, args.date_policy) for name in model_names}
    legacy_nist = load_adapted_nist_report() if args.legacy_nist_diff else None
    suite = aggregate_suite_report(
        model_reports,
        legacy_nist=legacy_nist,
        date_policy=args.date_policy,
    )
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(suite, indent=2), encoding="utf-8")

    md_path = out_path.with_suffix(".md")
    lines = [
        "# CMPLX-Standards Suite Report",
        "",
        f"Generated: `{suite['generated_utc']}`",
        f"Date policy: `{args.date_policy}`",
        "",
        "| Model | Records | Avg fit |",
        "|---|---:|---:|",
    ]
    for name, report in sorted(model_reports.items()):
        summary = report.get("summary") or {}
        lines.append(
            f"| `{name}` | {summary.get('record_count', 0)} | "
            f"{summary.get('average_fit_score', 0)} |"
        )
    if legacy_nist:
        lines.extend(
            [
                "",
                f"NIST legacy diff: `{legacy_nist.get('record_count', 0)}` papers "
                f"(diff-only, not gate)",
            ]
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "output": str(out_path),
                "models": model_names,
                "date_policy": args.date_policy,
                "total_records_graded": suite["summary"]["total_records_graded"],
                "average_model_fit_score": suite["summary"]["average_model_fit_score"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
