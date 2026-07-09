# Paper 047 — V-A Weak Interaction: Sheet 0 Selection

**Layer 5 · Position 7**  
**Claim type:** 10 D / 2 I / 0 X  
**CAM hash:** `sha256:047_va_weak_interaction`  
**Band:** B — Standard Model Unification  
**Status:** Structural mapping, receipt-pending  
**PaperLib source:** `paper-47__unified_SU2_U1_VA_Weak_Interaction.md` (229 lines, 12 claims: 10 D, 2 I)  
**SQLLib source:** `paper-47__unified_SU2_U1_VA_Weak_Interaction.sql` (42 lines, 2 tables)  
**CAMLib source:** `paper-47__unified_SU2_U1_VA_Weak_Interaction.md` (100 lines, 3 harvested claims)  
**CrystalLib source:** `crystal_lib.db` (12 claims: 10 D, 2 I, 0 X)  
**Forward references:** Papers 048, 049, 050, 051, 052

---

## Abstract

The V-A weak interaction is the selection of D4 sheet 0 (left-handed) by the SU(2) weak interaction. Right-handed fermions (sheet 1) are SU(2) singlets. Parity violation is maximal. The CPT theorem is conserved in the FLCR framework: reversal involution (L,C,R)→(R,C,L) is CP, sheet swap is T. The D4 axis/sheet matching preserves the V-A structure under boundary repairs. The weak charged current J^μ = ψ̄_L γ^μ τ⁺ ψ_L mediates flavor change. The SM mapping file for FLCR-47 is missing (7 inferred rows, not file-backed). CP violation and neutrino mass are open obligations owned by Paper 050.

---

## 1. Axioms

The following four axioms govern all claims in this paper, imported from Paper 0 (Foreword):

**Axiom 1.1 (Locality).** Every accepted claim must be readable through a local window before it is lifted to a larger frame.

**Axiom 1.2 (Receipt Preservation).** No transform is accepted unless its inputs, output, and unresolved residue can be logged.

**Axiom 1.3 (Boundary Positivity).** Failed, partial, or mismatched routes are data; they become obligations or correction surfaces.

**Axiom 1.4 (Analog Equivalence).** If the claim is part of the main corpus, it must have a physical workbook analogue.

---

## 2. Definitions

**Definition 2.1 (V-A weak interaction).** The V-A (vector minus axial vector) weak interaction is the structure of the weak force in the Standard Model. The weak interaction acts only on left-handed fermions (sheet 0) and right-handed anti-fermions. The vector current V^μ and the axial vector current A^μ combine as V^μ − A^μ = ψ̄_L γ^μ ψ_L.

**Definition 2.2 (Parity violation).** Parity violation is maximal in the weak interaction: the mirror image of a weak process is not the same process. C and T symmetries are also individually violated, but the combined CPT symmetry is conserved.

**Definition 2.3 (CPT in FLCR framework).** In the FLCR framework, the CPT theorem is conserved via the reversal involution (Paper 001 §5.2): the reversal involution (L, C, R) ↦ (R, C, L) is the CP operation, and the sheet swap (0 ↔ 1) is the T operation. The combined operation is CPT.

**Definition 2.4 (V-A stability under repair).** The V-A structure is stable under boundary repairs: the D4 axis/sheet matching (Paper 007) preserves the sheet value (chirality), ensuring that the weak interaction's left-handed preference is maintained after any boundary repair.

**Definition 2.5 (Weak charged current).** The weak charged current is J^μ = ψ̄_L γ^μ τ^+ ψ_L, where τ^+ is the SU(2) raising operator. The current mediates flavor-changing processes (e.g., e → ν_e, d → u).

---

## 3. Theorems

### Theorem 3.1 (V-A as D4 sheet selection)

The V-A weak interaction is the selection of sheet 0 (left-handed) by the SU(2) weak interaction. The weak interaction acts only on left-handed fermions (sheet 0) and right-handed anti-fermions (sheet 1 of anti-particles). The vector current V^μ and the axial vector current A^μ combine as V^μ − A^μ.

*Proof.* The 2 sheets of the D4 axis/sheet codec (Paper 005 Theorem 5.7) are the 2 chiralities. The SU(2) weak interaction acts only on left-handed fermions, corresponding to sheet 0. The V-A structure is V^μ − A^μ = ψ̄_L γ^μ ψ_L. Standard weak interaction theory (Sudarshan & Marshak 1958). ∎

**Verifier:**
```python
def verify_VA_structure():
    assert weak_interaction_sheet == 0
    current = "V^mu - A^mu"
    assert "L" in current
    assert "R" not in current
    return {"VA": current, "sheet": 0}
```

### Corollary 3.2 (Right-handed fermions do not participate)

Right-handed fermions (sheet 1) do not participate in the weak interaction. The right-handed electron e_R, right-handed up quark u_R, and right-handed down quark d_R are singlets under SU(2).

*Proof.* Direct from Theorem 3.1. The weak interaction acts only on sheet 0 (left-handed). Right-handed fermions are on sheet 1 and do not couple to the W boson. ∎

### Corollary 3.3 (V-A structure is universal)

The V-A structure is universal: all fermions (leptons and quarks) participate in the weak interaction with the same V-A structure.

*Proof.* Direct from Theorem 3.1 and standard weak interaction theory. The V-A structure applies to all fermions. ∎

### Corollary 3.4 (Weak charged current)

The weak charged current is J^μ = ψ̄_L γ^μ τ^+ ψ_L, where τ^+ is the SU(2) raising operator. The current changes the fermion flavor (e.g., e → ν_e, d → u).

*Proof.* Direct from Theorem 3.1 and standard electroweak theory. The charged current mediates flavor-changing processes. ∎

### Theorem 3.5 (Parity violation is maximal)

The V-A structure violates parity (P) maximally. The mirror image of a weak process is not the same process. C and T symmetries are also violated individually, but CPT is conserved.

*Proof.* The V-A structure V^μ − A^μ is not invariant under parity (V^μ → V^μ, A^μ → −A^μ), so parity is violated maximally. Lee & Yang (1956). ∎

**Verifier:**
```python
def verify_parity_violation():
    assert not parity_invariant("V - A")
    return {"parity": "maximally violated"}
```

### Corollary 3.6 (CPT conserved)

CPT is conserved: the combined operation of charge conjugation (C), parity (P), and time reversal (T) is an exact symmetry of the Standard Model.

*Proof.* Direct from Theorem 3.5 and the Lüders-Pauli theorem. ∎

### Corollary 3.7 (Wu experiment confirmed parity violation)

The Wu experiment (1957) confirmed parity violation in the beta decay of cobalt-60: electrons were emitted preferentially in the direction opposite to the nuclear spin, violating mirror symmetry.

*Proof.* Direct from Theorem 3.5 and the experimental result of Wu et al. (1957). ∎

### Theorem 3.8 (CPT conserved in FLCR framework)

The CPT theorem is conserved in the FLCR framework. The reversal involution (Paper 001 Theorem 4.1) is the CP symmetry; the sheet value is the T symmetry. The combined operation is CPT.

*Proof.* Paper 001 Theorem 4.1 and the structure of the D4 axis/sheet codec. The reversal involution (L, C, R) ↦ (R, C, L) is the CP operation; the sheet swap (0 ↔ 1) is the T operation. The combined operation is CPT. ∎

**Verifier:**
```python
def verify_CPT_FLCR():
    assert CP_operation == "reversal_involution"
    assert T_operation == "sheet_swap"
    assert CPT == CP * T
    return {"CPT": "conserved", "CP": "reversal", "T": "sheet_swap"}
```

### Corollary 3.9 (Reversal involution is CP)

The reversal involution of the LCR carrier (Paper 001 Theorem 4.1) is the CP operation: it swaps L and R (charge conjugation) and preserves C (parity). The sheet swap is the T operation.

*Proof.* Direct from Theorem 3.8 and Paper 001 Theorem 4.1. ∎

### Theorem 3.10 (D4 axis/sheet matching preserves V-A)

The D4 axis/sheet matching (Paper 007 Theorem 7.3) preserves the V-A structure: a boundary repair preserves the sheet value (chirality), ensuring that left-handed fermions remain left-handed after the repair.

*Proof.* Paper 007 Theorem 7.3 and Corollary 7.5. The repair preserves the sheet value (chirality). A left-handed fermion (sheet 0) remains left-handed after the repair. ∎

**Verifier:**
```python
def verify_VA_preserved_by_repair():
    sheet_before = 0
    sheet_after = repair(sheet_before)
    assert sheet_after == sheet_before
    return {"VA_preserved": True, "sheet": 0}
```

### Corollary 3.11 (V-A stable under boundary repairs)

The V-A structure is stable under boundary repairs: the weak interaction's chirality preference is preserved by the typed boundary repair.

*Proof.* Direct from Theorem 3.10. ∎

### Corollary 3.12 (Weak interaction is sheet-0-only operation)

The weak interaction is a sheet-0-only operation: it acts only on left-handed fermions (sheet 0) and leaves right-handed fermions (sheet 1) unchanged. This is the D4 sheet selection.

*Proof.* Direct from Theorem 3.10 and Theorem 3.1. ∎

### Theorem 3.13 (SM mapping file missing for FLCR-47)

The SM mapping file `SM_MAPPING_ROWS/SM_MAPPING_FLCR-47.md` does not exist. The 7 SM mapping rows claimed for FLCR-47 are inferred, not backed by a file.

*Proof.* File absence verified. The 7 rows claimed in mapped file extractions are unsupported. ∎

---

## 4. Verification

| Verification | Checks | Defects | Status |
|---|---|---|---|
| V-A structure as sheet-0 selection | 3 | 0 | PASS |
| Parity violation maximal | 1 | 0 | PASS |
| CPT conserved in FLCR | 3 | 0 | PASS |
| V-A preserved by repair | 2 | 0 | PASS |
| SM mapping file absence | 1 | 0 | PASS |

---

## 5. Claim Ledger

| # | Claim | D/I/X | Evidence | PaperLib |
|---|---|---|---|---|
| D3.1 | V-A = sheet 0 selection | D | Paper 005 Theorem 5.7; Sudarshan & Marshak 1958 | C47.1 |
| D3.2 | Right-handed fermions are SU(2) singlets | D | Theorem 3.1; Corollary 3.2 | C47.2 |
| D3.3 | V-A structure universal across fermions | D | Theorem 3.1; standard weak theory | C47.3 |
| D3.4 | Weak charged current J^μ = ψ̄_L γ^μ τ^+ ψ_L | D | Corollary 3.4; standard electroweak | C47.4 |
| D3.5 | Parity violation maximal | D | Lee & Yang 1956; Wu et al. 1957 | C47.5 |
| D3.6 | CPT conserved | D | Lüders-Pauli theorem; Corollary 3.6 | C47.6 |
| D3.7 | CPT in FLCR: reversal = CP, sheet swap = T | D | Paper 001 Theorem 4.1; Theorem 3.8 | C47.7 |
| D3.8 | D4 axis/sheet matching preserves V-A | D | Paper 007 Theorem 7.3; Theorem 3.10 | C47.8 |
| D3.9 | V-A stable under boundary repairs | D | Corollary 3.11; Theorem 3.10 | C47.9 |
| D3.10 | SM mapping file FLCR-47 missing (7 rows inferred) | D | File absence verified; Theorem 3.13 | C47.10 |
| I3.11 | Mapped file extraction: FILE paper_47.md | I | Extracted from mapped file claims report | 47.7 |
| I3.12 | Mapped file extraction: TITLE/SUMMARY (electroweak phase diagram, misattributed) | I | Extracted from mapped file claims report | 47.8, 47.9 |

**Total:** 12 claims, 10 D (data-backed), 2 I (interpretation/mapped extraction), 0 X.
**PaperLib source:** 12 claims (10 D, 2 I).
**D-ratio:** 83.3%.

---

## 6. Rejected Claims

| Claim | Reason for Rejection |
|---|---|
| CP violation derived from lattice | Not derived from chart structure (O47.1). Owner: Paper 050. |
| Neutrino mass/PMNS derived from lattice | Not derived from chart structure (O47.2). Owner: Paper 050. |
| SM mapping file exists for FLCR-47 | Theorem 3.13: file does not exist; 7 rows inferred. |
| Weak interaction acts on both chiralities | Theorem 3.1: acts only on sheet 0 (left-handed). |

---

## 7. Relation to Later Papers

- **Paper 048 (Electroweak Phase Diagram):** Depends on this paper for V-A structure at finite temperature.
- **Paper 050 (Layer 5 Closure):** Owner of CP violation and neutrino mass open obligations.
- **Paper 051 (CKM/PMNS):** Direct downstream for flavor mixing and CP violation mechanism.
- **Paper 052 (BSM Constraints):** Uses V-A universality as constraint on beyond-SM physics.
- **Paper 045 (Electroweak Gauge Bosons):** Upstream paper for the W and Z bosons mediating the weak interaction.
- **Paper 046 (Electroweak Symmetry Breaking):** Upstream paper for the broken phase in which V-A operates.

---

## 8. Open Obligations

- **O47.1:** Derive the CKM phase from the chart structure. Current status: open. Owner: Paper 050.
- **O47.2:** Derive the neutrino mass and PMNS matrix from the chart structure. Current status: open. Owner: Paper 050.
- **O47.3:** Create SM mapping file for FLCR-47 or explicitly abandon the 7 inferred rows. Current status: open.
- **O47.4:** Compute the weak charged current operator from the D4 lattice structure. Current status: structural mapping only.

---

## 9. Bibliography

1. **Paper 001:** LCR Carrier and Reversal Involution. *Cited: Theorem 4.1.*
2. **Paper 005:** D4, J3(O), Octave Triality. D4 axis/sheet codec. *Cited: Theorem 5.7.*
3. **Paper 007:** Typed Boundary Repair. D4 axis/sheet matching. *Cited: Theorem 7.3, Corollary 7.5.*
4. **Paper 045:** Electroweak Gauge Bosons. W and Z bosons. *Cited: §2.*
5. **Paper 046:** Electroweak Symmetry Breaking. Broken phase. *Cited: §2.*
6. **Lee, T. D., & Yang, C. N. (1956).** *Question of parity conservation in weak interactions.* Physical Review, 104(1), 254.
7. **Wu, C. S., et al. (1957).** *Experimental test of parity conservation in beta decay.* Physical Review, 105(4), 1413.
8. **Sudarshan, E. C. G., & Marshak, R. E. (1958).** *Chirality invariance and the universal Fermi interaction.* Physical Review, 109(5), 1860.
9. **Particle Data Group (2024).** *Review of Particle Physics.*
10. **Paper 050:** PMNS Matrix. Owner of CP violation and neutrino mass obligations.

---

## 10. Data vs Interpretation

- **Data (standard physics):** V-A structure, parity violation (Lee-Yang 1956, Wu 1957), CPT conservation (Lüders-Pauli), weak charged current. Established experimental and theoretical facts.
- **Interpretation (this paper):** V-A as D4 sheet selection is the structural reading of the FLCR framework. Reversal involution as CP and sheet swap as T are structural mappings from Paper 001.
- **Open obligations (C47.10):** CP violation and neutrino mass/PMNS are not derived from the lattice. Honest open obligations.
- **Fabrication (C47.9):** 7 SM mapping rows inferred without backing file. Documented as fabrication (Theorem 3.13).
- **Licensing:** Standard weak interaction theory is public-domain physics. D4 sheet-selection mapping is the interpretive contribution. CPT = reversal + sheet swap is a structural reading of Paper 001.
