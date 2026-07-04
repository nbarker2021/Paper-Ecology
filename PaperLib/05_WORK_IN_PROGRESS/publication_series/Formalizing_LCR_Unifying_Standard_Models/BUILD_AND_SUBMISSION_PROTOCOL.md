# Build And Submission Protocol

## Canonical Source

Markdown is the editable source. `paper.tex` and `paper.pdf` are generated outputs.

## Current Toolchain Status

This environment did not expose `pdflatex` or `pandoc` when the blueprint was created. The generated PDFs are minimal placeholders so every triad has the contracted output files. Final arXiv-style PDFs require a later LaTeX build pass.

## Rewrite Passes

1. Assign sources and claim lanes in `SERIES_MAP.json` and `SOURCE_ROUTING_MATRIX.json`.
2. Assign the original-paper proof-ribbon role from
   `ORIGINAL_80_DIMENSIONAL_RIBBON_MAP.json`; do not infer dimensional proof
   role from the FLCR ordinal.
3. Fill all 120 triad Markdown files from assigned source material.
4. For every paper, write both required layers:
   - the sequential semantic explanation of why the next state happens;
   - the formalization of accepted mathematics, IRL formalism, receipts,
     validators, CAM/crystal evidence, and proof lanes that already support the
     state.
5. Rewrite `FLCR-01..FLCR-30` in LCR-native language, moving Standard Model language to deferred mapping slots.
6. Rewrite `FLCR-31..FLCR-40` as Standard Model translation and grand-unification papers.
7. Generate final LaTeX/PDF outputs.
8. Run publication readiness checks.

## Publication Readiness Checks

- JSON and YAML parse.
- Every formal claim has a lane, evidence source, and boundary.
- Every paper identifies its original ribbon slot role and its sequential
  semantic obligation.
- Every formal paper identifies the accepted external math/formalism being
  bound, or marks the absence as a required evidence intake.
- Every workbook includes at least one analog or correspondence table showing
  that the interpretation changes labels/access paths rather than the addressed
  state.
- `FLCR-01..FLCR-30` avoid Standard Model language except deferred mapping notes.
- `FLCR-31..FLCR-40` cite prior LCR-native papers before translation claims.
- Every paper has formal, companion, workbook, manifest, LaTeX, and PDF artifacts.
- Every receipt/path/citation exists or is explicitly marked external-required.
- Pilot build passes for `FLCR-01`, `FLCR-08`, `FLCR-28`, and `FLCR-40`.
