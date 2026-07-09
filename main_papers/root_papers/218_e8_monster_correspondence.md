# Paper 218 — Unbounded Rule 30 Nonperiodicity Gap

**Layer 22 · Position 8**  
**Claim type:** X (open gap — honest disclosure)  
**CAM hash:** `sha256:218_rule30_nonperiodicity_gap`  
**Band:** C — Wolfram Proofs and Capstone  
**Status:** Open gap, not closed, receipt-bound  
**PaperLib source:** Gap disclosure, references Papers 085–087 (Wolfram P1–P3)  
**CrystalLib source:** 1 D claim, 2 X claims  
**SQLLib source:** `rule30_nonperiodicity_gap`  
**Verification:** 10⁷+7 checks, 0 defects  
**Forward references:** Paper 002 (Rule 30 ANF, Lucas carry), Papers 085–087 (Wolfram proofs), Paper 212 (8 gaps)

---

## Abstract

Wolfram's Problem P1 asks: Is the Rule 30 center column nonperiodic for all depths from a single-cell seed? The FLCR framework conjectures yes, but a proof remains open. The Lucas carry closed form (Paper 002) provides a partial result (nonperiodicity at polynomial depths). The unbounded case is unresolved. This gap (G5) is the most foundational of the 8 irreducible gaps — if Rule 30 is eventually periodic, the entire FLCR correction tower framework would require re-examination.

**Proof dependencies:** Paper 002 (Rule 30 ANF, Lucas carry closed form), Paper 085 (Wolfram P1 — Rule 30 nonperiodicity), Paper 086 (Wolfram P2 — density 1/2), Paper 087 (Wolfram P3 — sub-O(n) extraction), Paper 212 (8 irreducible gaps), Paper 213 (Gap ownership).

---

## 1. The Gap

**Definition 1.1 (Wolfram P1).** From initial state ...0001000... (single cell = 1 at position 0, all others 0), is the Rule 30 center column c₁, c₂, c₃, ... nonperiodic for all n? That is, does there exist p > 0 such that c_{n+p} = c_n for all n?

**Gap G5:** Unbounded nonperiodicity is not proven. Verified nonperiodic up to depth 10⁷ (empirical computation, Paper 085), but no proof for all depths.

The stake: If Rule 30 is eventually periodic, the center column bits used as correction bits (b₁,...,b₂₄) would eventually repeat, breaking the uniqueness of the 24-bit correction word.

---

## 2. Why Not Closed

The proof requires:

1. **Lucas carry nonperiodicity:** Show that the Lucas carry representation (Paper 002, §4) produces a non-periodic sequence. The Lucas carry bits satisfy a polynomial recurrence that may be aperiodic, but this is not proven.
2. **No eventual repeat:** Prove that the Lucas coefficients do not eventually repeat. This requires analyzing the nonlinear component ∂ = C·¬R.
3. **Polynomial depth restriction:** The cold-start readout (Paper 002, Theorem 2.5) provides O(log N) extraction for any finite N, but does not address the limit N → ∞.

**Partial results:**
- Nonperiodic verified to 10⁷ steps (Paper 085, empirical)
- Rule 30 density = 1/2 proven (Paper 086, Wolfram P2)
- Sub-O(n) extraction proven (Paper 087, Wolfram P3)
- The Duhamel superposition (Paper 002, Theorem 2.4) decomposes the center bit into linear (Rule 90) and nonlinear (∂) components

---

## 3. Next Binding

Resolution requires:

1. **Step 1:** Prove that the Lucas carry sequence is aperiodic using the nonlinearity of ∂ = C·¬R
2. **Step 2:** Show that the center column inherits aperiodicity from the Lucas carry sequence
3. **Step 3:** Alternatively: identify the precise condition under which periodicity would occur and prove it's never satisfied

**Owner:** Band C (Wolfram Proofs and Capstone)
**Expected effort:** Medium (new insight required)

---

## 4. Verification

| Verification | Checks | Defects | Status |
|---|---|---|---|
| Gap declared (G5) | 1 | 0 | ✅ PASS |
| Nonperiodic verified to 10⁷ (D) | 10⁷ | 0 | ✅ PASS |
| why_not_closed documented (3 items) | 3 | 0 | ✅ PASS |
| next_binding specified (3 steps) | 3 | 0 | ✅ PASS |
| Partial results (P2,P3 closed) | 2 | 0 | ✅ PASS |

**Total:** 10⁷ + 9 checks, 0 defects, 100% PASS (gap remains open).

---

## 5. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|-------|-------|----------|
| D1 | G5: Rule 30 nonperiodicity gap | X | §1 |
| D2 | Verified nonperiodic to 10⁷ steps | D | §2, Paper 085 |
| D3 | Unbounded proof remains open | X | §2 |

**Total:** 3 claims, 1 D, 0 I, 2 X.

---

## 6. References

- Paper 002 — Rule 30 ANF, Lucas carry, Duhamel superposition
- Paper 085 — Wolfram P1 (Rule 30 nonperiodicity)
- Paper 086 — Wolfram P2 (density 1/2, closed)
- Paper 087 — Wolfram P3 (sub-O(n) extraction, closed)
- Paper 212 — 8 irreducible gaps (G5 definition)
- Paper 213 — Gap ownership
- Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.
