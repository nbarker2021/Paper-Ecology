# PaperLib — Canon Papers & Disposition Directive

**Last organized: 2026-07-03**

---

## ⚠️ ABSOLUTE RULE — ZERO EXCEPTIONS

**The ONLY Canon papers are `paper-00__` through `paper-100__` (101 files).**  
**`README.md` is the only other file permitted at the top level.**  
**Everything else in this folder is raw material. Raw material gets harvested, then deleted.**

The active-rework papers (`00_` through `32_`, `04b_`, `NP-12`, `NP-14`, `NP-15`) are **NOT Canon.** They are legacy drafts whose sole purpose is to be stripped for content and integrated into the unified `paper-XX__` series.

---

## What Is Canon (Immutable)

| File | Status |
|------|--------|
| `paper-00__unified_transport_contract_and_foreword.md` | **Canon** |
| `paper-01__unified_lcr_kernel_and_chart.md` | **Canon** |
| ... | ... |
| `paper-99__unified_Applied_Forge_Validation.md` | **Canon** |
| `paper-100__unified_Capstone_100_Paper_Series_and_Complete_Framework_Synthesis.md` | **Canon** |
| `README.md` | **Folder governance only** |

**Total Canon: 101 papers + 1 README.**

---

## Disposition Hierarchy (Non-Canon → Canon Integration)

When harvesting from any non-Canon source (active-rework papers, external literature, scripts, evidence, etc.), content flows through this decision tree:

```
Does this content fit the structure of an existing paper-XX__?
    ├── YES → Integrate directly into that paper-XX__
    │         (overwrite/append; use the paper-XX__ form, not the source form)
    │
    └── NO → Can it be supplemental to an existing paper-XX__?
              ├── YES → Create supplement section within that paper-XX__
              │
              └── NO → Does it deserve a new sequential paper (paper-101__, etc.)?
                        ├── YES → Create new paper-NN__
                        │
                        └── NO → Create (RO) — Reordering Obligation
                                  (forces reordering/restructuring of papers)
```

### (RO) — Reordering Obligation
An **(RO)** is created when content does not fit any existing paper, cannot be supplemental, and does not warrant a new sequential paper. It is a **blocking item** that forces restructuring — either:
- Reordering existing papers to create space for the new content
- Merging/splitting existing papers
- Rewriting paper boundaries to accommodate the gap

(RO)s are tracked in `04_SUPPORTING_DATA_AND_EVIDENCE/` until resolved, then deleted.

---

## Folder Inventory & Disposition Rules

### `00_EXTERNAL_LITERATURE_MAPPING/` — External Research Catalog (27 files)
- **Contents:** 23 rounds of external literature mapping (195 papers catalogued), master index, synthesis, supplements A–V.
- **Purpose:** Mine for citations, calibration anchors, and gap-closure data.
- **Action:** Extract every citation and integration paragraph into the appropriate `paper-XX__`. Then **DELETE this folder.**

### `01_FINAL_PAPERS_FLCR_UNIFIED/` — Compiled Bulk Archives (342 files)
- **Contents:** `ALL_FORMAL_PAPERS.md`, `ALL_COMPANION_PAPERS.md`, `ALL_WORKBOOKS.md`, CAM database, evidence notebooks, D-drive gap audit, archive manifests.
- **Purpose:** Bulk-compiled versions of material. Verify if any compiled content is newer/cleaner than current Canon.
- **Action:** Compare against top-level `paper-XX__`. Port any superior formulations. Then **DELETE this folder.**

### `02_ARCHIVE_BACKUPS_AND_ZIPS/` — Version History (13 files)
- **Contents:** 12 ZIP archives of `Formalizing_LCR`, `_backup_before_archive_supplement_20260626_212645/`.
- **Purpose:** Cold backup. No canonical value.
- **Action:** Keep the single most recent ZIP as emergency recovery. **DELETE everything else.**

### `03_SCRIPTS_AND_TOOLS/` — Build Scripts, DBs, Query Tools (22 files)
- **Contents:** `scripts/`, `models/`, `tools/`, `.py` files, `.db` files.
- **Purpose:** Operational tooling for paper generation and cross-referencing.
- **Action:** Evaluate each script. If it generates/validates Canon content, document its function in the relevant `paper-XX__` and move the script to a dedicated tooling repo (NOT in PaperLib). **DELETE this folder.**

### `04_SUPPORTING_DATA_AND_EVIDENCE/` — Audits, Harvests, Cross-References (47 files)
- **Contents:** `AGENT_CRYSTAL_WORK_HARVEST`, `CROSS_REFERENCES.json`, `CONSISTENCY_AUDIT.md`, `CAM_CLAIM_100_SCORE_AUDIT`, `ORBITAL_DATA_CROSS_POPULATION_AUDIT`, `PAPER_REWORKS_CRYSTAL_PROJECTION`, `U24_FRAMEWORK_DECONSTRUCTION`, `CQE_vs_U24_CAPABILITY_COMPARISON`, `NSIT_*` files, `OBLIGATION_AUDIT.md`, verification reports, receipts, and 40+ JSON/CSV/Markdown support files.
- **Purpose:** Evidence and analysis produced during development.
- **Action:** Strip every verified claim, citation, and data point into the appropriate `paper-XX__`. Track any unresolved (RO)s here temporarily. Then **DELETE this folder.**

### `05_WORK_IN_PROGRESS/` — Drafts, Queues, Supplements, Series (7 items)
- **Contents:** `UFT_paper_series/`, `publication_series/`, `queues/`, `supplements/`, `virtuous/`, `lattice_forge_unification/`.
- **Purpose:** Work-in-progress materials, draft supplements, publication pipelines.
- **Action:** Evaluate each item. Port ready content to `paper-XX__`. Delete stale/superseded content. **DELETE this folder once harvested.**

### `06_ACTIVE_REWORK_HARVEST/` — Legacy Active-Rework Papers (38 files)
- **Contents:** `00_Established_Grounding_and_Axiom_Contract.md` through `32_The_Supervisor_Cursor.md`, plus `04b_Fano_Simplex_Lift.md`, `NP-12_Electron_Hole_Exciton_Accounting_For_Open_Math.md`, `NP-14_Accumulator_Closure_of_Unresolved_Receipts.md`, `NP-15_IRL_Data_Addressing_for_Open_Predictions.md`.
- **Purpose:** These are **legacy drafts only.** Their names and numbering are irrelevant. They exist solely to be harvested.
- **Action:** For each active-rework paper, read its content and determine where it belongs in the `paper-00__` through `paper-100__` Canon. Integrate the content using the Disposition Hierarchy above. **Once fully harvested, DELETE this folder.** The `paper-XX__` papers are the only surviving form.

---

## Disposition Workflow (For Every Non-Canon Source)

1. **Read** the source file/folder.
2. **Classify** each content item using the hierarchy: `paper-XX__` direct integration → supplement → new sequential paper → (RO).
3. **Write** the integrated content into the target `paper-XX__` in the **unified form**, not the source form.
4. **Mark** the source item as harvested.
5. **Delete** the source file/folder once 100% harvested.
6. **Repeat** until only `paper-00__` through `paper-100__` + `README.md` remain.

---

## Golden Rule

> **If it is not a `paper-XX__` file, it is raw material. Raw material gets processed into `paper-XX__`, then discarded. No exceptions.**

Do not maintain parallel sources of truth. Do not let folder contents drift out of sync with Canon. The `paper-00__` through `paper-100__` files are the only permanent artifacts.

---

*Organized by: CQE/CMPLX curation agent*  
*Date: 2026-07-03*  
*Next action: Begin controlled-batch harvest of `06_ACTIVE_REWORK_HARVEST/` into `paper-XX__` Canon*
