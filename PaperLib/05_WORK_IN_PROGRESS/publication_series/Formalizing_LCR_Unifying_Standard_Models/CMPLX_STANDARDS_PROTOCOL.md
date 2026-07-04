# CMPLX-Standards Protocol

Status: active replacement name and tool surface for the old NIST/NSIT paper
validation idea.

CMPLX-Standards is the universal measurement layer used to grade data against a
declared CMPLX model. It reports how close each record is to perfect inclusion
in that model, what fields keep the record from being perfect, and whether the
record is inclusive, partial, weak, or non-inclusive.

## Role

CMPLX-Standards does not prove claims and does not grant ASSEMBLE. It measures
model fit so downstream validators can route the row honestly.

The basic flow is:

```text
data payload + model contract
-> CMPLX-Standards grading report
-> evidence queue routing
-> receipt/citation/CAM/calibration/synthesis/falsifier validator
-> promotion decision
```

## First Active Model

Model:

- `CMPLX-Standards/models/normal_form_ingress_model.json`

Input:

- `NORMAL_FORM_INGRESS_MATRIX.json`

Output:

- `CMPLX_STANDARDS_NORMAL_FORM_INGRESS_REPORT.json`
- `CMPLX_STANDARDS_NORMAL_FORM_INGRESS_REPORT.md`

Current readout:

- Records graded: 200
- Average fit score: 99.881735
- Average distance to perfect: 0.001183
- Perfect-fit rows: 175
- Model-inclusive rows: 25

The 25 non-perfect rows are still model-inclusive. Their residues are mostly
empty dependency lists on standard-import or synthesis-facing rows. That is a
useful measurement: the rows are structurally ready for normal-form review, but
some need explicit dependency attachment before they are perfect.

## Forward Rule

New standards should be written as CMPLX-Standards model contracts first. The
older NIST/NSIT names remain provenance labels for prior reports only.

