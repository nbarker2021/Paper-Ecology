# Paper 19 — Observer Face-Selection

**Status.** IPMC for the finite observer face-selection mechanism: four selectable frame faces, three retained latent faces per selection, gluon `C` invariance under antipodal reversal, the static `Z4` face template, and the bounded observer-route evidence after all eight chart states activate. ECO for SPINOR signature observation, consciousness/measurement-collapse interpretation, and global physical observer theorem.

---

## Abstract

Paper 19 defines observation as selecting one face of a local registered state while retaining the unselected faces as obligations. The closed result is finite: four frame faces are available, selecting one retains three latent faces, the gluon coordinate `C` is invariant under `L ↔ R` antipodal reversal over all eight chart states, and the static `Z4` face template splits as two fixed points plus six period-4 states. Bounded Monster-D4 route evidence supports the observer-face reading after all eight chart states activate, but it remains labeled `pass_with_open_gaps`.

This paper does not prove consciousness, physical measurement collapse, a completed SPINOR signature, or a global observer theorem.

**Keywords:** observer, face selection, latent face, gluon invariance, antipodal reversal, `Z4` template, SPINOR.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 19.1 | The observer has four selectable frame faces: `C-centroid`, `R-centroid`, `C-flipped`, `L-centroid`. | [D] | `observer_face_selection_receipt.json`: 7/7 |
| 19.2 | Selecting one face retains exactly three latent faces. | [D] | Same receipt |
| 19.3 | The gluon coordinate `C` is invariant under `L ↔ R` antipodal reversal for all eight chart states. | [D] | Same receipt |
| 19.4 | The static `Z4` face template has two fixed points, zero period-2 states, and six period-4 states. | [D] | Same receipt |
| 19.5 | The bounded observer-route harness provides evidence after all eight chart states activate, but remains open-gap evidence. | [D] | Same receipt |
| 19.6 | Observation is `D4` face selection: 8 atlas faces, select 1, retain 7 as latent obligations. | [D] | `observation_is_face_selection_receipt.json`: 5/5 |
| 19.7 | The selection process is lossless; unselected faces can be reconstructed. | [D] | Same receipt |
| 19.8 | SPINOR signature observation remains open. | [X] | Explicit obligation |
| 19.9 | Consciousness or measurement-collapse interpretation remains open. | [X] | Explicit obligation |
| 19.10 | Global physical observer theorem remains open. | [X] | Explicit obligation |

---

## 2. Definitions

**Face.** One selectable reading of the local chart: a frame, chirality, or dyad side.

**Face selection.** The act of committing one face as active.

**Latent face.** An unselected face carried forward with a recovery rule.

**Gluon.** The coordinate `C`, the locally invariant midpoint of the `L | C | R` window.

**Open observer promotion.** Any claim that turns this finite selection machinery into consciousness, physical collapse, or an unverified SPINOR signature.

---

## 3. Theorems and Proofs

### Theorem 19.1 — Four Selectable Frame Faces

The observer has four selectable frame faces: `C-centroid`, `R-centroid`, `C-flipped`, and `L-centroid`.

**Proof.** The verifier defines four frame faces indexed `0..3`. For each face, the selection table records the selected face and the three latent faces. The four faces are:

| Index | Selected Face | Latent Faces |
|-------|-------------|--------------|
| 0 | `C-centroid` | `R-centroid`, `C-flipped`, `L-centroid` |
| 1 | `R-centroid` | `C-centroid`, `C-flipped`, `L-centroid` |
| 2 | `C-flipped` | `C-centroid`, `R-centroid`, `L-centroid` |
| 3 | `L-centroid` | `C-centroid`, `R-centroid`, `C-flipped` |

All four faces are defined and selectable. ∎

### Theorem 19.2 — Latent Face Retention

Selecting one face retains exactly three latent faces.

**Proof.** For each of the four selections in Theorem 19.1, the verifier records `latent_count = 3`. No selection deletes latent faces; all are retained with recovery rules. ∎

### Theorem 19.3 — Gluon Invariance under Antipodal Reversal

The gluon coordinate `C` is invariant under `L ↔ R` antipodal reversal for all eight chart states.

**Proof.** For each state `s = (L,C,R)`, the antipode is `swap_LR(s) = (R,C,L)`. The gluon is `gluon(s) = C`. Therefore `gluon(swap_LR(s)) = C = gluon(s)`. The verifier checks all eight states and confirms invariance on every row. ∎

### Theorem 19.4 — Static Z4 Face Template

The static `Z4` face template has two fixed points, zero period-2 states, and six period-4 states.

**Proof.** The `Z4` verifier applies the 4-frame composite label (wrap steps in each of the four centroid frames) to all eight states. It reports: `fixed_point_count = 2` (the true vacua `(0,0,0)` and `(1,1,1)` with label `(0,0,0,0)`), `period_2_count = 0`, and `period_4_count = 6` (all other states). This is a static coordinate-frame template, not a temporal Rule 30 periodicity claim. ∎

### Theorem 19.5 — Bounded Observer-Route Evidence

The Monster-D4 lift harness provides bounded observer-route evidence after all eight chart states activate, but carries open gaps.

**Proof.** The harness reports `pass_with_open_gaps`: all eight chart states are enumerated by depth 13, `all_eight_seen = true`, D4 lift holds after activation (`all_lift_ok = true`), and the `G2 → F4 → T5A` route stays within three moves. However, `n3_empirical_s3_closed = false`, confirming the evidence is bounded with open gaps, not a completed global observer theorem. ∎

### Theorem 19.6 — Observation Is D4 Face Selection

Observation is `D4` face selection: the center projection selects `C` (the observed face); the boundary `L,R` and the seven unselected atlas views are retained as latent alternatives (obligations); the selection is lossless.

**Proof.** The `verify_observation_is_face_selection` verifier checks: 8 atlas faces select 1 and retain 7, observation is center projection (`C`), latent alternatives are retained, selection is lossless with reconstruction possible, and the seven unselected faces are obligations. All 5 checks pass. ∎

---

## 4. Verifiers and Receipts

### 4.1 Observer Face Selection

`verify_observer_face_selection.py` → `observer_face_selection_receipt.json`

| Check | Result |
|-------|--------|
| `four_faces_exist` | pass |
| `each_selection_retains_three_latent_faces` | pass |
| `gluon_invariant_under_antipode` | pass |
| `z4_face_template_passes` | pass |
| `bounded_observer_route_evidence_passes` | pass |
| `spinor_class_remains_open` | pass (explicitly acknowledged) |
| `consciousness_postulate_not_promoted` | pass (explicitly acknowledged) |

**Status:** `pass`, 7/7.

### 4.2 Observation Is Face Selection

`verify_observation_is_face_selection.py` → `observation_is_face_selection_receipt.json`

| Check | Result |
|-------|--------|
| `atlas_8_faces_select_1_retain_7` | pass |
| `observation_is_center_projection` | pass |
| `latent_alternatives_retained` | pass |
| `selection_lossless_reconstruction` | pass |
| `seven_unselected_are_obligations` | pass |

**Status:** `pass`, 5/5.

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **19.1:** Four faces are defined by the four centroid frames.
2. **19.2:** Selecting 1 from 4 leaves 3; this is basic counting.
3. **19.3:** The antipode swaps `L` and `R` but leaves `C` unchanged; this is by definition of `swap_LR`.
4. **19.4:** Apply the `Z4` label to all 8 states; count fixed points and periods.
5. **19.6:** The atlas has 8 faces (chart states); selecting 1 leaves 7 unselected.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F19.1 | A selected face deletes rather than retains latent faces. | The verifier records all three latent faces for every selection. |
| F19.2 | The gluon `C` changes under `L ↔ R` antipodal reversal. | `swap_LR` preserves `C` by definition. |
| F19.3 | The `Z4` template contains period-2 states. | `period_2_count = 0` confirmed. |
| F19.4 | Bounded open-gap evidence is promoted as a completed theorem. | The harness is explicitly `pass_with_open_gaps`. |
| F19.5 | SPINOR is claimed observed without a receipt. | `spinor_class_remains_open = true`. |
| F19.6 | Consciousness or measurement collapse is derived from face selection. | Explicitly rejected as an open observer promotion. |

---

## 7. Relation to Later Papers

- **Paper 18** exports bounded representation routes. Paper 19 says how an observer selects a face of such a route without deleting the alternatives.
- **Paper 20** can therefore ledger each selected face and each retained obligation separately.
- **Papers 21+** may attempt to close the SPINOR signature and the global observer theorem, but must supply separate derivation and calibration receipts.

---

## 8. Open Obligations

1. **SPINOR signature observation.** The SPINOR class is not observed or verified in this paper.
2. **Full frame-inversion `Q(S)` executable binding.** The promoted paper layer does not bind the full frame-inversion operator.
3. **Consciousness or measurement-collapse interpretation.** The finite selection machinery is not a derivation of consciousness or quantum measurement collapse.
4. **Global physical observer theorem.** The bounded evidence does not close a global observer theorem.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. Monster group and exceptional structures.
3. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and `D4` / `E8` structures.
4. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(2)`, `SU(3)`, and representation theory.
5. M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995. Quantum measurement and field theory.
6. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
7. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
8. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and Monster group.
9. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. Finite group data.
10. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.

---

## 10. Conclusion

Paper 19 closes finite observer face-selection. The selection mechanism is useful precisely because it preserves the unselected faces instead of turning them into hidden assumptions. The gluon `C` is invariant under antipodal reversal, the `Z4` template provides a static coordinate frame, and the bounded observer-route evidence supports the reading without closing a global observer theorem. The remaining work is SPINOR signature, physical measurement interpretation, and global observer theory — not the finite selection proof itself.
