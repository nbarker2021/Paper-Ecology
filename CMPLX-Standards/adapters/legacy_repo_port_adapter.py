"""Port legacy repo work into CMPLX-Standards validation records.

The adapter has two lanes:

1. Executable/contract ports with real self-checks.
2. A broad whole-queue intake that treats every legacy ability seed as a
   standards-scored candidate so the reports reveal what to promote next.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tokenize
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .mdhg_memory_port import run_mdhg_self_check
except ImportError:  # direct script execution
    from mdhg_memory_port import run_mdhg_self_check

CMPLX_ROOT = Path(__file__).resolve().parents[2]
STANDARDS_DIR = Path(__file__).resolve().parents[1]
AUDIT_OUT = CMPLX_ROOT / "_drive-audit" / "output"
PARTSFACTORY_SRC = CMPLX_ROOT / "CMPLX-PartsFactory-main" / "src"
LEGACY_SEED_QUEUE = AUDIT_OUT / "LEGACY_REPO_ABILITY_SEED_QUEUE.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def path_status(paths: list[Path]) -> tuple[str, list[str]]:
    missing = [str(path) for path in paths if not path.exists()]
    return ("pass" if not missing else "warn", missing)


def _coerce_seed_paths(seed: dict[str, Any]) -> list[Path]:
    paths: list[Path] = []
    for entry in seed.get("source_paths") or []:
        if isinstance(entry, dict) and entry.get("path"):
            paths.append(Path(str(entry["path"])))
        elif isinstance(entry, str):
            paths.append(Path(entry))
    if seed.get("source_path"):
        main_path = Path(str(seed["source_path"]))
        if main_path not in paths:
            paths.insert(0, main_path)
    return paths


def _path_stats(paths: list[Path]) -> dict[str, Any]:
    existing = [path for path in paths if path.exists()]
    total_bytes = 0
    file_count = 0
    dir_count = 0
    suffixes: dict[str, int] = {}
    newest_mtime = 0.0
    for path in existing:
        try:
            stat = path.stat()
        except OSError:
            continue
        newest_mtime = max(newest_mtime, stat.st_mtime)
        if path.is_file():
            file_count += 1
            total_bytes += stat.st_size
            suffix = path.suffix.lower() or "[none]"
            suffixes[suffix] = suffixes.get(suffix, 0) + 1
        elif path.is_dir():
            dir_count += 1
    return {
        "declared_path_count": len(paths),
        "existing_path_count": len(existing),
        "missing_path_count": len(paths) - len(existing),
        "file_count": file_count,
        "dir_count": dir_count,
        "total_declared_bytes": total_bytes,
        "suffix_counts": dict(sorted(suffixes.items())),
        "newest_modified_utc": (
            datetime.fromtimestamp(newest_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
            if newest_mtime
            else None
        ),
    }


def _promotion_readiness(seed: dict[str, Any], path_stats: dict[str, Any]) -> dict[str, Any]:
    confidence = float(seed.get("confidence") or 0.0)
    port_mode = str(seed.get("port_mode") or "unknown")
    blockers = [str(item) for item in seed.get("blockers") or []]
    mode_score = {
        "direct_port": 1.0,
        "minor_rewrite": 0.82,
        "rebuild_better": 0.58,
    }.get(port_mode, 0.45)
    source_score = min(1.0, float(path_stats.get("existing_path_count") or 0) / 3.0)
    blocker_score = max(0.0, 1.0 - 0.12 * len(blockers))
    score = round(100.0 * confidence * mode_score * source_score * blocker_score, 3)
    if score >= 75:
        band = "promote_next"
    elif score >= 55:
        band = "promote_after_review"
    elif score >= 35:
        band = "needs_rewrite"
    else:
        band = "hold_for_evidence"
    return {
        "score": score,
        "band": band,
        "confidence": confidence,
        "port_mode": port_mode,
        "mode_score": mode_score,
        "source_score": round(source_score, 3),
        "blocker_score": round(blocker_score, 3),
        "blocker_count": len(blockers),
    }


def _syntax_probe(paths: list[Path], *, max_files: int = 80, max_bytes: int = 1_000_000) -> dict[str, Any]:
    py_paths = [path for path in paths if path.suffix.lower() == ".py" and path.exists() and path.is_file()]
    checked: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    for path in py_paths[:max_files]:
        try:
            size = path.stat().st_size
        except OSError as exc:
            failures.append({"path": str(path), "error": f"stat:{type(exc).__name__}:{exc}"})
            continue
        if size > max_bytes:
            skipped.append({"path": str(path), "reason": f"size>{max_bytes}", "bytes": size})
            continue
        try:
            with tokenize.open(path) as handle:
                source = handle.read()
            compile(source, str(path), "exec")
            checked.append({"path": str(path), "status": "pass", "bytes": size})
        except Exception as exc:
            failures.append({"path": str(path), "error": f"{type(exc).__name__}:{exc}", "bytes": size})
    if len(py_paths) > max_files:
        skipped.append({"path": "[remaining_python_files]", "reason": f"max_files>{max_files}", "count": len(py_paths) - max_files})
    return {
        "python_file_count": len(py_paths),
        "checked_count": len(checked),
        "passed_count": len(checked),
        "failed_count": len(failures),
        "skipped_count": len(skipped),
        "status": "pass" if not failures else "warn",
        "checked": checked,
        "failures": failures[:20],
        "skipped": skipped[:20],
    }


def base_record(
    *,
    port_id: str,
    source_seed: str,
    ability_family: str,
    destination: str,
    port_status: str,
    source_paths: list[Path],
    validation_status: str,
    validation_summary: dict[str, Any],
    honesty_boundary: str,
    blockers: list[str] | None = None,
) -> dict[str, Any]:
    source_state, missing = path_status(source_paths)
    all_blockers = list(blockers or [])
    all_blockers.extend(f"missing:{path}" for path in missing)
    if source_state != "pass" and port_status == "ported":
        port_status = "partial"
    return {
        "port_id": port_id,
        "source_seed": source_seed,
        "ability_family": ability_family,
        "source_paths": [str(path) for path in source_paths],
        "destination": destination,
        "port_status": port_status,
        "validation_status": validation_status,
        "validation_summary": validation_summary,
        "honesty_boundary": honesty_boundary,
        "blockers": all_blockers or ["none"],
        "provenance_label": "legacy_repo_port_adapter",
    }


def load_legacy_seed_queue() -> list[dict[str, Any]]:
    doc = load_json(LEGACY_SEED_QUEUE)
    if not isinstance(doc, dict):
        return []
    return [row for row in (doc.get("seeds") or []) if isinstance(row, dict)]


def broad_seed_record(seed: dict[str, Any]) -> dict[str, Any]:
    source_paths = _coerce_seed_paths(seed)
    stats = _path_stats(source_paths)
    syntax_probe = _syntax_probe(source_paths)
    readiness = _promotion_readiness(seed, stats)
    validation_status = "pass" if stats["existing_path_count"] else "indexed"
    blockers = [str(item) for item in seed.get("blockers") or []]
    return base_record(
        port_id=f"legacy-port:intake:{seed.get('seed_id', 'unknown')}",
        source_seed=str(seed.get("seed_id") or "unknown"),
        ability_family=str(seed.get("ability_family") or "unknown"),
        source_paths=source_paths,
        destination="CMPLX-Standards broad legacy intake / promotion queue",
        port_status="candidate_indexed",
        validation_status=validation_status,
        validation_summary={
            "seed_title": seed.get("title"),
            "source_repo": seed.get("source_repo"),
            "source_surface": seed.get("source_surface"),
            "port_mode": seed.get("port_mode"),
            "port_rationale": seed.get("port_rationale"),
            "pipeline_targets": seed.get("pipeline_targets") or [],
            "proposed_flcr_targets": seed.get("proposed_flcr_targets") or [],
            "forge_reforge_action": seed.get("forge_reforge_action"),
            "path_stats": stats,
            "syntax_probe": syntax_probe,
            "promotion_readiness": readiness,
            "candidate_checks": {
                "has_seed_id": bool(seed.get("seed_id")),
                "has_source_paths": bool(source_paths),
                "has_existing_source": bool(stats["existing_path_count"]),
                "has_pipeline_targets": bool(seed.get("pipeline_targets")),
                "has_flcr_targets": bool(seed.get("proposed_flcr_targets")),
                "has_port_mode": bool(seed.get("port_mode")),
                "syntax_probe_clean": syntax_probe["status"] == "pass",
            },
        },
        honesty_boundary=(
            "Broad intake record only. The source is indexed and scored for promotion; "
            "it is not yet an executable adapter unless another record with the same "
            "seed is marked ported or contract_bound."
        ),
        blockers=blockers or ["needs_executable_port_review"],
    )


def mdhg_record() -> dict[str, Any]:
    self_check = run_mdhg_self_check()
    return base_record(
        port_id="legacy-port:mdhg-memory-cache",
        source_seed="LEGACY-MDGH-MMDB-005",
        ability_family="mmdb_mdhg_memory_pipeline",
        source_paths=[
            Path(r"D:\repo_harvest\CMPLXDevKit\CMPLXLOCALMCP\mcp_os\agrm_mdhg_integration\mdhg_ca.py"),
            Path(r"D:\repo_harvest\CMPLXMCP\agrm_snap\mdhg_v0_2_2025_08_13.py"),
        ],
        destination=str(STANDARDS_DIR / "adapters" / "mdhg_memory_port.py"),
        port_status="ported",
        validation_status=str(self_check.get("status")),
        validation_summary=self_check,
        honesty_boundary=(
            "Stdlib MDHG slot/cache behavior is ported. Numpy AGRM/SNAP vector search "
            "remains lineage evidence for a later richer adapter."
        ),
    )


def _partsfactory_import_scope():
    if str(PARTSFACTORY_SRC) not in sys.path:
        sys.path.insert(0, str(PARTSFACTORY_SRC))
    os.environ.setdefault("SNAP_MINT_RECEIPT", "0")
    os.environ.setdefault("TARPIT_MINT_RECEIPT", "0")


def run_snap_runtime_self_check() -> dict[str, Any]:
    _partsfactory_import_scope()
    from cmplx.snap import SNAPEngine

    engine = SNAPEngine()
    label = engine.label(
        "e8 lattice function with subprocess",
        key="standards-port:snap-runtime",
        context={"tested": False},
    )
    dynamic = engine.labeler.register_dynamic_label(
        "crystal://standards-port/snap-runtime",
        "user-search-label",
    )
    ledger = engine.ledger_export()
    checks = {
        "structural_label": label.has("string") and label.has("text"),
        "domain_label": label.has("e8") and label.has("geometric"),
        "risk_label": label.has("uses_subprocess") and label.has("needs_review"),
        "dynamic_label": dynamic.has("user-search-label"),
        "ledger_verified": bool(ledger.get("verified")),
        "ledger_has_entry": int(ledger.get("length") or 0) >= 1,
    }
    status = "pass" if all(checks.values()) else "partial"
    return {
        "status": status,
        "checks": checks,
        "stats": {
            "rule_count": engine.labeler.rule_count,
            "ledger_length": ledger.get("length"),
            "ledger_head_present": bool(ledger.get("head")),
            "label_count": len(label.all_labels),
        },
        "sample_labels": label.to_dict(),
        "dynamic_label": dynamic.to_dict(),
    }


def snap_runtime_record() -> dict[str, Any]:
    self_check = run_snap_runtime_self_check()
    return base_record(
        port_id="legacy-port:snap-label-ledger-runtime",
        source_seed="LEGACY-TMN-CRYSTAL-001",
        ability_family="snap_labeling_crystal_memory",
        source_paths=[
            PARTSFACTORY_SRC / "cmplx" / "snap" / "labeler.py",
            PARTSFACTORY_SRC / "cmplx" / "snap" / "provider.py",
            PARTSFACTORY_SRC / "cmplx" / "snap" / "ledger.py",
            Path(r"D:\repo_harvest\CMPLX\core\src\cmplx\universal_access\snap_system.py"),
            Path(r"D:\repo_harvest\CMPLX\core\src\cmplx\misc\unified_snap.py"),
        ],
        destination=str(PARTSFACTORY_SRC / "cmplx" / "snap"),
        port_status="ported",
        validation_status=str(self_check.get("status")),
        validation_summary=self_check,
        honesty_boundary=(
            "SNAP literal and user labels plus ledger verification are executable "
            "in PartsFactory. Broader SNAPDNA/persona migration remains a separate port."
        ),
    )


def run_tarpit_runtime_self_check() -> dict[str, Any]:
    _partsfactory_import_scope()
    from cmplx.morphon import Morphon
    from cmplx.morphon.links import KEY_TARPIT_ATOM_ID, LINKAGE_MORPHON_TARPIT
    from cmplx.symbolic.tarpit.provider import TarPitSymbolicProvider

    provider = TarPitSymbolicProvider(default_max_steps=20, program_length=8)
    morphon = Morphon.forge(payload={"text": "standards-port:tarpit"})
    program = provider.encode_to_etp(morphon)
    atom_out, linked = provider.probe_atom_for_morphon(morphon)
    atom = atom_out.get("atom") or {}
    checks = {
        "program_length": len(program) == 8,
        "program_alphabet": all(ch in "}<>+01" for ch in program),
        "atom_id_present": bool(atom.get("atom_id")),
        "derivation_hash_present": bool(atom_out.get("derivation_hash")),
        "linkage_kind": linked.payload.get("linkage_kind") == LINKAGE_MORPHON_TARPIT,
        "linked_atom_id": linked.payload.get(KEY_TARPIT_ATOM_ID) == atom.get("atom_id"),
    }
    status = "pass" if all(checks.values()) else "partial"
    return {
        "status": status,
        "checks": checks,
        "stats": {
            "program_length": len(program),
            "default_dimension": provider.default_dimension,
            "default_max_steps": provider.default_max_steps,
            "atom_mass": atom.get("mass"),
        },
        "program": program,
        "atom": atom,
        "derivation_hash": atom_out.get("derivation_hash"),
        "linkage": {
            "morphon_id": linked.id,
            "tarpit_atom_id": linked.payload.get(KEY_TARPIT_ATOM_ID),
            "linkage_kind": linked.payload.get("linkage_kind"),
        },
    }


def tarpit_runtime_record() -> dict[str, Any]:
    self_check = run_tarpit_runtime_self_check()
    return base_record(
        port_id="legacy-port:tarpit-symbolic-provider-runtime",
        source_seed="LEGACY-PARTSFACTORY-LATTICE-016",
        ability_family="tarpit_symbolic_etp_morphon_bridge",
        source_paths=[
            PARTSFACTORY_SRC / "cmplx" / "symbolic" / "tarpit" / "provider.py",
            PARTSFACTORY_SRC / "cmplx" / "symbolic" / "tarpit" / "aggregation.py",
            PARTSFACTORY_SRC / "cmplx" / "symbolic" / "tarpit" / "atoms.py",
            PARTSFACTORY_SRC / "cmplx" / "symbolic" / "tarpit" / "ecology.py",
            Path(r"D:\repo_harvest\CMPLX\core\src\cmplx\unified_families\unified_tarpit.py"),
            Path(r"D:\repo_harvest\CMPLX\core\src\cmplx\adapters\tarpit_navigation_bridge.py"),
        ],
        destination=str(PARTSFACTORY_SRC / "cmplx" / "symbolic" / "tarpit"),
        port_status="ported",
        validation_status=str(self_check.get("status")),
        validation_summary=self_check,
        honesty_boundary=(
            "TarPit ETP encoding and morphon-to-atom linkage are executable in "
            "PartsFactory. Full tarpit chemistry/ecology sweep remains a larger runtime gate."
        ),
    )


def manifest_contract_record(
    *,
    port_id: str,
    source_seed: str,
    ability_family: str,
    manifest_path: Path,
    required_paths: list[Path],
    required_fields: list[str],
    required_terms: list[str],
    destination: str,
    honesty_boundary: str,
) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    text_blob = "\n".join(read_text(path) for path in required_paths)
    field_checks = {
        field: isinstance(manifest, dict) and bool(manifest.get(field))
        for field in required_fields
    }
    term_checks = {term: term.lower() in text_blob.lower() for term in required_terms}
    status = "pass" if all(field_checks.values()) and all(term_checks.values()) else "partial"
    return base_record(
        port_id=port_id,
        source_seed=source_seed,
        ability_family=ability_family,
        source_paths=[manifest_path, *required_paths],
        destination=destination,
        port_status="contract_bound",
        validation_status=status,
        validation_summary={
            "manifest_id": manifest.get("umbrella_id") if isinstance(manifest, dict) else None,
            "field_checks": field_checks,
            "term_checks": term_checks,
            "manifest_status": manifest.get("status") if isinstance(manifest, dict) else "missing",
        },
        honesty_boundary=honesty_boundary,
        blockers=[] if status == "pass" else ["contract_terms_or_fields_missing"],
    )


def build_legacy_repo_port_payload() -> dict[str, Any]:
    concrete_records = [
        mdhg_record(),
        snap_runtime_record(),
        tarpit_runtime_record(),
        manifest_contract_record(
            port_id="legacy-port:cmplx-morsr-contract",
            source_seed="LEGACY-MORSR-NVEST-013",
            ability_family="morsr_diagnostic_contract",
            manifest_path=CMPLX_ROOT / "CMPLX-MORSR" / "00_state_and_manifest" / "MASTER_MANIFEST.json",
            required_paths=[
                CMPLX_ROOT / "CMPLX-MORSR" / "02_engine_blueprint" / "MORSR_PULSE_PROTOCOL.md",
                CMPLX_ROOT / "CMPLX-MORSR" / "04_integration" / "CMPLX_PORT_BINDINGS.md",
            ],
            required_fields=["umbrella_id", "canonical_loop", "required_honesty_layer", "ports"],
            required_terms=["240-direction", "hidden guess", "receipt", "recenter"],
            destination="CMPLX-Standards legacy_repo_port model / future cmplx.morsr adapter",
            honesty_boundary="Contract scaffold only; final supplied MORSR implementation is not assumed.",
        ),
        manifest_contract_record(
            port_id="legacy-port:cqe-morsr-validation-loop",
            source_seed="LEGACY-MORSR-NVEST-013",
            ability_family="cqe_morsr_validation",
            manifest_path=CMPLX_ROOT / "CQE_MORSR" / "00_state_and_manifest" / "MASTER_MANIFEST.json",
            required_paths=[
                CMPLX_ROOT / "CQE_MORSR" / "02_engine_blueprint" / "CQE_MORSR_VALIDATION_LOOP.md",
                CMPLX_ROOT / "CQE_MORSR" / "04_integration" / "CQE_PIPELINE_BINDINGS.md",
            ],
            required_fields=["umbrella_id", "canonical_loop", "required_records", "required_cqe_layer"],
            required_terms=["seal expected result", "commit hidden guess", "reveal", "score"],
            destination="CMPLX-Standards hidden-result validation model",
            honesty_boundary="CQE_MORSR is a validation wrapper and receipt discipline, not the final MORSR engine.",
        ),
        manifest_contract_record(
            port_id="legacy-port:cmplx-nvest-adapter-contract",
            source_seed="LEGACY-MORSR-NVEST-013",
            ability_family="nvest_wave_diagnostic",
            manifest_path=CMPLX_ROOT / "CMPLX-NVEST" / "00_state_and_manifest" / "MASTER_MANIFEST.json",
            required_paths=[
                CMPLX_ROOT / "CMPLX-NVEST" / "04_integration" / "ADAPTER_CONTRACT.md",
                CMPLX_ROOT / "CMPLX-NVEST" / "02_engine_blueprint" / "ENGINE_PROTOCOL.md",
            ],
            required_fields=["umbrella_id", "canonical_loop", "required_honesty_layer", "required_cqe_layer"],
            required_terms=["translate_target", "decompose", "gate", "emit_receipt"],
            destination="CMPLX-Standards domain-neutral diagnostic application model",
            honesty_boundary="NVEST remains domain-neutral diagnostic scaffolding; finance-specific behavior requires separate evidence.",
        ),
    ]
    broad_records = [broad_seed_record(seed) for seed in load_legacy_seed_queue()]
    readiness_sorted = sorted(
        (
            {
                "source_seed": row["source_seed"],
                "ability_family": row["ability_family"],
                "readiness": row["validation_summary"]["promotion_readiness"],
                "pipeline_targets": row["validation_summary"]["pipeline_targets"],
                "source_path_count": row["validation_summary"]["path_stats"]["existing_path_count"],
            }
            for row in broad_records
        ),
        key=lambda row: row["readiness"]["score"],
        reverse=True,
    )
    records = [*concrete_records, *broad_records]
    return {
        "schema": "cmplx_standards_legacy_repo_port_payload.v1",
        "adapter_id": "legacy_repo_port_adapter",
        "generated_utc": utc_now(),
        "concrete_record_count": len(concrete_records),
        "broad_intake_record_count": len(broad_records),
        "record_count": len(records),
        "promotion_queue": readiness_sorted,
        "records": records,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build legacy repo port payload")
    parser.add_argument(
        "-o",
        "--output",
        default=str(AUDIT_OUT / "LEGACY_REPO_PORT_STANDARDS_PAYLOAD.json"),
    )
    args = parser.parse_args(argv)
    payload = build_legacy_repo_port_payload()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(out),
                "record_count": payload["record_count"],
                "statuses": {
                    status: sum(1 for row in payload["records"] if row["validation_status"] == status)
                    for status in sorted({row["validation_status"] for row in payload["records"]})
                },
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
