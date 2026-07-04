# Normal Form Ingress Matrix

Generated: `2026-07-01T02:46:01+00:00`

Scope: every row in `OBLIGATION_ROWS.json` that is not `receipt_bound`.

This pass does not promote rows to ASSEMBLE. It creates the missing
validator surface for rows that need normal-form conversion before any
receipt, citation, CAM, calibration, synthesis, or falsifier closure.

## Summary

- Total obligation rows: `1105`
- Receipt-bound rows excluded: `1005`
- Normal-form ingress rows: `100`
- Papers represented: `7`

### Rows By Claim Family

| Claim family | Rows |
|---|---:|
| `cross_paper_synthesis` | 5 |
| `external_calibration` | 5 |
| `ledger_action` | 5 |
| `normal_form_derivation` | 11 |
| `receipt_replay` | 19 |
| `residue_falsifier` | 42 |
| `standard_import` | 13 |

### Rows By FLCR

| FLCR | Rows | Dominant family |
|---|---:|---|
| `FLCR-01` | 16 | `residue_falsifier` |
| `FLCR-04` | 12 | `receipt_replay` |
| `FLCR-10` | 12 | `residue_falsifier` |
| `FLCR-20` | 15 | `residue_falsifier` |
| `FLCR-29` | 13 | `residue_falsifier` |
| `FLCR-30` | 12 | `residue_falsifier` |
| `FLCR-39` | 20 | `residue_falsifier` |

## Validator Contract

The CMPLX-Standards layer needs a new standard named
`paper.normal_form_conversion`. A row passes that standard only when it has:

1. A generalized Kimi normal form.
2. A paper-specific Kimi normal form.
3. An advanced form appropriate to its evidence family.
4. An explicit FLCR conversion rule.
5. A falsifier, residue, citation target, dataset/comparator, or replay gate.

A pass through this standard moves a row into the next evidence queue. It
does not directly grant ASSEMBLE.

## First Rows

| Obligation | Family | Gate |
|---|---|---|
| `FLCR-10-OBL-001` | `standard_import` | citation target, object mapping, and conservative-extension boundary |
| `FLCR-10-OBL-003` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-10-OBL-004` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |
| `FLCR-10-OBL-005` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-10-OBL-006` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-10-OBL-007` | `standard_import` | citation target, object mapping, and conservative-extension boundary |
| `FLCR-10-OBL-009` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-10-OBL-011` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-10-OBL-012` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-10-OBL-013` | `standard_import` | citation target, object mapping, and conservative-extension boundary |
| `FLCR-10-OBL-014` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |
| `FLCR-10-OBL-016` | `standard_import` | citation target, object mapping, and conservative-extension boundary |
| `FLCR-20-OBL-001` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |
| `FLCR-20-OBL-002` | `normal_form_derivation` | standard normal form, paper normal form, conversion rule, and falsifier |
| `FLCR-20-OBL-003` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-004` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |
| `FLCR-20-OBL-005` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |
| `FLCR-20-OBL-006` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-007` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-008` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-009` | `ledger_action` | ledger row type, import/export rule, affected obligation ids, and validator receipt |
| `FLCR-20-OBL-010` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-011` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-012` | `standard_import` | citation target, object mapping, and conservative-extension boundary |
| `FLCR-20-OBL-013` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-20-OBL-014` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |
| `FLCR-20-OBL-015` | `ledger_action` | ledger row type, import/export rule, affected obligation ids, and validator receipt |
| `FLCR-29-OBL-001` | `cross_paper_synthesis` | dependency papers, dependency lanes, residual obligations, and falsifier |
| `FLCR-29-OBL-002` | `normal_form_derivation` | standard normal form, paper normal form, conversion rule, and falsifier |
| `FLCR-29-OBL-003` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-29-OBL-005` | `external_calibration` | dataset, units, uncertainty/comparator, and pass/fail criteria |
| `FLCR-29-OBL-006` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-29-OBL-007` | `normal_form_derivation` | standard normal form, paper normal form, conversion rule, and falsifier |
| `FLCR-29-OBL-008` | `cross_paper_synthesis` | dependency papers, dependency lanes, residual obligations, and falsifier |
| `FLCR-29-OBL-009` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-29-OBL-010` | `cross_paper_synthesis` | dependency papers, dependency lanes, residual obligations, and falsifier |
| `FLCR-29-OBL-011` | `residue_falsifier` | explicit failure condition, next binding action, and owner surface |
| `FLCR-29-OBL-012` | `standard_import` | citation target, object mapping, and conservative-extension boundary |
| `FLCR-29-OBL-013` | `ledger_action` | ledger row type, import/export rule, affected obligation ids, and validator receipt |
| `FLCR-29-OBL-015` | `receipt_replay` | receipt path, verifier name, replay scope, and content-address check |

Full machine-readable rows are in `NORMAL_FORM_INGRESS_MATRIX.json`.
