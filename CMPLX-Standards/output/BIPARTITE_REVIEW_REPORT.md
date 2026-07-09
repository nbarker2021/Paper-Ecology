# CMPLX Bipartite Review Report

**Generated:** 2026-07-03T20:00:00+00:00
**Schema:** cmplx.bipartite_review.v1

## Executive Summary

- **Total findings:** 21
- **High severity:** 6
- **Medium severity:** 3
- **Low severity:** 12

---

## Side A — Historical Data Review (What We Missed)

Sources scanned: **18** | Missing sources: **0** | Findings: **18**

### Severity Breakdown
- **High:** 3
- **Medium:** 3
- **Low:** 12

### Findings

1. **[MEDIUM]** legacy_seed_coverage
   - 16 legacy seeds identified in harvest. Only 7 marked direct-port. None explicitly in current suite as ability_seed records.
   - *Recommendation:* Promote the 7 direct_port candidates into ability_seed model after CMPLX-Standards gate validation.

2. **[LOW]** triad_octad_assemblies
   - 5 triads and 3 octads defined as candidate assemblies. These are composite groupings, not individual records.
   - *Recommendation:* Triads/octads belong in a higher-level assembly model (not yet defined). Consider adding 'assembly_cluster' model.

3. **[HIGH]** unresolved_blockers
   - 24 unique blockers preventing legacy seed promotion: ['avoid_duplicate_canonicalization', 'choose_mmdb_contract', 'coin_library_scope_review', 'convert_markdown_registry_to_structured_index', 'decouple_http_service_assumptions', 'dedupe_lattice_implementations', 'dedupe_three_registry_surfaces', 'dirty_repo_scope_review']...
   - *Recommendation:* Resolve blockers or document as accepted residues. Many are CMPLX-Standards gate prerequisites.

4. **[HIGH]** high_volume_skipped
   - 1301 of 9392 registry rows flagged (13.9%). Top skip reasons: {'substantive_content_in_low_type': 452, 'slot_keyword_present': 348, 'pipeline_action_mismatch': 297, 'path_naming_convention': 204}.
   - *Recommendation:* ROUTE_SLOT (254) and REGISTER_TOOL (43) recommendations should be actioned.

5. **[HIGH]** flcr_papers_misrouted
   - 3 FLCR papers in skip audit top findings were marked MANUAL_REVIEW but heuristics suggest ROUTE_SLOT.
   - *Recommendation:* All FLCR papers (FLCR-01 through FLCR-40) should be in assembled_paper or normal_form models. Verify none are missing.

6. **[MEDIUM]** nist_peer_metadata
   - NIST legacy diff contains peer_recommendation and apply_next for each FLCR-01..40. These fields are NOT in current assembled_paper or normal_form model contracts.
   - *Recommendation:* Create a 'peer_review_metadata' sub-model or extension to capture NIST-derived peer recommendations without polluting model fit.

7. **[LOW]** nist_standards_detail
   - Each NIST record has 6 standard-level checks (claim_coverage, obligation_continuity, etc.). Current suite abstracts these into fit_score but loses granularity.
   - *Recommendation:* Consider preserving per-standard granularity as optional extensions for audit traceability.

8. **[MEDIUM]** closure_state_unverified
   - CLOSURE_INCLUSION_PASS_STATE exists but was not inspected in detail. It may contain additional records or bindings not reflected in current suite.
   - *Recommendation:* Ingest and diff against current suite if closure pass produced new records.

9. **[LOW]** unharvested_source
   - archive_crystal_queue has 6 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review ARCHIVE_HISTORY_CRYSTAL_QUEUE.json for model-mappable records.

10. **[LOW]** unharvested_source
   - flcr24_split_lane has 8 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review FLCR24_SPLIT_LANE_HUNT_REPORT.json for model-mappable records.

11. **[LOW]** unharvested_source
   - flcr24_widened has 7 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review FLCR24_WIDENED_HUNT_REPORT.json for model-mappable records.

12. **[LOW]** unharvested_source
   - legacy_repo_findings has 6 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review LEGACY_REPO_FINDINGS_ASSEMBLY.json for model-mappable records.

13. **[LOW]** unharvested_source
   - tmn_legacy_triad has 10 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review TMN_LEGACY_TRIAD_STANDARDS_GRADE.json for model-mappable records.

14. **[LOW]** unharvested_source
   - critical_connections has 13 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review CRITICAL_CONNECTIONS_REPORT.json for model-mappable records.

15. **[LOW]** unharvested_source
   - proof_chain has 12 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review PROOF_CHAIN_CONTEXT_REVIEW.json for model-mappable records.

16. **[LOW]** unharvested_source
   - paper_aggregation has 10 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review PAPER_AGGREGATION_CONTENT_SCAN.json for model-mappable records.

17. **[LOW]** unharvested_source
   - paper_content_needs has 8 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review PAPER_CONTENT_NEEDS_REPORT.json for model-mappable records.

18. **[LOW]** unharvested_source
   - obligation_rows has 10 top-level keys and may contain data not yet mapped to any model.
   - *Recommendation:* Review OBLIGATION_ROWS.json for model-mappable records.

---

## Side B — Completeness & Inclusion Review (Current Suite)

Models checked: **11** | Records audited: **442** | Findings: **3**

### Severity Breakdown
- **High:** 3

### Findings

1. **[HIGH]** low_model_fit — sm_mapping_row
   - Model 'sm_mapping_row' average fit 87.24 below 90 threshold.
   - *Recommendation:* Requires immediate remediation before any promotion.

2. **[HIGH]** zero_perfect_fit — assembled_paper
   - Model 'assembled_paper' has zero perfect-fit records.
   - *Recommendation:* Every model should have at least some perfect-fit records. Investigate model contract or data quality.

3. **[HIGH]** zero_perfect_fit — sm_mapping_row
   - Model 'sm_mapping_row' has zero perfect-fit records.
   - *Recommendation:* Every model should have at least some perfect-fit records. Investigate model contract or data quality.

---

## Unified Recommendations (All)

### High Priority
- **unresolved_blockers:** Resolve blockers or document as accepted residues. Many are CMPLX-Standards gate prerequisites.
- **high_volume_skipped:** ROUTE_SLOT (254) and REGISTER_TOOL (43) recommendations should be actioned.
- **flcr_papers_misrouted:** All FLCR papers (FLCR-01 through FLCR-40) should be in assembled_paper or normal_form models. Verify none are missing.
- **low_model_fit:** Requires immediate remediation before any promotion.
- **zero_perfect_fit:** Every model should have at least some perfect-fit records. Investigate model contract or data quality.
- **zero_perfect_fit:** Every model should have at least some perfect-fit records. Investigate model contract or data quality.

### Medium Priority
- **legacy_seed_coverage:** Promote the 7 direct_port candidates into ability_seed model after CMPLX-Standards gate validation.
- **nist_peer_metadata:** Create a 'peer_review_metadata' sub-model or extension to capture NIST-derived peer recommendations without polluting model fit.
- **closure_state_unverified:** Ingest and diff against current suite if closure pass produced new records.

### Low Priority
- **triad_octad_assemblies:** Triads/octads belong in a higher-level assembly model (not yet defined). Consider adding 'assembly_cluster' model.
- **nist_standards_detail:** Consider preserving per-standard granularity as optional extensions for audit traceability.
- **unharvested_source:** Review ARCHIVE_HISTORY_CRYSTAL_QUEUE.json for model-mappable records.
- **unharvested_source:** Review FLCR24_SPLIT_LANE_HUNT_REPORT.json for model-mappable records.
- **unharvested_source:** Review FLCR24_WIDENED_HUNT_REPORT.json for model-mappable records.
- **unharvested_source:** Review LEGACY_REPO_FINDINGS_ASSEMBLY.json for model-mappable records.
- **unharvested_source:** Review TMN_LEGACY_TRIAD_STANDARDS_GRADE.json for model-mappable records.
- **unharvested_source:** Review CRITICAL_CONNECTIONS_REPORT.json for model-mappable records.
- **unharvested_source:** Review PROOF_CHAIN_CONTEXT_REVIEW.json for model-mappable records.
- **unharvested_source:** Review PAPER_AGGREGATION_CONTENT_SCAN.json for model-mappable records.
- **unharvested_source:** Review PAPER_CONTENT_NEEDS_REPORT.json for model-mappable records.
- **unharvested_source:** Review OBLIGATION_ROWS.json for model-mappable records.

---

## Conclusion

The bipartite review confirms the current suite is structurally sound with **zero non/weak inclusive records**.
However, Side A identifies historical data (legacy seeds, skipped registry rows, NIST metadata) that should be
progressively incorporated to deepen the standards surface without destabilizing model fit.

**Next action:** Prioritize high-severity findings from Side A (blocker resolution, ROUTE_SLOT actioning) while
maintaining Side B's completeness gate.
