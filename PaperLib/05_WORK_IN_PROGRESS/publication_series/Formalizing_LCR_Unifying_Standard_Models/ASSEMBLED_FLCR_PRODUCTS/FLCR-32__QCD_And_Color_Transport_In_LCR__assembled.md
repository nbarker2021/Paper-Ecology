# FLCR-32 — QCD And Color Transport In LCR

**Assembled paper product** — publication-grade unified form (ASSEMBLE fulfilled).

| Field | Value |
|---|---|
| Status | `ASSEMBLE` |
| Guardrail tier | `assemble_clean` |
| ASSEMBLE fulfilled | yes |
| Pipeline decision | `ASSEMBLE` |
| Formal source | `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-32\formal.md` |
| Evidence attached (review payload) | 751 |
| Review pass | 33 |
| CMPLX-Standards fit | 73.529412% (`partial_inclusive`) |
| Standards model | `cmplx.assembled_paper` |

## Abstract

This paper formalizes QCD/color language as a translation of finite face transport. The operative object is QCD color translation. The core result is that finite six-face transport can support a QCD-facing translation only with explicit scope separating structural color from measured QCD. The paper also defines how this result routes forward: FLCR-32 cites FLCR-14 before making any color-transport claim. Its main residue is explicit: physical quark confinement, CKM, and measured QCD parameters remain external calibration.

## Keywords

QCD color translation; LCR; receipt; claim lane; normal form.

## Formal Claims

| Claim | Lane | Statement |
|-------|------|-----------|
| Theorem 32.1 | `standard_theorem_citation_bound_result` | finite six-face transport can support a QCD-facing translation only with explicit scope separating structural color from measured QCD |
| Proposition 32.2 | `normal_form_result` | QCD color translation can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 32.3 | `falsifier_or_open_obligation` | physical quark confinement, CKM, and measured QCD parameters remain external calibration |

## Reviewer Claim Ledger

This ledger expands the formal-claims table into review actions. It is intended to make proof granularity explicit: what is being claimed, what evidence type can support it, what boundary remains, and what the next review action is.

| Formal row | Type | Claim in review terms | Evidence required | Boundary | Next review action |
|---|---|---|---|---|---|
| Theorem 32.1 | external target or comparator | finite six-face transport can support a QCD-facing translation only with explicit scope separating structural color from measured QCD | named external theorem, definition layer, citation target, or imported standard formalism | imports the external object as-is; does not silently reprove or redefine it | attach final citation metadata and mapping rule |
| Proposition 32.2 | translation grammar | QCD color translation can be imported by later papers only through its declared source, receipt, and lane | definitions, normal-form construction, conversion rule, and downstream-use boundary | internal formal coherence; no measured physical identity without a separate calibration row | check that the normal form is named and the conversion rule is explicit |
| Protocol 32.3 | obligation/falsifier | physical quark confinement, CKM, and measured QCD parameters remain external calibration | explicit missing derivation, adapter, receipt, dataset, comparator, or failed test condition | does not negate satisfied lower-level rows | name the next binding action and owner surface |

## Claim Granularity And Review Table

The table below separates the claim types so the paper is reviewable without accepting the whole FLCR vocabulary at once.

| Claim type | What this paper may claim | Acceptance test | What is not claimed by that row |
|---|---|---|---|
| Formal-system result | `FLCR-32` defines or uses **QCD And Color Transport In LCR** as a typed FLCR object with declared inputs, operations, outputs, and residue. | Definitions, formal claims, construction steps, and downstream-use rules are internally consistent and lane typed. | External physical truth, measured prediction, or identity with a standard theory. |
| Computational or receipt-bound result | Enumerations, TarPit runs, CAM/crystal routes, verifier rows, and generated artifacts are claims about the stated finite or executable domain. | A named receipt, validator, manifest, pass report, or rebuild result exists and matches the row scope. | Completeness outside the enumerated domain or physical correctness outside the tested comparator. |
| Imported theorem or external definition | The Standard Model or adjacent physics object is closed only as an external target definition when the relevant definition/citation row is present. | The source theorem, definition layer, or citation target is named and the mapping into this paper is explicit. | A new proof of the imported theorem or a hidden change in the imported object's meaning. |
| Interpretive bridge or analogy | Analog, workbook, visual, or translation language may explain why the construction is useful. | The analogy preserves the relevant structure and does not promote itself into a theorem. | That the analogy alone proves the formal, computational, or physical claim. |
| Physical or calibration-facing claim | Measured values, physical identity, and predictive accuracy require scale, units, dataset, uncertainty, comparator, and pass/fail criteria. | A dataset, citation, calibration protocol, uncertainty, comparator, or falsifier is attached. | A physical conclusion supported only by shared vocabulary rather than calibration, comparator data, or a stated falsifier. |
| Open obligation or falsifier | A missing derivation, adapter, receipt, dataset, or failed comparator is a named research channel. | The next binding action and the reason the stronger claim is not closed are stated. | That the base formal result is false merely because a stronger downstream claim remains unfinished. |

## Proof Sources And Receipt Index

| Receipt path | Source | Row-scoped | Confidence |
|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-gluon_oloid_worldline_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-invariant_transfer_su2u1_in_su3_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-standard_model_real_comparison_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_carrier_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_literalized_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-monster_internal_map_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_sm_anomaly_cancellation_from_charge_table.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_sm_charge_table_from_su5_embedding.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_sm_charge_table_from_u1_su2_su3.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_su5_observer_decomposition.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_su5_spin_state_interface.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\kernel\staging\papers\suite18_cl_paper_db\CL_production-proof-re... | timeline_node | no | referenced |
| D:\CQE_CMPLX\kernel\staging\papers\suite81_claude_codex_memory\Claude work\CL... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-bo... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-22-me... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-25-ph... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-26-zp... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-mo... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\production-form... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_coupling... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_nbody_3_... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_observer... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_rg_flow_... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_rg_thres... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_spectre_... | timeline_node | no | referenced |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_standard... | timeline_node | no | referenced |
| quark_face_transport_literalized_receipt.json | formal_md | no | referenced |
| quark_face_transport_receipt.json | formal_md | no | referenced |

### Applied closure carry (full paths)

| Receipt path | Source | Row-scoped | Confidence | Verifier |
|---|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-gluon_oloid_worldline_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-invariant_transfer_su2u1_in_su3_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-standard_model_real_comparison_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_carrier_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_literalized_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-monster_internal_map_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_sm_anomaly_cancellation_from_charge_table.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_sm_charge_table_from_su5_embedding.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_sm_charge_table_from_u1_su2_su3.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_su5_observer_decomposition.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_su5_spin_state_interface.json | closure_applied | no | receipt_bound | PASS |

## Closure Inclusions (Carried Upward)

_Receipt-bound evidence carried upward from closure passes — included in assembled product index._

| Evidence ID | Lane | Target section | Proof path | Weight |
|---|---|---|---|---|
| PEEP-2026-006 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-012 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-013 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-015 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-018 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-024 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |

## External Calibration

| DOI | Readiness | Provenance | Confidence | Paired to formal |
|---|---|---|---|---|
| 10.1112/blms.13228 | nist_pass | peep_index | PASS | yes |

### Unpaired seed DOIs

- `10.1038/s41467-025-61209-y` — seed reference (not primary paired DOI)
- `10.1103/physrevc.103.054904` — seed reference (not primary paired DOI)

## Obligation Crosswalk

_No open obligations — or all receipt-bound._

## Attached Evidence Index

| Category | Count | Tier | Notes |
|---|---|---|---|
| Timeline nodes | 314 | supporting_context | Provenance graph pass5 |
| Timeline edges | 287 | supporting_context | Includes zip crosswalk |
| Registry DISCOVERY rows | 0 | supporting_context | Context only |
| Seed candidates | 6 | external_candidates | IRL review appendix |
| Ingress 80 records | 2 | external_candidates | Curated seeds only |
| PEEP bindings (routed) | 8 | required_direct | Includes LOCAL-GAP |
| Falsifier gaps (audit) | 8 | required_direct | From assembly audit |

## Falsifiers And Comparators

| Record | DOI | Decision | Falsifier score | Title |
|---|---|---|---|---|
| PEEP-2026-011 | 10.1112/blms.13228 | ASSEMBLE | 85 | Umbrella Open Obligations As Idempotent-Semifield Overclaim Comparator |
| LOCAL-GAP-0007 |  | REROUTE_OR_REPAIR | 25 | CQE-paper-29-monster_energy_bound_hypotheses_receipt.json |
| LOCAL-GAP-0011 |  | REROUTE_OR_REPAIR | 25 | verify_rule30_whole_integer_n_coverage.json |
| LOCAL-GAP-0015 |  | REROUTE_OR_REPAIR | 25 | CQE-paper-22-metaforge_materials_receipt.json |
| LOCAL-GAP-0018 |  | REROUTE_OR_REPAIR | 25 | verify_rg_thresholds_from_e8_shear_complement.json |
| LOCAL-GAP-0051 |  | REROUTE_OR_REPAIR | 25 | verify_spectre_tiling_deephole_path.json |
| LOCAL-GAP-0056 |  | REROUTE_OR_REPAIR | 25 | verify_su5_observer_decomposition.json |
| LOCAL-GAP-0057 |  | REROUTE_OR_REPAIR | 25 | verify_observer_post_su3_electroweak_route.json |

## Open Gaps (Substantive Only)

_No assembly-stage blockers — substantive obligation/falsifier rows listed above if open._

### Pending external pair queue

- `EQ-REG-0065` — DISCOVERY_EXTERNAL_PAIR_REQUIRED: Find 2025/current peer-reviewed external paper and promote to PEEP package.

## Seed Appendix (IRL Review)

| Seed ID | DOI | Type | Confidence | NIST readiness |
|---|---|---|---|---|
| CAND-Q-12 | 10.1038/s41467-025-61209-y | external_pairing_candidate_queue | 0.85 | ready_if_unpaired |
| CLAIM-10.1103/physrevc.103 | 10.1103/physrevc.103.054904 | lane_claim_queue_ingress | 0.6 | PASS |
| EXT80-32 | 10.1103/physrevc.103.054904 | ingress_80_curated_seed | 0.55 | seed_only |
| EQ-REG-0005 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| REG-348193 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-aca850 | None | registry_discovery_external_pair | 0.45 | unscored |

## Timeline And Registry Context

| Motif | Node count | Provenance |
|---|---|---|
| rule30_lineage | 134 | timeline_graph.pass5 |
| jordan_lineage | 57 | timeline_graph.pass5 |
| lattice_forge_lineage | 173 | timeline_graph.pass5 |
| moonshine_lineage | 128 | timeline_graph.pass5 |
| forge_lineage | 81 | timeline_graph.pass5 |
| hub_receipt_lineage | 101 | timeline_graph.pass5 |
| sm_bridge_lineage | 307 | timeline_graph.pass5 |

### Sample timeline nodes

- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\epi...` — era=pre-formal role=zip_stratum
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\fri...` — era=pre-formal role=zip_stratum
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\his...` — era=pre-formal role=zip_stratum
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\sta...` — era=pre-formal role=zip_stratum
- `D:\CQE_CMPLX\CMPLX-R30-main\CATALOG\porting_context_catalog.md` — era=origin role=zip_stratum
- `D:\CQE_CMPLX\CMPLX-R30-main\DISCLOSURES\OPEN_OBLIGATIONS_SUMMARY.md` — era=origin role=zip_stratum
- `D:\CQE_CMPLX\CMPLX-R30-main\FORMALIZATION\SESSION3_SOURCE_GROUNDED_...` — era=origin role=zip_stratum
- `D:\CQE_CMPLX\CMPLX-R30-main\scripts\unify_claim_umbrellas.py` — era=origin role=source_truth

**Adjacent band:** FLCR-30, FLCR-31, FLCR-33, FLCR-34

## CMPLX-Standards Grade

- **Model:** `cmplx.assembled_paper` v0.1.0
- **Fit score:** 73.529412% — band `partial_inclusive`
- **Distance to perfect:** 0.264706
- **Missing model fields:** `required_direct.open_obligations`, `blockers`, `assembled_section_count`, `has_proof_receipt_index`, `has_obligation_crosswalk`, `has_external_calibration`, `has_falsifiers_section`, `has_honesty_boundary`

## Assembly Certification


ASSEMBLE-fulfilled product — publication-grade unified form; substantive open obligations and falsifier rows retained where genuinely open.

- ASSEMBLE gates satisfied for this slot.
- Unattached evidence retains `provenance_label` and `confidence`.
- Open obligation rows and falsifier gaps above remain honest carry-forward items.

_Generated 2026-07-01T06:22:56.010186+00:00 — intake schema v1.2_
