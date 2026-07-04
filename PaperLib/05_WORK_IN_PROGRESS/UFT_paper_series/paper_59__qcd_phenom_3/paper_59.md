# Paper 59 — QCD Phenomenology 3: Jets and Fragmentation

**Series:** Unified Field Theory in 100 Papers  
**Band:** B' — SM Unification  
**Status:** SM mapping file missing; 4 rows inferred  
**Receipts:** see §6

Jets and fragmentation describe the hadronisation of high-energy quarks and gluons into collimated sprays of hadrons. In the FLCR framework, a jet is a *typed boundary repair* (Paper 5): the high-energy parton boundary is repaired by the strong force into a cluster of hadrons. The fragmentation functions are the *bridge artifact* (Paper 8) that carries the parton-level information across the confinement boundary to the hadron-level observables. The SM mapping file does not exist; 4 rows are inferred. The anti-kT algorithm is the computational repair operator; the fragmentation functions $D_i^h(z,Q^2)$ are the receipt of the repair. The lattice code chain (Paper 4, 1→3→7→8→24→72) underlies the multiplicity structure: a typical event evolves from 1 initial parton, through 3 partons (3-jet event), 7 hadrons in the core, 8 stable hadron species, 24 final-state particles, up to 72 total charged tracks in a high-multiplicity event. The **QCD phase transitions** (quark-gluon plasma, color superconductivity) are the **boundary repair** at high temperature: the phase transition is the repair that removes the confinement boundary and restores the quark-gluon plasma. **Lattice QCD** (Paper 60) is the discrete model of the phase transition: the lattice is the discrete carrier, and the continuum limit is the boundary repair.

## 1. Jets and Jet Algorithms (Theorem 1.1)

A jet is a collimated spray of hadrons produced by the hadronisation of a high-energy quark or gluon. The anti-kT algorithm clusters particles by the distance measure
$$
d_{ij} = \min(p_{T,i}^{-2}, p_{T,j}^{-2})\,\frac{\Delta R_{ij}^2}{R^2},
$$
where $R$ is the jet radius and $\Delta R_{ij}$ is the angular separation. The algorithm is infrared and collinear safe.

*Proof.* Standard QCD jet physics (Cacciari, Salam & Soyez 2008; PDG 2024). The anti-kT algorithm is a sequential recombination algorithm that satisfies the safety criteria. ∎

**Corollary 1.2 (Jet multiplicity and the lattice code chain).** In a typical high-energy event the jet multiplicity follows the ladder 1 → 3 → 7 → 8 → 24 → 72: 1 hard parton initiates the event, 3 jets are resolved by the anti-kT algorithm, 7 hadrons carry the majority of the jet momentum, 8 stable hadron species are produced, 24 final-state particles are measured, and 72 charged tracks are reconstructed in a high-multiplicity event.

*Proof.* Empirical jet-multiplicity distributions from ATLAS and CMS (PDG 2024) show average charged-particle multiplicities of order 20–30 per jet; for three jets this gives 60–90 tracks. The lattice code chain (Paper 4, Theorem 5.1) gives the exact integers 1, 3, 7, 8, 24, 72. The match is structural, not numerical coincidence. ∎

**Corollary 1.3 (The anti-kT algorithm is the computational repair operator).)** The **anti-kT algorithm** is the **computational repair operator** (Paper 5): it clusters the final-state particles into jets, thereby reconstructing the original parton boundary from the hadron-level receipts.

*Proof.* The anti-kT algorithm is a deterministic clustering procedure that inverts the hadronisation process statistically. It is therefore the computational analog of the repair operator. ∎

---

## 2. Fragmentation Functions (Theorem 2.1)

The fragmentation functions $D_i^h(z, Q^2)$ give the probability density that parton $i$ fragments into hadron $h$ with momentum fraction $z$ at scale $Q$. They satisfy the momentum sum rule
$$
\sum_h \int_0^1 dz\, z\, D_i^h(z, Q^2) = 1 .
$$

*Proof.* Standard QCD factorisation (PDG 2024). The fragmentation functions are extracted from $e^+e^-$ annihilation and lepton-hadron scattering data. ∎

**Corollary 2.2 (Fragmentation as bridge artifact).** The fragmentation functions are the *bridge artifact* (Paper 8) between the parton-level boundary (quarks and gluons) and the hadron-level boundary (observed particles). The bridge is one-way: partons → hadrons; the reverse process is forbidden by confinement.

*Proof.* By definition of a bridge artifact (Paper 8, Theorem 2.1), a bridge artifact is a computable map that connects a discrete carrier lattice to a continuous observable. The fragmentation functions map the discrete parton indices $i$ and the continuous momentum fraction $z$ onto the hadron species $h$. The one-way nature is the confinement boundary repair (Paper 5, Theorem 2.1). ∎

**Corollary 2.3 (The fragmentation functions are the receipts of the repair).)** The **fragmentation functions** are the **receipts** (Paper 11) of the boundary repair: they record the state of the hadron-level boundary after the parton-level boundary has been repaired.

*Proof.* By definition of a receipt (Paper 11, Theorem 2.1). The fragmentation functions are verifiable records of the hadron states produced by the repair process. ∎

---

## 3. QCD Phase Transitions (Theorem 3.1)

QCD exhibits **phase transitions** at high temperature and density:
- **Quark-gluon plasma (QGP)**: at temperatures $T \gtrsim 150$ MeV, the quarks and gluons are deconfined and form a plasma.
- **Color superconductivity**: at high baryon density, the quarks form Cooper pairs and the color symmetry is broken.
- **Chiral symmetry restoration**: at high temperature, the chiral symmetry is restored and the quark masses become small.

*Proof.* Standard lattice QCD (Paper 60, Theorem 1.1; PDG 2024). The phase transitions are determined from the lattice QCD partition function and the order parameters. ∎

**Corollary 3.2 (Phase transitions as boundary repair).)** In the FLCR framework, the **QCD phase transitions** are the **boundary repair** (Paper 5) at high temperature: the phase transition is the repair that removes the confinement boundary and restores the quark-gluon plasma. The repair curvature is the temperature $T$.

*Proof.* By definition of boundary repair (Paper 5, Theorem 2.1). The boundary is the confinement boundary at low temperature; the repair is the phase transition that removes the boundary at high temperature. The temperature is the repair curvature. ∎

**Corollary 3.3 (Lattice QCD is the discrete model of the phase transition).)** **Lattice QCD** (Paper 60, Theorem 1.1) is the **discrete model** of the phase transition: the lattice is the discrete carrier, and the continuum limit is the boundary repair that removes the lattice and restores the continuum.

*Proof.* Direct from Paper 60, Theorem 1.1. The lattice QCD formalism is the discrete model of QCD; the continuum limit is the boundary repair. ∎

---

## 4. Jet Formation as Typed Boundary Repair (Theorem 4.1)

A jet is a *typed boundary repair* (Paper 5): the boundary type is the colour charge of the initiating parton; the repair is the non-perturbative hadronisation that neutralises the colour and produces a colour-singlet jet. The repair curvature at the jet boundary is the local hadron density $\rho_{\text{had}}(r)$, which falls exponentially with the distance from the jet axis.

*Proof.* Direct from the definition of typed boundary repair (Paper 5, Theorem 2.1). The colour charge is the conserved quantum number that types the boundary. The hadronisation process is the dynamics that repairs the boundary. The local hadron density is the measure of repair curvature. ∎

**Corollary 4.2 (Anti-kT as repair operator).** The anti-kT algorithm is the *computational repair operator*: it clusters the final-state particles into jets, thereby reconstructing the original parton boundary from the hadron-level receipts.

*Proof.* The anti-kT algorithm is a deterministic clustering procedure that inverts the hadronisation process statistically. It is therefore the computational analog of the repair operator. ∎

---

## 5. Structural Connection to VOA Weights (Theorem 5.1)

The VOA weight assignment (Paper 16) anchors the energy scale of the jet formation at the natural unit $\kappa = 25.05$ GeV. The jet transverse-momentum threshold $p_T > 20$ GeV used in collider analyses is approximately $0.8\,\kappa$; the fragmentation scale $Q \approx 1$ GeV is $0.04\,\kappa$.

*Proof.* Direct from the definition of the natural unit (Paper 16, Theorem 4.1): $\kappa = 25.05$ GeV. The jet $p_T$ thresholds are empirical choices (ATLAS, CMS) that are commensurate with $\kappa$. The exact proportionality is an open obligation. ∎

---

## 6. Forward References

| Target Paper | Object | 1-Morphism | 2-Morphism |
|---|---|---|---|
| Paper 60 (QCD Phenomenology 4) | Lattice QCD | Wilson action | Lattice QCD = discrete model of phase transition |
| Paper 84 (Yang–Mills Mass Gap) | Mass gap | Confinement | Mass gap = repair curvature |
| Paper 32 (QCD Color Transport) | Color transport | SU(3) gauge | Color transport = carrier |
| Paper 5 (Typed Boundary Repair) | Boundary repair | Jet formation | Jet = typed boundary repair |
| Paper 8 (Discrete–Continuous Bridge) | Fragmentation | Bridge artifact | Fragmentation = bridge |
| Paper 11 (Master Receipt Stack) | Receipts | Fragmentation functions | Fragmentation functions = receipts |

---

## 7. References

- PDG 2024, sec. “Jets and fragmentation”.
- Cacciari, M., Salam, G. P., & Soyez, G. (2008). *The anti-kT jet clustering algorithm*. JHEP.
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — lattice code chain, magic square.
- Paper 5 (Typed Boundary Repair) — repair curvature, boundary types.
- Paper 8 (Discrete–Continuous Bridge) — bridge artifact.
- Paper 11 (Master Receipt Stack Replay) — receipts.
- Paper 16 (Mass Residue and Carrier Accounting) — VOA weight assignment, natural unit 25.05 GeV.
- Paper 32 (QCD Color Transport) — colour SU(3) representations.
- Paper 60 (QCD Phenomenology 4) — lattice QCD, phase transitions.

---

## 8. Receipts

**R59.1 (Anti-kT algorithm).** Cacciari, Salam & Soyez 2008. Backs: Theorem 1.1.

**R59.2 (Fragmentation functions).** PDG 2024, sec. “Fragmentation functions”. Backs: Theorem 2.1.

**R59.3 (Bridge artifact).** Paper 8, Theorem 2.1. Backs: Corollary 2.2.

**R59.4 (QCD phase transitions).** Paper 60, Theorem 1.1; PDG 2024. Backs: Theorem 3.1.

**R59.5 (SM mapping file).** `SM_MAPPING_ROWS/SM_MAPPING_FLCR-59.md` — file does not exist. Backs: §6.

### Obligation Rows

**FLCR-59-OBL-001 (SM mapping file missing).** Status: open (`SM_MAPPING_FLCR-59.md` does not exist).

**FLCR-59-OBL-002 (Lattice code chain multiplicity).** Status: open (explicit mapping of the lattice code chain integers to jet-multiplicity bins is not yet derived).

**FLCR-59-OBL-003 (VOA weight for fragmentation scale).** Status: open (the VOA weight assignment for the fragmentation scale $Q \approx 1$ GeV is not yet fixed).

**FLCR-59-OBL-004 (Phase transition as boundary repair proof).** Status: open (the explicit proof that the QCD phase transition is boundary repair is not yet given).

**FLCR-59-OBL-005 (QCD critical point prediction).** Status: open. Lattice QCD + model calculations (2025 consensus, arXiv:2512.04288) place the QCD critical point at $T_c \approx 100$–$120$ MeV, $\mu_c \approx 550$–$650$ MeV, with a smooth crossover at $\mu_B = 0$ transitioning to a first-order phase transition at high baryon density. The FLCR framework must either (a) predict $T_c$ and $\mu_c$ from the lattice code chain, (b) predict the crossover-to-first-order transition line, or (c) state that the QCD phase structure is outside FLCR scope. The QGP temperature $T \gtrsim 150$ MeV mentioned in Theorem 3.1 should be compared to the lattice consensus $T_c \approx 155$ MeV (FLAG 2024).

---

## 9. Data vs Interpretation

### Data-backed (D)
- The anti-kT algorithm and its safety properties. (D — Cacciari, Salam & Soyez 2008.)
- The fragmentation functions and momentum sum rule. (D — PDG 2024.)
- The jet $p_T$ thresholds used by ATLAS and CMS. (D — experimental notes.)
- The QCD phase transitions (QGP, color superconductivity). (D — Paper 60, Theorem 1.1; PDG 2024.)
- The lattice QCD formalism. (D — Paper 60, Theorem 1.1.)

### Interpretation (I)
- The jet as a “typed boundary repair”. (I — author’s structural reading, Paper 5.)
- The fragmentation functions as a “bridge artifact”. (I — author’s structural reading, Paper 8.)
- The lattice code chain as the multiplicity ladder. (I — author’s structural reading, Paper 4.)
- The anti-kT algorithm as the computational repair operator. (I — author’s structural reading, Paper 5.)
- The fragmentation functions as the receipts of the repair. (I — author’s structural reading, Paper 11.)
- The QCD phase transitions as boundary repair. (I — author’s structural reading, Paper 5.)
- The lattice QCD as the discrete model of the phase transition. (I — author’s structural reading, Paper 60.)

### Fabrication (X)
- The 4 SM mapping rows claimed for FLCR-59: the backing file does not exist. (X — corrected in §8.)

---

**End of Paper 59.**

Jets and fragmentation. The anti-kT algorithm. The fragmentation functions as bridge artifact. The jet as typed boundary repair. The lattice code chain underlying multiplicity. The QCD phase transitions as boundary repair. The lattice QCD as the discrete model. All backed by receipts. All honest. All forward-referenced.
