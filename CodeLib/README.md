# CodeLib — Paper-Attached Code Artifacts & Disposition Directive

**Last organized: 2026-07-03**

---

## ⚠️ ABSOLUTE RULE — ZERO EXCEPTIONS

**The ONLY Canon artifacts are `paper-00__` through `paper-100__` (101 files).**
**`README.md` is the only other file permitted at the top level.**
**Everything else in this folder is raw material. Raw material gets harvested, then deleted.**

The active-rework and supporting directories (`00_` through `06_`) are **NOT Canon.** They are staging areas whose sole purpose is to be stripped for content and integrated into the unified `paper-XX__` series.

---

## What Is Canon (Immutable)

| File | Status | Purpose |
|------|--------|---------|
| `paper-00__unified_transport_contract_and_foreword.*` | **Canon** | Grounding / Axiom Contract — foundational code |
| `paper-01__unified_lcr_kernel_and_chart.*` | **Canon** | LCR Carrier — local state machine code |
| ... | ... | ... |
| `paper-99__unified_Applied_Forge_Validation.*` | **Canon** | Applied Forge validation suite |
| `paper-100__unified_Capstone_100_Paper_Series_and_Complete_Framework_Synthesis.*` | **Canon** | Complete framework synthesis |
| `README.md` | **Folder governance only** | This file |

**Total Canon: 101 papers + 1 README.**

---

## Disposition Hierarchy (Non-Canon → Canon Integration)

When harvesting from any non-Canon source (active-rework code, external libraries, scripts, evidence, etc.), content flows through this decision tree:

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

### `00_EXTERNAL_LITERATURE_MAPPING/` — External research catalog and citations
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

### `01_FINAL_CODE_PACKAGES_FLCR_UNIFIED/` — Compiled, verified code packages per paper
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

### `02_ARCHIVE_BACKUPS_AND_ZIPS/` — Version history and cold backups
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

### `03_SCRIPTS_AND_TOOLS/` — Build scripts, generators, and validation tools
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

### `04_SUPPORTING_DATA_AND_EVIDENCE/` — Test data, benchmarks, receipts, and proofs
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

### `05_WORK_IN_PROGRESS/` — Draft implementations and queued work
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

### `06_ACTIVE_REWORK_HARVEST/` — Legacy code being harvested into canon
- **Contents:** Raw material, staging, and compiled artifacts for this library type.
- **Purpose:** Operational material for paper generation and cross-referencing.
- **Action:** Evaluate each item. If it generates/validates Canon content, integrate into the relevant `paper-XX__` and move the item to a dedicated tooling repo (NOT in CodeLib). **DELETE this folder once harvested.**

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
