# Connection Wiring Queue

Top **10 non-obvious connections** from `DEEP_REVIEW_PASS1_SUMMARY.md` with concrete file paths to link.  
Status after Phase 13: **10 wired** (3 discovery bridges + 7 connection/citation/motif).

| # | Δ | Type | Source → Target | Files to link | Status | Action |
|---:|--:|------|-----------------|---------------|--------|--------|
| 1 | 14 | `discovery_bridge` | LOCAL-GAP-0001 ↔ Folded Strand | `EVIDENCE_INTAKE_SCORE_NOTEBOOK.json` → `LOCAL-GAP-0001`; receipt: `kernel/staging/papers/suite18_cl_paper_db/CL_proof-source-lattice-forge-inventory.md`; parent: `CMPLX-Kernel/lib-forge/MASTER_PAPER_Folded_Strand.md`; PEEP: `PEEP-2026-006` | **Wired** | REROUTE_OR_REPAIR via `BRIDGE-0001` in `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` |
| 2 | 14 | `discovery_bridge` | LOCAL-GAP-0002 ↔ Jordan J3 | `LOCAL-GAP-0002`; receipt: `suite18_cl_paper_db/CL_proof-source-jordan-j3-octonion.md`; workbook: `FLCR-03/workbook.md`, `FLCR-04/workbook.md`, `FLCR-05/workbook.md`; PEEP: `PEEP-2026-005` | **Wired** | REROUTE_OR_REPAIR via `BRIDGE-0002`; dedupe `LOCAL-GAP-0012` |
| 3 | 14 | `discovery_bridge` | LOCAL-GAP-0003 ↔ Rule30 receipt | `LOCAL-GAP-0003`; receipt: `CQECMPLX-Formal-Suite/lib/src/lattice_forge/receipts/verify_rule30_winding_number_proof.json`; workbook: `FLCR-06/workbook.md`, `FLCR-09/workbook.md`; PEEP: `PEEP-2026-018` | **Wired** | REROUTE_OR_REPAIR via `BRIDGE-0003`; external comparator deferred |
| 4 | 12 | `missing_link` | FLCR-17 → FLCR-18 | `FLCR-17/formal.md` → `FLCR-18/formal.md`; `SOURCE_ROUTING_MATRIX.json` FLCR-17 `legacy_paths` + `upstream_publication_refs` | **Wired** | Added `17_E6_E8_Error_Correction_Tower.md`; upstream FLCR-02/03/18 |
| 5 | 20 | `implicit_dependency` | FLCR-18 → FLCR-17 | `FLCR-18/formal.md`; `FLCR-18/workbook.md`; `SOURCE_ROUTING_MATRIX.json` | **Wired** | `DEP-FLCR-18-17` in manifest; workbook theorem dependency table |
| 6 | 10 | `shared_motif` | FLCR-02 → FLCR-17 | `FLCR-02/formal.md`, `FLCR-17/formal.md`; slots 02/17/18; glossary: `SLOT_1_80_GENERALIZED_ONTOLOGY.md` moonshine cluster | **Wired** | `MOTIF-MOONSHINE-02-17-18` |
| 7 | 10 | `shared_motif` | FLCR-03 → FLCR-17 | `FLCR-03/formal.md`, `FLCR-17/formal.md`; `FLCR-03/workbook.md`; lattice-forge + moonshine slot family | **Wired** | `MOTIF-FORGE-03-17-18` |
| 8 | 10 | `shared_motif` | FLCR-09 → FLCR-21 | `FLCR-09/formal.md`, `FLCR-21/formal.md`; forge motif; slots 09→21→22 | **Wired** | `MOTIF-FORGE-09-21-22` + pipeline keyword map |
| 9 | 20 | `implicit_dependency` | FLCR-24 → FLCR-11 | `FLCR-24/formal.md`, `FLCR-11/formal.md`; `SOURCE_ROUTING_MATRIX.json`; slot 24 | **Wired** | `CITE-FLCR-24` → FLCR-01/11/18; FLCR-24 gaps cleared |
| 10 | 20 | `implicit_dependency` | FLCR-26 → FLCR-06 | `FLCR-26/formal.md`, `FLCR-06/formal.md`; `FLCR-06/workbook.md` obligation ledger; slot 26 | **Wired** | `CITE-FLCR-26` → FLCR-06 causal_code receipt |

## Manifest locations

| Artifact | Path |
|----------|------|
| Discovery bridge wiring | `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` → `discovery_bridge_wiring[]` |
| Citation binding wiring | `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` → `citation_binding_wiring[]` |
| Implicit dependency wiring | `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` → `implicit_dependency_wiring[]` |
| Shared motif wiring | `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` → `shared_motif_wiring[]` |
| Slot promotion gates | `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` → `slot_promotion_gates[]` |
| Pipeline loader | `tools/build_evidence_slot_assembly_pipeline.py` |
| Routing matrix | `SOURCE_ROUTING_MATRIX.json` |

## Apply-pass metrics (Phase 13)

- Connections scanned: 926 → **926** (wiring records in notebook, not rescore)
- Total content gaps: 178 → **166** (−12)
- FLCR-24 FLCR-01/11/18 citation gaps: **resolved**
- Connection queue: **10/10 wired**
- ASSEMBLE: **28 unchanged**; 0 fake PEEP
