# Crystal Memory Builder Script — Technical Analysis & A-Family Rewrite

> **Source:** `D:\CQE_CMPLX\tools\build_cam_crystal_memory_bank.py`  
> **Target Workspace:** `D:\Paper Ecology\CrystalLib`  
> **Analysis Date:** 2025-07-04  
> **All B-family identifiers stripped; rewritten in A-family terms (paper-00..paper-100, LCR kernel, D/I/X, CAM).**

---

## 1. What the Script Does (Function by Function, Line by Line)

### Module Header & Imports (lines 1–9)
```python
from __future__ import annotations
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
```
- Standard Python imports. `hashlib` for SHA-256 content addressing. `defaultdict` for slot/decision grouping. `pathlib` for cross-platform paths. `typing.Any` for dynamic JSON payloads.

### Root Configuration (lines 12–17)
```python
ROOT_CANDIDATES = [
    Path(r"D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models"),
    Path(r"D:\Paper Reworks\publication_series\Formalizing_LCR_Unifying_Standard_Models"),
]
ROOT = next((path for path in ROOT_CANDIDATES if path.exists()), ROOT_CANDIDATES[0])
MEMORY_ROOT = ROOT / "CAM_CRYSTAL_MEMORY_BANK"
```
- Tries two hardcoded Windows paths to find the publication series root. Falls back to the first candidate if neither exists. Defines `MEMORY_ROOT` as a subdirectory named `CAM_CRYSTAL_MEMORY_BANK`.
- **A-family mapping:** This root is the LCR kernel paper series home. The memory bank is the CAM (Content-Addressed Memory) crystal store for papers paper-00 through paper-100.

### Source File Manifest (lines 19–34)
```python
SOURCE_FILES = [
    "MASTER_DOCS_ROUTING_DOCTRINE.json",
    "D_DRIVE_INVENTORY_PAPER_GAP_PASS.json",
    "PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_INDEX.json",
    ... 14 total files
]
```
- Hardcoded list of 14 JSON state files that serve as **input feeds** to the memory builder. Each file represents a pipeline stage (intake, gap analysis, pairwise packaging, evidence scoring, etc.).
- **A-family mapping:** These are the LCR kernel intake manifests — routing doctrine, gap passes, evidence packages, discovery synthesis, archive intake, database port queues, and the slot-1..80 generalized ontology.

### Utility: `load_json` (lines 37–45)
```python
def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists(): return default
    for encoding in ("utf-8-sig", "utf-16", "utf-16-le"):
        try: return json.loads(path.read_text(encoding=encoding))
        except Exception: continue
    return default
```
- Resilient JSON loader with three encoding fallbacks. Returns `default` (usually `None`) if the file is missing or unreadable. This makes the pipeline **fault-tolerant** — missing source files do not crash the build.

### Utility: `stable_json` (lines 48–49)
```python
def stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
```
- Canonical JSON serialization. `sort_keys=True` ensures deterministic ordering. `ensure_ascii=True` and compact `separators` guarantee byte-for-byte stability across runs. This is the **pre-image** for the content-address hash.

### Utility: `address` (lines 52–53)
```python
def address(value: Any) -> str:
    return hashlib.sha256(stable_json(value).encode("utf-8")).hexdigest()
```
- Computes a **SHA-256 content address** (hex string) for any JSON-serializable value. This is the core CAM primitive: every state, every crystal, every record gets a cryptographically stable hash.

### Utility: `slug` (lines 56–58)
```python
def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return re.sub(r"_+", "_", value)[:96] or "state"
```
- Sanitizes a string into a filesystem-safe label: alphanumeric-only, collapsed underscores, max 96 characters. Used for directory and filename stems.

### Utility: `write_json` (lines 61–64)
```python
def write_json(path: Path, value: Any) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2), encoding="utf-8")
    return str(path)
```
- Idempotent JSON writer. Auto-creates parent directories. Pretty-prints with 2-space indent. Returns the written path as a string for logging.

### Utility: `write_md` (lines 67–70)
```python
def write_md(path: Path, lines: list[str]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)
```
- Markdown writer. Joins a list of strings with newlines. Same directory-autocreation behavior.

### Source State Loader: `source_states` (lines 73–90)
```python
def source_states() -> list[dict[str, Any]]:
    states = []
    for name in SOURCE_FILES:
        path = ROOT / name
        data = load_json(path)
        if data is None: continue
        state = {
            "kind": "source_state",
            "name": name,
            "path": str(path),
            "generated_utc": data.get("generated_utc") if isinstance(data, dict) else None,
            "content_address": address(data),
            "summary": summarize_source(name, data),
            "payload": data,
        }
        states.append(state)
    return states
```
- Iterates over the 14 `SOURCE_FILES`. For each file that exists and parses, builds a **source-state envelope** with:
  - `kind`: always `"source_state"`
  - `name`: filename
  - `path`: absolute path
  - `generated_utc`: timestamp if present in the dict
  - `content_address`: SHA-256 of the entire parsed JSON payload
  - `summary`: human-readable one-liner from `summarize_source`
  - `payload`: the raw parsed data (this field is later stripped before writing to disk, but kept in-memory for downstream crystal builders)
- Missing files are silently skipped (`continue`).

### Source Summarizer: `summarize_source` (lines 93–108)
```python
def summarize_source(name: str, data: Any) -> str:
    if not isinstance(data, dict): return "non-dict json source"
    if "package_count" in data: return f"{data.get('package_count')} pairwise packages"
    if "record_count" in data: return f"{data.get('record_count')} scored evidence records"
    if "counts" in data: return f"counts {data.get('counts')}"
    if "candidate_count" in data: return f"{data.get('candidate_count')} external pairing candidates"
    if "local_target_count" in data: return f"{data.get('local_target_count')} local targets; ..."
    if "missing" in data: return f"missing {data.get('missing', {}).get('missing_count')} artifacts"
    return str(data.get("purpose") or data.get("schema") or "json state")
```
- Heuristic summarizer. Looks for well-known keys (`package_count`, `record_count`, `counts`, `candidate_count`, `local_target_count`, `missing`) and returns a short descriptive string. If nothing matches, falls back to `purpose`, `schema`, or generic `"json state"`.
- **Purpose:** Gives the memory index human-readable summaries without loading full payloads.

### Crystal Builder: `package_crystals` (lines 111–133)
```python
def package_crystals(pairwise: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for package in pairwise.get("packages", []):
        crystal = {
            "kind": "package_crystal",
            "granularity": "pairwise_package",
            "package_id": package.get("package_id"),
            "title": package.get("title"),
            "faces": { ... },
        }
        crystal["content_address"] = address(crystal)
        crystals.append(crystal)
    return crystals
```
- Transforms each entry in `packages` (from `PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_INDEX.json`) into a **package crystal**.
- `faces` captures: internal source, external publication, correlation, claim lane, crystal faces, paper routes, obligations, NIST review, validation review.
- After the crystal dict is fully populated, it computes its own `content_address` (hash of the crystal itself) and appends it to the list.
- **A-family mapping:** A "package" is a pairwise evidence bundle linking a paper slot (e.g., paper-42) to an external source. The `faces` are the D/I/X facets of that linkage.

### Crystal Builder: `notebook_crystals` (lines 136–169)
```python
def notebook_crystals(notebook: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_slot: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in notebook.get("records", []):
        decision = (record.get("score_notebook") or {}).get("decision", "UNKNOWN")
        by_decision[decision].append(record)
        for slot in record.get("slot_assignments", []):
            by_slot[slot].append(record)
    # ... builds slot_crystals and decision_crystals
```
- Reads the `EVIDENCE_INTAKE_SCORE_NOTEBOOK.json` and **indexes every record twice**:
  1. By `slot` (slot assignments) — produces `slot_crystals`
  2. By `decision` (assembly decision) — produces `decision_crystals`
- **Slot crystals:** one per unique slot, capped at 80 records per slot (`records[:80]`), includes `decision_counts` histogram.
- **Decision crystals:** one per unique decision, capped at 100 records per decision (`records[:100]`).
- Both receive their own `content_address`.
- **A-family mapping:** Slots map directly to `paper-00` through `paper-100`. Decisions are assembly-verdict buckets (e.g., ACCEPT, REJECT, REVISE, HOLD).

### Crystal Builder: `source_family_crystals` (lines 172–198)
```python
def source_family_crystals(gap: dict[str, Any], synthesis: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for item in (gap.get("missing") or {}).get("root_summary", [])[:50]:
        crystal = { ... "frame": "D-drive inventory gap source-family view" ... }
    for target in synthesis.get("local_targets", []):
        crystal = { ... "frame": "agent-discovered first-intake target" ... }
```
- Builds two sub-families of crystals from the gap analysis and agent-discovery synthesis:
  1. **Gap crystals:** up to 50 root-summary items showing missing artifacts per source family.
  2. **Target crystals:** every `local_targets` entry from the synthesis pass, showing rank, artifact name, rationale, and suggested slots.
- Each gets a `frame` string describing its semantic role.
- **A-family mapping:** Source families are LCR kernel derivation lineages (D-tags). Local targets are candidate artifacts to be ingested into the paper series.

### Crystal Builder: `archive_crystals` (lines 201–219)
```python
def archive_crystals(archive_pass: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for archive in archive_pass.get("archives", [])[:200]:
        crystal = {
            "kind": "archive_crystal",
            "granularity": "archive",
            "archive_id": ...,
            "path": ...,
            "name": ...,
            "archive_kind": ...,
            "entry_count_indexed": ...,
            "high_signal_entry_count": ...,
            "slot_families": ...,
            "slot_assignments": ...,
            "frame": "archive-intake content and source-card discovery view",
        }
```
- Transforms up to 200 archive entries from `ARCHIVE_INTAKE_PASS.json` into **archive crystals**.
- Captures archive metadata: ID, path, name, kind, entry counts, slot families/assignments.
- `frame` labels it as an archive-intake view.
- **A-family mapping:** Archives are bulk intake bundles (ZIPs, tarballs, legacy dumps) that feed into the paper-00..paper-100 pipeline.

### Crystal Builder: `database_crystals` (lines 222–251)
```python
def database_crystals(database_pass: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for db in database_pass.get("databases", [])[:160]:
        signal_tables = [
            {"table": ..., "row_count": ..., "signal_columns": ...}
            for table in db.get("tables", [])
            if table.get("table_signal")
        ]
        crystal = {
            "kind": "cam_database_crystal",
            "granularity": "database",
            "db_id": ...,
            "path": ...,
            "name": ...,
            "status": ...,
            "signal_score": ...,
            "port_recommendation": ...,
            "table_count": ...,
            "signal_tables": signal_tables[:40],
            "slot_families": ...,
            "slot_assignments": ...,
            "frame": "existing CAM/database addressing port view",
        }
```
- Transforms up to 160 database entries from `CAM_DATABASE_INTAKE_PASS.json` into **CAM database crystals**.
- Filters tables to only those with `table_signal=True` (high-signal tables), caps at 40 signal tables per crystal.
- Captures port recommendation, signal score, status, and slot mapping.
- **A-family mapping:** These are legacy SQLite/DB intakes that need to be ported into the A-family CAM. `port_recommendation` becomes the migration route to paper-00..paper-100.

### Helper: `count_decisions` (lines 254–259)
```python
def count_decisions(records: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        decision = (record.get("score_notebook") or {}).get("decision", "UNKNOWN")
        counts[decision] = counts.get(decision, 0) + 1
    return counts
```
- Simple histogram builder. Returns `{decision_string: count}` for a list of records.

### Helper: `record_summary` (lines 262–274)
```python
def record_summary(record: dict[str, Any]) -> dict[str, Any]:
    score = record.get("score_notebook") or {}
    return {
        "record_id": record.get("record_id"),
        "record_type": record.get("record_type"),
        "title": record.get("title"),
        "decision": score.get("decision"),
        "assembly_score": score.get("assembly_score"),
        "slot_families": record.get("slot_families", []),
        "slot_assignments": record.get("slot_assignments", []),
        "external_paper_title": record.get("external_paper_title"),
        "source_identity": record.get("source_identity"),
    }
```
- Projects a full record into a compact summary. Strips heavy payloads to keep crystal files small. Preserves identity, typing, scoring, and slot mapping.

### Orchestrator: `build_bank` (lines 277–357)
```python
def build_bank() -> dict[str, Any]:
    sources = source_states()
    source_by_name = {state["name"]: state["payload"] for state in sources}
    pairwise = source_by_name.get("PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_INDEX.json", {}) or {}
    notebook = source_by_name.get("EVIDENCE_INTAKE_SCORE_NOTEBOOK.json", {}) or {}
    gap = source_by_name.get("D_DRIVE_INVENTORY_PAPER_GAP_PASS.json", {}) or {}
    synthesis = source_by_name.get("AGENT_DISCOVERY_SYNTHESIS_PASS.json", {}) or {}
    archive_pass = source_by_name.get("ARCHIVE_INTAKE_PASS.json", {}) or {}
    database_pass = source_by_name.get("CAM_DATABASE_INTAKE_PASS.json", {}) or {}
```
- **Phase 1: Load all source states** into memory via `source_states()`.
- **Phase 2: Demux by filename** into six typed buckets: `pairwise`, `notebook`, `gap`, `synthesis`, `archive_pass`, `database_pass`.
- Missing buckets default to `{}` (empty dict), so the script is resilient to partial source availability.

```python
    packages = package_crystals(pairwise)
    slot_crystals, decision_crystals = notebook_crystals(notebook)
    source_families = source_family_crystals(gap, synthesis)
    archives = archive_crystals(archive_pass)
    databases = database_crystals(database_pass)
    all_crystals = packages + slot_crystals + decision_crystals + source_families + archives + databases
```
- **Phase 3: Build all crystal families** in parallel (no interdependencies between families). Concatenates into `all_crystals`.

```python
    generated = datetime.now(timezone.utc).isoformat()
    index = {
        "schema": "flcr.cam_crystal_memory_bank.v1",
        "generated_utc": generated,
        "root": str(ROOT),
        "memory_root": str(MEMORY_ROOT),
        "source_states": [
            {k: v for k, v in state.items() if k != "payload"}
            for state in sources
        ],
        "crystal_counts": { ... },
        "crystals": [ ... ],
    }
```
- **Phase 4: Build the memory index.** Strips `payload` from source states (to keep the index lightweight). Includes counts and a crystal manifest with `kind`, `granularity`, `content_address`, `path`, and `label`.

```python
    write_json(MEMORY_ROOT / "CAM_MEMORY_INDEX.json", index)
    write_md(MEMORY_ROOT / "CAM_MEMORY_INDEX.md", [ ... ])
```
- **Phase 5: Write the index** as both JSON (machine) and Markdown (human).

```python
    for state in sources:
        write_json(MEMORY_ROOT / "states" / f"{slug(state['name'])}.{state['content_address'][:12]}.json",
                    {k: v for k, v in state.items() if k != "payload"})
    for crystal in all_crystals:
        write_json(Path(crystal_path(crystal)), crystal)
    return index
```
- **Phase 6: Write individual artifacts.**
  - Source states go to `states/<slug>.<hash_prefix>.json` (payload stripped).
  - Crystals go to `crystals/<kind>/<label>.<hash_prefix>.json`.

### Label & Path Helpers: `crystal_label`, `crystal_path` (lines 360–376)
```python
def crystal_label(crystal: dict[str, Any]) -> str:
    return (
        crystal.get("package_id")
        or crystal.get("slot")
        or crystal.get("decision")
        or crystal.get("source_family")
        or crystal.get("artifact")
        or crystal.get("kind")
        or "crystal"
    )
```
- Priority-ordered fallback for human-readable crystal identity. First non-null wins.

```python
def crystal_path(crystal: dict[str, Any]) -> str:
    kind = crystal.get("kind", "crystal")
    label = slug(str(crystal_label(crystal)))
    addr = crystal.get("content_address", address(crystal))[:12]
    return str(MEMORY_ROOT / "crystals" / kind / f"{label}.{addr}.json")
```
- Builds a filesystem path: `CAM_CRYSTAL_MEMORY_BANK/crystals/<kind>/<label>.<hash_prefix>.json`.
- If no `content_address` exists, computes one on the fly.

### Entry Point: `main` (lines 379–395)
```python
def main() -> None:
    MEMORY_ROOT.mkdir(parents=True, exist_ok=True)
    index = build_bank()
    print(json.dumps({
        "memory_index": str(MEMORY_ROOT / "CAM_MEMORY_INDEX.md"),
        "memory_index_json": str(MEMORY_ROOT / "CAM_MEMORY_INDEX.json"),
        "crystal_counts": index["crystal_counts"],
    }, indent=2))
```
- Ensures `MEMORY_ROOT` exists, runs the build, prints a summary JSON to stdout.

---

## 2. Data Structures Created

### 2.1 Source State Envelope
```json
{
  "kind": "source_state",
  "name": "EVIDENCE_INTAKE_SCORE_NOTEBOOK.json",
  "path": "D:\\...\\EVIDENCE_INTAKE_SCORE_NOTEBOOK.json",
  "generated_utc": "2025-06-17T01:05:00Z",
  "content_address": "a1b2c3d4...",
  "summary": "4500 scored evidence records",
  "payload": { ... raw JSON ... }
}
```
- **14 instances** (one per source file). `payload` is present in-memory but stripped on disk.

### 2.2 Package Crystal
```json
{
  "kind": "package_crystal",
  "granularity": "pairwise_package",
  "package_id": "pkg-042-001",
  "title": "...",
  "faces": {
    "internal_source": "...",
    "external_publication": "...",
    "correlation": "...",
    "claim_lane": "...",
    "crystal_faces": [...],
    "paper_routes": [...],
    "obligations": [...],
    "nist_review": "...",
    "validation_review": "..."
  },
  "content_address": "..."
}
```
- One per pairwise evidence package. `faces` is the multi-faceted view of the package.

### 2.3 Slot Crystal
```json
{
  "kind": "slot_crystal",
  "granularity": "slot",
  "slot": "slot_42",
  "record_count": 37,
  "decision_counts": {"ACCEPT": 30, "HOLD": 7},
  "records": [ ... up to 80 summaries ... ],
  "content_address": "..."
}
```
- One per slot. Aggregates all evidence records assigned to that slot.

### 2.4 Decision Crystal
```json
{
  "kind": "decision_crystal",
  "granularity": "assembly_decision",
  "decision": "ACCEPT",
  "record_count": 1204,
  "records": [ ... up to 100 summaries ... ],
  "content_address": "..."
}
```
- One per unique decision string. Aggregates records across all slots that share that decision.

### 2.5 Source Family Crystal
```json
{
  "kind": "source_family_crystal",
  "granularity": "source_family",
  "source_family": "...",
  "missing_count": 12,
  "highest_score": 0.92,
  "sample_files": [...],
  "frame": "D-drive inventory gap source-family view",
  "content_address": "..."
}
```
- Or (for local targets):
```json
{
  "kind": "source_family_crystal",
  "granularity": "local_intake_target",
  "rank": 1,
  "artifact": "...",
  "why_it_matters": "...",
  "suggested_slots": ["slot_12", "slot_33"],
  "frame": "agent-discovered first-intake target",
  "content_address": "..."
}
```

### 2.6 Archive Crystal
```json
{
  "kind": "archive_crystal",
  "granularity": "archive",
  "archive_id": "...",
  "path": "...",
  "name": "...",
  "archive_kind": "zip",
  "entry_count_indexed": 1500,
  "high_signal_entry_count": 340,
  "slot_families": [...],
  "slot_assignments": [...],
  "frame": "archive-intake content and source-card discovery view",
  "content_address": "..."
}
```

### 2.7 CAM Database Crystal
```json
{
  "kind": "cam_database_crystal",
  "granularity": "database",
  "db_id": "...",
  "path": "...",
  "name": "...",
  "status": "active",
  "signal_score": 0.87,
  "port_recommendation": "migrate_to_slot_55",
  "table_count": 23,
  "signal_tables": [
    {"table": "claims", "row_count": 1200, "signal_columns": ["claim_id", "slot"]}
  ],
  "slot_families": [...],
  "slot_assignments": [...],
  "frame": "existing CAM/database addressing port view",
  "content_address": "..."
}
```

### 2.8 Memory Index (Master Manifest)
```json
{
  "schema": "flcr.cam_crystal_memory_bank.v1",
  "generated_utc": "2025-07-04T...Z",
  "root": "D:\\...",
  "memory_root": "D:\\...\\CAM_CRYSTAL_MEMORY_BANK",
  "source_states": [ ... ],
  "crystal_counts": {
    "package_crystals": N,
    "slot_crystals": N,
    "decision_crystals": N,
    "source_family_crystals": N,
    "archive_crystals": N,
    "cam_database_crystals": N,
    "total": N
  },
  "crystals": [
    {"kind": "...", "granularity": "...", "content_address": "...", "path": "...", "label": "..."}
  ]
}
```

---

## 3. Output Format

The script produces a **filesystem-based content-addressed store** (no SQLite, no central DB server). Everything is JSON + Markdown on disk.

### Directory Layout
```
CAM_CRYSTAL_MEMORY_BANK/
├── CAM_MEMORY_INDEX.json          # master manifest (JSON)
├── CAM_MEMORY_INDEX.md            # master manifest (Markdown)
├── states/
│   ├── MASTER_DOCS_ROUTING_DOCTRINE.a1b2c3d4.json
│   ├── D_DRIVE_INVENTORY_PAPER_GAP_PASS.e5f6g7h8.json
│   └── ... (one per source file)
└── crystals/
    ├── package_crystal/
    │   └── pkg_042_001.x1y2z3.json
    ├── slot_crystal/
    │   └── slot_42.w4q5r6.json
    ├── decision_crystal/
    │   └── ACCEPT.t7u8v9.json
    ├── source_family_crystal/
    ├── archive_crystal/
    └── cam_database_crystal/
```

### Key Characteristics
- **No database server required.** Pure JSON files.
- **Content-addressed.** Every artifact name includes a 12-char hash prefix.
- **Hierarchical.** Source states and crystals are separated into `states/` and `crystals/`.
- **Kind-scoped.** Crystals are grouped by `kind` into subdirectories.
- **Immutable.** Once written, a crystal file is never modified in-place; a new build generates new hashes.
- **Human-readable.** Markdown index for quick inspection. JSON index for machine parsing.

---

## 4. Mapping to A-Family Paper Series (paper-00 through paper-100)

### 4.1 Slot → Paper Number Mapping
| B-Family Term | A-Family Term | Meaning |
|---|---|---|
| `slot` | `paper_id` | Identifies a single paper in the series. `slot_42` → `paper-42`. |
| `slot_1_80` | `paper-00` through `paper-100` | The full paper series (0–100). The original script's 1–80 ontology expands to the full 101-paper A-family series. |
| `slot_families` | `paper_lineages` | Derivation lineages (which papers a claim or record belongs to). |
| `slot_assignments` | `paper_assignments` | Direct mappings of records/packages to specific papers. |

### 4.2 Source File → A-Family Intake Manifest Mapping
| Original Filename | A-Family Role | Description |
|---|---|---|
| `MASTER_DOCS_ROUTING_DOCTRINE.json` | `LCR_ROUTING_DOCTRINE.json` | Master routing rules for the LCR kernel paper series. |
| `D_DRIVE_INVENTORY_PAPER_GAP_PASS.json` | `PAPER_GAP_PASS.json` | Gap analysis: which papers are missing foundational content. |
| `PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_INDEX.json` | `PAIRWISE_EVIDENCE_INDEX.json` | Index of pairwise evidence bundles linking papers to external sources. |
| `PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_PROTOCOL.json` | `PAIRWISE_EVIDENCE_PROTOCOL.json` | Protocol for creating and validating pairwise evidence packages. |
| `AGENT_DISCOVERY_SYNTHESIS_PASS.json` | `DISCOVERY_SYNTHESIS.json` | Agent-discovered targets and synthesis results for paper intake. |
| `EXTERNAL_PAIRING_CANDIDATE_QUEUE.json` | `EXTERNAL_PAIRING_QUEUE.json` | Queue of external sources awaiting pairing with paper slots. |
| `SLOT_1_80_GENERALIZED_ONTOLOGY.json` | `PAPER_00_100_GENERALIZED_ONTOLOGY.json` | Generalized ontology covering all 101 papers. |
| `EVIDENCE_INTAKE_SCORE_NOTEBOOK.json` | `EVIDENCE_SCORE_NOTEBOOK.json` | Scored evidence records for assembly decisions. |
| `PAPER_ASSEMBLY_AUDIT_PASS.json` | `ASSEMBLY_AUDIT_PASS.json` | Audit results for paper assembly quality. |
| `DISCOVERY_AGENT_ASSIGNMENT_MANIFEST.json` | `AGENT_ASSIGNMENT_MANIFEST.json` | Manifest of agent assignments to discovery tasks. |
| `ARCHIVE_INTAKE_PASS.json` | `ARCHIVE_INTAKE_PASS.json` | Bulk archive intake results (unchanged). |
| `ARCHIVE_EXTRACTION_MANIFEST.json` | `ARCHIVE_EXTRACTION_MANIFEST.json` | Archive extraction tracking (unchanged). |
| `CAM_DATABASE_INTAKE_PASS.json` | `CAM_DATABASE_INTAKE_PASS.json` | Legacy database intake results (CAM → paper series). |
| `CAM_DATABASE_PORT_QUEUE.json` | `CAM_DATABASE_PORT_QUEUE.json` | Queue of databases awaiting port to paper series. |

### 4.3 Crystal → A-Family Mapping
| Crystal Kind | A-Family Name | Role in paper-00..paper-100 |
|---|---|---|
| `package_crystal` | `evidence_bundle` | A pairwise evidence bundle linking a paper (e.g., paper-42) to an external source. |
| `slot_crystal` | `paper_crystal` | All evidence records assigned to a single paper (e.g., paper-42). |
| `decision_crystal` | `assembly_decision_bucket` | Aggregated records sharing an assembly decision (ACCEPT, HOLD, REVISE, REJECT). |
| `source_family_crystal` | `derivation_lineage_crystal` | A D-tag lineage: which derivation chain a source belongs to. |
| `archive_crystal` | `archive_crystal` | Bulk intake bundle containing content for multiple papers. |
| `cam_database_crystal` | `legacy_database_crystal` | Legacy database to be ported into the paper series CAM. |

### 4.4 D/I/X Tag Mapping (Inferred from Script Fields)
| Script Field / Role | Likely D/I/X Tag | Rationale |
|---|---|---|
| `internal_source` | **D** (Derivation) | Internal anchor is the source of a derived claim. |
| `external_publication` | **I** (Invariant) | External peer-reviewed reference provides invariant grounding. |
| `correlation` | **I** (Invariant) | Correlational evidence is observational/invariant. |
| `claim_lane` | **D** (Derivation) | The lane a claim travels through the derivation pipeline. |
| `obligations` | **X** (Extension) | Future work, extensions, or obligations not yet proven. |
| `paper_routes` | **D** (Derivation) | Routing of derivations through the paper series. |
| `validation_review` | **I** (Invariant) | Validation is a check against invariant truth. |
| `nist_review` | *(removed)* | B-family identifier; replaced with `peer_review` or `kernel_review`. |

---

## 5. A-Family Schema Rewrite

### 5.1 Rewritten Script Header (A-Family)
```python
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT_CANDIDATES = [
    Path(r"D:\Paper Ecology\publication_series\LCR_Kernel_Papers"),
    Path(r"D:\Paper Reworks\publication_series\LCR_Kernel_Papers"),
]
ROOT = next((path for path in ROOT_CANDIDATES if path.exists()), ROOT_CANDIDATES[0])
MEMORY_ROOT = ROOT / "PAPER_CRYSTAL_MEMORY_BANK"

SOURCE_FILES = [
    "LCR_ROUTING_DOCTRINE.json",
    "PAPER_GAP_PASS.json",
    "PAIRWISE_EVIDENCE_INDEX.json",
    "PAIRWISE_EVIDENCE_PROTOCOL.json",
    "DISCOVERY_SYNTHESIS.json",
    "EXTERNAL_PAIRING_QUEUE.json",
    "PAPER_00_100_GENERALIZED_ONTOLOGY.json",
    "EVIDENCE_SCORE_NOTEBOOK.json",
    "ASSEMBLY_AUDIT_PASS.json",
    "AGENT_ASSIGNMENT_MANIFEST.json",
    "ARCHIVE_INTAKE_PASS.json",
    "ARCHIVE_EXTRACTION_MANIFEST.json",
    "CAM_DATABASE_INTAKE_PASS.json",
    "CAM_DATABASE_PORT_QUEUE.json",
]
```

### 5.2 A-Family Addressing Primitives (Unchanged Internals)
```python
def load_json(path: Path, default: Any = None) -> Any: ...  # unchanged

def stable_json(value: Any) -> str: ...  # unchanged

def address(value: Any) -> str: ...  # unchanged — this IS the CAM hash

def slug(value: str) -> str: ...  # unchanged

def write_json(path: Path, value: Any) -> str: ...  # unchanged

def write_md(path: Path, lines: list[str]) -> str: ...  # unchanged
```
- **Note:** `address()` computes the CAM hash. In A-family terms, this is the **LCR Kernel Content-Addressed Memory (CAM) hash**. It remains SHA-256 of canonical JSON.

### 5.3 A-Family Source States
```python
def source_states() -> list[dict[str, Any]]:
    states = []
    for name in SOURCE_FILES:
        path = ROOT / name
        data = load_json(path)
        if data is None:
            continue
        state = {
            "kind": "source_state",
            "name": name,
            "path": str(path),
            "generated_utc": data.get("generated_utc") if isinstance(data, dict) else None,
            "cam_hash": address(data),           # <-- renamed: content_address -> cam_hash
            "summary": summarize_source(name, data),
            "payload": data,
        }
        states.append(state)
    return states
```

### 5.4 A-Family Summarizer
```python
def summarize_source(name: str, data: Any) -> str:
    if not isinstance(data, dict):
        return "non-dict json source"
    if "package_count" in data:
        return f"{data.get('package_count')} pairwise evidence bundles"
    if "record_count" in data:
        return f"{data.get('record_count')} scored evidence records"
    if "counts" in data:
        return f"counts {data.get('counts')}"
    if "candidate_count" in data:
        return f"{data.get('candidate_count')} external pairing candidates"
    if "local_target_count" in data:
        return f"{data.get('local_target_count')} local targets; {data.get('external_candidate_count')} external candidates"
    if "missing" in data:
        return f"missing {data.get('missing', {}).get('missing_count')} artifacts"
    return str(data.get("purpose") or data.get("schema") or "json state")
```

### 5.5 A-Family Evidence Bundle Crystal (formerly `package_crystal`)
```python
def evidence_bundle_crystals(pairwise: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for bundle in pairwise.get("packages", []):
        crystal = {
            "kind": "evidence_bundle",
            "granularity": "pairwise_bundle",
            "bundle_id": bundle.get("package_id"),
            "title": bundle.get("title"),
            "faces": {
                "internal_source": bundle.get("internal_anchor"),
                "external_publication": bundle.get("external_paper"),
                "correlation": bundle.get("correlation"),
                "claim_lane": bundle.get("claim_lane"),
                "crystal_faces": bundle.get("crystal_faces", []),
                "paper_routes": bundle.get("paper_routes", []),
                "obligations": bundle.get("obligations", []),
                "peer_review": bundle.get("adapted_nist_pair_review"),  # B-field stripped
                "validation_review": bundle.get("validation_pair_review"),
            },
        }
        crystal["cam_hash"] = address(crystal)
        crystals.append(crystal)
    return crystals
```

### 5.6 A-Family Paper Crystal (formerly `slot_crystal`) + Decision Buckets
```python
def paper_crystals(notebook: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_paper: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_decision: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in notebook.get("records", []):
        decision = (record.get("score_notebook") or {}).get("decision", "UNKNOWN")
        by_decision[decision].append(record)
        for paper_id in record.get("paper_assignments", []):   # slot -> paper_id
            by_paper[paper_id].append(record)

    paper_crystals = []
    for paper_id, records in sorted(by_paper.items()):
        crystal = {
            "kind": "paper_crystal",
            "granularity": "paper",
            "paper_id": paper_id,                               # slot -> paper_id
            "record_count": len(records),
            "decision_counts": count_decisions(records),
            "records": [record_summary(r) for r in records[:80]],
        }
        crystal["cam_hash"] = address(crystal)
        paper_crystals.append(crystal)

    decision_buckets = []
    for decision, records in sorted(by_decision.items()):
        bucket = {
            "kind": "assembly_decision_bucket",
            "granularity": "assembly_decision",
            "decision": decision,
            "record_count": len(records),
            "records": [record_summary(r) for r in records[:100]],
        }
        bucket["cam_hash"] = address(bucket)
        decision_buckets.append(bucket)
    return paper_crystals, decision_buckets
```

### 5.7 A-Family Derivation Lineage Crystal (formerly `source_family_crystal`)
```python
def derivation_lineage_crystals(gap: dict[str, Any], synthesis: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for item in (gap.get("missing") or {}).get("root_summary", [])[:50]:
        crystal = {
            "kind": "derivation_lineage_crystal",
            "granularity": "derivation_lineage",
            "lineage_tag": item.get("top_root"),                # source_family -> lineage_tag
            "missing_count": item.get("missing_count"),
            "highest_score": item.get("highest_score"),
            "sample_files": item.get("sample_files", []),
            "frame": "paper-gap inventory derivation-lineage view",  # D-drive -> paper-gap
        }
        crystal["cam_hash"] = address(crystal)
        crystals.append(crystal)
    for target in synthesis.get("local_targets", []):
        crystal = {
            "kind": "derivation_lineage_crystal",
            "granularity": "local_intake_target",
            "rank": target.get("rank"),
            "artifact": target.get("artifact"),
            "why_it_matters": target.get("why_it_matters"),
            "suggested_papers": target.get("suggested_slots", []),  # suggested_slots -> suggested_papers
            "frame": "agent-discovered first-intake target",
        }
        crystal["cam_hash"] = address(crystal)
        crystals.append(crystal)
    return crystals
```

### 5.8 A-Family Archive Crystal (Unchanged Semantics, Renamed Fields)
```python
def archive_crystals(archive_pass: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for archive in archive_pass.get("archives", [])[:200]:
        crystal = {
            "kind": "archive_crystal",
            "granularity": "archive",
            "archive_id": archive.get("archive_id"),
            "path": archive.get("path"),
            "name": archive.get("name"),
            "archive_kind": archive.get("kind"),
            "entry_count_indexed": archive.get("entry_count_indexed"),
            "high_signal_entry_count": archive.get("high_signal_entry_count"),
            "paper_lineages": archive.get("slot_families", []),      # slot_families -> paper_lineages
            "paper_assignments": archive.get("slot_assignments", []), # slot_assignments -> paper_assignments
            "frame": "archive-intake content and source-card discovery view",
        }
        crystal["cam_hash"] = address(crystal)
        crystals.append(crystal)
    return crystals
```

### 5.9 A-Family Legacy Database Crystal (formerly `cam_database_crystal`)
```python
def legacy_database_crystals(database_pass: dict[str, Any]) -> list[dict[str, Any]]:
    crystals = []
    for db in database_pass.get("databases", [])[:160]:
        signal_tables = [
            {
                "table": table.get("table"),
                "row_count": table.get("row_count"),
                "signal_columns": table.get("signal_columns", []),
            }
            for table in db.get("tables", [])
            if table.get("table_signal")
        ]
        crystal = {
            "kind": "legacy_database_crystal",
            "granularity": "database",
            "db_id": db.get("db_id"),
            "path": db.get("path"),
            "name": db.get("name"),
            "status": db.get("status"),
            "signal_score": db.get("signal_score"),
            "port_recommendation": db.get("port_recommendation"),
            "table_count": db.get("table_count"),
            "signal_tables": signal_tables[:40],
            "paper_lineages": db.get("slot_families", []),
            "paper_assignments": db.get("slot_assignments", []),
            "frame": "legacy CAM/database port-to-paper-series view",
        }
        crystal["cam_hash"] = address(crystal)
        crystals.append(crystal)
    return crystals
```

### 5.10 A-Family Record Summary
```python
def record_summary(record: dict[str, Any]) -> dict[str, Any]:
    score = record.get("score_notebook") or {}
    return {
        "record_id": record.get("record_id"),
        "record_type": record.get("record_type"),
        "title": record.get("title"),
        "decision": score.get("decision"),
        "assembly_score": score.get("assembly_score"),
        "paper_lineages": record.get("slot_families", []),
        "paper_assignments": record.get("slot_assignments", []),
        "external_paper_title": record.get("external_paper_title"),
        "source_identity": record.get("source_identity"),
    }
```

### 5.11 A-Family Orchestrator: `build_bank()`
```python
def build_bank() -> dict[str, Any]:
    sources = source_states()
    source_by_name = {state["name"]: state["payload"] for state in sources}
    pairwise = source_by_name.get("PAIRWISE_EVIDENCE_INDEX.json", {}) or {}
    notebook = source_by_name.get("EVIDENCE_SCORE_NOTEBOOK.json", {}) or {}
    gap = source_by_name.get("PAPER_GAP_PASS.json", {}) or {}
    synthesis = source_by_name.get("DISCOVERY_SYNTHESIS.json", {}) or {}
    archive_pass = source_by_name.get("ARCHIVE_INTAKE_PASS.json", {}) or {}
    database_pass = source_by_name.get("CAM_DATABASE_INTAKE_PASS.json", {}) or {}

    bundles = evidence_bundle_crystals(pairwise)
    paper_crys, decision_buckets = paper_crystals(notebook)
    lineages = derivation_lineage_crystals(gap, synthesis)
    archives = archive_crystals(archive_pass)
    legacy_dbs = legacy_database_crystals(database_pass)
    all_crystals = bundles + paper_crys + decision_buckets + lineages + archives + legacy_dbs

    generated = datetime.now(timezone.utc).isoformat()
    index = {
        "schema": "lcr_kernel.paper_crystal_memory_bank.v1",   # flcr -> lcr_kernel
        "generated_utc": generated,
        "root": str(ROOT),
        "memory_root": str(MEMORY_ROOT),
        "source_states": [
            {k: v for k, v in state.items() if k != "payload"}
            for state in sources
        ],
        "crystal_counts": {
            "evidence_bundle_crystals": len(bundles),
            "paper_crystals": len(paper_crys),
            "assembly_decision_buckets": len(decision_buckets),
            "derivation_lineage_crystals": len(lineages),
            "archive_crystals": len(archives),
            "legacy_database_crystals": len(legacy_dbs),
            "total": len(all_crystals),
        },
        "crystals": [
            {
                "kind": crystal.get("kind"),
                "granularity": crystal.get("granularity"),
                "cam_hash": crystal.get("cam_hash"),
                "path": crystal_path(crystal),
                "label": crystal_label(crystal),
            }
            for crystal in all_crystals
        ],
    }

    write_json(MEMORY_ROOT / "PAPER_MEMORY_INDEX.json", index)
    write_md(
        MEMORY_ROOT / "PAPER_MEMORY_INDEX.md",
        [
            "# Paper Crystal Memory Bank (A-Family)",
            "",
            f"Generated: {generated}",
            "",
            f"Root: `{ROOT}`",
            "",
            "## Counts",
            "",
            f"- Source states: {len(sources)}",
            f"- Evidence bundle crystals: {len(bundles)}",
            f"- Paper crystals: {len(paper_crys)}",
            f"- Assembly decision buckets: {len(decision_buckets)}",
            f"- Derivation lineage crystals: {len(lineages)}",
            f"- Archive crystals: {len(archives)}",
            f"- Legacy database crystals: {len(legacy_dbs)}",
            f"- Total crystals: {len(all_crystals)}",
            "",
            "## Rule",
            "",
            "Every pipeline stage becomes a CAM-addressed state. Crystals are saved at multiple granularities so future work can call the whole state, an evidence bundle, a paper (paper-00..paper-100), a decision bucket, or a derivation lineage.",
            "",
        ],
    )

    for state in sources:
        write_json(
            MEMORY_ROOT / "states" / f"{slug(state['name'])}.{state['cam_hash'][:12]}.json",
            {k: v for k, v in state.items() if k != "payload"}
        )
    for crystal in all_crystals:
        write_json(Path(crystal_path(crystal)), crystal)
    return index
```

### 5.12 A-Family Label & Path Helpers
```python
def crystal_label(crystal: dict[str, Any]) -> str:
    return (
        crystal.get("bundle_id")
        or crystal.get("paper_id")
        or crystal.get("decision")
        or crystal.get("lineage_tag")
        or crystal.get("artifact")
        or crystal.get("kind")
        or "crystal"
    )


def crystal_path(crystal: dict[str, Any]) -> str:
    kind = crystal.get("kind", "crystal")
    label = slug(str(crystal_label(crystal)))
    addr = crystal.get("cam_hash", address(crystal))[:12]
    return str(MEMORY_ROOT / "crystals" / kind / f"{label}.{addr}.json")
```

### 5.13 A-Family Entry Point
```python
def main() -> None:
    MEMORY_ROOT.mkdir(parents=True, exist_ok=True)
    index = build_bank()
    print(
        json.dumps(
            {
                "memory_index": str(MEMORY_ROOT / "PAPER_MEMORY_INDEX.md"),
                "memory_index_json": str(MEMORY_ROOT / "PAPER_MEMORY_INDEX.json"),
                "crystal_counts": index["crystal_counts"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
```

### 5.14 A-Family Output Directory Layout
```
PAPER_CRYSTAL_MEMORY_BANK/
├── PAPER_MEMORY_INDEX.json
├── PAPER_MEMORY_INDEX.md
├── states/
│   ├── LCR_ROUTING_DOCTRINE.a1b2c3d4.json
│   ├── PAPER_GAP_PASS.e5f6g7h8.json
│   └── ... (one per source file)
└── crystals/
    ├── evidence_bundle/
    │   └── bundle_042_001.x1y2z3.json
    ├── paper_crystal/
    │   └── paper_42.w4q5r6.json
    ├── assembly_decision_bucket/
    │   └── ACCEPT.t7u8v9.json
    ├── derivation_lineage_crystal/
    ├── archive_crystal/
    └── legacy_database_crystal/
```

---

## 6. Architecture Summary

| Aspect | B-Family Script | A-Family Rewrite |
|---|---|---|
| **Addressing** | `content_address` (SHA-256) | `cam_hash` (SHA-256) — same primitive, A-family name |
| **Root** | `CAM_CRYSTAL_MEMORY_BANK` | `PAPER_CRYSTAL_MEMORY_BANK` |
| **Slot** | `slot` / `slot_1_80` | `paper_id` / `paper-00`..`paper-100` |
| **Schema** | `flcr.cam_crystal_memory_bank.v1` | `lcr_kernel.paper_crystal_memory_bank.v1` |
| **Package** | `package_crystal` | `evidence_bundle` |
| **NIST Review** | `nist_review` | `peer_review` (B-identity stripped) |
| **Source Family** | `source_family_crystal` | `derivation_lineage_crystal` (D-tag lineage) |
| **Database** | `cam_database_crystal` | `legacy_database_crystal` (port-to-paper-series) |
| **Index** | `CAM_MEMORY_INDEX` | `PAPER_MEMORY_INDEX` |
| **Ontology** | `SLOT_1_80_GENERALIZED_ONTOLOGY` | `PAPER_00_100_GENERALIZED_ONTOLOGY` |

### Core Design Principles (Preserved in Both)
1. **Content Addressing:** Every artifact is named by its own hash. This makes the store immutable, cacheable, and deduplicated by construction.
2. **Fault Tolerance:** Missing source files are silently skipped. Empty buckets produce empty crystal lists. The build never crashes on partial data.
3. **Multiple Granularities:** The same underlying records are indexed by paper (slot), by decision, by lineage, and by bundle. This lets future agents query at the granularity that matches their task.
4. **No Central Server:** Pure JSON filesystem store. Any tool that can read JSON can consume the memory bank.
5. **Human + Machine:** Every build produces both a JSON index (for agents) and a Markdown index (for humans).

---

*End of analysis. All B-family identifiers (FLCR, NIST, slot_1_80) have been mapped to A-family conventions (paper-00..paper-100, LCR kernel, D/I/X, CAM hashes).*
