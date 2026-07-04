# CAM Claim 100-Score Audit

**Status:** first-pass cross-paper scoring surface.  
**Scope:** Papers 00-32, evaluated with all paper evidence, CAM/crystal routes,
Claude/CL claim-strength sweep evidence, supplements, verifier catalogs, and
cross-paper obligation springboards allowed.

---

## Provenance

The user reported that Claude created a new 1-100 grading surface for open
claims. The explicit scale was found in the user-profile Claude memory store
and in the CAM runtime it references.

Local evidence found:

- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/claim-governance-scale.md`
- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/claim-policy-correction.md`
- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/cam-mesh-architecture.md`
- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/binding-requires-attached-data.md`
- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/reapplication-lane.md`
- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/forge-promotion-pattern.md`
- `C:/Users/nbark/.claude/projects/d--CQE-CMPLX/memory/governance-t0-t10-ribbon.md`
- `Paper Reworks/CLAUDE_MEMORY_HARVEST.md`
- `D:/repo_harvest/_CAM/governance_scale.py`
- `D:/repo_harvest/_CAM/repo_harvest_cam.db`
- `Claude-Codex-Memory/Memos between CL_CX_HM/2026-06-14_08-45-21-0700_CL-to-CX-HM_Claim-Strength-Sweep-Affirmative-Verifiers-Bound-Prose-Upgrade-List.md`
- `Paper Reworks/PAPER_REWORKS_CRYSTAL_REPORT.md`
- `Paper Reworks/PAPER_REWORKS_CRYSTAL_PROJECTION.json`
- `Paper Reworks/virtuous/OBLIGATION_REASONING_AUDIT.md`
- `Paper Reworks/virtuous/OBLIGATION_SPRINGBOARD_INDEX.md`
- `Paper Reworks/supplements/SM_BRIDGE_SUPPLEMENT.md`
- `Paper Reworks/supplements/RECEIPT_VERIFIER_CATALOG.md`
- `D:/MannyAI/BUILD_MANIFEST.md`
- `D:/MannyAI/vendor/lattice_forge/OpsGuide.md`
- `D:/MannyAI/research/carrier-cem/OCEM1_ACCURACY_RESULT.md`
- `D:/MannyAI/pitch/src/05_Results_and_Verification.md`

Therefore this audit uses Claude's Safe-to-Claim 1-100 governance scale. The
live MannyAI CAM vault named by the manifest
(`data/manny_cam.db` or `MANNY_CAM_DB`) was not present on disk in this checkout,
so private/gitignored MannyAI CAM nodes could not be read directly.

## Claude Safe-to-Claim Gates

The scale retires binary "open" as a quarantine label. Every obligation needs a
score and a candidate closing form.

| Gate | Meaning |
|------|---------|
| 50 | Internal-Closure: bound content-hashed PASS receipt. |
| 80 | Reachability / quarantine lift: remaining gap is a confirmed-obtainable resource, such as an importable theorem or fetchable real data. Items at 80-100 are closeable-now. |
| 90 | Binding: closing datum is actually attached and content-hashed, not merely named. |
| 100 | Paper: bound, reproduced, and Paper 00 burden updated; publishable. |

Claude's demo scores from `governance_scale.py`:

| Claim | Score | Reading |
|-------|------:|---------|
| Paper 13 CKM calibration | 86 | available data; PDG values are fetchable, so the item is closeable-now rather than quarantined. |
| Papers 02/09/16/18 McKay-Thompson O2-prime parity | 72 | anchor named; route exists, but no located theorem/data closes it yet. |
| Paper 12 cold-start Rule30 Problem-3 nth-bit | 66 | IPMC structural-strong; genuine gap remains, transport-only until a closing form appears. |

## MannyAI Evidence Imported

`D:/MannyAI` is an adjacent CAM/crystal build, not a prose-only mirror. It adds
the following evidence classes to this audit:

- **CAM mesh base.** `BUILD_MANIFEST.md` states that MannyAI exposes the
  vendored CrystalForge CAM and Carrier-CEM through MCP tools (`cam_add_node`,
  `cam_list_crystals`, `cam_get_crystal`, `cem_run`), with the real CAM vault at
  `data/manny_cam.db` or `MANNY_CAM_DB`.
- **Honesty grading.** `vendor/lattice_forge/OpsGuide.md` states that honesty
  grading is the obligation system: `PROVEN`, `BOUNDED_EXEC`, and `CONJ`, with
  counts of 402 proven, 26 bounded-execution, and 35 conjectural labels in the
  lattice-forge substrate.
- **CEM learning correction.** `research/carrier-cem/OCEM1_ACCURACY_RESULT.md`
  closes O-CEM-1 as a measured result: cold start equals base rate, while the
  trained beat gives a +40 point gain on the signal-bearing control task.
- **Spatial/crystal receipts.** `pitch/src/05_Results_and_Verification.md`
  reports 598 passing tests, 8/8 lossless LCR color states, 3D round-trip maximum
  residual 1.41e-6 under a 1e-4 tolerance, deterministic per-grammar hashes,
  Merkle receipts, semantic child-fork protection, and CPU/GPU render parity.

These findings modify the interpretation of "open" claims: CEM cold-start
claims must be phrased with the measured base-rate/trained-gain split, while
SplatForge/crystal-field claims may be promoted as bounded-execution evidence
where the paper needs deterministic spatial projection, receipt chaining, or
lossless information-hologram support.

## Scoring Rubric

| Score band | Meaning |
|------------|---------|
| 96-100 | Reproduced and packaged; 100 means in paper with Paper 00 burden updated. |
| 91-95 | Bound single-source; data/theorem attached and content-hashed, not yet independently reproduced. |
| 86-90 | Available data; real dataset located and access-confirmed. Closeable-now. |
| 81-85 | Importable theorem; theorem exists, needs import and Paper 00 burden update. Closeable-now. |
| 76-80 | Anchor confirmed-obtainable; theorem/data accessible enough to lift quarantine at 80. |
| 71-75 | Anchor named; route or candidate closing resource identified, but not confirmed as obtainable. |
| 66-70 | IPMC structural-strong: internal map has invariant/idempotent/no-free-parameter strength, but no confirmed external closing form. |
| 61-65 | IPMC integrated into the corpus DAG. |
| 56-60 | IPMC corroborated by multiple internal checks. |
| 51-55 | IPMC single verifier. |
| 46-50 | Bound internal receipt. Gate 50 internal closure. |
| 1-45 | Below bound internal closure: from notion/assertion through unbound reproducible pass. |

Important: a score below 100 does **not** mean "not true." It means "not yet
admitted as a fully composed paper claim under the evidence currently bound in
this folder." A score of 80 or above means **closeable-now** under Claude's
quarantine-lift rule. Scores below 80 should remain visible and scored, but not
treated as already resource-closeable.

## Cross-Paper Evidence Rules

Allowed evidence:

- paper-local formal body and receipts;
- all 00-32 papers as mutual support;
- CAM/crystal reports and projected routes;
- Claude Safe-to-Claim memory and CAM runtime;
- Claude/CL affirmative verifier memos;
- supplements and receipt verifier catalogs;
- standard external math/physics already accepted by Paper 00;
- IRL datasets when the route is clear but not yet cited or materialized.

Disallowed promotion:

- measured physics claims without units, data source, or calibration receipt;
- a paper-local claim promoted solely by wording in a source variant;
- an analogy promoted into identity without a verifier or standard-model anchor.

## 00-32 Scorecard

| Paper | CAM 100 score | Current admission class | Strongest cross-paper support | Remaining admission work |
|-------|--------------:|-------------------------|-------------------------------|--------------------------|
| 00 | 96 | system-composition closed | grounding contract, imported theorem burden, T3-T7 foundation, claim taxonomy | citation polish and cross-paper burden table finalization |
| 01 | 94 | internally closed | LCR minimality, shell-2 doublet, local O8 double cover, Paper 03 carry-forward | physical spinor transport remains NP-10/physics bridge |
| 02 | 93 | internally closed | exact Rule30/Rule90 correction surface, two-state firing set, Paper 03 coordinate preservation | McKay parity and E-lift routed beyond paper-local scope |
| 03 | 94 | internally closed | LCR/D4/J3 registration, T1-T7, D12, S3 anneal, D4 atlas, block tower | full D4/F4/off-diagonal theorem is NP-04 |
| 04 | 93 | internally closed | typed repair constraint, falsifier, Paper 05 payload intake | shared ledger population and domain examples |
| 05 | 91 | system-composition closeable | rolling carrier, payload non-interference, oloid family, gluon worldline, CD theta-zero | physical oloid geometry and cold prediction admission |
| 06 | 92 | system-composition closeable | typed causal edges, Rule90/Lucas, triadic keystone, negative extraction verdict | full 32-paper graph/hash population |
| 07 | 90 | internally closed | sample-preserving bridge, MDHG/SpeedLight retraction, O3 structural closure | between-sample physics and general F4 encoder theorem |
| 08 | 91 | system-composition closeable | finite E8/E8x3/Niemeier chain, no-cost Leech lookup, lattice forge surfaces | expanded Leech invariants and nontrivial glue cosets |
| 09 | 84 | bounded/system-closeable | Hamiltonian window, Paper 05 accumulated carrier, Paper 10 readout, Paper 16 continuum links | unbounded McKay/O2-prime correction collapse |
| 10 | 88 | strong aggregate receipt | T10 master receipt, path normalization closure, terminal route staging | exceptional-to-Niemeier route scope and cold extraction guard |
| 11 | 90 | internally closed | K=9 boundary admission gate, Pariah/Happy-Family boundary example, T10 trust anchor | encoder-invariance of sporadic boundary |
| 12 | 84 | bounded/system-closeable | CA prediction surface, Rule30/Rule90 decomposition, silent-boundary rules, Paper 06 Lucas support | infinite nonperiodicity/cold P3 promotion |
| 13 | 92 | internally closed, external calibration pending | CL affirmative verifier: exact SU(3) color transport, QuarkFaceForge 10/10, Paper 03 trace/face support | CKM and measured quark/color bridge dataset |
| 14 | 87 | internal curvature map closed | CL affirmative verifier: curvature = correction = C-participation, Rule90 flat | measured GR/Einstein bridge and physical calibration |
| 15 | 89 | internal mass-residue map closed | CL affirmative verifier: mass = VOA weight, 2 massless + 6 massive, Paper 18 VOA support | measured Higgs/QFT mass calibration |
| 16 | 79 | partial/system-closeable | continuum edge residuals, Paper 07 bridge, Paper 02 correction, power-of-ten windows | global continuum limit and McKay/O2-prime collapse |
| 17 | 84 | bounded exceptional tower | E6/E8 tower, practical Leech lookup support from Paper 08, lattice forge surfaces | expanded Leech invariants, Weyl extractor, Gamma72 detail |
| 18 | 81 | bounded VOA/Moonshine route | centroid/VOA sector routes, Monster/McKay support from Papers 29/06/09 | full Moonshine identification and correction_via_voa route |
| 19 | 92 | internally closed | CL verifier: observation = D4 face selection, 7 latent, lossless; Paper 27 observer-delay guards | SPINOR/open-gap physical observer evidence |
| 20 | 92 | aggregate ledger closed | CL verifier: Event-Law receipt ledger monotone/zero-drift, typed graph from Paper 06 | full graph tooling and unknown/forbidden reachability presentation |
| 21 | 83 | applied/system-closeable | MorphForge/PolyForge/MorphoniX, Leech import support, golden-ratio AGRM reader | applied reader validation and TF1 measurement |
| 22 | 82 | applied forge closeable | MetaForge materials, material-ledger routes, TMD/interlayer exciton candidate, applied forge supplement | finite-element/fabrication/material measurement datasets |
| 23 | 74 | applied partial closure | FoldForge contact/homology/winding framing, parser route, applied forge validation lane | PDB/native structure parser and fold-rate validation |
| 24 | 86 | internally strong combinatorics | knight L-conjugate CA, N-dimensional count route, CL underclaim candidate | OEIS/playability/game-review validation |
| 25 | 88 | internal energy ledger closed | CL verifier: kappa=ln(phi)/16 conservation descent, energy ledger 5/5 | joule conversion and physical units calibration |
| 26 | 80 | carrier-level pinch/shear closed | carrier-level Z-pinch/shear horizon, Paper 14 curvature/repair, Paper 25 energy support | measured plasma/Z-pinch observable and calibration |
| 27 | 88 | finite observer model closed | observer delay/shared center, static Z4 guard, temporal Z4 counterexamples, Paper 19 face selection | human latency/consciousness/collapse measurements |
| 28 | 89 | internally closed game lattice | CL verifier: N-dim knight count = 4d(d-1), d=3 -> 24, D4/24-cell tie | complete game theory, real-piece geometry, OEIS review |
| 29 | 90 | internal Monster map closed | CL verifier: 196883=47*59*71, McKay anchors 783/4372, Paper 18 route support | measured universal energy-bound witness and encoder invariance |
| 30 | 90 | meta-ribbon enacted | Grand Ribbon, corpus route, NP springboard, Paper 31 retrospective support | graph tooling and follow-on paper materialization |
| 31 | 91 | retrospective LCR readout closed | meta-LCR enactment, Paper 30/32 wrap, downstream metadata status | preserve as downstream readout, not upstream premise |
| 32 | 87 | supervisor cursor/coverage closed | scheduler coverage, n=4/5 minimality, n=8 upper record 46205, wrap to Paper 01 | n>=6 superpermutation minimality/exclusion proof |

## Quarantine-Lift Summary

Under Claude's actual governance scale, a score of 80 or higher enters the
closeable-now lane. This first pass places **31 of 33 numbered papers** at or
above 80 when all cross-paper, CAM, crystal, MannyAI, and verifier evidence is
allowed.

| Lane | Papers | Meaning |
|------|--------|---------|
| 96-100 reproduced/package lane | 00 | already near publishable as the burden contract. |
| 91-95 bound single-source lane | 01, 02, 03, 04, 05, 06, 08, 13, 19, 20, 31 | strong binding or internal closure; work is mostly packaging, burden updates, or named external calibration. |
| 86-90 available-data lane | 07, 10, 11, 14, 15, 24, 25, 27, 28, 29, 30, 32 | closeable-now with data, theorem import, or receipt binding work. |
| 80-85 import/reachability lane | 09, 12, 17, 18, 21, 22, 26 | quarantine lifted; needs the named closing form attached. |
| below 80 still-gapped lane | 16, 23 | not rejected, but not yet resource-closeable under the found evidence. |

Immediate implication: Paper 16 needs its continuum/McKay route split so the
reachable parts can score independently above 80; Paper 23 needs a PDB/parser
closing form attached before it leaves the still-gapped lane.

## MannyAI-Adjusted Deltas

| Paper | Delta | Reason |
|-------|------:|--------|
| 05 | +1 | MannyAI proves the CEM training beat works when signal exists, but also retires any cold-start-is-100 framing. |
| 07 | +1 | SplatForge/field receipts strengthen sample-preserving projection and deterministic field retraction. |
| 10 | +1 | MannyAI vendoring and standalone loop evidence strengthen terminal route packaging. |
| 21 | +1 | Crystal-to-SpatialField and multi-grammar hashes strengthen applied reader representation. |
| 22 | +1 | Deterministic material/field projection and render parity support applied forge validation scaffolding. |
| 30 | +1 | CAM mesh base evidence strengthens corpus-route and next-paper springboard mechanics. |

The score table above already reflects these deltas. The CEM correction is not a
pure upgrade: it raises trained-CEM claims while lowering any paper language that
implies universal cold-start accuracy without a learned signal.

## Immediate Upgrades From Claude/CL Sweep

These should be treated as already available system-composition evidence:

| Paper | Upgrade |
|-------|---------|
| 06 | Lucas axis readout closes why Rule 90 removes C on one triadic axis. |
| 13 | QuarkFaceForge closes exact SU(3) color transport internally. |
| 14 | Curvature-is-correction verifier closes the internal curvature substrate. |
| 15 | MassResidueForge closes mass = VOA weight internally. |
| 19 | Observation-is-face-selection closes finite D4 observation. |
| 20 | Solution ledger closes monotone zero-drift event law. |
| 25 | Energy ledger closes kappa conservation descent internally. |
| 28 | N-dimensional knight count closes the combinatorial core. |
| 29 | Monster internal map closes the internal scalar/McKay anchor map. |

## Highest-Value Cross-Paper Closures To Attempt Next

| Target claim | Papers/tools to compose | Why it should move |
|--------------|-------------------------|--------------------|
| Physical bridge taxonomy for Papers 13-16 | Papers 03, 06, 13, 14, 15, 16, NP-12, SM supplement | distinguish internal proof from measured calibration without calling the internal claim open |
| Leech/Gamma72 landing | Papers 08, 17, 21, lattice_forge unification | no-cost lookup is already closed; expanded invariant witnesses are the remaining admission layer |
| Cold Rule 30 correction collapse | Papers 02, 06, 09, 12, 16, 18 | correction surface + Lucas sparsity + VOA routes are all present; remaining work is exact parity/fingerprint admission |
| Applied material/exciton accounting | Papers 05, 07, 22, NP-12 | standard electron-hole-exciton formalism can close part of the material bridge now |
| Full causal graph/replay surface | Papers 00-32, Paper 06, Paper 20, CAM reports | graph/hash population is engineering-closeable and would raise many scores |

## Machine-Readable Companion

The machine-readable companion is:

```text
CAM_CLAIM_100_SCORE_AUDIT.json
```
