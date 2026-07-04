# FLCR-13 — Cellular Automata Prediction Surfaces

**Assembled paper product** — curated unified form for IRL review.

| Field | Value |
|---|---|
| Status | `ASSEMBLE` |
| Pipeline decision | `ASSEMBLE` |
| Formal source | `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-13\formal.md` |
| Evidence attached (review payload) | 938 |
| Review pass | 30 |
| CMPLX-Standards fit | 73.529412% (`partial_inclusive`) |
| Standards model | `cmplx.assembled_paper` |

## Abstract

This paper formalizes bounded prediction surfaces for elementary cellular automata. The operative object is CA prediction surface. The core result is that finite and bounded CA readouts can be receipt-closed without claiming unbounded Rule 30 future-bit extraction. The paper also defines how this result routes forward: finite surfaces feed admission, window, and falsifier papers as testable local machines. Its main residue is explicit: unbounded nonperiodicity, cold nth-bit extraction, and full prediction remain separate mathematical obligations.

## Keywords

CA prediction surface; LCR; receipt; claim lane; normal form.

## Formal Claims

| Claim | Lane | Statement |
|-------|------|-----------|
| Theorem 13.1 | `receipt_bound_internal_result` | finite and bounded CA readouts can be receipt-closed without claiming unbounded Rule 30 future-bit extraction |
| Proposition 13.2 | `normal_form_result` | CA prediction surface can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 13.3 | `falsifier_or_open_obligation` | unbounded nonperiodicity, cold nth-bit extraction, and full prediction remain separate mathematical obligations |

## Reviewer Claim Ledger

This ledger expands the formal-claims table into review actions. It is intended to make proof granularity explicit: what is being claimed, what evidence type can support it, what boundary remains, and what the next review action is.

| Formal row | Type | Claim in review terms | Evidence required | Boundary | Next review action |
|---|---|---|---|---|---|
| Theorem 13.1 | finite/executable result | finite and bounded CA readouts can be receipt-closed without claiming unbounded Rule 30 future-bit extraction | receipt, validator, executable pass, generated artifact, or finite enumeration | the stated finite/executable domain only | verify the receipt exists and its scope matches the claim |
| Proposition 13.2 | formal construction | CA prediction surface can be imported by later papers only through its declared source, receipt, and lane | definitions, normal-form construction, conversion rule, and downstream-use boundary | internal formal coherence; no measured physical identity without a separate calibration row | check that the normal form is named and the conversion rule is explicit |
| Protocol 13.3 | obligation/falsifier | unbounded nonperiodicity, cold nth-bit extraction, and full prediction remain separate mathematical obligations | explicit missing derivation, adapter, receipt, dataset, comparator, or failed test condition | does not negate satisfied lower-level rows | name the next binding action and owner surface |

## Claim Granularity And Review Table

The table below separates the claim types so the paper is reviewable without accepting the whole FLCR vocabulary at once.

| Claim type | What this paper may claim | Acceptance test | What is not claimed by that row |
|---|---|---|---|
| Formal-system result | `FLCR-13` defines or uses **Cellular Automata Prediction Surfaces** as a typed FLCR object with declared inputs, operations, outputs, and residue. | Definitions, formal claims, construction steps, and downstream-use rules are internally consistent and lane typed. | External physical truth, measured prediction, or identity with a standard theory. |
| Computational or receipt-bound result | Enumerations, TarPit runs, CAM/crystal routes, verifier rows, and generated artifacts are claims about the stated finite or executable domain. | A named receipt, validator, manifest, pass report, or rebuild result exists and matches the row scope. | Completeness outside the enumerated domain or physical correctness outside the tested comparator. |
| Imported theorem or external definition | Imported mathematics remains an external theorem/citation target; this paper may use it only through declared mappings and conservative-extension discipline. | The source theorem, definition layer, or citation target is named and the mapping into this paper is explicit. | A new proof of the imported theorem or a hidden change in the imported object's meaning. |
| Interpretive bridge or analogy | Analog, workbook, visual, or translation language may explain why the construction is useful. | The analogy preserves the relevant structure and does not promote itself into a theorem. | That the analogy alone proves the formal, computational, or physical claim. |
| Physical or calibration-facing claim | Physical or Standard Model identity is not claimed here unless the paper contains an explicit calibration row; the default status is deferred mapping. | A dataset, citation, calibration protocol, uncertainty, comparator, or falsifier is attached. | A physical conclusion supported only by shared vocabulary rather than calibration, comparator data, or a stated falsifier. |
| Open obligation or falsifier | A missing derivation, adapter, receipt, dataset, or failed comparator is a named research channel. | The next binding action and the reason the stronger claim is not closed are stated. | That the base formal result is false merely because a stronger downstream claim remains unfinished. |

## Proof Sources And Receipt Index

| Receipt path | Source | Row-scoped | Confidence |
|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_centroid_voa_chain.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_gauss_fourier_lift.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_voa_sector_decomposition.json | closure_applied | no | receipt_bound |
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
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_su5_observer_decomposition.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\kernel\staging\papers\suite81_claude_codex_memory\CX-NotebookLM\CX_CADForge_Demo_Export\wireblock_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\bijection_method_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-field_form_membership_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-number_is_ribbon_digital_root_receipt.json | closure_applied | no | receipt_bound |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-01-bijective_shell2_doublet_receipt.json | closure_applied | no | receipt_bound |

_… and 120 more receipt references._

### Applied closure carry (full paths)

| Receipt path | Source | Row-scoped | Confidence | Verifier |
|---|---|---|---|---|
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_centroid_voa_chain.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_gauss_fourier_lift.json | closure_applied | no | receipt_bound | PASS |
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge\receipts\verify_voa_sector_decomposition.json | closure_applied | no | receipt_bound | PASS |
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
| D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\verify_su5_observer_decomposition.json | closure_applied | no | receipt_bound | PASS |
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

_Proven ASSEMBLE-validated or receipt-bound evidence queued for re-inclusion — IRL-equivalent weight in review; does not inflate ASSEMBLE without receipt closure._

| Evidence ID | Lane | Target section | Proof path | Weight |
|---|---|---|---|---|
| PEEP-2026-001 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-006 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-012 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-013 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-014 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-015 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-018 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-020 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-024 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-006 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-012 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-013 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-014 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-015 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-018 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-020 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-024 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-026 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |
| PEEP-2026-034 | ASSEMBLE | Attached Evidence Index |  | IRL_equivalent_proposal_only |

## External Calibration (Candidates — Not Promoted)

| DOI | Readiness | Provenance | Confidence | Paired to formal |
|---|---|---|---|---|
| 10.1103/j3s5-gjpf | nist_pass | peep_index | PASS | yes |
| 10.1007/s00220-025-05376-5 | nist_pass | peep_index | PASS | yes |
| 10.25088/complexsystems.34.3.259 | nist_pass | peep_index | PASS | yes |
| 10.25088/ComplexSystems.34.3.259 | nist_pass | peep_index | PASS | yes |

### Unpaired seed DOIs

- `10.1016/j.physd.2021.133074` — **candidate** (seed; not paired to formal.md)
- `10.25088/ComplexSystems.34.3.259` — **candidate** (seed; not paired to formal.md)

## Obligation Crosswalk

_No open obligations — or all receipt-bound._

## Attached Evidence Index

| Category | Count | Tier | Notes |
|---|---|---|---|
| Timeline nodes | 193 | supporting_context | Provenance graph pass5 |
| Timeline edges | 12 | supporting_context | Includes zip crosswalk |
| Registry DISCOVERY rows | 0 | supporting_context | Not promoted |
| Seed candidates | 19 | external_candidates | IRL review appendix |
| Ingress 80 records | 2 | external_candidates | Curated seeds only |
| PEEP bindings (routed) | 55 | required_direct | Includes LOCAL-GAP |
| Falsifier gaps (audit) | 53 | required_direct | From assembly audit |

## Falsifiers And Comparators

| Record | DOI | Decision | Falsifier score | Title |
|---|---|---|---|---|
| PEEP-2026-007 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | Centroid VOA Verifier As Umbral-Moonshine Module Comparator |
| PEEP-2026-008 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | Pariah Monster Boundary As Umbral Moonshine Pariah Comparator |
| PEEP-2026-009 | 10.1007/s00220-025-05376-5 | ASSEMBLE | 85 | Monster Moonshine D4 Chain As Cone-VOA Module Comparator |
| PEEP-2026-029 | 10.25088/complexsystems.34.3.259 | ASSEMBLE | 85 | FLCR-03 Correction Surface As CA Self-Composition Comparator |
| PEEP-2026-038 | 10.25088/ComplexSystems.34.3.259 | ASSEMBLE | 85 | FLCR-30 Meta-Framer As CA Self-Composition Comparator |
| LOCAL-GAP-0001 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-lattice-forge-inventory.md |
| LOCAL-GAP-0002 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-jordan-j3-octonion.md |
| LOCAL-GAP-0003 |  | REROUTE_OR_REPAIR | 25 | verify_rule30_winding_number_proof.json |
| LOCAL-GAP-0004 |  | REROUTE_OR_REPAIR | 25 | CL_proof-source-lattice-forge-inventory.md |
| LOCAL-GAP-0007 |  | REROUTE_OR_REPAIR | 25 | CQE-paper-29-monster_energy_bound_hypotheses_receipt.json |
| LOCAL-GAP-0008 |  | REROUTE_OR_REPAIR | 25 | verify_rule30_proof_obligations.json |
| LOCAL-GAP-0010 |  | REROUTE_OR_REPAIR | 25 | manifest.json |
| LOCAL-GAP-0011 |  | REROUTE_OR_REPAIR | 25 | verify_rule30_whole_integer_n_coverage.json |
| LOCAL-GAP-0012 |  | REROUTE_OR_REPAIR | 25 | rule30.py |
| LOCAL-GAP-0013 |  | REROUTE_OR_REPAIR | 25 | centroid_voa.py |

## Open Gaps And Blockers

_No explicit blockers — verify PEEP/NIST gates before ASSEMBLE promotion._

### Pending external pair queue

- `EQ-REG-0046` — DISCOVERY_EXTERNAL_PAIR_REQUIRED: Find 2025/current peer-reviewed external paper and promote to PEEP package.

## Seed Appendix (IRL Review)

| Seed ID | DOI | Type | Confidence | NIST readiness |
|---|---|---|---|---|
| CLAIM-10.1016/j.physd.2021 | 10.1016/j.physd.2021.133074 | lane_claim_queue_ingress | 0.6 | PASS |
| EXT80-13 | 10.1016/j.physd.2021.133074 | ingress_80_curated_seed | 0.55 | seed_only |
| EQ-REG-0002 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| EQ-REG-0003 | None | external_pair_queue_non_flcr | 0.5 | needs_external_doi |
| REG-101807 | None | registry_discovery_external_pair | 0.45 | unscored |
| REG-68f630 | None | registry_discovery_external_pair | 0.45 | unscored |
| CAND-Q-04 | 10.25088/ComplexSystems.34.3.259 | external_pairing_candidate_queue | 0.4 | promoted_or_bound |
| LEGACY-R30-PROOF-015 |  | legacy_repo_ability_seed | 0.9 | not_applicable_legacy_ability_seed |
| ARCHIVE-F88C5CAC7385F3CD |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-5AE5699E3EFFE832 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-FB90E404417667A3 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-E9FC1BAA0D04B4B7 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-BBB3E61913300A90 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-926C69EC131D6C92 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-CD7854FE25715261 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-BA342BFE0D6EAA66 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-635946AD2F192622 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-95FF0AF1EAF17D37 |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |
| ARCHIVE-2A6752E40269853A |  | archive_history_crystal | 0.84 | not_applicable_archive_history_seed |

_Seeds are candidates only — pairing to formal.md requires NIST + receipt gates._

## Timeline And Registry Context

| Motif | Node count | Provenance |
|---|---|---|
| rule30_lineage | 131 | timeline_graph.pass5 |
| jordan_lineage | 50 | timeline_graph.pass5 |
| lattice_forge_lineage | 157 | timeline_graph.pass5 |
| moonshine_lineage | 59 | timeline_graph.pass5 |
| forge_lineage | 49 | timeline_graph.pass5 |
| hub_receipt_lineage | 3 | timeline_graph.pass5 |
| sm_bridge_lineage | 10 | timeline_graph.pass5 |

### Sample timeline nodes

- `D:\CQE_CMPLX\CMPLX-R30-main\DATA\cache\reverse-atlas-projected-rule...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\DATA\cache\reverse-atlas-rule30-center-...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\DATA\wolfram-rule30-center\manifest.json` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\extended_memory\manifest.json` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\centroid_voa.py` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\contributions_r...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\contribution_va...` — era=origin role=source_truth
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\cqe_rule30_solv...` — era=bridge role=bridge_reference

**Adjacent band:** FLCR-11, FLCR-12, FLCR-14, FLCR-15

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

_Generated 2026-07-01T02:44:51.604468+00:00 — intake schema v1.1_
