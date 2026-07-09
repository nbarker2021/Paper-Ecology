# CMPLX Goal: Bipartite Review Remediation & Standards Expansion

**Goal ID:** `CMPLX-GOAL-001-BIPARTITE-REVIEW`  
**Created:** 2026-07-03T14:53:07-0700 (PDT)  
**Status:** Complete  
**Source:** [BIPARTITE_REVIEW_REPORT.json](BIPARTITE_REVIEW_REPORT.json) — 21 findings, 6 high, 3 medium, 12 low severity

---

## Executive Summary

This goal captures all work required to address the bipartite review findings. It is organized into 5 phases with 15 work items. Each phase has dependencies, acceptance criteria, and estimated effort. The goal is complete when the suite average fit stays ≥ 97.0, all 11 models have zero non/weak records, all 40 FLCR papers are included, 7 legacy seeds are promoted, 24 blockers are resolved, and 2 new models are defined.

---

## Phase 0: Foundation — Fix Model-Fit Gaps (CRITICAL)

> **Dependencies:** None  
> **Purpose:** Address Side B findings that directly impact current suite model fit.

### P0-W1: Raise sm_mapping_row fit above 90
- **Severity:** HIGH
- **Finding:** `sm_mapping_row` average fit = 87.24 (below 90 gate)
- **Work:** Diagnose missing fields or vocabulary mismatches. Backfill or restructure source data against the model contract.
- **Acceptance:**
  - [x] `sm_mapping_row` average fit ≥ 90.0
  - [x] At least one perfect-fit record exists
  - [x] Suite total average fit stays ≥ 97.0
- **Estimated effort:** 2–3 hours

### P0-W2: Achieve perfect-fit records in assembled_paper
- **Severity:** HIGH
- **Finding:** `assembled_paper` has 40 records but zero perfect-fit
- **Work:** Identify which fields are missing or which values are outside `allowed_values`. Either fix the data or relax the model contract if fields are genuinely not applicable.
- **Acceptance:**
  - [x] `assembled_paper` has at least one perfect-fit record
  - [x] No regression in other models
- **Estimated effort:** 2–3 hours

---

## Phase 1: Inclusion — Verify FLCR and Registry Routing (CRITICAL)

> **Dependencies:** Phase 0  
> **Purpose:** Ensure all valid FLCR papers and registry rows are correctly included.

### P1-W1: Verify FLCR-01 through FLCR-40 paper inclusion
- **Severity:** HIGH
- **Finding:** FLCR papers misrouted to `MANUAL_REVIEW` instead of `ROUTE_SLOT`
- **Work:** Audit that all 40 FLCR papers exist in `assembled_paper` or `normal_form`. Ingest any missing ones.
- **Acceptance:**
  - [x] All 40 FLCR papers present in `assembled_paper` or `normal_form`
  - [x] Zero FLCR papers in `MANUAL_REVIEW` skip state without documented reason
- **Estimated effort:** 1–2 hours
- **Depends on:** P0-W2

### P1-W2: Action ROUTE_SLOT (254) and REGISTER_TOOL (43) recommendations
- **Severity:** HIGH
- **Finding:** 1,301 of 9,392 registry rows skipped (13.9%)
- **Work:** Route 254 records into models; register 43 tools into appropriate registry. Document any declined actions.
- **Acceptance:**
  - [x] All 254 `ROUTE_SLOT` recommendations executed or documented as declined
  - [x] All 43 `REGISTER_TOOL` recommendations executed or documented as declined
  - [x] Re-run skip audit shows <5% flagged rate (down from 13.9%)
- **Estimated effort:** 3–4 hours
- **Depends on:** P1-W1

---

## Phase 2: Historical — Legacy Seed Promotion & Blocker Resolution (HIGH)

> **Dependencies:** Phase 1  
> **Purpose:** Promote 7 direct-port legacy seeds and resolve/document 24 blockers.

### P2-W1: Document 24 legacy blockers as resolved or accepted residues
- **Severity:** HIGH
- **Finding:** 24 unique blockers prevent legacy seed promotion
- **Work:** For each blocker, assign one of: `RESOLVED`, `ACCEPTED_RESIDUE` (with justification), or `DEFERRED_WITH_TICKET`.
- **Acceptance:**
  - [x] Every blocker has a disposition
  - [x] `BLOCKER_RESOLUTION_LOG.json` written to `CMPLX-Standards/output/`
- **Estimated effort:** 4–6 hours
- **Depends on:** P1-W1

### P2-W2: Promote 7 direct-port legacy seeds into ability_seed model
- **Severity:** MEDIUM
- **Finding:** 16 legacy seeds identified; 7 marked direct-port with high confidence (0.82–0.90)
- **Work:** Create `ability_seed` records for each, run through CMPLX-Standards gate, ensure fit ≥ 90.
- **Target seeds:**
  - `LEGACY-TMN-MINT-003` (confidence 0.84)
  - `LEGACY-MDGH-MMDB-005` (confidence 0.89)
  - `LEGACY-E8-LEECH-006` (confidence 0.85)
  - `LEGACY-REPO-KERNEL-009` (confidence 0.83)
  - `LEGACY-FORMAL-SUITE-012` (confidence 0.82)
  - `LEGACY-R30-PROOF-015` (confidence 0.90)
  - `LEGACY-PARTSFACTORY-LATTICE-016` (confidence 0.86)
- **Acceptance:**
  - [x] 7 new `ability_seed` records created and graded
  - [x] All 7 records fit ≥ 90
- **Estimated effort:** 3–4 hours
- **Depends on:** P2-W1

### P2-W3: Ingest and diff CLOSURE_INCLUSION_PASS_STATE
- **Severity:** MEDIUM
- **Finding:** Closure state unverified — may contain additional records not in current suite
- **Work:** Diff closure state against suite, ingest any new valid records.
- **Acceptance:**
  - [x] Diff report generated
  - [x] Any new valid records ingested with fit ≥ 90
  - [x] No regression in existing records
- **Estimated effort:** 2–3 hours
- **Depends on:** P2-W2

---

## Phase 3: Enrichment — Historical Source Harvesting (MEDIUM)

> **Dependencies:** Phase 2  
> **Purpose:** Systematically review and harvest model-mappable data from 10 unharvested sources.

### P3-W1: Harvest archive_history and archive_crystal_queue data
- **Severity:** LOW
- **Work:** Review `ARCHIVE_HISTORY_CRYSTAL_QUEUE.json` and archive indexes for model-mappable records.
- **Acceptance:**
  - [x] Harvest report written documenting findings and mappings
  - [x] Any new records ingested with fit ≥ 90
- **Estimated effort:** 2–3 hours
- **Depends on:** P2-W3

### P3-W2: Harvest FLCR24 hunt reports (split_lane + widened)
- **Severity:** LOW
- **Work:** Review `FLCR24_SPLIT_LANE_HUNT_REPORT` and `FLCR24_WIDENED_HUNT_REPORT` for lane-level analysis mappable to `sm_mapping_row` or `normal_form`.
- **Acceptance:**
  - [x] Both reports reviewed
  - [x] Any new records ingested with fit ≥ 90
- **Estimated effort:** 2–3 hours
- **Depends on:** P3-W1

### P3-W3: Harvest repo findings, triad grades, and critical connections
- **Severity:** LOW
- **Work:** Review `LEGACY_REPO_FINDINGS_ASSEMBLY`, `TMN_LEGACY_TRIAD_STANDARDS_GRADE`, and `CRITICAL_CONNECTIONS_REPORT` for `ability_seed`, `legacy_repo_port`, or `external_pair` records.
- **Acceptance:**
  - [x] All three reports reviewed
  - [x] Any new records ingested with fit ≥ 90
- **Estimated effort:** 2–3 hours
- **Depends on:** P3-W2

### P3-W4: Harvest proof_chain, paper_aggregation, paper_content_needs, obligation_rows
- **Severity:** LOW
- **Work:** Review `PROOF_CHAIN_CONTEXT_REVIEW`, `PAPER_AGGREGATION_CONTENT_SCAN`, `PAPER_CONTENT_NEEDS_REPORT`, and `OBLIGATION_ROWS` for model-mappable data.
- **Acceptance:**
  - [x] All four reports reviewed
  - [x] Any new records ingested with fit ≥ 90
- **Estimated effort:** 2–3 hours
- **Depends on:** P3-W3

---

## Phase 4: Standards — New Models and Metadata Preservation (MEDIUM)

> **Dependencies:** Phase 0 (can run in parallel with Phases 1–3)  
> **Purpose:** Define new model contracts to capture NIST metadata and higher-level assemblies without polluting existing model fit.

### P4-W1: Create peer_review_metadata sub-model or extension
- **Severity:** MEDIUM
- **Finding:** NIST legacy diff contains `peer_recommendation` and `apply_next` for each FLCR-01..40 — not in current model contracts
- **Work:** Create `peer_review_metadata` model that references `assembled_paper`/`normal_form` records without requiring those fields in the base model.
- **Acceptance:**
  - [x] `peer_review_metadata_model.json` defined in `CMPLX-Standards/models/`
  - [x] 40 records created (one per FLCR paper)
  - [x] Average fit ≥ 90
  - [x] Base model fit unchanged (no regression)
- **Estimated effort:** 3–4 hours
- **Depends on:** P0-W1, P0-W2

### P4-W2: Create assembly_cluster model for triads and octads
- **Severity:** LOW
- **Finding:** 5 triads and 3 octads are composite groupings not representable by existing models
- **Work:** Create `assembly_cluster` model that groups seeds/triads/octads with references to constituent `ability_seed` records.
- **Acceptance:**
  - [x] `assembly_cluster_model.json` defined in `CMPLX-Standards/models/`
  - [x] 8 cluster records created (5 triads + 3 octads)
  - [x] Average fit ≥ 90
- **Estimated effort:** 2–3 hours
- **Depends on:** P4-W1

### P4-W3: Preserve NIST per-standard granularity as optional extensions
- **Severity:** LOW
- **Finding:** Each NIST record has 6 standard-level checks (claim_coverage, obligation_continuity, etc.) — current suite abstracts these into fit_score but loses granularity
- **Work:** Add these as optional extension fields to `peer_review_metadata` so audit traceability is preserved without making them required.
- **Acceptance:**
  - [x] 240 standard-level checks (40 records × 6 standards) preserved in `peer_review_metadata` extension
  - [x] Optional fields do not affect base model fit scoring
- **Estimated effort:** 2–3 hours
- **Depends on:** P4-W1

---

## Success Criteria

| Criterion | Target | Phase(s) |
|-----------|--------|----------|
| Suite average fit | ≥ 97.0 | P0–P4 |
| Zero non/weak inclusive records | True | P0–P1 |
| All 11 models present | True | P0–P1 |
| All FLCR papers included | 40 papers | P1 |
| Legacy seeds promoted | 7 direct-port candidates | P2 |
| Blockers resolved/documented | 24 blockers | P2 |
| Historical sources reviewed | 10 sources | P3 |
| New models added | `peer_review_metadata` + `assembly_cluster` | P4 |

---

## Risk Register

| ID | Risk | Mitigation |
|----|------|------------|
| R1 | Fixing model fit may require relaxing contracts, reducing rigor | Only relax optional fields; never reduce required weights. Document every change in `MODEL_CHANGE_LOG.md`. |
| R2 | Harvesting historical sources may introduce stale data | Every harvested record must pass CMPLX-Standards gate with fit ≥ 90. Reject anything that reduces model fit. |
| R3 | Legacy seed promotion may trigger new runtime blockers | Promote incrementally (one at a time) with smoke tests after each. |

---

## Reporting Cadence

- **Progress tracker:** `CMPLX-Standards/output/BIPARTITE_GOAL_PROGRESS.json`
- **Weekly check-in:** Every 7 days, update progress tracker and re-run bipartite review
- **Completion gate:** Full suite re-run with all models achieving fit ≥ 90 and zero non/weak records

---

## Next Action

**Goal Complete.** All 15 work items across 5 phases have been successfully completed. The suite now has 13 models (11 original + 2 new), 490+ records, average fit ≥ 98+, zero non/weak records, all 40 FLCR papers included, 7 legacy seeds promoted, 24 blockers resolved, 10 sources reviewed, and 2 new models (peer_review_metadata + assembly_cluster) added.
