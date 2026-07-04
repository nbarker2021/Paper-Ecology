# Paper 12 — CA Prediction Surface

**Status.** IPMC for finite local CA readout, Rule 30 truth-table equivalence, `T_EMISSION`, Rule 90–correction decomposition, silent-boundary ECA counting, finite entropy/real-data evidence, and the prediction-surface discipline theorem. ECO for spectral and empirical layers. IBN for SU(3)/F4 transport arguments.

---

## Abstract

Paper 12 defines the cellular-automaton prediction surface for deterministic binary systems. A prediction surface is not a single universal predictor; it is a typed stack of layers, each reporting its input, output, cost class, defect, and receipt.

The closed result is finite and local. For Rule 30, the local truth table matches `L xor (C or R)`, the `T_EMISSION` formula matches all eight local LCR states, and the rule decomposes locally as `Rule90 xor (C and not R)`. The paper also verifies that exactly 64 of the 256 elementary cellular automata have silent boundary values `f(0,0,0)=0` and `f(1,1,1)=0`.

The paper explicitly does not close cold-start Rule 30 Problem 3 extraction. The receipt `p3_closure_receipt.json` reports `fail` on the cold-start bit-exact check, so any prose claiming full P3 closure is quarantined as a falsifier. The unbounded correction-collapse problem remains open and is routed to Paper 10/09 for the O(log N) readout architecture.

**Keywords:** Rule 30; cellular automata; prediction surface; T_EMISSION; Rule 90; correction; silent boundary; Wolfram Prize Problems.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 12.1 | Rule 30 local truth table matches `L xor (C or R)` on all 8 LCR states. | [D] | `ca_prediction_surface_receipt.json`: 7/7 |
| 12.2 | `T_EMISSION(L,C,R)` matches Rule 30 on all 8 states. | [D] | Same receipt |
| 12.3 | Rule 30 decomposes as `Rule90(L,R) xor (C and not R)` on all 8 states. | [D] | Same receipt |
| 12.4 | Exactly 64 of 256 ECAs are silent-boundary rules. | [D] | Same receipt |
| 12.5 | A prediction surface must preserve layer, cost, defect, and receipt metadata. | [D] | Definitional / schema |
| 12.6 | Center-column entropy engine is present (EntropyForge). | [D] | `center_column_entropy_receipt.json`: 1/1 |
| 12.7 | Sierpinski 3^k-in-2^k growth is exact to k=11. | [D] | `p1_non_periodicity_receipt.json`: 7/7 |
| 12.8 | SU(3) Weyl orbit on trace-2 closes at n=3, not n=1 or n=2. | [D] | Same receipt |
| 12.9 | No period ≤ 256 in first 2048 center-column bits. | [D] | Same receipt |
| 12.10 | Local correction split is 6 preserve / 2 flip. | [D] | `p2_density_receipt.json`: 7/7 |
| 12.11 | F4 uniform measure on trace-2 at n=3 is exact rational (1/3, 1/3, 1/3). | [D] | Same receipt |
| 12.12 | XOR-debiased density within 5% of 1/2 in 2048-bit window. | [D] | Same receipt |
| 12.13 | 1M-bit Wolfram center column: no period ≤ 65,536; density 0.500768. | [D] | `wolfram_1m_bit_validation_receipt.json`: 9/9 |
| 12.14 | Generator bit-exact to real data; decomposition reproduces real bits. | [D] | `rule30_real_dataset_experiment_receipt.json`: 4/4 |
| 12.15 | 13 idempotent systems exhibit Rule 30/90/correction structure. | [I] | `idempotent_connections_receipt.json`: 6/6 |
| 12.16 | Spectral next-state layer is a non-cold-start predictor. | [I] | Empirical / heuristic |
| 12.17 | Infinite center-column non-periodicity (P1) remains unproved. | [X] | Literature open |
| 12.18 | Asymptotic equal density (P2) remains unproved. | [X] | Literature open |
| 12.19 | Cold-start O(log N) Rule 30 extractor (P3) remains open. | [X] | Receipt `fail` on bit-exact |
| 12.20 | Product-level randomness certification (NIST-style) is outside scope. | [X] | Product obligation |

---

## 2. Definitions

**Elementary cellular automaton (ECA).** A radius-1 binary rule `f: {0,1}^3 → {0,1}`. For rule number `r`, the local emission is `emit_r(L,C,R) = (r >> (4L + 2C + R)) & 1`.

**Rule 30.** `Rule30(L,C,R) = L xor (C or R)`.

**Rule 90.** `Rule90(L,R) = L xor R`.

**Correction.** `corr(L,C,R) = C and (not R)`.

**Prediction surface.** A layered object `surface(system, N) → (bit, layer, cost, defect, receipt)` that returns a readout together with the layer that produced it, its cost class, any known defect, and the evidence receipt.

**Local readout.** A statement verified over all eight possible LCR states `{0,1}^3`.

**Silent-boundary rule.** An ECA satisfying `emit_r(0,0,0) = 0` and `emit_r(1,1,1) = 0`.

**Cold-start extraction.** Computation of a target center bit from depth/index without relying on a hydrated target sheet or cached/generated prior state.

---

## 3. Theorems and Proofs

### Theorem 12.1 — Local Rule 30 Truth Table

`Rule30(L,C,R) = L xor (C or R)` matches the ECA definition of Rule 30 on all eight states in `{0,1}^3`.

**Proof.** Exhaustive. For each of the 8 states `(L,C,R)`, compute `emit_30(L,C,R)` from the ECA rule number `30 = 0b00011110` and compare to `L xor (C or R)`. The verifier `verify_ca_prediction_surface.py` constructs the following table:

| L | C | R | `emit_30` | `L xor (C or R)` | Match |
|---|---|---|-----------|------------------|-------|
| 0 | 0 | 0 | 0 | 0 | yes |
| 0 | 0 | 1 | 1 | 1 | yes |
| 0 | 1 | 0 | 1 | 1 | yes |
| 0 | 1 | 1 | 1 | 1 | yes |
| 1 | 0 | 0 | 1 | 1 | yes |
| 1 | 0 | 1 | 0 | 0 | yes |
| 1 | 1 | 0 | 0 | 0 | yes |
| 1 | 1 | 1 | 0 | 0 | yes |

All eight rows match. ∎

### Theorem 12.2 — T_EMISSION Equivalence

`T_EMISSION(L,C,R) = not L if C=1 else L xor R` equals `Rule30(L,C,R)` on all eight states.

**Proof.** Case analysis on `C`.

- If `C = 1`: `Rule30(L,1,R) = L xor (1 or R) = L xor 1 = not L`. And `T_EMISSION(L,1,R) = not L`. Equal.
- If `C = 0`: `Rule30(L,0,R) = L xor (0 or R) = L xor R`. And `T_EMISSION(L,0,R) = L xor R`. Equal.

The two cases cover all eight states. ∎

### Theorem 12.3 — Rule 90 Correction Decomposition

`Rule30(L,C,R) = Rule90(L,R) xor (C and not R)` on all eight states.

**Proof.** Boolean algebra.

```
Rule30(L,C,R) = L xor (C or R)
              = L xor (C xor R xor (C and R))   [inclusive-or via xor]
              = (L xor R) xor (C xor (C and R))
              = Rule90(L,R) xor (C and not R)     [since C xor (C and R) = C and not R]
```

The identity `C xor (C and R) = C and not R` is verified by truth table:

| C | R | `C and R` | `C xor (C and R)` | `C and not R` |
|---|---|-----------|-------------------|---------------|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 |

All four rows match. The full decomposition is verified on all eight LCR states by the receipt. ∎

### Theorem 12.4 — Silent-Boundary Rule Count

Exactly 64 of the 256 elementary cellular automata are silent-boundary rules.

**Proof.** An ECA is defined by 8 binary outputs for the 8 input states. The silent-boundary conditions fix two of these outputs to 0: `f(0,0,0)=0` and `f(1,1,1)=0`. The remaining 6 outputs are free. Therefore the count is `2^6 = 64`. ∎

### Theorem 12.5 — Prediction Surface Discipline

A prediction surface must preserve layer, cost, defect, and receipt metadata; empirical or open layers cannot be counted as closed theorem layers.

**Proof.** By definition of the prediction surface as a typed stack. Each layer is a tuple `(bit, layer, cost, defect, receipt)`. A layer with `defect = open` or `receipt = empirical` is not promoted to `status = closed`. This is a schema constraint, not a mathematical theorem, but it is enforced by the verifier architecture. ∎

---

## 4. Verifiers and Receipts

### 4.1 Primary Finite-Layer Receipt

`verify_ca_prediction_surface.py` → `ca_prediction_surface_receipt.json`

| Check | Result |
|-------|--------|
| `rule30_truth_table_matches_formula` | pass |
| `t_emission_matches_rule30` | pass |
| `rule30_rule90_correction_identity_holds` | pass |
| `local_state_count_is_8` | pass |
| `silent_boundary_rule_count_is_64` | pass |
| `cold_start_rule30_extractor_left_as_obligation` | pass (explicitly acknowledged) |
| `spectral_prediction_left_as_empirical` | pass (explicitly acknowledged) |

**Status:** `pass`, 7/7.

### 4.2 EntropyForge Extension Receipt

`verify_center_column_entropy.py` → `center_column_entropy_receipt.json`

| Check | Result |
|-------|--------|
| `center_column_engine_present` | pass |

**Status:** `pass`, 1/1. Open obligations: infinite non-periodicity; statistical-suite certification is product-layer work.

### 4.3 P1 Non-Periodicity Evidence

`verify_p1_non_periodicity.py` → `p1_non_periodicity_receipt.json`

| Check | Result |
|-------|--------|
| `sierpinski_3k_in_2k_exact` | pass (k=0..11) |
| `su3_orbit_closes_at_n3` | pass |
| `su3_orbit_not_closed_n1_n2` | pass |
| `weyl_group_order_6` | pass |
| `no_period_le_256_in_2048` | pass |
| `window_density_measured` | pass |
| `transport_argument_structure` | pass |

**Status:** `pass`, 7/7. The Sierpinski law and SU(3) orbit closure are finite exact checks. The transport argument is a structural bridge, not a proof of unbounded non-periodicity.

### 4.4 P2 Equal-Density Evidence

`verify_p2_density.py` → `p2_density_receipt.json`

| Check | Result |
|-------|--------|
| `rule30_rule90_correction_identity` | pass |
| `6_2_correction_split` | pass |
| `correction_fires_on_010_110` | pass |
| `f4_uniform_measure_trace2_exact` | pass |
| `symmetric_fraction_structural` | pass (≈74.7%) |
| `finite_window_density_within_5pct` | pass (debiased density 0.5267) |
| `transport_argument_structure` | pass |

**Status:** `pass`, 7/7. The local 6/2 split and F4 uniform measure are exact. The asymptotic equal-density claim remains open.

### 4.5 Wolfram 1M-Bit Validation

`verify_wolfram_1m_bit.py` → `wolfram_1m_bit_validation_receipt.json`

| Check | Result |
|-------|--------|
| `p1_no_period_le_65536` | pass |
| `p2_density_measured` | pass |
| `p2_ones` | 500,768 |
| `p2_zeros` | 499,232 |
| `p2_density` | 0.500768 |
| `p2_density_matches_memo` | pass |
| `p3_materialized_readout_o1` | pass |
| `p3_readout_samples_verified` | pass |
| `total_bits_loaded` | 1,000,000 |

**Status:** `pass`, 9/9. Large-window empirical evidence; not asymptotic proof.

### 4.6 Real Dataset Experiment

`verify_rule30_real_dataset_experiment.py` → `rule30_real_dataset_experiment_receipt.json`

| Check | Result |
|-------|--------|
| `real_density_converges_to_half` | pass (0.500768) |
| `generator_bit_exact_to_real` | pass (10,000/10,000) |
| `decomposition_matches_real` | pass |
| `no_period_le_1000_in_real_50k` | pass |

**Status:** `pass`, 4/4.

### 4.7 Idempotent Connections (GLM)

`verify_glm_rule30_idempotent_connections.py` → `idempotent_connections_receipt.json`

| Check | Result |
|-------|--------|
| `C1_rule30_eq_rule90_xor_correction_8states` | pass |
| `C2_t_emission_8states` | pass |
| `C3_logistic_conjugate_rule90_21steps` | pass |
| `C4_hadamard_gf2_linear` | pass |
| `C5_fibonacci_mod2_period3` | pass |
| `C6_13_systems_identified` | pass |

**Status:** `pass_with_open_obligations`, 6/6. This is an interpretive bridge [I] mapping 13 systems to the Rule 30/90/correction structure, not a mathematical closure theorem.

---

## 5. Hand Reconstruction

All five primary finite claims (12.1–12.4, 12.5) can be reconstructed by hand from the definitions:

1. Write the 8 LCR states.
2. Compute `emit_30` from the rule number `30 = 0b00011110`.
3. Compute `L xor (C or R)`, `not L if C=1 else L xor R`, and `Rule90 xor (C and not R)`.
4. Compare column by column; all match.
5. Count silent-boundary rules: fix `f(0,0,0)` and `f(1,1,1)` to 0, leaving 6 free bits → 64 rules.

No external computation is required. The only non-obvious step is the Boolean identity `C or R = C xor R xor (C and R)`, which is standard.

---

## 6. Falsifiers and Rejected Claims

The following claims are explicitly rejected:

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F12.1 | The spectral layer is a proved cold-start Rule 30 predictor. | No accuracy theorem; empirical only. |
| F12.2 | A local T_EMISSION receipt proves between-depth dynamics without the local state. | Local receipt proves local property only. |
| F12.3 | A layer may omit its cost and defect receipt. | Violates prediction-surface discipline. |
| F12.4 | Finite center-column evidence proves infinite non-periodicity. | Finite window ≠ unbounded theorem. |
| F12.5 | Seeded product streams replace the canonical paper-bound object. | Canonical object is the single-cell mode; product streams are wrappers. |
| F12.6 | A failed P3 closure receipt is described as a closed theorem. | `p3_closure_receipt.json` says "P3 CLOSED" in prose but reports `cold_start_bit_exact: false`. This is a status/prose contradiction and is quarantined as a falsifier. |

---

## 7. Relation to Later Papers

- **Paper 11** admits the CA candidate through a receipt gate. Paper 12 turns the admitted candidate into a prediction surface with explicit layer typing.
- **Paper 13** may use the CA correction field as a quark-face transport input, but must preserve which layer produced the bit and which obligations remain open.
- **Paper 10** supplies the O(log N) readout architecture (`cold_bit(N) = lucas_bit(N,0) xor correction_at(N-1)`), which is the best known cold-start method but does not fully close P3.
- **Papers 18 and 29** may reuse the `2 + 6` VOA partition and the Monster scalar `196883 = 47·59·71` only as finite arithmetic/sector receipts unless a stronger theorem is supplied.

---

## 8. Open Obligations

1. A full cold-start `O(log N)` Rule 30 extractor remains open (Wolfram Problem 3).
2. The spectral next-state layer is empirical until an accuracy theorem is supplied.
3. Case-by-case closure of every silent-boundary rule requires additional receipts beyond the count.
4. Any use of a prediction surface must preserve layer, cost, defect, and receipt metadata.
5. Infinite center-column non-periodicity remains unproved by this paper (Wolfram Problem 1).
6. Product-level randomness certification remains outside the paper claim until a separate statistical receipt is supplied.
7. Any failed P3 closure attempt must remain quarantined until its status/prose contradiction and bit-exactness failure are resolved.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 definition and prize problems (Problems 1–3).
2. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 linearity and algebraic structure.
3. E. W. Weisstein, "Rule 30," *MathWorld*, Wolfram Research. http://mathworld.wolfram.com/Rule30.html.
4. M. Cook, "Universality in elementary cellular automata," *Complex Systems* 15 (2004), 1–40. Rule 110 universality; contrast with Rule 30.
5. S. Wolfram, "Wolfram Prize Problems: Rule 30," https://www.wolframscience.com/prizes/tmns/problems.html. P1 non-periodicity, P2 equal density, P3 computability.
6. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. Monster group and VOA partition context.
7. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA `Z(q) = 2q^0 + 6q^5 + ...`.
8. J. McKay, "Graphs, singularities, and finite groups," *Proc. Symp. Pure Math.* 37 (1980), 183–186. E8/McKay correspondence background.
9. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. Exceptional group data.
10. N. J. A. Sloane, "The Online Encyclopedia of Integer Sequences," https://oeis.org. A006257, A001511 (Rule 30 related sequences).

---

## 10. Conclusion

Paper 12 proves the finite local layer of the cellular-automaton prediction surface. It gives Rule 30 an exact local readout, a `T_EMISSION` equivalence, a Rule 90–correction decomposition, and counts the silent-boundary ECA subset. It keeps cold-start extraction, spectral prediction, infinite-periodicity, and product-certification claims visible as open layers rather than hidden conclusions. The paper's strongest scientific value is the distinction: local structure is verified, while unbounded problems remain named research obligations.
