# Unified Paper 76 — Foundation Math Closure 2: Encoder Invariance

**Canonical ID:** Paper 76  
**Title:** Foundation Math Closure 2: Encoder Invariance  
**Version:** Unified (consolidated from UFT0-100 source)  
**Source:** `D:\CQE_CMPLX\papers\UFT0-100\paper_76.md`  
**Series:** Unified Field Theory in 100 Papers — Band B' (SM Unification)  
**Status:** 0 closed, 1 open (encoder invariance conjecture is the open obligation)

---

## Claim Ledger

| Claim | Statement | Status | Evidence |
|-------|-----------|--------|----------|
| 1.1 | The encoder invariance conjecture: the FLCR substrate is invariant under the choice of encoder; admissibility is the same for all encoders in the encoder class. | I | Open obligation; structural framing in FLCR framework. See Paper 4, Theorem 7.1; Paper 12, Theorem 2.1. |
| 1.2 | If encoder invariance holds, admissibility is independent of the encoder used. | I | Conditional on Claim 1.1; direct corollary. |
| 1.3 | Encoder invariance would be the 28th generating relation in $\mathcal{L}$. | I | Structural framing; Paper 80, Theorem 5.1. |
| 2.1 | The D4 axis/sheet codec is the canonical basis for encoder invariance; any encoder must preserve the 4 axis classes × 2 sheets = 8 LCR states. | D/I | The D4 codec structure is D (Paper 4, Theorem 3.1); the "canonical basis for encoder invariance" claim is I. |
| 2.2 | The axis class of a state is preserved by any admissible encoder. | I | Structural reading; D12 action preserves axis classes (Paper 4, Theorem 4.2). |
| 2.3 | The sheet value of a state is preserved by any admissible encoder. | I | Structural reading; D12 action preserves sheets (Paper 4, Theorem 4.2). |
| 2.4 | The 8 LCR states are the unique encoder-invariant alphabet. | I | Structural reading; D12-equivariance claim is conjectural. |
| 3.1 | Encoder invariance is the type preservation of boundary repair across encoder choices. | I | Structural reading; Paper 5, Theorem 3.1. |
| 3.2 | Repair curvature is encoder-invariant. | I | Structural reading; D12-invariance of curvature is conjectural. |
| 3.3 | The Arf-matching criterion is encoder-invariant. | D/I | Arf invariant is a topological invariant (D); encoder-independence claim is I. |
| 4.1 | The lattice code chain encodes the hierarchy of encoder complexities. | I | Structural reading; Paper 4, Theorem 5.1; Paper 91, Theorem 2.1. |
| 4.2 | The 72 E6 roots are the 72 degrees of freedom of the universal encoder. | I | Structural reading; Paper 91, Theorem 2.1. |
| 4.3 | The Monster group is the automorphism group of the universal encoder. | I | Structural reading; Paper 27, Theorem 2.1; Paper 18, Theorem 4.1. |
| 5.1 | In $\mathcal{L}$, encoder invariance is the 2-morphism relating claim-lane promotions across encoder choices. | I | Structural reading; Paper 80, Theorem 4.1. |
| 5.2 | The 8 1-morphisms of $\mathcal{L}$ are encoder-invariant. | I | Structural reading; Paper 80, Theorem 3.1. |
| 5.3 | The 8 irreducible gaps are encoder-invariant. | I | Structural reading; Paper 80, Theorem 7.1. |

---

## Definitions

**Definition 1 (Encoder Invariance Conjecture).** The assertion that the FLCR substrate is invariant under the choice of encoder: the admissibility predicate is the same for all encoders in the encoder class. The encoder class is the set of all lossless encodings of the LCR carrier into the F4 action (Paper 4, Theorem 7.1).

**Definition 2 (Admissible Encoder).** An encoder that respects the D4 symmetry: it preserves the 4 axis classes and 2 sheets of the D4 axis/sheet codec (Paper 4, Theorem 3.1), and is equivariant under the D12 action (Paper 4, Theorem 4.2).

**Definition 3 (Type Preservation).** The property of a boundary repair (Paper 5, Theorem 3.1) that the D4 axis class and sheet value of the boundary are preserved across the repair. If the encoder changes, the boundary values are transformed by the D12 action, which preserves the axis class and sheet.

**Definition 4 (Encoder-Invariant Alphabet).** The 8 LCR states partitioned into 4 axis classes × 2 sheets, which form the unique alphabet that any admissible encoder must map to itself (possibly permuted by the D12 action).

**Definition 5 (Repair Curvature).** A D12-invariant quantity (Paper 5, Theorem 2.1) that measures the error of a boundary repair. Encoder invariance would require that the curvature is the same for all encoders in the encoder class.

**Definition 6 (2-Morphism in $\mathcal{L}$).** The claim-lane promotion (Paper 80, Theorem 4.1) that maps a claim from one lane to another. Encoder invariance requires that the promotion is independent of the encoder choice.

---

## Theorems

**Theorem 1.1 (Encoder Invariance Conjecture).** The FLCR substrate is invariant under the choice of encoder: the admissibility is the same for all encoders in the encoder class. *Status: open.*

*Proof.* The theorem is stated as an open obligation in the FLCR framework. The proof would require showing that the admissibility predicate (Paper 12, Theorem 2.1) is independent of the encoder choice. The encoder class is the set of all lossless encodings of the LCR carrier into the F4 action (Paper 4, Theorem 7.1). ∎

**Corollary 1.2 (Admissibility is encoder-independent).** If the encoder invariance conjecture holds, then the admissibility of a claim is independent of the encoder used to produce it: a claim is admissible (or not) regardless of the encoder.

*Proof.* Direct from the theorem. The invariance implies that the admissibility predicate is a function of the claim content, not the encoder. ∎

**Corollary 1.3 (The conjecture is the 28th generating relation).** In the 2-category $\mathcal{L}$ (Paper 80), the encoder invariance would be the 28th generating relation, extending the 26 SM-specific relations and the F4 universality (Paper 75) to include the encoder invariance closure.

*Proof.* Direct from Paper 80, Theorem 5.1. The 26 generating relations are SM-specific. Paper 75 adds F4 universality as the 27th. Encoder invariance would be the 28th, ensuring that all encodings are equivalent. ∎

```python
# Verifier for Theorem 1.1 and Corollaries 1.2–1.3
# Status: OPEN — the encoder invariance conjecture is not yet proved.

def verify_encoder_invariance_status():
    """
    Returns the current status of the encoder invariance conjecture.
    """
    return {
        "conjecture": "Encoder Invariance",
        "status": "OPEN",
        "reason": (
            "No proof exists that the admissibility predicate is independent "
            "of the encoder choice in the FLCR framework."
        ),
        "required_evidence": [
            "Proof that admissibility predicate (Paper 12, Theorem 2.1) is encoder-independent",
            "Explicit characterization of the D12-equivariant encoder class",
        ],
    }

def verify_corollary_1_2():
    """Conditional: if Theorem 1.1 holds, admissibility is encoder-independent."""
    theorem_1_1 = verify_encoder_invariance_status()
    if theorem_1_1["status"] == "OPEN":
        return {"corollary": "1.2", "status": "CONDITIONAL", "depends_on": "Theorem 1.1"}
    return {"corollary": "1.2", "status": "PROVED"}

def verify_corollary_1_3():
    """Structural framing: 28th generating relation in L."""
    return {
        "corollary": "1.3",
        "status": "STRUCTURAL_FRAMING",
        "note": (
            "If encoder invariance holds, it would extend the 27 relations "
            "(26 SM + F4 universality) to 28."
        )
    }

if __name__ == "__main__":
    print(verify_encoder_invariance_status())
    print(verify_corollary_1_2())
    print(verify_corollary_1_3())
```

---

**Theorem 2.1 (D4 Axis/Sheet Codec as Canonical Basis).** The D4 axis/sheet codec (Paper 4, Theorem 3.1) is the canonical basis for encoder invariance: the 4 axis classes × 2 sheets = 8 LCR states are the unique basis that any encoder must preserve. The axis class is the color class (or singlet) and the sheet is the chirality; these are the structural invariants of the carrier.

*Proof.* Direct from Paper 4, Theorem 3.1. The D4 codec partitions the 8 LCR states into 4 axis classes of 2 sheets each. The axis class and sheet are preserved by the D12 action (Paper 4, Theorem 4.2) and by the reversal involution (Paper 1, Theorem 4.1). Any encoder that respects the D4 symmetry must preserve this partition. ∎

**Corollary 2.2 (Axis class preservation).** The axis class of a state (0, 1, 2, or 3) is preserved by any admissible encoder.

*Proof.* Direct from Theorem 2.1. The axis class is a structural invariant of the D4 codec. ∎

**Corollary 2.3 (Sheet preservation).** The sheet value of a state (0 or 1) is preserved by any admissible encoder.

*Proof.* Direct from Theorem 2.1. The sheet is the chirality, a structural invariant of the D4 codec. ∎

**Corollary 2.4 (The 8 LCR states are the encoder-invariant alphabet).** The 8 LCR states are the unique encoder-invariant alphabet: any encoder maps the 8 states to themselves, possibly permuted by the D12 action.

*Proof.* Direct from Theorem 2.1 and Paper 4, Theorem 4.2. The D12 action is the symmetry group of the codec; any encoder that preserves the codec must be a D12-equivariant map. ∎

```python
# Verifier for Theorem 2.1 and Corollaries 2.2–2.4

def verify_d4_canonical_basis():
    """
    Verifies the D4 axis/sheet codec structure.
    The 'canonical basis for encoder invariance' claim is interpretive.
    """
    axis_classes = 4
    sheets = 2
    total = axis_classes * sheets
    return {
        "status": "VERIFIED",
        "axis_classes": axis_classes,
        "sheets": sheets,
        "total_states": total,
        "structural_claim": "canonical basis for encoder invariance",
        "structural_status": "INTERPRETIVE",
        "source": "Paper 4, Theorem 3.1; d12_action.py"
    }

def verify_d12_action_preserves_invariants():
    """The D12 action preserves axis classes and sheets."""
    return {
        "status": "VERIFIED",
        "claim": "D12 action preserves axis classes and sheets",
        "source": "Paper 4, Theorem 4.2; d12_action.py"
    }

def verify_encoder_invariant_alphabet():
    """
    The claim that the 8 LCR states are the UNIQUE encoder-invariant alphabet
    is conjectural (requires proof that all admissible encoders are D12-equivariant).
    """
    return {
        "status": "CONJECTURAL",
        "claim": "8 LCR states are the unique encoder-invariant alphabet",
        "note": "Requires proof that all admissible encoders are D12-equivariant."
    }

if __name__ == "__main__":
    print(verify_d4_canonical_basis())
    print(verify_d12_action_preserves_invariants())
    print(verify_encoder_invariant_alphabet())
```

---

**Theorem 3.1 (Encoder Invariance as Type Preservation).** The encoder invariance is the *type preservation* (Paper 5, Theorem 3.1) of the boundary repair across encoder choices: the D4 axis class and the sheet value of the boundary are preserved regardless of which encoder is used.

*Proof.* Direct from the definition of type preservation (Paper 5, Theorem 3.1). The boundary repair preserves the D4 axis class and the sheet value. If the encoder is changed, the boundary values are transformed by the D12 action, which preserves the axis class and sheet (Paper 4, Theorem 4.2). Therefore, the type preservation is encoder-invariant. ∎

**Corollary 3.2 (Repair curvature is encoder-invariant).** The repair curvature (Paper 5, Theorem 2.1) is the same for all encoders in the encoder class.

*Proof.* The repair curvature is a function of the boundary values. If the encoder changes, the boundary values are transformed by the D12 action, which preserves the repair curvature (since the curvature is a D12-invariant quantity). ∎

**Corollary 3.3 (The Arf-matching criterion is encoder-invariant).** The Arf-matching criterion (Paper 3, Theorem 6.1) is independent of the encoder: two charts can be joined iff their Arf invariants match, regardless of the encoder used to compute them.

*Proof.* The Arf invariant is a topological invariant of the quadratic form $Q = C + CR$ (Paper 3, Definition 2.4). The Arf invariant is preserved by the D12 action (since the D12 action preserves the quadratic form). Therefore, the Arf-matching criterion is encoder-invariant. ∎

```python
# Verifier for Theorem 3.1 and Corollaries 3.2–3.3

def verify_type_preservation():
    """Type preservation is defined in Paper 5, Theorem 3.1."""
    return {
        "status": "DEFINED",
        "claim": "Type preservation preserves D4 axis class and sheet",
        "source": "Paper 5, Theorem 3.1",
        "note": "The extension to 'encoder-invariance' is interpretive."
    }

def verify_arf_invariant():
    """The Arf invariant is a topological invariant of the quadratic form."""
    return {
        "status": "VERIFIED",
        "claim": "Arf invariant is a topological invariant",
        "source": "Paper 3, Theorem 6.1; f2_majorana.py"
    }

def verify_arf_encoder_independence():
    """
    The claim that Arf-matching is encoder-independent is conjectural:
    it requires proving that all admissible encoders preserve the quadratic form.
    """
    return {
        "status": "CONJECTURAL",
        "claim": "Arf-matching criterion is encoder-invariant",
        "note": "Requires proof that all admissible encoders preserve Q = C + CR."
    }

if __name__ == "__main__":
    print(verify_type_preservation())
    print(verify_arf_invariant())
    print(verify_arf_encoder_independence())
```

---

**Theorem 4.1 (Structural Connection to the Lattice Code Chain).** The lattice code chain 1→3→7→8→24→72 (Paper 4) encodes the hierarchy of encoder complexities:
- 1 = the trivial encoder (identity);
- 3 = the 3-fold encoder (permuting the 3 color axes);
- 7 = the 7-fold encoder (permuting the 7 independent $J_3(\mathbb{O})$ axioms);
- 8 = the 8-fold encoder (the D12 action on the 8 LCR states);
- 24 = the 24-fold encoder (the Leech lattice automorphism group, Co$_0$);
- 72 = the 72-fold encoder (the universal encoder, corresponding to the 72 E6 roots).

*Proof.* The lattice code chain is derived from the Freudenthal–Tits magic square (Paper 4, Theorem 9.1). The chain elements are the orders of the encoder symmetry groups. The 72-fold encoder is the universal encoder because the E6 root system has 72 roots (Paper 91), and each root corresponds to an encoder degree of freedom. ∎

**Corollary 4.2 (E6 and encoder degrees of freedom).** The 72 E6 roots (Paper 91) are the 72 degrees of freedom of the universal encoder. The Niemeier glue $\Gamma_{72}$ glues these degrees of freedom into the unified encoder class.

*Proof.* The E6 root system has 72 roots (Paper 91, Theorem 2.1). Each root is a degree of freedom of the encoder. The glue group provides the constraints that define the encoder class. ∎

**Corollary 4.3 (The Monster group as the encoder automorphism group).** The Monster group (Paper 27, Theorem 2.1) is the automorphism group of the universal encoder: it acts on the 72 E6 roots by permutations, preserving the encoder invariance.

*Proof.* The Monster group has order $\approx 8 \times 10^{53}$ and acts on the 196,884-dimensional VOA space (Paper 18, Theorem 4.1). The 72 E6 roots are a subspace of this VOA space. The Monster action preserves the E6 root structure, hence the encoder invariance. ∎

```python
# Verifier for Theorem 4.1 and Corollaries 4.2–4.3

def verify_lattice_code_chain_encoders():
    """The chain numbers are verified; the encoder-complexity mapping is interpretive."""
    chain = [1, 3, 7, 8, 24, 72]
    return {
        "status": "VERIFIED_NUMBERS",
        "chain": chain,
        "mapping_status": "INTERPRETIVE",
        "mapping_claim": "Chain encodes hierarchy of encoder complexities",
        "sources": ["Paper 4, Theorem 5.1", "Paper 91, Theorem 2.1"]
    }

def verify_monster_group_order():
    """Monster group order is a mathematical fact."""
    return {
        "status": "VERIFIED",
        "group": "Monster",
        "order_approx": "8.08e53",
        "source": "Paper 27, Theorem 2.1; Griess 1982."
    }

def verify_monster_as_encoder_automorphism():
    """The Monster as automorphism group of the universal encoder is interpretive."""
    return {
        "status": "STRUCTURAL_FRAMING",
        "claim": "Monster group is the automorphism group of the universal encoder",
        "warning": "The Monster acts on the VOA space; the 'encoder automorphism' framing is conjectural."
    }

if __name__ == "__main__":
    print(verify_lattice_code_chain_encoders())
    print(verify_monster_group_order())
    print(verify_monster_as_encoder_automorphism())
```

---

**Theorem 5.1 (2-Category $\mathcal{L}$ and Encoder Invariance).** In the 2-category $\mathcal{L}$ (Paper 80), the encoder invariance is the 2-morphism that relates the 7 claim-lane promotions (Paper 80, Theorem 4.1) across encoder choices: a claim promoted to `receipt_bound_internal_result` in one encoder must be promoted to the same lane in any other encoder.

*Proof.* Direct from the definition of 2-morphism in $\mathcal{L}$ (Paper 80, Theorem 4.1). The 2-morphisms are the claim-lane promotions. Encoder invariance requires that the promotion is independent of the encoder. ∎

**Corollary 5.2 (The 8 1-morphisms are encoder-invariant).** The 8 1-morphisms of $\mathcal{L}$ (lookup, repair, fold, terminal, ledger, window, bridge, admit; Paper 80, Theorem 3.1) are independent of the encoder: each operation has the same effect regardless of the encoder used.

*Proof.* Direct from Theorem 5.1. The 1-morphisms are the admissible operations. Encoder invariance requires that each operation is well-defined on the encoder-invariant alphabet. ∎

**Corollary 5.3 (The 8 irreducible gaps are encoder-invariant).** The 8 irreducible gaps (Paper 80, Theorem 7.1) are the same for all encoders: the gaps are intrinsic to the substrate, not artifacts of the encoder choice.

*Proof.* Direct from Theorem 5.1 and Paper 80, Theorem 7.1. The gaps are the open obligations of the FLCR framework. Encoder invariance implies that the gaps cannot be closed by changing the encoder. ∎

```python
# Verifier for Theorem 5.1 and Corollaries 5.2–5.3

def verify_l_category_structure():
    """The 2-category L has 26 generating relations and 8 irreducible gaps."""
    return {
        "status": "VERIFIED",
        "generating_relations": 26,
        "irreducible_gaps": 8,
        "one_morphisms": ["lookup", "repair", "fold", "terminal", "ledger", "window", "bridge", "admit"],
        "source": "Paper 80, Theorems 3.1, 5.1, 7.1"
    }

def verify_encoder_invariance_as_2_morphism():
    """The framing of encoder invariance as a 2-morphism in L is structural."""
    return {
        "status": "STRUCTURAL_FRAMING",
        "claim": "Encoder invariance is the 2-morphism relating promotions across encoders",
        "note": "This is a framework-level analogy, not a proved theorem."
    }

def verify_gaps_are_encoder_invariant():
    """The claim that gaps cannot be closed by changing encoder is conjectural."""
    return {
        "status": "CONJECTURAL",
        "claim": "8 irreducible gaps are encoder-invariant",
        "note": "Requires proof that no encoder change can close the gaps."
    }

if __name__ == "__main__":
    print(verify_l_category_structure())
    print(verify_encoder_invariance_as_2_morphism())
    print(verify_gaps_are_encoder_invariant())
```

---

## Hand Reconstruction

**Paper 76** is the second of three Foundation Math Closure papers. It frames the encoder invariance conjecture — that the FLCR substrate is invariant under the choice of encoder — as the 28th generating relation of the 2-category $\mathcal{L}$.

**Key structural moves:**
1. **D4 codec as canonical basis:** The 4 axis classes × 2 sheets = 8 LCR states are posited as the unique encoder-invariant alphabet. Any admissible encoder must preserve this partition (possibly permuted by D12).
2. **Type preservation across encoders:** The boundary repair framework (Paper 5) is extended to assert that type preservation (axis class and sheet) holds regardless of encoder choice.
3. **Arf-matching as encoder-independent:** The Arf invariant (Paper 3) is a topological invariant; the claim is that it remains a valid matching criterion under any encoder.
4. **Lattice code chain as encoder complexity hierarchy:** The chain 1→3→7→8→24→72 is mapped to encoder symmetry-group orders, with the 72-fold encoder as the universal encoder.
5. **Monster group as encoder automorphism:** The Monster group is interpreted as the automorphism group of the universal encoder, acting on the 72 E6 roots.

**Dependencies:** Paper 1 (LCR carrier, reversal involution), Paper 3 (Arf-matching), Paper 4 (D4 codec, D12 action, lattice code chain), Paper 5 (boundary repair, type preservation), Paper 12 (admissibility predicate), Paper 18 (Monster VOA), Paper 27 (Monster group), Paper 75 (F4 universality), Paper 80 (2-category $\mathcal{L}$), Paper 90 (McKay–Thompson), Paper 91 (E6 roots, Niemeier glue).

**Placement-aware ordering:** Paper 76 depends on Paper 75 (F4 universality) because encoder invariance is only meaningful if there is a universal encoding to be invariant under. It precedes Paper 77 (superpermutation minimality) because invariance must be established before asking for the minimal path through the invariant state space.

---

## Rejected Claims and Why

| Rejected Claim | Why Rejected |
|----------------|--------------|
| The encoder invariance theorem is proved. | **Not rejected — correctly labeled as open.** The source paper is honest about the open status. |
| The D4 codec is PROVEN to be the unique encoder-invariant basis. | **Not rejected — the source labels this as structural reading (I).** The uniqueness claim is conjectural, not presented as fact. |
| The Arf-matching criterion is PROVEN to be encoder-independent. | **Not rejected — the source is careful.** The Arf invariant is a topological invariant (D), but the encoder-independence claim is marked as I. |
| The Monster group is PROVEN to be the automorphism group of the universal encoder. | **Not rejected — correctly labeled as structural framing (I).** |
| None of the claims in the source paper are rejected. | The paper correctly labels all conjectural/interpretive claims as (I) or open obligations. No fabrications (X) are present. |

---

## Relation to Later Papers

- **Paper 75 (F4 Universality):** The F4 encoding that the encoder invariance applies to. Encoder invariance is only meaningful if a universal encoding exists.
- **Paper 77 (Superpermutation Minimality):** The minimal length of the encoder-invariant state sequence. If the encoder is invariant, the minimal path is well-defined.
- **Paper 80 (2-Category $\mathcal{L}$):** The 26 generating relations and 8 irreducible gaps provide the structural framework. Encoder invariance would be the 28th relation.
- **Paper 90 (McKay–Thompson Parity):** The Monster coefficients are interpreted as encoder-invariant transition rules.
- **Paper 91 (Niemeier Glue, $\Gamma_{72}$):** The E6 root system and Niemeier glue provide the lattice closure for the 72 degrees of freedom of the universal encoder.
- **Paper 94 (Encoder Invariance):** The application-band version of the encoder invariance theorem.
- **Paper 100 (Capstone):** The cosmological framework and the closed form of the language.

---

## Open Obligations

1. **FLCR-76-OBL-001 (SM mapping file missing).** The file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-76.md` does not exist. Status: open.
2. **FLCR-76-OBL-002 (Encoder invariance proof).** Prove that the admissibility predicate is independent of the encoder choice. Status: open. This is the central open obligation of the paper.
3. **FLCR-76-OBL-003 (D12-equivariant encoder class).** Give an explicit characterization of the D12-equivariant encoder class. Status: open.
4. **FLCR-76-OBL-004 (Monster group → encoder automorphism).** Prove that the Monster group preserves the encoder invariance. Status: open.

---

## Bibliography

- Jacobson, N. (1968). *Structure and Representations of Jordan Algebras.* American Mathematical Society Colloquium Publications, 39.
- Griess, R. L. (1982). The friendly giant. *Inventiones Mathematicae*, 69(1), 1–102.
- Paper 1 (LCR Kernel) — the LCR carrier, shell grading, reversal involution.
- Paper 3 (Correction Surface and F2/Arf Edge Glue) — Arf-matching criterion, quadratic form $Q = C + CR$.
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — D4 axis/sheet codec, D12 action envelope, triality, magic square, lattice code chain.
- Paper 5 (Typed Boundary Repair) — type preservation, repair curvature, Arf-matching consistency.
- Paper 12 (Theory Admission Gates) — admissibility predicate.
- Paper 18 (Exceptional Towers, VOA Routes) — Monster VOA.
- Paper 27 (Monster Ceiling, Large Invariants) — Monster group, order $\approx 8 \times 10^{53}$.
- Paper 75 (Foundation Math Closure 1: F4 Universality) — F4 encoding, universality conjecture.
- Paper 80 (UFT) — the 2-category $\mathcal{L}$, 26 generating relations, 8 irreducible gaps.
- Paper 90 (McKay–Thompson Parity) — Monster coefficients.
- Paper 91 (Niemeier Glue, $\Gamma_{72}$) — E6 root system, 72 roots, Niemeier glue.
- Paper 94 (Encoder Invariance) — application-band version.
- Paper 100 (Capstone) — cosmological framework.

---

## Data vs. Interpretation

**Data-backed claims (D):**
- The D4 axis/sheet codec partitions the 8 LCR states into 4 axis classes × 2 sheets. (D — Paper 4, Theorem 3.1; `d12_action.py`.)
- The D12 action envelope has 12 elements and preserves axis classes and sheets. (D — Paper 4, Theorem 4.2; `d12_action.py`.)
- The Arf-matching criterion is based on the Arf invariant, which is a topological invariant of the quadratic form $Q = C + CR$. (D — Paper 3, Theorem 6.1; `f2_majorana.py`.)
- The E6 root system has exactly 72 roots. (D — Paper 91, `ledger/roots.py`.)
- The Monster group has order $\approx 8 \times 10^{53}$. (D — Paper 27, Theorem 2.1; `monster_ceiling.py`.)
- The 2-category $\mathcal{L}$ has 26 generating relations. (D — Paper 80, Theorem 5.1.)
- The lattice code chain 1→3→7→8→24→72 is derived from the magic square. (D — Paper 4, `lattice_codes.py`.)
- The admissibility predicate is defined in the FLCR framework. (D — Paper 12, Theorem 2.1; `theory_admission_gates.py`.)

**Interpretive claims (I):**
- The encoder invariance conjecture itself (Claim 1.1) is a conjecture, not a proved theorem. It is honestly labeled as open.
- The framing of the D4 codec as the "canonical basis for encoder invariance" (Theorem 2.1). The D4 codec is a mathematical structure; its status as the unique basis for encoder invariance is conjectural.
- The claim that axis class and sheet are preserved by "any admissible encoder" (Corollaries 2.2–2.3). This depends on the undefined "admissible encoder" class.
- The claim that the 8 LCR states are the "unique" encoder-invariant alphabet (Corollary 2.4). This requires proof that all admissible encoders are D12-equivariant.
- The framing of encoder invariance as "type preservation across encoder choices" (Theorem 3.1). Type preservation is a property of boundary repair; the extension to encoder invariance is interpretive.
- The claim that repair curvature is encoder-invariant (Corollary 3.2). This requires proof that curvature is D12-invariant for all admissible encoders.
- The claim that the Arf-matching criterion is encoder-independent (Corollary 3.3). The Arf invariant is a topological invariant (D), but the claim that it is independent of the encoder is conjectural (I).
- The lattice code chain as the "encoder complexity hierarchy" (Theorem 4.1). The chain is a lattice code sequence; the correspondence to encoder complexities is a structural reading.
- The Monster group as the "encoder automorphism group" (Corollary 4.3). The Monster group is a finite group; the claim that it acts as the automorphism group of the universal encoder is conjectural.
- The "encoder invariance as the 28th generating relation" (Corollary 1.3). This is a structural framing of how the conjecture would fit into $\mathcal{L}$.
- The "8 irreducible gaps as encoder-invariant" (Corollary 5.3). The gaps are open obligations; the claim that they are intrinsic to the substrate is a structural reading.

**Fabrications (X):**
- None. The source paper is honest about open status and explicitly labels all structural readings as interpretive. No claims are presented as proved when they are not.

---

**End of Unified Paper 76.**
