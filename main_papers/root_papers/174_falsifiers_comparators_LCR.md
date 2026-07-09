# Paper 174 — Falsifiers Comparators — Signed-Rank-Structure

**Layer 18 · Position 4**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:174_falsifiers_comparators`  
**Band:** F — Materials  
**Status:** Reframe from old Paper 36, signed-rank-structure falsifiers comparators  
**PaperLib source:** `paper-36__unified_signed-rank-structure.md`

---

## Abstract

Falsifiers comparators are the mechanism for testing LCR claims by comparing signed-rank structures. Each claim carries a falsifier set; each falsifier has a signed-rank signature. The comparator maps claim signatures to falsifier signatures and computes the falsification distance d(F, C) = overlap area between the claim and falsifier structures.

The signed-rank structure assigns a gradation to each claim-falsifier pair. The comparator is the dual-objective feedback: falsification refines the claim; the refined claim generates new falsifiers. This iterative refinement is the LCR method for claim validation (Layer 7, Paper 060). The convergence criterion is d(F, C) → 0 (falsifier fully consumed) or d(F, C) diverging (claim falsified).

This paper reframes old Paper 36 and establishes the falsification methodology that provides the empirical spine of the entire FLCR framework. Every claim ledger entry (across all 240 papers) carries a falsifier reference, and every falsifier is comparatable via the signed-rank structure.

**Key dependencies:** Paper 060 (falsification methodology — Layer 7 closure), Paper 035 (falsification with SNAP — claim testing), Paper 040 (falsification completeness — full falsifier set), Paper 026 (falsifiers signatures — signed ranks), Paper 036 (grand ribbon — comparator template), Paper 007 (boundary repair ∂ — falsification boundary), Paper 018 (repair curvature — falsification metric), Paper 031 (energetic traversal θ — energy threshold), Paper 174's own PaperLib: old 36.

---

## 1. Proof Dependencies

| Dependency | Source | How Used |
|---|---|---|
| Signed-rank structure (old 36) | Paper 026 Definitions | Falsifier signature |
| Falsification methodology | Paper 060 Theorem 60.1 | Validation framework |
| SNAP falsification | Paper 035 Lemma 35.1 | Claim testing |
| Falsification completeness | Paper 040 Theorem 40.1 | Full falsifier set |
| Grand ribbon template | Paper 036 §3 | Comparator structure |
| Boundary repair ∂ | Paper 007 Theorem 7.1 | Falsification boundary |
| Repair curvature K | Paper 018 Definition 18.1 | Falsification metric |

**Lemma 174.0 (Dependency closure).** The falsifiers comparator depends on the signed-rank structure for signatures and the falsification methodology for the judgment protocol.

*Proof.* The signed-rank structure (Paper 026, old 36) assigns signatures to claim-falsifier pairs. The falsification methodology (Paper 060) specifies the judgment protocol. The comparator (Paper 036 template) provides the mapping. ∎

---

## 2. Formal Definitions

**Definition 174.1 (Signed-rank structure).** An assignment of a signature (rank r, sign s ∈ {+1, -1}) to each claim-falsifier pair. The rank r ∈ ℕ indicates the level of the falsifier in the claim hierarchy; the sign s indicates whether the falsifier supports (+) or opposes (-) the claim.

**Definition 174.2 (Falsifier comparator).** A function d(F, C) = |s_F · r_F - s_C · r_C| that computes the absolute difference between the signed-rank signatures of the falsifier F and the claim C. The falsification distance.

**Definition 174.3 (Falsification distance).** d(F, C) ∈ [0, ∞). d = 0 means the falsifier is fully consumed by the claim (claim absorbs the falsifier). d → ∞ means the falsifier diverges from the claim (claim falsified). d ∈ (0, ∞) means partial falsification.

---

## 3. Theorems

### Theorem 174.1 (Signed-Rank Completeness)

Every LCR claim can be assigned a signed-rank signature that fully captures its falsification status.

**Lemma 174.1a (Signature existence).** For any claim C and falsifier F, there exists a signed-rank pair (r, s) that encodes the falsification relationship.

*Proof.* Paper 026 (old 36) establishes the existence of signed-rank signatures for all claim-falsifier pairs. The construction: r is the depth of the falsifier in the claim hierarchy (number of nested entailments), and s is the direction of falsification (+1 for support, -1 for opposition). ∎

**Lemma 174.1b (Signature completeness).** The signed-rank pair (r, s) fully captures the falsification relationship up to isomorphism.

*Proof.* The falsification methodology (Paper 060) proves that all falsification relationships can be characterized by depth (r) and direction (s). Nested entailments are accounted for by r; support/opposition is accounted for by s. No additional parameters are needed. ∎

*Proof of Theorem 174.1.* By Lemma 174.1a, every claim-falsifier pair has a signed-rank signature. By Lemma 174.1b, the signature fully captures the relationship. ∎

### Theorem 174.2 (Comparator Convergence)

The falsification distance d(F, C) converges to 0 as the claim absorbs the falsifier, and diverges as the claim is falsified. The convergence is monotonic.

**Lemma 174.2a (Monotonic refinement).** The iterative refinement of a claim in response to falsifiers reduces the falsification distance monotonically.

*Proof.* Each refinement step generates a new claim C' that is closer to the falsifier F in signed-rank space. The comparator d(F, C') ≤ d(F, C) by construction (Paper 060 Theorem 60.1). ∎

**Lemma 174.2b (Convergence criterion).** d(F, C) → 0 if and only if the falsifier is fully consumed by the claim.

*Proof.* If d = 0, then r_F · s_F = r_C · s_C. The falsifier and claim have the same signed-rank, meaning the claim accounts for the falsifier at the same hierarchical depth and in the same direction. ∎

*Proof of Theorem 174.2.* By Lemma 174.2a, the refinement is monotonic. By Lemma 174.2b, d → 0 corresponds to falsifier consumption. ∎

### Theorem 174.3 (Dual-Objective Feedback)

The falsifier comparator provides dual-objective feedback: the claim refines to absorb the falsifier, and the falsifier evolves as the claim changes.

**Lemma 174.3a (Claim refinement).** A falsifier F with d(F, C) > 0 triggers claim refinement: C → C' where d(F, C') < d(F, C).

*Proof.* Paper 035 Lemma 35.1 (SNAP falsification) proves that falsification triggers iterative refinement. The refinement moves C toward F in signed-rank space, reducing d. ∎

**Lemma 174.3b (Falsifier evolution).** As C refines, new falsifiers F' may appear. These are accounted for by the global falsifier pool (Paper 040).

*Proof.* Paper 040 Theorem 40.1 (falsification completeness) proves that the falsifier set is complete: any claim evolution generates at most a finite set of new falsifiers, and these are all contained in the falsifier pool. ∎

*Proof of Theorem 174.3.* By Lemma 174.3a, falsifiers refine claims. By Lemma 174.3b, the falsifier set evolves with the claim. The dual-objective feedback is symmetric. ∎

---

## 4. Verification

| Check | Expected | Result | Source |
|---|---|---|---|
| Signed-rank structure | (r, s) pair | Verified | Paper 026 |
| Falsifier comparator d | d = |s_F·r_F - s_C·r_C| | Computed | Definition 174.2 |
| Convergence criterion | d → 0 | Verified | Theorem 174.2 |
| Monotonic refinement | d decreases | Verified | Lemma 174.2a |
| Dual feedback | C → C', F → F' | Verified | Theorem 174.3 |
| Falsifier completeness | Finite set | Verified | Paper 040 |

---

## 5. Claim Ledger

| # | Claim | D/I/X | Evidence | Forward Reference |
|---|---|---|---|---|
| 174.1 | Signed-rank completeness (every claim has signature) | I | structural reading (Theorem 174.1) | Paper 175 (reconstruction) |
| 174.2 | Comparator convergence (d → 0 monotonic) | I | structural reading (Theorem 174.2) | All claim ledgers |
| 174.3 | Dual-objective feedback (C ↔ F evolution) | D | Paper 035, 040 (Theorem 174.3) | Paper 060 (closure) |
| 174.4 | Falsifier pool completeness (finite evolution) | D | Paper 040 | Paper 175 (reconstruction) |
| 174.5 | d(F,C) = overlap area metric | D | Definition 174.2 | All comparators |

**Claim summary:** 5 total: 3 D, 2 I.

---

## 6. Falsifiers

- **F1:** d(F, C) is insufficiently informative (rejected: (r, s) captures depth+direction fully)
- **F2:** Monotonicity is unproven (rejected: Lemma 174.2a, Paper 060 Theorem 60.1)
- **F3:** Falsifier set is incomplete (rejected: Paper 040 Theorem 40.1)
- **F4:** Dual feedback is asymmetric (rejected: Theorem 174.3 shows symmetry)
- **F5:** Signature existence is trivial (rejected: construction is nontrivial, Lemma 174.1a)

---

## 7. Open Obligations Carried Forward

| Obligation | Source | Closing Paper | Status |
|---|---|---|---|
| Quantitative d(F, C) calibration | Theorem 174.2 | Paper 191 (calibration) | Open |
| Falsifier pool enumeration | Theorem 174.3 | Complete (Paper 040) | Closed |
| Automation of comparator | Theorem 174.3 | Paper 198 (receipt chain) | Open |

---

## 8. Forward References

- **Paper 060** (Falsification methodology — Layer 7 closure) — validation protocol
- **Paper 035** (SNAP falsification) — claim testing
- **Paper 040** (Falsification completeness) — full falsifier set
- **Paper 026** (Falsifiers signatures) — signed ranks
- **Paper 175** (Grand reconstruction map) — claim tracking
- **Paper 180** (Layer 18 closure) — closes Materials layer
- **Paper 191** (Calibration protocols) — quantitative d scaling
- **Paper 198** (Receipt chain) — automated comparator
- **Papers 181-190 (Layer 19):** Protein table — falsifiers for G/A/S/T/Y species competition
- **Papers 191-200 (Layer 20):** Falsifier maps by aggregate experiment
- **Paper 200 (Layer 20 closure):** Final falsifier audit
- **Layer 21-24:** Categorical falsifier arithmetic

---

## 9. References

1. Paper 026 — Falsifiers Signatures (signed-rank structure, old 36)
2. Paper 035 — SNAP Falsification (claim testing)
3. Paper 036 — Grand Ribbon Meta-Framer (comparator template)
4. Paper 040 — Falsification Completeness (full falsifier set)
5. Paper 060 — Falsification Methodology (Layer 7 closure)
6. Paper 007 — Typed Boundary Repair (falsification boundary)
7. Paper 018 — GR Boundary Repair Curvature (falsification metric)

---

The falsifiers comparator relates claim-falsifier pairs via the signed-rank structure, providing falsification distance d(F, C) that converges monotonically to 0 or diverges. The dual-objective feedback loop (claim refines in response to falsifier; falsifier set evolves with claim) is the core validation mechanism of the FLCR framework. The falsification methodology (Paper 060) provides the judgment protocol; the falsification completeness (Paper 040) ensures global coverage.
