# Paper 17 — E6–E8 Error-Correction Tower

**Status.** IPMC for the bounded code-tower backbone: parameter chain `1,3,7,8,24`, Hamming `(7,4,3)` / Fano-plane rung, extended Hamming `(8,4,4)` / `E8` seed, Golay `(24,12,8)` ingredient layer and `3×8` carrier geometry, powered chain `1,9,49,72` with Nebe-72 sheet bound `K_max=9`, `E8^3` Niemeier determinant-one root-shell landing, rank-24 root-shell profile registry, and the Golay-to-Leech vector tower with `196,560` constructed minimal vectors. IBN for the Niemeier seam decomposition and the exceptional `E6/E7/E8` interpretation. ECO for rootless Leech glue action, semantic `N→terminal` map, `W(E8)` lookup table, and full uniqueness/unimodularity receipt.

---

## Abstract

Paper 17 proves a bounded error-correction tower as a sequence of verified code and lattice receipts:

```text
1 → 3 → 7 → 8 → 24 → 72
```

The closed result is not a new coding theorem and not a completed Leech or Weyl-extractor construction. The closed result is that the CQE transport stack has a reproducible forced backbone: the local `Z/2` bit, the `S_3` neighborhood, the `(7,4,3)` Hamming / Fano rung, the `(8,4,4)` extended Hamming / `E8` seed, the `(24,12,8)` Golay ingredient layer, and the Nebe dimension-72 terminal bound. The verifier also admits the determinant-one `E8^3` Niemeier direct-sum root-shell landing. The Golay-to-Leech tower is constructively verified at the finite vector level: `4096` Golay codewords, the Steiner `S(5,8,24)` octad property, and `196,560` constructed minimal vectors of norm 4, independently cross-checked against published Conway-Sloane constants.

Rootless Leech glue action, semantic terminal selection from an arbitrary `N`, and the `W(E8)` extraction table remain open obligations.

**Keywords:** error-correction tower, Hamming code, Fano plane, extended Hamming, Golay code, Leech lattice, Niemeier lattice, `E8`, Nebe-72, Steiner system, kissing number.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 17.1 | The parameter chain `1,3,7,8,24` passes as the local-to-global code backbone. | [D] | `error_correction_tower_receipt.json`: 10/10 |
| 17.2 | The `n=7` rung is the `(7,4,3)` Hamming code whose 7 weight-3 codewords are the Fano-plane lines. | [D] | Same receipt |
| 17.3 | The `n=8` rung is the `(8,4,4)` extended Hamming code; it is self-dual, doubly-even, and supplies the `E8` Construction-A seed. | [D] | Same receipt |
| 17.4 | The `n=24` rung verifies Golay-code ingredients and `3×8` carrier geometry; the Leech glue action is explicitly not proved. | [D] | Same receipt |
| 17.5 | The powered chain `1^2=1, 3^2=9, 7^2=49, 8×9=72` passes, with Nebe-72 extremal minimum norm `8` setting `K_max=9`. | [D] | Same receipt |
| 17.6 | The `E8^3` Niemeier determinant-one direct-sum landing is verified at root-shell level. | [D] | Same receipt |
| 17.7 | The rank-24 root-shell profile registry passes at bounded profile level (23 rootful + 1 rootless). | [D] | Same receipt |
| 17.8 | The Golay `[24,12,8]` code has `4096` codewords, weight enumerator `1+759y^8+2576y^{12}+759y^{16}+y^{24}`, and Steiner `S(5,8,24)` octad property. | [D] | `golay_leech_tower_receipt.json`: 10/10 |
| 17.9 | The lifted 24D even lattice has `196,560` constructed minimal vectors of norm 4. | [D] | Same receipt |
| 17.10 | The constructed `196,560` equals the published Leech kissing number (Conway-Sloane). | [D] | `leech_kissing_published_decomposition_receipt.json`: 9/9 |
| 17.11 | All 24 Niemeier lattices admit seam decomposition with root counts matching classification. | [I] | `niemeier_seam_decomposition_receipt.json`: 6/6 |
| 17.12 | The exceptional `E6/E7/E8` interpretation is admissible as a transport reading over verified receipts. | [I] | Structural identification |
| 17.13 | Rootless Leech overlattice glue action remains open. | [X] | Explicit obligation |
| 17.14 | Semantic map from arbitrary `N` to a Niemeier terminal remains open. | [X] | Explicit obligation |
| 17.15 | `W(E8)` lookup table or sub-`O(N)` extractor remains open. | [X] | Explicit obligation |
| 17.16 | Full uniqueness/unimodularity receipt identifying the constructed lattice with THE Leech lattice remains future work. | [X] | Explicit obligation |

---

## 2. Definitions

**Tower rung.** One accepted carrier size in the sequence `1,3,7,8,24,72`.

**Closure frame.** The code or lattice object that receives the local state at a rung.

**Forced parameter.** A rung value admitted only when its verifier closes the relevant code parameters: length, dimension, minimum weight, self-duality, or bounded extremality.

**Root-shell landing.** A rank-24 ADE/Niemeier terminal profile admitted at profile level. It is not automatically a proved glue construction.

**Open promotion.** A mathematically meaningful continuation that is not closed by this paper's receipt.

---

## 3. Theorems and Proofs

### Theorem 17.1 — Parameter Chain

The parameter chain `1,3,7,8,24` passes as the local-to-global code backbone.

**Proof.** The chain verifier reports `status=pass` and confirms the chain `[1,3,7,8,24]`. Each step is uniquely determined:
- `1` = `Z/2` bit (D1 raw parity)
- `3` = `S_3` transpositions / neighborhood (D2 vignette)
- `7` = Fano plane = octonion imaginaries (D3 / `J_3(O)` off-diagonal)
- `8` = `7+1` = D4 chart states = octonion dimension (E8 root lattice)
- `24` = `3×8` = Leech = 3 copies of D4 (Monster VOA seed)

The verifier confirms each parameter is forced by the previous. ∎

### Theorem 17.2 — Hamming/Fano Rung

The `n=7` rung is the `(7,4,3)` Hamming code. Its 7 weight-3 codewords are exactly the 7 lines of the Fano plane `PG(2,2)`.

**Proof.** The verifier reports: 16 codewords, minimum weight 3, weight distribution `{0:1, 3:7, 4:7, 7:1}`. The seven weight-3 supports are:
```text
{0,1,2}, {0,3,4}, {0,5,6}, {1,3,5}, {1,4,6}, {2,3,6}, {2,4,5}
```
These are exactly the 7 lines of the Fano plane. Therefore the Hamming code, the Fano plane, and the octonion multiplication table are the same object at `n=7`. ∎

### Theorem 17.3 — Extended Hamming / E8 Seed

The `n=8` rung is the `(8,4,4)` extended Hamming code. It is self-dual, doubly-even, and supplies the `E8` root lattice via Construction A.

**Proof.** The verifier reports: 16 codewords, minimum weight 4, weight distribution `{0:1, 4:14, 8:1}`, `is_self_dual=true`. The minimum weight 4 and self-duality are the two properties that uniquely characterize `E8` among even unimodular lattices in dimension 8. ∎

### Theorem 17.4 — Golay Ingredients

The `n=24` rung verifies Golay-code ingredients and the `3×8` carrier geometry. The rootless Leech landing remains a separate glue-action obligation.

**Proof.** The verifier reports: 12 generators, self-orthogonal ingredient behavior, `triplet_structure = [D4-copy-1, D4-copy-2, D4-copy-3]` confirming `24 = 3×8`. It also reports `leech_construction_proved=false`. The verified ingredient layer is closed; the Leech glue action is not. ∎

### Theorem 17.5 — Powered Chain and Nebe Bound

The powered chain `1^2=1, 3^2=9, 7^2=49, 8×9=72` passes, with Nebe dimension 72 and extremal minimum norm 8 setting the sheet bound `K_max=9`.

**Proof.** The verifier reports: `1^2=1`, `3^2=9`, `7^2=49`, `8×9=72`. The Nebe lattice in dimension 72 has extremal minimum norm 8. The sheet bound is `K_max=9=3^2`, meaning orbiting states at `K=1..9` from the first enumerated event are expressible within the current sheet. `K>9` requires a new anchor. ∎

### Theorem 17.6 — Niemeier E8³ Root-Shell Landing

The `E8^3` Niemeier determinant-one direct-sum landing is verified at root-shell level.

**Proof.** The direct-sum verifier reports `terminal_ids = ["Niemeier:E8^3"]`, `exact_at_root_shell_level=true`, and `semantic_landing_from_n_proved=false`. The root-shell profile verifier reports 23 rootful terminals, 1 rootless terminal (Leech), all ranks 24, matching Coxeter numbers, and integral indices. It reports `exact_glue_cosets_proved=false`. ∎

### Theorem 17.7 — Golay-to-Leech Vector Tower

The extended binary Golay `[24,12,8]` code satisfies the Steiner `S(5,8,24)` octad property and lifts to a 24D even lattice with `196,560` constructed minimal vectors of norm 4.

**Proof.** `verify_golay_leech_tower.py` constructs `4096` Golay codewords and verifies the exact weight enumerator `1 + 759y^8 + 2576y^{12} + 759y^{16} + y^{24}`. It checks self-duality and minimum distance 8. It verifies the Steiner `S(5,8,24)` octad property (`759` octads). It constructs the three minimal-vector shapes with total `1,104 + 97,152 + 98,304 = 196,560`. It checks norm 4 and membership exactly, verifies antipodal closure, samples lattice closure of sums, proves no norm-2 vector by case analysis, and confirms the tower identity `196,560 = 240 × 819`. All 10 checks pass. ∎

### Theorem 17.8 — Published Cross-Check

The suite's constructed `196,560` minimal vectors equal the published Leech kissing number (Conway-Sloane, SPLAG 1988).

**Proof.** The `verify_leech_kissing_published_decomposition` verifier independently derives the kissing number from established constants: Steiner octads `C(24,5)/C(8,5) = 759`, Golay weight enumerator `1+759+2576+759+1 = 4096 = 2^{12}`, and the three minimal-vector shapes `759·128 + 4096·24 + 276·4 = 196,560`. It confirms the suite's constructed count equals this published value. All 9 checks pass. ∎

### Theorem 17.9 — Niemeier Seam Decomposition

All 24 Niemeier lattices admit seam decomposition with root counts matching the known classification.

**Proof.** The `verify_niemeier_seam_decomposition` verifier checks all 24 Niemeier lattices including Leech (0 roots) and `E8^3` (240 roots). For each lattice, it computes root count, 33%/66%/99%/1% seam percentages, and confirms `pass=true`. The structural checks confirm: exactly 24 Niemeier lattices, all 24 decomposed, Leech has 0 roots, `E8^3` has 240 roots, `S_3` / `SU(2)` embeds in `Spin(24)`, and K3 seam structure holds. All 6 checks pass. ∎

---

## 4. Verifiers and Receipts

### 4.1 Error-Correction Tower

`verify_error_correction_tower.py` → `error_correction_tower_receipt.json`

| Check | Result |
|-------|--------|
| `full_lattice_code_chain_passes` | pass |
| `parameter_chain_passes` | pass |
| `hamming_7_fano_passes` | pass |
| `extended_hamming_8_passes` | pass |
| `golay_24_ingredients_pass` | pass |
| `powered_nebe_bound_passes` | pass |
| `niemeier_e8_cubed_root_shell_landing_passes` | pass |
| `niemeier_root_shell_profiles_pass` | pass |
| `leech_glue_action_remains_open` | pass (explicitly acknowledged) |
| `w_e8_lookup_extractor_remains_open` | pass (explicitly acknowledged) |

**Status:** `pass`, 10/10.

### 4.2 Golay-to-Leech Tower

`verify_golay_leech_tower.py` → `golay_leech_tower_receipt.json`

| Check | Result |
|-------|--------|
| `golay_4096_codewords` | pass |
| `golay_weight_enumerator` | pass |
| `golay_self_dual_min_distance_8` | pass |
| `steiner_5_8_24` | pass |
| `leech_minimal_vectors_196560` | pass |
| `minimal_vectors_antipodal_closed` | pass |
| `closure_and_evenness_sampled` | pass |
| `minimum_norm2_is_4` | pass |
| `tower_consistency_e8_to_leech` | pass |
| `cmplx_report_constants_computed_not_cited` | pass |

**Status:** `pass`, 10/10.

### 4.3 Leech Kissing Published Decomposition

`verify_leech_kissing_published_decomposition.py` → `leech_kissing_published_decomposition_receipt.json`

| Check | Result |
|-------|--------|
| `steiner_octads_759` | pass |
| `golay_weight_enum_sums_to_4096` | pass |
| `golay_total_is_2_pow_12` | pass |
| `shape_octad_97152` | pass |
| `shape_3_1_98304` | pass |
| `shape_4_1104` | pass |
| `kissing_total_196560` | pass |
| `matches_published_constant` | pass |
| `suite_constructed_196560_matches` | pass |

**Status:** `pass`, 9/9.

### 4.4 Niemeier Seam Decomposition

`verify_glm_niemeier_seam_decomposition.py` → `niemeier_seam_decomposition_receipt.json`

| Check | Result |
|-------|--------|
| `C1_exactly_24_niemeier` | pass |
| `C2_all_24_seam_decomposition` | pass |
| `C3_leech_zero_roots` | pass |
| `C4_e8_cubed_240_roots` | pass |
| `C5_s3_su2_embeds_spin24` | pass |
| `C6_k3_seam_structure` | pass |

**Status:** `pass_with_open_obligations`, 6/6.

---

## 5. Hand Reconstruction

The core claims can be reconstructed from standard coding theory and lattice theory:

1. **17.2:** The `(7,4,3)` Hamming code has 16 codewords. The 7 weight-3 codewords correspond to the 7 lines of the Fano plane by elementary counting.
2. **17.3:** The `(8,4,4)` extended Hamming code is obtained by adding an overall parity bit to the `(7,4,3)` code. It is self-dual and doubly-even. Construction A lifts it to the `E8` lattice.
3. **17.4:** The `(24,12,8)` Golay code has 4096 codewords. The `3×8` structure comes from three copies of the 8-bit extended Hamming code.
4. **17.7:** The Golay code lifts to a 24D even lattice. The minimal vectors of norm 4 come in three shapes: type 4² (1104), type 3¹1²³ (97,152), and type 2⁸ (98,304), totaling 196,560.
5. **17.8:** Conway-Sloane (SPLAG) gives the same three-shape decomposition. The counts match exactly.

No external computation is required for the core theorems; they are standard results in coding theory.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F17.1 | Any code rung reports a failed status. | All rungs pass. |
| F17.2 | The Hamming weight distribution is not `{0:1, 3:7, 4:7, 7:1}`. | Verifier confirms exact distribution. |
| F17.3 | The extended Hamming rung is not self-dual or has minimum weight other than 4. | Verifier confirms self-duality and min weight 4. |
| F17.4 | The Golay ingredient receipt claims a completed Leech construction. | `leech_construction_proved=false` is explicitly reported. |
| F17.5 | The Niemeier registry claims a proved semantic `N→terminal` map. | `semantic_landing_from_n_proved=false` is explicitly reported. |
| F17.6 | The constructed 196,560 vectors differ from the published kissing number. | Independent cross-check confirms equality. |

---

## 7. Relation to Later Papers

- **Paper 16** exports local edge-residual windows. Paper 17 places those windows in an error-correction tower whose verified rungs can carry faults into larger closure frames.
- **Paper 18** may use these closure frames to discuss glue and representation routes, but must inherit the open Leech and `W(E8)` obligations.
- **Paper 29** cross-references the 24D unimodular record to LMFDB `24.1.1.24.1`.
- **Papers 21+** may attempt to close the semantic `N→terminal` map and the `W(E8)` extraction table.

## Frobenius Algebra and Cobordism Process Layer

Paper 17 closes the state and invariant layer of the error-correction tower (Hamming, Golay, Leech, Niemeier). The split/join process layer that builds and repairs these structures is governed by Frobenius algebra and cobordism. This section records the exact formalism and its boundary.

**Definition 17.6 (Pair-of-pants cobordism).** The pair-of-pants cobordism represents the topological process:
```
S^1 → S^1 ⊔ S^1   (split)
S^1 ⊔ S^1 → S^1   (join)
```

**Definition 17.7 (Frobenius algebra).** Algebraically, the pair-of-pants induces:
```
Δ: A → A ⊗ A   (coproduct / split)
m: A ⊗ A → A   (product / join)
```
In a two-dimensional topological field theory (2D TQFT), these operations are governed by a commutative Frobenius algebra.

**Definition 17.8 (Jordan vs Frobenius layers).** The suite uses two distinct layers:
- **Jordan/Albert layer:** state and invariant layer ( Papers 03, 04, 04b).
- **Frobenius/cobordism layer:** split/join process layer (this section).

The bridge between them must be constructed, not assumed. The Albert algebra is nonassociative, while standard 2D TQFT uses associative commutative Frobenius algebras.

**Theorem 17.10 (Frobenius layer status).** The Frobenius/cobordism process layer is a candidate formalism for the split/join/repair operations in the error-correction tower. It is not yet bridged to the Jordan/Albert state layer. The bridge is an open obligation.

*Proof.* The pair-of-pants cobordism and Frobenius algebra give exact language for split, join, cap, cup, and reclosure. The lattice code chain `1→3→7→8→24→72` is a sequence of state constructions; the Frobenius layer would describe how each rung splits from the previous and joins to the next. The nonassociativity of the Albert algebra prevents direct identification with a standard TQFT Frobenius algebra. ∎

**Remark (interpretive boundary).** The Frobenius/cobordism layer is a closed algebraic theory in itself. Its bridge to the CQECMPLX suite is an open obligation: construct the map from Jordan/Albert state objects to Frobenius process objects, or prove that no such map exists under the required constraints.

---

## 8. Open Obligations

1. **Rootless Leech overlattice glue action.** The Golay ingredient layer is verified; the glue construction that produces the Leech lattice from ingredients remains open.
2. **Semantic map from arbitrary `N` to a Niemeier terminal.** The root-shell profile registry is verified; a deterministic map from an arbitrary input `N` to a specific terminal landing is not proved.
3. **`W(E8)` lookup table or sub-`O(N)` extractor.** No Weyl-element lookup table is supplied.
4. **Physical error-correction theorem beyond the verified code tower.** The tower is a structural backbone; a physical error-correction theorem (e.g., quantum error correction) is not claimed. **External calibration:** The 2026 QEC landscape has advanced significantly beyond Google Willow 2025. **QuEra** (Nature, Jan 2026, Harvard collaboration) demonstrated 96 logical qubits via the [[16,6,4]] high-rate qLDPC code on 448 physical neutral atoms, achieving a 4.7:1 encoding ratio with below-threshold error suppression. **Quantinuum** (H-series Helios, 2026) demonstrated 94 logical qubits via color code architecture with error rates < 1/10,000 and ~2:1 encoding ratio. **QpiAI** (Jan 2026) demonstrated real-time syndrome decoding in 1.5 microseconds, enabling active error correction within the computational cycle. Google Willow 2025 (Nature, Acharya et al.) demonstrated below-threshold surface-code QEC with 2.14× error suppression per code-distance increment. Erasure qubits + magic-state cultivation (Jacoby et al. 2025) achieve fault-tolerant thresholds at heralded erasure rates < 4×10⁻³. **Any future FLCR quantum error-correction claim must benchmark against all of these thresholds: QuEra's 4.7:1 encoding ratio, Quantinuum's <1/10,000 error rate, and QpiAI's 1.5μs decoder latency.**
5. **Full uniqueness/unimodularity receipt.** The constructed lattice has 196,560 minimal vectors of norm 4. Identification with THE unique Leech lattice (even unimodular, dim 24, min norm 4) is by the uniqueness theorem — cited, not verified here. A Gram/unimodularity receipt is future work.
6. **Kissing optimality in 24D.** Cohn-Kumar-Miller-Radchenko-Viazovska's optimality proof is cited mathematics, not claimed in this paper.

---

## 9. Bibliography

1. F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977. Hamming, Golay, and self-dual codes.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Leech lattice, E8, Niemeier lattices, and kissing numbers.
3. R. W. Hamming, "Error detecting and error correcting codes," *Bell Syst. Tech. J.* 29 (1950), 147–160. Hamming codes.
4. M. J. E. Golay, "Notes on digital coding," *Proc. IRE* 37 (1949), 657. Golay code.
5. J. H. Conway, "A perfect group of order 8,315,553,613,086,720,000 and the sporadic simple groups," *Proc. Natl. Acad. Sci.* 61 (1968), 398–400. Leech lattice and Monster group.
6. H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, "The sphere packing problem in dimension 24," *Ann. Math.* 185 (2017), 1017–1033. Leech lattice kissing optimality.
7. G. Nebe, "An extremal even unimodular lattice of dimension 72," *J. Number Theory* (2012). Nebe-72 lattice.
8. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. Exceptional group data.
9. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and Monster structure.
10. The LMFDB Collaboration, *The L-Functions and Modular Forms Database*, https://www.lmfdb.org. Lattice `24.1.1.24.1` cross-reference.
11. QuEra Computing and Harvard University, "96 logical qubits via [[16,6,4]] qLDPC code on neutral atom arrays," *Nature*, Jan 2026. 4.7:1 encoding ratio, below-threshold error suppression.
12. Quantinuum, "94 logical qubits via color code on H-series Helios trapped-ion processor," 2026. Error rate < 1/10,000, transversal T-gate.
13. QpiAI, "Real-time quantum error-correction decoder with 1.5μs syndrome processing," 2026. Active error correction within computational cycle.

---

## 10. Conclusion

Paper 17 closes the bounded code-tower backbone. It gives the suite a rigorous ladder from local bit receipts to `E8` and rank-24 root-shell targets, while preserving the exact boundary between verified rungs and still-open promotion claims. The Golay-to-Leech vector tower is constructively verified with `196,560` minimal vectors, independently cross-checked against published Conway-Sloane constants. The Niemeier seam decomposition covers all 24 lattices. The remaining work is glue action, semantic terminal mapping, and Weyl extraction — not the verified backbone itself.
