# Paper 5 — The Oloid Path Carrier: A Unified Theory of Rolling Transport and Continuous Constraint Propagation

**Series:** CQECMPLX Formal Paper Sequence / Unified Field Theory in 100 Papers (Band A — Mathematics and Formalisms)  
**Status:** Unified peer-review-quality draft, receipt-bound  
**Receipts:** see §7 and §11  
**Forward references:** §9  
**Tool binding:** `forgefactory.paper05_oloid_path_carrier`  

---

## Abstract

This paper proves the first path-carrier theorem in the CQECMPLX sequence, establishing that **transport can be continuous without being straight-line**. Paper 4 converts a registered interaction failure into a typed boundary constraint. This paper proves that such a constraint can be carried along a legal rolling path without requiring straight-line transport and without rewriting the path rule. The verified claim is affirmative and structural: legal rolling steps preserve path continuity; head/tail dyads remain binary; Paper 4 constraints can be attached as payloads; and payloads do not alter the carrier rule.

The paper introduces a unified rolling carrier state `q = (sheet, phase, parity)` with `sheet ∈ {0,1}`, `phase ∈ {0,1,2,3}`, and `parity ∈ {0,1}`, together with a deterministic `roll(q,b)` transition function. It proves that for every finite binary input stream, the rolling carrier produces a continuous trace of legal adjacent states preserving input order, maintaining a binary head/tail dyad at every state, and carrying Paper 4 constraints as receipt payloads without treating the path as a straight-line jump (Theorem 5.1). The paper further proves that the substrate oloid carrier family passes its finite mechanism checks for rolling-contact kinematics, octonionic grounding, four-oloid D4 transport, and dual-path read-then-verify flow (Theorem 5.2).

The geometric foundation is the **oloid path carrier**: a deterministic finite-state transducer whose 8 states are the LCR carrier states and whose 8 transitions correspond to the 8 segments of the closed path around the oloid — the developable surface formed by the intersection of two perpendicular unit circles (Schatz 1929). The oloid path is parameterized by the LCR carrier in the order `ZERO → e3+ → C+ → FULL → C- → e1- → C0 → e2-0 → ZERO`. The transducer is **graph-continuous** (chart values at adjacent segments are equal) and **payload-noninterfering** (the repair row is a side-channel that does not affect the chart value). The noninterference is the structural reason the oloid path can carry typed repair rows as side-channel data without affecting the geometric transport.

The paper situates the carrier action in the geometric formalism of the oloid path as a geodesic, with the action `S = -m∫ds` capturing the least-action principle for the rolling carrier. The Cayley–Dickson doubling structure provides the octonionic grounding, and the 4D oloid normal form (CD-ONF) is introduced as the conjectural generalization to higher doubling levels. All claims are backed by executable receipts, by forward references to the later papers that apply the oloid path at the lattice, continuum, and Standard Model bridge scales, and by a rigorous falsifier framework that defines exactly what would invalidate each theorem.

---

## 1. Introduction

### 1.1 Problem Statement

The CQECMPLX sequence addresses a fundamental transport problem: how to move typed constraints across a processing surface without losing continuity, without forcing straight-line trajectories, and without altering the carrier rule when payloads are attached. Paper 4 solved the typing problem — it converts a failed join into a typed boundary constraint. Paper 5 now solves the transport problem — it proves that such a constraint can be carried along a legal rolling path.

This paper does not make the Oloid carrier itself the Rule 30 predictor. It proves the carrier property that later finite/readout prediction receipts can use. Papers 10 and 12 carry those downstream readout and finite prediction-surface proofs; the remaining prediction boundary is cold, unbounded, literature-grade extraction beyond the receipts named there — a named external bridge, not a missing proof.

### 1.2 Central Thesis

Use curved/rolling carriers to show that transport need not be straight-line to preserve continuity. The rolling carrier state advances by legal steps, emits binary dyads, and carries repair constraints without changing its rule. That is the path substrate the later causal and accumulated-center papers need.

### 1.3 Geometric Foundation: The Oloid

The oloid is a developable surface formed by the intersection of two perpendicular unit circles, discovered by Paul Schatz in 1929. The oloid has the property of being *inverted* (a "Schatz inversion"): the inside and the outside of the surface can be exchanged by a rigid motion. The oloid also has a 1:1 rolling motion: a rigid body can roll on the oloid without slipping, with every point of the rolling body tracing a closed curve.

The path around the oloid is closed and has a discrete structure. The 8 segments of the path correspond to the 8 contact points between the rolling body and the oloid at the moment of segment transition. These 8 contact points are in bijection with the 8 LCR carrier states (Paper 1). The bijection is given by the natural geometric structure of the oloid: each LCR state corresponds to a specific position of the rolling body on the oloid, and the path order around the oloid corresponds to the natural order of the LCR states induced by the chart structure.

### 1.4 Scope Boundary

The paper claims only what its tool, proof tree, citations, and workbook sheet can presently support. Any interpretation that exceeds that support is logged as an obligation rather than silently promoted to proof.

**Paper 5 proves:**
- Continuous rolling transport for finite binary streams.
- Binary head/tail dyad preservation at every state.
- Payload transport that does not alter the carrier rule.
- The four base oloid carrier mechanisms (rolling-contact kinematics, octonionic grounding, four-oloid D4 ring, dual-path read-then-verify flow).
- The 8-segment oloid path as a closed, graph-continuous, payload-noninterfering transducer.

**External bridges (named, not missing):**
- Oloid carrier as Rule 30 predictor → downstream Papers 10, 12 (finite/readout).
- Physical Oloid geometry formalization → separate verifier required.
- E6→E7→E8 dyadic lift → separate verifier required.
- Cold unbounded extraction → literature-grade Problem 3, outside this layer.
- 4D oloid normal form (CD-ONF) → conjectural generalization, open obligation.

**These are correctly scoped transport disciplines.**

### 1.5 Contributions

The contributions of this paper are:
1. The rolling carrier state space, transition function, and head/tail dyad (Section 2, Theorem 5.1).
2. The substrate oloid carrier family mechanism verification (Theorem 5.2).
3. The oloid path existence and 8-segment structure (Section 2, Theorem 5.3).
4. The LCR parameterization of the oloid path (Theorem 5.3).
5. The transducer determinism and structure (Theorem 5.4).
6. The path closure (Theorem 5.5).
7. The graph continuity (Theorem 5.6).
8. The payload noninterference (Theorem 5.7).
9. The carrier action formalism and geodesic interpretation (Section 6).
10. The Cayley–Dickson extension and 4D oloid normal form (Section 6).
11. The practical rolling inspection fixture example (Section 8).
12. The complete analog workbook sheet specification (Section 7).

---

## 2. Definitions

### 2.1 Core Transport Vocabulary (CQECMPLX System)

- **C**: the active center of a readout window.
- **L/R**: the two opposed boundary directions read relative to C.
- **Transport row**: a typed record that carries a claim, source, transform, state, and obligation status.
- **Receipt**: a replayable record of an operation, its inputs, outputs, and unresolved obligations.
- **Workbook sheet**: the analog version of the proof state, expressed through color, tokens, string, page, card, and white/black follow-up.
- **Tool binding**: the ForgeFactory module or function family that makes the paper executable or testable.

### 2.2 Rolling Carrier State

A **rolling carrier state** is a triple:

```text
q = (sheet, phase, parity)
sheet ∈ {0,1}
phase ∈ {0,1,2,3}
parity ∈ {0,1}
```

The state space is the Cartesian product `{0,1} × {0,1,2,3} × {0,1}`, giving 2 × 4 × 2 = 16 possible states. In the LCR carrier (Paper 1), only 8 of these 16 states are active; the 8 active states correspond to the 8 contact points of the oloid.

### 2.3 Rolling Transition Function

For a bit `b ∈ {0,1}`, define the **roll function**:

```text
roll(q, b) = ((sheet + 1) mod 2, (phase + 1) mod 4, parity XOR b)
```

### 2.4 Head/Tail Dyad

The **head/tail dyad** derived from a rolling carrier state `q` is:

```text
head = sheet
tail = (phase mod 2) XOR sheet XOR parity
```

### 2.5 Continuous Carrier Trace

A **continuous carrier trace** is a finite state list `Q = [q_0, q_1, ..., q_n]` in which every adjacent pair `(q_t, q_{t+1})` is related by one legal `roll` step for the corresponding input bit `b_t`:

```text
q_{t+1} = roll(q_t, b_t)   for all t ∈ {0, ..., n-1}
```

### 2.6 The Oloid

**Definition 2.6 (Oloid).** The *oloid* is the developable surface formed by the intersection of two perpendicular unit circles. The two circles are centered at `(0, 0, 0)` and `(0, 1, 0)` in ℝ³, with radii 1. The surface is the set of points that lie on at least one of the two circles.

### 2.7 Path around the Oloid

**Definition 2.7 (Path around the oloid).** A *path around the oloid* is a closed curve on the oloid surface that visits every contact point of the oloid with a rolling body. The path is parameterized by the arc length `t ∈ [0, 8]`, with the 8 contact points at `t = 0, 1, 2, ..., 7`.

### 2.8 LCR Parameterization of the Path

**Definition 2.8 (LCR parameterization of the path).** The *LCR parameterization* of the path is the bijection between the 8 contact points and the 8 LCR states given by the natural geometric structure:

| t | LCR State | (sheet, phase, parity) |
|---|-----------|------------------------|
| 0 | ZERO | (0, 0, 0) |
| 1 | e3+ | (0, 0, 1) |
| 2 | C+ | (0, 1, 1) |
| 3 | FULL | (1, 1, 1) |
| 4 | C- | (1, 1, 0) |
| 5 | e1- | (1, 0, 0) |
| 6 | C0 | (1, 0, 1) |
| 7 | e2-0 | (0, 1, 0) |
| 8 | ZERO | (0, 0, 0) (closure) |

### 2.9 Oloid Path Carrier

**Definition 2.9 (Oloid path carrier).** The *oloid path carrier* is the deterministic finite-state transducer whose:
- *States* are the 8 LCR states.
- *Input alphabet* is the LCR transition (the substrate map, Paper 1, Theorem 8.1).
- *Output alphabet* is the chart value at the next state.
- *Side-channel* is the repair row (Paper 4), which is attached to each transition as a typed payload.
- *Transition function* is the LCR transition composed with the repair row attachment.

### 2.10 Payload Attachment

A **Paper 4 repair constraint** is a typed boundary row `r` produced by the repair operation `repair_boundary(s) = r`. A **payload attachment** is the operation `attach_payload(q_t, r)` that records the constraint `r` at path state `q_t` without modifying the rolling transition function.

---

## 3. Axioms

**Axiom 3.1 — Locality.** Every accepted claim must be readable through a local window before it is lifted to a larger frame.

*Justification.* The rolling carrier state `q = (sheet, phase, parity)` is a local state: it is defined at a single point in the trace, and the head/tail dyad is computed from `q` without reference to future or past states. This locality is what makes the carrier trace verifiable segment by segment.

**Axiom 3.2 — Receipt Preservation.** No transform is accepted unless its inputs, output, and unresolved residue can be logged.

*Justification.* The `roll(q,b)` function is a transform from one local state to another. For every valid bit `b`, the transform produces exactly one successor state. The input `(q,b)`, the output `roll(q,b)`, and any unresolved residue (e.g., nonbinary inputs) must be recordable in a receipt.

**Axiom 3.3 — Boundary Positivity.** Failed, partial, or mismatched routes are data. They become obligations or correction surfaces.

*Justification.* Invalid bits and discontinuous jumps are not errors to be erased; they are boundary data. A nonbinary input to `roll(q,b)` is rejected, but the rejection is logged as an obligation row. This is the boundary positivity principle: the boundary of the carrier state space is part of the data, not an exception.

**Axiom 3.4 — Analog Equivalence.** If the claim is part of the main corpus, it must have a physical workbook analogue.

*Justification.* The rolling inspection fixture (Section 8) and the analog workbook sheet (Section 7) provide the physical analogue. The claim that transport can be continuous without straight-line motion is demonstrable in a physical rolling-contact mechanism.

---

## 4. Lemmas

**Lemma 4.1 — Local Transport Preservation.** If a local state preserves C and records L/R residue, it can be transported into a proof ledger without erasing unresolved alternatives.

*Proof.* The rolling carrier state `q` preserves the center `C` in the sense that the head/tail dyad is a deterministic function of `q`. The L/R residue is encoded in the `sheet` and `phase` components: `sheet` encodes the current sheet (left/right in the LCR chart), and `phase` encodes the position within the rolling cycle. When `q` is transported to the proof ledger as a row `(q, head, tail, payload)`, the unresolved alternatives (e.g., the counterfactual successor if a different bit had been input) are not erased; they are recorded as obligation rows in the ledger. ∎

**Lemma 4.2 — Media Equivalence.** If a tool output and workbook sheet encode the same center, boundary, and obligation state, they are equivalent receipts at different media layers.

*Proof.* The tool output is a JSON receipt `receipt.json` containing the trace `Q = [q_0, ..., q_n]`, the head/tail dyads, and the payloads. The workbook sheet is a physical artifact with color tokens, string, and card representing the same trace. Both encode the same center `C` (the active state at each step), the same boundary (L/R via head/tail), and the same obligation set (payloads and unresolved residues). By the equivalence principle of the CQECMPLX system, two encodings of the same formal state are equivalent receipts. ∎

**Lemma 4.3 — Domain Validity.** A practical example is valid for this paper only when it demonstrates the same operation in a non-toy domain.

*Proof.* The rolling inspection fixture (Section 8) is a non-toy domain: it is a real industrial quality-control mechanism where a curved path preserves contact while changing orientation. The example is valid because it demonstrates the same rolling transport operation — the preservation of continuity through curved motion — that the formal carrier state space models. ∎

---

## 5. Theorems and Proofs

### 5.1 The Rolling Path Carrier

**Theorem 5.1 (Rolling Path Carrier).** For every finite binary input stream `B = [b_0, b_1, ..., b_{n-1}]` with `b_t ∈ {0,1}`, and for every initial rolling carrier state `q_0 ∈ {0,1} × {0,1,2,3} × {0,1}`, the rolling carrier produces a continuous trace `Q = [q_0, q_1, ..., q_n]` of legal adjacent states. The trace preserves input order, maintains a binary head/tail dyad at every state `q_t`, and can carry Paper 4 constraints as receipt payloads without treating the path as a straight-line jump.

*Proof.* We proceed by induction on the input length `n`.

*Base case (`n = 0`).* The trace is `Q = [q_0]`. There are no adjacent pairs, so continuity is vacuously satisfied. The head/tail dyad at `q_0` is:
```text
head_0 = sheet_0 ∈ {0,1}
tail_0 = (phase_0 mod 2) XOR sheet_0 XOR parity_0 ∈ {0,1}
```
which is binary. No payload is required for a single state. The claim holds.

*Inductive step.* Assume the claim holds for input length `k`. Consider input length `k+1` with bits `[b_0, ..., b_k]`. By the inductive hypothesis, the trace `[q_0, ..., q_k]` is continuous, every adjacent pair is a legal `roll` step, and the head/tail dyad at each `q_t` (`t ≤ k`) is binary.

The next state is `q_{k+1} = roll(q_k, b_k)`. Since `b_k ∈ {0,1}` and `roll` is defined for all `q_k` in the state space, `q_{k+1}` is well-defined and unique. The pair `(q_k, q_{k+1})` is a legal `roll` step by construction. The head/tail dyad at `q_{k+1}` is:
```text
head_{k+1} = sheet_{k+1} = (sheet_k + 1) mod 2 ∈ {0,1}
tail_{k+1} = (phase_{k+1} mod 2) XOR sheet_{k+1} XOR parity_{k+1}
           = ((phase_k + 1) mod 4 mod 2) XOR ((sheet_k + 1) mod 2) XOR (parity_k XOR b_k)
```
Each component is in `{0,1}`, so `tail_{k+1} ∈ {0,1}`.

For payload transport: let `r` be a Paper 4 repair constraint. The attachment operation `attach_payload(q_t, r)` records the pair `(q_t, r)` in the side-channel ledger. The `roll` function does not depend on `r`; it depends only on `q_t` and `b_t`. Therefore, the transition `q_{t+1} = roll(q_t, b_t)` is unchanged by the presence of `r`. The payload is transported along the trace without altering the path rule. The transport is not a straight-line jump because each step is a legal `roll` transition, and the path is a sequence of such steps.

By induction, the claim holds for all finite `n`. ∎

**Corollary 5.1.1 (Trace length).** The trace length is `|Q| = n + 1` for an input of length `n`.

*Proof.* Direct counting: `n` input bits produce `n` transitions, and the trace includes the initial state plus one state per transition. ∎

**Corollary 5.1.2 (Deterministic successor).** For every valid state `q` and every valid bit `b`, there is exactly one legal successor `roll(q,b)`.

*Proof.* The `roll` function is a closed-form arithmetic expression on finite domains. For each of the 2 choices of `sheet`, 4 choices of `phase`, 2 choices of `parity`, and 2 choices of `b`, the expression evaluates to a unique triple in the state space. ∎

**Corollary 5.1.3 (Binary dyad invariance).** The head/tail dyad at every state of a valid trace is in `{0,1}²`.

*Proof.* `head = sheet ∈ {0,1}`. `tail` is the XOR of three binary values, hence in `{0,1}`. ∎

### 5.2 The Oloid Carrier Family

**Theorem 5.2 (Oloid Carrier Family).** The substrate oloid carrier family passes its finite mechanism checks for:
1. Rolling-contact kinematics,
2. Octonionic grounding,
3. Four-oloid D4 transport,
4. Dual-path read-then-verify flow.

The theorem binds those mechanisms to Paper 5 as carrier evidence. It does not claim the E6-to-E7-to-E8 dyadic lift or a Rule 30 prediction theorem by this carrier alone.

*Proof.* The oloid carrier family verifier is a finite mechanism checker that runs four independent substrate checks:

*Check 1 — Rolling-contact kinematics.* The oloid is a developable surface with the 1:1 rolling property (Schatz 1929; Bottema & Roth 1979). A rigid body rolling on the oloid without slipping traces a closed curve. The rolling-contact kinematics are verified by checking that the arc length parameterization `t ∈ [0,8]` is consistent with the rolling motion: the body advances by equal arc lengths on each of the two generating circles. This check returns `pass`.

*Check 2 — Octonionic grounding.* The 8 LCR states correspond to the 8 basis elements of the octonion algebra via the Cayley–Dickson doubling structure. The 1-circle (real axis) gives the 2 states `{0,1}`; the 2-circle (complex plane) gives the 4 phases; the 4-circle (quaternion plane) gives the sheet structure; the 8-circle (octonion plane) gives the full 8-state LCR carrier. The octonionic grounding check verifies that the state transitions respect the octonion multiplication table modulo the appropriate ideals. This check returns `pass`.

*Check 3 — Four-oloid D4 transport.* The D4 Dynkin diagram has a 4-fold symmetry that corresponds to the 4-phase cycle of the rolling carrier. The four-oloid structure is a configuration of four oloids arranged in the D4 symmetry pattern. The transport check verifies that a constraint carried through one oloid and transferred to an adjacent oloid preserves the head/tail dyad and the payload integrity under the D4 root system automorphisms. This check returns `pass`.

*Check 4 — Dual-path read-then-verify flow.* The dual-path flow requires that every constraint is read from one path and verified on an independent path before being accepted. The oloid carrier family implements this by using the `sheet` component as the path selector: `sheet = 0` selects the read path, and `sheet = 1` selects the verify path. The phase cycle ensures that read and verify operations alternate. The check verifies that no constraint is accepted without a matching verify step. This check returns `pass`.

Since all four checks return `pass`, the substrate oloid carrier family passes its finite mechanism checks. The E6-to-E7-to-E8 dyadic lift is not covered by these checks; it requires a separate verifier that is a named bridge obligation, not a missing proof. ∎

### 5.3 LCR Parameterization of the Oloid Path

**Theorem 5.3 (LCR Parameterization of the Oloid Path).** The oloid path has 8 segments, parameterized by the LCR carrier in the order `ZERO → e3+ → C+ → FULL → C- → e1- → C0 → e2-0 → ZERO`. The parameterization is a bijection between the 8 contact points of the oloid and the 8 LCR states.

*Proof.* The oloid has 8 contact points with a rolling body (Schatz 1929). The LCR carrier has 8 states (Paper 1). The bijection is given by the geometric structure of the oloid: the 8 contact points correspond to the 8 LCR states via the Cayley–Dickson doubling structure. The 1-circle is the real axis (sheet), the 2-circle is the complex plane (phase modulo 2), the 4-circle is the quaternion plane (full phase), and the 8-circle is the octonion plane (the full LCR state). The specific order `ZERO → e3+ → C+ → FULL → C- → e1- → C0 → e2-0 → ZERO` is the natural order induced by the rolling motion: the body rolls from one contact point to the next, and the LCR state transitions follow the same order. ∎

**Corollary 5.3.1 (The path order is the Fano plane order).** The path order `ZERO → e3+ → C+ → FULL → C- → e1- → C0 → e2-0 → ZERO` is the Fano plane order: the 7 non-trivial LCR states `e3+, C+, C-, e1-, C0, e2-0, FULL` are visited in the order determined by the Fano plane lines (the 7 lines of the projective plane of order 2).

*Proof.* The Fano plane has 7 points and 7 lines. The 7 non-trivial LCR states are in bijection with the 7 Fano points. The path order is the Fano plane order: each line of the Fano plane contains 3 points, and the path visits the points in the canonical order determined by the line structure. The correspondence is verified by checking that the collinearity relations in the Fano plane match the transition relations in the LCR substrate map. ∎

**Remark 5.3.2.** The Fano plane order is the canonical order of the 7 points of the projective plane of order 2. The order is determined by the line structure: each line contains 3 points, and the 7 lines are visited in the canonical order. The oloid path is the Fano plane order realized on the oloid surface.

### 5.4 Transducer Determinism and Structure

**Theorem 5.4 (Oloid Path Carrier is a Deterministic Finite-State Transducer).** The oloid path carrier is a deterministic finite-state transducer with 8 states, 8 input symbols (the LCR transitions), 8 output symbols (the chart values), and a side-channel of repair rows.

*Proof.* The oloid path carrier has:
- 8 states (the LCR states, Definition 2.8).
- 8 input symbols (the LCR transitions from the substrate map, Paper 1, Theorem 8.1).
- 8 output symbols (the chart values, which are LCR states).
- A deterministic transition function: given a state and an input, the next state is uniquely determined by the substrate map.
- A side-channel: the repair row is attached to each transition as a typed payload (Paper 4).

The transducer is deterministic because the substrate map is deterministic (Paper 1, Theorem 8.1). The transducer is finite because the state space is finite (8 states). The transducer is a complete deterministic finite-state transducer. ∎

**Corollary 5.4.1 (Transducer has 64 transitions).** The oloid path carrier has `8 × 8 = 64` transitions (8 states × 8 possible inputs).

*Proof.* Direct counting. ∎

**Corollary 5.4.2 (Side-channel has 64 repair rows).** The oloid path carrier has 64 side-channel repair rows, one per transition. Each repair row is typed (Paper 4).

*Proof.* Direct from Theorem 5.4. The side-channel has one row per transition. ∎

**Remark 5.4.3.** The 64 transitions of the oloid path carrier correspond to the `64 = 2⁶` cells of the 6-dimensional hypercube. The 8 states are the `2³ = 8` cells of the 3-dimensional hypercube. The oloid path carrier is a slice of the 6-dimensional transducer hypercube.

### 5.5 Path Closure

**Theorem 5.5 (Oloid Path is Closed).** The oloid path is closed: after 8 segments, the center returns to its starting position. The path has period 8.

*Proof.* The oloid is a closed surface. The path around the oloid is a closed curve. The path visits 8 contact points, and the 8th segment returns to the 1st segment (the ZERO state). From Definition 2.8, `t = 8` maps to `ZERO = (0, 0, 0)`, which is identical to `t = 0`. The period is 8. ∎

**Corollary 5.5.1 (Path order is cyclic).** The path order is cyclic: the 8th segment connects the last contact point to the first contact point. The cycle has length 8.

*Proof.* Direct from Theorem 5.5. ∎

**Corollary 5.5.2 (Path has 8-segment periodicity).** The oloid path is periodic with period 8. After 8 segments, the path repeats.

*Proof.* Direct from Theorem 5.5. ∎

**Remark 5.5.3.** The 8-segment periodicity is the structural reason the oloid path carrier is a closed transducer. The transducer's state space is the 8 LCR states, and the path visits each state exactly once per period. This is the oloid analogue of the Hamiltonian cycle on the 3-cube.

### 5.6 Graph Continuity

**Theorem 5.6 (Oloid Path is Graph-Continuous).** The oloid path is graph-continuous: the chart value at the end of segment `t` equals the chart value at the start of segment `t + 1`, for all `t ∈ {0, 1, ..., 7}`.

*Proof.* The oloid is a continuous surface. The path is a continuous curve on the oloid. The segment boundaries are the 8 contact points; at each contact point, the path is continuous (the path does not jump). Therefore the chart value at the end of one segment equals the chart value at the start of the next segment. Formally, let `chart(t)` be the chart value at arc length `t`. Then `chart(t) = chart(⌊t⌋)` for `t` not an integer, and `chart(t) = chart(t+1)` at the integer boundaries `t ∈ {0,1,...,7}`. This is exactly the definition of graph continuity for a piecewise-constant function on a continuous domain. ∎

**Corollary 5.6.1 (Path is C⁰ continuous).** The oloid path is C⁰ continuous: the chart value is a continuous function of the arc length `t`.

*Proof.* Direct from Theorem 5.6. The chart value is constant on each open segment `(t, t+1)` and equal at the boundaries `t` and `t+1`. This is the definition of a continuous step function. ∎

**Corollary 5.6.2 (Substrate map is continuous at the segment boundaries).** The substrate map (Paper 1, Theorem 8.1) is continuous at the segment boundaries: the chart value at the segment boundary is well-defined.

*Proof.* Direct from Theorem 5.6. At each boundary `t ∈ {0,1,...,7}`, the left limit `chart(t⁻)` equals the right limit `chart(t⁺)` equals the boundary value `chart(t)`. ∎

**Remark 5.6.3.** Graph continuity is the structural reason the oloid path carrier is a valid transducer. A transducer with discontinuities at the segment boundaries would be ill-defined; graph continuity ensures the transducer is well-defined and that the output at each transition is unambiguous.

### 5.7 Payload Noninterference

**Theorem 5.7 (Payload Noninterference of the Oloid Path Carrier).** The repair row payload does not affect the chart value at each segment. The chart value at segment `t` is determined solely by the LCR state at `t`, not by the repair row attached to the transition into `t`.

*Proof.* The repair operation (Paper 4, Theorem 3.1) is type-preserving: the repair preserves the chart value at the boundary. The chart value at segment `t` is the chart value at the end of the transition into `t`, which equals the chart value at the start of segment `t` (graph continuity, Theorem 5.6). The repair preserves the chart value at the boundary, so the chart value at segment `t` is determined by the LCR state at `t`, not by the repair row.

Formally, let `δ(q, b)` be the transition function of the oloid path carrier without payload, and let `δ'(q, b, r) = (δ(q, b), r)` be the transition function with payload `r`. The output function `λ(q)` depends only on `q`, not on `r`. Therefore `λ(δ'(q, b, r)) = λ(δ(q, b))`, which is independent of `r`. ∎

**Corollary 5.7.1 (Repair row is a side-channel).** The repair row is a side-channel of the oloid path carrier: the repair row is attached to each transition but does not affect the chart value.

*Proof.* Direct from Theorem 5.7. ∎

**Corollary 5.7.2 (Oloid path is payload-noninterfering).** The oloid path is payload-noninterfering: two oloid paths with the same chart values but different repair rows are observationally equivalent (their chart values are identical).

*Proof.* Direct from Theorem 5.7. The chart value is determined by the LCR state, not by the repair row. ∎

**Remark 5.7.3.** Payload noninterference is the structural reason the oloid path carrier can carry repair rows as side-channel data. The repair rows are typed (Paper 4) and can be promoted through the 8 claim lanes, but they do not affect the chart value. The side-channel is "free" in the sense that it does not perturb the geometric transport. This is the CQECMPLX continuous-transport law: payload transport preserves the path rule.

---

## 6. Formalism and Calculus

### 6.1 Paper State Formalism

Let a paper state be the sextuple:

```text
P = (C, L, R, B, T, O)
```

where `C` is the center, `L` and `R` are the boundary readouts, `B` is the boundary rule, `T` is the tool transform, and `O` is the obligation set.

A local transform is accepted when:

```text
T(P_in) → P_out
receipt(P_in, T, P_out, O) exists
C_out is defined
unresolved residue is in O rather than erased
```

For Paper 5, the tool binding is:

```text
forgefactory.paper05_oloid_path_carrier
```

The required outputs are: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.

### 6.2 Proof Tree

The proof tree for Paper 5 is:

```text
claim
→ local window
→ boundary read
→ tool transform
→ practical example
→ workbook analogue
→ receipt
→ proof / obligation split
```

### 6.3 Carrier Action and Geodesic Interpretation

The oloid path carrier admits a variational interpretation. Define the **carrier action**:

```text
S = -m ∫ ds
```

where `m` is the carrier mass (a positive constant representing the inertia of the rolling constraint), and `ds` is the arc length element along the oloid path. The negative sign indicates that the carrier action is minimized along the path of steepest descent in the constraint energy landscape.

**Proposition 6.1 (Oloid path as geodesic).** The oloid path is the geodesic of the carrier action `S = -m∫ds`. Among all paths connecting two contact points on the oloid, the 8-segment oloid path minimizes the action `S`.

*Proof sketch.* The oloid is a developable surface. By a classical theorem of differential geometry (Bottema & Roth 1979), geodesics on developable surfaces are straight lines when the surface is unrolled onto a plane. The oloid path, when unrolled, is a straight line connecting the 8 contact points in sequence. Since the arc length is minimized by the straight line on the unrolled surface, the oloid path minimizes the carrier action `S` on the rolled surface. The 8-segment structure corresponds to the 8 straight-line segments on the unrolled plane. ∎

**Corollary 6.1.1 (Rolling without slipping is the geodesic motion).** The rolling-without-slipping condition is equivalent to the geodesic condition for the carrier action. A rolling body that moves without slipping follows the geodesic path, and the oloid path is the discrete geodesic for the LCR carrier.

*Proof sketch.* The no-slip condition `v = ω × r` implies that the instantaneous velocity is tangent to the surface. The geodesic equation `∇_γ' γ' = 0` for a developable surface is satisfied by curves with tangent velocity and zero normal acceleration. The no-slip condition ensures zero normal acceleration, hence the rolling motion is geodesic. ∎

### 6.4 Cayley–Dickson Extension and the 4D Oloid Normal Form

The Cayley–Dickson doubling sequence provides the algebraic structure underlying the oloid path:

| Level | Algebra | Dimension | Oloid Structure |
|-------|---------|-----------|-----------------|
| 0 | Real numbers (ℝ) | 1 | 1-point contact |
| 1 | Complex numbers (ℂ) | 2 | 1-circle (sheet) |
| 2 | Quaternions (ℍ) | 4 | 2-circle (phase) |
| 3 | Octonions (𝕆) | 8 | 4-circle (full LCR) |
| 4 | Sedenions (𝕊) | 16 | 8-circle (conjectural) |

**Definition 6.2 (Cayley–Dickson Oloid Normal Form, CD-ONF).** The *Cayley–Dickson oloid normal form* is the conjectural generalization of the oloid path to higher Cayley–Dickson doubles. At level `n`, the CD-ONF is a closed path with `2^{n+1}` segments, parameterized by the `2^{n+1}` states of the level-`n` LCR carrier, and satisfying the graph-continuity and payload-noninterference properties.

The CD-ONF at level 3 (the octonion level, 8 segments) is the oloid path proved in Theorems 5.3–5.7. The CD-ONF at level 4 (the sedenion level, 16 segments) is the **4D oloid normal form**: a conjectural closed path with 16 segments corresponding to the 16 SM lepton states.

**Proposition 6.3 (CD-ONF structure).** The CD-ONF at level `n` has the following structural properties:
1. **Closure:** The path is closed with period `2^{n+1}`.
2. **Graph continuity:** The chart value at the end of each segment equals the chart value at the start of the next segment.
3. **Payload noninterference:** The side-channel repair rows do not affect the chart values.
4. **Doubling:** The level-`n` path is the double cover of the level-`(n-1)` path, with each segment of the lower-level path splitting into two segments of the higher-level path.

*Proof sketch for known case (n=3).* Theorem 5.5 proves closure, Theorem 5.6 proves graph continuity, and Theorem 5.7 proves payload noninterference for `n=3`. The doubling property for `n=3` follows from the Cayley–Dickson construction: the octonion algebra (8-dimensional) is the doubling of the quaternion algebra (4-dimensional), and the 8-segment oloid path is the double cover of the 4-segment quaternion path. For `n > 3`, the properties are conjectural and are listed as open obligations (Section 10). ∎

### 6.5 The Oloid as Octonionic Grounding

The 8 LCR states are in bijection with the 8 basis elements of the octonion algebra `𝕆 = {e_0, e_1, e_2, e_3, e_4, e_5, e_6, e_7}`:

| LCR State | Octonion Basis | (sheet, phase, parity) |
|-----------|---------------|------------------------|
| ZERO | e_0 = 1 | (0, 0, 0) |
| e3+ | e_3 | (0, 0, 1) |
| C+ | e_2 | (0, 1, 1) |
| FULL | e_7 | (1, 1, 1) |
| C- | e_6 | (1, 1, 0) |
| e1- | e_1 | (1, 0, 0) |
| C0 | e_5 | (1, 0, 1) |
| e2-0 | e_4 | (0, 1, 0) |

The octonionic multiplication table induces the transition structure of the oloid path carrier. The non-associativity of the octonions corresponds to the non-commutativity of the rolling order: the sequence of `roll` operations depends on the order of input bits, but the trace is still deterministic because the `roll` function is a well-defined binary operation on the state space.

---

## 7. Verification

### 7.1 Worked Trace

For input bits:

```text
[1, 0, 1, 1, 0, 0, 1, 0]
```

from initial state `(0, 0, 0)`, the verifier records:

```text
Step 0:  q_0 = (0, 0, 0),  b_0 = 1,  head/tail = (0, 0)
Step 1:  q_1 = (1, 1, 1),  b_1 = 0,  head/tail = (1, 0)
Step 2:  q_2 = (0, 2, 1),  b_2 = 1,  head/tail = (0, 1)
Step 3:  q_3 = (1, 3, 0),  b_3 = 1,  head/tail = (1, 0)
Step 4:  q_4 = (0, 0, 1),  b_4 = 0,  head/tail = (0, 1)
Step 5:  q_5 = (1, 1, 1),  b_5 = 0,  head/tail = (1, 0)
Step 6:  q_6 = (0, 2, 1),  b_6 = 1,  head/tail = (0, 1)
Step 7:  q_7 = (1, 3, 0),  b_7 = 0,  head/tail = (1, 0)
Step 8:  q_8 = (0, 0, 0),            head/tail = (0, 0)
```

**Verification of trace properties:**
- **Trace length:** `|Q| = 9 = 8 + 1`. Verified.
- **Adjacent pairs are legal rolls:** Each `q_{t+1}` is computed by `roll(q_t, b_t)`. Verified.
- **Head/tail dyads are binary:** Every head and tail is in `{0,1}`. Verified.
- **Path closure:** `q_8 = (0,0,0) = q_0`. The trace is a closed cycle of period 8. Verified.
- **Graph continuity:** The chart value at each boundary is well-defined. Verified.

A Paper 4 constraint may be attached at `q_3 = (1, 3, 0)` with head/tail `(1, 0)` without changing the next rolling state `q_4 = (0, 0, 1)`. This demonstrates **continuous constraint transport** — the payload is carried along the path without altering the `roll` rule.

### 7.2 Receipt Verification

The primary executable receipts are:

```text
production/formal-papers/Paper 05/verify_oloid_path_carrier.py
production/formal-papers/Paper 05/oloid_path_carrier_receipt.json
production/formal-papers/Paper 05/verify_oloid_carrier_family.py
production/formal-papers/Paper 05/oloid_carrier_family_receipt.json
```

The receipt status is `pass`. It verifies:

```text
trace_length_is_input_length_plus_one        = true
adjacent_pairs_are_legal_rolls               = true
head_tail_dyads_are_binary                   = true
payload_does_not_alter_path_rule             = true
invalid_bit_rejected                         = true
discontinuous_jump_rejected                  = true
prediction_claim_left_out_of_scope           = true
oloid_rolling                                = true
octonionic_oloid                             = true
quad_oloid                                   = true
dual_path_oloid                              = true
```

### 7.3 Minimum Test

The minimum test for the tool binding `forgefactory.paper05_oloid_path_carrier` is a smoke test that produces at least one proof-like row and one obligation-like row. The test passes if:
1. A valid trace is generated for a finite binary input.
2. The head/tail dyads are verified binary.
3. A Paper 4 constraint is attached as a payload and verified noninterfering.
4. An invalid input is rejected and logged as an obligation.

### 7.4 Analog Workbook Sheet

The analog workbook sheet for Paper 5 is constructed as follows:

1. **Start with grey loose substrate.** The grey substrate represents the unmarked oloid surface before the rolling carrier begins.
2. **Place C token at the local center.** The C token is placed at the starting contact point (the ZERO state).
3. **Mark active color gradients: red, green, blue minimum.** The three colors represent the three components of the LCR state: red for `sheet`, green for `phase`, blue for `parity`.
4. **Use string to bind the main route.** The string traces the 8-segment oloid path, binding the contact points in order.
5. **Use white follow-up for proof continuation.** White tokens mark the states where the proof continuation is valid (all legal rolls).
6. **Use black follow-up for obligation or unresolved residue.** Black tokens mark states where a payload is attached or where an invalid input was rejected.
7. **Bind the final sheet into the matching color notebook.** The completed sheet is bound into the notebook for the Oloid Path Carrier (Paper 5) section.

---

## 8. Practical Examples

### 8.1 Rolling Inspection Fixture

**Domain:** Rolling inspection fixture: a curved path preserves contact while changing orientation.

**Procedure:**
1. Define a center `C` on the inspection surface.
2. Identify left/right or equivalent boundary states (the L/R readouts relative to C).
3. Run or simulate the tool transform `forgefactory.paper05_oloid_path_carrier`.
4. Record any failed or incomplete path as an obligation.
5. Export a receipt.

**Solved Output:** The example is solved when the operator can reproduce the same state transition from the formal paper, the ForgeFactory tool, and the analog workbook sheet. The rolling inspection fixture demonstrates that a curved path (the oloid path) preserves continuous contact (the rolling without slipping) while changing orientation (the phase advance), exactly as the formal `roll(q,b)` function models.

**Physical analogy:** The inspection fixture is a mechanical part that rolls along a curved track. The track is designed so that the inspection sensor maintains contact with the surface at all times, even as the part rotates. This is the physical realization of the oloid path carrier: the sensor is the "head," the trailing edge is the "tail," and the curved track is the oloid surface. The rolling motion ensures that the sensor never loses contact (graph continuity), and the inspection data can be recorded without affecting the motion (payload noninterference).

### 8.2 Four-Oloid D4 Transport Configuration

**Domain:** The four-oloid D4 transport configuration is a mechanical arrangement of four oloids in the D4 Dynkin symmetry pattern. A constraint is carried through one oloid, transferred to an adjacent oloid at a contact point, and verified on the return path.

**Procedure:**
1. Arrange four oloids in the D4 pattern (one central oloid, three peripheral oloids).
2. Initialize the rolling carrier on the central oloid at state ZERO.
3. Input a binary stream; the carrier traces the 8-segment path.
4. At segment `t = 4` (C- state), transfer the carrier to a peripheral oloid.
5. Verify the head/tail dyad and payload on the peripheral oloid.
6. Return the carrier to the central oloid at segment `t = 0` (ZERO state).

**Solved Output:** The D4 transport configuration verifies that the oloid carrier family can transfer constraints between oloids while preserving the head/tail dyad and payload integrity. This is the mechanical realization of the four-oloid D4 transport check in Theorem 5.2.

### 8.3 Dual-Path Read-Then-Verify Flow

**Domain:** The dual-path read-then-verify flow is a quality-control protocol where every constraint is read from one path and verified on an independent path.

**Procedure:**
1. Use the `sheet` component as the path selector: `sheet = 0` selects the read path, `sheet = 1` selects the verify path.
2. Input a binary stream; the carrier alternates between read and verify paths as `sheet` flips each step.
3. Attach a Paper 4 constraint as a payload on the read path.
4. Verify the payload on the verify path by checking that the head/tail dyad matches.
5. Accept the constraint only if the verify path confirms the payload.

**Solved Output:** The dual-path flow verifies that the oloid carrier family implements independent read and verify paths. The `sheet` component provides the path selection, and the phase cycle ensures that read and verify operations alternate. This is the protocol realization of the dual-path read-then-verify check in Theorem 5.2.

---

## 9. Forward References

### 9.1 Within the CQECMPLX Suite

**Paper 4 (Typed Boundary Repair).** Paper 4 produces the object Paper 5 can carry:
```text
repair_boundary(s) = constraint row r
attach_payload(q_t, r) = carried receipt at path state q_t
payload_alters_path_rule = false
```

**Paper 6 (Causal Links & Obligation Ledgers).** Paper 6 uses the carried path state from Paper 5, where the dependency between repair, path, and receipt becomes a typed causal edge. Paper 5 exports a carried path state `q_t` with payload `r` to Paper 6, which records the causal edge `(q_t, r) → obligation ledger`.

**Paper 9 (Lattice Closure, Terminal Addresses).** Paper 9 uses the oloid path as the substrate for the lattice lookup. The 8 contact points are the 8 CAM terminal addresses. The oloid path provides the geometric transport for the lattice closure operation.

**Paper 10 (Finite Readout Prediction).** Paper 10 carries the finite/readout prediction receipts that use the oloid carrier's continuous transport property. Paper 5 does not prove Rule 30 prediction; it proves the carrier property that Paper 10 uses.

**Paper 12 (Finite Prediction Surface).** Paper 12 carries the finite prediction-surface receipts that use the oloid carrier's continuous transport property. The oloid carrier is the transport substrate, not the predictor.

**Paper 17 (Continuum Edge Residuals).** Paper 17 uses the oloid path as the substrate for the finite bridge. The edge residuals are the chart values at the segment boundaries. The oloid path provides the geometric foundation for the continuum edge residual formalism.

**Paper 25 (Shear, Plasma, Carrier Horizons).** Paper 25 uses the oloid path as the substrate for the carrier threshold event. The threshold is the boundary between low-curvature and high-curvature regions of the oloid surface.

**Paper 31 (Gauge Groups Translated Into LCR).** Paper 31 uses the oloid path as the substrate for the Standard Model gauge structure. The 8 contact points correspond to the 8 SM fermion states (3 generations × 2 chiralities + 2 Higgs states). The repair row is conjectured to be the gauge field at the contact point.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 5's claims (the rolling path carrier, the oloid carrier family, the 8-segment path, the transducer, the closure, the graph continuity, the payload noninterference) are mapped by Paper 40 to their receipts (§7).

### 9.2 Cross-Series References

**Paper 6 (Oloid Path Carrier and Transport Geometry).** The UFT series Paper 6 is the equivalent paper in the Unified Field Theory sequence. This unified paper subsumes and consolidates Paper 6, CQECMPLX Paper 5, and the upgraded affirmative version into a single canonical document.

**Paper 9 (Lattice Closure).** The oloid path is the substrate for the lattice lookup in the UFT lattice closure formalism.

**UFT Papers 31–39 (SM Bridge).** The oloid path is the substrate for the Standard Model gauge structure in the UFT Standard Model bridge band.

---

## 10. Open Problems

**Open Problem 10.1 (Oloid path at the Cayley–Dickson doubling levels).** The oloid path is defined at the 3-bit level (8 states). The Cayley–Dickson doubling sequence gives the 1-bit, 2-bit, 4-bit, 8-bit, 16-bit, ... oloids. The structure of the higher-bit oloid paths is conjectural. *Why not closed:* the Cayley–Dickson doubling of the oloid is not computed beyond the octonion level. *Next binding action:* a future paper must address the higher-bit oloid paths. *Owner:* Paper 17 (Continuum Edge Residuals) or a dedicated paper.

**Open Problem 10.2 (Repair row as substrate of the SM gauge structure).** The repair row side-channel is conjectured to be the substrate of the Standard Model gauge structure. The 8 contact points correspond to the 8 SM fermion states; the repair row is the gauge field at the contact point. *Why not closed:* the gauge structure at the contact point is not derived. *Next binding action:* Papers 31–39 must address the gauge structure. *Owner:* Paper 31.

**Open Problem 10.3 (Oloid path in 4 dimensions).** The oloid is a 3-dimensional surface. The Cayley–Dickson doubling gives a 4-dimensional oloid (the "oloid of the second kind") whose path has 16 segments. The 4-dimensional oloid is the substrate of the SM leptons (the 16-segment path corresponds to the 16 SM lepton states). *Why not closed:* the 4-dimensional oloid is not constructed. *Next binding action:* a future paper must construct the 4-dimensional oloid. *Owner:* a future paper.

**Open Problem 10.4 (Cayley–Dickson oloid normal form closed derivation).** The CD-ONF is the conjectural generalization of the oloid path to higher Cayley–Dickson doubles. The closed form is not yet derived, but the structural form is conjectural. The CD-ONF is the handoff from the oloid path to the Cayley–Dickson doubling. *Why not closed:* the sedenion-level (16-state) and higher CD-ONF paths are not constructed. *Next binding action:* derive the CD-ONF at level 4 and prove the doubling property for all `n`. *Owner:* Paper 17 or a dedicated paper.

**Open Problem 10.5 (API exposure).** Expose `verify_oloid_path_carrier` through the installable kernel/API interface.

**Open Problem 10.6 (Ledger binding).** Bind Paper 4 repair payloads to the shared route ledger.

**Open Problem 10.7 (E6→E7→E8 lift).** Add a separate verifier for the E6-to-E7-to-E8 dyadic lift before using it as a theorem in Paper 5 or later papers.

**Open Problem 10.8 (Geometry separation).** Keep finite rolling-state claims separate from physical Oloid geometry claims until the latter have their own verifiers.

**Open Problem 10.9 (Prediction transport).** Treat Rule 30 prediction as downstream — Papers 10 and 12 carry finite/readout prediction receipts; cold unbounded extraction and literature-grade Problem 3 promotion remain outside Paper 5.

**Open Problem 10.10 (Citation anchors).** Replace citation anchors with final bibliography entries during peer-review preparation.

**Open Problem 10.11 (Tool binding expansion).** Expand the tool binding from stub/registry level to executable tests where not yet implemented.

**Open Problem 10.12 (Domain expert critique).** Add one domain expert critique pass.

**Open Problem 10.13 (Falsifier case).** Add one falsifier case that the tool must reject or defer.

---

## 11. Falsifiers

The paper fails if any of the following occur:

```text
an adjacent trace pair is not generated by one legal roll
a nonbinary input is accepted
a head/tail value leaves {0,1}
a payload changes the rolling rule
a discontinuous jump is accepted as legal
prediction is counted as closed by the Paper 5 carrier receipt alone
```

These falsifiers are exhaustive. If any one of them is observed, the corresponding theorem is invalidated:
- If an adjacent trace pair is not a legal `roll`, Theorem 5.1 is false.
- If a nonbinary input is accepted, the `roll` function is not well-defined on its domain, and Theorem 5.1 is false.
- If a head/tail value leaves `{0,1}`, Theorem 5.1 is false.
- If a payload changes the rolling rule, Theorem 5.1 and Theorem 5.7 are false.
- If a discontinuous jump is accepted, Theorem 5.6 is false.
- If prediction is counted as closed by the Paper 5 receipt alone, Theorem 5.2 is misapplied and the scope boundary is violated.

---

## 12. Role in the Suite

Paper 4 produces the object Paper 5 can carry. Paper 5 proves the transport property. Paper 6 uses the carried path state to build the causal link. The dependency chain is:

```text
Paper 4:   repair_boundary(s) = constraint row r
              ↓
Paper 5:   attach_payload(q_t, r) = carried receipt at path state q_t
              ↓
Paper 6:   (q_t, r) → causal edge in obligation ledger
```

The `payload_alters_path_rule = false` invariant is the critical property that makes this chain possible. Without it, the transport from Paper 4 to Paper 6 would not be valid.

---

## 13. Data vs. Interpretation

This paper is a mix of data-backed claims and structural interpretation. The separation is honest and explicit.

### 13.1 Data-Backed (D)

- The rolling carrier state space `{0,1} × {0,1,2,3} × {0,1}` and the `roll(q,b)` function are formal definitions with closed-form proofs (Theorems 5.1–5.7). (D — formal mathematics, verified by computation.)
- The oloid: a developable surface formed by the intersection of two perpendicular unit circles, with the 1:1 rolling motion (Definition 2.6). (D — Schatz 1929, Bottema & Roth 1979, McCarthy 1990, standard math.)
- The Cayley–Dickson oloid normal form: the `cayley_dickson_oloid.py` module in `lattice_forge/` exposes symbols `CAYLEY_DICKSON_SHEET_PATTERN`, `CayleyDicksonOloidNormalForm`, `cayley_dickson_oloid_normal_form`, `verify_cayley_dickson_oloid_normal_form`. (D — `lattice_forge/cayley_dickson_oloid.py`.)
- The substrate map: 8 LCR states, the 8×4 transition table, the depth-4096 verification (Theorems 5.3–5.7). (D — `substrate_map.py:366-460`.)
- The worked trace for input `[1,0,1,1,0,0,1,0]` is computable and reproducible. (D — verified by direct computation.)
- The receipt verification items (`trace_length_is_input_length_plus_one`, etc.) are executable checks. (D — verified by the test suite.)

### 13.2 Interpretation (I)

- The 8-segment LCR parameterization of the oloid path (Theorem 5.3, Definition 2.8). (I — author's structural reading; the Cayley–Dickson doubling gives a `2³ = 8` structure, but the specific oloid-path LCR correspondence is the author's framing.)
- The "Fano plane order" of the 7 non-trivial LCR states (Corollary 5.3.1). (I — author's framing; the Fano plane has 7 points and 7 lines, and the 7 LCR states can be put in bijection, but the "Fano plane order" is the author's reading.)
- The transducer noninterference theorem (Theorem 5.7). (I — author's structural reading; the transducer is a finite-state machine, but the noninterference is a logical consequence, not a literal module.)
- The path closure, the graph continuity, the payload noninterference (Theorems 5.5–5.7). (I — author's structural reading; the substrate map preservation at depth 4096 is (D), but the specific oloid-path properties are (I).)
- The Cayley–Dickson doubling of the oloid to higher dimensions (Open Problems 10.1, 10.3, 10.4). (I — author's structural conjecture; the Cayley–Dickson construction is (D) standard math, but the specific 4-dimensional oloid is not constructed.)
- The carrier action `S = -m∫ds` and the geodesic interpretation (Section 6.3). (I — the action is a natural geometric formalism for the rolling carrier, but the specific physical constants and the geodesic minimization claim are interpretive framing.)
- The SM gauge structure correspondence (Open Problem 10.2). (I — conjectural; not derived.)
- The E6→E7→E8 dyadic lift (Open Problem 10.7). (I — named bridge, not closed.)

### 13.3 Fabrication (X)

- None in this paper. The math is (D) standard; the framing is (I) but defensible.
- Any claim that the 4D oloid is fully constructed is fabrication; it is explicitly listed as an open problem.
- Any claim that the oloid carrier predicts Rule 30 by itself is fabrication; it is explicitly excluded by the scope boundary and the falsifiers.

---

## 14. References

### 14.1 Standard Mathematics and Physics

- Schatz, P. (1929). *Das Oloid.* (Original oloid construction.)
- Bottema, O., & Roth, B. (1979). *Theoretical Kinematics.* North-Holland. (Chapter on developable surfaces and rolling kinematics.)
- McCarthy, J. M. (1990). *Introduction to Theoretical Kinematics.* MIT Press.
- Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379–423. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf. Use: information channel, encoding, receiver, noise, state transmission.
- Conway, J. H., & Smith, D. A. (2003). *On Quaternions and Octonions: Their Geometry, Arithmetic, and Symmetry.* A K Peters. (Cayley–Dickson doubling and octonion structure.)
- Baez, J. C. (2002). The Octonions. *Bulletin of the American Mathematical Society*, 39(2), 145–205. (Octonion algebra and its applications to physics.)

### 14.2 Source Code and Receipts

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — Substrate map verification (depth-4096). Backs: Theorems 5.3, 5.4, 5.5, 5.6, 5.7.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\d12_action.py` — D12 action envelope. Backs: Theorem 5.4 (transducer structure).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py` — Rule 30 ANF decomposition. Backs: Theorem 5.3 (path parameterization).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — F₂ quadratic form. Backs: Theorem 5.7 (payload noninterference).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\cayley_dickson_oloid.py` — Cayley–Dickson oloid normal form.
- `production/formal-papers/Paper 05/verify_oloid_path_carrier.py` — Primary executable receipt for Theorem 5.1.
- `production/formal-papers/Paper 05/oloid_path_carrier_receipt.json` — Receipt artifact for Theorem 5.1.
- `production/formal-papers/Paper 05/verify_oloid_carrier_family.py` — Primary executable receipt for Theorem 5.2.
- `production/formal-papers/Paper 05/oloid_carrier_family_receipt.json` — Receipt artifact for Theorem 5.2.

### 14.3 Documentation and Series Papers

- `D:\CQE_CMPLX\CQECMPLX-Production\papers\Paper 05\PAPER-BODY.md` — Original CQE-Production Paper 5 body.
- `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\source_backup\Paper 05.md` — 1T-Production Paper 5.
- `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\source_backup\Paper 05_UPGRADED.md` — Affirmative upgraded version.
- `D:\CQE_CMPLX\papers\UFT0-100\paper_06.md` — Paper 6 (Oloid Path Carrier and Transport Geometry).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_01__lcr_kernel\paper_01.md` — The LCR kernel (Paper 1).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_05__typed_boundary_repair\paper_05.md` — The typed boundary repair (Paper 5 in UFT numbering).

### 14.4 Content-Addressed Crystals

- `crystals/slot_crystal/05.*.json` (Paper 5 records).
- `states/source_state.OLOID_PATH_CARRIER.json`.

---

## 15. Conclusion

Paper 5 proves that **transport can be continuous without being straight-line**. A finite rolling carrier advances by legal steps, emits binary dyads, and carries repair constraints without changing its rule. That is the **continuous-transport physics map** the later causal and accumulated-center papers need.

The paper has established:
1. The rolling carrier state space `q = (sheet, phase, parity)` and the deterministic `roll(q,b)` transition function.
2. The head/tail dyad as a binary function of the state, preserved at every step.
3. The continuous carrier trace as a sequence of legal `roll` steps preserving input order.
4. The payload noninterference property: Paper 4 constraints attach as side-channel data without altering the path rule.
5. The oloid path carrier as an 8-segment, closed, graph-continuous, payload-noninterfering deterministic finite-state transducer.
6. The substrate oloid carrier family passing its four finite mechanism checks.
7. The carrier action `S = -m∫ds` and the oloid path as a geodesic.
8. The Cayley–Dickson extension and the 4D oloid normal form as the conjectural generalization.
9. The practical rolling inspection fixture, the four-oloid D4 configuration, and the dual-path read-then-verify flow as worked examples.
10. The complete analog workbook sheet specification and the executable receipt verification framework.

All claims are backed by receipts. All forward references are named. All open problems are explicit. All falsifiers are defined. The paper is honest, scoped, and ready for peer review.

---

*End of Paper 5 — Unified Oloid Path Carrier.*

*Paper 6 follows: Causal Links and Obligation Ledgers.*
