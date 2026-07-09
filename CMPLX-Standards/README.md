# CMPLX-Standards

CMPLX-Standards is the renamed and rewritten NIST/NSIT tool surface.

It is a universal grading tool for asking:

- Does this data belong in the model?
- How close is it to perfect model inclusion?
- Which fields keep it from being perfect?
- Is it model-inclusive, partial, weak, or non-inclusive?

It is not a proof oracle and does not promote claims by itself. It produces a
measurement report that downstream validators, receipt binders, paper builders,
and external-data comparators can consume.

## Core Contract

Input:

1. A JSON payload containing records.
2. A CMPLX-Standards model contract.

Output:

1. Per-record fit score from `0` to `100`.
2. Per-record distance to perfect from `1` to `0`.
3. Inclusion band:
   - `perfect_fit`
   - `model_inclusive`
   - `partial_inclusive`
   - `weak_inclusive`
   - `non_inclusive`
4. Missing fields and vocabulary failures.
5. Aggregate score and band counts.

## Usage

```powershell
python CMPLX-Standards\cmplx_standards.py `
  --input papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\NORMAL_FORM_INGRESS_MATRIX.json `
  --model CMPLX-Standards\models\normal_form_ingress_model.json `
  --output papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CMPLX_STANDARDS_NORMAL_FORM_INGRESS_REPORT.json `
  --markdown papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CMPLX_STANDARDS_NORMAL_FORM_INGRESS_REPORT.md
```

## Development Direction

This tool should grow alongside the rest of the system. Each new model family
gets a model contract under `models/`. The same grader can then evaluate papers,
normal forms, receipt rows, external datasets, comparator rows, CAM/crystal
memory, or tool outputs.

The older NIST/NSIT reports become model-specific inputs or prior reports. The
CMPLX-Standards layer is the reusable measurement surface.

## Forge / ReForge Runtime Gate

Forge, ReForge, Rhenium, and Lattice Forge deployment is now a standards model:

```powershell
python CMPLX-Standards\run_standards_suite.py --models forge_runtime
```

This runs `adapters/forge_runtime_adapter.py`, which checks canonical import
resolution, editable package installs, the Lattice Forge seed/overlay runtime,
ForgeFactory/ReForge engine registry, and a sample receipted Forge lookup.

## General Application Validation

The broader application gate is:

```powershell
python CMPLX-Standards\run_standards_suite.py --models application_validation
```

This builds a reusable application-validation payload from paper `verify_*.py`
tools, receipt artifacts, source paths, runtime commands, test commands,
standards models, and declared validator links. It is the forward CMPLX
replacement for one-off application checks.

## Legacy Repo Port Gate

Older repo findings are scored in two layers: concrete executable/contract
ports plus broad intake records for every legacy seed in the queue:

```powershell
python CMPLX-Standards\run_standards_suite.py --models legacy_repo_port
```

Current first-pass ports:

- MDHG memory/cache behavior as executable stdlib adapter.
- SNAP label/ledger runtime from PartsFactory as executable provider check.
- TarPit symbolic ETP provider from PartsFactory as executable morphon-atom linkage check.
- CMPLX-MORSR diagnostic umbrella contract.
- CQE_MORSR hidden-result validation loop contract.
- CMPLX-NVEST domain-neutral diagnostic adapter contract.
- Full 16-seed legacy queue as `candidate_indexed` broad intake records with
  source-path statistics, syntax probes, and promotion-readiness scoring.

## FLCR80 Repo Slot Readings

The full workspace registry and seed queues can be projected onto the original
80-ribbon slot map:

```powershell
python CMPLX-Standards\run_standards_suite.py --models flcr80_repo_slot
```

This runs `tools/build_flcr80_repo_slot_readings.py` and grades all 80 slot
records against `models/flcr80_repo_slot_model.json`. The scoring basis is the
fixed `ORIGINAL_80_DIMENSIONAL_RIBBON_MAP.json`, not an arbitrary repo-readiness
scale.
