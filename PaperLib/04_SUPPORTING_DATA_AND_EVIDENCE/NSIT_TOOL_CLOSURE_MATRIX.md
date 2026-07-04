# NSIT Validation Tool Closure Matrix

**Status:** first-pass reapplication matrix.  
**Purpose:** record what existing validation tools already close across the
paper corpus when applied individually or in batches, without relying on legacy
`open`/`closed` labels.

---

## Inventory Baseline

The first NSIT evidence inventory found:

| Artifact class | Count |
|----------------|------:|
| validators | 220 |
| receipt/data artifacts | 1786 |
| formal-paper-like artifacts | 1137 |
| supplements | 114 |
| memory/CAM artifacts | 86 |

This means the validity problem is not mainly "write new theory." The immediate
work is to reapply the existing validators and tool families to every claim they
can legitimately cover, then attach the receipts.

## Closure Modes

| Mode | Meaning |
|------|---------|
| `individual_tool_closure` | One verifier/tool directly validates the target claim. |
| `batch_tool_unison_closure` | Multiple tools close a claim only when composed over the same output/evidence surface. |
| `partial_with_residue` | A tool closes the internal/verifiable core while leaving an explicitly named residue. |
| `external_data_bind` | The tool route exists, but a dataset/theorem/lab value must be fetched and content-bound before Gate 90. |
| `not_yet_resource_closeable` | No attached or confirmed-obtainable closing form has been found. |

## Known Reapplied Closures

Extracted from
`D:/CQE_CMPLX/git-hosted-roots/CQECMPLX-Production/governance/legacy-tracking/REAPPLICATION_LEDGER.md`.

| Target / obligation | Mode | Existing tool(s) | Paper binding | Receipt | Validity effect |
|---------------------|------|------------------|---------------|---------|-----------------|
| O2-prime verifiable core: Rule30 = Rule90 plus correction, Lucas closed form, depth-N decomposition | individual_tool_closure | `lattice_forge/rule90_linearization.py` | Paper 06 | `rule90_lucas_decomposition_receipt.json` 7/7 | Internal correction core closes; unbounded McKay collapse remains separate. |
| PFC-2 E8 root enumeration | individual_tool_closure | `E8Forge` | Paper 08 | `e8_hemisphere_partition_receipt.json` 5/5 | 240 roots, 120 antipodal pairs, clean split confirmed. |
| T1-T4 algebra foundation | batch_tool_unison_closure | `octonion.py`, `jordan_j3.py`, `rule30.py`, `f4_action.py` | Paper 03 | `algebra_foundation_T1_T4_receipt.json` 8/8 | Octonions, J3(O), chart isomorphism, exact n=3 closure bound. |
| T5-T7 plus shell-2 doublet | batch_tool_unison_closure | `f4_action.py`, `core.py` | Papers 03 and 01 | `su3_closure_T5_T7_receipt.json` 10/10; `bijective_shell2_doublet_receipt.json` 7/7 | SU(3)/8x8 closure and single-tape doublet close. |
| T_D12 idempotent chain | individual_tool_closure | `lattice_forge/d12_action.py` | Paper 03 | `d12_idempotent_chain_receipt.json` 6/6 | D12 idempotent chain closes on D4 chart. |
| Lattice code chain 1->3->7->8->24->72 | individual_tool_closure | `lattice_forge/lattice_codes.py` | Paper 08 | `lattice_code_chain_receipt.json` 6/6 | E8/Fano/Hamming/Golay/Leech chain closes. |
| Centroid / VOA sector chain | individual_tool_closure | `lattice_forge/centroid_voa.py` | Paper 18 | `centroid_voa_chain_receipt.json` 5/5 | Finite VOA sector chain closes. |
| Oloid carrier family | batch_tool_unison_closure | `lattice_forge/oloid_*.py` | Paper 05 | `oloid_carrier_family_receipt.json` 4/4 | Oloid carrier family closes; E6->E7->E8 lift remains separate. |
| O7 Niemeier:E8^3 partial carrier/Leech landing | partial_with_residue | `enumerated_glue.py`, `nebe_gamma72.py` | Paper 08 | `niemeier_leech_enumeration_receipt.json` 6/6 | E8^3 carriers and Leech landing close; exact glue reps were residue before later batch closure. |
| D4 block tower + G2->F4 exceptional conjugate | batch_tool_unison_closure | `block_d4.py`, `block_tower.py`, `g2_f4_t5_conjugate.py` | Paper 03 | `d4_block_tower_exceptional_receipt.json` 3/3 | D4 block, block tower, and exceptional conjugate close. |
| O2'' F2 bridge algebraic core + unipotent orbits + substrate map | partial_with_residue | `f2_majorana.py`, `unipotent_orbits.py`, `substrate_map.py` | Paper 08 | `f2_bridge_unipotent_substrate_receipt.json` 3/3 | F2 Arf core, E8 unipotent orbit tables, substrate map close; registry population was separate. |
| O7 exact Niemeier:E8^3 glue cosets | batch_tool_unison_closure | E8Forge over three E8 blocks | Paper 08 | `o7_niemeier_e8cubed_glue_closed_receipt.json` 7/7 | Glue cosets = `{0}`; identity glue; 720 roots. |
| O8 spinor SU(2) double cover | batch_tool_unison_closure | `oloid_kinematic` frame inversion semantics | Paper 01 | `o8_spinor_double_cover_closed_receipt.json` 6/6 | F^2 = -1 at 2pi; F^4 = +1 at 4pi. |
| O2'' registry population | batch_tool_unison_closure | `f2_arf`, `lucas_recurrence`, `rule30_decomposition`, `f2_edge_glue` validators | Paper 08 | `o2pp_registry_populated_receipt.json` 6/6 | 314 facts accepted; 0 rejected. |
| Paper 13 Standard-Model quark-face transport | batch_tool_unison_closure | SU(3) T4 closure, D12 trace conservation, side-flip chirality, J3(O) faces, QuarkFaceForge | Paper 13 | `quark_face_transport_literalized_receipt.json` 10/10 | Exact structural color-transport claim closes; physical-quark identity remains transport-scoped. |

## Standards-Level Validation Tools

These do not close a mathematical theorem by themselves; they close validity
requirements around the artifact or evidence record.

| Tool / standard | Location | What it closes |
|-----------------|----------|----------------|
| `claim.cpt_envelope` | `src/cqe_standards/standards/claim.cpt_envelope.json` | Claim has boundary, falsifier, imports, evidence split, validators, scope, and coordinate contract. |
| `receipt.content_addressed` | `src/cqe_standards/standards/receipt.content_addressed.json` | Receipt carries required fields and a body hash matching the canonical content. |
| `lcr.lane_grant` | `src/cqe_standards/standards/lcr.lane_grant.json` | L/C/R lane policy and grants are consistent. |
| `paper_validator.py` adapter | `src/cqe_standards/adapters/paper_validator.py` | Legacy `verify_*.py` scripts become normalized `Verdict` records. |
| Kimi/MCP `SystemValidator` | `D:/repo_harvest/CMPLXMCP/validation/system_validator.py` | Runs suite-level validation across MCP tools, universal system, AGRM/MDHG, integration, and performance. |

## Batch Reapplication Rule

For every paper claim, NSIT should attempt these applications before declaring
the claim not resource-closeable:

1. Search direct paper-local verifiers and receipts.
2. Search theorem-registry verifiers by object name.
3. Search lattice-forge and forge-family `verify_*` functions.
4. Search reapplication ledger closures and promotion manifests.
5. Compose tools over shared output surfaces when the claim names more than one
   structure.
6. Apply the reasoned closure pass in `NSIT_REASONED_CLOSURE_PASS.md`: standard
   math, physics, CS, numerical analysis, and formal-methods closure routes.
7. Only after those passes, assign a below-80 Safe-to-Claim score.

## Reasoned Reapplication Families

These are closure candidates that come from applying ordinary field knowledge
and cross-paper reasoning, then demanding a receipt, citation, or attached data
before promotion.

| Family | Papers likely affected | Expected action |
|--------|------------------------|-----------------|
| Leech/E8/Golay operational lookup | 08, 17, 21, 29 | Promote no-cost lookup and construction-surface claims when lattice-forge receipts are attached; keep expanded invariant/Gamma72 residue separate. |
| Symbolic-vs-physical carrier split | 05, 07, 13, 15, 16, 22, 25, 26 | Close symbolic addressable-carrier claims internally; route physical carrier identity to NP-06/NP-12 calibration. |
| Electron-hole-exciton standard accounting | 07, 15, 16, 22 | Treat hole/exciton/recombination/screening/band-gap explanations as standard physics when the material model is present; keep CQE residue to addressability and obligation calculus. |
| SU(2) spinor double-cover local semantics | 01, 19, 27 | Bind O8 receipt and standard double-cover theorem; route physical observer claims to NP-10. |
| Finite CA and bounded search | 12, 24, 28, 32 | Promote finite verified surfaces; keep unbounded prediction, full game theory, and minimality residues separate. |
| Formal-methods closure | 00, 06, 10, 20, 30, 32 | Close paper-form, receipt, lane, and causal-graph obligations through standards reports. |
| Applied forge internal/external split | 21, 22, 23, 24, 28 | Promote internal representation/generation kernels; route real-world benchmark/data obligations to NP-07. |

## Immediate Batch Candidates

| Candidate | Papers likely affected | Why |
|-----------|------------------------|-----|
| Rule90/Lucas/correction plus Paper 09 McKay witness | 02, 06, 09, 12, 16, 18 | Core correction machinery is already closed in parts; batch pass can separate what is valid now from O2-prime residue. |
| D4/J3/Oloid/Spinor batch | 01, 03, 05, 13, 19, 27 | O8 spinor closure plus D4 face selection likely propagates through observer papers. |
| E8/Leech/Niemeier/Golay batch | 08, 17, 21, 29 | E8, Leech, code chain, and exact E8^3 glue closures should be reapplied jointly. |
| Centroid/VOA/Mass/Energy batch | 09, 15, 18, 25, 29 | VOA sector chain and kappa/energy ledgers likely close shared internal mass-energy accounting claims. |
| Applied forge validation batch | 21, 22, 23, 24, 28 | Existing forge validators may close representation/generation cores while leaving external validation separate. |
