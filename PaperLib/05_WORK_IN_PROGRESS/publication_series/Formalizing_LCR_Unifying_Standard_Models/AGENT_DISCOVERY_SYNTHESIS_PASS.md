# Agent Discovery Synthesis Pass

Generated: 2026-06-29T22:06:12.296338+00:00

For each local target, create an internal source card, attach one or more external candidates or newly searched 2025/current papers, state the observation/correlation, run pairwise NIST/validation, classify into generalized 1-80 slots, then let the assembly audit accept/reroute/discover.

## Local Intake Targets

| Rank | Artifact family/file | Why it matters | Suggested slots |
|---|---|---|---|
| 1 | EVIDENCE_INTAKE_SCORE_NOTEBOOK.* | Already ranks candidate evidence rows and decisions. | all_by_row |
| 2 | D_DRIVE_INVENTORY_PAPER_GAP_PASS.* + D:\CQE_CMPLX\d_drive_unintegrated_inventory.csv | Best current gap map for weak/missing artifacts. | 01-79 |
| 3 | SLOT_1_80_GENERALIZED_ONTOLOGY.* | Canonical generalized slot definitions. | routing_ontology |
| 4 | ORIGINAL_80_DIMENSIONAL_RIBBON_MAP.* | Canonical 00-79 source-backed/expansion map. | 00-79 |
| 5 | ORIGINAL_80_PUBLICATION_EXPANSION_PLAN.* | Shows source-backed vs expansion-needed slots. | 33-79 |
| 6 | SOURCE_ROUTING_MATRIX.json / SOURCE_PLACEMENT_MATRIX.json | Existing FLCR source-to-paper routing. | publication_overlay, multi_slot |
| 7 | D:\CQE_CMPLX\complete_inventory.json | Broad production corpus inventory. | 00-32, publication_overlay |
| 8 | D:\CQE_CMPLX\gap_analysis\FINAL_GAP_REPORT.md + master_gap_registry_FINAL.csv | Backward-walk gap report and absorption order. | 04-09, 00-32 |
| 9 | D:\CQE_CMPLX\gap_analysis\paper_review_inventory\* | Database-first review protocol and DB source map. | ledger_action, bridge_action, window_action |
| 10 | D:\CQE_CMPLX\PAPERS_CONTENT.db / PAPERS_LINEAGE.db / PAPERS_LIVE.db | Structured paper text, lineage, topics, theorem/code/table evidence. | 00-32, all_families |
| 11 | D:\CQE_CMPLX\TMN_*.db | Tool/runtime/formalization mapping. | 01, 06, 07, 09, 11, 16, 17, 19 |
| 12 | D:\CQE_CMPLX\CMPLX-R30-main\CATALOG\*.csv | Claim/evidence/formula/term catalogs for Rule 30 corpus. | 01, 02, 03, 06, 08, 09 |
| 13 | cmplx_morphism_ledger_seed_v0_6.db | Morphism ledger for witnesses, terminal forms, transport obligations. | 03, 06, 07, 08 |
| 14 | D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\...\receipts\*.json | Machine receipts for Rule 30, E8, Leech, observer, boundary, etc. | 01, 03, 06, 08, 09, 41-79 |
| 15 | D:\CQE_CMPLX\kernel\staging\papers\suite81_claude_codex_memory\Claude work\CL-Paper-Evidence-DB\CL_proof-source-*.md | High-scoring unintegrated proof-source docs. | 01, 03, 06, 08, 09 |
| 16 | lattice-forge/docs/cqe/extracted_formalizations/texts/*.md | Extracted formalizations: D4/J3O, theorem registry, transport, Rule 30. | 01, 03, 06, 07, 08, 09 |
| 17 | D:\CQE_CMPLX\cqekernel\ + BUILD_SUMMARY.md | Stable stdlib kernel and LCR window machine. | 01, 03, 06, 08, 09 |
| 18 | D:\CQE_CMPLX\ACTUAL_COMPUTATIONAL_SUBSTRATE.md | Verified/open boundary map; prevents overclaim routing. | 02, 06, 07, 09, 42, 46, 47, 49 |
| 19 | standard_model_defining_papers\* | Current SMD/SMB bridge papers and source registry. | 41-79 |
| 20 | PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_* | Current complete pairwise package examples. | 41, 43, 46, 47, 48, 49 |

## External Pairing Candidates

| Paper | Venue/year | DOI | Pairs with | Suggested slots |
|---|---|---|---|---|
| Rethinking the production and publication of machine-readable expressions of research findings | Scientific Data 2025 | 10.1038/s41597-025-04905-0 | claim envelopes, receipt discipline, machine-readable publication outputs | 01, 11, 19, 28, 29, 40, 61, 71 |
| Provenance-driven nanopublications: representing source lineage and trust networks for multi-source assertions | International Journal on Digital Libraries 2025 | 10.1007/s00799-025-00431-x | CAM/source routing, multi-source assertions, trust/provenance graph for claims | 01, 07, 11, 28, 39, 49, 59 |
| Fast, Verified Computation for HOL ITPs | Journal of Automated Reasoning 2025 | 10.1007/s10817-025-09719-8 | forge/kernel verification, proof-producing computation, receipt-bound internal results | 01, 09, 10, 11, 19, 20, 50 |
| Fast Simulation of Cellular Automata by Self-Composition | Complex Systems 2025 | 10.25088/ComplexSystems.34.3.259 | correction surface, Rule 30/CA replay, bounded finite computation | 03, 13, 30, 43, 60 |
| Linear models of the exceptional Lie algebra e8 | Rev. Real Acad. Cienc. Exactas Fis. Nat. Ser. A-Mat. 2025 | 10.1007/s13398-025-01768-3 | D4/J3/triality surface, E6/E8 transport tower, exceptional algebra adapters | 04, 14, 18, 27, 31, 40, 58, 78 |
| Operational Quantum Reference Frame Transformations | Quantum 2025 | 10.22331/q-2025-03-27-1680 | observer-state, frame selection, relative observables | 26, 38, 47, 57, 67 |
| Measurement events relative to temporal quantum reference frames | Quantum 2025 | 10.22331/q-2025-01-30-1616 | observer delay, temporal ordering, discrete-time/windowed measurement claims | 10, 26, 27, 37, 47, 57 |
| Cabibbo-Kobayashi-Maskawa unitarity deficit reduction via finite nuclear size | Physical Review Research 2025 | 10.1103/z8g6-9j25 | TarPit/Standard Model coupling adapter, CKM residual ledger, calibrated physical-observable boundary | 16, 25, 33, 40, 56, 66, 76 |
| The fine-structure constant: a review of measurement results and possible space-time variations | Measurement Techniques 2025 | 10.1007/s11018-025-02433-2 | fine-structure/alpha adapter boundary, metrology anchors, no-fit versus calibration claims | 16, 24, 25, 33, 43, 53, 63, 73 |
| Crystal hypergraph convolutional networks | npj Computational Materials 2025 | 10.1038/s41524-025-01826-9 | CAM/crystal projection, materials descriptors, higher-order local environments | 20, 21, 28, 36, 46, 56, 66 |
| Topologically enhanced exciton transport | Nature Communications 2025 | 10.1038/s41467-025-66276-9 | electron-hole-exciton accounting, topology/transport correspondence, physical calibration lane | 34, 36, 44, 54, 64, 74 |
| A generalized platform for artificial intelligence-powered autonomous enzyme engineering | Nature Communications 2025 | 10.1038/s41467-025-61209-y | applied forge and FoldForge protein workflows, closed-loop candidate generation, external validation boundary | 22, 32, 42, 52, 62, 72 |