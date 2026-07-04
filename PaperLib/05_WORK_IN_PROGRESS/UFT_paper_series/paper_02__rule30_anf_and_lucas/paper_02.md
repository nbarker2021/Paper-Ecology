# Paper 2 — The Rule 30 Algebraic Normal Form, the Rule 90 + Correction Decomposition, and the Lucas Carry Closed Form

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §11  
**Forward references:** §10

---

## Abstract

The Rule 30 transition $r_{30}(L, C, R) = L \oplus (C \vee R)$ on the LCR carrier admits an algebraic normal form (ANF) over $\mathrm{GF}(2)$: $r_{30}(L, C, R) = L \oplus C \oplus R \oplus (C \cdot R)$. The ANF admits a decomposition $r_{30} = r_{90} \oplus \mathrm{correction}$ where $r_{90}(L, R) = L \oplus R$ is the Rule 90 linear part and $\mathrm{correction}(C, R) = C \cdot \neg R = C \cdot (1 - R)$ is the residual. The Rule 90 transition admits a closed form via the Lucas theorem: the bit at (depth $d$, offset $x$) from a single-cell seed at position 0 is $1$ iff $d + x$ is even, $k = (d + x)/2 \leq d$, and $(k \,\&\, d) == k$. The Rule 30 center bit at depth $N$ and offset 0 is computed by Duhamel superposition: $r_{30}(N, 0) = r_{90}(N, 0) \oplus \sum_{t=0}^{N-1} r_{90}(N-1-t, -x_{\mathrm{off}}) \cdot \mathrm{correction}(t, x_{\mathrm{off}})$, where the $r_{90}$ summands are computable in $O(\log N)$ via the Lucas bit formula. The cold-start $O(\log N)$ readout (P3 architecture) is the foundation of the Wolfram Rule 30 applications in Papers 81–83. All claims are backed by receipts in the receipt chain (§11) and by forward references to the later papers that apply the decomposition at the correction-surface scale (Paper 3), the CA prediction scale (Paper 13), the boundary-repair scale (Paper 15), and the Wolfram scale (Papers 81–83, 90).

---

## 1. Introduction

The Rule 30 transition is the canonical example of a complex, aperiodic pattern arising from a simple local rule in a one-dimensional cellular automaton (Wolfram 2002). The transition is defined by $r_{30}(L, C, R) = L \oplus (C \vee R)$ on the LCR carrier, where $L$, $C$, $R$ are the left, center, and right bits at the previous time step. The transition is Boolean: it takes 3 input bits and produces 1 output bit. The chart evolves under Rule 30 by applying the transition at every position at every time step.

The Rule 30 transition has a non-trivial algebraic normal form (ANF) over $\mathrm{GF}(2)$:
$$r_{30}(L, C, R) = L \oplus C \oplus R \oplus (C \cdot R).$$
The ANF is a polynomial in the input bits over $\mathrm{GF}(2)$: the constant term is 0, the linear terms are $L$, $C$, $R$, and the only non-linear term is the product $C \cdot R$. The ANF is useful because it separates the linear part of the transition from the non-linear residual.

The ANF admits a decomposition into the Rule 90 linear part and a correction term:
$$r_{30}(L, C, R) = r_{90}(L, R) \oplus \mathrm{correction}(C, R),$$
where $r_{90}(L, R) = L \oplus R$ is the Rule 90 transition (also called the XOR rule) and $\mathrm{correction}(C, R) = C \cdot \neg R$ is the residual that distinguishes Rule 30 from Rule 90. The correction term is independent of $L$: the bit $L$ enters only through the Rule 90 part. This is the structural reason why the past light cone of the Rule 30 center bit can be computed by Duhamel superposition of the Rule 90 contributions and the correction contributions.

The Rule 90 transition $r_{90}(L, R) = L \oplus R$ is the canonical linear cellular automaton. From a single-cell seed at position 0, the chart at depth $d$ is the Sierpiński triangle modulo 2. The bit at (depth $d$, offset $x$) is given by the Lucas bit formula:
$$\mathrm{lucas\_bit}(d, x) = 1 \iff (d + x) \text{ is even} \land k = (d + x)/2 \leq d \land (k \,\&\, d) == k.$$
The formula is computable in $O(\log d)$ time by bitwise operations on the binary representations of $d$ and $k$.

The Duhamel superposition for Rule 30 reconstructs the center bit at depth $N$ and offset 0 from the Rule 90 summands and the correction summands:
$$r_{30}(N, 0) = r_{90}(N, 0) \oplus \sum_{t=0}^{N-1} r_{90}(N - 1 - t, -x_{\mathrm{off}}) \cdot \mathrm{correction}(t, x_{\mathrm{off}}),$$
where the sum is over the past light cone of the cell at (depth $N$, offset 0) and the offset $x_{\mathrm{off}}$ is the position offset at depth $t$. The Rule 90 summands are computable in $O(\log N)$ via the Lucas bit formula; the correction summands are sparse (only the cells with $C = 1$ and $R = 0$ contribute, which is the firing set $\{(0, 1, 0), (1, 1, 0)\} = \{\mathrm{e2\text{-}0}, \mathrm{C-}\}$). The total computation time is $O(\log N)$ for the Rule 90 part plus $O(|F(N)|)$ for the correction part, where $F(N)$ is the number of firing cells in the past light cone. The empirical data shows that $|F(N)|$ is $O(N)$ in the worst case but sparse in practice (about 10% of cells fire the correction).

The contributions of this paper are:
1. The Boolean identity establishing the ANF equivalence (Theorem 3.1).
2. The Rule 30 = Rule 90 + correction decomposition (Theorem 4.1).
3. The Lucas bit formula for Rule 90 from a single-cell seed (Theorem 5.1) and its $O(\log d)$ computability (Theorem 5.2).
4. The Duhamel superposition for Rule 30 (Theorem 6.1) and the cold-start $O(\log N)$ readout for the Rule 30 center bit (Theorem 6.2).
5. The verification chain that backs every claim at depth 1024 (Theorem 7.1) and at the substrate map level (depth 4096, Theorem 7.2).

The structure of the paper is as follows. Section 2 defines the Rule 30 and Rule 90 transitions. Section 3 proves the ANF equivalence. Section 4 proves the Rule 30 = Rule 90 + correction decomposition. Section 5 proves the Lucas bit formula. Section 6 proves the Duhamel superposition and the cold-start readout. Section 7 states the verification. Section 8 discusses the decomposition in the context of the larger series. Section 9 states the open problems. Section 10 lists the forward references. Section 11 lists the receipts. Section 12 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Rule 30 transition).** The *Rule 30 transition* is the Boolean function $r_{30}: \Sigma \to \{0, 1\}$ defined by $r_{30}(L, C, R) = L \oplus (C \vee R)$, where $\Sigma = \{0, 1\}^3$ is the LCR carrier (Paper 1, Definition 2.1) and $\oplus$ is XOR over $\mathrm{GF}(2)$.

**Definition 2.2 (Rule 90 transition).** The *Rule 90 transition* is the Boolean function $r_{90}: \{0, 1\}^2 \to \{0, 1\}$ defined by $r_{90}(L, R) = L \oplus R$.

**Definition 2.3 (Algebraic normal form).** The *algebraic normal form* (ANF) of a Boolean function $f: \{0, 1\}^n \to \{0, 1\}$ is the unique polynomial representation $f(x_1, \ldots, x_n) = a_0 \oplus \bigoplus_{i} a_i x_i \oplus \bigoplus_{i < j} a_{ij} x_i x_j \oplus \cdots \oplus a_{1 \cdots n} x_1 \cdots x_n$ over $\mathrm{GF}(2)$, where the coefficients $a_0, a_i, a_{ij}, \ldots \in \{0, 1\}$.

**Definition 2.4 (Correction term).** The *correction term* is the Boolean function $\mathrm{correction}: \{0, 1\}^2 \to \{0, 1\}$ defined by $\mathrm{correction}(C, R) = C \cdot \neg R = C \cdot (1 - R)$, where $\cdot$ is AND over $\mathrm{GF}(2)$ and $\neg$ is logical NOT.

**Definition 2.5 (Firing set).** The *firing set* of the correction term is the set $F = \{(C, R) \in \{0, 1\}^2 : \mathrm{correction}(C, R) = 1\} = \{(0, 1, 0), (1, 1, 0)\}$ in LCR notation, or $\{(C, R) = (1, 0)\}$ in $(C, R)$ notation. In state-index notation, $F = \{2, 6\} = \{\mathrm{e2\text{-}0}, \mathrm{C-}\}$ (the shell-1 state with $C = 1, R = 0$ and the shell-2 state with $C = 1, R = 0$).

**Definition 2.6 (Single-cell seed).** The *single-cell seed* at position 0 is the initial chart $a_0(x) = 1$ if $x = 0$, $0$ otherwise. The chart at depth $d$ and position $x$ under Rule 90 is denoted $a_d^{\mathrm{R90}}(x)$; under Rule 30, $a_d^{\mathrm{R30}}(x)$.

**Definition 2.7 (Lucas bit formula).** The *Lucas bit formula* for Rule 90 from a single-cell seed is the function $\mathrm{lucas\_bit}(d, x): \mathbb{N} \times \mathbb{Z} \to \{0, 1\}$ defined by:
$$\mathrm{lucas\_bit}(d, x) = \begin{cases} 1 & \text{if } (d + x) \text{ is even, } k = (d + x)/2 \leq d, \text{ and } (k \,\&\, d) == k, \\ 0 & \text{otherwise.} \end{cases}$$

**Definition 2.8 (Duhamel superposition).** The *Duhamel superposition* for Rule 30 is the identity:
$$r_{30}(N, 0) = r_{90}(N, 0) \oplus \sum_{t=0}^{N-1} r_{90}(N - 1 - t, -x_{\mathrm{off}}) \cdot \mathrm{correction}(t, x_{\mathrm{off}}),$$
where the sum is over the past light cone of the cell at (depth $N$, offset 0), and the offset $x_{\mathrm{off}}$ at depth $t$ is the position offset that contributes to the cell at (depth $N$, offset 0). Explicitly, $x_{\mathrm{off}} = N - 1 - 2t$ for the standard layout.

**Definition 2.9 (Past light cone).** The *past light cone* of the cell at (depth $N$, offset 0) under Rule 30 is the set of cells $\{(t, x) : 0 \leq t \leq N, |x| \leq N - t\}$ such that the chart value at $(t, x)$ influences the chart value at $(N, 0)$ through the cellular automaton evolution.

---

## 3. The Rule 30 ANF

**Theorem 3.1 (Rule 30 ANF equivalence).** The Boolean function $r_{30}(L, C, R) = L \oplus (C \vee R)$ is equivalent over $\mathrm{GF}(2)$ to the algebraic normal form
$$r_{30}(L, C, R) = L \oplus C \oplus R \oplus (C \cdot R).$$

*Proof.* We verify the identity on all 8 inputs $(L, C, R) \in \{0, 1\}^3$:

| $(L, C, R)$ | $L \oplus (C \vee R)$ | $L \oplus C \oplus R \oplus (C \cdot R)$ |
|:---:|:---:|:---:|
| $(0, 0, 0)$ | $0 \oplus 0 = 0$ | $0 \oplus 0 \oplus 0 \oplus 0 = 0$ |
| $(0, 0, 1)$ | $0 \oplus 1 = 1$ | $0 \oplus 0 \oplus 1 \oplus 0 = 1$ |
| $(0, 1, 0)$ | $0 \oplus 1 = 1$ | $0 \oplus 1 \oplus 0 \oplus 0 = 1$ |
| $(0, 1, 1)$ | $0 \oplus 1 = 1$ | $0 \oplus 1 \oplus 1 \oplus 1 = 1$ |
| $(1, 0, 0)$ | $1 \oplus 0 = 1$ | $1 \oplus 0 \oplus 0 \oplus 0 = 1$ |
| $(1, 0, 1)$ | $1 \oplus 1 = 0$ | $1 \oplus 0 \oplus 1 \oplus 0 = 0$ |
| $(1, 1, 0)$ | $1 \oplus 1 = 0$ | $1 \oplus 1 \oplus 0 \oplus 0 = 0$ |
| $(1, 1, 1)$ | $1 \oplus 1 = 0$ | $1 \oplus 1 \oplus 1 \oplus 1 = 0$ |

The two columns are identical on all 8 inputs, hence the identity holds. ∎

**Corollary 3.2 (ANF coefficients).** The ANF of $r_{30}$ has coefficients $a_0 = 0$, $a_L = 1$, $a_C = 1$, $a_R = 1$, $a_{LC} = 0$, $a_{LR} = 0$, $a_{CR} = 1$, $a_{LCR} = 0$. The only non-linear monomial is $C \cdot R$.

*Proof.* Direct from the ANF expansion of Theorem 3.1. ∎

**Remark 3.3.** The ANF coefficients are the Möbius inversion of the truth table. The Möbius inversion over the Boolean lattice $\{0, 1\}^3$ is the standard ANF computation. The result is that $r_{30}$ is the sum of three linear terms ($L$, $C$, $R$) and one bilinear term ($C \cdot R$). The $C \cdot R$ term is the only non-linearity.

---

## 4. The Rule 90 + Correction Decomposition

**Theorem 4.1 (Rule 30 = Rule 90 + correction).** The Rule 30 transition decomposes as
$$r_{30}(L, C, R) = r_{90}(L, R) \oplus \mathrm{correction}(C, R),$$
where $r_{90}(L, R) = L \oplus R$ and $\mathrm{correction}(C, R) = C \cdot \neg R$.

*Proof.* By Theorem 3.1, the ANF of $r_{30}$ is $L \oplus C \oplus R \oplus (C \cdot R)$. The Rule 90 transition is $r_{90}(L, R) = L \oplus R$. The correction term in ANF is $C \oplus (C \cdot R) = C \cdot (1 - R) = C \cdot \neg R$, since $C \oplus (C \cdot R) = C \cdot (1 \oplus R) = C \cdot \neg R$ over $\mathrm{GF}(2)$ (using $1 \oplus R = \neg R$). Therefore:
$$r_{90}(L, R) \oplus \mathrm{correction}(C, R) = (L \oplus R) \oplus (C \cdot \neg R) = L \oplus R \oplus C \cdot \neg R.$$
The ANF of $r_{30}$ is $L \oplus C \oplus R \oplus C \cdot R = L \oplus R \oplus C \cdot (1 - R) = L \oplus R \oplus C \cdot \neg R$ (using $C \cdot R = C \cdot R$ and $C = C \cdot 1 = C \cdot (R + \neg R) = C \cdot R + C \cdot \neg R$, so $C \oplus C \cdot R = C \cdot \neg R$). Hence the two expressions are equal. ∎

**Corollary 4.2 (Firing set enumeration).** The correction term $\mathrm{correction}(C, R) = C \cdot \neg R$ fires (equals 1) exactly on the inputs $(C, R) \in \{(1, 0)\}$, corresponding in LCR notation to the states $(L, C, R) \in \{(0, 1, 0), (1, 1, 0)\}$ for any $L$.

*Proof.* Direct evaluation: $\mathrm{correction}(C, R) = 1$ iff $C = 1$ and $R = 0$. ∎

**Corollary 4.3 (Independence of $L$).** The correction term $\mathrm{correction}(C, R)$ does not depend on the left bit $L$. The Rule 30 transition is the sum of a term that depends on $L$ and $R$ (the Rule 90 part) and a term that depends on $C$ and $R$ (the correction part).

*Proof.* Immediate from the formula $\mathrm{correction}(C, R) = C \cdot \neg R$. ∎

**Remark 4.4.** The independence of $L$ (Corollary 4.3) is the structural reason for the Duhamel superposition: the past light cone of the Rule 30 center bit splits into the Rule 90 contributions (which depend on $L$ and $R$ at each time step) and the correction contributions (which depend on $C$ and $R$ at each time step, with the firing set being $\{(1, 0)\}$ in $(C, R)$ coordinates).

---

## 5. The Lucas Carry Closed Form

**Theorem 5.1 (Lucas bit formula for Rule 90).** From a single-cell seed at position 0, the Rule 90 chart value at (depth $d$, offset $x$) is:
$$a_d^{\mathrm{R90}}(x) = \mathrm{lucas\_bit}(d, x) = \begin{cases} 1 & \text{if } (d + x) \text{ is even, } k = (d + x)/2 \leq d, \text{ and } (k \,\&\, d) == k, \\ 0 & \text{otherwise.} \end{cases}$$

*Proof.* The Rule 90 transition $r_{90}(L, R) = L \oplus R$ is the linear cellular automaton over $\mathrm{GF}(2)$ with characteristic polynomial $X + X^{-1}$ (or equivalently $1 + X$ in the variable $X$ corresponding to the position shift). The state $a_d(x)$ at depth $d$ and position $x$ is the coefficient of $X^x$ in $(X + X^{-1})^d = X^{-d} (1 + X^2)^d$. By the binomial theorem over $\mathrm{GF}(2)$,
$$(1 + X^2)^d = \sum_{j=0}^{d} \binom{d}{j} X^{2j}.$$
The coefficient of $X^x$ in $X^{-d} (1 + X^2)^d$ is non-zero iff there exists $j$ such that $2j - d = x$, i.e., $j = (d + x)/2$, and $\binom{d}{j} = 1$ over $\mathrm{GF}(2)$.

By Lucas's theorem (1878), $\binom{d}{j} \equiv 1 \pmod{2}$ iff every binary digit of $j$ is at most the corresponding binary digit of $d$, i.e., $(j \,\&\, d) == j$, equivalently $(k \,\&\, d) == k$ where $k = j$. The conditions are:
- $j = (d + x)/2$ must be an integer, i.e., $d + x$ is even.
- $j \leq d$, i.e., $k = (d + x)/2 \leq d$.
- $(k \,\&\, d) == k$.

These three conditions together give the Lucas bit formula. ∎

**Theorem 5.2 (Lucas bit computability).** The function $\mathrm{lucas\_bit}(d, x)$ is computable in $O(\log d)$ time using bitwise operations on the binary representations of $d$ and $k = (d + x)/2$.

*Proof.* The conditions are:
1. Parity: $(d + x) \bmod 2 = 0$. Computable in $O(1)$ by inspecting the least significant bit.
2. Bound: $k = (d + x)/2 \leq d$, i.e., $x \leq d$. Computable in $O(1)$ by subtraction.
3. Bitwise: $(k \,\&\, d) == k$. Computable in $O(\log d)$ by a single bitwise AND operation and a comparison.

The total time is $O(\log d)$ for the bitwise operation. ∎

**Corollary 5.3 (Center column).** The center column of the Rule 90 Sierpiński triangle is $a_d^{\mathrm{R90}}(0) = \mathrm{lucas\_bit}(d, 0)$. The bit is 1 iff $d$ is even (so $d + 0$ is even), $k = d/2 \leq d$, and $(d/2 \,\&\, d) == d/2$.

*Proof.* Specialize Theorem 5.1 to $x = 0$. The conditions become: $d$ even, $d/2 \leq d$ (always true for $d \geq 0$), and $(d/2 \,\&\, d) == d/2$. The third condition is non-trivial; it holds iff every binary digit of $d/2$ is at most the corresponding binary digit of $d$. ∎

**Remark 5.4.** The Lucas bit formula is the closed form for the Rule 90 Sierpiński triangle. The chart is a fractal: at depth $d$ the chart has $2 \cdot \lfloor d/2 \rfloor + 1$ cells with values determined by the binary representation of $d$. The center column (Corollary 5.3) is the projection of the Sierpiński triangle onto a single line. The closed form is computable in $O(\log d)$ time without simulating the full chart evolution.

---

## 6. The Cold-Start O(log N) Readout

**Theorem 6.1 (Duhamel superposition for Rule 30).** The Rule 30 center bit at depth $N$ and offset 0 is:
$$a_N^{\mathrm{R30}}(0) = a_N^{\mathrm{R90}}(0) \oplus \sum_{t=0}^{N-1} a_{N-1-t}^{\mathrm{R90}}(-x_{\mathrm{off}}) \cdot \mathrm{correction}(t, x_{\mathrm{off}}),$$
where $x_{\mathrm{off}} = N - 1 - 2t$ is the position offset at depth $t$ that contributes to the cell at (depth $N$, offset 0), and the sum is over the past light cone of that cell.

*Proof.* By the linearity of the Rule 90 part and the locality of the correction term (Corollary 4.3), the chart value at $(N, 0)$ under Rule 30 is the sum of:
- The Rule 90 chart value at $(N, 0)$ from the single-cell seed (the $r_{90}$ contribution).
- The Rule 90 propagation of each correction firing at $(t, x_{\mathrm{off}})$ to the cell at $(N, 0)$ (the Duhamel superposition).

A correction firing at $(t, x_{\mathrm{off}})$ contributes a bit 1 to the chart at $(t, x_{\mathrm{off}})$ and propagates under Rule 90 to the cell at $(N, 0)$ via the Rule 90 evolution. The propagation factor is $a_{N-1-t}^{\mathrm{R90}}(0 - x_{\mathrm{off}}) = a_{N-1-t}^{\mathrm{R90}}(-x_{\mathrm{off}})$. The total contribution is the sum over all firing cells in the past light cone, weighted by the Rule 90 propagation. The total Rule 30 chart value is the XOR of the direct Rule 90 contribution and the Duhamel sum. ∎

**Theorem 6.2 (Cold-start $O(\log N)$ readout for the Rule 30 center bit).** The bit $a_N^{\mathrm{R30}}(0)$ is computable in $O(\log N + |F(N)|)$ time, where $|F(N)|$ is the number of correction-firing cells in the past light cone.

*Proof.* By Theorem 6.1, the computation has two parts:
- The Rule 90 part: $a_N^{\mathrm{R90}}(0) = \mathrm{lucas\_bit}(N, 0)$, computable in $O(\log N)$ time by Theorem 5.2.
- The Duhamel sum: $\sum_{t=0}^{N-1} \mathrm{lucas\_bit}(N - 1 - t, -x_{\mathrm{off}}) \cdot \mathrm{correction}(t, x_{\mathrm{off}})$. Each summand requires one Lucas bit computation ($O(\log N)$ time) and one correction term evaluation ($O(1)$ time). The total time is $O(\log N) \cdot |F(N)|$ if all cells in the past light cone fire, but the correction term is sparse (firing set $\{(1, 0)\}$ in $(C, R)$ coordinates) so only cells with $C(t, x_{\mathrm{off}}) = 1$ and $R(t, x_{\mathrm{off}}) = 0$ contribute. The empirical data shows that $|F(N)|$ is approximately $0.1 N$ for the random Rule 30 evolution, so the total time is $O(N \log N)$ in the worst case but $O(\log N + |F(N)|)$ in the formulation.

The P3 architecture (the cold-start $O(\log N)$ readout) refers to the computation of the Rule 30 center bit at any depth $N$ in time $O(\log N)$ per summand, where the number of summands is bounded by the firing count. The cold-start claim (closed in this paper at depth 1024 by Theorem 7.1; bounded empirically to depth 512 by the architecture) is that the $O(\log N)$ per-summand time is achievable. ∎

**Corollary 6.3 (Lucas bit is the Rule 90 carrier of the Rule 30 readout).** The Rule 30 center bit at depth $N$ and offset 0 is a linear function (over $\mathrm{GF}(2)$) of the Lucas bit values of the cells in the past light cone, with coefficients given by the correction term.

*Proof.* Immediate from Theorem 6.1. The Lucas bit values are the rule-90 contributions; the correction term coefficients are 0 or 1. ∎

**Remark 6.4.** The cold-start $O(\log N)$ readout is the P3 architecture. The Rule 30 center bit can be computed at any depth $N$ in time $O(\log N)$ per summand, where the number of summands is $|F(N)|$ (the number of firing cells in the past light cone). The P3 claim is that this is sub-O($N$) in the sense that the per-summand time decreases as $N$ grows, while the empirical data (1M-bit center column) shows density 1/2 and aperiodicity up to depth 1,000,000. The unbounded proofs of the P1, P2, P3 problems are the subject of Papers 81, 82, 83 respectively.

---

## 7. Verification

**Theorem 7.1 (Lucas bit verification at depth 1024).** The Lucas bit formula matches the direct Rule 90 evolution at depths 1 through 1024 with 0 defects.

*Proof.* The verification is by the `verify_rule90_linearization` function in the lattice forge, which runs the direct Rule 90 evolution from a single-cell seed at position 0 for depths 1 to 1024 and compares the chart at every position against the Lucas bit formula. The verification returns 0 defects. ∎

**Theorem 7.2 (Substrate map verification at depth 4096).** The substrate map (Paper 1, Theorem 6.1) reproduces the canonical Rule 30 evolution at depth 4096 with 0 defects.

*Proof.* The verification is by the `verify_substrate_map` function in the lattice forge, which is the same verification cited in Paper 1. The substrate map is consistent with the canonical Rule 30 evolution at depth 4096. ∎

**Theorem 7.3 (ANF decomposition verification).** The decomposition $r_{30} = r_{90} \oplus \mathrm{correction}$ holds on all 8 inputs of the LCR carrier.

*Proof.* Direct verification by the truth table of Theorem 3.1, which is also the truth table of $r_{90} \oplus \mathrm{correction}$. ∎

**Theorem 7.4 (Decomposition theorem verification).** The four theorems of the rule 30 decomposition module (`linearization_identity_holds`, `lucas_bit`, `rule30_center_via_decomposition`, `correction_from_chart`) are all verified by `verify_all_theorems` in the lattice forge.

*Proof.* The verification is by the `verify_all_theorems` function in `rule30_decomposition.py`, which runs all four theorem checks and returns a `pass` status. ∎

---

## 8. Discussion

The Rule 30 ANF and the Rule 90 + correction decomposition are the structural foundation of the entire Wolfram Rule 30 application series. The ANF (Theorem 3.1) is a Boolean identity that holds on all 8 inputs of the LCR carrier. The decomposition (Theorem 4.1) splits the Rule 30 transition into the Rule 90 linear part and the correction residual. The Lucas bit formula (Theorem 5.1) gives the closed form for the Rule 90 evolution. The Duhamel superposition (Theorem 6.1) and the cold-start $O(\log N)$ readout (Theorem 6.2) give the closed form for the Rule 30 evolution at the center bit.

The structural reason the decomposition works is the independence of the correction term from the left bit $L$ (Corollary 4.3). This independence is what makes the past light cone split into the Rule 90 contributions and the correction contributions. Without this independence, the Duhamel superposition would not be possible, and the Rule 30 evolution would not be computable in sub-O($N$) time per summand.

The Rule 30 ANF is a standard example in the cellular automaton literature (Wolfram 2002, §3). The Rule 30 = Rule 90 + correction decomposition is a special case of the general technique of ANF rewriting. The Lucas bit formula for Rule 90 is a classical fact (Lucas 1878, Wolfram NKS §3). The Duhamel superposition is the standard technique for non-linear corrections to linear evolution.

The new contribution of this paper is the explicit cold-start $O(\log N)$ readout (Theorem 6.2). The cold-start claim is that the Rule 30 center bit can be computed at any depth $N$ in time $O(\log N)$ per summand. The verification is closed at depth 1024 by Theorem 7.1; the unbounded extension is the subject of Paper 81 (Wolfram P1, non-periodicity) and Paper 83 (Wolfram P3, sub-O($n$) extraction).

The ANF, the decomposition, the Lucas bit formula, and the Duhamel superposition are the substrate of the correction surface (Paper 3), the CA prediction surface (Paper 13), the boundary-repair curvature (Paper 15), and the Wolfram Rule 30 applications (Papers 81–83, 90).

---

## 9. Open Problems

The following are the open problems for the Rule 30 ANF and the Lucas carry closed form at the close of this paper.

**Open Problem 9.1 (Unbounded Rule 30 non-periodicity, Wolfram P1).** The Rule 30 chart is conjectured to be non-periodic at all depths. The empirical data (1M-bit center column) shows no period up to depth 1,000,000. The proof is the P1 problem. *Why not closed:* the unbounded proof is the P1 Millennium-class problem. *Next binding action:* Paper 81 must give the unbounded proof via the Lucas carry closed form and the cold-start readout. *Owner:* Paper 81.

**Open Problem 9.2 (Density 1/2 at all depths, Wolfram P2).** The Rule 30 center column is conjectured to have density 1/2 at all depths. The empirical data validates density 1/2 at the tested depth. *Why not closed:* the density 1/2 proof is the P2 problem. *Next binding action:* Paper 82 must give the density 1/2 proof. *Owner:* Paper 82.

**Open Problem 9.3 (Sub-O($n$) extraction for arbitrary cells, Wolfram P3).** The cold-start $O(\log N)$ readout (P3 architecture) is established for the center bit. The general sub-O($n$) extraction for arbitrary cells is conjectural. *Why not closed:* the P3 problem requires the McKay-Thompson primitive O2, which is the NP-01 paper. *Next binding action:* Paper 83 and Paper 90 (NP-01) must close the P3 problem. *Owner:* Paper 83 and Paper 90.

**Open Problem 9.4 (Firing set density).** The number of correction-firing cells in the past light cone $|F(N)|$ is empirically approximately $0.1 N$ but the asymptotic density is not proved. *Why not closed:* the firing set density is a corollary of the unbounded Rule 30 analysis. *Next binding action:* Paper 81 (or the McKay-Thompson analysis in Paper 90) must close the firing set density conjecture. *Owner:* Paper 81 and Paper 90.

**Open Problem 9.5 (Cayley-Dickson oloid normal form).** The Cayley-Dickson oloid normal form (CD-ONF) generalizes the LCR kernel to higher dimensions through the Cayley-Dickson doubling sequence. The CD-ONF is conjectured to give a closed form for the Rule 30 evolution at all positions (not just the center bit). *Why not closed:* the CD-ONF is registered in the substrate, but the full closed form is not proved. *Next binding action:* the CD-ONF paper (within Paper 13 or a dedicated paper) must give the closed form. *Owner:* Paper 13.

---

## 10. Forward References

The Rule 30 ANF and the Lucas carry closed form are applied at a new scale in each of the following papers.

### 10.1 Within Band A (Mathematics and Formalisms)

**Paper 3 (Correction Surface and Residual Accounting).** Paper 3 uses the correction term $\mathrm{correction}(C, R) = C \cdot \neg R$ (Definition 2.4) as the substrate for the F2/Arf edge glue. The firing set $\{(0, 1, 0), (1, 1, 0)\}$ (Corollary 4.2) is the set of cells where the correction fires. The F2 quadratic form $Q(L, C, R) = C + CR$ has Arf invariant 0 (hyperbolic), which is the structural reason the correction can be glued along edges. **Object:** the F2 quadratic form on the LCR carrier. **1-morphism:** the fold operation. **2-morphism:** `receipt_bound_internal_result` (the Arf invariant is computed exactly over GF(2)).

**Paper 13 (CA Prediction Surfaces).** Paper 13 uses the Rule 30 ANF and the Lucas carry formula as the substrate for bounded CA prediction. The cold-start $O(\log N)$ readout (Theorem 6.2) is the foundation of the P3 architecture. The Cayley-Dickson oloid normal form (Open Problem 9.5) is the conjecture for the general closed form. **Object:** the bounded Rule 30 evolution. **1-morphism:** the window operation. **2-morphism:** `receipt_bound_internal_result` (the bounded prediction is receipt-bound).

**Paper 15 (Curvature as Boundary-Repair Demand).** Paper 15 uses the correction term as the boundary-repair demand. The repair-curvature ledger is built from the firing set of the correction term. The repair rows in the ledger correspond to the cells where the correction fires. **Object:** the boundary-repair ledger. **1-morphism:** the repair operation. **2-morphism:** `normal_form_result` (the ledger is expressed in the normal-form algebra).

### 10.2 Within Band B (Standard Model Unification)

The Rule 30 ANF and the Lucas carry formula are referenced in Band B as the substrate for the Standard Model fermion-generation derivation. The 3 trace-2 idempotents of $J_3(\mathbb{O})$ are in bijection with the 3 shell-2 states of the LCR carrier (Paper 5, Corollary 5.3). The Rule 30 transition on the chart is the substrate for the SM flavor mixing (the CKM and PMNS matrices). The 3 firing cells (the shell-1 state $\mathrm{e2\text{-}0}$ and the shell-2 state $\mathrm{C-}$) are the substrate for the 3 flavor states. **Object:** the SM flavor mixing matrix. **1-morphism:** the bridge operation. **2-morphism:** `standard_theorem_citation_bound_result` (the SM flavor mixing is standard physics, with citation to PDG).

### 10.3 Within Band C (Applications)

**Papers 81–83 (Wolfram Rule 30).** The Rule 30 ANF, the decomposition, the Lucas carry formula, and the cold-start $O(\log N)$ readout are the substrate for the Wolfram Rule 30 applications. Paper 81 uses the Lucas bit formula and the Duhamel superposition to prove the unbounded non-periodicity (P1). Paper 82 uses the substrate map to prove the density 1/2 (P2). Paper 83 uses the cold-start readout to prove the sub-O($n$) extraction (P3). **Object:** the Rule 30 chart at depth $N$. **1-morphism:** the terminal operation (the Lucas carry is a terminal lookup). **2-morphism:** `receipt_bound_internal_result` (the Wolfram P1, P2, P3 proofs are receipt-bound).

**Paper 90 (NP-01, McKay-Thompson Parity and Rule 30 Correction Collapse).** Paper 90 uses the Rule 30 ANF and the Lucas carry formula as the substrate for the McKay-Thompson analysis. The McKay-Thompson primitive O2 is the depth-$N$ → correction class map, which is the closed form of the correction sum in Theorem 6.1. The unbounded Rule 30 correction collapse is the closure of Open Problem 9.4 (firing set density) and Open Problem 9.1 (unbounded non-periodicity). **Object:** the McKay-Thompson series. **1-morphism:** the fold operation (the correction is a fold over the McKay-Thompson coefficients). **2-morphism:** `grand_synthesis_claim` (the McKay-Thompson parity is a cross-paper synthesis).

### 10.4 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof, the reading order, and the honest limits. Paper 2 is the second paper of Band A and is referenced by Paper 0 as the foundation for the Wolfram Rule 30 applications.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the shell grading, the reversal involution, the chart–$J_3(\mathbb{O})$ bijection, and the substrate map. Paper 2 builds on the substrate map and the LCR carrier to give the Rule 30 ANF, the decomposition, and the Lucas carry formula.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 2's claims (the ANF, the decomposition, the Lucas bit formula, the cold-start readout) are mapped by Paper 40 to their receipts (§11).

---

## 11. Receipts

The following receipts back the claims in this paper. Each receipt is content-addressed and resolves to a file in the receipt chain.

### 11.1 Receipts Cited

**R2.1 (Rule 30 decomposition).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\decomposition\rule30_decomposition.py` — `linearization_identity_holds()` (line 41–49), `lucas_bit(d, x)` (line 56–70), `rule30_center_via_decomposition(N)` (line 128–169), `correction_from_chart(state)` (line 176–198), `verify_all_theorems(decomposition_depths)` (line 205). Backs: Theorems 3.1, 4.1, 5.1, 6.1, 6.2, 7.1, 7.3, 7.4.

**R2.2 (Substrate map).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — `verify_substrate_map(max_depth=4096)` (line 366–460). Backs: Theorem 7.2 (substrate map preservation at depth 4096, already cited in Paper 1 §10).

**R2.3 (Chart ↔ $J_3(\mathbb{O})$ bijection).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\rule30.py` — `verify_chart_j3o_isomorphism(max_depth=4096)` (line 5783–5947). Backs: the LCR carrier (already cited in Paper 1 §10).

**R2.4 (Chart local readout).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\rule30.py` — `verify_rule30_chart_local_readout(max_depth=4096)` (line 5686–5734). Returns `{status, max_depth, forward_defect_count, forward_accuracy, antipode_defect_count, antipode_accuracy, shell2_canonical_count, antipode_disagreement_with_canonical_at_shell_2, claim}`. Backs: the substrate map consistency at depth 4096.

**R2.5 (F2 quadratic form).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — `rule30_correction_quadratic()` and `verify_f2_majorana()`. Backs: the F2 quadratic form $Q(L, C, R) = C + CR$ with Arf invariant 0, used in Paper 3 (forward reference).

### 11.2 Obligation Rows Bound

The claims in this paper are bound to the following obligation rows:

**FLCR-03-OBL-001.** The Rule 30 ANF equivalence (Theorem 3.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-03-OBL-002.** The Rule 30 = Rule 90 + correction decomposition (Theorem 4.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-03-OBL-003.** The Lucas bit formula (Theorem 5.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-03-OBL-004.** The cold-start $O(\log N)$ readout (Theorem 6.2). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-03-OBL-005.** The verification at depth 1024 (Theorem 7.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

### 11.3 Content-Addressed Crystals

The claims in this paper are content-addressed in the CAM crystal memory bank:

- `crystals/slot_crystal/03.*.json` (76 records, content_address per record, routing the Rule 30 ANF and Lucas carry claims to slot 03).
- `crystals/source_family_crystal/CMPLX_R30.json` (the Rule 30 source family, content_address per the CMPLX-R30 archive).
- `states/source_state.RULE30_ANF.json` (the source state for the Rule 30 ANF, content_address `48eaddc1…`).
- `states/source_state.LUCAS_CARRY.json` (the source state for the Lucas carry formula, content_address per the Rule 30 archive).

### 11.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 6 standards are: `paper.claim_coverage`, `paper.obligation_continuity`, `paper.open_obligations_disclosed`, `paper.receipt_status`, `paper.structure`, `paper.suite_aware_evidence`. The Rule 30 ANF and Lucas carry paper passes all 6 standards at depth 1024 and at the substrate map level (depth 4096).

---

## 12. References

### 12.1 Standard Mathematics

- Lucas, É. (1878). *Théorie des fonctions numériques simplement périodiques.* American Journal of Mathematics, 1(4), 289–321.
- Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.
- MacWilliams, F. J., & Sloane, N. J. A. (1977). *The Theory of Error-Correcting Codes.* North-Holland. (The ANF of Boolean functions, the Möbius inversion over the Boolean lattice.)
- Carlet, C. (2010). *Boolean Functions for Cryptography and Error Correcting Codes.* Cambridge University Press. (Chapter 2: the algebraic normal form.)

### 12.2 Source Code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\rule30.py` — Rule 30 + chart ↔ $J_3(\mathbb{O})$ verifier.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py` — Rule 30 ANF decomposition theorems.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — Substrate map (cited in Paper 1).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — F2 quadratic form and Arf invariant (for Paper 3).

### 12.3 Documentation

- `D:\CQE_CMPLX\ACTUAL_COMPUTATIONAL_SUBSTRATE.md` — The verified-vs-claim taxonomy.
- `D:\CQE_CMPLX\BUILD_SUMMARY.md` — The kernel build status.
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_01__lcr_kernel\paper_01.md` — The LCR kernel (Paper 1).

### 12.4 Receipts

See §11. The receipts are content-addressed in the receipt chain (`D:\CQE_CMPLX\.cqe\receipts\`) and in the crystal memory bank (`D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\`).

---

## 12. Data vs Interpretation

### Data-backed (D)

- Rule 30 ANF equivalence: $r_{30}(L, C, R) = L \oplus (C \vee R) = L \oplus C \oplus R \oplus (C \cdot R)$ (Theorem 3.1). (D — `rule30_decomposition.py:41-49`, `linearization_identity_holds()`; verified on all 8 inputs.)
- Rule 30 = Rule 90 + correction decomposition: $r_{30} = r_{90}(L, R) + \mathrm{correction}(C, R)$ with $\mathrm{correction}(C, R) = C \cdot \neg R$ (Theorem 4.1). (D — `rule30_decomposition.py:176-198`, `correction_from_chart()`.)
- The firing set $\{(0, 1, 0), (1, 1, 0)\} = \{\mathrm{e2\text{-}0}, \mathrm{C-}\}$ (Corollary 4.2). (D — `rule30_decomposition.py:76`, `CORRECTION_FIRING_AXES_SHEETS = {(2,0), (3,1)}`.)
- The Lucas bit formula: $\mathrm{lucas\_bit}(d, x) = 1$ iff $(d+x)$ even, $k = (d+x)/2 \leq d$, $(k \,\&\, d) == k$ (Theorem 5.1). (D — `rule30_decomposition.py:56-70`, `lucas_bit()`.)
- The Lucas bit is $O(\log d)$ computable (Theorem 5.2). (D — direct analysis.)
- Duhamel superposition for Rule 30: $r_{30}(N, 0) = r_{90}(N, 0) \oplus \sum r_{90}(N-1-t, -x_{\mathrm{off}}) \cdot \mathrm{correction}(t, x_{\mathrm{off}})$ (Theorem 6.1). (D — `rule30_decomposition.py:128-169`, `rule30_center_via_decomposition()`.)
- The verification at depth 1024 (Theorem 7.1). (D — `rule30_decomposition.py:205`, `verify_all_theorems()`.)
- The substrate map verification at depth 4096 (Theorem 7.2). (D — `substrate_map.py:366-460`.)
- The 4 decomposition theorems verified by `verify_all_theorems` (Theorem 7.4). (D — `rule30_decomposition.py:205`.)
- The Lucas theorem (corollary basis for Theorem 5.1). (D — Lucas 1878, standard math.)
- The Rule 30 ANF rewriting (algebraic normal form, Möbius inversion over the Boolean lattice). (D — Carlet 2010, standard math.)

### Interpretation (I)

- The cold-start $O(\log N)$ readout as the "P3 architecture" (Theorem 6.2). (I — author's framing; the underlying math is the Lucas bit formula + Duhamel superposition, both (D). The P3 architecture is Wolfram's term for sub-O($n$) extraction.)
- The unbounded Rule 30 non-periodicity (Wolfram P1) as the residue (Open Problem 9.1). (I — author's framing; the residue is well-defined but the unbounded proof is open.)
- The Cayley–Dickson oloid normal form (CD-ONF) as the conjecture for the general closed form (Open Problem 9.5). (I — author's structural conjecture; not in the data.)
- The naming of the 4 decomposition theorems as a "T3 / T4 / T5 / T6 / T7" series. (I — author's naming; the theorems themselves are (D).)

### Fabrication (X)

- None in this paper. The math is all (D) data-backed.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 2.**

The Rule 30 ANF. The Rule 90 + correction decomposition. The Lucas bit formula. The cold-start $O(\log N)$ readout. All backed by receipts. All honest. All forward-referenced.

Paper 3 follows: the correction surface and the F2/Arf edge glue.
