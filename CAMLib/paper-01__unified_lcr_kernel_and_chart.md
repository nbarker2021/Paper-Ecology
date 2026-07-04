# Paper 01: LCR Chain Carrier

**Domain:** Carrier Theory  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 1.1: Minimal LCR Carrier

- **Claim Text:** Any ordered local carrier that preserves a distinguished center and records two addressable boundary directions requires at least three slots. The carrier (L, C, R) realizes this lower bound, and is therefore minimal.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-01__unified_lcr_kernel_and_chart.py`
- **SQLLib Source:** `D:/SQLLib/paper-01__unified_lcr_kernel_and_chart.sql`
- **Status:** verified
- **Verifier:** `verify_lcr_carrier()`

### Claim 1.2: Shell-2 Doublet Binding

- **Claim Text:** In the binary LCR chart, the shell = 2 stratum is exactly {(1,1,0), (1,0,1), (0,1,1)}. Left-right reversal exchanges (1,1,0) and (0,1,1) while fixing (1,0,1). Therefore the shell-2 stratum carries the finite single-tape doublet interface used by later trace-2 and closure papers.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-01__unified_lcr_kernel_and_chart.py`
- **SQLLib Source:** `D:/SQLLib/paper-01__unified_lcr_kernel_and_chart.sql`
- **Status:** verified
- **Verifier:** `verify_bijective_shell2_doublet()`

### Claim 1.3: O8 Spinor Double-Cover Closure

- **Claim Text:** The frame-inversion operator F carried by the oloid kinematic layer realizes the local SU(2) to SO(3) double-cover semantics required by O8: F² gives the spinor sign at 2π and F⁴ returns to the origin at 4π.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-01__unified_lcr_kernel_and_chart.py`
- **SQLLib Source:** `D:/SQLLib/paper-01__unified_lcr_kernel_and_chart.sql`
- **Status:** verified
- **Verifier:** `verify_o8_spinor_double_cover_closed()`

---

## Cross-References

- [Paper 00: Established Grounding / Axiom Contract](paper-00__unified_transport_contract_and_foreword.md)
- [Paper 02: Correction Surface](paper-02__unified_correction_surface_and_rule30_decomposition.md)
- [Paper 03: D4/J3 Triality Surface](paper-03__unified_d4_j3_triality_and_correction_surface.md)
- [Paper 05: Oloid Path Carrier](paper-05__unified_oloid_path_carrier.md)

---

## Recovery Notes

3LSR Recovered: LCR minimal three-address carrier, shell-2 doublet orbit structure, O8 spinor double-cover via frame inversion, boundary address vs value correction.

---

## Disposition

This paper is classified as **`canon`**.
It is part of the core canonical paper series.
