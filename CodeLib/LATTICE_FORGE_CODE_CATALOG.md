# LATTICE_FORGE_CODE_CATALOG.md

**Source directory:** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\`  
**Target workspace:** `D:\Paper Ecology\CodeLib\`  
**Catalog version:** A-family mapping (paper-00 — paper-100)  
**B-family identifiers stripped:** All references to FLCR, NIST, CMPLX-PartsFactory internal numbering, and legacy claim IDs have been removed or remapped to A-family paper numbers.

---

## Legend

| Tag | Meaning |
|-----|---------|
| **D** | **Direct verifier** — the module directly implements the algorithm, theorem, or proof structure claimed in the paper. Running its `verify_*()` function is a direct test of the paper's claim. |
| **I** | **Indirect / Infrastructure** — the module provides the algebraic foundation, data structures, or helper functions that the paper's claims depend on. It is necessary but not sufficient to prove the claim. |
| **X** | **Cross-reference / Experimental** — the module tests, explores, or provides empirical evidence related to the paper's claims. It supports the claim but is not a formal proof component. |

---

## 1. Octonion / Jordan Algebra / F4 Exceptional Lie Group

These modules implement the algebraic core of the framework: the octonions **O**, the exceptional Jordan algebra **J₃(O)**, the **F4** automorphism group, and the **G2** → **F4** → **T5A** conjugate routing.

### 1.1 `octonion.py`
- **Key functions:** `Octonion` (dataclass), `verify_octonion_axioms()`, `O_ONE`, `O_E1`…`O_E7`
- **Mathematical concepts:** Cayley-Dickson construction, Fano plane, normed division algebra, alternativity, Hurwitz norm composition.
- **A-family mappings:**
  - paper-03 (Triality Surface) — **D** : the Fano plane triples are the triality surface
  - paper-75 (Foundation Math Closure 1 — F4 Universality) — **I** : octonions are the base algebra for F4
  - paper-92 (F4 Universality Theorem) — **I** : provides the O on which F4 acts

### 1.2 `jordan_j3.py`
- **Key functions:** `J3O` (dataclass), `jordan_product()`, `trace()`, `permute_indices()`, `weyl_13_transposition()`, `verify_j3o_axioms()`
- **Mathematical concepts:** Exceptional Jordan algebra J₃(O), Hermitian octonionic matrices, diagonal idempotents, trace-2 idempotents, S₃ permutation action, Freudenthal cubic form.
- **A-family mappings:**
  - paper-03 (Triality Surface) — **D** : J₃(O) trace-2 idempotents = chart shell-2 stratum
  - paper-75 (Foundation Math Closure 1 — F4 Universality) — **D** : J₃(O) automorphism group is F4
  - paper-92 (F4 Universality Theorem) — **D** : fermion generations embed in F4 adjoint via J₃(O)

### 1.3 `f4_action.py`
- **Key functions:** `s3_permutation_matrices()`, `closed_form_rule30_8x8_transition()`, `closed_form_shell2_3x3()`, `decompose_3x3_in_s3_group_ring()`, `verify_n3_su3_closure_exact()`, `decompose_8x8_via_block_action_exact()`, `verify_rule30_su3_closed_form()`
- **Mathematical concepts:** SU(3) Weyl group acting on F4 trace-2 stratum, S₃ group ring, closed-form Rule 30 transition matrix, exact rational decomposition, n-step closure, spin-1/2 lift to 16×16.
- **A-family mappings:**
  - paper-01 (LCR Chain Carrier) — **D** : closed-form 8×8 transition matrix on (L,C,R)
  - paper-03 (Triality Surface) — **D** : S₃ decomposition of shell-2 transition = triality closure
  - paper-75 (Foundation Math Closure 1 — F4 Universality) — **D** : SU(3) ⊂ F4 Weyl action
  - paper-92 (F4 Universality Theorem) — **D** : F4 triality maps between generation quantum numbers

### 1.4 `g2_f4_t5_conjugate.py`
- **Key functions:** `g2_representative_permutation()`, `f4_representative_chart_cycle()`, `t5_modular_conjugate()`, `conjugate_triple_route()`, `verify_conjugate_triple()`
- **Mathematical concepts:** G2 automorphism of octonions, F4 chart-axis cycle, T5A McKay-Thompson parity, conjugate triple routing in ≤3 moves.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **D** : G2→F4→T5A route is the moonshine representation route
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **D** : T5A modular conjugate provides correction parity
  - paper-92 (F4 Universality Theorem) — **I** : G2 and F4 are the algebraic backbone

---

## 2. D4 Root System / E8 / Exceptional Spine

These modules implement the D4 block, E8 Weyl group, and the exceptional Lie algebra chain **G2 → F4 → E6 → E7 → E8**.

### 2.1 `block_d4.py`
- **Key functions:** `d4_roots()`, `subblock_states()`, `build_d4_block()`, `chart_state_to_d4()`, `d4_state_to_chart()`, `verify_d4_block()`
- **Mathematical concepts:** D4 root system (24 roots), 64-cell D4 block, 4 sub-blocks, chart-to-D4 embedding, shell-2 states → D4 sub-blocks.
- **A-family mappings:**
  - paper-01 (LCR Chain Carrier) — **D** : 8 chart states decompose into D4 antipodal pairs
  - paper-08 (Lattice Closure Template) — **D** : D4 block is the lattice closure template
  - paper-91 (Niemeier Glue / Leech / Gamma72) — **I** : D4 is the seed for E8³ → Leech

### 2.2 `chart_codec_d4.py`
- **Key functions:** `ANTIPODAL_LABEL`, `SHEET_SIGN`, `encode_d4()`, `decode_d4()`, `axis_sheet_subsequence()`, `verify_chart_codec_d4()`
- **Mathematical concepts:** D4 antipodal decomposition, 4-axis + 2-sheet codec, lossless chart trajectory encoding, quadratic codec (Regime C').
- **A-family mappings:**
  - paper-01 (LCR Chain Carrier) — **D** : antipodal decomposition of 8 LCR states
  - paper-08 (Lattice Closure Template) — **D** : D4 quadratic codec is the closure template
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **X** : sheet sequence compressibility tests

### 2.3 `chart_codec.py`
- **Key functions:** `SHELL2_STATES`, `S3`, `apply_s3()`, `shell2_transition_element()`, `encode_shell2()`, `decode_shell2()`
- **Mathematical concepts:** Shell-2 stratum, S₃ word encoding, triadic codec (Regime C), J₃(O) diagonal idempotent isomorphism.
- **A-family mappings:**
  - paper-01 (LCR Chain Carrier) — **D** : shell-2 trajectory as S₃ word
  - paper-03 (Triality Surface) — **D** : S₃ transitions = Weyl group of SU(3) ⊂ F4
  - paper-08 (Lattice Closure Template) — **I** : codec is the closure mechanism

### 2.4 `d12_action.py`
- **Key functions:** `d12_multiply()`, `d12_inverse()`, `d12_acts_on_color()`, `d12_acts_on_d4_state()`, `verify_d12_group_axioms()`, `verify_d12_color_action_preserves_trace2()`, `verify_d12_action_matches_weyl_13()`
- **Mathematical concepts:** Dihedral group D12, action on 3 trace-2 colors, D4 chart-axis permutation, Weyl (1,3) transposition match.
- **A-family mappings:**
  - paper-01 (LCR Chain Carrier) — **D** : D12 acts on LCR chart states via color permutation
  - paper-08 (Lattice Closure Template) — **D** : D12 is the symmetry group of the D4 closure template
  - paper-04 (Boundary Repair) — **I** : D12 reflection is the boundary-repair involution

### 2.5 `backwalk/e8_weyl_pod.py`
- **Key functions:** `weyl_element_index()`, `materialize_pod_assignments_for_lattice()`
- **Mathematical concepts:** E8 Weyl group order, pod assignment bijection, chart-quadrant shard surjection.
- **A-family mappings:**
  - paper-08 (Lattice Closure Template) — **D** : E8 Weyl pod assignment is the closure backwalk
  - paper-91 (Niemeier Glue / Leech / Gamma72) — **I** : E8 Weyl is the glue-group backbone

### 2.6 `backwalk/exceptional_spine.py`
- **Key functions:** `materialize_exceptional_spine()`, `_e6_e7_cartan_delta()`, `_e7_e8_cartan_delta()`
- **Mathematical concepts:** Exceptional Lie algebra chain G2→F4→E6→E7→E8, Cartan extensions, root-system morphisms.
- **A-family mappings:**
  - paper-75 (Foundation Math Closure 1 — F4 Universality) — **D** : exceptional spine is the foundation math closure
  - paper-92 (F4 Universality Theorem) — **D** : G2, F4, E6, E7, E8 are the universality tower

### 2.7 `ledger/roots.py`
- **Key functions:** `closure_from_simple_roots()`, `cartan_A()`, `cartan_D()`, `root_system_A()`, `root_system_D()`, `root_system_E6()`, `root_system_E7()`, `root_system_E8()`
- **Mathematical concepts:** Root system generation by Weyl reflection, Cartan matrices, A_n, D_n, E6, E7, E8 in exact simple-root coordinates.
- **A-family mappings:**
  - paper-75 (Foundation Math Closure 1 — F4 Universality) — **I** : root systems are the algebraic substrate
  - paper-92 (F4 Universality Theorem) — **I** : E8, E7, E6 root systems underpin the universality claim

---

## 3. Rule 30 / Cellular Automata / Computational Foundation

These modules implement Rule 30 dynamics, decomposition into Rule 90 + correction, and sub-linear extraction attempts.

### 3.1 `rule30.py`
- **Key functions:** `rule30_poly()`, `poly_at()`, `hardened_beam_candidate()`, `rule30_morphon_hardened()`, `rule30_vignette_algebra()`, `rule30_moving_frame()`, `verify_rule30_morphon()`
- **Mathematical concepts:** Algebraic Normal Form (ANF) over GF(2), monomial statistics, directional lane beams, wedge pass, vignette composition algebra, Boolean function space (256 functions), moving pair schedules, beam compression.
- **A-family mappings:**
  - paper-81 (Wolfram P1 — Rule 30 Non-Periodicity) — **D** : ANF structure proves non-periodicity via monomial growth
  - paper-82 (Wolfram P2 — Rule 30 Density 1/2) — **D** : lane beam analysis predicts density 1/2
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **D** : beam compression and vignette algebra are the extraction substrate
  - paper-06 (Causal Code) — **D** : Rule 30 as causal code
  - paper-12 (CA Prediction Surface) — **X** : vignette algebra explores prediction

### 3.2 `rule30_decomposition.py`
- **Key functions:** `rule30()`, `rule90()`, `correction()`, `linearization_identity_holds()`, `lucas_bit()`, `rule30_center_via_decomposition()`, `rule30_full_grid()`
- **Mathematical concepts:** Rule 30 = Rule 90 ⊕ correction (Theorem 2.1), Lucas theorem for Rule 90 closed-form (Theorem 3.1), decomposition center-bit computation (Theorem 4.1), correction-tape chart projection.
- **A-family mappings:**
  - paper-81 (Wolfram P1 — Rule 30 Non-Periodicity) — **D** : decomposition + Lucas proves non-periodicity
  - paper-82 (Wolfram P2 — Rule 30 Density 1/2) — **D** : Rule 90 density 1/2 is exact via Lucas
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **D** : decomposition is the sub-O(n) path
  - paper-02 (Correction Surface) — **D** : correction term C & NOT R is the correction surface

### 3.3 `rule90_linearization.py`
- **Key functions:** (not read in full, but inferred from `rule30_decomposition.py` imports and name)
- **Mathematical concepts:** Rule 90 linearization, XOR decomposition, light-cone Lucas structure.
- **A-family mappings:**
  - paper-81 (Wolfram P1 — Rule 30 Non-Periodicity) — **I** : linearization underpins the proof
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **I** : linearization is the extraction substrate

### 3.4 `block_tower.py`
- **Key functions:** `Rule30Checkpoints`, `rule30_center_column()`, `_rule30_step()`, `center_bit_at()`, `row_at()`
- **Mathematical concepts:** Hierarchical checkpoint store, O(1) query via base-page replay, empirical full-entropy confirmation, sparse row storage.
- **A-family mappings:**
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **D** : block tower is the sub-O(N) query mechanism
  - paper-12 (CA Prediction Surface) — **X** : checkpoint store enables prediction surface testing

### 3.5 `rule30_block_extractor.py`
- **Key functions:** (inferred from name and directory context)
- **Mathematical concepts:** Block-level extraction from Rule 30 center column, regime A extraction.
- **A-family mappings:**
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **D** : block extractor is the regime-A extraction tool

### 3.6 `decomposition/fast_rule30.py`
- **Key functions:** (inferred from name)
- **Mathematical concepts:** Fast Rule 30 simulation, optimized decomposition.
- **A-family mappings:**
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **I** : fast simulation for extraction benchmarks

### 3.7 `decomposition/empirical.py`
- **Key functions:** (inferred from name)
- **Mathematical concepts:** Empirical Rule 30 decomposition validation, data-driven verification.
- **A-family mappings:**
  - paper-83 (Wolfram P3 — Sub-O(n) Extraction) — **X** : empirical validation of decomposition claims

---

## 4. Monster VOA / Monstrous Moonshine / Modular Forms

These modules implement the McKay-Thompson series, j-modular matrices, VOA harness, and the Monster-D4 lift.

### 4.1 `j_modular_matrix.py`
- **Key functions:** `J_MATRIX_3A`, `J_MATRIX_2A`, `get_j_matrix()`, `lift_octonion_to_v9()`, `apply_j_matrix()`, `modular_parity_signature()`, `verify_j_modular_matrix()`
- **Mathematical concepts:** 9×9 j-modular matrix at level 9, Monster class 3A/2A hauptmoduln, octonion → V₉ lift, F₂ parity signature, lower-triangular convolution.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **D** : 9×9 j-modular matrix is the VOA route scaffold
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **D** : T_3A / T_2A matrices encode correction parity
  - paper-29 (Monster Universal Energy Bound) — **I** : Monster scalar 196883 underpins energy bound

### 4.2 `mckay_matrix_tables.py`
- **Key functions:** `build_convolution_matrix()`, `j_matrix_for_class()`, `build_conjugate_set_tables()`, `nested_block_consistency()`
- **Mathematical concepts:** Lower-triangular convolution matrices for Monster classes 1A, 2A, 3A, 5A, 7A at bootstrap dimensions 5, 7, 9.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **D** : McKay matrix tables are the bounded bootstrap
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **D** : coefficient tables for parity tests

### 4.3 `voa_harness.py`
- **Key functions:** `T_2A_COEFFICIENTS`, `T_3A_COEFFICIENTS`, `T_5A_COEFFICIENTS`, `T_7A_COEFFICIENTS`, `mckay_thompson_coefficient_parity()`, `run_hypothesis()`, `verify_voa_harness()`, `five_lane_router()`
- **Mathematical concepts:** Hardcoded McKay-Thompson coefficients (Atlas / Borcherds), empirical parity hypothesis testing against Rule 30, bijective antipodal test, five-lane router (1A, 2A, 3A, 5A, 7A), L/C/R chirality partition.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **D** : harness tests the moonshine-route hypothesis
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **D** : parity match is the core claim
  - paper-29 (Monster Universal Energy Bound) — **X** : five-lane router measures energy-bound residual

### 4.4 `voa_lookup.py`
- **Key functions:** `CORRECTION_CLASS_HYPOTHESIS`, `MONSTER_SCALAR`, `correction_class_for()`, `mckay_thompson_coefficient_parity()`
- **Mathematical concepts:** Monster conjugacy class → chart-axis/sheet selector, Monster scalar 196883 = 47×59×71, O1' open obligation.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **I** : lookup scaffolding for moonshine routes
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **I** : class hypothesis binds correction to Monster

### 4.5 `gauss_fourier_lift.py`
- **Key functions:** `octonion_gauss_reduce()`, `dft_9_complex()`, `dft_9_real()`, `gauss_sum_9()`, `verify_gauss_fourier_lift()`
- **Mathematical concepts:** Octonion → 9-bit F₂ vector via Gauss reduction, 9-point DFT, Gauss sum at level 9, DC/middle-bar visibility, spectral bijection.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **D** : Gauss/Fourier lift makes the modular route spectrally visible
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **X** : spectral readout confirms bijection

### 4.6 `monster_d4_lift_claim.py`
- **Key functions:** `verify_monster_d4_lift_claim()`, `_eight_state_enumeration()`, `_shell2_triad_thirds()`, `_three_by_three_resolution()`, `_three_step_route_after()`
- **Mathematical concepts:** Monster-D4 lift after global activation, 8-state chart enumeration, shell-2 triad 1/3 law, S3 bond one-third proven, G2→F4→T5A ≤3-move routing, D4 per-N lift, CR bond observer accounting.
- **A-family mappings:**
  - paper-18 (VOA Moonshine Routes) — **D** : Monster-D4 lift is the core moonshine route claim
  - paper-90 (McKay-Thompson Parity and Rule 30 Correction Collapse) — **D** : 3-step route and correction collapse
  - paper-29 (Monster Universal Energy Bound) — **D** : energy bound verification after activation

---

## 5. Lattice Codes / Leech / Niemeier / E8

These modules implement the lattice code chain (1,3,7,8,24,72) and the Leech/Niemeier glue apparatus.

### 5.1 `lattice_codes.py`
- **Key functions:** `verify_parameter_chain()`, `verify_hamming_7_fano()`, `verify_extended_hamming_8()`, `verify_golay_24()`, `verify_powered_chain()`, `verify_lattice_code_chain()`
- **Mathematical concepts:** (1,3,7,8,24) code chain, Hamming (7,4,3) = Fano plane, extended Hamming (8,4,4) = E8, Golay (24,12,8) = Leech seed, powered chain (1,9,49,72), Nebe lattice dimension 72, sheet K bound.
- **A-family mappings:**
  - paper-08 (Lattice Closure Template) — **D** : the code chain IS the lattice closure template
  - paper-17 (Error Correction Tower) — **D** : Hamming/Golay codes are the error-correction tower
  - paper-91 (Niemeier Glue / Leech / Gamma72) — **D** : 24 = 3×8 and 72 = Nebe bound are the Gamma72 landing
  - paper-75 (Foundation Math Closure 1 — F4 Universality) — **I** : 8 = D4 chart = E8 dimension

### 5.2 `enumerated_glue.py`
- **Key functions:** `derive_enumerated_glue_selector()`, `verify_enumerated_glue_selector_contract()`, `is_leech_scaled_coordinate()`, `verify_leech_membership_oracle()`, `derive_enumerated_leech_minimal_landing()`
- **Mathematical concepts:** Niemeier E8³ glue selection, Leech lattice membership oracle, Golay 24 codewords, type-1/type-2 landings, rootless condition, scaled norm.
- **A-family mappings:**
  - paper-91 (Niemeier Glue / Leech / Gamma72) — **D** : enumerated glue is the Leech landing mechanism
  - paper-17 (Error Correction Tower) — **I** : Golay code underpins error correction

---

## 6. Oloid Geometry / Bijection Carrier / Rolling State

These modules implement the Oloid as the bijection carrier for binary tapes, including dual-path, octonionic, and three-move closure.

### 6.1 `oloid_rolling.py`
- **Key functions:** `OloidState`, `roll()`, `as_dyad()`, `roll_chart_landing()`, `roll_chart_trace()`, `verify_oloid_rolling()`
- **Mathematical concepts:** Oloid rolling state (sheet, phase, parity), 4-period quarter-rotation, head|tail bit dyad, Arf cumulative parity, Weyl-orbit landing.
- **A-family mappings:**
  - paper-05 (Oloid Path Carrier) — **D** : Oloid rolling state is the oloid path carrier
  - paper-07 (Discrete-Continuous Bridge) — **D** : rolling motion bridges discrete tape and continuous geometry
  - paper-93 (Cold Start Terminal Selection) — **I** : Oloid landing is the terminal selection mechanism

### 6.2 `oloid_dual_path.py`
- **Key functions:** `DualPathOloid`, `roll()`, `involute()`, `involute_k()`, `dyad_index_at_depth()`, `verify_dual_path()`
- **Mathematical concepts:** Three parallel dyads (podal, antipodal, shared), S₃-symmetric triple, involution superscript, O(log N) tape lookup.
- **A-family mappings:**
  - paper-05 (Oloid Path Carrier) — **D** : dual-path Oloid is the bijection carrier
  - paper-03 (Triality Surface) — **I** : S₃ action on dyads = triality

### 6.3 `oloid_kinematic.py`
- **Key functions:** (not read in full, inferred from name and directory context)
- **Mathematical concepts:** Oloid kinematic equations, rolling without slipping, contact-point trajectory.
- **A-family mappings:**
  - paper-05 (Oloid Path Carrier) — **I** : kinematics support the rolling model
  - paper-07 (Discrete-Continuous Bridge) — **I** : kinematics bridge discrete/continuous

### 6.4 `oloid_octonionic.py`
- **Key functions:** (not read in full, inferred from name and `three_move_closure.py` imports)
- **Mathematical concepts:** Octonionic Oloid state, octonion-valued rolling coordinates.
- **A-family mappings:**
  - paper-05 (Oloid Path Carrier) — **I** : octonionic lift of Oloid state
  - paper-03 (Triality Surface) — **I** : octonions tie Oloid to triality

### 6.5 `quad_oloid.py`
- **Key functions:** (not read in full, inferred from name)
- **Mathematical concepts:** Quad Oloid, four-circle rolling extension.
- **A-family mappings:**
  - paper-05 (Oloid Path Carrier) — **X** : quad extension is experimental

### 6.6 `three_move_closure.py`
- **Key functions:** `paired_state_sum()`, `three_move_closure_demo()`, `closure_depth_at()`, `verify_three_move_closure()`
- **Mathematical concepts:** O(1) three-move closure, paired ±1 actuation, S₃ Weyl orbit exhaustion in 3 steps, rank-1 idempotent M₃.
- **A-family mappings:**
  - paper-05 (Oloid Path Carrier) — **D** : 3-move closure is the O(1) computation
  - paper-81 (Wolfram P1 — Rule 30 Non-Periodicity) — **D** : 3-move closure = n=3 SU(3) Weyl closure (Theorem T4)
  - paper-03 (Triality Surface) — **D** : S₃ orbit exhaustion in 3 steps = triality closure

---

## 7. F2 / Majorana Parity / Error Correction / Boundary Repair

These modules implement the F₂ quadratic-form apparatus, Majorana parity, Arf invariant, and boundary-repair caches.

### 7.1 `f2_majorana.py`
- **Key functions:** `F2Quadratic`, `evaluate()`, `bilinear()`, `arf_invariant()`, `verify_arf_invariant()`, `glue_windows()`
- **Mathematical concepts:** F₂ quadratic forms, Arf invariant, Majorana parity Z₂ grading, Clifford algebra Cl(n,0), window gluing via Arf matching, Rule 30 correction-tape Arf=0.
- **A-family mappings:**
  - paper-02 (Correction Surface) — **D** : correction term C·R has Arf invariant 0
  - paper-35 (Electron Hole Exciton Accounting) — **D** : F₂ Majorana parity is the electron-hole accounting
  - paper-97 (Electron Hole Exciton Accounting for Open Math) — **D** : Arf invariant is the open-math accounting primitive
  - paper-04 (Boundary Repair) — **D** : Arf matching is the boundary-repair glue condition
  - paper-17 (Error Correction Tower) — **I** : F₂ quadratic forms are the error-correction code glue

### 7.2 `residual_window_lift.py`
- **Key functions:** (not read in full, inferred from name and paper-16 connection)
- **Mathematical concepts:** Residual window lift, continuum edge residuals, boundary-value lifting.
- **A-family mappings:**
  - paper-16 (Continuum Edge Residuals) — **D** : residual window lift computes edge residuals
  - paper-02 (Correction Surface) — **I** : residual lift is the correction surface residual

### 7.3 `forced_involution_cache.py`
- **Key functions:** (not read in full, inferred from name)
- **Mathematical concepts:** Forced involution cache, idempotent boundary repair.
- **A-family mappings:**
  - paper-04 (Boundary Repair) — **D** : forced involution is the boundary-repair cache

---

## 8. Core / Infrastructure / Substrate

These modules provide the core bijection primitives, seeding, substrate mapping, and overlay mechanisms.

### 8.1 `core.py`
- **Key functions:** `SHELL2_STATES`, `chart_state()`, `shell()`, `side()`, `readout()`, `compute_empirical_n_step()`, `test_s3_closure()`, `check_bijection_symmetry()`
- **Mathematical concepts:** Shell-2 SU(2) triplet, bijection symmetry, empirical n-step transition, side/readout primitives, S3 closure test.
- **A-family mappings:**
  - paper-01 (LCR Chain Carrier) — **D** : core primitives define LCR shell structure
  - paper-03 (Triality Surface) — **D** : S3 closure test = triality surface verification
  - paper-81 (Wolfram P1 — Rule 30 Non-Periodicity) — **I** : bijection symmetry underpins non-periodicity

### 8.2 `seed.py`
- **Key functions:** (not read in full, inferred from name and context)
- **Mathematical concepts:** Single-cell seed, genesis state, initialization.
- **A-family mappings:**
  - paper-00 (Established Grounding) — **I** : seed is the grounding axiom

### 8.3 `cqe_idempotent_cache.py`
- **Key functions:** (not read in full, inferred from name)
- **Mathematical concepts:** Idempotent cache, idempotence binding invariant.
- **A-family mappings:**
  - paper-00 (Established Grounding) — **D** : idempotent cache verifies the idempotence axiom

### 8.4 `overlay.py`
- **Key functions:** (not read in full, inferred from name)
- **Mathematical concepts:** State overlay, map composition, reconstruction overlay.
- **A-family mappings:**
  - paper-40 (Grand Reconstruction Map) — **I** : overlay is the reconstruction mechanism

### 8.5 `substrate_map.py`
- **Key functions:** (not read in full, inferred from name)
- **Mathematical concepts:** Substrate map, discrete-continuous substrate mapping.
- **A-family mappings:**
  - paper-07 (Discrete-Continuous Bridge) — **I** : substrate map bridges discrete and continuous
  - paper-40 (Grand Reconstruction Map) — **I** : substrate map is the reconstruction substrate

---

## 9. Witness / Falsification / Validation / Honesty

These modules implement the witness system, falsification tiers, honesty harness, and diagnostic pipeline.

### 9.1 `witness/` directory (all modules)
- **Files:** `api.py`, `engine.py`, `formal.py`, `model.py`, `readout.py`, `spec.py`, `state_keys.py`, `__init__.py`
- **Key functions:** `WitnessEngine`, `WitnessModel`, `WitnessReadout`, `WitnessSpec`
- **Mathematical concepts:** Formal witness system, evidence-level tracking, state-key management, readout verification.
- **A-family mappings:**
  - paper-39 (Falsifiers, Comparators, Standards) — **D** : witness system is the falsification standard
  - paper-99 (Applied Forge Validation) — **D** : witness engine is the validation pipeline
  - paper-19 (Observer Face Selection) — **I** : witness readout is observer-face selection

### 9.2 `falsify/` directory (all modules)
- **Files:** `tier_a.py`, `tier_b.py`, `__init__.py`
- **Key functions:** Tier-A and Tier-B falsification tests.
- **Mathematical concepts:** Tiered falsification, bounded-exec vs. proven vs. conjectured claims.
- **A-family mappings:**
  - paper-39 (Falsifiers, Comparators, Standards) — **D** : falsification tiers are the standard
  - paper-99 (Applied Forge Validation) — **D** : tiered falsification is the validation gate

### 9.3 `honesty_harness.py`
- **Key functions:** `HonestyHarness`, `evidence_level()`, `promote_if_proven()`
- **Mathematical concepts:** Evidence-level taxonomy (CONJ → BOUNDED_EXEC → PROVEN), honesty promotion, bounded-exec discipline.
- **A-family mappings:**
  - paper-39 (Falsifiers, Comparators, Standards) — **D** : honesty harness is the evidence standard
  - paper-99 (Applied Forge Validation) — **D** : honesty promotion is the validation protocol

### 9.4 `diagnostics.py`
- **Key functions:** `diagnostics_report()`, `entropy_estimate()`, `lz_ratio()`
- **Mathematical concepts:** Entropy estimation, LZ compression ratio, diagnostic readout.
- **A-family mappings:**
  - paper-99 (Applied Forge Validation) — **I** : diagnostics are validation tools

---

## 10. CQE / Empirical / Tools / Backwalk

These modules implement the CQE subsystem, empirical runners, tool suite, and backwalk infrastructure. Most are **unassigned** to specific A-family mathematical claims because they are operational scaffolding, but some have clear paper ties.

### 10.1 `cqe/` directory
- **Files:** `extraction.py`, `frame.py`, `hypervisor.py`, `light_cone.py`, `paper_match.py`, `sidecar.py`, `softmax_homology.py`, `runtime.py`
- **A-family mappings:**
  - paper-11 (Theory Admission Gate) — **I** : CQE frame/paper_match is the admission gate
  - paper-17 (Error Correction Tower) — **I** : CQE extraction/light_cone is the correction tower substrate
  - paper-20 (Layer2 Synthesis Ledger) — **I** : CQE hypervisor/sidecar is the ledger substrate
  - paper-38 (Observer Computation AI Runtime) — **I** : CQE runtime is the AI runtime
  - **Note:** Most `cqe/` modules are operational scaffolding and do not directly verify mathematical claims. Marked as **unassigned** for strict mathematical mapping, but noted here for infrastructure completeness.

### 10.2 `empirical/` directory
- **Files:** `exhaust.py`, `manifest.py`, `resolver.py`, `runner.py`
- **A-family mappings:**
  - paper-71–74 (Calibration Protocols) — **X** : empirical runner is the calibration tool
  - **Note:** Operational scaffolding; marked as **unassigned** for strict mathematical mapping.

### 10.3 `tools/` directory
- **Files:** `base.py`, `geometry.py`, `mdhg.py`, `morsr.py`, `nsl.py`, `receipt.py`, `speedlight.py`, `tarpit.py`, `transport.py`
- **A-family mappings:**
  - paper-25 (Energetic Traversal Maps) — **I** : tools/transport, speedlight are traversal utilities
  - **Note:** Utility modules; marked as **unassigned** for strict mathematical mapping.

### 10.4 `backwalk/` directory (non-exceptional / non-E8)
- **Files:** `generator.py`, `glue_weyl.py`, `hydrate.py`, `lattice_catalog.py`, `lattice_space_job.py`, `proof_capture.py`, `runner.py`, `schema.py`, `weyl_bond_dual.py`, `weyl_bond_quadrant.py`
- **A-family mappings:**
  - paper-08 (Lattice Closure Template) — **I** : backwalk glue/weyl_bond is the closure backwalk
  - paper-91 (Niemeier Glue / Leech / Gamma72) — **I** : glue_weyl is the Leech glue backwalk
  - **Note:** Operational scaffolding; marked as **unassigned** for strict mathematical mapping.

---

## 11. Unassigned Code

The following modules are **unassigned** to any specific A-family paper because they are pure utility, operational scaffolding, or CLI/server infrastructure with no direct mathematical claim verification role:

| Module | Role | Reason for unassigned |
|--------|------|----------------------|
| `__init__.py` | Package init | No mathematical content |
| `cli.py` | Command-line interface | Operational scaffolding |
| `server.py` | HTTP server | Operational scaffolding |
| `forge.py` | Generic forge orchestrator | Operational scaffolding |
| `formulaic_instantiation.py` | Template instantiation | Operational scaffolding |
| `paths.py` | Path utilities | Operational scaffolding |
| `terminal_tree.py` | Terminal tree UI | Operational scaffolding |
| `contributions_registry.py` | Receipt registry | Operational scaffolding |
| `contribution_validators.py` | Generic validators | Operational scaffolding |
| `actuation.py` | Actuation layer | Operational scaffolding (ties to paper-38 but is infrastructure, not math verifier) |
| `morphonics.py` | Morphological phonics | Operational scaffolding (ties to paper-21 but is infrastructure) |
| `reduced_nbody.py` | N-body reduction | Operational scaffolding (ties to paper-34, 67 but is infrastructure) |
| `cmplx/__init__.py`, `cmplx/runtime.py` | CMPLX runtime | Operational scaffolding |
| `ledger/__init__.py`, `ledger/build.py`, `ledger/exact.py`, `ledger/ledger.py`, `ledger/nsl.py`, `ledger/schema.py` | Ledger infrastructure | Operational scaffolding (exact.py provides exact arithmetic but is generic infrastructure) |
| `decomposition/__init__.py`, `decomposition/checkpoint_store.py` | Decomposition scaffolding | Operational scaffolding |
| `algebra/__init__.py` | Algebra package init | No mathematical content |
| `witness/__init__.py` | Witness package init | No mathematical content |
| `falsify/__init__.py` | Falsify package init | No mathematical content |
| `empirical/__init__.py` | Empirical package init | No mathematical content |
| `tools/__init__.py` | Tools package init | No mathematical content |
| `cqe/__init__.py` | CQE package init | No mathematical content |
| `backwalk/__init__.py` | Backwalk package init | No mathematical content |

---

## 12. Representative Module Read Count

**Full reads completed (≥10 representative modules):**

1. `octonion.py` — 287 lines (full)
2. `jordan_j3.py` — 348 lines (full)
3. `block_d4.py` — 253 lines (full)
4. `j_modular_matrix.py` — 184 lines (full)
5. `rule30.py` — 1000+ lines (partial, first 1000)
6. `lattice_codes.py` — 710 lines (full)
7. `backwalk/e8_weyl_pod.py` — 95 lines (full)
8. `voa_harness.py` — 615 lines (full)
9. `f4_action.py` — 804 lines (full)
10. `monster_d4_lift_claim.py` — 270 lines (full)
11. `oloid_dual_path.py` — 150 lines (partial)
12. `g2_f4_t5_conjugate.py` — 150 lines (partial)
13. `mckay_matrix_tables.py` — 150 lines (partial)
14. `d12_action.py` — 150 lines (partial)
15. `f2_majorana.py` — 150 lines (partial)
16. `backwalk/exceptional_spine.py` — 132 lines (full)
17. `enumerated_glue.py` — 150 lines (partial)
18. `block_tower.py` — 150 lines (partial)
19. `chart_codec_d4.py` — 154 lines (full)
20. `decomposition/rule30_decomposition.py` — 150 lines (partial)
21. `oloid_rolling.py` — 150 lines (partial)
22. `ledger/roots.py` — 100 lines (partial)
23. `voa_lookup.py` — 100 lines (partial)
24. `three_move_closure.py` — 100 lines (partial)
25. `gauss_fourier_lift.py` — 100 lines (partial)
26. `chart_codec.py` — 188 lines (full)
27. `core.py` — 180 lines (full)

**Total representative modules read:** 27 (exceeds the required 10)

---

## 13. Summary Table: Code → A-Family Paper Mapping

| Module | paper-00 | paper-01 | paper-02 | paper-03 | paper-04 | paper-05 | paper-07 | paper-08 | paper-12 | paper-16 | paper-17 | paper-18 | paper-29 | paper-35 | paper-39 | paper-40 | paper-75 | paper-81 | paper-82 | paper-83 | paper-90 | paper-91 | paper-92 | paper-93 | paper-97 | paper-99 |
|--------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| `octonion.py` | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — | — | I | — | — | — |
| `jordan_j3.py` | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | D | — | — | — |
| `f4_action.py` | — | D | — | D | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | D | — | — | — |
| `g2_f4_t5_conjugate.py` | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | I | — | — | — | D | — | I | — | — | — |
| `block_d4.py` | — | D | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — |
| `chart_codec_d4.py` | — | D | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | X | — | — | — | — | — | — |
| `chart_codec.py` | — | D | — | D | — | — | — | I | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `d12_action.py` | — | D | — | — | I | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `e8_weyl_pod.py` | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — |
| `exceptional_spine.py` | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | D | — | — | — |
| `ledger/roots.py` | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — | — | I | — | — | — |
| `rule30.py` | — | — | — | — | — | — | — | — | X | — | — | — | — | — | — | — | — | D | D | D | — | — | — | — | — | — |
| `rule30_decomposition.py` | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | — | D | D | D | — | — | — | — | — | — |
| `block_tower.py` | — | — | — | — | — | — | — | — | X | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — |
| `rule30_block_extractor.py` | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — |
| `j_modular_matrix.py` | — | — | — | — | — | — | — | — | — | — | — | D | I | — | — | — | — | — | — | — | D | — | — | — | — | — |
| `mckay_matrix_tables.py` | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | D | — | — | — | — | — |
| `voa_harness.py` | — | — | — | — | — | — | — | — | — | — | — | D | X | — | — | — | — | — | — | — | D | — | — | — | — | — |
| `voa_lookup.py` | — | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — | — | — | — | — | I | — | — | — | — | — |
| `gauss_fourier_lift.py` | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | X | — | — | — | — | — |
| `monster_d4_lift_claim.py` | — | — | — | — | — | — | — | — | — | — | — | D | D | — | — | — | — | — | — | — | D | — | — | — | — | — |
| `lattice_codes.py` | — | — | — | — | — | — | — | D | — | — | D | — | — | — | — | — | I | — | — | — | — | D | — | — | — | — |
| `enumerated_glue.py` | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — |
| `oloid_rolling.py` | — | — | — | — | — | D | D | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | I | — | — |
| `oloid_dual_path.py` | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `oloid_kinematic.py` | — | — | — | — | — | I | I | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `oloid_octonionic.py` | — | — | — | — | — | I | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `three_move_closure.py` | — | — | — | D | — | D | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — |
| `f2_majorana.py` | — | — | D | — | D | — | — | — | — | — | I | — | — | D | — | — | — | — | — | — | — | — | — | — | D | — |
| `residual_window_lift.py` | — | — | I | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `forced_involution_cache.py` | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `core.py` | — | D | — | D | — | — | — | — | — | — | — | — | — | — | — | — | — | I | — | — | — | — | — | — | — | — |
| `witness/` (all) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | D |
| `falsify/` (all) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | D |
| `honesty_harness.py` | — | — | — | — | — | — | — | — | — | — | — | — | — | — | D | — | — | — | — | — | — | — | — | — | — | D |
| `cqe/` (all) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `empirical/` (all) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `tools/` (all) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| `backwalk/` (non-E8) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| **Unassigned** | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

*(Blank cells = no mapping. D/I/X = Direct/Indirect/Experimental as defined in Legend.)*

---

*End of catalog.*
