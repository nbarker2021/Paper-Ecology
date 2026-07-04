# FLCR-03 — Correction Surface And Residual Accounting

**Assembled paper product** — curated unified form for IRL review.

| Field | Value |
|---|---|
| Status | `ASSEMBLE` |
| Pipeline decision | `ASSEMBLE` |
| Formal source | `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-03\formal.md` |
| Evidence attached (review payload) | 778 |
| Review pass | 30 |
| CMPLX-Standards fit | 73.529412% (`partial_inclusive`) |
| Standards model | `cmplx.assembled_paper` |

## Abstract

This paper formalizes the correction surface as an exact Boolean residual between a linear radius-1 carrier and the Rule 30 target. Over GF(2), Rule 30 decomposes into Rule 90 plus the residual C and not R. The correction surface is therefore a finite syndrome-like obstruction, not an unexplained repair force and not a physical field without later calibration.

## Keywords

Rule 30; Rule 90; GF(2); residual; syndrome.

## Formal Claims

| Claim | Lane | Statement |
|-------|------|-----------|
| Theorem 3.1 | `receipt_bound_internal_result` | The Rule 30 correction surface over the binary LCR chart is exactly C and not R. |
| Proposition 3.2 | `receipt_bound_internal_result` | The left bit indexes two copies of the same obstruction because the residual condition is independent of L. |
| Protocol 3.3 | `falsifier_or_open_obligation` | Any later physical, McKay, VOA, or telemetry interpretation must consume this residual through a typed promotion lane. |

## Reviewer Claim Ledger

This ledger expands the formal-claims table into review actions. It is intended to make proof granularity explicit: what is being claimed, what evidence type can support it, what boundary remains, and what the next review action is.

| Formal row | Type | Claim in review terms | Evidence required | Boundary | Next review action |
|---|---|---|---|---|---|
| Theorem 3.1 | finite/executable result | The Rule 30 correction surface over the binary LCR chart is exactly C and not R | receipt, validator, executable pass, generated artifact, or finite enumeration | the stated finite/executable domain only | verify the receipt exists and its scope matches the claim |
| Proposition 3.2 | finite/executable result | The left bit indexes two copies of the same obstruction because the residual condition is independent of L | receipt, validator, executable pass, generated artifact, or finite enumeration | the stated finite/executable domain only | verify the receipt exists and its scope matches the claim |
| Protocol 3.3 | obligation/falsifier | Any later physical, McKay, VOA, or telemetry interpretation must consume this residual through a typed promotion lane | explicit missing derivation, adapter, receipt, dataset, comparator, or failed test condition | does not negate satisfied lower-level rows | name the next binding action and owner surface |

## Claim Granularity And Review Table

The table below separates the claim types so the paper is reviewable without accepting the whole FLCR vocabulary at once.

| Claim type | What this paper may claim | Acceptance test | What is not claimed by that row |
|---|---|---|---|
| Formal-system result | `FLCR-03` defines or uses **Correction Surface And Residual Accounting** as a typed FLCR object with declared inputs, operations, outputs, and residue. | Definitions, formal claims, construction steps, and downstream-use rules are internally consistent and lane typed. | External physical truth, measured prediction, or identity with a standard theory. |
| Computational or receipt-bound result | Enumerations, TarPit runs, CAM/crystal routes, verifier rows, and generated artifacts are claims about the stated finite or executable domain. | A named receipt, validator, manifest, pass report, or rebuild result exists and matches the row scope. | Completeness outside the enumerated domain or physical correctness outside the tested comparator. |
| Imported theorem or external definition | Imported mathematics remains an external theorem/citation target; this paper may use it only through declared mappings and conservative-extension discipline. | The source theorem, definition layer, or citation target is named and the mapping into this paper is explicit. | A new proof of the imported theorem or a hidden change in the imported object's meaning. |
| Interpretive bridge or analogy | Analog, workbook, visual, or translation language may explain why the construction is useful. | The analogy preserves the relevant structure and does not promote itself into a theorem. | That the analogy alone proves the formal, computational, or physical claim. |
| Physical or calibration-facing claim | Physical or Standard Model identity is not claimed here unless the paper contains an explicit calibration row; the default status is deferred mapping. | A dataset, citation, calibration protocol, uncertainty, comparator, or falsifier is attached. | A physical conclusion supported only by shared vocabulary rather than calibration, comparator data, or a stated falsifier. |
| Open obligation or falsifier | A missing derivation, adapter, receipt, dataset, or failed comparator is a named research channel. | The next binding action and the reason the stronger claim is not closed are stated. | That the base formal result is false merely because a stronger downstream claim remains unfinished. |

## Proof Sources And Receipt Index

| Receipt path | Source | Row-scoped | Confidence |
|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_actuation_module.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_bijection_method.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_chart_j3o_isomorphism.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_d12_action_matches_weyl_13.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_hamming_7_fano.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_j3o_axioms.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_octonionic_oloid.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_octonion_axioms.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_parameter_chain.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_powered_chain.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_three_move_closure.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_transport_obligations.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-algebra_foundation_T1_T4_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d12_idempotent_chain_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-triality_surface_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-oloid_carrier_family_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-triadic_keystone_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-atlas_unipotent_orbits_real_data_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-lattice_closure_template_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-092-chart_j3o_isomorphism_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-bijection_cold_start_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-t10_master_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_literalized_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-rule30_shell_verification_ledger_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-boundary_repair_curvature_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-error_correction_tower_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-20-layer2_synthesis_ledger_receipt.json | closure_applied | no | receipt_bound |

_… and 15 more receipt references._

### Applied closure carry (full paths)

| Receipt path | Source | Row-scoped | Confidence | Verifier |
|---|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_actuation_module.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_bijection_method.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_chart_j3o_isomorphism.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_d12_action_matches_weyl_13.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_hamming_7_fano.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_j3o_axioms.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_octonionic_oloid.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_octonion_axioms.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_parameter_chain.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_powered_chain.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_three_move_closure.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_transport_obligations.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-algebra_foundation_T1_T4_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d12_idempotent_chain_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-triality_surface_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-oloid_carrier_family_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-triadic_keystone_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-atlas_unipotent_orbits_real_data_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-lattice_closure_template_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-092-chart_j3o_isomorphism_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-bijection_cold_start_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-t10_master_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_literalized_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-rule30_shell_verification_ledger_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-boundary_repair_curvature_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-error_correction_tower_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-20-layer2_synthesis_ledger_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-hyperpermutation_audit_receipt.json | closure_applied | no | receipt_bound | PASS |

## Closure Inclusions (Carried Upward)

_Proven ASSEMBLE-validated or receipt-bound evidence queued for re-inclusion — IRL-equivalent weight in review; does not inflate ASSEMBLE without receipt closure._

| Evidence ID | Lane | Target section | Proof path | Weight |
|---|---|---|---|---|
| PEEP-2026-006 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-012 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-014 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-015 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-024 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-006 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-012 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-014 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-015 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-024 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-034 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |

## External Calibration (Candidates — Not Promoted)

| DOI | Readiness | Provenance | Confidence | Paired to formal |
|---|---|---|---|---|
| 10.25088/complexsystems.34.3.259 | nist_pass | peep_index | PASS | yes |
| 10.1063/5.0280632 | nist_pass | peep_index | PASS | yes |
| 10.1007/s00220-025-05376-5 | nist_pass | peep_index | PASS | yes |
| 10.1007/s00012-025-00908-5 | nist_pass | peep_index | PASS | yes |

### Unpaired seed DOIs

- `10.25088/ComplexSystems.34.3.259` — **candidate** (seed; not paired to formal.md)
- `10.5194/soil-7-217-2021` — **candidate** (seed; not paired to formal.md)

## Obligation Crosswalk

_No open obligations — or all receipt-bound._

## Attached Evidence Index

| Category | Count | Tier | Notes |
|---|---|---|---|
| Timeline nodes | 464 | supporting_context | Provenance graph pass5 |
| Timeline edges | 40 | supporting_context | Includes zip crosswalk |
| Registry DISCOVERY rows | 0 | supporting_context | Not promoted |
| Seed candidates | 24 | external_candidates | IRL review appendix |
| Ingress 80 records | 2 | external_candidates | Curated seeds only |
| PEEP bindings (routed) | 17 | required_direct | Includes LOCAL-GAP |
| Falsifier gaps (audit) | 17 | required_direct | From assembly audit |

## Falsifiers And Comparators

| Record | DOI | Decision | Falsifier score | Title |
|---|---|---|---|---|
| PEEP-2026-005 | 10.1063/5.0280632 | ASSEMBLE | 85 | Jordan J3(O) And Octonion Substrate As Exceptional-Jordan Comparator |
| PEEP-2026-007 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | Centroid VOA Verifier As Umbral-Moonshine Module Comparator |
| PEEP-2026-008 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | Pariah Monster Boundary As Umbral Moonshine Pariah Comparator |
| PEEP-2026-009 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | Monster Moonshine D4 Chain As Cone-VOA Module Comparator |
| PEEP-2026-010 | 10.1063/5.0280632 | ASSEMBLE | 85 | Chart J3O Isomorphism As Exceptional-Jordan Geometry Comparator |
| PEEP-2026-013 | 10.1007/s00012-025-00908-5 | ASSEMBLE | 85 | D4 J30 Idempotent Bridge Tests As Finite-Basis Semiring Comparator |
| PEEP-2026-018 | 10.25088/complexsystems.34.3.259 | ASSEMBLE | 85 | LCR Rule 30 Synthesis As CA Self-Composition Comparator |
| PEEP-2026-020 | 10.25088/complexsystems.34.3.259 | ASSEMBLE | 85 | Rule30 Prize Submission As CA Benchmark Comparator |
| PEEP-2026-021 | 10.25088/complexsystems.34.3.259 | ASSEMBLE | 85 | Rule30 Agent Outline As CA Simulation Protocol Comparator |
| PEEP-2026-022 | 10.25088/complexsystems.34.3.259 | ASSEMBLE | 85 | Rule30 Agent Final Paper As CA Evidence Comparator |
| PEEP-2026-029 | 10.25088/complexsystems.34.3.259 | ASSEMBLE | 85 | FLCR-03 Correction Surface As CA Self-Composition Comparator |
| LOCAL-GAP-0002 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-jordan-j3-octonion.md |
| LOCAL-GAP-0017 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-jordan-j3-octonion.md |
| LOCAL-GAP-0050 |  | REROUTE_OR_REPAIR | 25 | jordan_j3.py |
| LOCAL-GAP-0051 |  | REROUTE_OR_REPAIR | 25 | verify_spectre_tiling_deephole_path.json |

## Open Gaps And Blockers

_No explicit blockers — verify PEEP/NIST gates before ASSEMBLE promotion._

### Pending external pair queue

- `EQ-REG-0036` — DISCOVERY_EXTERNAL_PAIR_REQUIRED: Find 2025/current peer-reviewed external paper and promote to PEEP package.

## Seed Appendix (IRL Review)

| Seed ID | DOI | Type | Confidence | NIST readiness |
|---|---|---|---|---|
| FORM-FORM-002 | None | foundational_form | 0.7 | classical_theorem_exempt |
| CLAIM-10.5194/soil-7-217-2 | 10.5194/soil-7-217-2021 | lane_claim_queue_ingress | 0.6 | PASS |
| EXT80-03 | 10.5194/soil-7-217-2021 | ingress_80_curated_seed | 0.55 | seed_only |
| EQ-REG-0002 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0003 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0004 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0008 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0012 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0014 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0015 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0016 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0020 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| REG-0628b8 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-101807 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-68f630 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-831df4 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-97091c | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-b18c49 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-b946ff | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-ddfe2b | None | registry_discovery_external_pair | 0.45 | unscored |

_… and 4 additional seed candidates._

_Seeds are candidates only — pairing to formal.md requires NIST + receipt gates._

## Timeline And Registry Context

| Motif | Node count | Provenance |
|---|---|---|
| rule30_lineage | 345 | timeline_graph.pass5 |
| jordan_lineage | 451 | timeline_graph.pass5 |
| lattice_forge_lineage | 372 | timeline_graph.pass5 |
| moonshine_lineage | 227 | timeline_graph.pass5 |
| forge_lineage | 122 | timeline_graph.pass5 |
| hub_receipt_lineage | 51 | timeline_graph.pass5 |
| sm_bridge_lineage | 67 | timeline_graph.pass5 |

### Sample timeline nodes

- `zip_ref:Kimi_Agent_Rule30InvariantProof(2).zip` — era=origin role=zip_stratum
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\alg...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\ARC...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\ass...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference

**Adjacent band:** FLCR-01, FLCR-02, FLCR-04, FLCR-05

## CMPLX-Standards Grade

- **Model:** `cmplx.assembled_paper` v0.1.0
- **Fit score:** 73.529412% — band `partial_inclusive`
- **Distance to perfect:** 0.264706
- **Missing model fields:** `required_direct.open_obligations`, `blockers`, `assembled_section_count`, `has_proof_receipt_index`, `has_obligation_crosswalk`, `has_external_calibration`, `has_falsifiers_section`, `has_honesty_boundary`

_Standards grade measures intake completeness vs `assembled_paper_model` — not ASSEMBLE promotion._

## Honesty Boundary

Abundant intake for IRL review — candidates labeled; ASSEMBLE gates unchanged.

- Abundant intake ≠ ASSEMBLE inflation.
- Only `ASSEMBLE` pipeline status + PEEP/NIST/receipt gates permit result promotion.
- All unattached evidence retains `provenance_label` and `confidence`.

_Generated 2026-07-01T02:44:51.130111+00:00 — intake schema v1.1_
