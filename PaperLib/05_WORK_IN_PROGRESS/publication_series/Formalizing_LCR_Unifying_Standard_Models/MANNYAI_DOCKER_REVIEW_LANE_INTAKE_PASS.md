# MannyAI Docker Review Lane Intake Pass

Generated: `2026-06-29T18:49:56.430016+00:00`

This pass adds `D:/MannyAI` and `D:/DockerContainers/Manny Docker Starter` as first-class review-lane source roots for the FLCR papers. It distinguishes runtime/code evidence, standards conformance, node/window memory, deployment topology, and operations guardrails.

## Inventory Summary

| Root | Files | Directories | Bytes | Top suffixes |
|---|---:|---:|---:|---|
| D:\MannyAI | 114 | 21 | 2676960 | {'.py': 63, '.md': 28, '.pdf': 8, '.html': 8, '.json': 3, '<none>': 1, '.ini': 1, '.txt': 1, '.png': 1} |
| D:\DockerContainers\Manny Docker Starter | 330 | 213 | 19123004 | {'.json': 117, '.db': 66, '.py': 47, '.md': 39, '.yml': 13, '<none>': 10, '.sh': 5, '.txt': 5, '.yaml': 5, '.sql': 4, '.ps1': 3, '.conf': 3} |

## Key Readouts

- `standards_conformance`: `{'canonical_count': 32, 'total_verdicts': 192, 'by_status': {'PASS': 192, 'FAIL': 0, 'OPEN': 0, 'EXTERNAL_REQUIRED': 0, 'NOT_APPLICABLE': 0}}`
- `suite_resolution`: `{'paper_count': 99, 'total_items': 782, 'resolved_items': 776, 'unresolved_items': 6, 'reworks_indexed': 52}`
- `glue`: `{'total_obligations': 95, 'obligations_with_candidates': 95, 'coverage_ratio': 1.0}`
- `node_verify`: `{'canonical_count': 32, 'by_verdict': {'OPEN': 0, 'FAIL': 7, 'PASS': 25}, 'total_duration_seconds': 353.889}`
- `windows`: `{'root_window_id': 'window_00_31', 'levels': [{'size': 2, 'count': 16}, {'size': 4, 'count': 8}, {'size': 8, 'count': 4}, {'size': 16, 'count': 2}, {'size': 32, 'count': 1}]}`

## Review Lanes

| Lane | Claim Lane | Targets | Use | Boundary | Evidence Exists |
|---|---|---|---|---|---|
| mannyai_cam_crystal_mcp | `cam_crystal_reapplication_result` | FLCR-02, FLCR-08, FLCR-20, FLCR-28, FLCR-38, FLCR-40 | Treats CAM/crystal operations and MCP tools as addressable runtime evidence for lookup, crystal projection, content-addressed writes, and carrier-CEM execution. | Runtime/MCP conformance is a review lane and tool route; it does not replace mathematical proof or physical calibration. | 5/5 |
| mannyai_splatforge_field_runtime | `cam_crystal_reapplication_result` | FLCR-20, FLCR-21, FLCR-22, FLCR-23, FLCR-28, FLCR-36, FLCR-38 | Adds the spatial/field forge as the bridge between crystals, grammar dispatch, deterministic render/readout, LCR ring controls, and reconstruction. | Useful as executable/adapter evidence; domain claims still need per-domain data, receipts, or calibrators. | 9/9 |
| mannyai_carrier_cem_and_research_receipts | `receipt_bound_internal_result` | FLCR-01, FLCR-07, FLCR-11, FLCR-19, FLCR-26, FLCR-28, FLCR-38 | Adds carrier-CEM, grant enforcement, learner/specialization, sealed receipt chains, and research receipts as direct review-lane sources. | Cold-start accuracy and domain dispatch remain bounded by the manifest's open obligations unless closed by tests. | 5/5 |
| docker_standards_suite | `normal_form_result` | FLCR-07, FLCR-11, FLCR-12, FLCR-28, FLCR-30, FLCR-39, FLCR-40 | Treats the Docker-hosted MannyAI standards stack as a first-class review lane for structure, claim coverage, receipt status, open obligations, obligation continuity, and suite-aware evidence. | Standards passing proves conformance to the review protocol, not truth of every imported claim. | 6/6 |
| docker_window_node_databases | `cam_crystal_reapplication_result` | FLCR-10, FLCR-11, FLCR-19, FLCR-28, FLCR-29, FLCR-30, FLCR-40 | Adds the 2/4/8/16/32 window hierarchy, node DBs, paper manifests, and central MannyAI DB as review-lane memory surfaces. | Databases are intake/query sources; individual rows must be quoted or receipted before being promoted. | 5/5 |
| docker_mcp_and_deployment_surface | `receipt_bound_internal_result` | FLCR-20, FLCR-28, FLCR-30, FLCR-38, FLCR-39 | Adds Docker/MCP deployment, container topology, normalized compose, running-container snapshots, and ReForge integration as operational review lanes. | Deployment topology is infrastructure evidence; services should not be assumed live unless current health checks are run. | 7/7 |
| docker_observability_security_governance | `falsifier_or_open_obligation` | FLCR-07, FLCR-12, FLCR-28, FLCR-39, FLCR-40 | Adds operational guardrails, monitoring, deployment policy, Kubernetes/Helm surfaces, and security documentation as automation-review guardrails. | Security/deployment docs are guardrails and falsifier lanes for automation, not restrictions on human hypothesis generation. | 6/6 |

## Paper Manifest Updates

| Paper | Lanes |
|---|---|
| `FLCR-01` | `mannyai_carrier_cem_and_research_receipts` |
| `FLCR-02` | `mannyai_cam_crystal_mcp` |
| `FLCR-07` | `mannyai_carrier_cem_and_research_receipts`, `docker_standards_suite`, `docker_observability_security_governance` |
| `FLCR-08` | `mannyai_cam_crystal_mcp` |
| `FLCR-10` | `docker_window_node_databases` |
| `FLCR-11` | `mannyai_carrier_cem_and_research_receipts`, `docker_standards_suite`, `docker_window_node_databases` |
| `FLCR-12` | `docker_standards_suite`, `docker_observability_security_governance` |
| `FLCR-19` | `mannyai_carrier_cem_and_research_receipts`, `docker_window_node_databases` |
| `FLCR-20` | `mannyai_cam_crystal_mcp`, `mannyai_splatforge_field_runtime`, `docker_mcp_and_deployment_surface` |
| `FLCR-21` | `mannyai_splatforge_field_runtime` |
| `FLCR-22` | `mannyai_splatforge_field_runtime` |
| `FLCR-23` | `mannyai_splatforge_field_runtime` |
| `FLCR-26` | `mannyai_carrier_cem_and_research_receipts` |
| `FLCR-28` | `mannyai_cam_crystal_mcp`, `mannyai_splatforge_field_runtime`, `mannyai_carrier_cem_and_research_receipts`, `docker_standards_suite`, `docker_window_node_databases`, `docker_mcp_and_deployment_surface`, `docker_observability_security_governance` |
| `FLCR-29` | `docker_window_node_databases` |
| `FLCR-30` | `docker_standards_suite`, `docker_window_node_databases`, `docker_mcp_and_deployment_surface` |
| `FLCR-36` | `mannyai_splatforge_field_runtime` |
| `FLCR-38` | `mannyai_cam_crystal_mcp`, `mannyai_splatforge_field_runtime`, `mannyai_carrier_cem_and_research_receipts`, `docker_mcp_and_deployment_surface` |
| `FLCR-39` | `docker_standards_suite`, `docker_mcp_and_deployment_surface`, `docker_observability_security_governance` |
| `FLCR-40` | `mannyai_cam_crystal_mcp`, `docker_standards_suite`, `docker_window_node_databases`, `docker_observability_security_governance` |

## Review Application Rule

Use these source roots as review lanes, not as automatic proof promotion. A lane can supply executable evidence, standards conformance, routing memory, deployment topology, or automation guardrails. A paper may promote a stronger claim only when the specific row also has a paper-local receipt, external citation, calibration target, CAM reconstruction, or falsifier boundary.
