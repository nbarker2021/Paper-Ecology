# Paper 14 — GR Boundary-Repair Curvature

**Status.** IPMC for the finite boundary-repair curvature ledger, zero-repair demonstrated rows, positive repair demand on visible open lifts, the Paper 13 `SU(3)` closure as a zero-repair flat reference, and the oloid/Cayley-Dickson curved-carrier receipts. IBN for the curvature = correction identity. ECO for physical GR curvature measurement and Einstein field equation derivation.

---

## Abstract

Paper 14 defines curvature inside CQECMPLX as boundary-repair demand. The closed result is a finite receipt theorem: each transport row has a typed status, demonstrated rows carry zero repair score, non-closed lifts carry positive repair score, and the exact Paper 13 `SU(3)` closure provides a zero-repair reference. The oloid and Cayley-Dickson modules supply a curved carrier with a verified repeating `1,8,8,1` normal-form pattern and three-dyad involution coherence. The paper also records the substrate identity: curvature = correction, with Rule 90 as the flat geodesic and Rule 30 curving exactly at the correction sites.

This is not a derivation of General Relativity. Riemann curvature, Ricci curvature, Einstein tensors, stress-energy measurement, and gravitational phenomena remain external or later-theory obligations. The paper provides the repair-accounting substrate that such a bridge would need to preserve.

**Keywords:** boundary repair, repair score, CQECMPLX curvature, transport ledger, oloid carrier, Cayley-Dickson normal form, correction = curvature.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 14.1 | The transport ledger is a finite typed repair ledger whose rows carry explicit proof boundaries. | [D] | `boundary_repair_curvature_receipt.json`: 9/9 |
| 14.2 | Demonstrated rows have repair score `0`. | [D] | Same receipt |
| 14.3 | Open or lifted rows have positive repair score. | [D] | Same receipt |
| 14.4 | Exact `n=3` `SU(3)` closure from Paper 13 is a zero-repair reference (residual squared `0`). | [D] | Same receipt; Paper 13 receipt |
| 14.5 | Cayley-Dickson/Oloid normal form verifies the repeating `1,8,8,1` pattern. | [D] | Same receipt |
| 14.6 | Dual-path oloid verifies three-dyad involution coherence. | [D] | Same receipt |
| 14.7 | Curvature = correction: Rule 90 is the flat geodesic; Rule 30 curves at correction sites. | [I] | `curvature_is_correction_receipt.json`: 5/5 |
| 14.8 | Integrated curvature over the 8-state chart equals `2` (the two correction-firing states). | [I] | Same receipt |
| 14.9 | General Relativity curvature is a candidate interpretation of repair demand, not a closed theorem. | [X] | Explicit scope boundary |
| 14.10 | Riemann/Ricci/Einstein tensor derivation remains an external obligation. | [X] | Explicit scope boundary |
| 14.11 | nth-bit extraction from the oloid normal form alone remains open. | [X] | Explicit honesty boundary |

---

## 2. Definitions

**Repair demand.** Unresolved transport residue preserved as an obligation instead of erased.

**Repair score.** A finite ledger scalar assigned by classification:

| Classification | Score |
|----------------|-------|
| `demonstrated` | 0 |
| `bounded_local` | 1 |
| `bounded_external` | 2 |
| `registered_landing_forms` | 3 |
| `open` | 4 |

**Flat reference.** A closed transport whose exact residual is `0`.

**Curved carrier.** A carrier that transports a state through a non-flat or multi-dyad route while preserving a receipt and an honesty boundary.

---

## 3. Theorems and Proofs

### Theorem 14.1 — Repair-Ledger Curvature

For each promoted transport row, `curvature_CQE(route) = repair_score(route.classification)` is a well-defined finite substrate quantity. It is zero exactly on demonstrated rows and positive on visible non-closed lifts.

**Proof.** The transport ledger contains four rows with explicit classifications. The verifier assigns repair score by the classification table above. For the current ledger:

| Row ID | Classification | Score |
|--------|---------------|-------|
| `LCR_TO_D4_AXIS_SHEET` | demonstrated | 0 |
| `D4_TO_J3O_DIAGONAL_CARRIER` | demonstrated | 0 |
| `J3O_TO_G2_F4_T5A_ROUTE` | bounded_local | 1 |
| `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` | registered_landing_forms | 3 |

The verifier checks: all rows have boundaries, demonstrated rows have score 0, and non-demonstrated rows have positive score. All checks pass. ∎

### Theorem 14.2 — Zero-Repair Flat Reference

The exact `n=3` shell-2 `SU(3)` closure from Paper 13 is a zero-repair reference because its rational residual squared is `0`.

**Proof.** Paper 13 (Theorem 13.4) proves that the `n=3` shell-2 conditional matrix decomposes over the `S_3` permutation matrices with exact rational coefficients and residual squared exactly `0`. A zero residual requires no repair at that closure layer. Therefore its repair score is `0`. The verifier checks this explicitly. ∎

### Theorem 14.3 — Curved Carrier Receipt

The Cayley-Dickson/Oloid verifier establishes the tested `1,8,8,1` normal-form pattern, and the dual-path oloid verifier establishes three-dyad involution coherence. These are carrier receipts, not cold nth-bit extraction theorems.

**Proof.** The oloid normal-form verifier checks the repeating pattern `1, 8, 8, 1` across the tested range. The generated form carries an honesty string: "normal_form_only: generates podal/antipodal Cayley-Dickson sheet placement; does not by itself prove nth-bit extraction." The dual-path oloid verifier checks: triple involution podal matches, triple involution antipodal matches, triple involution shared matches, and dyad level coherence at levels 0, 1, and 2. All checks pass. ∎

### Theorem 14.4 — Curvature = Correction

Rule 90 is the flat geodesic (no correction, no curvature). Rule 30 curves exactly at the correction-firing sites `{(0,1,0), (1,1,0)}`. The integrated curvature over the 8-state chart equals `2`.

**Proof.** From Paper 2 (Correction Surface Decomposition), Rule 30 = Rule 90 XOR correction, where correction fires exactly on the two states `(0,1,0)` and `(1,1,0)`. On the remaining six states, correction is `0` and Rule 30 coincides with Rule 90. Therefore the curvature (deviation from flat) is concentrated at exactly two sites. The integrated curvature is the count of firing sites: `2`. The verifier checks: `curvature_equals_correction`, `flat_geodesic_is_rule90_no_C`, `curvature_at_correction_firing_pair`, `integrated_curvature_is_2`, and `curved_sites_are_repair_sites`. All 5 checks pass. ∎

### Theorem 14.5 — GR Scope Boundary

No receipt in this paper constructs Riemann, Ricci, Einstein, or stress-energy tensors. Any statement equating the repair ledger with physical GR curvature is a bridge obligation until supplied with a separate derivation and calibration receipt.

**Proof.** The verifier explicitly checks `gr_physics_left_as_obligation = true`. The receipt rejects the claim that Einstein field equations are verified. This is a scope boundary, not a mathematical theorem, but it is enforced by the verifier architecture. ∎

## Fano Structure Constants and su(3) Commutator Witness

Paper 14 defines curvature as boundary-repair demand. The Fano structure constants provide candidate color-transition data, but any physical gauge identification requires a commutator-preserving witness.

**Definition 14.6 (Fano structure constants as candidate color data).** The oriented Fano three-form φ = Σ ε_{ijk} e_i ∧ e_j ∧ e_k defines structure constants ε_{ijk} that are candidate color-transition data. For each Fano line {i,j,k}, the triple (e_i, e_j, e_k) forms a quaternionic associative subalgebra.

**Definition 14.7 (su(3) commutator witness requirement).** The missing witness for the "eight gluons" statement is a commutator-preserving linear map:
Φ_g: T_LCR → su(3),

such that for all a, b in the LCR transition algebra T_LCR:
[Φ_g(a), Φ_g(b)] = f_{ab}^c Φ_g(c),

where f_{ab}^c are the structure constants of su(3).

**Theorem 14.6 (Commutator witness is required).** Without a commutator-preserving map Φ_g: T_LCR → su(3), the identification of the eight LCR chart operations with gluon generators, or of the eight octonionic directions with color adjoint states, remains structurally suggestive but not derived.

*Proof.* The standard gluon sector is su(3) ≅ End₀(ℂ³), the traceless endomorphisms of color space. A count of eight directions is insufficient to establish an isomorphism with the eight-dimensional su(3) adjoint representation. The required witness is a Lie-algebra homomorphism from the LCR transition algebra to su(3) that preserves brackets. No such map is constructed in this paper. ∎

**Theorem 14.7 (Standard Model bridge routes).** Two precise routes from octonions to SU(3) exist in the literature:

- Route 1: SU(3) ⊂ G₂. Choose a preferred unit imaginary u ∈ Im𝕆. Its stabilizer in G₂ = Aut(𝕆) is SU(3), giving 𝕆 ≅ ℂ ⊕ ℂ³.
- Route 2: SU(3) × SU(3) / ℤ₃ ⊂ F₄. This gives a subgroup chain F₄ ⊃ ℤ₃ × SU(3) × SU(3) ⊃ SU(3) × SU(2) × U(1).

Both routes are mathematically real, but neither automatically derives electroweak SU(2) × U(1), chirality, or full Standard Model content. Those require additional representation and dynamics problems.

*Proof.* Route 1 is standard: G₂ acts transitively on the unit imaginary octonions, and the stabilizer of any one is SU(3). Route 2 follows from the known maximal subgroup structure of F₄. The additional requirements for electroweak and full SM content are documented in the literature and are explicitly open in this paper. ∎

**Remark (interpretive boundary).** The Fano structure constants are closed algebraic data. The su(3) commutator witness is an open obligation. Any paper that claims the eight LCR states are quark colors, or the eight directions are gluon generators, must either construct Φ_g or demote the claim to interpretive bridge status.

---

## 4. Verifiers and Receipts

### 4.1 Boundary-Repair Curvature

`verify_boundary_repair_curvature.py` → `boundary_repair_curvature_receipt.json`

| Check | Result |
|-------|--------|
| `transport_ledger_passes_with_open_lifts` | pass |
| `transport_rows_have_boundaries` | pass |
| `demonstrated_rows_have_zero_repair` | pass |
| `open_lifts_have_nonzero_repair` | pass |
| `flat_su3_reference_has_zero_residual` | pass |
| `oloid_normal_form_passes` | pass |
| `oloid_honesty_boundary_present` | pass |
| `dual_path_oloid_passes` | pass |
| `gr_physics_left_as_obligation` | pass (explicitly acknowledged) |

**Status:** `pass`, 9/9.

### 4.2 Curvature = Correction

`verify_curvature_is_correction.py` → `curvature_is_correction_receipt.json`

| Check | Result |
|-------|--------|
| `curvature_equals_correction` | pass |
| `flat_geodesic_is_rule90_no_C` | pass |
| `curvature_at_correction_firing_pair` | pass |
| `integrated_curvature_is_2` | pass |
| `curved_sites_are_repair_sites` | pass |

**Status:** `pass`, 5/5.

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **14.1:** The four transport rows are classified by inspection; scores are assigned from the classification table.
2. **14.2:** Demonstrated rows (finite codec, diagonal carrier) have score 0 by definition.
3. **14.3:** The bounded route (score 1) and the landing-forms row (score 3) have positive scores by definition.
4. **14.4:** Paper 13's residual is 0; therefore its repair score is 0.
5. **14.5:** The oloid pattern is verified by direct enumeration of the normal form.
6. **14.7:** Rule 30 = Rule 90 XOR correction (Paper 2). Correction fires on exactly 2 states. Therefore curvature is concentrated at 2 sites, integrated curvature = 2.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F14.1 | A demonstrated transport row has nonzero repair score. | Contradicts the ledger definition. |
| F14.2 | An open lift can be treated as zero curvature. | Non-closed rows have positive repair score. |
| F14.3 | Einstein field equations are verified by this receipt. | No Riemann/Ricci/Einstein tensors are constructed. |
| F14.4 | The oloid normal form proves nth-bit extraction by itself. | Honesty boundary explicitly states it does not. |
| F14.5 | The curvature = correction identity proves physical GR curvature. | It is an internal substrate identity only. |

---

## 7. Relation to Later Papers

- **Paper 13** supplies the exact zero-repair flat reference (`SU(3)` closure with residual 0).
- **Paper 14** defines how visible residue becomes repair magnitude, and records the curvature = correction identity.
- **Paper 15** may use this repair magnitude as mass-residue input, but must preserve the open physical boundary.
- **Papers 16+** may attempt to bridge the repair ledger to Riemannian geometry, but must supply separate derivation and calibration receipts.
- **Paper 3** closes the Fano structure constants and the su(3) commutator witness requirement. Any claim that the eight LCR states are quark colors or the eight directions are gluon generators must either construct Φ_g or route to an open obligation.

---

## 8. Open Obligations

1. **Riemann/Ricci/Einstein tensor derivation.** The repair ledger is a substrate accounting quantity, not a physical curvature tensor.
2. **Calibrated gravitational measurement.** No measured gravitational effect is claimed or derived.
3. **nth-bit extraction from the oloid normal form alone.** The normal form is a carrier pattern, not a cold-start extractor.
4. **Physical GR curvature interpretation.** Any bridge from repair score to spacetime curvature requires a separate derivation and external calibration.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and Rule 90 definitions.
2. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 linearity.
3. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. Exceptional group context.
4. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Cayley-Dickson and octonion structure.
5. R. M. Wald, *General Relativity*, University of Chicago Press, 1984. Standard GR reference for curvature, Riemann, and Einstein tensors.
6. S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of Space-Time*, Cambridge University Press, 1973. Singularity theorems and curvature.
7. C. W. Misner, K. S. Thorne, J. A. Wheeler, *Gravitation*, W. H. Freeman, 1973. Classic GR text for curvature and field equations.
8. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` background.
9. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)`, `SU(2)`, `U(1)` group structure.
10. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and exceptional structure.

---

## 10. Data vs Interpretation

### Data-backed (D)

- The transport ledger with typed repair scores is a finite exact check. (D — `boundary_repair_curvature_receipt.json`)
- The demonstrated rows have repair score 0; non-closed rows have positive scores. (D — `boundary_repair_curvature_receipt.json`)
- The Paper 13 SU(3) closure has residual squared 0, giving a zero-repair flat reference. (D — Paper 13 receipt)
- The oloid normal form verifies the repeating `1,8,8,1` pattern. (D — `boundary_repair_curvature_receipt.json`)
- The dual-path oloid verifies three-dyad involution coherence. (D — `boundary_repair_curvature_receipt.json`)

### Interpretation (I)

- The curvature = correction identity (Rule 90 as flat geodesic, Rule 30 curving at correction sites) is the author's structural reading. (I — the underlying finite checks are (D).)
- The integrated curvature over the 8-state chart equals 2, which is a discrete Gauss-Bonnet-style count. (I — the count of correction-firing states is (D), but the "curvature" framing is interpretive.)
- Any bridge from repair score to physical GR curvature is an interpretive candidate, not a closed theorem. (I — explicitly scoped as open.)

### Fabrication (X)

- None in this paper. The finite substrate claims are (D) verified. The physical GR interpretation is honestly marked as (X) open.

---

## 11. Conclusion

Paper 14 closes the substrate theorem for boundary-repair curvature: repair is typed, scored, receipt-bearing, and carried on verified non-flat support. The curvature = correction identity gives a discrete Gauss-Bonnet-style count: integrated curvature over the 8-state chart equals 2, the number of correction-firing states. The paper does not close General Relativity. The result is useful because it makes the curvature analogy testable instead of rhetorical, and it provides the repair-accounting substrate that any later physical bridge would need to preserve.


---

## Claim Ledger (from mapped_file_claims_report.md)

| Claim ID | Literal Claim | D/I/X | Source File |
|----------|---------------|-------|-------------|
| 14.1 | 137 continuation surfaces include Paper 014, E8 roots, SM bosons, Fibonacci, triality | D | CAM_ROUTED_NETWORK_MAP.md |
| 14.2 | Riemann continuation surfaces include Paper 14, Riemann tensor, boundary-repair operator, torsion | D | CAM_ROUTED_NETWORK_MAP.md |
| 14.3 | T_D12_CHAIN: 17 non-trivial idempotent sequences (R30 Paper 14) | D | CAM_ROUTED_NETWORK_MAP.md |
