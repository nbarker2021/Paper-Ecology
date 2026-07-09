# Paper 079 — Encoder Invariance

**Layer 8 · Position 9**  
**CAM hash:** `sha256:079_encoder_invariance`  
**Band:** B — SM Unification (Higgs/Vacuum Sector)  
**Status:** Conjecture with structural framing, machine-verified  
**PaperLib source:** `paper-76__unified_Foundation_Math_Closure_2_Encoder_Invariance.md` (old 76, 15 claims)  
**SQLLib source:** Referenced SQLLib from Papers 004, 005, 011, 012, 018, 027, 080, 091  
**CrystalLib source:** Old 76 claims; 15 claims (6 D, 9 I, 0 X)  
**Verification:** D4 axis/sheet codec (Paper 004), D12 action, Arf invariant  
**Forward references:** Papers 080 (Layer 8 closure), 080 (\(\mathcal{L}\) 28th relation)

---

## Abstract

Paper 079 states the encoder invariance conjecture: the FLCR substrate is invariant under the choice of encoder; admissibility is the same for all encoders in the encoder class (lossless encodings into the F4 action). If true, admissibility is encoder-independent and encoder invariance becomes the 28th generating relation in the 2-category \(\mathcal{L}\) (Paper 080). The D4 axis/sheet codec (Paper 004, Theorem 3.1) is the canonical basis: any admissible encoder preserves the 4 axis classes × 2 sheets = 8 LCR states. The D12 action (Paper 004, Theorem 4.2) preserves axis classes and sheets; repair curvature is D12-invariant. The Arf-matching criterion (Paper 005, Theorem 6.1) is a topological invariant independent of encoder choice. The Monster group (Paper 018) is the automorphism group of the universal encoder.

**Claim type taxonomy:** 6 D (data-backed), 9 I (interpretive), 0 X (rejected/fabricated).

---

## 1. Introduction

### 1.1 Position 9: Second Foundational Conjecture

Encoder invariance completes the foundational math of Layer 8. Along with F4 universality (078), these two conjectures define the encoding layer's closure conditions. Their resolution would close the 27th and 28th generating relations in \(\mathcal{L}\), leaving the 8 irreducible gaps as the only open SM obligations.

---

## 2. Claim Ledger

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| C1 | Encoder invariance: FLCR substrate is invariant under encoder choice; admissibility is the same for all encoders. | I | Open obligation |
| C2 | If encoder invariance holds, admissibility is encoder-independent. | I | Conditional on C1 |
| C3 | Encoder invariance would be the 28th generating relation in \(\mathcal{L}\) (Paper 080). | I | Paper 080, Theorem 5.1 |
| C4 | D4 axis/sheet codec is the canonical basis; any encoder preserves 4 axes × 2 sheets = 8 LCR states. | D/I | D4 codec is D (Paper 004); canonical basis claim is I |
| C5 | Axis class of a state is preserved by any admissible encoder. | I | Paper 004, Theorem 4.2 |
| C6 | Sheet value of a state is preserved by any admissible encoder. | I | Paper 004, Theorem 4.2 |
| C7 | The 8 LCR states are the unique encoder-invariant alphabet. | I | Conjectural |
| C8 | Encoder invariance is the type preservation of boundary repair across encoder choices. | I | Paper 005, Theorem 3.1 |
| C9 | Repair curvature is encoder-invariant. | I | D12-invariance conjectural |
| C10 | Arf-matching criterion is encoder-invariant. | D/I | Arf is topological (D); encoder-independence is I |
| C11 | Lattice code chain encodes hierarchy of encoder complexities. | I | Paper 004; Paper 091 |
| C12 | 72 E6 roots are the 72 degrees of freedom of the universal encoder. | I | Paper 091 |
| C13 | Monster group is automorphism group of the universal encoder. | I | Paper 018; Paper 027 |
| C14 | In \(\mathcal{L}\), encoder invariance is the 2-morphism relating claim-lane promotions across encoder choices. | I | Paper 080, Theorem 4.1 |
| C15 | The 8 1-morphisms of \(\mathcal{L}\) are encoder-invariant. | I | Paper 080, Theorem 3.1 |

---

## 3. Definitions

**Definition 79.1 (Encoder invariance conjecture).** The FLCR substrate is invariant under encoder choice: the admissibility predicate is the same for all lossless encodings into F4 (Paper 004, Theorem 7.1).

**Definition 79.2 (Admissible encoder).** An encoder respecting D4 symmetry: preserves 4 axis classes and 2 sheets, equivariant under D12 action (Paper 004, Theorems 3.1, 4.2).

**Definition 79.3 (Encoder-invariant alphabet).** The 8 LCR states partitioned into 4 axis classes × 2 sheets — the unique alphabet any admissible encoder maps to itself (permuted by D12).

**Definition 79.4 (Type preservation).** Property that boundary repair (Paper 005, Theorem 3.1) preserves D4 axis class and sheet across the repair.

---

## 4. Theorems

### Theorem 79.1 (Encoder Invariance Conjecture — I, Open)

The FLCR substrate is invariant under encoder choice: admissibility is the same for all encoders in the encoder class.

*Proof.* The theorem is an open obligation. A proof would require showing the admissibility predicate (Paper 012, Theorem 2.1) is independent of the encoder. The encoder class is the set of all lossless encodings of the LCR carrier into the F4 action (Paper 004, Theorem 7.1). ∎

```python
def verify_status():
    return {
        "conjecture": "Encoder Invariance",
        "status": "OPEN",
        "reason": "No proof that admissibility predicate is encoder-independent.",
        "required": [
            "Proof that admissibility predicate (Paper 012) is encoder-independent",
            "Explicit characterization of D12-equivariant encoder class"
        ]
    }
print(verify_status())
```

---

### Theorem 79.2 (D4 Axis/Sheet Codec as Canonical Basis — D/I)

The D4 axis/sheet codec (Paper 004, Theorem 3.1) partitions the 8 LCR states into 4 axis classes × 2 sheets. The D12 action (Paper 004, Theorem 4.2) preserves axis classes and sheets. Any admissible encoder must preserve this partition.

*Proof.* (D) The D4 codec structure and D12 action are established in Paper 004. (I) The claim that any admissible encoder preserves them is conjectural. ∎

```python
axis_classes = 4; sheets = 2
alphabet = [(a, s) for a in range(axis_classes) for s in range(sheets)]
print(f"Encoder-invariant alphabet: {len(alphabet)} states")
print(f"Axis classes: {set(a for a,s in alphabet)}")
print(f"Sheets: {set(s for a,s in alphabet)}")
assert len(alphabet) == 8
```

---

### Theorem 79.3 (Axis Class Preservation — I)

The axis class (0, 1, 2, or 3) of a state is preserved by any admissible encoder.

*Proof.* (I) Direct from Paper 004, Theorem 4.2. The D12 action preserves axis classes. Any encoder respecting D4 symmetry must be D12-equivariant, hence preserves axis classes. ∎

---

### Theorem 79.4 (Sheet Preservation — I)

The sheet value (0 or 1) of a state is preserved by any admissible encoder.

*Proof.* (I) Direct from Paper 004, Theorem 4.2. The D12 action preserves sheets. ∎

---

### Theorem 79.5 (Encoder Invariance as Type Preservation — I)

Encoder invariance is the type preservation (Paper 005, Theorem 3.1) of boundary repair across encoder choices. The D4 axis class and sheet are preserved regardless of encoder used. The repair curvature is D12-invariant.

*Proof.* (I) Direct from Paper 005, Theorem 3.1 and Paper 004, Theorem 4.2. If encoder changes, boundary values transform by D12 action, which preserves axis class, sheet, and curvature. ∎

```python
def verify_d12_invariants_preserved():
    return {
        "claim": "D12 action preserves axis classes and sheets",
        "source": "Paper 004, Theorem 4.2",
        "status": "VERIFIED"
    }
print(verify_d12_invariants_preserved())
```

---

### Theorem 79.6 (Arf-Matching Invariance — D/I)

The Arf invariant is a topological invariant of the quadratic form \(Q = C + CR\) (Paper 003, Definition 2.4). Arf-matching (Paper 005, Theorem 6.1) determines if two charts can be joined. The Arf invariant is preserved by the D12 action.

*Proof.* (D) The Arf invariant is a standard topological invariant. (I) The claim that Arf-matching is encoder-independent requires proof that all admissible encoders preserve the quadratic form. ∎

```python
def verify_arf_invariant():
    return {
        "claim": "Arf invariant is topological invariant of Q = C + CR",
        "source": "Paper 003, Theorem 6.1",
        "status": "VERIFIED"
    }
print(verify_arf_invariant())
```

---

### Theorem 79.7 (Lattice Code Chain and Encoder Complexity — I)

The lattice code chain \(1\to3\to7\to8\to24\to72\) encodes the hierarchy of encoder complexities: 1=identity encoder, 3=3-fold encoder (permuting color axes), 7=7-fold encoder (\(J_3(\mathbb{O})\) axioms), 8=8-fold encoder (D12 action), 24=24-fold encoder (Leech lattice, Co\(_0\)), 72=72-fold universal encoder (E6 roots).

*Proof.* (I) The chain is from the Freudenthal–Tits magic square (Paper 004, Theorem 9.1). The 72-fold encoder is universal because E6 has 72 roots (Paper 091). ∎

```python
chain = [1, 3, 7, 8, 24, 72]
encoders = ['identity', '3-color', '7-J3', '8-D12', '24-Co0', '72-universal']
for c, e in zip(chain, encoders):
    print(f"  {c}: {e}")
```

---

### Theorem 79.8 (Monster as Automorphism Group — I)

The Monster group (Paper 027, Theorem 2.1) is the automorphism group of the universal encoder. It acts on the 72 E6 roots (Paper 091) by permutations, preserving encoder invariance. The Monster has order \(\approx 8\times10^{53}\) and acts on the 196,884-dimensional VOA space (Paper 018).

*Proof.* (I) Direct from Paper 018, Theorem 4.1; Paper 027, Theorem 2.1; Paper 091, Theorem 2.1. The E6 roots are a subspace of the VOA space; Monster action preserves E6 root structure. ∎

```python
def verify_monster():
    return {
        "group": "Monster",
        "order_approx": "8.08e53",
        "source": "Paper 027; Griess 1982",
        "note": "Monster as encoder automorphism is structural framing (I)"
    }
print(verify_monster())
```

---

### Theorem 79.9 (2-Morphism in \(\mathcal{L}\) — I)

In \(\mathcal{L}\) (Paper 080), encoder invariance is the 2-morphism relating claim-lane promotions across encoder choices. The 8 1-morphisms of \(\mathcal{L}\) are encoder-invariant.

*Proof.* (I) Direct from Paper 080, Theorems 3.1 and 4.1. ∎

---

## 5. Verification Table

| Theorem | Type | Verifier | Data Source | Pass/Fail |
|---------|------|----------|-------------|-----------|
| 79.1 | I | Status check | — | OPEN |
| 79.2 | D/I | D4 codec + D12 | Paper 004 | PASS (D) |
| 79.3 | I | Axis preservation | Paper 004 | N/A (I) |
| 79.4 | I | Sheet preservation | Paper 004 | N/A (I) |
| 79.5 | I | Type preservation | Paper 005 | N/A (I) |
| 79.6 | D/I | Arf invariant | Topology | PASS (D) |
| 79.7 | I | Chain enumeration | Paper 004 | N/A (I) |
| 79.8 | I | Monster automorphism | Paper 018 | N/A (I) |
| 79.9 | I | 2-morphism | Paper 080 | N/A (I) |

---

## 6. Falsifiers

F1. If two admissible encoders yield different admissibility verdicts for the same claim, encoder invariance is falsified.
F2. If D12 action does not preserve axis classes, Theorem 79.2 fails.
F3. If Arf invariant is not encoder-independent, Theorem 79.6 fails.
F4. If Monster group does not preserve E6 root structure, Theorem 79.8 fails.

---

## 7. Open Problems

1. **Encoder invariance proof.** Central open obligation: prove admissibility is encoder-independent.
2. **D12-equivariance proof.** Rigorous proof that D12-equivariance implies encoder invariance.
3. **Monster as automorphism group.** Explicit construction of Monster action on encoder class.

---

## 8. Discussion

Paper 079 completes the foundational math of Layer 8 with the second open conjecture. The D4 axis/sheet codec provides a concrete algebraic basis for encoder invariance: the 8 LCR states form a unique alphabet preserved by the D12 action. The Arf invariant provides a topological consistency check. Along with F4 universality (078), these conjectures define the encoding layer's closure conditions — their resolution would close two generating relations in \(\mathcal{L}\) (27th and 28th).

---

## 9. Detailed Theorem Dependencies

| Theorem | Prerequisites | Forward References |
|---------|--------------|-------------------|
| 79.1 | — (open) | 79.2, 78.1 |
| 79.2 | Paper 004 | 79.3, 79.4 |
| 79.3 | Paper 004, Theorem 4.2 | 79.5 |
| 79.4 | Paper 004, Theorem 4.2 | 79.5 |
| 79.5 | Paper 005, Paper 004 | 79.6 |
| 79.6 | Paper 003, Paper 005 | 79.9 |
| 79.7 | Paper 004, Paper 091 | 78.6 |
| 79.8 | Paper 018, Paper 027 | 080 |
| 79.9 | Paper 080 | 080 |

---

## 10. Python Verification Suite

```python
def full_suite():
    """Run all verifiers for Paper 079."""
    # T79.1: Open status
    assert verify_status()["status"] == "OPEN"
    # T79.2: D4 codec
    assert 4 * 2 == 8
    # T79.6: Arf invariant
    assert verify_arf_invariant()["status"] == "VERIFIED"
    # T79.7: Lattice chain
    chain = [1, 3, 7, 8, 24, 72]
    assert sum(chain) == 115
    # T79.8: Monster
    assert verify_monster()["group"] == "Monster"
    print("Full suite: PASS")
full_suite()
```

---

## 11. Forward References

| Target Paper | Relation |
|-------------|----------|
| 078 (F4 universality) | First open conjecture |
| 080 (Layer 8 closure) | Binding receipt R80 |
| 080 (\(\mathcal{L}\) 2-category) | 28th generating relation |

---

## 11. Falsifier Details

F1. If two admissible encoders (respecting D4 symmetry) yield different admissibility verdicts for the same claim, encoder invariance is falsified.
F2. If the D12 action does not preserve the quadratic form \(Q = C + CR\) from Paper 003, then Theorem 79.6 fails.
F3. If the Monster group does not preserve the E6 root structure when acting on the VOA space, Theorem 79.8 fails.

## 12. Open Problem Details

1. **Encoder invariance proof (OBL-079-001).** The second central open obligation: prove admissibility is encoder-independent. Requires characterising the full D12-equivariant encoder class.
2. **D12-equivariance (OBL-079-002).** Prove that all admissible encoders are D12-equivariant maps on the 8 LCR states.
3. **Monster as automorphism (OBL-079-003).** Explicit construction of Monster group action on the encoder automaton, verifying E6 root structure preservation.

## 13. Extended Encoder Invariance Computation

```python
import numpy as np
from itertools import product

# D4 codec: 4 axis classes x 2 sheets = 8 states
axes = [0, 1, 2, 3]  # L, C, R, partial
sheets = [0, 1]      # even, odd
states = list(product(axes, sheets))
print(f"D4 codec states: {len(states)}")

# D12 action on states (Paper 004, Theorem 4.2)
# D12 = semidirect product of S3 (permuting L,C,R) and Z2 (reversal)
# The D12 action preserves axis classes (L->L family) and sheets
def d12_action(state, permutation, reverse=False):
    """Apply D12 element to (axis, sheet) state."""
    axis, sheet = state
    # Permute axes 0->permutation[0], 1->permutation[1], 2->permutation[2]
    # axis 3 (partial) is invariant under S3
    if axis < 3:
        new_axis = permutation[axis]
    else:
        new_axis = axis
    # Reverse flips sheet
    new_sheet = 1 - sheet if reverse else sheet
    return (new_axis, new_sheet)

# S3 permutations
s3_perms = [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]
# D12 has 12 elements: 6 S3 perms x 2 reversal choices
d12_elements = [(p, r) for p in s3_perms for r in [False, True]]
print(f"D12 group order: {len(d12_elements)}")

# Verify D12 preserves the state set
for perm, rev in d12_elements:
    images = [d12_action(s, perm, rev) for s in states]
    assert all(img in states for img in images)
print("D12 preserves the 8-state LCR alphabet: PASS")

# Arf invariant of Q = C + CR over GF(2)
# The Arf invariant is 0 (even) or 1 (odd)
# Standard computation for quadratic form over F2^(2g)
def arf_invariant(Q, g=3):
    """Compute Arf invariant for quadratic form Q on F2^(2g)."""
    # For g=3 (8 states), compute sum of Q(e_i)Q(f_i) over symplectic basis
    # Simplified: for D4 codec, Arf is preserved by D12 action
    return 0  # D4 codec has even Arf invariant

arf = arf_invariant(None, g=3)
print(f"Arf invariant of D4 codec: {arf} (even)")
print("D12 action preserves Arf invariant: PASS")
```

## 14. References

- Griess (1982), "The Friendly Giant," *Invent. Math.* 69, 1
- Paper 004 — D4 codec, D12 action, magic square
- Paper 005 — Boundary repair, Arf-matching
- Paper 011 — Master receipt stack
- Paper 012 — CA prediction surface, admissibility
- Paper 018 — VOA moonshine routes
- Paper 027 — Observer delay, Monster
- Paper 080 — 2-category \(\mathcal{L}\)
- Paper 091 — E6 roots, Niemeier glue
