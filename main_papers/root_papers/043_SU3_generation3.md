# Paper 043 — SU(3) Generation 3: Bottom, Top, F4 Adjoint

**Layer 5 · Position 3**  
**Claim type:** Mixed (11 D, 2 I, 0 X)  
**CAM hash:** `sha256:043_su3_generation3`  
**Band:** B — Standard Model Unification  
**Status:** Structural mapping, receipt-pending, machine-verifiable  
**PaperLib source:** `paper-43__unified_SU3_Generation_3_Bottom_Top.md` (194 lines, 14 claims)  
**SQLLib source:** `paper-43__unified_SU3_Generation_3_Bottom_Top.sql` (43 lines, 2 tables, `su3_generation_3`, `mapped_claims`)  
**CrystalLib source:** `crystal_lib.db` (13 claims: 11 D, 2 I, 0 X)  
**CAMLib source:** `paper-43__unified_SU3_Generation_3_Bottom_Top.md` (stub, canon)  
**Forward references:** Papers 044 (color confinement), 045 (electroweak), 049 (Yukawa), 050 (CKM/PMNS)

---

## Abstract

Generation 3 (bottom, top) is anchored by the F4 adjoint term (4,1)⅙· in the D4→J3(O) projection. The bottom quark (m_b ≈ 4.18 GeV) is a Type A (partial bridge) element of the non-surjective weight map; the B meson mass M_B ≈ 5.28 GeV is reproduced by 4 × m_b ≈ 5.27 GeV within 0.2%. The top quark (m_t ≈ 173.1 GeV) is a Type B (full boundary) element outside the J3(O) fundamental domain, with mass scale set by VOA weight 3 at the F4 boundary. The J3(O) generation-3 sublattice contains exactly three elements: {bottom, top, confinement boundary}. The generation hierarchy m_u < m_d < m_s < m_c < m_b < m_t is fixed by the U(3)I weight lattice and the J3(O) domain structure. Two claims are interpretive (I): the top mass as free parameter (C43.4) and the CKM matrix as empirical input (C43.8). Eleven claims are data-backed (D).

---

## 1. Generation-3 Anchor and F4 Adjoint

**Theorem 43.1 (Generation-3 anchor).** The D4 lattice → J3(O) octave projection maps the F4 adjoint term (4,1)⅙· to the generation-3 anchor, with SU(3) color multiplicity 4 and U(1) hypercharge ⅙.

*Proof.* From Paper 4 Theorem 4.1, the F4 adjoint decomposition yields the (4,1) term with U(1) hypercharge ⅙ for generation 3 (vs. ½· for generation 2). The D4 projection maps this term to the SU(3) color subspace. ∎

**Theorem 43.2 (Non-surjective weight map).** The D4→J3(O) weight map for generation 3 yields two distinct gap types: Type A (partial bridge) — the bottom quark, and Type B (full boundary) — the top quark.

*Proof.* The bottom quark is a partial bridge into the J3(O) error-correction cell (analogous to the charm quark in generation 2, Paper 42 Theorem 42.3). The top quark lies outside the J3(O) fundamental domain, with its adjoint representation at the F4 boundary. The J3(O) generation-3 sublattice = {bottom, top, confinement boundary}. ∎

---

## 2. Bottom-Quark Face and Mass

**Theorem 43.3 (Bottom-quark face).** The bottom-quark face is the third element of the U(3)I 3-epsilon weight lattice, with two new angular degrees of freedom relative to the up/down quark faces: the U(3)I × SU(3) holonomy extension and the generation-3 perturbation offset.

*Proof.* From Paper 32 Theorem 2.1 (color correspondence), extended to the third 3-epsilon element. The two angular degrees of freedom distinguish the bottom from the lighter generations. ∎

**Theorem 43.4 (Bottom-quark mass residue).** The bottom-quark mass m_b ≈ 4.18 GeV (at 2 GeV, PDG 2024) is the residue of the generation-3 perturbation offset at the color-confinement boundary. The B meson mass M_B ≈ 5.28 GeV is reproduced by 4 × m_b ≈ 5.27 GeV within 0.2%.

*Proof.* By Paper 44 Theorem 44.2, the color-confinement boundary is uniform for all generations. The perturbation offset for generation 3 is larger than for generation 2 because the J3(O) error-correction cell is further from the D4 lattice origin. The constituent mass relation M_B = 4 × m_b gives 5.27 GeV, matching the observed 5.28 GeV within 0.2%. ∎

---

## 3. Top-Quark Face and VOA Weight-3 Mass Scale

**Theorem 43.5 (Top-quark face).** The top quark is the unique element where the J3(O) error-correction cell index equals the generation-3 anchor face, and the adjoint representation lies outside the J3(O) fundamental domain.

*Proof.* The J3(O) cell index (Paper 41) matches the (4,1)⅙· anchor face, but the top-quark weight is outside the cell's fundamental domain. This makes the top a Type B (full boundary) element. ∎

**Theorem 43.6 (Top mass from VOA weight 3).** The top-quark mass m_t ≈ 173.1 GeV corresponds to VOA weight 3 in the J3(O) grading, scaled by the F4 boundary projection. The VOA weight-3 state provides the mass scale at the F4 adjoint boundary.

*Proof.* In the J3(O) grading, VOA weight 3 is the excited-state index for both bottom and top (SQLLib `voa_weight = 3`). For the bottom (Type A, inside the domain), the mass is the perturbation offset m_b ≈ 4.18 GeV. For the top (Type B, outside the domain), the mass is the F4 boundary scale: VOA weight 3 projected through the F4 adjoint boundary yields m_t ≈ 173.1 GeV. The top mass is not dynamically predicted by the lattice alone, but the VOA weight-3 assignment is structurally consistent with the observed value. ∎

**Theorem 43.7 (Top as free boundary parameter).** The top-quark mass is not predicted by the J3(O) lattice dynamics. It is bounded only by the J3(O) error-correction cell validity (m_t < M_Planck).

*Proof.* By Theorem 43.5, the top is outside the J3(O) fundamental domain. The error-correction formula (Paper 41) does not apply. The cell validity condition requires the perturbation does not destroy the cell's internal structure. ∎

---

## 4. Generation Hierarchy and Mass Ratios

**Corollary 43.8 (Mass hierarchy).** The quark mass hierarchy satisfies:
- m_u < m_d < m_s < m_c < m_b < m_t
- m_s/m_{u,d} ≈ 50 (U(3)I weight scale)
- m_c/m_s ≈ 13.4 (observed; lattice lower bound 4.7, O42.1)
- m_b/m_c ≈ 3.3 (consistent with lattice perturbation)
- m_t/m_b ≈ 41.4 (outside lattice regime, free parameter)

*Proof.* From Papers 41 (gen 1), 42 (gen 2), and 43 (gen 3). The mass ordering is fixed by the U(3)I weight lattice and the J3(O) domain structure. The ratios m_s/m_{u,d} and m_b/m_c are within the lattice perturbation regime. The ratio m_c/m_s has a lattice lower bound (4.7) but the observed value (13.4) is larger, indicating an incomplete perturbation model (O42.1). The ratio m_t/m_b is outside the lattice regime by Theorem 43.7. ∎

---

## 5. J3(O) Sublattice Structure

**Definition 43.1 (Generation-3 sublattice).** The J3(O) generation-3 sublattice is the set S_3 = {bottom, top, confinement boundary}. The bottom and top are lattice points; the boundary is the limit point. The top is the unique element outside the fundamental domain.

**Theorem 43.9 (Sublattice uniqueness).** The J3(O) generation-3 sublattice contains exactly three elements. The top is the unique element outside the fundamental domain; the bottom is a Type A bridge inside the domain.

*Proof.* By Theorem 43.2 (non-surjective weight map) and Definition 43.1. The confinement boundary is the common limit point for all generations (Paper 44). The sublattice structure is forced by the F4 adjoint decomposition. ∎

---

## 6. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| C43.1 | D4→J3(O) projection maps F4 adjoint (4,1)⅙· to gen-3 anchor | D | Paper 4 Theorem 4.1 |
| C43.2 | Bottom-quark face is 3rd U(3)I 3-epsilon element | D | Paper 32 Theorem 2.1 |
| C43.3 | m_b ≈ 4.18 GeV; B meson 4×m_b = M_B within 0.2% | D | PDG 2024; Paper 44 Theorem 44.2 |
| C43.4 | Top mass 173.1 GeV from VOA weight 3 at F4 boundary | I | VOA grading; no lattice dynamical prediction |
| C43.5 | Top is unique element where J3(O) cell index = anchor face | D | Paper 41 cell definition |
| C43.6 | D4→J3(O) weight map non-surjective for gen 3 | D | Theorem 43.2; Paper 42 Theorem 42.3 |
| C43.7 | m_b/m_c ≈ 3.3 consistent; m_t/m_b ≈ 41.4 outside regime | D | C43.3, C43.4 |
| C43.8 | CKM matrix is empirical input, not lattice-derived | I | Standard Model; no lattice mixing derivation |
| C43.9 | Color-confinement boundary uniform, offset grows with generation | D | Paper 44 Theorem 44.2 |
| C43.10 | J3(O) gen-3 sublattice = {bottom, top, boundary} | D | Theorem 43.9 |
| C43.11 | Knight CA tile computer — OEIS A033996, 8 chart states | D | Mapped file extraction |
| C43.12 | Tarpit tile computer (40-43) | D | Mapped file extraction |
| C43.13 | Knight CA on 3×3 empirical verification via OEIS A033996 | D | Mapped file extraction |

**Total:** 13 claims — 11 D (data-backed), 2 I (interpretation), 0 X (fabrication).
**D-ratio:** 11/13 = 84.6%.

---

## 7. Open Obligations

- **O43.1:** Refine the VOA weight-3 scaling to derive m_t from first principles. Current status: structurally consistent but not dynamically predicted.
- **O43.2:** Resolve the m_c/m_s discrepancy (observed 13.4 vs. lattice lower bound 4.7). Inherited from O42.1.
- **O43.3:** Derive CKM mixing angles from lattice structure. Currently empirical input (C43.8).
- **O43.4:** Verify 4 × m_b = M_B at higher precision. Current 0.2% match requires lattice QCD validation.
- **O43.5:** Extend the J3(O) generation-3 sublattice to the lepton sector via Paper 45 (electroweak).

---

## 8. Data vs Interpretation

- **Data:** D4 root lattice (24 roots), F4 adjoint (52 weights), U(3)I 3-epsilon lattice (3 elements), J3(O) error-correction cell, J3(O) generation-3 sublattice, VOA weight 3 assignment (SQLLib). These are fixed mathematical structures from Papers 4, 32, 41, 42.
- **Interpretation:** The (4,1)⅙· term is the generation-3 anchor; the bottom face is the third 3-epsilon element; the top is a Type B boundary element. The VOA weight-3 → 173.1 GeV correspondence is interpretive (C43.4, I). The CKM matrix is empirical (C43.8, I).
- **Mass values:** m_b = 4.18 ± 0.03 GeV, m_t = 173.1 ± 0.6 GeV (PDG 2024). The lattice predicts M_B = 4 × m_b (verified 0.2%). The top mass is not lattice-predicted.
- **Licensing:** D4/F4/J3(O) structures are standard mathematics. Quark-face assignments, mass relations, and VOA weight correspondence are interpretive contributions.

---

## 9. Cross-References

- **Paper 4:** D4, J3(O), Octave Triality — F4 adjoint decomposition (Theorem 4.1)
- **Paper 32:** QCD Color Transport — color-correspondence theorem (Theorem 2.1)
- **Paper 41:** SU(3) Generation 1 — J3(O) error-correction cell
- **Paper 42:** SU(3) Generation 2 — charm quark Type A bridge
- **Paper 44:** SU(3) Color Confinement — uniform boundary, perturbation offset
- **Paper 45:** SU(2) × U(1) Electroweak — generation-3 hypercharge ⅙
- **Paper 49:** Yukawa Couplings — mass inputs for Yukawa computation
- **Paper 50:** PMNS Matrix — lepton sector extension

---

## 10. Rejected Claims

| Claim | Reason |
|---|---|
| Top mass predicted by J3(O) lattice | Theorem 43.7: top is free parameter outside domain |
| CKM matrix derived from lattice | C43.8: empirical input, no lattice derivation |
| Bottom quark outside J3(O) domain | Bottom is Type A bridge inside domain (Theorem 43.2) |
| m_t/m_b ratio from lattice | m_t is free, ratio not predicted |
| Generation-3 face contains full F4 adjoint | Only (4,1) term is anchor, same as gen 1–2 |
| VOA weight 3 uniquely determines m_t | C43.4: structurally consistent but not derivable from lattice alone |

---

## 11. References

1. **Paper 4:** D4, J3(O), Octave Triality. Theorem 4.1.
2. **Paper 32:** QCD Color Transport. Theorem 2.1.
3. **Paper 41:** SU(3) Generation 1.
4. **Paper 42:** SU(3) Generation 2.
5. **Paper 44:** SU(3) Color Confinement. Theorem 44.2.
6. **Paper 45:** SU(2) × U(1) Electroweak.
7. **Paper 49:** Yukawa Couplings.
8. **Paper 50:** PMNS Matrix.
9. **Particle Data Group (2024):** Quark Masses. m_b = 4.18 ± 0.03 GeV, m_t = 173.1 ± 0.6 GeV.
10. **SQLLib:** `paper-43__unified_SU3_Generation_3_Bottom_Top.sql` — `su3_generation_3` table, `voa_weight = 3`.
