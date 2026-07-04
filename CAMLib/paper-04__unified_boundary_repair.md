# Paper 04: Boundary Repair

**Domain:** Boundary Repair / Constraint Routing  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 4.1: Typed Boundary Repair

- **Claim Text:** A failed join is repairable in the CQECMPLX paper kernel if and only if it can be converted into a typed constraint that preserves the original state, the Paper 03 coordinate, the reason for failure, and at least one next legal route.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-04__unified_boundary_repair.py`
- **SQLLib Source:** `D:/SQLLib/paper-04__unified_boundary_repair.sql`
- **Status:** verified
- **Verifier:** `verify_boundary_repair()`

---

## Cross-References

- [Paper 02: Correction Surface](paper-02__unified_correction_surface_and_rule30_decomposition.md)
- [Paper 03: D4/J3 Triality Surface](paper-03__unified_d4_j3_triality_and_correction_surface.md)
- [Paper 05: Oloid Path Carrier](paper-05__unified_oloid_path_carrier.md)

---

## Recovery Notes

3LSR Recovered: Typed boundary constraint schema (state, axis_sheet, reason, status, next_legal_routes, source_paper, target_paper), idempotent repair operation, untyped failure rejection.

---

## Disposition

This paper is classified as **`canon`**.
It is part of the core canonical paper series.
