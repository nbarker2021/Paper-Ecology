# CMPLX-Standards Protocol

**Version:** 1.0.0  
**Date:** 2026-07-03  
**Status:** Operational  
**Primary Gate:** `CMPLX-Standards/run_standards_suite.py`  

---

## Purpose

CMPLX-Standards is the NIST-adjacent measurement and grading surface for all CMPLX work. It replaces the older `run_flcr_nist_review_suite.py` and `NSIT_VALIDITY_REBUILD_PROTOCOL.md` while preserving their provenance.

**Core principle:** Measurement, not promotion. The tool grades model fit; it does not silently promote claims because shape passes.

---

## Architecture

```
run_standards_suite.py (orchestrator)
    ├── cmplx_standards.py (universal grader)
    ├── adapters/ (data builders)
    │   ├── nist_legacy_adapter.py — NIST diff (not a forward gate)
    │   ├── paper_validator_adapter.py — verify_*.json receipts
    │   ├── forge_runtime_adapter.py — Forge/ReForge deployment checks
    │   ├── application_validator_adapter.py — App gate validation
    │   ├── legacy_repo_port_adapter.py — Legacy repo port scoring
    │   ├── flcr80_repo_slot_adapter.py — 80-slot ribbon map readings
    │   └── mdhg_memory_port.py — Stdlib-only memory/cache port
    └── models/ (JSON model contracts)
        ├── normal_form_ingress_model.json
        ├── assembled_paper_model.json
        ├── maximal_manuscript_model.json
        ├── sm_mapping_row_model.json
        ├── external_pair_model.json
        ├── ability_seed_model.json
        ├── verifier_receipt_model.json
        ├── forge_runtime_model.json
        ├── application_validation_model.json
        ├── legacy_repo_port_model.json
        └── flcr80_repo_slot_model.json
```

---

## Quick Start

### 1. Lightweight Check (2 models, ~30 seconds)

```bash
cd D:\CQE_CMPLX\CMPLX-Standards
python run_standards_suite.py --models normal_form,ability_seed
```

**Output:** `D:\CQE_CMPLX\_drive-audit\output\CMPLX_STANDARDS_SUITE_REPORT.json`

### 2. Full Suite (11 models, ~2 minutes)

```bash
cd D:\CQE_CMPLX\CMPLX-Standards
python run_standards_suite.py --full
```

**Output:** `D:\CQE_CMPLX\_drive-audit\output\CMPLX_STANDARDS_SUITE_REPORT.json`

### 3. Full Suite + NIST Legacy Diff

```bash
cd D:\CQE_CMPLX\CMPLX-Standards
python run_standards_suite.py --full --legacy-nist-diff
```

---

## Model Reference

| Model | Records | What it grades | Adapter |
|-------|---------|---------------|---------|
| `normal_form` | Obligation rows | Readiness for normal-form conversion | Direct loader |
| `assembled_paper` | Paper intake JSONs | 15-section assembled products | Direct loader |
| `maximal_manuscript` | Manuscript records | Reader-facing FLCR manuscripts | Direct loader |
| `sm_mapping_row` | SM mapping rows | FLCR-to-SM mapping | Direct loader |
| `external_pair` | External evidence | Peer-reviewed calibration packages | Direct loader |
| `ability_seed` | Ability seeds | Local/legacy seed catalog | Direct loader |
| `verifier_receipt` | verify_*.json | On-disk verification receipts | `paper_validator_adapter.py` |
| `forge_runtime` | Forge records | Lattice Forge deployment health | `forge_runtime_adapter.py` |
| `application_validation` | App targets | General app gate validation | `application_validator_adapter.py` |
| `legacy_repo_port` | Repo ports | Legacy repo promotion readiness | `legacy_repo_port_adapter.py` |
| `flcr80_repo_slot` | Ribbon slots | 80-slot ribbon map readings | `flcr80_repo_slot_adapter.py` |

---

## Inclusion Bands

| Band | Threshold | Meaning |
|------|-----------|---------|
| `perfect_fit` | ≥ 1.00 | Every required field present, model vocabulary used |
| `model_inclusive` | ≥ 0.90 | Close enough to route into model use with bounded residues |
| `partial_inclusive` | ≥ 0.65 | Useful signal but needs completion before strong model use |
| `weak_inclusive` | ≥ 0.35 | Weakly aligned, should remain exploratory |
| `non_inclusive` | < 0.35 | Does not belong in the model without rework or a new model |

---

## Interpreting Results

### Good Fit (≥ 90)
- Data is ready for downstream use
- May have minor missing fields but nothing blocking

### Partial Fit (65–89)
- Has useful structure but needs work
- Check `missing_fields` in the report for specifics

### Weak/Non-Inclusive (< 65)
- Significant gaps or misalignment
- Review whether the data belongs in this model at all
- Consider creating a new model contract if the data is valid but structurally different

---

## Known Issues & Data Gaps

### Maximal Manuscript (fit ~32)
- **Status:** Data gap, not code bug
- **Issue:** `MAXIMAL_FLCR_MANUSCRIPTS/` contains bare paper IDs without manuscript content
- **Impact:** 39/40 records graded as `non_inclusive`
- **Action needed:** Populate manuscript records with `has_abstract`, `has_main_results`, `has_construction`, etc.

### Verifier Receipts (fit ~75)
- **Status:** Partial data gap
- **Issue:** Older `verify_*.json` files missing `schema`, `honesty_boundary`, `boundary` fields
- **Impact:** 7/20 receipts graded as `weak_inclusive`
- **Action needed:** Backfill missing fields in old receipts, or accept as legacy data

### Assembled Papers (fit ~90)
- **Status:** Minor gaps
- **Issue:** Some intake JSONs missing `required_direct.open_obligations`, `receipts`, `blockers`
- **Impact:** 10/40 records graded as `partial_inclusive`
- **Action needed:** Complete intake forms for papers with missing fields

---

## Running Against PaperLib

To grade the unified paper suite in `D:\PaperLib\`:

```bash
cd D:\PaperLib
python grade_unified_papers.py
```

This produces `CMPLX_STANDARDS_UNIFIED_PAPER_REPORT.json` using the `models/unified_paper_model.json` contract.

---

## Daily Operations

### Morning Standup Check
```bash
python run_standards_suite.py --models normal_form,verifier_receipt,forge_runtime
```

### Weekly Full Audit
```bash
python run_standards_suite.py --full
```

### Before Release
```bash
python run_standards_suite.py --full --legacy-nist-diff
# Compare against previous report for drift
```

---

## Forward Roadmap

1. **Phase 7 Lane A (Current):** CMPLX-Standards operational, NIST/NSIT preserved as lineage
2. **Phase 7 Lane B:** Maximal manuscript population — fill data gaps
3. **Phase 8:** Service offering — external clients can submit payloads for grading
4. **Phase 9:** Automated CI integration — standards gate on every commit

---

## Files

| Path | Purpose |
|------|---------|
| `CMPLX-Standards/cmplx_standards.py` | Core grader |
| `CMPLX-Standards/run_standards_suite.py` | Orchestrator |
| `CMPLX-Standards/models/` | Model contracts |
| `CMPLX-Standards/adapters/` | Data builders |
| `CMPLX-Standards/MODEL_REGISTRY.json` | NIST→CMPLX mapping |
| `_drive-audit/output/CMPLX_STANDARDS_SUITE_REPORT.json` | Latest report |
| `D:\PaperLib\grade_unified_papers.py` | PaperLib-specific grader |
| `D:\PaperLib\models\unified_paper_model.json` | PaperLib model contract |

---

*Generated by CMPLX-Standards v1.0.0*
