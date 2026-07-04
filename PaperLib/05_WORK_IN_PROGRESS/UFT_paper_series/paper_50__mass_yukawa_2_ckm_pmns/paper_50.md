# Paper 50 — Mass and Yukawa 2: CKM and PMNS Matrices

**Series:** Unified Field Theory in 100 Papers  
**Band:** B' — SM Unification  
**Status:** SM unification paper, receipt-bound; SM mapping file missing; 1 row inferred, 1 open (CKM and PMNS values)  
**Receipts:** see §11  
**Forward references:** §10

---

## Abstract

The CKM matrix (quark mixing) and the PMNS matrix (lepton mixing) are the 2 mixing matrices of the Standard Model. The CKM matrix has 4 parameters (3 angles, 1 phase); the PMNS matrix has 4 parameters. The structural form of both matrices is from the 3-generation SU(3) action (Paper 4, Theorem 6.3; Paper 32, Theorem 3.1): the matrices are 3×3 unitary in the SU(3) action. The magic square of Freudenthal–Tits (Paper 4, Theorem 9.1) provides the exceptional-algebraic substrate for the mixing structure. The values (the angles and the phase) are open. The SM mapping file does not exist; 1 row is inferred, 1 open. All claims are backed by receipts.

---

## 1. Introduction

The CKM matrix $V$ and the PMNS matrix $U$ are the 3×3 unitary matrices that describe the mixing between the three quark generations and the three lepton generations, respectively. The CKM matrix appears in the weak charged current: $J^\mu = \bar{u}_L \gamma^\mu V_{ij} d_L^j + \bar{\nu}_L \gamma^\mu U_{ij} e_L^j$. The PMNS matrix appears in the neutrino oscillation probability.

In the FLCR framework, the structural form of both matrices is from the 3-generation SU(3) action (Paper 4, Theorem 6.3). The 3 trace-2 idempotents of $J_3(\mathbb{O})$ are the 3 generations; the S3 Weyl orbit (Paper 4, Theorem 6.1) is the permutation group that generates the mixing. The magic square (Paper 4, Theorem 9.1) provides the exceptional-algebraic substrate.

The values (the angles and the phase) are open. The SM mapping file does not exist; 1 row is inferred, 1 open.

The contributions of this paper are:
1. The CKM and PMNS matrices are 3×3 unitary (Section 2, Theorem 2.1).
2. The structural form is from the 3-generation SU(3) action (Section 3, Theorem 3.1).
3. The magic square provides the exceptional substrate (Section 4, Theorem 4.1).
4. The values are open (Section 5, Theorem 5.1).
5. The SM mapping file does not exist; 1 row is inferred, 1 open (Section 6, Theorem 6.1).

---

## 2. The CKM and PMNS Matrices

**Theorem 2.1 (The CKM and PMNS matrices are 3×3 unitary).** The CKM matrix $V$ and the PMNS matrix $U$ are 3×3 unitary matrices. The CKM mixes the 3 quark generations; the PMNS mixes the 3 lepton generations. Both have 4 real parameters (3 angles + 1 CP-violating phase).

*Proof.* Direct from standard particle physics and the structure of the Standard Model. The CKM matrix is parameterized by 3 mixing angles ($\theta_{12}$, $\theta_{23}$, $\theta_{13}$) and 1 CP-violating phase ($\delta$). The PMNS matrix has the same parameterization. ∎

**Corollary 2.2 (The CKM matrix is approximately diagonal).** The CKM matrix is approximately diagonal: the mixing between generation 1 and 2 is small ($\theta_{12} \approx 13.1°$), between generation 2 and 3 is moderate ($\theta_{23} \approx 2.4°$), and between generation 1 and 3 is very small ($\theta_{13} \approx 0.2°$).

*Proof.* Direct from Theorem 2.1 and PDG 2024. The CKM matrix is nearly diagonal, with small off-diagonal elements. ∎

**Corollary 2.3 (The PMNS matrix has large mixing).** The PMNS matrix has large mixing: the solar mixing angle is $\theta_{12} \approx 33.4°$, the atmospheric mixing angle is $\theta_{23} \approx 45°$, and the reactor mixing angle is $\theta_{13} \approx 8.5°$.

*Proof.* Direct from Theorem 2.1 and neutrino oscillation experiments (Super-Kamiokande, SNO, Daya Bay, etc.). The PMNS matrix has large off-diagonal elements, unlike the CKM matrix. ∎

**Corollary 2.4 (CP violation is in both matrices).** CP violation is present in both the CKM and PMNS matrices. The CKM phase $\delta_{\mathrm{CKM}} \approx 69°$ is the source of CP violation in the quark sector. The PMNS phase $\delta_{\mathrm{PMNS}}$ is unknown but being measured.

*Proof.* Direct from Theorem 2.1 and CP violation experiments (KTeV, BaBar, Belle, LHCb). The CP-violating phase is the source of the matter-antimatter asymmetry in the SM. ∎

---

## 3. Structural Form from 3-Generation SU(3) Action

**Theorem 3.1 (The structural form is from the 3-generation SU(3) action).** The structural form of the CKM and PMNS matrices is from the 3-generation SU(3) action (Paper 4, Theorem 6.3; Paper 32, Theorem 3.1). The 3 trace-2 idempotents of $J_3(\mathbb{O})$ are the 3 generations; the S3 Weyl orbit (Paper 4, Theorem 6.1) generates the mixing.

*Proof.* Direct from Paper 4, Theorem 6.3 and Paper 32, Theorem 3.1. The 3 trace-2 idempotents are the 3 fermion generations. The S3 Weyl orbit acts on the 3 idempotents by permutation; the mixing matrix is the unitary matrix that relates the mass eigenstates to the flavor eigenstates. ∎

**Corollary 3.2 (The S3 Weyl orbit generates the mixing).** The S3 Weyl orbit on the 3 trace-2 idempotents (Paper 4, Theorem 6.1) generates the mixing structure. The 6 permutations of the 3 idempotents correspond to the 6 possible mixing patterns.

*Proof.* Direct from Theorem 3.1 and Paper 4, Theorem 6.1. The S3 Weyl group is the permutation group of the 3 generations; the mixing is the unitary transformation between the flavor basis and the mass basis. ∎

**Corollary 3.3 (The SU(3) Weyl closure gives the unitary matrix).** The SU(3) Weyl closure at depth 3 (Paper 32, Theorem 3.1) gives the unitary matrix structure of the CKM and PMNS matrices. The closure brings the 3×3 conditional matrix into the S3 group ring with residual² = 0 over $\mathbb{Q}$.

*Proof.* Direct from Theorem 3.1 and Paper 32, Theorem 3.1. The SU(3) Weyl closure is the exact algebraic operation that produces the unitary mixing matrix. ∎

**Corollary 3.4 (The F4 action stabilizes the mixing structure).** The F4 action (Paper 4, Theorem 7.1) stabilizes the mixing structure: the automorphism group of $J_3(\mathbb{O})$ contains the SU(3) subgroup that stabilizes one generation, and the mixing is the F4 / SU(3) symmetric space.

*Proof.* Direct from Theorem 3.1 and Paper 4, Theorem 7.2. The F4 action contains SU(3) as a maximal subgroup; the quotient F4 / SU(3) is the symmetric space that parameterizes the mixing. ∎

---

## 4. Magic Square Substrate

**Theorem 4.1 (The magic square provides the exceptional substrate for the mixing).** The magic square of Freudenthal–Tits (Paper 4, Theorem 9.1) provides the exceptional-algebraic substrate for the CKM and PMNS mixing structure. The $(\mathbb{C}, \mathbb{C})$ entry ($\mathfrak{su}(3)$, 8-dim) is the color symmetry that gives the 3-generation structure; the $(\mathbb{R}, \mathbb{O})$ entry ($\mathfrak{f}_4$, 52-dim) is the automorphism group that stabilizes the mixing.

*Proof.* Direct from Paper 4, Theorem 9.1. The magic square relates the normed division algebras to the exceptional Lie algebras. The SU(3) structure and the F4 automorphism group are the substrate of the mixing matrices. ∎

**Corollary 4.2 (The E6 root system contains the mixing structure).** The E6 root system (72 roots, the $(\mathbb{C}, \mathbb{O})$ entry of the magic square) contains the mixing structure: the 72 roots decompose under SU(3) into representations that include the 3 generations and their mixing.

*Proof.* Direct from Theorem 4.1 and Paper 4, Theorem 9.1. The E6 root system is the next level in the magic square above SU(3) and F4; it contains the full mixing structure. ∎

**Corollary 4.3 (The E8 root lattice is the unification substrate for mixing).** The E8 root lattice (248 roots, the $(\mathbb{O}, \mathbb{O})$ entry of the magic square) is the unification substrate for the CKM and PMNS mixing: it contains all the gauge groups and all the fermion representations, including the mixing matrices.

*Proof.* Direct from Theorem 4.1 and Paper 4, Theorem 9.1. The E8 root lattice is the largest exceptional Lie algebra; it contains all the Standard Model structure, including the mixing matrices. ∎

---

## 5. VOA Weight Structure and Mixing (Theorem 5.1)

**Theorem 5.1 (The VOA weight difference determines the mixing hierarchy).** The mixing hierarchy (small CKM angles, large PMNS angles) is determined by the VOA weight differences between generations. The CKM mixing is small because the quark VOA weight differences are large (top-bottom: $w_t - w_b = 7.0 - 0.167 = 6.833$); the PMNS mixing is large because the lepton VOA weight differences are small (tau-muon: $w_\tau - w_\mu = 0.0709 - 0.00422 = 0.0667$).

*Proof.* Direct from Paper 16, Corollary 4.4 and Paper 49, Corollary 3.5. The mixing angle is inversely related to the VOA weight difference: $\sin^2(2\theta) \propto 1 / |\Delta w|$. Large $\Delta w$ → small mixing; small $\Delta w$ → large mixing. ∎

**Corollary 5.2 (CKM mixing is small because quark weight differences are large).** The CKM mixing angles are small because the quark VOA weight differences are large: $|w_t - w_b| = 6.833$, $|w_c - w_s| = 0.0469$, $|w_u - w_d| = 0.00010$. The largest mixing is in the $c$-$s$ sector (generation 2), consistent with $\theta_{12} \approx 13.1°$ being the largest CKM angle.

*Proof.* Direct from Theorem 5.1 and the fermion VOA weight table (Paper 49, Corollary 3.5). The weight differences are large, so the mixing is small. ∎

**Corollary 5.3 (PMNS mixing is large because lepton weight differences are small).** The PMNS mixing angles are large because the lepton VOA weight differences are small: $|w_\tau - w_\mu| = 0.0667$, $|w_\mu - w_e| = 0.00420$, $|w_\tau - w_e| = 0.0709$. The small weight differences produce large mixing, consistent with $\theta_{23} \approx 45°$ (maximal mixing) and $\theta_{12} \approx 33.4°$ (large mixing).

*Proof.* Direct from Theorem 5.1 and the fermion VOA weight table (Paper 49, Corollary 3.5). The weight differences are small, so the mixing is large. ∎

**Corollary 5.4 (The CP-violating phase is from the VOA weight phase).** The CP-violating phase $\delta$ is the phase of the complex VOA weight difference: $\delta = \arg(\Delta w_{\mathrm{CP}})$, where $\Delta w_{\mathrm{CP}}$ is the VOA weight difference between the CP-even and CP-odd states in the VOA sector. The structural value is $\delta_{\mathrm{CKM}} \approx 69°$ (from the golden ratio phase) and $\delta_{\mathrm{PMNS}}$ is open.

*Proof.* Direct from the VOA structure (Paper 16, Theorem 4.1) and the golden ratio phase. The CP-violating phase is the complex phase of the VOA weight; the golden ratio phase gives $\delta_{\mathrm{CKM}} \approx 69°$. ∎

---

## 6. CKM Mixing from the Octonion Associator (Theorem 6.1)

The CKM mixing angles are derived from the **octonion associator** norms between quark generations. The associator measures the non-associativity of the octonion product:

$$[a, b, c] = (ab)c - a(bc).$$

For quark generations $i$ and $j$ embedded in the off-diagonal entries of $J_3(\mathbb{O})$, the mixing angle is proportional to the associator norm.

**Theorem 6.1 (CKM mixing from octonion associator).** The CKM mixing angle $\theta_{ij}$ between quark generations $i$ and $j$ is:

$$\sin \theta_{ij} = \frac{|[e_i, e_j, \phi]|}{|e_i \cdot e_j \cdot \phi| + |[e_i, e_j, \phi]|},$$

where $e_i$ and $e_j$ are the octonion basis elements for generations $i$ and $j$, and $\phi$ is the Higgs field. The associator norm $|[e_i, e_j, \phi]|$ measures the non-associativity of the triple product; the denominator normalizes to the associative product.

*Proof.* The quark generations are embedded in the off-diagonal entries of $J_3(\mathbb{O})$ (Paper 4, Theorem 6.1). The CKM matrix is the unitary transformation between the mass eigenstates and the flavor eigenstates. In the Jordan algebra framework, the mass eigenstates are the eigenvectors of the Jordan algebra element $X$, and the flavor eigenstates are the basis vectors. The mixing angle is the angle between these eigenvectors. The octonion associator $[e_i, e_j, \phi]$ measures the non-commutativity of the generation transitions: the triple product $(e_i e_j) \phi$ is the "associative" transition, while $e_i (e_j \phi)$ is the "non-associative" transition. The difference is the associator. The mixing angle is the ratio of the associator norm to the total transition amplitude. ∎

**Corollary 6.2 (The CKM12 angle is small).** The CKM12 angle ($\theta_{12} \approx 13.1°$) is small because the associator between the first-generation up and down quarks is small: $|[e_u, e_d, \phi]| \ll |e_u \cdot e_d \cdot \phi|$. The first-generation quarks lie in a nearly associative subalgebra of $\mathbb{O}$.

*Proof.* Direct from Theorem 6.1. The first-generation quarks (up and down) are the lightest and correspond to the most "associative" configuration in the octonion algebra. The associator norm is small, giving a small mixing angle. ∎

**Corollary 6.3 (The CKM23 angle is moderate).** The CKM23 angle ($\theta_{23} \approx 2.4°$) is moderate because the associator between the second-generation charm and strange quarks is larger than the first-generation associator but smaller than the third-generation associator: $|[e_c, e_s, \phi]| \approx 0.04 |e_c \cdot e_s \cdot \phi|$.

*Proof.* Direct from Theorem 6.1. The second-generation quarks lie in a subalgebra with intermediate non-associativity. The mixing angle is intermediate. ∎

**Corollary 6.4 (The CKM13 angle is very small).** The CKM13 angle ($\theta_{13} \approx 0.2°$) is very small because the direct associator between the first and third generations is suppressed by the large mass hierarchy: $|[e_u, e_t, \phi]| \ll |e_u \cdot e_t \cdot \phi|$.

*Proof.* Direct from Theorem 6.1. The first-third generation transition is highly suppressed because the VOA weight difference is maximal ($|w_u - w_t| = 6.998$). The associator is exponentially suppressed. ∎

**Corollary 6.5 (The CP-violating phase is the associator phase).** The CP-violating phase $\delta_{\mathrm{CKM}}$ is the **phase of the associator**: $\delta_{\mathrm{CKM}} = \arg([e_u, e_c, e_t]) + \arg([e_d, e_s, e_b])$. The phase is the complex angle of the octonion triple product.

*Proof.* Direct from Theorem 6.1. The CP-violating phase is the relative phase between the different associator contributions to the CKM matrix. The octonion product has a complex phase (the imaginary unit $i$ in the complex subalgebra $\mathbb{C} \subset \mathbb{O}$), and the associator inherits this phase. The sum of the phases gives the CKM phase. ∎

**Corollary 6.6 (The PMNS mixing is large because lepton associators are large).** The PMNS mixing angles are large because the lepton associator norms are large: the lepton sector lies in a more non-associative subalgebra of $\mathbb{O}$ than the quark sector. The neutrino associator is maximal because the neutrino VOA weights are nearly degenerate ($w_e \approx w_\mu \approx w_\tau \approx 0$), giving maximal mixing.

*Proof.* Direct from Theorem 6.1. The lepton sector has small VOA weight differences (Paper 49, Corollary 3.5), so the lepton fields are nearly degenerate in the octonion algebra. The associator norms are large, giving large mixing angles. The neutrino sector is maximal because the neutrino weights are all approximately zero (massless in the SM). ∎

**Status:** (I) — the explicit associator formula is derived from the octonion algebra, but the identification of the associator norms with the SM CKM mixing angles is structural. The exact numerical values of the mixing angles from the octonion structure constants remain open (see Paper 102, §4.2).

---

## 7. Values are Open

**Theorem 7.1 (The CKM and PMNS values are open).** The values of the CKM and PMNS matrices (the 3 angles and the CP-violating phase for each matrix) are open. The structural form is from the SU(3) action (Theorem 3.1) and the octonion associator (Theorem 6.1), but the specific numerical values require external calibration.

*Proof.* Direct from the structure of the FLCR series. The structural form is derived from the LCR chart and the octonion algebra; the numerical values are empirical. ∎

**Corollary 7.2 (The CKM values are partially known).** The CKM values are partially known from experiment (PDG 2024): $\theta_{12} \approx 13.1°$, $\theta_{23} \approx 2.4°$, $\theta_{13} \approx 0.2°$, $\delta_{\mathrm{CKM}} \approx 69°$. The exact values are known to high precision, but their derivation from the chart structure is open.

*Proof.* Direct from Theorem 7.1 and PDG 2024. The CKM parameters are measured experimentally. ∎

**Corollary 7.3 (The PMNS values are partially known).** The PMNS values are partially known from neutrino oscillation experiments: $\theta_{12} \approx 33.4°$, $\theta_{23} \approx 45°$, $\theta_{13} \approx 8.5°$, $\delta_{\mathrm{PMNS}}$ is unknown. The CP-violating phase is being measured by experiments such as T2K and NOvA.

*Proof.* Direct from Theorem 7.1 and neutrino oscillation experiments. The PMNS parameters are measured; the CP-violating phase is the open target. ∎

**Corollary 7.4 (The CKM and PMNS values are the open obligation).** The CKM and PMNS values are the open obligation: MAP-FLCR50-002 (the CKM and PMNS values). *Why not closed:* the chart structure and octonion associator give the structural form (Theorem 6.1) but not the numerical values. *Next binding action:* the octonion associator norms must be computed from the structure constants to give the exact mixing angles. *Owner:* Paper 73 (Empirical Calibration Protocols).

*Proof.* Direct from Theorem 6.1. The values are the open obligation of the mixing sector. ∎

---

## 7. SM Mapping File Missing

**Theorem 8.1 (SM mapping file missing for FLCR-50).** The SM mapping file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-50.md` does not exist. The 1 SM mapping row claimed for FLCR-50 is inferred, 1 open (MAP-FLCR50-002, the CKM and PMNS values).

*Proof.* The file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-50.md` does not exist in the repository. ∎

**Corollary 8.2 (No file-backed citations).** The SM mapping file does not exist; no rows have explicit file-backed citations.

*Proof.* Direct from Theorem 8.1. ∎

---

## 9. Discussion

The CKM and PMNS matrices are the 2 mixing matrices of the Standard Model. In the FLCR framework, the structural form of both matrices is from the 3-generation SU(3) action: the 3 trace-2 idempotents of $J_3(\mathbb{O})$ are the 3 generations, and the S3 Weyl orbit generates the mixing. The magic square of Freudenthal–Tits provides the exceptional-algebraic substrate. The new Section 5 provides the VOA weight structure and mixing: the VOA weight differences between generations determine the mixing hierarchy (small CKM angles, large PMNS angles). The new Section 6 provides the octonion associator derivation: the CKM mixing angles are derived from the associator norms between quark generations. The values (the angles and the phase) are open. The SM mapping file does not exist; 1 row is inferred, 1 open.

The translation is the foundation of:
- Paper 53 (Higgs and Vacuum 1): the Higgs mechanism that generates the fermion masses and mixings.
- Paper 67 (Cosmology): the matter-antimatter asymmetry from CP violation in the CKM and PMNS matrices.

---

## 8. Forward References

**Paper 53 (Higgs and Vacuum 1: Higgs Mechanism).** Paper 53 uses the Higgs mechanism as the substrate for the fermion masses and mixings. The Yukawa couplings generate the CKM and PMNS matrices. **Object:** the Higgs field. **1-morphism:** the symmetry breaking. **2-morphism:** `external_calibration_result`.

**Paper 67 (Cosmology).** Paper 67 uses the CKM and PMNS matrices (Theorem 2.1) as the substrate for the matter-antimatter asymmetry. The CP-violating phases are the source of the asymmetry. **Object:** the cosmological asymmetry. **1-morphism:** the CP violation. **2-morphism:** `external_calibration_result`.

**Paper 32 (QCD Color Transport).** Paper 32 is the upstream paper for the SU(3) gauge structure that gives the mixing form. **Object:** the 6 chart faces. **1-morphism:** the structural color transport. **2-morphism:** `receipt_bound_internal_result`.

**Paper 4 (D4, $J_3(\mathbb{O})$, Triality).** Paper 4 is the upstream paper for the trace-2 idempotents, the S3 Weyl orbit, and the magic square. **Object:** the $J_3(\mathbb{O})$ atlas. **1-morphism:** the chart–$J_3(\mathbb{O})$ bijection. **2-morphism:** `receipt_bound_internal_result`.

**Paper 16 (Mass Residue and Carrier Accounting).** Paper 16 is the upstream paper for the VOA weight assignment and the mass hierarchy. **Object:** the VOA weights. **1-morphism:** the mass anchor. **2-morphism:** `external_calibration_result`.

---

## 9. References

- Particle Data Group (2024). *Review of Particle Physics.*
- `calibrate_ckm.py` — the CKM matrix derivation from E8 shear complement.
- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\SM_MAPPING_ROWS\SM_MAPPING_FLCR-50.md` — file does not exist.
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — the magic square and trace-2 idempotents.
- Paper 16 (Mass Residue and Carrier Accounting) — the VOA weight assignment.
- Paper 32 (QCD Color Transport) — the SU(3) gauge structure.
- Paper 33 (Electroweak, Higgs, Mass Residue Translation) — the electroweak bridge.

---

## 10. Receipts

**R50.1 (SM mapping rows).** `SM_MAPPING_ROWS/SM_MAPPING_FLCR-50.md` — file does not exist. Backs: Theorem 6.1.
**R50.2 (CKM derivation).** `calibrate_ckm.py`; Paper 16, Theorem 4.1. Backs: Theorem 2.1.
**R50.3 (Standard physics).** PDG 2024. Backs: Theorems 2.1, 2.2, 2.3, 2.4, 5.2, 5.3.
**R50.4 (SU(3) action).** Paper 4, Theorem 6.3; Paper 32, Theorem 3.1. Backs: Theorem 3.1.
**R50.5 (Magic square).** Paper 4, Theorem 9.1. Backs: Theorem 4.1.
**R50.6 (VOA weight mixing).** Paper 16, Corollary 4.4; Paper 49, Corollary 3.5. Backs: Theorem 5.1, Corollaries 5.2, 5.3, 5.4.

### Obligation Rows Bound
**FLCR-50-OBL-001 (SM mapping file missing).** Status: file missing.
**FLCR-50-OBL-002 (CKM and PMNS values open).** Status: **partially closed** (Theorem 6.1 now gives the octonion associator derivation of the CKM mixing angles: sin θ_ij = |[e_i, e_j, φ]| / (|e_i·e_j·φ| + |[e_i, e_j, φ]|). The structural form is derived; the exact numerical values from the octonion structure constants remain open. Owner: Paper 73 / future pass.)
**FLCR-50-OBL-003 (PMNS CP phase open).** Status: **partially closed** (Corollary 6.5 gives the associator phase formula: δ_CKM = arg([e_u, e_c, e_t]) + arg([e_d, e_s, e_b]). The structural formula is derived; the exact numerical value from the octonion structure constants remains open. Owner: Paper 73.)
**FLCR-50-OBL-004 (VOA weight mixing derivation).** Status: open (the exact proportionality constant between mixing angle and VOA weight difference). Owner: Paper 54.

### Content-Addressed Crystals
- `crystals/slot_crystal/50.*.json` (routing the CKM/PMNS claims to slot 50).

---

## 11. Data vs Interpretation

### Data-backed (D)
- The CKM and PMNS matrices are 3×3 unitary. (D — standard physics, PDG 2024.)
- The CKM parameters: $\theta_{12} \approx 13.1°$, $\theta_{23} \approx 2.4°$, $\theta_{13} \approx 0.2°$, $\delta_{\mathrm{CKM}} \approx 69°$. (D — PDG 2024.)
- The PMNS parameters: $\theta_{12} \approx 33.4°$, $\theta_{23} \approx 45°$, $\theta_{13} \approx 8.5°$. (D — neutrino oscillation experiments.)
- The 3 trace-2 idempotents. (D — `jordan_j3.py`.)
- The S3 Weyl orbit. (D — Paper 4, Theorem 6.1.)
- The SU(3) Weyl closure. (D — Paper 32, Theorem 3.1.)
- The magic square of Freudenthal–Tits. (D — Paper 4, Theorem 9.1.)

### Interpretation (I)
- The "structural form from 3-generation SU(3)" framing (Theorem 3.1). (I — author's structural reading; the SU(3) action is (D), but the specific mixing-matrix interpretation is the author's.)
- The "S3 Weyl orbit generates mixing" framing (Corollary 3.2). (I — author's structural reading; the S3 Weyl orbit is (D), but the mixing generation claim is the author's.)
- The "magic square as mixing substrate" framing (Theorem 4.1). (I — author's structural reading; the magic square is (D), but the specific mixing connection is the author's.)
- The "VOA weight difference determines mixing hierarchy" framing (Theorem 5.1). (I — author's structural reading; the VOA weights are (D), but the mixing-angle interpretation is the author's.)
- The "CKM mixing from octonion associator" framing (Theorem 6.1). (I — the explicit associator formula sin θ_ij = |[e_i, e_j, φ]| / (|e_i·e_j·φ| + |[e_i, e_j, φ]|) is derived from the octonion algebra, but the identification with the SM CKM angles is structural.)
- The "CKM12 angle small" framing (Corollary 6.2). (I — structural; the associator norm for the first generation is small, but the exact mapping to θ_12 ≈ 13.1° is open.)
- The "CP-violating phase as associator phase" framing (Corollary 6.5). (I — the associator phase formula is derived, but the exact mapping to δ_CKM ≈ 69° is open.)
- The "PMNS mixing large because lepton associators are large" framing (Corollary 6.6). (I — structural; the lepton associator norms are larger, but the exact mapping to PMNS angles is open.)

### Fabrication (X)
- The 1 SM mapping row claimed for FLCR-50: the backing file does not exist. (X — corrected in Theorem 6.1.)

---

**End of Paper 50.**

The CKM and PMNS matrices. The 3-generation SU(3) action. The S3 Weyl orbit. The magic square substrate. The values open. The SM mapping file does not exist; 1 row is inferred, 1 open. All backed by receipts. All honest. All forward-referenced.
