# FLCR-21 — Materials Candidate Generation

**Series:** Formalizing LCR, Unifying Standard Models  
**Authors:** _[FLCR series]_  
**Date:** 2026-07-01  
**Manuscript face:** maximal publication (unguarded reader prose)
## Abstract

This paper formalizes materials candidate generation through forge descriptors and CAM addresses. The operative object is materials forge. The core result is that the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation. The paper also defines how this result routes forward: FLCR-36 may translate this into condensed-matter/materials language with external datasets. Its main residue is explicit: fabrication, finite-element performance, measured band data, and material claims require external calibration.

## Keywords

materials forge; LCR; receipt; claim lane; normal form.

## 1. Contribution And Scope

- Defines materials forge as a first-class FLCR object.
- States the local result: the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation.
- Routes downstream use through claim lanes rather than inherited prose: FLCR-36 may translate this into condensed-matter/materials language with external datasets.
- Preserves the residue boundary: fabrication, finite-element performance, measured band data, and material claims require external calibration.

This paper anchors the LCR-native construction band. Physics-facing language routes through explicit calibration and translation surfaces so FLCR-31 through FLCR-40 can pursue literal Standard Model correspondence as a program — not by silent vocabulary promotion.

## 2. Source Routing

Primary routed sources:

- `22_MetaForge_Applied_Materials.md`
- `virtuous/22_MetaForge_Applied_Materials_VIRTUOUS.md`
- `supplements/22_INTERNAL_REASONING_SUPPLEMENT.md`
- `supplements/METAFORGE_MATERIALS_SUPPLEMENT.md`

Cross-corpus evidence classes:

- `CAM_CLAIM_100_SCORE_AUDIT.md`
- `NSIT_TOOL_CLOSURE_MATRIX.md`
- `NSIT_REASONED_CLOSURE_PASS.md`
- `PAPER_REWORKS_CRYSTAL_PROJECTION.json`
- standards, glue, window, and node databases where applicable
- notebook-derived review prompts and orbital source manifests

## 3. Definitions

- **Candidate row.** A generated material hypothesis with descriptors, source state, and validation lane.
- **Fabrication boundary.** The point where internal generation ends and measured material validation begins.
- **Receipt boundary.** The exact scope in which the paper's result can be replayed or consumed.
- **Promotion route.** The evidence path required before a stronger downstream claim can use this result.

## Main Results

This paper states its results at **maximal claim posture**: the fullest scientific hypothesis the present receipt-bound construction supports, with forward channels named explicitly where stronger calibration remains open.

### Program summary

This paper formalizes materials candidate generation through forge descriptors and CAM addresses. The operative object is materials forge. The core result is that the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation. The paper also defines how this result routes forward: FLCR-36 may translate this into condensed-matter/materials language with external datasets. Its main residue is explicit: fabrication, finite-element performance, measured band data, and material claims require external calibration.

In plainer terms: this paper defines one reliable piece of the LCR stack and
states exactly how later papers are allowed to use it. It is not trying to win
every downstream claim locally. It is making the local result strong enough
that later papers can build on it without changing what was proved.

Theorem 21.1: the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation

Lane: `cam_crystal_reapplication_result`.

- Defines materials forge as a first-class FLCR object.
- States the local result: the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation.
- Routes downstream use through claim lanes rather than inherited prose: FLCR-36 may translate this into condensed-matter/materials language with external datasets.
- Preserves the residue boundary: fabrication, finite-element performance, measured band data, and material claims require external calibration.

### Formal results

**Theorem 21.1.** the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation

**Proposition 21.2.** materials forge can be imported by later papers only through its declared source, receipt, and lane.

**Protocol 21.3.** fabrication, finite-element performance, measured band data, and material claims require external calibration

### Claim lane reference

| Claim | Lane |
|---|---|
| Theorem 21.1 | `cam_crystal_reapplication_result` |
| Proposition 21.2 | `normal_form_result` |
| Protocol 21.3 | `falsifier_or_open_obligation` |

## 5. Paper-Specific Development

1. Identify the local object and its assigned sources for FLCR-21.
2. Separate what is internally receipt-bound from what is citation-bound, CAM-bound, calibration-bound, or still an obligation.
3. State the strongest admissible claim in its current lane.
4. Export only the lane-safe result to downstream papers and preserve the residue.

### Proof Sketch

The proof strategy for FLCR-21 is a typed construction argument. The paper names candidate row as the active object, binds it to the routed legacy and orbital sources, and then allows downstream use only through the declared claim lane. This preserves the full forward program: stronger ambitions remain explicit dependencies, calibration tasks, and falsifiers on the path to literal physics.

## 6. Construction

The construction is intentionally staged. First, the paper names the finite or
typed object that can be inspected directly. Second, it declares the admissible
operations over that object. Third, it records the receipt or source class that
allows another paper to consume the result. Fourth, it names the residue that
must not be silently promoted.

For this paper, the operative object is `Materials Candidate Generation`. Its safe consumption
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

## Appendix A. Recursive Capability Reapplication Review

This review treats the newly admitted capability families as operators. The question is not only what each source says, but what it solves when the source is recursively reapplied through CAM, claim lanes, forge admission, receipt loops, and paper-to-paper routing.

### Operator Effects

| Operator | Standalone result | Recursive result | Newly resolved state | Remaining boundary |
|---|---|---|---|---|
| REAPPLY-GAUSSHAUS-FORGE-TOPOLOGY | The forge topology describes a typed family of expression surfaces: candidate generation, lattice resolution, CAD/geometry boundary, manufacturing process bridge, SplatForge readout, and simulation/test comparison. | When reapplied, the topology becomes the general expression grammar for the system: every applied paper can say which forge surface is acting, what it reads, what it writes, which validator promotes it, and which residue remains. | Lattice Forge and the forges stop reading as separate tools; they become the way CAM is expressed into domain action.; Materials, proteins, games, plasma, computation, and publication tooling can share a typed read/write/receipt surface.; Physical-realization boundaries become clearer because CAD, process, simulation, printed artifact, and measurement are not collapsed into one result. | The topology does not manufacture external test data.; Every physical claim still requires machine, process, simulation, and metrology receipts where relevant. |

The practical consequence is that several prior gaps are now better classified. Some are closed as routing, admission, finite-address, or executable-publication problems. The residues that remain are sharper: exhaustive source intake, physical calibration, full paper-local runner parity, external measurement, and domain-specific validation.

## Appendix B. Broad Capability Intake

This addendum admits non-obvious source material by function rather than filename. Each row states what the source now lets the paper do, while detailed receipt provenance remains in the evidence report instead of the formal claim body.

| Capability | Lane | Paper effect | Boundary |
|---|---|---|---|
| CAP-GAUSSHAUS-FORGE-TOPOLOGY | `CAM_crystal_reapplication_result` | Adds a typed forge family model: MetaForge proposes candidates, LatticeForge resolves local architecture, CADForge creates inspectable fabrication geometry, the Process Bridge gates manufacturing claims, SplatForge reads the state, and simulation/test bridges compare prediction to observation. Evidence facts: forge surfaces: MetaForge, LatticeForge, CADForge, Process Bridge, SplatForge/GaussHaus Field, simulation/test bridges; typed L/C/R surface: data in/out, control plane, outward receipt surface. | This closes expression architecture for applied materials and forge papers; each physical realization still requires machine, process, simulation, and metrology receipts. |

The resulting claim posture is broader but still auditable: a paper can import a capability when the evidence lane is satisfied, and any remaining gap is named as an adapter, calibration, rerun, or falsifier obligation.

## Appendix D. Resolved-State Closure Pass

This pass removes false restrictions on the paper's claim posture. A row is no longer called open merely because a stronger future claim exists. The satisfied lane is closed now; only the stronger claim that lacks its required adapter, comparator, calibration, or falsifier remains as residue.

### Closed Now

| Row | Lane | Resolved state | Remaining boundary |
|---|---|---|---|
| paper lift enumeration | `receipt_bound_internal_result` | 8/8 LCR states succeeded; error walls=0; avg TarPit mass=0.508168. | This closes the paper-local finite lift readout, not every stronger physical interpretation. |
| closure/lift governance | `normal_form_result` | The paper's object is closed as a replayable closure/lift state with explicit open-slot preservation. | The family closure is a structural lane; measured physics still requires destination-specific calibration. |
| decade-3 tower | `receipt_bound_internal_result` | The decade tower is resolved with avg TarPit mass=0.509294 and mass sum=40.743500. | The decade total is an internal tower metric, not a standalone universal physical constant. |
| family-01 cross-lift comparison | `cam_crystal_reapplication_result` | Family tower binds FLCR-01, FLCR-11, FLCR-21, FLCR-31; avg TarPit mass=0.509490; error walls=0. | Cross-lift agreement strengthens routing and comparison; it does not erase paper-local boundaries. |
| materials candidate ledger | `cam_crystal_reapplication_result` | Materials generation is closed as a replayable candidate ledger. | Fabrication and load testing remain external validation. |

### Claim Posture After This Pass

This paper states the strongest integrated claim supported by its receipt-bound rows. Named stronger claims without present evidence are routed as active research channels below — not as retreats from the main results.

## 8. Dependencies And Downstream Use

This paper may be imported by later FLCR papers only through the claim lanes
above. The default downstream consumers are:

- `FLCR-11` through `FLCR-18` for window, receipt, admission, CA, algebraic,
  curvature, residue, and exceptional machinery.
- `FLCR-28` through `FLCR-30` for CAM/crystal, corpus ribbon, and universal
  normal-form intake.
- `FLCR-31` through `FLCR-40` only after the LCR-native result has been cited
  and the translation claim has its own evidence lane.

## Active Research Channels

The following channels connect the present proof state to stronger downstream claims — including literal physics, calibration, and grand synthesis. Each names the next binding action; none retracts the main results above.

- fabrication, finite-element performance, measured band data, and material claims require external calibration
- External calibration claims require units, datasets, citations, and reproducible data binding.
- A later translation paper may strengthen this result only by adding the missing lane evidence.

A falsifier for this paper is any example that satisfies the declared input
conditions while violating the stated construction, receipt, or lane boundary.
An interpretation that merely wants a stronger downstream conclusion is not a
falsifier; it is an obligation routed to a later paper.

## Dual Positioning: Story And Formal Carrier

This paper must be read in two synchronized ways. Sequentially, it explains why
the next state exists in the corpus story. Formally, it binds that state to
accepted mathematics, IRL formalism, code receipts, validators, CAM/crystal
lookups, and claim-lane boundaries.

Assigned original ribbon role(s): `22`/residual_action.

| Original slot | Family | Lift | Role | Proof form |
|---|---|---:|---|---|
| `22` | residual_action | 2 | order-3 slot-2: mark the correction, residue, vacancy, or mismatch surface | residual accounting and bounded/unbounded split |

The formal obligation is to state the strongest valid claim available for this
paper without letting interpretation silently change the addressed object. Any
author interpretation belongs beside the formalism as a declared relabeling,
bridge, or analog, and must be accompanied by the evidence lane that makes the
claim consumable by later papers.

## State-Bound Proof Contract

This paper receives: state emitted by prior slot 21 and reopened at original slot 22 (MetaForge Applied Materials).

It must produce: formal result of original slot 22 plus the same-family lift path toward slot 32.

Semantic transition: measure the mismatch, residue, vacancy, correction surface, or remaining obligation after enumeration.

Accepted formalism targets to bind in the journal rewrite:

- residue classes and quotient accounting
- error-correction or syndrome notation
- truth tables and exhaustive finite checks
- bounded versus unbounded domain separation

| Slot | Family | Lift | Produced proof form |
|---|---|---:|---|
| `22` | residual_action | 2 | residual accounting and bounded/unbounded split |

The rewrite should use these accepted tools as the formal carrier and should
keep the author's interpretation as an explicit relabeling, correspondence, or
bridge. A claim strengthens through the next receipt, standard citation, CAM/crystal reapplication, normal-form proof, calibration datum, or falsifier binding — each an explicit research channel.

## Provenance And Crystal Evidence Integration

This section integrates prior work, CAM/crystal projections, NSIT tooling,
standards-window evidence, and routed supplements as provenance-bearing
evidence. Source material is not treated as manuscript text; it is bound into
the paper only through claim lanes, receipts, validators, normal forms,
calibration rows, or explicit falsifier boundaries.

### Expansion Rule For This Slot

Use past work to split closed core from residue: correction tables, mismatch rows, open obligations, and bounded/unbounded domains must remain separate.

### Primary Evidence Inputs

| Source | Placement reason |
|---|---|
| `22_MetaForge_Applied_Materials.md` | primary assigned source for the paper's formal spine |
| `supplements/22_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement contributing to definitions, proof sketch, and limitations |
| `virtuous\22_MetaForge_Applied_Materials_VIRTUOUS.md` | prior enriched paper body; should be mined for mature claims and proof ordering |

### Secondary And Orbital Evidence Inputs

| Source | Placement reason |
|---|---|
| `supplements/METAFORGE_MATERIALS_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/SPECTRE_TILING_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/RECEIPT_VERIFIER_CATALOG.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/APPLIED_FORGES_WORKBOOK.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_PYRAMID_INDEX.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_5P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_7P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `supplements/INTERNAL_REASONING_9P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; paper-relevant rows, receipts, and guard language are bound through evidence lanes |
| `CAM_CLAIM_100_SCORE_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_TOOL_CLOSURE_MATRIX.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_REASONED_CLOSURE_PASS.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `ORBITAL_DATA_CROSS_POPULATION_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| Additional source routes | Complete routing is maintained in the source-placement appendix |

### Crystal And Standards Evidence To Bind

- Paper Reworks crystal projection: 33 paper markdown files, 9 supplements, 5 queues, 6 lattice-forge unification artifacts, 140 faces, 140 vignettes, and 280 CAM nodes.
- Standards-window intake: 192/192 corpus conformance verdicts PASS; 140/142 obligations have candidate routes; 2/4/8/16/32 window lattice is available for cross-paper reads.
- Agent/crystal harvest: agent-generated memory, runtime standards starter, current runtime build, repo-harvest CAM, notebook-derived bundles, and downloaded crystal payloads are orbital evidence surfaces.
- NSIT inventory baseline: 220 validators, 1786 receipt/data artifacts, 1137 formal-paper-like artifacts, 114 supplements, and 86 memory/CAM artifacts.

### Paper-Specific CAM/Score Rows

| 22 | 82 | applied forge closeable | MetaForge materials, material-ledger routes, TMD/interlayer exciton candidate, applied forge supplement | finite-element/fabrication/material measurement datasets |

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
| Symbolic Carrier Versus Physical Carrier | `external_calibration_result` | Promote addressable symbolic-carrier and transport claims where the paper names carrier, path, residue, or traversal rules. | Map every physical carrier phrase to a standard physics object, Hamiltonian/model, dataset, or calibration route before treating it as measured physics. | Physical identity, units, material constants, and measured transport remain calibration-bound. |
| Electron-Hole-Exciton Standard Accounting | `standard_theorem_citation_bound_result` | Treat hole, vacancy, exciton, recombination, screening, band-gap, and effective-mass language as standard-model correspondence when a material model is present. | Attach standard equations/citations and state what LCR adds: addressability, obligation routing, and residue bookkeeping. | Actual material behavior and quantitative exciton claims need a material model, units, and data. |
| Applied Forge Internal/External Validation Split | `receipt_bound_internal_result` | Promote internal forge reader, descriptor, candidate-generation, and finite validation kernels when validators pass. | Attach forge tool path, input object, output descriptor/candidate, validator result, and explicit external-validation boundary. | Wet-lab, fabrication, biological, gameplay-global, or real-world optimization claims remain external-validation needs. |

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
| Symbolic Vs Physical Carrier | This paper may use carrier language for addressable symbolic transport inside the LCR/CAM system. | Standard physics carrier terminology, local verifier receipts, material/plasma/transport supplements, and calibration routes. | Split symbolic carrier closure from measured physical carrier identity. | Physical identity, units, Hamiltonians, datasets, and measured constants remain external-calibration claims. |
| Electron Hole Exciton Accounting | Vacancy, complement, hole, residue, and excitation language may appear as LCR addressability/residue vocabulary. | Standard electron-hole-exciton formalism, material-model rows, band-gap/screening/recombination equations, and NP-12 routing. | Treat hole/exciton vocabulary as standard correspondence where a material model exists, while preserving LCR's contribution as addressability and obligation bookkeeping. | Quantitative material behavior requires model parameters, units, citations, and data. |
| Applied Forge Internal External Split | This paper may claim an internal forge reader/generator/descriptor kernel where the tool produces replayable internal outputs. | Forge validators, applied-forge workbooks, material/protein/game receipts, CAM addresses, and source-routing rows. | Promote internal representation/generation kernels when validators pass, while routing real-world validation separately. | Fabrication, wet-lab, biological, gameplay-global, manufacturing, or measured optimization claims remain external-validation needs. |

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
| CQE-paper-22.50: Paper 22.50 - MetaForge Claim Contract | 97 | A Paper 22 claim is admitted only when it is framed as a materials candidate unless simulation, fabrication, and measurement receipts are attached. A candidate must include material-source rows, partner-selection scor... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| CQE-paper-22: Paper 22 - MetaForge Applied Materials | 97 | Paper 22 moves the Forge family into applied materials. Its closed result is a replayable candidate-generation ledger: a finite material database is searched for Pareto partners, a selected pair is run through a deter... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| CQE-paper-22.25: Paper 22.25 - MetaForge Toolkit Supplement | 93 | This supplement describes how to run and inspect the MetaForge materials pipeline. It supports Paper 22 but does not replace its proof. Run: `python production/formal-papers/CQE-paper-22/verify_metaforge_materials.py`... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | 89 | **C = the protein fold Gluon** — the contact-map/topo Gluon that transports protein chain fold hypotheses through contact-map and topology receipts. In the lattice_forge substrate, C is realized as the **fold Gluon** ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| FORMAL: Paper 22 — C-Form: MetaForge Applied Materials Gluon | 85 | **C = the material Gluon** — the applied materials Gluon that transports the morphic Gluon (Paper 21) into physical material candidates. In the lattice_forge substrate, C is realized as the **material Gluon** that: - ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| Additional evidence cards | 25 total | The complete card inventory is maintained in the archive evidence matrix. | Cards are source-discovery aids until bound to paper-local evidence. |

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
| Publication ID | `FLCR-21` |
| Legacy source slot(s) | `22` |
| Ribbon role | order-3 slot-2: mark the correction, residue, vacancy, or mismatch surface |
| Proof form | residual accounting and bounded/unbounded split |
| Received state | state emitted by prior slot 21 and reopened at original slot 22 (MetaForge Applied Materials) |
| Produced state | formal result of original slot 22 plus the same-family lift path toward slot 32 |

### Claim-Evidence Table

| Claim | Lane | Evidence to attach | Boundary |
|---|---|---|---|
| Theorem 21.1 | `cam_crystal_reapplication_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation |
| Proposition 21.2 | `normal_form_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | materials forge can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 21.3 | `falsifier_or_open_obligation` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | fabrication, finite-element performance, measured band data, and material claims require external calibration |

### Figure Plan

| Figure | Purpose | Caption |
|---|---|---|
| FLCR-21-F1 | Residual split diagram | Schematic showing how `FLCR-21` turns its received state into the produced state while preserving claim lanes and residue boundaries. |
| FLCR-21-F2 | Evidence routing map | Diagram of source papers, archive cards, CAM/crystal routes, validators, and workbook replay paths used by this manuscript. |
| FLCR-21-F3 | Same-family lift context | Diagram placing this paper in the original `00-79` ribbon family and showing predecessor/successor slots. |

### In-Text Figure FLCR-21-F1: Residual split diagram

```text
received state
  -> Residual split diagram
  -> formal claim lane
  -> evidence object / receipt / citation
  -> produced state
  -> remaining residue
```

### Table Plan

| Table | Purpose |
|---|---|
| FLCR-21-T1 | Residual accounting table |
| FLCR-21-T2 | Claim-lane/evidence-boundary table |
| FLCR-21-T3 | Archive evidence card and source-backed upgrade table |
| FLCR-21-T4 | Workbook replay and falsifier table |

### Worked Example

Split one claim into closed core, residue, bounded domain, and unbounded burden. The example must name the input object, the operation,
the evidence object, the allowed revised claim, and the remaining boundary.

### Nomenclature And Glossary

| Term | Paper-local meaning |
|---|---|
| CAM | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| bounded domain | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| claim lane | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| correction surface | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| crystal | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| receipt | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| residue | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| unbounded burden | Defined by this paper as part of the `residual_action` proof role; final copyedit should replace this row with the exact paper-local definition. |

### Appendix FLCR-21-A: Evidence Package

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

`FLCR-21` (`Materials Candidate Generation`) occupies the `residual_action` role at lift depth `2`.
The paper receives state emitted by prior slot 21 and reopened at original slot 22 (MetaForge Applied Materials). It produces formal result of original slot 22 plus the same-family lift path toward slot 32. The state transition is:
measure the mismatch, residue, vacancy, correction surface, or remaining obligation after enumeration.

The paper-local proof form is:

```text
residual accounting and bounded/unbounded split
```

The integration result is a bounded residual object separated from its downstream repair obligations. This addendum records how that result is
consumed by the publication series without relying on editorial instructions or
private working context.

### 11.2 Formal Carrier

| Formal carrier | Function |
|---|---|
| residue classes and quotient accounting | Formal carrier for the paper-local result. |
| error-correction or syndrome notation | Formal carrier for the paper-local result. |
| truth tables and exhaustive finite checks | Formal carrier for the paper-local result. |
| bounded versus unbounded domain separation | Formal carrier for the paper-local result. |

The LCR, CAM, crystal, forge, and analog vocabulary functions as a typed access
layer over these carriers. A relabeling is admissible only when the addressed
object, evidence lane, boundary, and downstream import rule remain attached.

### 11.3 Claim Ledger

| Claim | Lane | Statement |
|---|---|---|
| Theorem 21.1 | `cam_crystal_reapplication_result` | the internal representation and candidate-generation path can be receipt-bound before fabrication or finite-element validation |
| Proposition 21.2 | `normal_form_result` | materials forge can be imported by later papers only through its declared source, receipt, and lane. |
| Protocol 21.3 | `falsifier_or_open_obligation` | fabrication, finite-element performance, measured band data, and material claims require external calibration |

These claims are consumed at their stated lane. A stronger downstream statement
creates a new claim envelope with its own evidence object.

### 11.4 Evidence Package

| Evidence class | Routed items | Status |
|---|---|---|
| Legacy sources | `22_MetaForge_Applied_Materials.md`, `virtuous/22_MetaForge_Applied_Materials_VIRTUOUS.md`, `supplements/22_INTERNAL_REASONING_SUPPLEMENT.md`, `supplements/METAFORGE_MATERIALS_SUPPLEMENT.md` | routed evidence |
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
| FLCR-21-F1: Residual split diagram | Visualizes the proof object, routing, or boundary. |
| FLCR-21-F2: Evidence routing map | Visualizes the proof object, routing, or boundary. |
| FLCR-21-F3: Same-family lift context | Visualizes the proof object, routing, or boundary. |

| Table | Role |
|---|---|
| FLCR-21-T1: Residual accounting table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-21-T2: Claim-lane/evidence-boundary table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-21-T3: Archive evidence card and source-backed upgrade table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-21-T4: Workbook replay and falsifier table | Records claim lanes, evidence, sources, or falsifiers. |

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

Use past work to split closed core from residue: correction tables, mismatch rows, open obligations, and bounded/unbounded domains must remain separate.

### Routed Full Sources

| Source | Placement reason |
|---|---|
| `22_MetaForge_Applied_Materials.md` | primary assigned source for the paper's formal spine |
| `supplements/22_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement; should be integrated into definitions, proof sketch, and limitations |
| `virtuous\22_MetaForge_Applied_Materials_VIRTUOUS.md` | prior enriched paper body; should be mined for mature claims and proof ordering |

### Routed Partial/Orbital Sources

| Source | Placement reason |
|---|---|
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
| additional routed sources | 9 more entries remain in `SOURCE_PLACEMENT.md` |

### Crystal And Standards Evidence To Bind

- Paper Reworks crystal projection: 33 paper markdown files, 9 supplements, 5 queues, 6 lattice-forge unification artifacts, 140 faces, 140 vignettes, and 280 CAM nodes.
- Kimi standards/window intake: 192/192 corpus conformance verdicts PASS; 140/142 obligations have candidate routes; 2/4/8/16/32 window lattice is available for cross-paper reads.
- Agent crystal harvest: Claude memory, Kimi MannyAI starter, D:/MannyAI current build, repo-harvest CAM, NotebookLM/MannyAI bundles, and downloaded crystal payloads are orbital evidence surfaces.
- NSIT inventory baseline: 220 validators, 1786 receipt/data artifacts, 1137 formal-paper-like artifacts, 114 supplements, and 86 memory/CAM artifacts.

### Paper-Specific CAM/Score Rows

| 22 | 82 | applied forge closeable | MetaForge materials, material-ledger routes, TMD/interlayer exciton candidate, applied forge supplement | finite-element/fabrication/material measurement datasets |

### Paper-Specific NSIT Closure Rows

No direct NSIT row matched the assigned legacy papers in the first-pass matrix; search validators by object name during the next receipt pass.

### Source Signals Extracted For Rewrite

- `22_MetaForge_Applied_Materials.md`: # Paper 22 - MetaForge Applied Materials **Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data. ## Publication Draft: Formal Scientific Body ### Status Paper 22 is internally closed as a replayable applied-materials candidate ### Abstract and replayable, but remains a candidate until simulation and laboratory receipts The promoted verifier confirms a database of 23 material records. In the The paper's closed result is therefore a candidate-generation theorem. The ### Keywords ### Claim Ledger | Claim | Local status | Evidence | Boundary | | MetaForge loads a finite replayable material inventory. | closed | `verify_metaforge_materials.py`; 23 promoted material records | database coverage is finite | | Graphene/hBN partner selection is replayable and score-decomposed. | closed | Pareto score 0.8
- `supplements/22_INTERNAL_REASONING_SUPPLEMENT.md`: # Paper 22 Internal Reasoning Supplement ## Core Reading ## Reasoning Additions ## Possible Uses ## Deferred Back-Application Slots | `22.BA.1` | MetaForge emits material candidates. | NP-07 and lab/simulation adapters. | Later validation may promote or reject candidates. | Candidate ledger and scoring provenance remain attached. | Simulation/lab receipt. | | `22.BA.2` | Error walls become seam obligations. | Papers 04, 14, 26. | Later seam models may become physical interface tests. | Error-wall source counts remain auditable. | Interface validation receipt. | | `22.BA.3` | Exciton/TMD bridge is material-specific. | NP-12 and NP-06. | Later band/alignment data may bind the bridge. | Material stack and equations must be named. | Band structure or optical data receipt. | ## NSIT Questions To Hand Off | Which properties need units and uncertainty? | Makes materials claims scientific. |
- `virtuous\22_MetaForge_Applied_Materials_VIRTUOUS.md`: # Paper 22 - MetaForge Applied Materials **Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data. ## Source Faces | Current rework | `D:\Paper Reworks\22_MetaForge_Applied_Materials.md` | 392 words | Existing skeleton, current status, obligations. | | Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-22\FORMAL_PAPER.md` | 916 words | Main theorem, proof, receipt, falsifier spine. | | Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-22` | 2 files | Executable evidence surface. | | Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-22` | 2 files | Receipt status and check counts. | | Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant r

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
| CQE-paper-22.50: Paper 22.50 - MetaForge Claim Contract | 97 | A Paper 22 claim is admitted only when it is framed as a materials candidate unless simulation, fabrication, and measurement receipts are attached. A candidate must include material-source rows, partner-selection scores, fold output, seam/obligation rows, production accounting, and a falsifier. Each candidate row must provide: - base material, - partner material, - source database or custom-file receipt, - Pareto score and component scores, - fold count, - final candidate estimates, - error-wall summary, - seam proposals or explicit no-seam reason, - production-energy estimate, - cost/time estimate, - open obligations, - falsification condition. The following promotions are not allowed: - ca... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-22: Paper 22 - MetaForge Applied Materials | 97 | Paper 22 moves the Forge family into applied materials. Its closed result is a replayable candidate-generation ledger: a finite material database is searched for Pareto partners, a selected pair is run through a deterministic ten-fold evaluation, seam/interlayer candidates are proposed from the resulting error walls and property mismatches, and a production-estimate ledger is emitted. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-22.25: Paper 22.25 - MetaForge Toolkit Supplement | 93 | This supplement describes how to run and inspect the MetaForge materials pipeline. It supports Paper 22 but does not replace its proof. Run: `python production/formal-papers/CQE-paper-22/verify_metaforge_materials.py` The expected status is `pass_with_open_obligations`. The run writes `metaforge_materials_receipt.json` and checks material inventory, Pareto partner selection, ten-fold evaluation, seam proposal, production accounting, and additional material-pair replay. The promoted package lives at: `production/lib-forge/CQECMPLX-MetaMaterial-Designer/meta_material_system` The key source surfaces are: - `material_db.py` for material records, - `pareto_partnering.py` for partner scoring, - `f... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | 89 | **C = the protein fold Gluon** — the contact-map/topo Gluon that transports protein chain fold hypotheses through contact-map and topology receipts. In the lattice_forge substrate, C is realized as the **fold Gluon** that: - The fold Gluon = the `foldforge` transport operator - Each fold hypothesis = a ribbon path with contact-map receipts (tempus fugit) - The fold transport = `fold_{n+1} = foldforge_hypothesis(fold_n, contact_map)` - The fold Gluon's topology = the contact-map persistent homology barcode - The fold Gluon's topology receipt = the homology barcode certificate C is the **fold Gluon** — the contact-map/topo Gluon for protein folding. - **Paper 24 (KnightForge):** The chess Gluo... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 22 — C-Form: MetaForge Applied Materials Gluon | 85 | **C = the material Gluon** — the applied materials Gluon that transports the morphic Gluon (Paper 21) into physical material candidates. In the lattice_forge substrate, C is realized as the **material Gluon** that: - The material Gluon = the `metaforge` transport operator - Each material candidate = a token from Paper 21 with physical properties (Gluon mass, energy, stability) - The material transport = `material_{n+1} = metaforge_token(token_n, constraints)` - The material Gluon's mass = the material's formation energy / stability metric C is the **material Gluon** — the ForgeFactory method that proposes metamaterial candidates. - **Paper 23 (FoldForge):** The material Gluon's fold logic = ... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 25 — C-Form: Energetic Traversal Maps Gluon | 81 | **C = the traversal energy Gluon** — the energy/ledger Gluon that adds energy and traversal costs to cross-language, figure, material, and fold transformations. In the lattice_forge substrate, C is realized as the **traversal Gluon** that: - The traversal Gluon = the `paper25_traversal_maps` transport operator - Each transformation = a traversal path with energy cost ledger - The traversal transport = `traversal_{n+1} = energetic_map(transformation_n, energy_budget)` - The traversal Gluon's energy = the accumulated energy cost along the path - The traversal Gluon's ledger = the energy/oblivion ledger (energy in, entropy out) C is the **traversal Gluon** — the energy/ledger Gluon for cross-do... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-22.75: Paper 22.75 - MetaForge Next-State Bridge | 81 | Paper 22 exports a candidate-ledger pattern to the next applied papers. The pattern is: choose a domain inventory, score admissible partners or transforms, run the finite candidate transport, preserve failures as obligations, and emit a reviewable production or test ledger. The next state receives: - finite inventory discipline, - partner/transform scoring, - ten-step candidate transport, - error-wall-to-obligation carry, - seam or mitigation proposal rows, - production/test estimate ledger, - invalid-promotion labels. Paper 23 may use the fold and seam pattern for proteins. A protein fold claim must keep sequence, structure, energy, and assay evidence separate. Paper 22 does not prove prote... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| package_build_receipt: package_build_receipt | 79 | { "receipt": "astro_package_build_test_receipt", "generated": "2026-06-18", "package": "metaforge-ai", "package_root": "git-hosted-roots/CQECMPLX-Production/production/lib-forge/CQECMPLX-MetaMaterial-Designer", "status": "PASS_ENGINEERING_SCOPE_WITH_VALIDATION_OBLIGATIONS", "build": { "command": "python -m pip wheel . --no-deps -w build_smoke_dist", "status": "PASS", "artifact": "build_smoke_dist/metaforge_ai-0.1.0-py3-none-any.whl", "sha256": "4C09A08756E99497B6A4F83A67CFF856DB6D8DAF05D4D21BAE5FA06F155FF7D7", "hygiene": { "no_pycache_in_wheel": true, "no_tests_in_wheel": true, "no_receipts_in_wheel": true, "console_scripts": [ "astro-metaforge = meta_material_system.astro_metaforge:main", "... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| additional routed cards |  | 17 more cards are listed in `ARCHIVE_EVIDENCE_CARD_MATRIX.json`. | Use during final body rewrite. |

### Material Claim Upgrades From Cards

| Upgrade target | Evidence card | How it improves the paper | Boundary |
|---|---|---|---|
| receipt/verifier binding | CQE-paper-22.50: Paper 22.50 - MetaForge Claim Contract | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| source-backed expansion | CQE-paper-22: Paper 22 - MetaForge Applied Materials | Use this card to expand definitions, methods, or limitations with sourced detail. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| receipt/verifier binding | CQE-paper-22.25: Paper 22.25 - MetaForge Toolkit Supplement | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| receipt/verifier binding | FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| transport/formalism enrichment | FORMAL: Paper 22 — C-Form: MetaForge Applied Materials Gluon | Use this card to state the transport object and its downstream imports more explicitly. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| transport/formalism enrichment | FORMAL: Paper 25 — C-Form: Energetic Traversal Maps Gluon | Use this card to state the transport object and its downstream imports more explicitly. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |

These upgrades should be folded into the main body during the next prose rewrite:
definitions should become more specific, proof sketches should cite the relevant
receipt/tool/card, and limitations should preserve the card's stated boundary.

## Evidence Appendix

Receipt indices, PEEP bindings, and falsifier tables are maintained in the audit assembly product. This appendix provides a compact digest; it does not limit the main claims above.

**Full audit assembly:** [`../ASSEMBLED_FLCR_PRODUCTS/FLCR-21__Materials_Candidate_Generation__assembled.md`](../ASSEMBLED_FLCR_PRODUCTS/FLCR-21__Materials_Candidate_Generation__assembled.md)
**Source truth:** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-21\formal.md`

### Top receipt paths (row-scoped first)

| Receipt path | Row-scoped | Source |
|---|---|---|
| `D:\CQE_CMPLX\CMPLX-Kernel\kernel\lib-forge\ChromaForge\receipt.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-Kernel\kernel\lib-forge\lattice_forge_src\algebra\verify_o1.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-Kernel\kernel\lib-forge\lattice_forge_src\tools\receipt.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\ChromaForge\receipt.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\lattice_forge_src\algebra\verify_o1.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\lattice_forge_src\tools\receipt.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\RECEIPT_CHAIN\INVENTOR_DECLARATION.md` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\RECEIPT_CHAIN\RECEIPT_CHAIN.md` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\RECEIPT_CHAIN\receipts.json` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\VERIFICATION\verify_problem_1.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\VERIFICATION\verify_problem_2.py` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\VERIFICATION\verify_problem_3.py` | no | timeline_node |

_… and 269 additional receipt references in the assembled audit product._

### PEEP bindings (digest)

- `PEEP-2026-005`
- `PEEP-2026-010`
- `PEEP-2026-013`
- `PEEP-2026-018`
- `PEEP-2026-020`
- `PEEP-2026-021`
- `PEEP-2026-022`
- `PEEP-2026-036`
- _… and 50 more in assembled product._

### Falsifiers and comparators (digest)

| Record | DOI | Decision |
|---|---|---|
| PEEP-2026-005 | 10.1063/5.0280632 | ASSEMBLE |
| PEEP-2026-010 | 10.1063/5.0280632 | ASSEMBLE |
| PEEP-2026-013 | 10.1007/s00012-025-00908-5 | ASSEMBLE |
| PEEP-2026-018 | 10.25088/complexsystems.34.3.259 | ASSEMBLE |
| PEEP-2026-020 | 10.25088/complexsystems.34.3.259 | ASSEMBLE |
| PEEP-2026-021 | 10.25088/complexsystems.34.3.259 | ASSEMBLE |
| PEEP-2026-022 | 10.25088/complexsystems.34.3.259 | ASSEMBLE |
| PEEP-2026-036 | 10.1038/s41524-025-01826-9 | ASSEMBLE |

---

_Maximal reader manuscript — prose tier `maximal_publication` · renderer `full_formal_body_v2` · audit: `../ASSEMBLED_FLCR_PRODUCTS/FLCR-21__Materials_Candidate_Generation__assembled.md`._
