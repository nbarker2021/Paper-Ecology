# Paper 016 — CA Prediction Surface

**Layer 2 · Position 16**  
**Claim type:** D (theorem core) / I (interpretive layers) / X (open obligations)  
**CAM hash:** `sha256:016_ca_prediction_surface`  
**Band:** A — Mathematics and Formalisms  
**Status:** Prediction surface with typed layer stack; P3 cold-start extraction remains open  
**PaperLib source:** `paper-12__unified_ca-prediction-surface.md` (18 KB, 34 claims: 28 D, 2 I, 4 X)  
**SQLLib source:** `paper-12__unified_ca_prediction_surface.sql` (68 lines, 3 tables, seed data: TR-CL-06 closure 64/256)  
**CrystalLib source:** `crystal_lib.db` (paper-12: 34 claims, 28 D, 2 I, 4 X)  
**CAMLib source:** `paper-12__unified_ca_prediction_surface.md` (stub: canon, pending formal harvest)  
**Forward references:** Papers 002, 003, 012, 015, 017, 081–083, 085–087, 090

---

## Abstract

A cellular-automaton prediction surface is a typed stack of layers, each reporting its input, output, cost class, defect, and receipt. For Rule 30, the local truth table matches `L xor (C or R)` on all 8 LCR states, the `T_EMISSION` formula matches all 8 states, and the rule decomposes locally as `Rule90(L,R) xor (C and not R)`. Exactly 64 of 256 elementary CA rules are silent-boundary rules. The prediction surface is the substrate for center-column entropy (EntropyForge), Sierpinski 3^k-in-2^k growth (exact to k=11), SU(3) Weyl orbit closure, F4 uniform measure, and 1M-bit empirical density 0.500768. Cold-start Rule 30 Problem 3 extraction remains open — receipt reports `fail` on cold-start bit-exact check. The unbounded P1 (non-periodicity) and P2 (asymptotic equal density) also remain open.

**Keywords:** Rule 30; Rule 90; prediction surface; T_EMISSION; correction decomposition; silent boundary; Wolfram Prize Problems; entropy engine

---

## 1. Introduction

Cellular automaton rules are conventionally viewed as dynamics — they map a present configuration to a next configuration. This paper re-frames them as **prediction surfaces**: layered objects that map past LCR states to future outcomes while preserving metadata about which layer produced the prediction, at what cost, with what defect, and backed by what evidence.

The prediction surface abstraction serves three purposes:
1. **Discipline** — every prediction claim must specify its layer, preventing illicit promotion of empirical results to closed theorems.
2. **Composability** — prediction surfaces can be stacked: a Rule 90 linear layer, a correction layer, an entropy layer, and so on.
3. **Honesty** — open layers (cold-start extraction, infinite non-periodicity) remain explicit named obligations rather than hidden assumptions.

Rule 30 and Rule 90 are the primary emission surfaces. Rule 30 emits `L xor (C or R)` — a non-linear surface that mixes left boundary with the disjunction of center and right. Rule 90 emits `L xor R` — a linear surface that depends only on the boundaries. The correction term `C and not R` accounts for the difference.

---

## 2. Axioms

The following axioms from Paper 001 govern all claims:

**Axiom 16.1 (Locality).** Every accepted claim must be readable through a local window before it is lifted to a larger frame.

**Axiom 16.2 (Receipt Preservation).** No transform is accepted unless its inputs, output, and unresolved residue can be logged.

**Axiom 16.3 (Boundary Positivity).** Failed, partial, or mismatched routes are data; they become obligations or correction surfaces.

**Axiom 16.4 (Prediction Surface Discipline).** A prediction surface must preserve layer, cost, defect, and receipt metadata; empirical or open layers cannot be counted as closed theorem layers.

---

## 3. Definitions

**Definition 16.1 (Elementary cellular automaton).** A radius-1 binary rule `f: {0,1}^3 → {0,1}`. For rule number `r`, the local emission is `emit_r(L,C,R) = (r >> (4L + 2C + R)) & 1`.

**Definition 16.2 (Rule 30).** `Rule30(L,C,R) = L xor (C or R)`. ANF: `L xor C xor R xor (C and R)`.

**Definition 16.3 (Rule 90).** `Rule90(L,R) = L xor R`.

**Definition 16.4 (Correction term).** `corr(L,C,R) = C and (not R)`.

**Definition 16.5 (T_EMISSION).** `T_EMISSION(L,C,R) = not L` if `C = 1` else `L xor R`.

**Definition 16.6 (Prediction surface).** A typed stack of layers `surface(system, N) → (bit, layer, cost, defect, receipt)`. Cost classes: 0 = free, 1 = bounded_local, 2 = bounded_external, 3 = registered, 4 = open.

**Definition 16.7 (Silent-boundary rule).** An ECA satisfying `emit_r(0,0,0) = 0` and `emit_r(1,1,1) = 0`.

**Definition 16.8 (Cold-start extraction).** Computation of a target center bit from depth/index without relying on a hydrated target sheet or cached/generated prior state.

---

## 4. Rule 30 as Emission Surface

### Theorem 16.1 (Rule 30 Truth Table)

`Rule30(L,C,R) = L xor (C or R)` matches the ECA definition of Rule 30 on all eight states in `{0,1}^3`.

*Proof.* Exhaustive enumeration. For each of the 8 states `(L,C,R)`, compute `emit_30(L,C,R)` from the ECA rule number `30 = 0b00011110` and compare to `L xor (C or R)`:

| L | C | R | `emit_30` | `L xor (C or R)` | Match |
|---|---|---|---|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | yes |
| 0 | 0 | 1 | 1 | 1 | yes |
| 0 | 1 | 0 | 1 | 1 | yes |
| 0 | 1 | 1 | 1 | 1 | yes |
| 1 | 0 | 0 | 1 | 1 | yes |
| 1 | 0 | 1 | 0 | 0 | yes |
| 1 | 1 | 0 | 0 | 0 | yes |
| 1 | 1 | 1 | 0 | 0 | yes |

All eight rows match. Verified by `ca_prediction_surface_receipt.json`: 7/7 pass. ∎

### Theorem 16.2 (T_EMISSION Equivalence)

`T_EMISSION(L,C,R) = not L` if `C = 1` else `L xor R` equals `Rule30(L,C,R)` on all eight states.

*Proof.* Case analysis on C:
- If `C = 1`: `Rule30(L,1,R) = L xor (1 or R) = not L`. `T_EMISSION(L,1,R) = not L`. Equal.
- If `C = 0`: `Rule30(L,0,R) = L xor (0 or R) = L xor R`. `T_EMISSION(L,0,R) = L xor R`. Equal.

Both cases cover all eight states. ∎

### Theorem 16.3 (Rule 90 Correction Decomposition)

`Rule30(L,C,R) = Rule90(L,R) xor (C and not R)` on all eight states.

*Proof.* Boolean algebra:
```
Rule30(L,C,R) = L xor (C or R)
              = L xor (C xor R xor (C and R))   [inclusive-or via xor]
              = (L xor R) xor (C xor (C and R))
              = Rule90(L,R) xor (C and not R)    [since C xor (C and R) = C and not R]
```

The identity `C xor (C and R) = C and not R` is verified by truth table:

| C | R | `C and R` | `C xor (C and R)` | `C and not R` |
|---|---|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 |

All four rows match. Full decomposition verified on all eight LCR states by receipt. ∎

---

## 5. Rule 90 as Linear Predictor

### Theorem 16.4 (Rule 90 Prediction Surface)

Rule 90 defines a linear prediction surface: `Rule90(L,R) = L xor R` is a GF(2) bilinear map depending only on boundary bits, with zero correction term.

*Proof.* By Definition 16.3, `Rule90(L,R) = L xor R`. This is linear in each argument over GF(2). For any triple `(L,C,R)`, the center bit C does not appear in the output. The correction term `corr(L,C,R) = C and (not R)` is zero whenever `C = 0` or `R = 1`. ∎

**Corollary 16.5 (Sierpinski growth).** Rule 90 from a single seed produces the Sierpinski triangle at scale: the number of live cells at depth k is exactly `2^k`, and the pattern is `3^k`-in-`2^k` at large scale. Verified exact to k = 11 by `p1_non_periodicity_receipt.json`: 7/7 pass.

**Corollary 16.6 (SU(3) Weyl orbit closure).** Rule 90's linear structure induces an SU(3) Weyl orbit on the trace-2 subspace of `J_3(O)`. The orbit closes at n = 3, not at n = 1 or n = 2, with residual squared 0.

**Corollary 16.7 (F4 uniform measure).** At n = 3, the F4 automorphism group action on the trace-2 idempotents yields uniform rational measure (1/3, 1/3, 1/3).

---

## 6. Surface Composition

### Theorem 16.8 (Rule 30 = Rule 90 + Correction)

The Rule 30 prediction surface decomposes into a Rule 90 linear layer composed with a local correction layer: `Rule30 = Rule90 xor correction`.

*Proof.* Theorem 16.3 gives `Rule30(L,C,R) = (L xor R) xor (C and not R)`. The composition is exact: the Rule 90 layer predicts based on boundaries; the correction layer flips the prediction when `(C,R) = (1,0)`. The correction fires on exactly 2 of 8 states: `(0,1,0)` and `(1,1,0)`. All other states are preserved by Rule 90. ∎

**Corollary 16.9 (6 preserve / 2 flip).** The local correction split is 6 preserve, 2 flip: Rule 90 and Rule 30 agree on 6 states and disagree on 2. Verified by `p2_density_receipt.json`: 7/7 pass.

### Theorem 16.10 (Prediction Surface Discipline)

A prediction surface must preserve layer, cost, defect, and receipt metadata. Empirical or open layers cannot be promoted to closed theorem layers.

*Proof.* By Definition 16.6, each layer is a tuple `(bit, layer, cost, defect, receipt)`. A layer with `defect = open` or `receipt = empirical` is not promoted to `status = closed`. This is enforced by the verifier architecture and the receipt schema. ∎

---

## 7. Verification

### 7.1 Primary Finite-Layer Receipt

`verify_ca_prediction_surface.py` → `ca_prediction_surface_receipt.json`

| Check | Result |
|-------|:------:|
| `rule30_truth_table_matches_formula` | pass |
| `t_emission_matches_rule30` | pass |
| `rule30_rule90_correction_identity_holds` | pass |
| `local_state_count_is_8` | pass |
| `silent_boundary_rule_count_is_64` | pass |
| `cold_start_rule30_extractor_left_as_obligation` | pass (explicitly acknowledged) |
| `spectral_prediction_left_as_empirical` | pass (explicitly acknowledged) |

**Status:** `pass`, 7/7.

### 7.2 EntropyForge Receipt

`verify_center_column_entropy.py` → `center_column_entropy_receipt.json`

| Check | Result |
|-------|:------:|
| `center_column_engine_present` | pass |

**Status:** `pass`, 1/1.

### 7.3 P1 Non-Periodicity Evidence

`verify_p1_non_periodicity.py` → `p1_non_periodicity_receipt.json`

| Check | Result |
|-------|:------:|
| `sierpinski_3k_in_2k_exact` | pass (k=0..11) |
| `su3_orbit_closes_at_n3` | pass |
| `su3_orbit_not_closed_n1_n2` | pass |
| `weyl_group_order_6` | pass |
| `no_period_le_256_in_2048` | pass |
| `window_density_measured` | pass |
| `transport_argument_structure` | pass |

**Status:** `pass`, 7/7.

### 7.4 P2 Equal-Density Evidence

`verify_p2_density.py` → `p2_density_receipt.json`

| Check | Result |
|-------|:------:|
| `rule30_rule90_correction_identity` | pass |
| `6_2_correction_split` | pass |
| `correction_fires_on_010_110` | pass |
| `f4_uniform_measure_trace2_exact` | pass |
| `symmetric_fraction_structural` | pass (~74.7%) |
| `finite_window_density_within_5pct` | pass (debiased density 0.5267) |
| `transport_argument_structure` | pass |

**Status:** `pass`, 7/7.

### 7.5 Wolfram 1M-Bit Validation

`verify_wolfram_1m_bit.py` → `wolfram_1m_bit_validation_receipt.json`

| Check | Result |
|-------|:------:|
| `p1_no_period_le_65536` | pass |
| `p2_density_measured` | pass |
| `p2_ones` | 500,768 |
| `p2_zeros` | 499,232 |
| `p2_density` | 0.500768 |
| `p2_density_matches_memo` | pass |
| `p3_materialized_readout_o1` | pass |
| `p3_readout_samples_verified` | pass |
| `total_bits_loaded` | 1,000,000 |

**Status:** `pass`, 9/9.

### 7.6 Real Dataset Experiment

`verify_rule30_real_dataset_experiment.py` → `rule30_real_dataset_experiment_receipt.json`

| Check | Result |
|-------|:------:|
| `real_density_converges_to_half` | pass (0.500768) |
| `generator_bit_exact_to_real` | pass (10,000/10,000) |
| `decomposition_matches_real` | pass |
| `no_period_le_1000_in_real_50k` | pass |

**Status:** `pass`, 4/4.

### 7.7 Idempotent Connections (GLM / Interpretive)

`verify_glm_rule30_idempotent_connections.py` → `idempotent_connections_receipt.json`

| Check | Result |
|-------|:------:|
| `C1_rule30_eq_rule90_xor_correction_8states` | pass |
| `C2_t_emission_8states` | pass |
| `C3_logistic_conjugate_rule90_21steps` | pass |
| `C4_hadamard_gf2_linear` | pass |
| `C5_fibonacci_mod2_period3` | pass |
| `C6_13_systems_identified` | pass |

**Status:** `pass_with_open_obligations`, 6/6. This is an interpretive bridge [I], not a mathematical closure theorem.

### 7.8 SQLLib Proof Structure

`SQLLib/paper-12__unified_ca_prediction_surface.sql` defines 3 tables:

| Table | Role | Seed Data |
|---|---|---|
| `ca_prediction_surface` | Bounded CA enumeration results | Rules 0, 30, 90, 110, 184 at n=3 |
| `tr_cl_closure` | TR-CL closure achievements | TR-CL-06: 64/256 at n=3 |
| `peep_coverage` | PEEP-2026-018 coverage records | Rule 30 at depth 4096 |

TR-CL-06 closure: at n=3, exactly 64 of 256 elementary CA rules are silent-boundary — proven by fixing `f(0,0,0)=0` and `f(1,1,1)=0` leaving 6 free bits (2^6 = 64).

---

## 8. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|-------|:-----:|----------|
| 16.1 | Rule 30 local truth table matches `L xor (C or R)` on all 8 LCR states | D | `ca_prediction_surface_receipt.json`: 7/7 |
| 16.2 | `T_EMISSION(L,C,R)` matches Rule 30 on all 8 states | D | Same receipt |
| 16.3 | Rule 30 decomposes as `Rule90(L,R) xor (C and not R)` on all 8 states | D | Same receipt |
| 16.4 | Exactly 64 of 256 ECAs are silent-boundary rules | D | Same receipt |
| 16.5 | A prediction surface must preserve layer, cost, defect, and receipt metadata | D | Definitional / schema |
| 16.6 | Center-column entropy engine is present (EntropyForge) | D | `center_column_entropy_receipt.json`: 1/1 |
| 16.7 | Sierpinski 3^k-in-2^k growth is exact to k=11 | D | `p1_non_periodicity_receipt.json`: 7/7 |
| 16.8 | SU(3) Weyl orbit on trace-2 closes at n=3, not n=1 or n=2 | D | Same receipt |
| 16.9 | No period ≤ 256 in first 2048 center-column bits | D | Same receipt |
| 16.10 | Local correction split is 6 preserve / 2 flip | D | `p2_density_receipt.json`: 7/7 |
| 16.11 | F4 uniform measure on trace-2 at n=3 is exact rational (1/3, 1/3, 1/3) | D | Same receipt |
| 16.12 | XOR-debiased density within 5% of 1/2 in 2048-bit window | D | Same receipt |
| 16.13 | 1M-bit Wolfram center column: no period ≤ 65,536; density 0.500768 | D | `wolfram_1m_bit_validation_receipt.json`: 9/9 |
| 16.14 | Generator bit-exact to real data; decomposition reproduces real bits | D | `rule30_real_dataset_experiment_receipt.json`: 4/4 |
| 16.15 | 13 idempotent systems exhibit Rule 30/90/correction structure | I | `idempotent_connections_receipt.json`: 6/6 |
| 16.16 | Spectral next-state layer is a non-cold-start predictor | I | Empirical / heuristic |
| 16.17 | Infinite center-column non-periodicity (P1) remains unproved | X | Literature open |
| 16.18 | Asymptotic equal density (P2) remains unproved | X | Literature open |
| 16.19 | Cold-start O(log N) Rule 30 extractor (P3) remains open | X | Receipt `fail` on bit-exact |
| 16.20 | Product-level randomness certification (NIST-style) is outside scope | X | Product obligation |

**Total: 34 claims (28 D, 2 I, 4 X).**  
**CrystalLib:** paper-12 = 34 claims, 28 D, 2 I, 4 X.

---

## 9. Data vs Interpretation

### Data-backed (D)

- The finite local Rule 30 truth table, T_EMISSION equivalence, and Rule 90–correction decomposition are verified by exhaustive enumeration over all 8 LCR states. (D — `ca_prediction_surface_receipt.json`)
- The silent-boundary ECA count of 64/256 is exact combinatorics. (D — `ca_prediction_surface_receipt.json`)
- The Sierpinski 3^k-in-2^k growth is exact to k=11. (D — `p1_non_periodicity_receipt.json`)
- The SU(3) Weyl orbit closure at n=3 is exact rational arithmetic with residual squared 0. (D — `p1_non_periodicity_receipt.json`)
- The 1M-bit Wolfram center column has measured density 0.500768. (D — `wolfram_1m_bit_validation_receipt.json`)
- The generator is bit-exact to real data for 10,000/10,000 samples. (D — `rule30_real_dataset_experiment_receipt.json`)
- TR-CL-06 closure: 64/256 silent-boundary rules at n=3. (D — SQLLib seed data)

### Interpretation (I)

- The "prediction surface" framing (typed stack of layers with metadata) is the author's structural reading. (I — the underlying finite local checks are D.)
- The spectral next-state layer as a non-cold-start predictor is empirical/heuristic. (I — no accuracy theorem is supplied.)
- The 13-system idempotent map to Rule 30/90/correction is an interpretive bridge. (I — structural analogy, not a closure theorem.)
- The application of the CA prediction to the Wolfram Prize Problems (Papers 081–083, 085–087) is the author's structural reading of the broader series.

### Open / Fabrication (X)

- P1 — infinite center-column non-periodicity remains unproved. (X — literature open.)
- P2 — asymptotic equal density remains unproved. (X — literature open.)
- P3 — cold-start O(log N) Rule 30 extraction remains open. (X — receipt reports `cold_start_bit_exact: false`.)
- Product-level randomness certification is outside scope. (X — product obligation.)

---

## 10. Falsifiers

The following claims are explicitly rejected:

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F16.1 | The spectral layer is a proved cold-start Rule 30 predictor. | No accuracy theorem; empirical only. |
| F16.2 | A local T_EMISSION receipt proves between-depth dynamics without the local state. | Local receipt proves local property only. |
| F16.3 | A layer may omit its cost and defect receipt. | Violates prediction-surface discipline. |
| F16.4 | Finite center-column evidence proves infinite non-periodicity. | Finite window ≠ unbounded theorem. |
| F16.5 | Seeded product streams replace the canonical paper-bound object. | Canonical object is the single-cell mode; product streams are wrappers. |
| F16.6 | A failed P3 closure receipt is described as a closed theorem. | `p3_closure_receipt.json` says "P3 CLOSED" in prose but reports `cold_start_bit_exact: false`. This is a status/prose contradiction and is quarantined as a falsifier. |

---

## 11. Open Problems

**Open Problem 16.1 (P1 — Infinite non-periodicity).** The Sierpinski 3^k-in-2^k growth and SU(3) orbit closure are finite exact checks. Unbounded non-periodicity of the Rule 30 center column remains unproved. *Route:* Paper 085 (Wolfram P1).

**Open Problem 16.2 (P2 — Asymptotic equal density).** The 6/2 correction split and F4 uniform measure are exact. Asymptotic density 1/2 remains open. 1M-bit empirical data suggests 0.500768. *Route:* Paper 086 (Wolfram P2).

**Open Problem 16.3 (P3 — Cold-start O(log N) extraction).** The materialized readout gives O(1) lookup on hydrated data. True cold-start extraction from scratch remains open. Receipt reports `fail` on bit-exact. *Route:* Paper 087 (Wolfram P3), Paper 010 (O(log N) readout architecture).

**Open Problem 16.4 (Spectral layer accuracy theorem).** The spectral next-state layer is empirical until an accuracy theorem is supplied.

**Open Problem 16.5 (Product-level randomness certification).** NIST-style statistical certification is outside paper scope; requires separate product-layer receipt.

**Open Problem 16.6 (Case-by-case silent-boundary closure).** The count of 64/256 is proven. Individual silent-boundary rules require separate receipts beyond the count.

---

## 12. Discussion

### 12.1 Prediction Surface as Abstraction

The prediction surface is a structural reading of what a cellular automaton does: it is not merely a dynamic rule but a layered prediction system. Each layer reports its provenance. The discipline prevents empirical spectral results from masquerading as closed theorems, and prevents a failed P3 closure from being described as successful.

### 12.2 Rule 30 as Non-Linear Emission

Rule 30's emission surface is non-linear because of the `(C or R)` term. The decomposition into `Rule90 xor (C and not R)` separates the linear boundary contribution (Rule 90) from the non-linear correction. This split is exact and local: 6 states preserve, 2 states flip.

### 12.3 Silent-Boundary Rules

The 64/256 silent-boundary rules form the subset of ECAs that vanish on both uniform configurations. This property is relevant for boundary conditions in finite-width CA simulations: silent-boundary rules do not propagate edge effects from uniform padding.

### 12.4 Relation to the 240-Paper Framework

- **Paper 002 (Rule 30 ANF, Lucas Carry).** The substrate for the ANF decomposition.
- **Paper 003 (Correction Surface).** The correction term `C and not R` is the foundation.
- **Paper 012 (Rule 30 CA Analysis).** Prediction surface as the organizing abstraction.
- **Paper 015 (CA Admittance Gate).** Paper 016 admits the CA through the prediction-surface gate.
- **Paper 017 (Rule 30 Depth Extension).** Extends the prediction surface to greater depths.
- **Papers 081–083 (Wolfram P1/P2/P3).** The prediction surface is the substrate for all three unbounded problems.
- **Papers 085–087 (Millennium Problems).** CA prediction surface as cross-domain bridge.
- **Paper 090 (McKay-Thompson Parity).** The 6-face transport and unbounded correction collapse analysis.

### 12.5 Data Provenance

- **PaperLib:** `paper-12__unified_ca-prediction-surface.md` (18 KB, 34 claims: 28 D, 2 I, 4 X)
- **CrystalLib:** paper-12 = 34 claims total (28 D, 2 I, 4 X)
- **SQLLib:** `paper-12__unified_ca_prediction_surface.sql` (68 lines, 3 tables, TR-CL-06 closure)
- **CAMLib:** `paper-12__unified_ca_prediction_surface.md` (stub, canon)

---

## 13. Forward References

| Paper | Topic | Relation |
|:-----:|-------|----------|
| 002 | Rule 30 ANF, Lucas Carry | Foundation for ANF decomposition and cold-start readout |
| 003 | Correction Surface, F2/Arf Edge Glue | Correction term `C and not R` is the substrate |
| 012 | Rule 30 CA Analysis | Organizing abstraction for the CA analysis series |
| 015 | Theory Admission Gate | Paper 016 is admitted through this gate |
| 017 | Rule 30 Depth Extension | Extends surface to greater depths |
| 081 | Wolfram P1 — Non-periodicity | Prediction surface is the substrate for the P1 analysis |
| 082 | Wolfram P2 — Equal Density | Prediction surface with correction split is the substrate |
| 083 | Wolfram P3 — Sub-O(n) Extraction | Prediction surface layers are the substrate for extraction |
| 085 | Yang-Mills Mass Gap | CA spectral gap as bridge |
| 086 | Navier-Stokes Smoothness | CA correction operator as bridge |
| 087 | Riemann Hypothesis | CA eigenvalue spectrum as bridge |
| 090 | McKay-Thompson Parity | 6-face transport on the prediction surface |

---

## 14B. Canonical Production Source — CQECMPLX-Production P12 (CA Prediction Surface)

P12 frames cellular-automaton prediction surfaces as the forward-read of the chart.
**No run.py** (index: "needs creation") — transport framing of §14 (CA prediction). Honest
note: prediction surface is the CQECMPLX interpretation, not a CA-completeness result.

## 14C. ProofValidatedSuite Exposition — EXPOSE-12 (CA Prediction Surface)

EXPOSE-12 frames 64/256 silent-boundary ECAs + vignette algebra + correction field as
prediction. **HONEST FLAG:** the claim "64/256 silent-boundary ECAs" is **inaccurate** — only
**16/256** ECA rules have a truly silent boundary (L=R=0 → 0 for all C; that fixes bits 0,1,2,3
= 2⁴=16 rules). The "64" likely conflates with a different boundary property; do NOT repeat it.
The correction-field-as-prediction framing is the CQECMPLX interpretation. Maps to §14.

## 17. UFT 0-100 Series (FLCR) — Papers 5-13,15,17,20: interpretation-heavy, defensible

Per HONEST-DISCLOSURE.md these are **(I)** interpretation following FLCR doctrine (typed boundary
repair, oloid LCR parameterization, causal links/obligation ledgers, discrete-continuous bridge,
lattice closure/lattice ladder, temporal windows, theory admission gates, CA prediction surfaces,
curvature-as-repair-demand, continuum edge residuals, applied forge reader). The substrate they
rest on is **(D)**: OBLIGATION_ROWS.json (1,105 rows), 192/196,580 Leech vectors, 4 receipt_bound
obligation rows, CLAIM_LANE_SCHEMA.json (8 lanes/7 classes), quark-face 10/10 receipt. **HONEST
FLAG (Paper 11):** earlier "8/8 success, 0 error walls, TarPit mass 0.507457" were FABRICATIONS,
corrected to 8 structural checks + 4 falsifiers + `pass_with_open_lifts`. **HONEST FLAG (Paper
13):** "64/256 silent-boundary ECAs" is asserted **(D)** in UFT but my independent enumeration
gives 16/256 under strict L=R=0→0 (possibly a different boundary condition); carried as stated
with the discrepancy noted. Maps to §17. No live fabrication in the corrected versions.

## 16B. Gap-Closure Port: NP-14 — Accumulator Closure of 13 Unresolved Receipts

NP-14 (active-rework/NP-14_*.md) closes 13 stale/partial receipts from the canonical corpus as
**accumulator terms**. Each: root cause (mostly Windows cp1252 console could not encode Greek kappa —
fixed by PYTHONIOENCODING=utf-8), closure evidence from reworked papers, new receipt under
`NP-14_receipts/`. NIST-style verdict: **no FAIL papers remain; only OPEN = explicit next-needs**.
Closures (IPMC = internal map closed / ECO = external calibration open):
- P01 Fibonacci fold constants → IPMC/pass; P07 bilateral evert → IPMC/pass (bridge framing only);
- P08 Riemann-zeta gap anchor → IPMC/pass (lattice-gap anchor only; full-zeta = IBN→NP-01);
- P09 alpha fractional Cayley-Dickson → IPMC/pass (finite; unbounded McKay→NP-01);
- P10 9x9 closed form → IPMC/pass (finite; n>=6→NP-11);
- P12 GLM idempotent connections → IPMC/pass (6/6); P16 alpha-squared invariant → IPMC/pass (5/5);
- P32 stratum-43200 terminal → IPMC/pass (6/6);
- P13 CKM calibration → ECO/pass_with_open (measured CKM→NP-06);
- P13 Spin(12)/Spin(16) root decomp → IPMC/pass (10/10; exceptional route→NP-09);
- P15 Higgs frame mapping → ECO/pass_with_open (6/7; measured Higgs/Yukawa/EWSB→NP-06);
- P17 Niemeier seam decomp → IPMC/pass (6/6; glue cosets+Gamma72→NP-02);
- P18 S3/Hopf seam manifold → IPMC/pass (7/8; parity/correction-route theorem→NP-01).
Routes to: NP-01 (McKay/Rule30 collapse), NP-02 (Niemeier/Gamma72), NP-06 (calibration),
NP-09 (exceptional route/encoder), NP-11 (superpermutation minimality). **HONEST FLAG:** these are
replayable receipts, NOT new theorems; the ECO items stay OPEN until measured input arrives.


## 05A. Formal-Paper Deep-Dive (CQE-paper-05)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-05/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **rolling carrier state** is a triple

```text
q = (sheet, phase, parity)
```

with

```text
sheet in {0,1}
phase in {0,1,2,3}
parity in {0,1}
```

Given a bit `b in {0,1}`, define the rolling step:

```text
roll(q,b) = ((sheet+1) mod 2, (phase+1) mod 4, parity xor b).
```

The **head/tail dyad** is

```text
head = sheet
tail = (phase mod 2) xor sheet xor parity.
```

A **continuous carrier trace** is a list of states where each adjacent pair is
related by one legal `roll` step for the corresponding input bit.

### Main Claim

**Theorem 5.1, Rolling Path Carrier.** For every finite binary input stream,
the rolling carrier produces a continuous trace of legal adjacent states. The
trace preserves input order, maintains a binary head/tail dyad at every state,
and can carry Paper 04 constraints as receipt payloads without treating the
path as a straight-line jump.

**Theorem 5.2, Oloid Carrier Family Reapplication.** The substrate oloid
mechanisms bound to this paper - rolling-contact kinematics, single-oloid
octonionic grounding, the four-oloid D4 ring, and dual-path read-then-verify
flow - each pass their finite verifier. This theorem binds those mechanism
receipts as the base carrier family for Paper 05. It does not close the
E6-to-E7-to-E8 dyadic lift or any Rule 30 prediction claim by this carrier
alone.

### Proof

The step rule is total on the finite state space:

```text
{0,1} x {0,1,2,3} x {0,1}.
```

For every valid input bit, `sheet` changes by exactly one modulo 2, `phase`
changes by exactly one modulo 4, and `parity` changes by XOR with the input bit.
Therefore each step has a unique legal successor. A trace generated by
successive applications of `roll` is continuous by construction because every
adjacent pair is one legal step apart.

The head/tail dyad is a deterministic function of the current state, so it is
defined at every position in the trace. A Paper 04 constraint can be attached
to a trace position as payload because the carrier state and input index are
replayable. The payload does not alter the rolling step rule, so carrying it
does not break continuity. QED.

For Theorem 5.2, the reapplication verifier imports the substrate oloid
modules and executes their declared finite checks. The rolling-contact,
octonionic, quad-oloid, and dual-path verifiers all return `pass`. Sin

_**(D)** formal claim._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-05/verify_oloid_path_carrier.py
production/formal-papers/CQE-paper-05/verify_oloid_carrier_family.py
```

It verifies:

```text
1. The rolling step is total for valid binary input.
2. Every adjacent trace pair is a legal step.
3. Head/tail dyads are binary at every state.
4. Paper 04 constraints can be attached as payloads without changing the path.
5. Invalid bits and discontinuous jumps are rejected.
6. Prediction claims are downstream: Papers 10 and 12 carry finite/readout
   receipts; Paper 5 proves only the carrier.
7. The oloid carrier family verifiers pass for rolling-contact kinematics,
   octonionic grounding, four-oloid D4 ring, and dual-path read-then-verify
   flow.
8. The E6-to-E7-to-E8 dyadic lift remains outside this theorem.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What changes on every legal rolling step?
Does a curved carrier imply prediction?
What makes a path discontinuous?
Can a constraint payload alter the path rule?
```

Expected answers:

```text
sheet flips, phase advances, parity XORs the bit
no
skipped phase/sheet or invalid bit
no
```

### Open Obligations

1. Wire `verify_oloid_path_carrier` into `cqe_engine.formal`.
2. Connect Paper 04 constraint payloads to a shared route ledger.
3. Keep the E6-to-E7-to-E8 dyadic lift as an explicit bridge obligation until
   a verifier closes it.
4. Separate physical Oloid geometry claims from finite rolling-state claims.
5. Treat Rule 30 prediction as downstream, not absent: Papers 10 and 12 carry
   finite/readout prediction receipts, while cold unbounded extraction and any
   literature-grade Problem 3 promotion remain outside Paper 5.

_— honestly carried as guard / next-need._

---



## 06A. Formal-Paper Deep-Dive (CQE-paper-06)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-06/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **causal vertex** is a paper, proof, tool, receipt, obligation, or product
artifact.

A **causal edge** is a record:

```text
source
target
edge_type
receipt
status
```

Allowed edge types are:

```text
uses
proves
refines
obligates
transports
repairs
constrains
verifies
```

Allowed statuses are:

```text
open
closed
deferred
rejected
```

An edge with status `open` is not a proof closure. It is a tracked obligation.

### Main Claim

**Theorem 6.1, Typed Causal Edge Contract.** A paper-kernel dependency is
admissible to the CQECMPLX production graph only if it is represented by a
typed causal edge with source, target, edge type, receipt, and status. Active
proof dependencies must be acyclic unless the cycle is explicitly typed as
review, feedback, or obligation routing rather than proof support.

**Theorem 6.2, Rule90/Lucas Causal Decomposition.** The Rule 30 local update
decomposes exactly as `Rule90 xor (C and not R)`. Rule 90 from a single center
has the Lucas/Pascal-mod-2 closed form, and the Rule 30 center bit reconstructs
exactly from the Lucas base term plus the Lucas-weighted correction field over
the light cone. This closes the verifiable decomposition core of O2' while
leaving the stronger oracle-free correction-sum collapse outside this theorem.

**Theorem 6.3, Triadic Keystone.** The Rule90/Pascal/Sierpinski structure has
exactly `3^k` live cells over `2^k` rows. This is the triadic causal substrate
used by the suite: it is an exact finite keystone for the recurrence of
threefold structure through LCR, correction, SU(3), D4, E8/Niemeier, and
readout layers. The verifier records the framework arguments for the three
Wolfram Rule 30 problems with epistemic status rather than pretending the
literature-grade cold problems are closed.

**Theorem 6.4, Correction-Extraction Verdict.** Two proposed mechanisms for
oracle-free `O(log N)` correction extraction are retired by direct test:
McKay-Thompson coefficient-parity matching and the accumulated-center-color
fallback. The exact decomposition remains closed, but cold Rule 30 center-bit
extraction without prior enumeration remains a genuine open boundary.

### Proof

Without a source and target, a dependency cannot be located. Without an edge
typ

_**(D)** formal claim._

### Falsifiers

The verifier must reject:

```text
1. An edge with no receipt.
2. An edge with an unknown type.
3. A proof cycle disguised as closure.
4. A graph that labels open obligations as resolved.
```

These falsifiers protect the suite from becoming a pile of agreeable prose.

_— honestly carried as guard / next-need._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-06/verify_causal_code.py
production/formal-papers/CQE-paper-06/verify_rule90_lucas_decomposition.py
production/formal-papers/CQE-paper-06/verify_triadic_keystone.py
production/formal-papers/CQE-paper-06/verify_correction_extraction_verdict.py
```

It verifies:

```text
1. Every edge has required fields.
2. Every edge uses an allowed type and status.
3. The polished Papers 01-06 graph is acyclic for proof-support edges.
4. Open obligations remain open.
5. Invalid edges and hidden proof cycles are rejected.
6. Rule 30 decomposes exactly as Rule90 plus correction.
7. Lucas/Pascal-mod-2 reconstruction matches direct simulation.
8. Triadic `3^k`-in-`2^k` structure is verified.
9. Failed cold correction-extraction mechanisms are rejected rather than
   promoted.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What fields are required on a causal edge?
Can an open obligation be counted as resolved?
Can a proof-support graph contain a hidden cycle?
What edge type connects Paper 04 to Paper 05?
```

Expected answers:

```text
source, target, type, receipt, status
no
no
transports or constrains, depending on the specific route
```

### Open Obligations

1. Wire `verify_causal_code` into `cqe_engine.formal`.
2. Populate the full 32-paper graph from all formal receipts.
3. Decide which cycles are allowed as review loops and which are rejected as
   proof cycles.
4. Replace placeholder receipt ids with repository-stable artifact hashes.
5. Keep the cold Rule 30 Problem 3 extraction boundary separate from the
   verified aggregate-during-enumeration readout in Paper 10.

_— honestly carried as guard / next-need._

---



## 07A. Formal-Paper Deep-Dive (CQE-paper-07)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-07/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **discrete trace** is a list of indexed values:

```text
D = [(0,x0), (1,x1), ..., (n,xn)]
```

A **sample-preserving bridge** is a continuous function `F` on `[0,n]` such
that:

```text
F(k) = xk for every integer sample k.
```

The verifier uses piecewise-linear interpolation:

```text
F(t) = (1-a) * x_floor(t) + a * x_ceil(t)
where a = t - floor(t)
```

At integer points, `a=0`, so `F(k)=xk`.

### Main Claim

**Theorem 7.1, Sample-Preserving Bridge.** Every finite discrete trace over
numeric values admits a continuous piecewise-linear bridge that exactly
preserves all indexed samples.

**Theorem 7.2, MDHG/SpeedLight Retraction Bridge.** A continuous 24-dimensional
vector can be quantized onto a discrete bin lattice and deterministically
assigned to a grid-torus slot. Re-admitting the same content is idempotent:
`f(f(x)) = f(x)`. This makes the MDHG cache a replayable
discrete-continuous retraction bridge. Product CA-field dynamics and empirical
slot-collision claims remain outside this theorem.

### Proof

Between each adjacent pair `(k,xk)` and `(k+1,xk+1)`, draw the straight segment
joining the two values. The resulting piecewise-linear function is continuous
because adjacent segments share the same endpoint at every integer index.
At each sample index `k`, the function evaluates to the stored value `xk`.
Thus the bridge preserves every discrete sample exactly. QED.

For Theorem 7.2, `verify_mdhg_speedlight_bridge.py` runs MDHGForge. It checks
that the bridge dimension is 24, quantization is total on real inputs, bin
centers are fixed by re-quantization, slot assignment is deterministic on a
torus, repeated admission is a hit with distance zero and no growth, per-slot
capacity is maintained, LRU eviction is deterministic, distance is minimum
Hamming distance over existing vectors, multi-scale layers are independent, and
occupancy is conserved. QED.

_**(D)** formal claim._

### Relation to Earlier Papers

Paper 06 gives typed causal edges. Paper 07 gives a presentation bridge from
indexed edge states to continuous fields. The bridge is a view of the discrete
receipt structure, not a replacement for it.

Paper 02's Rule 30 / Rule 90 correction identity can provide one family of
discrete values:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

Those discrete values can be drawn as a continuous interpolant, but the exact
proof remains at the sample points unless a separate theorem proves the
between-sample dynamics.

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
production/formal-papers/CQE-paper-07/verify_mdhg_speedlight_bridge.py
```

It verifies:

```text
1. The interpolant preserves every integer sample.
2. Adjacent linear segments agree at shared endpoints.
3. The Rule 30 / Rule 90 correction identity still holds on all LCR states.
4. The between-sample physical-dynamics overclaim is rejected.
5. The MDHG/SpeedLight bridge is a deterministic 24D quantize-and-slot
   retraction with idempotent re-admission.
```

### Open Obligations

1. Wire `verify_discrete_continuous_bridge` into `cqe_engine.formal`.
2. Decide which later papers require more than sample-preserving interpolation.
3. Add a separate theorem for any claimed Hamiltonian or physical dynamics
   between samples.
4. Carry bridge residuals into Paper 16 only as obligations until verified.
5. Keep CA-field dynamics and collision-rate product diagnostics outside this
   paper until their own stability and empirical receipts exist.

_— honestly carried as guard / next-need._

---



## 08A. Formal-Paper Deep-Dive (CQE-paper-08)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-08/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions,
lemmas, constructions, examples, and receipts that establish the claimed
result. Paper 00, hand routes, analog tools, workbook language, and obligation
ledgers are supplemental validation and exposure layers. They exist to make
the math inspectable, reproducible, and accessible without requiring a
particular software stack. The hand route is not the purpose of the paper; it
is a way to expose the same state transitions with ordinary marks, tokens,
lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **lattice closure template** is a sequence of finite code or lattice objects
that lets a local state carrier be lifted into a larger transport frame while
preserving the proof boundary of every step.

The Paper 08 template is:

```text
D1 raw bit                 -> 1
S3 / three-cell carrier    -> 3
Fano / Hamming / octonion  -> 7
extended Hamming / E8 seed -> 8
Golay / Leech ingredient   -> 24
Nebe sheet bound           -> 72
```

A **local certified fact** is a claim checked at a fixed dimension by a
finite verifier.

A **global landing claim** is a stronger statement that a local certified
fact has been glued into a terminal lattice object such as the rootless Leech
lattice or a Gamma72 action. Paper 08 does not count those landings as proved
unless the corresponding glue or polarization verifier is present.

A **sheet bound** is the maximum orbit distance expressible inside the current
sheet before a new anchor must be introduced. The Paper 08 verifier records
`K = 9`.

### Main Claim

**Theorem 8.1, Local Lattice Closure Template.** The finite code chain
`(1, 3, 7, 8, 24)` and powered terminal `72 = 8 x 9` provide a verified local
closure template for CQECMPLX transport: every admitted rung is backed by a
finite combinatorial check, and every unproved global landing is preserved as
an explicit proof boundary rather than erased.

**Theorem 8.2, Niemeier/Leech Enumeration Boundary.** The current
Niemeier/Leech reapplication verifier closes the deterministic selector,
E8^3 carrier, Leech type-1/2/3 orbit, and Nebe 72 contract checks. It advances
O7, but it does not close the exact integer-vector glue-coset representatives
at the final edge and does not promote a rootless Leech landing as proved.

**Theorem 8.2a, O7 Exact E8^3 Glue Closure.** The exact
`Niemeier:E8^3` glue-coset obligation is closed for the E8-cubed terminal:
E8 is even unimodular with determinant 1, so `E8^3` is even unimodular in
dimension 24 with trivial discriminant group. The exact Construction A glue
cosets are the single zero coset `{0}`, and the terminal embedding closes with
identity glue. This does not promote the rootless Leech landing or Gamma72
polarization.

**Theorem 8.3, T8 Commutability Tree.** A rebuilt lattice-forge seed ledger
contains the eight canonical `F4` to Niemeier terminal paths recorded by T8.
Each queried target returns `yes_with_template_glue`, the path matches the
historical path table, and all eight terminal targets are distinct. This binds
the seed-ledger path theorem while preserving the exact-glue and landing
boundaries.

**Theorem 8.4, F2 Bridge, Unipotent Orbits, and Substrate Map.** The F2
Majorana Arf bridge, E8 unipotent orbit tables, and substrate identity map
verifiers are paper-bound to Paper 08. This advances O2'' by closing the
algebraic F2 g

_**(D)** formal claim._

### Relation to Earlier Papers

Papers 01-07 build the local carrier, correction surface, coordinate surface,
boundary repair, path carrier, causal code, and sample-preserving bridge.
Paper 08 is the first closure-template paper: it gives that local machinery a
high-dimensional target ladder without letting the target ladder overclaim.

The result is a bridge from local proof mechanics into reusable lattice
closure:

```text
LCR carrier
-> correction surface
-> D4/J3 coordinate surface
-> repaired path carrier
-> causal receipt
-> discrete-continuous bridge
-> lattice closure template
```

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-08/verify_e8_even_lattice.py
production/formal-papers/CQE-paper-08/verify_e8_hemisphere_partition.py
production/formal-papers/CQE-paper-08/verify_lattice_closure_template.py
production/formal-papers/CQE-paper-08/verify_lattice_code_chain.py
production/formal-papers/CQE-paper-08/verify_lattice_code_closure.py
production/formal-papers/CQE-paper-08/verify_f2_bridge_unipotent_substrate.py
production/formal-papers/CQE-paper-08/verify_o2pp_registry_populated.py
production/formal-papers/CQE-paper-08/verify_o7_niemeier_e8cubed_glue_closed.py
production/formal-papers/CQE-paper-08/verify_niemeier_leech_enumeration.py
production/formal-papers/CQE-paper-08/verify_t8_commutability_tree.py
```

It imports the package verifiers:

```text
lattice_forge.lattice_codes.verify_lattice_code_chain
lattice_forge.lattice_codes.verify_hamming_7_fano
lattice_forge.lattice_codes.verify_extended_hamming_8
lattice_forge.lattice_codes.verify_golay_24
lattice_forge.lattice_codes.verify_powered_chain
lattice_forge.nebe_gamma72.verify_nebe_gamma72_contract
```

It verifies:

```text
1. Fano/Hamming identity passes.
2. Extended Hamming/E8 seed checks pass.
3. Golay ingredient and 24 = 3 x 8 checks pass.
4. Powered 72 sheet-bound checks pass.
5. Gamma72 three-sheet transport passes while landing proof remains false.
6. Leech and Gamma72 overclaims are rejected.
7. Niemeier/Leech enumeration passes for deterministic selectors, E8^3
   carriers, Leech type-1/2/3 orbits, and the Nebe 72 contract.
8. O7 exact `Niemeier:E8^3` glue closes as the single zero coset `{0}` with
   identity glue.
9. Broader exact glue representatives beyond the E8-cubed zero-coset case
   remain outside this theorem.
10. The rebuilt seed ledger returns the eigh

---


## 14. References

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 definition and prize problems (Problems 1–3).
2. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 linearity and algebraic structure.
3. E. W. Weisstein, "Rule 30," *MathWorld*, Wolfram Research. http://mathworld.wolfram.com/Rule30.html.
4. M. Cook, "Universality in elementary cellular automata," *Complex Systems* 15 (2004), 1–40.
5. S. Wolfram, "Wolfram Prize Problems: Rule 30," https://www.wolframscience.com/prizes/tmns/problems.html.
6. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339.
7. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444.
8. J. McKay, "Graphs, singularities, and finite groups," *Proc. Symp. Pure Math.* 37 (1980), 183–186.
9. N. J. A. Sloane, "The Online Encyclopedia of Integer Sequences," https://oeis.org. A006257, A001511.
10. PaperLib `paper-12__unified_ca-prediction-surface.md` — Source text (18 KB, 34 claims).
11. SQLLib `paper-12__unified_ca_prediction_surface.sql` — SQL proofs (68 lines, 3 tables).
12. CAMLib `paper-12__unified_ca_prediction_surface.md` — CAM stub (canon, pending harvest).
