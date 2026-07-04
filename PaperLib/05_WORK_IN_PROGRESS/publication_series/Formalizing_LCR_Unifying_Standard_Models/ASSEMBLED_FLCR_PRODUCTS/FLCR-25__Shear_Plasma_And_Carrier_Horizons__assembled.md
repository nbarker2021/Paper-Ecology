# FLCR-25 — Shear, Plasma, And Carrier Horizons

**Assembled paper product** — publication-grade unified form (ASSEMBLE fulfilled).

| Field | Value |
|---|---|
| Status | `ASSEMBLE` |
| Guardrail tier | `assemble_clean` |
| ASSEMBLE fulfilled | yes |
| Pipeline decision | `ASSEMBLE` |
| Formal source | `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-25\formal.md` |
| Evidence attached (review payload) | 878 |
| Review pass | 33 |
| CMPLX-Standards fit | 73.529412% (`partial_inclusive`) |
| Standards model | `cmplx.assembled_paper` |

## Abstract

This paper formalizes shear and horizon events as carrier-level thresholds. The operative object is carrier horizon. The core result is that pinch, shear, and horizon conditions can be represented as internal carrier threshold events. The paper also defines how this result routes forward: FLCR-37 may use these thresholds for plasma/energy translation after measurement binding. Its main residue is explicit: measured Z-pinch observables, plasma identity, and laboratory calibration remain external.

## Keywords

carrier horizon; LCR; receipt; claim lane; normal form.

## Formal Claims

| Claim | Lane | Statement |
|-------|------|-----------|
| Theorem 25.1 | `cam_crystal_reapplication_result` | pinch, shear, and horizon conditions can be represented as internal carrier threshold events |
| Proposition 25.2 | `normal_form_result` | carrier horizon can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 25.3 | `falsifier_or_open_obligation` | measured Z-pinch observables, plasma identity, and laboratory calibration remain external |

## Reviewer Claim Ledger

This ledger expands the formal-claims table into review actions. It is intended to make proof granularity explicit: what is being claimed, what evidence type can support it, what boundary remains, and what the next review action is.

| Formal row | Type | Claim in review terms | Evidence required | Boundary | Next review action |
|---|---|---|---|---|---|
| Theorem 25.1 | CAM route | pinch, shear, and horizon conditions can be represented as internal carrier threshold events | CAM/crystal route, source node, projection, window, or addressable evidence artifact | routing and reapplication evidence; not a standalone physical proof | check the CAM source, route, and attached data are named |
| Proposition 25.2 | formal construction | carrier horizon can be imported by later papers only through its declared source, receipt, and lane | definitions, normal-form construction, conversion rule, and downstream-use boundary | internal formal coherence; no measured physical identity without a separate calibration row | check that the normal form is named and the conversion rule is explicit |
| Protocol 25.3 | obligation/falsifier | measured Z-pinch observables, plasma identity, and laboratory calibration remain external | explicit missing derivation, adapter, receipt, dataset, comparator, or failed test condition | does not negate satisfied lower-level rows | name the next binding action and owner surface |

## Claim Granularity And Review Table

The table below separates the claim types so the paper is reviewable without accepting the whole FLCR vocabulary at once.

| Claim type | What this paper may claim | Acceptance test | What is not claimed by that row |
|---|---|---|---|
| Formal-system result | `FLCR-25` defines or uses **Shear, Plasma, And Carrier Horizons** as a typed FLCR object with declared inputs, operations, outputs, and residue. | Definitions, formal claims, construction steps, and downstream-use rules are internally consistent and lane typed. | External physical truth, measured prediction, or identity with a standard theory. |
| Computational or receipt-bound result | Enumerations, TarPit runs, CAM/crystal routes, verifier rows, and generated artifacts are claims about the stated finite or executable domain. | A named receipt, validator, manifest, pass report, or rebuild result exists and matches the row scope. | Completeness outside the enumerated domain or physical correctness outside the tested comparator. |
| Imported theorem or external definition | Imported mathematics remains an external theorem/citation target; this paper may use it only through declared mappings and conservative-extension discipline. | The source theorem, definition layer, or citation target is named and the mapping into this paper is explicit. | A new proof of the imported theorem or a hidden change in the imported object's meaning. |
| Interpretive bridge or analogy | Analog, workbook, visual, or translation language may explain why the construction is useful. | The analogy preserves the relevant structure and does not promote itself into a theorem. | That the analogy alone proves the formal, computational, or physical claim. |
| Physical or calibration-facing claim | Physical or Standard Model identity is not claimed here unless the paper contains an explicit calibration row; the default status is deferred mapping. | A dataset, citation, calibration protocol, uncertainty, comparator, or falsifier is attached. | A physical conclusion supported only by shared vocabulary rather than calibration, comparator data, or a stated falsifier. |
| Open obligation or falsifier | A missing derivation, adapter, receipt, dataset, or failed comparator is a named research channel. | The next binding action and the reason the stronger claim is not closed are stated. | That the base formal result is false merely because a stronger downstream claim remains unfinished. |

## Proof Sources And Receipt Index

| Receipt path | Source | Row-scoped | Confidence |
|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d4_atlas_bijectivity_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-atlas_unipotent_orbits_real_data_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-e8_even_lattice_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-niemeier_leech_enumeration_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o1_weyl_e8_construction_closed_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o2pp_registry_populated_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o7_niemeier_e8cubed_glue_closed_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-hamiltonian_window_emergence_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-rule30_shell_verification_ledger_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-boundary_repair_curvature_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-golay_leech_tower_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-leech_kissing_published_decomposition_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-18-voa_moonshine_routes_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-19-observer_face_selection_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-27-waveform_collapse_mechanism_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-30-rule30_corpus_provenance_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-alena_morph_e8_kit_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-e8_routed_constructor_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-octad_e8_structure_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-p120_e8_cayley_dickson_doubling_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\kernel\staging\papers\suite81_claude_codex_memory\CX-NotebookLM\CX_CADForge_Demo_Export\wireblock_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-field_form_membership_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-number_is_ribbon_digital_root_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-bijective_shell2_doublet_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-lcr_carrier_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-o8_spinor_double_cover_closed_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_monitor_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_receipt.json | closure_applied | no | receipt_bound |

_… and 93 more receipt references._

### Applied closure carry (full paths)

| Receipt path | Source | Row-scoped | Confidence | Verifier |
|---|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d4_atlas_bijectivity_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-atlas_unipotent_orbits_real_data_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-e8_even_lattice_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-niemeier_leech_enumeration_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o1_weyl_e8_construction_closed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o2pp_registry_populated_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-o7_niemeier_e8cubed_glue_closed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-hamiltonian_window_emergence_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-rule30_shell_verification_ledger_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-boundary_repair_curvature_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-golay_leech_tower_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-leech_kissing_published_decomposition_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-18-voa_moonshine_routes_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-19-observer_face_selection_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-27-waveform_collapse_mechanism_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-30-rule30_corpus_provenance_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-alena_morph_e8_kit_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-e8_routed_constructor_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-octad_e8_structure_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-p120_e8_cayley_dickson_doubling_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\kernel\staging\papers\suite81_claude_codex_memory\CX-NotebookLM\CX_CADForge_Demo_Export\wireblock_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-field_form_membership_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-number_is_ribbon_digital_root_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-bijective_shell2_doublet_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-lcr_carrier_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-o8_spinor_double_cover_closed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_monitor_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-02-correction_surface_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-algebra_foundation_T1_T4_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d12_idempotent_chain_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d4_block_tower_exceptional_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-su3_closure_T5_T7_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-triality_annealing_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-triality_surface_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-04-boundary_repair_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-cd_conjugation_gluon_oloid_theta0_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-gluon_oloid_worldline_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-oloid_carrier_family_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-05-oloid_path_carrier_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-causal_code_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-correction_extraction_verdict_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-lucas_axis_readout_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-rule90_lucas_decomposition_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-triadic_keystone_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-07-discrete_continuous_bridge_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-07-mdhg_speedlight_bridge_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-07-o3_universality_closed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-e8_hemisphere_partition_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-f2_bridge_unipotent_substrate_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-lattice_closure_template_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-lattice_code_chain_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-lattice_code_closure_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-t8_commutability_tree_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-kappa_conservation_law_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-u_r30_quantum_circuit_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-092-chart_j3o_isomorphism_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-094-spectre_7fold_substitution_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-bijection_cold_start_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-ologn_readout_architecture_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-t10_master_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-100-completion_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-100-hyperpermutation_fixedpoint_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-11-sporadic_admission_boundary_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-11-theory_admission_gate_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-ca_prediction_surface_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-center_column_entropy_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-p1_non_periodicity_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-p2_density_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-rule30_real_dataset_experiment_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-rule30_real_dataset_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-12-wolfram_1m_bit_validation_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-invariant_transfer_su2u1_in_su3_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_literalized_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-quark_face_transport_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-13-standard_model_real_comparison_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-14-curvature_is_correction_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-eight_states_one_dual_reading_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_framing_2x2x2_vs_3x3_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_gravity_drive_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_carrier_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-mass_residue_literalized_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-15-ninth_is_forced_printout_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-16-continuum_edge_residuals_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-17-error_correction_tower_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-18-centroid_voa_chain_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-19-observation_is_face_selection_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-20-layer2_synthesis_ledger_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-20-solution_ledger_affirmed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-21-agrm_golden_sweep_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-25-energy_ledger_affirmed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-26-pinch_driven_roll_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-28-conway_glider_oloid_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-28-glider_collision_cascade_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-28-gosper_gun_emitter_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-28-ndim_knight_ca_affirmed_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-lmfdb_moonshine_anchor_real_data_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-monster_internal_map_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-moonshine_real_data_experiment_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-29-supersingular_prime_ceiling_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-43200_pyramid_structure_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-higher_order_superperm_manager_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-houston_872_attempt_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-hyperpermutation_audit_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-lcr_superperm_handbuild_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-32-n6_871_reduction_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-formal-PH3-gluon_aliasing_illusion_receipt.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\production-formal-papers-CQE-paper-13-ckm_calibration_receipt.json | closure_applied | no | receipt_bound | PASS |

## Closure Inclusions (Carried Upward)

_No closure inclusions queued for this slot._

## External Calibration

| DOI | Readiness | Provenance | Confidence | Paired to formal |
|---|---|---|---|---|
| 10.1103/z8g6-9j25 | nist_pass | peep_index | PASS | yes |

### Unpaired seed DOIs

- `10.1007/s11018-025-02433-2` — seed reference (not primary paired DOI)
- `10.1038/s41467-020-17912-z` — seed reference (not primary paired DOI)

## Obligation Crosswalk

| Obligation ID | Section | Status | Evidence needed | Claim (excerpt) |
|---|---|---|---|---|
| FLCR-25-OBL-001 | §4 Formal Claims / Theorem 25.1 | derived_pending_receipt | cam_crystal_reapplication_result | Pinch, shear, and horizon conditions can be represented as internal carrier threshold events. |
| FLCR-25-OBL-002 | §4 Formal Claims / Proposition 25.2 | derived_pending_receipt | normal_form_result | Carrier horizon can be imported by later papers only through declared source, receipt, and lane. |
| FLCR-25-OBL-003 | §4 Formal Claims / Protocol 25.3 | staged_open | falsifier_or_open_obligation | Measured Z-pinch observables, plasma identity, and laboratory calibration remain external. |
| FLCR-25-OBL-004 | Claim Binding Queue / Symbolic Carrie... | staged_open | external_calibration_result | Map every physical carrier phrase to standard physics object, Hamiltonian/model, dataset, or cali... |
| FLCR-25-OBL-005 | Slot 25 CKM comparator (deferred Phas... | staged_open | external_calibration_result | CKM unitarity/alpha review comparator deferred; PEEP-017 transport lane only per CAR-ROUTE-017 sl... |
| FLCR-25-OBL-006 | Acceptance Blockers | staged_open | standard_theorem_citation_bound_result | Final citations and receipt identifiers must be attached before reviewer acceptance. |
| FLCR-25-OBL-007 | Acceptance Blockers | staged_open | falsifier_or_open_obligation | Proof sketch must be promoted into formal proof or labeled construction argument. |
| FLCR-25-OBL-008 | Source-Backed Evidence / CQE-paper-26 | derived_pending_receipt | receipt_bound_internal_result | Z-pinch/shear physics map at carrier layer; physical Z-pinch reading not discharged without calib... |
| FLCR-25-OBL-009 | Slot 25 partial wiring (Phase 12) | staged_open | external_calibration_result | PEEP-017 quasicrystal transport comparator reuse; no new external comparator; CKM deferred. |
| FLCR-25-OBL-010 | Major Revision Requests | staged_open | standard_theorem_citation_bound_result | Replace placeholder source classes with receipt hashes or dataset identifiers. |
| FLCR-25-OBL-011 | §9 Limitations And Falsifiers | staged_open | falsifier_or_open_obligation | Internal carrier threshold events do not imply measured Z-pinch observables. |
| FLCR-25-OBL-012 | State-Bound Proof Contract | derived_pending_receipt | receipt_bound_internal_result | Bind state from slot 25 reopened at slot 26 with pinch/shear receipt replay. |
| FLCR-25-OBL-013 | Publication Readiness Tasks | staged_open | receipt_bound_internal_result | Validator identities and receipt hashes recorded in manifest or receipt appendix. |
| FLCR-25-OBL-014 | Worked Example / FLCR-25-T3 | derived_pending_receipt | receipt_bound_internal_result | Workbook replay must demonstrate carrier horizon readout with named falsifier per claim lane. |
| FLCR-25-OBL-001 | §4 Formal Claims / Theorem 25.1 | derived_pending_receipt | cam_crystal_reapplication_result | Pinch, shear, and horizon conditions can be represented as internal carrier threshold events. |
| FLCR-25-OBL-002 | §4 Formal Claims / Proposition 25.2 | derived_pending_receipt | normal_form_result | Carrier horizon can be imported by later papers only through declared source, receipt, and lane. |
| FLCR-25-OBL-003 | §4 Formal Claims / Protocol 25.3 | staged_open | falsifier_or_open_obligation | Measured Z-pinch observables, plasma identity, and laboratory calibration remain external. |
| FLCR-25-OBL-004 | Claim Binding Queue / Symbolic Carrie... | staged_open | external_calibration_result | Map every physical carrier phrase to standard physics object, Hamiltonian/model, dataset, or cali... |
| FLCR-25-OBL-005 | Slot 25 CKM comparator (deferred Phas... | staged_open | external_calibration_result | CKM unitarity/alpha review comparator deferred; PEEP-017 transport lane only per CAR-ROUTE-017 sl... |
| FLCR-25-OBL-006 | Acceptance Blockers | staged_open | standard_theorem_citation_bound_result | Final citations and receipt identifiers must be attached before reviewer acceptance. |
| FLCR-25-OBL-007 | Acceptance Blockers | staged_open | falsifier_or_open_obligation | Proof sketch must be promoted into formal proof or labeled construction argument. |
| FLCR-25-OBL-008 | Source-Backed Evidence / CQE-paper-26 | derived_pending_receipt | receipt_bound_internal_result | Z-pinch/shear physics map at carrier layer; physical Z-pinch reading not discharged without calib... |
| FLCR-25-OBL-009 | Slot 25 partial wiring (Phase 12) | staged_open | external_calibration_result | PEEP-017 quasicrystal transport comparator reuse; no new external comparator; CKM deferred. |
| FLCR-25-OBL-010 | Major Revision Requests | staged_open | standard_theorem_citation_bound_result | Replace placeholder source classes with receipt hashes or dataset identifiers. |
| FLCR-25-OBL-011 | §9 Limitations And Falsifiers | staged_open | falsifier_or_open_obligation | Internal carrier threshold events do not imply measured Z-pinch observables. |

_… and 45 open obligations._

## Attached Evidence Index

| Category | Count | Tier | Notes |
|---|---|---|---|
| Timeline nodes | 169 | supporting_context | Provenance graph pass5 |
| Timeline edges | 12 | supporting_context | Includes zip crosswalk |
| Registry DISCOVERY rows | 0 | supporting_context | Context only |
| Seed candidates | 4 | external_candidates | IRL review appendix |
| Ingress 80 records | 2 | external_candidates | Curated seeds only |
| PEEP bindings (routed) | 25 | required_direct | Includes LOCAL-GAP |
| Falsifier gaps (audit) | 25 | required_direct | From assembly audit |

## Falsifiers And Comparators

| Record | DOI | Decision | Falsifier score | Title |
|---|---|---|---|---|
| PEEP-2026-034 | 10.1103/z8g6-9j25 | ASSEMBLE | 85 | FLCR-25 Carrier Horizon As CKM Unitarity Comparator |
| LOCAL-GAP-0001 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-lattice-forge-inventory.md |
| LOCAL-GAP-0002 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-jordan-j3-octonion.md |
| LOCAL-GAP-0007 |  | REROUTE_OR_REPAIR | 25 | CQE-paper-29-monster_energy_bound_hypotheses_receipt.json |
| LOCAL-GAP-0010 |  | REROUTE_OR_REPAIR | 25 | manifest.json |
| LOCAL-GAP-0012 |  | REROUTE_OR_REPAIR | 25 | rule30.py |
| LOCAL-GAP-0013 |  | REROUTE_OR_REPAIR | 25 | centroid_voa.py |
| LOCAL-GAP-0014 |  | REROUTE_OR_REPAIR | 25 | centroid_voa.py |
| LOCAL-GAP-0015 |  | REROUTE_OR_REPAIR | 25 | CQE-paper-22-metaforge_materials_receipt.json |
| LOCAL-GAP-0017 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-jordan-j3-octonion.md |
| LOCAL-GAP-0018 |  | REROUTE_OR_REPAIR | 25 | verify_rg_thresholds_from_e8_shear_complement.json |
| LOCAL-GAP-0021 |  | REROUTE_OR_REPAIR | 25 | contribution_validators.py |
| LOCAL-GAP-0023 |  | REROUTE_OR_REPAIR | 25 | verify_alpha_em_from_pfc2_e8_estimate.json |
| LOCAL-GAP-0040 |  | REROUTE_OR_REPAIR | 25 | verify_voa_sector_decomposition.json |
| LOCAL-GAP-0041 |  | REROUTE_OR_REPAIR | 25 | verify_centroid_voa_chain.json |

## Open Gaps (Substantive Only)

_No assembly-stage blockers — substantive obligation/falsifier rows listed above if open._

### Pending external pair queue

- `EQ-REG-0058` — DISCOVERY_EXTERNAL_PAIR_REQUIRED: Find 2025/current peer-reviewed external paper and promote to PEEP package.

## Seed Appendix (IRL Review)

| Seed ID | DOI | Type | Confidence | NIST readiness |
|---|---|---|---|---|
| CAND-Q-09 | 10.1007/s11018-025-02433-2 | external_pairing_candidate_queue | 0.85 | ready_if_unpaired |
| CLAIM-10.1038/s41467-020-1 | 10.1038/s41467-020-17912-z | lane_claim_queue_ingress | 0.6 | PASS |
| EXT80-25 | 10.1038/s41467-020-17912-z | ingress_80_curated_seed | 0.55 | seed_only |
| CAND-Q-08 | 10.1103/z8g6-9j25 | external_pairing_candidate_queue | 0.4 | promoted_or_bound |

## Timeline And Registry Context

| Motif | Node count | Provenance |
|---|---|---|
| rule30_lineage | 107 | timeline_graph.pass5 |
| jordan_lineage | 50 | timeline_graph.pass5 |
| lattice_forge_lineage | 154 | timeline_graph.pass5 |
| moonshine_lineage | 56 | timeline_graph.pass5 |
| forge_lineage | 50 | timeline_graph.pass5 |
| hub_receipt_lineage | 4 | timeline_graph.pass5 |
| sm_bridge_lineage | 8 | timeline_graph.pass5 |

### Sample timeline nodes

- `D:\CQE_CMPLX\CMPLX-R30-main\DATA\cache\reverse-atlas-projected-rule...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\DATA\cache\reverse-atlas-rule30-center-...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\DATA\wolfram-rule30-center\manifest.json` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\extended_memory\manifest.json` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\centroid_voa.py` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\contributions_r...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\contribution_va...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\cqe_rule30_solv...` — era=bridge role=bridge_reference

**Adjacent band:** FLCR-23, FLCR-24, FLCR-26, FLCR-27

## CMPLX-Standards Grade

- **Model:** `cmplx.assembled_paper` v0.1.0
- **Fit score:** 73.529412% — band `partial_inclusive`
- **Distance to perfect:** 0.264706
- **Missing model fields:** `closure_inclusions`, `blockers`, `assembled_section_count`, `has_proof_receipt_index`, `has_obligation_crosswalk`, `has_external_calibration`, `has_falsifiers_section`, `has_honesty_boundary`

## Assembly Certification


ASSEMBLE-fulfilled product — publication-grade unified form; substantive open obligations and falsifier rows retained where genuinely open.

- ASSEMBLE gates satisfied for this slot.
- Unattached evidence retains `provenance_label` and `confidence`.
- Open obligation rows and falsifier gaps above remain honest carry-forward items.

_Generated 2026-07-01T06:22:55.693827+00:00 — intake schema v1.2_
