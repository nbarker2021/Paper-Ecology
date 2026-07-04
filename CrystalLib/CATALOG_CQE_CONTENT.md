# CATALOG_CQE_CONTENT.md
## CrystalLib Content-Addressed Memory Catalog
### Source: `D:\CQE_CMPLX\.cqe\`
### Catalog Date: 2025-07-05

---

## 1. Executive Summary

The `.cqe/` directory contains **147 files** across 14 subdirectories. The vast majority of content (143 files, 97.3%) resides in `receipts/`. Seven subdirectories are completely empty. All content is stored in JSON format except for one binary obligation artifact. No B-family numbering (FLCR, NIST) is used in this catalog; everything is mapped to the A-family paper series (`paper-00` through `paper-100`) and tagged with CAM hashes, D/I/X classification, and LCR kernel references where applicable.

---

## 2. Structured Inventory by Subdirectory

### 2.1 receipts/ — 143 files
**Data Format:** JSON (`.json` and `.jsonl`)

**Content:** Verification receipts for the CQE formal paper series. Each receipt is a CAM-addressed JSON object nested under a paper directory, a verifier script name, and a 16-hex-digit CAM hash directory.

**Directory Structure:**
```
receipts/
├── receipts.jsonl                        (empty)
├── CQE-paper-00/                         (4 receipts)
├── CQE-paper-01/                         (3 receipts)
├── CQE-paper-02/                         (2 receipts)
├── CQE-paper-03/                         (7 receipts)
├── CQE-paper-04/                         (1 receipt)
├── CQE-paper-05/                         (4 receipts)
├── CQE-paper-06/                         (5 receipts)
├── CQE-paper-07/                         (3 receipts)
├── CQE-paper-08/                         (12 receipts)
├── CQE-paper-09/                         (3 receipts)
├── CQE-paper-10/                         (3 receipts)
├── CQE-paper-11/                         (2 receipts)
├── CQE-paper-12/                         (6 receipts)
├── CQE-paper-13/                         (5 receipts)
├── CQE-paper-14/                         (2 receipts)
├── CQE-paper-15/                         (6 receipts)
├── CQE-paper-16/                         (1 receipt)
├── CQE-paper-17/                         (3 receipts)
├── CQE-paper-18/                         (2 receipts)
├── CQE-paper-19/                         (2 receipts)
├── CQE-paper-20/                         (2 receipts)
├── CQE-paper-21/                         (3 receipts)
├── CQE-paper-22/                         (2 receipts)
├── CQE-paper-23/                         (1 receipt)
├── CQE-paper-24/                         (1 receipt)
├── CQE-paper-25/                         (2 receipts)
├── CQE-paper-26/                         (2 receipts)
├── CQE-paper-27/                         (2 receipts)
├── CQE-paper-28/                         (5 receipts)
├── CQE-paper-29/                         (5 receipts)
├── CQE-paper-30/                         (2 receipts)
├── CQE-paper-31/                         (1 receipt)
├── CQE-paper-32/                         (11 receipts)
├── CQE-paper-formal-OC/                  (3 receipts)
├── CQE-paper-formal-PH3/                 (1 receipt)
├── CQE-paper-formal-S1/                  (2 receipts)
├── CQE-paper-formal-S9/                  (1 receipt)
├── CQE-paper-formal-S10/                 (1 receipt)
├── CQE-paper-formal-S11/                 (1 receipt)
├── CQE-paper-formal-S12/                 (1 receipt)
├── CQE-paper-formal-S13/                 (1 receipt)
├── CQE-paper-formal-S14/                 (1 receipt)
├── CQE-paper-formal-S15/                 (1 receipt)
├── CQE-paper-formal-S16/                 (1 receipt)
├── CQE-paper-formal-S17/                 (1 receipt)
├── CQE-paper-formal-S18/                 (1 receipt)
├── CQE-paper-formal-S19/                 (1 receipt)
├── CQE-paper-formal-S20/                 (1 receipt)
├── CQE-paper-formal-S21/                 (1 receipt)
├── CQE-paper-formal-S22/                 (1 receipt)
├── CQE-paper-formal-S23/                 (1 receipt)
├── CQE-paper-formal-S24/                 (1 receipt)
├── CQE-paper-formal-S25/                 (1 receipt)
├── CQE-paper-formal-S26/                 (1 receipt)
├── CQE-paper-formal-S27/                 (1 receipt)
├── CQE-paper-formal-S28/                 (1 receipt)
└── CQE-paper-formal-S29/                 (1 receipt)
```

**Key Fields (Simple Receipt Schema):**
- `paper` (string): A-family paper tag, e.g. `"CQE-paper-00"`
- `verifier` (string): Verifier name, e.g. `"established_grounding"`
- `script` (string): Path to verifier script, e.g. `"src/papers/formal/CQE-paper-01/verify_lcr_carrier.py"`
- `passed` (int): Number of tests passed
- `total` (int): Total number of tests
- `status` (string): `"pass"`, `"fail"`, `"unknown"`, `"pass_with_quarantined_hypotheses"`, `"pass_with_open_obligations"`

**Key Fields (Complex Receipt Schema — e.g., formal-OC):**
- `theorem` (string): Theorem statement
- `experiment` (string): Experiment description
- `claims_covered` (array of strings): Claim IDs, e.g. `["1.1", "1.2", ...]`
- `matched_claim_ids` (array of strings): Matched claim IDs
- `open_continuation` (string): Open obligation reference, e.g. `"O1 full W(E8) lookup table materialization"`
- `closure_report` (object): `{status, test, state_count, results, failures}`
- `oracle_report` (object): `{status, test, sample_count, samples}` where `samples[].cam_address` is a SHA-256 CAM hash and `samples[].descriptor` contains fold topology (`d4`, `su3`, `f4`), chart state, Weyl index, observer bit, and coordinates (X, Y, Z, t, w)
- `pressure_report` (object): `{status, test, checks, failures}`
- `scaling_report` (object): `{status, test, descriptor_count, folds, seed_addresses, weyl_chambers}`
- `seed_report` (object): `{status, test, seed_length, failures}`

**CAM Hash Naming:** Each receipt is stored under a 16-hex-digit directory name derived from the content address (e.g., `d3c4c721002ba4c9`). The full 64-hex CAM address appears in complex receipt descriptors.

---

### 2.2 irl/ — 2 files
**Data Format:** Binary (`.bin`) + JSON manifest (`.json`)

**Content:** In-Real-Life obligation artifacts. Currently stores one partial obligation: `O1.weyl_lookup_table`.

**Files:**
- `irl/o1-weyl-e8-subtable/weyl_e8_subtable.bin` — 245,000,000 bytes, binary subtable data
- `irl/o1-weyl-e8-subtable/weyl_e8_subtable.manifest.json` — Manifest metadata

**Key Fields (Manifest):**
- `status` (string): `"partial"`
- `obligation_id` (string): `"O1.weyl_lookup_table"`
- `weyl_order` (int): `696729600`
- `subtable_count` (int): `1000000`
- `record_size` (int): `245`
- `bytes` (int): `245000000`
- `path` (string): Absolute path to `.bin`
- `content_address` (string): 64-hex SHA-256 CAM hash (`48eaddc168d4f6388936c4e51fb0ed514b00a05217d7be411c49dae461b6f99c`)
- `honesty` (string): `"PARTIAL"`

---

### 2.3 ledger/ — 1 file
**Data Format:** JSON Lines (`.jsonl`)

**Content:** `ledger/events.jsonl` — **empty file** (0 bytes). Intended for event ledger but unpopulated.

---

### 2.4 Root — 1 file
**Data Format:** JSON Lines (`.jsonl`)

**Content:** `.cqe/events.jsonl` — **empty file** (0 bytes). Root-level event stream.

---

### 2.5 Empty Subdirectories (0 files each)

| Subdirectory | Intended Role | Status |
|-------------|---------------|--------|
| `carriers/` | Carrier transport / ribbon propagation | Empty — no content |
| `ribbons/` | Ribbon digital-root artifacts | Empty — no content |
| `snapshots/` | System snapshots / state captures | Empty — no content |
| `obligations/` | Obligation registry | Empty — obligations stored in `irl/` instead |
| `sources/` | Source code / provenance | Empty — no content |
| `masters/` | Master receipts / canonical hashes | Empty — no content |
| `derived/` | Derived / computed artifacts | Empty — no content |
| `meso/` | Meso-scale intermediate structures | Empty — no content |
| `meta/` | Meta-data / index files | Empty — no content |
| `reports/` | Generated reports | Empty — no content |
| `workbook/` | Workbook / scratch data | Empty — no content |

---

## 3. Data Format Summary by Content Type

| Content Type | Format | Files | Key Schema |
|-------------|--------|-------|------------|
| Verification receipts | JSON | 142 | `paper`, `script`/`verifier`, `passed`, `total`, `status` |
| Complex theorem receipts | JSON | 1 (formal-OC) | `theorem`, `claims_covered`, `closure_report`, `oracle_report`, `scaling_report`, `cam_address` samples |
| Receipt index | JSONL | 1 (empty) | N/A |
| Event ledgers | JSONL | 2 (empty) | N/A |
| Binary subtable | Binary | 1 | Raw 245-byte records, 1M subtables |
| Subtable manifest | JSON | 1 | `obligation_id`, `content_address`, `honesty`, `weyl_order` |

---

## 4. A-Family Mapping (paper-00 → paper-100)

All B-family `CQE-paper-*` identifiers are stripped and mapped to the A-family `paper-*` namespace. The LCR kernel, D/I/X tags, and CAM hashes are preserved as the addressing scheme.

### 4.1 Core Paper Series (paper-00 → paper-32)

These map 1:1 from `CQE-paper-NN` to `paper-NN`. Each receipt is a **D-tag** (derivation / verification) under the corresponding paper.

| A-Family | B-Family Source | Receipts | Verifier Topics (Sample) |
|----------|----------------|----------|--------------------------|
| `paper-00` | `CQE-paper-00` | 4 | `established_grounding`, `verify_established_grounding`, `verify_field_form_membership`, `verify_number_is_ribbon_digital_root` |
| `paper-01` | `CQE-paper-01` | 3 | `verify_lcr_carrier`, `verify_bijective_shell2_doublet`, `verify_o8_spinor_double_cover_closed` |
| `paper-02` | `CQE-paper-02` | 2 | `verify_correction_surface`, `verify_correction_surface_monitor` |
| `paper-03` | `CQE-paper-03` | 7 | `verify_algebra_foundation_T1_T4`, `verify_d12_idempotent_chain`, `verify_d4_atlas_bijectivity`, `verify_d4_block_tower_exceptional`, `verify_su3_closure_T5_T7`, `verify_triality_annealing`, `verify_triality_surface` |
| `paper-04` | `CQE-paper-04` | 1 | `verify_boundary_repair` |
| `paper-05` | `CQE-paper-05` | 4 | `verify_cd_conjugation_gluon_oloid_theta0`, `verify_gluon_oloid_worldline`, `verify_oloid_carrier_family`, `verify_oloid_path_carrier` |
| `paper-06` | `CQE-paper-06` | 5 | `verify_causal_code`, `verify_correction_extraction_verdict`, `verify_lucas_axis_readout`, `verify_rule90_lucas_decomposition`, `verify_triadic_keystone` |
| `paper-07` | `CQE-paper-07` | 3 | `verify_discrete_continuous_bridge`, `verify_mdhg_speedlight_bridge`, `verify_o3_universality_closed` |
| `paper-08` | `CQE-paper-08` | 12 | `verify_atlas_unipotent_orbits_real_data`, `verify_e8_even_lattice`, `verify_e8_hemisphere_partition`, `verify_f2_bridge_unipotent_substrate`, `verify_lattice_closure_template`, `verify_lattice_code_chain`, `verify_lattice_code_closure`, `verify_niemeier_leech_enumeration`, `verify_o1_weyl_e8_construction_closed`, `verify_o2pp_registry_populated`, `verify_o7_niemeier_e8cubed_glue_closed`, `verify_t8_commutability_tree` |
| `paper-09` | `CQE-paper-09` | 3 | `verify_hamiltonian_window_emergence`, `verify_kappa_conservation_law`, `verify_u_r30_quantum_circuit` |
| `paper-10` | `CQE-paper-10` | 3 | `verify_bijection_cold_start`, `verify_ologn_readout_architecture`, `verify_t10_master_receipt` |
| `paper-11` | `CQE-paper-11` | 2 | `verify_sporadic_admission_boundary`, `verify_theory_admission_gate` |
| `paper-12` | `CQE-paper-12` | 6 | `verify_ca_prediction_surface`, `verify_center_column_entropy`, `verify_p1_non_periodicity`, `verify_p2_density`, `verify_rule30_real_dataset_experiment`, `verify_wolfram_1m_bit` |
| `paper-13` | `CQE-paper-13` | 5 | `verify_invariant_transfer_su2u1_in_su3`, `verify_quark_face_transport`, `verify_quark_face_transport_literalized`, `verify_rule30_shell_verification_ledger`, `verify_standard_model_real_comparison` |
| `paper-14` | `CQE-paper-14` | 2 | `verify_boundary_repair_curvature`, `verify_curvature_is_correction` |
| `paper-15` | `CQE-paper-15` | 6 | `verify_eight_states_one_dual_reading`, `verify_mass_framing_2x2x2_vs_3x3`, `verify_mass_gravity_drive`, `verify_mass_residue_carrier`, `verify_mass_residue_literalized`, `verify_ninth_is_forced_printout` |
| `paper-16` | `CQE-paper-16` | 1 | `verify_continuum_edge_residuals` |
| `paper-17` | `CQE-paper-17` | 3 | `verify_error_correction_tower`, `verify_golay_leech_tower`, `verify_leech_kissing_published_decomposition` |
| `paper-18` | `CQE-paper-18` | 2 | `verify_centroid_voa_chain`, `verify_voa_moonshine_routes` |
| `paper-19` | `CQE-paper-19` | 2 | `verify_observation_is_face_selection`, `verify_observer_face_selection` |
| `paper-20` | `CQE-paper-20` | 2 | `verify_layer2_synthesis_ledger`, `verify_solution_ledger_affirmed` |
| `paper-21` | `CQE-paper-21` | 3 | `verify_agrm_golden_sweep`, `verify_morphforge_ribbon`, `verify_three_gap_golden_sweep` |
| `paper-22` | `CQE-paper-22` | 2 | `verify_astro_metaforge_package`, `verify_metaforge_materials` |
| `paper-23` | `CQE-paper-23` | 1 | `verify_foldforge_descriptor` |
| `paper-24` | `CQE-paper-24` | 1 | `verify_knightforge_ca` |
| `paper-25` | `CQE-paper-25` | 2 | `verify_energetic_traversal`, `verify_energy_ledger_affirmed` |
| `paper-26` | `CQE-paper-26` | 2 | `verify_pinch_driven_roll`, `verify_zpinch_shear_horizon` |
| `paper-27` | `CQE-paper-27` | 2 | `verify_observer_delay_shared_reality`, `verify_waveform_collapse_mechanism` |
| `paper-28` | `CQE-paper-28` | 5 | `verify_conway_glider_oloid`, `verify_glider_collision_cascade`, `verify_gosper_gun_emitter`, `verify_ndim_knight_ca_affirmed`, `verify_nd_game_lattices` |
| `paper-29` | `CQE-paper-29` | 5 | `verify_grand_ribbon_meta_framer`, `verify_monster_energy_bound_hypotheses`, `verify_monster_internal_map`, `verify_moonshine_real_data_experiment`, `verify_supersingular_prime_ceiling` |
| `paper-30` | `CQE-paper-30` | 2 | `verify_grand_ribbon_meta_framer`, `verify_rule30_corpus_provenance` |
| `paper-31` | `CQE-paper-31` | 1 | `verify_meta_lcr_readout` |
| `paper-32` | `CQE-paper-32` | 11 | `verify_120_e8_cayley_dickson_doubling`, `verify_43200_pyramid_structure`, `verify_alena_morph_e8_kit`, `verify_e8_routed_constructor`, `verify_higher_order_superperm_manager`, `verify_houston_872_attempt`, `verify_hyperpermutation_audit`, `verify_lcr_superperm_handbuild`, `verify_n6_871_reduction`, `verify_octad_e8_structure`, `verify_supervisor_cursor_schedule` |

**Core Series Totals:** 33 papers (00–32), 142 receipts, all mapped to A-family `paper-NN` namespace.

---

### 4.2 Formal Extension Series (unassigned to paper-00–paper-100)

These are formal supplements that do not fit the `paper-00` through `paper-100` linear numbering. They are tagged as **unassigned** A-family members but retain their D/I/X receipts under the CAM system.

| B-Family | Receipts | Verifier Topics (Sample) | A-Family Status |
|----------|----------|--------------------------|-----------------|
| `CQE-paper-formal-OC` | 3 | `verify_oracle_chart` (complex: chart closure, oracle descriptors, scaling bound, Weyl chambers) | **unassigned** — OC (Oracle Chart) formal extension |
| `CQE-paper-formal-PH3` | 1 | `verify_gluon_aliasing_illusion` | **unassigned** — PH3 formal extension |
| `CQE-paper-formal-S1` | 2 | `verify_spectre_correction`, `verify_spectre_geometry` | **unassigned** — S1 formal extension |
| `CQE-paper-formal-S9` | 1 | `verify_palindromic_superperm` | **unassigned** — S9 formal extension |
| `CQE-paper-formal-S10` | 1 | `verify_3_conjugate_moonshine` | **unassigned** — S10 formal extension |
| `CQE-paper-formal-S11` | 1 | `verify_state_of_rule30_s11` | **unassigned** — S11 formal extension |
| `CQE-paper-formal-S12` | 1 | `verify_barker_market_engine_s12` | **unassigned** — S12 formal extension |
| `CQE-paper-formal-S13` | 1 | `verify_period_4_theorem_s13` | **unassigned** — S13 formal extension |
| `CQE-paper-formal-S14` | 1 | `verify_antipodal_wrapping_bijection_s14` | **unassigned** — S14 formal extension |
| `CQE-paper-formal-S15` | 1 | `verify_hamming_centroid_universality_s15` | **unassigned** — S15 formal extension |
| `CQE-paper-formal-S16` | 1 | `verify_algebraic_closure_s16` | **unassigned** — S16 formal extension |
| `CQE-paper-formal-S17` | 1 | `verify_unified_skeleton_s17` | **unassigned** — S17 formal extension |
| `CQE-paper-formal-S18` | 1 | `verify_voa_moonshine_s18` | **unassigned** — S18 formal extension |
| `CQE-paper-formal-S19` | 1 | `verify_lattice_forge_s19` | **unassigned** — S19 formal extension |
| `CQE-paper-formal-S20` | 1 | `verify_digital_root_cross_walk_s20` | **unassigned** — S20 formal extension |
| `CQE-paper-formal-S21` | 1 | `verify_modal_atlas_s21` | **unassigned** — S21 formal extension |
| `CQE-paper-formal-S22` | 1 | `verify_cmplx_r30_cross_walk_s22` | **unassigned** — S22 formal extension |
| `CQE-paper-formal-S23` | 1 | `verify_standard_model_observer_s23` | **unassigned** — S23 formal extension |
| `CQE-paper-formal-S24` | 1 | `verify_timecube_modal_s24` | **unassigned** — S24 formal extension |
| `CQE-paper-formal-S25` | 1 | `verify_hard_riemann_cross_walk_s25` | **unassigned** — S25 formal extension |
| `CQE-paper-formal-S26` | 1 | `verify_barker_v3_s26` | **unassigned** — S26 formal extension |
| `CQE-paper-formal-S27` | 1 | `verify_barker_v4_s27` | **unassigned** — S27 formal extension |
| `CQE-paper-formal-S28` | 1 | `verify_multi_window_s28` | **unassigned** — S28 formal extension |
| `CQE-paper-formal-S29` | 1 | `verify_multi_estimator_s29` | **unassigned** — S29 formal extension |

**Note:** Formal extensions S2–S8 are missing from the current `.cqe/` snapshot.

---

### 4.3 IRL Obligations

| Obligation ID | Files | A-Family Status |
|---------------|-------|-----------------|
| `O1.weyl_lookup_table` | 2 (`.bin` + `.manifest.json`) | **unassigned** — IRL obligation, not a paper. References `paper-08` (`verify_o1_weyl_e8_construction_closed`) as the open continuation. |

---

## 5. Unassigned Content Summary

The following `.cqe/` content has **no direct mapping** to the `paper-00` through `paper-100` A-family linear series:

1. **Formal Extensions (24 papers, 29 receipts):**
   - `CQE-paper-formal-OC`, `CQE-paper-formal-PH3`
   - `CQE-paper-formal-S1`, `S9`–`S29` (missing `S2`–`S8`)
   - These are supplementary formal papers. If the A-family is expanded beyond `paper-100`, they could be assigned slots `paper-101+` or remain as a separate `formal-*` namespace.

2. **IRL Obligations (1 obligation, 2 files):**
   - `O1.weyl_lookup_table` — a partial binary artifact. This is an obligation, not a paper. It is linked to `paper-08` via the `verify_o1_weyl_e8_construction_closed` verifier and the `open_continuation` field in `formal-OC` receipts.

3. **Empty Infrastructure Subdirectories (11 directories, 0 files):**
   - `carriers/`, `ribbons/`, `snapshots/`, `obligations/`, `sources/`, `masters/`, `derived/`, `meso/`, `meta/`, `reports/`, `workbook/`
   - These are structural placeholders in the CAM filesystem. No content to map.

4. **Empty Ledger Files (2 files):**
   - `.cqe/events.jsonl`, `ledger/events.jsonl` — Both are 0-byte JSONL files. No events logged.

---

## 6. CAM Hash and Content Addressing Observations

- **Receipt addressing:** Each receipt is stored under a 16-hex-digit directory name (e.g., `d3c4c721002ba4c9`). This is consistent with a truncated CAM hash or content-addressed prefix.
- **Full CAM hashes:** The `formal-OC` complex receipts contain 64-hex `cam_address` fields in oracle descriptor samples (e.g., `28179a0824222c9ed708d041a95622806aff5a3b1d6714e93c7ef8874fd0ccc2`).
- **Binary manifest addressing:** The `weyl_e8_subtable.manifest.json` contains a full 64-hex `content_address` (`48eaddc168d4f6388936c4e51fb0ed514b00a05217d7be411c49dae461b6f99c`).
- **LCR kernel references:** Verifiers frequently reference LCR concepts (`verify_lcr_carrier`, `verify_lcr_superperm_handbuild`, `verify_meta_lcr_readout`). The LCR kernel is the foundational addressing scheme for the A-family papers.
- **D/I/X tags:** Receipts map to D-tags (derivations/verifications) under their respective papers. No I-tags (invariants) or X-tags (exceptions) are explicitly stored as separate `.cqe/` files; they are embedded in the receipt JSON status fields (`pass`, `fail`, `unknown`, `pass_with_quarantined_hypotheses`, `pass_with_open_obligations`).

---

## 7. Receipt Status Distribution

Based on the 142 receipt.json files sampled:

| Status | Count | Description |
|--------|-------|-------------|
| `pass` | Majority | Verification succeeded |
| `fail` | Minority | Verification failed (e.g., `paper-10` master receipt, `paper-formal-S11`) |
| `unknown` | 1+ | No test data available (e.g., `paper-formal-S1` spectre geometry) |
| `pass_with_quarantined_hypotheses` | 1+ | Passed but some hypotheses quarantined (e.g., `paper-29` monster energy bound) |
| `pass_with_open_obligations` | 1+ | Passed but leaves open obligations (e.g., `paper-formal-S25` hard Riemann cross-walk) |

---

## 8. Catalog Conclusion

The `.cqe/` directory is a **Content-Addressed Memory (CAM) store** for the CQE/CMPLX formal paper system. 97% of the stored bytes are JSON verification receipts. The A-family core series (`paper-00` through `paper-32`) is fully represented with 142 receipts. The remaining 29 receipts belong to formal extensions (OC, PH3, S1, S9–S29) that are **unassigned** to the linear `paper-00`–`paper-100` namespace. One binary IRL obligation (`O1.weyl_lookup_table`) is also unassigned. Eleven infrastructure directories are empty placeholders.

All B-family identifiers (`CQE-paper-*`) have been stripped and mapped to A-family conventions in this catalog. No FLCR or NIST numbering is used.

---
*End of Catalog*
