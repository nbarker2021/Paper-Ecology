# Data-Gathering Subagent Queues

Four read-only data-gathering agents were assigned non-overlapping lanes.

## Queue 01: Hosted / Production Archives

**Agent:** Noether  
**Roots:** `D:\CQE_CMPLX\git-hosted-roots`, `D:\CQE_CMPLX\CQECMPLX-Production`  
**Manifest:** `queue_01_hosted_production_archives.json`

Priority order:

1. Paper 09, 12, 31, 32 receipt deltas, then suite/migration receipts.
2. `open_obligation_batch*_report.md` and payload JSON.
3. `claims.jsonl`, `paper_topology.*`, `verifier_index.csv`, `CRYSTAL_VERIFIER_INDEX.md`.
4. Source-harvest work order, SM proof-gap audit, claim-proof-theorem standard.
5. Dyad briefs and `LATTICE_FORGE_MODULE_PAPER_MAP.md`.
6. Mirrored `lib-forge` / `papers` only after hash dedupe.

## Queue 02: Kernel / g Mirrors

**Agent:** Zeno  
**Roots:** `D:\CQE_CMPLX\CMPLX-Kernel`, `D:\CQE_CMPLX\g`  
**Manifest:** `queue_02_kernel_g_mirrors.json`

Priority order:

1. `CMPLX-Kernel\lib-forge\papers_output\CQE-paper-00.md` through `CQE-paper-32.md`, plus `CQE-paper-32-obs.md`.
2. `FINAL_FORMAL_PAPER.md`, `MASTER_PAPER_Folded_Strand.md`, and `summary_papers`.
3. Paper 00 workbook packets and claim JSON.
4. Active lattice-forge docs under `g\CMPLX-PartsFactory\packages\lattice-forge\docs`.
5. Lattice-forge structured artifacts: claims, expected outputs, extracted formalization manifest.
6. R30 proof layer.
7. Formalization mirrors.
8. Kernel-ring curated forms.
9. `g\CMPLX-1T` only through indexes/reports first.

## Queue 03: Historical / Formal / Gap

**Agent:** Raman  
**Roots:** `historical_pastworks`, `CQECMPLX-ProofValidatedSuite`, `CQECMPLX-Formal-Suite`, `gap_analysis`  
**Manifest:** `queue_03_historical_formal_gap.json`

Priority order:

1. `gap_analysis\master_gap_registry_FINAL.csv` and `FINAL_GAP_REPORT.md`.
2. Formal-Suite ontology, master framework, unification charter, honesty appendix.
3. Formal-Suite receipt set and receipt validator.
4. Current formal spine folders.
5. Historical best-form bundle.
6. Historical open obligations and extracted claims.
7. SM audit.
8. ProofValidatedSuite form manifests.
9. Kimi Rule 30 proof/prize lineage.

## Queue 04: Lattice Forge Unification

**Agent:** Heisenberg  
**Roots:** all workspace roots, filtered to `lattice_forge` / `lattice-forge` variants  
**Manifest:** `queue_04_lattice_forge_unification.json`

Priority order:

1. Canonical package: `CMPLX-PartsFactory-main\packages\lattice-forge`.
2. Product extension source: `CQE-CMPLX-1T-Production\src\lattice_forge`.
3. Product clone: `GaussHaus\src\lattice_forge`.
4. R30 proof snapshot.
5. Formal-Suite proof/receipt copy.
6. Forge ring / AirLock lineage.
7. Historical/mirror copies as read-only provenance.
8. Product-stick shim cleanup.

## Output Artifacts

- `D:\Paper Reworks\lattice_forge_unification\LATTICE_FORGE_UNIFICATION_MAP.md`
- `D:\Paper Reworks\lattice_forge_unification\EXTENSION_CANDIDATES.md`
- `D:\Paper Reworks\supplements\LATTICE_FORGE_UNIFICATION_SUPPLEMENT.md`
