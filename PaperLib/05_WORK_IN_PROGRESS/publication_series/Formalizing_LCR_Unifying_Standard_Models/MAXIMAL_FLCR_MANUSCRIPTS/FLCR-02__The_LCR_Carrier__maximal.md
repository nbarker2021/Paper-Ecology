# FLCR-02 — The LCR Carrier

**Series:** Formalizing LCR, Unifying Standard Models  
**Authors:** _[FLCR series]_  
**Date:** 2026-07-01  
**Manuscript face:** maximal publication (unguarded reader prose)
## Abstract

This paper defines the LCR carrier as the canonical radius-1 local readout with a distinguished center and two ordered boundary slots. The carrier is finite, inspectable, and minimal: any smaller carrier collapses either the center or one boundary address. The paper proves the binary eight-state surface, reversal action, shell grading, and shell-2 doublet-plus-pivot structure used by later papers.

## Keywords

LCR carrier; radius-1 cellular automaton; C2 action; shell grading; minimal arity.

## 1. Contribution And Scope

- Defines LCR as the primitive local address surface for the series.
- Proves the three-slot arity lower bound for center-plus-two-boundary data.
- Registers the binary shell profile 1,3,3,1 and the reversal action.
- Separates internal spinor-like local semantics from physical spin transport.

This paper anchors the LCR-native construction band. Physics-facing language routes through explicit calibration and translation surfaces so FLCR-31 through FLCR-40 can pursue literal Standard Model correspondence as a program — not by silent vocabulary promotion.

### Series Posture Inherited From FLCR-01

This paper inherits the FLCR-01 doctrine. Guardrails are automation controls:
they govern AI agents, validators, build scripts, generated prose, and claim
promotion workflows. They are not restrictions on human creativity or
hypothesis formation.

The paper should therefore name the strongest intended reading of `The LCR Carrier`,
display the parts already proved at this layer, and route the remaining
distance as explicit open obligations. Those obligations are channels from the
current prestate into later exploration.

The analog/workbook layer is also an access kit. It should preserve the local
state in forms that can eventually be replayed without electricity, internet,
computers, or paper. Later papers may work toward literal physics even where
this local paper only supplies the finite or LCR-native carrier.

## 2. Source Routing

Primary routed sources:

- `01_LCR_Chain_Carrier.md`
- `supplements/01_INTERNAL_REASONING_SUPPLEMENT.md`

Cross-corpus evidence classes:

- `CAM_CLAIM_100_SCORE_AUDIT.md`
- `NSIT_TOOL_CLOSURE_MATRIX.md`
- `NSIT_REASONED_CLOSURE_PASS.md`
- `PAPER_REWORKS_CRYSTAL_PROJECTION.json`
- standards, glue, window, and node databases where applicable
- notebook-derived review prompts and orbital source manifests

## 3. Definitions

- **LCR state.** A triple (L, C, R) with left boundary, center, and right boundary coordinates.
- **Binary chart.** The finite carrier {0,1}^3 containing exactly eight states.
- **Shell grade.** The Hamming weight of the binary state, giving multiplicities 1,3,3,1.
- **Reversal.** The C2 action rho(L,C,R) = (R,C,L).

## Main Results

This paper states its results at **maximal claim posture**: the fullest scientific hypothesis the present receipt-bound construction supports, with forward channels named explicitly where stronger calibration remains open.

### Program summary

This paper defines the LCR carrier as the canonical radius-1 local readout with a distinguished center and two ordered boundary slots. The carrier is finite, inspectable, and minimal: any smaller carrier collapses either the center or one boundary address. The paper proves the binary eight-state surface, reversal action, shell grading, and shell-2 doublet-plus-pivot structure used by later papers.

In plainer terms: this paper defines one reliable piece of the LCR stack and
states exactly how later papers are allowed to use it. It is not trying to win
every downstream claim locally. It is making the local result strong enough
that later papers can build on it without changing what was proved.

Theorem 2.1: The LCR carrier is the minimal address-preserving carrier for one center and two distinguishable boundary slots.

Lane: `receipt_bound_internal_result`.

- Defines LCR as the primitive local address surface for the series.
- Proves the three-slot arity lower bound for center-plus-two-boundary data.
- Registers the binary shell profile 1,3,3,1 and the reversal action.
- Separates internal spinor-like local semantics from physical spin transport.

### Formal results

**Theorem 2.1.** The LCR carrier is the minimal address-preserving carrier for one center and two distinguishable boundary slots.

**Theorem 2.2.** In the binary chart, reversal is an involution and partitions the carrier into fixed states and reversal pairs.

**Proposition 2.3.** The shell profile of {0,1}^3 is the binomial profile 1,3,3,1.

### Claim lane reference

| Claim | Lane |
|---|---|
| Theorem 2.1 | `receipt_bound_internal_result` |
| Theorem 2.2 | `receipt_bound_internal_result` |
| Proposition 2.3 | `standard_theorem_citation_bound_result` |

## 5. Paper-Specific Development

1. Represent each local observation as (L,C,R), preserving left boundary, center, and right boundary.
2. Enumerate the binary chart {0,1}^3 and compute shell grade by Hamming weight.
3. Apply reversal rho(L,C,R)=(R,C,L) and record fixed points and two-state orbits.
4. Use the arity lower bound to show why fewer than three slots destroys either center identity or boundary distinction.

### Proof Sketch

The finite proof is direct enumeration plus a minimality argument. There are exactly eight binary triples. Reversal applied twice returns the original triple, so it is a C2 action. Any two-slot representation has only two addresses and therefore must identify two of the three roles {left, center, right}; this violates the carrier contract.

## 6. Construction

The construction is intentionally staged. First, the paper names the finite or
typed object that can be inspected directly. Second, it declares the admissible
operations over that object. Third, it records the receipt or source class that
allows another paper to consume the result. Fourth, it names the residue that
must not be silently promoted.

For this paper, the operative object is `The LCR Carrier`. Its safe consumption
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

## Recent External Quantum Evidence Intake

These rows add newly routed external physics papers as citation-bound or calibration-bound evidence. They are not CAM receipts unless a later tool run reconstructs their signatures.

| Source | Lane | How It Helps This Paper | Boundary |
|---|---|---|---|
| EXT-RQM-CONSISTENT-2026: Quantum mechanics based on real numbers: A consistent description; DOI `10.1103/4k13-sdjh`; arXiv `2503.17307` | `standard_theorem_citation_bound_result` | Supports the carrier-layer distinction between an addressed physical state and the representational field chosen to describe it. | Do not infer that every LCR relabeling is physically equivalent; equivalence requires an explicit construction or adapter. |

## 7. Evidence And Receipts

| Evidence source | What it contributes |
|-----------------|---------------------|
| Paper 01 legacy body | Carrier enumeration, shell-2 doublet, local O8/double-cover route. |
| Internal supplement 01 | Radius-1 CA grounding, arity lower bound, C2 action, binomial shell grading. |
| NSIT tool matrix | T5-T7 plus shell-2 doublet receipt and O8 spinor double-cover closure route. |
| CAM Claim 100 Score Audit | Paper 01 scored 94 as internally closed, with physical spinor transport deferred. |

## Appendix C. Implementation Intake

This addendum binds implementation work that was not fully represented in the earlier paper routing. The rows below are not pasted source text; they are evidence-lane imports that change what the paper can claim now.

| Implementation source | Lane | Claim effect | Boundary |
|---|---|---|---|
| IMPL-LCR-TYPED-KERNEL | `normal_form_result` | Promotes L/C/R from notation to operational lane contract: LAdapter, CKernel, RChannel, strict policy gates, and lane classification. | This closes operational admission and policy routing; it does not by itself prove external physical identity. |
| IMPL-R30-LATTICE-THEOREM-REGISTRY | `standard_theorem_citation_bound_result` | Adds executable theorem registry rows for octonions, J3(O), chart-to-J3(O), exact n=3 SU(3) Weyl closure, Rule-30 8x8 transition, Niemeier routes, relational qubit closure, Monster/Pariah boundary, and computational ISA signatures. Verification: Targeted pytest passed: 11 Rule-30 normal-form/proof-shell tests, including address decomposition, centroid state, proof-shell dependency acyclicity, Niemeier obligation boundaries, scoped claim promotion, and full dependency closure. | Imports verifier-backed internal/formal results; transported physical interpretations remain lane-bound. |

The immediate paper effect is stronger claim posture where these implementation rows satisfy the relevant lane. Remaining caution is reserved for specific claims that still lack an adapter, comparator, calibration target, or rerun receipt.

## Appendix D. Resolved-State Closure Pass

This pass removes false restrictions on the paper's claim posture. A row is no longer called open merely because a stronger future claim exists. The satisfied lane is closed now; only the stronger claim that lacks its required adapter, comparator, calibration, or falsifier remains as residue.

### Closed Now

| Row | Lane | Resolved state | Remaining boundary |
|---|---|---|---|
| paper lift enumeration | `receipt_bound_internal_result` | 8/8 LCR states succeeded; error walls=0; avg TarPit mass=0.526710. | This closes the paper-local finite lift readout, not every stronger physical interpretation. |
| carrier enumeration | `normal_form_result` | The LCR carrier action is closed as an addressable finite-state surface for its declared domain. | The family closure is a structural lane; measured physics still requires destination-specific calibration. |
| decade-1 tower | `receipt_bound_internal_result` | The decade tower is resolved with avg TarPit mass=0.510370 and mass sum=40.829567. | The decade total is an internal tower metric, not a standalone universal physical constant. |
| family-02 cross-lift comparison | `cam_crystal_reapplication_result` | Family tower binds FLCR-02, FLCR-12, FLCR-22, FLCR-32; avg TarPit mass=0.511700; error walls=0. | Cross-lift agreement strengthens routing and comparison; it does not erase paper-local boundaries. |
| finite LCR carrier | `receipt_bound_internal_result` | The 2x2x2 carrier is closed as the finite local object consumed by later papers. | Physical interpretation of a carrier requires adapter rows. |

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

- The shell-2 doublet is an internal interface, not a measured particle claim.
- SU(2)-style language may be used as standard analogy only where explicitly lane-tagged.
- Later observer or physics papers must attach calibration or observer receipts before consuming this as physical spin.

A falsifier for this paper is any example that satisfies the declared input
conditions while violating the stated construction, receipt, or lane boundary.
An interpretation that merely wants a stronger downstream conclusion is not a
falsifier; it is an obligation routed to a later paper.

## Dual Positioning: Story And Formal Carrier

This paper must be read in two synchronized ways. Sequentially, it explains why
the next state exists in the corpus story. Formally, it binds that state to
accepted mathematics, IRL formalism, code receipts, validators, CAM/crystal
lookups, and claim-lane boundaries.

Assigned original ribbon role(s): `01`/enumeration_action.

| Original slot | Family | Lift | Role | Proof form |
|---|---|---:|---|---|
| `01` | enumeration_action | 0 | order-1 slot-1: start the active one-dimensional action / enumerate the center state | enumeration proof and identity preservation |

The formal obligation is to state the strongest valid claim available for this
paper without letting interpretation silently change the addressed object. Any
author interpretation belongs beside the formalism as a declared relabeling,
bridge, or analog, and must be accompanied by the evidence lane that makes the
claim consumable by later papers.

## State-Bound Proof Contract

This paper receives: state emitted by prior slot 00 and reopened at original slot 01 (LCR Chain Carrier).

It must produce: formal result of original slot 01 plus the same-family lift path toward slot 11.

Semantic transition: select the active center and enumerate the addressable state space at the current lift.

Accepted formalism targets to bind in the journal rewrite:

- finite set enumeration
- ordered tuples and projections
- group actions on finite carriers
- minimality or lower-bound arguments

| Slot | Family | Lift | Produced proof form |
|---|---|---:|---|
| `01` | enumeration_action | 0 | enumeration proof and identity preservation |

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

Use past work to increase the state inventory: enumerate the local carrier, admission candidates, or applied reader objects before interpretation is added.

### Primary Evidence Inputs

| Source | Placement reason |
|---|---|
| `01_LCR_Chain_Carrier.md` | primary assigned source for the paper's formal spine |
| `supplements/01_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement contributing to definitions, proof sketch, and limitations |

### Secondary And Orbital Evidence Inputs

| Source | Placement reason |
|---|---|
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
| `PAPER_REWORKS_CRYSTAL_PROJECTION.json` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NEW_PAPER_NEEDS.md` | route relevant obligations into this paper's burden table: NP-04 F4 Encoder Universality And Exceptional Route Conditions |
| Additional source routes | Complete routing is maintained in the source-placement appendix |

### Crystal And Standards Evidence To Bind

- Paper Reworks crystal projection: 33 paper markdown files, 9 supplements, 5 queues, 6 lattice-forge unification artifacts, 140 faces, 140 vignettes, and 280 CAM nodes.
- Standards-window intake: 192/192 corpus conformance verdicts PASS; 140/142 obligations have candidate routes; 2/4/8/16/32 window lattice is available for cross-paper reads.
- Agent/crystal harvest: agent-generated memory, runtime standards starter, current runtime build, repo-harvest CAM, notebook-derived bundles, and downloaded crystal payloads are orbital evidence surfaces.
- NSIT inventory baseline: 220 validators, 1786 receipt/data artifacts, 1137 formal-paper-like artifacts, 114 supplements, and 86 memory/CAM artifacts.

### Paper-Specific CAM/Score Rows

| 01 | 94 | internally closed | LCR minimality, shell-2 doublet, local O8 double cover, Paper 03 carry-forward | physical spinor transport remains NP-10/physics bridge |

### Paper-Specific NSIT Closure Rows

| T5-T7 plus shell-2 doublet | batch_tool_unison_closure | `f4_action.py`, `core.py` | Papers 03 and 01 | `su3_closure_T5_T7_receipt.json` 10/10; `bijective_shell2_doublet_receipt.json` 7/7 | SU(3)/8x8 closure and single-tape doublet close. |
| O8 spinor SU(2) double cover | batch_tool_unison_closure | `oloid_kinematic` frame inversion semantics | Paper 01 | `o8_spinor_double_cover_closed_receipt.json` 6/6 | F^2 = -1 at 2pi; F^4 = +1 at 4pi. |

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
| Spinor/SU(2) Double-Cover Local Semantics | `receipt_bound_internal_result` | Promote local 2pi sign-flip / 4pi return semantics where the O8/frame-inversion receipt is attached. | Bind the O8 receipt and cite standard SU(2)->SO(3) double-cover semantics as standard analogy/support. | Physical observer, quantum measurement, and empirical spin claims remain routed to observer/physics calibration. |

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
| Spinor Double Cover Local | This paper may claim local frame-inversion or spinor-style behavior only for its finite/internal carrier object. | O8 frame-inversion receipt plus standard SU(2)->SO(3) double-cover semantics. | Promote local 2pi sign-flip / 4pi return semantics as internal carrier semantics when the receipt is attached. | Do not promote to empirical spin, quantum measurement, or physical observer claims without external physics calibration. |

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
| CQE-paper-10: Paper 10 - T10 Master Receipt | 81 | Paper 10 proves the first stack-level receipt theorem in the CQECMPLX suite. Its object is not a new physical mechanism. Its object is the proof that Paper 00 and Papers 01-09 are bound into one inspectable and replay... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| FORMAL: Paper 24 — C-Form: KnightForge / N-Dimensional Chess Automata Gluon | 77 | **C = the chess automata Gluon** — the L-conjugate CA Gluon that generalizes knight moves to N-dimensional board operators. In the lattice_forge substrate, C is realized as the **chess Gluon** that: - The chess Gluon ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| FINAL_FORMAL_PAPER: Complete Formal Claims: The Folded Strand | 75 | We present the complete closed-form claim set of the CQE_CMPLX corpus: - 33 papers = 33 folding operations on a self-complementary strand - 144 tools = cumulative analog kit = digital twin surface - 135 digital twins ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| SUMMARY-V-32-Theorems-Registry: Summary Paper V — The 32 Theorems in One Table: Closed-Form Registry | 75 | This paper is the **complete closed-form registry of all 32 theorems** in the CQE_CMPLX corpus. Each theorem is stated precisely, given its formal context (where it is proven), and listed with its verifier. The table ... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| CQE-paper-10.25: Paper 10.25 - Toolkit for the T10 Master Receipt | 73 | Paper 10.25 describes the tools for reviewing the T10 master receipt. These tools expose receipt binding, transport classification, local witness replay, and lookup cache materialization. They do not close the open li... | Source-backed support; promotion requires the paper-local claim lane and evidence boundary. |
| Additional evidence cards | 34 total | The complete card inventory is maintained in the archive evidence matrix. | Cards are source-discovery aids until bound to paper-local evidence. |

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
| Publication ID | `FLCR-02` |
| Legacy source slot(s) | `01` |
| Ribbon role | order-1 slot-1: start the active one-dimensional action / enumerate the center state |
| Proof form | enumeration proof and identity preservation |
| Received state | state emitted by prior slot 00 and reopened at original slot 01 (LCR Chain Carrier) |
| Produced state | formal result of original slot 01 plus the same-family lift path toward slot 11 |

### Claim-Evidence Table

| Claim | Lane | Evidence to attach | Boundary |
|---|---|---|---|
| Theorem 2.1 | `receipt_bound_internal_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | The LCR carrier is the minimal address-preserving carrier for one center and two distinguishable boundary slots. |
| Theorem 2.2 | `receipt_bound_internal_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | In the binary chart, reversal is an involution and partitions the carrier into fixed states and reversal pairs. |
| Proposition 2.3 | `standard_theorem_citation_bound_result` | Receipt, source card, validator, citation, or CAM route named in the paper manifest | The shell profile of {0,1}^3 is the binomial profile 1,3,3,1. |

### Figure Plan

| Figure | Purpose | Caption |
|---|---|---|
| FLCR-02-F1 | State enumeration chart | Schematic showing how `FLCR-02` turns its received state into the produced state while preserving claim lanes and residue boundaries. |
| FLCR-02-F2 | Evidence routing map | Diagram of source papers, archive cards, CAM/crystal routes, validators, and workbook replay paths used by this manuscript. |
| FLCR-02-F3 | Same-family lift context | Diagram placing this paper in the original `00-79` ribbon family and showing predecessor/successor slots. |

### In-Text Figure FLCR-02-F1: State enumeration chart

```text
received state
  -> State enumeration chart
  -> formal claim lane
  -> evidence object / receipt / citation
  -> produced state
  -> remaining residue
```

### Table Plan

| Table | Purpose |
|---|---|
| FLCR-02-T1 | State inventory table |
| FLCR-02-T2 | Claim-lane/evidence-boundary table |
| FLCR-02-T3 | Archive evidence card and source-backed upgrade table |
| FLCR-02-T4 | Workbook replay and falsifier table |

### Worked Example

Enumerate the local carrier or admission candidates and classify each row before interpretation. The example must name the input object, the operation,
the evidence object, the allowed revised claim, and the remaining boundary.

### Nomenclature And Glossary

| Term | Paper-local meaning |
|---|---|
| CAM | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| addressable slot | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| center state | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| claim lane | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| crystal | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| enumeration | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| finite domain | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |
| receipt | Defined by this paper as part of the `enumeration_action` proof role; final copyedit should replace this row with the exact paper-local definition. |

### Appendix FLCR-02-A: Evidence Package

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

`FLCR-02` (`The LCR Carrier`) occupies the `enumeration_action` role at lift depth `0`.
The paper receives state emitted by prior slot 00 and reopened at original slot 01 (LCR Chain Carrier). It produces formal result of original slot 01 plus the same-family lift path toward slot 11. The state transition is:
select the active center and enumerate the addressable state space at the current lift.

The paper-local proof form is:

```text
enumeration proof and identity preservation
```

The integration result is an identity-preserving inventory of admissible state objects. This addendum records how that result is
consumed by the publication series without relying on editorial instructions or
private working context.

### 11.2 Formal Carrier

| Formal carrier | Function |
|---|---|
| finite set enumeration | Formal carrier for the paper-local result. |
| ordered tuples and projections | Formal carrier for the paper-local result. |
| group actions on finite carriers | Formal carrier for the paper-local result. |
| minimality or lower-bound arguments | Formal carrier for the paper-local result. |

The LCR, CAM, crystal, forge, and analog vocabulary functions as a typed access
layer over these carriers. A relabeling is admissible only when the addressed
object, evidence lane, boundary, and downstream import rule remain attached.

### 11.3 Claim Ledger

| Claim | Lane | Statement |
|---|---|---|
| Theorem 2.1 | `receipt_bound_internal_result` | The LCR carrier is the minimal address-preserving carrier for one center and two distinguishable boundary slots. |
| Theorem 2.2 | `receipt_bound_internal_result` | In the binary chart, reversal is an involution and partitions the carrier into fixed states and reversal pairs. |
| Proposition 2.3 | `standard_theorem_citation_bound_result` | The shell profile of {0,1}^3 is the binomial profile 1,3,3,1. |

These claims are consumed at their stated lane. A stronger downstream statement
creates a new claim envelope with its own evidence object.

### 11.4 Evidence Package

| Evidence class | Routed items | Status |
|---|---|---|
| Legacy sources | `01_LCR_Chain_Carrier.md`, `supplements/01_INTERNAL_REASONING_SUPPLEMENT.md` | routed evidence |
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
| FLCR-02-F1: State enumeration chart | Visualizes the proof object, routing, or boundary. |
| FLCR-02-F2: Evidence routing map | Visualizes the proof object, routing, or boundary. |
| FLCR-02-F3: Same-family lift context | Visualizes the proof object, routing, or boundary. |

| Table | Role |
|---|---|
| FLCR-02-T1: State inventory table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-02-T2: Claim-lane/evidence-boundary table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-02-T3: Archive evidence card and source-backed upgrade table | Records claim lanes, evidence, sources, or falsifiers. |
| FLCR-02-T4: Workbook replay and falsifier table | Records claim lanes, evidence, sources, or falsifiers. |

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

Use past work to increase the state inventory: enumerate the local carrier, admission candidates, or applied reader objects before interpretation is added.

### Routed Full Sources

| Source | Placement reason |
|---|---|
| `01_LCR_Chain_Carrier.md` | primary assigned source for the paper's formal spine |
| `supplements/01_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement; should be integrated into definitions, proof sketch, and limitations |

### Routed Partial/Orbital Sources

| Source | Placement reason |
|---|---|
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
| `PAPER_REWORKS_CRYSTAL_PROJECTION.json` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NEW_PAPER_NEEDS.md` | route relevant obligations into this paper's burden table: NP-04 F4 Encoder Universality And Exceptional Route Conditions |
| additional routed sources | 4 more entries remain in `SOURCE_PLACEMENT.md` |

### Crystal And Standards Evidence To Bind

- Paper Reworks crystal projection: 33 paper markdown files, 9 supplements, 5 queues, 6 lattice-forge unification artifacts, 140 faces, 140 vignettes, and 280 CAM nodes.
- Kimi standards/window intake: 192/192 corpus conformance verdicts PASS; 140/142 obligations have candidate routes; 2/4/8/16/32 window lattice is available for cross-paper reads.
- Agent crystal harvest: Claude memory, Kimi MannyAI starter, D:/MannyAI current build, repo-harvest CAM, NotebookLM/MannyAI bundles, and downloaded crystal payloads are orbital evidence surfaces.
- NSIT inventory baseline: 220 validators, 1786 receipt/data artifacts, 1137 formal-paper-like artifacts, 114 supplements, and 86 memory/CAM artifacts.

### Paper-Specific CAM/Score Rows

| 01 | 94 | internally closed | LCR minimality, shell-2 doublet, local O8 double cover, Paper 03 carry-forward | physical spinor transport remains NP-10/physics bridge |

### Paper-Specific NSIT Closure Rows

| T5-T7 plus shell-2 doublet | batch_tool_unison_closure | `f4_action.py`, `core.py` | Papers 03 and 01 | `su3_closure_T5_T7_receipt.json` 10/10; `bijective_shell2_doublet_receipt.json` 7/7 | SU(3)/8x8 closure and single-tape doublet close. |
| O8 spinor SU(2) double cover | batch_tool_unison_closure | `oloid_kinematic` frame inversion semantics | Paper 01 | `o8_spinor_double_cover_closed_receipt.json` 6/6 | F^2 = -1 at 2pi; F^4 = +1 at 4pi. |

### Source Signals Extracted For Rewrite

- `01_LCR_Chain_Carrier.md`: # Paper 01 — LCR Chain Carrier **Status:** IPMC — internal physics map closed for the minimal-carrier, shell-2 doublet, and local O8 frame-inversion theorems; SU(2)/spinor/O8 physical transport bridges are named and scoped. **Verifiers:** - `verify_lcr_carrier.py` → `lcr_carrier_receipt.json` — **pass**, 8/8 - `verify_bijective_shell2_doublet.py` → `bijective_shell2_doublet_receipt.json` — **pass**, 7/7 - `verify_o8_spinor_double_cover_closed.py` → `o8_spinor_double_cover_closed_receipt.json` — **pass**, 6/6 ## Publication Draft: Formal Scientific Body ### Abstract ordered local triple `(L, C, R)`. The result closed here is deliberately finite. carrier realizes that lower bound, and the verifier receipts enumerate the full The paper also closes two local interface claims. First, the shell-2 stratum trace-2 and closure papers. Second, a local O8 frame-inversion verifier realizes `4*pi` ad
- `supplements/01_INTERNAL_REASONING_SUPPLEMENT.md`: # Paper 01 Internal Reasoning Supplement This supplement does not replace Paper 01's receipts. It records additional ways to strengthen, clarify, or route the paper's claims. ## Core Reading Paper 01 is a finite arity and symmetry theorem. The LCR triple is not only a claim is finite and exact: carrier arity, reversal symmetry, orbit structure, ## Firm Applications | Radius-1 CA neighborhood | `(L,C,R)` is the standard three-cell local neighborhood for elementary cellular automata. | State that LCR is the canonical radius-1 local readout, while CQE adds claim typing and receipt discipline. | | SU(2)->SO(3) double-cover guard | The `2*pi` sign flip / `4*pi` return is standard spinor double-cover behavior. | Paper 01 can cite the standard semantics as analogy/support, while the receipt closes only local carrier semantics. | | Finite-state interface contract | The shell-2 doublet-plus-pivot

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
| CQE-paper-10: Paper 10 - T10 Master Receipt | 81 | Paper 10 proves the first stack-level receipt theorem in the CQECMPLX suite. Its object is not a new physical mechanism. Its object is the proof that Paper 00 and Papers 01-09 are bound into one inspectable and replayable unit. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 24 — C-Form: KnightForge / N-Dimensional Chess Automata Gluon | 77 | **C = the chess automata Gluon** — the L-conjugate CA Gluon that generalizes knight moves to N-dimensional board operators. In the lattice_forge substrate, C is realized as the **chess Gluon** that: - The chess Gluon = the `knightforge` transport operator - Each piece = a ribbon state with move-set Gluon - The knight's L-move = the L-conjugate move in the 8-state shell=2 stratum - The N-dimensional board = the powered lattice code chain (1→9→49→72) - The move-set Gluon = the piece's allowed transition matrix C is the **chess Gluon** — the L-conjugate CA Gluon for N-dimensional automata. - **Paper 25 (Energetic Traversal):** The chess Gluon's move energy = the traversal Gluon's cost. - **Pape... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FINAL_FORMAL_PAPER: Complete Formal Claims: The Folded Strand | 75 | We present the complete closed-form claim set of the CQE_CMPLX corpus: - 33 papers = 33 folding operations on a self-complementary strand - 144 tools = cumulative analog kit = digital twin surface - 135 digital twins = exact rational-verifiable operations - 11 bilateral verifications = digital-analog isomorphism proven - 32 formal theorems = exact rational arithmetic (zero mismatches) - 1 retrospective observation = single H-bond reads identically from both strands | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SUMMARY-V-32-Theorems-Registry: Summary Paper V — The 32 Theorems in One Table: Closed-Form Registry | 75 | This paper is the **complete closed-form registry of all 32 theorems** in the CQE_CMPLX corpus. Each theorem is stated precisely, given its formal context (where it is proven), and listed with its verifier. The table is the corpus's theorem index. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-10.25: Paper 10.25 - Toolkit for the T10 Master Receipt | 73 | Paper 10.25 describes the tools for reviewing the T10 master receipt. These tools expose receipt binding, transport classification, local witness replay, and lookup cache materialization. They do not close the open lifts. The toolkit works with: ```text Paper 00 binding observer center C00 00 -> 1 encoding event paper receipt bindings P01..P09 transport obligation rows lookup receipts open-lift set master verdict ``` Primary executable files: ```text production/formal-papers/CQE-paper-10/verify_t10_master_receipt.py production/formal-papers/CQE-paper-10/t10_master_receipt.json ``` Primary package bindings: ```text lattice_forge.transport_obligations.verify_transport_obligations lattice_forge... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 01 — Side-Flip SU(2) Doublet (T_BIJECTIVE) | 73 | **PROVEN by structural identification** on the T3 chart/J₃(O) isomorphism. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| block-01-dyad-01-08: Block 01 Dyad Brief - Papers 1 and 8 | 71 | Source: Dyad Agent A, read-only synthesis. No files edited by agent. Final scientific focus: Paper 1 is the minimal carrier theorem. The integer paper should prove that `(L,C,R)` is the smallest ordered local carrier preserving one observer-selected center and two distinguishable boundary addresses. It should also prove the binary inventory facts: eight states, shell counts `1,3,3,1`, left-right reversal `rho(L,C,R) = (R,C,L)`, center preservation, involution, four fixed states, two reversal pairs, and the correction that opposition is address-based rather than value-based. Proof/evidence files: ```text corpus/legacy/papers-source/CQE-paper-01.md production/formal-papers/CQE-paper-01/FORMAL_... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SOURCE: Paper 13 - Standard-Model Quark-Face Transport | 71 | The substrate registers a sequence's local `(L, C, R)` chart state into the diagonal of `J_3(O)`, the natural 3-position Hermitian-octonion algebra whose automorphism group is `F_4` (PROOF Paper 13). On the `shell=2` stratum the three states `{(1,1,0),(1,0,1),(0,1,1)}` are exactly the three trace-2 idempotents `{E11+E22, E11+E33, E22+E33}` on which the `SU(3)` Weyl group `S_3` acts by permuting diagonal indices (`f4_action.py`). This paper reads that structure as a *quark-face transport*: the three diagonal positions are treated as the three color faces, the `shell=2` doublet carries the `SU(2)` spin-1/2 structure on a single tape (Paper 01, `T_BIJECTIVE`), and the bounded `G_2 -> F_4 -> T5A... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| additional routed cards |  | 26 more cards are listed in `ARCHIVE_EVIDENCE_CARD_MATRIX.json`. | Use during final body rewrite. |

### Material Claim Upgrades From Cards

| Upgrade target | Evidence card | How it improves the paper | Boundary |
|---|---|---|---|
| receipt/verifier binding | CQE-paper-10: Paper 10 - T10 Master Receipt | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| transport/formalism enrichment | FORMAL: Paper 24 — C-Form: KnightForge / N-Dimensional Chess Automata Gluon | Use this card to state the transport object and its downstream imports more explicitly. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| source-backed expansion | FINAL_FORMAL_PAPER: Complete Formal Claims: The Folded Strand | Use this card to expand definitions, methods, or limitations with sourced detail. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| receipt/verifier binding | SUMMARY-V-32-Theorems-Registry: Summary Paper V — The 32 Theorems in One Table: Closed-Form Registry | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| receipt/verifier binding | CQE-paper-10.25: Paper 10.25 - Toolkit for the T10 Master Receipt | Move the relevant result from narrative support into a receipt-bound evidence row. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |
| source-backed expansion | FORMAL: Paper 01 — Side-Flip SU(2) Doublet (T_BIJECTIVE) | Use this card to expand definitions, methods, or limitations with sourced detail. | Keep the card's stated boundary; do not upgrade to physical/domain validation unless the card carries that evidence. |

These upgrades should be folded into the main body during the next prose rewrite:
definitions should become more specific, proof sketches should cite the relevant
receipt/tool/card, and limitations should preserve the card's stated boundary.

## Evidence Appendix

Receipt indices, PEEP bindings, and falsifier tables are maintained in the audit assembly product. This appendix provides a compact digest; it does not limit the main claims above.

**Full audit assembly:** [`../ASSEMBLED_FLCR_PRODUCTS/FLCR-02__The_LCR_Carrier__assembled.md`](../ASSEMBLED_FLCR_PRODUCTS/FLCR-02__The_LCR_Carrier__assembled.md)
**Source truth:** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\FLCR-02\formal.md`

### Top receipt paths (row-scoped first)

| Receipt path | Row-scoped | Source |
|---|---|---|
| `D:\CQE_CMPLX\CMPLX-R30-main\RECEIPT_CHAIN\RECEIPT_CHAIN.md` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\RECEIPT_CHAIN\receipts.json` | no | timeline_node |
| `D:\CQE_CMPLX\CMPLX-R30-main\VERIFICATION\verify_problem_3.py` | no | timeline_node |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-established_grounding_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-00-number_is_ribbon_digital_root_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-03-d4_atlas_bijectivity_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-correction_extraction_verdict_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-06-rule90_lucas_decomposition_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-atlas_unipotent_orbits_real_data_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-08-lattice_closure_template_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-hamiltonian_window_emergence_receipt.json` | no | closure_applied |
| `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-09-u_r30_quantum_circuit_receipt.json` | no | closure_applied |

_… and 44 additional receipt references in the assembled audit product._

### PEEP bindings (digest)

- `PEEP-2026-011`
- `LOCAL-GAP-0001`
- `LOCAL-GAP-0002`
- `LOCAL-GAP-0004`
- `LOCAL-GAP-0007`
- `LOCAL-GAP-0010`
- `LOCAL-GAP-0013`
- `LOCAL-GAP-0014`
- _… and 10 more in assembled product._

### Falsifiers and comparators (digest)

| Record | DOI | Decision |
|---|---|---|
| PEEP-2026-011 | 10.1112/blms.13228 | ASSEMBLE |
| LOCAL-GAP-0001 |  | REROUTE_OR_REPAIR |
| LOCAL-GAP-0002 |  | REROUTE_OR_REPAIR |
| LOCAL-GAP-0004 |  | REROUTE_OR_REPAIR |
| LOCAL-GAP-0007 |  | REROUTE_OR_REPAIR |
| LOCAL-GAP-0010 |  | REROUTE_OR_REPAIR |
| LOCAL-GAP-0013 |  | REROUTE_OR_REPAIR |
| LOCAL-GAP-0014 |  | REROUTE_OR_REPAIR |

---

_Maximal reader manuscript — prose tier `maximal_publication` · renderer `full_formal_body_v2` · audit: `../ASSEMBLED_FLCR_PRODUCTS/FLCR-02__The_LCR_Carrier__assembled.md`._
