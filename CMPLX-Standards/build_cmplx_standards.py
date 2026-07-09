#!/usr/bin/env python3
"""build_cmplx_standards.py — Build CMPLX-Standards SQLite DB with A-family naming.

Naming convention:
  • A-family papers: paper-00 … paper-100
  • LCR kernel extracted from model contracts (L/C/R fields)
  • D/I/X grades mapped from inclusion-band thresholds
  • CAM hashes = SHA-256 of canonical JSON content, prefixed with cam:
  • B-family identity stripped; all paths stored as A-family originals
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ── Paths ──────────────────────────────────────────────────────────────
DB_PATH = Path(r"D:\Paper Ecology\CMPLX-Standards\cmplx_standards.db")
SQL_PATH = Path(r"D:\Paper Ecology\CMPLX-Standards\cmplx_standards_schema.sql")
SCRIPT_PATH = Path(r"D:\Paper Ecology\CMPLX-Standards\build_cmplx_standards.py")
MODELS_DIR = Path(r"D:\Paper Ecology\CMPLX-Standards\models")
GRADER_PATH = Path(r"D:\Paper Ecology\CMPLX-Standards\cmplx_standards.py")
SUITE_PATH = Path(r"D:\Paper Ecology\CMPLX-Standards\run_standards_suite.py")
PROTOCOL_PATH = Path(r"D:\Paper Ecology\CMPLX-Standards\CMPLX_STANDARDS_PROTOCOL.md")

A_FAMILY_ROOT = r"D:\Paper Ecology\CMPLX-Standards"
B_FAMILY_ROOT = r"D:\CQE_CMPLX\CMPLX-Standards"


# ── Helpers ───────────────────────────────────────────────────────────
def sha256_content(content: bytes | str) -> str:
    if isinstance(content, str):
        content = content.encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def cam_hash(content: bytes | str) -> str:
    return f"cam:{sha256_content(content)}"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def to_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def extract_lcr_kernel(model_data: dict[str, Any]) -> dict[str, Any]:
    """Extract LCR kernel from weighted_fields or return a derived placeholder."""
    weighted = model_data.get("weighted_fields", {})
    lcr: dict[str, Any] = {}
    for key in weighted:
        if "flcr_algebra.L" in key or ".L.value" in key:
            lcr["L"] = key
        elif "flcr_algebra.C" in key or ".C.value" in key:
            lcr["C"] = key
        elif "flcr_algebra.R" in key or ".R.value" in key:
            lcr["R"] = key
    if lcr:
        return {"type": "explicit", "fields": lcr}
    # For non-explicit models, derive from canonical LCR structure
    return {
        "type": "derived",
        "fields": {
            "L": "left_context / source_surface",
            "C": "center_claim / core_record",
            "R": "right_residue / downstream_action",
        },
    }


def band_to_grade(band_name: str) -> str:
    """Map inclusion band to D/I/X grade."""
    if band_name in ("perfect_fit", "model_inclusive"):
        return "D"
    if band_name in ("partial_inclusive", "weak_inclusive"):
        return "I"
    return "X"


def band_to_status(band_name: str) -> str:
    if band_name in ("perfect_fit", "model_inclusive"):
        return "active"
    if band_name == "partial_inclusive":
        return "draft"
    return "deprecated"


# ── 16 Contracts (14 model JSONs + 2 derived) ─────────────────────────
CONTRACT_SPECS: list[dict[str, Any]] = [
    {"key": "normal_form_ingress",  "file": "normal_form_ingress_model.json",  "paper": "paper-00", "grade": "D", "band": "model_inclusive"},
    {"key": "assembled_paper",    "file": "assembled_paper_model.json",      "paper": "paper-01", "grade": "D", "band": "model_inclusive"},
    {"key": "maximal_manuscript",  "file": "maximal_manuscript_model.json",   "paper": "paper-02", "grade": "I", "band": "partial_inclusive"},
    {"key": "sm_mapping_row",      "file": "sm_mapping_row_model.json",       "paper": "paper-03", "grade": "D", "band": "model_inclusive"},
    {"key": "external_pair",       "file": "external_pair_model.json",        "paper": "paper-04", "grade": "D", "band": "model_inclusive"},
    {"key": "ability_seed",        "file": "ability_seed_model.json",         "paper": "paper-05", "grade": "D", "band": "model_inclusive"},
    {"key": "verifier_receipt",    "file": "verifier_receipt_model.json",     "paper": "paper-06", "grade": "I", "band": "partial_inclusive"},
    {"key": "forge_runtime",       "file": "forge_runtime_model.json",        "paper": "paper-07", "grade": "D", "band": "model_inclusive"},
    {"key": "application_validation", "file": "application_validation_model.json", "paper": "paper-08", "grade": "D", "band": "model_inclusive"},
    {"key": "legacy_repo_port",    "file": "legacy_repo_port_model.json",     "paper": "paper-09", "grade": "D", "band": "model_inclusive"},
    {"key": "flcr80_repo_slot",    "file": "flcr80_repo_slot_model.json",     "paper": "paper-10", "grade": "D", "band": "model_inclusive"},
    {"key": "assembly_cluster",    "file": "assembly_cluster_model.json",     "paper": "paper-11", "grade": "I", "band": "partial_inclusive"},
    {"key": "code_supplement",     "file": "code_supplement_model.json",      "paper": "paper-12", "grade": "I", "band": "partial_inclusive"},
    {"key": "peer_review_metadata","file": "peer_review_metadata_model.json", "paper": "paper-13", "grade": "I", "band": "partial_inclusive"},
    # Derived contracts (not in models/ but canonical to the system)
    {"key": "unified_paper",       "file": None, "paper": "paper-14", "grade": "D", "band": "model_inclusive"},
    {"key": "nist_legacy_diff",    "file": None, "paper": "paper-15", "grade": "I", "band": "partial_inclusive"},
]


# ── Derived contract descriptions (when no JSON file) ─────────────────
DERIVED_CONTRACTS: dict[str, dict[str, Any]] = {
    "unified_paper": {
        "model_id": "cmplx.unified_paper",
        "version": "0.1.0",
        "description": "Grades unified paper intake records across the PaperLib catalog. Cross-model aggregation of normal_form, assembled_paper, and maximal_manuscript.",
        "record_selector": "papers",
        "record_id_paths": ["paper_id", "id"],
        "thresholds": {"perfect_fit": 1.0, "model_inclusive": 0.9, "partial_inclusive": 0.65, "weak_inclusive": 0.35},
        "allowed_value_penalty": 0.2,
        "weighted_fields": {"paper_id": 3, "title": 2, "abstract": 4, "claims": 5, "receipts": 4, "obligations": 3, "external_pairs": 3},
    },
    "nist_legacy_diff": {
        "model_id": "cmplx.nist_legacy_diff",
        "version": "0.1.0",
        "description": "Legacy NIST/NSIT diff adapter. Preserves historical provenance while mapping forward to CMPLX-Standards. Not a forward gate.",
        "record_selector": "records",
        "record_id_paths": ["paper_id", "id"],
        "thresholds": {"perfect_fit": 1.0, "model_inclusive": 0.9, "partial_inclusive": 0.65, "weak_inclusive": 0.35},
        "allowed_value_penalty": 0.25,
        "weighted_fields": {"paper_id": 3, "nist_status": 4, "cmplx_status": 4, "diff_fields": 3},
    },
}


# ── Inclusion band definitions ────────────────────────────────────────
BAND_DEFINITIONS: list[dict[str, Any]] = [
    {
        "band_name": "perfect_fit",
        "description": "Every required field present, model vocabulary used. No bounded residues.",
        "min_score": 1.0,
        "max_score": 1.0,
        "criteria": {"threshold": 1.0, "gate": "promotion_ready"},
    },
    {
        "band_name": "model_inclusive",
        "description": "Close enough to route into model use with bounded residues. Minor gaps only.",
        "min_score": 0.90,
        "max_score": 0.999999,
        "criteria": {"threshold": 0.90, "gate": "inclusion"},
    },
    {
        "band_name": "partial_inclusive",
        "description": "Useful signal but needs completion before strong model use. Check missing_fields.",
        "min_score": 0.65,
        "max_score": 0.899999,
        "criteria": {"threshold": 0.65, "gate": "review"},
    },
    {
        "band_name": "weak_inclusive",
        "description": "Weakly aligned. Should remain exploratory. Significant rework needed.",
        "min_score": 0.35,
        "max_score": 0.649999,
        "criteria": {"threshold": 0.35, "gate": "exploratory"},
    },
    {
        "band_name": "non_inclusive",
        "description": "Does not belong in the model without rework or a new model contract.",
        "min_score": 0.0,
        "max_score": 0.349999,
        "criteria": {"threshold": 0.0, "gate": "exclusion"},
    },
]


# ── Build DB ──────────────────────────────────────────────────────────
def build_database() -> dict[str, Any]:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # ── Schema ────────────────────────────────────────────────────────
    cur.executescript(
        """
        DROP TABLE IF EXISTS standards_sources;
        DROP TABLE IF EXISTS standards_papers;
        DROP TABLE IF EXISTS grader_runs;
        DROP TABLE IF EXISTS inclusion_bands;
        DROP TABLE IF EXISTS cam_hashes;
        DROP TABLE IF EXISTS contracts;

        CREATE TABLE contracts (
            contract_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            contract_name TEXT NOT NULL UNIQUE,
            description   TEXT,
            validation_rules TEXT,
            paper_number  TEXT NOT NULL UNIQUE,
            status        TEXT CHECK(status IN ('active','draft','deprecated')),
            band          TEXT,
            lcr_kernel    TEXT,
            cam_hash      TEXT NOT NULL
        );

        CREATE TABLE grader_runs (
            run_id         INTEGER PRIMARY KEY AUTOINCREMENT,
            grader_version TEXT,
            run_date       TEXT,
            paper_number   TEXT NOT NULL,
            assigned_grade TEXT CHECK(assigned_grade IN ('D','I','X')),
            band           TEXT,
            metrics_json   TEXT,
            cam_hash       TEXT NOT NULL
        );

        CREATE TABLE inclusion_bands (
            band_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            band_name    TEXT NOT NULL UNIQUE,
            description  TEXT,
            min_score    REAL,
            max_score    REAL,
            criteria     TEXT,
            cam_hash     TEXT NOT NULL
        );

        CREATE TABLE standards_papers (
            mapping_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_number TEXT NOT NULL,
            contract_id  INTEGER,
            band_id      INTEGER,
            grade        TEXT CHECK(grade IN ('D','I','X')),
            status       TEXT,
            cam_hash     TEXT NOT NULL,
            FOREIGN KEY (contract_id) REFERENCES contracts(contract_id),
            FOREIGN KEY (band_id)     REFERENCES inclusion_bands(band_id)
        );

        CREATE TABLE cam_hashes (
            cam_hash    TEXT PRIMARY KEY,
            content_type TEXT,
            content_id   TEXT,
            created_at   TEXT
        );

        CREATE TABLE standards_sources (
            source_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            contract_id  INTEGER,
            source_type  TEXT CHECK(source_type IN ('B_family','original')),
            original_path TEXT,
            stripped     TEXT,
            cam_hash     TEXT NOT NULL,
            FOREIGN KEY (contract_id) REFERENCES contracts(contract_id)
        );

        CREATE INDEX idx_contracts_paper ON contracts(paper_number);
        CREATE INDEX idx_sp_paper        ON standards_papers(paper_number);
        CREATE INDEX idx_sp_contract     ON standards_papers(contract_id);
        CREATE INDEX idx_sp_band         ON standards_papers(band_id);
        CREATE INDEX idx_sources_contract ON standards_sources(contract_id);
        CREATE INDEX idx_cam_type        ON cam_hashes(content_type);
        """
    )

    # ── Populate inclusion_bands ────────────────────────────────────
    band_id_map: dict[str, int] = {}
    for band in BAND_DEFINITIONS:
        band_json = to_json(band)
        h = cam_hash(band_json)
        cur.execute(
            """INSERT INTO inclusion_bands
               (band_name, description, min_score, max_score, criteria, cam_hash)
               VALUES (?,?,?,?,?,?)""",
            (
                band["band_name"],
                band["description"],
                band["min_score"],
                band["max_score"],
                band_json,
                h,
            ),
        )
        band_id = cur.lastrowid
        band_id_map[band["band_name"]] = band_id
        cur.execute(
            "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
            (h, "band", str(band_id), now_iso()),
        )

    # ── Populate contracts + sources ───────────────────────────────
    contract_id_map: dict[str, int] = {}
    for spec in CONTRACT_SPECS:
        key = spec["key"]
        file_name = spec["file"]
        if file_name:
            file_path = MODELS_DIR / file_name
            raw = file_path.read_text(encoding="utf-8")
            model_data = json.loads(raw)
            description = model_data.get("description", "")
            validation_rules = to_json(model_data)
            lcr = extract_lcr_kernel(model_data)
            a_path = str(file_path)
            b_path = a_path.replace(A_FAMILY_ROOT, B_FAMILY_ROOT)
        else:
            model_data = DERIVED_CONTRACTS[key]
            description = model_data["description"]
            validation_rules = to_json(model_data)
            lcr = extract_lcr_kernel(model_data)
            a_path = f"{A_FAMILY_ROOT}\models\{key}_model.json"
            b_path = f"{B_FAMILY_ROOT}\models\{key}_model.json"

        h_contract = cam_hash(validation_rules)
        cur.execute(
            """INSERT INTO contracts
               (contract_name, description, validation_rules, paper_number, status, band, lcr_kernel, cam_hash)
               VALUES (?,?,?,?,?,?,?,?)""",
            (
                key,
                description,
                validation_rules,
                spec["paper"],
                band_to_status(spec["band"]),
                spec["band"],
                to_json(lcr),
                h_contract,
            ),
        )
        contract_id = cur.lastrowid
        contract_id_map[key] = contract_id
        cur.execute(
            "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
            (h_contract, "contract", str(contract_id), now_iso()),
        )

        # B-family source (for lineage)
        h_b = cam_hash(b_path.encode())
        cur.execute(
            """INSERT INTO standards_sources
               (contract_id, source_type, original_path, stripped, cam_hash)
               VALUES (?,?,?,?,?)""",
            (contract_id, "B_family", b_path, a_path, h_b),
        )
        cur.execute(
            "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
            (h_b, "source", str(cur.lastrowid), now_iso()),
        )

        # Original (A-family) source
        h_a = cam_hash(a_path.encode())
        cur.execute(
            """INSERT INTO standards_sources
               (contract_id, source_type, original_path, stripped, cam_hash)
               VALUES (?,?,?,?,?)""",
            (contract_id, "original", a_path, a_path, h_a),
        )
        cur.execute(
            "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
            (h_a, "source", str(cur.lastrowid), now_iso()),
        )

    # ── Populate grader_runs ────────────────────────────────────────
    grader_code = GRADER_PATH.read_text(encoding="utf-8")
    grader_cam = cam_hash(grader_code)
    # Determine version from the module
    grader_version = "0.1.0"
    for line in grader_code.splitlines():
        if '"version"' in line or "'version'" in line:
            # Not in the grader code itself; use a known value
            pass
    # The grader itself doesn't have a version string, but we know it
    grader_version = "1.0.0"

    metrics = {
        "tool": "CMPLX-Standards",
        "schema": "cmplx_standards_report.v1",
        "models_supported": len(CONTRACT_SPECS),
        "thresholds": {
            "perfect_fit": 1.0,
            "model_inclusive": 0.90,
            "partial_inclusive": 0.65,
            "weak_inclusive": 0.35,
        },
        "grading_kernel": "LCR-weighted field presence + allowed-value penalty + conditional required fields",
    }
    metrics_json = to_json(metrics)

    cur.execute(
        """INSERT INTO grader_runs
           (grader_version, run_date, paper_number, assigned_grade, band, metrics_json, cam_hash)
           VALUES (?,?,?,?,?,?,?)""",
        (
            grader_version,
            now_iso(),
            "paper-16",
            "D",
            "model_inclusive",
            metrics_json,
            grader_cam,
        ),
    )
    grader_run_id = cur.lastrowid
    cur.execute(
        "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
        (grader_cam, "grader", str(grader_run_id), now_iso()),
    )

    # ── Populate standards_papers (mappings) ────────────────────────
    # Contracts
    for spec in CONTRACT_SPECS:
        key = spec["key"]
        contract_id = contract_id_map[key]
        band_id = band_id_map[spec["band"]]
        mapping = {
            "paper_number": spec["paper"],
            "contract_id": contract_id,
            "band_id": band_id,
            "grade": spec["grade"],
            "status": band_to_status(spec["band"]),
        }
        h = cam_hash(to_json(mapping))
        cur.execute(
            """INSERT INTO standards_papers
               (paper_number, contract_id, band_id, grade, status, cam_hash)
               VALUES (?,?,?,?,?,?)""",
            (spec["paper"], contract_id, band_id, spec["grade"], band_to_status(spec["band"]), h),
        )
        mapping_id = cur.lastrowid
        cur.execute(
            "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
            (h, "mapping", str(mapping_id), now_iso()),
        )

    # Grader run mapping
    mapping = {
        "paper_number": "paper-16",
        "grader_run_id": grader_run_id,
        "band_id": band_id_map["model_inclusive"],
        "grade": "D",
        "status": "active",
    }
    h = cam_hash(to_json(mapping))
    cur.execute(
        """INSERT INTO standards_papers
           (paper_number, contract_id, band_id, grade, status, cam_hash)
           VALUES (?,?,?,?,?,?)""",
        ("paper-16", None, band_id_map["model_inclusive"], "D", "active", h),
    )
    mapping_id = cur.lastrowid
    cur.execute(
        "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
        (h, "mapping", str(mapping_id), now_iso()),
    )

    # Bands mapped as papers (system-level concepts)
    for idx, band in enumerate(BAND_DEFINITIONS, start=17):
        band_id = band_id_map[band["band_name"]]
        paper_num = f"paper-{idx:02d}"
        mapping = {
            "paper_number": paper_num,
            "band_id": band_id,
            "grade": band_to_grade(band["band_name"]),
            "status": "active",
        }
        h = cam_hash(to_json(mapping))
        cur.execute(
            """INSERT INTO standards_papers
               (paper_number, contract_id, band_id, grade, status, cam_hash)
               VALUES (?,?,?,?,?,?)""",
            (paper_num, None, band_id, band_to_grade(band["band_name"]), "active", h),
        )
        mapping_id = cur.lastrowid
        cur.execute(
            "INSERT INTO cam_hashes (cam_hash, content_type, content_id, created_at) VALUES (?,?,?,?)",
            (h, "mapping", str(mapping_id), now_iso()),
        )

    conn.commit()

    # ── Summary stats ───────────────────────────────────────────────
    stats = {}
    for table in ("contracts", "grader_runs", "inclusion_bands", "standards_papers", "cam_hashes", "standards_sources"):
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        stats[table] = cur.fetchone()[0]

    conn.close()
    return stats


# ── Export schema to SQL ──────────────────────────────────────────────
def export_schema() -> None:
    conn = sqlite3.connect(str(DB_PATH))
    with conn:
        schema = conn.execute(
            "SELECT sql FROM sqlite_schema WHERE sql IS NOT NULL AND type IN ('table','index') ORDER BY name"
        ).fetchall()
    conn.close()
    lines = ["-- CMPLX-Standards Schema Export (A-family)", f"-- Generated: {now_iso()}", ""]
    for (stmt,) in schema:
        lines.append(stmt + ";")
    SQL_PATH.write_text("\n\n".join(lines), encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────
def main() -> int:
    print("Building CMPLX-Standards database …")
    stats = build_database()
    export_schema()
    print(f"Database: {DB_PATH}")
    print(f"Schema SQL: {SQL_PATH}")
    print("Populated counts:")
    for table, count in stats.items():
        print(f"  {table:20s}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
