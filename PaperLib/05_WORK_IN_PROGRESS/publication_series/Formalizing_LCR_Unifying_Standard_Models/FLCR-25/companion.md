# FLCR-25 Companion - Shear, Plasma, And Carrier Horizons

## What This Paper Is Doing

This paper formalizes shear and horizon events as carrier-level thresholds. The operative object is carrier horizon. The core result is that pinch, shear, and horizon conditions can be represented as internal carrier threshold events. The paper also defines how this result routes forward: FLCR-37 may use these thresholds for plasma/energy translation after measurement binding. Its main residue is explicit: measured Z-pinch observables, plasma identity, and laboratory calibration remain external.

In plainer terms: this paper defines one reliable piece of the LCR stack and
states exactly how later papers are allowed to use it. It is not trying to win
every downstream claim locally. It is making the local result strong enough
that later papers can build on it without changing what was proved.

## Strongest Claim

Theorem 25.1: pinch, shear, and horizon conditions can be represented as internal carrier threshold events

Lane: `cam_crystal_reapplication_result`.

## Why It Matters

- Defines carrier horizon as a first-class FLCR object.
- States the local result: pinch, shear, and horizon conditions can be represented as internal carrier threshold events.
- Routes downstream use through claim lanes rather than inherited prose: FLCR-37 may use these thresholds for plasma/energy translation after measurement binding.
- Preserves the residue boundary: measured Z-pinch observables, plasma identity, and laboratory calibration remain external.

## What It Does Not Claim Yet

- measured Z-pinch observables, plasma identity, and laboratory calibration remain external
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

Assigned original ribbon role(s): `26`/ledger_action.

The interpretive move in this paper must be presented as label management over
an already-addressed state. Where the paper changes language, it must say what
object remains invariant and what access path, label, or analogy changed.
## Narrative State Contract

The story obligation is to show why the received state naturally demands this
paper's transition:

```text
received state -> Shear, Plasma, And Carrier Horizons -> produced state
```

Received state: state emitted by prior slot 25 and reopened at original slot 26 (Z Pinch and Shear Horizon).

Produced state: formal result of original slot 26 plus the same-family lift path toward slot 36.

The companion should make the transition intelligible without treating metaphor
as proof. It may use the author's interpretation aggressively, but it must keep
the invariant object visible.
## Past Work Story Intake

This paper's story layer should explain how the older papers, supplements, and
crystal projections make the next state feel necessary rather than arbitrary.

For this slot, the narrative emphasis is:

Use past work to turn obligations into graph rows: event, observer, dependency, validator, falsifier, and next lane.

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
| Symbolic Carrier Versus Physical Carrier | `external_calibration_result` | Promote addressable symbolic-carrier and transport claims where the paper names carrier, path, residue, or traversal rules. | Map every physical carrier phrase to a standard physics object, Hamiltonian/model, dataset, or calibration route before treating it as measured physics. | Physical identity, units, material constants, and measured transport remain calibration-bound. |
## Delta Story

The human-readable story for this paper should present the deltas as honest
growth rather than contradiction. The earlier paper was correct at its local
time slice; the later evidence returns through a named lane and sharpens the
representation.

| Delta | Local claim at paper time | Later evidence | Revised representation | Boundary kept |
|---|---|---|---|---|
| Symbolic Vs Physical Carrier | This paper may use carrier language for addressable symbolic transport inside the LCR/CAM system. | Standard physics carrier terminology, local verifier receipts, material/plasma/transport supplements, and calibration routes. | Split symbolic carrier closure from measured physical carrier identity. | Physical identity, units, Hamiltonians, datasets, and measured constants remain external-calibration claims. |
## Archive Evidence Story Cards

These cards explain what older mirrors, toolkit supplements, claim contracts,
or formal variants add to this paper's story.

| Source card | Score | Contribution | Integration action |
|---|---:|---|---|
| FORMAL: Paper 23 — C-Form: FoldForge Protein Folding Gluon | 89 | **C = the protein fold Gluon** — the contact-map/topo Gluon that transports protein chain fold hypotheses through contact-map and topology receipts. In the lattice_forge substrate, C is realized as the **fold Gluon** that: - The fold Gluon = the `foldforge` transport operator - Each fold hypothesis = a ribbon path with contact-map receipts (tempus fugit) - The fold transport = `fold_{n+1} = foldforge_hypothesis(fold_n, contact_map)` - The fold Gluon's topology = the contact-map persistent homology barcode - The fold Gluon's topology receipt = the homology barcode certificate C is the **fold Gluon** — the contact-map/topo Gluon for protein folding. - **Paper 24 (KnightForge):** The chess Gluo... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-26.25: Paper 26.25 - Z-Pinch and Shear Toolkit Supplement | 85 | This supplement shows how to reproduce Paper 26's carrier and shear receipt. The proof is in Paper 26 and its formal verifier; the physical Z-pinch reading is not discharged here. Run: `python production/formal-papers/CQE-paper-26/verify_zpinch_shear_horizon.py` The expected status is `pass_with_open_obligations`. The verifier checks the integer Oloid period, octonion period, octonion non-associativity, the 16-bit Rule 30 carrier shear probe, and the transport-ledger pinch classification. Draw a four-position rolling strip. Advance one quarter turn per tape bit and record sheet, phase, and parity. Beside it, draw two orient threads, one for the `e4` carrier and one for the `e5` carrier. Mark... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| SUMMARY-III-Computational-Substrates: Summary Paper III — Computational Substrates: The Gluon as Fold, Knight, Traversal, Pinch, Delay, Game, Monster | 83 | This paper presents the **computational substrate applications** of the Gluon formalism. We do not use the word "Gluon" because the fit is good. We use it because the substrate **IS** SU(3), and the computational substrates ARE **specialized gluon field configurations** in different physical regimes. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 25 — C-Form: Energetic Traversal Maps Gluon | 81 | **C = the traversal energy Gluon** — the energy/ledger Gluon that adds energy and traversal costs to cross-language, figure, material, and fold transformations. In the lattice_forge substrate, C is realized as the **traversal Gluon** that: - The traversal Gluon = the `paper25_traversal_maps` transport operator - Each transformation = a traversal path with energy cost ledger - The traversal transport = `traversal_{n+1} = energetic_map(transformation_n, energy_budget)` - The traversal Gluon's energy = the accumulated energy cost along the path - The traversal Gluon's ledger = the energy/oblivion ledger (energy in, entropy out) C is the **traversal Gluon** — the energy/ledger Gluon for cross-do... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| CQE-paper-26: Paper 26 - Z-Pinch and Shear Horizon | 81 | Paper 26 states the CQECMPLX Z-pinch/shear physics map at the carrier layer. Its closed content is the Oloid/octonion carrier algebra and a ledger definition of pinch/shear as an analog boundary event. This is a valid internal pinch/shear model. Magnetic confinement, friction, plasma collapse, and energy-generation claims require an external observable bridge. | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| FORMAL: Paper 24 — C-Form: KnightForge / N-Dimensional Chess Automata Gluon | 77 | **C = the chess automata Gluon** — the L-conjugate CA Gluon that generalizes knight moves to N-dimensional board operators. In the lattice_forge substrate, C is realized as the **chess Gluon** that: - The chess Gluon = the `knightforge` transport operator - Each piece = a ribbon state with move-set Gluon - The knight's L-move = the L-conjugate move in the 8-state shell=2 stratum - The N-dimensional board = the powered lattice code chain (1→9→49→72) - The move-set Gluon = the piece's allowed transition matrix C is the **chess Gluon** — the L-conjugate CA Gluon for N-dimensional automata. - **Paper 25 (Energetic Traversal):** The chess Gluon's move energy = the traversal Gluon's cost. - **Pape... | keep this as supplement evidence unless it upgrades a specific spine-paper claim status with a receipt-backed boundary. |
| additional routed cards |  | 14 more cards are listed in `ARCHIVE_EVIDENCE_CARD_MATRIX.json`. | Use during final body rewrite. |
## Journal Reader Guide

Read the formal paper as a journal manuscript with three layers:

1. The main argument states what this paper proves or routes.
2. The figures and tables show how the state moves through the ribbon.
3. The appendix/glossary/checklist make the claim boundaries reviewable.

For `FLCR-25`, the most important figure is `FLCR-25-F1`: Causal/obligation ledger graph.
The most important table is `FLCR-25-T1`: Obligation ledger table.
