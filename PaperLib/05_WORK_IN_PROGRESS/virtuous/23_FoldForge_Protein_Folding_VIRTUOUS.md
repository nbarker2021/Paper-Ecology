# Paper 23 - FoldForge Protein Folding

**Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data.

**Method:** preserve the strongest representation of each source face; when
sources disagree, keep the disagreement as a named boundary or next-need.

---

## Source Faces

| Face | Path | Words / count | Contribution |
|------|------|---------------|--------------|
| Current rework | `D:\Paper Reworks\23_FoldForge_Protein_Folding.md` | 405 words | Existing skeleton, current status, obligations. |
| Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-23\FORMAL_PAPER.md` | 881 words | Main theorem, proof, receipt, falsifier spine. |
| Companion variant | `CQE-paper-23.25.md` | 208 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-23.50.md` | 237 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-23.75.md` | 173 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-23_UPGRADED.md` | 974 words | Alternate toolkit/contract/bridge phrasing. |
| Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-23` | 1 files | Executable evidence surface. |
| Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-23` | 2 files | Receipt status and check counts. |
| Saved CAM nodes | `D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json` | 1 relevant nodes | Prior crystal evidence and obligation nodes. |
| Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant rows | Closure/partial-closure status updates. |

## Virtuous Synthesis

Paper 23 applies the Forge reading discipline to protein-chain descriptors. Its
closed result is not a protein structure predictor. Its closed result is a
replayable descriptor receipt: a residue chain is converted into local `(L, C,
R)` windows, a contact-map receipt is generated, local side changes are marked
as candidate bifurcations, and the result is paired with the bounded oloid
winding substrate and its explicit open gaps.

This version treats the formal paper as the proof spine, the companion variants as interface contracts, and the CAM/GLM rows as status-bearing crystal data. The paper's open obligations are not deleted; they are the next work items required before stronger claims can be promoted.

## Companion Face Digest

- **Paper 23.25 - FoldForge Toolkit Supplement.** This supplement explains how to reproduce the FoldForge descriptor receipt. It
is support material. The proof-carrying item is Paper 23 and its formal receipt.
- **Paper 23.50 - FoldForge Claim Contract.** # Paper 23.50 - FoldForge Claim Contract ## Admission Rule A Paper 23 claim is admitted only when it is framed as a fold descriptor unless PDB, experimental, or validated simulation evidence is attached. A descriptor must include a residue chart, contact-map receipt, candidate bifurcation list, winding evidence, open obligations, and a falsifier. ## Required Fields Each admitted descriptor must provide: - protein or peptide identifier, - residue sequence, - residue encoding rule, - complete local-window count, - contact predicate, - contact-map receipt, - candidate bifurcation list, - winding or topology descriptor, - substrate verifier status, - open biological obligations, - falsification rule. ## Rejected Promotions The following promotions are not allowed: - contact map to native structure, - candidate bifurcation to real turn without structure comparison, - bounded winding trace to 
- **Paper 23.75 - FoldForge Next-State Bridge.** # Paper 23.75 - FoldForge Next-State Bridge ## Bridge Role Paper 23 exports a chain-descriptor pattern. It starts with a local sequence, builds contact or adjacency receipts, marks candidate transitions, and keeps global interpretation open until a domain verifier closes it. ## Exported Artifacts The next state receives: - local chain-window discipline, - contact-map receipt discipline, - candidate transition marks, - bounded topology/winding witness status, - explicit validation obligations, - invalid-promotion labels. ## Use in Paper 24 Paper 24 may translate the chain and contact-map idea into paths on a board or automaton lattice. A chess or game-state path may be read as a local sequence with adjacency receipts, but it must prove its own rules and reachability. ## Use in Later Applied Papers Later biological, material, CAD, or game papers may use the FoldForge pattern when an object
- **Paper 23 - FoldForge Protein Folding (UPGRADED: Affirmative Protein Descriptor Physics Map).** (Affirmative)

## Receipt Surface

| Receipt | Summary |
|---------|---------|
| `foldforge_descriptor_receipt.json` | status=pass_with_open_obligations |
| `calibration_plan.json` | status=template_ready_needs_bioparser |

## Open Obligations as Next Needs

| ID | Current row | CAM/GLM status |
|----|-------------|----------------|
| `23.1` | \| 23.1 \| PDB validation \| External calibration \| | carry as next need |
| `23.2` | \| 23.2 \| Native structure prediction \| External calibration \| | carry as next need |
| `23.3` | \| 23.3 \| Depth-only winding extraction \| Tooling \| | carry as next need |
| `23.4` | \| 23.4 \| Biological encoding parser \| Engineering \| | carry as next need |
| `23.5` | \| 23.5 \| Fold-rate and thermodynamic validation \| External calibration \| | carry as next need |

## Obligation Springboard Lanes

Obligations return to the earliest paper they can affect, then rework upward through each paper in the lane before the local claim is promoted.

### Local Claim Pressure

- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.
- Engineering and adapter gaps should be promoted to work items, not used as theorem premises.

### Local Lane Table

| Obligation | Return start | Upward lane | Rework instruction |
|------------|--------------|-------------|--------------------|
| `23.1` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `23.2` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `23.3` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `23.4` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `23.5` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |

## Detailed Expansion Pass

### Paper-Level Thesis

Paper 23 functions as the suite's FoldForge protein-folding calibration bridge. Its virtuous version should therefore make three layers visible at once: the formal claim that is actually proved, the receipt or verifier evidence that lets the claim be replayed, and the explicit boundary that prevents the reader from promoting an open lift into a closed theorem.

The companion variants are used as exposition and interface contracts. They may contribute terminology, examples, and downstream preconditions, but the canonical formal paper remains the proof spine.

### Claim Status Ledger

No explicit claim/theorem lines were extracted from the formal spine. Use the abstract, proof, receipts, and obligation table to reconstruct the claim ledger before publication.

### Evidence and Receipt Detail

The receipt surface should be discussed in prose, not only listed. Passing receipts make the paper replayable; failed, partial, or missing checks become local boundaries.
- `foldforge_descriptor_receipt.json`: status=pass_with_open_obligations.
- `calibration_plan.json`: status=template_ready_needs_bioparser.
Verifier files are the strongest executable surface. The paper should name the verifier next to any claim it supports.
- `verify_foldforge_descriptor.py` should be mapped to the claim or obligation it checks.

### Obligation Workups

**23.1.** | 23.1 | PDB validation | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `FoldForge protein-folding calibration bridge` boundary before this obligation can strengthen the source paper.

**23.2.** | 23.2 | Native structure prediction | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `FoldForge protein-folding calibration bridge` boundary before this obligation can strengthen the source paper.

**23.3.** | 23.3 | Depth-only winding extraction | Tooling |

- **Status reading:** requires tooling/adapter work before theorem use.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`.
- **Paper-local consequence:** Route this into tooling or adapter work before using it as a premise in the paper's theorem.
- **Rewrite requirement:** turn the gap into an adapter/tooling task and avoid depending on it as a completed premise.
- **Upward effect:** Papers in the lane must preserve the `FoldForge protein-folding calibration bridge` boundary before this obligation can strengthen the source paper.

**23.4.** | 23.4 | Biological encoding parser | Engineering |

- **Status reading:** requires tooling/adapter work before theorem use.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`.
- **Paper-local consequence:** Route this into tooling or adapter work before using it as a premise in the paper's theorem.
- **Rewrite requirement:** turn the gap into an adapter/tooling task and avoid depending on it as a completed premise.
- **Upward effect:** Papers in the lane must preserve the `FoldForge protein-folding calibration bridge` boundary before this obligation can strengthen the source paper.

**23.5.** | 23.5 | Fold-rate and thermodynamic validation | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `FoldForge protein-folding calibration bridge` boundary before this obligation can strengthen the source paper.

### Cross-Paper Inheritance

The springboard lane means this paper cannot be revised in isolation. The upstream papers in the lane must preserve the following inherited roles before the local claim can be strengthened:

- Paper 09: finite Hamiltonian-window substrate and receipt-preserving temporal readout.
- Paper 10: master receipt, replay boundary, and open-lift visibility layer.
- Paper 11: theory-admission gate and boundary classifier.
- Paper 12: cellular-automaton prediction surface and Rule 30 scope boundary.
- Paper 13: Standard-Model quark-face transport and calibration boundary.
- Paper 14: GR boundary-repair curvature map and physical-curvature guard.
- Paper 15: QFT/Higgs mass-residue carrier and measured-mass calibration guard.
- Paper 16: continuum-edge residual layer and finite-window-to-limit boundary.
- Paper 17: E6/E8 correction tower and exceptional-lattice lift surface.
- Paper 18: VOA/Moonshine representation route and identification guard.
- Paper 19: observer face-selection and physical-observer boundary.
- Paper 20: layer-2 synthesis ledger and reachability status surface.
- Paper 21: MorphForge/PolyForge/MorphoniX engineering bridge.
- Paper 22: MetaForge applied-materials calibration bridge.
- Paper 23: FoldForge protein-folding calibration bridge.

### Publication-Grade Rewrite Targets

For the next manual/editorial pass, expand the paper body around these targets:

1. Put the strongest closed theorem in the opening synthesis, then immediately state the largest thing it does not prove.
2. Move every calibration, physical-identification, and external-validation claim into a guarded paragraph with its required witness named.
3. Place verifier and receipt names beside the exact claims they support.
4. Preserve open lifts as first-class obligations rather than treating them as editorial TODOs.


## Canonical Formal Spine

## Abstract

Paper 23 applies the Forge reading discipline to protein-chain descriptors. Its
closed result is not a protein structure predictor. Its closed result is a
replayable descriptor receipt: a residue chain is converted into local `(L, C,
R)` windows, a contact-map receipt is generated, local side changes are marked
as candidate bifurcations, and the result is paired with the bounded oloid
winding substrate and its explicit open gaps.

The receipt proves that FoldForge can emit candidate fold/topology descriptors
without hiding the difference between a descriptor and a biological prediction.
It does not claim native coordinates, free-energy minima, fold rates, AlphaFold
parity, PDB validation, or measured thermodynamic behavior.

## Closed Evidence

The verifier uses the sequence `MKTFFVLLLCTFTVLA` as a compact demonstration
chain. It encodes residues by a simple hydrophobic/polar bit, produces 16 local
windows, and has 14 complete interior `(L, C, R)` windows. The contact-map
heuristic emits a symmetric, zero-diagonal map with nonzero contacts. Local side
changes in the residue windows become candidate bifurcation marks.

The lattice substrate contributes a bounded winding witness. With `max_depth =
512` and `max_order = 4`, the winding proof returns `pass_with_open_gaps`; its
schema verifier passes; its operator is stable across pages; and its finite
operator has 8 states. The standing gap is named:
`DEPTH_ONLY_WINDING_EXTRACTOR_PENDING`.

The direct oloid predictor is not promoted beyond its evidence. On a 128-depth
window it returns `pass_with_open_gaps` with defects, so Paper 23 treats it as
diagnostic substrate rather than biological proof. The bifurcation detector
schema also passes with open gaps and carries
`MIGRATION_DIRECTION_FORCED_BY_PARITY_PENDING`.

## Definitions

A residue chart is the sequence of overlapping local windows
`(residue[n-1], residue[n], residue[n+1])`. `C` is the active residue. `L` and
`R` are its two backbone neighbors. A contact map is a symmetric matrix recording
which residue pairs satisfy the selected contact predicate. In this verifier the
predicate is deliberately simple: separated hydrophobic residues form a
candidate contact. A bifurcation mark is a side-change event in the local
window, used as a candidate turn or topology marker.

A winding trace is the bounded oloid/spinor trace supplied by the lattice
substrate. It is a trace witness, not a depth-only theorem. A FoldForge descriptor
is admitted only when it carries both its contact-map receipt and its open
validation obligations.

## Claims

1. A residue chain can be read as local CQE windows.

The verifier constructs one chart row per residue and confirms that the interior
chain has complete left-center-right windows.

2. A replayable contact-map receipt can be emitted.

The example contact map is symmetric, has zero diagonal, has nonzero contacts,
and has density strictly between 0 and 1. This proves the receipt format and
replay rule, not biological correctness.

3. Local side changes can be marked as candidate fold events.

The local window sequence emits side-change marks. These marks are descriptors
only; they become biological claims only after comparison to deposited or
experimentally measured structures.

4. The oloid winding substrate is bounded and honest about its gap.

The winding model verifies as a bounded trace witness with a stable 8-state
operator. It also carries the depth-only extractor gap, so the paper does not
claim a closed all-`N` winding formula.

5. FoldForge remains a candidate descriptor until validated.

The direct oloid predictor and bifurcation detector both carry open gaps. Paper
23 treats those gaps as part of the result.

## Theorem 23

FoldForge is a valid CQE protein-fold descriptor kernel when it returns a
replayable residue-window chart, contact-map receipt, candidate bifurcation list,
bounded winding witness, and explicit validation obligations for a chosen
protein-chain observation.

## Proof

Run `verify_foldforge_descriptor.py`. The first check builds the residue chart
and verifies the local-window count. This imports the Paper 21 reader into a
protein-chain setting without making any global structure claim.

The second check builds the contact map. Symmetry and zero diagonal are required
because a residue-residue contact is an unordered relation and a residue is not
treated as contacting itself. Nonzero contact density proves that the example
produces a reviewable receipt.

The third check marks local side changes. These marks are the candidate
bifurcations. They are useful precisely because they are not allowed to become
turn, knot, or fold claims without a later PDB comparison.

The fourth check verifies the bounded winding substrate. The accepted claim is
the bounded trace witness and stable operator. The receipt also records
`DEPTH_ONLY_WINDING_EXTRACTOR_PENDING`, so an all-depth shortcut is not silently
claimed.

The fifth and sixth checks confirm that the less-closed substrate components
remain visible. The oloid predictor has defects in the tested window, and the
bifurcation detector carries its parity-direction gap. Because the verifier
passes only while those gaps remain explicit, the paper proves the descriptor
kernel and not a biological structure theorem.

Therefore Paper 23 closes FoldForge as a reproducible contact-map and topology
descriptor surface with open biological validation obligations.

## Receipt

The formal receipt is generated at:

`production/formal-papers/CQE-paper-23/foldforge_descriptor_receipt.json`

## Open Obligations

PDB validation remains open. Native structure prediction is not claimed.
Depth-only winding extraction remains open. The biological encoding remains a
demonstration choice. Fold-rate and thermodynamic validation remain open.

## Suite Role

Paper 22 proves the applied candidate-ledger pattern. Paper 23 uses the same
pattern for protein-chain descriptors. Paper 24 may reuse the local-window and
path-descriptor discipline for game or automata lattices, but it must not inherit
protein-specific biological claims.

## Rework Integration Notes

- Keep the claim-strength tags attached to each theorem or bridge.
- Import companion variant language only when it strengthens exposition without
  promoting an open bridge.
- Treat every obligation row as a routed next-need: verifier, witness, adapter,
  calibration, documentation pass, or explicit guard.
- If a CAM/GLM row proposes `partially_closed`, update the paper body and
  obligation audit together; do not silently mark it closed.
## Upward Rework Intake

Downstream obligations now spring back through this paper. Rework this paper's definitions, receipts, guards, and claim-strength language before carrying the lane upward.

### Reasoned Claim Pressure

- Receipt-closed items may strengthen replayability and audit language, but they do not close unrelated transport, physical, or cold-start mathematical obligations.
- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.
- Engineering and adapter gaps should be promoted to work items, not used as theorem premises.
- Guard obligations must appear next to the claims they constrain, so the reader cannot miss the boundary.

### Intake Category Counts

| Category | Count |
|----------|------:|
| `external_calibration` | 14 |
| `open_next_need` | 9 |
| `claim_guard` | 5 |
| `engineering_gap` | 3 |
| `closed_receipt` | 1 |
| `receipt_integrity` | 1 |

### Routed Lanes

| Source | Obligation | Full lane | Required local action |
|--------|------------|-----------|-----------------------|
| `24` | `24.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `24` | `24.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `24` | `24.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `24` | `24.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `25` | `25.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `25` | `25.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `25` | `25.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `25` | `25.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `27` | `27.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `27` | `27.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `27` | `27.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `27` | `27.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `28` | `28.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28` | `28.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28` | `28.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `28` | `28.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `28` | `28.5` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `29` | `29.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `29` | `29.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `30` | `30.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `30` | `30.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `30` | `30.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout. |
| `31` | `31.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `31` | `31.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims. |
| `31` | `31.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `32` | `32.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32` | `32.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32` | `32.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `32` | `32.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
