"""Deploy/check Forge, ReForge, and Lattice Forge as CMPLX-Standards inputs."""

from __future__ import annotations

import argparse
import importlib
import importlib.metadata as metadata
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CMPLX_ROOT = Path(__file__).resolve().parents[2]
STANDARDS_DIR = Path(__file__).resolve().parents[1]
AUDIT_OUT = CMPLX_ROOT / "_drive-audit" / "output"
RUNTIME_ROOT = CMPLX_ROOT / "_runtime" / "forge_reasoning"
LATTICE_FORGE_ROOT = CMPLX_ROOT / "CMPLX-PartsFactory-main" / "packages" / "lattice-forge"
LATTICE_FORGE_SRC = LATTICE_FORGE_ROOT / "src"
FORGEFACTORY_ROOT = (
    CMPLX_ROOT / "CQECMPLX-AirLock" / "forgefactory-v0.3-lineage-read" / "ForgeFactory_v0_3"
)
FORGEFACTORY_SRC = FORGEFACTORY_ROOT / "src"
WRAPPER = CMPLX_ROOT / "tools" / "forge_runtime_env.ps1"

EXPECTED_IMPORT_PREFIXES = {
    "lattice_forge": LATTICE_FORGE_SRC,
    "forgefactory": FORGEFACTORY_SRC,
    "reforge_engine_contracts": FORGEFACTORY_SRC,
    "reforge_engine_hardening": FORGEFACTORY_SRC,
    "reforge_kimi_adapter": FORGEFACTORY_SRC,
    "reforge_researchcraft": FORGEFACTORY_SRC,
    "reforge_pixleforge": FORGEFACTORY_SRC,
    "reforge_wireforge": FORGEFACTORY_SRC,
    "reforge_frameforge": FORGEFACTORY_SRC,
    "reforge_pixl8forge": FORGEFACTORY_SRC,
    "rhenium_engine": FORGEFACTORY_SRC,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def prepend_runtime_paths() -> None:
    for path in (FORGEFACTORY_SRC, LATTICE_FORGE_SRC):
        text = str(path)
        if text in sys.path:
            sys.path.remove(text)
        sys.path.insert(0, text)


def as_posixish(path: Path | str | None) -> str:
    return str(path or "")


def path_under(path: str | Path | None, expected: Path) -> bool:
    if not path:
        return False
    try:
        Path(path).resolve().relative_to(expected.resolve())
        return True
    except ValueError:
        return False


def base_record(
    *,
    record_id: str,
    kind: str,
    component: str,
    status: str,
    expected_path: Path | str,
    actual_path: Path | str,
    command: str,
    result_status: str,
    evidence_level: str,
    receipt_id: str = "not_applicable",
    output_summary: dict[str, Any] | None = None,
    blockers: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "deployment_id": record_id,
        "kind": kind,
        "component": component,
        "status": status,
        "expected_path": as_posixish(expected_path),
        "actual_path": as_posixish(actual_path),
        "command": command,
        "result_status": result_status,
        "evidence_level": evidence_level,
        "receipt_id": receipt_id,
        "output_summary": output_summary or {"note": "not_applicable"},
        "blockers": blockers or ["none"],
        "provenance_label": "forge_runtime_adapter",
    }


def package_editable_location(dist_name: str) -> str:
    try:
        dist = metadata.distribution(dist_name)
    except metadata.PackageNotFoundError:
        return ""
    direct_url_path = Path(str(dist.locate_file("direct_url.json")))
    if direct_url_path.exists():
        try:
            direct = json.loads(direct_url_path.read_text(encoding="utf-8"))
            if direct.get("dir_info", {}).get("editable"):
                return str(Path(direct.get("url", "")).as_posix().replace("file:///", ""))
        except Exception:
            return ""
    return ""


def package_record(dist_name: str, expected_root: Path) -> dict[str, Any]:
    try:
        version = metadata.version(dist_name)
        editable = package_editable_location(dist_name)
        status = "pass" if version else "fail"
        if editable and not path_under(editable, expected_root):
            status = "warn"
        result_status = f"installed:{version}"
        actual = editable or "installed_non_editable"
        blockers: list[str] = [] if status == "pass" else ["editable_location_mismatch"]
    except metadata.PackageNotFoundError:
        status = "fail"
        result_status = "missing"
        actual = ""
        blockers = ["package_missing"]
    return base_record(
        record_id=f"package:{dist_name}",
        kind="package_install",
        component=dist_name,
        status=status,
        expected_path=expected_root,
        actual_path=actual,
        command=f"python -m pip show {dist_name}",
        result_status=result_status,
        evidence_level="package_metadata",
        blockers=blockers,
    )


def path_record(record_id: str, component: str, path: Path) -> dict[str, Any]:
    exists = path.exists()
    return base_record(
        record_id=record_id,
        kind="runtime_path",
        component=component,
        status="pass" if exists else "fail",
        expected_path=path,
        actual_path=path if exists else "",
        command="Test-Path",
        result_status="exists" if exists else "missing",
        evidence_level="filesystem",
        blockers=[] if exists else ["path_missing"],
    )


def import_record(module_name: str, expected_prefix: Path) -> dict[str, Any]:
    try:
        module = importlib.import_module(module_name)
        origin = Path(getattr(module, "__file__", "") or "")
        ok = path_under(origin, expected_prefix)
        return base_record(
            record_id=f"import:{module_name}",
            kind="import_resolution",
            component=module_name,
            status="pass" if ok else "warn",
            expected_path=expected_prefix,
            actual_path=origin,
            command=f"python -c \"import {module_name}; print({module_name}.__file__)\"",
            result_status="resolved_canonical" if ok else "resolved_noncanonical",
            evidence_level="import_resolution",
            blockers=[] if ok else ["noncanonical_import_path"],
        )
    except Exception as exc:
        return base_record(
            record_id=f"import:{module_name}",
            kind="import_resolution",
            component=module_name,
            status="fail",
            expected_path=expected_prefix,
            actual_path="",
            command=f"import {module_name}",
            result_status=repr(exc),
            evidence_level="import_resolution",
            blockers=["import_failed"],
        )


def lattice_seed_records() -> list[dict[str, Any]]:
    try:
        from lattice_forge import Forge

        RUNTIME_ROOT.mkdir(parents=True, exist_ok=True)
        forge = Forge.open(RUNTIME_ROOT)
        status = forge.status()
        verify = forge.verify_seed()
        receipt_id = str(verify.get("receipt_id", "missing_receipt"))
        return [
            base_record(
                record_id="lattice:status",
                kind="lattice_seed",
                component="lattice_forge.Forge.status",
                status="pass" if status.get("seed_integrity") == "ok" else "fail",
                expected_path=LATTICE_FORGE_ROOT,
                actual_path=status.get("seed_db", ""),
                command="lattice-forge status",
                result_status=f"seed_integrity:{status.get('seed_integrity')}",
                evidence_level="self_check",
                output_summary={
                    "seed_sha256": status.get("seed_sha256"),
                    "overlay_db": status.get("overlay_db"),
                    "summary": status.get("summary", {}),
                },
            ),
            base_record(
                record_id="lattice:verify_seed",
                kind="lattice_seed",
                component="lattice_forge.Forge.verify_seed",
                status="pass" if verify.get("result", {}).get("status") == "pass" else "fail",
                expected_path=LATTICE_FORGE_ROOT,
                actual_path=status.get("seed_db", ""),
                command="lattice-forge verify-seed",
                result_status=str(verify.get("result", {}).get("status")),
                evidence_level=str(verify.get("evidence_level", "self_check")),
                receipt_id=receipt_id,
                output_summary=verify.get("result", {}),
            ),
        ]
    except Exception as exc:
        return [
            base_record(
                record_id="lattice:verify_seed",
                kind="lattice_seed",
                component="lattice_forge",
                status="fail",
                expected_path=LATTICE_FORGE_ROOT,
                actual_path="",
                command="lattice-forge verify-seed",
                result_status=repr(exc),
                evidence_level="self_check",
                blockers=["seed_verification_failed"],
            )
        ]


def forgefactory_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    try:
        from forgefactory.factory import compose
        from forgefactory.registry import list_engines

        engines = list_engines()
        composition = compose("CMPLX-Standards Forge/ReForge deployment smoke.")
        summary = composition.get("summary") or {}
        records.append(
            base_record(
                record_id="forgefactory:engines",
                kind="reforge_registry",
                component="forgefactory.registry",
                status="pass" if len(engines) >= 10 else "warn",
                expected_path=FORGEFACTORY_ROOT,
                actual_path=FORGEFACTORY_SRC / "forgefactory" / "registry.py",
                command="forgefactory engines",
                result_status=f"engine_count:{len(engines)}",
                evidence_level="curated_registry",
                output_summary={"engine_count": len(engines), "engines": engines},
                blockers=[] if len(engines) >= 10 else ["engine_count_below_expected"],
            )
        )
        records.append(
            base_record(
                record_id="forgefactory:smoke",
                kind="reforge_smoke",
                component="forgefactory.compose",
                status="pass" if summary.get("fragment_count", 0) >= 1 else "warn",
                expected_path=FORGEFACTORY_ROOT,
                actual_path=FORGEFACTORY_SRC / "forgefactory" / "factory.py",
                command="forgefactory smoke",
                result_status="compose_ok",
                evidence_level="runtime_smoke",
                output_summary=summary,
                blockers=[] if summary.get("fragment_count", 0) >= 1 else ["fragment_count_zero"],
            )
        )
    except Exception as exc:
        records.append(
            base_record(
                record_id="forgefactory:smoke",
                kind="reforge_smoke",
                component="forgefactory",
                status="fail",
                expected_path=FORGEFACTORY_ROOT,
                actual_path="",
                command="forgefactory smoke",
                result_status=repr(exc),
                evidence_level="runtime_smoke",
                blockers=["forgefactory_smoke_failed"],
            )
        )
    return records


def sample_lookup_record() -> dict[str, Any]:
    try:
        from lattice_forge import Forge

        forge = Forge.open(RUNTIME_ROOT)
        result = forge.can_close("G2", "A2^12")
        return base_record(
            record_id="lattice:sample_can_close:G2:A2_12",
            kind="forge_lookup",
            component="Forge.can_close",
            status="pass" if result.get("answer") else "fail",
            expected_path=LATTICE_FORGE_ROOT,
            actual_path=result.get("query_id", ""),
            command="lattice-forge can-close G2 A2^12",
            result_status=str(result.get("answer")),
            evidence_level=str(result.get("evidence_level", "")),
            receipt_id=str(result.get("receipt_id", "missing_receipt")),
            output_summary={
                "answer": result.get("answer"),
                "query_id": result.get("query_id"),
                "event_id": result.get("event_id"),
            },
        )
    except Exception as exc:
        return base_record(
            record_id="lattice:sample_can_close:G2:A2_12",
            kind="forge_lookup",
            component="Forge.can_close",
            status="fail",
            expected_path=LATTICE_FORGE_ROOT,
            actual_path="",
            command="lattice-forge can-close G2 A2^12",
            result_status=repr(exc),
            evidence_level="runtime_lookup",
            blockers=["sample_lookup_failed"],
        )


def build_forge_runtime_payload() -> dict[str, Any]:
    prepend_runtime_paths()
    records: list[dict[str, Any]] = []
    records.extend(
        [
            path_record("path:wrapper", "forge_runtime_env.ps1", WRAPPER),
            path_record("path:lattice_forge_root", "lattice-forge", LATTICE_FORGE_ROOT),
            path_record("path:forgefactory_root", "forgefactory", FORGEFACTORY_ROOT),
            path_record("path:runtime_root", "forge_reasoning_runtime", RUNTIME_ROOT),
        ]
    )
    records.extend(
        [
            package_record("lattice-forge", LATTICE_FORGE_ROOT),
            package_record("forgefactory", FORGEFACTORY_ROOT),
            package_record(
                "cqecmplx-forge",
                CMPLX_ROOT / "git-hosted-roots" / "CQECMPLX-Production" / "production",
            ),
        ]
    )
    records.extend(
        import_record(module_name, expected)
        for module_name, expected in sorted(EXPECTED_IMPORT_PREFIXES.items())
    )
    records.extend(lattice_seed_records())
    records.extend(forgefactory_records())
    records.append(sample_lookup_record())
    pass_count = sum(1 for row in records if row.get("status") == "pass")
    warn_count = sum(1 for row in records if row.get("status") == "warn")
    fail_count = sum(1 for row in records if row.get("status") == "fail")
    return {
        "schema": "cmplx_standards_forge_runtime_payload.v1",
        "adapter_id": "forge_runtime_adapter",
        "generated_utc": utc_now(),
        "runtime_root": str(RUNTIME_ROOT),
        "record_count": len(records),
        "pass_count": pass_count,
        "warn_count": warn_count,
        "fail_count": fail_count,
        "records": records,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build Forge/ReForge runtime standards payload")
    parser.add_argument(
        "-o",
        "--output",
        default=str(AUDIT_OUT / "FORGE_RUNTIME_STANDARDS_PAYLOAD.json"),
    )
    args = parser.parse_args(argv)
    payload = build_forge_runtime_payload()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(out),
                "record_count": payload["record_count"],
                "pass_count": payload["pass_count"],
                "warn_count": payload["warn_count"],
                "fail_count": payload["fail_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
