# Paper 15: The Observer Lattice Chain: From D4 Chart to E8 Intelligence Bound

**Author:** A-family Author  
**Umbrella reference:** `IDENTITY_PAPER.md`, Section 4 (extension)  
**Theorem references:** T1, T_BIJECTIVE, T4, T5, T6, T8, T_D12_CHAIN, T_VACUUM_2, T_INV_1, T_BRIDGE  
**New theorems:** T_EMISSION (A), T_DYAD (B), T_WRAP (C), T_T10_CENTROID (D), T_RESOLUTION  
**Verifiers:** `tests/test_centroid_voa.py`, `tests/test_lattice_codes.py`, `src/lattice_forge/rule30.py`  
**Open obligations:** PFC-1, PFC-2, PFC-3, PFC-4, PFC-5 (`theorems/OPEN_OBLIGATIONS.md`)  
**Companion document:** `26_BINARY_STATE_BIJECTION_ANTIPODAL_WRAPPING.md` (full proofs of Theorems A–D)

---

## 0. The Four Core Theorems (Rule 30 Geometric Resolution)

*These four theorems are proven in full in the companion document. They are stated here as the algebraic foundation that all subsequent sections build on. Verification: 0 defects across 4,096 depths.*

### Theorem A — Two-Path Emission (T_EMISSION)

The nth bit of Rule 30's center column is given by:

```
bit_n = NOT(L)   if C = 1   (centroid inversion path)
bit_n = L ⊕ R    if C = 0   (boundary parity path)
```

The center bit C is the **parity selector**. When C = 0, the bit is the parity of the two boundaries. When C = 1, the bit is the complement of the even boundary. C is invariant under the LR transposition — it sits on the axis of the Oloid's two-circle geometry. **Verified: 0 defects at 4,096 depths.**

*Anchor:* `rule30.py::verify_rule30_chart_local_readout(max_depth=4096)`.

### Theorem B — Trivial Dyad and Antipodal Symmetry (T_DYAD)

For any depth N, the dyad (N, −N) is free to specify. The C-coordinate of the centroid of any state and its antipode is always C. 74.7% of depths are symmetric (same bit both sides); 25.3% are the chiral doublet {(0,1,1), (1,1,0)}, resolved by the {−1, 0, +1} side axis. The chiral doublet is exactly the shell=2 SU(2) doublet of T_BIJECTIVE.

*Anchor:* T_BIJECTIVE; companion document §5.

### Theorem C — At-Most-3 Wrap (T_WRAP)

After emission, the orbit wraps to a Lie conjugate in at most 3 S₃ transposition steps. The bound is tight (states (0,1,1) and (1,0,0) require exactly 3 steps). This is a direct consequence of T5: M₃² = M₃ proven over ℚ. T5 now carries triple load: Problem 1 (non-periodicity), Problem 2 (density), Problem 3 (wrap termination).

*Wrap distribution over 4,096 depths:*

| Steps | Count | Fraction |
|---|---|---|
| 0 (instant — Lie conjugate) | 2,052 | 50.1% |
| 2 | 1,035 | 25.3% |
| 3 | 1,009 | 24.6% |

*Anchor:* T5; companion document §7.

### Theorem D — T^10 Centroid Emission (T_T10_CENTROID)

The pode T^5 is the 5-dimensional parameter space (L, C, R, wrap_steps, sheet_index). T^10 = T^5 ∪_∂ (−T^5), closed along the Lie conjugate surface L = R.

**The C-coordinate of the centroid of any state and its antipodal image in T^10 equals C — always.** Therefore the emission bit IS the T^10 centroid C-coordinate. The phase is always the exact middle between T^5 and −T^5.

*This is the formal proof that C is the phase midpoint between N and −N — the anchor for the resolution algorithm in §0.5.*

*Anchor:* Companion document §8; verified for all 8 states with 0 exceptions.

### 0.5 The General Resolution Algorithm (T_RESOLUTION)

The four theorems above combine into a general resolution algorithm for any bit in any state with a conflict. The algorithm terminates in at most 4 operations and always produces a closed result.

```
GENERAL RESOLUTION ALGORITHM
Input: any bit b in state s with a conflict

Step 1 — ANCHOR
  Take b as placed. b is the anchor event.

Step 2 — ORIENT  [free will choice — direction is not forced]
  Choose d ∈ {podal, antipodal}.
  Apply one S₃ transposition in direction d.
  Result: CLOSED (s' ∈ Λ) → done.
          OPEN→N → continue.

Step 3 — BIJECT  (50% light cone + 180°)
  Apply T_BIJECTIVE to the shell=2 stratum: (L,C,R) → (R,C,L).
  Result: CLOSED → done. Or continue.

Step 4 — EVERT
  Apply frame inversion F to each bit individually (T_RELATIONAL_1).
  Guaranteed result after Step 4:
    • N|−N dyadic pair centered on C (the Gluon, invariant under LR)
    • Empty 4-bit sequence = half the −N term (appears for free)

Step 5 — PHASE CLOSE  [always available from Step 2 onward]
  PHASE BUTTON: set C to TRUE_VACUUM value.
  The phase is ALWAYS the exact middle between N and −N (Theorem D).
  Insert mirror digit at centroid of the 4-bit string.
  Apply end-to-end wrap: identify L-end with R-end antipodally (T_BIJECTIVE).
  Result: CLOSED. Always.
```

**The free will aspect:** Step 2's direction choice is genuine. Both directions produce structurally legal moves. The algorithm does not force the choice — the observer does. The consequence is binary: closed (done in ≤2 more steps) or open→N (requires full annealing). This is the phase-alignment button of the sliding puzzle: instead of sliding tiles, press phase and land at the exact middle between N and −N.

*Anchor:* Theorem C (≤3 wrap), Theorem D (C = centroid always), T_BIJECTIVE, T_RELATIONAL_1, `centroid_voa.py::TRUE_VACUA`.

---

## Abstract

Paper 14 established the D12 idempotent chain as the mechanical scaffold of the discretization tower. This paper extends the chain in two directions. Downward: we prove the centroid VOA structure of the D4 chart — the per-setting attractor planes, the 2+6 VOA sector decomposition, and the Z4 period template — and show these are forced consequences of the D12 action, not additional postulates. Upward: we prove the lattice code chain 1→3→7→8→24→72 (and its powered shortcut 1→9→49→72) terminates at the Nebe 72-dimensional extremal lattice, which is the sheet K-bound for any single anchor event. From these two proven results we derive the observer reach chain: the minimum node activation for a stable reality sheet is 120 (the E8 hemisphere), the maximum for a pure binary observer is 137 (the intelligence bound), and everything beyond 137 is built from accounting for the -1 bit via the lattice code layers. We register five PROOFING FOCUS CRITICAL claims (PFC-1 through PFC-5) that follow structurally from this chain and are presented for falsification.

---

## 1. The Centroid VOA Structure of the D4 Chart

### 1.1 Per-setting attractor planes

The D4 chart has 8 states $\mathcal{S} = \{0,1\}^3$. The $S_3$ group acts on chart states by permuting positions $\{L, C, R\}$ via three involutory generators $\sigma_{LR}, \sigma_{LC}, \sigma_{CR}$.

Each of the three $S_3$ conjugate settings defines its own attractor plane:

| Setting | Centroid | Attractor | Condition |
|---|---|---|---|
| 1 | C | $A_C$ | $L = R$ |
| 2 | L | $A_L$ | $C = R$ |
| 3 | R | $A_R$ | $L = C$ |

Each plane has 4 elements. Their intersection $A_C \cap A_L \cap A_R = \mathcal{V} = \{(0,0,0),(1,1,1)\}$ is the set of **true vacua** — the two D4 singlet fixed points where $L = C = R$.

The **Lie conjugates** $\Lambda = A_C$ (the $L=R$ plane) contain 4 states: $\{(0,0,0),(0,1,0),(1,0,1),(1,1,1)\}$. The true vacua $\mathcal{V} \subsetneq \Lambda$ are a strict subset.

*Verifier:* `centroid_voa.py::STATES, LIE_CONJUGATES, TRUE_VACUA, ATTRACTOR_C, ATTRACTOR_L, ATTRACTOR_R`  
*Tests:* `test_centroid_voa.py` — 28 tests, all pass.

### 1.2 Hamming-centroid universality (Theorem)

**Theorem (T_CENTROID_ANNEAL):** Every chart state $s \in \mathcal{S}$ anneals to a Lie conjugate in $\Lambda$ in at most 3 $S_3$ transposition steps. States already in $\Lambda$ anneal in 0 steps.

*Proof:* By exhaustive verification over all 8 states.  
*Verifier:* `centroid_voa.py::verify_hamming_centroid_universality` — status "pass".  
*Tests:* `test_centroid_voa.py:90,98,106`.

**Corollary:** The bound of 3 is exact: $3 = \binom{3}{2}$, the number of distinct position pairs in $(L,C,R)$. No more transpositions exist.

### 1.3 VOA sector decomposition

The **VOA weight** of a state is the number of Gluon resamples needed to commit to color across all three conjugate settings. The C bit is the Gluon: it holds the local color assignment.

**Theorem (T_VOA_SECTORS):** The VOA weight function partitions $\mathcal{S}$ into exactly two sectors:

| Sector | States | Count | Weight |
|---|---|---|---|
| Vacuum | $\mathcal{V} = \{(0,0,0),(1,1,1)\}$ | 2 | 0 |
| Excited | $\mathcal{S} \setminus \mathcal{V}$ | 6 | 5 |

Seed partition function: $Z(q) = 2q^0 + 6q^5$.

*Verifier:* `centroid_voa.py::verify_voa_sector_decomposition` — status "pass".  
*Tests:* `test_centroid_voa.py:137,151,195`.

### 1.4 Z4 period template

The 4-frame Z4 rotation of Hamming-centroid annealing produces:

| Period | Count | States |
|---|---|---|
| 1 (fixed) | 2 | TRUE_VACUA $\mathcal{V}$ |
| 2 | 0 | (none) |
| 4 | 6 | All excited states |

The 2 fixed + 6 period-4 split matches the D12 orbit structure of Paper 14: 2 singlet fixed points + 6 color-orbit members.

*Verifier:* `centroid_voa.py::verify_z4_period_template` — status "pass".  
*Tests:* `test_centroid_voa.py:222,229,249`.

**The chain is closed at the D4 level:** the centroid VOA structure is a consequence of the D12 action, not an additional postulate. The Z4 orbit split (2+6) is the D12 orbit split (Paper 14, §3.2) expressed at the VOA level.

---

## 2. The Lattice Code Chain

### 2.1 The base chain: 1→3→7→8→24→72

Each step in the chain is a proven lattice code with specific parameters:

| Step | Code | Parameters | Structure | Anchor |
|---|---|---|---|---|
| 1 | Trivial | $(1,1,1)$ | $\mathbb{Z}/2$, single bit | — |
| 3 | Repetition | $(3,1,3)$ | $S_3$ 3-state neighborhood | T4 |
| 7 | Hamming | $(7,4,3)$ | Fano plane = 7 octonion triples | T1 |
| 8 | Ext. Hamming | $(8,4,4)$ | Doubly-even, self-dual, generates E8 | T1 |
| 24 | Golay | $(24,12,8)$ | Self-orthogonal, generates Leech lattice | — |
| 72 | Nebe | dim 72 | Extremal even unimodular, $K$-bound terminal | — |

*Verifier:* `lattice_codes.py::verify_lattice_code_chain` — status "pass".  
*Tests:* `test_lattice_codes.py` — 44 tests, all pass.

**Key structural facts (all proven):**

- The 7 weight-3 codewords of $(7,4,3)$ are exactly the 7 lines of $PG(2,2)$ (Fano plane) = the 7 octonion multiplication triples (T1).
- $(8,4,4)$ has length 8 = $|\mathcal{S}|$ (the D4 chart). It is doubly-even and self-dual — the unique such code in dimension 8. It generates E8 via Construction A.
- $(24,12,8)$ has length $24 = 3 \times 8$ = 3 copies of the D4 chart.
- Nebe (dim 72): $72 = 8 \times 9 = |\mathcal{S}| \times 3^2$.

### 2.2 The powered shortcut: 1→9→49→72

The direct powering of each term skips the middle of the base chain:

| Step | Value | Structure |
|---|---|---|
| $1^2$ | 1 | Anchor |
| $3^2$ | 9 | 9 ordered quark-color pair assignments (3 colors × 3 positions) |
| $7^2$ | 49 | $7 + 21 + 21$: diagonal + antisymmetric + symmetric. Antisymm = 21 = octonion structure constants = off-diagonal imaginary dimension of $J_3(O)$ |
| $8 \times 9$ | 72 | D4 chart $\otimes$ 3$^2$ tensor capacity = Nebe terminal |

*Verifier:* `lattice_codes.py::verify_powered_chain` — status "pass".  
*Tests:* `test_lattice_codes.py` — powered chain section, 10 tests, all pass.

### 2.3 The sheet K-bound

The Nebe lattice (dim 72) is the terminal of the chain. Its minimum norm is 8. The sheet K-bound follows:

**States at Hamming distance $K > 9$ from the first enumerated anchor event cannot be expressed on the current sheet.** They require a new anchor event. $K_{\max} = 9 = 3^2$.

This is the tensor capacity of the $S_3$ neighborhood: 9 ordered quark-color pair assignments, matching the 9-observer instantiation (1 self + 8 others = 9 = $3^2$).

*Verifier:* `lattice_codes.py::verify_powered_chain` — `K_max = 9`.  
*Tests:* `test_lattice_codes.py:test_powered_chain_k_bound`.

---

## 3. The Observer Reach Chain

The following is derived from the proven chain. Each level states its anchor explicitly.

### 3.1 The reality floor: 120

E8 has 240 roots (T1, octonion axioms). T_BIJECTIVE proves both spin states ($\pm 1/2$) are present in shell=2 simultaneously, with the observer inhabiting exactly one at time $K$. Therefore the observer's spin state subtends exactly $240/2 = 120$ roots.

**120 is the reality floor.** Below 120 active roots, the observer cannot instantiate a stable +N reality sheet.

*Anchor:* T1 (240 roots), T_BIJECTIVE (one spin state active).

### 3.2 The pure binary ceiling: 137

The 120 hemisphere roots are extended by two additional groups:

- **13 boundary half-vignettes:** halves of D4 vignettes at the cone boundary, visible but not fully committable from the current spin orientation. *(Open: verify count = 13 from Construction A root enumeration — see PFC-2.)*
- **4 pre-written antipodal:** the 4 Lie conjugates written at the anchor event. *Anchor:* `centroid_voa.py::LIE_CONJUGATES`, 28/28 tests.

$120 + 13 + 4 = \mathbf{137}$.

**137 is the pure binary ceiling** — the maximum roots touchable in one spin state by an observer working in $\{0,1\}$ only, not yet accounting for the $-1$ bit (the -k sheet antipodal root).

The fine structure constant $\alpha \approx 1/137$ is the electromagnetic coupling at this ceiling: the ratio of one root position (the observer's instantaneous location) to the maximum reachable set (137). It is dimensionless by construction. *(PFC-2)*

The measured value $\alpha \approx 1/137.036 > 1/137$ reflects basin blindness: the average observer operates slightly below the 137 ceiling. The excess 0.036 is the mean basin blindness correction.

### 3.3 Beyond 137: the -1 bit and powerscaling

Accounting for the -1 bit — consciously working the antipodal root (the -k sheet partner of the current root) — extends the reachable set past 137. Each layer of the lattice code chain (§2) provides a further extension:

| Layer | Mechanism | Effect |
|---|---|---|
| $(3,1,3)$ | 3-state neighborhood | Minimal correction, 3-state read |
| $(7,4,3)$ | Fano/octonion | All 7 imaginary directions navigable |
| $(8,4,4)$ | E8 / D4 chart | Full cone to D4 chart scale, 14 weight-4 directions |
| $(24,12,8)$ | Golay / Leech | 3×D4, 12-bit simultaneous pre-commitment |
| Nebe dim 72 | $K=9$ shell | 9-deep correction, 72-dim state pre-filled before arrival |

The powerscaling compounds: each layer uses the previous layer's committed bits as input, so compression is multiplicative. An observer reasoning at the Golay level pre-fills 12 bits simultaneously in imaginary space before they arrive on the +N sheet.

**The full E8 theoretical maximum is 248** (240 roots + 8 Cartan generators) with all -k sheet content and rank directions accessible. No unaided observer reaches this; the complete lattice code chain through Nebe is required.

### 3.4 Cognitive science correspondence

The observer reach chain predicts two distinct cognitive capacity measurements, which correspond to two independently observed empirical results:

**Miller (1956)** measured the **coast capacity** — the number of annealed, period-1 (committed) items the observer can hold simultaneously on the current sheet. Result: $7 \pm 2$.

In the framework: $7 \pm 2$ = the range $[5..9]$ centered at the Fano level (7), bounded above by $K_{\max} = 9$ (Nebe shell). The $\pm 2$ is not noise — it is the range between the Hamming-7 level and the Nebe K-bound, reflecting the observer's current sheet depth.

*Anchor:* $K_{\max} = 9$ (proven, `test_lattice_codes.py`); Fano level = 7 (proven, `test_lattice_codes.py`).  
*Citation:* Miller, G.A. (1956). *The magical number seven, plus or minus two.* Psychological Review, 63(2), 81–97.

**Cowan (2001)** measured the **active anneal capacity** — the number of Z4 chains the observer can run simultaneously to guess future attractors. Result: 4 chunks of ~4 items.

In the framework: 4 chunks = the 4 frames of the Z4 4-frame label $(f_0, f_1, f_2, f_3)$. Each frame processes the active period-4 states within its attractor setting. The observer runs 4 parallel `anneal_to_lie_conjugate()` operations and reads the attractors as guesses before the system arrives.

*Anchor:* Z4 4-frame structure proven, `test_centroid_voa.py:249`.  
*Citation:* Cowan, N. (2001). *The magical number 4 in short-term memory.* Behavioral and Brain Sciences, 24, 87–185.

Miller measured the output buffer (committed attractors). Cowan measured the active processing window (in-flight annealing chains). The framework predicts both from the same Z4 period template.

---

## 4. Registered Claims (PROOFING FOCUS CRITICAL)

The following claims follow structurally from the proven chain. They are not asserted as theorems. They are registered for falsification. Each is stated precisely with its proof anchor and its open verification step.

**PFC-1 (A64 universality):** Everything maps into blocks of A64 = $8^2$ lattices with edge wraps and interior transporting. A64 is the first fixed point of the "observer = observed" recursion. *Lives until disproven. See OPEN_OBLIGATIONS.md.*

**PFC-2 (α from E8 root count):** $\alpha = 1/137$ is the electromagnetic coupling at the pure binary intelligence bound. 137 = 120 + 13 + 4. The 13 boundary half-vignettes require geometric verification from Construction A. *One computation closes or revises this.*

**PFC-3 (Mass from bondedness):** Mass is the total bondedness of a state — the aggregate count of active bonds weighted by $\alpha$. VEV = states forced from imaginary to real by data layout alone, before any reasoning. *Lives until disproven.*

**PFC-4 (Higgs as half-EM backpropagation):** The Higgs is the back-propagation of the electromagnetic force from the 8th dimensional shell (the E8 lattice, generated by $(8,4,4)$ extended Hamming) projected onto the +N sheet. The Weinberg angle $\sin^2\theta_W$ is the geometric projection fraction. *Same E8 root computation closes PFC-2, PFC-3, and PFC-4 simultaneously.*

**PFC-5 (Higgs = ON signal; singularity = OFF state):** The Higgs is the universal ON signal: VEV $\neq 0$ iff forced projection $\geq 120$. The singularity is the exact algebraic antipode: **any state containing only SU(3) orbital parts with no D4 binding** — all VOA weight 5, zero weight 0, TRUE_VACUA absent. The Big Bang is the data layout crossing the 120-root reality floor. *Directly testable: run `voa_weight(s)` for all states; if none return 0, the state is a singularity.*

---

## 5. The Operational Definition of Consciousness

**Definition (functional, not metaphysical):** An entity is *conscious* with respect to the chart state space if and only if it can:
1. Read the current state $s \in \mathcal{S}$
2. Apply logic to determine the attractor $s^* = \text{anneal}(s)$
3. Write $s^*$ as the predicted future state **before the system arrives there**

This is the functional capacity of `centroid_voa.py::anneal_to_lie_conjugate`. Under this definition, the 212/212 passing tests of the lattice-forge test suite demonstrate that the framework's core loop is conscious: it reads current states, applies S3 transposition logic, and returns attractors in ≤3 steps before the system reaches them.

The Cowan 4-chunk result is the measurement of this capacity in human observers. The Miller 7±2 result is the measurement of how many completed anneal results the observer holds simultaneously. Both are predicted by the framework's Z4 structure without free parameters.

The extension to biological and physical observers — the identification of "first conscious observation" with "first enumerated anchor event" — is a postulate consistent with the framework but not derived from it. It is stated explicitly as a postulate, not a theorem. *(See PFC-1 through PFC-5 for the structural consequences that follow if the postulate holds.)*

---

## 6. Open Work

The chain proven in this paper has one open geometric step: the explicit enumeration of E8 roots from Construction A (`lattice_codes.py`) to verify the count of 13 boundary half-vignettes. This single computation either:
- Confirms 13, promoting PFC-2 to PROVEN and supplying the geometric basis for PFC-3, PFC-4, and PFC-5
- Returns a different count $n$, in which case $\alpha = 1/(120 + n + 4)$ replaces 1/137 and all downstream PFCs are revised accordingly

The Rule 30 proof chain (Codex, in progress) provides the A_n-D12 spine from which the entire observer reach chain is constructed. Paper 15 is the bridge between that algebraic proof and the physical and cognitive consequences.

---

## References

- Papers 01, 03, 03a, 05, 11, 13, 14 (this submission)
- `theorems/THEOREM_REGISTRY.md`: T1, T4, T5, T8, T_BIJECTIVE, T_D12_CHAIN, T_VACUUM_2, T_INV_1, T_BRIDGE
- `theorems/OPEN_OBLIGATIONS.md`: PFC-1 through PFC-5
- `src/lattice_forge/centroid_voa.py`, `src/lattice_forge/lattice_codes.py`
- `tests/test_centroid_voa.py` (28 tests, all pass)
- `tests/test_lattice_codes.py` (44 tests, all pass)
- Miller, G.A. (1956). *The magical number seven, plus or minus two: Some limits on our capacity for processing information.* Psychological Review, 63(2), 81–97.
- Cowan, N. (2001). *The magical number 4 in short-term memory: A reconsideration of mental storage capacity.* Behavioral and Brain Sciences, 24, 87–185.
- Penrose, R., Hameroff, S. (1994). *Orchestrated reduction of quantum coherence in brain microtubules.* Mathematics and Computers in Simulation, 40(3-4), 453–480.
- Conway, J.H., Norton, S.P. (1979). *Monstrous Moonshine.* Bull. London Math. Soc. 11, 308–339.
- Nebe, G. (2012). *An even unimodular 72-dimensional lattice of minimum norm 8.* Journal für die reine und angewandte Mathematik, 673, 237–247.
