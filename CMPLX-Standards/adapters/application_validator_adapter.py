"""General application validator built from paper validators and receipts."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CMPLX_ROOT = Path(__file__).resolve().parents[2]
STANDARDS_DIR = Path(__file__).resolve().parents[1]
AUDIT_OUT = CMPLX_ROOT / "_drive-audit" / "output"

PAPER_VALIDATOR_ROOTS = [
    CMPLX_ROOT / "CQE-CMPLX-1T-Production" / "src" / "papers" / "formal",
    CMPLX_ROOT / "CQECMPLX-Formal-Suite",
    CMPLX_ROOT / "papers" / "active-rework",
]

DEFAULT_APPLICATION_TARGETS = [
    {
        "app_id": "cmplx-standards",
        "app_type": "validator",
        "source_path": STANDARDS_DIR,
        "tests_command": "python CMPLX-Standards\\run_standards_suite.py --models application_validation,forge_runtime",
        "runtime_command": "python CMPLX-Standards\\run_standards_suite.py --full",
        "standards_model": "application_validation_model.json",
        "validator_links": ["paper_validation_catalog", "forge_runtime", "verifier_receipt"],
        "receipt_glob_roots": [AUDIT_OUT, STANDARDS_DIR],
    },
    {
        "app_id": "forge-runtime",
        "app_type": "runtime_substrate",
        "source_path": CMPLX_ROOT / "CMPLX-PartsFactory-main" / "packages" / "lattice-forge",
        "tests_command": (
            "powershell -NoProfile -ExecutionPolicy Bypass -File "
            "D:\\CQE_CMPLX\\tools\\forge_runtime_env.ps1 lattice-forge verify-seed"
        ),
        "runtime_command": (
            "powershell -NoProfile -ExecutionPolicy Bypass -File "
            "D:\\CQE_CMPLX\\tools\\forge_runtime_env.ps1 lattice-forge status"
        ),
        "standards_model": "forge_runtime_model.json",
        "validator_links": ["forge_runtime", "verifier_receipt"],
        "receipt_glob_roots": [CMPLX_ROOT / "_runtime" / "forge_reasoning", AUDIT_OUT],
    },
    {
        "app_id": "reforge-forgefactory",
        "app_type": "runtime_substrate",
        "source_path": (
            CMPLX_ROOT
            / "CQECMPLX-AirLock"
            / "forgefactory-v0.3-lineage-read"
            / "ForgeFactory_v0_3"
        ),
        "tests_command": (
            "powershell -NoProfile -ExecutionPolicy Bypass -File "
            "D:\\CQE_CMPLX\\tools\\forge_runtime_env.ps1 forgefactory smoke"
        ),
        "runtime_command": (
            "powershell -NoProfile -ExecutionPolicy Bypass -File "
            "D:\\CQE_CMPLX\\tools\\forge_runtime_env.ps1 forgefactory engines"
        ),
        "standards_model": "forge_runtime_model.json",
        "validator_links": ["forge_runtime", "paper00_transport_contract"],
        "receipt_glob_roots": [AUDIT_OUT],
    },
    {
        "app_id": "mannyai",
        "app_type": "cam_base",
        "source_path": Path(r"D:\MannyAI"),
        "tests_command": "cd D:\\MannyAI; python -m pytest",
        "runtime_command": "cd D:\\MannyAI; python run_cem.py",
        "standards_model": "ability_seed_model.json",
        "validator_links": ["ability_seed", "verifier_receipt", "forge_runtime"],
        "receipt_glob_roots": [Path(r"D:\MannyAI"), AUDIT_OUT],
    },
    {
        "app_id": "cqe-cmplx-1t-production",
        "app_type": "product_runtime",
        "source_path": CMPLX_ROOT / "CQE-CMPLX-1T-Production",
        "tests_command": (
            "cd D:\\CQE_CMPLX\\CQE-CMPLX-1T-Production; "
            "$env:PYTHONPATH='src;src/products'; python tests\\run_all.py"
        ),
        "runtime_command": "product-specific",
        "standards_model": "assembled_paper_model.json",
        "validator_links": ["verifier_receipt", "assembled_paper", "forge_runtime"],
        "receipt_glob_roots": [CMPLX_ROOT / "CQE-CMPLX-1T-Production", AUDIT_OUT],
    },
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def discover_paper_validation_tools() -> list[dict[str, Any]]:
    tools: list[dict[str, Any]] = []
    seen: set[str] = set()
    for root in PAPER_VALIDATOR_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("verify_*.py")):
            if any(part in path.parts for part in (".git", "__pycache__", "archive_history")):
                continue
            key = str(path.resolve()).lower()
            if key in seen:
                continue
            seen.add(key)
            paper_id = next((part for part in path.parts if part.startswith("CQE-paper-")), "")
            tools.append(
                {
                    "tool_id": path.stem,
                    "paper_id": paper_id,
                    "path": str(path),
                    "source_root": str(root),
                    "validator_family": infer_validator_family(path),
                }
            )
    return tools


def infer_validator_family(path: Path) -> str:
    text = path.stem.lower()
    if "rule30" in text or "center_column" in text:
        return "rule30"
    if "d4" in text or "triality" in text:
        return "d4_triality"
    if "hamiltonian" in text or "energy" in text:
        return "hamiltonian_energy"
    if "niemeier" in text or "lattice" in text or "root" in text:
        return "lattice"
    if "higgs" in text or "ckm" in text or "zeta" in text:
        return "physics_bridge"
    return "general_claim"


def discover_receipts(roots: list[Path]) -> list[str]:
    receipts: list[str] = []
    seen: set[str] = set()
    for root in roots:
        if not root.exists():
            continue
        for pattern in ("*receipt*.json", "verify_*.json", "*.receipt.json"):
            for path in sorted(root.rglob(pattern)):
                if any(part in path.parts for part in (".git", "__pycache__", "archive_history")):
                    continue
                key = str(path.resolve()).lower()
                if key not in seen:
                    seen.add(key)
                    receipts.append(str(path))
    return receipts


def target_to_record(
    target: dict[str, Any],
    *,
    validation_tools: list[dict[str, Any]],
) -> dict[str, Any]:
    source_path = Path(target["source_path"])
    receipt_paths = discover_receipts([Path(path) for path in target.get("receipt_glob_roots", [])])
    standards_model = STANDARDS_DIR / "models" / str(target.get("standards_model", ""))
    blockers: list[str] = []
    if not source_path.exists():
        blockers.append("source_path_missing")
    if not standards_model.exists():
        blockers.append("standards_model_missing")
    if not target.get("tests_command"):
        blockers.append("tests_command_missing")
    if not target.get("runtime_command"):
        blockers.append("runtime_command_missing")
    if not target.get("validator_links"):
        blockers.append("validator_links_missing")
    status = "pass" if not blockers else "warn"
    return {
        "application_id": target["app_id"],
        "application_type": target["app_type"],
        "source_path": str(source_path),
        "source_path_exists": "yes" if source_path.exists() else "no",
        "tests_command": target.get("tests_command"),
        "runtime_command": target.get("runtime_command"),
        "standards_model": str(standards_model),
        "standards_model_exists": "yes" if standards_model.exists() else "no",
        "validator_links": target.get("validator_links", []),
        "paper_validation_tool_count": len(validation_tools),
        "paper_validation_families": sorted(
            {tool["validator_family"] for tool in validation_tools}
        ),
        "receipt_count": len(receipt_paths),
        "receipt_paths": receipt_paths[:100] or ["none_found"],
        "status": status,
        "blockers": blockers or ["none"],
        "provenance_label": "application_validator_adapter",
    }


def build_application_validation_payload() -> dict[str, Any]:
    validation_tools = discover_paper_validation_tools()
    records = [
        target_to_record(target, validation_tools=validation_tools)
        for target in DEFAULT_APPLICATION_TARGETS
    ]
    return {
        "schema": "cmplx_standards_application_validation_payload.v1",
        "adapter_id": "application_validator_adapter",
        "generated_utc": utc_now(),
        "paper_validation_tool_count": len(validation_tools),
        "paper_validation_tools": validation_tools,
        "application_count": len(records),
        "records": records,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build general application validation payload")
    parser.add_argument(
        "-o",
        "--output",
        default=str(AUDIT_OUT / "APPLICATION_VALIDATION_STANDARDS_PAYLOAD.json"),
    )
    args = parser.parse_args(argv)
    payload = build_application_validation_payload()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(out),
                "application_count": payload["application_count"],
                "paper_validation_tool_count": payload["paper_validation_tool_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
