# Missed Content Review - Paper Reworks

Review date: 2026-06-26

This review treats an **open obligation** as the author's definition of the next
need. The goal is not to erase open items. The goal is to identify where the
rework drafts stop carrying rich source content and begin acting as skeletons.

## Executive finding

The rich-to-skeleton transition starts at **Paper 09**.

Papers **00-08** are developed paper drafts: they average roughly 1,430 words,
carry proof sketches, source conflicts, related-file context, and explicit
closure of earlier obligations.

Papers **09-32** are mostly generated skeletons: they keep a uniform 14-section
frame, but average roughly 480 words. Most have enough structure to be useful,
but not enough content to stand in for the formal papers, source-backup variants,
OpsGuides, and receipt context they cite.

## Triage by compression

These papers lost the most content relative to their canonical formal paper:

| Priority | Paper | Rework / formal word ratio | Pickup reason |
|----------|-------|-----------------------------|---------------|
| P0 | 29 | 30.2% | Formal paper has closed evidence, worked example, external-data anchors, and suite role that are mostly flattened. |
| P0 | 11 | 32.9% | Admission predicate needs richer T10-anchor, boundary, and falsifier treatment. |
| P0 | 21 | 33.5% | MorphForge reader has a much richer formal/source story than the rework carries. |
| P0 | 30 | 35.4% | Meta-framer should preserve richer ribbon/provenance packaging. |
| P1 | 13 | 39.8% | Quark-face paper loses several claims/proof steps and package literalization detail. |
| P1 | 15 | 40.3% | Mass-residue paper misses one GLM verifier and likely loses the 2x2x2 vs 3x3 basis story. |
| P1 | 26 | 40.1% | Z-pinch/shear paper needs more physical-boundary and mechanism detail. |
| P1 | 31 | 40.1% | Retrospective LCR readout needs more downstream-status protection. |
| P1 | 17 | 41.5% | E6-E8 tower misses Niemeier seam GLM verifier and needs Leech/open-lift precision. |
| P1 | 09 | 42.2% | Hamiltonian paper misses a GLM verifier and richer McKay/kappa source context. |

## Concrete misses already found

### 1. Source-backup variants are not actually missing

`INDEX.md`, `SYNTHESIS_DRAFT.md`, and `CROSS_CUTTING_INTEGRITY_NOTES.md` carry
the cross-cutting obligation to locate or recreate `.25`, `.50`, `.75`, and
`_UPGRADED.md` variants for Papers 09-32.

Those variants do exist under:

```text
D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\source_backup
```

Next need:

- Replace the "missing variants" obligation with an incorporation task.
- For each Paper 09-32, diff the formal paper against `.25`, `.50`, `.75`, and
  `_UPGRADED.md`.
- Import useful source texture without promoting overclaims.

### 2. GLM verifier rows were missed in multiple reworks

The rework verifier tables omit several GLM verifier surfaces present in the
canonical formal folders.

| Paper | Missing verifier row |
|-------|----------------------|
| 09 | `verify_glm_alpha_fractional_cayley_dickson.py` |
| 10 | `verify_glm_nine_by_nine_closed_form.py` |
| 13 | `verify_glm_spin12_spin16_root_decomp.py` |
| 15 | `verify_glm_higgs_frame_mapping.py` |
| 17 | `verify_glm_niemeier_seam_decomposition.py` |
| 18 | `verify_glm_s3_hopf_seam_manifold.py` |
| 32 | `verify_glm_43200_stratum_terminal.py` |

Next need:

- Add these verifier/receipt rows to the corresponding paper reworks.
- Classify each row as IPMC, ECO, bridge, or guard.
- Update `OBLIGATION_AUDIT.md` where the missing verifier changes an obligation
  from "missing" to "partially closed", "advanced", or "engineering".

### 3. Formal proof texture is being flattened into one-line theorems

Example: Paper 13 formal source carries:

- Claims 13.1-13.8.
- The shell-2 triple enumeration.
- The trace-2 `J_3(O)` idempotent mapping.
- The six-element `S_3` Weyl closure.
- Exact rational `SU(3)` group-ring closure.
- Bounded `G2/F4/T5A` classifier boundary.
- `QuarkFaceForge` literalization.
- Standard-Model real-data comparison, including exact/suggestive/non-match rows.

The rework mostly compresses this into one theorem plus a receipt table.

Next need:

- Restore claim-by-claim proof flow for Papers 09-18 first.
- Keep physical calibration as open, but do not delete the internal algebraic
  proof path that is already present.

### 4. Paper 29 lost its strongest explanatory material

Paper 29 formal source has sections for:

- Closed Evidence.
- Definitions.
- Claims.
- Proof.
- Worked Example.
- External Data Anchors.
- Open Obligations.
- Suite Role.

The rework keeps the headline `196883 = 47 x 59 x 71`, but loses much of the
evidence/readout narrative and the external-data-anchor explanation.

Next need:

- Rebuild Paper 29 from the formal paper first, then layer in source-backup
  variants.
- Keep the units bridge open, but restore the closed structural evidence:
  supersingular-prime ceiling, finite chart partition, LMFDB/Moonshine anchors,
  and falsifiable witness-function boundary.

### 5. Applied Forge papers are too thin for the product layer

Papers 21-28 are where the applied forges enter, but many reworks carry only a
minimal theorem, a receipt table, and open obligations. This is especially thin
for:

- Paper 21: MorphForge / PolyForge / MorphoniX.
- Paper 22: MetaForge applied materials.
- Paper 23: FoldForge protein folding.
- Paper 25: energetic traversal maps.
- Paper 26: Z-pinch and shear horizon.
- Paper 28: N-dimensional game lattices.

Next need:

- For each applied paper, add an "operational surface" section:
  input crystal, projection/readout, verifier receipt, output ledger, open
  calibration needs.
- Treat every open obligation as the next algorithmic need, not as a failure.

## Obligation buckets to preserve

Do not collapse these categories:

| Bucket | Meaning | Action |
|--------|---------|--------|
| Closed | A later paper or receipt closes it. | Reference the closure and keep the receipt path. |
| Partially closed / advanced | Some machinery exists but not the full claim. | State exactly what advanced and what remains. |
| Guard | Ongoing honesty boundary. | Preserve as a rule, not a TODO. |
| Engineering | Tooling, path, packaging, schema, or selector work. | Convert to work item. |
| Documentation | Bibliography, variant reconciliation, taxonomy, provenance. | Convert to doc pass. |
| Genuinely open | Real research/calibration gap. | Carry as next need with falsifier/witness requirements. |

## Recommended pickup order

1. **Repair the index/audit truth first**
   - Update the source-backup variant obligation: variants exist and need
     incorporation.
   - Add missing GLM verifier rows.
   - Reclassify affected obligations.

2. **Rebuild P0 papers from rich sources**
   - Paper 29.
   - Paper 11.
   - Paper 21.
   - Paper 30.

3. **Restore proof texture in P1 papers**
   - Papers 13, 15, 17, 18.
   - Then Papers 09, 10, 26, 31.

4. **Add operational surfaces to applied Forge papers**
   - Papers 21-28 should each say what crystal/ledger/forge input they consume,
     what projection or verifier they run, what receipt they emit, and what open
     obligation defines the next need.

5. **Only then expand synthesis**
   - `SYNTHESIS_DRAFT.md` should be updated after the per-paper content is
     restored, not before.

## Working rule for the next pass

When a section says **open obligation**, read it as:

```text
This is the next needed crystal, verifier, adapter, calibration, or witness.
```

The rework should not try to make open obligations disappear. It should make
them usable: named, routed, receipt-bound, and ready for the next algorithm.
