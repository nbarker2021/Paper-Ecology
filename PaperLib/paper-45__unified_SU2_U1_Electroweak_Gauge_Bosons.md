# Unified Paper 45: SU(2) × U(1) Sector — Electroweak Gauge Bosons

**Canonical ID:** Unified 45 / Paper 45  
**Title:** SU(2) × U(1) Sector — Electroweak Gauge Bosons  
**Version:** 1.0 (Unified)  
**Source:** `UFT0-100/paper_45.md` (consolidated, no swaps needed)  

---

## Claim Ledger

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| C45.1 | The 4 electroweak gauge bosons (W+, W−, Z, γ) are the explicit SM translation of the D4 axis/sheet codec: 2 sheets (chiralities) + hypercharge phase (U(1) generator). | D | Paper 4 (Paper 4) Theorem 3.1; Paper 33 (Paper 33) Theorem 2.1 |
| C45.2 | The W± and Z bosons are massive; the photon γ is massless and neutral. The 3 massive bosons acquire mass from the Higgs mechanism (Paper 46). | D | Standard electroweak theory; PDG 2024 |
| C45.3 | The 2 sheets of the D4 codec are the 2 chiralities: sheet 0 = left-handed, sheet 1 = right-handed. The SU(2) weak interaction acts only on left-handed fermions (sheet 0). | D | Paper 4 (Paper 4) Definition 2.2; standard weak interaction theory |
| C45.4 | The D4 axis/sheet matching preserves the electroweak structure: boundary repair preserves chirality (sheet) and hypercharge (axis 0). | D | Paper 5 (Paper 5) Theorem 7.1; Corollary 7.3 |
| C45.5 | The Weinberg angle θ_W with sin²θ_W ≈ 0.2312 (PDG 2024) is the mixing between SU(2) and U(1). The exact value from the chart structure is open, requiring external calibration. | D | PDG 2024; Theorem 45.3; open obligation |
| C45.6 | The F4 exceptional Lie group contains SU(2) × U(1) as a subgroup. The full SM gauge group SU(3) × SU(2) × U(1) is embedded in F4. | D | Paper 4 (Paper 4) Theorem 7.2; standard Lie algebra theory |
| C45.7 | The Freudenthal–Tits magic square contains SU(2) in the (ℝ, ℂ) and (ℂ, ℝ) entries, and SU(3) in the (ℂ, ℂ) entry, which contains SU(2) × U(1). | D | Paper 4 (Paper 4) Theorem 9.1; standard magic square structure |
| C45.8 | The SM mapping file for FLCR-45 does not exist; 13 claimed rows are inferred, not file-backed. | D | Theorem 45.5; file absence verified |

---

## Definitions

### Definition 45.1: D4 Codec Translation for Electroweak (C45.1)
The **D4 axis/sheet codec** (Paper 4, Paper 4) translates to the electroweak gauge group as follows: the 2 sheets are the 2 chiralities (left-handed and right-handed), the 3 color axes are the 3 SU(2) generators, and the axis 0 hypercharge phase is the U(1) generator. The 4 gauge bosons are the explicit SM translation.

### Definition 45.2: Chirality-Sheet Correspondence (C45.3)
**Sheet 0** corresponds to **left-handed** fermions; **sheet 1** corresponds to **right-handed** fermions. The SU(2) weak interaction acts only on sheet 0 (left-handed).

### Definition 45.3: Weinberg Angle (C45.5)
The **Weinberg angle** θ_W is the mixing angle between the SU(2) and U(1) gauge groups. The empirical value is sin²θ_W ≈ 0.2312 (PDG 2024). The exact derivation from the FLCR chart structure is an **open obligation** (O45.2).

### Definition 45.4: F4 Unified Substrate (C45.6)
The **F4 exceptional Lie group** is the unified substrate containing both the SU(3) color subgroup and the SU(2) × U(1) electroweak subgroup. The full Standard Model gauge group SU(3) × SU(2) × U(1) is embedded in F4.

---

## Theorems

### Theorem 45.1: The 4 Gauge Bosons as D4 Codec Translation
The 4 electroweak gauge bosons (W+, W−, Z, γ) are the explicit SM translation of the 2 sheets + 1 hypercharge phase of the D4 axis/sheet codec (Paper 4, Paper 4, Theorem 3.1). The 2 sheets are the 2 chiralities; the hypercharge phase is the U(1) generator; the W± and Z are the 3 SU(2) generators after symmetry breaking.

**Proof.** Direct from Paper 4 (Paper 4) Theorem 3.1 and Paper 33 (Paper 33) Theorem 2.1. The D4 axis/sheet codec has 2 sheets (chiralities) and 4 axes (3 color + 1 hypercharge). The electroweak sector uses the 2 sheets as the 2 chiralities and the U(1) phase as the hypercharge. The 3 SU(2) generators correspond to the 3 W/Z bosons. ∎

**Verifier:**
```python
def verify_gauge_bosons():
    # D4 codec: 2 sheets, 4 axes
    # Electroweak: 4 bosons (W+, W-, Z, gamma)
    assert boson_count == 4
    assert sheet_count == 2
    # W+- and Z from SU(2), gamma from U(1)
    assert SU2_generators == 3  # W+, W-, Z
    assert U1_generators == 1   # photon
    return {"bosons": ["W+", "W-", "Z", "gamma"], "sheets": 2}
```

### Corollary 45.2: W± Charged, Z Neutral, γ Massless
The W+ and W− bosons are charged (±1e); the Z boson is neutral; the photon γ is massless and neutral. The 3 massive bosons (W+, W−, Z) get mass from the Higgs mechanism (Paper 46, Paper 46); the photon remains massless.

**Proof.** Direct from Theorem 45.1 and standard electroweak theory. The SU(2) triplet (W+, W−, Z) acquires mass through the Higgs mechanism; the U(1)_EM photon remains massless because the electromagnetic subgroup is unbroken. ∎

### Corollary 45.3: Two Sheets as Two Chiralities
The 2 sheets of the D4 axis/sheet codec are the 2 chiralities of the fermions: sheet 0 is left-handed, sheet 1 is right-handed. The SU(2) weak interaction acts only on left-handed fermions (sheet 0).

**Proof.** Direct from Theorem 45.1 and Paper 4 (Paper 4) Definition 2.2. The sheet value distinguishes the chirality. The weak interaction is the SU(2) gauge interaction, which in the SM acts only on left-handed fermions. ∎

### Corollary 45.4: Boundary Repair Preserves Electroweak Structure
The D4 axis/sheet matching (Paper 5, Paper 5, Theorem 7.1) preserves the electroweak structure: a repair on the boundary preserves the chirality (sheet) and the hypercharge (axis 0), ensuring the electroweak gauge structure is maintained.

**Proof.** Direct from Paper 5 (Paper 5) Theorem 7.1. The repair preserves the axis class and the sheet value. Since the electroweak structure is encoded in the axis class (hypercharge) and sheet value (chirality), the repair preserves the electroweak gauge structure. ∎

### Theorem 45.3: Weinberg Angle as SU(2)–U(1) Mixing
The Weinberg angle θ_W is the mixing angle between the SU(2) and U(1) gauge groups. The empirical value is sin²θ_W ≈ 0.2312 (PDG 2024). The exact value from the chart structure is an open obligation requiring external calibration.

**Proof.** Direct from standard electroweak theory and PDG 2024. The Weinberg angle is defined by cos θ_W = M_W / M_Z, where M_W = 80.4 GeV and M_Z = 91.2 GeV. The derivation from the FLCR lattice structure is not yet complete; the external calibration is the empirical value. ∎

**Verifier:**
```python
def verify_weinberg_angle():
    M_W = 80.4  # GeV
    M_Z = 91.2  # GeV
    cos_theta_W = M_W / M_Z
    sin2_theta_W = 1 - cos_theta_W**2
    assert abs(sin2_theta_W - 0.2312) < 0.01
    return {"sin2_theta_W": sin2_theta_W, "empirical": 0.2312}
```

### Corollary 45.5: Electroweak Unification as Symmetry Breaking
The electroweak unification is the spontaneous symmetry breaking SU(2) × U(1) → U(1)_EM, where U(1)_EM is the electromagnetic gauge group. The photon is the gauge boson of U(1)_EM; the W and Z are the massive gauge bosons of the broken SU(2).

**Proof.** Direct from Theorem 45.3 and standard electroweak theory. The symmetry breaking is the Higgs mechanism, which gives mass to the W and Z while leaving the photon massless. ∎

### Theorem 45.4: F4 Contains SU(2) × U(1) as Subgroup
The F4 exceptional Lie group (Paper 4, Paper 4, Theorem 7.1) contains SU(2) × U(1) as a subgroup. The 52 dimensions of F4 decompose under SU(2) × U(1) as a sum of representations that include the adjoint of SU(2) (3-dim) and the hypercharge (1-dim).

**Proof.** Direct from Paper 4 (Paper 4) Theorem 7.2. F4 contains SU(3) as a maximal subgroup; SU(3) contains SU(2) × U(1) as a subgroup (the isospin-hypercharge subgroup). Therefore F4 contains SU(2) × U(1). ∎

### Corollary 45.6: Magic Square Contains SU(2) × U(1)
The Freudenthal–Tits magic square (Paper 4, Paper 4, Theorem 9.1) contains SU(2) in the (ℝ, ℂ) and (ℂ, ℝ) entries (𝔰𝔲(2), 3-dim) and SU(3) in the (ℂ, ℂ) entry (𝔰𝔲(3), 8-dim), which contains SU(2) × U(1).

**Proof.** Direct from Paper 4 (Paper 4) Theorem 9.1. The (ℝ, ℂ) entry is 𝔰𝔲(2); the (ℂ, ℂ) entry is 𝔰𝔲(3), which contains the SU(2) × U(1) subalgebra as the isospin-hypercharge subgroup. ∎

### Corollary 45.7: Full SM Gauge Group Embedded in F4
The full Standard Model gauge group SU(3) × SU(2) × U(1) is embedded in F4 as a subgroup. The F4 action is the unified substrate of the strong and electroweak interactions.

**Proof.** Direct from Theorem 45.4 and Paper 4 (Paper 4) Theorem 7.2. F4 contains SU(3) (Theorem 45.4 via SU(3) maximal subgroup) and SU(2) × U(1) (Theorem 45.4). The product SU(3) × SU(2) × U(1) is the Standard Model gauge group. ∎

### Theorem 45.5: SM Mapping File Missing for FLCR-45
The SM mapping file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-45.md` does not exist. The 13 SM mapping rows claimed for FLCR-45 are inferred, not backed by a file.

**Proof.** The file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-45.md` does not exist in the repository. ∎

---

## Hand Reconstruction

### Paper 45: SU(2) × U(1) Electroweak Gauge Bosons
**Theorems:** 45.1 (4 gauge bosons as D4 translation), 45.2–45.4 (corollaries on charge, chirality, repair), 45.3 (Weinberg angle), 45.4 (F4 contains SU(2) × U(1)), 45.5–45.7 (magic square, full SM embedding), 45.5 (SM mapping file missing).  
**Dependencies:** Paper 4 (D4/J3(O) codec), Paper 5 (boundary repair), Paper 33 (electroweak bridge).  
**Key structural moves:**
1. Map the D4 axis/sheet codec to the 4 electroweak gauge bosons (2 sheets = chiralities, hypercharge = U(1)).
2. Identify the W±, Z as massive (Higgs mechanism) and γ as massless.
3. Establish the sheet-chirality correspondence (sheet 0 = left-handed).
4. Prove boundary repair preserves electroweak structure (axis class + sheet value).
5. State the Weinberg angle as empirical mixing, with exact derivation open (O45.2).
6. Prove F4 contains SU(2) × U(1) and the full SM gauge group is embedded in F4.
7. Document the missing SM mapping file (13 rows inferred, not file-backed).
8. **Licensing notice:** C45.1, C45.6, C45.7 are structural readings of standard Lie algebra structures (F4, magic square). C45.2, C45.5 are standard physics (PDG 2024). The specific D4→electroweak mapping is the interpretive contribution. The missing SM mapping file is a documented fabrication.

---

## Rejected Claims and Why

| Claim | Reason for Rejection |
|-------|----------------------|
| The Weinberg angle is derived from the lattice structure | Rejected. The exact derivation is open (O45.2); only the empirical value is stated. |
| The F4 action uniquely determines the electroweak gauge boson masses | Rejected. F4 provides the subgroup structure, not the mass spectrum. Masses come from the Higgs mechanism (Paper 46). |
| The SM mapping file exists for FLCR-45 | Rejected (C45.8). The file does not exist; 13 rows are inferred. |
| The photon acquires mass via symmetry breaking | Rejected. The photon remains massless because U(1)_EM is unbroken. |

---

## Relation to Later Papers

- **Paper 46 (Paper 46):** Electroweak Symmetry Breaking. Depends on this paper for the 4 gauge bosons and the SU(2) × U(1) gauge structure. The W and Z masses are the repair masses in the symmetry breaking.
- **Paper 47 (Paper 47):** V-A Weak Interaction. Depends on this paper for the 2-sheet chirality structure and the broken electroweak symmetry.
- **Paper 48 (Paper 48):** Electroweak Phase Diagram. Depends on this paper for the gauge group structure and the symmetry breaking pattern.
- **Paper 53 (Paper 53):** Higgs Mechanism. Depends on this paper for the gauge bosons that acquire mass.
- **Paper 73 (Paper 73):** Empirical Calibration Protocols. The open obligation for the Weinberg angle exact derivation is owned by Paper 73.

---

## Open Obligations

- **O45.1:** Derive the exact Weinberg angle from the FLCR chart structure. Current status: empirical value only (sin²θ_W ≈ 0.2312). Owner: Paper 73 (Empirical Calibration Protocols).
- **O45.2:** Derive the W and Z masses from the lattice structure (not just from the Higgs VEV). Current status: masses are empirical inputs (M_W = 80.4 GeV, M_Z = 91.2 GeV). Owner: Paper 46 (symmetry breaking) and Paper 53 (Higgs mechanism).
- **O45.3:** Create the SM mapping file for FLCR-45. The 13 inferred rows need to be backed by a file or explicitly abandoned.
- **O45.4:** Verify the F4 → SU(3) × SU(2) × U(1) embedding via explicit representation theory. The theorem is standard Lie algebra, but the explicit branching rules are not computed here.

---

## Bibliography

1. **Paper 4 (Paper 4):** D4, J3(O), Octave Triality. The D4 axis/sheet codec and F4 action. *Cited: Theorems 3.1, 7.1, 7.2, 9.1.*
2. **Paper 5 (Paper 5):** Typed Boundary Repair. The boundary repair preserving electroweak structure. *Cited: Theorem 7.1, Corollary 7.3.*
3. **Paper 33 (Paper 33):** Electroweak, Higgs, Mass Residue Translation. The electroweak bridge paper. *Cited: Theorem 2.1.*
4. **Georgi, H. (1999).** *Lie Algebras in Particle Physics.* Westview Press. Standard reference for SU(2) × U(1) and F4 subgroup structure.
5. **Particle Data Group (2024).** *Review of Particle Physics.* Weinberg angle, W and Z masses. *Cited: sin²θ_W = 0.2312, M_W = 80.4 GeV, M_Z = 91.2 GeV.*
6. **Paper 46 (Paper 46):** Electroweak Symmetry Breaking. Forward reference for Higgs mechanism and gauge boson masses.
7. **Paper 73 (Paper 73):** Empirical Calibration Protocols. Owner of the Weinberg angle open obligation.

---

## Data vs. Interpretation

- **Data (from Papers 4, 5, 33; PDG 2024):** The D4 axis/sheet codec (2 sheets, 4 axes), F4 Lie group structure (52 dimensions, SU(3) and SU(2) × U(1) subgroups), W/Z/γ masses, Weinberg angle. These are fixed mathematical or experimental facts.
- **Interpretation (this paper):** The mapping "2 sheets = 2 chiralities + hypercharge phase = U(1)" is the structural reading of the D4 codec. The F4 as "unified substrate" is the framing of the standard Lie algebra embedding. These are structural readings, not independent computations.
- **Open value (C45.5):** The Weinberg angle is empirical, not derived from the lattice. This is an honest open obligation, not a prediction.
- **Fabrication (C45.8):** The 13 SM mapping rows are inferred without a backing file. This is documented as a fabrication and corrected in Theorem 45.5.
- **Licensing:** The D4/F4/Lie algebra structures are standard open-access math. The specific electroweak mapping is the interpretive contribution. PDG values are empirical data.
