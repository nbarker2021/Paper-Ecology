# FLCR-06 — Oloid Path Carrier And Transport Geometry

**Assembled paper product** — curated unified form for IRL review.

| Field | Value |
|---|---|
| Status | `ASSEMBLE` |
| Pipeline decision | `ASSEMBLE` |
| Formal source | `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-06\formal.md` |
| Evidence attached (review payload) | 1642 |
| Review pass | 30 |
| CMPLX-Standards fit | 73.529412% (`partial_inclusive`) |
| Standards model | `cmplx.assembled_paper` |

## Abstract

This paper defines the path carrier as a deterministic finite-state transducer. A repair row can travel as side-channel metadata while the carrier transition remains unchanged. The path theorem closes graph-continuous finite transport and payload noninterference; it does not by itself assert real oloid kinematics, gauge holonomy, or physical motion.

## Keywords

finite transducer; path carrier; payload noninterference; graph continuity; oloid.

## Formal Claims

| Claim | Lane | Statement |
|-------|------|-----------|
| Theorem 6.1 | `receipt_bound_internal_result` | The path carrier is a deterministic finite-state transducer over its declared state space. |
| Theorem 6.2 | `receipt_bound_internal_result` | Repair-row payloads are noninterfering side-channel data for the carrier transition. |
| Protocol 6.3 | `falsifier_or_open_obligation` | Physical oloid, holonomy, QCD, or mass interpretations require downstream calibration or theorem import. |

## Reviewer Claim Ledger

This ledger expands the formal-claims table into review actions. It is intended to make proof granularity explicit: what is being claimed, what evidence type can support it, what boundary remains, and what the next review action is.

| Formal row | Type | Claim in review terms | Evidence required | Boundary | Next review action |
|---|---|---|---|---|---|
| Theorem 6.1 | finite/executable result | The path carrier is a deterministic finite-state transducer over its declared state space | receipt, validator, executable pass, generated artifact, or finite enumeration | the stated finite/executable domain only | verify the receipt exists and its scope matches the claim |
| Theorem 6.2 | finite/executable result | Repair-row payloads are noninterfering side-channel data for the carrier transition | receipt, validator, executable pass, generated artifact, or finite enumeration | the stated finite/executable domain only | verify the receipt exists and its scope matches the claim |
| Protocol 6.3 | obligation/falsifier | Physical oloid, holonomy, QCD, or mass interpretations require downstream calibration or theorem import | explicit missing derivation, adapter, receipt, dataset, comparator, or failed test condition | does not negate satisfied lower-level rows | name the next binding action and owner surface |

## Claim Granularity And Review Table

The table below separates the claim types so the paper is reviewable without accepting the whole FLCR vocabulary at once.

| Claim type | What this paper may claim | Acceptance test | What is not claimed by that row |
|---|---|---|---|
| Formal-system result | `FLCR-06` defines or uses **Oloid Path Carrier And Transport Geometry** as a typed FLCR object with declared inputs, operations, outputs, and residue. | Definitions, formal claims, construction steps, and downstream-use rules are internally consistent and lane typed. | External physical truth, measured prediction, or identity with a standard theory. |
| Computational or receipt-bound result | Enumerations, TarPit runs, CAM/crystal routes, verifier rows, and generated artifacts are claims about the stated finite or executable domain. | A named receipt, validator, manifest, pass report, or rebuild result exists and matches the row scope. | Completeness outside the enumerated domain or physical correctness outside the tested comparator. |
| Imported theorem or external definition | Imported mathematics remains an external theorem/citation target; this paper may use it only through declared mappings and conservative-extension discipline. | The source theorem, definition layer, or citation target is named and the mapping into this paper is explicit. | A new proof of the imported theorem or a hidden change in the imported object's meaning. |
| Interpretive bridge or analogy | Analog, workbook, visual, or translation language may explain why the construction is useful. | The analogy preserves the relevant structure and does not promote itself into a theorem. | That the analogy alone proves the formal, computational, or physical claim. |
| Physical or calibration-facing claim | Physical or Standard Model identity is not claimed here unless the paper contains an explicit calibration row; the default status is deferred mapping. | A dataset, citation, calibration protocol, uncertainty, comparator, or falsifier is attached. | A physical conclusion supported only by shared vocabulary rather than calibration, comparator data, or a stated falsifier. |
| Open obligation or falsifier | A missing derivation, adapter, receipt, dataset, or failed comparator is a named research channel. | The next binding action and the reason the stronger claim is not closed are stated. | That the base formal result is false merely because a stronger downstream claim remains unfinished. |

## Proof Sources And Receipt Index

| Receipt path | Source | Row-scoped | Confidence |
|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_all_layers.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_all_theorems.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_chart_j3o_isomorphism.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_depth_extraction_accounting.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_extractor.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_f2_majorana.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_n3_su3_closure_exact.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_p3_weyl_engineering.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule30_chart_local_readout.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule30_predictor.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule90_linearization.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_substrate_map.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_voa_harness.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_monitor_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-algebra_foundation_T1_T4_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-su3_closure_T5_T7_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-oloid_path_carrier_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-correction_extraction_verdict_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-lucas_axis_readout_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-rule90_lucas_decomposition_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-triadic_keystone_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-07-discrete_continuous_bridge_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o2pp_registry_populated_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-u_r30_quantum_circuit_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-bijection_cold_start_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-ologn_readout_architecture_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-t10_master_receipt.json | closure_applied | no | receipt_bound |

_… and 83 more receipt references._

### Applied closure carry (full paths)

| Receipt path | Source | Row-scoped | Confidence | Verifier |
|---|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_all_layers.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_all_theorems.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_chart_j3o_isomorphism.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_depth_extraction_accounting.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_extractor.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_f2_majorana.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_n3_su3_closure_exact.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_p3_weyl_engineering.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule30_chart_local_readout.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule30_predictor.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_rule90_linearization.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_substrate_map.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_voa_harness.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_monitor_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-algebra_foundation_T1_T4_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-su3_closure_T5_T7_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-oloid_path_carrier_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-correction_extraction_verdict_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-lucas_axis_readout_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-rule90_lucas_decomposition_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-triadic_keystone_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-07-discrete_continuous_bridge_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o2pp_registry_populated_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-u_r30_quantum_circuit_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-bijection_cold_start_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-ologn_readout_architecture_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-t10_master_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-ca_prediction_surface_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-center_column_entropy_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-p2_density_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-rule30_real_dataset_experiment_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-rule30_real_dataset_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-wolfram_1m_bit_validation_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-rule30_shell_verification_ledger_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-boundary_repair_curvature_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-curvature_is_correction_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_carrier_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-16-continuum_edge_residuals_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-18-voa_moonshine_routes_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-30-rule30_corpus_provenance_receipt.json | closure_applied | no | receipt_bound | PASS |

## Closure Inclusions (Carried Upward)

_Proven ASSEMBLE-validated or receipt-bound evidence queued for re-inclusion — IRL-equivalent weight in review; does not inflate ASSEMBLE without receipt closure._

| Evidence ID | Lane | Target section | Proof path | Weight |
|---|---|---|---|---|
| PEEP-2026-003 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-013 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-018 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-020 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-029 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-013 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-018 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-020 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-029 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-034 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |

## External Calibration (Candidates — Not Promoted)

| DOI | Readiness | Provenance | Confidence | Paired to formal |
|---|---|---|---|---|
| 10.1039/D4SC07438F | nist_pass | peep_index | PASS | yes |
| 10.1007/s10817-025-09723-y | nist_pass | peep_index | PASS | yes |
| 10.1007/s00012-025-00908-5 | nist_pass | peep_index | PASS | yes |
| 10.1112/blms.13228 | nist_pass | peep_index | PASS | yes |
| 10.3390/axioms14020137 | nist_pass | peep_index | PASS | yes |
| 10.1007/s00220-025-05376-5 | nist_pass | peep_index | PASS | yes |
| 10.1039/D5DD00415B | nist_pass | peep_index | PASS | yes |
| 10.25088/ComplexSystems.34.3.259 | nist_pass | peep_index | PASS | yes |

### Unpaired seed DOIs

- `10.1002/lpor.202100003` — **candidate** (seed; not paired to formal.md)

## Obligation Crosswalk

_No open obligations — or all receipt-bound._

## Attached Evidence Index

| Category | Count | Tier | Notes |
|---|---|---|---|
| Timeline nodes | 1082 | supporting_context | Provenance graph pass5 |
| Timeline edges | 77 | supporting_context | Includes zip crosswalk |
| Registry DISCOVERY rows | 0 | supporting_context | Not promoted |
| Seed candidates | 46 | external_candidates | IRL review appendix |
| Ingress 80 records | 2 | external_candidates | Curated seeds only |
| PEEP bindings (routed) | 48 | required_direct | Includes LOCAL-GAP |
| Falsifier gaps (audit) | 46 | required_direct | From assembly audit |

## Falsifiers And Comparators

| Record | DOI | Decision | Falsifier score | Title |
|---|---|---|---|---|
| PEEP-2026-004 | 10.1007/s10817-025-09723-y | ASSEMBLE | 85 | Production Proof Receipts And Ribbon Schema As End-To-End Verification Compar... |
| PEEP-2026-006 | 10.1007/s00012-025-00908-5 | ASSEMBLE | 85 | Lattice Forge Inventory As Idempotent-Semiring Basis Comparator |
| PEEP-2026-011 | 10.1112/blms.13228 | ASSEMBLE | 85 | Umbrella Open Obligations As Idempotent-Semifield Overclaim Comparator |
| PEEP-2026-012 | 10.3390/axioms14020137 | ASSEMBLE | 85 | D12 Idempotent Chain Tests As Semicentral-Idempotent Comparator |
| PEEP-2026-014 | 10.3390/axioms14020137 | ASSEMBLE | 85 | D12 Action Verifier As Semicentral-Idempotent Action Comparator |
| PEEP-2026-015 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | D12 Moonshine Chain As Umbral Trace-Function Comparator |
| PEEP-2026-023 | 10.1112/blms.13228 | ASSEMBLE | 85 | Lattice Forge Prior Overclaim Paper As Semifield Overclaim Comparator |
| PEEP-2026-024 | 10.1007/s00012-025-00908-5 | ASSEMBLE | 85 | Lambda Rule30 Equivalence Report As Finite-Basis Equivalence Comparator |
| PEEP-2026-025 | 10.1039/D5DD00415B | ASSEMBLE | 85 | CQE CAM Crystal Database As MC3D Structure Provenance Comparator |
| PEEP-2026-038 | 10.25088/ComplexSystems.34.3.259 | ASSEMBLE | 85 | FLCR-30 Meta-Framer As CA Self-Composition Comparator |
| LOCAL-GAP-0001 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-lattice-forge-inventory.md |
| LOCAL-GAP-0003 |  | REROUTE_OR_REPAIR | 25 | verify_rule30_winding_number_proof.json |
| LOCAL-GAP-0004 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-lattice-forge-inventory.md |
| LOCAL-GAP-0008 |  | REROUTE_OR_REPAIR | 25 | verify_rule30_proof_obligations.json |
| LOCAL-GAP-0010 |  | REROUTE_OR_REPAIR | 25 | manifest.json |

## Open Gaps And Blockers

_No explicit blockers — verify PEEP/NIST gates before ASSEMBLE promotion._

### Pending external pair queue

- `EQ-REG-0039` — DISCOVERY_EXTERNAL_PAIR_REQUIRED: Find 2025/current peer-reviewed external paper and promote to PEEP package.

## Seed Appendix (IRL Review)

| Seed ID | DOI | Type | Confidence | NIST readiness |
|---|---|---|---|---|
| FORM-FORM-005 | None | foundational_form | 0.7 | classical_theorem_exempt |
| CLAIM-10.1002/lpor.2021000 | 10.1002/lpor.202100003 | lane_claim_queue_ingress | 0.6 | PASS |
| EXT80-06 | 10.1002/lpor.202100003 | ingress_80_curated_seed | 0.55 | seed_only |
| EQ-REG-0001 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0005 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0006 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0007 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0009 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0017 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0018 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0019 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0075 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| REG-00a810 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-099839 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-19ebf6 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-1b3aaa | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-39a751 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-42e30b | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-51d325 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-523b9d | None | registry_discovery_external_pair | 0.45 | unscored |

_… and 26 additional seed candidates._

_Seeds are candidates only — pairing to formal.md requires NIST + receipt gates._

## Timeline And Registry Context

| Motif | Node count | Provenance |
|---|---|---|
| rule30_lineage | 1064 | timeline_graph.pass5 |
| jordan_lineage | 341 | timeline_graph.pass5 |
| lattice_forge_lineage | 747 | timeline_graph.pass5 |
| moonshine_lineage | 390 | timeline_graph.pass5 |
| forge_lineage | 253 | timeline_graph.pass5 |
| hub_receipt_lineage | 92 | timeline_graph.pass5 |
| sm_bridge_lineage | 137 | timeline_graph.pass5 |

### Sample timeline nodes

- `zip_ref:Kimi_Agent_Rule30InvariantProof(2).zip` — era=origin role=zip_stratum
- `zip_ref:Barker_Rule30_Market_Engine.zip` — era=bridge role=zip_stratum
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\alg...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\ARC...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\ass...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference
- `D:\CQE_CMPLX\kernel\staging\papers\suite82_historical_pastworks\Bar...` — era=bridge role=bridge_reference

**Adjacent band:** FLCR-04, FLCR-05, FLCR-07, FLCR-08

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

_Generated 2026-07-01T02:44:51.260331+00:00 — intake schema v1.1_
