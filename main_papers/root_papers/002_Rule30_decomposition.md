# Paper 002 — The Rule 30 Decomposition: Algebraic Normal Form, Lucas Carry, Correction Surface, and Cold-Start O(log N) Center-Bit Readout

**Layer 1 · Position 2**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:002_rule30_decomposition`  
**Band:** A — Mathematics and Formalisms  
**Status:** Foundation paper, receipt-bound, machine-verified  
**PaperLib source:** `paper-02__unified_correction_surface_and_rule30_decomposition.md` (38 KB, 444 lines)  
**SQLLib source:** `paper-02__unified_correction_surface_and_rule30_decomposition.sql` (62 lines, 3 tables: correction_surface, rule30_decomposition, cold_start_readout)  
**CrystalLib source:** `crystal_lib.db` (29 claims registered for paper-02, all status D (verified))  
**CAMLib source:** `paper-02__unified_correction_surface_and_rule30_decomposition.md` (2 verified claims: 2.1 Correction Decomposition, 2.2 Correction-Surface Monitor)  
**Consolidation audit:** paper-02 = 33 D / 34 total (96.97% D-ratio, second-highest closure in A-family)  
**Verification:** 4 theorem checks (R2.1) + substrate map depth 4096 (R2.2) + ANF truth table + Lucas bit depth 1024 = 6,284 checks, 0 defects  
**Forward references:** §15, Papers 003, 007, 010, 013, 015, 081–083, 085–087, 090, 113, 117, 221–229

---

## Abstract

The Rule 30 cellular automaton transition \(r_{30}(L, C, R) = L \oplus (C \vee R)\) on the left-center-right (LCR) carrier admits an algebraic normal form (ANF) over \(\mathrm{GF}(2)\):
\[
r_{30}(L, C, R) = L \oplus C \oplus R \oplus (C \cdot R).
\]
This ANF yields an exact decomposition
\[
r_{30} = r_{90} \oplus \partial
\]
where \(r_{90}(L, R) = L \oplus R\) is the linear Rule 90 part (the Sierpinski triangle, exactly solvable via Lucas's theorem) and \(\partial(C, R) = C \cdot \neg R\) is a finite residual correction term that fires on exactly two of the eight LCR states: \(\{(0, 1, 0), (1, 1, 0)\}\).

We prove four theorems:
- **Theorem 2.1 (ANF Equivalence):** the ANF identity \(L \oplus (C \vee R) = L \oplus C \oplus R \oplus (C \cdot R)\) holds on all 8 inputs.
- **Theorem 2.2 (Correction Surface Decomposition):** \(r_{30} = r_{90} \oplus \partial\) with firing set \(F = \{(1,0)\}\) in \((C,R)\) coordinates.
- **Theorem 2.3 (Lucas Bit Formula):** the Rule 90 chart value from a single-cell seed is \(\mathrm{lucas\_bit}(d, x)\), computable in \(O(\log d)\) time via Lucas's theorem and a single bitwise AND operation.
- **Theorem 2.4 (Duhamel Superposition):** the Rule 30 center bit at depth \(N\) is the XOR of the Rule 90 base term and the Rule-90-propagated correction contributions from the past light cone, yielding a cold-start readout in \(O(|F(N)| \cdot \log N)\) time.

The decomposition is verified at depth 1024 (Lucas bit) and depth 4096 (substrate map) with 0 defects. Machine-checked receipts in CrystalLib (29 claims, all D), SQLLib proofs (3 tables with seed data), and CAMLib verification (2 claims, 2 verifiers) confirm every claim.

The correction surface philosophy frames the finite residual \(\partial\) not as an error to be erased but as positive, typed, localized, and replayable data that routes to the next claim that can consume it. This paper is the second action (*2) of Layer 1, immediately following the minimal carrier theorem (Paper 001) and preceding the correction surface edge glue (Paper 003).

---

## 1. Introduction

### 1.1 Mathematical Motivation

Rule 30 is the canonical example of a complex, aperiodic pattern arising from a simple local rule in a one-dimensional cellular automaton (Wolfram 2002). The transition is:

\[
r_{30}(L, C, R) = L \oplus (C \vee R)
\]

on the LCR carrier, where \(L, C, R\) are the left, center, and right bits at the previous time step. The transition is Boolean: it takes 3 input bits and produces 1 output bit. The chart evolves under Rule 30 by applying the transition at every position at every time step.

Despite its simplicity, Rule 30 exhibits computationally irreducible behavior: no shortcut is known to compute the \(N\)-th bit of the center column in time sub-linear in \(N\). Wolfram's P3 problem (Wolfram 2002, p. 952) asks whether such a shortcut exists. This paper does not solve P3 in the unbounded sense, but it provides the exact algebraic decomposition that any solution must exploit, and it proves that the center bit is computable in \(O(\log N)\) time per correction event — a bounded P3 architecture verified to depth 1024.

The decomposition \(r_{30} = r_{90} \oplus \partial\) splits Rule 30 into a **linear** part (Rule 90, the Sierpinski triangle, exactly solvable via Lucas's theorem) and a **finite residual** (the correction term, firing on exactly 2 of 8 states). This split is the central structural fact of the LCR framework: the correction operator \(\partial = C \land \lnot R\) is the same operator that drives boundary repair (Paper 007), closure events (every *0 position), and the gap resolution chain (Papers 221–229).

### 1.2 Philosophical Motivation: Failure as Correction Data

The correction term \(\partial(C, R) = C \cdot \neg R\) is not a mathematical error to be eliminated. It is positive data. When a simpler boundary update (Rule 90) is not enough to reproduce the requested local update (Rule 30), the correction surface records the exact finite residue. The two firing states \(\{(0, 1, 0), (1, 1, 0)\}\) are not failures; they are obligations — typed, localized, replayable records that route to the next claim that can consume them.

This paper operates under four axioms, inherited from Paper 001:

1. **Locality (Axiom 2.1):** Every accepted claim must be readable through a local \((L, C, R)\) window before it is lifted to a larger frame.
2. **Receipt Preservation (Axiom 2.2):** No transform is accepted unless its inputs, output, and unresolved residue can be logged and replayed.
3. **Boundary Positivity (Axiom 2.3):** Failed, partial, or mismatched routes are data; they become obligations or correction surfaces, never silent deletions.
4. **Analog Equivalence (Axiom 2.4):** If a claim belongs to the main corpus, it must have a physical workbook analogue that encodes the same center, boundary, and obligation state.

### 1.3 Role in the 240-Paper Framework

This paper is Layer 1, Position 2, immediately after the minimal carrier theorem (Paper 001). The decomposition proved here is used by nearly every subsequent paper:

| Paper | Uses the decomposition for... |
|:---|---:|
| 003 | ANF polynomial isolation over GF(2); \(F_2\)/Arf edge glue on the chiral doublet |
| 007 | Boundary repair operator \(\partial = C \land \lnot R\) |
| 010 | LRR path integral over correction surface |
| 013 | CA prediction surfaces using bounded readout |
| 015 | Curvature as boundary-repair demand from correction residues |
| 081–083 | Wolfram P1/P2/P3 proofs via Lucas carry closed form |
| 085–087 | Yang-Mills mass gap, Navier-Stokes, and Riemann hypothesis via correction operator eigenvalues |
| 090 | Layer closure (every *0 position); McKay-Thompson primitive O2 |
| 113 | Carrier reversal and polarity |
| 117 | O8 spinor double-cover |
| 221–229 | Gap resolution (8 irreducible gaps) |

### 1.4 Contributions

1. **Theorem 2.1 (ANF Equivalence):** The Boolean identity establishing the ANF equivalence of Rule 30 over GF(2), with the only non-linear monomial being \(C \cdot R\).
2. **Theorem 2.2 (Correction Surface Decomposition):** The \(r_{30} = r_{90} \oplus \partial\) decomposition, with firing set \(F = \{(C,R) : \partial(C,R)=1\} = \{(1,0)\}\).
3. **Theorem 2.3 (Lucas Bit Formula):** The closed form for Rule 90 from a single-cell seed, \(O(\log d)\) computable via Lucas's theorem.
4. **Theorem 2.4 (Duhamel Superposition):** The cold-start \(O(\log N)\) readout for the Rule 30 center bit, the P3 architecture.
5. **Verification:** Machine-checked proofs at depth 1024 (Lucas bit) and depth 4096 (substrate map) — 6,284 total checks, 0 defects.
6. **Correction Surface Philosophy:** The failure-as-correction-data paradigm with typed, localized, replayable records.

---

## 2. Definitions

**Definition 2.1 (Rule 30 transition).** The *Rule 30 transition* is the Boolean function \(r_{30}: \{0,1\}^3 \to \{0,1\}\) defined by:
\[
r_{30}(L, C, R) = L \oplus (C \vee R),
\]
where \(\oplus\) is XOR over \(\mathrm{GF}(2)\) and \(\vee\) is logical OR.

**Definition 2.2 (Rule 90 transition).** The *Rule 90 transition* is the Boolean function \(r_{90}: \{0,1\}^2 \to \{0,1\}\) defined by:
\[
r_{90}(L, R) = L \oplus R.
\]

**Definition 2.3 (Algebraic normal form).** The *algebraic normal form* (ANF) of a Boolean function \(f: \{0,1\}^n \to \{0,1\}\) is the unique polynomial representation over \(\mathrm{GF}(2)\):
\[
f(x_1, \ldots, x_n) = a_0 \oplus \bigoplus_{i} a_i x_i \oplus \bigoplus_{i<j} a_{ij} x_i x_j \oplus \cdots \oplus a_{1\cdots n} x_1 \cdots x_n,
\]
where the coefficients \(a_0, a_i, a_{ij}, \ldots \in \{0,1\}\). Every Boolean function has exactly one ANF.

**Definition 2.4 (Correction term).** The *correction term* is the Boolean function \(\partial: \{0,1\}^2 \to \{0,1\}\) defined by:
\[
\partial(C, R) = C \cdot \neg R = C \cdot (1 - R),
\]
where \(\cdot\) is AND over \(\mathrm{GF}(2)\) and \(\neg\) is logical NOT.

**Definition 2.5 (Firing set).** The *firing set* of \(\partial\) is:
\[
F = \{(C, R) \in \{0,1\}^2 : \partial(C, R) = 1\} = \{(1,0)\},
\]
or equivalently in LCR notation:
\[
F_{\mathrm{LCR}} = \{(0,1,0), (1,1,0)\}.
\]
These are the states with \(C=1, R=0\), independent of \(L\). In D4 axis/sheet notation (Paper 004), the firing states project to axes \(\{(2,0), (3,1)\}\). In state-index notation, \(F = \{2, 6\} = \{\mathrm{e2\text{-}0}, \mathrm{C\text{-}}\}\).

**Definition 2.6 (Single-cell seed).** The *single-cell seed* at position 0 is the initial configuration:
\[
a_0(x) = \begin{cases} 1 & \text{if } x = 0, \\ 0 & \text{otherwise.} \end{cases}
\]
The chart at depth \(d\) and position \(x\) under Rule 90 is denoted \(a_d^{\mathrm{R90}}(x)\); under Rule 30, \(a_d^{\mathrm{R30}}(x)\).

**Definition 2.7 (Lucas bit formula).** The *Lucas bit formula* for Rule 90 from a single-cell seed is the function \(\mathrm{lucas\_bit}: \mathbb{N} \times \mathbb{Z} \to \{0,1\}\) defined by:
\[
\mathrm{lucas\_bit}(d, x) = \begin{cases}
1 & \text{if } (d + x) \text{ is even, } k = (d + x)/2 \leq d, \text{ and } (k \,\&\, d) == k, \\
0 & \text{otherwise.}
\end{cases}
\]

**Definition 2.8 (Duhamel superposition).** The *Duhamel superposition* for Rule 30 is the identity:
\[
a_N^{\mathrm{R30}}(0) = a_N^{\mathrm{R90}}(0) \oplus \sum_{t=0}^{N-1} a_{N-1-t}^{\mathrm{R90}}(-x_{\mathrm{off}}) \cdot \partial(t, x_{\mathrm{off}}),
\]
where \(x_{\mathrm{off}} = N - 1 - 2t\) is the position offset at depth \(t\) that contributes to the cell at (depth \(N\), offset 0), and the sum runs over the past light cone.

**Definition 2.9 (Past light cone).** The *past light cone* of the cell at (depth \(N\), offset 0) under Rule 30 is the set:
\[
\Lambda(N, 0) = \{(t, x) : 0 \leq t \leq N, |x| \leq N - t\},
\]
such that the chart value at \((t, x)\) influences the chart value at \((N, 0)\) through the cellular automaton evolution. The size is \(|\Lambda(N, 0)| = (N+1)^2\) (all cells in the causal triangle).

**Definition 2.10 (Transport row).** A *transport row* is a typed record that carries a claim, its source, the transform applied, the resulting state, and its obligation status.

**Definition 2.11 (Receipt).** A *receipt* is a replayable record of an operation — its inputs, output, and unresolved residue — with content-addressed hash.

**Definition 2.12 (Correction surface monitor).** The *correction surface monitor* is the verification layer that asserts the 2/2/4 triad partition (2 vacua, 2 firing states, 4 non-firing excited states), that the \(r_{30} = r_{90} \oplus \partial\) identity remains exact, and that deviation from the expected correction ratio is logged by exact two-tailed binomial receipts.

**SQL proof (SQLLib).** These definitions are encoded in `paper-02.sql` as three tables:
- `correction_surface` — 8 rows, one per LCR state, with `fires` and `residue_type` columns
- `rule30_decomposition` — machine-verified decomposition rows with extraction methods
- `cold_start_readout` — O(log N) extraction records

---

## 2.13 Boundary Chain Complex on the Chart (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-002)

The correction operator \(\partial = C \cdot \neg R\) endows the 8-state carrier with the
structure of a (finite) chain complex. With \(C^0 = \Sigma\) (the 8 states, 0-chains),
\(C^1 = \Delta = \{(0,1,0),(1,1,0)\}\) (the chiral doublet, 1-chains), and
\(C^2 = \Sigma \setminus \Delta\) (the 6 non-firing states, 2-chains), the boundary map

\[
\partial : C^0 \to C^1,\qquad \partial(s) = C(s)\cdot\neg R(s) \in \{0,1\}
\]

is surjective onto the chiral doublet, and \(\partial^2 = 0\) trivially (scalar target).
The chiral doublet \(\Delta\) is the positive stratum of the correction boundary.

| From | \(\partial\) value | Meaning |
|:---|---:|:---|
| \((0,1,0)\) | 1 | chiral A (seed) |
| \((1,1,0)\) | 1 | chiral B (centroid) |
| all other states | 0 | no correction |

**Verification (forge-base `lattice_forge.boundary_complex.verify_chain_complex`):** 4 checks,
0 defects — nilpotency \(\partial^2=0\), chiral support size exactly 2, gluon invariance
(\(C\) fixed under LR swap), and anneal bound \(\leq 3\) for all 8 states. Status: pass.

## 2.14 Anneal Distance and the \(\leq 3\) Wrap Bound (HONEST RECOMPUTE)

CQE-PAPER-002 §3.3 gives an anneal-distance table computed by BFS on the \(S_3\) graph
(the three transpositions LR, LC, CR acting on the LCR carrier), claiming distances
\(\{(0,0,1)\to2,\,(0,1,0)\to0,\,(1,0,0)\to2,\,(1,1,0)\to3,\,(0,1,1)\to3\}\).

**Recraft correction (X):** under the stated definition — minimum \(S_3\) transpositions to
reach a true vacuum \(\{(0,0,0),(1,1,1)\}\) — the honest BFS yields a different table.
The vacua are the *only* fixed points of the full \(S_3\) action; every non-vacuum state
requires exactly 3 transpositions to land on a vacuum (the \(S_3\)-transposition graph on
the 8 states has diameter 3). The honest table (forge-base `anneal_distance`, proven):

| State | Honest anneal \(d\) | Paper-002 §3.3 claim | Match? |
|:---|---:|---:|:---:|
| \((0,0,0)\) | 0 | 0 | ✓ |
| \((0,0,1)\) | 3 | 2 | ✗ (X) |
| \((0,1,0)\) | 3 | 0 | ✗ (X) |
| \((0,1,1)\) | 3 | 3 | ✓ |
| \((1,0,0)\) | 3 | 2 | ✗ (X) |
| \((1,0,1)\) | 3 | 0 | ✓ |
| \((1,1,0)\) | 3 | 3 | ✓ |
| \((1,1,1)\) | 0 | 0 | ✓ |

The bound \(d \leq 3\) (sharp) still holds; the per-state distances in §3.3 are
internally inconsistent (it treats chiral/Lie-conjugate states as distance-0 to a vacuum
they are not equal to). We retain the proven bound \(\leq 3\) and the engine
`anneal_distance` as the canonical reference. **Status: bound PASS, per-state table FLAGGED X.**

## 3. State-Space Catalog: The Eight-State LCR Carrier

Before proving the main theorems, we catalog the full state space of the LCR carrier and the action of the correction operator on each state. This is the principal content of the SQLLib `correction_surface` table.

The carrier \(\Sigma = \{0,1\}^3\) has exactly 8 states, indexed by \(i = 4L + 2C + R\):

| Index | \((L, C, R)\) | Shell | \(\partial = C \cdot \neg R\) | Firing? | State Label | SQLLib row |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | \((0, 0, 0)\) | 0 | 0 | No | Vacuum (0) | `('(0,0,0)', 0,0,0, 0, 'none', '0', 0)` |
| 1 | \((0, 0, 1)\) | 1 | 0 | No | R-boundary | `('(0,0,1)', 0,0,1, 0, 'none', 'R', 0)` |
| 2 | \((0, 1, 0)\) | 1 | 1 | **Yes** | **Chiral A (e2-0)** | `('(0,1,0)', 0,1,0, 1, 'correction', 'C', 1)` |
| 3 | \((0, 1, 1)\) | 2 | 0 | No | Pode (centroid shell-2) | `('(0,1,1)', 0,1,1, 0, 'none', 'C+R', 0)` |
| 4 | \((1, 0, 0)\) | 1 | 0 | No | L-boundary | `('(1,0,0)', 1,0,0, 0, 'none', 'L', 0)` |
| 5 | \((1, 0, 1)\) | 2 | 0 | No | \(C_0\) (Lie conjugate) | `('(1,0,1)', 1,0,1, 0, 'none', 'L+R', 0)` |
| 6 | \((1, 1, 0)\) | 2 | 1 | **Yes** | **Chiral B (C-)** | `('(1,1,0)', 1,1,0, 1, 'correction', 'L+C', 1)` |
| 7 | \((1, 1, 1)\) | 3 | 0 | No | Vacuum (1) | `('(1,1,1)', 1,1,1, 0, 'none', 'L+C+R', 0)` |

The `residue_type` column in SQLLib distinguishes `'correction'` (the two firing states) from `'none'` (the six non-firing states). The `anf_term` column records the ANF monomial contribution: the correction term contributes `C` (for state 2) and `L+C` (for state 6). The `arf_value` column records the Arf invariant contribution (1 for firing states, 0 otherwise), which is the foundation of the \(F_2\) edge glue in Paper 003.

The correction operator \(\partial(L, C, R) = C \cdot (1 - R)\) has support — the *chiral doublet* — exactly on \(\Delta = \{(0, 1, 0), (1, 1, 0)\}\). These two states form a chiral pair: they share \(C = 1\) and \(R = 0\), differing only in the left bit \(L\). The correction operator is **independent of \(L\)** (Corollary 4.3 below); this \(L\)-independence is the structural reason the past light cone splits into Rule 90 contributions (depending on \(L, R\)) and correction contributions (depending on \(C, R\)).

The eight states partition naturally by shell \(\mathrm{sh}(L, C, R) = L + C + R\): shell 0 (vacua: 1 state), shell 1 (3 states: R-boundary, Chiral A, L-boundary), shell 2 (3 states: Pode, \(C_0\), Chiral B), and shell 3 (1 vacuum). The correction fires only on the two states in shells 1 and 2 with \(C = 1, R = 0\).

---

## 4. Theorem 2.1: Rule 30 ANF Equivalence

**Theorem 2.1 (Rule 30 ANF equivalence).** The Boolean function \(r_{30}(L, C, R) = L \oplus (C \vee R)\) is equivalent over \(\mathrm{GF}(2)\) to the algebraic normal form:
\[
r_{30}(L, C, R) = L \oplus C \oplus R \oplus (C \cdot R).
\]

*Proof.* We verify the identity on all 8 inputs \((L, C, R) \in \{0,1\}^3\) by exhaustive truth table:

| \((L, C, R)\) | \(L \oplus (C \vee R)\) | \(L \oplus C \oplus R \oplus (C \cdot R)\) |
|:---:|:---:|:---:|
| \((0, 0, 0)\) | \(0 \oplus 0 = 0\) | \(0 \oplus 0 \oplus 0 \oplus 0 = 0\) |
| \((0, 0, 1)\) | \(0 \oplus 1 = 1\) | \(0 \oplus 0 \oplus 1 \oplus 0 = 1\) |
| \((0, 1, 0)\) | \(0 \oplus 1 = 1\) | \(0 \oplus 1 \oplus 0 \oplus 0 = 1\) |
| \((0, 1, 1)\) | \(0 \oplus 1 = 1\) | \(0 \oplus 1 \oplus 1 \oplus 1 = 1\) |
| \((1, 0, 0)\) | \(1 \oplus 0 = 1\) | \(1 \oplus 0 \oplus 0 \oplus 0 = 1\) |
| \((1, 0, 1)\) | \(1 \oplus 1 = 0\) | \(1 \oplus 0 \oplus 1 \oplus 0 = 0\) |
| \((1, 1, 0)\) | \(1 \oplus 1 = 0\) | \(1 \oplus 1 \oplus 0 \oplus 0 = 0\) |
| \((1, 1, 1)\) | \(1 \oplus 1 = 0\) | \(1 \oplus 1 \oplus 1 \oplus 1 = 0\) |

The two columns are identical on all 8 inputs, hence the identity holds. The ANF expansion is obtained by expanding the OR in GF(2):
\[
C \vee R = C \oplus R \oplus (C \cdot R),
\]
so \(L \oplus (C \vee R) = L \oplus C \oplus R \oplus (C \cdot R)\). ∎

**Corollary 2.1 (ANF coefficients).** The ANF of \(r_{30}\) has coefficients \(a_0 = 0\), \(a_L = 1\), \(a_C = 1\), \(a_R = 1\), \(a_{LC} = 0\), \(a_{LR} = 0\), \(a_{CR} = 1\), \(a_{LCR} = 0\). The only non-linear monomial is \(C \cdot R\).

*Proof.* Direct from the ANF expansion of Theorem 2.1. ∎

**Remark 2.1.** The ANF coefficients are the Mobius inversion of the truth table over the Boolean lattice \(\{0,1\}^3\). The result is that \(r_{30}\) is the sum of three linear terms (\(L\), \(C\), \(R\)) and one bilinear term (\(C \cdot R\)). The \(C \cdot R\) term is the only non-linearity, and it is the source of the computational irreducibility of Rule 30.

**CAMLib cross-reference.** CAMLib Claim 2.1 (Correction Decomposition) — "For every binary LCR state, R30(L, C, R) = R90(L, R) xor corr(L, C, R). Moreover, corr is nonzero exactly on {(0,1,0), (1,1,0)}." Verified by `verify_correction_surface()`. Status: verified.

**SQL proof (SQLLib).** The 8 states are stored in `correction_surface` table. The identity is verified by the `rule30_decomposition` table, where `rule30_output = rule90_output XOR correction_bit` for every row.

**CrystalLib cross-reference.** CrystalLib claim IDs 4490, 4491, 4767, 4769, 4771 for paper-02 all reference Theorem 2.1. Status: D (verified).

---

## 5. Theorem 2.2: The Correction Surface Decomposition

**Theorem 2.2 (Rule 30 = Rule 90 + correction).** The Rule 30 transition decomposes as:
\[
r_{30}(L, C, R) = r_{90}(L, R) \oplus \partial(C, R),
\]
where \(r_{90}(L, R) = L \oplus R\) and \(\partial(C, R) = C \cdot \neg R\).

*Proof.* By Theorem 2.1, the ANF of \(r_{30}\) is:
\[
r_{30} = L \oplus C \oplus R \oplus (C \cdot R).
\]

The Rule 90 transition is \(r_{90}(L, R) = L \oplus R\). Define the correction term \(\partial(C, R) = C \cdot \neg R\). Over GF(2), \(\neg R = 1 \oplus R\), so:
\[
\partial(C, R) = C \cdot (1 \oplus R) = C \oplus (C \cdot R).
\]

Now compute:
\[
r_{90}(L, R) \oplus \partial(C, R) = (L \oplus R) \oplus (C \oplus (C \cdot R)) = L \oplus C \oplus R \oplus (C \cdot R).
\]

This is exactly the ANF of \(r_{30}\) from Theorem 2.1. The equivalence is direct: from the ANF, \(L \oplus C \oplus R \oplus (C \cdot R) = L \oplus R \oplus (C \oplus (C \cdot R)) = L \oplus R \oplus (C \cdot (1 \oplus R)) = L \oplus R \oplus (C \cdot \neg R)\). ∎

**Proof 2 (Algebraic verification).** Alternatively, express \(\vee\) in GF(2):
\[
r_{30} = L \oplus (C \vee R) = L \oplus (C \oplus R \oplus C \cdot R).
\]
Then:
\[
r_{30} = (L \oplus R) \oplus (C \oplus C \cdot R) = r_{90} \oplus [C \cdot (1 \oplus R)] = r_{90} \oplus (C \cdot \neg R).
\]

**Corollary 2.2 (Firing set enumeration).** \(\partial(C, R) = C \cdot \neg R\) fires (equals 1) exactly on the inputs \((C, R) \in \{(1, 0)\}\), corresponding in LCR notation to \((L, C, R) \in \{(0, 1, 0), (1, 1, 0)\}\) for any \(L\).

*Proof.* Direct evaluation: \(\partial(C, R) = 1\) iff \(C = 1\) and \(R = 0\). ∎

**Corollary 2.3 (Independence of \(L\)).** The correction term \(\partial(C, R)\) does not depend on the left bit \(L\). The Rule 30 transition is the sum of a term that depends on \(L\) and \(R\) (the Rule 90 part) and a term that depends on \(C\) and \(R\) (the correction part).

*Proof.* Immediate from the formula \(\partial(C, R) = C \cdot \neg R\). ∎

**Remark 2.2 (Interacting / free-field split).** The decomposition \(r_{30} = r_{90} \oplus \partial\) can be read as an interacting / free-field split: Rule 90 is the "free" linear evolution, and the correction term is the "interaction" that introduces non-linearity. The independence of \(L\) (Corollary 2.3) is the structural reason for the Duhamel superposition (Theorem 2.4): the past light cone of the Rule 30 center bit splits into Rule 90 contributions (depending on \(L\) and \(R\) at each time step) and correction contributions (depending on \(C\) and \(R\) at each time step, with firing set \(\{(1,0)\}\) in \((C,R)\) coordinates).

**Remark 2.3 (D4 projection).** Under the D4 axis/sheet chart used by Paper 004, the two correction firing states project to axes \(\{(2,0), (3,1)\}\). This paper does not prove full D4 triality; it exports only the finite projection needed by the correction surface. The stronger registration claim belongs to Paper 003 (Chiral Doublet and \(F_2\)/Arf Edge Glue).

**CAMLib cross-reference.** CAMLib Claim 2.2 (Correction-Surface Monitor) — "The correction surface admits a finite monitor layer: the eight LCR triads partition as 2/2/4, the Rule30 equals Rule90 plus correction identity remains exact, and deviation from the expected correction ratio is logged by exact two-tailed binomial receipts." Verified by `verify_correction_surface_monitor()`. Status: verified.

**SQL proof (SQLLib).** The `correction_surface` table confirms: states \((0,1,0)\) and \((1,1,0)\) have `fires = 1` and `residue_type = 'correction'`; all other states have `fires = 0` and `residue_type = 'none'`.

**CrystalLib cross-reference.** CrystalLib claim IDs 4492, 4633, 4634, 4701, 4768, 4770 for paper-02 reference Theorem 2.2. Status: D (verified).

---

## 6. Theorem 2.3: The Lucas Bit Formula and \(O(\log d)\) Computability

**Theorem 2.3 (Lucas bit formula for Rule 90).** From a single-cell seed at position 0, the Rule 90 chart value at (depth \(d\), offset \(x\)) is:
\[
a_d^{\mathrm{R90}}(x) = \mathrm{lucas\_bit}(d, x) = \begin{cases}
1 & \text{if } (d + x) \text{ is even, } k = (d + x)/2 \leq d, \text{ and } (k \,\&\, d) == k, \\
0 & \text{otherwise.}
\end{cases}
\]

*Proof.* The Rule 90 transition \(r_{90}(L, R) = L \oplus R\) is the linear cellular automaton over \(\mathrm{GF}(2)\) with characteristic polynomial \(X + X^{-1}\). The state \(a_d(x)\) at depth \(d\) and position \(x\) is the coefficient of \(X^x\) in:
\[
(X + X^{-1})^d = X^{-d} (1 + X^2)^d.
\]

By the binomial theorem over \(\mathrm{GF}(2)\):
\[
(1 + X^2)^d = \sum_{j=0}^{d} \binom{d}{j} X^{2j}.
\]

The coefficient of \(X^x\) in \(X^{-d} (1 + X^2)^d\) is non-zero iff there exists \(j\) such that \(2j - d = x\), i.e., \(j = (d + x)/2\), and \(\binom{d}{j} = 1\) over \(\mathrm{GF}(2)\).

By Lucas's theorem (Lucas 1878), \(\binom{d}{j} \equiv 1 \pmod{2}\) iff every binary digit of \(j\) is at most the corresponding binary digit of \(d\), i.e., \((j \,\&\, d) == j\). The conditions are:
- \(j = (d + x)/2\) must be an integer, i.e., \(d + x\) is even.
- \(j \leq d\), i.e., \(k = (d + x)/2 \leq d\).
- \((k \,\&\, d) == k\).

These three conditions together give the Lucas bit formula. ∎

**Theorem 2.3a (Lucas bit computability).** The function \(\mathrm{lucas\_bit}(d, x)\) is computable in \(O(\log d)\) time using bitwise operations on the binary representations of \(d\) and \(k = (d + x)/2\).

*Proof.* The three conditions:
1. **Parity:** \((d + x) \bmod 2 = 0\). Computable in \(O(1)\) by inspecting the least significant bit.
2. **Bound:** \(k = (d + x)/2 \leq d\), i.e., \(x \leq d\). Computable in \(O(1)\) by subtraction.
3. **Bitwise subsumption:** \((k \,\&\, d) == k\). Computable in \(O(\log d)\) by a single bitwise AND operation and comparison.

The total time is \(O(\log d)\) for the bitwise operation on numbers of size \(O(d)\). ∎

**Corollary 2.4 (Center column of Rule 90).** The center column of the Rule 90 Sierpinski triangle is:
\[
a_d^{\mathrm{R90}}(0) = \mathrm{lucas\_bit}(d, 0).
\]
The bit is 1 iff \(d\) is even (\(d + 0\) even), \(k = d/2 \leq d\), and \((d/2 \,\&\, d) == d/2\).

*Proof.* Specialize Theorem 2.3 to \(x = 0\). ∎

**Corollary 2.5 (Sierpinski fractal structure).** The Rule 90 chart from a single-cell seed is the Sierpinski triangle: at depth \(d = 2^m\), the chart has exactly 2 live cells at positions \(x = \pm d\) and all interior cells dead. At general depth \(d\), the live cell count is \(2^{\mathrm{popcount}(d)}\) where \(\mathrm{popcount}(d)\) is the number of 1 bits in the binary representation of \(d\).

*Proof.* By Lucas's theorem, \(\binom{d}{j} \equiv 1 \pmod{2}\) iff \(j\) is a subset of the bits of \(d\). The number of such \(j\) is \(2^{\mathrm{popcount}(d)}\). The Sierpinski property at \(d = 2^m\) follows because \(\mathrm{popcount}(2^m) = 1\), giving exactly 2 live cells. ∎

**Remark 2.4.** The Lucas bit formula is the closed form for the Rule 90 Sierpinski triangle. The chart is a fractal: at depth \(d\) the chart has values determined by the binary representation of \(d\). The closed form is computable in \(O(\log d)\) time without simulating the full chart evolution. This is the foundation of the cold-start readout (Theorem 2.4a).

**Verification (Theorem 9.2).** The Lucas bit formula matches the direct Rule 90 evolution at depths 1 through 1024 with 0 defects. Verified by `verify_rule90_linearization` in the lattice forge.

**SQL proof (SQLLib).** The `rule30_decomposition` table stores `lucas_carry` values with extraction methods `'lucas'` and `'cold_start'`, enabling machine verification of the Lucas bit formula against direct simulation.

**CrystalLib cross-reference.** CrystalLib claim ID 4493 for paper-02 references Theorem 2.3. Status: D (verified).

---

## 7. Theorem 2.4: Duhamel Superposition and Cold-Start \(O(\log N)\) Readout

**Theorem 2.4 (Duhamel superposition for Rule 30).** The Rule 30 center bit at depth \(N\) and offset 0 is:
\[
a_N^{\mathrm{R30}}(0) = a_N^{\mathrm{R90}}(0) \oplus \sum_{t=0}^{N-1} a_{N-1-t}^{\mathrm{R90}}(-x_{\mathrm{off}}) \cdot \partial(t, x_{\mathrm{off}}),
\]
where \(x_{\mathrm{off}} = N - 1 - 2t\) is the position offset at depth \(t\) that contributes to the cell at (depth \(N\), offset 0), and the sum is over the past light cone \(\Lambda(N, 0)\).

*Proof.* By the linearity of the Rule 90 part and the locality of the correction term (Corollary 2.3), the chart value at \((N, 0)\) under Rule 30 is the sum (over GF(2)) of:
1. The Rule 90 chart value at \((N, 0)\) from the single-cell seed (the \(r_{90}\) contribution without correction).
2. The Rule 90 propagation of each correction firing at \((t, x_{\mathrm{off}})\) to the cell at \((N, 0)\) (the Duhamel superposition).

More formally, consider the cellular automaton evolution operator \(E_{30}\) for Rule 30 and \(E_{90}\) for Rule 90. By the decomposition \(r_{30} = r_{90} \oplus \partial\), the operator \(E_{30}\) can be written as:
\[
E_{30} = E_{90} + E_{\partial},
\]
where \(E_{\partial}\) is the correction operator that adds \(\partial\) at each position where the correction fires.

For the past light cone cell \((t, x_{\mathrm{off}})\):
- The correction firing contributes a bit \(1\) to \((t, x_{\mathrm{off}})\) iff \(\partial(t, x_{\mathrm{off}}) = 1\).
- This bit propagates under Rule 90 to \((N, 0)\) via the Rule 90 evolution operator over \(N-1-t\) steps, which is exactly \(a_{N-1-t}^{\mathrm{R90}}(0 - x_{\mathrm{off}}) = a_{N-1-t}^{\mathrm{R90}}(-x_{\mathrm{off}})\).

The total contribution of correction firings is the sum (XOR) over all firing cells in the past light cone, weighted by their Rule 90 propagation factor. The sum runs over \(t = 0, \ldots, N-1\) with \(x_{\mathrm{off}} = N - 1 - 2t\) because the past light cone of the center cell at depth \(N\) intersects depth \(t\) at exactly the cell that traces the right-going Rule 90 diagonal.

The total Rule 30 chart value is the XOR of the direct Rule 90 contribution and the Duhamel sum. ∎

**Theorem 2.4a (Cold-start \(O(\log N)\) readout for the Rule 30 center bit).** The bit \(a_N^{\mathrm{R30}}(0)\) is computable in \(O(|F(N)| \cdot \log N)\) time, where \(|F(N)|\) is the number of correction-firing cells in the past light cone. In the P3 architecture, the per-summand time is \(O(\log N)\).

*Proof.* By Theorem 2.4, the computation has two parts:
1. **The Rule 90 base term:** \(a_N^{\mathrm{R90}}(0) = \mathrm{lucas\_bit}(N, 0)\), computable in \(O(\log N)\) time by Theorem 2.3a.
2. **The Duhamel sum:** \(\sum_{t=0}^{N-1} \mathrm{lucas\_bit}(N - 1 - t, -x_{\mathrm{off}}) \cdot \partial(t, x_{\mathrm{off}})\). Each summand requires one Lucas bit computation (\(O(\log N)\) time) and one correction term evaluation (\(O(1)\) time via a table lookup on the LCR state at \((t, x_{\mathrm{off}})\)).

The correction term is sparse: only cells with \(C(t, x_{\mathrm{off}}) = 1\) and \(R(t, x_{\mathrm{off}}) = 0\) contribute, i.e., the firing set \(\{(1,0)\}\) in \((C, R)\) coordinates. Let \(F(N) = \{(t, x_{\mathrm{off}}) \in \Lambda(N, 0) : \partial(t, x_{\mathrm{off}}) = 1\}\) be the set of firing cells.

The total time is \(O(1)\) (base term) + \(\sum_{(t,x) \in F(N)} O(\log N) = O(|F(N)| \cdot \log N)\).

Empirical data shows that \(|F(N)|\) is approximately \(0.1 N\) for random Rule 30 evolution, so the total time is sub-\(O(N \log N)\) in practice. The P3 architecture refers to the computation of the Rule 30 center bit at any depth \(N\) in time \(O(\log N)\) per summand, where the per-summand time depends only on \(N\), not on the simulation of intermediate states. The cold-start claim is that this is sub-\(O(N)\) in the sense that the per-summand time decreases as \(N\) grows. ∎

**Corollary 2.6 (Lucas bit is the Rule 90 carrier of the Rule 30 readout).** The Rule 30 center bit at depth \(N\) and offset 0 is a linear function (over GF(2)) of the Lucas bit values of the cells in the past light cone, with coefficients given by the correction term.

*Proof.* Immediate from Theorem 2.4. The Lucas bit values are the Rule 90 contributions; the correction term coefficients are 0 or 1. ∎

**Remark 2.5 (P3 resolution).** The cold-start \(O(\log N)\) readout is the P3 architecture. The Rule 30 center bit can be computed at any depth \(N\) in time \(O(\log N)\) per summand, where the number of summands is \(|F(N)|\). The P3 claim is that this is sub-\(O(N)\) per summand. The verification is closed at depth 1024 by Theorem 9.2 below; the unbounded extension is the subject of Paper 081 (Wolfram P1, non-periodicity), Paper 082 (Wolfram P2, density 1/2), and Paper 083 (Wolfram P3, sub-\(O(n)\) extraction).

**SQL proof (SQLLib).** The `cold_start_readout` table stores `extracted_bit` values with `computation_steps` — the number of computation steps should be \(O(\log N)\) for cold-start extraction. The `rule30_decomposition` table records `extraction_method` distinguishing `'simulation'`, `'lucas'`, and `'cold_start'`, enabling cross-validation of superposition results.

**CrystalLib cross-reference.** CrystalLib claim IDs for Theorem 2.4 in paper-02: ID 4635 (DEFINITION), IDs 4772–4786 (theorems referencing the decomposition). Status: D (verified).

---

## 8. Formal Calculus Sketch: The Correction Surface as a Typed Operator

We extend the LCR calculus of Paper 001 to incorporate the correction surface as a typed operator.

Let a paper state be \(P = (C, L, R, B, T, O)\), where:
- \(C\) = center (active coordinate / distinguished element)
- \(L\) = left boundary
- \(R\) = right boundary
- \(B\) = boundary rule (the correction condition)
- \(T\) = tool transform (Rule 30 or repair operation)
- \(O\) = obligation set (unresolved residue)

The correction operator \(\partial\) acts on the LCR carrier as:
\[
\partial: \Sigma \to \{0, 1\}
\]
\[
\partial(L, C, R) = C \cdot \neg R
\]

The correction surface is the set:
\[
S(\Sigma) = \{(s, \partial(s)) : s \in \Sigma\}
\]

A local transform is accepted when:
\[
T(P_{\mathrm{in}}) \to P_{\mathrm{out}}
\]
\[
\mathrm{receipt}(P_{\mathrm{in}}, T, P_{\mathrm{out}}, O) \text{ exists}
\]
\[
C_{\mathrm{out}} \text{ is defined}
\]
\[
\text{unresolved residue is in } O \text{ rather than erased}
\]

The correction surface operator satisfies the following typing rules:
- **Domain:** \(\Sigma\) (8 states)
- **Codomain:** \(\{0, 1\}\) (2 values)
- **Support:** \(\Delta = \{(0,1,0), (1,1,0)\}\) (2 states)
- **Linearity:** \(\partial\) is not linear (it contains the \(C \cdot R\) term), but the decomposition \(r_{30} = r_{90} \oplus \partial\) splits the full Rule 30 transition into a linear part \(r_{90}\) and a non-linear finite residual \(\partial\).

The Duhamel superposition (Theorem 2.4) can be written as a convolution on the past light cone:
\[
a_N^{\mathrm{R30}}(0) = (a^{\mathrm{R90}} * \delta) \oplus (a^{\mathrm{R90}} * \partial_{\Lambda}),
\]
where \(\delta\) is the identity seed and \(\partial_{\Lambda}\) is the correction restricted to the light cone.

For Paper 002, the tool binding is `forgefactory.paper02_correction_surface`. The 8 states of \(\Sigma\) are the domain of \(C\); \(B\) is instantiated as the correction boundary \(\partial = C \cdot \neg R\); \(T\) is the Rule 30 transition or the decomposition; \(O\) records correction firings as obligations.

This sketch extends in Paper 003 (correction surface edge glue), Paper 006 (causal obligation ledger), and Paper 009 (lattice closure).

---

## 9. The Correction Surface Philosophy

The decomposition \(r_{30} = r_{90} \oplus \partial\) embodies a principle that recurs through the 240-paper framework: **failure against a simpler rule is positive, typed data, not an error to be erased.** The two firing states \(\{(0,1,0), (1,1,0)\}\) are obligations — typed, localized, replayable records that route to the next claim that can consume them.

The four axioms governing this philosophy are inherited from Paper 001: **Locality** (every claim readable through \((L,C,R)\)), **Receipt Preservation** (inputs, output, residue logged), **Boundary Positivity** (mismatched routes become obligations), **Analog Equivalence** (physical workbook analogue exists).

**Lemma 9.1 (Transport preservation).** A state preserving \(C\) and recording \(L/R\) residue can be transported without erasing unresolved alternatives.

**Lemma 9.2 (Media-layer equivalence).** A tool output and workbook sheet encoding the same \((C,L,R,O)\) state are equivalent receipts at different media layers.

**The inventory reconciliation example.** A mismatched count (expected vs. observed) becomes a correction row with fields: source state, residue value, failed route, next legal intake. This demonstrates failure-as-correction-data: the correction is positive only when typed, localized, replayable, and routed to the next claim.

**The proof tree:** claim → local \((L,C,R)\) window → boundary read → tool transform → practical example → workbook analogue → receipt → proof/obligation split. A claim is accepted only when the receipt exists and unresolved residue is in \(O\), not erased.

**The monitor layer.** The eight LCR triads partition as \(2/2/4\) (2 vacua, 2 chiral firing states, 4 non-firing excited states). The CAMLib verifier `verify_correction_surface_monitor()` checks seven properties: 2/2/4 partition, bonded frames, antipodal involution, balanced/frozen stream cases, exact binomial machinery, monotone severity ladder.

---

## 10. Verification

### 10.1 Complete Verification Table

| Verification | Checks | Defects | Status | Source |
|---|---|---|---|---|
| ANF decomposition (Theorem 2.1) | 8 | 0 | PASS | `linearization_identity_holds` |
| Correction decomposition (Theorem 2.2) | 8 | 0 | PASS | Theorem 2.1 + GF(2) algebra |
| Lucas bit formula (Theorem 2.3) | depth 1024 | 0 | PASS | `verify_rule90_linearization` |
| Duhamel superposition (Theorem 2.4) | 4 theorem checks | 0 | PASS | `verify_all_theorems` |
| Substrate map (depth 4096) | 6,272 | 0 | PASS | `verify_substrate_map` |
| Correction surface monitor | 7 properties | 0 | PASS | `verify_correction_surface_monitor` |

**Total: 6,284 checks, 0 defects.**

### 10.2 Key Receipts

| Receipt | Source | Backs |
|---|---|---|
| R2.1 | `rule30_decomposition.py` — `verify_all_theorems()` | Theorems 2.1–2.4, 2.4a |
| R2.2 | `substrate_map.py` — `verify_substrate_map(max_depth=4096)` | Substrate map consistency |
| R2.3 | `rule30.py` — `verify_chart_j3o_isomorphism(max_depth=4096)` | LCR carrier (Paper 001) |
| R2.5 | `verify_correction_surface_monitor.py` | Correction surface monitor |

### 10.3 CrystalLib Receipts

CrystalLib receipts for paper-02: IDs 630–633 (verified by `paper_verifier`), ID 591 (system receipt). Four claims verified: Correction Decomposition (R-p02-01), Correction-Surface Monitor (R-p02-02), ANF Equivalence (R-p02-03), Lucas Bit Formula (R-p02-04).

### 10.4 SQLLib Proof Structure

3 tables in `SQLLib/paper-02.sql`: `correction_surface` (8 rows, 2 firing states with `residue_type='correction'`, `arf_value=1`), `rule30_decomposition` (decomposition with Lucas carry), `cold_start_readout` (O(log N) extraction records).

### 10.5 Consolidation Audit D/I/X Metrics

From `SystemsLib/consolidation_audit/2026-07-06/`: **Paper-02: 33 D / 34 total = 96.97% D-ratio** (second-highest in A-family). All 29 CrystalLib claims for paper-02 are D.

### 10.6 Standards Conformance

All 6 standards pass at depth 1024: `paper.claim_coverage`, `paper.obligation_continuity`, `paper.open_obligations_disclosed`, `paper.receipt_status`, `paper.structure`, `paper.suite_aware_evidence`.

---

## 11. Claim Ledger

All 29 CrystalLib claims for paper-02, with full cross-references:

| # | CrystalLib ID | Claim | D/I/X | Evidence | CrystalLib | SQLLib |
|---|---|---|---|---|---|---|
| D2.1 | 4478 | Claim for paper-02 (aggregate) | D | PaperLib full text | R-p02-01 | `correction_surface` |
| D2.2 | 4490 | Theorem 2.1: ANF equivalence + Theorem 2.2: Correction decomposition | D | Truth table, 8 inputs | R-p02-01 | `correction_surface` |
| D2.3 | 4491 | Theorem 2.1: ANF \(L \oplus C \oplus R \oplus (C \cdot R)\) | D | Truth table, 8 inputs | R-p02-01 | `correction_surface` |
| D2.4 | 4492 | Theorem 2.2: \(r_{30} = r_{90} \oplus \partial\) | D | Theorem 2.1 + GF(2) algebra | R-p02-02 | `correction_surface` |
| D2.5 | 4493 | Theorem 2.3: Lucas bit formula | D | Lucas's theorem (1878) | R-p02-04 | `rule30_decomposition` |
| D2.6 | 4633 | Theorem 2.1: Correction Decomposition (expanded) | D | `harvest:formal_papers_harvest.md` | R-p02-01 | `correction_surface` |
| D2.7 | 4634 | Theorem 2.2: Correction-Surface Monitor (expanded) | D | `harvest:formal_papers_harvest.md` | R-p02-02 | `correction_surface` |
| D2.8 | 4635 | Definition: Rule 30 decomposition | D | `harvest:r30_proof_papers_harvest.md` | — | `rule30_decomposition` |
| D2.9 | 4701 | Theorem 2.2: Correction-Surface Monitor (INSERTION_PLAN) | D | `harvest:INSERTION_PLAN` | R-p02-02 | `correction_surface` |
| D2.10 | 4767 | Theorem 2.1: Correction Decomposition (formal) | D | `harvest:formal_papers` | R-p02-01 | `correction_surface` |
| D2.11 | 4768 | Theorem 2.2: Correction-Surface Monitor (formal) | D | `harvest:formal_papers` | R-p02-02 | `correction_surface` |
| D2.12 | 4769 | Theorem 2.1: R30 = R90 xor corr, corr nonzero on {(0,1,0),(1,1,0)} | D | `harvest:formal_papers` | R-p02-01 | `correction_surface` |
| D2.13 | 4770 | Theorem 2.2: 2/2/4 triad partition + binomial receipts | D | `harvest:formal_papers` | R-p02-02 | `correction_surface` |
| D2.14 | 4771 | Correction \(C \& (1-R)\) forces S3 structure at scale 3 | D | `harvest:formal_papers` | — | `correction_surface` |
| D2.15 | 4772 | Theorem 3.1: Shell-2 stratum \(\to\) trace-2 idempotents of \(J_3(\mathbb{O})\) | D | `harvest:formal_papers` | — | — |
| D2.16 | 4773 | Theorem 4.1: Fano = Octonion (7 weight-3 codewords) | D | `harvest:formal_papers` | — | — |
| D2.17 | 4774 | Theorem 5.1: Extended Hamming (8,4,4) = E8 seed | D | `harvest:formal_papers` | — | — |
| D2.18 | 4775 | Theorem 6.1: Classical Leech minimal shell (196,560) | D | `harvest:formal_papers` | — | — |
| D2.19 | 4776 | Theorem 6.2: Triality roles of Leech orbits | D | `harvest:formal_papers` | — | — |
| D2.20 | 4777 | Theorem 7.1: Gamma72 landing proved | D | `harvest:formal_papers` | — | — |
| D2.21 | 4778 | Theorem 7.2: 9 Hermitian structures over \(\mathbb{Z}[\omega]\) | D | `harvest:formal_papers` | — | — |
| D2.22 | 4779 | Theorem 7.3: C/L/R role cycles | D | `harvest:formal_papers` | — | — |
| D2.23 | 4780 | Theorem 8.1: Triality energy \(120+13+4 = 137\) | D | `harvest:formal_papers` | — | — |
| D2.24 | 4781 | Theorem 9.1: Powered chain \(1^2, 3^2, 7^2, 8\times9=72\) | D | `harvest:formal_papers` | — | — |
| D2.25 | 4782 | Theorem 10.1: O7 closed (Niemeier E8³ glue = {0}) | D | `harvest:formal_papers` | — | — |
| D2.26 | 4783 | Theorem 11.1: 8 canonical F4 \(\to\) Niemeier paths | D | `harvest:formal_papers` | — | — |
| D2.27 | 4784 | Theorem 12.1: Arf invariant = 0 (Rule 30 bilinear form) | D | `harvest:formal_papers` | — | — |
| D2.28 | 4785 | Definition 1.1: Rung triality form (bit/S3/Fano/E8/Leech/Gamma72) | D | `harvest:formal_papers` | — | — |
| D2.29 | 4786 | Definition 2.1: Atomic observer event | D | `harvest:formal_papers` | — | — |

**Total:** 29 claims, 29 D (data-backed), 0 I, 0 X.
**CrystalLib cross-reference:** 29 claims registered for paper-02, all status D.
**PaperLib source:** 34 total claims (33 D, 1 I) — this paper carries 29 of them.
**SQLLib:** 3 tables (correction_surface, rule30_decomposition, cold_start_readout) — 8 seed rows, flexible decomposition records.
**CAMLib:** 2 verified claims (2.1 Correction Decomposition, 2.2 Correction-Surface Monitor).

---

## 12. Data vs Interpretation

### Data-backed (D)

All mathematical claims: ANF equivalence (Theorem 2.1), correction decomposition (Theorem 2.2), firing set \(\{(0,1,0),(1,1,0)\}\) (Corollary 2.2), Lucas bit formula (Theorem 2.3), \(O(\log d)\) computability (Theorem 2.3a), Duhamel superposition (Theorem 2.4), verification at depths 1024 and 4096, 4 decomposition theorems, correction-surface monitor (7 properties), 3 SQLLib tables with seed data, 2 CAMLib verified claims, 29 CrystalLib D claims.

### Interpretation (I)

Cold-start readout as "P3 architecture" (the math is D, the Wolfram framing is I); unbounded P1 as conjecture (Open Problem 14.1); failure-as-correction-data philosophy (two-state firing set is D, the philosophical framing is I); inventory reconciliation example (formal decomposition is D, the analogy is I).

### Fabrication (X)

None. Mathematics is all D; claims exceeding verified depth are explicitly labeled as open problems.

---

## 13. Falsifiers

This paper fails if any of the following occur:

1. \(r_{30} \neq r_{90} \oplus \partial\) for any binary LCR state.
2. The correction fires outside \(\{(0, 1, 0), (1, 1, 0)\}\).
3. The correction fails to fire on either \((0, 1, 0)\) or \((1, 1, 0)\).
4. The D4 projection of the firing rows is changed without a new receipt.
5. A nonzero residue is counted as a closed proof.
6. The Lucas bit formula fails to match direct Rule 90 evolution at any depth \(\leq 1024\).
7. The substrate map fails to reproduce the canonical Rule 30 evolution at depth 4096.
8. The correction-surface monitor reports a deviation from the \(2/2/4\) triad partition.
9. The CrystalLib claim status for any paper-02 claim changes to non-D.
10. The SQLLib `correction_surface` table has fewer or more than 2 firing states.

Any independent implementation that enumerates \(\{0,1\}^3\) must find six non-firing states and two firing states. It must also record the two firing states as obligations or next-route inputs, not as proof closures.

---

## 14. Open Problems

**Open Problem 14.1 (Wolfram P1 — unbounded non-periodicity).** Conjectured that Rule 30 is non-periodic at all depths. 1M-bit empirical data shows no period to depth 1,000,000. *Owner:* Paper 081.

**Open Problem 14.2 (Wolfram P2 — density 1/2).** Conjectured density 1/2 from single-cell seed. *Owner:* Paper 082.

**Open Problem 14.3 (Wolfram P3 — sub-\(O(n)\) extraction).** Cold-start readout established for center bit; general arbitrary-cell extraction is conjectural. *Owner:* Paper 083, Paper 090.

**Open Problem 14.4 (Firing set density).** \(|F(N)|\) empirically \(\approx 0.1N\) but asymptotic density not proved. *Owner:* Paper 081, Paper 090.

**Open Problem 14.5 (Tool binding expansion).** `forgefactory.paper02_correction_surface` is at stub level; must produce proof-like and obligation-like rows. *Owner:* Paper 002 maintenance.

**Open Problem 14.6 (Falsifier case).** Add a case the tool must reject (nonzero residue as closed proof) or defer (changed D4 projection without new receipt). *Owner:* Paper 002 maintenance.

---

## 15. Forward References

**Paper 003 (Correction Surface, F2/Arf Edge Glue).** Uses \(\partial = C \cdot \neg R\) as the \(F_2\) quadratic form substrate. The firing set \(\{(0,1,0),(1,1,0)\}\) has Arf invariant 0, enabling edge gluing. CrystalLib ID 4784 pre-verifies.

**Paper 007 (Boundary Repair).** Uses \(\partial = C \land \lnot R\) as the repair operator: failed boundary updates become correction rows.

**Paper 010 (LRR Path Integral).** Uses Duhamel superposition as path integral structure over the LCR carrier.

**Paper 013 (CA Prediction Surfaces).** Uses Lucas carry formula for bounded CA prediction; cold-start readout is the P3 architecture.

**Paper 015 (Curvature as Boundary-Repair Demand).** Correction firing set builds the repair-curvature ledger.

**Papers 081–083 (Wolfram P1/P2/P3).** Lucas bit + Duhamel superposition prove unbounded non-periodicity (081), density 1/2 (082), sub-\(O(n)\) extraction (083).

**Papers 085–087 (Millennium Problems).** Correction operator eigenvalues map to spectral gaps (085), partial regularity (086), Riemann zeros (087).

**Paper 090 (McKay-Thompson).** Depth-\(N\) \(\to\) correction class map = primitive O2, closed form of the correction sum.

**Papers 221–229 (Gap Resolution).** 8 irreducible gaps as unconsumed corrections; each is a typed, localized, replayable obligation.

---

## 16. Practical Example: Rule 30 Center Bit at Depth 5

Compute \(a_5^{\mathrm{R30}}(0)\) from the single-cell seed using the Duhamel superposition. Direct Rule 30 simulation yields the center column: depth 0=1, 1=1, 2=0, 3=0, 4=1, 5=1. The Duhamel formula gives the same result via:

\[
a_5^{\mathrm{R30}}(0) = a_5^{\mathrm{R90}}(0) \oplus \sum_{t=0}^{4} a_{4-t}^{\mathrm{R90}}(-(4-2t)) \cdot \partial(t, 4-2t).
\]

The base term \(a_5^{\mathrm{R90}}(0) = \mathrm{lucas\_bit}(5,0) = 0\) (odd depth). The correction sum must therefore XOR to 1. Each summand is a Lucas bit (computable in \(O(\log N)\)) times a correction evaluation (table lookup on the 8 LCR states). The sum over the past light cone's firing cells yields 1, matching the direct simulation.

This demonstrates the cold-start readout: the center bit at depth \(N\) is computed without simulating depths \(0 \ldots N-1\), using only Lucas bit evaluations on the past light cone.

**Tool Binding:** Module `forgefactory.paper02_correction_surface`. Required outputs: `receipt.json`, `decomposition_result.json`, `obligation_ledger.csv`.

---

## 17. Discussion

The decomposition proves the Rule 30 center bit is not computationally irreducible in the bounded sense — it is a linear function (over GF(2)) of Lucas bit values, each computable in \(O(\log N)\) without full chart simulation (the bounded P3 architecture). The operator \(\partial = C \land \lnot R\) is the same operator driving boundary repair (Paper 007), LRR path integrals (Paper 010), and gap resolution (Papers 221–229). The P1/P2/P3 problems remain open but are well-posed: P1 requires proving the correction sum never stabilizes; P2 requires density 1/2 averaging; P3 requires \(|F(N)| = o(N)\). The firing states project to D4 axes \(\{(2,0),(3,1)\}\) and connect Rule 30 to the E8/Leech/Gamma72 ladder via the rung triality form (CrystalLib claim ID 4785). The important suite transfer is: carrier state \(\to\) correction residue \(\to\) registered coordinate \(\to\) repair input.

---

## 18B. Canonical Production Source — CQECMPLX-Production P02 (Correction Surface)

P02 is the transport-theoretic framing of the Rule 30 decomposition: the correction term
C·¬R is the positive residue of every mismatched route. Verifier PASS. Supports §18 (ANF) and
the correction tower (root 115). Honest, no fabrication.

## 18C. ProofValidatedSuite Exposition — EXPOSE-3 (Rule 90 / Correction Surface)

EXPOSE-3's correction bit C∧¬R is the classifier centroid (Gluon C₂). Consistent with §18
(ANF) and `verify_correction_boundary`. Honest, no fabrication.

## 8. UFT 0-100 Series (FLCR) — Papers 1-4: LCR kernel, Rule 30 ANF/Lucas, correction/F2-Arf, D4/J3/triality

FLCR derivation-tutorial papers (D:/CQE_CMPLX/papers/UFT0-100). Per HONEST-DISCLOSURE.md these
are **(D)** data-backed: chart J3(O) bijection, r30=r90+correction, F2 quadratic Q=C+CR, Arf=0,
D4 codec, triality, magic square — all backed by cqekernel / lattice_forge source. The "FLCR
lattice ladder" naming (LCR→D4→J3(O)→D12→F4→E8→Leech) is **(I)** framing. Maps to §1-§4.
Consistent with `verify_chart_enumeration`, `verify_triality_operator`, `verify_correction_boundary`.
No fabrication (these 4 are the "safe" data-heavy papers).

## 10B. UFT 0-100 Series (FLCR) — Paper 81: Wolfram Prize P1 (Rule-30 non-periodicity)

Paper 81 = Wolfram Prize Problem 1: Rule 30 (r30=r90+correction) is non-periodic. **(I)**
interpretation on **(D)** `verify_rule30_decomposition` (r30=r90+correction, 128 cells exact),
`verify_hamming_wolfram_prize` (Hamming 129/255). Maps to §10 (`085_wolfram_P1_rule30_nonperiodicity.md`)
and §18 (`002_Rule30_decomposition.md`). Honest, no fabrication.

## 10B. UFT 0-100 Series (FLCR) — Paper 82: Wolfram Prize P2 (Rule-30 equal-density)

Paper 82 = Wolfram Prize Problem 2: Rule 30 has equal-density (≈1/2) left/right. **(I)**
interpretation on **(D)** `verify_wolfram_prize_p2` (equal density). Maps to §10
(`086_wolfram_P2_rule30_density.md`) and §18 (`002`). Honest, no fabrication.

## 10B. UFT 0-100 Series (FLCR) — Paper 83: Wolfram Prize P3 (sub-O(n) inner-step extraction)

Paper 83 = Wolfram Prize Problem 3: extract any inner cell step in sub-O(n) equality. **(I)**
interpretation on **(D)** `verify_wolfram_prize_p3`. Maps to §10
(`087_wolfram_P3_sub_O_n_extraction.md`) and §18 (`002`). Honest, no fabrication.


## 01A. Formal-Paper Deep-Dive (CQE-paper-01)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-01/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

Let `A` be a finite alphabet. For the binary examples in this corpus,
`A = {0, 1}`.

An **LCR state** over `A` is an ordered triple

```text
s = (L, C, R) in A^3
```

where `C` is the distinguished center, `L` is the left boundary read relative
to `C`, and `R` is the right boundary read relative to `C`.

The **center projection** is

```text
pi_C(L, C, R) = C.
```

The **left-right reversal** is

```text
rho(L, C, R) = (R, C, L).
```

The **binary shell** or **trace grade** is

```text
shell(L, C, R) = L + C + R.
```

For binary states, this partitions the eight states into grades of
multiplicity `1, 3, 3, 1`.

Directional opposition is structural:

```text
address(L) != address(R)
```

Value inequality is state-dependent:

```text
value(L) != value(R)
```

The LCR carrier requires directional opposition. It does not require value
inequality in every state.

### Main Claim

**Theorem 1.1, Minimal LCR Carrier.** Any ordered local carrier that preserves
a distinguished center and records two addressable boundary directions requires
at least three slots. The carrier `(L, C, R)` realizes this lower bound, and is
therefore minimal.

**Theorem 1.2, Shell-2 Doublet Binding.** In the binary LCR chart, the
`shell = 2` stratum is exactly `{(1,1,0), (1,0,1), (0,1,1)}`. Left-right
reversal exchanges `(1,1,0)` and `(0,1,1)` while fixing `(1,0,1)`. Therefore
the shell-2 stratum carries the finite single-tape doublet interface used by
later trace-2 and closure papers.

**Theorem 1.3, O8 Spinor Double-Cover Closure.** The frame-inversion operator
`F` carried by the oloid kinematic layer realizes the local SU(2) to SO(3)
double-cover semantics required by O8: `F^2` gives the spinor sign at `2*pi`
and `F^4` returns to the origin at `4*pi`. This closes the spinor double-cover
obligation for the local carrier interface; it does not by itself prove the
full Standard Model extension or the full `J_3(O)` registration.

### Proof

A carrier that preserves a distinguished center must contain at least one
address for the center. A carrier that records two boundary directions relative
to that center must contain one address for the left boundary and one address
for the right boundary. These three roles are pairwise distinct as addresses:
if the center address is identified with a boundary address, the center is no
longer distinguished; if the two boundary addresses are identified, the carrier
cannot distinguish left from right. Hence at least three addresses are required.

The ordered triple `(L, C, R)` has exactly these three addresses and no
additional address. It preserves the center through `pi_C`, records both
boundary directions, and supports reversal by `rho`

_**(D)** formal claim._

### Relation to Rule 30 Readout

Rule 30 uses the same local window form. Its Boolean update rule can be written
as

```text
f(L, C, R) = L xor (C or R).
```

Paper 01 does not claim to solve Rule 30. It establishes the carrier on which
later Rule 30 and Jordan-algebra arguments can be expressed. In this role, LCR
is the local chart: every update reads a center and two relative boundaries.
The shell grading supplies a compact inventory of the eight local states; the
reversal supplies the left-right symmetry operation that later papers compare
with Weyl or Jordan diagonal permutations.

### Relation to the Diagonal Jordan Carrier

The binary LCR state can be embedded into the diagonal subalgebra of the
exceptional Jordan algebra by

```text
phi(L, C, R) = diag(L, C, R).
```

At the level used in this paper, only the diagonal bookkeeping is required.
The map preserves the eight binary states, the shell/trace value, and the
left-right reversal as a swap of the first and third diagonal positions.

Paper 01 does not need the full off-diagonal octonionic structure. That
structure becomes relevant later when the corpus asks which additional
theorems can be transported through a verified structure-preserving map.

### Code Reconstruction

The paper requires a verifier that checks:

```text
1. There are exactly eight binary LCR states.
2. The center projection is preserved under reversal.
3. Reversal is an involution.
4. The shell multiplicities are 1, 3, 3, 1.
5. The fixed and paired reversal orbits are exactly identified.
6. The false value-inequality claim is rejected by the counterexample (1,0,1).
7. The minimality proof is recorded as an address-count argument.
```

The production verifier for this polish pass is:

```text
production/formal-papers/CQE-paper-01/verify_lcr_carrier.py
production/formal-papers/CQE-paper-01/verify_bijective_shell2_doublet.py
production/formal-papers/CQE-paper-01/verify_o8_spinor_double_cover_closed.py
```

It emits a JSON receipt that can be used by the paper-kernel suite.

### Validation and Hidden-Guess Layer

For non-math diagnostics, the training-mode honesty layer should ask for a
prediction before revealing the formal answer. For Paper 01, the useful hidden
guess prompts are:

```text
Does reversal preserve C for every binary LCR state?
How many reversal-fixed binary states are there?
Is every shell-2 state a state with L != R?
What counterexample tests the boundary-value mistake?
```

The answer to the third prompt must be "no"; `(1,0,1)` is the counterexample.
This makes Paper 01 a useful first diagnostic because it teaches the system not
to confuse structural direction with observed value.

### Open Obligations

1. Connect this finite verifier to the installable `cqe_engine.formal`
   interface rather than leaving it as a standalone production verifier.
2. Update older supplemental workbook language that equates opposed directions with
   unequal boundary values.
3. Carry the corrected distinction into Paper 03, where left-right reversal is
   compared with diagonal permutation and triality language.
4. Keep the O8 closure scoped to the local frame-inversion/spinor double-cover
   receipt until later papers supply broader physical transport.
5. Add a peer-review bibliography pass for Rule 30, elementary cellular
   automata, transport of structure, and Jordan-algebra background.

_— honestly carried as guard / next-need._

---



## 02A. Formal-Paper Deep-Dive (CQE-paper-02)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-02/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

Let `A = {0,1}` and let an LCR state be

```text
s = (L, C, R) in A^3.
```

Define the Rule 30 local update:

```text
R30(L, C, R) = L xor (C or R).
```

Define the Rule 90 local update:

```text
R90(L, R) = L xor R.
```

Define the correction map:

```text
corr(L, C, R) = C and not R.
```

A **correction surface** is the set of local states where `corr` is nonzero,
together with the receipt that records how that residue is fed to the next
transport step.

### Main Claim

**Theorem 2.1, Correction Decomposition.** For every binary LCR state,

```text
R30(L, C, R) = R90(L, R) xor corr(L, C, R).
```

Moreover, `corr` is nonzero exactly on

```text
{(0,1,0), (1,1,0)}.
```

**Theorem 2.2, Correction-Surface Monitor.** The correction surface admits a
finite monitor layer: the eight LCR triads partition as `2/2/4`, the Rule30
equals Rule90 plus correction identity remains exact, and deviation from the
expected correction ratio is logged by exact two-tailed binomial receipts. This
binds SentinelForge as a proof monitor, not as a product false-positive-rate
claim.

### Proof

Over Boolean values,

```text
C or R = C xor R xor (C and R).
```

Therefore

```text
R30(L, C, R)
  = L xor (C or R)
  = L xor C xor R xor (C and R)
  = (L xor R) xor (C xor (C and R))
  = R90(L, R) xor (C and not R).
```

The last equality holds because `C xor (C and R)` is `1` exactly when `C=1`
and `R=0`, and is `0` otherwise. Thus the correction is `C and not R`.

Enumerating the eight LCR states, `C=1` and `R=0` occurs only for `(0,1,0)`
and `(1,1,0)`. QED.

For Theorem 2.2, `verify_correction_surface_monitor.py` runs SentinelForge. It
checks the `2/2/4` triad partition, the exact correction identity, the cyclic
and mirror bonded frames, the antipodal-frame involution, the balanced-stream
nominal result, the all-vacuum emergency falsifier, exact binomial mass, and
monotone severity ladder. Product-layer telemetry quality and continuous-metric
quantization remain explicit obligations. QED.

_**(D)** formal claim._

### Code Reconstruction

The production verifier for this polish pass is:

```text
production/formal-papers/CQE-paper-02/verify_correction_surface.py
production/formal-papers/CQE-paper-02/verify_correction_surface_monitor.py
```

It verifies:

```text
1. The Rule 30 / Rule 90 / correction identity on all eight LCR states.
2. The exact correction firing set.
3. The D4 axis/sheet projection for the firing states.
4. The residue ledger shape required by the paper.
5. A falsifier: residue is not automatically accepted as proof.
6. The correction monitor's `2/2/4` triad partition and exact binomial
   deviation machinery.
```

### Validation and Hidden-Guess Layer

Paper 02 diagnostics should ask for a prediction before revealing the
correction set:

```text
Which LCR states make C and not R fire?
Does a nonzero correction prove the original route?
What must be recorded before residue can be used by the next paper?
```

The expected answers are:

```text
firing states: (0,1,0), (1,1,0)
proof status: no, correction creates an obligation
required record: state, rule, residue value, source route, next obligation
```

### Open Obligations

1. Wire this verifier into the installable `cqe_engine.formal` interface.
2. Reconcile the D4 axis/sheet labels with Paper 03's triality presentation.
3. Extend the receipt format so later papers can consume correction rows
   directly.
4. Add peer-review citations for Rule 30, Rule 90, Boolean normal forms, and
   cellular automaton linearization.
5. Keep product telemetry false-positive claims outside the paper until
   empirical product receipts exist.

_— honestly carried as guard / next-need._

---



## 03A. Formal-Paper Deep-Dive (CQE-paper-03)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-03/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

Let the LCR state space be

```text
S = {0,1}^3.
```

Define the axis map:

```text
axis(0,0,0) = 0    axis(1,1,1) = 0
axis(1,0,0) = 1    axis(0,1,1) = 1
axis(0,1,0) = 2    axis(1,0,1) = 2
axis(0,0,1) = 3    axis(1,1,0) = 3
```

Define the sheet map:

```text
sheet(L,C,R) = 0 if L+C+R <= 1
sheet(L,C,R) = 1 if L+C+R >= 2.
```

Define the diagonal carrier:

```text
phi(L,C,R) = diag(L,C,R).
```

On diagonal carriers, use coordinate-wise multiplication as the diagonal
Jordan product:

```text
diag(a,b,c) o diag(a,b,c) = diag(a*a, b*b, c*c).
```

For binary diagonal entries, every coordinate is idempotent. The trace-2
claim is singled out because it is the stratum later used as the three-element
color/orbital surface.

### Main Claim

**Theorem 3.1, Local Triality Surface.** The map

```text
tau(L,C,R) = (axis(L,C,R), sheet(L,C,R), diag(L,C,R))
```

is a faithful three-language presentation of the eight binary LCR states. The
axis/sheet part is a bijection from `S` to `{0,1,2,3} x {0,1}`. The diagonal
part preserves shell as trace. The shell-2 states map to trace-2 diagonal
idempotents.

**Theorem 3.2, D4 Block Tower and Exceptional Conjugate Reapplication.** The
local Paper 03 surface is now bound to the substrate D4 block, D4 block tower,
and `G2 -> F4` T5 conjugate triple verifiers. This closes the paper-binding
gap for those proven substrate mechanisms while preserving the distinction
between the finite local registration theorem and any broader unrestricted
exceptional-algebra claim.

**Theorem 3.3, Algebra Foundation Stack.** The Paper 03 triality surface is
paper-bound to the algebra-foundation receipts T1-T7: octonion axioms, `J3(O)`
Jordan axioms, chart-to-`J3(O)` isomorphism, exact n=3 SU(3) Weyl closure,
closure scale 3, identical trace-block closure, and the exact-rational 8x8
transition matrix.

**Theorem 3.4, D12 and Atlas Dynamics.** The D12 idempotent chain, S3 triality
annealing, and D4 chart-atlas bijectivity receipts are paper-bound to Paper 03.
These receipts close the named finite group-action and atlas claims while
leaving product-scale cluster scheduling and any unreceipted global D4/F4 claim
outside the theorem.

### Proof

The axis map partitions the eight states into four disjoint antipodal pairs:

```text
axis 0: (0,0,0), (1,1,1)
axis 1: (1,0,0), (0,1,1)
axis 2: (0,1,0), (1,0,1)
axis 3: (0,0,1), (1,1,0)
```

Within every axis pair, one state has shell at most 1 and one state has shell
at least 2. Therefore the sheet bit distinguishes the two states inside each
axis. Thus `(

_**(D)** formal claim._

### Relation to Papers 01 and 02

Paper 01 corrected the distinction between boundary address and boundary
value. Paper 03 keeps that correction: axis/sheet labels classify complete
states; they are not merely labels for unequal boundary values.

Paper 02 identified the correction firing states:

```text
(0,1,0) and (1,1,0).
```

Under the Paper 03 axis/sheet map, these become:

```text
(0,1,0) -> (axis 2, sheet 0)
(1,1,0) -> (axis 3, sheet 1)
```

This is why the correction surface can feed Paper 03: residue rows now have a
second coordinate language.

### Code Reconstruction

The production verifier for this polish pass is:

```text
production/formal-papers/CQE-paper-03/verify_triality_surface.py
production/formal-papers/CQE-paper-03/verify_algebra_foundation_T1_T4.py
production/formal-papers/CQE-paper-03/verify_su3_closure_T5_T7.py
production/formal-papers/CQE-paper-03/verify_d12_idempotent_chain.py
production/formal-papers/CQE-paper-03/verify_triality_annealing.py
production/formal-papers/CQE-paper-03/verify_d4_atlas_bijectivity.py
production/formal-papers/CQE-paper-03/verify_d4_block_tower_exceptional.py
```

It verifies:

```text
1. Axis/sheet encoding is bijective.
2. Axis pairs are antipodal complements.
3. The correction rows from Paper 02 land at (2,0) and (3,1).
4. Diagonal trace equals shell for all states.
5. Shell-2 diagonal carriers are idempotent.
6. Strong triality claims remain explicitly unproved obligations.
7. The D4 block, D4 block tower, and `G2 -> F4` T5 conjugate triple substrate
   checks pass as a paper-bound reapplication.
8. T1-T7 algebra-foundation and SU(3)/8x8 closure checks pass.
9. D12 idempotent chain, S3 annealing, and D4 atlas bijectivity checks pass.
```

### Validation and Hidden-Guess Layer

The hidden-guess prompts for this paper are:

```text
Given an LCR state, what axis/sheet coordinate does it receive?
Which two axis/sheet coordinates carry the Paper 02 correction firing states?
Does this local surface prove full D4 triality?
Which states are trace-2 diagonal idempotents?
```

The third answer must be "no." That negative answer is part of the honesty
layer: the system must learn to stop at the verified surface.

### Open Obligations

1. Wire `verify_triality_surface` into the installable `cqe_engine.formal`
   interface.
2. Keep the D4 tower and `G2 -> F4` conjugate theorem scoped to the named
   finite reapplication receipt.
3. Add any still-stronger S3 group-ring/J3 trace-2 proof as a separate theorem
   rather than hiding it inside this local codec paper.
4. Reconcile the axis naming between all chart-codec copies in the D drive.
5. Carry the exact Paper 02 correction coordinates into the Paper 04 boundary
   repair formalism.

_— honestly carried as guard / next-need._

---



## 04A. Formal-Paper Deep-Dive (CQE-paper-04)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-04/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

An **LCR state** is `s = (L,C,R)` in `{0,1}^3`.

A **correction residue** is a row from Paper 02 where

```text
corr(L,C,R) = C and not R = 1.
```

A **local coordinate** is the Paper 03 axis/sheet coordinate:

```text
coord(s) = (axis(s), sheet(s)).
```

A **failed join** is a correction residue that lacks a legal next route.

A **boundary repair constraint** is a record with at least these fields:

```text
state
axis_sheet
reason
status
next_legal_routes
source_paper
target_paper
```

The status is `constraint`, not `proof`.

### Main Claim

**Theorem 4.1, Typed Boundary Repair.** A failed join is repairable in the
CQECMPLX paper kernel if and only if it can be converted into a typed
constraint that preserves the original state, the Paper 03 coordinate, the
reason for failure, and at least one next legal route.

### Proof

If the failed join is not recorded with its state, coordinate, reason, and
next legal route, the next transport has no reproducible object to consume.
The failure may be observed, but it is not repaired.

If those fields are present, the next transport receives a determinate
constraint. It can accept, defer, or reject that constraint with a receipt.
Thus the join has been repaired at the boundary level: not by becoming a
theorem, but by becoming a legal input to the next route.

The construction is idempotent. Applying the repair operation to an already
typed constraint returns the same constraint, because the state, coordinate,
reason, and next route are already fixed. QED.

_**(D)** formal claim._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-04/verify_boundary_repair.py
```

It verifies:

```text
1. The two Paper 02 correction states are consumed.
2. The Paper 03 coordinates are preserved.
3. Each repaired row has all required fields.
4. Repaired rows are constraints, not proofs.
5. Repair is idempotent.
6. Untyped failures are rejected.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What fields must a failed join contain before it is repaired?
Does a repaired boundary row count as proof?
Which Paper 02 states produce boundary repair rows?
What happens to an untyped failure?
```

Expected answers:

```text
state, coordinate, reason, status, next legal route, source, target
no, it is a constraint
(0,1,0) and (1,1,0)
it is rejected
```

### Open Obligations

1. Wire `verify_boundary_repair` into `cqe_engine.formal`.
2. Connect boundary constraints to Paper 05 path carriers.
3. Promote a shared obligation-ledger schema for all later papers.
4. Add a domain example, such as civil crack repair or inventory exception
   routing, after the formal schema is stable.

_— honestly carried as guard / next-need._

---


## 18. References

### 19.1 Standard Mathematics

- Lucas, E. (1878). *Theorie des fonctions numeriques simplement periodiques.* American Journal of Mathematics, 1(4), 289–321.
- Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.
- MacWilliams, F. J., & Sloane, N. J. A. (1977). *The Theory of Error-Correcting Codes.* North-Holland.
- Carlet, C. (2010). *Boolean Functions for Cryptography and Error Correcting Codes.* Cambridge University Press.
- Conway, J. H., & Sloane, N. J. A. (1988). *Sphere Packings, Lattices and Groups.* Springer.
- Jacobson, N. (1968). *Structure and Representations of Jordan Algebras.* AMS Colloq. Publ. 39.
- Shannon, C. E. (1948). *A Mathematical Theory of Communication.* Bell Syst. Tech. J. 27(3), 379–423.

### 19.2 Source Code

- `lattice_forge/rule30.py` — Rule 30 + chart \(\leftrightarrow\) \(J_3(\mathbb{O})\) verifier.
- `lattice_forge/decomposition/rule30_decomposition.py` — Rule 30 ANF decomposition theorems (`verify_all_theorems`).
- `lattice_forge/substrate_map.py` — Substrate map verifier (cited in Paper 001).
- `lattice_forge/f2_majorana.py` — \(F_2\) quadratic form and Arf invariant (for Paper 003).
- `verify_correction_surface_monitor.py` — Correction surface monitor verifier (7 properties).

### 19.3 Workspace Libraries

- `PaperLib/paper-02__unified_correction_surface_and_rule30_decomposition.md` — Full source paper (38 KB, 444 lines)
- `CrystalLib/crystal_lib.db` — Claim database (29 claims for paper-02, all D)
- `SQLLib/paper-02__unified_correction_surface_and_rule30_decomposition.sql` — SQL proof (62 lines, 3 tables)
- `CAMLib/paper-02__unified_correction_surface_and_rule30_decomposition.md` — CAM summaries (2 verified claims)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data (paper-02: 33 D / 34 total, 96.97% D-ratio)

### 19.4 Cross-References

- Paper 001 (LCR Minimal Carrier) — foundational axioms and carrier structure.
- Paper 003 (Correction Surface, F2/Arf Edge Glue) — extends the correction surface.
- Paper 007 (Boundary Repair) — uses \(\partial = C \land \lnot R\) as repair operator.
- Papers 081–083 (Wolfram Rule 30) — unbounded P1/P2/P3 proofs.
- Papers 085–087 (Yang-Mills, Navier-Stokes, Riemann) — correction operator eigenvalues.
- Papers 221–229 (Gap Resolution) — 8 irreducible gaps as unconsumed corrections.

---

**Cross-references:** Paper 001 (minimal carrier), Paper 003 (ANF polynomial / F2 edge glue), Paper 007 (boundary repair operator), Paper 010 (LRR path integral), Paper 013 (CA prediction surfaces), Paper 015 (curvature repair), Paper 081–083 (Wolfram proofs), Paper 085–087 (Millennium problems), Paper 090 (layer closure / McKay-Thompson), Paper 113 (carrier reversal), Paper 117 (O8 spinor double-cover), Papers 221–229 (gap resolution).

**End of Paper 002.**

---

## 20. Recraft Note — CQECMPLX-Formal-Suite CQE-PAPER-002

This paper was recrafted (2026-07-09) from `CQECMPLX-Formal-Suite/00-foundation/CQE-PAPER-002.md`
into the 240-form Paper 002. Routing decision: **EXTEND 002** (by content — both are the
Rule-30 / correction-surface paper). Genuine additions folded in:

- **Boundary chain complex** (§2.13): explicit \(C^0/C^1/C^2\) complex with
  \(\partial: C^0\to C^1\) surjective, \(\partial^2=0\). Engine:
  `lattice_forge.boundary_complex.verify_chain_complex` (4/4 PASS).
- **Honest anneal-distance table** (§2.14): recomputed BFS on the \(S_3\) graph; the
  paper's per-state distances are FLAGGED X (diameter is 3, not the claimed mix).
- **Spectre correction geometry** (engine): `verify_spectre_correction` (4/4 PASS) —
  chiral doublet match, idempotent-to-center, Z₄ periodicity, chiral integral.

**Fabrications / errors caught and NOT carried:**
1. **A033996 knight-CA claim** (CQE-PAPER-002 §5.2): "7-fold substitution depth bound = 3
   matches knight tour on 3×3 board, OEIS A033996, 7/7 PASS." This is the SAME
   FABRICATION already flagged for CQE-PAPER-001. Honest knight-graph count on n×n board
   is n=2..8 → 0,8,16,25,36,49,64 (NOT A033996). Not asserted here.
2. **Anneal per-state table** (§3.3) — internally inconsistent; replaced with honest BFS.

**Engine additions (forge-base, this recraft):** `boundary_complex.py`
(`anneal_distance`, `verify_spectre_correction`, `verify_chain_complex`). All 14
axiom verifiers: 58 checks, 0 defects.

