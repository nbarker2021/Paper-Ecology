# Discovery Agent Assignment Manifest

Generated: 2026-07-01T02:56:05.203664+00:00

Assign persistent pipeline roles for finding, pairing, classifying, validating, and assembling evidence into the 1-80 master docs.

| Agent | Mission | Outputs |
|---|---|---|
| local_artifact_discovery | Mine D-drive/CQE/MannyAI/Docker/repo_harvest artifacts and create internal source cards. | `internal_source_card`, `candidate_slot_assignments`, `missing_external_pair_queries` |
| external_paper_pairing | Find 2025/current peer-reviewed journal papers or stable preprints that constrain/support/falsify each internal source card. | `external_journal_paper_card`, `correlation_claim`, `external_comparator_lane` |
| slot_classifier | Disassemble each internal/external pair into generalized 1-80 slot families with multi-slot assignment. | `slot_families`, `slot_assignments`, `primary_slot`, `secondary_slots` |
| nist_validation_notebook | Run adapted NIST/validation checks at every chain step and maintain the running score notebook. | `score_notebook_row`, `pass_fail_review`, `reroute_reason` |
| paper_assembly_auditor | Audit the score notebook and decide assemble, reroute/repair, or return to discovery. | `assembly_queue`, `reroute_queue`, `discovery_queue`, `paper_local_obligations` |