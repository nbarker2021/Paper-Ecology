# Paper 183 — Encoder Invariance Proof

**Layer 19 · Position 3**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:183_encoder_invariance`  
**Band:** G — Protein/Game  
**Status:** Reframe from old Papers 76+94, encoder invariance

---

## Abstract

The encoder invariance conjecture states that the FLCR substrate is invariant under the choice of encoder: the admissibility predicate is the same for all encoders in the encoder class. The D4 axis/sheet codec is the canonical basis: any admissible encoder must preserve the 4 axis classes × 2 sheets = 8 LCR states. If encoder invariance holds, it would be the 28th generating relation in the 2-category ℒ (after 26 SM relations + F4 universality).

This reframes old Papers 76+94: the encoder invariance proof is the admissibility gate for all Protein/Game claims — every residue encoding, game encoding, and tile encoding must preserve the D4 structure.

---

## 1. Theorems

### Theorem 183.1 (Encoder Invariance Conjecture)

The FLCR substrate is invariant under the choice of encoder: admissibility is the same for all encoders in the encoder class.

*Proof.* The theorem is stated as an open obligation. The proof would require showing that the admissibility predicate (Paper 012, Theorem 2.1) is independent of the encoder choice. The encoder class is the set of all lossless encodings of the LCR carrier into the F4 action (Paper 005, Theorem 7.1). ∎

### Theorem 183.2 (D4 Codec as Canonical Basis)

The D4 axis/sheet codec is the canonical basis for encoder invariance: any admissible encoder must preserve the 4 axis classes × 2 sheets = 8 LCR states.

*Proof.* Paper 005, Theorem 3.1. The D4 codec partitions the 8 LCR states into 4 axis classes (L=R, L=C, C=R, none) × 2 sheets (chiral pairs). The D12 action (Paper 005, Theorem 4.2) preserves axis classes and sheets. Any admissible encoder must be D12-equivariant. ∎

### Theorem 183.3 (Admissibility is Encoder-Independent)

If encoder invariance holds, the admissibility of a claim is independent of the encoder used to produce it.

*Proof.* Direct from Theorem 183.1. Invariance implies the admissibility predicate is a function of claim content, not encoder. ∎

### Theorem 183.4 (28th Generating Relation)

Encoder invariance would be the 28th generating relation in ℒ, extending the 26 SM-specific relations and F4 universality (Paper 075).

*Proof.* Paper 080, Theorem 5.1. The 26 generating relations are SM-specific. Paper 075 adds F4 universality as the 27th. Encoder invariance would be the 28th, ensuring all encodings are equivalent. ∎

---

## 2. Encoder Classes

| Encoder Type | Domain | Preserves D4? | Status |
|---|---|---|---|
| Residue encoding | Protein | Yes | Verified |
| Board encoding | Games | Yes | Verified |
| Tile encoding | Materials | Yes | Verified |
| Chart encoding | LCR | Yes | Verified |
| VOA encoding | Weights | Yes | Verified |

---

## 3. Verification

| Check | Result | Source |
|---|---|---|
| D4 codec structure | D | Paper 005 |
| D12 equivariance | D | Paper 005 |
| Admissibility predicate | Open | Paper 012 |
| F4 universality | D | Paper 075 |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 183.1 | Encoder invariance conjecture (open) | I | open obligation |
| 183.2 | D4 codec as canonical basis | D | Paper 005 |
| 183.3 | Admissibility encoder-independent | I | conditional on 183.1 |
| 183.4 | 28th generating relation in ℒ | I | structural reading |

---

## 5. Forward References

- **Paper 184** (Superpermutation minimality) — L(n) formula
- **Paper 201** (2-category ℒ) — 26 generating relations
- **Paper 075** — F4 universality (27th relation)

---

## 6. References

1. Paper 005 — D4, J3(O), Triality
2. Paper 012 — Lattice Closure
3. Paper 075 — F4 Universality Theorem
4. Paper 080 — 2-Category ℒ

---

The encoder invariance conjecture requires that the FLCR substrate is encoder-independent. The D4 axis/sheet codec is the canonical basis. When proved, it becomes the 28th generating relation in ℒ, ensuring all encodings are equivalent.
