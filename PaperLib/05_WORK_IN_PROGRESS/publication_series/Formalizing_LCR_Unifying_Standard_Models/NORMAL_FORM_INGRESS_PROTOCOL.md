# Normal Form Ingress Protocol

Status: active gate for non-receipt-bound obligations.

Purpose: make every non-receipt-bound paper obligation validator-readable before
it can become an FLCR claim. This is the missing layer between open prose and
CMPLX-Standards validation.

## Required Forms

Each obligation must carry all four forms below.

1. Generalized Kimi normal form: the standard tuple used across the whole
   series: source identity, typed object, operation or relation, evidence lane,
   dependency set, scope boundary, falsifier or residue, and validator gate.
2. Paper-specific Kimi normal form: the same claim expressed in the local paper's
   object language, section, dependencies, and import boundary.
3. Advanced normal form: the lane-specific refinement. Examples include
   citation-conservative-extension form, memory-route replay form, unit-bearing
   comparator form, dependency-braided synthesis form, and negative-space
   falsifier form.
4. FLCR conversion rule: the explicit conversion into FLCR algebra:
   L=source/provenance/dependencies, C=typed claim operator, and
   R=residue/falsifier/validator gate.

## CMPLX-Standards Standard To Add

`paper.normal_form_conversion`

PASS means the conversion is explicit enough that a validator can reject it
without interpreting free prose. PASS does not grant ASSEMBLE; it routes the row
to the next evidence queue.

FAIL means the row remains `staged_open`.

OPEN means the row has not yet been supplied with one or more of the required
forms.

## Promotion Discipline

Normal-form review is not a substitute for receipts, citations, calibration
data, or falsifiers. It is the legal ingress that decides which of those
evidence paths is actually required and makes the conversion auditable.
