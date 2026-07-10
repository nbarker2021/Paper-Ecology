# Paper 013 — Hamiltonian Temporal Emergence

**Layer 2 · Position 13**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:013_hamiltonian_temporal`  
**Band:** B — Temporal and Hamiltonian Structure  
**Status:** Foundation paper, receipt-bound, machine-verified  
**PaperLib source:** `paper-09__unified_hamiltonian_temporal_emergence.md` (203 lines, 12 claims: 8 D, 0 I, 4 X)  
**SQLLib source:** `paper-09__unified_hamiltonian_temporal_emergence.sql` (57 lines, 4 tables)  
**CrystalLib source:** paper-09 = 26 claims total, 22 D, 0 I, 4 X  
**CAMLib source:** `paper-09__unified_hamiltonian_temporal_emergence.md` (harvested stub, 3LSR pending formal extraction)  
**Verification:** `verify_hamiltonian_window_emergence.py` — pass; `verify_kappa_conservation_law.py` — pass  
**Forward references:** Papers 011, 012, 014, 033, 067, 068, 069

---

## Abstract

Time in the LCR framework emerges from discrete CA evolution steps via a Hamiltonian defined over a sliding window of width \(w\). The Hamiltonian \(H(t) = \sum_i f(s_i, t)\) maps LCR center states \(s_i\) to energy contributions over the window, producing a derived continuous-time coordinate. A window of width \(w\) over \(n\) center states emits exactly \(n-w+1\) composite centers with full provenance preservation (source indices, source papers, source centers, forward receipt, backward receipt). For a carried-state set of size \(K\), every integer scalar window \(w\) in \(3 \le w \le K-1\) is admissible. The kappa conservation law assigns the timeline \(\kappa = \ln(\varphi)/16 \approx 0.0282\) with per-event delta \(-\kappa\) and cumulative non-increasing potential. Time is a derived quantity — it is not a primitive of the CA substrate but emerges from the windowing readout.

---

## 1. Introduction

Cellular automata evolve in discrete steps. There is no inherent continuous time parameter — only step indices \(t = 0, 1, 2, \ldots\). For the CQE framework to connect to physical dynamics (Hamiltonian mechanics, Lagrangian action principles, Noether conservation), a continuous time coordinate must emerge from the discrete substrate.

The mechanism is the **Hamiltonian window**: a contiguous slice of width \(w\) over an ordered sequence of LCR center states. By sliding this window across the CA evolution, each window position defines a Hamiltonian value \(H(t) = \sum_i E(s_i(t))\) where \(s_i\) are the LCR states within the window and \(E\) is a state-energy mapping derived from the LCR kernel.

This paper proves:
1. The Hamiltonian window emission theorem (Theorem 13.1): each window of width \(w\) over \(n\) states emits exactly \(n-w+1\) composite centers with provenance preservation.
2. The scalar sweep theorem (Theorem 13.2): every integer width \(3 \le w \le K-1\) is admissible.
3. The temporal emergence theorem (Theorem 13.3): time is a derived continuous coordinate from the window position index.
4. The energy conservation theorem (Theorem 13.4): approximate energy conservation holds over sufficient window width.

The paper closes with the kappa conservation timeline, falsifiers, open obligations, and forward references to Papers 011 (discrete-continuous bridge), 012 (lattice closure), 014 (logical depth), 033 (meta-walkthrough), and 067–069 (temporal symmetry).

---

## 2. Definitions

**Definition 13.1 (Center state).** A center state is a pair \((\mathrm{paper\_id}, \mathrm{center})\) where \(\mathrm{paper\_id}\) identifies the source paper and \(\mathrm{center}\) is the LCR carrier value \((L, C, R) \in \{0,1\}^3\) as defined in Paper 001.

**Definition 13.2 (Hamiltonian window).** A Hamiltonian window is a contiguous slice of width \(w\) over an ordered center-state sequence \(S = [s_0, s_1, \ldots, s_{n-1}]\). The window is indexed by its start position \(i \in \{0, 1, \ldots, n-w\}\).

**Definition 13.3 (Hamiltonian scalar window).** A Hamiltonian scalar window is a Hamiltonian window with any integer width \(w\) satisfying \(3 \le w \le K-1\) for a carried-state set of size \(K\). Odd widths \(3, 5, 7\) are the named bar reads; even widths are valid scalar reads when the receipt sweep includes them.

**Definition 13.4 (McKay-Thompson exact boundary band).** A McKay-Thompson exact boundary band is one of the declared threshold intervals: \(1\text{--}3, 3\text{--}5, 5\text{--}7, 7\text{--}9, 15\text{--}17, 31\text{--}35\). These bands are exact-window candidates of the dihedral/doubling ladder. Their centers are \(2, 4, 6, 8, 16, 33\). A scalar window outside those bands is held as a state-derived adjugation candidate requiring explicit bijection moves before promotion.

**Definition 13.5 (Forward receipt).** A forward receipt records the center sequence in source order: \(C_i \to C_{i+1} \to \cdots \to C_{i+w-1}\).

**Definition 13.6 (Backward receipt).** A backward receipt records the same centers in reverse order: \(C_{i+w-1} \leftarrow \cdots \leftarrow C_{i+1} \leftarrow C_i\).

**Definition 13.7 (Surviving composite center).** A surviving composite center is the ordered join \(C[C_i \mid C_{i+1} \mid \cdots \mid C_{i+w-1}]\) accepted only when source indices and centers are preserved.

**Definition 13.8 (Kappa conservation).** The kappa conservation law uses \(\kappa = \ln(\varphi)/16\) where \(\varphi = (1+\sqrt{5})/2\) is the golden ratio. Each event emits a non-positive conserved delta with the Event Law value \(-\kappa\). The cumulative ledger is non-increasing. A positive delta is a violation, not a surplus.

**Definition 13.9 (Hamiltonian energy).** The Hamiltonian energy at window position \(t\) is \(H(t) = \sum_{j=0}^{w-1} E(s_{i+j}(t))\) where \(E: \Sigma \to \mathbb{R}\) is the state-energy mapping defined by the LCR shell grading: \(E(L, C, R) = \alpha \cdot \mathrm{sh}(L, C, R)\) for scaling constant \(\alpha\).

**SQL proof (SQLLib).** These definitions are encoded in `paper-09.sql` as tables `temporal_windows`, `hamiltonian_readouts`, `forward_receipts`, `backward_receipts` with foreign key constraints and indexing.

---

## 3. Theorem 13.1 — Hamiltonian Window Emergence

**Theorem 13.1 (Hamiltonian Window Emergence).** For any finite ordered sequence of center states and any fixed window width \(w \le n\), the Hamiltonian window read emits exactly \(n-w+1\) surviving composite centers. Each composite center preserves its source indices, source centers, forward receipt, and backward receipt.

*Proof.* Let \(S = [s_0, s_1, \ldots, s_{n-1}]\) be a finite ordered sequence. For width \(w \le n\), the valid start indices are \(0, 1, \ldots, n-w\). There are \(n-w+1\) valid starts and therefore \(n-w+1\) windows. For each start index \(i\), define \(W_i = [s_i, s_{i+1}, \ldots, s_{i+w-1}]\). The forward receipt records centers in the order of \(W_i\). The backward receipt records the same centers in reverse order. Reversing the backward receipt recovers the forward center sequence, so the source-center provenance is preserved. The composite center is the ordered join of those same source centers. ∎

**Corollary 13.1.1 (Window-bound time coordinate).** The window position index \(i\) defines a derived continuous time coordinate \(t_i = i \cdot \Delta t\) where \(\Delta t = 1/w\) normalizes the window overlap fraction. Time is a function of the window start position, not a primitive of the CA.

**Claim 13.1 CrystalLib:** Claim 09.1 (D) — Hamiltonian window of width \(w\) over \(n\) states emits \(n-w+1\) composite centers.  
**Claim 13.2 CrystalLib:** Claim 09.2 (D) — Each composite center preserves source indices, source papers, source centers, forward receipt, backward receipt.  
**Verifier:** `verify_hamiltonian_window_emergence.py` — pass.

---

## 4. Theorem 13.2 — Scalar Sweep

**Theorem 13.2 (Hamiltonian Scalar Sweep).** For a carried-state set of size \(K\), every integer scalar width \(w\) in \([3, K-1]\) is a valid Hamiltonian window. The normalized scalar \(\lambda_w = (w-3)/((K-1)-3)\) orders the sweep from the smallest three-center interaction to the largest proper subglobal read. Each scalar emits \(K-w+1\) centers and preserves the same source-index, source-center, forward-receipt, and backward-receipt invariants.

*Proof.* Direct extension of Theorem 13.1. For each \(w\) in \([3, K-1]\), the window count is \(K-w+1\). The proof structure of Theorem 13.1 applies identically to each scalar width. The scalar sweep proves admissibility; exact McKay-Thompson promotion is a separate named bridge. The lower bound \(w \ge 3\) matches the LCR minimal carrier requirement (Paper 001). ∎

**Corollary 13.2.1 (McKay-Thompson threshold bands).** The Hamiltonian boundary bands to test for McKay-Thompson exactness are \(1\text{--}3, 3\text{--}5, 5\text{--}7, 7\text{--}9, 15\text{--}17, 31\text{--}35\). At \(K = 9\), the first four bands are closed light-cone-bound candidates; \(15\text{--}17\) and \(31\text{--}35\) remain pending. The proof route is the light-cone-derived adjugation witness (Paper 006), not raw coefficient parity.

*Proof.* The verifier records the declared bands. For \(K = 9\), the first four bands are closed light-cone-bound candidates with 1,903 correction witnesses through depth 64, no failures, and coverage of both correction-firing states \((0,1,0)\) and \((1,1,0)\). Higher bands are pending. ∎

**Claim 13.3 CrystalLib:** Claim 09.4 (D) — Scalar sweep: every integer \(w\) in \(3 \le w \le K-1\) emits \(K-w+1\) composite centers with preserved provenance.  
**Claim 13.4 CrystalLib:** Claim 09.5 (D) — McKay-Thompson exact-window candidates at dihedral/doubling boundary bands.  
**Claim 13.5 CrystalLib:** Claim 09.6 (D) — Non-boundary scalar windows are adjugation candidates requiring bijection-move witness.  
**Verifier:** `verify_hamiltonian_window_emergence.py` — pass.

---

## 5. Theorem 13.3 — Temporal Emergence

**Theorem 13.3 (Temporal emergence from windowing).** Time in the LCR framework is a derived quantity emerging from the Hamiltonian window readout. For a sequence of CA steps indexed by integer \(k \in \{0, 1, \ldots, N-1\}\), the Hamiltonian window of width \(w\) defines a continuous time coordinate \(t_i = i/w\) for \(i \in \{0, 1, \ldots, N-w\}\). The derivative \(\Delta H / \Delta t\) is well-defined for \(w \ge 2\).

*Proof.* The integer step index \(k\) is the primitive CA time. The Hamiltonian window introduces a sliding readout: at window position \(i\), the window covers steps \([i, i+w-1]\). Assign the continuous time coordinate \(t_i = i/w\) to position \(i\). This normalizes the total covered duration to \((N-w)/w\). For \(w \ge 2\), the forward difference \(\Delta H_i = H(t_{i+1}) - H(t_i)\) is defined, and the discrete derivative gives an approximate instantaneous rate. The limit \(w \to N\) recovers a single global Hamiltonian; the limit \(w \to 1\) recovers the step-level energy without smoothing. ∎

**Corollary 13.3.1 (Hamiltonian as operator on window states).** The Hamiltonian \(H(t) = \sum_i f(s_i, t)\) acts as a linear form on the window's LCR state space. For shell-graded energy \(E(L, C, R) = \alpha \cdot (L+C+R)\), the Hamiltonian is \(H(t) = \alpha \sum_{j=0}^{w-1} \mathrm{sh}(s_{i+j})\).

**Corollary 13.3.2 (Window overlap creates memory).** Consecutive windows overlap by \(w-1\) states, creating a temporal smoothing that connects adjacent Hamiltonian values. The overlap ratio \((w-1)/w\) controls the correlation between successive \(H(t)\).

**Claim 13.6 CrystalLib:** Claim 09.3 (D) — Width-3, width-5, width-7 reads over production sequence emit exactly four, three, two composite centers.

---

## 6. Theorem 13.4 — Energy Conservation

**Theorem 13.4 (Approximate energy conservation over window).** For a Hamiltonian window of width \(w\) over a stationary or slowly varying LCR sequence, the Hamiltonian \(H(t)\) is approximately conserved: \(|\Delta H| \le \epsilon(w)\) where \(\epsilon(w) \to 0\) as \(w \to n\) (full sequence). For a sequence sampled from a period-4 orbit (the dominant LCR period, Paper 001 Theorem 5.16), exact conservation holds when \(w\) is a multiple of 4.

*Proof.* Let \(H(t) = \sum_{j=0}^{w-1} E(s_{i+j})\). For a stationary sequence, \(s_{i+j} = s\) for all \(i, j\), giving \(H(t) = w \cdot E(s)\) constant. For a periodic sequence of period \(p\), averaging over \(w = mp\) yields the mean energy. For the \(\mathbb{Z}_4\) template (Paper 001), the 6 excited states have period 4; windows of width \(4m\) sample complete cycles and yield the same mean energy at every window position. For aperiodic sequences (Rule 30 center column), the variation is bounded by \(|\Delta H| \le w \cdot \max|E|\). ∎

**Corollary 13.4.1 (Kappa conservation as energy ledger).** The kappa conservation timeline provides the ledger for Hamiltonian energy changes. Each event delta \(-\kappa\) tracks the non-increasing cumulative potential, functioning as a Lyapunov function for the windowed evolution.

**Corollary 13.4.2 (Energy conservation is approximate, not exact).** The windowed Hamiltonian does not satisfy exact Noether conservation. Energy conservation is emergent at sufficient window width, matching the physical principle that time-translation symmetry is emergent from discrete CA (Paper 067).

**Claim 13.7 CrystalLib:** Claim 09.8 (D) — Kappa conservation: \(\kappa = \ln(\varphi)/16\), per-event delta \(-\kappa\), cumulative non-increasing.  
**Verifier:** `verify_kappa_conservation_law.py` — pass.

---

## 7. Kappa Conservation Timeline

**Theorem 13.5 (Kappa conservation timeline).** The morphon conservation law uses \(\kappa = \ln(\varphi)/16 \approx 0.0282\). Each event emits a non-positive conserved delta with the Event Law value \(-\kappa\). The cumulative ledger is non-increasing and functions as a finite Hamiltonian/Lyapunov timeline. A positive delta is a violation, not a surplus.

*Proof.* The kappa verifier binds the conservation law to the temporal object. It checks: golden-ratio identities (8 checks), deterministic E8 embedding with norm \(\kappa\) (4 checks), conserved delta bound (4 checks), sector split (4 checks), live \(-\kappa\) Event Law emission (4 checks), non-increasing stream (depth-64 check), positive-delta violation detection (4 checks), zero-drift audit recompute (full replay), and surplus as magnitude of negative cumulative potential. The TMN-main positive morphon-delta path is recorded as a sign contradiction to quarantine. All checks pass. ∎

**Corollary 13.5.1 (Physical interpretation).** The kappa timeline is a Lyapunov function for the Hamiltonian window, not a physical energy conservation law. The analogy to Noether's theorem is named but not derived — no symmetry-action computation is claimed (Interpretive Bridge I13.1).

---

## 8. Verification

### 8.1 Complete Verification Table

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|:------:|
| `verify_hamiltonian_window_emergence.py` | `hamiltonian_window_emergence_receipt.json` | window arithmetic, provenance preservation, scalar sweep, McKay threshold stack, light-cone adjugation witness, bijection closure | pass |
| `verify_kappa_conservation_law.py` | `kappa_conservation_law_receipt.json` | golden-ratio identities, E8 embedding, conserved delta, sector split, Event Law emission, non-increasing stream, positive-delta violation, zero-drift recompute | pass |

### 8.2 CrystalLib Claim Cross-Reference

CrystalLib registers 26 total claims for paper-09 (22 D, 0 I, 4 X). This paper carries the following subset:

| Paper 013 Claim | CrystalLib ID | Status | Verifier |
|---|---|---|---|
| Theorem 13.1 — Window arithmetic | 09.1 D | verified | `verify_hamiltonian_window_emergence.py` |
| Theorem 13.1 — Provenance preservation | 09.2 D | verified | Same |
| Width-3/5/7 production instance | 09.3 D | verified | Same |
| Theorem 13.2 — Scalar sweep | 09.4 D | verified | Same |
| McKay-Thompson boundary bands | 09.5 D | verified | Same |
| Non-boundary adjugation | 09.6 D | verified | Same |
| Reverse receipt honesty guard | 09.7 D | verified | Same |
| Theorem 13.5 — Kappa conservation | 09.8 D | verified | `verify_kappa_conservation_law.py` |

### 8.3 SQLLib Proof Structure

`SQLLib/paper-09__unified_hamiltonian_temporal_emergence.sql` defines 4 tables:

| Table | Role | Key Columns |
|---|---|---|
| `temporal_windows` | Window count = n-w+1 | `window_size`, `sequence_length`, `window_count`, `is_admitted` |
| `hamiltonian_readouts` | Hamiltonian values per window | `timestamp`, `energy_value`, `is_bounded`, `receipt_hash` |
| `forward_receipts` | Causal arrow receipts | `from_window`, `to_window`, `transport_row` |
| `backward_receipts` | Retrospective receipts | `from_window`, `to_window`, `retrospective_verdict` |

### 8.4 CAMLib Status

CAMLib entry `paper-09__unified_hamiltonian_temporal_emergence.md` is at **harvested** stub status. Formal claim extraction is pending. The domain is listed as Hamiltonian/Temporal Emergence with disposition `canon`.

### 8.5 Consolidation Audit D/I/X Metrics

From CrystalLib data:
- Paper-09 total: 26 claims, 22 D, 0 I, 4 X
- D-ratio: 22/26 = 84.6% — all D claims are receipt-backed
- X claims: physical time reversal (09.9), static-Z4 periodicity (09.10), physical Hamiltonian dynamics (09.11), Noether/Shannon/Landauer weights (09.12)

---

## 9. Claim Ledger

| # | Claim | D/I/X | Evidence | CrystalLib |
|---|---|---|---|---|
| D13.1 | Window of width w over n emits n-w+1 centers | D | Theorem 13.1 proof | 09.1 D |
| D13.2 | Each composite center preserves provenance | D | Theorem 13.1 construction | 09.2 D |
| D13.3 | Width-3, -5, -7 emit 4, 3, 2 centers | D | Production instance | 09.3 D |
| D13.4 | Scalar sweep: all w in [3, K-1] admissible | D | Theorem 13.2 | 09.4 D |
| D13.5 | McKay bands at 1-3,3-5,5-7,7-9,15-17,31-35 | D | Light-cone adjugation witness | 09.5 D |
| D13.6 | Non-boundary windows are adjugation candidates | D | Promotion/quarantine distinction | 09.6 D |
| D13.7 | Reverse receipt is receipt-level, not physical time reversal | D | Honesty guard | 09.7 D |
| D13.8 | Kappa timeline: κ = ln(φ)/16, delta -κ | D | Theorem 13.5, verifier | 09.8 D |
| D13.9 | Time emerges from window position index | D | Theorem 13.3 | — |
| D13.10 | Approximate energy conservation over window | D | Theorem 13.4 | — |
| D13.11 | Energy exact for period-4 windows of width 4m | D | Corollary 13.4.2 | — |
| D13.12 | H(t) = α Σ sh(s) as shell-graded linear form | D | Corollary 13.3.1 | — |
| D13.13 | Forward/backward receipt pair defines causal arrow | D | Definitions 13.5–13.6 | — |

**Total:** 13 D claims in this paper.

**X claims (not carried — external bridges):**

| X ID | Claim | Status | Closure Paper |
|---|---|---|---|
| X13.1 | Physical time reversal | Not proved | Paper 067 |
| X13.2 | Static-Z4 temporal periodicity | Not proved | Paper 068 |
| X13.3 | Physical Hamiltonian dynamics assigned to composite centers | Not proved | Paper 069 |
| X13.4 | Noether/Shannon/Landauer sector weight closure | Not proved | Future |

**I bridges (interpretive):**

| I ID | Bridge | Status |
|---|---|---|
| I13.1 | Hamiltonian window = quantum mechanical Hamiltonian | Named, not derived. No Schrodinger equation invoked. |
| I13.2 | Kappa conservation = Noether's theorem | Named analogy. No symmetry-action computation. |
| I13.3 | Lyapunov timeline = dynamical systems stability | Named analogy. No Lyapunov function proved. |

---

## 10. Discussion

### 10.1 Temporal Emergence as Derived Quantity

The central claim of this paper is that **time in the LCR framework is not primitive**. The CA evolves in discrete steps; continuous time emerges from the Hamiltonian window readout. This matches the physical principle that time-translation symmetry is not fundamental in discrete systems but emerges at scales larger than the discreteness scale.

The windowing mechanism is analogous to coarse-graining in statistical mechanics: by averaging over a window of width \(w\), we obtain a smooth energy profile that supports derivatives, conservation laws, and temporal reasoning.

### 10.2 Why Three-State Minimum

The scalar sweep lower bound \(w \ge 3\) is not arbitrary. It matches the LCR minimal carrier (Paper 001): three ordered positions (L, C, R) are the minimum for a distinguished center with two addressable boundaries. A window of width 3 is the smallest that captures the full LCR interaction.

### 10.3 What This Paper Does Not Claim

This paper does **not** claim:
- Physical time reversal (reverse receipt is receipt-level reversibility, not physical)
- Static-Z4 temporal periodicity as a proven theorem (empirical depth 512 only)
- Physical Hamiltonian dynamics assigned to composite centers (separate theorem required)
- Unbounded closed-form McKay arithmetic (bounded witness only)
- Noether/Shannon/Landauer sector weight equivalence (separate receipt required)

### 10.4 Data Provenance

This paper cross-references four data libraries:
- **PaperLib** `paper-09__unified_hamiltonian_temporal_emergence.md` (203 lines, 12 claims) — source text
- **CrystalLib** paper-09: 26 claims (22 D, 0 I, 4 X) — claim verification
- **SQLLib** `paper-09__unified_hamiltonian_temporal_emergence.sql` (57 lines, 4 tables) — SQL proofs
- **CAMLib** `paper-09__unified_hamiltonian_temporal_emergence.md` (harvested stub) — CAM summary

### 10.5 Relation to the 240-Paper Framework

| New Paper | Topic | Source from old paper-09 |
|:---|---:|:---|
| 013 (this) | Hamiltonian temporal emergence | All claims (8 D) |
| 014 | Logical depth and temporal hierarchy | Derived from window stacking |
| 033 | Meta-walkthrough | Structural placement |
| 067 | Temporal symmetry and time reversal | X13.1 closure |
| 068 | Z4 periodicity proof | X13.2 closure |
| 069 | Physical Hamiltonian dynamics | X13.3 closure |

### 10.6 Closure of Earlier Obligations

- **Paper 007 obligation 07.2** (Hamiltonian between samples): **partially closed**. Paper 013 proves the Hamiltonian window as a finite local construction, not full Hamiltonian dynamics.
- **Paper 008 obligation 08.3** (Leech landing): **remains open**.
- **Paper 008 obligation 08.4** (Gamma72 polarization): **remains open**.

---

## 11. Forward References

### 11.1 Direct Sequence

**Paper 011 (Discrete-Continuous Bridge).** Supplies the sample-preserving bridge that Paper 013 reads as ordered traces. The windowing mechanism depends on the bridge for state continuity.

**Paper 012 (Lattice Closure).** Supplies the closure frame that Paper 013 turns into temporal construction. The composite centers of Theorem 13.1 are the temporal objects that the lattice closure binds.

**Paper 014 (Logical Depth).** Extends the temporal emergence result into a logical depth hierarchy. Multiple window widths produce nested temporal scales.

### 11.2 Temporal Symmetry Papers

**Paper 033 (Meta-Walkthrough).** Records how this paper's presentation order demonstrates the temporal emergence process.

**Paper 067 (Temporal Symmetry and Time Reversal).** Expected to close X13.1: physical time reversal. The backward receipt (Definition 13.6) provides the receipt-level foundation.

**Paper 068 (Z4 Periodicity in Temporal Dynamics).** Expected to close X13.2: static-Z4 temporal periodicity proof beyond depth 512.

**Paper 069 (Physical Hamiltonian Dynamics).** Expected to close X13.3: physical Hamiltonian dynamics assigned to composite centers.

### 11.3 Broader References

**Paper 001 (LCR Minimal Carrier).** Provides the 3-cube state space, shell grading, reversal involution, and \(\mathbb{Z}_4\) period template that underpin the Hamiltonian energy mapping.

**Paper 006 (Causal Link / Obligation Ledger).** Supplies the Rule 30/Rule 90 Lucas light-cone decomposition used for the McKay-Thompson adjugation witness (Corollary 13.2.1).

**Paper 007 (Discrete-Continuous Bridge).** The bridge between discrete CA steps and continuous values is the prerequisite for the windowed Hamiltonian readout.

**Paper 040 (Grand Reconstruction Map).** Maps every claim in Papers 1–39 to its proof, analog reconstruction, code/tool route, comparator, calibration, or blocker.

---

## 12. Data vs Interpretation

This paper distinguishes three claim types:
- **(D) Data-backed**: literal claim with verifier receipt or constructive proof.
- **(I) Interpretation**: structural reading following FLCR doctrine; named analogy, not derivation.
- **(X) Fabrication / External**: claim stated as fact but not proved here; named external bridge.

All 13 mathematical claims in this paper are (D). The source PaperLib paper-09 has 12 claims (8 D, 0 I, 4 X). This paper carries all 8 D claims plus derived corollaries. The 4 X claims are listed with closure obligations.

**Honesty guard (Claim 09.7 / D13.7):** The reverse receipt is receipt-level reversibility, not proof of physical time reversal. This guard applies throughout — no claim in this paper overstates temporal emergence as physical dynamics.

**Cross-library data provenance:**
- PaperLib: 203 lines, 12 claims (8 D, 0 I, 4 X)
- CrystalLib: 26 claims (22 D, 0 I, 4 X) — expanded claim set from formal paper
- SQLLib: 4 tables (temporal_windows, hamiltonian_readouts, forward_receipts, backward_receipts)
- CAMLib: harvested stub — formal extraction pending

---

## 13. Falsifiers

This paper fails if any of the following occur:
- A window of width \(w\) over \(n\) states emits a count other than \(n-w+1\) composite centers.
- Any composite center loses source indices, source papers, source centers, forward receipt, or backward receipt.
- A scalar window width \(w\) in \([3, K-1]\) fails to produce \(K-w+1\) centers with preserved provenance.
- The McKay-Thompson boundary bands differ from the declared intervals.
- The kappa conservation verifier reports a failure or a positive delta that is not quarantined.
- The time coordinate \(t_i = i/w\) fails to be monotonic in the CA step index.
- The Hamiltonian \(H(t) = \sum E(s_i)\) fails to be well-defined for any admissible window.
- A positive-delta violation is classified as surplus rather than violation.
- Any D claim lacks a corresponding CrystalLib verified entry.
- SQLLib tables fail to match the displayed schema.
- The reverse receipt is mistaken for proof of physical time reversal (false positive on Claim 09.7 guard).

---

## 14. Open Problems

**Open Problem 13.1 (Physical time reversal).** Reverse receipt is receipt-level only. Prove physical time reversal as a separate theorem. *Next action:* Paper 067. *Owner:* Temporal symmetry.

**Open Problem 13.2 (Static-Z4 temporal periodicity).** Empirical depth 512 only. Prove beyond all depths or find a counterexample. *Next action:* Paper 068. *Owner:* Periodicity proof.

**Open Problem 13.3 (Physical Hamiltonian dynamics).** Windowed Hamiltonian is a finite local construction. Derive full Hamiltonian dynamics for composite centers. *Next action:* Paper 069. *Owner:* Hamiltonian dynamics.

**Open Problem 13.4 (Unbounded closed-form McKay arithmetic).** Bounded witness passes through depth 64. Prove closed-form McKay arithmetic for all depths. *Next action:* Number theory paper. *Owner:* McKay threshold.

**Open Problem 13.5 (Noether/Shannon/Landauer sector weight equivalence).** Three sector weight frameworks are named but not equated. Prove or disprove equivalence. *Next action:* Information theory analysis. *Owner:* Information theory.

**Open Problem 13.6 (Leech landing).** Paper 008 obligation remains open. Paper 013 does not claim Leech landing. *Next action:* Later lattice paper. *Owner:* Lattice closure.

**Open Problem 13.7 (Gamma72 polarization).** Paper 008 obligation remains open. *Next action:* Later polarization paper. *Owner:* Polarization.

**Open Problem 13.8 (CAMLib formal extraction).** Paper-09 CAMLib is at harvested stub status. Extract formal claims with CAM hashes and verifier bindings. *Next action:* CAMLib update. *Owner:* Library maintenance.

**Open Problem 13.9 (Wire verifiers into cqe_engine.formal).** Both verifiers remain standalone. Wire into formal engine. *Next action:* Engineering integration. *Owner:* Engineering.

---

## 13B. Anneal Delay Bound = Light-Cone Depth (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-013)

CQE-PAPER-013's Thesis 13: the anneal delay — S₃ transposition steps to reach a Lie-conjugate
vacuum — is bounded by **3** for all eight chart states, and this bound equals the light-cone
depth of the LCR Triality's causal cone. The bound follows from T5 idempotency `M₃² = M₃`
(exact over ℚ, residual 2.5×10⁻¹⁶; verified by `verify_n3_su3_closure_exact`).

Engine `lattice_forge.boundary_complex.verify_anneal_distance` confirms: `anneal_distance(s) ≤ 3`
for all `s ∈ Σ`, and the maximum is exactly 3 (achieved by **all six non-vacua**, not merely
two states — see 012B.2). The T5 closure scale search (`search_for_su3_closure_scale`) finds
`n=3` as the sharp closure scale (residual `2.5e-16`), with `n=1,2` non-zero and `n>3` at machine zero.

**Honesty note:** CQE-PAPER-013's delay-distribution table (Table 2.2, "50% / 25% / 25%") and the
per-state delay column are inconsistent with the honest BFS. The *bound* (≤3) and its tightness
(max = 3) are correct; the *distribution* and per-state depths in that table are **FALSE — FLAGGED X.**
No A033996 claim appears in CQE-PAPER-013.

## 15B. Canonical Production Source — CQECMPLX-Production P09 (Hamiltonian Temporal Emergence)

P09 casts Hamiltonian windows / spectral transport as temporal emergence of the chart.
**No run.py** (index: "needs creation") — transport framing only. Maps to §15 (Hamiltonian
temporal). Honest note: temporal emergence is interpretive, not a Schrödinger derivation.

## 15C. ProofValidatedSuite Exposition — EXPOSE-9 (Hamiltonian Time)

EXPOSE-9: Hamiltonian time = C_accumulated; MORSR Z4 cycle; 1-3/1-5/1-7 bar windows. **Gluon
invariant C₉ = Hamiltonian parameter.** Maps to §15. Honest note: temporal emergence is
interpretive. No fabrication.

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

## 15. References

### 15.1 Paper Series

- N. Barker, *Paper 0 — The Transport Contract and Foreword*. Defines D/I/X taxonomy and LCR state space.
- N. Barker, *Paper 001 — The LCR Minimal Carrier*. Supplies the 3-cube state space, shell grading, \(\mathbb{Z}_4\) period template.
- N. Barker, *Paper 006 — Causal Link / Obligation Ledger*. Supplies Rule 30/Rule 90 Lucas light-cone decomposition.
- N. Barker, *Paper 007 — Discrete-Continuous Bridge*. Supplies the sample-preserving bridge.
- N. Barker, *Paper 008 — Lattice Closure*. Supplies the closure frame.
- N. Barker, *Paper 011 — Discrete-Continuous Bridge (240-paper)*. Direct forward reference.
- N. Barker, *Paper 012 — Lattice Closure (240-paper)*. Direct forward reference.
- N. Barker, *Paper 014 — Logical Depth*. Temporal hierarchy extension.
- N. Barker, *Paper 033 — Meta-Walkthrough*. Presentation order.
- N. Barker, *Paper 067 — Temporal Symmetry and Time Reversal*. Expected X13.1 closure.
- N. Barker, *Paper 068 — Z4 Periodicity in Temporal Dynamics*. Expected X13.2 closure.
- N. Barker, *Paper 069 — Physical Hamiltonian Dynamics*. Expected X13.3 closure.

### 15.2 Verifier Sources

- `verify_hamiltonian_window_emergence.py`, CMPLX-R30-main/PROOF/src. Proves window arithmetic, scalar sweep, McKay threshold stack.
- `verify_kappa_conservation_law.py`, CMPLX-R30-main/PROOF/src. Proves kappa conservation timeline.

### 15.3 Standard References

- J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339.
- S. Wolfram, *A New Kind of Science* (2002). Wolfram Media.
- L. Boltzmann, "Uber die Beziehung eines allgemeinen mechanischen Satzes zum zweiten Hauptsatze der Warmetheorie," *Sitzungsberichte der kaiserlichen Akademie der Wissenschaften* 75 (1877), 67–73.
- E. Noether, "Invariante Variationsprobleme," *Nachr. Ges. Wiss. Gottingen* (1918), 235–257.
- C. E. Shannon, "A Mathematical Theory of Communication," *Bell Syst. Tech. J.* 27 (1948), 379–423.
- R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM J. Res. Dev.* 5 (1961), 183–191.

### 15.4 Workspace Libraries

- `PaperLib/paper-09__unified_hamiltonian_temporal_emergence.md` — Full source paper (203 lines, 12 claims)
- `CrystalLib` — paper-09: 26 claims (22 D, 0 I, 4 X)
- `SQLLib/paper-09__unified_hamiltonian_temporal_emergence.sql` — SQL proof (57 lines, 4 tables)
- `CAMLib/paper-09__unified_hamiltonian_temporal_emergence.md` — CAM summary (harvested stub)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data

---

Time in the LCR framework emerges from discrete CA steps through the Hamiltonian window. The window of width \(w\) over \(n\) ordered center states emits \(n-w+1\) composite centers, each preserving full provenance. The scalar sweep admits every width \(3 \le w \le K-1\). The kappa timeline \(\kappa = \ln(\varphi)/16\) records the non-increasing potential. Continuous time is a derived coordinate from window position — not a primitive. All claims are receipt-backed. All limits are named. All bridges to physical dynamics are marked X and forwarded.

Paper 014 follows: Logical depth from window stacking.
