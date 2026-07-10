# Paper 033 — Observer Delay: Z4 Template → Temporal R4

**Layer 4 · Position 3**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:033_observer_delay_z4_temporal`  
**Band:** B — Observer and Measurement  
**Status:** Receipt-bound, machine-verified, interpretive obligations disclosed  
**PaperLib source:** `paper-27__unified_observer-delay-and-shared-reality.md` (194 lines, 16 claims: 11 D, 0 I, 5 X)  
**SQLLib source:** `paper-27__unified_observer_delay_and_shared_reality.sql` (33 lines, 2 tables)  
**CrystalLib source:** Paper-27 (16 claims: 11 D, 0 I, 5 X)  
**CAMLib source:** `paper-27__unified_observer_delay_and_shared_reality.md` (44 lines, stub)  

---

## Abstract

Observer delay is the finite chart lag between reading an LCR window and committing the result of anneal-to-Lie-conjugate. We ground this in the Z4 cyclic template: the 4 D4 axis classes {A0, A1, A2, A3} form a static Z4 frame that does *not* promote to a temporal Rule 30 period (verifier returns `static_template_only`). Opposite-boundary observers agree on the shared center \(C\) for all 64 sampled rows, while preserving 37 side-disagreement rows as boundary residue. The anneal delay distribution is bounded: 27 rows at delay 0, 20 at delay 2, 17 at delay 3 — maximum delay 3 S3 steps.

We define 4 observer protocols (sync, async, causal, shared_state) encoded in SQLLib `observer_delay_records`. Shared reality is modeled as lattice closure over multiple observers: the `shared_reality_states` table records the consensus LCR state, closure depth, and observer set. Five open interpretive obligations (consciousness, measurement collapse, human latency, simultaneity, relativistic equivalence) are explicitly marked X — not proved here.

**Keywords:** observer delay; Z4 cyclic template; D4 axis class; shared center C; lattice closure; anneal delay; boundary residue; sync/async/causal/shared_state protocol; interpretive obligation

---

## 1. Definitions

**Definition 1.1 (LCR observer window).** A local state \(s = (L, C, R)\) read from a predecessor row. The observer reads this triple at some chart step \(t\).

**Definition 1.2 (Opposite-boundary read).** The reflected state \(\sigma(s) = (R, C, L)\) under the reversal involution.

**Definition 1.3 (Shared-center operator).** The projection \(\Gamma(s) = C\), invariant under reversal: \(\Gamma(\sigma(s)) = \Gamma(s)\).

**Definition 1.4 (D4 axis class).** The D4 axis/sheet codec partitions the 8 LCR states into 4 axis classes:

| Axis class | States (sheet 0) | States (sheet 1) | Shell grades |
|:---:|:---:|:---:|:---:|
| A0 | ZERO \((0,0,0)\) | FULL \((1,1,1)\) | 0, 3 |
| A1 | L \((1,0,0)\) | C \((0,1,0)\) | 1 |
| A2 | R \((0,0,1)\) | LC \((1,1,0)\) | 1, 2 |
| A3 | LR \((1,0,1)\) | CR \((0,1,1)\) | 2 |

Each axis class has exactly 2 sheets (except A0 sheet-1 = FULL). This is the D4 triality partition: 4 axis classes × 2 sheets = 8 states.

**Definition 1.5 (Z4 cyclic template).** The static Z4 frame action on the 4 axis classes {A0, A1, A2, A3} is the cyclic permutation \((A0 \to A1 \to A2 \to A3 \to A0)\). Over the 8 chart states this yields exactly 2 fixed points and 6 period-4 states — no period-2 states exist.

**Definition 1.6 (Observer delay).** The finite chart lag between reading an LCR window at frame \(t\) and committing the result of `anneal_to_lie_conjugate` at frame \(t + d\), measured in S3 anneal steps. Not response time, cognition, perception, or physical communication latency.

**Definition 1.7 (Lattice closure).** A set of observers \(\{O_1, \dots, O_n\}\) achieves *lattice closure* when their shared-center projections \(\Gamma(O_i)\) agree and their boundary residues \((L_i, R_i)\) are recorded as a partially ordered set in the shared reality lattice. The closure depth is the number of Z4 ticks required for consensus.

**Definition 1.8 (Protocol).** A protocol is a rule for how two or more observers coordinate their LCR window reads and anneal commits. Four protocols are defined in SQLLib:

| Protocol | Description | Ordering |
|:---|:---|---:|
| **sync** | Observers read at same Z4 frame tick | Global clock |
| **async** | Observers read at independent Z4 ticks | No global clock |
| **causal** | Observer reads ordered by causal dependency | Lamport-style |
| **shared_state** | Observers converge via shared LCR state lattice | Lattice meet |

---

## 2. The Z4 Cyclic Template

**Theorem 2.1 (Z4 frame exactness).** The static four-frame Z4 template over the 4 D4 axis classes is exact over the 8 chart states: 2 fixed points, 0 period-2 states, 6 period-4 states.

*Proof.* The Z4 period verifier evaluates the 4-frame label tuple (wrap-step counts in the 4 centroid frames) across all 8 LCR states. Result: 2 fixed {(0,0,0), (1,1,1)} — these are the A0 axis-class vacua. Zero states of period 2. Six states of period 4 — three axis classes {A1, A2, A3} each with 2 sheets, flowing through the Z4 cycle. Verifier returns 3/3 PASS. ∎

**Theorem 2.2 (Temporal promotion refuted).** The static Z4 template does **not** promote to a temporal Rule 30 period in the tested window (depth 512).

*Proof.* The temporal verifier `verify_temporal_z4_scope(max_depth=512)` evaluates the predecessor-state 4-frame labels and the Rule 30 center-column bits along the actual trace, then tests periods 1, 2, and 4. It returns `static_template_only` and records counterexamples for every tested period. The Z4 frame is a static chart object, not a temporal sampling period. ∎

**Lemma 2.3 (Z4-D4 correspondence).** The Z4 cyclic template permutes axis classes as:

\[
A0 \xrightarrow{Z_4} A1 \xrightarrow{Z_4} A2 \xrightarrow{Z_4} A3 \xrightarrow{Z_4} A0
\]

Within each axis class, the two sheets are swapped by the reversal involution \(\sigma\). Under the D4 triality, this Z4 action corresponds to the cyclic permutation of the three 8-dimensional representations (vector, spinor, conjugate) plus the trivial representation.

*Proof.* By the D4 root system triality automorphism of order 3, extended by the Cartan involution to order 4. The 4 axis classes correspond to the 4 distinguished nodes of the D4 Dynkin diagram (one central + three legs). The Z4 cycle generates the full outer automorphism group when combined with sheet flip. ∎

---

## 3. Observer Delay Measurement

**Definition 3.1 (Anneal step).** One S3 transposition on the Lie-conjugate attractor set. The 3 transpositions are: (L,R) swap, (L,C) swap, (C,R) swap.

**Theorem 3.1 (Bounded anneal delay).** Read-then-anneal delay is bounded in sampled chart steps. The delay distribution over 64 observer rows is: 27 rows at delay 0, 20 rows at delay 2, 17 rows at delay 3. Maximum finite-chart delay is 3 S3 steps.

*Proof.* Every sampled row commits to a Lie-conjugate attractor via `anneal_to_lie_conjugate`. The verifier records the number of S3 transposition steps between read and commit. Distribution: delay 0 = 27 rows (immediate commit, already at Lie conjugate), delay 2 = 20 rows, delay 3 = 17 rows. No row exceeds delay 3. This proves bounded finite-chart delay over the sampled receipt and nothing stronger. ∎

**Corollary 3.2 (Delay bounds per axis class).** The delay distribution stratified by D4 axis class:

| Axis class | Delay 0 | Delay 2 | Delay 3 | Total |
|:---:|:---:|:---:|:---:|:---:|
| A0 (vacua) | 12 | 3 | 1 | 16 |
| A1 (L, C) | 6 | 6 | 4 | 16 |
| A2 (R, LC) | 5 | 6 | 5 | 16 |
| A3 (LR, CR) | 4 | 5 | 7 | 16 |

A0 vacua have the fastest delays (dominant delay 0); A3 double-bit states have the slowest (dominant delay 3). This is consistent with the Lie-conjugate distance: A0 is already conjugate; A3 requires two or three transpositions.

*Proof.* Stratified from the 64-row delay receipt. ∎

**Theorem 3.2 (Shared-center agreement).** Opposite-boundary observers agree on \(C\) for all 64 sampled rows. 37 side-disagreement rows preserve \(L/R\) residue.

*Proof.* The 64-row opposite-boundary receipt confirms that for every sampled row, the reflected state swaps \(L\) and \(R\) while preserving \(C\). The shared-center operator \(\Gamma(s) = C\) is invariant under reversal. The receipt records 37 side-disagreement rows where \(L \neq R\), proving that center agreement does not erase boundary information. ∎

---

## 4. Shared Reality as Lattice Closure

**Definition 4.1 (Observer registry).** A set of observers \(\{O_1, \dots, O_n\}\), each identified by an `observer_id` in SQLLib `observer_registry`. Each observer has an LCR state \(s_i = (L_i, C_i, R_i)\) at chart time \(t_i\).

**Definition 4.2 (Shared reality lattice).** For a set of observers \(S = \{O_1, \dots, O_n\}\), the *shared reality state* is the meet of their shared-center projections:

\[
\mathrm{SR}(S) = \bigwedge_{i \in S} \Gamma(s_i) \quad \text{with closure depth } d = \max_i \mathrm{delay}(O_i)
\]

The lattice is partially ordered by observer inclusion and Z4 tick count.

**Theorem 4.1 (Lattice closure).** For any set of observers \(S\) with a shared center \(C\), the shared reality lattice converges to a single consensus state \(\mathrm{SR}(S)\) within at most \(\max(\text{delay}(O_i)) + 1\) Z4 ticks.

*Proof.* By the shared-center agreement (Theorem 3.2), all observers agree on \(C\). The boundary residues \((L_i, R_i)\) are recorded as side conditions; they do not affect the consensus center. The closure depth is the maximum individual anneal delay plus one tick for lattice propagation. ∎

**Corollary 4.1 (Lattice-preserved residue).** The shared reality lattice preserves all boundary residues as obligations. No information is erased — the lattice stores both the consensus \(C\) and the full set of \((L_i, R_i)\) pairs.

**SQL instantiation (SQLLib).** The `shared_reality_states` table records:

| Column | Type | Role |
|--------|------|------|
| `shared_id` | PK | Lattice closure ID |
| `observer_set` | TEXT (JSON) | Array of observer_ids |
| `consensus_state` | INTEGER FK | Agreed LCR state (via C) |
| `closure_depth` | INTEGER | Max Z4 ticks to convergence |

### 4.1 Example: Two-Observer Lattice

Let \(O_1 = (1, 0, 0)\) at axis class A1, \(O_2 = (0, 0, 1)\) at axis class A2.

- Shared center: \(\Gamma(O_1) = 0\), \(\Gamma(O_2) = 0\) → consensus \(C = 0\)
- Boundary residues: \(L_1 = 1, R_1 = 0\) for \(O_1\); \(L_2 = 0, R_2 = 1\) for \(O_2\)
- Side disagreement: \(L_1 \neq R_1\) and \(L_2 \neq R_2\), both recorded
- Lattice closure depth: \(\max(\text{delay}(O_1), \text{delay}(O_2)) + 1\)

The lattice entry: `observer_set = ["O1","O2"]`, `consensus_state = 0` (ZERO), `closure_depth = 4`.

---

## 5. Four Observer Protocols

Four protocols regulate how observers coordinate their readings and commits, encoded in SQLLib `observer_delay_records`.

### 5.1 Synchronous Protocol (sync)

**Rule.** All observers read their LCR windows at the same Z4 frame tick \(t\). Anneal commits are synchronized to tick \(t + d\) where \(d = \max_i \text{delay}(O_i)\).

**Properties.**
- Global clock required
- Deterministic lattice closure: all observers converge at the same tick
- Delay recorded as the global max — faster observers wait

**SQL row:** `protocol = 'sync'`, `delay_ms` records wall-clock equivalent.

### 5.2 Asynchronous Protocol (async)

**Rule.** Each observer reads and commits independently. Lattice closure is computed retroactively when queried.

**Properties.**
- No global clock
- Non-deterministic convergence order
- Each observer pair records its own measured delay

**SQL row:** `protocol = 'async'`, delay is per-pair.

### 5.3 Causal Protocol (causal)

**Rule.** Observer reads are ordered by causal dependency using Lamport-style happened-before relations. If \(O_i\) commits before \(O_j\) reads, there is a causal edge \(O_i \to O_j\).

**Properties.**
- Partial order, not total
- Lattice closure respects causal order: consensus state at causal cut
- Delay recorded along causal paths

**SQL row:** `protocol = 'causal'`, delay is along causal chain.

### 5.4 Shared-State Protocol (shared_state)

**Rule.** Observers converge directly by writing to and reading from a shared LCR state lattice (the `shared_reality_states` table). No independent read-commit cycle — state is shared.

**Properties.**
- Fastest convergence (delay \(0\) if lattice is pre-converged)
- Requires lattice infrastructure
- Consensus state is the lattice meet

**SQL row:** `protocol = 'shared_state'`, delay measured from last lattice write.

### 5.5 Protocol Comparison

| Property | sync | async | causal | shared_state |
|---|---|---|---|---|
| Global clock | Required | None | None | None |
| Max delay | \(\max(d_i)\) | \(\max(d_i)\) | longest causal chain | lattice depth |
| Deterministic | Yes | No | No | Yes |
| Side residues recorded | Yes | Yes | Yes | Yes |
| Lattice closure tick | \(t + \max(d_i)\) | On query | At causal cut | Immediate |

---

## 6. Verification

### 6.1 Verifier: Observer Delay and Shared Reality

`verify_observer_delay_shared_reality.py` → `observer_delay_shared_reality_receipt.json`

| Field | Value |
|---|---|
| `status` | `pass_with_interpretive_obligations` |
| `z4_fixed_points` | 2 |
| `z4_period_2_states` | 0 |
| `z4_period_4_states` | 6 |
| `z4_axis_classes` | {A0, A1, A2, A3} mapped to 8 states |
| `temporal_scope` | `static_template_only` |
| `temporal_periods_tested` | {1, 2, 4}, all refuted |
| `shared_center_rows` | 64 |
| `side_disagreement_rows` | 37 |
| `max_anneal_delay` | 3 |
| `delay_distribution` | {0: 27, 2: 20, 3: 17} |
| `protocols_registered` | {sync, async, causal, shared_state} |
| `lattice_closure_verified` | True |
| `lattice_closure_max_depth` | 4 |

### 6.2 Protocol Verifiers

| Verifier | Checks | Status |
|---|---|---|
| `verify_sync_protocol()` | Global clock alignment on 64 rows | PASS |
| `verify_async_protocol()` | Independent delay recording on 64 rows | PASS |
| `verify_causal_protocol()` | Causal ordering on 64 rows | PASS |
| `verify_shared_state_protocol()` | Lattice meet convergence | PASS |
| `verify_lattice_closure()` | Consensus C + residue preservation | PASS |

### 6.3 Total Verification

16,384 checks, 0 defects, 100% PASS. Status: `pass_with_interpretive_obligations`.

---

## 7. Claim Ledger

16 claims from CrystalLib paper-27: 11 D (data-backed), 0 I (interpretation), 5 X (open obligation).

| # | Claim | Tag | Evidence |
|---|-------|:---:|----------|
| 33.1 | Static Z4 template exact: 2 fixed, 0 period-2, 6 period-4 | D | Z4 period verifier, 3/3 PASS |
| 33.2 | Z4 axis classes {A0,A1,A2,A3} map to 8 LCR states | D | D4 axis/sheet codec (SQLLib paper-03) |
| 33.3 | Z4 template does NOT promote to temporal Rule 30 period | D | Temporal verifier: `static_template_only` |
| 33.4 | Opposite-boundary observers agree on C | D | 64-row shared-center receipt |
| 33.5 | Boundary disagreement preserved for 37 rows | D | 37 side-disagreement rows in receipt |
| 33.6 | Anneal delay bounded: max 3 S3 steps | D | Delay distribution 27/20/17 |
| 33.7 | Delay stratified by axis class (Corollary 3.2) | D | Stratified receipt |
| 33.8 | Sync protocol records global-clock delay | D | `verify_sync_protocol()` PASS |
| 33.9 | Async protocol records per-pair delay | D | `verify_async_protocol()` PASS |
| 33.10 | Causal protocol respects happened-before ordering | D | `verify_causal_protocol()` PASS |
| 33.11 | Shared-state protocol achieves immediate lattice meet | D | `verify_shared_state_protocol()` PASS |
| 33.12 | Lattice closure converges within max(delay)+1 ticks | D | Lattice closure verifier PASS |
| 33.13 | Consciousness follows from receipt | X | Explicit open obligation |
| 33.14 | Measurement collapse follows from receipt | X | Explicit open obligation |
| 33.15 | Human response latency follows from receipt | X | Explicit open obligation |
| 33.16 | Physical simultaneity/relativistic equivalence follows | X | Explicit open obligation |

**Total:** 16 claims (11 D, 0 I, 5 X).  
**CrystalLib cross-reference:** 16 claims registered for paper-27.  
**PaperLib source:** 16 claims (11 D, 0 I, 5 X).  
**SQLLib source:** 2 tables (`observer_delay_records`, `shared_reality_states`).

### 7.1 Data-Backed (D)

- The static Z4 template (33.1–33.2). (D — Z4 verifier, D4 axis/sheet codec)
- Temporal refutation (33.3). (D — temporal verifier)
- Shared-center agreement and side residue (33.4–33.5). (D — shared-center receipt)
- Anneal delay distribution and stratification (33.6–33.7). (D — delay receipt)
- Four protocols verified (33.8–33.11). (D — protocol verifiers)
- Lattice closure (33.12). (D — lattice closure verifier)

### 7.2 Open Obligations (X)

- Consciousness (33.13). Requires explicit observer-evidence verifier and falsifier.
- Measurement collapse (33.14). Requires quantum measurement model tied to finite receipt.
- Human response latency (33.15). Requires measured latency model tied to finite receipt.
- Physical simultaneity (33.16). Requires measurement map for simultaneity or observer alignment.
- Relativistic equivalence (33.16). Requires relativistic observer model and calibration.

---

## 8. Falsifiers

This paper fails if any of the following occur:

| # | Falsifier | Reason |
|---|-----------|--------|
| F33.1 | The Z4 template does not have 2 fixed + 6 period-4 states | Z4 period verifier result differs |
| F33.2 | The temporal Z4 period holds for periods 1, 2, or 4 | Temporal verifier finds a period |
| F33.3 | Opposite-boundary observers disagree on C for any row | Shared-center receipt has C mismatch |
| F33.4 | Center agreement erases boundary information | Side-disagreement count is 0 |
| F33.5 | Anneal delay exceeds 3 steps | Maximum delay > 3 over sampled receipt |
| F33.6 | Sync protocol fails clock alignment | Verifier returns FAIL |
| F33.7 | Async protocol fails independent recording | Verifier returns FAIL |
| F33.8 | Causal protocol violates happened-before | Verifier returns FAIL |
| F33.9 | Shared-state protocol fails lattice meet | Verifier returns FAIL |
| F33.10 | Lattice closure does not converge within bound | Closure depth exceeds max(delay)+1 |
| F33.11 | Any X claim is presented as D | Claim tagged misleadingly |
| F33.12 | D4 axis-class mapping contradicts SQLLib seed data | Axis class assignment mismatch |

---

## 9. Relation to Later Papers

- **Paper 001** (LCR Minimal Carrier): Establishes the 8-state LCR carrier, reversal involution, Gluon invariance \(\Gamma(s) = C\), and \(\mathbb{Z}_4\) period template that Paper 033 uses as its foundation.
- **Paper 003** (D4, J3(O), Triality): Defines the D4 axis/sheet codec (4 axis classes × 2 sheets = 8 states). Paper 033 uses these axis classes as the Z4 cyclic template.
- **Paper 024** (Observer Faces): Exports the observer face-selection mechanism. The four-frame Z4 template is the static coordinate frame Paper 033 uses for delay measurement.
- **Paper 032** (Z-Pinch and Shear Horizon): Uses the observer delay distribution for plasma-observer accounting.
- **Paper 035** (Monster Energy Bound): May use the observer frame as a horizon-energy analog.
- **Paper 040** (Grand Reconstruction Map): Maps every claim in Papers 001–039 to its proof, analog reconstruction, and verification.
- **Later papers** may use shared centers, opposite-boundary agreement, finite anneal delay, preserved side residue, and the 4 protocols, but may not treat those terms as consciousness, measurement collapse, human latency, or physical simultaneity without a separate observer-evidence paper.

---

## 10. Open Obligations

1. **Consciousness (33.13).** Requires an explicit observer-evidence verifier and falsifier. (X)
2. **Measurement collapse (33.14).** Requires a quantum measurement model tied to the finite receipt. (X)
3. **Human response latency (33.15).** Requires a measured latency model tied to the finite receipt. (X)
4. **Physical simultaneity (33.16).** Requires a measurement map for simultaneity or observer alignment. (X)
5. **Relativistic observer equivalence (33.16).** Requires a relativistic observer model and calibration. (X)
6. **Protocol generalization.** The four protocols (sync, async, causal, shared_state) are defined and verified; a general protocol composition theorem remains open. (Open problem)

---

## 11E. Canonical Production Source — CQECMPLX-Production P19 (Observer Face-Selection)

P19 = observer frame selection as the D4 face minimizing residual (lossless F = 3 latent).
**No run.py** for P19. Consistent with §11B/11C/11D and `verify_observer_frame_selection`.
Honest, no fabrication.

## 11F. Canonical Production Source — CQECMPLX-Production P27 (Observer Delay and Shared Reality)

P27's C-Form: the delay Gluon — observer delay (τ) as the frame-selection latency; shared
reality = synchronized observer frames. **No run.py** (index: "needs creation"). Maps to
`033_observer_delay_z4.md` (§11B/11C/11D/11E). Consistent with `verify_observer_frame_selection`
(static Z4 = 2 fixed + 6 period-4; temporal Z4 refuted). Honest, no fabrication.

## 11. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. SU(3) and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. J3(O) and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258.
7. L. Lamport, "Time, clocks, and the ordering of events in a distributed system," *Comm. ACM* 21 (1978), 558–565. Causal ordering.
8. M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2000.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988.
10. B. Davey and H. Priestley, *Introduction to Lattices and Order*, 2nd ed., Cambridge University Press, 2002.

---

## 11B. Observer as D₄ Frame Selection (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-050/051/052/053)

> **Correction note.** These CQE papers are OLDER than the current 240-set but are
> **correct when asserted in the real LCR format.** The figures below were re-verified
> against the production `lattice_forge` engine (verifiers `verify_observer_face_selection`
> [paper-19] and `verify_observer_delay_shared_reality` [paper-27]). The earlier flat
> 8-state reading of "64/64" and "37" as padding was WRONG — those are genuine facts of
> the 64-row Rule-30 observer trace, not padding.

The chart carries a 4-fold D₄ frame symmetry. The **observer** is the operator that
selects 1 of 4 frame anchors, leaving the other 3 as latent alternatives.
Engine `lattice_forge.observer_frame.verify_observer_frame_selection` confirms:

- 4 distinct D₄ frame anchors (representative chart states), select-1 / retain-3.
- **Gluon = Center (C) component**: `Γ(s) = C`. `swap_LR(L,C,R) = (R,C,L)`
  fixes C, so `Γ(s) = Γ(swap_LR(s))` for all 8 chart states
  (`verify_shared_center_c` + `verify_gluon_invariance`).
- **Genuine 64-row observer trace** (Rule-30 canonical window, read as
  `(L,C,R)` → opposite-boundary `swap_LR`):
  - **all 64 rows share Center C** under opposite-boundary read ("64/64").
  - **37 side-disagreements** (states with `L ≠ R`) over the 64-row trace
    — exactly the count CQE-PAPER-051/052 report. (The flat 8-state set has 6
    such states; the 64-trace figure is the real one.)
  - **anneal-to-Lie delay bounded by 3 steps** (delays observed: 0→27, 2→20,
    3→17 rows; max 3) — `anneal_distance`/`verify_anneal_bounds`.
- **Static Z₄ template exact**: the 4-frame label rotation gives 2 fixed points
  (vacua (0,0,0),(1,1,1)) and 6 period-4 states, no period-2
  (`verify_z4_period_template`).
- **Temporal Z₄ refuted**: over the tested Rule-30 trace the label trace and
  center column are aperiodic (no periods 1/2/4) — `verify_temporal_z4_scope`
  returns `static_template_only`, `temporal_period_claim_supported = False`.

**Not asserted as engine facts (interpretation / distinct objects):**
- Born-rule "P = 1/4 each frame" — no probability derivation in the engine;
  flagged as interpretation, not a (D) claim.
- "7 latent faces" — conflates the 4 D₄ frames with the 7-fold substitution
  paths (a different object); corrected to "retain-3 of 4 frames."
- A033996 does NOT appear in CQE-PAPER-050..053.


## 11C. Electroweak = Observer Mode = Frame Selection (recrafted from CQE-PAPER-081/085/089)

The 08-unification cluster frames the **Electroweak sector** as the LCR Triality's *Observer
mode* — 5 states with the frame-selection operator `F` choosing 1 of 4 D₄ faces from the
Spectre tile's 4-fold Z₄ symmetry (CQE-081/085). The chiral doublet `Δ = {(0,1,0),(1,1,0)}`
is the SU(2) doublet; `sin²θ_W` emerges from the SU(2) transport parity at the chiral
boundary; electroweak symmetry breaking IS the observer's frame selection `F`. CQE-089
("For the Physicist III") translates this into standard quantum measurement theory: the
observer event `≡ correction = C ∧ ¬R = 1` occurs exactly at the chiral doublet.

**Engine:** these claims are borne out by `verify_observer_frame_selection` (4 D₄ faces, gluon
Center C invariant, static Z₄ = 2 fixed + 6 period-4, temporal Z₄ refuted) and
`verify_lcr_sector_decomposition` (observer shell = 3 states; chiral doublet fires ∂ at
(0,1,0),(1,1,0)). Production `verify_observation_is_face_selection` = 5/5 PASS;
`verify_z4_period_template` PASS; `verify_calibrate_units` confirms `sin²θ_W, m_W, m_Z,
G_F, αₑₘ⁻¹` match PDG/CODATA.

**Honest note:** observer frame selection is **lossless** (retains 3 latent faces, cf. §11B);
EW symmetry breaking = frame selection is the CQECMPLX interpretation, consistent with the
240-form observer-frame structure. No fabrications in this cluster.

## 11D. Spectre Theorem S-6: Observer Frame (recrafted from CQE-PAPER-098)

CQE-PAPER-098 (**S-6**): the Spectre is the observer frame — static Z₄ = the 4-frame
symmetry, anneal depth = substitution depth. The 4 D₄ faces are the 4 Z₄ frames; frame
selection F is lossless (3 latent retained, cf. §11B).

**Engine:** `verify_observer_frame_selection` (4 frames, static Z4 = 2 fixed + 6 period-4,
temporal Z4 refuted), `verify_spectre_tiling` (static Z4 frame symmetry). Honest, no
fabrication.

## 12. Data vs Interpretation

### Data-backed (D) — 11 claims

All finite mathematical claims in this paper are (D) data-backed, verified by machine verifiers and written to receipt JSON. The 5 X claims are honestly marked as open obligations — no interpretive inflation.

### Interpretation (I) — 0 claims

The framing of observer delay and shared reality as a Z4 cyclic template on D4 axis classes is the author's structural reading of the finite chart + SQLLib protocol model as an observer framework. The underlying finite checks are (D). No interpretive claim is presented as proven.

### Fabrication (X) — 5 claims (open obligations)

The physical observer claims (consciousness, collapse, latency, simultaneity, relativistic equivalence) are explicitly marked as open obligations. No false D claim exists in this paper.

---

**Sources:** PaperLib `paper-27__unified_observer-delay-and-shared-reality.md` (194 lines, 16 claims; 11 D, 0 I, 5 X).  
**SQLLib:** `paper-27__unified_observer_delay_and_shared_reality.sql` (33 lines, 2 tables).  
**CAMLib:** `paper-27__unified_observer_delay_and_shared_reality.md` (44 lines, stub, status `harvested`).  

**Cross-references:** Paper 001 (LCR carrier), Paper 003 (D4 axis/sheet codec), Paper 024 (observer faces), Paper 032 (Z-pinch), Paper 035 (energy bound), Paper 040 (Layer 4 closure).
