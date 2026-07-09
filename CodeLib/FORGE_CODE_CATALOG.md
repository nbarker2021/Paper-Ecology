# FORGE_CODE_CATALOG.md
## A-Family Verifier Catalog for D:\CQE_CMPLX Python Code

**Generated:** Catalog of all forge-related Python code in the A-family workspace, with verifier-to-paper mappings.  
**Scope:** ForgeFactory, reforge engines, rhenium engine, lattice_forge math substrate, A-family engine core, build/test/pass scripts.  
**Convention:** `D` = Definition, `I` = Implementation, `X` = eXecution/test.  
**B-family identity stripped:** All `CQE-paper-XX`, `FLCR`, `NIST`, and B-family numbering have been mapped to `paper-00`–`paper-100` or removed.

---

## 1. ForgeFactory Code (Registry, Paper Tools, CLI)

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `src/forgefactory/registry.py` | `EngineRecord`, `ENGINE_REGISTRY`, `list_engines()`, `layer_map()` — canonical registry of all forge engines (latticeforge, contracts, hardening, rhenium, paper-00 tool, morphonix) and their layered architecture. | `paper-00` (registry as baseline transport contract), `paper-10` (T10 Master Receipt registry), `paper-21` (MorphForge / PolyForge / MorphoniX planned layer) | D, I |
| `src/forgefactory/cli.py` | `main()`, `_cmd_engines()`, `_cmd_compose()`, `_cmd_paper00()`, `_cmd_smoke()` — command-line interface for engine listing, work composition, paper-00 tool invocation, and smoke-test orchestration. | `paper-00` (I, X — transport contract CLI), `paper-10` (I — compose engine CLI), `paper-11` (X — smoke test admission gate) | I, X |
| `src/forgefactory/factory.py` | `compose()`, `export_project()`, `_sha()` — composes work through the curated Rhenium path with fallback to local adapters; exports JSON receipts, world graphs, and factory registry to project directories. | `paper-00` (I — transport composition), `paper-10` (I — master receipt composition), `paper-20` (I — Layer-2 synthesis ledger export) | I |
| `src/forgefactory/papers/paper00_transport_contract.py` | `Paper00Claim`, `TransportRow`, `build_transport_row()`, `validate_transport_row()`, `run_manufacturing_example()`, `build_workbook_sheet()` — core paper-00 claim-to-receipt validator and analog workbook sheet generator. | `paper-00` (D, I, X — baseline transport contract definitions, implementation, and runnable manufacturing example) | D, I, X |
| `src/forgefactory/__init__.py` | Package init for ForgeFactory. | `paper-00` (D — package structure) | D |

---

## 2. reforge Engine Code (Contracts, Hardening, Adapters)

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `src/reforge_engine_contracts/core.py` | `LCRBlock` (dataclass with L/C/R/gamma/axis/sheet/voa_weight/correction/color_state), `GraphNode`, `GraphEdge`, `Receipt` (dataclass with blocks/nodes/edges/followup), `stable_id()`, `VALID_COLORS`, `VALID_FOLLOWUPS`, `VALID_NODE_TYPES` — shared schema types for LCR blocks, graph nodes/edges, and proof/obligation receipts. | `paper-00` (D — LCR block and receipt definitions), `paper-01` (D — LCR Chain Carrier block schema), `paper-02` (D — correction surface via `correction` field), `paper-03` (D — D4 axis/sheet labels in block) | D |
| `src/reforge_engine_contracts/validation.py` | (imported by core) Contract validation helpers. | `paper-11` (I — validation logic for theory admission) | I |
| `src/reforge_engine_hardening/health.py` | `run_health()` — runs `pytest -q` across curated engine workspaces and collects return codes, output, and timing; health-check orchestration for engine suites. | `paper-11` (I, X — theory admission gate / health check runner), `paper-00` (X — smoke test health) | I, X |
| `src/reforge_engine_hardening/unified_encode.py` | (hardening encoding utilities) | `paper-00` (I — unified encoding hardening) | I |
| `src/reforge_kimi_adapter/adapter.py` | `adapt_work_fragment()`, `batch_adapt()`, `save_receipt()`, `configure_paths()`, `WorldForgeNode`, `WorldForgeEdge` — text-to-LCR triad encoder, D4 codec wrapper, VOA weight/correction/gluon annealing, and WorldForge graph generation. | `paper-00` (I — transport adapter), `paper-01` (I — LCR chain carrier encoding), `paper-02` (I — correction surface computation), `paper-03` (I — D4 axis/sheet codec) | I |
| `src/reforge_glyphforge/cli.py` | GlyphForge CLI for document/language-demand fragment routing. | `paper-00` (I — fragment routing), `paper-19` (I — observer face-selection routing) | I |
| `src/reforge_glyphforge/fumu.py` | `analyze_text()` — semantic fragment analysis for text-to-obligation routing. | `paper-00` (I — semantic obligation routing), `paper-19` (I — observer face-selection) | I |
| `src/reforge_glyphforge/researchcraft_bridge.py` | Bridge to local-first graph/receipt persistence. | `paper-20` (I — Layer-2 synthesis ledger persistence) | I |
| `src/reforge_frameforge/motion.py` | Movement paths over wireframes. | `paper-05` (I — oloid path carrier motion), `paper-24` (I — N-dimensional chess automata motion) | I |
| `src/reforge_frameforge/__init__.py` | FrameForge package init. | `paper-05` (D — frame/wire orientation scaffolding) | D |

---

## 3. Rhenium Engine Code

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `src/rhenium_engine/orchestrator.py` | `compose_work()`, `encode_text()`, `glyph_analyze()`, `make_world_graph()`, `export_composition()` — global ReForge product composition engine: text → LCR receipt → glyph analysis → world graph → proof/obligation summary. | `paper-00` (I — global transport composition), `paper-10` (I — T10 Master Receipt orchestration), `paper-20` (I — Layer-2 synthesis composition), `paper-30` (I — Grand Ribbon Meta-Framer composition) | I |
| `src/rhenium_engine/registry.py` | `EngineRecord`, `ENGINE_REGISTRY`, `list_engines()`, `layer_map()` — Rhenium-specific registry (rhenium, kimi, worldforge, researchcraft, glyphforge, pixleforge, wireforge, frameforge, pixl8forge). | `paper-00` (D — engine registry definitions), `paper-10` (D — master receipt registry), `paper-21` (D — MorphForge/PolyForge registry layer) | D |
| `src/rhenium_engine/server.py` | Rhenium server / service wrapper. | `paper-00` (I — transport server), `paper-10` (I — receipt server) | I |
| `src/rhenium_engine/cli.py` | Rhenium CLI entry point. | `paper-00` (I — orchestration CLI), `paper-10` (I — master receipt CLI) | I |
| `src/rhenium_engine/__init__.py` | Package init. | `paper-00` (D — package structure) | D |

---

## 4. lattice_forge / Math Substrate Code

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `src/lattice_forge/core.py` | `SHELL2_STATES`, `shell()`, `side()`, `readout()`, `sequence_to_triples()`, `compute_empirical_n_step()`, `test_s3_closure()`, `check_bijection_symmetry()`, `probe()` — SU(2) doublet bijection on shell=2 stratum, S3 group-ring closure test, n-step transition matrix over GF(2), forward-tape negative-state encoding. | `paper-03` (I — D4/J3 triality and SU(2) bijection), `paper-06` (I — Causal Code / S3 closure), `paper-07` (I — Discrete-Continuous Bridge / transition matrix), `paper-08` (I — E8/Niemeier/Leech closure context) | I |
| `src/lattice_forge/forge.py` | `Forge` facade class, `extract_answer()`, `evidence_level()`, `verify_seed()`, `object()`, `can_close()`, `terminal_tree()`, `morphonics_model()`, `rule30_morphon()`, `verify_rule30()`, `rule30_vignettes()`, `rule30_moving_frame()`, `rule30_color_chirality()`, `rule30_lagrangian()`, `rule30_mandelbrot_scalar()`, `rule30_reduced_alphabet()`, `rule30_symmetry_environment()`, `rule30_physics_method_stack()`, `rule30_whole_integer_n_coverage()`, `rule30_readout_ribbon_machine()`, `rule30_dihedral_block_hypervisor()`, `rule30_hypervisor_extension_tape()`, `rule30_sheet_operator()`, `rule30_mandelbrot_field_address()`, `rule30_exit_trajectory()`, `rule30_sheet_lift()`, `rule30_julia_resolution()`, `rule30_torsor_functor_term()`, `rule30_spinor_oloid_model()`, `rule30_oloid_winding_from_n()`, `rule30_winding_number_proof()`, `rule30_nth_bit_expression()`, `rule30_proof_obligation_ledger()` — high-level facade exposing all seeded lattice-forge queries with overlay receipt tracking. | `paper-00` (X — verification runner), `paper-03` (I — D4/J3 triality), `paper-05` (I — oloid path carrier), `paper-06` (I — causal code / Rule 30), `paper-12` (I — CA Prediction Surface), `paper-21` (I — MorphForge / PolyForge) | I, X |
| `src/lattice_forge/rule30.py` | `rule30_poly()`, `poly_at()`, `monomial_stats()`, `dominant_lane()`, `hardened_beam_candidate()`, `rule30_morphon_hardened()`, `rule30_vignette_algebra()`, `rule30_moving_frame()`, `rule30_color_chirality_cipher()`, `rule30_discrete_lagrangian()`, `rule30_lagrangian_depth_trace()`, `rule30_mandelbrot_boundary_scalar()`, `rule30_mandelbrot_field_address()`, `rule30_exit_trajectory()`, `rule30_sheet_lift()`, `rule30_julia_resolution()`, `rule30_torsor_functor_term()`, `rule30_spinor_oloid_model()`, `rule30_oloid_winding_from_n()`, `rule30_oloid_antipodal_winding()`, `rule30_winding_number_proof()`, `rule30_nth_bit_expression()`, `rule30_proof_obligation_ledger()`, `rule30_readout_ribbon_machine()`, `rule30_dihedral_block_hypervisor()`, `rule30_hypervisor_extension_tape()`, `rule30_sheet_operator()`, `rule30_whole_integer_n_scalar_coverage()`, `rule30_symmetry_environment()`, `rule30_physics_method_stack()`, `rule30_reduced_alphabet_catalog()`, `verify_rule30_*()` — exhaustive Rule 30 ANF polynomial engine, beam compression, vignette composition algebra, moving frames, chirality ciphers, Lagrangian traces, Mandelbrot/Julia boundary scalars, oloid winding models, sheet operators, hypervisor tapes, and proof-obligation ledgers. | `paper-06` (I — Causal Code / Rule 30 ANF), `paper-12` (I — CA Prediction Surface), `paper-03` (I — D4/J3 Triality via lane beams), `paper-05` (I — Oloid Path Carrier / winding models), `paper-07` (I — Discrete-Continuous Bridge / Lagrangian traces), `paper-08` (I — E8/Niemeier context via boundary scalars), `paper-24` (I — N-Dimensional Chess Automata / moving frames) | I |
| `src/lattice_forge/transport_obligations.py` | `transport_obligations()`, `verify_niemeier_landing_registry()`, `verify_niemeier_root_shell_profiles()`, `verify_niemeier_direct_sum_index_one_landings()`, `verify_transport_obligations()` — explicit four-layer transport proof boundaries (LCR→D4→J3(O)→G2/F4/T5A→Niemeier), with local witness calls and open-lift tracking. | `paper-00` (D — transport obligation definitions), `paper-03` (I — D4 axis/sheet codec witness), `paper-05` (I — oloid path / G2-F4-T5A route), `paper-08` (I — E8/Niemeier/Leech Closure / landing registry), `paper-17` (I — E6-E8 Error-Correction Tower / root shell profiles) | D, I |
| `src/lattice_forge/ledger/build.py` | `NIEMEIER_FORMS`, `PARIAHS`, `MONSTER_PRIMES`, `component_root_count()`, `component_coxeter_number()`, `component_determinant()`, `terminal_discriminant_profile()`, `seed_roots()`, `seed_niemeier()`, `seed_pariahs()`, `seed_morphisms()`, `seed_morphism_witnesses()`, `seed_component_terminal_morphisms()`, `seed_terminal_glue_profiles()`, `seed_glue_templates()`, `insert_object()`, `insert_root_system()`, `insert_morphism()`, `insert_morphism_witness()`, `insert_nsl_boundary()`, `insert_prime_factor_profile()` — complete seed construction for 24 Niemeier terminals, 6 pariahs, Monster order factorization, ADE root-system exact vectors, Gram forms, reflection actions, discriminant profiles, glue-index requirements, and morphism witnesses. | `paper-08` (I — E8/Niemeier/Leech Closure), `paper-17` (I — E6-E8 Error-Correction Tower), `paper-18` (I — VOA/Moonshine Representation Routes), `paper-29` (I — Monster/Universal Energy-Bound Hypotheses), `paper-03` (I — G2/F4/D4 morphism witnesses) | I |
| `src/lattice_forge/ledger/ledger.py` | `Ledger` class — SQLite-backed registry for objects, invariants, morphisms, vectors, path metrics, discriminant profiles, RAG cards, construction status. | `paper-08` (I — Niemeier/Leech ledger), `paper-20` (I — Layer-2 Synthesis Ledger) | I |
| `src/lattice_forge/ledger/exact.py` | `matrix_json()`, `vector_json()`, `norm2()`, `dot()`, `reflect()`, `stable_hash()`, `determinant()`, `parse_vector_json()`, `parse_matrix_json()` — exact rational linear algebra for root-system computations. | `paper-08` (I — exact root-system arithmetic), `paper-03` (I — D4 exact reflection actions) | I |
| `src/lattice_forge/ledger/roots.py` | `RootSystemData`, `core_root_systems()`, `component_root_system()`, `direct_sum_root_system()`, `parse_root_system_label()` — exact ADE root system data generation and parsing. | `paper-08` (I — ADE root system exact data), `paper-17` (I — E6-E8 root systems) | I |
| `src/lattice_forge/ledger/schema.py` | SQL schema definitions for the Ledger (object_registry, gram_forms, exact_vectors, invariants, morphisms, adjacency, path_metrics, etc.). | `paper-08` (D — ledger schema), `paper-20` (D — synthesis ledger schema) | D |
| `src/lattice_forge/ledger/nsl.py` | `NSLTerm` — Noether-Shannon-Landauer boundary term computation. | `paper-16` (I — Continuum Edge Residuals / NSL boundary), `paper-09` (I — Hamiltonian Temporal Emergence) | I |
| `src/lattice_forge/morphonics.py` | `morphonics_model_v0_2()`, `verify_morphonics_model()` — terminal-tree verification → morphonics model generation. | `paper-21` (I — MorphForge / PolyForge / MorphoniX) | I |
| `src/lattice_forge/overlay.py` | `OverlayStore` — SQLite overlay for receipts, events, queries. | `paper-00` (I — receipt overlay), `paper-20` (I — synthesis ledger overlay) | I |
| `src/lattice_forge/seed.py` | `SeedStore` — seeded object database with integrity checks. | `paper-00` (I — seed integrity), `paper-08` (I — Niemeier seed store) | I |
| `src/lattice_forge/chart_codec.py` | LCR chart encoding/decoding primitives. | `paper-01` (I — LCR Chain Carrier codec), `paper-00` (I — baseline transport codec) | I |
| `src/lattice_forge/chart_codec_d4.py` | `encode_d4()`, `decode_d4()`, `verify_chart_codec_d4()` — D4 axis/sheet codec for LCR triads with round-trip verification. | `paper-03` (I — D4/J3 Triality codec), `paper-00` (I — transport codec witness) | I |
| `src/lattice_forge/centroid_voa.py` | `gluon()`, `voa_weight()`, `anneal_to_lie_conjugate()` — VOA (Vertex Operator Algebra) weight and gluon gamma computations, Lie-conjugate annealing. | `paper-18` (I — VOA/Moonshine Representation Routes), `paper-02` (I — correction surface / gluon gamma) | I |
| `src/lattice_forge/f4_action.py` | F4 group action decompositions. | `paper-03` (I — F4 action / D4/J3 triality), `paper-17` (I — E6-E8 tower / F4 subalgebra) | I |
| `src/lattice_forge/g2_f4_t5_conjugate.py` | `verify_conjugate_triple()` — G2 → F4 → T5A conjugate route verification. | `paper-03` (I — G2/F4/T5A conjugate route), `paper-05` (I — oloid path carrier / conjugate route) | I |
| `src/lattice_forge/jordan_j3.py` | `verify_j3o_axioms()` — J3(O) Jordan algebra diagonal carrier and trace-2 idempotent axioms. | `paper-03` (I — J3(O) diagonal carrier / triality), `paper-05` (I — oloid path / J3(O) carrier) | I |
| `src/lattice_forge/octonion.py` | Octonion multiplication and norm structures. | `paper-03` (I — J3(O) / octonion substrate), `paper-07` (I — Discrete-Continuous Bridge / octonion norms) | I |
| `src/lattice_forge/cayley_dickson_oloid.py` | Cayley-Dickson construction for oloid algebra. | `paper-05` (I — oloid path carrier / Cayley-Dickson), `paper-03` (I — triality via Cayley-Dickson) | I |
| `src/lattice_forge/oloid_*.py` | Multiple oloid modules: `oloid_predictor.py`, `oloid_rolling.py`, `oloid_dual_path.py`, `oloid_octonionic.py`, `oloid_model_selection.py`, `quad_oloid.py` — oloid parameterization, winding, antipodal paths, dual-path routing, model selection. | `paper-05` (I — Oloid Path Carrier), `paper-07` (I — Discrete-Continuous Bridge / oloid paths), `paper-24` (I — N-Dimensional Chess Automata / oloid routing) | I |
| `src/lattice_forge/nebe_gamma72.py` | Nebe γ72 lattice constructions. | `paper-08` (I — Niemeier/Leech / Nebe construction), `paper-18` (I — VOA/Moonshine / γ72) | I |
| `src/lattice_forge/unipotent_orbits.py` | Unipotent orbit classification. | `paper-08` (I — E8/Niemeier / unipotent orbits), `paper-29` (I — Monster/energy-bound / orbit structure) | I |
| `src/lattice_forge/universal_frame.py` | Universal frame template for boundary orientation. | `paper-04` (I — Boundary Repair / universal frame), `paper-19` (I — Observer Face-Selection / universal frame) | I |
| `src/lattice_forge/temporal_z4_scope.py` | Z4 temporal scope for positional encoding replacement. | `paper-09` (I — Hamiltonian Temporal Emergence / Z4 scope), `paper-07` (I — Discrete-Continuous Bridge / Z4) | I |
| `src/lattice_forge/substrate_map.py` | Substrate mapping for computational carrier layers. | `paper-00` (I — baseline transport substrate), `paper-13` (I — Standard-Model Quark-Face Transport / substrate) | I |
| `src/lattice_forge/binary_boundary_adapter.py` | `adapt()` — binary-to-boundary adapter for bit streams. | `paper-00` (I — binary boundary adapter), `paper-01` (I — LCR chain carrier / binary adapter) | I |
| `src/lattice_forge/block_d4.py`, `block_tower.py` | D4 block constructions and block-tower stacking. | `paper-03` (I — D4/J3 Triality / block constructions), `paper-17` (I — E6-E8 Error-Correction Tower / block tower) | I |
| `src/lattice_forge/d12_action.py` | D12 action group. | `paper-08` (I — D12 Niemeier terminal action), `paper-03` (I — D4/D12 triality actions) | I |
| `src/lattice_forge/f2_majorana.py` | F2 Majorana operator models. | `paper-13` (I — Standard-Model Quark-Face Transport / Majorana operators), `paper-15` (I — QFT/Higgs Mass-Residue / Majorana) | I |
| `src/lattice_forge/lattice_codes.py` | Lattice code constructions (Leech, Niemeier). | `paper-08` (I — E8/Niemeier/Leech lattice codes), `paper-17` (I — E6-E8 Error-Correction Tower / lattice codes) | I |
| `src/lattice_forge/voa_lookup.py`, `cmplx_lookup_cache.py` | VOA lookup tables and cache. | `paper-18` (I — VOA/Moonshine lookup), `paper-02` (I — correction surface lookup cache) | I |
| `src/lattice_forge/cqe_app.py` | A-family application wrapper. | `paper-00` (I — app wrapper), `paper-20` (I — synthesis app) | I |
| `src/lattice_forge/cqe_rule30_solver.py` | Rule 30 solver application. | `paper-06` (I — Causal Code solver), `paper-12` (I — CA Prediction Surface solver) | I |
| `src/lattice_forge/enumerated_glue.py` | Enumerated glue codes for overlattice construction. | `paper-08` (I — Niemeier glue codes), `paper-17` (I — E6-E8 tower glue) | I |
| `src/lattice_forge/terminal_tree.py` | Terminal tree construction for object hierarchies. | `paper-08` (I — Niemeier terminal tree), `paper-20` (I — synthesis terminal tree) | I |
| `src/lattice_forge/contributions_registry.py`, `contribution_validators.py` | Contribution registry and validators. | `paper-00` (I — contribution registry), `paper-11` (I — theory admission validators) | I |
| `src/lattice_forge/unified_tarpit.py` | Unified tarpit / sink for unresolved obligations. | `paper-00` (I — obligation tarpit), `paper-16` (I — Continuum Edge Residuals / tarpit) | I |

---

## 5. A-Family Engine Core (cqe_engine / lib-forge)

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `cqe-production-v0.1/lib-forge/cqe_engine/registry.py` | `Registry` class, `PAPERS_32`, `_load_all()`, `arity_table()` — loads the 32 canonical A-family papers (paper-00 through paper-31) from anchor INTENT.md files. | `paper-00` through `paper-31` (D — paper registry and canonical ordering; I — loading implementation) | D, I |
| `cqe-production-v0.1/lib-forge/cqe_engine/paper.py` | `Paper` dataclass, `fill_default_slots()` — paper with Ribbon and back-propagation list; fills C (center/title) and A (citation anchor) slots by default. | `paper-00` (D — paper structure definition), `paper-10` (D — receipt structure), `paper-20` (D — synthesis paper structure) | D |
| `cqe-production-v0.1/lib-forge/cqe_engine/ribbon.py` | `Ribbon`, `Slot`, `SlotName` (L, C, R, B, T, O, A, W) — 8-slot ribbon with source-kind tracking (binary, vector, binary+vector). | `paper-00` (D — ribbon slot definitions), `paper-01` (D — LCR slot schema), `paper-10` (D — master receipt ribbon) | D |
| `cqe-production-v0.1/lib-forge/cqe_engine/transport.py` | `transport()`, `Receipt` dataclass — applies a tool to a ribbon, computes obligation delta (closed/opened slots), writes receipt JSON to `proof-receipts/paper-NN/<tool>/`. | `paper-00` (I — baseline transport contract implementation), `paper-02` (I — correction surface transport) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/hydrate.py` | `hydrate()`, `HydrationResult` — rehydrates action map from filled ribbon slots; reports obligated (empty) slots and arity. | `paper-00` (I — hydration / obligation detection), `paper-02` (I — correction surface hydration) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/backprop.py` | `back_propagate()`, `BackPropRecord` — fills a ribbon slot from a D:/ artifact, records provenance and source-kind. | `paper-00` (I — artifact back-propagation), `paper-02` (I — correction surface back-propagation) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/arity.py` | `arity_report()`, `ArityReport` — computes arity (filled slot count) and obligation status for papers. | `paper-00` (I — arity computation), `paper-11` (I — theory admission arity check) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/paths.py` | `anchor()`, `paper_dir()`, `receipt_path()` — path resolution for paper directories and receipt storage. | `paper-00` (I — path resolution), `paper-10` (I — receipt path resolution) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/foundation.py` | Foundation module for A-family engine boot. | `paper-00` (I — engine foundation), `paper-11` (I — theory admission foundation) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/hamiltonian_windows.py` | Hamiltonian window computations. | `paper-09` (I — Hamiltonian Temporal Emergence), `paper-07` (I — Discrete-Continuous Bridge / Hamiltonian windows) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/normalization_braces.py` | Normalization brace structures. | `paper-02` (I — correction surface normalization), `paper-16` (I — Continuum Edge Residuals / braces) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/scope.py` | Scope management for paper contexts. | `paper-00` (I — transport scope), `paper-19` (I — Observer Face-Selection / scope) | I |
| `cqe-production-v0.1/lib-forge/cqe_engine/_boot.py` | Engine boot launcher. | `paper-00` (X — boot execution), `paper-11` (X — admission gate boot) | X |
| `cqe-production-v0.1/lib-forge/cqe_engine/_validate.py` | Engine validation script. | `paper-00` (X — validation), `paper-11` (X — admission validation) | X |
| `cqe-production-v0.1/lib-forge/cqe_shared_memory/memory.py` | Shared memory module for cross-paper state. | `paper-20` (I — Layer-2 Synthesis Ledger / shared memory), `paper-27` (I — Observer Delay and Shared Reality / shared memory) | I |
| `cqe-production-v0.1/lib-forge/cqe_shared_memory/jacobian.py` | Jacobian computation for shared memory updates. | `paper-07` (I — Discrete-Continuous Bridge / Jacobian), `paper-14` (I — GR Boundary-Repair Curvature / Jacobian) | I |
| `cqe-production-v0.1/lib-forge/cqe_shared_memory/socratic.py` | Socratic query interface for shared memory. | `paper-19` (I — Observer Face-Selection / socratic query), `paper-27` (I — Observer Delay / socratic) | I |
| `cqe-production-v0.1/lib-forge/CQE_spawner/scan.py`, `emit.py`, `spawn.py` | Spawner suite: scan, emit, spawn for paper-runner orchestration. | `paper-00` (I — transport spawner), `paper-10` (I — master receipt spawner), `paper-20` (I — synthesis spawner) | I |
| `cqe-production-v0.1/lib-forge/CQE_spawner_patent/spawn_patent.py`, `templates.py` | Patent spawner and templates. | `paper-22` (I — MetaForge Applied Materials / patent spawning), `paper-00` (I — transport patent templates) | I |
| `cqe-production-v0.1/papers/02-CQE-tool/run.py` | Paper-02 tool runner (correction surface). | `paper-02` (X — correction surface runner) | X |

---

## 6. Test Scripts, Pass Scripts, Build Scripts

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `cqe-production-v0.1/tests/test_cqe_engine.py` | `test_registry_loads_32_papers()`, `test_default_arity_is_2_of_8()`, `test_hydrate_default_lists_obligations()`, `test_back_propagate_records_and_fills()`, `test_back_propagate_rejects_bad_source_kind()`, `test_transport_writes_receipt_and_closes_obligations()` — full pytest suite for registry, arity, hydration, back-propagation, transport, and receipt writing. | `paper-00` (X — engine test), `paper-02` (X — correction surface test), `paper-10` (X — receipt test), `paper-11` (X — theory admission test) | X |
| `cqe-production-v0.1/tests/test_paper00_runs.py` | `test_paper00_runs_clean()` — smoke test that runs the paper-00 tool and asserts PASS in stdout. | `paper-00` (X — smoke test / pass script) | X |
| `cqe-production-v0.1/tests/test_fermionic_bosonic.py` | Fermionic/bosonic paper tests. | `paper-13` (X — Standard-Model Quark-Face Transport), `paper-15` (X — QFT/Higgs Mass-Residue) | X |
| `cqe-production-v0.1/tests/test_shared_memory.py` | Shared memory tests. | `paper-20` (X — Layer-2 Synthesis Ledger), `paper-27` (X — Observer Delay and Shared Reality) | X |
| `forgefactory-v0.3-lineage-read/ForgeFactory_v0_3/tests/test_forgefactory_smoke.py` | ForgeFactory smoke tests. | `paper-00` (X — forgefactory smoke), `paper-10` (X — master receipt smoke) | X |
| `forgefactory-v0.3-lineage-read/ForgeFactory_v0_3/tests/test_latticeforge_integration.py` | LatticeForge integration tests. | `paper-03` (X — D4/J3 integration), `paper-06` (X — Rule 30 integration), `paper-08` (X — Niemeier integration) | X |
| `forgefactory-v0.3-lineage-read/ForgeFactory_v0_3/tests/test_paper00_tool.py` | Paper-00 tool tests. | `paper-00` (X — paper-00 tool test) | X |
| `test_imports.py` (root) | Root-level import sanity test. | `paper-00` (X — import sanity), `paper-11` (X — admission gate import test) | X |
| `CMPLX-Kernel-runtime/boot.py` | Kernel runtime boot script. | `paper-00` (X — runtime boot), `paper-10` (X — master receipt runtime boot) | X |
| `CMPLX-Kernel-runtime/cmplx_kernel/adapters.py` | Kernel runtime adapters. | `paper-00` (I — runtime adapter), `paper-01` (I — LCR runtime adapter) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/diagnostics.py` | Kernel diagnostics. | `paper-11` (I — theory admission diagnostics), `paper-00` (I — baseline diagnostics) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/schemas.py` | Kernel runtime schemas. | `paper-00` (D — runtime schema), `paper-10` (D — receipt schema) | D |
| `CMPLX-Kernel-runtime/cmplx_kernel/state_store.py` | State store for kernel runtime. | `paper-20` (I — Layer-2 synthesis state store), `paper-00` (I — baseline state store) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/token_sidecar.py` | Token sidecar for runtime authentication. | `paper-00` (I — token sidecar), `paper-19` (I — observer face-selection / token sidecar) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/operator_server.py` | Operator server for kernel runtime. | `paper-00` (I — operator server), `paper-10` (I — master receipt server) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/operator_security.py` | Security module for kernel runtime. | `paper-11` (I — theory admission security), `paper-19` (I — observer face-selection security) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/docker_adapter.py` | Docker adapter for kernel runtime. | `paper-00` (I — container adapter), `paper-22` (I — MetaForge / Docker adapter) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/kernel_explorer.py` | Kernel explorer / introspection tool. | `paper-00` (I — kernel introspection), `paper-20` (I — synthesis explorer) | I |
| `CMPLX-Kernel-runtime/cmplx_kernel/module_registry.py` | Module registry for kernel runtime. | `paper-00` (I — module registry), `paper-10` (I — master receipt module registry) | I |
| `CMPLX-Kernel_CuratedRepoForms_*/kernel/cmplx_kernel/*.py` | Curated repo forms of kernel modules (adapters, diagnostics, schemas, token_sidecar) — identical semantics to runtime versions above. | Same mappings as corresponding runtime files. | D, I, X |
| `CQE-engine-mirror/*.{py}` | Mirror copies of engine core (`arity.py`, `backprop.py`, `hydrate.py`, `registry.py`, `ribbon.py`, `transport.py`, `_boot.py`, `_probe.py`) — identical verifier semantics. | Same mappings as `cqe-production-v0.1/lib-forge/cqe_engine/` counterparts. | D, I, X |
| `CQE-engine-v0.1/cqe_engine/*.py` | v0.1 engine source (`arity.py`, `backprop.py`, `hydrate.py`, `paper.py`, `paths.py`, `registry.py`, `ribbon.py`, `transport.py`, `_boot.py`) — earlier lineage, same paper mappings. | Same mappings as production engine counterparts. | D, I, X |
| `CQECMPLX-Production/lib-forge/cqe-paper-00__axiom_00_*/run.py` | Paper-00 axiom runners (axiom_00_1 through axiom_00_4). | `paper-00` (X — axiom runners) | X |
| `CQECMPLX-Production/lib-forge/cqe-paper-00__lemma_00_*/run.py` | Paper-00 lemma runners (lemma_00_1 through lemma_00_3). | `paper-00` (X — lemma runners) | X |
| `CQECMPLX-Production/papers/CQE-paper-00/02-CQE-tool/run.py` | Production paper-00 tool runner. | `paper-00` (X — production tool runner) | X |

---

## 7. API Server & Workspace Orchestration

| File | Key Functions / Concepts | A-Family Paper Verification | D/I/X |
|------|--------------------------|----------------------------|-------|
| `api.py` (workspace root) | FastAPI server: `Workspace` loader, `dashboard()`, `agent_probe()`, `health()`, `list_units()`, `unit_info()`, `list_groups()`, `git_summary()`, `environment()`, `status()`, `validate()`, `server_info()`, `frontier_info()`, `frontier_think()`, `frontier_generate()`, `frontier_reason()`, `frontier_learn()`, `runtime_info()`, `runtime_status()`, `flcr_papers()` → mapped to `papers()`, `flcr_verify_paper()` → mapped to `verify_paper()`, `lattice_rule30()`, `projector_run()`, `uft_papers()`, `uft_stats()`, `cap_search()`, `cap_by_classification()`, `cap_by_import()`, `cap_by_path()`, `cap_overview()`, `cap_file_detail()` — workspace server for humans and agents, frontier model stubs, runtime endpoints, capability query index, and unified paper registry. | `paper-00` (I — workspace API), `paper-10` (I — runtime / master receipt API), `paper-19` (I — observer face-selection / projector API), `paper-20` (I — Layer-2 synthesis / capability query API), `paper-30` (I — Grand Ribbon Meta-Framer / frontier API), `paper-06` (I — Rule 30 lattice endpoint), `paper-12` (I — CA Prediction Surface endpoint) | I |

**Note on `api.py` B-family stripping:** The original file contains `FLCR` terminology in runtime endpoint paths (`/runtime/flcr/*`). These are mapped to A-family paper endpoints (`/runtime/papers/*`, `/runtime/verify/*`) in this catalog. The `uft_papers()` and `uft_stats()` endpoints are retained as A-family paper registry queries (papers 0–100). The `MannyAI` frontier model references are noted as unassigned scaffolding (see below).

---

## 8. Unassigned Code

The following code **cannot be directly mapped** to a specific A-family paper claim (paper-00 through paper-100) because it is either infrastructure scaffolding, external model stubs, or B-family-specific branding that does not correspond to an A-family mathematical or operational claim:

| File / Code Region | Reason for Unassignment |
|-------------------|------------------------|
| `api.py` — `MannyAI Frontier Model` stubs (`frontier_think`, `frontier_generate`, `frontier_reason`, `frontier_learn`) | External model scaffolding; not a verifier for any A-family paper claim. The frontier model is a placeholder/stub for a future AI architecture, not a proof or implementation of papers 0–100. |
| `api.py` — `CapabilityIndex` query tool (`cap_search`, `cap_by_classification`, etc.) | Workspace metadata tooling; useful for agent navigation but not a verifier for any specific paper claim. |
| `src/forgefactory/morphonix/spec.py`, `__init__.py` | Planned future layer (grid sweep, bifurcations, token/form database). Status is `"planned"`; no executable claims to verify yet. |
| `src/lattice_forge/cqe_app.py` (app wrapper only) | Thin application wrapper without mathematical claims. |
| `src/reforge_researchcraft`, `src/reforge_pixleforge`, `src/reforge_wireforge`, `src/reforge_pixl8forge` | Image/pixel/video/orientation engine modules that are **registered** but their internal implementations were not fully readable in the representative sample. They are listed as registered engines in the registry but their verifiable claims await deeper inspection. |
| `CMPLX-Kernel/CMPLX-Kernel_Production_*/source/CQE_CMPLX-workspace/build_cache.py` | Workspace build cache; pure infrastructure. |
| `CMPLX-Kernel/CMPLX-Kernel_Production_*/source/CQE_CMPLX-workspace/CMPLX-PartsFactory-main/docs/identity-review-wave-*/scripts/run_*.py` | Identity-review wave scripts (bootstrap, hash lanes, docker smoke, compose profile, runtime wiring). These are **integration smoke tests** for workspace hygiene, not verifiers for A-family mathematical claims. They verify infrastructure health, not paper claims. |
| `CMPLX-Kernel/CMPLX-Kernel_Production_*/source/CQE_CMPLX-nonlib-forge-files/CMPLX-PartsFactory-main/tests/worlds/test_forge_*.py` | Test files for non-library forge provider/witness worlds; integration-level, not paper-claim verifiers. |
| `forgefactory-v0.3-lineage-read/ForgeFactory_v0_3/build/lib/*` | Build artifacts (copies of `src/`); redundant with source mappings. |
| `CQECMPLX-Formal-Suite/lib/src/rhenium_engine/*.py` | Formal-suite copies of rhenium engine; same mappings as `src/rhenium_engine/` but noted as duplicate lineage. |
| `.venv` / `site-packages` | External dependencies (FastAPI, Click, etc.); not A-family code. |

---

## 9. Summary Tables

### 9.1 Paper Coverage Matrix

| A-Family Paper | Title | Verifying Files (representative) | D/I/X Count |
|----------------|-------|----------------------------------|---------------|
| `paper-00` | Baseline Transport Contract | `forgefactory/papers/paper00_transport_contract.py`, `cqe_engine/transport.py`, `cqe_engine/hydrate.py`, `cqe_engine/backprop.py`, `reforge_kimi_adapter/adapter.py`, `forgefactory/cli.py`, `forgefactory/factory.py`, `rhenium_engine/orchestrator.py`, `lattice_forge/transport_obligations.py`, `api.py`, `test_paper00_runs.py`, `test_cqe_engine.py` | D: 8, I: 12, X: 8 |
| `paper-01` | LCR Chain Carrier | `reforge_engine_contracts/core.py`, `reforge_kimi_adapter/adapter.py`, `lattice_forge/chart_codec.py`, `lattice_forge/core.py` | D: 4, I: 4 |
| `paper-02` | Correction Surface | `reforge_engine_contracts/core.py`, `reforge_kimi_adapter/adapter.py`, `cqe_engine/backprop.py`, `cqe_engine/transport.py`, `cqe_engine/hydrate.py`, `lattice_forge/centroid_voa.py`, `cqe_engine/normalization_braces.py` | D: 2, I: 6 |
| `paper-03` | D4/J3 Triality | `lattice_forge/core.py`, `lattice_forge/forge.py`, `lattice_forge/rule30.py`, `lattice_forge/chart_codec_d4.py`, `lattice_forge/f4_action.py`, `lattice_forge/g2_f4_t5_conjugate.py`, `lattice_forge/jordan_j3.py`, `lattice_forge/octonion.py`, `lattice_forge/cayley_dickson_oloid.py`, `lattice_forge/block_d4.py`, `lattice_forge/ledger/build.py` | D: 3, I: 11 |
| `paper-04` | Boundary Repair | `lattice_forge/universal_frame.py`, `lattice_forge/binary_boundary_adapter.py` | D: 1, I: 2 |
| `paper-05` | Oloid Path Carrier | `lattice_forge/forge.py`, `lattice_forge/rule30.py`, `lattice_forge/g2_f4_t5_conjugate.py`, `lattice_forge/jordan_j3.py`, `lattice_forge/oloid_*.py`, `lattice_forge/cayley_dickson_oloid.py`, `lattice_forge/reforge_frameforge/motion.py` | I: 8 |
| `paper-06` | Causal Code | `lattice_forge/core.py`, `lattice_forge/forge.py`, `lattice_forge/rule30.py`, `lattice_forge/cqe_rule30_solver.py`, `api.py` | I: 6, X: 1 |
| `paper-07` | Discrete-Continuous Bridge | `lattice_forge/core.py`, `lattice_forge/rule30.py`, `lattice_forge/temporal_z4_scope.py`, `cqe_engine/hamiltonian_windows.py`, `cqe_shared_memory/jacobian.py` | I: 5 |
| `paper-08` | E8/Niemeier/Leech Closure | `lattice_forge/ledger/build.py`, `lattice_forge/ledger/ledger.py`, `lattice_forge/ledger/exact.py`, `lattice_forge/ledger/roots.py`, `lattice_forge/transport_obligations.py`, `lattice_forge/nebe_gamma72.py`, `lattice_forge/lattice_codes.py`, `lattice_forge/unipotent_orbits.py`, `lattice_forge/enumerated_glue.py` | D: 2, I: 9 |
| `paper-09` | Hamiltonian Temporal Emergence | `lattice_forge/temporal_z4_scope.py`, `cqe_engine/hamiltonian_windows.py` | I: 2 |
| `paper-10` | T10 Master Receipt | `forgefactory/registry.py`, `rhenium_engine/orchestrator.py`, `rhenium_engine/registry.py`, `cqe_engine/registry.py`, `cqe_engine/paper.py`, `api.py`, `forgefactory/factory.py` | D: 5, I: 4, X: 1 |
| `paper-11` | Theory Admission Gate | `reforge_engine_hardening/health.py`, `cqe_engine/arity.py`, `cqe_engine/_validate.py`, `cqe_engine/_boot.py`, `test_cqe_engine.py`, `test_imports.py` | I: 3, X: 4 |
| `paper-12` | CA Prediction Surface | `lattice_forge/forge.py`, `lattice_forge/rule30.py`, `api.py` | I: 3, X: 1 |
| `paper-13` | Standard-Model Quark-Face Transport | `lattice_forge/f2_majorana.py`, `lattice_forge/substrate_map.py` | I: 2 |
| `paper-14` | GR Boundary-Repair Curvature | `cqe_shared_memory/jacobian.py` | I: 1 |
| `paper-15` | QFT/Higgs Mass-Residue Carrier | `lattice_forge/f2_majorana.py` | I: 1 |
| `paper-16` | Continuum Edge Residuals | `lattice_forge/ledger/nsl.py`, `lattice_forge/unified_tarpit.py`, `cqe_engine/normalization_braces.py` | I: 3 |
| `paper-17` | E6-E8 Error-Correction Tower | `lattice_forge/ledger/build.py`, `lattice_forge/ledger/roots.py`, `lattice_forge/block_tower.py`, `lattice_forge/lattice_codes.py`, `lattice_forge/enumerated_glue.py` | I: 5 |
| `paper-18` | VOA/Moonshine Representation Routes | `lattice_forge/centroid_voa.py`, `lattice_forge/voa_lookup.py`, `lattice_forge/nebe_gamma72.py` | I: 3 |
| `paper-19` | Observer Face-Selection | `api.py` (projector), `reforge_glyphforge/cli.py`, `cqe_engine/scope.py`, `cqe_shared_memory/socratic.py`, `kernel/token_sidecar.py`, `kernel/operator_security.py` | I: 4 |
| `paper-20` | Layer-2 Synthesis Ledger | `forgefactory/factory.py`, `rhenium_engine/orchestrator.py`, `lattice_forge/ledger/ledger.py`, `lattice_forge/overlay.py`, `lattice_forge/seed.py`, `cqe_shared_memory/memory.py`, `kernel/state_store.py`, `kernel/kernel_explorer.py` | I: 6 |
| `paper-21` | MorphForge / PolyForge / MorphoniX | `forgefactory/registry.py` (planned), `lattice_forge/forge.py`, `lattice_forge/morphonics.py`, `forgefactory/morphonix/spec.py` | D: 2, I: 3 |
| `paper-22` | MetaForge Applied Materials | `CQE_spawner_patent/spawn_patent.py`, `kernel/docker_adapter.py` | I: 2 |
| `paper-23` | FoldForge Protein Folding | — | No direct verifier found in sampled code. |
| `paper-24` | KnightForge / N-Dimensional Chess Automata | `lattice_forge/rule30.py` (moving frame), `reforge_frameforge/motion.py`, `lattice_forge/oloid_*.py` | I: 3 |
| `paper-25` | Energetic Traversal Maps | — | No direct verifier found in sampled code. |
| `paper-26` | Z-Pinch and Shear Horizon | — | No direct verifier found in sampled code. |
| `paper-27` | Observer Delay and Shared Reality | `cqe_shared_memory/memory.py`, `cqe_shared_memory/socratic.py`, `tests/test_shared_memory.py` | I: 2, X: 1 |
| `paper-28` | N-Dimensional Game Lattices | — | No direct verifier found in sampled code. |
| `paper-29` | Monster/Universal Energy-Bound Hypotheses | `lattice_forge/ledger/build.py` (Monster/pariah seeding), `lattice_forge/unipotent_orbits.py` | I: 2 |
| `paper-30` | Grand Ribbon Meta-Framer | `rhenium_engine/orchestrator.py`, `api.py` (frontier/runtime) | I: 2 |
| `paper-31` | It Was Still Just LCR | `cqe_engine/registry.py` (paper-31 in 32-paper list), `lattice_forge/core.py` (LCR bijection) | D: 1, I: 1 |
| `paper-32` – `paper-100` | (A-family papers beyond the 32-paper seed) | — | No direct verifiers in this codebase. The engine is designed to scale; these papers await claim ledger insertion. |

### 9.2 Engine-Layer to Paper Mapping

| Engine Layer | Primary Code Location | Verified Papers |
|--------------|------------------------|-----------------|
| **Math Substrate** (Rule30, D4, J3, VOA, oloid, Leech/Niemeier) | `lattice_forge/*.py` | `paper-03`, `paper-05`, `paper-06`, `paper-07`, `paper-08`, `paper-12`, `paper-17`, `paper-18`, `paper-24`, `paper-29` |
| **Contract / Schema** (LCR, Graph, Receipt) | `reforge_engine_contracts/core.py` | `paper-00`, `paper-01`, `paper-02`, `paper-03` |
| **Hardening / Health** | `reforge_engine_hardening/*.py` | `paper-11`, `paper-00` |
| **Adapter / Encoding** | `reforge_kimi_adapter/adapter.py` | `paper-00`, `paper-01`, `paper-02`, `paper-03` |
| **Orchestration / Composition** | `rhenium_engine/orchestrator.py`, `forgefactory/factory.py` | `paper-00`, `paper-10`, `paper-20`, `paper-30` |
| **Registry / Metadata** | `forgefactory/registry.py`, `rhenium_engine/registry.py`, `cqe_engine/registry.py` | `paper-00`–`paper-31` (D), `paper-10` (D) |
| **Transport / Hydration** | `cqe_engine/transport.py`, `cqe_engine/hydrate.py`, `cqe_engine/backprop.py` | `paper-00`, `paper-02` |
| **Ledger / Root Systems** | `lattice_forge/ledger/*.py` | `paper-08`, `paper-17`, `paper-18`, `paper-20`, `paper-29` |
| **API / Runtime** | `api.py`, `kernel/*.py` | `paper-00`, `paper-10`, `paper-19`, `paper-20`, `paper-30` |
| **Tests / Pass Scripts** | `tests/test_*.py`, `run.py`, `_validate.py` | `paper-00`–`paper-31` (X) |

---

## 10. Representative Files Read (≥ 17 files)

The following files were read **in full** to produce this catalog:

1. `forgefactory/registry.py` — engine registry and layer map
2. `forgefactory/cli.py` — CLI entry point
3. `forgefactory/factory.py` — composition and export
4. `reforge_engine_contracts/core.py` — LCRBlock, GraphNode, GraphEdge, Receipt schemas
5. `reforge_engine_hardening/health.py` — engine health runner
6. `rhenium_engine/orchestrator.py` — global compose_work orchestrator
7. `rhenium_engine/registry.py` — rhenium engine registry
8. `lattice_forge/core.py` — SU(2) triplet, S3 closure, bijection symmetry
9. `lattice_forge/forge.py` — Forge facade, rule30 verifiers, morphonics
10. `cqe_engine/registry.py` — 32-paper A-family registry
11. `cqe_engine/paper.py` — Paper dataclass with Ribbon
12. `test_paper00_runs.py` — paper-00 smoke test
13. `api.py` — workspace FastAPI server
14. `lattice_forge/transport_obligations.py` — four-layer transport obligations
15. `cqe_engine/backprop.py` — artifact back-propagation
16. `forgefactory/papers/paper00_transport_contract.py` — paper-00 transport contract tool
17. `test_cqe_engine.py` — full CQE engine pytest suite
18. `lattice_forge/ledger/build.py` — Niemeier forms, root systems, discriminant profiles
19. `lattice_forge/rule30.py` — Rule 30 ANF, vignette algebra, moving frame (partial read, first 1000 lines)
20. `cqe_engine/transport.py` — transport with receipt
21. `cqe_engine/hydrate.py` — hydration of ribbon slots
22. `reforge_kimi_adapter/adapter.py` — text-to-LCR/D4/VOA adapter

---

*End of catalog.*
