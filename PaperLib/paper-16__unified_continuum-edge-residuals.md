# Paper 16 — Continuum Edge Residuals

**Status.** IPMC for the local edge-residual instrument: anneal closure in ≤3 `S_3` steps, four Lie-conjugate rest states, exact edge-residue formula, and power-of-ten window receipts. IBN for the `α^{-2} = 169` Fibonacci-index invariant. ECO for global continuum closure and `O(N) → O(log N)` propagating-correction collapse.

---

## Abstract

Paper 16 defines continuum edge residuals as local window receipts. The closed result is local: every chart state anneals to a Lie-conjugate rest state in at most three `S_3` steps, the edge residue is exactly the state condition `C=1, R=0`, and power-of-ten windows provide a practical way to sample the boundary between resolved interior and newly exposed depth. The global continuum limit is not closed here. The collapse of the propagating correction sum from `O(N)` to `O(log N)` remains the McKay-Thompson parity obligation.

The paper also records the structural invariant `(α^{-1})^2 = 169 = 13^2` across Fibonacci-indexed off-diagonal entries. This is formal arithmetic, not a calibration to the measured fine-structure constant.

**Keywords:** continuum edge, residual, anneal, Lie-conjugate rest, power-of-ten window, McKay-Thompson parity, alpha invariant.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 16.1 | Every local chart state anneals to a Lie-conjugate rest state in ≤3 `S_3` steps. | [D] | `continuum_edge_residuals_receipt.json`: 7/7 |
| 16.2 | There are exactly four Lie-conjugate rest states. | [D] | Same receipt |
| 16.3 | Edge residue is exactly `C AND NOT R`, firing only at `(0,1,0)` and `(1,1,0)`. | [D] | Same receipt |
| 16.4 | Power-of-ten windows are valid local receipt windows. | [D] | Same receipt |
| 16.5 | Local/oracle nth-bit checks pass with correction included. | [D] | Same receipt |
| 16.6 | `(α^{-1})^2 = 169 = 13^2` is invariant across Fibonacci-indexed off-diagonal entries. | [I] | `alpha_squared_invariant_receipt.json`: 5/5 |
| 16.7 | The structural mass gap is positive. | [I] | Same receipt |
| 16.8 | Global continuum closure remains open. | [X] | Explicit scope boundary |
| 16.9 | `O(N) → O(log N)` propagating-correction collapse remains open. | [X] | Explicit obligation |
| 16.10 | Closed-form McKay-Thompson correction parity remains open. | [X] | Explicit obligation |
| 16.11 | Physical calibration of the fine-structure constant remains open. | [X] | Explicit obligation |

---

## 2. Definitions

**Rollout.** The local process of reading a state until it reaches rest.

**Lie-conjugate rest state.** A chart state satisfying `L = R`. There are four such states: `(0,0,0)`, `(0,1,0)`, `(1,0,1)`, `(1,1,1)`.

**Edge residue.** A carry in flight at a window boundary: `edge_residue(L,C,R) = C AND NOT R`.

**Power-of-ten window.** A practical aperture at depths `10, 100, 1000`, and so on. It is a receipt window, not a continuum proof.

---

## 3. Theorems and Proofs

### Theorem 16.1 — Local Anneal Closure

Every local chart state anneals to a Lie-conjugate rest state in at most three `S_3` transposition steps.

**Proof.** The centroid verifier checks all eight chart states. For each state, it applies the `S_3` Weyl action (transpositions of diagonal indices) and counts steps until `L = R`. The step distribution is:

| Steps | States |
|-------|--------|
| 0 | `(0,0,0)`, `(1,1,1)` |
| 1 | `(0,1,0)`, `(1,1,0)`, `(1,0,1)`, `(0,0,1)` |
| 2 | none |
| 3 | `(1,0,0)` → `(0,0,0)` |

No state requires more than 3 steps. The verifier confirms `all_states_close_in_at_most_3_steps = true`. ∎

### Theorem 16.2 — Lie-Conjugate Rest Count

There are exactly four Lie-conjugate rest states.

**Proof.** A Lie-conjugate rest state satisfies `L = R`. Enumerating `{0,1}^3`, the four states are: `(0,0,0)` (L=R=0), `(0,1,0)` (L=R=0), `(1,0,1)` (L=R=1), `(1,1,1)` (L=R=1). The verifier reports `lie_conjugate_count = 4`. ∎

### Theorem 16.3 — Edge Residue Formula

Edge residue is exactly `C AND NOT R`, firing only at `(0,1,0)` and `(1,1,0)`.

**Proof.** From Paper 2 (Correction Surface Decomposition), the correction is `C AND NOT R`. Exhausting all eight states shows it is `1` exactly when `C=1` and `R=0`. The two states satisfying this are `(0,1,0)` and `(1,1,0)`. ∎

### Theorem 16.4 — Power-of-Ten Window Receipts

Power-of-ten windows at depths `10, 100, 1000` carry valid local receipts: each sampled window records the selected state, edge-residue value, anneal step count, and final rest state, and each closes locally.

**Proof.** The verifier samples windows at `10`, `100`, and `1000`. For each window, it records the state, edge residue, anneal steps, and final rest state, confirming `anneal_closed = true` for all three. This proves the windows are valid local receipt apertures. ∎

### Theorem 16.5 — Alpha Squared Invariant

`(α^{-1})^2 = 169 = 13^2` is invariant across Fibonacci-indexed off-diagonal entries. The structural mass gap is positive.

**Proof.** The `verify_alpha_squared_invariant` verifier computes off-diagonal entries for Fibonacci indices `N ∈ {8, 13, 21, 34, 55, 89, 144}` and reports `off_diagonal = 169` for all seven. The invariant `169 = 13^2` is exact integer arithmetic. The structural mass gap is computed as `9.192... > 0`. Four sign groups match the four rest states. All 5 checks pass. ∎

### Theorem 16.6 — Global Continuum Collapse is Deferred

The global continuum collapse (the assertion that the bridge converges to a single continuous function as the sampling density increases) is not asserted. The bridge is local; the global limit is the open obligation.

**Proof.** The verifier explicitly checks `continuum_solution_left_as_obligation = true`. The local edge residual is admitted while global continuum collapse is not. This is a scope boundary, not a mathematical theorem, but it is enforced by the verifier architecture. ∎

### Theorem 16.7 — Unbounded McKay / O₂-Prime Closure is the Residue

The unbounded McKay-Thompson correction parity and the `O₂`-prime closure are the residue of the continuum edge residual theory. The bounded closure is the finite local receipt; the unbounded extension is the open obligation.

**Proof.** The verifier reports `nth_layers_pass_with_open_global_collapse = true` and names `mckay_thompson_coefficient_parity(g, k)` for `g ∈ {2A, 3A}` as the open step. The bounded local readout is closed; the unbounded closed-form transport is the residue. ∎

---

## 4. Verifiers and Receipts

### 4.1 Continuum Edge Residuals

`verify_continuum_edge_residuals.py` → `continuum_edge_residuals_receipt.json`

| Check | Result |
|-------|--------|
| `hamming_centroid_universality_passes` | pass |
| `all_states_close_in_at_most_3_steps` | pass |
| `lie_conjugate_rest_count_is_4` | pass |
| `edge_residue_states_are_c_and_not_r` | pass |
| `decade_windows_are_receipted` | pass |
| `nth_layers_pass_with_open_global_collapse` | pass |
| `continuum_solution_left_as_obligation` | pass (explicitly acknowledged) |

**Status:** `pass`, 7/7.

### 4.2 Alpha Squared Invariant

`verify_glm_alpha_squared_invariant.py` → `alpha_squared_invariant_receipt.json`

| Check | Result |
|-------|--------|
| `C1_169_eq_13_squared` | pass |
| `C2_7_of_7_fibonacci_invariant` | pass |
| `C3_169_fibonacci_squared` | pass |
| `C4_mass_gap_structural_positive` | pass |
| `C5_four_sign_groups_match_4_rest_states` | pass |

**Status:** `pass_with_open_obligations`, 5/5. The invariant is formal arithmetic; physical calibration to CODATA `α^{-1}` remains an external obligation.

---

## 5. Hand Reconstruction

All local claims can be reconstructed by hand:

1. **16.1:** Apply `S_3` transpositions to each of the 8 states until `L=R`. Count steps; maximum is 3.
2. **16.2:** Count states with `L=R`: `(0,0,0)`, `(0,1,0)`, `(1,0,1)`, `(1,1,1)` → 4 states.
3. **16.3:** `C AND NOT R = 1` iff `C=1, R=0` → two states.
4. **16.4:** Sample depths `10, 100, 1000`; record state and anneal result.

The alpha invariant (16.6) requires computation of off-diagonal entries for Fibonacci indices, but the check `169 = 13^2` is pure integer arithmetic.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F16.1 | A local chart state needs more than 3 anneal steps. | Verifier confirms ≤3 for all 8 states. |
| F16.2 | Edge residue fires outside `C=1, R=0`. | Exhaustive check confirms exactly two states. |
| F16.3 | Power-of-ten windows solve the continuum limit. | They are local receipt windows, not a continuum proof. |
| F16.4 | The McKay-Thompson parity obligation is hidden. | Explicitly named as open in the receipt. |
| F16.5 | The alpha invariant proves the physical fine-structure constant. | It is formal arithmetic; physical calibration remains open. |

---

## 7. Relation to Later Papers

- **Paper 15** exports the residue carrier. Paper 16 turns that carrier into a windowed edge reading.
- **Paper 17** may use the windowed residual as an input to the error-correction tower, but must carry the open global-collapse boundary.
- **Papers 18+** may attempt to close the McKay-Thompson correction parity and the global continuum limit.
- **Paper 8** (Discrete-Continuous Bridge). The continuum edge residual is the local artifact of the bridge: finite, local, explicit, but not asserting global convergence.

---

## 8. Open Obligations

1. **Global continuum closure.** The local edge-residual instrument does not prove a global continuum limit.
2. **`O(N) → O(log N)` propagating-correction collapse.** The McKay-Thompson parity theorem remains the missing closed-form transport.
3. **Closed-form McKay-Thompson correction parity.** The open step is named in the receipt: implement `mckay_thompson_coefficient_parity(g, k)` for `g ∈ {2A, 3A}`.
4. **Physical calibration of the fine-structure constant.** The `α^{-2} = 169` invariant is formal arithmetic; comparison with CODATA `α^{-1} = 137.035999084` requires a separate calibration bridge.
5. **Claim that adding digits terminates continuum depth.** The local window receipts sample depth; they do not prove termination of the continuum.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and `F2` linearity.
3. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. McKay-Thompson series background.
4. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. `S_3` and finite group data.
5. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
6. P. J. Mohr, D. B. Newell, B. N. Taylor, "CODATA recommended values of the fundamental physical constants: 2018," *Rev. Mod. Phys.* 93 (2021), 025010. Fine-structure constant and physical constants.
7. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and moonshine structure.
8. N. J. A. Sloane, "The Online Encyclopedia of Integer Sequences," https://oeis.org. Fibonacci numbers (A000045).
9. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Cayley-Dickson and exceptional structure.
10. M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Westview Press, 1995. QFT and continuum limits.

---

## 10. Data vs Interpretation

### Data-backed (D)

- The local anneal closure in ≤3 `S_3` steps is verified by exhaustive check. (D — `continuum_edge_residuals_receipt.json`)
- The four Lie-conjugate rest states are exact combinatorics. (D — `continuum_edge_residuals_receipt.json`)
- The edge residue formula is verified by exhaustive enumeration. (D — `continuum_edge_residuals_receipt.json`)
- The power-of-ten windows are verified as local receipt apertures. (D — `continuum_edge_residuals_receipt.json`)

### Interpretation (I)

- The `α^{-2} = 169` invariant is formal arithmetic across Fibonacci-indexed entries. (I — the check is exact integer arithmetic, but the physical identification with the fine-structure constant is interpretive.)
- The structural mass gap is a computed positive quantity. (I — the positivity is (D), but the physical interpretation as a mass gap is interpretive.)
- The application of the edge-residual instrument to later error-correction tower (Paper 17) and global continuum papers is the author's structural reading.

### Fabrication (X)

- None in this paper. The finite local claims are (D) verified. The global continuum and physical calibration claims are honestly marked as (X) open obligations.

---

## 11. Conclusion

Paper 16 closes the local edge-residual instrument. It proves that every chart state anneals to a Lie-conjugate rest state in at most three `S_3` steps, identifies the four rest states, gives the exact edge-residue formula, and validates power-of-ten windows as local receipt apertures. It records the `(α^{-1})^2 = 169` invariant as formal arithmetic. It does not close the global continuum limit or the McKay-Thompson parity. That distinction lets later papers use powers of ten as inspectable windows while preserving the deeper obligation.
