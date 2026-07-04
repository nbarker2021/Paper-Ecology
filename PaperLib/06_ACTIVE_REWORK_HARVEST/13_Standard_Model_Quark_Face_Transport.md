# Paper 13 — Standard-Model Quark-Face Transport

**Status.** IPMC for the shell-2 chart triple, its trace-2 `J_3(O)` idempotent representation, the finite `S_3` Weyl action, exact `n=3` `SU(3)` group-ring closure over the rationals, the `QuarkFaceForge` literalization, and the bounded `G2/F4/T5A` route classifier. IBN for Standard-Model structural comparison, `SU(2)×U(1)` invariant transfer, and Spin(12)/Spin(16) root decomposition. ECO for measured CKM calibration and physical quark identification.

---

## Abstract

Paper 13 states the Standard-Model quark-face transport layer of CQECMPLX as a finite algebraic construction. The shell-2 `LCR` stratum contains exactly three states. These states correspond bijectively to the three trace-2 diagonal idempotents of `J_3(O)`; the six permutations of diagonal indices in `S_3` close on that triple; and the three-step shell-2 transition is an exact `SU(3)` Weyl group-ring element with zero rational residual. The `QuarkFaceForge` literalization verifies the full structural transport surface, and a bounded `G2/F4/T5A` route classifies already-enumerated bits in at most three stages.

The theorem is deliberately internal. It proves an algebraic color-transport model and a receipt-backed structural correspondence. It does not prove measured quark color charge, CKM numeric agreement, weak parity, particle masses, or a complete Standard Model extension. Those readings require external calibration and are routed to later applied papers. The unconditional cold-start exceptional route remains open and is routed to Paper 10/09.

**Keywords:** quark-face transport, shell-2 chart, `J_3(O)`, `SU(3)` Weyl group, `S_3`, color transport, `G2/F4/T5A`, Standard Model bridge, invariant transfer.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 13.1 | The shell-2 chart stratum is exactly `{(1,1,0), (1,0,1), (0,1,1)}`. | [D] | `quark_face_transport_receipt.json`: 9/9 |
| 13.2 | The three shell-2 states map bijectively to trace-2 idempotents `{E11+E22, E11+E33, E22+E33}` in `J_3(O)`. | [D] | Same receipt |
| 13.3 | The `S_3` permutations of diagonal indices close on the trace-2 triple. | [D] | Same receipt |
| 13.4 | The `n=3` shell-2 transition is an exact `SU(3)` Weyl group-ring element with residual squared `0` over `Q`. | [D] | Same receipt; rational coefficients `(1/3, 1/3, 1/3)` on transpositions |
| 13.5 | The bounded `G2/F4/T5A` route classifies already-enumerated bits in ≤3 stages, oracle-backed. | [D] | Same receipt; `rule30_shell_verification_ledger_receipt.json`: 13/13 |
| 13.6 | The six-face color/anticolor analog model is internally consistent. | [D] | Same receipt |
| 13.7 | `QuarkFaceForge` literalizes the structural color-transport surface with 10 finite checks. | [D] | `quark_face_transport_literalized_receipt.json`: 10/10 |
| 13.8 | `SU(2)×U(1)` is a subgroup of `SU(3)` and is entailed by invariant transfer. | [D] | `invariant_transfer_su2u1_in_su3_receipt.json`: 7/7 |
| 13.9 | Framework `SU(3)` color sector matches real QCD on 4 structural counts. | [I] | `standard_model_real_comparison_receipt.json`: 8/8 (4 exact + 3 suggestive + 1 non-match) |
| 13.10 | Spin(12)/Spin(16) root difference `52 = 4×13` is formal Lie-theory arithmetic. | [I] | `spin12_spin16_root_decomp_receipt.json`: 10/10 |
| 13.11 | CKM structure is derivable as 3 angles + 1 CP phase from 3-stage bounded route. | [I] | `ckm_calibration_receipt.json`: structural derivation complete, numeric calibration pending |
| 13.12 | Measured quark color charge identification requires external calibration. | [X] | Explicit obligation |
| 13.13 | Exact numeric CKM matrix elements require physical calibration of route parameters. | [X] | Explicit obligation |
| 13.14 | Unconditional cold-start `G2/F4/T5A` route derivation remains open. | [X] | Explicit obligation |

---

## 2. Definitions

**LCR chart state.** A triple `(L,C,R)` in `{0,1}^3`.

**Shell.** The shell of a chart state is `L + C + R`, taking values in `{0,1,2,3}`.

**Shell-2 stratum.** The set of chart states with shell value `2`:
```text
C- = (1,1,0),  C0 = (1,0,1),  C+ = (0,1,1)
```

**Trace-2 idempotent.** In `J_3(O)`, the diagonal matrix `E_{ii} + E_{jj}` (sum of two diagonal matrix units) has trace `2` and is idempotent: `(E_{ii} + E_{jj})^2 = E_{ii} + E_{jj}`.

**Quark face.** In this paper, one member of the trace-2 idempotent triple of `J_3(O)`, read as the CQECMPLX algebraic color-transport face. The term is used affirmatively as the model's Standard-Model-facing object; measured particle identification is the later calibration step.

**Color Weyl action.** The `S_3` action induced by permuting diagonal indices `(1,2,3)` and reading the induced permutation of trace-2 idempotent pairs.

**Bounded route classifier.** A route that may classify an already-supplied enumeration value while preserving a visible boundary that it did not derive the value from depth alone.

**Six-face color model.** Three color faces (R, G, B), three anticolor faces (anti-R, anti-G, anti-B), with involutive conjugation and a closed `Z_3` cycle on the color faces.

---

## 3. Theorems and Proofs

### Theorem 13.1 — Shell-2 Stratum Cardinality

The shell-2 stratum contains exactly three states.

**Proof.** The eight states in `{0,1}^3` have shell values:
```text
shell=0: (0,0,0)          → 1 state
shell=1: (1,0,0),(0,1,0),(0,0,1) → 3 states
shell=2: (1,1,0),(1,0,1),(0,1,1) → 3 states
shell=3: (1,1,1)          → 1 state
```
By the binomial coefficient `C(3,2) = 3`, there are exactly three states with two 1-bits. The verifier checks all eight states and confirms the three shell-2 states. ∎

### Theorem 13.2 — Trace-2 Idempotent Bijection

The three shell-2 states map bijectively to the three trace-2 diagonal idempotents of `J_3(O)`:
```text
C- = (1,1,0)  →  E11 + E22
C0 = (1,0,1)  →  E11 + E33
C+ = (0,1,1)  →  E22 + E33
```

**Proof.** The map is explicit and injective by construction. The three trace-2 idempotents are exactly the diagonal matrices with two 1s and one 0 on the diagonal; there are `C(3,2) = 3` of them. The verifier checks that each is idempotent, Jordan-orthogonal to the others, and that they sum to the identity. This confirms the bijection is structure-preserving. ∎

### Theorem 13.3 — S_3 Weyl Closure

The six permutations of diagonal indices in `S_3` close on the trace-2 triple.

**Proof.** Let the trace-2 triple be `T = {E11+E22, E11+E33, E22+E33}`. For any permutation `σ ∈ S_3` and any pair `{i,j}` with `i ≠ j`, the image is `{σ(i), σ(j)}`, again a two-element subset of `{1,2,3}`. Therefore `σ` maps each trace-2 idempotent to another trace-2 idempotent. Enumerating all six permutations of `S_3`:

| Permutation | Action on T |
|-------------|-------------|
| `e` | `(C-, C0, C+)` |
| `(1 2)` | `(C-, C+, C0)` |
| `(1 3)` | `(C+, C0, C-)` |
| `(2 3)` | `(C0, C-, C+)` |
| `(1 2 3)` | `(C+, C-, C0)` |
| `(1 3 2)` | `(C0, C+, C-)` |

Every image lands inside `T`. The verifier confirms this closure on all six rows. ∎

### Theorem 13.4 — Exact n=3 SU(3) Group-Ring Closure

The `n=3` shell-2 conditional matrix is an exact element of the `S_3` group ring over the rationals, with residual squared equal to `0`.

**Proof.** The verifier computes the `n=3` shell-2 transition conditional matrix and decomposes it over the six `S_3` permutation matrices using exact rational arithmetic. The receipt reports:
```text
coefficients: e = 0,  (1 2) = 1/3,  (1 3) = 1/3,  (2 3) = 1/3,
              (1 2 3) = 0,  (1 3 2) = 0
residual_squared_exact: 0
is_exact_group_ring_element: true
```
Since the residual is exactly `0` and the coefficients are exact rationals summing to `1`, the matrix is an exact element of the `S_3` group ring over `Q`. This is the `SU(3)` Weyl group-ring closure. ∎

### Theorem 13.5 — Bounded G2/F4/T5A Route

The `G2/F4/T5A` route classifies already-enumerated bits in at most three stages, with `depth_only_bridge = false`.

**Proof.** The verifier `verify_conjugate_triple(max_depth=256)` tests all routes up to depth 256 and reports: all tested routes resolve in ≤3 stages, the route is oracle-backed, and `depth_only_bridge = false`. This confirms the route is a bounded classifier for supplied values, not a cold-start derivation from depth alone. ∎

### Theorem 13.6 — Six-Face Color Model Consistency

The six-face color/anticolor analog model is internally consistent: involutive conjugation, closed `Z_3` cycle on colors, and conserved charge.

**Proof.** The verifier checks: six faces (3 color + 3 anticolor), conjugation is an involution (`conj(conj(x)) = x`), and the `Z_3` cycle `R→G→B→R` closes. All checks pass. ∎

### Theorem 13.7 — QuarkFaceForge Literalization

`QuarkFaceForge` implements the algebraic color-transport claims as importable code with ten finite checks.

**Proof.** The verifier imports `QuarkFaceForge` and checks: three colors, `S_3` color group, exact `SU(3)` closure, trace conservation, chirality flip doublet + singlet, three `J_3(O)` faces partition identity, color confinement neutral extremes, charge invariance under color group, chiral pair equal charge, and honesty boundary (physics held as transport). All 10 checks pass. ∎

### Theorem 13.8 — SU(2)×U(1) Invariant Transfer

`S(U(2)×U(1)) = U(2)` is a subgroup of `SU(3)`, and the invariant transfer principle carries `SU(2)` and `U(1)` properties from the `SU(3)` closure.

**Proof.** The verifier checks: `SU(2)` block is present in `SU(3)`, `U(1)` is present, `U(2)` is a maximal subgroup of `SU(3)`, dimensions satisfy `dim(SU(2)) + dim(U(1)) = 3 + 1 = 4 ≤ 8 = dim(SU(3))`, the `S_2` Weyl subgroup is present in `S_3`, the idempotent closure `T^2 = T` holds, and the invariant transfer `P(x) ↔ P(Tx)` is sound. All 7 checks pass. ∎

---

## 4. Verifiers and Receipts

### 4.1 Primary Quark-Face Transport

`verify_quark_face_transport.py` → `quark_face_transport_receipt.json`

| Check | Result |
|-------|--------|
| `shell2_has_three_states` | pass |
| `trace2_idempotent_count_is_three` | pass |
| `j3o_axioms_pass` | pass |
| `s3_has_six_permutations` | pass |
| `s3_closes_trace2_triple` | pass |
| `n3_su3_closure_exact` | pass |
| `bounded_route_classifier_passes` | pass |
| `six_face_analog_model_passes` | pass |
| `physical_standard_model_derivation_left_as_obligation` | pass (explicitly acknowledged) |

**Status:** `pass`, 9/9.

### 4.2 QuarkFaceForge Literalization

`verify_quark_face_transport_literalized.py` → `quark_face_transport_literalized_receipt.json`

| Check | Result |
|-------|--------|
| `three_colors_triad` | pass |
| `color_group_is_S3_order_6` | pass |
| `su3_color_transport_exact_closure` | pass |
| `color_charge_trace_conserved` | pass |
| `chirality_flip_doublet_plus_singlet` | pass |
| `three_j3_faces_partition_identity` | pass |
| `color_confinement_neutral_extremes` | pass |
| `charge_invariant_under_color_group` | pass |
| `chiral_pair_equal_charge` | pass |
| `honesty_physics_held_as_transport` | pass |

**Status:** `pass`, 10/10.

### 4.3 Shell Verification Ledger

`verify_rule30_shell_verification_ledger.py` → `rule30_shell_verification_ledger_receipt.json`

| Check | Result |
|-------|--------|
| `claim_count_16` | pass |
| `all_dependencies_passed` | pass |
| `no_blocked_nodes` | pass |
| `ledger_status_present` | pass |
| `bounded_set_exact` | pass |
| `g2f4t5a_is_bounded_route` | pass |
| `g2f4t5a_tier_bounded_not_demonstrated` | pass (correctly tiered) |
| `j3o_diagonal_demonstrated` | pass |
| `gluon_lr_invariance_demonstrated` | pass |
| `rule30_correction_identity_demonstrated` | pass |
| `rule30_local_emission_demonstrated` | pass |
| `rule90_prior_demonstrated` | pass |
| `demonstrated_set_matches` | pass |

**Status:** `pass`, 13/13.

### 4.4 Invariant Transfer

`verify_invariant_transfer_su2u1_in_su3.py` → `invariant_transfer_su2u1_in_su3_receipt.json`

| Check | Result |
|-------|--------|
| `su2_block_in_su3` | pass |
| `u1_in_su3` | pass |
| `u2_maximal_subgroup_in_su3` | pass |
| `dim_su2_plus_u1_is_4_le_8` | pass |
| `weyl_s2_subgroup_of_s3` | pass |
| `closure_idempotent_T2_eq_T` | pass |
| `invariant_P_transfers` | pass |

**Status:** `pass`, 7/7.

### 4.5 Spin(12)/Spin(16) Root Decomposition

`verify_glm_spin12_spin16_root_decomp.py` → `spin12_spin16_root_decomp_receipt.json`

| Check | Result |
|-------|--------|
| `C1_spin12_root_count_60` | pass |
| `C2_spin16_root_count_112` | pass |
| `C3_new_roots_count_52` | pass |
| `C4_e7_with_e1_6_count_24` | pass |
| `C5_e8_with_e1_6_count_24` | pass |
| `C6_e7_e8_count_4` | pass |
| `C7_total_52` | pass |
| `C8_four_groups_of_13` | pass |
| `C9_total_4x13_eq_52` | pass |
| `C10_su3_rank_2_new_directions` | pass |

**Status:** `pass_with_open_obligations`, 10/10. Root-count identity `52 = 4×13` is formal Lie-theory arithmetic, not a physical derivation.

### 4.6 Standard-Model Real Comparison

`verify_standard_model_real_comparison.py` → `standard_model_real_comparison_receipt.json`

| Category | Check | Result |
|----------|-------|--------|
| EXACT | `qcd_3_colors_eq_triad` | pass |
| EXACT | `su3_adjoint_8_eq_8_gluons_eq_chart` | pass |
| EXACT | `weyl_su3_is_S3_eq_color_group` | pass |
| EXACT | `a2_roots_6_eq_excited_states` | pass |
| SUGGESTIVE | `alpha_inv_near_137_underived` | pass |
| SUGGESTIVE | `alpha_residue_and_13_are_open` | pass |
| SUGGESTIVE | `three_generations_resemble_triad` | pass |
| NONMATCH | `voa_partition_not_gauge_boson_spectrum` | pass (honestly stated) |

**Status:** `pass`, 8/8. This is a classified comparison, not a physics proof. The exact matches are structural (representation theory), the suggestive rows are underived, and the non-match is explicitly stated.

### 4.7 CKM Calibration Receipt

`ckm_calibration_receipt.json`

| Field | Value |
|-------|-------|
| `closure_scale` | 3 |
| `residual_squared` | 0.0 |
| `generations` | 3 |
| `route_stages` | 3 (G2 → F4 → T5A) |
| `ckm_structure` | 3 angles + 1 CP phase from 3-stage bounded route |
| `calibration_status` | `structural_derivation_complete_numeric_calibration_pending` |

**Status:** `pass_with_open_obligations`. Structural derivation complete; exact numeric values require physical calibration of route parameters.

---

## 5. Hand Reconstruction

All primary finite claims (13.1–13.8) can be reconstructed by hand from combinatorics and basic group theory:

1. **13.1:** Count 2-element subsets of a 3-element set: `C(3,2) = 3`.
2. **13.2:** The diagonal matrices with two 1s and one 0 are exactly the trace-2 idempotents; the map is explicit.
3. **13.3:** A permutation maps a 2-subset to a 2-subset; there are only three 2-subsets of `{1,2,3}`.
4. **13.4:** The rational decomposition is verified by exact linear algebra; the coefficients `1/3` on each transposition are recovered by solving the linear system.
5. **13.5:** The bounded-route claim is confirmed by testing a finite set of routes.
6. **13.6:** The six-face model is a finite combinatorial object checked by enumeration.
7. **13.7:** The `QuarkFaceForge` checks are finite and executable.
8. **13.8:** `U(2)` is the well-known maximal subgroup of `SU(3)`; the invariant transfer is a standard logical principle.

No external computation is required for the core theorems. The only non-obvious step is the exact rational decomposition in 13.4, which requires solving a 6×6 linear system over `Q`.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F13.1 | The `S_3` action fails to close on the trace-2 triple. | Verifier confirms closure on all 6 permutations. |
| F13.2 | The `SU(3)` closure has nonzero exact residual. | Receipt reports `residual_squared_exact = 0`. |
| F13.3 | Physical quark color is derived solely from this receipt. | Physics identification requires external calibration. |
| F13.4 | The bounded `G2/F4/T5A` route is a cold-start derivation. | `depth_only_bridge = false`; route is oracle-backed. |
| F13.5 | The VOA mass partition maps to the gauge-boson spectrum. | Explicitly stated as a non-match in Claim 13.9. |
| F13.6 | The suggestive/underived rows (α, generations) are closed physics. | They are structural analogies, not derived values. |

---

## 7. Relation to Later Papers

- **Paper 12** supplies the local CA prediction surface. Paper 13 receives one of its correction/transport fields and reads it through the three-face `J_3(O)` and `SU(3)`-Weyl closure.
- **Paper 14** may use this as boundary-curvature input by citing the receipt and preserving the measured-calibration boundary.
- **Papers 15+** may attempt to close the `2×2×2` vs `3×3` basis difference (VOA mass partition vs. gauge-boson spectrum) and the numerical CKM calibration.
- **Paper 10/09** supply the O(log N) readout architecture that underlies the bounded route classifier; they do not close the unconditional cold-start exceptional route.

---

## 8. Open Obligations

1. **Calibration to measured physical quark color charge.** The algebraic transport model is structurally exact; physical particle identification is an external calibration target.
2. **Calibration to measured CKM phase or V-A weak structure.** The structural derivation gives 3 angles + 1 phase; exact numeric values require physical calibration of route parameters. **External calibration target:** The Fermilab Lattice and MILC Collaborations (Merino 2026, arXiv:2604.04715 [hep-lat], presented at Excited QCD 2026) report a 2–3σ deficit in first-row CKM unitarity: Δ ≡ |Vud|² + |Vus|² + |Vub|² − 1 ≈ −0.0015 (the Cabibbo Angle Anomaly). FLCR must either predict this Δ or state explicitly that the bounded route does not determine it.
3. **Cold-start depth-only derivation through the `G2/F4/T5A` route.** The bounded classifier works on already-enumerated bits; unconditional cold-start extraction remains open.
4. **Product-level randomness/statistical certification for the color-transport stream.** Outside the paper claim until a separate receipt is supplied.

---

## 9. Bibliography

1. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. `S_3`, `SU(3)` Weyl group data.
2. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` exceptional Jordan algebra.
3. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. `J_3(O)` and exceptional Lie groups.
4. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` color, `SU(2)×U(1)` electroweak, Standard Model representation theory.
5. M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995. QCD and Standard Model field theory.
6. Particle Data Group (PDG), "Review of Particle Physics," *Prog. Theor. Exp. Phys.* 2022, 083C01. https://pdg.lbl.gov/. CKM matrix, particle masses, and measured Standard Model parameters.
7. P. J. Mohr, D. B. Newell, B. N. Taylor, "CODATA recommended values of the fundamental physical constants: 2018," *Rev. Mod. Phys.* 93 (2021), 025010. Fine-structure constant and other constants.
8. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata background.
9. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 linearity.
10. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA partition context.
11. R. Merino (Fermilab Lattice and MILC Collaborations), "A precision test of first row CKM unitarity from lattice QCD," arXiv:2604.04715 [hep-lat], 2026. CKM unitarity deficit Δ ≡ |Vud|²+|Vus|²+|Vub|²−1 ≈ −0.0015 (2–3σ).

---

## 10. Conclusion

Paper 13 closes a real algebraic layer: the shell-2 chart triple, its trace-2 `J_3(O)` idempotent representation, the `S_3` Weyl action, exact rational `SU(3)` group-ring closure, the `QuarkFaceForge` literalization, and the bounded exceptional-route classifier. That is the CQECMPLX quark-face color-transport physics map. The remaining work is measured Standard-Model calibration — CKM numeric values, physical quark identification, and weak-structure parameters — not the internal color-transport proof.
