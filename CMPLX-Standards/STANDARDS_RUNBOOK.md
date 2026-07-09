# CMPLX-Standards Operational Runbook

**For:** Standards validation of CMPLX builds  
**When:** Daily check, weekly audit, pre-release gate  
**Where:** `D:\CQE_CMPLX\CMPLX-Standards\`  

---

## 1. Environment Setup

Ensure the following paths exist:

```
D:\CQE_CMPLX\CMPLX-Standards\          (this directory)
D:\CQE_CMPLX\_drive-audit\output\      (report output)
D:\CQE_CMPLX\tools\forge_runtime_env.ps1  (Forge wrapper)
```

Python 3.10+ required. No pip dependencies for core grader (stdlib only).

---

## 2. Daily Check (5 minutes)

**Goal:** Verify core systems are healthy.

```powershell
cd D:\CQE_CMPLX\CMPLX-Standards
python run_standards_suite.py --models normal_form,verifier_receipt,forge_runtime
```

**Expected results:**
- `normal_form`: avg fit ≥ 95
- `verifier_receipt`: avg fit ≥ 70
- `forge_runtime`: avg fit ≥ 95, pass_count ≥ 20

**If any model drops below threshold:**
1. Read the report: `D:\CQE_CMPLX\_drive-audit\output\CMPLX_STANDARDS_SUITE_REPORT.json`
2. Identify lowest-fit records
3. Check `missing_fields` for blockers
4. File a ticket or fix immediately

---

## 3. Weekly Full Audit (15 minutes)

**Goal:** Comprehensive health check across all 11 models.

```powershell
cd D:\CQE_CMPLX\CMPLX-Standards
python run_standards_suite.py --full
```

**Review checklist:**
- [ ] Total records graded > 400
- [ ] Average model fit > 85
- [ ] No `non_inclusive` records in critical models (normal_form, forge_runtime, application_validation)
- [ ] Maximal manuscript fit trending upward (currently ~32, target > 60)
- [ ] NIST legacy diff attached if `--legacy-nist-diff` used

**Save report with date stamp:**
```powershell
copy D:\CQE_CMPLX\_drive-audit\output\CMPLX_STANDARDS_SUITE_REPORT.json `
     D:\CQE_CMPLX\_drive-audit\output\CMPLX_STANDARDS_SUITE_REPORT_%date:~-4,4%-%date:~-10,2%-%date:~-7,2%.json
```

---

## 4. PaperLib Standards Check (10 minutes)

**Goal:** Grade unified papers against CMPLX-Standards.

```powershell
cd D:\PaperLib
python grade_unified_papers.py
```

**Review checklist:**
- [ ] All 101 papers graded
- [ ] Average fit = 100 (all papers have required sections)
- [ ] Cross-references verified
- [ ] Content hashes match (run `python cmplx_query.py verify "Paper N"` for spot checks)

---

## 5. Pre-Release Gate (30 minutes)

**Goal:** Block release if standards are not met.

```powershell
cd D:\CQE_CMPLX\CMPLX-Standards
python run_standards_suite.py --full --legacy-nist-diff
```

**Release criteria:**

| Model | Min Avg Fit | Max Non-Inclusive |
|-------|-------------|-------------------|
| normal_form | 95 | 0 |
| assembled_paper | 85 | 2 |
| forge_runtime | 95 | 0 |
| application_validation | 95 | 0 |
| ability_seed | 95 | 0 |
| legacy_repo_port | 90 | 1 |
| flcr80_repo_slot | 95 | 0 |
| verifier_receipt | 70 | 3 |
| sm_mapping_row | 85 | 2 |
| external_pair | 95 | 0 |
| maximal_manuscript | 30* | N/A |

*Maximal manuscript is currently data-limited; this threshold will rise as manuscripts are populated.

**If any criterion fails:**
1. Do NOT proceed with release
2. Fix blockers or adjust threshold with documented justification
3. Re-run until all criteria pass

---

## 6. Troubleshooting

### "ModuleNotFoundError: No module named 'lattice_forge'"
**Cause:** Forge runtime adapter cannot import lattice_forge  
**Fix:** Run the Forge wrapper first:
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\CQE_CMPLX\tools\forge_runtime_env.ps1 lattice-forge status
```

### "missing_or_invalid_input" in report
**Cause:** Model input file does not exist or is malformed  
**Fix:** Check the adapter for the model. Most inputs are in:
- `papers/active-rework/publication_series/...`
- `_drive-audit/output/`

### Low fit scores in maximal_manuscript
**Cause:** Manuscript records are bare (paper IDs only, no content)  
**Fix:** This is a known data gap. Populate `MAXIMAL_FLCR_MANUSCRIPTS/` with actual manuscript content.

### Old receipts missing schema/boundary
**Cause:** Pre-standards verify_*.json files  
**Fix:** Either backfill fields or accept as legacy. The adapter will still grade them, just with lower fit.

---

## 7. Extending the Suite

### Add a new model

1. Create `models/my_new_model.json` with:
   - `model_id`, `version`, `description`
   - `record_selector` (JSON path to records array)
   - `record_id_paths` (identifiers)
   - `weighted_fields` (path → weight)
   - `allowed_values` (vocabulary enforcement)
   - `conditional_required_fields` (contextual requirements)
   - `thresholds` (band boundaries)

2. Add to `MODEL_REGISTRY.json`:
```json
"my_new_model": {
    "key": "my_new_model",
    "replaces": "what this replaces",
    "input": "path/to/input.json"
}
```

3. Add to `FULL_MODEL_SET` in `run_standards_suite.py`

4. Create adapter if needed (optional, can use direct loader)

### Add a new adapter

1. Create `adapters/my_adapter.py` with `build_payload()` function
2. Import in `run_standards_suite.py`
3. Add to `resolve_payload()` switch

---

## 8. Emergency Contacts

| Issue | Contact | Response |
|-------|---------|----------|
| Standards code bug | File issue in CMPLX-Standards/ | ASAP |
| Model contract update | Update `models/*.json` | Immediate |
| Data gap (missing inputs) | Populate source directories | Within sprint |
| Release gate failure | Do not release | Block until fixed |

---

## 9. Historical Reports

Archive weekly reports in:
```
D:\CQE_CMPLX\_drive-audit\output\archive\
```

Naming convention:
```
CMPLX_STANDARDS_SUITE_REPORT_YYYY-MM-DD.json
CMPLX_STANDARDS_SUITE_REPORT_YYYY-MM-DD.md
```

---

*Last updated: 2026-07-03*
