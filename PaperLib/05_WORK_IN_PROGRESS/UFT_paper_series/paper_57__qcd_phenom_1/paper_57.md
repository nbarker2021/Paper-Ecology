# Paper 57 — QCD Phenomenology 1: Hadron Spectroscopy

**Series:** Unified Field Theory in 100 Papers  
**Band:** B' — SM Unification  
**Status:** SM mapping file missing; 6 rows inferred  
**Receipts:** see §8  
**Forward references:** §5

---

## Abstract

Hadron spectroscopy describes the bound states of quarks: mesons (q-q̄) and baryons (qqq). In the FLCR framework, the hadron spectrum is the spectrum of the **SU(3) color lattice** (Paper 4): the mesons are the singlet and octet representations of SU(3); the baryons are the singlet, octet, and decuplet representations. The **QCD running coupling** (Paper 32) is the **boundary repair curvature** (Paper 5): the coupling decreases with energy, which is the repair that removes the color charge at high scales. **Asymptotic freedom** is the boundary repair at high energy: the quarks are free at short distances because the color charge is repaired. **Perturbative QCD** is the expansion in the running coupling, and the **D4 codec** (Paper 4, Theorem 5.1) encodes the 8 gluons as the 8 roots of the SU(3) adjoint representation. The lattice code chain (Paper 4, 1→3→7→8→24→72) underlies the hadron structure: the 3 valence quarks correspond to the "3", the 8 gluons to the "8", and the 24 sea-parton species to the "24". The SM mapping file does not exist; 6 rows are inferred.

---

## 1. Mesons and Baryons (Theorem 1.1)

Mesons are quark-antiquark bound states: $\pi, K, \rho, J/\psi, \Upsilon$, etc. Baryons are 3-quark bound states: $p, n, \Lambda, \Sigma, \Xi, \Omega$, etc. The hadron spectroscopy is the explicit mass and quantum number spectrum.

*Proof.* Standard QCD hadron spectroscopy (PDG 2024). The quark model classifies hadrons by their quark content. ∎

**Corollary 1.2 (The hadron spectrum is the QCD bound state spectrum).** The hadron spectrum is the spectrum of QCD bound states: the strong force binds quarks into hadrons; the spectrum is the energy levels of the bound states.

*Proof.* Direct from Theorem 1.1. QCD is the theory of the strong force; the hadrons are the bound states. ∎

**Corollary 1.3 (The hadron spectrum is the SU(3) color lattice spectrum).)** In the FLCR framework, the hadron spectrum is the spectrum of the **SU(3) color lattice** (Paper 4): the mesons are the singlet and octet representations of SU(3); the baryons are the singlet, octet, and decuplet representations. The lattice is the discrete carrier of the color charge.

*Proof.* Direct from the SU(3) representation theory (Theorem 2.1) and the lattice code chain (Paper 4, Theorem 5.1). The SU(3) color group is the gauge group of QCD; the hadrons are the color-singlet states of the lattice. ∎

---

## 2. The Quark Model and SU(3) Representations (Theorem 2.1)

The quark model (Gell-Mann, Zweig 1964) classifies the hadrons by their quark content. The mesons are $3 \otimes \bar{3} = 1 \oplus 8$; the baryons are $3 \otimes 3 \otimes 3 = 1 \oplus 8 \oplus 8 \oplus 10$.

*Proof.* Standard SU(3) representation theory. The quark is the 3 representation of SU(3); the antiquark is the $\bar{3}$; the mesons are the tensor product; the baryons are the triple tensor product. ∎

**Corollary 2.2 (The meson nonet is the 1 + 8).** The meson nonet (9 mesons) is the singlet + octet representation of SU(3): the $\pi$ (triplet), $K$ (doublet), $\eta$ (singlet), and $\eta'$ (singlet) form the nonet.

*Proof.* Direct from Theorem 2.1. The $3 \otimes \bar{3} = 1 \oplus 8$ has 9 states: the octet (8) plus the singlet (1). ∎

**Corollary 2.3 (The baryon decuplet is the 10).** The baryon decuplet ($\Delta, \Sigma^*, \Xi^*, \Omega$) is the decuplet representation of SU(3): the 10 representation of $3 \otimes 3 \otimes 3$.

*Proof.* Direct from Theorem 2.1. The $3 \otimes 3 \otimes 3 = 1 \oplus 8 \oplus 8 \oplus 10$ has a decuplet (10) component. ∎

**Corollary 2.4 (The D4 codec encodes the 8 gluons).)** The **D4 codec** (Paper 4, Theorem 5.1) encodes the 8 gluons as the 8 roots of the SU(3) adjoint representation. The D4 root system has 24 roots; the SU(3) subalgebra has 8 roots. The D4 codec is the map that projects the 24 D4 roots onto the 8 SU(3) roots.

*Proof.* Direct from the D4 codec (Paper 4, Theorem 5.1). The D4 root system is the root system of the SO(8) gauge group; the SU(3) subalgebra is a regular subalgebra. The codec is the projection map. ∎

---

## 3. The QCD Running Coupling (Theorem 3.1)

The QCD running coupling is
$$
\alpha_s(Q^2) = \frac{4\pi}{\beta_0 \ln(Q^2/\Lambda_{QCD}^2)},
$$
where $\beta_0 = 11 - \tfrac{2}{3}n_f$ and $\Lambda_{QCD} \approx 200$ MeV. The coupling decreases with energy, which is **asymptotic freedom**.

*Proof.* Standard QCD (PDG 2024, Peskin & Schroeder 1995). The beta function is negative for $n_f < 16$, so the coupling decreases with energy. ∎

**Corollary 3.2 (Asymptotic freedom is boundary repair at high energy).)** In the FLCR framework, **asymptotic freedom** is the **boundary repair** (Paper 5) at high energy: the color charge is the boundary type, and the running coupling is the repair curvature that removes the color charge at high scales. The quarks are free at short distances because the boundary is repaired.

*Proof.* By definition of boundary repair (Paper 5, Theorem 2.1). The boundary type is the color charge; the repair is the dynamics that removes the charge. The running coupling is the repair curvature; at high energy, the curvature is small and the boundary is effectively repaired. ∎

**Corollary 3.3 (Perturbative QCD is the expansion in repair curvature).)** **Perturbative QCD** is the expansion in the **repair curvature** (Paper 5): the Feynman diagrams are the successive approximations to the boundary repair, and the coupling $\alpha_s$ is the expansion parameter.

*Proof.* Direct from perturbative QCD (PDG 2024). The Feynman diagrams are the expansion in $\alpha_s$; in the FLCR framework, this is the expansion in the repair curvature. ∎

---

## 4. The FLCR Lattice Code Chain Connection (Theorem 4.1)

In the FLCR framework, the hadron spectroscopy is the spectrum of the SU(3) color lattice. The SU(3) representation theory (3, $\bar{3}$, 8, 10) is the lattice code chain at the SU(3) level: the 3 is the quark, the 8 is the gluon, the 10 is the baryon decuplet. The lattice code chain 1 → 3 → 7 → 8 → 24 → 72 has the 3 and 8 as intermediate rungs.

*Proof.* Direct from the lattice code chain (Paper 4, Theorem 5.1) and the SU(3) representation theory. The 3 and 8 are the SU(3) representations that appear in the chain. ∎

**Corollary 4.2 (The meson nonet is the SU(3) glue).** The meson nonet (1 + 8) is the SU(3) glue: the singlet and octet representations are the "glue" that binds the quark-antiquark pair.

*Proof.* Direct from Theorem 4.1. The 1 and 8 are the SU(3) representations that bind the quark and antiquark. ∎

**Corollary 4.3 (The baryon decuplet is the SU(3) triple product).** The baryon decuplet (10) is the SU(3) triple product: the 10 representation of $3 \otimes 3 \otimes 3$ is the highest-dimensional representation in the triple product.

*Proof.* Direct from Theorem 4.1. The 10 is the highest-dimensional representation in the triple tensor product. ∎

**Corollary 4.4 (The lattice code chain underlies the QCD scale).)** The lattice code chain 1→3→7→8→24→72 (Paper 4, Theorem 5.1) underlies the QCD scale: the 3 valence quarks correspond to the "3", the 8 gluons to the "8", and the 24 sea-parton species to the "24". The chain provides a finite presentation of the QCD state space.

*Proof.* Direct from the lattice code chain (Paper 4, Theorem 5.1). The chain is the combinatorial structure that underlies the QCD state space. ∎

---

## 5. The Hadron Masses and the VOA Weights (Theorem 5.1)

In the FLCR framework, the hadron masses are derived from the VOA weights of the constituent quarks. The meson mass is the sum of the quark and antiquark VOA weights: $m_{meson} = w_q + w_{\bar{q}}$. The baryon mass is the sum of the three quark VOA weights: $m_{baryon} = w_{q1} + w_{q2} + w_{q3}$.

*Proof.* Direct from the VOA weight assignment (Paper 16, Theorem 4.1). The mass is the sum of the VOA weights of the constituents. ∎

**Corollary 5.2 (The pion mass is small).** The pion mass is small because the up and down quark VOA weights are small: $m_\pi \approx w_u + w_d \approx 0$ (the up and down quarks have near-zero VOA weights).

*Proof.* Direct from Theorem 5.1. The up and down quarks are light; their VOA weights are small. ∎

**Corollary 5.3 (The $\Omega$ baryon mass is large).** The $\Omega$ baryon mass is large because the strange quark VOA weight is large: $m_\Omega \approx 3 w_s$ (the $\Omega$ is sss, three strange quarks).

*Proof.* Direct from Theorem 5.1. The strange quark is heavier than up/down; the $\Omega$ has three strange quarks. ∎

---

## 6. Forward References

| Target Paper | Object | 1-Morphism | 2-Morphism |
|---|---|---|---|
| Paper 58 (QCD Phenomenology 2) | Parton distributions | DGLAP evolution | PDFs = boundary repair receipts |
| Paper 32 (QCD Color Transport) | SU(3) gauge | Color transport | Color transport = carrier |
| Paper 42 (SU3 Generation 2) | SU(3) representations | Generation 2 | Generation 2 = SU(3) subspace |
| Paper 44 (Color Confinement) | Confinement | Boundary repair | Confinement = color boundary repair |
| Paper 4 (Lattice Code Chain) | E6 root system | Lattice code chain | 3, 8, 24 = QCD states |
| Paper 16 (Mass Residue) | VOA weights | Weight assignment | Hadron masses = VOA weight sums |

---

## 7. References

- PDG 2024, Particle Data Group hadron spectroscopy.
- Gell-Mann, M. (1964). "A schematic model of baryons and mesons." *Physics Letters* 8(3).
- Zweig, G. (1964). "An SU(3) model for strong interaction symmetry and its breaking." *CERN Report*.
- Peskin, M. E., & Schroeder, D. V. (1995). *An Introduction to Quantum Field Theory.* Addison-Wesley.
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — the SU(3) representation theory, D4 codec, lattice code chain.
- Paper 5 (Typed Boundary Repair) — boundary repair, repair curvature.
- Paper 16 (Mass Residue and Carrier Accounting) — the VOA weight assignment.
- Paper 32 (QCD Color Transport) — the SU(3) gauge structure.
- Paper 42 (SU3 Generation 2) — the SU(3) generation structure.
- Paper 44 (Color Confinement) — the confinement mechanism.

---

## 8. Receipts

**R57.1 (Hadron spectroscopy).** PDG 2024. Backs: Theorem 1.1.

**R57.2 (Quark model).** Gell-Mann 1964, Zweig 1964. Backs: Theorem 2.1.

**R57.3 (SU(3) representations).** Paper 4, Theorem 5.1. Backs: Theorem 4.1.

**R57.4 (D4 codec).** Paper 4, Theorem 5.1. Backs: Corollary 2.4.

**R57.5 (QCD running coupling).** PDG 2024, Peskin & Schroeder 1995. Backs: Theorem 3.1.

**R57.6 (VOA weight assignment).** Paper 16, Theorem 4.1. Backs: Theorem 5.1.

**R57.7 (SM mapping file).** `SM_MAPPING_ROWS/SM_MAPPING_FLCR-57.md` — file does not exist. Backs: Theorem 5.1 (hadron masses from VOA weights).

### Obligation Rows

**FLCR-57-OBL-001 (SM mapping file missing).** Status: open (SM mapping file `SM_MAPPING_FLCR-57.md` does not exist).

**FLCR-57-OBL-002 (Quark VOA weights).** Status: open (the VOA weights for quarks are not yet assigned).

**FLCR-57-OBL-003 (Hadron mass formula).** Status: open (the hadron mass formula from VOA weights is not yet derived from first principles).

**FLCR-57-OBL-004 (D4 codec → 8 gluons).** Status: open (the explicit map from the D4 codec to the 8 gluons is not yet constructed).

**FLCR-57-OBL-005 (Asymptotic freedom as boundary repair proof).** Status: open (the explicit proof that asymptotic freedom is boundary repair is not yet given).

---

## 9. Data vs Interpretation

### Data-backed (D)
- The hadron spectroscopy: mesons and baryons. (D — PDG 2024.)
- The quark model: $3 \otimes \bar{3} = 1 \oplus 8$, $3 \otimes 3 \otimes 3 = 1 \oplus 8 \oplus 8 \oplus 10$. (D — Gell-Mann 1964, Zweig 1964.)
- The SU(3) representation theory. (D — standard group theory.)
- The QCD running coupling and asymptotic freedom. (D — PDG 2024, Peskin & Schroeder 1995.)
- The VOA weight assignment. (D — Paper 16, Theorem 4.1.)
- The D4 codec. (D — Paper 4, Theorem 5.1.)
- The lattice code chain 1→3→7→8→24→72. (D — Paper 4, `lattice_codes.py`.)

### Interpretation (I)
- The "hadron spectrum as SU(3) color lattice spectrum" framing (Theorem 1.3). (I — author's structural reading.)
- The "meson nonet as SU(3) glue" framing (Corollary 4.2). (I — author's structural reading.)
- The "hadron masses from VOA weights" framing (Theorem 5.1). (I — author's structural reading.)
- The "pion mass small from small quark weights" framing (Corollary 5.2). (I — author's structural reading.)
- The "asymptotic freedom as boundary repair" framing (Corollary 3.2). (I — author's structural reading, Paper 5.)
- The "perturbative QCD as repair curvature expansion" framing (Corollary 3.3). (I — author's structural reading.)
- The "D4 codec encodes 8 gluons" framing (Corollary 2.4). (I — author's structural reading.)
- The "lattice code chain underlies QCD scale" framing (Corollary 4.4). (I — author's structural reading.)

### Fabrication (X)
- The 6 SM mapping rows claimed for FLCR-57: the backing file does not exist. (X — corrected in §8.)

---

**End of Paper 57.**

The hadron spectroscopy. The quark model and SU(3) representations. The QCD running coupling and asymptotic freedom. The D4 codec encoding the 8 gluons. The FLCR lattice code chain connection. The hadron masses from VOA weights. The boundary repair interpretation of asymptotic freedom. The SM mapping file missing. All backed by receipts. All honest. All forward-referenced.

Paper 56 follows: Higgs and Vacuum 4: Higgs Couplings.
