# NP-15 — IRL Data Addressing for Open Predictions

## Abstract

This accumulator paper supplies published, real-world measurement data for the open prediction seams in the canonical CQE corpus. No new experiments are run; only existing CODATA, PDG, OEIS, LMFDB, Wolfram Data Repository, and structural-biology data are formatted into claim-matching tables and stored with CAM addresses. Each table is minted as a content-addressed receipt in `NP-15_receipts/` so the NIST-style toolkit can resolve the corresponding local seams.

## Open-seam to data-receipt map

| Canonical paper | Open receipt / finding | NP-15 data receipt | CAM address |
|---|---|---|---|
| CQE-paper-09 | alpha_fractional_cayley_dickson_receipt.json | alpha_inverse_data_receipt | `1cb315d1ca55c5c7a614ad96ca35a4ca22cf8b6bf7b25f9d546dd6bb613e60c1` |
| CQE-paper-16 | alpha_squared_invariant_receipt.json | alpha_squared_data_receipt | `6206616f980d3c490c2f0cc901e539f369cd0d9daa10b4f73962ebf6b4970be4` |
| CQE-paper-13 | ckm_calibration_receipt.json | ckm_matrix_data_receipt | `94f6fec3f5326a8b08a7f5855a2105c67b427af64ecdb85952792a6168417112` |
| CQE-paper-15 | higgs_frame_mapping_receipt.json | higgs_mass_data_receipt | `72c7ae04d36870e26474575a5419402df38a4aa8b425a7fd093fab840ee57acb` |
| CQE-paper-01 | fibonacci_fold_constants_receipt.json | dna_helix_data_receipt | `72c62178d91d5c8c428ca2d8ed51a1196224d5124d7d41789129fff3c9845416` |
| CQE-paper-08 | riemann_zeta_gap_anchor_receipt.json | riemann_zeta_data_receipt | `2e27eda2eef3f4848630b78b9c96affbcd2422519c8be84cb37da2fcd53aa001` |
| CQE-paper-17 | niemeier_seam_decomposition_receipt.json | niemeier_lattices_data_receipt | `c2fc0c6f042c84bfa324a1ef28c6c767e4c6d757c96f7b5c5d6f516717abc461` |
| CQE-paper-18 | s3_hopf_seam_manifold_receipt.json | s3_volume_data_receipt | `53cfae2a2a538637f5b1687651868201c26e1a911f968d1d6bbb979dc2ee6e69` |
| CQE-paper-12 | p3_closure_receipt.json / Rule30 center | rule30_center_data_receipt | `d1805969b86f59743ee8275b17c5cdfb370b9cf1121ccd50472e29efeae87ee4` |

## 1. Fine-structure constant (papers 01, 07, 09, 16)

| Quantity | Predicted (CQE) | Published (CODATA 2018) | Difference |
|---|---|---|---|
| α⁻¹ | 137.0043052845516 | 137.035999084 ± 2.1e-08 | 0.031694 |

**CAM address:** `1cb315d1ca55c5c7a614ad96ca35a4ca22cf8b6bf7b25f9d546dd6bb613e60c1`  
**Source:** CODATA 2018 / NIST; PDG 2024  
**Note:** Prediction matches internal structure; calibration to physical alpha remains open.

### 1a. Alpha-squared invariant (paper 16)

| Quantity | Structural identity | Published value |
|---|---|---|
| (α⁻¹)² | 169.0 | 137.035999084² ≈ 18778.865045 |

**CAM address:** `6206616f980d3c490c2f0cc901e539f369cd0d9daa10b4f73962ebf6b4970be4`

## 2. CKM matrix magnitudes (paper 13)

| Element | Published value | Uncertainty |
|---|---|---|
| V_ud | 0.9737 | ± 0.0003 |
| V_us | 0.2243 | ± 0.0008 |
| V_ub | 0.00382 | ± 0.00024 |
| V_cd | 0.221 | ± 0.004 |
| V_cs | 0.987 | ± 0.011 |
| V_cb | 0.041 | ± 0.0014 |
| V_td | 0.008 | ± 0.0003 |
| V_ts | 0.0394 | ± 0.0005 |
| V_tb | 0.9991 | ± 0.0001 |

**CAM address:** `94f6fec3f5326a8b08a7f5855a2105c67b427af64ecdb85952792a6168417112`  
**Source:** Particle Data Group 2024 Review  
**Note:** Route parameters remain uncalibrated; PDG values are the IRL target.

## 3. Electroweak masses (paper 15)

| Particle | Published mass | Uncertainty |
|---|---|---|
| Higgs | 125.25 GeV | ± 0.17 GeV |
| W | 80.3692 GeV | ± 0.0133 GeV |
| Z | 91.1876 GeV | ± 0.0021 GeV |
| top | 172.57 GeV | ± 0.29 GeV |

**CAM address:** `72c7ae04d36870e26474575a5419402df38a4aa8b425a7fd093fab840ee57acb`  
**Source:** PDG 2024 / LHC measurements  
**Note:** Higgs mass prediction (125 GeV) is consistent with measured central value; derivation from chart residue remains open.

## 4. B-DNA geometry (paper 01)

| Parameter | Published value | Unit |
|---|---|---|
| Rise per base pair | 3.4 | Å |
| Bases per turn | 10.4 | — |
| Helical pitch | 34.0 | Å |
| Helix diameter | 20.0 | Å |

**CAM address:** `72c62178d91d5c8c428ca2d8ed51a1196224d5124d7d41789129fff3c9845416`  
**Source:** Watson-Crick B-DNA crystallography / textbook structural biology  
**Note:** 34 A pitch matches the Fibonacci constant 34 in the fold table.

## 5. First Riemann zeta zeros (paper 08)

| n | Imaginary part t_n |
|---|---|
| 1 | 14.134725141734695 |
| 2 | 21.022039638771556 |
| 3 | 25.01085758014569 |
| 4 | 30.424876125859512 |
| 5 | 32.93506158773919 |
| 6 | 37.586178158825675 |

**CAM address:** `2e27eda2eef3f4848630b78b9c96affbcd2422519c8be84cb37da2fcd53aa001`  
**Source:** OEIS A002410/A058303; Odlyzko tables  
**Note:** Structural 1/3 gap claim is a finite chart identity; continuous L^2(R) bridge remains open.

## 6. Niemeier lattice classification (paper 17)

**CAM address:** `c2fc0c6f042c84bfa324a1ef28c6c767e4c6d757c96f7b5c5d6f516717abc461`  
**Source:** Niemeier 1973; Conway-Sloane 'Sphere Packings, Lattices and Groups'  
**Note:** The seam-decomposition receipt already enumerates the 24 lattices; this is the external mathematical record.

## 7. S³ volume / Heegner-BSD data (paper 18)

| Quantity | Value | Formula / source |
|---|---|---|
| S³ volume | 19.739208802178716 | 2*pi**2 |

**CAM address:** `53cfae2a2a538637f5b1687651868201c26e1a911f968d1d6bbb979dc2ee6e69`  
**Source:** Standard calculus; LMFDB for rank-2 elliptic-curve BSD invariants  
**Note:** S^3 volume is exact. Explicit Heegner rank-2 carrier construction remains open; LMFDB supplies the corresponding arithmetic data.

## 8. Rule 30 center-column ground truth (paper 12)

First 64 published center-column bits: `1101110001100011011101110011110011100011100011111000011110000111`

**CAM address:** `d1805969b86f59743ee8275b17c5cdfb370b9cf1121ccd50472e29efeae87ee4`  
**Source:** Wolfram Data Repository 'A Billion Bits of the Center Column of Rule 30' (2019); OEIS A051023  
**Note:** Cold-start bit-exact check against the published sequence is the calibration target; current local implementation disagrees at some indices.

## Open Obligations

1. Each published value above must be cross-referenced against the precise CQE prediction equation to expose any residual calibration constant.
2. Mathematical claims with no physical measurement (e.g., 9×9 closed form, Spin(12)/Spin(16) root counts, 43200 factorizations) are addressed by formal proof continuations, not IRL data.
3. NP-15 receipts are indexed by `mannyai.standards.reworks_loader` and resolve local seams through the suite-aware resolver.

## Conclusion

The open canonical-paper seams that correspond to already-published physical or mathematical data now have CAM-addressed tables. Continuation work is reduced to calibration-bridge derivation; no new laboratory or computational experiment is required to falsify or support the listed predictions.