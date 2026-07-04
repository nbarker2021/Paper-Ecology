# Paper 28 - N-Dimensional Game Lattices

**Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data.

**Method:** preserve the strongest representation of each source face; when
sources disagree, keep the disagreement as a named boundary or next-need.

---

## Source Faces

| Face | Path | Words / count | Contribution |
|------|------|---------------|--------------|
| Current rework | `D:\Paper Reworks\28_N_Dimensional_Game_Lattices.md` | 503 words | Existing skeleton, current status, obligations. |
| Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-28\FORMAL_PAPER.md` | 911 words | Main theorem, proof, receipt, falsifier spine. |
| Companion variant | `CQE-paper-28.25.md` | 198 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-28.50.md` | 191 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-28.75.md` | 160 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-28_UPGRADED.md` | 1049 words | Alternate toolkit/contract/bridge phrasing. |
| Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-28` | 5 files | Executable evidence surface. |
| Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-28` | 6 files | Receipt status and check counts. |
| Saved CAM nodes | `D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json` | 1 relevant nodes | Prior crystal evidence and obligation nodes. |
| Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant rows | Closure/partial-closure status updates. |

## Virtuous Synthesis

Paper 28 defines a local-rule game lattice as a finite chart operator. A game
piece reads a local `(L, C, R)` neighborhood, emits a Rule 30-style occupancy
bit, moves through an S3 trace-2 orbit, logs forbidden carriers as residue, and
anneals to a Lie-conjugate state in at most three steps.

This version treats the formal paper as the proof spine, the companion variants as interface contracts, and the CAM/GLM rows as status-bearing crystal data. The paper's open obligations are not deleted; they are the next work items required before stronger claims can be promoted.

## Companion Face Digest

- **Paper 28.25 - N-Dimensional Game Lattice Toolkit Supplement.** This supplement shows how to reproduce Paper 28's local-rule game-lattice
receipt. The proof is in Paper 28 and its formal verifier; full game solving
is not claimed.
- **Paper 28.50 - N-Dimensional Game Lattice Claim Contract.** This contract defines the minimum fields required before a game-lattice claim
can be promoted.
- **Paper 28.75 - N-Dimensional Game Lattice Next-State Precondition.** This supplement defines what Paper 28 exports to later applied tools.
- **Paper 28 - N-Dimensional Game Lattices (UPGRADED: Affirmative Local-Rule Game Lattice Physics Map).** (Affirmative)

## Receipt Surface

| Receipt | Summary |
|---------|---------|
| `conway_glider_oloid_receipt.json` | status=pass; checks=6/6 |
| `glider_collision_cascade_receipt.json` | status=pass; checks=6/6 |
| `gosper_gun_emitter_receipt.json` | status=pass; checks=6/6 |
| `nd_game_lattices_receipt.json` | status=pass_with_open_obligations |
| `ndim_knight_ca_affirmed_receipt.json` | status=pass; checks=5/5 |
| `calibration_plan.json` | status=formula_verified_oeis_query_ready |

## Open Obligations as Next Needs

| ID | Current row | CAM/GLM status |
|----|-------------|----------------|
| `28.1` | \| 28.1 \| General N-dimensional game solver \| Later applied paper \| | carry as next need |
| `28.2` | \| 28.2 \| Non-code-tower dimensions (dimension 5 rejected) \| Out of scope / documented \| | carry as next need |
| `28.3` | \| 28.3 \| Real game-piece geometry per piece type \| Tooling \| | carry as next need |
| `28.4` | \| 28.4 \| Complete game theory (strategy, termination, winning, fairness) \| External / later paper \| | carry as next need |
| `28.5` | \| 28.5 \| OEIS identity \| External verification \| | carry as next need |

## Obligation Springboard Lanes

Obligations return to the earliest paper they can affect, then rework upward through each paper in the lane before the local claim is promoted.

### Local Claim Pressure

- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.
- Engineering and adapter gaps should be promoted to work items, not used as theorem premises.

### Local Lane Table

| Obligation | Return start | Upward lane | Rework instruction |
|------------|--------------|-------------|--------------------|
| `28.1` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28.2` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28.3` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `28.4` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `28.5` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |

## Detailed Expansion Pass

### Paper-Level Thesis

Paper 28 functions as the suite's N-dimensional game-lattice applied surface. Its virtuous version should therefore make three layers visible at once: the formal claim that is actually proved, the receipt or verifier evidence that lets the claim be replayed, and the explicit boundary that prevents the reader from promoting an open lift into a closed theorem.

The companion variants are used as exposition and interface contracts. They may contribute terminology, examples, and downstream preconditions, but the canonical formal paper remains the proof spine.

### Claim Status Ledger

No explicit claim/theorem lines were extracted from the formal spine. Use the abstract, proof, receipts, and obligation table to reconstruct the claim ledger before publication.

### Evidence and Receipt Detail

The receipt surface should be discussed in prose, not only listed. Passing receipts make the paper replayable; failed, partial, or missing checks become local boundaries.
- `conway_glider_oloid_receipt.json`: status=pass; checks=6/6.
- `glider_collision_cascade_receipt.json`: status=pass; checks=6/6.
- `gosper_gun_emitter_receipt.json`: status=pass; checks=6/6.
- `nd_game_lattices_receipt.json`: status=pass_with_open_obligations.
- `ndim_knight_ca_affirmed_receipt.json`: status=pass; checks=5/5.
- `calibration_plan.json`: status=formula_verified_oeis_query_ready.
Verifier files are the strongest executable surface. The paper should name the verifier next to any claim it supports.
- `verify_conway_glider_oloid.py` should be mapped to the claim or obligation it checks.
- `verify_glider_collision_cascade.py` should be mapped to the claim or obligation it checks.
- `verify_gosper_gun_emitter.py` should be mapped to the claim or obligation it checks.
- `verify_nd_game_lattices.py` should be mapped to the claim or obligation it checks.
- `verify_ndim_knight_ca_affirmed.py` should be mapped to the claim or obligation it checks.

### Obligation Workups

**28.1.** | 28.1 | General N-dimensional game solver | Later applied paper |

- **Status reading:** open next-need.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`.
- **Paper-local consequence:** Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
- **Rewrite requirement:** leave the item live as the next verifier, witness, adapter, calibration, or documentation pass.
- **Upward effect:** Papers in the lane must preserve the `N-dimensional game-lattice applied surface` boundary before this obligation can strengthen the source paper.

**28.2.** | 28.2 | Non-code-tower dimensions (dimension 5 rejected) | Out of scope / documented |

- **Status reading:** open next-need.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`.
- **Paper-local consequence:** Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
- **Rewrite requirement:** leave the item live as the next verifier, witness, adapter, calibration, or documentation pass.
- **Upward effect:** Papers in the lane must preserve the `N-dimensional game-lattice applied surface` boundary before this obligation can strengthen the source paper.

**28.3.** | 28.3 | Real game-piece geometry per piece type | Tooling |

- **Status reading:** requires tooling/adapter work before theorem use.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`.
- **Paper-local consequence:** Route this into tooling or adapter work before using it as a premise in the paper's theorem.
- **Rewrite requirement:** turn the gap into an adapter/tooling task and avoid depending on it as a completed premise.
- **Upward effect:** Papers in the lane must preserve the `N-dimensional game-lattice applied surface` boundary before this obligation can strengthen the source paper.

**28.4.** | 28.4 | Complete game theory (strategy, termination, winning, fairness) | External / later paper |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `N-dimensional game-lattice applied surface` boundary before this obligation can strengthen the source paper.

**28.5.** | 28.5 | OEIS identity | External verification |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `N-dimensional game-lattice applied surface` boundary before this obligation can strengthen the source paper.

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
- Paper 24: KnightForge combinatorial-game surface.
- Paper 25: energetic traversal and unit-calibration bridge.
- Paper 26: Z-pinch/shear-horizon physical-witness bridge.
- Paper 27: observer-delay/shared-reality guard layer.
- Paper 28: N-dimensional game-lattice applied surface.

### Publication-Grade Rewrite Targets

For the next manual/editorial pass, expand the paper body around these targets:

1. Put the strongest closed theorem in the opening synthesis, then immediately state the largest thing it does not prove.
2. Move every calibration, physical-identification, and external-validation claim into a guarded paragraph with its required witness named.
3. Place verifier and receipt names beside the exact claims they support.
4. Preserve open lifts as first-class obligations rather than treating them as editorial TODOs.


## Canonical Formal Spine

## Abstract

Paper 28 defines a local-rule game lattice as a finite chart operator. A game
piece reads a local `(L, C, R)` neighborhood, emits a Rule 30-style occupancy
bit, moves through an S3 trace-2 orbit, logs forbidden carriers as residue, and
anneals to a Lie-conjugate state in at most three steps.

The closed result is constructive and bounded. The verifier proves the forced
code-tower dimensions `{1,3,7,8,24,72}`, checks the dimension-8 extended
Hamming board, enumerates a six-row S3 move orbit for a robot on the dimension
8 board, logs one forbidden straight carrier, and confirms that all orbit rows
close under centroid annealing. The paper does not claim to solve chess, Go,
arbitrary games, arbitrary dimensions, or any complete game-theoretic problem.

## Closed Evidence

The receipt is generated by
`production/formal-papers/CQE-paper-28/verify_nd_game_lattices.py`. It imports
the live `lattice_codes`, `centroid_voa`, `f4_action`, and `rule30` package
surfaces.

`verify_lattice_code_chain` passes. Its forced dimensions are `1`, `3`, `7`,
`8`, `24`, and `72`; the powered shortcut is `1`, `9`, `49`, and `72`; and the
sheet-K bound is `9`.

`verify_extended_hamming_8` passes with 16 codewords, minimum weight 4, and
weight distribution `{0:1, 4:14, 8:1}`. This supplies the worked board's
dimension-8 lattice surface.

The finite robot example starts at chart state `(1,0,1)`. The S3 move orbit has
six rows and three unique target states: `(0,1,1)`, `(1,0,1)`, and `(1,1,0)`.
Five rows are legal orbit moves and one identity carrier is logged as
forbidden. Every row closes to a Lie-conjugate state in at most three anneal
steps.

## Definitions

A local-rule game is a finite receipt `(lattice, neighborhood, move rule,
obligation ledger)`. The move rule reads a local `(L, C, R)` chart state and
emits an occupancy bit.

An admissible dimension is one of the verified code-tower dimensions
`{1,3,7,8,24,72}`. A game on another dimension may exist as a candidate, but it
does not inherit this proof surface without its own verifier.

A move orbit is the set of trace-2 states produced by the six S3 permutations.
Repeated target states are retained in the receipt because they came from
different group elements.

A forbidden carrier is a move row that the game policy excludes. It is logged
as a constraint, not deleted.

A closed game solver claim is a claim about strategy, termination, winning
states, fairness, or complete game solution. This paper does not make such a
claim.

## Claims

1. The verified code-tower dimensions define admissible game-lattice surfaces.

2. Dimension 8 is a valid worked board through the extended Hamming verifier.

3. A trace-2 S3 orbit supplies a finite move surface for a local-rule piece.

4. Rule 30 local emission gives each orbit row a replayable occupancy bit.

5. Forbidden carriers can be logged without deleting the move receipt.

6. Every chart row in the receipt closes to a Lie-conjugate attractor in at
most three steps.

7. General game solving and real-game strategy are open obligations.

## Theorem 28

An N-dimensional game lattice is valid in the CQE kernel when it is presented
as a finite local-rule receipt on an admissible code-tower dimension: the move
orbit is enumerated, emissions are replayable, forbidden carriers are logged,
and every row carries its closure or obligation status.

## Proof

The dimension claim follows from `verify_lattice_code_chain`. The verifier
passes every layer of the chain and returns the forced dimension set
`{1,3,7,8,24,72}`. This proves that the game board dimensions used here are
not arbitrary choices inside this kernel.

The worked-board claim follows from `verify_extended_hamming_8`. The
dimension-8 board has the expected extended Hamming parameters: 16 codewords,
minimum weight 4, and weight distribution `{0:1, 4:14, 8:1}`.

The move-orbit claim follows from `S3_PERMUTATIONS` and the trace-2 state map.
Starting from `(1,0,1)`, the six S3 elements produce six receipt rows and three
unique target states. The identity row is marked `forbidden_logged`; it remains
in the receipt as a constraint. The other five rows are legal orbit moves.

The emission claim follows from `rule30_bit` applied to every target state. The
closure claim follows from `anneal_to_lie_conjugate`: the maximum anneal count
in the worked receipt is three, and the global centroid closure verifier also
passes over all eight chart states. Therefore the local-rule game lattice is
closed as a finite receipt.

Nothing in the receipt evaluates strategy, game termination, winning states,
or arbitrary real-piece geometry. Those are therefore obligations, not hidden
claims.

## Worked Example

The worked example is a dimension-8 robot with forbidden straight carriers.
The active state is `(1,0,1)`. Its legal surface is the S3 orbit of the trace-2
state. The identity carrier is disallowed by policy and logged. The remaining
five orbit rows are available moves. Each row records the permutation, target
state, Rule 30 emitted bit, anneal count, final attractor, and carrier status.

This is enough to prove a local-rule game-lattice receipt. It is not enough to
solve a game.

## Open Obligations

The general N-dimensional game solver is not claimed. The receipt proves finite
orbit closure, not arbitrary solvability.

Non-code-tower dimensions remain open. Dimension 5 is explicitly rejected by
the verifier as outside the inherited proof surface.

Real game-piece geometry remains open. Each piece type needs its own map into
the trace-2/S3 orbit.

Complete game theory remains open. Legal move receipts do not prove strategy,
termination, winning states, or fairness.

## Suite Role

Paper 28 extends Paper 24's board automata into a reusable local-rule game
receipt. It gives the suite a controlled way to talk about game-like systems,
CAD constraints, robot movement, and search surfaces without pretending that a
finite move receipt is a complete solver.

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
| `external_calibration` | 3 |
| `open_next_need` | 3 |
| `claim_guard` | 2 |
| `engineering_gap` | 2 |
| `closed_receipt` | 1 |
| `receipt_integrity` | 1 |

### Routed Lanes

| Source | Obligation | Full lane | Required local action |
|--------|------------|-----------|-----------------------|
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
