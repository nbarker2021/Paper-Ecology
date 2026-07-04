# CMPLX-Standards Normal-Form Gate Addendum

Generated context: after the structural NIST-style paper review and after the
normal-form ingress pass.

The older NIST/NSIT labels are historical provenance for prior reports. The
forward tool name is `CMPLX-Standards`.

## Added Gate

CMPLX-Standards now grades:

`paper.normal_form_conversion`

This model applies to every row in `OBLIGATION_ROWS.json` whose status is not
`receipt_bound`.

Required fields:

1. Generalized Kimi normal form.
2. Paper-specific Kimi normal form.
3. Advanced lane form.
4. Explicit FLCR conversion rule.
5. CMPLX-Standards gate with residue, falsifier, citation target,
   dataset/comparator, replay receipt gate, synthesis dependency, or ledger
   action gate.

## Current Readout

- Total obligation rows: 209
- Receipt-bound rows excluded from this gate: 9
- Rows entering normal-form ingress: 200
- Records graded by CMPLX-Standards: 200
- Average fit score: 99.881735
- Average distance to perfect: 0.001183
- Perfect-fit rows: 175
- Model-inclusive rows: 25

## Promotion Rule

A high CMPLX-Standards score only measures fit to the model contract. It does
not grant ASSEMBLE and does not replace receipts, citations, CAM/crystal replay,
calibration data, synthesis dependency checks, or falsifier closure.

