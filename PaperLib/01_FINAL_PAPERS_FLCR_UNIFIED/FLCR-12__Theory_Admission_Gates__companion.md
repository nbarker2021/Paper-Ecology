# FLCR-12 Companion - Theory Admission Gates

## What This Paper Is Doing

This paper formalizes admission control for theories and candidate claims. The operative object is admission gate. The core result is that a candidate theory is admissible only when its object, lane, evidence class, residue, and falsifier are declared before promotion. The paper also defines how this result routes forward: later Standard Model translations must pass through this gate before appearing as FLCR claims. Its main residue is explicit: sporadic-boundary and encoder-invariance examples remain import routes, not blanket admission.

In plainer terms: this paper defines one reliable piece of the LCR stack and
states exactly how later papers are allowed to use it. It is not trying to win
every downstream claim locally. It is making the local result strong enough
that later papers can build on it without changing what was proved.

## Strongest Claim

Theorem 12.1: a candidate theory is admissible only when its object, lane, evidence class, residue, and falsifier are declared before promotion

Lane: `receipt_bound_internal_result`.

## Why It Matters

- Defines admission gate as a first-class FLCR object.
- States the local result: a candidate theory is admissible only when its object, lane, evidence class, residue, and falsifier are declared before promotion.
- Routes downstream use through claim lanes rather than inherited prose: later Standard Model translations must pass through this gate before appearing as FLCR claims.
- Preserves the residue boundary: sporadic-boundary and encoder-invariance examples remain import routes, not blanket admission.

## What It Does Not Claim Yet

- sporadic-boundary and encoder-invariance examples remain import routes, not blanket admission
- External calibration claims require units, datasets, citations, and reproducible data binding.
- A later translation paper may strengthen this result only by adding the missing lane evidence.

## How Later Papers Should Use It

Later papers cite this paper by claim and lane. If a later paper needs a
stronger statement, it must add the missing receipt, standard theorem citation,
CAM/crystal reapplication, normal-form proof, calibration datum, or falsifier
boundary. It does not inherit stronger language from older drafts.

## Reader Check

Before accepting a downstream use of this paper, ask:

1. Which exact claim is being consumed?
2. Which lane admits that claim?
3. What receipt, theorem, CAM route, or calibration source travels with it?
4. What residue is still forbidden from promotion?

## Why This State Happens Next

This companion layer carries the semantic story: why this paper appears here,
why the preceding state needs this move, and how the next paper is allowed to
consume it. Its job is not to weaken the formal claim; its job is to make the
state transition legible.

Assigned original ribbon role(s): `11`/enumeration_action.

The interpretive move in this paper must be presented as label management over
an already-addressed state. Where the paper changes language, it must say what
object remains invariant and what access path, label, or analogy changed.
## Narrative State Contract

The story obligation is to show why the received state naturally demands this
paper's transition:

```text
received state -> Theory Admission Gates -> produced state
```

Received state: state emitted by prior slot 10 and reopened at original slot 11 (Theory Admission Gate).

Produced state: formal result of original slot 11 plus the same-family lift path toward slot 21.

The companion should make the transition intelligible without treating metaphor
as proof. It may use the author's interpretation aggressively, but it must keep
the invariant object visible.
## Past Work Story Intake

This paper's story layer should explain how the older papers, supplements, and
crystal projections make the next state feel necessary rather than arbitrary.

For this slot, the narrative emphasis is:

Use past work to increase the state inventory: enumerate the local carrier, admission candidates, or applied reader objects before interpretation is added.

The companion should explicitly distinguish three voices:

| Voice | What belongs here |
|---|---|
| Accepted formalism | Standard math, CS, physics, or verified code result that already exists outside the interpretation. |
| Author interpretation | The LCR/CAM/crystal relabeling that makes the state addressable in this corpus. |
| Corpus story | Why this paper has to happen at this exact ribbon position and what later papers inherit. |
## Claim Reclassification Story

The companion should explain the claim-binding queue in human terms: what the
older paper was allowed to say at its time, what later evidence now lets it say
more sharply, and what still cannot be promoted.

| Queue | Lane | Promote now | Bind next | Residue |
|---|---|---|---|---|
| Negative And Failed-Route Receipts As Guards | `falsifier_or_open_obligation` | Use failed routes, rejected candidates, and boundary receipts as exclusion evidence and counterexample guards. | Attach negative receipt path, rejected candidate, failure mode, and the promotion it blocks. | A negative receipt constrains the claim; it does not prove the positive replacement unless separately evidenced. |
## Delta Story

The human-readable story for this paper should present the deltas as honest
growth rather than contradiction. The earlier paper was correct at its local
time slice; the later evidence returns through a named lane and sharpens the
representation.

| Delta | Local claim at paper time | Later evidence | Revised representation | Boundary kept |
|---|---|---|---|---|
| Negative Receipts As Guards | This paper may preserve failed routes and rejected candidates as meaningful boundary data. | Negative receipts, failed verifier rows, rejected-as-datum outputs, and obligation ledgers. | Use negative receipts as exclusion evidence and promotion guards. | A negative receipt blocks a promotion; it does not prove a positive replacement unless separately evidenced. |
## Archive Evidence Story Cards

These cards explain what older mirrors, toolkit supplements, claim contracts,
or formal variants add to this paper's story.

| Source card | Score | Contribution | Integration action |
|---|---:|---|---|
| CQE-paper-11.25: Paper 11.25 - Toolkit for the Theory Admission Gate | 81 | Paper 11.25 describes the tools for reviewing the theory admission gate. These tools expose candidate admission, boundary routing, rejected-as-datum behavior, and the Pariah/Happy-Family worked boundary receipt. The toolkit works with: ```text candidate theory T10 trust anchor Gluon mass trusted spectrum K_max = 9 declared encoder admission receipt verdict ``` Primary executable files: ```text production/formal-papers/CQE-paper-11/verify_theory_admission_gate.py production/formal-papers/CQE-paper-11/theory_admission_gate_receipt.json ``` Primary bindings: ```text T_ADMISSION lattice_forge.ledger.build_seed_database CMPLX-Kernel/lib-forge/part1_constants.py CMPLX-Kernel/lib-forge/part2_steps.... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 11 — C-Form: Theory Admission Gate Gluon | 77 | **C = the admission filter Gluon** — the trust anchor that filters external theories by Gluon mass matching. In the lattice_forge substrate, C is realized as the **admission gate** that: - Takes an external theory's Gluon mass (computed from its transport signature) - Compares against the master receipt Gluon (Paper 10) and the trusted Gluon spectrum from `CmplxLookupCache` - Admits if: `mass(theory) ∈ spectrum(trusted_Gluons)` and `mass(theory) ≤ K_max=9` - Outputs: `admitted` (Gluon mass matches), `boundary` (Gluon mass at K>9), `rejected` (no match) C is the **admission Gluon** — the filter that only passes theories with matching Gluon topology. - **Paper 20 (Layer-2 Synthesis Ledger):** ... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SUMMARY-II-Folded-Strand-Physics: Summary Paper II — Folded Strand Physics: The Gluon as Quark, Mass, Curvature, Tower, and Moonshine | 75 | This paper presents the **physics applications** of the Gluon formalism. We do not use the word "Gluon" because the fit is good. We use it because the substrate **IS** SU(3), and the physics IS the **standard model gauge theory in its algebraic / closed-form representation**. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SOURCE: Paper 11 - Theory Admission Gate | 71 | This paper admits external theories as transport candidates whose failures become boundary receipts rather than summary dismissals. An external theory enters by an encoder that maps its objects to a binary tape (the worked case is *bit-length parity* of a group order), after which the same `n = 3` SU(3) Weyl test is applied. The admission gate has three outlets: *admitted* (closes, `res^2 = 0`, idempotent), *boundary* (closes where the established theory does not, marking a `-1` boundary state), and *rejected-as-datum* (does not close under the declared encoder, logged as an open-encoder obligation rather than a dismissal). The load-bearing empirical case is the Pariah/Happy-Family inversion... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 10 — C-Form: T10 Master Receipt Gluon | 69 | **C = the master receipt Gluon** — the `LookupReceipt` that binds Papers 00-09 into a single inspectable, replayable causal unit. In the lattice_forge substrate, C is realized as the **master receipt** that: - Composes all 10 paper receipts into a single `LookupReceipt` via `CmplxLookupCache` - The master receipt's Gluon = the XOR of all 10 paper C-forms: `C_T10 = C₀ ⊕ C₁ ⊕ ... ⊕ C₉` - The master receipt certifies: every claim in 00-09 has a receipt, every obligation is logged, every transport is replayable C is the **master receipt Gluon** — the binding Gluon that makes the stack inspectable. - **Paper 11 (Theory Admission Gate):** The master receipt Gluon is the admission authority — only ... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-11_UPGRADED: Paper 11 - Theory Admission Gate (UPGRADED: Affirmative Encoder-Bound Filter Physics Map) | 69 | Paper 11 **proves the theory admission gate** for the CQECMPLX suite. An external theory is not admitted because it sounds compatible with the framework, and it is not discarded because a first transport attempt fails. It **is evaluated as a candidate** against the carried observer center, the Paper 10 master receipt, a trusted spectrum, and the `K=9` sheet boundary inherited from the lattice closure layer. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| additional routed cards |  | 14 more cards are listed in `ARCHIVE_EVIDENCE_CARD_MATRIX.json`. | Use during final body rewrite. |
## Journal Reader Guide

Read the formal paper as a journal manuscript with three layers:

1. The main argument states what this paper proves or routes.
2. The figures and tables show how the state moves through the ribbon.
3. The appendix/glossary/checklist make the claim boundaries reviewable.

For `FLCR-12`, the most important figure is `FLCR-12-F1`: State enumeration chart.
The most important table is `FLCR-12-T1`: State inventory table.
