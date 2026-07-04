# Cross-Cutting Integrity Notes — CQE-Papers 09–32

This file collects the integrity issues that span multiple papers after the batch read of the production corpus.

## 1. Receipt-status mismatches

Several formal papers claim pass-like status while their production receipts report `fail` or `pass_with_*_obligations`:

- **Paper 09:** `hamiltonian_window_emergence_receipt.json` now passes after normalizing `ROOT` to the repo root and scoping the McKay route to the light-cone adjugation witness. Unbounded closed-form McKay arithmetic (09.2/09.3) remains open.
- **Paper 10:** `t10_master_receipt.json` now passes after normalizing `ROOT` and updating the Paper-00 source lookup to the canonical `src/papers/source_backup` path.
- **Paper 11:** `theory_admission_gate_receipt.json` now passes after normalizing `ROOT` so the T10 trust anchor loads from the correct path.
- **Paper 12:** `p3_closure_receipt.json` still reports `fail` on `cold_start_bit_exact`. This is a substantive open obligation, not a path bug: cold Rule 30 Problem 3 extraction remains unclosed.
- **Papers 21–32:** multiple receipts report `pass_with_open_*` or interpretive statuses. These are correctly scoped in the skeletons.

## 2. Claim-taxonomy tension

`CQE-paper-formal-CLAIM` lists `CQE-09` to `CQE-18` as having `0 ECO`, yet:

- **Paper 13** contains a CKM calibration bridge (physical quark/color-charge identification).
- **Paper 15** maps the internal mass-residue carrier to the Higgs mass `125.25 GeV`.

The taxonomy's 'Calibration layer' separately lists Higgs and CKM, but per-paper classification must retain **both** IPMC and ECO labels. The skeletons mark the internal algebraic parts as IPMC and the physical calibrations as ECO.

## 3. R30 umbrella mismatch

`CMPLX-R30-main/PROOF/papers/09_*.md`–`16_*.md` are older umbrella papers (transformer worldsheet, Wow signal, Pariah boundary, physical constants, observer lattice chain, magic square, D12 Moonshine chain, digit rollout). They **do not** align 1:1 with the production `CQE-paper-09`–`CQE-paper-16`. They should be treated as historical cross-references only.

## 4. Missing promoted verifiers

The Lane-A dyad brief noted Papers 16 and 24 lacked dedicated promoted verifiers. The production repo now contains `verify_continuum_edge_residuals.py` and `verify_knightforge_ca.py`, but both heavily wrap `lattice_forge.centroid_voa` package checks. Future work may promote stronger, paper-specific verifiers.

## 5. No AirLock specs for 09–32

`CQECMPLX-AirLock/cqe-production-v0.1/papers/` contains only `CQE-paper-01` through `CQE-paper-05`. Specifications for Papers 06–32 are missing from the AirLock layer.

## 6. Source-backup variants

The `.25/.50/.75/_UPGRADED.md` companion variants were not found in the primary production repo for Papers 09–32. Only single historical mirrors (`PAPER-BODY.md`, `SOURCE.md`, `01-CQE-formal/FORMAL.md`) were located under `CQECMPLX-Production/papers/CQE-paper-NN/`.

## 7. Global open obligations carried forward

These obligations appear across multiple papers:

- **McKay-Thompson parity (O2′):** Papers 02, 09, 16, 18.
- **`W(E8)` lookup table (O1):** Papers 08, 17.
- **Full Moonshine identification:** Papers 18, 29.
- **Physical-unit / energy bridges:** Papers 25, 26, 29.

These remain open until their respective source papers produce receipts that close them.
