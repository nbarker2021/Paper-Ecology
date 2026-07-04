# FLCR NIST Normal-Form Gate Addendum

Generated context: after `FLCR_NIST_AND_REVIEW_SUITE_REPORT.md`.

The existing NIST-style report records structural coverage: required paper
sections exist, receipts are parseable where attached, open obligations are
disclosed, and suite-aware continuations are visible. That PASS is not a
substantive closure of non-receipt-bound obligations.

## Added Gate

The NIST/NSIT validator layer now requires:

`paper.normal_form_conversion`

This standard applies to every row in `OBLIGATION_ROWS.json` whose status is
not `receipt_bound`.

Required fields:

1. Generalized Kimi normal form.
2. Paper-specific Kimi normal form.
3. Advanced lane form.
4. Explicit FLCR conversion rule.
5. Validator-readable residue, falsifier, citation target, dataset/comparator,
   replay receipt gate, synthesis dependency, or ledger action gate.

## Current Readout

- Total obligation rows: 209
- Receipt-bound rows excluded from this gate: 9
- Rows entering normal-form ingress: 200
- Papers represented: 13

Machine-readable source:

- `NORMAL_FORM_INGRESS_MATRIX.json`
- `NORMAL_FORM_INGRESS_MATRIX.md`
- `NORMAL_FORM_INGRESS_PROTOCOL.md`

## Promotion Rule

A PASS on `paper.normal_form_conversion` only routes the row into its lawful
next evidence queue. It does not grant ASSEMBLE and does not replace receipts,
citations, CAM/crystal replay, calibration data, synthesis dependency checks, or
falsifier closure.

