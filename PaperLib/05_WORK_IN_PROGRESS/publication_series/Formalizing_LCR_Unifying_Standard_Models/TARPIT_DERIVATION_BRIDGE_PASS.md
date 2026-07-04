# TarPit Derivation Bridge Pass

Created: 2026-06-28

## Result

TarPit already closes the exact internal mass side. The gap is not "can this system assign mass to data?" The gap is adapter authority: which declared 2x2 handshake maps TarPit/VOA/kappa mass coordinates into unitful Standard Model observables without quietly using the target value as an anchor.

## What Is Closed Now

| Layer | Status | Evidence |
|---|---|---|
| TarPit data mass | closed internal | `CMPLX-PartsFactory-main/src/cmplx/symbolic/tarpit/grain.py` exposes `DimensionalExtent.mass_1d` and `mass_2d`; `ecology.py` emits `final_mass`. |
| Mass-residue carrier | closed internal | `MassResidueForge` states mass as VOA conformal weight: 2 massless vacua, 6 massive excited states, mass gap 5, residue carrier `C AND NOT R`. |
| Paper-15 receipt | closed internal | `CQE-paper-15-mass_residue_literalized_receipt.json` passes 10/10 internal checks. |
| Kappa event quantum | closed internal strong | `verify_kappa_derivation.json` binds `kappa = ln(phi)/16` and asserts no external calibration. |
| CKM structure | closed structural | CKM receipt maps exact SU(3) closure and bounded route to three angles plus one CP phase. |
| Measured targets | recorded | NP-15 receipts record CODATA/PDG alpha, CKM, Higgs, W, Z, and top values. |

## What Is Actually Open

The remaining open work is narrower and more useful than the papers previously implied:

1. **Adapter authority.** Define the exact adapter from TarPit/VOA/kappa coordinates to physical units.
2. **Promotion reconciliation.** Resolve the conflict between receipts that say `external_calibration_needed=false` for kappa constants and receipts that keep Higgs/alpha/CKM in a calibration-bound lane.
3. **No-fit rule.** A physical derivation cannot use the target observable as its scale anchor.
4. **Residual ledger.** Every promoted physical number needs a residual against PDG/CODATA with uncertainties.

## Immediate Derivation Target

Create `tarpit_kappa_physical_adapter`:

```text
TarPit final_mass / DimensionalExtent vector
  + VOA weight/residue state
  + kappa = ln(phi)/16
  + sector tag
  + unit map
  -> predicted physical quantity
  -> residual and claim-lane promotion decision
```

Promotion rule: promote only when the adapter does not use the target observable as an anchor and the residual is within the declared uncertainty or a pre-registered estimate tolerance.

## Lift Tower Execution

The adapter surface is now executable as a tower queue. `tools/tarpit_lift_tower_pass.py` loads `STATE_BOUND_PROOF_CONTRACT_MATRIX.json`, feeds every FLCR lift through the full 2x2x2 LCR enumeration, decomposes each enumerated state into Rule-30 linear/obstruction/correction and VOA mass terms, runs each row through TarPit, and recomposes the results into paper, slot-family, and decade towers.

Current receipt: `TARPIT_LIFT_TOWER_PASS.json`.

| Item | Count |
|---|---:|
| FLCR lifts | 40 |
| LCR states per lift | 8 |
| TarPit enumeration rows | 320 |
| Successful TarPit runs | 320 |
| Error walls | 0 |
| Slot-family towers | 10 |
| Decade towers | 4 |

This closes the practical concern raised here: the first enumeration can be fully decomposed and then recomposed upward into stacked math/geometry towers. The remaining adapter work now starts from a complete TarPit tower receipt instead of an abstract claim.

## Universal Process Derivation Atlas

The next layer is now active as `UNIVERSAL_TARPIT_PROCESS_DERIVATION_PASS.json`. It treats TarPit readout, pairwise bondedness, and crystal comparison as a shared metric ledger for natural processes. Each process is assembled as LCR items, run through TarPit, compared through pair bonds/triads, projected against crystal forms, and checked against standard target rows where data already exists.

| Process family | Components | Pair bonds | Compared targets | External/adapter rows |
|---|---:|---:|---:|---:|
| Fine-structure constant | 4 | 6 | 2 | 0 |
| Electroweak mass residue | 7 | 21 | 3 | 0 |
| CKM bounded route | 12 | 66 | 0 | 9 |
| Crystal zoo bondedness | 9 | 36 | 3 | 0 |
| Chemical bond energy forms | 7 | 21 | 0 | 3 |
| Universe-scale TarPit tower | 8 | 28 | 3 | 0 |
| Waveform encoding collapse | 18 | 153 | 1 | 1 |
| Beta decay topology | 6 | 15 | 0 | 2 |

Global receipt summary: 8 process families, 71 LCR components, 346 pair bonds, 346 triads, all TarPit process runs successful. This is the correct generalization: the TarPit readout is not just mass; it is a process metric substrate. Bondedness can now be computed across assembled forms, not only inside individual rows.

## Damascus Folding Of Emitted Forms

The emitted process forms are now recursively readable. `DAMASCUS_TARPIT_FOLDING_PASS.json` takes the universal process atlas outputs, converts each emitted process form into new LCR components, runs those forms back through TarPit, and repeats the operation for five additional folds.

| Fold layer | Forms | Pair bonds | Triads | Avg TarPit mass | Nearest crystal family |
|---:|---:|---:|---:|---:|---|
| 0 | 8 | 120 | 120 | 0.507530 | kagome |
| 1 | 8 | 168 | 168 | 0.513572 | kagome |
| 2 | 8 | 168 | 168 | 0.509083 | kagome |
| 3 | 8 | 168 | 168 | 0.509664 | kagome |
| 4 | 8 | 168 | 168 | 0.512665 | kagome |
| 5 | 8 | 168 | 168 | 0.505553 | kagome |

This is the Damascus operation: emit, fold, re-read, emit again. The pass preserves lineage and measures mass, bondedness, crystal proximity, open load, and closed load at every fold. It does not replace process-specific physical adapters; it supplies their recursive metric substrate.

## Fine-Bonding Stabilization Derivation

`FINE_BONDING_STABILIZATION_DERIVATION_PASS.json` now specializes the TarPit/Damascus stack around the fine-structure and fine-bonding question. The pass localizes the useful signal to the first Damascus refold: the global process ledger moves from `120` pair bonds at fold 0 to `168` pair bonds and `168` triads at fold 1, then remains locked at `168` through fold 5 while open load stays `15` and the nearest crystal family remains `kagome`.

| Reading | Value | Meaning |
|---|---:|---|
| Fold-0 pair bonds | 120 | E8 positive-root hemisphere count appears as the seed fold bond surface. |
| Stable pair bonds | 168 | Fold 1 through fold 5 stabilize at the Fano/Hamming automorphism order. |
| Stable triads | 168 | Pair-bond stabilization is mirrored by triad stabilization. |
| Pair-bond jump | 48 | First-refold added boundary lanes after the seed emission. |
| Open load | 15 | Open obligation mass stays constant during stabilization. |
| Hamming address | 137 | The address is represented as the 1-3-7 Hamming chain. |
| PFC2 realization | 137 = 120 + 13 + 4 | E8 positive-root floor plus boundary half-vignettes plus D4 faces. |
| Weak-face selector | 137 mod 4 = 1 | Candidate exterior face selector for the diagonal-removal adapter. |

This moves the fine-bonding search from an intuition into a receipt-backed adapter target. The next exact adapter is:

```text
linear Hamming/PFC2 address 137
  - diagonal removal of the E8 positive-root floor 120
  -> boundary dispersion 17
  -> split as 13 boundary half-vignettes + 4 D4 faces
  -> mod-4 residue 1 as the candidate exterior weak-face selector
```

The physical alpha claim is not promoted by this receipt alone. What is promoted is the location and shape of the derivation: the no-target-anchor adapter must prove the diagonal-removal boundary split and then compute the residual against CODATA alpha without using alpha as the scale anchor.
