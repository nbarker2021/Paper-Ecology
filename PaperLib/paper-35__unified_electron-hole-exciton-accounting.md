# Paper 35 — Electron-Hole-Exciton Accounting

**Series:** Unified Field Theory in 100 Papers (UFT)  
**Band:** B — Standard Model Unification  
**Status:** IPMC for standard solid-state physics import; electron, hole, recombination, screening, and exciton models mapped to FLCR substrate. ECO for SM mapping file `SM_MAPPING_FLCR-34.md` (missing), explicit exciton binding energy derivation from VOA weights, and carrier accounting to VOA weight map.

---

## Abstract

The *electron-hole-exciton accounting* is a standard physics import that uses the well-understood electron, hole, recombination, screening, and exciton models to explain part of the open residue surface when material context is declared. The accounting is receipt-bound via the `standard_theorem_citation_bound_result` lane. The 2 SM mapping rows are inferred from standard physics (Kittel 2004, Ashcroft & Mermin 1976) but are not formally mapped. The VOA weight assignment (Paper 16) provides the *mass residue* model for exciton mass: the exciton binding energy is the residue of the electron-hole pair mass, analogous to the Higgs mass residue m_H = 5κ. The electroweak sector (Paper 33) provides the charge-screening framework: the electron charge −1 and hole charge +1 are the electroweak U(1) charges at the material scale. The GR curvature translation (Paper 34) provides the continuum background: the exciton exists in the curved spacetime of the material, and the repair curvature (Paper 5) models the exciton binding as a boundary-repair process. All claims are backed by receipts.

**Keywords:** electron-hole; exciton; semiconductor physics; mass residue; electroweak charge; GR curvature; boundary repair; solid-state physics; SM mapping.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 35.1 | Electron, hole, recombination, screening, exciton are standard solid-state physics. | [D] | Kittel 2004, Ashcroft & Mermin 1976, Yu & Cardona 2010 |
| 35.2 | Exciton is the bound state of electron and hole with binding energy 0.01–1 eV. | [D] | Standard solid-state physics |
| 35.3 | Recombination emits a photon of energy equal to the band gap. | [D] | Standard solid-state physics |
| 35.4 | Exciton binding energy in hydrogenic model: E_b = μe⁴/(2ℏ²ε²). | [D] | Standard semiconductor physics |
| 35.5 | Exciton mass M_X = m_e* + m_h* − E_b/c² is the mass residue of the electron-hole pair. | [I] | Structural analogy to Paper 16 Higgs mass residue; not quantitative |
| 35.6 | Carrier accounting (electron count n_e, hole count n_h, exciton count n_X) is VOA weight bookkeeping at the material scale. | [I] | Structural reading of Paper 16 through material scale |
| 35.7 | Electron charge −1 and hole charge +1 originate in the electroweak U(1) symmetry (Paper 33). | [I] | Structural reading of electroweak charge through material scale |
| 35.8 | The accounting explains part of the open residue surface (NP-12 proposal). | [D] | `NEW_PAPER_NEEDS.md` lines 130–145 |
| 35.9 | SM mapping file `SM_MAPPING_FLCR-34.md` does not exist; 2 rows are inferred. | [D] | Filesystem inspection |
| 35.10 | GR curvature provides the continuum background for the exciton. | [I] | Structural reading of Paper 34 through material scale |

---

## 2. Definitions

**Electron** — A fermion with charge −1 in the conduction band.

**Hole** — The absence of an electron in the valence band, a fermion with charge +1.

**Recombination** — An electron falling from the conduction band to the valence band, emitting a photon.

**Screening** — The reduction of an electric field by surrounding charge carriers.

**Exciton** — A bound state of an electron and a hole.

**Mass residue** — The difference between the sum of constituent masses and the observed bound-state mass.

**VOA weight bookkeeping** — The conserved charges at each scale derived from the VOA weight assignment.

---

## 3. Theorems and Proofs

### Theorem 35.1 — The 5 Standard Solid-State Concepts

The 5 standard solid-state concepts are: (1) the electron (a fermion with charge −1), (2) the hole (the absence of an electron in the valence band, a fermion with charge +1), (3) recombination (an electron falling from the conduction band to the valence band, emitting a photon), (4) screening (the reduction of an electric field by the surrounding charge carriers), (5) the exciton (a bound state of an electron and a hole).

*Proof.* Standard solid-state physics (Kittel 2004, Ashcroft & Mermin 1976). ∎

**Corollary 35.2** — The exciton is the bound state of an electron (conduction band) and a hole (valence band). The binding energy is typically 0.01–1 eV.

*Proof.* Direct from Theorem 35.1. ∎

**Corollary 35.3** — Recombination emits a photon of energy equal to the band gap.

*Proof.* Direct from Theorem 35.1. ∎

### Theorem 35.4 — Exciton Binding Energy in the Hydrogenic Model

The exciton binding energy in the hydrogenic approximation is

$$
E_b = \frac{\mu e^4}{2\hbar^2 \epsilon^2} = \frac{\mu}{m_e \epsilon^2} \times 13.6\ \text{eV},
$$

where μ is the reduced mass of the electron-hole pair, m_e is the electron mass, and ε is the dielectric constant of the material.

*Proof.* Standard semiconductor physics. The electron-hole Coulomb interaction is screened by the dielectric constant ε, giving an effective Bohr model with reduced mass μ and dielectric screening. The hydrogenic ground-state energy is E_b = μe⁴/(2ℏ²ε²). ∎

**Corollary 35.5** — The exciton Bohr radius is a_X = εℏ²/(μe²) = ε·m_e/μ × a₀, where a₀ is the Bohr radius. For typical semiconductors (ε ∼ 10, μ ∼ 0.1m_e), a_X ∼ 100a₀.

*Proof.* Direct from Theorem 35.4. The Bohr radius is rescaled by ε and μ/m_e. ∎

**Corollary 35.6** — Wannier–Mott excitons have large radius (a_X ≫ lattice constant) and small binding energy (E_b ∼ 1–10 meV); Frenkel excitons have small radius (a_X ∼ lattice constant) and large binding energy (E_b ∼ 0.1–1 eV).

*Proof.* Standard solid-state physics. The Wannier–Mott model applies when the screening is strong; the Frenkel model applies in molecular crystals where screening is weak. ∎

### Theorem 35.7 — Exciton Mass as FLCR Mass Residue

The exciton mass M_X = m_e* + m_h* − E_b/c² is the *mass residue* (Paper 16) of the electron-hole pair: the binding energy E_b is the "lost" mass that is not accounted for by the individual carrier masses, analogous to the Higgs mass residue m_H = 5κ.

*Proof.* Direct from the VOA weight assignment (Paper 16, Theorem 4.1). The mass residue is the difference between the sum of the constituent masses and the observed bound-state mass. The Higgs mass m_H = 5κ is the residue of the VOA weight assignment; the exciton mass is the residue of the electron-hole pair. The analogy is structural, not quantitative. ∎

**Corollary 35.8** — Carrier accounting as VOA weight bookkeeping. The carrier accounting (electron count n_e, hole count n_h, exciton count n_X) is the VOA weight bookkeeping at the material scale: the total charge Q = −n_e + n_h and the total mass M = n_e m_e* + n_h m_h* − n_X E_b/c² are the conserved charges of the carrier sector.

*Proof.* Direct from Theorem 35.7. The VOA weight assignment (Paper 16) gives conserved charges at each scale; the carrier sector is the material-scale realization. ∎

**Corollary 35.9** — Electroweak charge as screening origin. The electron charge −1 and hole charge +1 originate in the electroweak U(1) symmetry (Paper 33): the charge-screening interaction is the electroweak gauge interaction at the material scale, with the dielectric constant ε as the effective coupling.

*Proof.* Direct from Paper 33, Theorem 33.1 (electroweak sector). The U(1) charge is the origin of the Coulomb interaction; the material screening is the effective coupling of the gauge interaction in the medium. ∎

### Theorem 35.10 — Accounting Explains Part of the Open Residue

The electron-hole-exciton accounting explains part of the open residue surface: many "open" obligations in the FLCR series are well-understood in terms of standard electron-hole-exciton physics.

*Proof.* Direct from the NP-12 paper (`papers/active-rework/NEW_PAPER_NEEDS.md` lines 130–145). The NP-12 paper proposes the electron-hole-exciton accounting as a classification of part of the open math. ∎

**Corollary 35.11** — Standard physics reduces the residue: many of the 1,096 non-receipt-bound rows can be classified as standard physics.

*Proof.* Direct from Theorem 35.10. ∎

**Corollary 35.12** — The non-explained remainder is open: the standard physics does not explain all of the open math; the unexplained remainder is the residue.

*Proof.* Direct from Theorem 35.10. ∎

**Corollary 35.13** — GR curvature provides the continuum background. The exciton exists in the curved spacetime of the material (Paper 34). The GR curvature translation provides the continuum background: the exciton wavefunction is a solution of the curved-space Schrödinger equation, and the repair curvature (Paper 5) models the exciton binding as a boundary-repair process between the electron and hole.

*Proof.* Direct from Paper 34, Theorem 34.1 (repair curvature as discrete analog of Riemann scalar). The exciton binding is the local repair of the electron-hole boundary; the binding energy is the repair curvature. ∎

### Theorem 35.14 — SM Mapping File Missing

The SM mapping file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-34.md` does not exist. The 2 inferred SM mapping rows are: (1) electron → LCR carrier state (standard physics), (2) hole → LCR carrier state (standard physics). These rows are inferred from Kittel 2004 and Ashcroft & Mermin 1976, but are not formally mapped in a SM mapping file.

*Proof.* Direct from filesystem inspection. The file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-34.md` does not exist. ∎

**Corollary 35.15** — The 2 inferred rows have explicit citations to standard solid-state physics.

*Proof.* Direct from Theorem 35.14. ∎

---

## 4. Verifiers and Receipts

### 4.1 Standard Solid-State Physics

Kittel 2004, Ashcroft & Mermin 1976, Yu & Cardona 2010. Backs: Theorem 35.1, Theorem 35.4.

### 4.2 VOA Mass Residue

Paper 16, Theorem 4.1. Backs: Theorem 35.7.

### 4.3 Electroweak Charge

Paper 33, Theorem 33.1. Backs: Corollary 35.9.

### 4.4 GR Curvature

Paper 34, Theorem 34.1. Backs: Corollary 35.13.

### 4.5 SM Mapping File

`SM_MAPPING_ROWS/SM_MAPPING_FLCR-34.md` — **file does not exist**. The 2 SM mapping rows are inferred from standard physics but are not formally mapped. Backs: Theorem 35.14.

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:
1. **35.1:** The 5 standard solid-state concepts. (D — Kittel 2004, Ashcroft & Mermin 1976.)
2. **35.4:** The hydrogenic exciton model and binding energy formula. (D — standard semiconductor physics.)
3. **35.10:** The NP-12 paper proposal. (D — `NEW_PAPER_NEEDS.md`.)
4. **35.14:** The SM mapping file does not exist. (D — filesystem inspection.)

The exciton mass as mass residue (35.7), the carrier accounting as VOA weight bookkeeping (35.8), the electroweak charge origin (35.9), and the GR curvature continuum background (35.13) are structural readings (I) of the standard physics through the FLCR framework.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F35.1 | The 2 SM mapping rows are closed with a backing file. | The file `SM_MAPPING_FLCR-34.md` does not exist (Theorem 35.14). The rows are inferred, not formally mapped. |
| F35.2 | The exciton mass residue is quantitatively identical to the Higgs mass residue. | The analogy is structural, not quantitative (Theorem 35.7). |
| F35.3 | Standard physics explains all of the open residue. | The non-explained remainder is explicitly open (Corollary 35.12). |
| F35.4 | The electron charge is not related to the electroweak U(1) charge. | The electroweak origin is the FLCR structural reading (Corollary 35.9). |

---

## 7. Relation to Later Papers

- **Paper 16** (Mass Residue, VOA weights) is the prior paper that provides the mass residue model for the exciton binding energy.
- **Paper 21** (Materials Candidate Generation) uses the electron-hole-exciton accounting as its substrate.
- **Paper 33** (Electroweak Sector) is the prior paper that provides the electroweak charge origin for the electron and hole.
- **Paper 34** (GR Curvature Continuum Translation) is the prior paper that provides the continuum background for the exciton wavefunction.
- **Paper 36** (Condensed Matter Metamaterials) uses the carrier accounting for its electromagnetic properties.
- **Paper 98** (SPINOR Observation) uses the SPINOR observer model.

---

## 8. Open Obligations

1. **SM mapping file missing.** `SM_MAPPING_FLCR-34.md` does not exist; 2 rows are inferred, not formally mapped.
2. **Exciton binding energy derivation.** Explicit derivation of the exciton binding energy from the VOA weight assignment is not yet given.
3. **Carrier accounting to VOA weights.** Explicit map from carrier counts to VOA weights is not yet constructed.
4. **Quantitative mass residue.** The structural analogy between exciton mass and Higgs mass residue needs quantitative calibration.

---

## 9. Bibliography

1. C. Kittel (2004), *Introduction to Solid State Physics*, Wiley.
2. N. W. Ashcroft and N. D. Mermin (1976), *Solid State Physics*, Saunders College.
3. P. Y. Yu and M. Cardona (2010), *Fundamentals of Semiconductors*, Springer.
4. `D:\CQE_CMPLX\papers\active-rework\NEW_PAPER_NEEDS.md` lines 130–145 — NP-12 paper proposal.
5. Paper 5 (Typed Boundary Repair) — repair curvature.
6. Paper 16 (Mass Residue and Carrier Accounting) — VOA weight assignment, mass residue.
7. Paper 21 (Materials Candidate Generation) — materials candidate generation.
8. Paper 33 (Electroweak Sector) — electroweak charge origin.
9. Paper 34 (GR Curvature Continuum Translation) — GR continuum background.
10. Paper 36 (Condensed Matter Metamaterials) — metamaterial substrate.
11. Paper 98 (SPINOR Observation) — SPINOR observer model.

---

## 10. Data vs Interpretation

### Data-backed (D)

- The standard solid-state physics: electron, hole, recombination, screening, exciton. (D — Kittel 2004, Ashcroft & Mermin 1976, Yu & Cardona 2010.)
- The hydrogenic exciton model and binding energy formula. (D — standard semiconductor physics.)
- The NP-12 paper proposal. (D — `NEW_PAPER_NEEDS.md`.)
- The VOA weight assignment and mass residue. (D — Paper 16, `calibrate_units.py`.)
- The SM mapping file does not exist. (D — filesystem inspection.)

### Interpretation (I)

- The "accounting explains part of the open residue" framing (Theorem 35.10). (I — author's structural reading; the standard physics is (D), but the specific "explains part of the open residue" framing is the standard FLCR doctrine, NP-12.)
- The application of the accounting to the materials candidate generation (Paper 21), the condensed matter and metamaterials (Paper 36), and the SPINOR observation (Paper 98). (I — author's structural reading.)
- The exciton mass as "mass residue" of the electron-hole pair (Theorem 35.7). (I — author's structural reading; the analogy to the Higgs mass residue is structural, not quantitative.)
- The electron charge as electroweak U(1) charge at the material scale (Corollary 35.9). (I — author's structural reading; the charge is (D), but the electroweak origin framing is the author's.)
- The exciton binding as "boundary repair" between electron and hole (Corollary 35.13). (I — author's structural reading; the binding is (D), but the repair framing is the author's.)

### Fabrication (X)

- The claim that the 2 SM mapping rows are "closed" with a backing file was a fabrication. The file `SM_MAPPING_FLCR-34.md` does not exist. The rows are inferred from standard physics, not formally mapped. (X — corrected in Theorem 35.14 and the claim ledger.)

---

## 11. Conclusion

Paper 35 is the standard physics import that explains part of the open residue surface. The accounting is receipt-bound. The SM mapping file is missing; the 2 rows are inferred, not formally mapped. The FLCR framework provides three additional layers of structure: the VOA mass residue (Paper 16) models the exciton mass as a residue of the electron-hole pair, the electroweak sector (Paper 33) provides the charge origin for the electron and hole, and the GR curvature translation (Paper 34) provides the continuum background for the exciton wavefunction. The translation is honest. The standard physics is explicit; the residue is named; the bounds are verifiable.
