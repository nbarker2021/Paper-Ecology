#!/usr/bin/env python3
"""CMPLX-Standards universal model-fit grader.

This is the rewritten NIST/NSIT surface for CMPLX work. It is deliberately a
measurement tool, not a proof oracle: it grades records against a declared model
contract and reports how close the data is to perfect inclusion, partial
inclusion, weak inclusion, or non-inclusion.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_THRESHOLDS = {
    "perfect_fit": 1.0,
    "model_inclusive": 0.90,
    "partial_inclusive": 0.65,
    "weak_inclusive": 0.35,
}


@dataclass(frozen=True)
class FieldCheck:
    path: str
    weight: float
    present: bool
    score: float
    message: str


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def get_path(obj: Any, path: str) -> Any:
    cur = obj
    for part in path.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None
        else:
            return None
    return cur


def is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return len(value) > 0
    if isinstance(value, float) and math.isnan(value):
        return False
    return True


def extract_records(payload: Any, record_selector: str | None = None) -> list[dict[str, Any]]:
    if record_selector:
        selected = get_path(payload, record_selector)
    else:
        selected = None
        if isinstance(payload, dict):
            for key in ("entries", "rows", "records", "items", "artifacts", "verdicts"):
                if isinstance(payload.get(key), list):
                    selected = payload[key]
                    break
        if selected is None:
            selected = payload

    if isinstance(selected, list):
        return [row for row in selected if isinstance(row, dict)]
    if isinstance(selected, dict):
        return [selected]
    return []


def record_id(record: dict[str, Any], id_paths: list[str]) -> str:
    for path in id_paths:
        value = get_path(record, path)
        if is_present(value):
            return str(value)
    return "unknown"


def field_checks(record: dict[str, Any], model: dict[str, Any]) -> list[FieldCheck]:
    weighted_fields = model.get("weighted_fields", {})
    checks: list[FieldCheck] = []
    for path, raw_weight in weighted_fields.items():
        weight = float(raw_weight)
        value = get_path(record, path)
        present = is_present(value)
        checks.append(
            FieldCheck(
                path=path,
                weight=weight,
                present=present,
                score=weight if present else 0.0,
                message="present" if present else "missing or empty",
            )
        )
    return checks


def allowed_value_checks(record: dict[str, Any], model: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for path, allowed in model.get("allowed_values", {}).items():
        value = get_path(record, path)
        passed = value in allowed
        out.append(
            {
                "path": path,
                "value": value,
                "allowed": allowed,
                "passed": passed,
                "message": "allowed value" if passed else "value outside model vocabulary",
            }
        )
    return out


def conditional_checks(record: dict[str, Any], model: dict[str, Any]) -> list[FieldCheck]:
    out: list[FieldCheck] = []
    conditionals = model.get("conditional_required_fields", {})
    for selector_path, cases in conditionals.items():
        selector_value = get_path(record, selector_path)
        required = cases.get(str(selector_value), [])
        for item in required:
            if isinstance(item, dict):
                path = item["path"]
                weight = float(item.get("weight", 1.0))
            else:
                path = str(item)
                weight = 1.0
            value = get_path(record, path)
            present = is_present(value)
            out.append(
                FieldCheck(
                    path=path,
                    weight=weight,
                    present=present,
                    score=weight if present else 0.0,
                    message=(
                        f"present for {selector_path}={selector_value}"
                        if present
                        else f"missing for {selector_path}={selector_value}"
                    ),
                )
            )
    return out


def inclusion_band(fit: float, thresholds: dict[str, float]) -> str:
    if fit >= thresholds["perfect_fit"]:
        return "perfect_fit"
    if fit >= thresholds["model_inclusive"]:
        return "model_inclusive"
    if fit >= thresholds["partial_inclusive"]:
        return "partial_inclusive"
    if fit >= thresholds["weak_inclusive"]:
        return "weak_inclusive"
    return "non_inclusive"


def grade_record(record: dict[str, Any], model: dict[str, Any]) -> dict[str, Any]:
    checks = field_checks(record, model) + conditional_checks(record, model)
    allowed_checks = allowed_value_checks(record, model)
    total_weight = sum(check.weight for check in checks)
    earned = sum(check.score for check in checks)

    if total_weight == 0:
        field_fit = 1.0
    else:
        field_fit = earned / total_weight

    allowed_failures = [check for check in allowed_checks if not check["passed"]]
    vocabulary_penalty = 0.0
    if allowed_checks:
        vocabulary_penalty = len(allowed_failures) / len(allowed_checks) * float(
            model.get("allowed_value_penalty", 0.20)
        )

    fit = max(0.0, min(1.0, field_fit - vocabulary_penalty))
    thresholds = {**DEFAULT_THRESHOLDS, **model.get("thresholds", {})}
    missing = [check.path for check in checks if not check.present]

    return {
        "record_id": record_id(record, model.get("record_id_paths", ["record_id", "id", "obligation_id"])),
        "fit_score": round(fit * 100.0, 6),
        "distance_to_perfect": round(1.0 - fit, 6),
        "inclusion_band": inclusion_band(fit, thresholds),
        "field_fit": round(field_fit, 6),
        "vocabulary_penalty": round(vocabulary_penalty, 6),
        "missing_fields": missing,
        "allowed_value_failures": allowed_failures,
        "checks": [
            {
                "path": check.path,
                "weight": check.weight,
                "present": check.present,
                "score": check.score,
                "message": check.message,
            }
            for check in checks
        ],
    }


def grade_payload(payload: Any, model: dict[str, Any]) -> dict[str, Any]:
    records = extract_records(payload, model.get("record_selector"))
    grades = [grade_record(record, model) for record in records]
    bands = Counter(grade["inclusion_band"] for grade in grades)
    if grades:
        avg_fit = sum(g["fit_score"] for g in grades) / len(grades)
        avg_distance = sum(g["distance_to_perfect"] for g in grades) / len(grades)
    else:
        avg_fit = 0.0
        avg_distance = 1.0

    return {
        "schema": "cmplx_standards_report.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "tool": "CMPLX-Standards",
        "model_id": model.get("model_id", "unknown_model"),
        "model_version": model.get("version", "0.0.0"),
        "summary": {
            "record_count": len(records),
            "average_fit_score": round(avg_fit, 6),
            "average_distance_to_perfect": round(avg_distance, 6),
            "bands": dict(sorted(bands.items())),
        },
        "interpretation": {
            "perfect_fit": "data contains every field required by the model contract and uses model vocabulary",
            "model_inclusive": "data is close enough to route into model use with bounded residues",
            "partial_inclusive": "data has useful signal but needs completion before strong model use",
            "weak_inclusive": "data is weakly aligned and should remain exploratory",
            "non_inclusive": "data does not currently belong in the model without rework or a new model",
        },
        "grades": grades,
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    summary = report["summary"]
    lines = [
        "# CMPLX-Standards Report",
        "",
        f"Generated: `{report['generated_utc']}`",
        "",
        f"Model: `{report['model_id']}`",
        "",
        "## Summary",
        "",
        f"- Records: `{summary['record_count']}`",
        f"- Average fit score: `{summary['average_fit_score']}`",
        f"- Average distance to perfect: `{summary['average_distance_to_perfect']}`",
        "",
        "### Inclusion Bands",
        "",
        "| Band | Count |",
        "|---|---:|",
    ]
    for band, count in summary["bands"].items():
        lines.append(f"| `{band}` | {count} |")
    lines.extend(["", "## Lowest-Fit Records", "", "| Record | Fit | Distance | Band | Missing fields |", "|---|---:|---:|---|---|"])
    for grade in sorted(report["grades"], key=lambda item: item["fit_score"])[:40]:
        missing = ", ".join(grade["missing_fields"][:6])
        if len(grade["missing_fields"]) > 6:
            missing += ", ..."
        lines.append(
            f"| `{grade['record_id']}` | {grade['fit_score']} | "
            f"{grade['distance_to_perfect']} | `{grade['inclusion_band']}` | {missing or 'none'} |"
        )
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="cmplx-standards",
        description="Grade arbitrary data against a CMPLX model contract.",
    )
    parser.add_argument("--input", required=True, help="JSON payload to grade")
    parser.add_argument("--model", required=True, help="CMPLX-Standards model contract JSON")
    parser.add_argument("--output", "-o", required=True, help="write JSON report here")
    parser.add_argument("--markdown", help="optional markdown report path")
    args = parser.parse_args(argv)

    payload = load_json(Path(args.input))
    model = load_json(Path(args.model))
    report = grade_payload(payload, model)
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.markdown:
        write_markdown(report, Path(args.markdown))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
