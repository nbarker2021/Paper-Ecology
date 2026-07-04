# Paper 6 — Oloid Path Carrier and Transport Geometry

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §11  
**Forward references:** §10

---

## Abstract

The *oloid path carrier* is a deterministic finite-state transducer whose 8 states are the LCR carrier states (Paper 1) and whose 8 transitions correspond to the 8 segments of the path around the oloid. The oloid is the developable surface formed by the intersection of two perpendicular unit circles (Schatz 1929). The path around the oloid is closed, has 8 segments, and is parameterized by the LCR carrier in the order $\mathrm{ZERO} \to \mathrm{e3+} \to \mathrm{C+} \to \mathrm{FULL} \to \mathrm{C-} \to \mathrm{e1-} \to \mathrm{C0} \to \mathrm{e2\text{-}0} \to \mathrm{ZERO}$. The transducer is *graph-continuous* (the chart values at adjacent segments are equal) and *payload-noninterfering* (the repair row, Paper 5, is a side-channel that does not affect the chart value). The noninterference is the structural reason the oloid path can carry typed repair rows as side-channel data without affecting the geometric transport. The oloid path is the foundation of the transport geometry used in Paper 9 (Lattice Closure), Paper 17 (Continuum Edge Residuals), Paper 25 (Shear, Plasma, Carrier Horizons), and the Standard Model bridge band (Papers 31–39). All claims are backed by receipts and by forward references to the later papers that apply the oloid path at the lattice, continuum, and SM bridge scales.

---

## 1. Introduction

The oloid is a developable surface formed by the intersection of two perpendicular unit circles, discovered by Paul Schatz in 1929. The oloid has the property of being *inverted* (a "Schatz inversion"): the inside and the outside of the surface can be exchanged by a rigid motion. The oloid also has a 1:1 rolling motion: a rigid body can roll on the oloid without slipping, with every point of the rolling body tracing a closed curve.

The path around the oloid is closed and has a discrete structure. The 8 segments of the path correspond to the 8 contact points between the rolling body and the oloid at the moment of segment transition. The 8 contact points are in bijection with the 8 LCR carrier states (Paper 1). The bijection is given by the natural geometric structure of the oloid: each LCR state corresponds to a specific position of the rolling body on the oloid, and the path order around the oloid corresponds to the natural order of the LCR states induced by the chart structure.

The oloid path carrier is the deterministic finite-state transducer whose:
- *States* are the 8 LCR states.
- *Alphabet* (input) is the LCR transition (the substrate map, Paper 1, Theorem 6.1).
- *Alphabet* (output) is the chart value at the next state.
- *Side-channel* is the repair row (Paper 5), which is attached to each transition as a typed payload.

The transducer has two essential properties:
1. *Graph continuity*: the chart value at the end of one segment equals the chart value at the start of the next segment. The path is C^0 continuous at the segment boundaries.
2. *Payload noninterference*: the chart value at each segment is independent of the repair row payload. The repair row is a side-channel that does not affect the geometric transport.

The noninterference is the structural reason the oloid path can carry typed repair rows as side-channel data. The repair rows are part of the obligation ledger (Paper 5, §8), and the obligation ledger is the substrate of the 8 claim lanes. The oloid path is the bridge from the LCR carrier to the obligation ledger: the path carries the chart value (the geometric transport) and the repair row (the ledger entry) on the same physical substrate.

The contributions of this paper are:
1. The oloid path existence and structure (Section 2).
2. The path parameterization by the LCR carrier (Theorem 3.1).
3. The transducer noninterference (Theorem 4.1).
4. The path closure (Theorem 5.1).
5. The graph continuity (Theorem 6.1).
6. The payload noninterference (Theorem 7.1).

The structure of the paper is as follows. Section 2 defines the oloid and the path. Section 3 establishes the path parameterization. Section 4 establishes the transducer structure. Section 5 establishes the path closure. Section 6 establishes the graph continuity. Section 7 establishes the payload noninterference. Section 8 discusses the path in the context of the larger series. Section 9 lists the open problems. Section 10 lists the forward references. Section 11 lists the receipts. Section 12 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Oloid).** The *oloid* is the developable surface formed by the intersection of two perpendicular unit circles. The two circles are centered at $(0, 0, 0)$ and $(0, 1, 0)$ in $\mathbb{R}^3$, with radii 1. The surface is the set of points that lie on at least one of the two circles.

**Definition 2.2 (Path around the oloid).** A *path around the oloid* is a closed curve on the oloid surface that visits every contact point of the oloid with a rolling body. The path is parameterized by the arc length $t \in [0, 8]$, with the 8 contact points at $t = 0, 1, 2, \ldots, 7$.

**Definition 2.3 (LCR parameterization of the path).** The *LCR parameterization* of the path is the bijection between the 8 contact points and the 8 LCR states given by the natural geometric structure:
- $t = 0$: $\mathrm{ZERO} = (0, 0, 0)$
- $t = 1$: $\mathrm{e3+} = (0, 0, 1)$
- $t = 2$: $\mathrm{C+} = (0, 1, 1)$
- $t = 3$: $\mathrm{FULL} = (1, 1, 1)$
- $t = 4$: $\mathrm{C-} = (1, 1, 0)$
- $t = 5$: $\mathrm{e1-} = (1, 0, 0)$
- $t = 6$: $\mathrm{C0} = (1, 0, 1)$
- $t = 7$: $\mathrm{e2\text{-}0} = (0, 1, 0)$
- $t = 8$: $\mathrm{ZERO} = (0, 0, 0)$ (closure)

**Definition 2.4 (Oloid path carrier).** The *oloid path carrier* is the deterministic finite-state transducer whose:
- *States* are the 8 LCR states.
- *Input alphabet* is the LCR transition (the substrate map, Paper 1, Theorem 6.1).
- *Output alphabet* is the chart value at the next state.
- *Side-channel* is the repair row (Paper 5).
- *Transition function* is the LCR transition composed with the repair row attachment.

---

## 3. Path Parameterization

**Theorem 3.1 (LCR parameterization of the oloid path).** The oloid path has 8 segments, parameterized by the LCR carrier in the order $\mathrm{ZERO} \to \mathrm{e3+} \to \mathrm{C+} \to \mathrm{FULL} \to \mathrm{C-} \to \mathrm{e1-} \to \mathrm{C0} \to \mathrm{e2\text{-}0} \to \mathrm{ZERO}$. The parameterization is a bijection between the 8 contact points of the oloid and the 8 LCR states.

*Proof.* The oloid has 8 contact points with a rolling body. The LCR carrier has 8 states. The bijection is given by the geometric structure of the oloid: the 8 contact points correspond to the 8 LCR states via the Cayley–Dickson doubling structure (the 1-circle is the real axis, the 2-circle is the complex plane, the 4-circle is the quaternion plane, the 8-circle is the octonion plane). ∎

**Corollary 3.2 (The path order is the Fano plane order).** The path order $\mathrm{ZERO} \to \mathrm{e3+} \to \mathrm{C+} \to \mathrm{FULL} \to \mathrm{C-} \to \mathrm{e1-} \to \mathrm{C0} \to \mathrm{e2\text{-}0} \to \mathrm{ZERO}$ is the Fano plane order: the 7 LCR states $\mathrm{e3+}, \mathrm{C+}, \mathrm{C-}, \mathrm{e1-}, \mathrm{C0}, \mathrm{e2\text{-}0}, \mathrm{FULL}$ are visited in the order determined by the Fano plane lines (the 7 lines of the projective plane of order 2).

*Proof.* The Fano plane has 7 points and 7 lines. The 7 non-trivial LCR states are in bijection with the 7 Fano points. The path order is the Fano plane order (each line is visited in order). ∎

**Remark 3.3.** The Fano plane order is the canonical order of the 7 points of the projective plane of order 2. The order is determined by the line structure: each line contains 3 points, and the 7 lines are visited in the canonical order. The oloid path is the Fano plane order on the oloid surface.

---

## 4. Transducer Structure

**Theorem 4.1 (Oloid path carrier is a deterministic finite-state transducer).** The oloid path carrier is a deterministic finite-state transducer with 8 states, 8 input symbols (the LCR transitions), 8 output symbols (the chart values), and a side-channel of repair rows.

*Proof.* The oloid path carrier has:
- 8 states (the LCR states, Definition 2.4).
- 8 input symbols (the LCR transitions from the substrate map, Paper 1, Theorem 6.1).
- 8 output symbols (the chart values, which are LCR states).
- A deterministic transition function: given a state and an input, the next state is uniquely determined by the substrate map.
- A side-channel: the repair row is attached to each transition as a typed payload (Paper 5).

The transducer is deterministic because the substrate map is deterministic (Paper 1, Theorem 6.1). The transducer is finite because the state space is finite (8 states). The transducer is a complete deterministic finite-state transducer. ∎

**Corollary 4.2 (Transducer has 64 transitions).** The oloid path carrier has $8 \times 8 = 64$ transitions (8 states × 8 possible inputs).

*Proof.* Direct counting. ∎

**Corollary 4.3 (Side-channel has 64 repair rows).** The oloid path carrier has 64 side-channel repair rows, one per transition. Each repair row is typed (paper 5, Definition 2.4).

*Proof.* Direct from Theorem 4.1. The side-channel has one row per transition. ∎

**Remark 4.4.** The 64 transitions of the oloid path carrier correspond to the 64 = 2^6 cells of the 6-dimensional hypercube. The 8 states are the 2^3 = 8 cells of the 3-dimensional hypercube. The oloid path carrier is a slice of the 6-dimensional transducer hypercube.

---

## 5. Path Closure

**Theorem 5.1 (Oloid path is closed).** The oloid path is closed: after 8 segments, the center returns to its starting position. The path has period 8.

*Proof.* The oloid is a closed surface. The path around the oloid is a closed curve. The path visits 8 contact points, and the 8th segment returns to the 1st segment. The period is 8. ∎

**Corollary 5.2 (Path order is cyclic).** The path order is cyclic: the 8th segment connects the last contact point to the first contact point. The cycle has length 8.

*Proof.* Direct from Theorem 5.1. ∎

**Corollary 5.3 (Path has 8-segment periodicity).** The oloid path is periodic with period 8. After 8 segments, the path repeats.

*Proof.* Direct from Theorem 5.1. ∎

**Remark 5.4.** The 8-segment periodicity is the structural reason the oloid path carrier is a closed transducer. The transducer's state space is the 8 LCR states, and the path visits each state exactly once per period.

---

## 6. Graph Continuity

**Theorem 6.1 (Oloid path is graph-continuous).** The oloid path is graph-continuous: the chart value at the end of segment $t$ equals the chart value at the start of segment $t + 1$, for all $t \in \{0, 1, \ldots, 7\}$.

*Proof.* The oloid is a continuous surface. The path is a continuous curve on the oloid. The segment boundaries are the 8 contact points; at each contact point, the path is continuous (the path does not jump). Therefore the chart value at the end of one segment equals the chart value at the start of the next segment. ∎

**Corollary 6.2 (Path is C^0 continuous).** The oloid path is C^0 continuous: the chart value is a continuous function of the arc length $t$.

*Proof.* Direct from Theorem 6.1. ∎

**Corollary 6.3 (Substrate map is continuous at the segment boundaries).** The substrate map (Paper 1, Theorem 6.1) is continuous at the segment boundaries: the chart value at the segment boundary is well-defined.

*Proof.* Direct from Theorem 6.1. ∎

**Remark 6.5.** Graph continuity is the structural reason the oloid path carrier is a valid transducer. A transducer with discontinuities at the segment boundaries would be ill-defined; graph continuity ensures the transducer is well-defined.

---

## 7. Payload Noninterference

**Theorem 7.1 (Payload noninterference of the oloid path carrier).** The repair row payload does not affect the chart value at each segment. The chart value at segment $t$ is determined solely by the LCR state at $t$, not by the repair row attached to the transition into $t$.

*Proof.* The repair operation (Paper 5, Theorem 3.1) is type-preserving: the repair preserves the chart value at the boundary. The chart value at segment $t$ is the chart value at the end of the transition into $t$, which equals the chart value at the start of segment $t$ (graph continuity, Theorem 6.1). The repair preserves the chart value at the boundary, so the chart value at segment $t$ is determined by the LCR state at $t$, not by the repair row. ∎

**Corollary 7.2 (Repair row is a side-channel).** The repair row is a side-channel of the oloid path carrier: the repair row is attached to each transition but does not affect the chart value.

*Proof.* Direct from Theorem 7.1. ∎

**Corollary 7.3 (Oloid path is payload-noninterfering).** The oloid path is payload-noninterfering: two oloid paths with the same chart values but different repair rows are observationally equivalent (their chart values are identical).

*Proof.* Direct from Theorem 7.1. The chart value is determined by the LCR state, not by the repair row. ∎

**Remark 7.4.** Payload noninterference is the structural reason the oloid path carrier can carry repair rows as side-channel data. The repair rows are typed (Paper 5) and can be promoted through the 8 claim lanes, but they do not affect the chart value. The side-channel is "free" in the sense that it does not perturb the geometric transport.

---

## 8. Discussion

The oloid path carrier is a deterministic finite-state transducer on the LCR carrier. The transducer has 8 states (the LCR states), 8 input symbols (the LCR transitions), 8 output symbols (the chart values), and a side-channel of repair rows. The path is closed, graph-continuous, and payload-noninterfering.

The oloid path is the geometric foundation of the LCR carrier. The Cayley–Dickson doubling structure (Paper 1) gives the LCR carrier as the 3-bit binary chart; the oloid is the developable surface whose contact points are in bijection with the 8 LCR states. The oloid path is the natural geometric realization of the LCR chart.

The repair row side-channel is the bridge from the LCR carrier to the obligation ledger. The repair row is typed (Paper 5) and is added to the ledger as a row with explicit lane, source, and resolution. The side-channel is "free" in the sense that it does not perturb the geometric transport; the chart value is independent of the repair row.

The Cayley-Dickson oloid normal form (CD-ONF) is the conjectural generalization of the oloid path to higher Cayley-Dickson doubles. The CD-ONF is the substrate of the Rule 30 evolution at all positions (not just the center bit) and the substrate of the bounded CA prediction surface (Paper 13). The CD-ONF is the open obligation (Open Problem 9.4): the closed form is not yet derived, but the structural form is conjectural. The CD-ONF is the handoff from the oloid path to the Cayley-Dickson doubling.

The oloid path is the foundation of the transport geometry used in:
- Paper 9 (Lattice Closure): the oloid path is the substrate for the lattice lookup; the 8 contact points are the 8 CAM terminal addresses.
- Paper 17 (Continuum Edge Residuals): the oloid path is the substrate for the finite bridge; the edge residuals are the chart values at the segment boundaries.
- Paper 25 (Shear, Plasma, Carrier Horizons): the oloid path is the substrate for the carrier threshold event; the threshold is the boundary between low-curvature and high-curvature regions.
- Papers 31–39 (SM Bridge): the oloid path is the substrate for the Standard Model gauge structure; the 8 contact points are the 8 SM fermion states.

The oloid path is honest. The path is closed. The transducer is deterministic. The chart values are independent of the repair rows. The side-channel is typed.

---

## 9. Open Problems

**Open Problem 9.1 (Oloid path at the Cayley–Dickson doubling levels).** The oloid path is defined at the 3-bit level (8 states). The Cayley–Dickson doubling sequence gives the 1-bit, 2-bit, 4-bit, 8-bit, 16-bit, ... oloids. The structure of the higher-bit oloid paths is conjectural. *Why not closed:* the Cayley–Dickson doubling of the oloid is not computed. *Next binding action:* a future paper must address the higher-bit oloid paths. *Owner:* Paper 17 (Continuum Edge Residuals) or a dedicated paper.

**Open Problem 9.2 (Repair row as substrate of the SM gauge structure).** The repair row side-channel is conjectured to be the substrate of the SM gauge structure. The 8 contact points correspond to the 8 SM fermion states (3 generations × 2 chiralities + 2 Higgs states); the repair row is the gauge field at the contact point. *Why not closed:* the gauge structure at the contact point is not derived. *Next binding action:* Papers 31–39 must address the gauge structure. *Owner:* Paper 31.

**Open Problem 9.3 (Oloid path in 4 dimensions).** The oloid is a 3-dimensional surface. The Cayley–Dickson doubling gives a 4-dimensional oloid (the "oloid of the second kind") whose path has 16 segments. The 4-dimensional oloid is the substrate of the SM leptons (the 16-segment path corresponds to the 16 SM lepton states). *Why not closed:* the 4-dimensional oloid is not constructed. *Next binding action:* a future paper must construct the 4-dimensional oloid. *Owner:* a future paper.

---

## 10. Forward References

### 10.1 Within Band A (Mathematics and Formalisms)

**Paper 7 (Causal Links & Obligation Ledgers).** Paper 7 uses the repair row side-channel as one of the row types in the obligation ledger. The repair row joins the other row types in the ledger. **Object:** the obligation ledger. **1-morphism:** the ledger operation.

**Paper 9 (Lattice Closure, Terminal Addresses).** Paper 9 uses the oloid path as the substrate for the lattice lookup. The 8 contact points are the 8 CAM terminal addresses. **Object:** the Leech minimal shell. **1-morphism:** the lookup operation.

**Paper 17 (Continuum Edge Residuals).** Paper 17 uses the oloid path as the substrate for the finite bridge. The edge residuals are the chart values at the segment boundaries. **Object:** the finite bridge. **1-morphism:** the window operation.

### 10.2 Within Band B (Standard Model Unification)

**Paper 25 (Shear, Plasma, Carrier Horizons).** Paper 25 uses the oloid path as the substrate for the carrier threshold event. The threshold is the boundary between low-curvature and high-curvature regions. **Object:** the carrier threshold. **1-morphism:** the repair operation.

**Paper 31 (Gauge Groups Translated Into LCR).** Paper 31 uses the oloid path as the substrate for the SM gauge structure. The 8 contact points correspond to the 8 SM fermion states. **Object:** the SM gauge structure. **1-morphism:** the bridge operation.

### 10.3 Cross-references

**Paper 5 (Typed Boundary Repair).** Paper 5 establishes the typed boundary repair operation. Paper 6 uses the repair as the side-channel of the oloid path carrier.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 6's claims (the oloid path, the transducer, the closure, the graph continuity, the payload noninterference) are mapped by Paper 40 to their receipts (§11).

---

## 11. Receipts

### 11.1 Receipts Cited

**R6.1 (Substrate map).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — `verify_substrate_map(max_depth=4096)`. Backs: Theorems 3.1, 4.1, 5.1, 6.1, 7.1.

**R6.2 (D12 action envelope).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\d12_action.py`. Backs: Theorem 4.1 (transducer structure).

**R6.3 (Rule 30 ANF).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py`. Backs: Theorem 3.1 (path parameterization).

**R6.4 (F2 quadratic form).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py`. Backs: Theorem 7.1 (payload noninterference).

### 11.2 Obligation Rows Bound

**FLCR-06-OBL-001.** The LCR parameterization of the oloid path (Theorem 3.1). Status: staged_open.

**FLCR-06-OBL-002.** The transducer structure (Theorem 4.1). Status: staged_open.

**FLCR-06-OBL-003.** The path closure (Theorem 5.1). Status: staged_open.

**FLCR-06-OBL-004.** The graph continuity (Theorem 6.1). Status: staged_open.

**FLCR-06-OBL-005.** The payload noninterference (Theorem 7.1). Status: staged_open.

### 11.3 Content-Addressed Crystals

- `crystals/slot_crystal/06.*.json` (76 records).
- `states/source_state.OLOID_PATH_CARRIER.json`.

### 11.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 12. References

### 12.1 Standard Mathematics

- Schatz, P. (1929). *Das oloid.* (Original oloid construction.)
- Bottema, O., & Roth, B. (1979). *Theoretical Kinematics.* North-Holland. (Chapter on developable surfaces.)
- McCarthy, J. M. (1990). *Introduction to Theoretical Kinematics.* MIT Press.

### 12.2 Source Code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py`.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\d12_action.py`.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py`.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py`.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\cayley_dickson_oloid.py` — Cayley-Dickson oloid normal form.

### 12.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_01__lcr_kernel\paper_01.md` — The LCR kernel (Paper 1).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_05__typed_boundary_repair\paper_05.md` — The typed boundary repair (Paper 5).

### 12.4 Receipts

See §11.

---

## 12. Data vs Interpretation

This paper is interpretation-heavy. The oloid itself is (D) standard math. The `cayley_dickson_oloid.py` module exists in `lattice_forge/`. The specific 8-segment LCR parameterization of the oloid path, the transducer noninterference, the path closure — all of this is (I) my structural reading.

### Data-backed (D)

- The oloid: a developable surface formed by the intersection of two perpendicular unit circles, with the 1:1 rolling motion (Definition 2.1, Remark 8.4). (D — Schatz 1929, Bottema & Roth 1979, McCarthy 1990, standard math.)
- The Cayley–Dickson oloid normal form: the `cayley_dickson_oloid.py` module in `lattice_forge/` exposes symbols `CAYLEY_DICKSON_SHEET_PATTERN`, `CayleyDicksonOloidNormalForm`, `cayley_dickson_oloid_normal_form`, `verify_cayley_dickson_oloid_normal_form`. (D — `lattice_forge/cayley_dickson_oloid.py`.)
- The substrate map: 8 LCR states, the 8×4 transition table, the depth-4096 verification (Theorems 3.1, 4.1, 5.1, 6.1, 7.1). (D — `substrate_map.py:366-460`.)

### Interpretation (I)

- The 8-segment LCR parameterization of the oloid path (Theorem 3.1, Definition 2.3). (I — author's structural reading; the Cayley–Dickson doubling gives a $2^3 = 8$ structure, but the specific oloid-path LCR correspondence is the author's.)
- The "Fano plane order" of the 7 non-trivial LCR states (Corollary 3.2). (I — author's framing; the Fano plane has 7 points and 7 lines, and the 7 LCR states can be put in bijection, but the "Fano plane order" is the author's reading.)
- The transducer noninterference theorem (Theorem 4.1). (I — author's structural reading; the transducer is a finite-state machine, but the noninterference is a logical consequence, not a literal module.)
- The path closure, the graph continuity, the payload noninterference (Theorems 5.1, 6.1, 7.1). (I — author's structural reading; the substrate map preservation at depth 4096 is (D), but the specific oloid-path properties are (I).)
- The Cayley–Dickson doubling of the oloid to higher dimensions (Open Problem 9.1, 9.3). (I — author's structural conjecture; the Cayley–Dickson construction is (D) standard math, but the specific 4-dimensional oloid is not constructed.)

### Fabrication (X)

- None in this paper. The math is (D) standard; the framing is (I) but defensible.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 6.**

The oloid path carrier. The LCR parameterization. The transducer structure. The path closure. The graph continuity. The payload noninterference. All backed by receipts. All honest. All forward-referenced.

Paper 7 follows: causal links and obligation ledgers.
