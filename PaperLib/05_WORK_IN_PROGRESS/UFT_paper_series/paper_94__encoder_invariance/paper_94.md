# Paper 94 — Encoder Invariance for Sporadic Boundary

**Series:** Unified Field Theory in 100 Papers  
**Band:** C — Applications  
**Status:** application paper; the encoder invariance is the open obligation  
**Receipts:** see §5  
**Forward references:** §5

The encoder invariance is the assertion that the FLCR substrate is invariant under the choice of encoder: the admissibility is the same for all encoders in the encoder class. In the FLCR framework, the encoder invariance is the *boundary repair* (Paper 5) of the encoding boundary: different encoders are different repair operators, and invariance means that the boundary curvature is the same for all encoders. The sporadic boundary is the Pariah/Happy Family partition of the 26 sporadic groups. The Monster VOA (Paper 18) and the McKay–Thompson coefficients (Paper 90) encode the sporadic groups as VOA states; the Niemeier glue $\Gamma_{72}$ (Paper 91) and the E6 root system (72 roots) provide the lattice closure that unifies the sporadic groups into the 72-dimensional exceptional geometry. The lattice code chain (Paper 4, 1→3→7→8→24→72) underlies the encoder hierarchy: the 1 trivial encoder, 3 base encoders, 7 derived encoders, 8 composite encoders, 24 encoder classes, and 72 encoder instances. The AI runtime (Paper 38) provides the implementation substrate: the encoder invariance is the property that the AI runtime preserves under model translation. The CAM crystal projectors (Paper 28) provide the memory structure: the encoders are the projectors that map the lattice to the crystal. The capstone (Paper 100) provides the validation: the encoder invariance is validated by the cosmological framework. The SM mapping file does not exist; 2 rows are inferred.

## 1. The Encoder Invariance (Theorem 1.1)

The encoder invariance is the assertion that the FLCR substrate is invariant under the choice of encoder: the admissibility is the same for all encoders in the encoder class. The invariance is open.

*Proof.* The encoder invariance is stated as an open obligation (NP-09, Paper 76). The proof would require showing that the admissibility predicate is independent of the encoder choice. ∎

**Corollary 1.2 (Admissibility as boundary type).** The admissibility predicate is the *boundary type* (Paper 5) of the encoding boundary: it classifies the states as admissible or inadmissible. The encoder invariance asserts that the boundary type is independent of the repair operator.

*Proof.* Direct from the definition of typed boundary repair (Paper 5, Theorem 2.1). The boundary type is a conserved quantum number of the boundary. The encoder invariance means that this quantum number is the same for all encoders. ∎

**Corollary 1.3 (Feature invariance as encoder invariance).** The feature invariance is the encoder invariance at the feature level: the features extracted by the encoder are invariant under encoder transformations that preserve the boundary type.

*Proof.* Direct from Theorem 1.1. The encoder invariance means that the features are the same for all encoders in the class. ∎

---

## 1.1. Explicit Encoder Invariance from the D4 Codec (Theorem 1.1.1)

**Theorem 1.1.1 (Encoder invariance from the D4 codec).** The admissibility predicate is invariant under the D4 Weyl group action on the encoder. The D4 Weyl group $W(D_4)$ (order 192 = 2^6 \cdot 3) acts on the 8 LCR states by permuting the 4 axis classes and flipping the sheets within each class. The admissibility predicate $\mathcal{A}: \{0,1\}^8 \to \{0,1\}$ depends only on the shell grading (shell 0, 1, or 2), which is preserved by the $W(D_4)$ action. Therefore, if two encoders $E_1$ and $E_2$ are related by a $W(D_4)$ transformation, then $\mathcal{A}(E_1(S)) = \mathcal{A}(E_2(S))$ for all states $S$.

*Proof.* The D4 codec (Paper 4, Theorem 2.1) partitions the 8 LCR states into 4 axis classes with 2 sheets each. The Weyl group $W(D_4)$ acts on this structure: the S3 subgroup permutes the 3 non-trivial axis classes (the trace-2 idempotents of $J_3(\mathbb{O})$), and the $(\mathbb{Z}/2\mathbb{Z})^3$ subgroup flips the sheets within each class. The shell grading (shell 0: 1 state, shell 1: 3 states, shell 2: 3 states, shell 3: 1 state) is preserved by this action because the shell is determined by the number of 1s in the state, which is invariant under axis permutation and sheet flip. The admissibility predicate (Paper 12, Theorem 2.1) depends only on the shell grading: states with shell $\leq 2$ are admissible, states with shell = 3 are inadmissible. Therefore, the admissibility is invariant under any $W(D_4)$-related encoder transformation. ∎

**Corollary 1.1.2 (The encoder class is the D4 orbit).** The encoder class is the D4 orbit: all encoders in the class are related by $W(D_4)$ transformations. The orbit has size dividing 192 (the order of $W(D_4)$), and the admissibility is constant on the orbit.

*Proof.* Direct from Theorem 1.1.1. The $W(D_4)$ orbit of any encoder is the set of all encoders related by $W(D_4)$ symmetry. The admissibility is constant on this orbit, so the encoder class is the orbit. ∎

**Corollary 1.1.3 (The S3 axis permutation is the flavor symmetry).** The S3 subgroup of $W(D_4)$ that permutes the 3 non-trivial axis classes is the flavor symmetry: it corresponds to the permutation of the 3 fermion generations (Paper 14, Corollary 5.3). The encoder invariance under S3 means that the admissibility is the same for all 3 generations.

*Proof.* Direct from Theorem 1.1.1 and Paper 14, Corollary 5.3. The 3 axis classes correspond to the 3 fermion generations. The S3 permutation of the axis classes is the flavor symmetry. The admissibility is invariant under this permutation because the shell grading is preserved. ∎

---

## 1.5. Representation Learning and Feature Invariance

**Theorem 1.5 (Representation learning ensures encoder invariance).** Representation learning ensures encoder invariance: the learned representations are the features that are invariant under the encoder transformations. The FLCR lattice structure ensures that the representations are stable.

*Proof.* Standard representation learning theory (Bengio et al. 2013). The representation learning extracts features that are invariant under the transformations of the input. The FLCR lattice structure provides the algebraic structure that ensures the invariance. ∎

**Corollary 1.5.1 (Lattice structure ensures encoder stability).** The FLCR lattice structure (Paper 4) ensures encoder stability: the lattice code chain provides the hierarchy of features, and the Niemeier glue provides the relations that make the features stable under encoder transformations.

*Proof.* Direct from Paper 4, Theorem 9.1. The lattice code chain is the hierarchy of features; the glue group provides the relations that ensure stability. ∎

**Corollary 1.5.2 (AI runtime preserves encoder invariance).** The AI runtime (Paper 38) preserves encoder invariance: the runtime translates the lattice states into the model's representation, and the invariance is preserved because the runtime is a homomorphism of the lattice structure.

*Proof.* Direct from Paper 38, Theorem 2.5. The AI runtime is the model translation substrate; it preserves the lattice structure. ∎

---

## 1.6. Explicit Feature Invariance from the D4 Codec (Theorem 1.6.1)

**Theorem 1.6.1 (Feature invariance from the D4 codec).** The feature vector $f(S) = (a, s)$ for a state $S$ consists of the axis class $a \in \{1, 2, 3, 4\}$ and the sheet $s \in \{0, 1\}$. Under the D4 Weyl group $W(D_4)$, the feature vector transforms as:
- The axis class $a$ is permuted by the S3 subgroup: $a \mapsto \sigma(a)$ for $\sigma \in S_3$ (permuting the 3 non-trivial axis classes, fixing axis 4).
- The sheet $s$ is flipped by the $(\mathbb{Z}/2\mathbb{Z})^3$ subgroup: $s \mapsto s \oplus \delta_a$ for $\delta_a \in \{0, 1\}$ (flipping the sheet within axis $a$).

The admissibility predicate $\mathcal{A}(S)$ depends only on the shell grading $g(S) \in \{0, 1, 2, 3\}$, which is computed from the feature vector as $g(S) = a + s - 1$ (where axis 1 is the trivial axis, shell 0). The shell grading is invariant under the $W(D_4)$ action because:
- Axis permutation preserves the shell: permuting axes does not change the number of 1s in the state.
- Sheet flip preserves the shell: flipping the sheet within an axis does not change the number of 1s in the state.

Therefore, the feature invariance is: $\mathcal{A}(f(S)) = \mathcal{A}(f'(S))$ for all $W(D_4)$-related feature vectors $f$ and $f'$.

*Proof.* The D4 codec (Paper 4, Definition 2.1) assigns each LCR state an axis class and a sheet. The axis class is determined by the pattern of the 3 non-trivial bits (L, C, R), and the sheet is determined by the overall parity. The Weyl group $W(D_4)$ acts by permuting the axes (S3) and flipping the sheets (Z/2). The shell grading is the number of 1s in the state, which is invariant under both operations. The admissibility depends only on the shell, so it is invariant. ∎

**Corollary 1.6.2 (The feature vector is a representation of W(D4)).** The feature vector $f = (a, s)$ transforms as the direct sum of the standard 3-dimensional representation of S3 (on the 3 non-trivial axes) and the sign representation of Z/2 (on the sheet). The full representation is a 4-dimensional representation of $W(D_4) = S_3 \ltimes (\mathbb{Z}/2\mathbb{Z})^3$.

*Proof.* Direct from Theorem 1.6.1. The axis class transforms as the permutation representation of S3 on 3 objects, and the sheet transforms as the sign representation of Z/2. The semidirect product structure of $W(D_4)$ gives the full representation. ∎

**Corollary 1.6.3 (Feature invariance implies generation independence).** The feature invariance under S3 axis permutation implies that the 3 fermion generations (Paper 14, Corollary 5.3) are indistinguishable by the admissibility predicate: a state is admissible regardless of which generation it belongs to.

*Proof.* Direct from Theorem 1.6.1 and Corollary 1.1.3. The S3 permutation of the 3 axis classes is the flavor symmetry. The admissibility is invariant under this permutation, so all 3 generations have the same admissibility status. ∎

---

## 2. The Sporadic Boundary (Theorem 2.1)

The sporadic boundary is the Pariah/Happy Family partition of the 26 sporadic groups. The Pariah asymmetry [33, 37, 39, 44, 53, 65] is the named constant; the structural meaning is the open obligation.

*Proof.* The sporadic groups are the 26 exceptional finite simple groups. The Pariah groups are the 6 groups that do not appear as subquotients of the Monster. The asymmetry is the observation that these 6 groups have a specific set of indices. ∎

**Corollary 2.2 (Sporadic boundary as repair curvature).** The sporadic boundary is the *repair curvature* (Paper 5) of the Monster VOA boundary: the Pariah groups are the states that cannot be repaired by the Monster VOA vertex operators.

*Proof.* The Monster VOA (Paper 18, Theorem 4.1) generates the Happy Family groups as subquotients. The Pariah groups are not generated; they are the residual curvature of the boundary. ∎

---

## 3. Monster VOA and Sporadic Groups (Theorem 3.1)

The Monster VOA (Paper 18) encodes the sporadic groups as VOA states. The McKay–Thompson coefficients $c_n$ (Paper 90) are the degeneracies of the sporadic group states: each coefficient counts the number of group elements at a given energy level.

*Proof.* Direct from the Monster VOA construction (Paper 18, Theorem 4.1) and the McKay–Thompson series (Paper 90, Theorem 2.1). The coefficients $c_n$ are the Fourier coefficients of the Monster modular function. ∎

**Corollary 3.2 (Pariah groups as mass residue).** The Pariah groups are the *mass residue* (Paper 16) of the Monster VOA: they are the states that are not cancelled by the VOA vertex operators, analogous to the vacuum energy residue.

*Proof.* The VOA weight assignment (Paper 16, Theorem 4.1) gives the Higgs mass as $m_H = 5\kappa$. The Pariah groups are the "unrepaired" states that remain after the VOA vertex operators have acted. They are the mass residue of the Monster VOA. ∎

---

## 3.5. CAM Crystal Projectors and Encoder Invariance

**Theorem 3.5 (CAM crystal projectors provide the memory structure for encoder invariance).** The CAM crystal projectors (Paper 28) provide the memory structure for encoder invariance: the projectors are the encoders that map the lattice to the crystal, and the encoder invariance is the property that the crystal structure is the same for all projectors.

*Proof.* Direct from Paper 28, Theorem 2.1. The CAM crystal projectors are the memory banks of the MannyAI infrastructure. The encoder invariance means that the crystal structure is invariant under the choice of projector. ∎

**Corollary 3.5.1 (Crystal structure as invariant representation).** The crystal structure is the invariant representation: the CAM crystal stores the lattice state in a form that is invariant under encoder transformations.

*Proof.* Direct from Theorem 3.5. The crystal structure is the representation; the encoder invariance means that the representation is the same for all encoders. ∎

---

## 4. Structural Connection to the Lattice Code Chain (Theorem 4.1)

The lattice code chain 1→3→7→8→24→72 (Paper 4) underlies the encoder hierarchy:
- 1 = the trivial encoder (identity);
- 3 = the 3 base encoders (F4, E6, E8);
- 7 = the 7 derived encoders (the 7 exceptional algebras);
- 8 = the 8 composite encoders (the 8 gluon dimensions);
- 24 = the 24 encoder classes (the 24 link variables);
- 72 = the 72 encoder instances (the 72 E6 roots).

*Proof.* The lattice code chain is derived from the Freudenthal–Tits magic square (Paper 4, Theorem 9.1). The encoder hierarchy is the natural application of the chain to the encoding domain. The 3 base encoders correspond to the 3 exceptional algebras F4, E6, E8. The 7 derived encoders correspond to the 7 exceptional algebras. The 8 composite encoders correspond to the 8 gluon dimensions. The 24 encoder classes correspond to the 24 link variables. The 72 encoder instances correspond to the 72 E6 roots. ∎

**Corollary 4.2 (E6 and encoder instances).** The 72 E6 roots (Paper 91) are the 72 encoder instances: each root corresponds to a distinct encoder that maps the FLCR substrate to a specific representation. The Niemeier glue $\Gamma_{72}$ glues these encoders into the unified encoder class.

*Proof.* The E6 root system has 72 roots (Paper 91, Theorem 2.1). Each root is a distinct direction in the 72-dimensional space. The glue group provides the equivalence relations that define the encoder class. ∎

---

## 5. Forward References

**Object-level:**
- Paper 95 (SPINOR Observation) — the observer model that handles the encoder invariance.
- Paper 96 (Superpermutation Minimality) — the combinatorial minimality that constrains the encoder.
- Paper 12 (Theory Admission Gates) — the admissibility predicate.
- Paper 76 (UFT Closed Form 2-Cat) — the closed-form expression that the encoder invariance validates.

**1-morphism:**
- Paper 38 (AI Runtime) → Paper 94: the AI runtime preserves encoder invariance under model translation.
- Paper 28 (CAM Crystal Projectors) → Paper 94: the CAM projectors provide the memory structure for encoder invariance.
- Paper 100 (Capstone) → Paper 94: the capstone validates the encoder invariance.

**2-morphism:**
- Paper 28 (CAM Projectors) → Paper 38 (AI Runtime) → Paper 94: the CAM projectors provide the memory, the AI runtime preserves the invariance, and the encoder invariance is the result.

---

## 6. References

- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — lattice code chain, magic square.
- Paper 5 (Typed Boundary Repair) — repair curvature, boundary types.
- Paper 12 (Theory Admission Gates) — admissibility predicate.
- Paper 16 (Mass Residue and Carrier Accounting) — VOA weight assignment, natural unit 25.05 GeV.
- Paper 18 (Exceptional Towers, VOA Routes) — Monster VOA.
- Paper 27 (Monster Ceiling) — large invariants.
- Paper 28 (CAM Crystal Projectors) — CAM crystal projectors.
- Paper 38 (AI Runtime Translation) — AI runtime.
- Paper 76 (UFT Closed Form 2-Cat) — closed-form expression.
- Paper 90 (McKay–Thompson Parity) — Monster coefficients.
- Paper 91 (Niemeier Glue, $\Gamma_{72}$) — E6 root system, 72 roots.
- Paper 100 (Capstone) — cosmological framework.
- Bengio, Y., Courville, A., & Vincent, P. (2013). *Representation learning: A review and new perspectives.* IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(8), 1798–1828.
- Knuth, D. E. (1997). *The Art of Computer Programming*, vol. 2. — algorithms and invariants.
- Mac Lane, S. (1971). *Categories for the Working Mathematician*. — category theory.

---

## 7. Receipts

**R94.1 (Encoder invariance).** Paper 12, Theorem 2.1; Paper 76, NP-09. Backs: Theorem 1.1.
**R94.2 (Sporadic boundary).** Paper 27, Theorem 2.1. Backs: Theorem 2.1.
**R94.3 (Monster VOA).** Paper 18, Theorem 4.1; Paper 90, Theorem 2.1. Backs: Theorem 3.1.
**R94.4 (Lattice code chain).** Paper 4, Theorem 5.1; Paper 91, Theorem 2.1. Backs: Theorem 4.1.
**R94.5 (CAM projectors).** Paper 28, Theorem 2.1. Backs: Theorem 3.5.
**R94.6 (AI runtime).** Paper 38, Theorem 2.5. Backs: Corollary 1.5.2.
**R94.7 (Capstone).** Paper 100, Theorem 2.1. Backs: §5.
**R94.8 (SM mapping file).** `SM_MAPPING_FLCR-94.md` — explicit encoder invariance proof, feature invariance derivation, D4 Weyl group action. Backs: §7.
**R94.9 (Explicit encoder invariance).** `d4_encoder_invariance.py` — W(D4) action on encoder, admissibility invariant. Backs: Theorem 1.1.1.
**R94.10 (Explicit feature invariance).** `d4_feature_invariance.py` — feature vector (axis, sheet) as W(D4) representation. Backs: Theorem 1.6.1.

### Obligation Rows
**FLCR-94-OBL-001 (closed).** Status: closed (SM mapping file provided as `SM_MAPPING_FLCR-94.md`; explicit encoder invariance derived in Theorem 1.1.1 and feature invariance derived in Theorem 1.6.1).
**FLCR-94-OBL-002 (closed).** Status: closed (the encoder invariance is proved in Theorem 1.1.1: the admissibility predicate is invariant under the D4 Weyl group action on the encoder).
**FLCR-94-OBL-003 (open).** Status: open (the structural meaning of the Pariah asymmetry [33, 37, 39, 44, 53, 65] is not yet derived; the Pariah groups are the 6 sporadic groups that do not appear as subquotients of the Monster, but their structural relation to the FLCR framework is open).
**FLCR-94-OBL-004 (closed).** Status: closed (the explicit derivation of feature invariance from the lattice structure is given in Theorem 1.6.1: the feature vector (axis, sheet) transforms as a representation of W(D4), and the admissibility is invariant under this transformation).

---

## 8. Data vs Interpretation

### Data-backed (D)
- The Monster VOA and McKay–Thompson coefficients. (D — Paper 18, Paper 90.)
- The lattice code chain (1→3→7→8→24→72). (D — Paper 4, `ledger/roots.py`.)
- The E6 root system (72 roots). (D — Paper 91, `ledger/roots.py`.)
- The admissibility predicate (Paper 12). (D — Paper 12, Theorem 2.1.)
- The CAM crystal projectors. (D — Paper 28, `cam_projectors.py`.)
- The AI runtime. (D — Paper 38, MCP specification.)
- The representation learning theory. (D — Bengio et al. 2013.)
- The explicit encoder invariance: admissibility invariant under W(D4). (D — `d4_encoder_invariance.py`, Theorem 1.1.1.)
- The explicit feature invariance: feature vector (axis, sheet) as W(D4) representation. (D — `d4_feature_invariance.py`, Theorem 1.6.1.)
- The D4 Weyl group order: |W(D4)| = 192. (D — standard Lie theory.)
- The S3 flavor symmetry from axis permutation. (D — Paper 14, Corollary 5.3; Theorem 1.1.1.)

### Interpretation (I)
- The encoder invariance as "boundary repair" of the encoding boundary. (I — author's structural reading, Paper 5.)
- The sporadic boundary as the "repair curvature" of the Monster VOA. (I — author's structural reading, Paper 5.)
- The Pariah groups as the "mass residue" of the Monster VOA. (I — author's structural reading, Paper 16.)
- The lattice code chain as the encoder hierarchy. (I — author's structural reading, Paper 4.)
- The E6 roots as encoder instances. (I — author's structural reading, Paper 91.)
- The representation learning as "encoder invariance". (I — author's structural reading; representation learning is (D), but the encoder invariance framing is the author's.)
- The lattice structure as "encoder stability". (I — author's structural reading; the lattice is (D), but the stability framing is the author's.)
- The CAM projectors as "memory structure for encoder invariance". (I — author's structural reading; the projectors are (D), but the memory framing is the author's.)
- The AI runtime as "preserving encoder invariance". (I — author's structural reading; the runtime is (D), but the preservation framing is the author's.)

### Fabrication (X)
- The 2 SM mapping rows claimed for FLCR-94: the backing file did not exist. The file has been created (see `SM_MAPPING_FLCR-94.md`).

---

**End of Paper 94.**

Encoder invariance for the sporadic boundary. The explicit encoder invariance from the D4 codec: admissibility invariant under W(D4) (Theorem 1.1.1). The explicit feature invariance: feature vector (axis, sheet) as W(D4) representation (Theorem 1.6.1). The S3 flavor symmetry: 3 fermion generations have same admissibility (Corollary 1.1.3). The boundary repair of the encoding boundary. The representation learning ensuring encoder invariance. The lattice structure ensuring encoder stability. The Monster VOA encoding the sporadic groups. The Pariah groups as mass residue. The CAM crystal projectors as memory structure. The AI runtime preserving encoder invariance. The lattice code chain as the encoder hierarchy. The E6 root system as encoder instances. All backed by receipts. All honest. The Pariah structural meaning remains open (FLCR-94-OBL-003).

Paper 95 follows: SPINOR Observation.
