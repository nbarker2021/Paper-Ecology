# Obligation Derivation Queue

Generated from **DEEP_REVIEW_PASS1** + post-apply `PAPER_CONTENT_NEEDS_REPORT.json` (2026-06-29).  
Refreshed **Phase 6 Wave 1 Lane B** (2026-06-30) after EXT80 derivation pass and top-50 normal-form crosswalk.  
**Rule:** Derive `falsifier_or_open_obligation` PEEP rows from `formal.md` prose only — **no fake PEEP**, no keyword-only assembly.

**HOLD (PEEP promotion blocked until obligation rows materialized):** FLCR-10, FLCR-20, FLCR-29, FLCR-30, FLCR-39 — **209 total rows in `OBLIGATION_ROWS.json` (Phase 13+14); 9 receipt-bound; holds remain until all receipt lanes bound per row**

| FLCR | Open obligations (formal.md) | ASSEMBLE | DISCOVERY | Honest next step |
|------|---------------------------:|---------:|----------:|------------------|
| **FLCR-01** | 16 | 16 | 5 | **Phase 14 derived** — 16 staged rows; bind receipt lanes per row before ASSEMBLE |
| **FLCR-04** | 14 | 10 | 0 | **Phase 14 derived** — map binary-invariance falsifier rows to PEEP-002/010; receipt lanes pending |
| **FLCR-05** | 13 | 2 | 0 | **Phase 14 derived** — oloid-path obligations staged; geometry comparator **BLOCKED** |
| **FLCR-10** | 15 | **0** | 44 | **HOLD** — 4/16 rows receipt-bound (T10 master); Protocol 10.3 + Moonshine lanes open |
| **FLCR-14** | 14 | 6 | 0 | **Phase 14 derived** — PEEP-027 boundary comparator scope only; CKM data-bound |
| **FLCR-15** | 14 | 2 | 0 | **Phase 14 derived** — Higgs mass calibration **not closed**; PEEP-001 deferred |
| **FLCR-18** | 25 | 2 | 0 | **Phase 14 derived** — Moonshine/VOA/observer-face + FLCR-17 dependency rows staged |
| **FLCR-19** | 18 | 0 | 5 | **Phase 14 derived** — CITE-FLCR-19 wired; ledger obligation rows staged, no ASSEMBLE |
| **FLCR-20** | 14 | **0** | 234 | **HOLD** — EXT80-20 DERIVATION_VALIDATED; 15 obligation rows in normal-form batch; forge validator receipts needed (Lane A) |
| **FLCR-25** | 14 | 0 | 130 | **Phase 14 derived** — slot 25 CKM **DEFER_ASSEMBLE**; PEEP-017 transport only |
| **FLCR-29** | 22 | **0** | 40 | **HOLD** — 2/15 rows receipt-bound (prime-chart); upstream graph + Monster ceiling open |
| **FLCR-30** | 21 | **0** | 112 | **HOLD** — 3/15 rows receipt-bound (grand-ribbon); Protocol 30.3 Kimi gate open |
| **FLCR-39** | 23 | **0** | 192 | **HOLD** — EXT80-39 DERIVATION_VALIDATED; 20 obligation rows in normal-form batch; comparator receipts needed (Lane A) |

## Phase 6 Wave 1 Lane B — EXT80 Derivation

| Slot | EXT80 ID | Derivation Status | Full-text | ASSEMBLE |
|------|----------|-------------------|-----------|----------|
| FLCR-20 | EXT80-20 | DERIVATION_VALIDATED | pending | BLOCKED |
| FLCR-24 | EXT80-24 | DERIVATION_VALIDATED | pending | BLOCKED |
| FLCR-39 | EXT80-39 | DERIVATION_VALIDATED | pending | BLOCKED |

Receipt: `EXTERNAL_PAPER_INGRESS_80_DERIVATION_PASS.json` — 80/80 ingress rows DERIVATION_VALIDATED; no ASSEMBLE promotion from ingress alone.

## Normal-Form Crosswalk (Top 50)

- Source: `NORMAL_FORM_INGRESS_MATRIX.md` (712 rows total)
- Batch size: 50 (priority: FLCR-20, FLCR-24, FLCR-39 obligations first)
- Validated: 50/50 (`normal_form_validated`)
- Standard: `paper.normal_form_conversion` — routes to next evidence queue, not ASSEMBLE

## Per-paper obligation samples (from `formal.md`)

### FLCR-10 (HOLD)
- Status: first-pass rich rewrite; requires final citation and build pass
- Convert proof sketch → numbered definitions/lemmas with explicit dependencies
- Replace placeholder source classes with receipt hashes or dataset identifiers
- **Next:** Run `extract_obligations` pass on `FLCR-10/formal.md` §4 Formal Claims → `CLAIM_LANE_SCHEMA.json` rows

### FLCR-20 (HOLD)
- Layer-2 synthesis ledger import rule obligations
- Unknown/forbidden reachability must remain explicit
- **Next:** Lane A receipt binding for forge validator receipts; EXT80-20 candidate awaits full-text anchor

### FLCR-29 (HOLD)
- Monster universal energy bound hypotheses — open comparator obligations
- **Next:** Derive one obligation row per formal claim in `FLCR-29/formal.md`; bind FLCR-09 forge motif after obligation queue clears

### FLCR-30 (HOLD)
- Grand ribbon meta-framer — keyword DISCOVERY dominates typed claims
- **Next:** Replace slot-30 keyword hits with content-derived lanes from §4 table

### FLCR-39 (HOLD)
- Grand synthesis residue declared in prose without falsifier PEEP rows
- **Next:** Lane A comparator receipt binding; EXT80-39 candidate awaits full-text anchor

## Queue summary

- **Papers queued:** 13 (all high-severity from deep review)
- **Obligation rows derived:** 13/13 — **209 total** in `OBLIGATION_ROWS.json` (Phase 13+14)
- **Receipt-bound rows:** 9 (FLCR-10: 4, FLCR-29: 2, FLCR-30: 3)
- **Normal-form batch validated:** 50/50 (Phase 6 Lane B)
- **EXT80 derivation validated:** 80/80 ingress; 3/3 priority blocked slots
- **PEEP promotion holds:** 5 (FLCR-10, 20, 29, 30, 39) — ASSEMBLE still 0 per held paper
- **Slot gates:** 24 DEFER_ASSEMBLE (Protocol 24.3); 25 DEFER_ASSEMBLE (CKM comparator)
- **Citation wiring complete:** FLCR-19 → FLCR-01/09/11; FLCR-24 → FLCR-01/11/18; FLCR-26 → FLCR-06
- **Connection wiring complete:** 10/10 (see `CONNECTION_WIRING_QUEUE.md`)
- **ASSEMBLE unchanged:** 37/40 (no fake PEEP added; no ingress-only promotion)

## Normal-form ingress added

The non-receipt-bound portion of this queue now has a validator-facing ingress
surface:

- `NORMAL_FORM_INGRESS_PROTOCOL.md`
- `NORMAL_FORM_INGRESS_MATRIX.md`
- `NORMAL_FORM_INGRESS_MATRIX.json`
- generator: `tools/normal_form_ingress_pass.py`
- derivation pass: `tools/external_paper_ingress_80_derivation_pass.py`

This ingress covers **712 rows**: every `OBLIGATION_ROWS.json` row whose status
is not `receipt_bound`. It requires each such row to carry a generalized Kimi
normal form, a paper-specific Kimi normal form, an advanced lane form, and an
explicit FLCR conversion rule before NIST/NSIT validators may route it to a
receipt, citation, CAM, calibration, synthesis, ledger, or falsifier closure.

This does **not** promote any row to ASSEMBLE. It creates the missing
`paper.normal_form_conversion` gate that must pass before later evidence queues
can bind the row honestly.
