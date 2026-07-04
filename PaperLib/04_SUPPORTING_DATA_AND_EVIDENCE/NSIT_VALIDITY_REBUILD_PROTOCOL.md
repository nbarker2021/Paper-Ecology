# NSIT Validity Rebuild Protocol

**Status:** historical bootstrap protocol; forward tool name is `CMPLX-Standards`.  
**Purpose:** gather every paper-like artifact and attached evidence, discard old
`open`/`closed` labels as verdict authority, and rebuild validity through a
standards-and-conformance process.

---

## Core Decision

Legacy state labels are no longer validity labels. Words such as `open`,
`closed`, `proved`, `pending`, `complete`, `bounded`, and `external` may remain
inside source text as historical data, but they are not the final state of the
claim. They become inputs to a standards review.

The validity process is:

```text
artifact inventory
-> evidence attachment
-> claim extraction
-> standards conformance
-> reasoned reapplication
-> Safe-to-Claim score
-> paper burden update
```

## Standards Suites To Use

| Suite | Location | Role |
|-------|----------|------|
| CQE Standards Board | `D:/CQE_CMPLX/CQE-CMPLX-1T-Production/src/cqe_standards/` | Stable Standard / Validator / Verdict / ConformanceReport contract. |
| CQE built-in standards | `src/cqe_standards/standards/*.json` | Existing standards for claim envelopes, receipts, LCR lane grants, and geometry. |
| Legacy paper validator adapter | `src/cqe_standards/adapters/paper_validator.py` | Bridges existing `verify_*.py` scripts into normalized verdicts. |
| Kimi / MCP validation suite | `D:/repo_harvest/CMPLXMCP/validation/` | Suite orchestration pattern: component validators, validation result schema, CLI/report workflow. |
| Claude Safe-to-Claim scale | `D:/repo_harvest/_CAM/governance_scale.py` and Claude memory | 1-100 validity gradient; `80` quarantine lift, `90` attached data, `100` paper-ready. |
| NSIT reasoned closure pass | `D:/Paper Reworks/NSIT_REASONED_CLOSURE_PASS.md` | Cross-paper and standard-field reasoning pass before anything is treated as residual. |

No exact `NSIT` string was found in the first scan. The local system matching
the requested role is the CQE Standards Board plus Kimi's suite-orchestrated
validation pattern. `NSIT` was used as the bootstrap name for that process.
The forward implementation name is now `CMPLX-Standards`.

## Artifact Classes

Every discovered item is classified without trusting its prior state label.

| Class | Meaning |
|-------|---------|
| `main_line_paper` | Numbered paper 00-32 in `D:/Paper Reworks`. |
| `formal_paper` | Any formal paper outside the main line. |
| `supplement` | Supplement, appendix, source integration, queue, or bridge paper. |
| `receipt_or_data` | JSON, JSONL, DB, CSV, receipt, verifier output, or dataset attached to a paper/claim. |
| `validator` | `verify_*.py`, standards validator, or validation suite test. |
| `memory_or_cam` | Claude, CAM, crystal, or MannyAI memory that supplies evidence or governance. |

## Validity Fields

Each claim-level record must eventually carry:

```text
record_id
artifact_id
claim_text
claim_class
scope_boundary
falsifier
evidence_ED_ID_DD
attached_data
validators
conformance_verdicts
safe_to_claim_score
candidate_closing_form
paper00_burden_update
```

## New Verdict Semantics

The CQE Standards Board `VerdictStatus` values are retained as execution
statuses, but they are not used as old binary paper states.

| Status | New reading |
|--------|-------------|
| `PASS` | This standard passed for this target. It does not alone prove the whole paper. |
| `FAIL` | This standard failed; record the failure and route remediation. |
| `OPEN` | Standards coverage missing or validator absent; not a claim verdict. |
| `EXTERNAL_REQUIRED` | External data, theorem, lab result, or source access is required. |
| `NOT_APPLICABLE` | Standard does not apply to this artifact. |

## Required Standards For Paper Claims

Initial standards to apply:

1. `claim.cpt_envelope`: every claim/theorem/lemma/hypothesis needs falsifier,
   boundary, coordinate contract, evidence split, validators, and imports.
2. `receipt.content_addressed`: every attached receipt must be hash checked.
3. `lcr.lane_grant`: any tool, runtime, or adapter claiming L/C/R behavior must
   satisfy lane-policy consistency.
4. `claim.safe_to_claim_score`: to be added from `governance_scale.py`; returns
   score band and gate details in the verdict details.
5. `paper.artifact_inventory`: to be added for this process; confirms the paper
   has its supplements, validators, receipts, data, and source variants attached.
6. `claim.reasoned_reapplication`: to be added for this process; confirms that
   cross-paper tools, CAM/crystal memory, and standard math/physics/CS formalism
   were attempted before a claim is scored as residual.
7. `paper.normal_form_conversion`: CMPLX-Standards model gate; confirms that
   every non-receipt-bound obligation has a generalized Kimi normal form,
   paper-specific Kimi normal form, advanced lane form, explicit FLCR conversion
   rule, and validator-readable falsifier/residue/gate before it can enter a
   downstream evidence queue.

## Immediate Implementation Steps

1. Build a complete artifact inventory across:
   - `D:/Paper Reworks`
   - `D:/CQE_CMPLX/CQE-CMPLX-1T-Production`
   - `D:/CQE_CMPLX/CMPLX-R30-main/PROOF`
   - `D:/CQE_CMPLX/historical_pastworks`
   - `D:/MannyAI`
   - `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory`
   - `D:/repo_harvest/_CAM`
2. Link likely attachments by paper number, title tokens, verifier names, receipt
   paths, and content hashes.
3. Build the validation tool closure matrix: all `verify_*`, standards
   validators, forge `verify()` methods, reapplication receipts, and Kimi/MCP
   suite tests must be mapped to the claims they can close individually or in
   batches.
4. Create claim-level records from paper sections, but leave old labels as
   `legacy_label_text`, not verdicts.
5. Run reasoned reapplication: local tools, cross-paper tools, CAM/crystal
   memory, and ordinary standard formalism.
6. Run available standards/legacy validators and emit conformance reports.
7. Run the normal-form ingress pass for every row that is not receipt-bound.
8. Rescore with Safe-to-Claim after attached data and normal-form gates are
   confirmed.

## First Output Files

| File | Role |
|------|------|
| `NSIT_PAPER_EVIDENCE_INVENTORY.json` | Generated artifact inventory. |
| `NSIT_PAPER_EVIDENCE_INVENTORY.md` | Human-readable summary. |
| `NSIT_TOOL_CLOSURE_MATRIX.md` | Tool reapplication matrix: individual and batch closures. |
| `NSIT_TOOL_CLOSURE_MATRIX.json` | Machine-readable tool closure matrix. |
| `NSIT_REASONED_CLOSURE_PASS.md` | Cross-domain reasoning pass and reclassification pressure. |
| `NSIT_REASONED_CLOSURE_PASS.json` | Machine-readable reasoning-pass queue. |
| `NSIT_VALIDITY_REBUILD_PROTOCOL.md` | This protocol. |
| `NORMAL_FORM_INGRESS_PROTOCOL.md` | Required generalized, paper-specific, advanced, and FLCR conversion forms for non-receipt-bound obligations. |
| `NORMAL_FORM_INGRESS_MATRIX.md` | Human-readable normal-form ingress readout. |
| `NORMAL_FORM_INGRESS_MATRIX.json` | Machine-readable normal-form ingress matrix for NIST/NSIT validators. |
