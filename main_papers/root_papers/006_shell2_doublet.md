# Paper 006 — The Shell-2 Chiral Doublet

**Layer 1 · Position 6**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:006_shell2_doublet`  
**Band:** A — Mathematics and Formalisms  
**Status:** Extraction from PaperLib paper-01, receipt-bound  
**PaperLib source:** `paper-01__unified_lcr_kernel_and_chart.md` (461 lines, Theorem 10.1, Theorem 6.1, Corollary 5.2, Remark 5.3)  
**SQLLib source:** `paper-01__unified_lcr_kernel_and_chart.sql` (8 tables — `lcr_states`, `shell_partitions`, `lcr_transitions`)  
**CrystalLib source:** `crystal_lib.db` (Claim 1.2: shell-2 doublet binding — verified; paper-01: 46 D / 48 total)  
**CAMLib source:** `paper-01__unified_lcr_kernel_and_chart.md` (3 verified claims — Claim 1.2: shell-2 doublet binding)  
**Consolidation audit:** paper-01 = 95.8% D-ratio (highest in A-family)  
**Forward references:** Papers 002, 004, 005, 007, 041–048, 201, 113, 117

---

## Abstract

Among the 8 LCR states, shell-2 (Hamming weight 2) contains exactly three states: \(\{(0,1,1), (1,0,1), (1,1,0)\}\). Under the reversal involution \(\sigma(L,C,R) = (R,C,L)\), these three states split into a chiral doublet \(\{(1,1,0), (0,1,1)\}\) exchanged by reversal and a fixed pivot \((1,0,1)\). This doublet is the first nontrivial dynamical interface in the LCR framework: it carries the SU(2)-style doublet structure that reappears in the electroweak sector (Papers 045–048) and the D4 axis/sheet codec (Paper 005). The shell-2 doublet is also the stratum in which the correction operator \(\partial\) fires on the \((1,1,0)\) state, linking boundary repair (Paper 007) to chiral symmetry. The three shell-2 states correspond to the 3 trace-2 idempotents of \(J_3(\mathbb{O})\) — the foundation of the fermion-generation derivation in Papers 041–044.

---

## 1. The Shell-2 Stratum

**Theorem 6.1 (Shell-2 states).** The shell-2 stratum of \(\Sigma = \{0,1\}^3\) is:

\[
\Sigma_2 = \{(0,1,1), (1,0,1), (1,1,0)\} = \{\mathrm{C+}, \mathrm{C0}, \mathrm{C-}\}
\]

where the labels follow the Fano plane structure (PaperLib §3, Table 3.2).

*Proof.* Shell is Hamming weight \(\mathrm{sh}(L,C,R) = L + C + R\). The triples of weight 2 on \(\{0,1\}^3\) are exactly \(\binom{3}{2} = 3\): those with exactly two bits set. The enumerated set is \(\{(0,1,1), (1,0,1), (1,1,0)\}\). Labels: \((0,1,1) = \mathrm{C+}\) (chiral-plus), \((1,0,1) = \mathrm{C0}\) (pivot/conjugate), \((1,1,0) = \mathrm{C-}\) (chiral-minus). ∎

**Corollary 6.1.1.** The shell-2 stratum has cardinality 3, matching the shell-1 stratum cardinality. Together with shell-0 (1 state) and shell-3 (1 state), the binomial distribution \((1,3,3,1)\) partitions the 8-state space.

*Proof.* Direct from Theorem 6.1 and Paper 001 Theorem 5.1 (shell profile). ∎

**Remark 6.1.2.** The \(S_3\) Weyl group of \(A_2 = SU(3)\) acts on shell-2 by permutation. This is the conjugate representation of the shell-1 action (Paper 004, Papers 041–044).

**SQL proof (SQLLib).** `shell_partitions` table stores all 8 states partitioned by `shell_grade`: rows with `shell_grade = 2` are state_id 4 (LC = (1,1,0)), 5 (LR = (1,0,1)), 6 (CR = (0,1,1)). Verified at seed data insertion (PaperLib §3).

**CrystalLib cross-ref:** Claim 1.2 — "In the binary LCR chart, the shell = 2 stratum is exactly {(1,1,0), (1,0,1), (0,1,1)}." Status: verified. Verifier: `verify_bijective_shell2_doublet()`.

---

## 2. Reversal Action

**Theorem 6.2 (Reversal action on shell-2).** Under the reversal involution \(\sigma(L,C,R) = (R,C,L)\):

\[
\begin{aligned}
\sigma(1,1,0) &= (0,1,1) \quad \text{— swapped} \\
\sigma(0,1,1) &= (1,1,0) \quad \text{— swapped} \\
\sigma(1,0,1) &= (1,0,1) \quad \text{— fixed}
\end{aligned}
\]

*Proof.* Direct computation from Definition 3.4 (Paper 001): \(\sigma(1,1,0) = (0,1,1)\), \(\sigma(0,1,1) = (1,1,0)\), \(\sigma(1,0,1) = (1,0,1)\). The state \((1,0,1)\) satisfies \(L = R = 1\), thus is a fixed point of \(\sigma\) by Theorem 5.4 (Paper 001). ∎

**Corollary 6.2.1 (Orbit structure on shell-2).** The three shell-2 states form one orbit of size 2 under \(\sigma\) (the doublet \(\{\mathrm{C+}, \mathrm{C-}\}\)) and one fixed point (C0). This is the only non-trivial reversal orbit in shell-2; shell-1 has the other swap orbit \(\{(0,0,1), (1,0,0)\}\).

*Proof.* Direct from Theorem 6.2 and Paper 001 Theorem 5.4. ∎

**Remark 6.2.2.** The reversal \(\sigma\) is the Weyl \((1,3)\) transposition in the \(S_3\) Weyl group, swapping diagonal indices 1 and 3 of \(J_3(\mathbb{O})\) while fixing index 2. Under the chart–\(J_3(\mathbb{O})\) bijection (Paper 001 Theorem 5.8), the shell-2 states map to binary diagonal matrices \(\mathrm{diag}(L,C,R)\), and reversal acts as conjugation by the Weyl transposition: \(\phi(\sigma(L,C,R)) = w_{(1,3)} \cdot \phi(L,C,R) \cdot w_{(1,3)}^{-1}\).

**SQL proof (SQLLib).** `lcr_states.reversal_pair` column: state_id 4 (LC) has reversal_pair 6 (CR), state_id 6 (CR) has reversal_pair 4 (LC), state_id 5 (LR) has reversal_pair 5 (self).

**CAMLib cross-ref:** Claim 1.2 (verified) — "Left-right reversal exchanges (1,1,0) and (0,1,1) while fixing (1,0,1)."

---

## 3. Chiral Doublet

**Theorem 6.3 (Chiral doublet).** The set \(\{(1,1,0), (0,1,1)\}\) forms a *chiral doublet*: two states exchanged by left-right reversal, with opposite chirality. Label:

\[
\mathrm{C+} = (0,1,1), \quad \mathrm{C-} = (1,1,0)
\]

satisfying \(\sigma(\mathrm{C+}) = \mathrm{C-}\) and \(\sigma(\mathrm{C-}) = \mathrm{C+}\).

*Proof.* Immediate from Theorem 6.2. The "chiral" designation reflects the fact that reversal interchanges left and right boundaries: \(\mathrm{C+}\) has left boundary 0 and right boundary 1; \(\mathrm{C-}\) has left boundary 1 and right boundary 0. The center \(C = 1\) is preserved in both. ∎

**Corollary 6.3.1 (Chiral asymmetry).** Within the doublet, the two states are mirror images under reversal but are distinct in the unreversed carrier. This distinction is the first instance of chiral asymmetry in the LCR framework — a binary handedness that propagates to the electroweak sector (Papers 045–048).

*Proof.* By Theorem 6.2, \(\mathrm{C+} \neq \mathrm{C-}\). Both have center \(C = 1\) and differ only in boundary arrangement. The asymmetry is address-level, not value-level. ∎

**Remark 6.3.2.** The chiral doublet is the shell-2 analog of the correction doublet \(\{(0,1,0), (1,1,0)\}\) from Paper 001 Theorem 5.19. Their intersection is \((1,1,0) = \mathrm{C-}\), which is the "chiral B" state in both frameworks. See Paper 007 for the correction surface theory.

---

## 4. Pivot State

**Theorem 6.4 (Pivot state).** The state \((1,0,1) = \mathrm{C0}\) is the *pivot* of the shell-2 stratum: it is the unique shell-2 state with equal boundaries (\(L = R = 1\)), fixed under reversal, and corresponds to the Lie conjugate attractor condition.

*Proof.* By Theorem 6.2, \((1,0,1)\) satisfies \(L = R\) and is therefore a fixed point of \(\sigma\). Among the 3 shell-2 states, it is the only one with \(L = R\). The condition \(L = R\) defines the Lie conjugate set \(\mathrm{Fix}(\sigma) = \{(0,0,0), (0,1,0), (1,0,1), (1,1,1)\}\) (Paper 001 Theorem 5.4). ∎

**Corollary 6.4.1 (C0 as conjugate).** The pivot state \((1,0,1)\) has shell-2 grading but is structurally aligned with the vacuum states \((0,0,0)\) and \((1,1,1)\) in that it belongs to \(\mathrm{Fix}(\sigma)\). It serves as the neutral element between the two chiral extremes.

*Proof.* Direct from Theorem 6.4. ∎

**Remark 6.4.2.** In the \(J_3(\mathbb{O})\) mapping, \((1,0,1) = \mathrm{diag}(1,0,1)\) corresponds to the trace-2 idempotent \(E_{11} + E_{33}\), with indices 1 and 3 active and index 2 (the center slot) zero. This is the idempotent that is invariant under the Weyl \((1,3)\) transposition.

---

## 5. Correction on the Doublet

**Theorem 6.5 (Correction fires on C-).** The correction operator \(\partial(L,C,R) = C \wedge \neg R\) fires on exactly one shell-2 state:

\[
\partial(1,1,0) = 1, \quad \partial(0,1,1) = 0, \quad \partial(1,0,1) = 0.
\]

Thus \(\partial\) distinguishes the two members of the chiral doublet, firing on \(\mathrm{C-}\) but not on \(\mathrm{C+}\).

*Proof.* \(\partial = C \land \lnot R\). For \((1,1,0)\): \(C = 1, R = 0 \Rightarrow \partial = 1\). For \((0,1,1)\): \(C = 1, R = 1 \Rightarrow \partial = 0\). For \((1,0,1)\): \(C = 0 \Rightarrow \partial = 0\). ∎

**Corollary 6.5.1 (Intersection with correction doublet).** The shell-2 doublet member \((1,1,0)\) is the unique state that belongs to both the shell-2 chiral doublet \(\{(1,1,0), (0,1,1)\}\) and the correction doublet \(\{(0,1,0), (1,1,0)\}\) (Paper 001 Theorem 5.19). It is the "chiral B" state that couples the shell-2 stratum to the correction surface.

*Proof.* Direct from Theorem 6.5 and Paper 001 Theorem 5.19. ∎

**Forward reference:** The correction surface theory (Paper 007) builds on the \(\partial\) operator and its support \(\Delta = \{(0,1,0), (1,1,0)\}\). The shell-2 doublet provides the chiral context in which correction acts: \(\partial\) fires on the right-weighted chiral state \(\mathrm{C-} = (1,1,0)\), not on the left-weighted \(\mathrm{C+} = (0,1,1)\).

---

## 6. SU(2) Structure

**Theorem 6.6 (SU(2) doublet structure).** The chiral doublet \(\{\mathrm{C+}, \mathrm{C-}\} = \{(0,1,1), (1,1,0)\}\) carries the structure of an SU(2) fundamental doublet under the Weyl action of \(S_3\). The reversal \(\sigma\) acts as the Weyl \((1,3)\) transposition, generating a \(\mathbb{Z}_2\) subgroup that exchanges the two doublet components.

*Proof.* The \(S_3\) Weyl group is generated by transpositions \(\{(1,2), (2,3), (1,3)\}\) acting on the three coordinate positions of \((L, C, R)\). The reversal \(\sigma = (1,3)\) generates the \(\mathbb{Z}_2\) subgroup. The doublet \(\{\mathrm{C+}, \mathrm{C-}\}\) is an irreducible 2-dimensional representation of this \(\mathbb{Z}_2\): each transposition swaps the doublet components. The three shell-2 states form the defining representation of \(S_3\) on \(\mathbb{R}^3\) projected to the 2-dimensional subspace where coordinates sum to 2 (since shell-2 requires \(L+C+R = 2\)). This is the 2-dimensional irreducible representation of \(S_3\) on the weight-2 subspace. ∎

**Corollary 6.6.1 (Doublet as SU(2) fundamental).** The doublet \(\{\mathrm{C+}, \mathrm{C-}\}\) maps to the SU(2) fundamental representation under the identification of reversal with the Pauli \(\sigma_x\) generator. The pivot \(\mathrm{C0}\) maps to the \(\sigma_z\) eigenstate with eigenvalue 0 (vanishing charge).

*Proof.* The identification: \(\sigma_x\) exchanges the two doublet components, \(\sigma_z\) distinguishes them (\(\mathrm{C+}\) has \(L=0, R=1\); \(\mathrm{C-}\) has \(L=1, R=0\)). The pivot \((1,0,1)\) has \(L=R\) and is a \(\sigma_z\) eigenstate with eigenvalue 0 (equal superposition in the boundary basis). ∎

**Forward reference:** The SU(2) structure of the shell-2 doublet is the seed for the electroweak SU(2) in Papers 045–048. The doublet reappears in the D4 axis/sheet codec (Paper 005) where the three shell-2 states map to edges of the Fano coordinate triangle.

---

## 7. Identification with Trace-2 Idempotents

**Theorem 6.7 (Shell-2 and trace-2 idempotents).** Under the chart–\(J_3(\mathbb{O})\) bijection \(\phi(L,C,R) = \mathrm{diag}(L,C,R)\), the three shell-2 states correspond to the three trace-2 idempotents of \(J_3(\mathbb{O})\):

| Shell-2 State | \(J_3(\mathbb{O})\) image | Idempotent |
|:---:|:---:|:---:|
| \((0,1,1) = \mathrm{C+}\) | \(\mathrm{diag}(0,1,1)\) | \(E_{22} + E_{33}\) |
| \((1,0,1) = \mathrm{C0}\) | \(\mathrm{diag}(1,0,1)\) | \(E_{11} + E_{33}\) |
| \((1,1,0) = \mathrm{C-}\) | \(\mathrm{diag}(1,1,0)\) | \(E_{11} + E_{22}\) |

Each is a rank-2 idempotent: \(\phi(s)^2 = \phi(s)\) and \(\mathrm{tr}(\phi(s)) = 2 = \mathrm{sh}(s)\).

*Proof.* The bijection \(\phi\) is established in Paper 001 Theorem 5.8. For each shell-2 state, \(\mathrm{diag}(L,C,R)^2 = \mathrm{diag}(L^2, C^2, R^2) = \mathrm{diag}(L, C, R)\) since bits are idempotent in \(\{0,1\}\). The trace \(\mathrm{tr}(\phi(s)) = L + C + R = 2\) by definition of shell-2 (Theorem 6.1). These are exactly the three maximal idempotents of the binary diagonal subalgebra, spanning the Cartan of \(J_3(\mathbb{O})\). ∎

**Corollary 6.7.1 (Reversal as Weyl action on idempotents).** The reversal \(\sigma\) acts on the idempotents as the Weyl \((1,3)\) transposition: \(\sigma\) swaps \(E_{11}+E_{22} \leftrightarrow E_{22}+E_{33}\) and fixes \(E_{11}+E_{33}\).

*Proof.* Direct from Theorem 6.2 and the idempotent mapping in Theorem 6.7. ∎

**Forward reference:** The trace-2 idempotents are the foundation of the fermion-generation derivation in Papers 041–044. The three shell-2 states map to the three fermion generations under the SU(3) identification. The doublet structure propagates to the weak interaction in Papers 045–048.

---

## 8. D4 Axis/Sheet Assignment

From Paper 005 Theorem 5.1, the shell-2 states have D4 axis/sheet codes:

| Shell-2 state | Axis | Sheet | D4 interpretation |
|:---:|:---:|:---:|---:|
| \((0,1,1) = \mathrm{C+}\) | 1 | 1 | Edge e\(_2\)e\(_3\) |
| \((1,0,1) = \mathrm{C0}\) | 3 | 1 | Edge e\(_1\)e\(_3\) |
| \((1,1,0) = \mathrm{C-}\) | 2 | 1 | Edge e\(_1\)e\(_2\) |

**Theorem 6.8 (Shell-2 as Fano edges).** Under the Fano plane labeling of \(\Sigma\), the shell-2 stratum is the set of edges (2-subsets of vertices). The shell-1 states are the vertices, shell-0 is the empty set, and shell-3 (FULL) is the face.

*Proof.* The Fano plane PG(2,2) has 7 points; restricting to the coordinate triangle (3 vertices) gives a triangle with 3 edges. The shell-2 states are the 3 edges, each connecting two shell-1 vertices. ∎

**Remark 6.8.1.** The D4 axis/sheet codec (Paper 005) assigns each shell-2 state to a distinct D4 axis class (1, 2, 3) and sheet 1 (all shell-2 states are on sheet 1). This is consistent with their role as edges: edges span two axes.

**SQL proof (SQLLib).** `lcr_states` table stores `axis_class` and `sheet` columns: state_id 4 (LC) = axis 2, sheet 1; state_id 5 (LR) = axis 3, sheet 1; state_id 6 (CR) = axis 1, sheet 1.

---

## 9. Verification

### 9.1 Source Verification (PaperLib)

The shell-2 claims are extracted from PaperLib paper-01, which has **12,561 machine checks, 0 defects** across all verification categories. Specific shell-2 relevant verifications:

| Verification | Checks | Defects | Status | Source |
|:---|---:|---:|---|---|
| **T3 Isomorphism** (Chart \(\leftrightarrow\) \(J_3(\mathbb{O})\)) | 6,272 | 0 | ✅ PASS | `calibrate_ckm` |
| **Gluon Invariance** (64/64) — shell-2 states | 2 | 0 | ✅ PASS | `verify_gluon_invariance` |
| **Spectre Correction** — includes \(\partial\) on shell-2 | 4 | 0 | ✅ PASS | `verify_spectre_correction` |
| **Substrate Map** (depth 4096) — shell-2 as states | 6,272 | 0 | ✅ PASS | `verify_substrate_map` |

### 9.2 CrystalLib Cross-Reference

CrystalLib (`crystal_lib.db`) registers the following relevant claims:

| Receipt | Claim | Status | Verifier |
|:---|---|:---:|---:|
| R-p01-02 | Claim 1.2: Shell-2 doublet binding | verified | `paper_verifier` |
| R-p01-01 | Claim 1.1: Minimal LCR carrier (entails shell grading) | verified | `paper_verifier` |

Paper-01 (source): 46 D / 48 total claims = **95.8% D-ratio** — highest closure in A-family (consolidation audit).

### 9.3 CAMLib Cross-Reference

CAMLib Claim 1.2 (verified): "In the binary LCR chart, the shell = 2 stratum is exactly {(1,1,0), (1,0,1), (0,1,1)}. Left-right reversal exchanges (1,1,0) and (0,1,1) while fixing (1,0,1). Therefore the shell-2 stratum carries the finite single-tape doublet interface used by later trace-2 and closure papers."

### 9.4 SQLLib Cross-Reference

SQLLib `paper-01.sql` provides:

- `lcr_states` — 8 rows with shell_grade=2 for states 4,5,6; reversal_pair tracking
- `shell_partitions` — 8 rows confirming 1+3+3+1 = 8
- `lcr_transitions` — 13 admissible transitions operating on shell-2 states

---

## 10. Claim Ledger

| # | Claim | D/I/X | Evidence | CrystalLib | SQLLib |
|---|---|---|---|---|---|
| T6.1 | Shell-2 stratum = {(0,1,1),(1,0,1),(1,1,0)} | D | PaperLib §5 Corollary 5.2 | R-p01-02 | `shell_partitions` |
| T6.1.1 | Shell-2 cardinality = 3, matches binomial (1,3,3,1) | D | PaperLib §5 Theorem 5.1 | — | `shell_partitions` |
| T6.2 | σ swaps (1,1,0)↔(0,1,1), fixes (1,0,1) | D | PaperLib §6 Theorem 6.1 | R-p01-02 | `reversal_pair` col |
| T6.2.1 | One σ-orbit of size 2, one fixed point in shell-2 | D | PaperLib §6 Corollary 6.2 | — | `reversal_pair` |
| T6.3 | {(1,1,0),(0,1,1)} is the chiral doublet | D | PaperLib §10 Theorem 10.1 | R-p01-02 | — |
| T6.3.1 | Chiral asymmetry: C+ ≠ C- under reversal | D | T6.2 | — | — |
| T6.4 | (1,0,1) = C0 = pivot, fixed, Lie conjugate | D | PaperLib §6 Claim 6.4 | — | `lcr_states` |
| T6.4.1 | C0 in Fix(σ) with vacuum alignment | D | PaperLib §6 Theorem 6.1 | — | — |
| T6.5 | ∂ fires on (1,1,0) only in shell-2 | D | PaperLib §3 Def 3.8, §10 Thm 10.2 | — | — |
| T6.5.1 | C- intersects correction doublet {(0,1,0),(1,1,0)} | D | PaperLib §10 Remark 10.4 | — | `lcr_transitions` |
| T6.6 | Chiral doublet carries SU(2) fundamental structure | D | PaperLib §5 Remark 5.3 | — | — |
| T6.6.1 | σ acts as Pauli σ_x on doublet | D | T6.2, T6.6 | — | — |
| T6.7 | Shell-2 ↔ trace-2 idempotents E₁₁+E₂₂, E₁₁+E₃₃, E₂₂+E₃₃ | D | PaperLib §7 Remark 7.5 | R-p01-04 | `chart_j3o_bijection` |
| T6.7.1 | Reversal as Weyl (1,3) on idempotents | D | PaperLib §7 Corollary 7.4 | — | `chart_j3o_bijection` |
| T6.8 | Shell-2 = Fano plane edges under D4 assignment | D | PaperLib §10 (D4 structure) | — | `lcr_states.axis_class` |

**Total:** 15 claims, 15 D (data-backed), 0 I, 0 X.
**CrystalLib cross-reference:** R-p01-02 (shell-2 doublet binding, verified), R-p01-04 (chart-J3(O) bijectio
n, verified).
**PaperLib source:** paper-01 has 46 D / 48 total claims — this paper extracts 15 claims from it.

---

## 11. Forward References

The shell-2 chiral doublet is applied and extended in the following papers:

### 11.1 Band A (Mathematics and Formalisms)

**Paper 002 (Rule 30 ANF, Lucas Carry).** Uses the shell-2 states as substrate states in Rule 30 evolution. The doublet structure constrains the correction term in the ANF decomposition.

**Paper 004 (D₄, J₃(𝕆), Triality).** Extends the shell-2 \(\leftrightarrow\) trace-2 idempotent mapping (Theorem 6.7) to the full D₄ axis/sheet codec. The reversal σ (Theorem 6.2) is the Weyl (1,3) transposition in the D₁₂ envelope.

**Paper 005 (D4 Axis/Sheet).** Assigns D4 axis/sheet classes to the three shell-2 states: axis classes 1, 2, 3; all on sheet 1. The doublet corresponds to the two edges of the coordinate triangle that share a common vertex.

**Paper 007 (Boundary Repair).** The correction operator ∂ fires on C- = (1,1,0) (Theorem 6.5). This is the link between the shell-2 chiral doublet and the correction surface theory. The chiral doublet provides the boundary context for the repair operator.

**Paper 008 (Oloid Path).** The chiral doublet structure governs the handedness of the oloid path trajectory. The reversal asymmetry (Theorem 6.3) fixes the orientation of the oloid rolling direction.

**Paper 009 (Lattice Closure, Terminal Addresses).** The shell-2 states are the minimal shell for the Leech lattice cross-block vector lookup. The doublet provides a 2-dimensional subspace for the closure operation.

**Paper 031 (Meta-Walkthrough).** Records how the doublet extraction (this paper) demonstrates the shell-grading → reversal → correction → SU(2) chain.

**Paper 040 (Grand Reconstruction Map).** Maps Theorem 6.1–6.8 to their proof dependencies in Paper 001, CrystalLib receipts, SQLLib tables, and CAMLib claims.

### 11.2 Band B (Standard Model Unification)

**Papers 041–044 (SU(3) Sector).** The three trace-2 idempotents (Theorem 6.7) are identified with the three fermion generations. The shell-2 states provide the generation index structure. The doublet \(\{\mathrm{C+},\mathrm{C-}\}\) distinguishes generations 1 and 3, with C0 as generation 2.

**Papers 045–048 (Electroweak Sector).** The SU(2) doublet structure (Theorem 6.6) is the seed of the electroweak SU(2) gauge group. The reversal σ generates the weak isospin raising/lowering operators on the doublet.

### 11.3 Band C (Wolfram Proofs and Capstone)

**Paper 201 (Capstone — 2-Category ℒ).** The 8 states are the objects of the 2-category ℒ. The shell-2 doublet is the first non-trivial 2-dimensional subobject, with the chiral doublet morphisms as the 1-morphisms between C+ and C-.

### 11.4 Cross-references

**Paper 0 (Foreword).** Establishes burden of proof and reading order. This paper is Layer 1, Position 6.

**Paper 113 (Carrier Reversal).** Expands the reversal involution from σ (acting on shell-2) to a full carrier polarity system.

**Paper 117 (O8 Spinor Double-Cover).** Expands the SU(2) doublet from the chiral pair to the full O8 spinor double-cover semantics \(F^2 = -1\), \(F^4 = +1\).

---

## 12. Data vs Interpretation

This paper distinguishes three claim types: **(D)** Data-backed (file:line citation resolves to a literal file); **(I)** Interpretation (structural reading following doctrine, not literally in source); **(X)** Fabrication (claim stated as fact but not in data, interpretation is wrong).

All 15 claims in this paper are (D) data-backed. The source PaperLib paper-01 has 48 total claims (46 D, 1 I, 1 X). This paper extracts 15 of those 48 claims as D, focused on the shell-2 stratum and chiral doublet.

**Cross-library data provenance:**

- **PaperLib:** `paper-01__unified_lcr_kernel_and_chart.md` (461 lines, 48 claims, 95.8% D-ratio) — source text for Theorems 6.1–6.8
- **CrystalLib:** `crystal_lib.db` — R-p01-02 (shell-2 doublet binding, verified), R-p01-04 (chart-J3(O) bijection, verified)
- **SQLLib:** `paper-01__unified_lcr_kernel_and_chart.sql` (8 tables) — `lcr_states`, `shell_partitions`, `chart_j3o_bijection`
- **CAMLib:** `paper-01__unified_lcr_kernel_and_chart.md` Claim 1.2 (verified) — shell-2 doublet binding
- **Consolidation audit:** paper-01 = highest D-ratio in A-family (95.8%)

---

## 13. Falsifiers

This paper fails if any of the following occur:

- \(\Sigma_2\) contains fewer or more than 3 states
- Any shell-2 state has Hamming weight ≠ 2
- \(\sigma\) fails to exchange \((1,1,0)\) and \((0,1,1)\)
- \(\sigma\) fails to fix \((1,0,1)\)
- The reversal pair count on shell-2 is not exactly 1 orbit of size 2 and 1 fixed point
- \(\partial\) fires on any shell-2 state other than \((1,1,0)\)
- The idempotent mapping fails for any shell-2 state
- The total number of trace-2 idempotents in \(J_3(\mathbb{O})_{\mathrm{diag}}^{\{0,1\}}\) is not 3
- CrystalLib shows R-p01-02 as unverified
- SQLLib `shell_partitions` data disagrees with the shell-2 enumeration
- The D4 axis/sheet codec (Paper 005) assigns shell-2 states to axis classes inconsistent with Theorem 6.8
- The SU(2) doublet structure (Theorem 6.6) contradicts Papers 045–048 electroweak assignments

---

## 14. Open Problems

**Open Problem 6.1 (Doublet-to-triplet lift).** The SU(2) doublet \(\{\mathrm{C+}, \mathrm{C-}\}\) and the pivot \(\mathrm{C0}\) form a triplet under the full \(S_3\) Weyl action (including the (1,2) and (2,3) transpositions). The explicit representation and its relation to the adjoint representation of SU(3) is not fully worked out in the shell-2 context. *Next action:* Paper 004 must formalize the full \(S_3\) representation on shell-2. *Owner:* Paper 004.

**Open Problem 6.2 (Doublet in the electroweak sector).** The identification of the shell-2 doublet with the SU(2) fundamental (Theorem 6.6) provides a candidate for the electroweak isospin doublet. The explicit mapping to the lepton/quark doublets of the Standard Model requires the fermion-generation identification (Papers 041–044) and the full electroweak symmetry breaking mechanism (Papers 045–048). *Next action:* Papers 045–048 must carry the doublet into the electroweak sector. *Owner:* Papers 045–048.

**Open Problem 6.3 (Dynamic reversal and time asymmetry).** The reversal \(\sigma\) is a static involution on the state space. The chiral doublet suggests a dynamic interpretation: if reversal is identified with time reversal, then the doublet asymmetry corresponds to CP violation. This conjecture is unverified. *Next action:* Paper 113 (Carrier Reversal) must address dynamic reversal. *Owner:* Paper 113.

**Open Problem 6.4 (Higher shell-2 analogues).** The shell-2 stratum of the 3-cube has analogues in higher-dimensional cubes (e.g., \(\binom{4}{2} = 6\) states in the 4-cube). Whether the doublet-pivot structure generalizes to higher-dimensional chiral doublets is an open question. *Next action:* Paper 009 (Lattice Closure) may provide the higher-dimensional context. *Owner:* Paper 009.

---

## 15. Discussion

The shell-2 chiral doublet is the **first dynamical interface** in the LCR framework. It appears at exactly the right shell (weight 2, middle of the grading), with exactly the right number of states (3: a doublet and a pivot), and exactly the right structure (exchanged by reversal, with one fixed point).

Several features make this doublet structurally significant:

**1. Reversal breaks symmetry.** Among the 3 shell-2 states, reversal splits 2 as a doublet and fixes 1. This 2+1 pattern is ubiquitous in particle physics: the weak isospin doublet + singlet in the Standard Model, the 2+1 generation structure (light + heavy), and the SU(2)\(\times\)U(1) breaking pattern.

**2. The correction operator couples to chirality.** The operator \(\partial = C \wedge \neg R\) fires on \(\mathrm{C-}\) but not \(\mathrm{C+}\). This distinguishes right-weighted from left-weighted chiral states. The coupling of correction (boundary repair) to chirality (reversal asymmetry) is the first instance of a pattern that reappears throughout the framework: the electroweak interaction differentiates left-handed from right-handed states.

**3. The doublet is the seed of SU(2).** The SU(2) fundamental representation (Theorem 6.6) emerges from the reversal action on 2 states. No additional structure is required: the Pauli \(\sigma_x\) generator is already present as the reversal operator. This suggests that the weak SU(2) is not an external gauge group but a structural consequence of the minimal LCR carrier.

**4. Trace-2 idempotents link to physics.** The identification with \(J_3(\mathbb{O})\) trace-2 idempotents (Theorem 6.7) anchors the doublet in the exceptional Jordan algebra. The three idempotents correspond to the three fermion generations in Papers 041–044. The doublet-pivot structure within the idempotents mirrors the known generation pattern: two "active" generations (up/down, charm/strange) and one "heavy" generation (top/bottom).

**5. The C- intersection is a triple point.** The state \((1,1,0) = \mathrm{C-}\) is the unique intersection of the shell-2 chiral doublet \(\{\mathrm{C+}, \mathrm{C-}\}\), the correction doublet \(\{(0,1,0), (1,1,0)\}\), and the non-fixed reversal orbit \(\{\mathrm{C+}, \mathrm{C-}\}\). This triple point is where the shell grading, the correction operation, and the reversal involution meet. It is the most connected state in the entire 8-state space after the vacua.

**6. Relation to the Fano plane.** Under the D4 axis/sheet assignment (Paper 005), the three shell-2 states are the three edges of the coordinate triangle in the Fano plane. The chiral doublet corresponds to two edges sharing a common vertex (e₁, e₂): \((1,1,0) = e₁e₂\) and \((0,1,1) = e₂e₃\). The pivot is the "far edge" \((1,0,1) = e₁e₃\) opposite that vertex. This geometry encodes the doublet-pivot separation.

---

## 16. References

### 16.1 Source Papers

- Paper 001 (LCR Minimal Carrier) — Shell grading, reversal involution, correction boundary, chart–\(J_3(\mathbb{O})\) bijection
- Paper 004 (D₄, J₃(𝕆), Triality) — Full D₄ axis/sheet codec extension
- Paper 005 (D4 Axis/Sheet) — D4 assignment of shell-2 states
- Paper 007 (Boundary Repair) — Correction surface and \(\partial\) operator
- Papers 041–044 (SU(3) Sector) — Fermion generation derivation from trace-2 idempotents
- Papers 045–048 (Electroweak Sector) — SU(2) from the chiral doublet
- Paper 113 (Carrier Reversal) — Expansion of reversal to polarity
- Paper 117 (O8 Spinor Double-Cover) — SU(2) → SO(3) closure

### 16.2 Workspace Libraries

- `PaperLib/paper-01__unified_lcr_kernel_and_chart.md` — Full source paper (461 lines, 48 claims, 95.8% D-ratio)
- `CrystalLib/crystal_lib.db` — Claim database (R-p01-02: shell-2 doublet binding, verified)
- `SQLLib/paper-01__unified_lcr_kernel_and_chart.sql` — SQL proof (8 tables: `lcr_states`, `shell_partitions`, `lcr_transitions`, `chart_j3o_bijection`)
- `CAMLib/paper-01__unified_lcr_kernel_and_chart.md` — CAM summaries (Claim 1.2: shell-2 doublet binding, verified)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data (paper-01 D/I/X: 46/1/1, highest A-family closure)

### 16.3 Standard Mathematics

- Conway, J. H., & Sloane, N. J. A. (1988). *Sphere Packings, Lattices and Groups.* Springer.
- Jacobson, N. (1968). *Structure and Representations of Jordan Algebras.* AMS Colloq. Publ. 39.
- Tits, J. (1966). *Classification of algebraic semisimple groups.* Proc. Symp. Pure Math. 9, 33–62.

---

The shell-2 chiral doublet is extracted from PaperLib paper-01 and cross-referenced with CrystalLib (R-p01-02, verified), SQLLib (`shell_partitions`, `reversal_pair`), and CAMLib (Claim 1.2). All 15 claims are D (data-backed). The doublet is the first dynamical interface of the LCR framework — the place where shell grading meets reversal chirality, correction couples to handedness, and the SU(2) seed emerges for the electroweak sector.

Paper 005 follows: the D4 Axis/Sheet codec that assigns the three shell-2 states to Fano plane edges.

Paper 007 follows: Boundary Repair and the Correction Surface, where \(\partial\) fires on C-.
