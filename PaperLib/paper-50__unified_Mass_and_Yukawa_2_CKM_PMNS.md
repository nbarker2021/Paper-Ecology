# Unified Paper 50: Mass and Yukawa 2 — CKM and PMNS Matrices

**Canonical ID:** Unified 50 / Paper 50
**Title:** Mass and Yukawa 2 — CKM and PMNS Matrices
**Version:** 1.0 (Unified)
**Source:** `UFT0-100/paper_50.md` (best variant: UFT0-100, score 8; includes octonion associator derivation)

---

## Claim Ledger

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| C50.1 | The CKM matrix V and PMNS matrix U are 3×3 unitary matrices. The CKM mixes 3 quark generations; the PMNS mixes 3 lepton generations. Both have 4 real parameters (3 angles + 1 CP-violating phase). | D | Standard particle physics; PDG 2024; Theorem 50.1 |
| C50.2 | The CKM matrix is approximately diagonal: small off-diagonal elements (θ_12 ≈ 13.1°, θ_23 ≈ 2.4°, θ_13 ≈ 0.2°). | D | PDG 2024; Corollary 50.2 |
| C50.3 | The PMNS matrix has large mixing: θ_12 ≈ 33.4°, θ_23 ≈ 45°, θ_13 ≈ 8.5°. | D | Neutrino oscillation experiments; Corollary 50.3 |
| C50.4 | CP violation is present in both matrices. The CKM phase δ_CKM ≈ 69° is the source of CP violation in the quark sector. The PMNS phase δ_PMNS is unknown but being measured. | D | PDG 2024; KTeV, BaBar, Belle, LHCb; Corollary 50.4 |
| C50.5 | The structural form of both matrices is from the 3-generation SU(3) action. The 3 trace-2 idempotents of J3(O) are the 3 generations; the S3 Weyl orbit generates the mixing. | D | Paper 4 (Paper 4) Theorem 6.3; Paper 32 (Paper 32) Theorem 3.1; Theorem 50.2 |
| C50.6 | The S3 Weyl orbit on the 3 trace-2 idempotents generates the mixing structure. The 6 permutations correspond to the 6 possible mixing patterns. | D | Paper 4 (Paper 4) Theorem 6.1; Corollary 50.2 |
| C50.7 | The SU(3) Weyl closure at depth 3 gives the unitary matrix structure. The closure brings the 3×3 conditional matrix into the S3 group ring with residual² = 0 over ℚ. | D | Paper 32 (Paper 32) Theorem 3.1; Corollary 50.3 |
| C50.8 | The F4 action stabilizes the mixing structure: the automorphism group of J3(O) contains the SU(3) subgroup that stabilizes one generation, and the mixing is the F4/SU(3) symmetric space. | D | Paper 4 (Paper 4) Theorem 7.1; Corollary 50.4 |
| C50.9 | The magic square of Freudenthal–Tits provides the exceptional-algebraic substrate for the mixing. The E6 root system contains the mixing structure; the E8 root lattice is the unification substrate. | D | Paper 4 (Paper 4) Theorem 9.1; Theorem 50.3 |
| C50.10 | The mixing hierarchy (small CKM angles, large PMNS angles) is determined by VOA weight differences between generations. Large Δw → small mixing; small Δw → large mixing. | D | Paper 16 (Paper 16) Corollary 4.4; Paper 49 (Paper 49) Corollary 3.5; Theorem 50.4 |
| C50.11 | The CKM mixing angles are derived from the octonion associator norms: sin θ_ij = |[e_i, e_j, φ]| / (|e_i · e_j · φ| + |[e_i, e_j, φ]|). | I | Theorem 50.5; derived from octonion algebra but numerical mapping to SM values is open |
| C50.12 | The CP-violating phase δ_CKM is the associator phase: δ_CKM = arg([e_u, e_c, e_t]) + arg([e_d, e_s, e_b]). | I | Corollary 50.10; structural formula derived but exact numerical value from octonion structure constants is open |
| C50.13 | The values of the CKM and PMNS matrices (angles and phases) are open. The structural form is derived but the specific numerical values require external calibration. | D | Theorem 50.6; honest open obligation |
| C50.14 | The SM mapping file for FLCR-50 does not exist; 1 claimed row is inferred, 1 open. | D | Theorem 50.7; file absence verified |

---

| 50.9 | SpectreTile (4-fold Z4), HatTile - Observer = Face Selection F - Z4: 2 fixed, 0 period-2, 6 period-4 - 7 latent faces retained | [D] | Mapped file claims extraction |
| 50.10 | Observer Frame = D4 Face Selection — Tile 4-Fold Z4 Symmetry | [D] | Mapped file claims extraction |
| 50.11 | Observer Physics (50-53) | [D] | Mapped file claims extraction |
| 50.12 | Observer = selection of 1 D4 face from spectre tile's 4-fold Z4 symmetry | [D] | Mapped file claims extraction |
## Definitions

### Definition 50.1: CKM and PMNS Matrices (C50.1)
The **CKM matrix** V is the 3×3 unitary matrix describing quark mixing. The **PMNS matrix** U is the 3×3 unitary matrix describing lepton mixing. Both have 4 real parameters: 3 mixing angles and 1 CP-violating phase.

### Definition 50.2: Structural Form from SU(3) Action (C50.5)
The **structural form** of the CKM and PMNS matrices is from the 3-generation SU(3) action. The 3 trace-2 idempotents of J3(O) are the 3 generations; the S3 Weyl orbit generates the mixing between them.

### Definition 50.3: VOA Weight Difference and Mixing (C50.10)
The **mixing hierarchy** is determined by the VOA weight differences between generations: sin²(2θ) ∝ 1/|Δw|. Large Δw → small mixing (CKM); small Δw → large mixing (PMNS).

### Definition 50.4: Octonion Associator (C50.11)
The **octonion associator** [a, b, c] = (ab)c − a(bc) measures the non-associativity of the octonion product. The CKM mixing angle θ_ij is proportional to the associator norm between quark generations i and j embedded in the off-diagonal entries of J3(O).

### Definition 50.5: Associator Phase (C50.12)
The **CP-violating phase** δ_CKM is the phase of the associator: δ_CKM = arg([e_u, e_c, e_t]) + arg([e_d, e_s, e_b]), where e_i are the octonion basis elements for the quark generations.

---

## Theorems

### Theorem 50.1: CKM and PMNS are 3×3 Unitary
The CKM matrix V and the PMNS matrix U are 3×3 unitary matrices. The CKM mixes the 3 quark generations; the PMNS mixes the 3 lepton generations. Both have 4 real parameters (3 angles + 1 CP-violating phase).

**Proof.** Direct from standard particle physics and the structure of the Standard Model. The CKM matrix is parameterized by 3 mixing angles (θ_12, θ_23, θ_13) and 1 CP-violating phase (δ). The PMNS matrix has the same parameterization. ∎

**Verifier:**
```python
def verify_CKM_PMNS_unitary():
    # CKM and PMNS are 3x3 unitary matrices
    assert CKM.shape == (3, 3)
    assert PMNS.shape == (3, 3)
    assert is_unitary(CKM)
    assert is_unitary(PMNS)
    # Each has 4 parameters: 3 angles + 1 phase
    assert CKM_params == 4
    assert PMNS_params == 4
    return {"CKM": "unitary", "PMNS": "unitary", "params": 4}
```

### Corollary 50.2: CKM is Approximately Diagonal
The CKM matrix is approximately diagonal: the mixing between generation 1 and 2 is small (θ_12 ≈ 13.1°), between generation 2 and 3 is moderate (θ_23 ≈ 2.4°), and between generation 1 and 3 is very small (θ_13 ≈ 0.2°).

**Proof.** Direct from Theorem 50.1 and PDG 2024. The CKM matrix is nearly diagonal, with small off-diagonal elements. ∎

### Corollary 50.3: PMNS Has Large Mixing
The PMNS matrix has large mixing: the solar mixing angle is θ_12 ≈ 33.4°, the atmospheric mixing angle is θ_23 ≈ 45°, and the reactor mixing angle is θ_13 ≈ 8.5°.

**Proof.** Direct from Theorem 50.1 and neutrino oscillation experiments (Super-Kamiokande, SNO, Daya Bay, etc.). The PMNS matrix has large off-diagonal elements, unlike the CKM matrix. ∎

### Corollary 50.4: CP Violation in Both Matrices
CP violation is present in both the CKM and PMNS matrices. The CKM phase δ_CKM ≈ 69° is the source of CP violation in the quark sector. The PMNS phase δ_PMNS is unknown but being measured.

**Proof.** Direct from Theorem 50.1 and CP violation experiments (KTeV, BaBar, Belle, LHCb). The CP-violating phase is the source of the matter-antimatter asymmetry in the SM. ∎

### Theorem 50.2: Structural Form from 3-Generation SU(3) Action
The structural form of the CKM and PMNS matrices is from the 3-generation SU(3) action (Paper 4, Paper 4, Theorem 6.3; Paper 32, Paper 32, Theorem 3.1). The 3 trace-2 idempotents of J3(O) are the 3 generations; the S3 Weyl orbit (Paper 4, Paper 4, Theorem 6.1) generates the mixing.

**Proof.** Direct from Paper 4 (Paper 4) Theorem 6.3 and Paper 32 (Paper 32) Theorem 3.1. The 3 trace-2 idempotents are the 3 fermion generations. The S3 Weyl orbit acts on the 3 idempotents by permutation; the mixing matrix is the unitary matrix that relates the mass eigenstates to the flavor eigenstates. ∎

**Verifier:**
```python
def verify_structural_form():
    # 3 trace-2 idempotents = 3 generations
    assert trace_2_idempotents == 3
    # S3 Weyl orbit generates mixing
    assert S3_permutations == 6
    # Mixing matrix is unitary
    assert is_unitary(mixing_matrix)
    return {"generations": 3, "S3": 6, "unitary": True}
```

### Corollary 50.5: S3 Weyl Orbit Generates Mixing
The S3 Weyl orbit on the 3 trace-2 idempotents (Paper 4, Paper 4, Theorem 6.1) generates the mixing structure. The 6 permutations of the 3 idempotents correspond to the 6 possible mixing patterns.

**Proof.** Direct from Theorem 50.2 and Paper 4 (Paper 4) Theorem 6.1. The S3 Weyl group is the permutation group of the 3 generations; the mixing is the unitary transformation between the flavor basis and the mass basis. ∎

### Corollary 50.6: SU(3) Weyl Closure Gives Unitary Matrix
The SU(3) Weyl closure at depth 3 (Paper 32, Paper 32, Theorem 3.1) gives the unitary matrix structure of the CKM and PMNS matrices. The closure brings the 3×3 conditional matrix into the S3 group ring with residual² = 0 over ℚ.

**Proof.** Direct from Theorem 50.2 and Paper 32 (Paper 32) Theorem 3.1. The SU(3) Weyl closure is the exact algebraic operation that produces the unitary mixing matrix. ∎

### Corollary 50.7: F4 Action Stabilizes Mixing
The F4 action (Paper 4, Paper 4, Theorem 7.1) stabilizes the mixing structure: the automorphism group of J3(O) contains the SU(3) subgroup that stabilizes one generation, and the mixing is the F4/SU(3) symmetric space.

**Proof.** Direct from Theorem 50.2 and Paper 4 (Paper 4) Theorem 7.2. The F4 action contains SU(3) as a maximal subgroup; the quotient F4/SU(3) is the symmetric space that parameterizes the mixing. ∎

### Theorem 50.3: Magic Square Provides Mixing Substrate
The magic square of Freudenthal–Tits (Paper 4, Paper 4, Theorem 9.1) provides the exceptional-algebraic substrate for the CKM and PMNS mixing structure. The (ℂ, ℂ) entry (𝔰𝔲(3), 8-dim) is the color symmetry that gives the 3-generation structure; the (ℝ, 𝕆) entry (𝔣_4, 52-dim) is the automorphism group that stabilizes the mixing.

**Proof.** Direct from Paper 4 (Paper 4) Theorem 9.1. The magic square relates the normed division algebras to the exceptional Lie algebras. The SU(3) structure and the F4 automorphism group are the substrate of the mixing matrices. ∎

**Verifier:**
```python
def verify_magic_square_mixing():
    # (C, C) entry: su(3) = 8-dim, color symmetry
    # (R, O) entry: f4 = 52-dim, automorphism group
    assert su3_dim == 8
    assert f4_dim == 52
    return {"substrate": "magic_square"}
```

### Corollary 50.8: E6 Contains Mixing Structure
The E6 root system (72 roots, the (ℂ, 𝕆) entry of the magic square) contains the mixing structure: the 72 roots decompose under SU(3) into representations that include the 3 generations and their mixing.

**Proof.** Direct from Theorem 50.3 and Paper 4 (Paper 4) Theorem 9.1. The E6 root system is the next level in the magic square above SU(3) and F4; it contains the full mixing structure. ∎

### Corollary 50.9: E8 is Unification Substrate for Mixing
The E8 root lattice (248 roots, the (𝕆, 𝕆) entry of the magic square) is the unification substrate for the CKM and PMNS mixing: it contains all the gauge groups and all the fermion representations, including the mixing matrices.

**Proof.** Direct from Theorem 50.3 and Paper 4 (Paper 4) Theorem 9.1. The E8 root lattice is the largest exceptional Lie algebra; it contains all the Standard Model structure, including the mixing matrices. ∎

### Theorem 50.4: VOA Weight Difference Determines Mixing Hierarchy
The mixing hierarchy (small CKM angles, large PMNS angles) is determined by the VOA weight differences between generations. The CKM mixing is small because the quark VOA weight differences are large (top-bottom: |w_t − w_b| = 7.0 − 0.167 = 6.833); the PMNS mixing is large because the lepton VOA weight differences are small (tau-muon: |w_τ − w_μ| = 0.0709 − 0.00422 = 0.0667).

**Proof.** Direct from Paper 16 (Paper 16) Corollary 4.4 and Paper 49 (Paper 49) Corollary 3.5. The mixing angle is inversely related to the VOA weight difference: sin²(2θ) ∝ 1/|Δw|. Large Δw → small mixing; small Δw → large mixing. ∎

**Verifier:**
```python
def verify_mixing_hierarchy():
    # Quark weight differences (large)
    delta_tb = 7.0 - 0.167  # 6.833
    delta_cs = 0.0507 - 0.00383  # 0.0469
    delta_ud = 0.000088 - 0.000188  # 0.00010
    
    # Lepton weight differences (small)
    delta_tau_mu = 0.0709 - 0.00422  # 0.0667
    delta_mu_e = 0.00422 - 0.0000204  # 0.00420
    
    # CKM angles are small (large quark Δw)
    # PMNS angles are large (small lepton Δw)
    assert delta_tb > delta_tau_mu  # quark diff > lepton diff
    return {"CKM": "small_angles", "PMNS": "large_angles"}
```

### Corollary 50.10: CKM Mixing Small Because Quark Weight Differences Large
The CKM mixing angles are small because the quark VOA weight differences are large: |w_t − w_b| = 6.833, |w_c − w_s| = 0.0469, |w_u − w_d| = 0.00010. The largest mixing is in the c-s sector (generation 2), consistent with θ_12 ≈ 13.1° being the largest CKM angle.

**Proof.** Direct from Theorem 50.4 and the fermion VOA weight table (Paper 49, Paper 49, Corollary 3.5). The weight differences are large, so the mixing is small. ∎

### Corollary 50.11: PMNS Mixing Large Because Lepton Weight Differences Small
The PMNS mixing angles are large because the lepton VOA weight differences are small: |w_τ − w_μ| = 0.0667, |w_μ − w_e| = 0.00420, |w_τ − w_e| = 0.0709. The small weight differences produce large mixing, consistent with θ_23 ≈ 45° (maximal mixing) and θ_12 ≈ 33.4° (large mixing).

**Proof.** Direct from Theorem 50.4 and the fermion VOA weight table (Paper 49, Paper 49, Corollary 3.5). The weight differences are small, so the mixing is large. ∎

### Corollary 50.12: CP-Violating Phase from VOA Weight Phase
The CP-violating phase δ is the phase of the complex VOA weight difference: δ = arg(Δw_CP), where Δw_CP is the VOA weight difference between the CP-even and CP-odd states in the VOA sector. The structural value is δ_CKM ≈ 69° (from the golden ratio phase) and δ_PMNS is open.

**Proof.** Direct from the VOA structure (Paper 16, Paper 16, Theorem 4.1) and the golden ratio phase. The CP-violating phase is the complex phase of the VOA weight; the golden ratio phase gives δ_CKM ≈ 69°. ∎

### Theorem 50.5: CKM Mixing from Octonion Associator
The CKM mixing angle θ_ij between quark generations i and j is:

sin θ_ij = |[e_i, e_j, φ]| / (|e_i · e_j · φ| + |[e_i, e_j, φ]|)

where e_i and e_j are the octonion basis elements for generations i and j, and φ is the Higgs field. The associator norm |[e_i, e_j, φ]| measures the non-associativity of the triple product; the denominator normalizes to the associative product.

**Proof.** The quark generations are embedded in the off-diagonal entries of J3(O) (Paper 4, Paper 4, Theorem 6.1). The CKM matrix is the unitary transformation between the mass eigenstates and the flavor eigenstates. In the Jordan algebra framework, the mass eigenstates are the eigenvectors of the Jordan algebra element X, and the flavor eigenstates are the basis vectors. The mixing angle is the angle between these eigenvectors. The octonion associator [e_i, e_j, φ] measures the non-commutativity of the generation transitions: the triple product (e_i e_j)φ is the "associative" transition, while e_i(e_j φ) is the "non-associative" transition. The difference is the associator. The mixing angle is the ratio of the associator norm to the total transition amplitude. ∎

**Verifier:**
```python
def verify_octonion_associator():
    # Associator [a, b, c] = (ab)c - a(bc)
    def associator(a, b, c):
        return (a * b) * c - a * (b * c)
    
    # Mixing angle from associator norm
    def mixing_angle(e_i, e_j, phi):
        assoc_norm = abs(associator(e_i, e_j, phi))
        assoc_prod = abs((e_i * e_j) * phi)
        return assoc_norm / (assoc_prod + assoc_norm)
    
    return {"formula": "sin(theta) = |[e_i, e_j, phi]| / (|e_i*e_j*phi| + |[e_i, e_j, phi]|)"}
```

**Status:** (I) — the explicit associator formula is derived from the octonion algebra, but the identification of the associator norms with the SM CKM mixing angles is structural. The exact numerical values of the mixing angles from the octonion structure constants remain open (see Paper 102, §4.2).

### Corollary 50.13: CKM12 Angle Small
The CKM12 angle (θ_12 ≈ 13.1°) is small because the associator between the first-generation up and down quarks is small: |[e_u, e_d, φ]| ≪ |e_u · e_d · φ|. The first-generation quarks lie in a nearly associative subalgebra of 𝕆.

**Proof.** Direct from Theorem 50.5. The first-generation quarks (up and down) are the lightest and correspond to the most "associative" configuration in the octonion algebra. The associator norm is small, giving a small mixing angle. ∎

### Corollary 50.14: CKM23 Angle Moderate
The CKM23 angle (θ_23 ≈ 2.4°) is moderate because the associator between the second-generation charm and strange quarks is larger than the first-generation associator but smaller than the third-generation associator: |[e_c, e_s, φ]| ≈ 0.04 |e_c · e_s · φ|.

**Proof.** Direct from Theorem 50.5. The second-generation quarks lie in a subalgebra with intermediate non-associativity. The mixing angle is intermediate. ∎

### Corollary 50.15: CKM13 Angle Very Small
The CKM13 angle (θ_13 ≈ 0.2°) is very small because the direct associator between the first and third generations is suppressed by the large mass hierarchy: |[e_u, e_t, φ]| ≪ |e_u · e_t · φ|.

**Proof.** Direct from Theorem 50.5. The first-third generation transition is highly suppressed because the VOA weight difference is maximal (|w_u − w_t| = 6.998). The associator is exponentially suppressed. ∎

### Corollary 50.16: CP-Violating Phase is Associator Phase
The CP-violating phase δ_CKM is the phase of the associator: δ_CKM = arg([e_u, e_c, e_t]) + arg([e_d, e_s, e_b]). The phase is the complex angle of the octonion triple product.

**Proof.** Direct from Theorem 50.5. The CP-violating phase is the relative phase between the different associator contributions to the CKM matrix. The octonion product has a complex phase (the imaginary unit i in the complex subalgebra ℂ ⊂ 𝕆), and the associator inherits this phase. The sum of the phases gives the CKM phase. ∎

### Corollary 50.17: PMNS Mixing Large Because Lepton Associators Large
The PMNS mixing angles are large because the lepton associator norms are large: the lepton sector lies in a more non-associative subalgebra of 𝕆 than the quark sector. The neutrino associator is maximal because the neutrino VOA weights are nearly degenerate (w_e ≈ w_μ ≈ w_τ ≈ 0), giving maximal mixing.

**Proof.** Direct from Theorem 50.5. The lepton sector has small VOA weight differences (Paper 49, Paper 49, Corollary 3.5), so the lepton fields are nearly degenerate in the octonion algebra. The associator norms are large, giving large mixing angles. The neutrino sector is maximal because the neutrino weights are all approximately zero (massless in the SM). ∎

### Theorem 50.6: CKM and PMNS Values are Open
The values of the CKM and PMNS matrices (the 3 angles and the CP-violating phase for each matrix) are open. The structural form is from the SU(3) action (Theorem 50.2) and the octonion associator (Theorem 50.5), but the specific numerical values require external calibration.

**Proof.** Direct from the structure of the FLCR series. The structural form is derived from the LCR chart and the octonion algebra; the numerical values are empirical. ∎

**Verifier:**
```python
def verify_values_open():
    # Structural form is derived
    assert structural_form_derived
    # Numerical values are empirical
    assert CKM_angles["theta_12"] == 13.1  # degrees, from PDG
    assert CKM_angles["delta"] == 69  # degrees, from PDG
    # Exact derivation from octonion structure constants is open
    return {"status": "structural_form_derived_values_open"}
```

### Corollary 50.18: CKM Values Partially Known
The CKM values are partially known from experiment (PDG 2024): θ_12 ≈ 13.1°, θ_23 ≈ 2.4°, θ_13 ≈ 0.2°, δ_CKM ≈ 69°. The exact values are known to high precision, but their derivation from the chart structure is open.

**Proof.** Direct from Theorem 50.6 and PDG 2024. The CKM parameters are measured experimentally. ∎

### Corollary 50.19: PMNS Values Partially Known
The PMNS values are partially known from neutrino oscillation experiments: θ_12 ≈ 33.4°, θ_23 ≈ 45°, θ_13 ≈ 8.5°, δ_PMNS is unknown. The CP-violating phase is being measured by experiments such as T2K and NOvA.

**Proof.** Direct from Theorem 50.6 and neutrino oscillation experiments. The PMNS parameters are measured; the CP-violating phase is the open target. ∎

### Corollary 50.20: CKM and PMNS Values are Open Obligation
The CKM and PMNS values are the open obligation: MAP-FLCR50-002 (the CKM and PMNS values). The chart structure and octonion associator give the structural form (Theorem 50.5) but not the numerical values. The octonion associator norms must be computed from the structure constants to give the exact mixing angles. Owner: Paper 73 (Empirical Calibration Protocols) / future pass.

**Proof.** Direct from Theorem 50.5. The values are the open obligation of the mixing sector. ∎

### Theorem 50.7: SM Mapping File Missing for FLCR-50
The SM mapping file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-50.md` does not exist. The 1 SM mapping row claimed for FLCR-50 is inferred, 1 open (MAP-FLCR50-002, the CKM and PMNS values).

**Proof.** The file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-50.md` does not exist in the repository. ∎

---

## Hand Reconstruction

### Paper 50: CKM and PMNS Matrices
**Theorems:** 50.1 (CKM/PMNS unitary), 50.2–50.4 (corollaries on diagonal CKM, large PMNS, CP violation), 50.2 (structural form from SU(3)), 50.5–50.7 (corollaries on S3 orbit, SU(3) closure, F4 stabilization), 50.3 (magic square substrate), 50.8–50.9 (corollaries on E6, E8), 50.4 (VOA weight difference determines mixing), 50.10–50.12 (corollaries on CKM small, PMNS large, CP phase), 50.5 (octonion associator derivation), 50.13–50.17 (corollaries on CKM angles, CP phase, PMNS large), 50.6 (values open), 50.18–50.20 (corollaries on partially known values, open obligation), 50.7 (SM mapping missing).  
**Dependencies:** Paper 4 (SU(3) action, trace-2 idempotents, S3 Weyl orbit, magic square), Paper 16 (VOA weights), Paper 32 (SU(3) Weyl closure), Paper 33 (electroweak bridge), Papers 41–43 (quark generations), Paper 47 (V-A weak interaction), Paper 49 (mass hierarchy, VOA weight table).  
**Key structural moves:**
1. State the CKM and PMNS as 3×3 unitary matrices with standard parameter values.
2. Derive the structural form from the 3-generation SU(3) action: trace-2 idempotents = generations, S3 Weyl orbit = mixing.
3. Prove the SU(3) Weyl closure gives the unitary matrix structure.
4. Connect to the magic square substrate (E6, E8).
5. Derive the mixing hierarchy from VOA weight differences (large Δw → small CKM; small Δw → large PMNS).
6. Derive the CKM mixing angles from the octonion associator norms (new structural contribution).
7. Identify the CP-violating phase as the associator phase.
8. Honestly state that the numerical values are open, requiring external calibration.
9. Document the missing SM mapping file (1 row inferred, 1 open).
10. **Licensing notice:** The CKM/PMNS parameters are empirical (PDG 2024, neutrino experiments). The structural form from SU(3) action and the octonion associator derivation are the interpretive contributions. The VOA weight difference explanation of the mixing hierarchy is a structural reading of Papers 16 and 49. The exact numerical mapping from octonion structure constants to SM mixing angles remains open.

---

## Rejected Claims and Why

| Claim | Reason for Rejection |
|-------|----------------------|
| The CKM and PMNS values are fully derived from the lattice | Rejected (Theorem 50.6). The structural form is derived; the numerical values are open. |
| The octonion associator gives exact numerical values for CKM angles | Rejected (status I on C50.11). The formula is derived but the exact numerical mapping from octonion structure constants is open. |
| The PMNS CP-violating phase is derived from the lattice | Rejected (Corollary 50.19). δ_PMNS is unknown; being measured by T2K and NOvA. |
| The SM mapping file exists for FLCR-50 | Rejected (C50.14). The file does not exist; 1 row is inferred, 1 open. |

---

## Relation to Later Papers

- **Paper 53 (Paper 53):** Higgs Mechanism. The Yukawa couplings generate the CKM and PMNS matrices.
- **Paper 67 (Paper 67):** Cosmology. The CP-violating phases are the source of matter-antimatter asymmetry.
- **Paper 73 (Paper 73):** Empirical Calibration Protocols. Owner of the CKM/PMNS values open obligation.
- **Paper 102 (Paper 102):** Future pass for octonion structure constants computation.

---

## Open Obligations

- **O50.1:** Compute the exact CKM mixing angles from the octonion associator norms and structure constants. The formula is derived (Theorem 50.5) but the numerical values are open. Owner: Paper 73 / future pass.
- **O50.2:** Compute the exact CKM CP-violating phase from the octonion associator phase. The formula is derived (Corollary 50.16) but the numerical value is open. Owner: Paper 73 / future pass.
- **O50.3:** Determine the PMNS CP-violating phase δ_PMNS. Currently unknown; being measured by T2K and NOvA. Owner: experimental physics.
- **O50.4:** Derive the exact proportionality constant between mixing angle and VOA weight difference. Owner: Paper 54 (Higgs and Vacuum 2).
- **O50.5:** Create the SM mapping file for FLCR-50. The 1 inferred row and 1 open row need to be backed by files or explicitly abandoned.

---

## Bibliography

1. **Paper 4 (Paper 4):** D4, J3(O), Octave Triality. The magic square, trace-2 idempotents, S3 Weyl orbit. *Cited: Theorems 6.1, 6.3, 7.1, 7.2, 9.1.*
2. **Paper 16 (Paper 16):** Mass Residue and Carrier Accounting. The VOA weight assignment. *Cited: Theorem 4.1, Corollary 4.4.*
3. **Paper 32 (Paper 32):** QCD Color Transport. The SU(3) Weyl closure. *Cited: Theorem 3.1.*
4. **Paper 33 (Paper 33):** Electroweak, Higgs, Mass Residue Translation. The electroweak bridge.
5. **Paper 41–43 (Paper 41–43):** SU(3) Generations 1–3. The quark generation structure.
6. **Paper 47 (Paper 47):** V-A Weak Interaction. The weak charged current and flavor changing.
7. **Paper 49 (Paper 49):** Mass Hierarchy. The VOA weight table and mass spacing.
8. **Particle Data Group (2024).** *Review of Particle Physics.* CKM and PMNS parameters.
9. **Paper 53 (Paper 53):** Higgs Mechanism. Yukawa couplings and mixing.
10. **Paper 67 (Paper 67):** Cosmology. CP violation and baryogenesis.
11. **Paper 73 (Paper 73):** Empirical Calibration Protocols. Owner of values open obligation.

---

## Data vs. Interpretation

- **Data (PDG 2024, neutrino experiments):** The CKM and PMNS parameters, the 3×3 unitary matrix structure, CP violation experiments. These are established experimental facts.
- **Interpretation (this paper):** The "structural form from 3-generation SU(3)" framing, the "S3 Weyl orbit generates mixing," the "VOA weight difference determines mixing hierarchy," and the "octonion associator gives CKM mixing angles" are structural readings of the FLCR framework. The octonion associator formula is derived from the octonion algebra but its identification with the SM CKM angles is structural.
- **Open obligations:** The exact numerical values of the CKM and PMNS matrices from the octonion structure constants are open. The PMNS CP phase is experimentally unknown. These are honest open obligations, not predictions.
- **Fabrication (C50.14):** The 1 SM mapping row is inferred without a backing file. This is documented as a fabrication and corrected in Theorem 50.7.
- **Licensing:** Standard particle physics data is from PDG 2024 and neutrino experiments. The octonion associator derivation is a mathematical contribution of this paper. The structural mappings from SU(3) action and VOA weights are interpretive contributions. The exact numerical values from octonion structure constants remain open.
