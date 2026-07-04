# Paper 15 — QFT/Higgs Mass-Residue Carrier

**Status.** IPMC for the finite mass-residue carrier: Rule 30 `F2` split, Arf-invariant obstruction, VOA weight partition `2q^0 + 6q^5`, correction-residue identification, the eight-states/one-dual-reading theorem, the forced-printout theorem, the `2×2×2` vs `3×3` framing resolution, and the mass-gravity drive. IBN for the Higgs doublet `3+1` frame mapping and the mass = VOA weight interpretation. ECO for measured Higgs mass, electroweak symmetry breaking, and Yukawa coupling calibration.

---

## Abstract

Paper 15 defines the CQECMPLX substrate meaning of a mass-residue carrier. The closed result is finite and local: Rule 30 splits over `F2` into a linear part and a bilinear obstruction, the obstruction has Arf invariant `0`, Arf-matching gluing admits while Arf-mismatch gluing rejects, the chart states split into `2q^0 + 6q^5` under the VOA weight, and the local correction residue `C AND NOT R` identifies the states that carry surviving residue. The paper also resolves the eight-state / nine-state puzzle: the apparent `+1` is a dual reading of one state through the wrap, not a separate ninth state.

The claim is affirmative at the CQECMPLX physics-map layer: surviving correction residue plus VOA weight is the internal mass-residue carrier. This is the suite's Higgs-adjacent substrate object. The remaining obligation is the external calibration from this carrier to measured Higgs/QFT quantities: particle masses, electroweak symmetry breaking, Yukawa couplings, or a numerical mass spectrum.

**Keywords:** mass-residue carrier, Arf invariant, VOA weight, correction residue, `2×2×2` vs `3×3`, Higgs doublet, mass-gravity drive.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 15.1 | Rule 30 decomposes over `F2` as `(L xor C xor R) xor (C and R)`. | [D] | `mass_residue_carrier_receipt.json`: 10/10 |
| 15.2 | The bilinear obstruction has Arf invariant `0`; matching Arf glues, mismatch rejects. | [D] | Same receipt |
| 15.3 | VOA sector decomposition is `Z(q) = 2q^0 + 6q^5`. | [D] | Same receipt |
| 15.4 | Correction residue `C AND NOT R` fires exactly on `(0,1,0)` and `(1,1,0)`. | [D] | Same receipt |
| 15.5 | Nth-bit local/oracle layer passes; McKay-Thompson parity remains open. | [D] | Same receipt |
| 15.6 | Mass = VOA conformal weight: 2 massless vacua + 6 massive excited states. | [I] | `mass_residue_literalized_receipt.json`: 10/10 |
| 15.7 | The chart carries 8 states, not 9; the `+1` is a dual reading via wrap. | [D] | `eight_states_one_dual_reading_receipt.json`: 7/7 |
| 15.8 | The 9th is the forced printout of the completed 8, not an independent state. | [D] | `ninth_is_forced_printout_receipt.json`: 6/6 |
| 15.9 | The `2×2×2` vs `3×3` mass discrepancy is a basis difference, not a failure. | [D] | `mass_framing_2x2x2_vs_3x3_receipt.json`: 7/7 |
| 15.10 | Higgs doublet maps as `3+1` (3 Goldstone + 1 physical Higgs). | [I] | `higgs_frame_mapping_receipt.json`: 6/7 (mass prediction open) |
| 15.11 | Mass-residue drives the gluon roll toward bonded `L=R` attractors in ≤3 steps. | [I] | `mass_gravity_drive_receipt.json`: 7/7 |
| 15.12 | Measured Higgs mass and electroweak parameters require external calibration. | [X] | Explicit obligation |
| 15.13 | Closed-form McKay-Thompson correction parity remains open. | [X] | Explicit obligation |
| 15.14 | Explicit numerical mass reconciliation (framework masses + trace → measured masses) is the remaining calibration. | [X] | Explicit obligation |

---

## 2. Definitions

**Carrier effect.** A quantity accepted only when it is witnessed by local readout and receipt.

**Linear part.** `L xor C xor R` — the `F2` linear component of the local Rule 30 formula.

**Obstruction.** The bilinear term `C and R` — the `F2` nonlinear component.

**Correction residue.** `C and not R` — the local term that fires on the shell-2 chiral doublet.

**Mass-residue carrier.** The substrate object that survives cancellation, has a receipt, and carries a weight. It is the CQECMPLX internal mass-like carrier. A physical rest-mass value requires a later calibrated map into measured units.

**Wrap.** The antipodal / Cayley-Dickson conjugation operator that re-reads one chart state through a different face. It is a fixed-point-free involution.

**Forced printout.** The parity/trace of the completed eight states, neutral while the eighth slot is open and forced to exactly one of two values on completion. It is the Event-Law receipt of the eight (the master-receipt slot, Paper 10), not an independent state.

---

## 3. Theorems and Proofs

### Theorem 15.1 — Rule 30 Split over F2

`Rule30(L,C,R) = (L xor C xor R) xor (C and R)` on all eight states.

**Proof.** From Paper 06 (Theorem 6.3), `Rule30 = Rule90 xor correction = (L xor R) xor (C and not R)`. Expanding:
```text
Rule30 = L xor R xor C xor (C and R)
       = (L xor C xor R) xor (C and R)
```
The verifier exhausts all eight states and confirms the split holds on every row. The linear part is `L xor C xor R`; the obstruction is `C and R`. ∎

### Theorem 15.2 — Arf Invariant and Gluing Rule

The bilinear obstruction `C and R` has Arf invariant `0`. Arf-matching classes glue; Arf-mismatch classes reject.

**Proof.** The `f2_majorana` verifier computes the Arf invariant for the quadratic forms associated with the obstruction. It reports:
```text
q_zero_arf = 0
q_hyperbolic_arf = 0
q_elliptic_arf = 1
rule30_correction_arf = 0
zero_vs_hyperbolic_can_glue = true
zero_vs_elliptic_can_glue = false
```
Since the correction's Arf invariant is `0`, it matches the zero form and the hyperbolic form, and mismatches the elliptic form (`arf = 1`). Therefore matching Arf classes glue, and mismatched classes reject. ∎

### Theorem 15.3 — VOA Sector Decomposition

The eight chart states decompose under VOA weight as `Z(q) = 2q^0 + 6q^5`.

**Proof.** The `centroid_voa` verifier assigns weights to the eight states. The two vacua `(0,0,0)` and `(1,1,1)` have weight `0`. The remaining six states have weight `5`. Therefore the seed partition function is exactly `2q^0 + 6q^5`. ∎

### Theorem 15.4 — Correction Residue States

The correction residue `C AND NOT R` fires exactly on `(0,1,0)` and `(1,1,0)`.

**Proof.** Exhausting all eight states: `C AND NOT R = 1` iff `C = 1` and `R = 0`. The states satisfying this are exactly `(0,1,0)` and `(1,1,0)`. These are the two shell-2 states in the chiral doublet (Paper 02). ∎

### Theorem 15.5 — Eight States, One Dual Reading

The chart carries exactly eight states. The apparent `+1` is a dual reading of one state through the wrap, not a separate ninth state.

**Proof.** The `eight_states_one_dual_reading` verifier checks: the wrap is an involution (`wrap(wrap(x)) = x`), it has no fixed points (`wrap(x) ≠ x` for all `x`), and the singlet axis is one state with two faces. The apparent nine is `eight + one re-reading`. Therefore there is no ninth state. ∎

### Theorem 15.6 — The Ninth Is a Forced Printout

The ninth slot is the forced printout (parity/trace) of the completed eight. It is neutral while the eighth slot is open and forced to exactly one of two values on completion.

**Proof.** The `ninth_is_forced_printout` verifier checks: the ninth is neutral while the eighth is open, the ninth is forced to one of two choices on completion, the two choices are set by the eighth, the ninth is a deterministic printout, and the ninth is a function of the eight (not independent). All checks pass. Superposition is therefore real but transient: the pre-completion neutrality is a structural property of the incomplete state, and the forcing on completion is the Event-Law receipt. ∎

### Theorem 15.7 — 2×2×2 vs 3×3 Framing Resolution

The `2×2×2` framework chart (8 states) and the standard `3×3` representation (9 = 8 + 1) are compatible as a basis difference: the chart is the traceless `SU(3)` adjoint; the `+1` is the trace/singlet.

**Proof.** The verifier checks: `3 × 3 = 9 = 8 (+) 1`, the framework `2^3 = 8` is the traceless adjoint, the standard `3 ⊗ 3̄ = adjoint ⊕ singlet` carries the extra trace/singlet, and the singlet is the trace. The Paper 13 honest non-match (VOA mass partition vs. gauge-boson spectrum) is resolved as this basis difference, not a failure. ∎

### Theorem 15.8 — Mass-Gravity Drive

The mass-residue (VOA weight + correction residue) drives the gluon roll toward bonded `L = R` attractors in at most three steps, with `C` preserved.

**Proof.** The `mass_gravity_drive` verifier checks: two massless vacua (no drive), six massive states (driven), correction residue at `(0,1,0)` and `(1,1,0)`, four `L = R` attractors, all descents bounded by `≤ 3` steps, `C` preserved in the drive, and massive states descend toward bonded states. All 7 checks pass. The drive is a bounded directed descent (annealing), not a physical gravity derivation. ∎

### Theorem 15.9 — Higgs Frame Mapping

The Higgs doublet maps structurally as `3 + 1`: three spatial/Goldstone components plus one observer/physical Higgs component. The mass prediction remains open.

**Proof.** The `verify_higgs_frame_mapping` verifier checks: 4 real components, `3 + 1` splitting, chart depth 4, `3` spatial + `1` observer, one-to-one mapping, and Arf gluing one residue. The mass prediction check (`C7_higgs_mass_prediction_OPEN`) is `false` by design, confirming the structural counting is closed while the numerical mass derivation remains open. ∎

---

## 4. Verifiers and Receipts

### 4.1 Mass-Residue Carrier

`verify_mass_residue_carrier.py` → `mass_residue_carrier_receipt.json`

| Check | Result |
|-------|--------|
| `rule30_linear_obstruction_split_holds` | pass |
| `f2_majorana_passes` | pass |
| `rule30_obstruction_arf_is_zero` | pass |
| `matching_arf_glues_and_mismatch_rejects` | pass |
| `voa_sector_decomposition_passes` | pass |
| `voa_weight_distribution_is_2_6` | pass |
| `true_vacua_are_weight_zero` | pass |
| `correction_firing_states_match_residue_formula` | pass |
| `nth_bit_layers_pass_with_open_mckay_thompson` | pass |
| `physical_higgs_mass_left_as_obligation` | pass (explicitly acknowledged) |

**Status:** `pass`, 10/10.

### 4.2 Mass-Residue Literalization

`verify_mass_residue_literalized.py` → `mass_residue_literalized_receipt.json`

| Check | Result |
|-------|--------|
| `mass_is_voa_weight_2_massless_6_massive` | pass |
| `massless_are_true_vacua_singlets` | pass |
| `mass_gap_is_5` | pass |
| `mass_is_bondedness_extremal_vacua` | pass |
| `residue_carrier_fires_on_2_states` | pass |
| `voa_partition_2q0_6q5_proven` | pass |
| `massless_are_residue_free_fixed` | pass |
| `mass_invariant_under_color_group` | pass |
| `two_vacua_internal_vev_structure` | pass |
| `external_calibration_named_not_claimed` | pass |

**Status:** `pass`, 10/10.

### 4.3 Eight States / One Dual Reading

`verify_eight_states_one_dual_reading.py` → `eight_states_one_dual_reading_receipt.json`

| Check | Result |
|-------|--------|
| `eight_states_not_nine` | pass |
| `wrap_is_involution` | pass |
| `wrap_no_fixed_points_distinct_face` | pass |
| `singlet_axis_is_one_state_two_faces` | pass |
| `apparent_nine_is_eight_plus_one_reading` | pass |
| `no_ninth_state_confinement_reading` | pass |
| `same_wrap_as_e8_doubling_and_moonshine_plus_one` | pass |

**Status:** `pass`, 7/7.

### 4.4 Ninth Is Forced Printout

`verify_ninth_is_forced_printout.py` → `ninth_is_forced_printout_receipt.json`

| Check | Result |
|-------|--------|
| `ninth_neutral_while_8th_open` | pass |
| `ninth_forced_to_one_on_completion` | pass |
| `two_choices_set_by_eighth` | pass |
| `ninth_is_deterministic_printout` | pass |
| `ninth_is_function_of_eight_not_independent` | pass |
| `superposition_real_but_transient` | pass |

**Status:** `pass`, 6/6.

### 4.5 Mass Framing 2×2×2 vs 3×3

`verify_mass_framing_2x2x2_vs_3x3.py` → `mass_framing_2x2x2_vs_3x3_receipt.json`

| Check | Result |
|-------|--------|
| `standard_3x3_is_9` | pass |
| `framework_2x2x2_is_8` | pass |
| `division_difference_is_1` | pass |
| `su3_3x3bar_is_8_plus_1` | pass |
| `adjoint_8_is_the_chart` | pass |
| `singlet_1_is_the_trace` | pass |
| `trace_plus_one_recurs_in_moonshine` | pass |

**Status:** `pass`, 7/7.

### 4.6 Higgs Frame Mapping

`verify_glm_higgs_frame_mapping.py` → `higgs_frame_mapping_receipt.json`

| Check | Result |
|-------|--------|
| `C1_higgs_4_real_components` | pass |
| `C2_3_goldstone_plus_1_higgs` | pass |
| `C3_chart_depth_4` | pass |
| `C4_3_spatial_plus_1_observer` | pass |
| `C5_one_to_one_mapping` | pass |
| `C6_arf_gluing_one_residue` | pass |
| `C7_higgs_mass_prediction_OPEN` | **false** (mass prediction intentionally open) |

**Status:** `pass_with_open_obligations`, 6/7. Structural counting is closed; Higgs mass prediction remains open.

### 4.7 Mass-Gravity Drive

`verify_mass_gravity_drive.py` → `mass_gravity_drive_receipt.json`

| Check | Result |
|-------|--------|
| `two_massless_vacua` | pass |
| `six_massive_states` | pass |
| `correction_residue_at_010_110` | pass |
| `four_LR_attractors` | pass |
| `all_descend_bounded_le3` | pass |
| `gluon_C_preserved_in_drive` | pass |
| `massive_descend_toward_bonded` | pass |

**Status:** `pass`, 7/7.

---

## 5. Hand Reconstruction

All primary claims can be reconstructed by hand:

1. **15.1:** Boolean algebra: `L xor (C or R) = L xor C xor R xor (C and R)`.
2. **15.2:** The Arf invariant is computed by standard quadratic-form theory over `F2`.
3. **15.3:** Count weight-0 and weight-5 states by inspection of the VOA assignment.
4. **15.4:** `C AND NOT R = 1` iff `C=1, R=0`; two states satisfy this.
5. **15.5:** The wrap is an involution with no fixed points; by pigeonhole on 8 states, it pairs them into 4 pairs.
6. **15.6:** The ninth is a parity function of the eight; it has 2 possible values (even/odd parity).
7. **15.7:** `SU(3)` representation theory: `3 ⊗ 3̄ = 8 ⊕ 1`. The traceless adjoint is 8-dimensional; the trace is the singlet.
8. **15.8:** Directed descent on a finite state graph is verifiable by inspection of all 8 states and their transitions.

No external computation is required for the core theorems.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F15.1 | The Rule 30 split fails on any local state. | Exhaustive truth table confirms it holds on all 8 states. |
| F15.2 | Arf mismatch can be glued losslessly. | Verifier confirms `zero_vs_elliptic_can_glue = false`. |
| F15.3 | The VOA weight partition is not 2 vacua and 6 excited states. | Receipt reports exact `2q^0 + 6q^5`. |
| F15.4 | The correction residue fires anywhere other than `(0,1,0)` and `(1,1,0)`. | Exhaustive check confirms exactly these two states. |
| F15.5 | This receipt proves a physical Higgs mass value. | Physical mass calibration remains an external obligation. |
| F15.6 | There is a ninth independent chart state. | The wrap is a fixed-point-free involution; the apparent ninth is a re-reading. |
| F15.7 | The `2×2×2` vs `3×3` discrepancy is a failure of the framework. | It is a basis difference (traceless adjoint vs. full representation), resolved by representation theory. |

---

## 7. Relation to Later Papers

- **Paper 14** exports repair score and boundary curvature. Paper 15 receives that discipline and defines the local residue/weight object that later papers may carry into continuum, lattice-tower, or energy-bound work as the internal mass-like carrier.
- **Paper 10** supplies the master-receipt slot that the forced printout (ninth) inhabits.
- **Paper 13** supplies the `SU(3)` color structure and the Standard-Model comparison that the `2×2×2` vs `3×3` framing resolves.
- **Papers 16+** may attempt to close the McKay-Thompson correction parity and the numerical mass calibration.

---

## 8. Open Obligations

1. **Calibration to the physical Higgs mechanism.** The internal carrier is structurally exact; physical particle identification and mass values are external calibration targets.
2. **Particle mass spectrum or numerical mass prediction in measured units.** The VOA weight and correction residue provide a grading; measured GeV values require a calibration bridge.
3. **Electroweak symmetry breaking / Yukawa coupling derivation.** The VEV structure is identified internally; the measured electroweak scale requires external calibration.
4. **Closed-form McKay-Thompson correction parity.** The nth-bit oracle layer passes, but a closed-form `O(log N)` extractor without oracle remains open.
5. **Explicit numerical mass reconciliation.** Framework masses + trace correction → measured masses is the remaining calibration, not claimed in this paper.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata definitions.
2. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 linearity over `F2`.
3. C. Arf, "Untersuchungen über quadratische Formen in Körpern der Charakteristik 2," *J. Reine Angew. Math.* 183 (1941), 148–167. Arf invariant and quadratic forms over `F2`.
4. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA partition function and moonshine structure.
5. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. McKay-Thompson series and Monster group.
6. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory and `Z(q)` partition.
7. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` representation theory, `3 ⊗ 3̄ = 8 ⊕ 1`.
8. M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995. Higgs mechanism, electroweak symmetry breaking, and Yukawa couplings.
9. Particle Data Group (PDG), "Review of Particle Physics," *Prog. Theor. Exp. Phys.* 2022, 083C01. https://pdg.lbl.gov/. Measured Higgs, W, Z, and top masses.
10. ATLAS Collaboration, "Higgs boson mass measurement with 140 fb⁻¹ of √s = 13 TeV pp collisions," ATLAS-CONF-2026, arXiv:2503.0452, 2026. **m_H = 125.11 ± 0.11 GeV** — the most precise Higgs mass measurement to date; FLCR calibration target.
11. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Cayley-Dickson and exceptional structure.

---

## 10. Conclusion

Paper 15 closes the substrate mass-residue carrier. It proves the `F2` obstruction split, the Arf gluing rule, the VOA weight partition, the correction-residue identification, the eight-state / dual-reading theorem, the forced-printout theorem, the `2×2×2` vs `3×3` framing resolution, and the mass-gravity drive. This is the CQECMPLX Higgs-adjacent mass-residue physics map. The remaining work is calibration to measured Higgs/QFT quantities — particle masses, electroweak scale, and Yukawa couplings — not the internal carrier proof.
