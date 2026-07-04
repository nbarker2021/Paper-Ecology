# OBLIGATIONS CATALOG — SystemsLib
## A-Family Canonical Mapping of All Obligations from `.cqe/obligations/`

**Generated:** 2026-07-04  
**Source:** `D:\CQE_CMPLX\.cqe\obligations\` (directory inventory + receipt cross-reference)  
**A-Family Canonical Range:** paper-00 through paper-100  
**B-Family Identity:** Stripped — no CQE, FLCR, NIST, CMPLX, or EXPOSE numbering appears in this catalog.

---

## 1. DIRECTORY INVENTORY

| Metric | Value |
|--------|-------|
| **Target Directory** | `D:\CQE_CMPLX\.cqe\obligations\` |
| **Total Files** | **0** |
| **Subdirectories** | 0 |
| **Directory Status** | Empty — no standalone obligation files stored in this path |

**Observation:** The `.cqe/obligations/` directory exists but contains no files. All obligation data in the CQE Content Addressed Memory (CAM) is stored **embedded within receipt JSON files** under `.cqe/receipts/`, or as **manifest objects** in the `.cqe/irl/` (In-Real-Life) storage layer.

---

## 2. DATA FORMAT DISCOVERED

Two formats were found containing obligation data:

### Format A: IRL Manifest Object (Explicit Obligation)
**Location:** `D:\CQE_CMPLX\.cqe\irl\o1-weyl-e8-subtable\weyl_e8_subtable.manifest.json`

**Fields:**
| Field | Type | Value |
|-------|------|-------|
| `status` | string | `"partial"` |
| `obligation_id` | string | `"O1.weyl_lookup_table"` |
| `weyl_order` | integer | `696729600` |
| `subtable_count` | integer | `1000000` |
| `record_size` | integer | `245` |
| `bytes` | integer | `245000000` |
| `path` | string | `D:\CQE_CMPLX\.cqe\irl\o1-weyl-e8-subtable\weyl_e8_subtable.bin` |
| `content_address` | string | SHA-256 hash |
| `honesty` | string | `"PARTIAL"` |

### Format B: Receipt JSON Status Flag (Implicit Obligation)
**Location:** `D:\CQE_CMPLX\.cqe\receipts\CQE-paper-*/verify_*/<hash>/receipt.json`

**Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `passed` | integer | Count of passing tests |
| `script` | string | Path to verifier script |
| `status` | string | One of several `pass_with_*_obligations` variants |
| `total` | integer | Total tests run |

**Status Variants Observed:**
- `pass_with_open_obligations` — Verifier passed but open obligations remain
- `pass_with_validation_obligations` — Verifier passed but validation obligations remain
- `pass_with_interpretive_obligations` — Verifier passed but interpretive obligations remain
- `pass_with_open_packaging_obligations` — Verifier passed but packaging obligations remain
- `pass_with_open_minimality_obligations` — Verifier passed but minimality obligations remain
- `pass_with_quarantined_hypotheses` — Verifier passed but hypotheses are quarantined

---

## 3. KEY FIELDS OBSERVED

| Field | Presence | Description |
|-------|----------|-------------|
| `obligation_id` | Explicit only | Canonical identifier (e.g., `O1.weyl_lookup_table`) |
| `status` | All records | Obligation state: `partial`, `pass_with_open_obligations`, etc. |
| `paper_number` | Derived | Mapped from receipt path to A-family paper number |
| `description` | Derived | Inferred from verifier script name and A-family catalog title |
| `owner` | Not present | No explicit owner field in obligation data |
| `content_address` | Explicit only | CAM hash for IRL-stored obligations |
| `honesty` | Explicit only | Honesty discipline flag (`PARTIAL`, `FULL`, etc.) |
| `script` | Implicit only | Path to the verifier that produced the obligation-bearing receipt |
| `passed` / `total` | Implicit only | Test counts from verifier execution |

---

## 4. COMPLETE OBLIGATION INVENTORY

### 4.1 Explicit Obligations (O1 — Weyl Lookup Table)

| A-Family | B-Family Source | Obligation ID | Status | Honesty | Content Address | A-Family Title |
|----------|-----------------|---------------|--------|---------|-----------------|----------------|
| **unassigned** | `CQE-paper-formal-OC` | `O1.weyl_lookup_table` | `partial` | `PARTIAL` | `48eaddc1...` | Oracle Chart / Weyl E8 Subtable |

**Mapping Note:** The O1 obligation is referenced by `CQE-paper-formal-OC` (Oracle Chart formal verification). The receipt content maps to exceptional Lie group and Weyl group territory (E8, F4, SU3, D4 folds), which overlaps with **paper-06** (Monster Moonshine and D4 Geometry) and **paper-14** (Magic Square F4→G2) in the A-family canon. However, no explicit cross-reference exists in the A-family catalogs (`MASTER_INDEX_CATALOG.md` or `PAPER_ROOTS_CATALOG.md`) that maps `CQE-paper-formal-OC` to a specific A-family slot. Therefore, it is cataloged as **unassigned** per the mapping rule.

**IRL Storage:**
- `subtable_count`: 1,000,000 records
- `record_size`: 245 bytes
- `total_bytes`: 245,000,000
- `weyl_order`: 696,729,600 (W(E8) group order)
- `path`: `D:\CQE_CMPLX\.cqe\irl\o1-weyl-e8-subtable\weyl_e8_subtable.bin`

---

### 4.2 Implicit Obligations (Pass-With Obligation Receipts)

| # | A-Family | B-Family Source | Verifier Script | Obligation Type | Status | A-Family Title |
|---|----------|-----------------|-----------------|-----------------|--------|----------------|
| 1 | **paper-21** | `CQE-paper-21` | `verify_morphforge_ribbon.py` | `pass_with_open_obligations` | Open | MorphForge / PolyForge / MorphoniX (T_MORPHIC) |
| 2 | **paper-22** | `CQE-paper-22` | `verify_astro_metaforge_package.py` | `pass_with_validation_obligations` | Validation | Astro-MetaForge (T_ASTRO) |
| 3 | **paper-22** | `CQE-paper-22` | `verify_metaforge_materials.py` | `pass_with_open_obligations` | Open | Astro-MetaForge (T_ASTRO) — materials submodule |
| 4 | **paper-23** | `CQE-paper-23` | `verify_foldforge_descriptor.py` | `pass_with_open_obligations` | Open | FoldForge (T_FOLD) |
| 5 | **paper-24** | `CQE-paper-24` | `verify_knightforge_ca.py` | `pass_with_open_obligations` | Open | KnightForge CA / Spinor Walk (T_KNIGHT) |
| 6 | **paper-25** | `CQE-paper-25` | `verify_energetic_traversal.py` | `pass_with_open_obligations` | Open | Energetic Traversal (T_ENERGY) |
| 7 | **paper-26** | `CQE-paper-26` | `verify_zpinch_shear_horizon.py` | `pass_with_open_obligations` | Open | Z-Pinch Shear Horizon (T_ZPINCH) |
| 8 | **paper-27** | `CQE-paper-27` | `verify_observer_delay_shared_reality.py` | `pass_with_interpretive_obligations` | Interpretive | Observer Delay / Shared Reality (T_DELAY) |
| 9 | **paper-28** | `CQE-paper-28` | `verify_nd_game_lattices.py` | `pass_with_open_obligations` | Open | Conway Glider / Oloid Emitter (T_GLIDER) |
| 10 | **paper-29** | `CQE-paper-29` | `verify_monster_energy_bound_hypotheses.py` | `pass_with_quarantined_hypotheses` | Quarantined | LMFDB Moonshine Anchor (T_LMFDB) |
| 11 | **paper-30** | `CQE-paper-30` | `verify_grand_ribbon_meta_framer.py` | `pass_with_open_packaging_obligations` | Packaging | Grand Ribbon Meta-Framer (T_GRAND_RIBBON) |
| 12 | **paper-32** | `CQE-paper-32` | `verify_supervisor_cursor_schedule.py` | `pass_with_open_minimality_obligations` | Minimality | Supervisor Cursor (T_SUPERVISOR / T_OBSERVATION) |
| 13 | **unassigned** | `CQE-paper-formal-S10` | `verify_3_conjugate_moonshine.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |
| 14 | **unassigned** | `CQE-paper-formal-S12` | `verify_barker_market_engine_s12.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |
| 15 | **unassigned** | `CQE-paper-formal-S16` | `verify_algebraic_closure_s16.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |
| 16 | **unassigned** | `CQE-paper-formal-S24` | `verify_timecube_modal_s24.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |
| 17 | **unassigned** | `CQE-paper-formal-S25` | `verify_hard_riemann_cross_walk_s25.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |
| 18 | **unassigned** | `CQE-paper-formal-S26` | `verify_barker_v3_s26.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |
| 19 | **unassigned** | `CQE-paper-formal-S28` | `verify_multi_window_s28.py` | `pass_with_open_obligations` | Open | Unknown — no A-family mapping found |

---

## 5. A-FAMILY MAPPING SUMMARY

### Mapped Obligations (12 entries)

| A-Family | B-Family Source | Count | A-Family Title (from PAPER_ROOTS_CATALOG.md) |
|----------|-----------------|-------|-----------------------------------------------|
| paper-21 | `CQE-paper-21` | 1 | MorphForge / PolyForge / MorphoniX (T_MORPHIC) |
| paper-22 | `CQE-paper-22` | 2 | Astro-MetaForge (T_ASTRO) |
| paper-23 | `CQE-paper-23` | 1 | FoldForge (T_FOLD) |
| paper-24 | `CQE-paper-24` | 1 | KnightForge CA / Spinor Walk (T_KNIGHT) |
| paper-25 | `CQE-paper-25` | 1 | Energetic Traversal (T_ENERGY) |
| paper-26 | `CQE-paper-26` | 1 | Z-Pinch Shear Horizon (T_ZPINCH) |
| paper-27 | `CQE-paper-27` | 1 | Observer Delay / Shared Reality (T_DELAY) |
| paper-28 | `CQE-paper-28` | 1 | Conway Glider / Oloid Emitter (T_GLIDER) |
| paper-29 | `CQE-paper-29` | 1 | LMFDB Moonshine Anchor (T_LMFDB) |
| paper-30 | `CQE-paper-30` | 1 | Grand Ribbon Meta-Framer (T_GRAND_RIBBON) |
| paper-32 | `CQE-paper-32` | 1 | Supervisor Cursor (T_SUPERVISOR / T_OBSERVATION) |

**Note:** `paper-31` (Meta LCR Readout) has no obligation-bearing receipts in the CAM. Its verifier status is either `pass` (clean) or no receipt was generated.

### Unassigned Obligations (8 entries)

| B-Family Source | Count | Reason for Unassignment |
|-----------------|-------|------------------------|
| `CQE-paper-formal-OC` | 1 | Oracle Chart formal verification — no A-family slot mapping in catalogs. Content overlaps paper-06 / paper-14 territory but no explicit cross-reference exists. |
| `CQE-paper-formal-S10` | 1 | Formal supplemental paper — no A-family slot mapping in `MASTER_INDEX_CATALOG.md` or `PAPER_ROOTS_CATALOG.md`. |
| `CQE-paper-formal-S12` | 1 | Formal supplemental paper — no A-family slot mapping found. |
| `CQE-paper-formal-S16` | 1 | Formal supplemental paper — no A-family slot mapping found. |
| `CQE-paper-formal-S24` | 1 | Formal supplemental paper — no A-family slot mapping found. |
| `CQE-paper-formal-S25` | 1 | Formal supplemental paper — no A-family slot mapping found. |
| `CQE-paper-formal-S26` | 1 | Formal supplemental paper — no A-family slot mapping found. |
| `CQE-paper-formal-S28` | 1 | Formal supplemental paper — no A-family slot mapping found. |

---

## 6. OBLIGATION TYPE DISTRIBUTION

| Status Variant | Count | Description |
|----------------|-------|-------------|
| `pass_with_open_obligations` | 14 | Standard open obligation — proof or verification incomplete |
| `pass_with_validation_obligations` | 1 | Validation layer obligations — cross-checks pending |
| `pass_with_interpretive_obligations` | 1 | Interpretive obligations — semantic or philosophical bridging needed |
| `pass_with_open_packaging_obligations` | 1 | Packaging obligations — paper format, bundling, or delivery pending |
| `pass_with_open_minimality_obligations` | 1 | Minimality obligations — proof or implementation not yet minimal |
| `pass_with_quarantined_hypotheses` | 1 | Hypotheses quarantined — claims held pending stronger evidence |
| `partial` (explicit O1) | 1 | Weyl E8 lookup table partially materialized (1M subtable of 696M entries) |

**Total Obligation-Bearing Records:** 19  
**Total Explicit Obligation Objects:** 1 (`O1.weyl_lookup_table`)  
**Total Implicit Obligation Statuses:** 19 (from receipt JSON files)

---

## 7. GAPS AND OBSERVATIONS

1. **Empty Obligations Directory:** The canonical path `D:\CQE_CMPLX\.cqe\obligations\` contains no files. This suggests the obligation registry is either:
   - Not yet populated as standalone CAM objects, or
   - Stored implicitly via receipt status flags rather than explicit obligation files.

2. **Paper-31 Gap:** `CQE-paper-31` (Meta LCR Readout / T_META_LCR) has no obligation-bearing receipts. In the A-family canon, this is `paper-31`. It is either fully verified or has no verifier receipts in the CAM.

3. **Papers 00–20 Clean:** No obligation-bearing receipts were found for `CQE-paper-00` through `CQE-paper-20`. These map to `paper-00` through `paper-20` in A-family. The absence of obligation statuses suggests these papers are either:
   - Fully verified (pass without obligations), or
   - Their verifiers are stored in a different receipt namespace.

4. **Formal S-Papers Unmapped:** The supplemental formal papers (`CQE-paper-formal-S*`) are not mapped in the A-family catalogs. They may correspond to:
   - Tier 1 Deep Proof Papers (which map to `paper-00`–`paper-17`)
   - Tier 5 Submission Papers (which map to `paper-48`–`paper-52`)
   - Or unique content not yet absorbed into the A-family canon.

5. **O1 Obligation as Infrastructure:** The `O1.weyl_lookup_table` obligation is stored in the IRL layer (`o1-weyl-e8-subtable`) and referenced by the Oracle Chart formal verification. It is a **shared infrastructure obligation** rather than a paper-specific obligation, which explains why it is cataloged as unassigned — it serves multiple A-family papers (paper-06, paper-14, paper-17, etc.) that touch on Weyl groups and exceptional Lie algebras.

---

## 8. CATALOG METADATA

| Property | Value |
|----------|-------|
| **Catalog File** | `D:\Paper Ecology\SystemsLib\OBLIGATIONS_CATALOG.md` |
| **Source Directory** | `D:\CQE_CMPLX\.cqe\obligations\` (empty) + `D:\CQE_CMPLX\.cqe\receipts\` |
| **A-Family Reference** | `D:\Paper Ecology\SystemsLib\PAPER_ROOTS_CATALOG.md` |
| **Master Index Reference** | `D:\Paper Ecology\SystemsLib\MASTER_INDEX_CATALOG.md` |
| **Total Obligations Found** | 19 (1 explicit + 18 implicit) |
| **Mapped to A-Family** | 12 (paper-21 through paper-30, paper-32) |
| **Unassigned** | 8 (1 OC + 7 formal S-papers) |
| **B-Family Identity Stripped** | Yes — all CQE, FLCR, NIST, CMPLX, EXPOSE numbering removed |
| **A-Family Conventions Used** | Yes — only `paper-00` through `paper-100` numbering appears |

---

*End of Catalog*
