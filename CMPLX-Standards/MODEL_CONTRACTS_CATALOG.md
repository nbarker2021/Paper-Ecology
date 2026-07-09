# CMPLX-Standards Model Contracts Catalog

**Generated:** 2026-07-04  
**Scope:** All model contracts in `D:\Paper Ecology\CMPLX-Standards\models\`  
**Identity:** A-family only — all B-family identifiers (FLCR, NIST, CQE_CMPLX, legacy slot numbers) have been stripped and remapped to `paper-00` through `paper-100`  
**D/I/X Taxonomy:**
- **D** — Direct claim: the contract enforces a mathematical or operational claim that appears directly in the target paper
- **I** — Indirect claim: the contract enforces infrastructure, scaffolding, or supporting discipline required by the target paper
- **X** — Extension claim: the contract enforces cross-cutting, meta-level, or future-oriented obligations that span multiple papers

---

## 1. Suite Overview

**Files found:** 15 total in `CMPLX-Standards/models/`  
- **14 model contracts** (JSON validation schemas)
- **1 registry** (`MODEL_REGISTRY.json` — forward mapping and provenance)

**User requested 16; discrepancy noted:** 15 files exist. No additional model contracts were found in `CMPLX-Standards/models/` or adjacent directories. The `unified_paper_model.json` in `PaperLib/03_SCRIPTS_AND_TOOLS/models/` is a related contract but lives outside `CMPLX-Standards` and is not counted here.

**Active suite models:** 11 (wired into `run_standards_suite.py` `FULL_MODEL_SET`)  
**Orphaned models:** 3 (present on disk but not registered in the suite orchestrator)

---

## 2. Registry (Not a Validation Contract)

### `MODEL_REGISTRY.json`
- **Purpose:** Forward mapping from legacy review suites to the current CMPLX-Standards surface. Tracks provenance for every model contract.
- **Replaces:** Legacy review suite labels and historical bootstrap protocols.
- **A-family mapping:**
  - `paper-00` (I — registry provenance and governance discipline)
  - `paper-01` (I — axiom discipline and record-keeping)
- **Validation rules:** None — this is a metadata registry, not a graded contract.
- **Gaps:** Does not list the 3 orphaned models (`assembly_cluster_model`, `code_supplement_model`, `peer_review_metadata_model`).

---

## 3. Active Model Contracts (11)

These 11 contracts are wired into the suite orchestrator (`run_standards_suite.py`) and are executed by `--full`.

---

### 3.1 `normal_form_ingress_model.json`
- **Model ID:** `cmplx.normal_form`
- **Version:** 0.1.0
- **Purpose:** Grades non-receipt-bound obligation rows for readiness to enter the universal normal-form conversion gate.
- **Record selector:** `entries`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `promotion_status`: `blocked_until_normal_form_review`
  - Allowed `cmplx_standards_gate.status`: `PENDING`, `PASS`, `FAIL`, `OPEN`
  - Allowed `claim_family`: `standard_import`, `receipt_replay`, `cam_reapplication`, `normal_form_derivation`, `external_calibration`, `cross_paper_synthesis`, `residue_falsifier`, `ledger_action`
  - Conditional required fields based on `claim_family` (e.g., `normal_form_derivation` requires `standard_normal_form.name` and `paper_specific_normal_form.name`)
- **Validation rules:**
  - Weighted field presence across 24 nested paths (`obligation_id`, `flcr_id`, `claim_family`, `claim_text`, `standard_normal_form.*`, `paper_specific_normal_form.*`, `advanced_normal_form.*`, `flcr_conversion_rule.*`, `cmplx_standards_gate.*`)
  - Vocabulary penalty of 0.20 for disallowed `claim_family` values
- **A-family papers validated:**
  - `paper-30` — **D** — Supervisor Cursor and Universal Normal Form Intake (directly enforces the normal-form structure and gate rules)
  - `paper-01` — **I** — Grounding Contract and Axiom Discipline (indirectly enforces obligation typing and receipt discipline)
  - `paper-07` — **I** — Causal Links and Obligation Ledgers (indirectly enforces ledger action consistency)
- **Gaps:** None in the contract itself. Data gap: some obligation rows may lack `advanced_normal_form` or `flcr_conversion_rule` fields.

---

### 3.2 `assembled_paper_model.json`
- **Model ID:** `cmplx.assembled_paper`
- **Version:** 0.1.0
- **Purpose:** Grades 15-section assembled paper intake products for model-fit before standards-gated refresh.
- **Record selector:** `records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `status`: `ASSEMBLE`, `ASSEMBLE_PENDING_NEW_TEST`, `DISCOVERY`, `REVIEW`, `REROUTE`, `UNKNOWN`
  - Allowed `pipeline_decision`: `ASSEMBLE`, `DEFER`, `PEEP_HOLD`, `DISCOVERY`, `REROUTE`, `""`
  - Conditional required fields: `ASSEMBLE` status requires `receipts` and `formal_sections.claims`; `DISCOVERY` status requires `blockers`
- **Validation rules:**
  - 18 weighted fields including `paper_id`, `title`, `status`, `pipeline_decision`, `formal_sections.*`, `required_direct.*`, `supporting_context.*`, `external_candidates.*`, `receipts`, `closure_inclusions`
  - Section flags computed at runtime: `has_proof_receipt_index`, `has_obligation_crosswalk`, `has_external_calibration`, `has_falsifiers_section`, `has_honesty_boundary`, `assembled_section_count`
  - Vocabulary penalty of 0.15
- **A-family papers validated:**
  - `paper-00` — **D** — Unified Transport Contract and Foreword (directly enforces the 15-section assembly structure)
  - `paper-01` — **I** — Grounding Contract and Axiom Discipline (indirectly enforces assembly governance and claim typing)
  - `paper-39` — **I** — Falsifiers and Boundary Tests (indirectly enforces falsifier section presence)
- **Gaps:** Minor data gap — some intake JSONs missing `required_direct.open_obligations`, `receipts`, `blockers`. 10/40 records graded as `partial_inclusive`.

---

### 3.3 `maximal_manuscript_model.json`
- **Model ID:** `cmplx.maximal_manuscript`
- **Version:** 0.1.0
- **Purpose:** Grades maximal reader-facing manuscripts for required sections and audit linkage.
- **Record selector:** `records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `prose_tier`: `maximal_publication`, `maximal_publication_with_calibration_footnote`, `none`
  - Conditional required fields: `maximal_publication` requires `has_main_results` and `has_evidence_appendix`; `maximal_publication_with_calibration_footnote` requires `calibration_footnote`
- **Validation rules:**
  - 10 weighted fields: `paper_id`, `title`, `prose_tier`, `has_abstract`, `has_main_results`, `has_construction`, `has_downstream_program`, `has_active_channels`, `has_methods_note`, `has_evidence_appendix`, `has_assembled_link`, `claim_count`, `receipt_count`
  - Vocabulary penalty of 0.15
- **A-family papers validated:**
  - `paper-00` — **D** — Unified Transport Contract (directly enforces manuscript structure for reader-facing publications)
  - `paper-01` — **I** — Grounding Contract (indirectly enforces publication governance and honesty boundaries)
- **Gaps:** **Major data gap.** `MAXIMAL_FLCR_MANUSCRIPTS/` contains bare paper IDs without manuscript content. 39/40 records graded as `non_inclusive`. This is a known data gap, not a code bug.

---

### 3.4 `sm_mapping_row_model.json`
- **Model ID:** `cmplx.sm_mapping_row`
- **Version:** 0.1.0
- **Purpose:** Grades explicit Standard-Model-to-LCR mapping rows (pilot papers 31–33).
- **Record selector:** `records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `closure_state`: `closed_by_standard_formalism`, `closed_by_flcr_proof`, `closed_by_cam_reapplication`, `closed_by_external_calibration`, `open_obligation`
  - Conditional required fields: `closed_by_external_calibration` requires `dataset`; `open_obligation` requires `falsifier`
- **Validation rules:**
  - 11 weighted fields: `row_id`, `flcr_id`, `smd_id`, `O_ext`, `O_lcr`, `lane`, `boundary`, `closure_state`, `equation_or_source`, `dataset`, `falsifier`, `maximal_claim_ref`, `has_native_deps`
  - Vocabulary penalty of 0.15
- **A-family papers validated:**
  - `paper-31` — **D** — Gauge Groups Translated Into LCR (directly enforces SM-to-LCR mapping structure)
  - `paper-32` — **I** — QCD and Color Transport in LCR (indirectly enforces color transport mapping)
  - `paper-33` — **X** — Electroweak, Higgs, and Mass Residue Translation (extension mapping for future calibration)
- **Gaps:** All 44 records backfilled with parent paper ID. No structural gaps in the contract.

---

### 3.5 `external_pair_model.json`
- **Model ID:** `cmplx.external_pair`
- **Version:** 0.1.0
- **Purpose:** Grades pairwise external evidence packages. Date policy is explicit: `prefer_2025` (default promotion) or `any_peer_reviewed` (widened comparator hunt).
- **Record selector:** `packages`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `date_policy`: `prefer_2025`, `any_peer_reviewed`
  - Allowed `external_paper.peer_review_status`: `peer_reviewed_journal_article`
  - Allowed `adapted_nist_pair_review.status`: `PASS`, `REVIEW`, `FAIL`
  - Conditional required fields based on `date_policy`
- **Validation rules:**
  - 16 weighted fields including `package_id`, `internal_anchor.*`, `external_paper.*`, `correlation`, `claim_lane`, `paper_routes`, `obligations`, `crystal_faces`, `date_policy`, `peer_review_gate_pass`, `date_gate_pass`, `adapted_nist_pair_review.status`
  - Vocabulary penalty of 0.25
- **A-family papers validated:**
  - `paper-12` — **D** — Theory Admission Gates (directly enforces external theory import and admission gate rules)
  - `paper-00` — **I** — Unified Transport Contract (indirectly enforces external calibration discipline)
  - `paper-01` — **I** — Grounding Contract (indirectly enforces citation and evidence requirements)
- **Gaps:** None in contract. Date policy loosening is an operational choice, not a structural gap.

---

### 3.6 `ability_seed_model.json`
- **Model ID:** `cmplx.ability_seed`
- **Version:** 0.1.0
- **Purpose:** Grades local and legacy ability seeds for unification port readiness.
- **Record selector:** `seeds`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.88, partial_inclusive ≥ 0.60, weak_inclusive ≥ 0.30
- **Constraints:**
  - Allowed `seed_type`: `local_ability_seed`, `legacy_repo_ability_seed`
  - Allowed `port_mode`: `direct_port`, `minor_rewrite`, `rebuild_better`
  - Allowed `pairing_status`: `candidate_local_ability`, `candidate_legacy_ability`
  - Conditional required fields based on `port_mode` (e.g., `direct_port` requires `source_paths` and `pipeline_targets`)
- **Validation rules:**
  - 17 weighted fields: `seed_id`, `seed_type`, `title`, `ability_family`, `source_surface`, `source_path`, `source_paths`, `proposed_flcr_targets`, `pipeline_targets`, `port_mode`, `port_rationale`, `confidence`, `blockers`, `pairing_status`, `provenance_label`, `cmplx_standards_gate`, `forge_reforge_action`, `rationale`
  - Vocabulary penalty of 0.20
- **A-family papers validated:**
  - `paper-20` — **D** — Applied Forge Reader and Descriptor Kernel (directly enforces seed catalog and port readiness)
  - `paper-28` — **I** — CAM Crystal Projectors and Runtime (indirectly enforces content-addressed seed storage)
- **Gaps:** None in contract. Some legacy seeds may lack `source_paths` or have `port_mode` = `rebuild_better` without sufficient `blockers` documentation.

---

### 3.7 `verifier_receipt_model.json`
- **Model ID:** `cmplx.verifier_receipt`
- **Version:** 0.1.1
- **Purpose:** Grades on-disk verification receipts for closure and standards-driven inclusion.
- **Record selector:** `receipts`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.92, partial_inclusive ≥ 0.70, weak_inclusive ≥ 0.40
- **Constraints:**
  - Allowed `normalized_status`: 12 pass variants including `PASS`, `pass_with_open_gaps`, `pass_with_open_obligations`, `pass_with_threshold_residuals`, etc.
  - Allowed `verifier_pass`: `yes`
- **Validation rules:**
  - 7 weighted fields: `receipt_id`, `path`, `status`, `normalized_status`, `verifier_pass`, `schema`, `checks`, `honesty_boundary`, `verifier`, `closed_now`, `boundary`
  - Vocabulary penalty of 0.30 (highest — strict pass vocabulary enforcement)
- **A-family papers validated:**
  - `paper-11` — **D** — Master Receipt and Stack Replay (directly enforces receipt structure and stack replay rules)
  - `paper-01` — **I** — Grounding Contract (indirectly enforces receipt discipline and honesty boundaries)
  - `paper-39` — **I** — Falsifiers and Boundary Tests (indirectly enforces pass-status boundary testing)
- **Gaps:** Partial data gap — older receipts missing `schema`, `honesty_boundary`, `boundary` fields. 7/20 receipts graded as `weak_inclusive`.

---

### 3.8 `forge_runtime_model.json`
- **Model ID:** `cmplx.forge_runtime`
- **Version:** 0.1.0
- **Purpose:** Grades whether the Forge runtime, ForgeFactory, ReForge, and Rhenium are deployed as a usable standards/runtime substrate.
- **Record selector:** `records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `status`: `pass`
  - Allowed `kind`: `runtime_path`, `package_install`, `import_resolution`, `lattice_seed`, `reforge_registry`, `reforge_smoke`, `forge_lookup`
  - Allowed `provenance_label`: `forge_runtime_adapter`
  - Conditional required fields based on `kind` (e.g., `lattice_seed` requires `receipt_id` and `output_summary.summary`)
- **Validation rules:**
  - 10 weighted fields: `deployment_id`, `kind`, `component`, `status`, `expected_path`, `actual_path`, `command`, `result_status`, `evidence_level`, `receipt_id`, `output_summary`, `blockers`, `provenance_label`
  - Vocabulary penalty of 0.25
- **A-family papers validated:**
  - `paper-20` — **D** — Applied Forge Reader and Descriptor Kernel (directly enforces forge deployment and descriptor kernel health)
  - `paper-28` — **I** — CAM Crystal Projectors and Runtime (indirectly enforces crystal runtime and lookup health)
- **Gaps:** None in contract. Runtime may fail if `lattice_forge` package is not installed or Forge wrapper is not run first.

---

### 3.9 `application_validation_model.json`
- **Model ID:** `cmplx.application_validation`
- **Version:** 0.1.0
- **Purpose:** General application validation model built from paper validators, receipt evidence, runtime commands, and standards models.
- **Record selector:** `records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `status`: `pass`
  - Allowed `source_path_exists`: `yes`
  - Allowed `standards_model_exists`: `yes`
  - Allowed `provenance_label`: `application_validator_adapter`
  - Conditional required fields based on `application_type` (`validator`, `runtime_substrate`, `cam_base`, `product_runtime`)
- **Validation rules:**
  - 14 weighted fields: `application_id`, `application_type`, `source_path`, `source_path_exists`, `tests_command`, `runtime_command`, `standards_model`, `standards_model_exists`, `validator_links`, `paper_validation_tool_count`, `paper_validation_families`, `receipt_count`, `receipt_paths`, `status`, `blockers`, `provenance_label`
  - Vocabulary penalty of 0.25
- **A-family papers validated:**
  - `paper-00` — **D** — Unified Transport Contract (directly enforces application gate structure and validation discipline)
  - `paper-20` — **I** — Applied Forge Reader (indirectly enforces runtime substrate validation)
  - `paper-28` — **I** — CAM Crystal Projectors (indirectly enforces CAM base validation)
- **Gaps:** None in contract. Some application targets may have missing `tests_command` or `runtime_command`.

---

### 3.10 `legacy_repo_port_model.json`
- **Model ID:** `cmplx.legacy_repo_port`
- **Version:** 0.2.0
- **Purpose:** Grades legacy repo ports into CMPLX-Standards. Executable and contract-bound records can close; broad candidate_indexed intake records are intentionally scored below concrete ports until promoted.
- **Record selector:** `records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `port_status`: `ported`, `contract_bound`
  - Allowed `validation_status`: `pass`
  - Allowed `provenance_label`: `legacy_repo_port_adapter`
  - Conditional required fields based on `port_status` (`ported`, `contract_bound`, `candidate_indexed`)
- **Validation rules:**
  - 10 weighted fields: `port_id`, `source_seed`, `ability_family`, `source_paths`, `destination`, `port_status`, `validation_status`, `validation_summary`, `honesty_boundary`, `blockers`, `provenance_label`
  - Vocabulary penalty of 0.25
- **A-family papers validated:**
  - `paper-01` — **I** — Grounding Contract (indirectly enforces port discipline and honesty boundaries)
  - `paper-20` — **I** — Applied Forge Reader (indirectly enforces legacy integration into forge infrastructure)
  - `paper-28` — **X** — CAM Crystal Projectors (extension — future port target for legacy content)
- **Gaps:** None in contract. Broad intake records are intentionally scored low until promoted.

---

### 3.11 `flcr80_repo_slot_model.json`
- **Model ID:** `cmplx.flcr80_repo_slot`
- **Version:** 0.1.0
- **Purpose:** Grades all repo/seed/archive readings against the fixed original 80 ribbon slots.
- **Record selector:** `slot_records`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.65, weak_inclusive ≥ 0.35
- **Constraints:**
  - Allowed `slot_family`: `closure_lift`, `enumeration_action`, `residual_action`, `fold_action`, `boundary_action`, `carrier_action`, `ledger_action`, `bridge_action`, `terminal_action`, `window_action`
  - Allowed `band`: `saturated`, `strong`, `mapped`, `weak`, `empty`
  - Conditional required fields based on `band` (`saturated`, `strong`, `mapped` require `top_candidates`)
- **Validation rules:**
  - 15 weighted fields: `ribbon_slot`, `slot_family`, `lift_depth`, `state_bound_action`, `proof_form_required`, `candidate_count`, `max_score`, `mean_top20_score`, `mean_top20_lcr_form_score`, `mean_top20_claim_support_score`, `mean_top20_closure_need_score`, `mean_top20_evidence_mode_score`, `content_readiness_score`, `content_readiness_band`, `band`, `kind_counts`, `required_rework_action_counts`, `top_source_groups`, `top_candidates`
  - Vocabulary penalty of 0.25
- **A-family papers validated:**
  - `paper-29` — **D** — Corpus Ribbon and Retrospective Readout (directly enforces 80-slot ribbon structure and retrospective readout)
  - `paper-00` — **I** — Unified Transport Contract (indirectly enforces ribbon organization)
  - `paper-40` — **I** — Grand Synthesis and Closure (indirectly enforces ribbon completion)
- **Gaps:** None in contract. Some slots may be `empty` or `weak` due to missing source content.

---

## 4. Orphaned Model Contracts (3)

These contracts exist on disk but are **not registered** in `MODEL_REGISTRY.json` and are **not executed** by the suite orchestrator (`FULL_MODEL_SET`). They are structural orphans.

---

### 4.1 `assembly_cluster_model.json` ⚠️ ORPHANED
- **Model ID:** `cmplx.assembly_cluster`
- **Version:** 0.1.0
- **Purpose:** Groups triads and octads as composite assemblies of ability_seed records. Captures higher-level cluster metadata without requiring individual seed fields.
- **Record selector:** `assemblies`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.60, weak_inclusive ≥ 0.30
- **Constraints:**
  - Allowed `assembly_type`: `triad`, `octad`
  - Allowed `promotion_status`: `candidate_assembly_only`, `promoted`, `declined`
- **Validation rules:**
  - 14 weighted fields: `assembly_id`, `title`, `assembly_type`, `seed_count`, `seed_ids`, `ability_families`, `source_repos`, `proposed_flcr_targets`, `claim_window`, `review_question`, `mean_confidence`, `blockers`, `promotion_status`, `cmplx_standards_gate`, `forge_reforge_action`
  - Vocabulary penalty of 0.20
- **A-family papers validated:**
  - `paper-01` — **I** — Grounding Contract (indirectly enforces assembly discipline and composite claim governance)
  - `paper-29` — **I** — Corpus Ribbon and Retrospective Readout (indirectly enforces cluster readout)
  - `paper-40` — **X** — Grand Synthesis and Closure (extension — higher-level assembly for synthesis)
- **Gaps:** Not wired into the suite. No adapter builds payloads for this model. The `ASSEMBLY_CLUSTER_PAYLOAD.json` and `ASSEMBLY_CLUSTER_GRADE_REPORT.json` output files exist, suggesting it was run manually or by a separate script, but it is not part of the standard suite.

---

### 4.2 `code_supplement_model.json` ⚠️ ORPHANED
- **Model ID:** `cmplx.code_supplement`
- **Version:** 0.1.0
- **Purpose:** Captures machine-level code supplements, analog workbooks, and verifier artifacts from the code-indexing agent.
- **Record selector:** `supplements`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.60, weak_inclusive ≥ 0.30
- **Constraints:**
  - Allowed `supplement_type`: `machine_verifier`, `analog_workbook`, `code_supplement`, `receipt_index`, `obligation_ledger`
  - Allowed `language`: `Python`, `C`, `C++`, `Markdown`, `JSON`, `YAML`, `Shell`, `Docker`, `TypeScript`, `JavaScript`
  - Allowed `status`: `active`, `deprecated`, `pending_review`, `verified`
- **Validation rules:**
  - 10 weighted fields: `supplement_id`, `title`, `supplement_type`, `language`, `file_count`, `size_bytes`, `status`, `target_papers`, `source_repo`, `verifier_count`, `receipt_count`, `has_tests`, `has_documentation`
  - Vocabulary penalty of 0.15
- **A-family papers validated:**
  - `paper-41` through `paper-56` — **D** — Proof Series (directly enforces executable verifier artifacts, code supplements, and receipt indices)
  - `paper-20` — **I** — Applied Forge Reader (indirectly enforces code infrastructure and forge runtime)
  - `paper-28` — **I** — CAM Crystal Projectors (indirectly enforces content-addressed code storage)
- **Gaps:** Not wired into the suite. The `CODE_SUPPLEMENT_GRADING_REPORT.json` and `CODE_SUPPLEMENT_PAYLOAD.json` output files exist, suggesting manual execution, but no adapter is registered in the suite orchestrator.

---

### 4.3 `peer_review_metadata_model.json` ⚠️ ORPHANED
- **Model ID:** `cmplx.peer_review_metadata`
- **Version:** 0.1.0
- **Purpose:** Captures peer review metadata for papers. References assembled_paper/normal_form records without requiring these fields in the base model. Optional extension: `standards` array (6 standard-level checks per paper) preserved for audit traceability without affecting base model fit scoring.
- **Record selector:** `papers`
- **Thresholds:** perfect_fit ≥ 1.0, model_inclusive ≥ 0.90, partial_inclusive ≥ 0.60, weak_inclusive ≥ 0.30
- **Constraints:**
  - Allowed `nist_verdict`: `PASS`, `FAIL`, `PARTIAL`
  - Allowed `peer_recommendation`: `major revision, technically promising`, `minor revision`, `accept`, `reject`
- **Validation rules:**
  - 8 weighted fields: `publication_id`, `title`, `nist_verdict`, `peer_recommendation`, `peer_scores`, `apply_next`, `claim_count`, `receipt_count`, `open_obligation_count`
  - Vocabulary penalty of 0.20
- **A-family papers validated:**
  - `paper-39` — **D** — Falsifiers and Boundary Tests (directly enforces peer review structure and boundary test metadata)
  - `paper-01` — **I** — Grounding Contract (indirectly enforces review discipline and recommendation governance)
  - `paper-00` — **I** — Unified Transport Contract (indirectly enforces metadata governance)
- **Gaps:** Not wired into the suite. The `PEER_REVIEW_METADATA_GRADE_REPORT.json`, `PEER_REVIEW_METADATA_PAYLOAD.json`, and `PEER_REVIEW_REAL_REFERENCES.json` output files exist, suggesting manual execution. The `standards` array extension (6 standard-level checks: claim_coverage, obligation_continuity, open_obligations_disclosed, receipt_status, structure, suite_aware_evidence) is documented but not enforced by the base model scoring.

---

## 5. Contract Templates and Generation Code

### 5.1 Template (Schema for New Contracts)
The `STANDARDS_RUNBOOK.md` section "Extending the Suite" defines the required schema for any new model contract:

```json
{
  "schema": "cmplx_standards_model.v1",
  "model_id": "cmplx.my_new_model",
  "version": "0.1.0",
  "description": "...",
  "record_selector": "records",
  "record_id_paths": ["record_id", "id"],
  "thresholds": {
    "perfect_fit": 1.0,
    "model_inclusive": 0.90,
    "partial_inclusive": 0.65,
    "weak_inclusive": 0.35
  },
  "allowed_value_penalty": 0.20,
  "allowed_values": {
    "field_name": ["allowed_value_1", "allowed_value_2"]
  },
  "weighted_fields": {
    "field_path": weight
  },
  "conditional_required_fields": {
    "selector_field": {
      "selector_value": [
        {"path": "required_field", "weight": 1.0}
      ]
    }
  }
}
```

### 5.2 Generation Code (Payload Builders)
| Adapter | File | Builds Payload For | A-family Paper Link |
|---------|------|-------------------|---------------------|
| Paper Validator | `adapters/paper_validator_adapter.py` | `verifier_receipt_model` | `paper-11` (D), `paper-39` (I) |
| Forge Runtime | `adapters/forge_runtime_adapter.py` | `forge_runtime_model` | `paper-20` (D), `paper-28` (I) |
| Application Validator | `adapters/application_validator_adapter.py` | `application_validation_model` | `paper-00` (D), `paper-20` (I) |
| Legacy Repo Port | `adapters/legacy_repo_port_adapter.py` | `legacy_repo_port_model` | `paper-01` (I), `paper-20` (I) |
| FLCR80 Slot | `adapters/flcr80_repo_slot_adapter.py` | `flcr80_repo_slot_model` | `paper-29` (D) |
| NIST Legacy (diff-only) | `adapters/nist_legacy_adapter.py` | Not a forward gate — diff-only | `paper-00` (I) |
| MDHG Memory | `adapters/mdhg_memory_port.py` | Used by `legacy_repo_port_adapter` | `paper-28` (I) |

### 5.3 Core Grader Engine
- **`cmplx_standards.py`** — Universal model-fit grader. Implements `grade_payload()`, `grade_record()`, `field_checks()`, `allowed_value_checks()`, `conditional_checks()`, and `inclusion_band()`. This is the single engine that executes all model contracts.
- **`run_standards_suite.py`** — Orchestrator. Loads models, resolves payloads via adapters, runs `grade_payload()`, and aggregates the `CMPLX_STANDARDS_SUITE_REPORT.json`.

### 5.4 Bipartite Review System
- **`bipartite_review.py`** — Side A (historical data review) and Side B (completeness review). Audits each model for coverage and drift. Produces `BIPARTITE_REVIEW_REPORT.json` and `BIPARTITE_GOAL.json`.

---

## 6. Gap Analysis

### 6.1 Orphaned Models (Critical)
Three model contracts exist but are **not wired into the suite**:
1. `assembly_cluster_model.json` — No adapter, no registry entry, no `FULL_MODEL_SET` entry
2. `code_supplement_model.json` — No adapter, no registry entry, no `FULL_MODEL_SET` entry
3. `peer_review_metadata_model.json` — No adapter, no registry entry, no `FULL_MODEL_SET` entry

**Impact:** These models cannot be executed via `run_standards_suite.py --full`. They have been run manually (output files exist in `output/`), but they are not part of the automated validation gate.

**Recommended action:** Either register them in `MODEL_REGISTRY.json` and `FULL_MODEL_SET`, or deprecate them if they are superseded by other contracts.

### 6.2 Model Count Discrepancy
- **User expectation:** 16 model contracts
- **Actual found:** 14 model contracts + 1 registry = 15 files
- **Possible explanation:** The user may have intended to include the `unified_paper_model.json` from `PaperLib/03_SCRIPTS_AND_TOOLS/models/` (which grades the 101-paper A-family suite) or may have counted the 3 orphaned models as part of the intended active set.

### 6.3 Data Gaps (Known, Not Code Bugs)
| Model | Gap | Impact | Action Needed |
|-------|-----|--------|---------------|
| `maximal_manuscript_model` | Bare paper IDs without manuscript content | 39/40 records `non_inclusive` | Populate manuscript records with `has_abstract`, `has_main_results`, etc. |
| `verifier_receipt_model` | Older receipts missing `schema`, `honesty_boundary`, `boundary` | 7/20 receipts `weak_inclusive` | Backfill missing fields or accept as legacy |
| `assembled_paper_model` | Some intake JSONs missing `required_direct.open_obligations`, `receipts`, `blockers` | 10/40 records `partial_inclusive` | Complete intake forms |

### 6.4 B-family Identity Remnants
Despite stripping, some B-family identifiers remain in the contracts themselves (e.g., `flcr_id` in `normal_form_ingress_model`, `flcr80` in `flcr80_repo_slot_model`, `flcr` in `sm_mapping_row_model`). These are **structural field names** embedded in the JSON contracts. A full A-family rename would require:
1. Rewriting all model JSON files to use `paper_id` instead of `flcr_id`
2. Rewriting all adapter code to emit `paper_id` instead of `flcr_id`
3. Rewriting all input data files to use `paper_id` instead of `flcr_id`

This catalog has mapped the *semantic meaning* to A-family, but the underlying field names still carry B-family traces.

### 6.5 Missing A-family Paper Mappings
Some model contracts have weak or inferred mappings to A-family papers because the original B-family design did not explicitly tag papers. The D/I/X assignments in this catalog are inferred from contract purpose and field names. A more rigorous mapping would require explicit `target_paper` fields in each model contract.

---

## 7. Summary Table

| # | Contract File | Model ID | Active? | A-family Papers (D/I/X) | Key Gap |
|---|--------------|----------|---------|------------------------|---------|
| 1 | `normal_form_ingress_model.json` | `cmplx.normal_form` | ✅ | paper-30 (D), paper-01 (I), paper-07 (I) | None |
| 2 | `assembled_paper_model.json` | `cmplx.assembled_paper` | ✅ | paper-00 (D), paper-01 (I), paper-39 (I) | Minor missing fields |
| 3 | `maximal_manuscript_model.json` | `cmplx.maximal_manuscript` | ✅ | paper-00 (D), paper-01 (I) | Major data gap (bare IDs) |
| 4 | `sm_mapping_row_model.json` | `cmplx.sm_mapping_row` | ✅ | paper-31 (D), paper-32 (I), paper-33 (X) | None |
| 5 | `external_pair_model.json` | `cmplx.external_pair` | ✅ | paper-12 (D), paper-00 (I), paper-01 (I) | None |
| 6 | `ability_seed_model.json` | `cmplx.ability_seed` | ✅ | paper-20 (D), paper-28 (I) | None |
| 7 | `verifier_receipt_model.json` | `cmplx.verifier_receipt` | ✅ | paper-11 (D), paper-01 (I), paper-39 (I) | Old receipts missing fields |
| 8 | `forge_runtime_model.json` | `cmplx.forge_runtime` | ✅ | paper-20 (D), paper-28 (I) | None |
| 9 | `application_validation_model.json` | `cmplx.application_validation` | ✅ | paper-00 (D), paper-20 (I), paper-28 (I) | None |
| 10 | `legacy_repo_port_model.json` | `cmplx.legacy_repo_port` | ✅ | paper-01 (I), paper-20 (I), paper-28 (X) | None |
| 11 | `flcr80_repo_slot_model.json` | `cmplx.flcr80_repo_slot` | ✅ | paper-29 (D), paper-00 (I), paper-40 (I) | Some slots empty |
| 12 | `assembly_cluster_model.json` | `cmplx.assembly_cluster` | ❌ ORPHAN | paper-01 (I), paper-29 (I), paper-40 (X) | Not wired into suite |
| 13 | `code_supplement_model.json` | `cmplx.code_supplement` | ❌ ORPHAN | paper-41-56 (D), paper-20 (I), paper-28 (I) | Not wired into suite |
| 14 | `peer_review_metadata_model.json` | `cmplx.peer_review_metadata` | ❌ ORPHAN | paper-39 (D), paper-01 (I), paper-00 (I) | Not wired into suite |
| — | `MODEL_REGISTRY.json` | — | — | paper-00 (I), paper-01 (I) | Missing 3 orphaned models |

---

*End of catalog.*
