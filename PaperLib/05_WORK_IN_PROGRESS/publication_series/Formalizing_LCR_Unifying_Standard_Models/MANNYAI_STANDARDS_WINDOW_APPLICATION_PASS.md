# MannyAI Standards And Window Application Pass

**Date:** 2026-06-28  
**Scope:** Apply the newly reviewed MannyAI/Kimi standards, glue, window, and instruction artifacts to the FLCR publication suite.  
**Status:** active routing upgrade; body rewrites remain staged by paper.

## Authority Rule

For publication work, the standards suite is the pass/fail authority and the older `verify_*.py` node summaries are evidence artifacts. This resolves the apparent conflict between:

- `mannyai/standards/corpus_conformance_report.json`: canonical 32-paper suite, 192/192 PASS, 0 FAIL, 0 OPEN.
- `mannyai/node/verify_summary.json`: older script-level evidence summary, 25 PASS and 7 FAIL.

The older failures are not discarded. They are routed as paper-local evidence, historical verifier gaps, or implementation obligations when their failing script names identify missing integration work. They do not override the standards-suite conformance result.

## Corpus Results To Bind

| Artifact | Result | Publication use |
|---|---:|---|
| `corpus_conformance_report.json` | 32 canonical papers, 192/192 PASS | FLCR-39 standards baseline; cited by FLCR-40 before synthesis claims |
| `suite_resolution_report.json` | 99 papers/items, 782 total items, 776 resolved, 6 unresolved | Cross-paper continuation graph; unresolved rows become explicit obligations |
| `glue_report.json` | 95/95 obligations have continuation candidates | Obligation springboard and dependency routing evidence |
| `window_summary.json` | 2/4/8/16/32 window hierarchy over papers 00-31 | FLCR-30 supervisor cursor and window scheduler evidence |
| MannyAI instruction docs | CAM-first, open-obligation, code-reuse, staleness doctrines | FLCR-28 runtime doctrine and FLCR-39 evidence policy |

## Six Unresolved Suite Rows

These rows are not failures of the standards suite. They are the next exact paper obligations.

| Source paper node | Item | Destination rule |
|---|---|---|
| `CQE-paper-formal-07` | `verify_grand_ribbon_meta_framer.py` | Route to FLCR-30 and FLCR-40 as supervisor-cursor/grand-ribbon verifier binding. |
| `CQE-paper-formal-PH1` | `kappa = ln(phi)/16 approx 0.0301` | Route to FLCR-31/33/39 as citation/normalization requirement before physics translation. |
| `CQE-paper-formal-PH2` | `Observer_5 = 3 + 2` | Route to FLCR-38/40 as observer decomposition needing explicit normal-form dependency. |
| `CQE-paper-formal-S11` | `Randomness and Cryptographic Vulnerabilities` | Route to FLCR-13/39 as comparator and falsifier surface. |
| `CQE-paper-formal-S29` | `The 8 Estimators` | Route to FLCR-28/39 as CAM/crystal estimator manifest requirement. |
| `CQE-paper-formal-U1` | `verify_quark_face_transport_literalized.py` | Route to FLCR-14/31/32/40 as quark-face transport verifier binding. |

## Paper Ownership

| FLCR paper | New responsibility from this pass |
|---|---|
| FLCR-28 | Owns MannyAI runtime intake, CAM-first doctrine, crystal/projector adapter discipline, and the unresolved 8-estimator manifest lane. |
| FLCR-30 | Owns 2/4/8/16/32 window scheduling, universal normal-form intake, and the grand-ribbon verifier binding. |
| FLCR-39 | Owns validation authority, standards/glue/window comparator rules, and the distinction between standards verdicts and legacy script evidence. |
| FLCR-40 | Consumes the standards and window results only through dependency-explicit synthesis lanes; unresolved rows remain blockers or named dependencies. |

## Upgrade Rule For Next Body Pass

Every formal paper should now receive a short "Standards and Window Binding" subsection. The subsection must state:

1. which standards or window artifact is relevant;
2. whether the relevant row is a conformance result, glue route, window route, legacy verifier artifact, or unresolved obligation;
3. which claim lane can consume it;
4. what would falsify or block promotion.

This keeps the suite from becoming a dump of text clips. Each imported fact has a formal role, a lane, and a downstream rule.
