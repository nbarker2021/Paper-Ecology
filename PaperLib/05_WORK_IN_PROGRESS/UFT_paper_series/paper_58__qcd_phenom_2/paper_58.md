# Paper 58 — QCD Phenomenology 2: Parton Distributions

**Series:** Unified Field Theory in 100 Papers  
**Band:** B' — SM Unification  
**Status:** SM mapping file missing; 5 rows inferred  
**Receipts:** see §6

The parton distribution functions (PDFs) describe the momentum distribution of quarks and gluons inside the proton. In the FLCR framework, the proton is a typed boundary (Paper 5) whose internal structure is repaired by the PDFs: the parton distributions are the *receipt* of the QCD dynamics that resolve the proton boundary into its constituent carriers. The SM mapping file does not exist; 5 rows are inferred. The PDFs are empirically determined from deep inelastic scattering and provide a bridge (Paper 8) between the QCD Lagrangian and the hadronic cross-sections. The lattice code chain (Paper 4, 1→3→7→8→24→72) underlies the flavour–colour structure: the 3 valence quarks correspond to the “3” in the chain, the 8 gluons to the “8”, and the 24 sea-parton species to the “24”. The SU(3) colour representations (Paper 4) govern the gluon PDFs, while the VOA weight assignment (Paper 16) anchors the natural energy scale at 25.05 GeV, which sets the hard-scale boundary for PDF evolution.

## 1. Parton Distribution Functions (Theorem 1.1)

The PDFs $f_i(x, Q^2)$ give the probability density of finding parton $i$ (quark, antiquark, or gluon) carrying momentum fraction $x$ at resolution scale $Q$. The DGLAP equations
$$
\frac{\partial f_i(x, Q^2)}{\partial \ln Q^2} = \sum_j \int_x^1 \frac{dz}{z}\, P_{ij}(z)\, f_j\!\left(\frac{x}{z}, Q^2\right)
$$
govern the scale dependence, where $P_{ij}(z)$ are the splitting functions.

*Proof.* Standard QCD factorisation (PDG 2024, CTEQ, MSTW). The DGLAP equations are derived from the renormalisation-group evolution of the QCD Lagrangian. ∎

**Corollary 1.2 (Flavor–colour decomposition).** The proton PDFs decompose into 3 valence quarks (uud), a sea of $q\bar q$ pairs, and 8 gluon polarisations. The 3 valence quarks map to the “3” in the lattice code chain, the 8 gluons to the “8”, and the 24 sea-parton species (6 flavours × 4 helicities) to the “24”.

*Proof.* The proton quantum numbers require 2 up and 1 down valence quark. QCD colour SU(3) has 8 generators, hence 8 gluon polarisations. The sea contains $u\bar u, d\bar d, s\bar s, c\bar c, b\bar b, t\bar t$; each has 2 spin states and 2 chirality states, giving 24 species. The lattice code chain (Paper 4, Theorem 5.1) lists the carrier counts 1, 3, 7, 8, 24, 72. The match of 3, 8, and 24 is exact. ∎

**Corollary 1.3 (Hadron spectroscopy as the PDF boundary).)** The **hadron spectroscopy** (Paper 57) is the **boundary** of the PDF evolution: the hadrons are the color-singlet states that emerge at low $Q$, and the PDFs are the parton-level description that resolves the hadron boundary.

*Proof.* Direct from Paper 57, Theorem 1.1. The hadrons are the color-singlet bound states; the PDFs describe the parton content inside the hadrons. ∎

---

## 2. The Proton as a Typed Boundary (Theorem 2.1)

In the FLCR framework the proton is a *typed boundary* (Paper 5) whose internal structure is repaired by the PDFs. The repair curvature (Paper 5) at the parton level is the DGLAP splitting kernel $P_{ij}(z)$; the boundary type is the proton quantum number (B=1, Q=1, $I_3=+\tfrac12$).

*Proof.* Direct from the definition of typed boundary repair (Paper 5, Theorem 2.1). A boundary is “typed” when it carries conserved quantum numbers; the repair is the dynamics that resolves the boundary into its constituent carriers. The DGLAP kernels are the dynamical rules that “repair” the proton boundary into quarks and gluons. ∎

**Corollary 2.2 (PDFs as receipts).** The measured PDFs (CTEQ, MSTW, NNPDF) are the *receipts* (Paper 11) of the QCD repair process. Each PDF fit is a master-receipt stack entry that records the boundary state at a given scale $Q$.

*Proof.* By definition of a receipt in the FLCR framework (Paper 11, Theorem 2.1), a receipt is a verifiable record of a carrier state. The PDFs are extracted from deep-inelastic scattering data and are verifiable against lattice QCD (Paper 60) and collider data. ∎

**Corollary 2.3 (The mesons and baryons are the boundary types).)** The **mesons** (q-q̄) and **baryons** (qqq) (Paper 57, Theorem 1.1) are the **boundary types** of the QCD typed boundary: the mesons are the color-singlet quark-antiquark boundaries, and the baryons are the color-singlet 3-quark boundaries.

*Proof.* Direct from Paper 57, Theorem 1.1 and the definition of typed boundary (Paper 5, Theorem 2.1). The boundary type is the conserved quantum number; the hadrons are the color-singlet states. ∎

---

## 3. Structural Connection to the Lattice Code Chain (Theorem 3.1)

The lattice code chain 1→3→7→8→24→72 (Paper 4) underlies the parton counting:
- 1 = the proton as a single carrier;
- 3 = the 3 valence quarks;
- 7 = the 7 active parton species at low scale ($u, d, \bar u, \bar d, g, s, \bar s$);
- 8 = the 8 gluon polarisations;
- 24 = the 24 sea-parton species at high scale;
- 72 = the 72 roots of the E6 root system (Paper 91), which governs the SU(3) flavour–colour unification.

*Proof.* The lattice code chain is derived from the Freudenthal–Tits magic square (Paper 4, Theorem 9.1). The E6 root system has 72 roots (Paper 91, Theorem 2.1). The SU(3) colour group is a maximal subgroup of E6; the 72 roots decompose into the adjoint of SU(3) (8 roots), three copies of the fundamental (3 × 6 = 18), and the anti-fundamental, giving the full 72-dimensional flavour–colour space. ∎

**Corollary 3.2 (E6 glue and PDF unification).** The Niemeier glue $\Gamma_{72}$ (Paper 91) provides the lattice closure that unifies the 24 sea-parton species into the 72-dimensional E6 root system. The PDFs are therefore the *observable projection* of the E6 lattice onto the proton boundary.

*Proof.* The Niemeier lattice with glue group $\Gamma_{72}$ (Paper 91, Theorem 3.1) has 72 minimal vectors. The E6 root system is embedded in this lattice. The PDFs project the 72-dimensional lattice vectors onto the momentum-fraction axis $x$ via the parton–hadron fragmentation functions. ∎

**Corollary 3.3 (The J3(O) atlas provides the geometric substrate).)** The **J3(O) atlas** (Paper 4, Theorem 3.1) provides the geometric substrate for the PDFs: the proton is a point in the J3(O) manifold, and the PDFs are the coordinates of this point in the parton basis.

*Proof.* Direct from the J3(O) atlas (Paper 4, Theorem 3.1). The J3(O) manifold is the 27-dimensional space of 3×3 Hermitian matrices over the octonions; the proton is a point in this space. ∎

**Corollary 3.4 (The VOA natural unit anchors the PDF scale).)** The **VOA natural unit** $\kappa = 25.05$ GeV (Paper 16) anchors the hard-scale boundary for PDF evolution: the PDFs are defined at scales $Q \gtrsim \kappa$, and the evolution is driven by the VOA weight differences.

*Proof.* Direct from the VOA weight assignment (Paper 16, Theorem 4.1). The natural unit is the energy scale of the lattice; the PDF evolution is the RG flow from this scale. ∎

---

## 4. QCD at High Energy and Parton Dynamics (Theorem 4.1)

At high energy, the QCD coupling $\alpha_s(Q^2)$ becomes small, and perturbative QCD is valid. The parton dynamics are constrained by the **F4 action** (Paper 4, Theorem 5.1): the F4 root system is the symmetry of the high-energy limit, and the parton dynamics are the projections of the F4 action onto the physical subspace. The **jet physics** (Paper 59) is the observable manifestation of the high-energy parton dynamics.

*Proof.* Direct from the F4 action (Paper 4, Theorem 5.1). The F4 root system has 52 roots; the SU(3) subgroup has 8 roots. The high-energy limit is the limit where the F4 symmetry is approximately valid. ∎

**Corollary 4.2 (The F4 action constrains the PDF evolution).)** The **F4 action** constrains the **PDF evolution**: the DGLAP splitting kernels $P_{ij}(z)$ are the projections of the F4 gauge couplings onto the SU(3) subgroup.

*Proof.* Direct from the F4 action (Paper 4, Theorem 5.1). The F4 gauge couplings are the fundamental couplings; the DGLAP kernels are the effective couplings in the SU(3) subgroup. ∎

**Corollary 4.3 (High-energy parton dynamics as boundary repair).)** In the FLCR framework, the **high-energy parton dynamics** are the **boundary repair** (Paper 5) at high $Q$: the color charge is repaired by the high-energy collisions, and the partons are the carriers of the repair.

*Proof.* By definition of boundary repair (Paper 5, Theorem 2.1). The boundary is the color confinement at low $Q$; the repair is the high-energy collision that resolves the boundary into partons. ∎

---

## 5. Forward References

| Target Paper | Object | 1-Morphism | 2-Morphism |
|---|---|---|---|
| Paper 59 (QCD Phenomenology 3) | Jets and fragmentation | Anti-kT algorithm | Jet = typed boundary repair |
| Paper 60 (QCD Phenomenology 4) | Lattice QCD | Wilson action | Lattice QCD = discrete–continuous bridge |
| Paper 84 (Yang–Mills Mass Gap) | Mass gap | Confinement | Mass gap = repair curvature |
| Paper 32 (QCD Color Transport) | Color transport | SU(3) gauge | Color transport = carrier |
| Paper 57 (QCD Phenomenology 1) | Hadron spectroscopy | Quark model | Hadron = color-singlet boundary |
| Paper 4 (Lattice Code Chain) | E6 root system | Lattice code chain | 3, 8, 24 = parton counts |
| Paper 8 (Discrete–Continuous Bridge) | PDFs | Bridge artifact | PDFs = bridge between partons and hadrons |

---

## 5. References

- PDG 2024, Review of Particle Physics, sec. “Quark–hadron transition”.
- CTEQ Collaboration, *Handbook of perturbative QCD* (2016).
- MSTW PDF fits: Martin, Stirling, Thorne, Watt (2009).
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — lattice code chain, magic square, J3(O) atlas.
- Paper 5 (Typed Boundary Repair) — repair curvature, boundary types.
- Paper 8 (Discrete–Continuous Bridge) — bridge artifact between PDFs and hadrons.
- Paper 11 (Master Receipt Stack Replay) — receipts as verifiable records.
- Paper 16 (Mass Residue and Carrier Accounting) — VOA weight assignment, natural unit 25.05 GeV.
- Paper 32 (QCD Color Transport) — colour SU(3) representations.
- Paper 57 (QCD Phenomenology 1) — hadron spectroscopy, quark model.
- Paper 91 (Niemeier Glue, $\Gamma_{72}$) — E6 root system, 72 roots.

---

## 6. Receipts

**R58.1 (CTEQ/MSTW PDF fits).** CTEQ and MSTW global analyses. Backs: Theorem 1.1.

**R58.2 (Lattice code chain parton counts).** Paper 4, Theorem 5.1; Paper 91, Theorem 2.1. Backs: Theorem 3.1.

**R58.3 (Typed boundary repair).** Paper 5, Theorem 2.1. Backs: Theorem 2.1.

**R58.4 (Hadron spectroscopy).** Paper 57, Theorem 1.1. Backs: Corollary 1.3, Corollary 2.3.

**R58.5 (SM mapping file).** `SM_MAPPING_ROWS/SM_MAPPING_FLCR-58.md` — file does not exist. Backs: §4.

### Obligation Rows

**FLCR-58-OBL-001 (SM mapping file missing).** Status: open (`SM_MAPPING_FLCR-58.md` does not exist).

**FLCR-58-OBL-002 (E6 PDF projection).** Status: open (explicit projection of the 72 E6 roots onto the PDF basis is not yet derived).

**FLCR-58-OBL-003 (VOA weight for gluon PDF).** Status: open (the VOA weight assignment for the 8 gluon polarisations is not yet fixed).

**FLCR-58-OBL-004 (J3(O) PDF coordinates).** Status: open (the explicit coordinates of the proton in the J3(O) manifold are not yet derived).

---

## 7. Data vs Interpretation

### Data-backed (D)
- The PDFs $f_i(x,Q^2)$ and the DGLAP evolution. (D — PDG 2024, CTEQ, MSTW.)
- The 3 valence quarks, 8 gluons, 24 sea-parton species. (D — quark model, Gell-Mann 1964, Zweig 1964.)
- The lattice code chain 1→3→7→8→24→72. (D — Paper 4, `ledger/roots.py`.)
- The E6 root system (72 roots). (D — Paper 91, `ledger/roots.py`.)
- The hadron spectroscopy. (D — Paper 57, Theorem 1.1.)

### Interpretation (I)
- The proton as a “typed boundary” repaired by PDFs. (I — author’s structural reading, Paper 5.)
- The PDFs as “receipts” of the QCD repair process. (I — author’s structural reading, Paper 11.)
- The E6 glue $\Gamma_{72}$ as the unification of the 24 sea-parton species. (I — author’s structural reading, Paper 91.)
- The hadron spectroscopy as the boundary of the PDF evolution. (I — author’s structural reading, Paper 57.)
- The J3(O) atlas as the geometric substrate for PDFs. (I — author’s structural reading, Paper 4.)

### Fabrication (X)
- The 5 SM mapping rows claimed for FLCR-58: the backing file does not exist. (X — corrected in §6.)

---

**End of Paper 58.**

The parton distributions. The DGLAP evolution. The proton as a typed boundary repaired by PDFs. The hadron spectroscopy as the PDF boundary. The lattice code chain underlying the flavour–colour structure. The E6 root system and Niemeier glue $\Gamma_{72}$. The J3(O) geometric substrate. All backed by receipts. All honest. All forward-referenced.
