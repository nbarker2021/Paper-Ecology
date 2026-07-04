# Agent Crystal Work Harvest

This harvest adds Claude, Kimi, MannyAI, repo-harvest CAM, and downloaded crystal-paper work to the orbital review surface. It does not grade claims; it identifies work products and where they must be cross-populated.

## Source Counts

| Source | Files | Key counts |
|---|---:|---|
| Claude memory | 35 | keyword files: 35 |
| Kimi MannyAI starter | 162 | paper manifests: 96; node DBs: 32; window DBs: 32 |
| D:/MannyAI current build | 896 | keyword files: 500 |
| Repo harvest CAM | 27 | keyword files: 27 |
| Downloads NotebookLM/MannyAI papers | 83 | selected files: 76 |
| Downloaded Kimi/Manny/Crystal zip payloads | 19 | entries indexed inside archives |

## Kimi Standards And Windows

- Corpus conformance: canonical papers `32`, verdicts `192`, statuses `{'PASS': 192, 'FAIL': 0, 'OPEN': 0, 'EXTERNAL_REQUIRED': 0, 'NOT_APPLICABLE': 0}`.
- Glue/obligation coverage: `140` of `142` obligations have candidates, coverage `0.9859`.
- Suite resolution: `188` of `188` items resolved across `96` papers.
- Brain/window lattice: `window_00_31` with 16x size-2, 8x size-4, 4x size-8, 2x size-16, 1x size-32.

## Downloaded Zip Payloads

| Zip | Entries | Keyword entries | Sample |
|---|---:|---:|---|
| `Kimi Agent Rule 30 Invariant Proof Analysis.zip` | 124 | 10 | theorem_engine.py; asset_mapping.md; DRYRUN_EXPLAINER.pdf; ARCHITECTURE.pdf; Barker_Sidecar_Kernel_v1.zip |
| `Kimi_Agent_CMPLX-1T Identity & Loan.zip` | 14 | 0 | CMPLX-1T_Executive_Summary.docx; CMPLX-1T_Executive_Summary.pdf; CMPLX-1T_Humanitarian_Fund_Charter.docx; CMPLX-1T_Humanitarian_Fund_Charter.pdf; CMPLX-1T_Investment_Agreement_Framework.docx |
| `Kimi_Agent_CMPLX-R30 代码审计.zip` | 205 | 7 | CMPLX-R30-FINAL-SUBMISSION.tar.gz; CMPLX-R30-full-checkpoint-v2.tar.gz; CMPLX-R30-full-checkpoint-v3.tar.gz; CMPLX-R30-full-checkpoint-v4.tar.gz; CMPLX-R30-full-checkpoint-v5.tar.gz |
| `CQE-CMPLX-1T-Dev-main (1).zip` | 4055 | 2900 | CQE-CMPLX-1T-Dev-main/; CQE-CMPLX-1T-Dev-main/.dockerignore; CQE-CMPLX-1T-Dev-main/.github/; CQE-CMPLX-1T-Dev-main/.github/license.yml; CQE-CMPLX-1T-Dev-main/.github/workflows/ |
| `CQECMPLX-Production-main (12).zip` | 9172 | 4445 | CQECMPLX-Production-main/; CQECMPLX-Production-main/.gitignore; CQECMPLX-Production-main/CALIBRATION_BRIDGES.md; CQECMPLX-Production-main/CLOSURE_CLAIM_2026-06-13.md; CQECMPLX-Production-main/FORGE_REGISTRY.json |
| `CQECMPLX_Hardened_Foundational_Dossiers_2026-06-22.zip` | 17 | 0 | CQECMPLX_Hardened_Foundational_Dossiers_2026-06-22/; CQECMPLX_Hardened_Foundational_Dossiers_2026-06-22/pdf/; CQECMPLX_Hardened_Foundational_Dossiers_2026-06-22/pdf/01_Hardened_Package_Ecology_and_Evidence_Model.pdf; CQECMPLX_Hardened_Foundational_Dossiers_2026-06-22/pdf/02_Hardened_First_Event_and_CQE_Kernel.pdf; CQECMPLX_Hardened_Foundational_Dossiers_2026-06-22/pdf/03_Hardened_Rule30_LCR_and_Local_Carrier.pdf |
| `CQECMPLX_NotebookLM_Deep_Dive_Pack_2026-06-22.zip` | 41 | 7 | CQECMPLX_NotebookLM_Deep_Dive_Pack_2026-06-22/; CQECMPLX_NotebookLM_Deep_Dive_Pack_2026-06-22/markdown/; CQECMPLX_NotebookLM_Deep_Dive_Pack_2026-06-22/markdown/00_Review_Protocol_and_Navigation.md; CQECMPLX_NotebookLM_Deep_Dive_Pack_2026-06-22/markdown/01_Package_Architecture_and_Evidence_Model.md; CQECMPLX_NotebookLM_Deep_Dive_Pack_2026-06-22/markdown/02_First_Event_and_CQE_Kernel.md |
| `cqekernel_benchmark_v1.zip` | 3 | 0 | cqekernel_bound/BENCHMARK_REPORT.md; cqekernel_bound/benchmark_results.json; cqekernel_bound/benchmark_suite.py |
| `cqekernel_bound.zip` | 15 | 0 | cqekernel_bound/; cqekernel_bound/pyproject.toml; cqekernel_bound/src/; cqekernel_bound/src/cqekernel_bound/; cqekernel_bound/src/cqekernel_bound/__init__.py |
| `cqekernel_bound_cam_v1.zip` | 44 | 21 | cqekernel_bound/; cqekernel_bound/pyproject.toml; cqekernel_bound/src/; cqekernel_bound/src/cqekernel_bound/; cqekernel_bound/src/cqekernel_bound/__init__.py |
| `MannyAI_Address_First_Local_Kernel_Patch.zip` | 35 | 22 | .env.local.example; MANIFEST.json; README.md; UPDATE_NOTES_LATTICE_FIT.md; VALIDATION.md |
| `MannyAI_Architecture_Series_2026-06-22.zip` | 31 | 31 | MannyAI_Architecture_Series_2026-06-22/; MannyAI_Architecture_Series_2026-06-22/pdf/; MannyAI_Architecture_Series_2026-06-22/pdf/17_MannyAI_Crystal_Manifest_and_Internal_CAM_Protocol.pdf; MannyAI_Architecture_Series_2026-06-22/pdf/18_Demand_to_Crystal_Compilation_and_Task_Agent_Assembly.pdf; MannyAI_Architecture_Series_2026-06-22/pdf/19_TMN_Roles_Kernel_Rings_and_Controlled_Tool_Routing.pdf |
| `MannyAI_Asset_Class_Mesh_v1_ControlPlane.zip` | 12 | 3 | BUILD_REPORT.json; MESH_TOPOLOGY.md; README.md; SHA256SUMS.txt; asset_mesh_manifest.json |
| `MannyAI_AssetMesh_Transport_001of005.zip` | 11 | 11 | MannyAI_Asset_Class_Mesh_v1_ControlPlane.zip; MannyAI_AssetMesh_T00_control_plane_001of001.zip; MannyAI_AssetMesh_T01_documents_001of002.zip; MannyAI_AssetMesh_T01_documents_002of002.zip; MannyAI_AssetMesh_T02_code_001of002.zip |
| `MannyAI_AssetMesh_Transport_002of005.zip` | 12 | 12 | MannyAI_AssetMesh_T04_indexed_csv_005of014.zip; MannyAI_AssetMesh_T04_indexed_csv_006of014.zip; MannyAI_AssetMesh_T04_indexed_csv_007of014.zip; MannyAI_AssetMesh_T04_indexed_csv_008of014.zip; MannyAI_AssetMesh_T04_indexed_csv_009of014.zip |
| `MannyAI_AssetMesh_Transport_003of005.zip` | 5 | 5 | MannyAI_AssetMesh_T05_cam_crystal_services_003of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_004of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_005of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_006of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_007of012.zip |
| `MannyAI_AssetMesh_Transport_004of005.zip` | 8 | 8 | MannyAI_AssetMesh_T05_cam_crystal_services_008of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_009of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_010of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_011of012.zip; MannyAI_AssetMesh_T05_cam_crystal_services_012of012.zip |
| `MannyAI_AssetMesh_Transport_005of005.zip` | 3 | 3 | MannyAI_AssetMesh_T07_supplements_003of003.zip; MannyAI_AssetMesh_T08_cross_class_assembly_001of001.zip; MannyAI_AssetMesh_T09_local_session_state_001of001.zip |
| `MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper_2026-06-22.zip` | 9 | 9 | MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper_2026-06-22/; MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper_2026-06-22/LOCAL_REPLAY_EVIDENCE.json; MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper_2026-06-22/16_MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper.md; MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper_2026-06-22/MannyAI_Reference_Architecture.yaml; MannyAI_Kernel_Ring_Crystal_Universe_Entry_Paper_2026-06-22/SOURCE_ANCHORS.md |

## Required Routing Implications

- **00-32 spine:** Kimi's `papers/nodes` and per-paper node DBs are direct orbital data for the numbered papers and should be cited as paper-brain/local-node evidence.
- **larger reasoning pyramid:** Kimi's window DBs and `window_summary.json` supply a binary 2/4/8/16/32 window lattice that should be cross-read with the 3/5/7/9 reasoning pyramid.
- **NSIT / standards:** Kimi's standards suite has 192/192 PASS for canonical 32-paper conformance; use as conformance evidence, not as claim-validity grading.
- **obligation cross-population:** Kimi's glue report maps 142 obligations with 140 candidate routes; this is a high-priority queue for paper edits and orbital backlinks.
- **CAM/crystal architecture:** Claude memory identifies repo harvest CAM as 18 crystals / 224 atoms and MannyAI as CAM+brain+TMN mint target; repo_harvest_cam.db and CMPLXMCP crystal tools need intake as CAM evidence.
- **MannyAI crystal paper series:** The Downloads NotebookLM bundle contains MannyAI papers 14-38, CAM address grammar, unified crystal manifest, asset mesh, and CAM crystal service assembly; these are not secondary notes and must orbit Papers 16, 20-23, 30-32 plus NP-05/NP-07/NP-13.

## Immediate Inclusion Queue

- Add `D:\DockerContainers\Manny Docker Starter\mannyai` and the Downloads NotebookLM/MannyAI paper folder to the NSIT inventory roots.
- Rebuild the NSIT inventory and orbital cross-population audit so these artifacts are counted.
- Cross-wire Kimi's 2/4/8/16/32 window lattice into the 3/5/7/9 internal reasoning pyramid.
- Use `glue_report.json` as an obligation candidate queue and `corpus_conformance_report.json` as standards-conformance evidence.
- Treat downloaded MannyAI papers 14-38 and CAM manifests as orbital papers around the 00-32 spine, especially Papers 16, 20-23, 30-32 and NP-05/NP-07/NP-13.
