# FLCR-28 Workbook - CAM, Crystal Projectors, And MannyAI Runtime

## Purpose

This workbook turns the CAM/crystal projector paper into a replayable runtime
exercise. A reader should be able to take a source object in any form, assign a
CAM address, project it through faces, collect vignettes, and route the result
to the next paper or algorithm without losing the source boundary.

## Materials

- `FLCR-28/formal.md`
- `CLAIM_LANE_SCHEMA.json`
- `PAPER_REWORKS_CRYSTAL_PROJECTION.json`
- `AGENT_CRYSTAL_WORK_HARVEST.json`
- Kimi standards/window/node databases
- MannyAI runtime/source folders
- Lattice forge actionization APIs
- Any source document, receipt, validator, figure, notebook, memory, or analog
  object being imported

## Projector Algorithm

Use this algorithm for every CAM/crystal import:

| Step | Action | Output |
|---|---|---|
| 1 | Create or locate the crystal | CAM address, source path, source hash if available |
| 2 | Load available faces | formal, companion, workbook, receipt, JSON, validator, API, memory, analog |
| 3 | Shine light through each face | claim-lane query, dependency query, residue query, falsifier query |
| 4 | Capture vignettes | small evidence readouts with source path and boundary |
| 5 | Route to next algorithm | import, compare, normal-form, tarpit, forge, calibration, falsifier, or obligation |

## 2x2 Adapter Handshake Worksheet

| Quadrant | Fill for this import |
|---|---|
| Source object | Exact source state, file, receipt, or memory object |
| Source face | Which representation is being projected |
| Target lane | Which claim lane the destination paper can consume |
| Target action | What the next algorithm is allowed to do |

The adapter succeeds only if all four cells are filled. If one cell is missing,
the row becomes an open obligation, not a silent import.

## CAM Address Receipt

```yaml
paper: FLCR-28
cam_address: ""
source_path: ""
source_hash: "external_or_pending"
faces_loaded:
  - formal
  - receipt
  - validator
projector_query: ""
vignette_output: ""
target_paper: ""
target_lane: ""
target_action: ""
residue: ""
falsifier: ""
```

## Face Query Table

| Face | Query | Required answer |
|---|---|---|
| Formal text | What claim does this support? | Claim sentence and lane |
| Receipt | What operation was replayed? | Input, operation, output, residue |
| Validator | What domain passed or failed? | Scope, count, pass/fail, limitation |
| Source card | What older work contributes? | Contribution and boundary |
| Forge/API | What lookup can be run? | Function, input, output, cache row |
| Analog | What state is preserved by relabeling? | Invariant object and transfer rule |
| Agent memory | What did the agent produce? | Source path, confidence, required corroboration |

## Vignette Record

Each vignette should be short but complete:

| Field | Required content |
|---|---|
| Vignette ID | Stable local ID |
| Source face | Which face produced the readout |
| Useful datum | What the readout contributes |
| Destination | Paper, supplement, forge, validator, or normal-form queue |
| Boundary | What the readout refuses to prove |
| Next action | Import, compare, calibrate, falsify, or leave as obligation |

## Forge Actionization

Use this table when a CAM object can become a lookup, verifier, or cached
answer.

| CAM item | Forge/API action | Typed result | Receipt/cache row | Boundary |
|---|---|---|---|---|
| Leech address candidate | `Forge.leech_lookup(address, payload)` | lookup result | lookup receipt | proves addressable construction only at input scope |
| Leech verifier | `Forge.verify_leech_lookup()` | pass/fail | verifier receipt | does not replace external calibration |
| Lattice code chain | `verify_lattice_code_chain` | chain validity | lattice receipt | limited to implemented code path |
| Golay-24 route | `verify_golay_24` | code validity | Golay receipt | not a physical claim by itself |
| Leech ribbon | `encode_leech_ribbon` | encoded ribbon | encoding receipt | downstream identity requires adapter |

## Worked Replay: Importing Kimi Standards

| Step | Filled value |
|---|---|
| Source object | Kimi standards/window report |
| Source face | conformance verdict and window database |
| Vignette | 192/192 conformance can support standards-surface claims |
| Target lane | `normal_form_result` or `cam_crystal_reapplication_result` |
| Target paper | FLCR-30, FLCR-39, FLCR-40 |
| Boundary | conformance is not physical calibration |
| Next action | attach standards row to claim-lane or falsifier table |

## Worked Replay: Importing Claude/MannyAI Crystal Work

| Step | Filled value |
|---|---|
| Source object | Agent crystal harvest or MannyAI runtime artifact |
| Source face | memory, source route, generated crystal, or instruction doc |
| Vignette | identifies a source, claim, route, or missing obligation |
| Target lane | `cam_crystal_reapplication_result` until corroborated |
| Target paper | whichever paper owns the object being routed |
| Boundary | agent output is not proof without receipt/citation/validator |
| Next action | source-placement, claim-binding, or workbook replay row |

## Analog Exercise

Build a physical crystal projector with index cards:

1. One card is the CAM address.
2. Each face is a different card: formal, receipt, validator, source, analog,
   forge, memory.
3. Shine a "query" by choosing one question: claim, dependency, residue,
   falsifier, or downstream use.
4. Write one vignette card.
5. Place the vignette in the target paper's tray.
6. Keep the source card attached so the vignette cannot become anonymous proof.

## Completion Criteria

- Every projected object has a CAM address or source path.
- Every face read produces a vignette with boundary.
- Every downstream import has a lane.
- Every forge action has an input, output, and receipt/cache row.
- Private or unavailable vault data remains explicitly marked as unavailable.
- No paper consumes agent memory, crystal output, or forge lookup as proof
  without the required receipt, citation, normal-form, calibration, or falsifier
  row.

## Label-Preserving Analog Transfer

The workbook must demonstrate that the author's interpretation changes labels,
coordinates, access paths, or analog handles, not the underlying addressed
state. The analog route should therefore be auditable against the formal claim
lane and the original ribbon role.

| Original slot | Family | Lift | Role | Proof form |
|---|---|---:|---|---|
| orbital | publication overlay | n/a | no legacy original slot assigned yet | intake and routing proof |

| Transfer check | Required answer |
|---|---|
| Addressed state | What object, receipt, theorem, or construction is unchanged? |
| Label/access change | Which name, analogy, coordinate, or query path changed? |
| Evidence lane | Which claim lane permits the transfer? |
| Downstream import | Which later paper may consume this result, and with what boundary? |

## State-Preserving Analog Contract

Analog invariance test: an orbital index: it may point to many source states, but it must not relabel them as a single proved theorem without a lane.

The workbook exercise is to fill this table with concrete receipts, equations,
citations, code paths, or CAM/crystal queries:

| Check | Required content |
|---|---|
| Received state | Exact source object entering the paper |
| Formal carrier | Accepted theorem, construction, verifier, or receipt being used |
| Interpretation label | The author's label, analogy, or access-path change |
| Invariant state | What remains unchanged under that relabeling |
| Produced state | What downstream paper is allowed to import |

| Slot | Contract |
|---|---|
| orbital | publication overlay; must declare sources, dependencies, and calibration/falsifier boundaries |

## Claim Binding Workbook

For each queue item, fill the replay row before strengthening the paper.

| Queue item | Local claim | Later evidence | Revised claim | Boundary kept |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

| Queue | Promote now | Bind next | Residue |
|---|---|---|---|
| none directly assigned | Use source routing and claim lanes to identify paper-local binding actions. | Search verifier catalog and CAM/crystal routes by object name. | Keep unbound claims in falsifier/open-obligation lanes. |

## Delta Replay Table

The workbook should make each delta reproducible.

| Delta | Replay action | Boundary check |
|---|---|---|
| Search By Object Name | Search by object name and add the first concrete receipt/citation/calibration candidate. | Until then, claims remain in their existing lanes. |

## Journal Submission Workbook

Before this paper is submitted, complete these rows.

| Artifact | Status | Required completion |
|---|---|---|
| Figures `FLCR-28-F1`, `FLCR-28-F2`, `FLCR-28-F3` | planned | Convert text schematics into final diagrams or leave as formal schematic figures. |
| Tables `FLCR-28-T1`-`FLCR-28-T4` | planned | Ensure all claim/evidence/source-card/workbook rows are complete. |
| Glossary | drafted | Replace generic term meanings with paper-local definitions. |
| Appendix FLCR-28-A | drafted | Attach receipt paths, verifier paths, source cards, and remaining external requirements. |
| Reviewer checklist | drafted | Mark pass/fail before final PDF build. |

## Archive Evidence Replay Cards

Use these cards as workbook replay targets.

| Upgrade target | Evidence card | How it improves the paper | Boundary |
|---|---|---|---|
| object-name search | none yet | Search verifier catalog, CAM routes, and source placement for a concrete card. | No promotion without evidence. |

| Replay field | Required value |
|---|---|
| Source card | Which archive/mirror card is being used? |
| Exact source path | Where is the original source? |
| Receipt or verifier | What executable or receipt object does it name? |
| Claim effect | What claim becomes stronger, narrower, or better bounded? |
| Boundary retained | What the card still refuses to promote. |

## Crystal/CAM Replay Checklist

Use this checklist to turn past work into auditable workbook material.

| Replay item | Required workbook action |
|---|---|
| Routed full sources | Reconstruct the local object and cite the exact source rows used. |
| CAM/crystal report | Query or cite the face/vignette/CAM node route relevant to this paper. |
| Kimi standards/window data | Mark conformance/window evidence separately from claim validity. |
| NSIT closure matrix | Attach validator rows where they close the paper's internal claim. |
| Claude score audit | Use the score as admission posture, not as a replacement for receipts. |
| Analog interpretation | Show the invariant state before and after relabeling. |

### Sources To Replay First

| Source | Placement reason |
|---|---|
| `supplements/CRYSTAL_CAM_PROJECTOR_SUPPLEMENT.md` | primary assigned source for the paper's formal spine |
| `AGENT_CRYSTAL_WORK_HARVEST.md` | primary assigned source for the paper's formal spine |
| `PAPER_REWORKS_CRYSTAL_REPORT.md` | primary assigned source for the paper's formal spine |
| `supplements/CRYSTAL_CAM_PROJECTOR_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/METAFORGE_MATERIALS_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/SPECTRE_TILING_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/RECEIPT_VERIFIER_CATALOG.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/APPLIED_FORGES_WORKBOOK.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_PYRAMID_INDEX.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_5P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_7P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_9P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `CAM_CLAIM_100_SCORE_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_TOOL_CLOSURE_MATRIX.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_REASONED_CLOSURE_PASS.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `ORBITAL_DATA_CROSS_POPULATION_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| additional routed sources | 17 more entries remain in `SOURCE_PLACEMENT.md` |
