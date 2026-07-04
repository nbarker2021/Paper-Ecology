# FLCR-19 - Layer-2 Synthesis Ledger

**Series:** Formalizing LCR, Unifying Standard Models  
**Artifact:** formal paper source  
**Status:** first-pass rich rewrite; requires final citation and build pass.  
**Claim posture:** maximal local claim posture with explicit lane boundaries.

## Abstract

This paper formalizes the first higher-layer synthesis ledger over prior papers. The operative object is layer-2 synthesis ledger. The core result is that prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved. The paper also defines how this result routes forward: this ledger becomes the bridge from base formalization to applied forge papers. Its main residue is explicit: unknown and forbidden reachability must remain explicit rather than hidden in summary prose.

## Keywords

layer-2 synthesis ledger; LCR; receipt; claim lane; normal form.

## External Reader Orientation

An outside reviewer should read this paper as a formal-system construction paper. Its local object is **Layer-2 Synthesis Ledger**. The paper's immediate contribution is: Aggregates prior layers while preserving unknown, forbidden, and deferred rows.

The nearest external anchors are finite-state reasoning, typed interfaces, proof-carrying records, conservative extension, and ordinary mathematical citation discipline. LCR terms are therefore internal labels for the construction unless a row explicitly imports an external theorem, citation, dataset, or calibration target.

It does not ask the reader to accept any Standard Model or literal-physics identification at this layer. Such mappings are deferred to the translation papers and must carry their own evidence.

## Reviewer Compression

**Core object.** Layer-2 Synthesis Ledger.

**Primary result.** This paper contributes the local formal object and its safe downstream-use rule.

**Primary non-result.** This paper does not claim direct identity with Standard Model or physical objects.

**Review strategy.** Evaluate the formal claim rows first, then inspect the receipt/citation/calibration rows that support each claim. Appendices provide routing and implementation context; they should not be read as stronger than their lane permits.

## Peer Reviewer Assessment

Reviewer assumption: the reviewer has been briefed on the FLCR structure, claim lanes, CAM/crystal routing, forge/action surfaces, and the distinction between internal formal results and external physical calibration.

**Recommendation.** major revision, technically promising.

**Review score vector.** orientation=2, claim_granularity=2, evidence_visibility=2, falsifier_visibility=2, journal_apparatus=1, base_layer_boundary=2.

**Formal claim rows reviewed.** 3.

### Reviewer Strength Finding

The manuscript is now readable as a bounded formal-system paper: it identifies its local object, separates internal construction from physical interpretation, and exposes claim lanes for review.

### Major Revision Requests

- Convert the strongest proof sketch into numbered definitions, lemmas, and propositions with explicit dependencies.
- Replace placeholder source classes with final citation keys, receipt hashes, or dataset identifiers wherever possible.
- Move repeated pass-derived material into a compact evidence appendix and keep the main body focused on the paper-local argument.
- Add at least one worked example showing the local object, legal operation, receipt, residue, and downstream import rule.

### Minor Revision Requests

- Normalize theorem capitalization and punctuation.
- Add final figure/table captions where the text currently describes diagrams schematically.
- Ensure every acronym and local term appears in the paper-local glossary.

### Acceptance Blockers

- A reviewer can accept the formal contribution without accepting later physics claims, but only if final citations and receipt identifiers are attached.
- The proof sketch must be promoted into a formal proof or explicitly labeled as a construction argument.


## 1. Contribution And Scope

- Defines layer-2 synthesis ledger as a first-class FLCR object.
- States the local result: prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved.
- Routes downstream use through claim lanes rather than inherited prose: this ledger becomes the bridge from base formalization to applied forge papers.
- Preserves the residue boundary: unknown and forbidden reachability must remain explicit rather than hidden in summary prose.

This paper belongs to the LCR-native construction band. Physics and Standard Model language, when it appears, is only a deferred mapping cue, analogy, or explicitly bounded calibration target. The paper's base object must remain stable enough for later papers to cite without importing a stronger physical claim by implication.

## 2. Source Routing

Primary routed sources:

- `20_Layer_2_Synthesis_Ledger.md`
- `virtuous/20_Layer-2_Synthesis_Ledger_VIRTUOUS.md`
- `supplements/20_INTERNAL_REASONING_SUPPLEMENT.md`

Cross-corpus evidence classes:

- `CAM_CLAIM_100_SCORE_AUDIT.md`
- `NSIT_TOOL_CLOSURE_MATRIX.md`
- `NSIT_REASONED_CLOSURE_PASS.md`
- `PAPER_REWORKS_CRYSTAL_PROJECTION.json`
- standards, glue, window, and node databases where applicable
- notebook-derived review prompts and orbital source manifests

## 3. Definitions

- **Layer-2 ledger.** A composed ledger whose nodes are already receipt-bearing paper results.
- **Monotone event law.** The rule that accepted ledger additions preserve prior receipt state.
- **Receipt boundary.** The exact scope in which the paper's result can be replayed or consumed.
- **Promotion route.** The evidence path required before a stronger downstream claim can use this result.

## 4. Formal Claims

| Claim | Lane | Statement |
|-------|------|-----------|
| Theorem 19.1 | `receipt_bound_internal_result` | prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved |
| Proposition 19.2 | `normal_form_result` | layer-2 synthesis ledger can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 19.3 | `falsifier_or_open_obligation` | unknown and forbidden reachability must remain explicit rather than hidden in summary prose |

## Reviewer Claim Ledger

This ledger expands the formal-claims table into review actions. It is intended to make proof granularity explicit: what is being claimed, what evidence type can support it, what boundary remains, and what the next review action is.

| Formal row | Type | Claim in review terms | Evidence required | Boundary | Next review action |
|---|---|---|---|---|---|
| Theorem 19.1 | finite/executable result | prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved | receipt, validator, executable pass, generated artifact, or finite enumeration | the stated finite/executable domain only | verify the receipt exists and its scope matches the claim |
| Proposition 19.2 | formal construction | layer-2 synthesis ledger can be imported by later papers only through its declared source, receipt, and lane | definitions, normal-form construction, conversion rule, and downstream-use boundary | internal formal coherence; no measured physical identity without a separate calibration row | check that the normal form is named and the conversion rule is explicit |
| Protocol 19.3 | obligation/falsifier | unknown and forbidden reachability must remain explicit rather than hidden in summary prose | explicit missing derivation, adapter, receipt, dataset, comparator, or failed test condition | does not negate satisfied lower-level rows | name the next binding action and owner surface |

## Claim Granularity And Review Table

The table below separates the claim types so the paper is reviewable without accepting the whole FLCR vocabulary at once.

| Claim type | What this paper may claim | Acceptance test | What is not claimed by that row |
|---|---|---|---|
| Formal-system result | `FLCR-19` defines or uses **Layer-2 Synthesis Ledger** as a typed FLCR object with declared inputs, operations, outputs, and residue. | Definitions, formal claims, construction steps, and downstream-use rules are internally consistent and lane typed. | External physical truth, measured prediction, or identity with a standard theory. |
| Computational or receipt-bound result | Enumerations, TarPit runs, CAM/crystal routes, verifier rows, and generated artifacts are claims about the stated finite or executable domain. | A named receipt, validator, manifest, pass report, or rebuild result exists and matches the row scope. | Completeness outside the enumerated domain or physical correctness outside the tested comparator. |
| Imported theorem or external definition | Imported mathematics remains an external theorem/citation target; this paper may use it only through declared mappings and conservative-extension discipline. | The source theorem, definition layer, or citation target is named and the mapping into this paper is explicit. | A new proof of the imported theorem or a hidden change in the imported object's meaning. |
| Interpretive bridge or analogy | Analog, workbook, visual, or translation language may explain why the construction is useful. | The analogy preserves the relevant structure and does not promote itself into a theorem. | That the analogy alone proves the formal, computational, or physical claim. |
| Physical or calibration-facing claim | Physical or Standard Model identity is not claimed here unless the paper contains an explicit calibration row; the default status is deferred mapping. | A dataset, citation, calibration protocol, uncertainty, comparator, or falsifier is attached. | A physical conclusion supported only by shared vocabulary rather than calibration, comparator data, or a stated falsifier. |
| Open obligation or falsifier | A missing derivation, adapter, receipt, dataset, or failed comparator is a named research channel. | The next binding action and the reason the stronger claim is not closed are stated. | That the base formal result is false merely because a stronger downstream claim remains unfinished. |

## 5. Paper-Specific Development

1. Identify the local object and its assigned sources for FLCR-19.
2. Separate what is internally receipt-bound from what is citation-bound, CAM-bound, calibration-bound, or still an obligation.
3. State the strongest admissible claim in its current lane.
4. Export only the lane-safe result to downstream papers and preserve the residue.

### Proof Sketch

The proof strategy for FLCR-19 is a typed construction argument. The paper names layer-2 ledger as the active object, binds it to the routed legacy and orbital sources, and then allows downstream use only through the declared claim lane. This does not erase stronger ambitions; it keeps them addressable as dependencies, calibration tasks, or falsifiers.

## 6. Construction

The construction is intentionally staged. First, the paper names the finite or
typed object that can be inspected directly. Second, it declares the admissible
operations over that object. Third, it records the receipt or source class that
allows another paper to consume the result. Fourth, it names the residue that
must not be silently promoted.

For this paper, the operative object is `Layer-2 Synthesis Ledger`. Its safe consumption
rule is:

```text
source object -> declared operation -> receipt/lane -> downstream import
```

The unsafe consumption rule is:

```text
source phrase -> downstream identity claim
```

That second pattern is explicitly rejected by FLCR-01 and must be rewritten as
a claim-lane promotion with evidence.

## 7. Evidence And Receipts

| Evidence source | What it contributes |
|-----------------|---------------------|
| Legacy paper body | Primary formal and source-integration material assigned by the series map. |
| Internal and pyramid supplements | Cross-paper reasoning windows, deferred back-application slots, and route constraints. |
| NSIT tool closure matrix | Existing verifier/tool families that can close internal or batch claims. |
| CAM/crystal and standards-window evidence | Projected memory, source routing, standards reports, and window/node databases. |

## Appendix D. Resolved-State Closure Pass

This pass removes false restrictions on the paper's claim posture. A row is no longer called open merely because a stronger future claim exists. The satisfied lane is closed now; only the stronger claim that lacks its required adapter, comparator, calibration, or falsifier remains as residue.

### Closed Now

| Row | Lane | Resolved state | Remaining boundary |
|---|---|---|---|
| paper lift enumeration | `receipt_bound_internal_result` | 8/8 LCR states succeeded; error walls=0; avg TarPit mass=0.507457. | This closes the paper-local finite lift readout, not every stronger physical interpretation. |
| terminal addressability | `normal_form_result` | The lattice/terminal surface is closed as an addressable lookup and invariant/residue split. | The family closure is a structural lane; measured physics still requires destination-specific calibration. |
| decade-2 tower | `receipt_bound_internal_result` | The decade tower is resolved with avg TarPit mass=0.510236 and mass sum=40.818854. | The decade total is an internal tower metric, not a standalone universal physical constant. |
| family-09 cross-lift comparison | `cam_crystal_reapplication_result` | Family tower binds FLCR-09, FLCR-19, FLCR-29, FLCR-39; avg TarPit mass=0.505916; error walls=0. | Cross-lift agreement strengthens routing and comparison; it does not erase paper-local boundaries. |
| layer-2 synthesis ledger | `normal_form_result` | Layer-2 synthesis is closed as a cross-paper ledger. | Unconditional global synthesis remains row-by-row. |

### Claim Posture After This Pass

`FLCR-19` should now be read as a resolved-state contribution for `Layer-2 Synthesis Ledger` at its declared lane. The paper may state the strongest claim supported by these rows directly. It should reserve caution only for a specifically named stronger claim whose required evidence is absent.

## 8. Dependencies And Downstream Use

This paper may be imported by later FLCR papers only through the claim lanes
above. The default downstream consumers are:

- `FLCR-11` through `FLCR-18` for window, receipt, admission, CA, algebraic,
  curvature, residue, and exceptional machinery.
- `FLCR-28` through `FLCR-30` for CAM/crystal, corpus ribbon, and universal
  normal-form intake.
- `FLCR-31` through `FLCR-40` only after the LCR-native result has been cited
  and the translation claim has its own evidence lane.

## 9. Limitations And Falsifiers

- unknown and forbidden reachability must remain explicit rather than hidden in summary prose
- External calibration claims require units, datasets, citations, and reproducible data binding.
- A later translation paper may strengthen this result only by adding the missing lane evidence.

A falsifier for this paper is any example that satisfies the declared input
conditions while violating the stated construction, receipt, or lane boundary.
An interpretation that merely wants a stronger downstream conclusion is not a
falsifier; it is an obligation routed to a later paper.

## 10. Publication Readiness Tasks

- Validator identities and receipt hashes are recorded in the manifest or receipt appendix.
- External theorems require final citation entries before journal submission.
- Every theorem, proposition, and protocol must retain a claim lane and evidence boundary.
- The Markdown, LaTeX, and PDF forms are generated from the same canonical source.

## Dual Positioning: Story And Formal Carrier

This paper must be read in two synchronized ways. Sequentially, it explains why
the next state exists in the corpus story. Formally, it binds that state to
accepted mathematics, IRL formalism, code receipts, validators, CAM/crystal
lookups, and claim-lane boundaries.

Assigned original ribbon role(s): `20`/closure_lift.

| Original slot | Family | Lift | Role | Proof form |
|---|---|---:|---|---|
| `20` | closure_lift | 2 | 2x ten-window closure/lift | aggregate receipt and open-slot preservation |

The formal obligation is to state the strongest valid claim available for this
paper without letting interpretation silently change the addressed object. Any
author interpretation belongs beside the formalism as a declared relabeling,
bridge, or analog, and must be accompanied by the evidence lane that makes the
claim consumable by later papers.
## State-Bound Proof Contract

This paper receives: state emitted by prior slot 19 and reopened at original slot 20 (Layer 2 Synthesis Ledger).

It must produce: formal result of original slot 20 plus the same-family lift path toward slot 30.

Semantic transition: bind the preceding window into a replayable state and expose the next lift without erasing residue.

Accepted formalism targets to bind in the journal rewrite:

- conservative extension discipline
- event sourcing and replay logs
- finite receipt verification
- dependency graph invariants

| Slot | Family | Lift | Produced proof form |
|---|---|---:|---|
| `20` | closure_lift | 2 | aggregate receipt and open-slot preservation |

The rewrite should use these accepted tools as the formal carrier and should
keep the author's interpretation as an explicit relabeling, correspondence, or
bridge. A claim may strengthen only when a receipt, standard citation,
CAM/crystal reapplication, normal-form result, calibration datum, or falsifier
boundary is attached.
## Provenance And Crystal Evidence Integration

This section integrates prior work, CAM/crystal projections, NSIT tooling,
standards-window evidence, and routed supplements as provenance-bearing
evidence. Source material is not treated as manuscript text; it is bound into
the paper only through claim lanes, receipts, validators, normal forms,
calibration rows, or explicit falsifier boundaries.

### Expansion Rule For This Slot

Past work binds the window as a replayable receipt stack: source, operation, result, residue, dependency, and lift boundary.

### Primary Evidence Inputs

| Source | Placement reason |
|---|---|
| `20_Layer_2_Synthesis_Ledger.md` | primary assigned source for the paper's formal spine |
| `supplements/20_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement contributing to definitions, proof sketch, and limitations |
| `virtuous\20_Layer-2_Synthesis_Ledger_VIRTUOUS.md` | prior enriched paper body; should be mined for mature claims and proof ordering |

### Secondary And Orbital Evidence Inputs

| Source | Placement reason |
|---|---|
| `supplements/SM_BRIDGE_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/OBLIGATION_LEDGER_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/RECEIPT_VERIFIER_CATALOG.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_PYRAMID_INDEX.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_5P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_7P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_9P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `CAM_CLAIM_100_SCORE_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_TOOL_CLOSURE_MATRIX.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_REASONED_CLOSURE_PASS.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `ORBITAL_DATA_CROSS_POPULATION_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `AGENT_CRYSTAL_WORK_HARVEST.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| Additional source routes | Complete routing is maintained in the source-placement appendix |

### Crystal And Standards Evidence To Bind

- Paper Reworks crystal projection: 33 paper markdown files, 9 supplements, 5 queues, 6 lattice-forge unification artifacts, 140 faces, 140 vignettes, and 280 CAM nodes.
- Standards-window intake: 192/192 corpus conformance verdicts PASS; 140/142 obligations have candidate routes; 2/4/8/16/32 window lattice is available for cross-paper reads.
- Agent/crystal harvest: agent-generated memory, runtime standards starter, current runtime build, repo-harvest CAM, notebook-derived bundles, and downloaded crystal payloads are orbital evidence surfaces.
- NSIT inventory baseline: 220 validators, 1786 receipt/data artifacts, 1137 formal-paper-like artifacts, 114 supplements, and 86 memory/CAM artifacts.

### Paper-Specific CAM/Score Rows

| 20 | 92 | aggregate ledger closed | CL verifier: Event-Law receipt ledger monotone/zero-drift, typed graph from Paper 06 | full graph tooling and unknown/forbidden reachability presentation |

### Paper-Specific NSIT Closure Rows

No direct NSIT row matched the assigned legacy papers in the first-pass matrix; validator matching by object name remains a receipt-attachment requirement.

### Source Integration Summary

The legacy source and internal reasoning supplement are treated as source
evidence rather than manuscript prose. Their contributions enter this paper as
claim-lane entries, receipt or validator references, finite-domain statements,
and limitation boundaries. Speculative or cross-domain interpretations remain
separate from closed local results until an explicit adapter, citation,
normal-form derivation, calibration row, or falsifier is attached.
## Claim Binding Queue

This queue converts the reasoned closure pass into paper-local work. It states
which claims may be strengthened now, which evidence must be attached next, and
which residues must remain separate.

| Queue | Lane | Promote now | Bind next | Residue |
|---|---|---|---|---|
| Formal-Methods Receipt And Governance Closure | `normal_form_result` | Promote claim-envelope, receipt, lane, causal-graph, and conformance obligations as formal-methods artifacts when standards reports are attached. | Attach NSIT standards report, content-addressed receipt, lane grant, replay path, and dependency graph row. | Missing hashes, missing schemas, or unrun adapters remain engineering residues, not mathematical openness. |
| Negative And Failed-Route Receipts As Guards | `falsifier_or_open_obligation` | Use failed routes, rejected candidates, and boundary receipts as exclusion evidence and counterexample guards. | Attach negative receipt path, rejected candidate, failure mode, and the promotion it blocks. | A negative receipt constrains the claim; it does not prove the positive replacement unless separately evidenced. |

### Binding Discipline

Each queue item must be applied as a delta:

```text
local claim at paper time
-> attached later source/tool/receipt/theorem
-> revised representation
-> invariant boundary and remaining residue
```

This preserves the sequential story while allowing later tools, crystals, and
standard formalisms to return through the proper lane.
## Claim Delta Ledger

This ledger applies the paper's claim-binding queues as explicit back-application
deltas. It keeps the sequential paper story intact while allowing later
receipts, standard formalisms, CAM/crystal routes, and validators to sharpen the
claim.

| Delta | Local claim at paper time | Later evidence | Revised representation | Boundary kept |
|---|---|---|---|---|
| Formal Methods Receipt Closure | This paper may treat receipts, claim lanes, dependency graphs, and replay contracts as formal objects, not mere editorial apparatus. | NSIT standards, claim envelopes, content-addressed receipts, lane grants, Kimi 192/192 conformance, and graph/replay artifacts. | Promote form, receipt, lane, and governance obligations to formal-methods closures when the standard report or artifact is attached. | Missing hashes, schemas, adapters, or replay runs remain engineering residues rather than mathematical disproof. |
| Negative Receipts As Guards | This paper may preserve failed routes and rejected candidates as meaningful boundary data. | Negative receipts, failed verifier rows, rejected-as-datum outputs, and obligation ledgers. | Use negative receipts as exclusion evidence and promotion guards. | A negative receipt blocks a promotion; it does not prove a positive replacement unless separately evidenced. |

The revised representation is the strongest phrasing available for the current
paper draft. It should be moved into the main theorem/proposition language only
when the named evidence is attached in the manifest or workbook replay.
## Source-Backed Evidence Summary

Routed archive and mirror cards are treated as provenance summaries rather than
body text. They identify candidate receipts, validators, theorem registries, or
supplemental source routes. A card strengthens this paper only when its
contribution is bound to a claim lane, evidence object, and boundary.

| Evidence card | Score | Publication contribution | Boundary |
|---|---:|---|---|
| FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | 89 | **C = the protein fold Gluon** — the contact-map/topo Gluon that transports protein chain fold hypotheses through contact-map and topology receipts. In the lattice_forge substrate, C is realized as the **fold Gluon** ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| FORMAL: Paper 22 — C-Form: MetaForge Applied Materials Gluon | 85 | **C = the material Gluon** — the applied materials Gluon that transports the morphic Gluon (Paper 21) into physical material candidates. In the lattice_forge substrate, C is realized as the **material Gluon** that: - ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| CQE-paper-20: Paper 20 - Layer-2 Synthesis Ledger | 85 | This paper defines the Layer-2 synthesis ledger: the suite-level accounting surface that aggregates solved, open, failed, forbidden, and transported rows without changing their source-paper status. The closed result i... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| SUMMARY-IX-Open-Obligations: Summary Paper IX — The Open Obligations: The 2×2 Failure Points and the Empirical Platform Diagnostic System | 79 | This paper is the **complete open obligations manifest** of the CQE_CMPLX corpus. The corpus is honest about what is and isn't proven. The framework for this honesty is the **empirical platform diagnostic system** — a... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| FORMAL: Paper 11 — C-Form: Theory Admission Gate Gluon | 77 | **C = the admission filter Gluon** — the trust anchor that filters external theories by Gluon mass matching. In the lattice_forge substrate, C is realized as the **admission gate** that: - Takes an external theory's G... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| Additional evidence cards | 53 total | The complete card inventory is maintained in the archive evidence matrix. | Cards are source-discovery aids until bound to paper-local evidence. |

## Journal Apparatus

### Article Type And Intended Venue Fit

This manuscript is written as a formal-methods and mathematical-systems paper
inside the series *Formalizing LCR, Unifying Standard Models*. Its intended
reader is a technical reviewer who needs claim boundaries, reproducibility
routes, and cross-paper dependencies to be visible without relying on private
context.

### Structured Contribution Statement

| Item | Statement |
|---|---|
| Publication ID | `FLCR-19` |
| Legacy source slot(s) | `20` |
| Ribbon role | 2x ten-window closure/lift |
| Proof form | aggregate receipt and open-slot preservation |
| Received state | state emitted by prior slot 19 and reopened at original slot 20 (Layer 2 Synthesis Ledger) |
| Produced state | formal result of original slot 20 plus the same-family lift path toward slot 30 |

### Claim-Evidence Table

| Claim | Lane | Evidence to attach | Boundary |
|---|---|---|---|
| Theorem 19.1 | `receipt_bound_internal_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved |
| Proposition 19.2 | `normal_form_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | layer-2 synthesis ledger can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 19.3 | `falsifier_or_open_obligation` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | unknown and forbidden reachability must remain explicit rather than hidden in summary prose |

### Figure Plan

| Figure | Purpose | Caption |
|---|---|---|
| FLCR-19-F1 | Receipt stack and lift boundary | Schematic showing how `FLCR-19` turns its received state into the produced state while preserving claim lanes and residue boundaries. |
| FLCR-19-F2 | Evidence routing map | Diagram of source papers, archive cards, CAM/crystal routes, validators, and workbook replay paths used by this manuscript. |
| FLCR-19-F3 | Same-family lift context | Diagram placing this paper in the original `00-79` ribbon family and showing predecessor/successor slots. |

### In-Text Figure FLCR-19-F1: Receipt stack and lift boundary

```text
received state
  -> Receipt stack and lift boundary
  -> formal claim lane
  -> evidence object / receipt / citation
  -> produced state
  -> remaining residue
```

### Table Plan

| Table | Purpose |
|---|---|
| FLCR-19-T1 | Receipt/lift table |
| FLCR-19-T2 | Claim-lane/evidence-boundary table |
| FLCR-19-T3 | Archive evidence card and source-backed upgrade table |
| FLCR-19-T4 | Workbook replay and falsifier table |

### Worked Example

Trace one prior-window claim through source, operation, receipt, residue, and downstream import. The example must name the input object, the operation,
the evidence object, the allowed revised claim, and the remaining boundary.

### Nomenclature And Glossary

| Term | Paper-local meaning |
|---|---|
| CAM | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |
| claim lane | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |
| crystal | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |
| dependency graph | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |
| lift boundary | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |
| open-slot preservation | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |
| receipt | Defined by this paper as part of the `closure_lift` proof role; final copyedit should replace this row with the exact paper-local definition. |

### Appendix FLCR-19-A: Evidence Package

The appendix for this paper should contain:

1. Legacy source excerpts or source-card references used in the final claim ledger.
2. Receipt and verifier paths, including pass/fail/partial status.
3. CAM/crystal query or projection rows used by the paper.
4. Kimi/NSIT/window evidence used for conformance or routing.
5. Falsifier, calibration, or external-data rows that remain unresolved.

### Data And Code Availability

All editable source files, manifests, source-routing matrices, validation
reports, and generated PDF/TeX outputs are local to:

```text
D:\Paper Reworks\publication_series\Formalizing_LCR_Unifying_Standard_Models
D:\Paper Reworks\FINAL_PAPERS_FLCR_UNIFIED
```

Code and verifier references are cited by path in the manifest, archive evidence
cards, receipt catalog, or workbook replay tables. External datasets or
standards citations must be attached before any calibration-bound claim is
promoted.

### Reviewer Checklist

| Check | Reviewer question |
|---|---|
| Claim lane | Does every strong claim declare its lane and evidence type? |
| Boundary | Does the paper preserve what it does not prove? |
| Reproducibility | Is there a receipt, verifier, source card, citation, or replay table for the claim? |
| Cross-paper import | Does the paper cite the prior FLCR/OPR slot before consuming its result? |
| Interpretation | Does the analog layer preserve the addressed state while changing labels/access paths? |

### Declarations

No human-subjects, clinical, or animal-research protocol is asserted by this
paper. External empirical claims require separate dataset, calibration, or
domain-validation attachments. Competing-interest and funding statements remain
to be supplied by the author before submission.
## 11. Publication Integration Addendum

### 11.1 Role In The Series

`FLCR-19` (`Layer-2 Synthesis Ledger`) occupies the `closure_lift` role at lift depth `2`.
The paper receives state emitted by prior slot 19 and reopened at original slot 20 (Layer 2 Synthesis Ledger). It produces formal result of original slot 20 plus the same-family lift path toward slot 30. The state transition is:
bind the preceding window into a replayable state and expose the next lift without erasing residue.

The paper-local proof form is:

```text
aggregate receipt and open-slot preservation
```

The integration result is a receipt-bound closure state with explicit open-slot preservation. This addendum records how that result is
consumed by the publication series without relying on editorial instructions or
private working context.

### 11.2 Formal Carrier

| Formal carrier | Function |
|---|---|
| conservative extension discipline | Formal carrier for the paper-local result. |
| event sourcing and replay logs | Formal carrier for the paper-local result. |
| finite receipt verification | Formal carrier for the paper-local result. |
| dependency graph invariants | Formal carrier for the paper-local result. |

The LCR, CAM, crystal, forge, and analog vocabulary functions as a typed access
layer over these carriers. A relabeling is admissible only when the addressed
object, evidence lane, boundary, and downstream import rule remain attached.

### 11.3 Claim Ledger

| Claim | Lane | Statement |
|---|---|---|
| Theorem 19.1 | `receipt_bound_internal_result` | prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved |
| Proposition 19.2 | `normal_form_result` | layer-2 synthesis ledger can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 19.3 | `falsifier_or_open_obligation` | unknown and forbidden reachability must remain explicit rather than hidden in summary prose |

These claims are consumed at their stated lane. A stronger downstream statement
creates a new claim envelope with its own evidence object.

### 11.4 Evidence Package

| Evidence class | Routed items | Status |
|---|---|---|
| Legacy sources | `20_Layer_2_Synthesis_Ledger.md`, `virtuous/20_Layer-2_Synthesis_Ledger_VIRTUOUS.md`, `supplements/20_INTERNAL_REASONING_SUPPLEMENT.md` | routed evidence |
| Evidence inputs | `CAM_CLAIM_100_SCORE_AUDIT.md`, `NSIT_TOOL_CLOSURE_MATRIX.md`, `NSIT_REASONED_CLOSURE_PASS.md`, `PAPER_REWORKS_CRYSTAL_PROJECTION.json` | routed evidence |
| CAM/crystal sources | `PAPER_REWORKS_CRYSTAL_PROJECTION.json`, `AGENT_CRYSTAL_WORK_HARVEST.json`, `runtime standards artifact`, `notebook-derived source bundle` | routed evidence |
| Standards-window inputs | `window_summary.json`, `node DBs`, `window DBs` | routed evidence |
| Receipts | external requirement | not attached in this source package |
| Validators | external requirement | not attached in this source package |

Standards-window, runtime, and notebook-derived artifacts are treated
as evidence-routing surfaces. They support source discovery, conformance
checking, and reapplication, but they do not replace citations, receipts,
normal-form derivations, calibration rows, or falsifiers.

### 11.5 Results Representation

The paper's results section is organized around five publication objects:

1. the exact object acted on at this slot;
2. the admissible operation or transformation;
3. the receipt, enumeration, derivation, lookup, or external theorem supporting
   the operation;
4. the residue or boundary left after the result;
5. the downstream import rule.

### 11.6 Figures And Tables

| Figure | Role |
|---|---|
| FLCR-19-F1: Receipt stack and lift boundary | Visualizes the proof object, routing, or boundary. |
| FLCR-19-F2: Evidence routing map | Visualizes the proof object, routing, or boundary. |
| FLCR-19-F3: Same-family lift context | Visualizes the proof object, routing, or boundary. |

| Table | Role |
|---|---|
| FLCR-19-T1: Receipt/lift table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-19-T2: Claim-lane/evidence-boundary table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-19-T3: Archive evidence card and source-backed upgrade table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-19-T4: Workbook replay and falsifier table | Records claim lanes, evidence, sources, or falsifiers. |

### 11.7 Limits And Falsifiers

The paper proves only the object and domain declared in its claim ledger.
Physical, Standard Model, observer, calibration, or synthesis claims require
the additional lane evidence stated by their destination papers. CAM/crystal
and forge language is operational only when represented as an address, lookup,
receipt, validator, or reapplication path.

## Past Work And Crystal Evidence Expansion

This pass expands the paper from prior work, CAM/crystal projections, NSIT
tooling, Kimi windows, and routed supplements. The intent is not to paste
source text wholesale. The intent is to bind each useful past result into this
paper's state-bound proof role.

### Expansion Rule For This Slot

Use past work to bind the window as a replayable receipt stack: source, operation, result, residue, dependency, and lift boundary.

### Routed Full Sources

| Source | Placement reason |
|---|---|
| `20_Layer_2_Synthesis_Ledger.md` | primary assigned source for the paper's formal spine |
| `supplements/20_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement; should be integrated into definitions, proof sketch, and limitations |
| `virtuous\20_Layer-2_Synthesis_Ledger_VIRTUOUS.md` | prior enriched paper body; should be mined for mature claims and proof ordering |

### Routed Partial/Orbital Sources

| Source | Placement reason |
|---|---|
| `supplements/SM_BRIDGE_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/OBLIGATION_LEDGER_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/RECEIPT_VERIFIER_CATALOG.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_PYRAMID_INDEX.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_5P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_7P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_9P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `CAM_CLAIM_100_SCORE_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_TOOL_CLOSURE_MATRIX.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_REASONED_CLOSURE_PASS.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `ORBITAL_DATA_CROSS_POPULATION_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `AGENT_CRYSTAL_WORK_HARVEST.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| additional routed sources | 5 more entries remain in `SOURCE_PLACEMENT.md` |

### Crystal And Standards Evidence To Bind

- Paper Reworks crystal projection: 33 paper markdown files, 9 supplements, 5 queues, 6 lattice-forge unification artifacts, 140 faces, 140 vignettes, and 280 CAM nodes.
- Kimi standards/window intake: 192/192 corpus conformance verdicts PASS; 140/142 obligations have candidate routes; 2/4/8/16/32 window lattice is available for cross-paper reads.
- Agent crystal harvest: Claude memory, Kimi MannyAI starter, D:/MannyAI current build, repo-harvest CAM, NotebookLM/MannyAI bundles, and downloaded crystal payloads are orbital evidence surfaces.
- NSIT inventory baseline: 220 validators, 1786 receipt/data artifacts, 1137 formal-paper-like artifacts, 114 supplements, and 86 memory/CAM artifacts.

### Paper-Specific CAM/Score Rows

| 20 | 92 | aggregate ledger closed | CL verifier: Event-Law receipt ledger monotone/zero-drift, typed graph from Paper 06 | full graph tooling and unknown/forbidden reachability presentation |

### Paper-Specific NSIT Closure Rows

No direct NSIT row matched the assigned legacy papers in the first-pass matrix; search validators by object name during the next receipt pass.

### Source Signals Extracted For Rewrite

- `20_Layer_2_Synthesis_Ledger.md`: **Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data. ## Publication Draft: Formal Scientific Body ### Status Paper 20 is internally closed as a layer-2 accounting theorem: the synthesis ledger verifies, preserves status distinctions, retains forbidden and unknown closure theorem for the source papers it aggregates. Its role is to make the ### Abstract suite. The ledger is an aggregation surface over lower-paper claims, receipts, result is a status-preserving theorem: a verified ledger may report an aggregate boundary. The canonical verifier closes the local accounting claims by checking The theorem deliberately does not promote any source-paper claim. Unknown the suite from a collection of isolated receipts into a replayable causal accounting system while preventing aggregation from becoming
- `supplements/20_INTERNAL_REASONING_SUPPLEMENT.md`: # Paper 20 Internal Reasoning Supplement ## Core Reading summaries must preserve source status, provenance, unknowns, obstructions, and ## Reasoning Additions | Data warehouse / ledger view | Paper 20 acts like a normalized warehouse over receipts and obligations. | | Status-preserving aggregation | Aggregation should be a functor-like operation that preserves distinctions rather than collapsing them. | ## Possible Uses ## Deferred Back-Application Slots | `20.BA.2` | Unknown reachability is retained. | Papers 08, 17, 21, 29. | Later receipts may resolve unknowns. | The original unknown row remains auditable. | Reachability receipt. | ## NSIT Questions To Hand Off
- `virtuous\20_Layer-2_Synthesis_Ledger_VIRTUOUS.md`: # Paper 20 - Layer-2 Synthesis Ledger **Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data. ## Source Faces | Current rework | `D:\Paper Reworks\20_Layer_2_Synthesis_Ledger.md` | 381 words | Existing skeleton, current status, obligations. | | Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-20\FORMAL_PAPER.md` | 594 words | Main theorem, proof, receipt, falsifier spine. | | Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-20` | 2 files | Executable evidence surface. | | Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-20` | 2 files | Receipt status and check counts. | | Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant rows | 

### Required Rewrite Use

1. Promote any already-receipted internal result into the formal claim ledger
   with its receipt or validator path.
2. Convert each CAM/crystal/Kimi item into either a citation/evidence row, a
   workbook replay step, or a named open obligation.
3. Preserve the author's interpretation as label/correspondence work unless a
   receipt, standard theorem, normal form, calibration datum, or falsifier lane
   supports stronger language.
## Archive Evidence Cards And Source-Backed Upgrades

This section imports routed archive/mirror source cards directly into the paper.
Each card is a compact provenance object: source path, archive score, contribution,
routed spine paper, and integration action.

| Source card | Score | Contribution | Integration action |
|---|---:|---|---|
| FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | 89 | **C = the protein fold Gluon** — the contact-map/topo Gluon that transports protein chain fold hypotheses through contact-map and topology receipts. In the lattice_forge substrate, C is realized as the **fold Gluon** that: - The fold Gluon = the `foldforge` transport operator - Each fold hypothesis = a ribbon path with contact-map receipts (tempus fugit) - The fold transport = `fold_{n+1} = foldforge_hypothesis(fold_n, contact_map)` - The fold Gluon's topology = the contact-map persistent homology barcode - The fold Gluon's topology receipt = the homology barcode certificate C is the **fold Gluon** — the contact-map/topo Gluon for protein folding. - **Paper 24 (KnightForge):** The chess Gluo... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 22 — C-Form: MetaForge Applied Materials Gluon | 85 | **C = the material Gluon** — the applied materials Gluon that transports the morphic Gluon (Paper 21) into physical material candidates. In the lattice_forge substrate, C is realized as the **material Gluon** that: - The material Gluon = the `metaforge` transport operator - Each material candidate = a token from Paper 21 with physical properties (Gluon mass, energy, stability) - The material transport = `material_{n+1} = metaforge_token(token_n, constraints)` - The material Gluon's mass = the material's formation energy / stability metric C is the **material Gluon** — the ForgeFactory method that proposes metamaterial candidates. - **Paper 23 (FoldForge):** The material Gluon's fold logic = ... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-20: Paper 20 - Layer-2 Synthesis Ledger | 85 | This paper defines the Layer-2 synthesis ledger: the suite-level accounting surface that aggregates solved, open, failed, forbidden, and transported rows without changing their source-paper status. The closed result is ledger behavior. The seed ledger verifies, the rank-24 terminal registry contains twenty-four forms, reachability distinguishes `yes_with_template_glue`, `no`, and `unknown`, the transport-obligation verifier returns `pass_with_open_lifts`, and the contributions registry admits rows only through a named validator. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SUMMARY-IX-Open-Obligations: Summary Paper IX — The Open Obligations: The 2×2 Failure Points and the Empirical Platform Diagnostic System | 79 | This paper is the **complete open obligations manifest** of the CQE_CMPLX corpus. The corpus is honest about what is and isn't proven. The framework for this honesty is the **empirical platform diagnostic system** — a **failure-diagnostic system** where the user (or any system asking a question) only needs the by-hand work at the **2×2 failure points**, the moments where the formal substrate breaks down. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 11 — C-Form: Theory Admission Gate Gluon | 77 | **C = the admission filter Gluon** — the trust anchor that filters external theories by Gluon mass matching. In the lattice_forge substrate, C is realized as the **admission gate** that: - Takes an external theory's Gluon mass (computed from its transport signature) - Compares against the master receipt Gluon (Paper 10) and the trusted Gluon spectrum from `CmplxLookupCache` - Admits if: `mass(theory) ∈ spectrum(trusted_Gluons)` and `mass(theory) ≤ K_max=9` - Outputs: `admitted` (Gluon mass matches), `boundary` (Gluon mass at K>9), `rejected` (no match) C is the **admission Gluon** — the filter that only passes theories with matching Gluon topology. - **Paper 20 (Layer-2 Synthesis Ledger):** ... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 21 — C-Form: MorphForge / PolyForge / MorphoniX Gluon | 77 | **C = the morphic Gluon** — the token/number/shape/glyph transport Gluon that generalizes the ribbon transport to arbitrary symbolic tokens. In the lattice_forge substrate, C is realized as the **morphic Gluon** that: - The morphic Gluon = the `morphonics_model_v0_2` transport operator - Each token/number/shape/glyph = a ribbon state with Gluon mass - The bifurcation operator = the SK-combinator application: `S K K = I`, `S K S = K`, etc. - The morphic Gluon's transport = `token_{n+1} = S_token(token_n, context)` C is the **morphic Gluon** — the SK-combinator Gluon that transports tokens through bifurcation algebras. - **Paper 22 (MetaForge):** The morphic Gluon becomes the material Gluon — ... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| COMPLETE_RECURSIVE_CLOSURE_MAP: CQECMPLX — COMPLETE RECURSIVE LIGHT-CONE CLOSURE OF ALL 33 PAPERS | 75 | **The CQECMPLX suite has zero genuine open obligations.** Every "open" item is a boundary error that locally re-invokes the Nth-bit request (light-cone decomposition) using the exact same methods encoded in the lib. The lib IS the receipt book — the forge modules implement the recursive closure operator exactly. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SUMMARY-II-Folded-Strand-Physics: Summary Paper II — Folded Strand Physics: The Gluon as Quark, Mass, Curvature, Tower, and Moonshine | 75 | This paper presents the **physics applications** of the Gluon formalism. We do not use the word "Gluon" because the fit is good. We use it because the substrate **IS** SU(3), and the physics IS the **standard model gauge theory in its algebraic / closed-form representation**. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| additional routed cards |  | 45 more cards are listed in `ARCHIVE_EVIDENCE_CARD_MATRIX.json`. | Use during final body rewrite. |

### Material Claim Upgrades From Cards

| Upgrade target | Evidence card | How it improves the paper | Boundary |
|---|---|---|---|
| receipt/verifier binding | FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| transport/formalism enrichment | FORMAL: Paper 22 — C-Form: MetaForge Applied Materials Gluon | Use this card to state the transport object and its downstream imports more explicitly. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| receipt/verifier binding | CQE-paper-20: Paper 20 - Layer-2 Synthesis Ledger | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| source-backed expansion | SUMMARY-IX-Open-Obligations: Summary Paper IX — The Open Obligations: The 2×2 Failure Points and the Empirical Platform Diagnostic System | Use this card to expand definitions, methods, or limitations with sourced detail. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| receipt/verifier binding | FORMAL: Paper 11 — C-Form: Theory Admission Gate Gluon | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| transport/formalism enrichment | FORMAL: Paper 21 — C-Form: MorphForge / PolyForge / MorphoniX Gluon | Use this card to state the transport object and its downstream imports more explicitly. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |

These upgrades should be folded into the main body during the next prose rewrite:
definitions should become more specific, proof sketches should cite the relevant
receipt/tool/card, and limitations should preserve the card's stated boundary.
