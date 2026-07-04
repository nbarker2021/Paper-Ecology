# Paper 02: Correction Surface

**Domain:** Correction Surface / Error Recovery  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 2.1: Correction Decomposition

- **Claim Text:** For every binary LCR state, R30(L, C, R) = R90(L, R) xor corr(L, C, R). Moreover, corr is nonzero exactly on {(0,1,0), (1,1,0)}.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-02__unified_correction_surface_and_rule30_decomposition.py`
- **SQLLib Source:** `D:/SQLLib/paper-02__unified_correction_surface_and_rule30_decomposition.sql`
- **Status:** verified
- **Verifier:** `verify_correction_surface()`

### Claim 2.2: Correction-Surface Monitor

- **Claim Text:** The correction surface admits a finite monitor layer: the eight LCR triads partition as 2/2/4, the Rule30 equals Rule90 plus correction identity remains exact, and deviation from the expected correction ratio is logged by exact two-tailed binomial receipts.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-02__unified_correction_surface_and_rule30_decomposition.py`
- **SQLLib Source:** `D:/SQLLib/paper-02__unified_correction_surface_and_rule30_decomposition.sql`
- **Status:** verified
- **Verifier:** `verify_correction_surface_monitor()`

---

## Cross-References

- [Paper 00: Established Grounding / Axiom Contract](paper-00__unified_transport_contract_and_foreword.md)
- [Paper 01: LCR Chain Carrier](paper-01__unified_lcr_kernel_and_chart.md)
- [Paper 03: D4/J3 Triality Surface](paper-03__unified_d4_j3_triality_and_correction_surface.md)
- [Paper 04: Boundary Repair](paper-04__unified_boundary_repair.md)

---

## Recovery Notes

3LSR Recovered: Rule 30 = Rule 90 XOR correction identity, C AND NOT R correction firing set, D4 axis/sheet projection for firing states, 2/2/4 triad partition monitor.

---

## Disposition

This paper is classified as **`canon`**.
It is part of the core canonical paper series.
