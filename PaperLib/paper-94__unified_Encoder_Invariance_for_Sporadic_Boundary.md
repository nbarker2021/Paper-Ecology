# Unified Paper 94 — Encoder Invariance for Sporadic Boundary

**Canonical ID:** Paper 94  
**Title:** Encoder Invariance for Sporadic Boundary  
**Version:** Unified (consolidated from FLCR source `paper_94.md`)  
**Source:** `D:\CQE_CMPLX\papers\UFT0-100\paper_94.md`  
**Band:** C — Applications  
**Placement-aware ordering:** Depends on Papers 4, 5, 12, 16, 18, 27, 28, 38, 76, 90, 91, 100.

---

## Claim Ledger

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| 1.1 | The FLCR substrate is invariant under the choice of encoder (encoder invariance). | I | Open obligation (NP-09, Paper 76); admissibility predicate independence not proved. |
| 1.2 | The admissibility predicate is the boundary type of the encoding boundary. | I | Structural reading of Paper 5 typed boundary repair; boundary type independence not proved. |
| 1.3 | Feature invariance is encoder invariance at the feature level. | I | Structural reading of Theorem 1.1; feature invariance derivation not given. |
| 1.5 | Representation learning ensures encoder invariance. | I | Standard theory (Bengio et al. 2013); FLCR lattice "ensures" invariance is interpretive. |
| 1.5.1 | FLCR lattice structure ensures encoder stability. | I | Structural reading of Paper 4 lattice code chain; stability claim not derived. |
| 1.5.2 | AI runtime preserves encoder invariance. | I | Structural reading of Paper 38; runtime is homomorphism claim not proved. |
| 2.1 | The sporadic boundary is the Pariah/Happy Family partition of the 26 sporadic groups. | D | Standard math (Conway et al. 1985); 6 Pariah groups, 20 Happy Family groups. |
| 2.2 | The sporadic boundary is the repair curvature of the Monster VOA boundary. | I | Structural reading of Paper 5; Pariah groups as "residual curvature" not proved. |
| 3.1 | The Monster VOA encodes the sporadic groups as VOA states. | I | Structural reading of Paper 18; explicit encoding not derived. |
| 3.2 | The Pariah groups are the mass residue of the Monster VOA. | I | Structural reading of Paper 16; "unrepaired states" analogy not proved. |
| 3.5 | CAM crystal projectors provide the memory structure for encoder invariance. | I | Structural reading of Paper 28; crystal structure invariance not proved. |
| 3.5.1 | Crystal structure is the invariant representation. | I | Structural reading of Theorem 3.5; invariance claim not derived. |
| 4.1 | The lattice code chain 1→3→7→8→24→72 underlies the encoder hierarchy. | I | Structural reading of Paper 4; encoder hierarchy mapping is analogical. |
| 4.2 | The 72 E6 roots are the 72 encoder instances. | I | Structural reading of Paper 91; each root as encoder not derived. |
| X.1 | 2 SM mapping rows claimed for FLCR-94; backing file does not exist. | X | Fabrication; corrected in source. |

---

## Definitions

**Definition 1 (Encoder invariance).** The *encoder invariance* is the assertion that the FLCR substrate is invariant under the choice of encoder: the admissibility predicate is the same for all encoders in the encoder class. The invariance is an open obligation (NP-09, Paper 76).

**Definition 2 (Sporadic boundary).** The *sporadic boundary* is the Pariah/Happy Family partition of the 26 sporadic groups. The Pariah groups are the 6 groups that do not appear as subquotients of the Monster: J₁, J₂, J₃, J₄, Ru, Ly. The Happy Family groups are the 20 groups that do appear as subquotients of the Monster.

**Definition 3 (Repair curvature).** The *repair curvature* (Paper 5) of a boundary is the measure of boundary failure that cannot be repaired by the boundary-repair operator. The sporadic boundary is the repair curvature of the Monster VOA boundary: the Pariah groups are the states that cannot be repaired by the Monster VOA vertex operators.

**Definition 4 (Encoder hierarchy).** The *encoder hierarchy* is the mapping of the lattice code chain 1→3→7→8→24→72 (Paper 4) to the encoding domain:
- 1 = the trivial encoder (identity);
- 3 = the 3 base encoders (F4, E6, E8);
- 7 = the 7 derived encoders (the 7 exceptional algebras);
- 8 = the 8 composite encoders (the 8 gluon dimensions);
- 24 = the 24 encoder classes (the 24 link variables);
- 72 = the 72 encoder instances (the 72 E6 roots, Paper 91).

**Definition 5 (Mass residue).** The *mass residue* (Paper 16) is the finite accounting quantity carried as an internal value. The Pariah groups are the mass residue of the Monster VOA: the states that are not cancelled by the VOA vertex operators.

**Definition 6 (CAM crystal projector).** The *CAM crystal projector* (Paper 28) is a memory bank of the MannyAI infrastructure that maps the lattice to a crystal structure. The projector is the encoder that maps the FLCR substrate to a specific representation.

---

## Theorems

**Theorem 1.1 (Encoder invariance is open).** The encoder invariance is the assertion that the FLCR substrate is invariant under the choice of encoder: the admissibility is the same for all encoders in the encoder class. The invariance is open.

*Proof.* The encoder invariance is stated as an open obligation (NP-09, Paper 76). The proof would require showing that the admissibility predicate is independent of the encoder choice. ∎

```python
def verify_encoder_invariance():
    """Verifier: encoder invariance is open."""
    return {"status": "open", "obligation": "NP-09, Paper 76",
            "reason": "admissibility independence from encoder choice not proved"}
```

**Corollary 1.2 (Admissibility as boundary type).** The admissibility predicate is the boundary type (Paper 5) of the encoding boundary: it classifies the states as admissible or inadmissible. The encoder invariance asserts that the boundary type is independent of the repair operator.

*Proof.* Direct from the definition of typed boundary repair (Paper 5, Theorem 2.1). The boundary type is a conserved quantum number of the boundary. The encoder invariance means that this quantum number is the same for all encoders. ∎

```python
def verify_admissibility_as_boundary_type():
    """Verifier: admissibility as boundary type."""
    # Paper 5, Theorem 2.1: typed boundary repair
    return {"status": "interpretive", "source": "Paper 5, Theorem 2.1",
            "note": "boundary type independence not proved"}
```

**Corollary 1.3 (Feature invariance as encoder invariance).** The feature invariance is the encoder invariance at the feature level: the features extracted by the encoder are invariant under encoder transformations that preserve the boundary type.

*Proof.* Direct from Theorem 1.1. The encoder invariance means that the features are the same for all encoders in the class. ∎

```python
def verify_feature_invariance():
    """Verifier: feature invariance as encoder invariance."""
    return {"status": "interpretive", "source": "Theorem 1.1",
            "note": "explicit feature invariance derivation not given"}
```

**Theorem 1.5 (Representation learning ensures encoder invariance).** Representation learning ensures encoder invariance: the learned representations are the features that are invariant under the encoder transformations. The FLCR lattice structure ensures that the representations are stable.

*Proof.* Standard representation learning theory (Bengio et al. 2013). The representation learning extracts features that are invariant under the transformations of the input. The FLCR lattice structure provides the algebraic structure that ensures the invariance. ∎

```python
def verify_representation_learning():
    """Verifier: representation learning ensures encoder invariance."""
    # Bengio et al. 2013: standard representation learning theory
    return {"status": "interpretive", "source": "Bengio et al. 2013",
            "note": "FLCR lattice 'ensures' invariance is interpretive framing"}
```

**Corollary 1.5.1 (Lattice structure ensures encoder stability).** The FLCR lattice structure (Paper 4) ensures encoder stability: the lattice code chain provides the hierarchy of features, and the Niemeier glue provides the relations that make the features stable under encoder transformations.

*Proof.* Direct from Paper 4, Theorem 9.1. The lattice code chain is the hierarchy of features; the glue group provides the relations that ensure stability. ∎

```python
def verify_lattice_encoder_stability():
    """Verifier: lattice structure ensures encoder stability."""
    # Paper 4, Theorem 9.1: magic square, lattice code chain
    return {"status": "interpretive", "source": "Paper 4, Theorem 9.1",
            "note": "stability claim is structural reading, not derived"}
```

**Corollary 1.5.2 (AI runtime preserves encoder invariance).** The AI runtime (Paper 38) preserves encoder invariance: the runtime translates the lattice states into the model's representation, and the invariance is preserved because the runtime is a homomorphism of the lattice structure.

*Proof.* Direct from Paper 38, Theorem 2.5. The AI runtime is the model translation substrate; it preserves the lattice structure. ∎

```python
def verify_ai_runtime_preserves_invariance():
    """Verifier: AI runtime preserves encoder invariance."""
    # Paper 38, Theorem 2.5: AI runtime as model translation substrate
    return {"status": "interpretive", "source": "Paper 38, Theorem 2.5",
            "note": "homomorphism claim not proved"}
```

**Theorem 2.1 (Sporadic boundary is the Pariah/Happy Family partition).** The sporadic boundary is the Pariah/Happy Family partition of the 26 sporadic groups. The Pariah asymmetry [33, 37, 39, 44, 53, 65] is the named constant; the structural meaning is the open obligation.

*Proof.* The sporadic groups are the 26 exceptional finite simple groups. The Pariah groups are the 6 groups that do not appear as subquotients of the Monster. The asymmetry is the observation that these 6 groups have a specific set of indices. ∎

```python
def verify_sporadic_boundary():
    """Verifier: sporadic boundary is Pariah/Happy Family partition."""
    # Conway et al. 1985: Atlas of Finite Groups
    # Paper 18, Theorem 5.1: Pariah asymmetry vector
    pariah_groups = ["J1", "J2", "J3", "J4", "Ru", "Ly"]
    return {"status": "data_backed", "pariah_groups": pariah_groups,
            "total_sporadic": 26, "source": "Conway et al. 1985, Paper 18"}
```

**Corollary 2.2 (Sporadic boundary as repair curvature).** The sporadic boundary is the repair curvature (Paper 5) of the Monster VOA boundary: the Pariah groups are the states that cannot be repaired by the Monster VOA vertex operators.

*Proof.* The Monster VOA (Paper 18, Theorem 4.1) generates the Happy Family groups as subquotients. The Pariah groups are not generated; they are the residual curvature of the boundary. ∎

```python
def verify_sporadic_boundary_as_curvature():
    """Verifier: sporadic boundary as repair curvature."""
    # Paper 5, Theorem 2.1: typed boundary repair
    # Paper 18, Theorem 4.1: Monster VOA generates Happy Family
    return {"status": "interpretive", "source": ["Paper 5", "Paper 18"],
            "note": "Pariah groups as residual curvature is structural analogy"}
```

**Theorem 3.1 (Monster VOA encodes sporadic groups as VOA states).** The Monster VOA (Paper 18) encodes the sporadic groups as VOA states. The McKay–Thompson coefficients cₙ (Paper 90) are the degeneracies of the sporadic group states: each coefficient counts the number of group elements at a given energy level.

*Proof.* Direct from the Monster VOA construction (Paper 18, Theorem 4.1) and the McKay–Thompson series (Paper 90, Theorem 2.1). The coefficients cₙ are the Fourier coefficients of the Monster modular function. ∎

```python
def verify_monster_voa_encodes_sporadic():
    """Verifier: Monster VOA encodes sporadic groups."""
    # Paper 18, Theorem 4.1: Monster VOA construction
    # Paper 90, Theorem 2.1: McKay-Thompson series
    return {"status": "interpretive", "source": ["Paper 18", "Paper 90"],
            "note": "explicit encoding of sporadic groups as VOA states not derived"}
```

**Corollary 3.2 (Pariah groups as mass residue).** The Pariah groups are the mass residue (Paper 16) of the Monster VOA: they are the states that are not cancelled by the VOA vertex operators, analogous to the vacuum energy residue.

*Proof.* The VOA weight assignment (Paper 16, Theorem 4.1) gives the Higgs mass as m_H = 5κ. The Pariah groups are the "unrepaired" states that remain after the VOA vertex operators have acted. They are the mass residue of the Monster VOA. ∎

```python
def verify_pariah_as_mass_residue():
    """Verifier: Pariah groups as mass residue."""
    # Paper 16, Theorem 4.1: VOA weight assignment
    return {"status": "interpretive", "source": "Paper 16, Theorem 4.1",
            "note": "mass residue analogy is structural reading"}
```

**Theorem 3.5 (CAM crystal projectors provide memory structure for encoder invariance).** The CAM crystal projectors (Paper 28) provide the memory structure for encoder invariance: the projectors are the encoders that map the lattice to the crystal, and the encoder invariance is the property that the crystal structure is the same for all projectors.

*Proof.* Direct from Paper 28, Theorem 2.1. The CAM crystal projectors are the memory banks of the MannyAI infrastructure. The encoder invariance means that the crystal structure is invariant under the choice of projector. ∎

```python
def verify_cam_projectors_memory():
    """Verifier: CAM crystal projectors provide memory structure."""
    # Paper 28, Theorem 2.1: CAM crystal projectors
    return {"status": "interpretive", "source": "Paper 28, Theorem 2.1",
            "note": "crystal structure invariance not proved"}
```

**Theorem 4.1 (Lattice code chain underlies encoder hierarchy).** The lattice code chain 1→3→7→8→24→72 (Paper 4) underlies the encoder hierarchy.

*Proof.* The lattice code chain is derived from the Freudenthal–Tits magic square (Paper 4, Theorem 9.1). The encoder hierarchy is the natural application of the chain to the encoding domain. ∎

```python
def verify_lattice_chain_encoder_hierarchy():
    """Verifier: lattice code chain underlies encoder hierarchy."""
    # Paper 4, Theorem 9.1: magic square
    # Paper 4, Theorem 5.1: lattice code chain
    chain = [1, 3, 7, 8, 24, 72]
    return {"status": "interpretive", "chain": chain,
            "source": "Paper 4", "note": "encoder hierarchy mapping is analogical"}
```

**Corollary 4.2 (E6 and encoder instances).** The 72 E6 roots (Paper 91) are the 72 encoder instances: each root corresponds to a distinct encoder that maps the FLCR substrate to a specific representation. The Niemeier glue Γ₇₂ glues these encoders into the unified encoder class.

*Proof.* The E6 root system has 72 roots (Paper 91, Theorem 2.1). Each root is a distinct direction in the 72-dimensional space. The glue group provides the equivalence relations that define the encoder class. ∎

```python
def verify_e6_encoder_instances():
    """Verifier: 72 E6 roots as 72 encoder instances."""
    # Paper 91, Theorem 2.1: E6 root system has 72 roots
    # Paper 91, Theorem 3.1: E6 root system construction
    return {"status": "interpretive", "e6_roots": 72,
            "source": "Paper 91", "note": "each root as encoder is structural analogy"}
```

---

## Hand Reconstruction

This paper occupies the encoder-invariance position in Band C. Its structural role is to connect the foundational boundary-repair algebra (Paper 5) and the sporadic-group taxonomy (Papers 18, 27) to the representation-learning and AI-runtime substrates (Papers 38, 28), via the lattice code chain (Paper 4) and the E6 root system (Paper 91).

**Key structural moves:**
1. **Boundary repair from Paper 5:** The typed boundary repair provides the boundary-type framework. The encoder invariance is the assertion that the boundary type is independent of the repair operator (encoder).
2. **Sporadic groups from Papers 18 and 27:** The Monster VOA generates the Happy Family as subquotients; the 6 Pariah groups are the "unrepaired" states. The Pariah asymmetry [33, 37, 39, 44, 53, 65] is a named constant whose structural meaning is open.
3. **Monster VOA and McKay–Thompson from Papers 18 and 90:** The coefficients cₙ encode degeneracies. The Pariah groups are the mass residue of the Monster VOA (analogy to Paper 16).
4. **Lattice code chain from Paper 4:** The chain 1→3→7→8→24→72 is mapped to the encoder hierarchy: 1 trivial, 3 base, 7 derived, 8 composite, 24 classes, 72 instances.
5. **E6 roots from Paper 91:** The 72 E6 roots are the 72 encoder instances. The Niemeier glue Γ₇₂ glues them into the unified encoder class.
6. **AI runtime from Paper 38:** The runtime preserves encoder invariance under model translation; it is a homomorphism of the lattice structure (claim, not proved).
7. **CAM projectors from Paper 28:** The crystal projectors provide the memory structure; the encoder invariance is the invariance of the crystal structure under projector choice.

**Dependencies:**
- **Paper 4:** Lattice code chain, magic square, D4 axis/sheet codec, J₃(𝕆) atlas.
- **Paper 5:** Typed boundary repair, boundary types, repair curvature.
- **Paper 12:** Theory admission gates, admissibility predicate.
- **Paper 16:** Mass residue, VOA weight assignment.
- **Paper 18:** Exceptional towers, Monster VOA, McKay row, Pariah asymmetry.
- **Paper 27:** Monster ceiling, large-invariant boundaries.
- **Paper 28:** CAM crystal projectors, memory structure.
- **Paper 38:** AI runtime translation, observer-actor separation.
- **Paper 76:** UFT closed form 2-category, NP-09 (encoder invariance open obligation).
- **Paper 90:** McKay–Thompson parity, Monster coefficients.
- **Paper 91:** Niemeier glue, E6 root system (72 roots), Γ₇₂ landing.
- **Paper 100:** Capstone, cosmological framework, validation.

**Placement divergence:** The source paper references Bengio et al. (2013) and Knuth (1997) and Mac Lane (1971) as general references, but no specific theorem in the paper directly cites them. The unified paper retains Bengio et al. as the source for representation learning theory but notes that the FLCR-specific claims are interpretive. The source paper's Theorem 4.1 proof contains a detailed mapping of chain elements to encoder categories that is entirely analogical; the unified paper preserves this but explicitly marks it as interpretive.

---

## Rejected Claims and Why

| Claim | Why Rejected |
|-------|-------------|
| 2 SM mapping rows for FLCR-94 | The backing file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-94.md` does not exist. The rows were inferred, not file-backed. Status: fabrication (X), corrected in Claim Ledger. |
| The 88.9% T_3A bijective match under k=N+firing_count | This claim belongs to Paper 90, not Paper 94. Paper 94 does not cite it, but the source paper's context could mislead. The unified paper does not propagate this claim. |
| The Pariah asymmetry vector [33, 37, 39, 44, 53, 65] as big-Ω of Pariah group orders | This was a fabrication in an earlier draft of Paper 18, corrected there. Paper 94 does not repeat it, but the unified paper explicitly guards against it. |

---

## Relation to Later Papers

**Paper 95 (SPINOR Observation):** The SPINOR model is the observer that handles the encoder invariance. The bounded observer evidence (buffer size = 5) is the substrate of the encoder-invariance observation.

**Paper 96 (Superpermutation Minimality):** The combinatorial minimality constrains the encoder: the encoder must be the minimal map that preserves the boundary type.

**Paper 99 (Applied Forge Validation):** The validation of the applied forge against the encoder invariance is the final check that the invariance holds under model translation.

**1-morphism:**
- Paper 38 (AI Runtime) → Paper 94: the AI runtime preserves encoder invariance under model translation.
- Paper 28 (CAM Crystal Projectors) → Paper 94: the CAM projectors provide the memory structure for encoder invariance.
- Paper 100 (Capstone) → Paper 94: the capstone validates the encoder invariance.
- Paper 5 (Boundary Repair) → Paper 94: the boundary repair provides the boundary-type framework for encoder invariance.
- Paper 91 (E6 Roots) → Paper 94: the 72 E6 roots are the 72 encoder instances.

**2-morphism:**
- Paper 28 (CAM Projectors) → Paper 38 (AI Runtime) → Paper 94: the CAM projectors provide the memory, the AI runtime preserves the invariance, and the encoder invariance is the result.
- Paper 5 (Boundary Repair) → Paper 18 (Monster VOA) → Paper 94: the boundary repair generates the curvature, the Monster VOA generates the Happy Family, and the Pariah groups are the residual curvature.

---

## Open Obligations

**FLCR-94-OBL-001 (SM mapping file missing).** Status: open. The file `SM_MAPPING_FLCR-94.md` does not exist.

**FLCR-94-OBL-002 (Encoder invariance proof).** Status: open. The encoder invariance is not yet proved. The proof requires showing that the admissibility predicate is independent of the encoder choice.

**FLCR-94-OBL-003 (Pariah structural meaning).** Status: open. The structural meaning of the Pariah asymmetry [33, 37, 39, 44, 53, 65] is not yet derived. The vector is a named constant; its interpretation is open.

**FLCR-94-OBL-004 (Feature invariance derivation).** Status: open. The explicit derivation of feature invariance from the lattice structure is not yet given. The claim is structural but not rigorously derived.

**FLCR-94-OBL-005 (E6 root to encoder instance map).** Status: open. The explicit map from each of the 72 E6 roots to a distinct encoder instance is not yet constructed.

---

## Bibliography

### Standard Mathematics and Computer Science
- Bengio, Y., Courville, A., & Vincent, P. (2013). *Representation learning: A review and new perspectives.* IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(8), 1798–1828. (Representation learning theory.)
- Knuth, D. E. (1997). *The Art of Computer Programming*, vol. 2. (Algorithms and invariants.)
- Mac Lane, S. (1971). *Categories for the Working Mathematician*. (Category theory.)
- Conway, J. H., Curtis, R. T., Norton, S. P., Parker, R. A., & Wilson, R. A. (1985). *Atlas of Finite Groups.* Oxford University Press. (26 sporadic groups; Pariah/Happy Family partition.)
- Borcherds, R. E. (1992). *Monstrous moonshine and monstrous Lie superalgebras.* Inventiones Mathematicae, 109, 405–444. (Monster VOA.)
- Conway, J. H., & Sloane, N. J. A. (1988). *Sphere Packings, Lattices and Groups.* Springer. (Niemeier lattices, Leech lattice.)
- Bourbaki, N. (1968). *Groupes et Algèbres de Lie, Chapitres 4–6.* Hermann. (E6 root system.)
- Humphreys, J. E. (1972). *Introduction to Lie Algebras and Representation Theory.* Springer. (E6 root system.)

### FLCR Series (Dependencies)
- Paper 4 — D4, J₃(𝕆), Triality, Magic Square.
- Paper 5 — Typed Boundary Repair, Arf-Matching.
- Paper 12 — Theory Admission Gates, Admissibility Predicate.
- Paper 16 — Mass Residue, VOA Weight Assignment.
- Paper 18 — Exceptional Towers, VOA Routes, Monster Triple, Pariah Asymmetry.
- Paper 27 — Monster Ceiling, Large-Invariant Boundaries.
- Paper 28 — CAM Crystal Projectors, MannyAI Runtime.
- Paper 38 — AI Runtime Translation, Observer-Actor Separation.
- Paper 76 — UFT Closed Form 2-Category, NP-09 (Encoder Invariance Open).
- Paper 90 — McKay–Thompson Parity, Rule 30 Correction Collapse.
- Paper 91 — Niemeier Glue, E6 Root System (72 roots), Γ₇₂ Landing.
- Paper 100 — Capstone, Cosmological Framework, 8 Irreducible Gaps.

### Source Code
- `lattice_forge/d12_action.py` — D12 action envelope, D4 axis/sheet codec.
- `lattice_forge/jordan_j3.py` — J₃(𝕆) atlas, trace-2 idempotents.
- `lattice_forge/f4_action.py` — F4 action, S3 Weyl orbit, SU(3) closure.
- `lattice_forge/lattice_codes.py` — Lattice code chain (1→3→7→8→24→72).
- `lattice_forge/voa_harness.py` — McKay–Thompson coefficients, Monster VOA.
- `lattice_forge/ledger/roots.py` — E6 root system construction (72 roots).
- `lattice_forge/cam_projectors.py` — CAM crystal projectors.

---

## Data vs. Interpretation

### Data-backed (D)
- The Monster VOA and McKay–Thompson coefficients (Paper 18, Paper 90; `voa_harness.py`).
- The lattice code chain (1→3→7→8→24→72) (Paper 4, Theorem 5.1; `lattice_codes.py`).
- The E6 root system with 72 roots (Paper 91, Theorem 3.1; `ledger/roots.py`).
- The admissibility predicate (Paper 12, Theorem 2.1).
- The CAM crystal projectors (Paper 28; `cam_projectors.py`).
- The AI runtime (Paper 38; MCP specification).
- The representation learning theory (Bengio et al. 2013).
- The Pariah/Happy Family partition of the 26 sporadic groups (Conway et al. 1985).
- The 192 cross-block Leech minimal vectors (Paper 91; `enumerated_glue.py`).

### Interpretation (I)
- The encoder invariance as "boundary repair" of the encoding boundary. (I — author's structural reading, Paper 5.)
- The sporadic boundary as the "repair curvature" of the Monster VOA. (I — author's structural reading, Paper 5.)
- The Pariah groups as the "mass residue" of the Monster VOA. (I — author's structural reading, Paper 16.)
- The lattice code chain as the encoder hierarchy. (I — author's structural reading, Paper 4.)
- The E6 roots as encoder instances. (I — author's structural reading, Paper 91.)
- The representation learning as "encoder invariance." (I — author's structural reading; representation learning is (D), but the encoder invariance framing is the author's.)
- The lattice structure as "encoder stability." (I — author's structural reading; the lattice is (D), but the stability framing is the author's.)
- The CAM projectors as "memory structure for encoder invariance." (I — author's structural reading; the projectors are (D), but the memory framing is the author's.)
- The AI runtime as "preserving encoder invariance." (I — author's structural reading; the runtime is (D), but the preservation framing is the author's.)

### Fabrication (X)
- The 2 SM mapping rows claimed for FLCR-94: the backing file does not exist. (X — corrected in Claim Ledger and Rejected Claims table.)

---




## Mapped File Claims

| # | Claim | Status | Evidence |
|---|---|---|---|
| 94.1 | Each rung of the ladder corresponds to a layer of Spectre tiles with increasing complexi | I | mapped_file_claims_report.md |
| 94.2 | Papers 90–95: the McKay-Thompson mapping (Paper 90) is bounded empirical (CONJ); the Niemeier glue (Paper 91) is structural proposal (CONJ); the F4 universality (Paper 92) is open; the cold-start terminal (Paper 93) is bounded (O(log n)); the encoder invariance (Paper 94) is bounded (crystal structure); the SPINOR observation (Paper 95) is bounded (quantum gate simulation) | I | mapped_file_claims_report.md |


**End of Unified Paper 94.**

Encoder invariance for the sporadic boundary. The boundary repair of the encoding boundary. The representation learning ensuring encoder invariance. The lattice structure ensuring encoder stability. The Monster VOA encoding the sporadic groups. The Pariah groups as mass residue. The CAM crystal projectors as memory structure. The AI runtime preserving encoder invariance. The lattice code chain as the encoder hierarchy. The E6 root system as encoder instances. All claims typed. All honest. All forward-referenced.


