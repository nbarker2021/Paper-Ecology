# Paper 24 - KnightForge / N-Dimensional Chess Automata

**Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data.

**Method:** preserve the strongest representation of each source face; when
sources disagree, keep the disagreement as a named boundary or next-need.

---

## Source Faces

| Face | Path | Words / count | Contribution |
|------|------|---------------|--------------|
| Current rework | `D:\Paper Reworks\24_KnightForge_N_Dimensional_Chess_Automata.md` | 427 words | Existing skeleton, current status, obligations. |
| Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-24\FORMAL_PAPER.md` | 788 words | Main theorem, proof, receipt, falsifier spine. |
| Companion variant | `CQE-paper-24.25.md` | 186 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-24.50.md` | 231 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-24.75.md` | 155 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-24_UPGRADED.md` | 896 words | Alternate toolkit/contract/bridge phrasing. |
| Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-24` | 1 files | Executable evidence surface. |
| Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-24` | 1 files | Receipt status and check counts. |
| Saved CAM nodes | `D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json` | 1 relevant nodes | Prior crystal evidence and obligation nodes. |
| Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant rows | Closure/partial-closure status updates. |

## Virtuous Synthesis

Paper 24 registers greedy non-attacking knight placement as a local-rule
cellular-automaton receipt whose states close under the L-conjugate centroid
structure. The chessboard is the concrete shadow of the proof. The proof itself
is the finite chart result: all `(L, C, R)` states anneal to one of four `L = R`
attractors in at most three S3 transposition steps, and the same chart states
split into the `2 + 6` VOA sector pattern.

This version treats the formal paper as the proof spine, the companion variants as interface contracts, and the CAM/GLM rows as status-bearing crystal data. The paper's open obligations are not deleted; they are the next work items required before stronger claims can be promoted.

## Companion Face Digest

- **Paper 24.25 - KnightForge Toolkit Supplement.** This supplement shows how to reproduce the KnightForge receipt. The proof is in
Paper 24 and its formal verifier; this file holds the tool and analog handling.
- **Paper 24.50 - KnightForge Claim Contract.** # Paper 24.50 - KnightForge Claim Contract ## Admission Rule A Paper 24 claim is admitted only when it is framed as a finite local-rule automaton or a frame operator unless a stronger game-theoretic proof is attached. The receipt must preserve occupied rows, rejected rows, local states, anneal trajectories, sector labels, and open obligations. ## Required Fields Each admitted board row must provide: - board size or lattice domain, - sweep order, - cell identifier, - `L`, `C`, and `R` bits, - occupancy or rejection decision, - attack/exclusion evidence, - side label, - L-conjugate attractor, - anneal step count, - frame label or reason absent, - closure status. ## Rejected Promotions The following promotions are not allowed: - finite greedy placement to solved chess, - frame operator to playable N-dimensional game, - board sequence to OEIS identity without search evidence, - chart sector 
- **Paper 24.75 - KnightForge Next-State Bridge.** # Paper 24.75 - KnightForge Next-State Bridge ## Bridge Role Paper 24 exports a local-rule board automaton. The next state receives a way to turn board moves into replayable `(L, C, R)` rows with closure receipts. It does not receive solved games. ## Exported Artifacts The next state receives: - finite board sweep order, - local exclusion rows, - occupied/rejected row accounting, - L-conjugate anneal receipts, - `2 + 6` sector labels, - N-dimensional frame-operator boundary, - invalid-promotion labels. ## Use in Paper 25 Paper 25 may treat occupied moves, rejected moves, and frame labels as traversal cost rows. It must still prove its own energy or action ledger. ## Use in Paper 28 Paper 28 may extend the board-local rule to broader game lattices. It must separate finite reachability proof from general game solvability. ## Boundary Paper 24 exports board-automata closure. It does not exp
- **Paper 24 - KnightForge / N-Dimensional Chess Automata (UPGRADED: Affirmative Board Automaton Physics Map).** (Affirmative)

## Receipt Surface

| Receipt | Summary |
|---------|---------|
| `knightforge_ca_receipt.json` | status=pass_with_open_obligations |

## Open Obligations as Next Needs

| ID | Current row | CAM/GLM status |
|----|-------------|----------------|
| `24.1` | \| 24.1 \| OEIS identity \| External verification \| | carry as next need |
| `24.2` | \| 24.2 \| N-dimensional playability \| Later applied paper \| | carry as next need |
| `24.3` | \| 24.3 \| Placement-class relation to `2+6` sector split \| Later formal paper \| | carry as next need |
| `24.4` | \| 24.4 \| Combinatorial-game expert review \| Peer review \| | carry as next need |

## Obligation Springboard Lanes

Obligations return to the earliest paper they can affect, then rework upward through each paper in the lane before the local claim is promoted.

### Local Claim Pressure

- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.

### Local Lane Table

| Obligation | Return start | Upward lane | Rework instruction |
|------------|--------------|-------------|--------------------|
| `24.1` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `24.2` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `24.3` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `24.4` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |

## Detailed Expansion Pass

### Paper-Level Thesis

Paper 24 functions as the suite's KnightForge combinatorial-game surface. Its virtuous version should therefore make three layers visible at once: the formal claim that is actually proved, the receipt or verifier evidence that lets the claim be replayed, and the explicit boundary that prevents the reader from promoting an open lift into a closed theorem.

The companion variants are used as exposition and interface contracts. They may contribute terminology, examples, and downstream preconditions, but the canonical formal paper remains the proof spine.

### Claim Status Ledger

No explicit claim/theorem lines were extracted from the formal spine. Use the abstract, proof, receipts, and obligation table to reconstruct the claim ledger before publication.

### Evidence and Receipt Detail

The receipt surface should be discussed in prose, not only listed. Passing receipts make the paper replayable; failed, partial, or missing checks become local boundaries.
- `knightforge_ca_receipt.json`: status=pass_with_open_obligations.
Verifier files are the strongest executable surface. The paper should name the verifier next to any claim it supports.
- `verify_knightforge_ca.py` should be mapped to the claim or obligation it checks.

### Obligation Workups

**24.1.** | 24.1 | OEIS identity | External verification |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `KnightForge combinatorial-game surface` boundary before this obligation can strengthen the source paper.

**24.2.** | 24.2 | N-dimensional playability | Later applied paper |

- **Status reading:** open next-need.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`.
- **Paper-local consequence:** Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
- **Rewrite requirement:** leave the item live as the next verifier, witness, adapter, calibration, or documentation pass.
- **Upward effect:** Papers in the lane must preserve the `KnightForge combinatorial-game surface` boundary before this obligation can strengthen the source paper.

**24.3.** | 24.3 | Placement-class relation to `2+6` sector split | Later formal paper |

- **Status reading:** open next-need.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`.
- **Paper-local consequence:** Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
- **Rewrite requirement:** leave the item live as the next verifier, witness, adapter, calibration, or documentation pass.
- **Upward effect:** Papers in the lane must preserve the `KnightForge combinatorial-game surface` boundary before this obligation can strengthen the source paper.

**24.4.** | 24.4 | Combinatorial-game expert review | Peer review |

- **Status reading:** open next-need.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`.
- **Paper-local consequence:** Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
- **Rewrite requirement:** leave the item live as the next verifier, witness, adapter, calibration, or documentation pass.
- **Upward effect:** Papers in the lane must preserve the `KnightForge combinatorial-game surface` boundary before this obligation can strengthen the source paper.

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

### Publication-Grade Rewrite Targets

For the next manual/editorial pass, expand the paper body around these targets:

1. Put the strongest closed theorem in the opening synthesis, then immediately state the largest thing it does not prove.
2. Move every calibration, physical-identification, and external-validation claim into a guarded paragraph with its required witness named.
3. Place verifier and receipt names beside the exact claims they support.
4. Preserve open lifts as first-class obligations rather than treating them as editorial TODOs.


## Canonical Formal Spine

## Abstract

Paper 24 registers greedy non-attacking knight placement as a local-rule
cellular-automaton receipt whose states close under the L-conjugate centroid
structure. The chessboard is the concrete shadow of the proof. The proof itself
is the finite chart result: all `(L, C, R)` states anneal to one of four `L = R`
attractors in at most three S3 transposition steps, and the same chart states
split into the `2 + 6` VOA sector pattern.

The paper does not solve chess, N-dimensional chess, or any named OEIS sequence.
It proves the CA receipt and the frame-operator lift. Playability, sequence
identity, and full combinatorial-game meaning remain obligations.

## Closed Evidence

The verifier calls the promoted `centroid_voa.py` substrate. The Hamming
centroid verifier passes, giving four L-conjugate attractors:
`(0,0,0)`, `(0,1,0)`, `(1,0,1)`, and `(1,1,1)`. Every chart state closes to
that plane in at most three steps. The sector verifier passes with partition
`Z(q) = 2q^0 + 6q^5`, two weight-zero vacua and six weight-five excited states.
The centroid chain verifier also passes with two fixed points and six period-4
states.

The local greedy-knight verifier sweeps an 8 by 8 board in numbered
boustrophedon order. At each cell it records the opposed knight-approach bits
`L` and `R`, the occupancy decision `C`, the side label `R - L`, the
L-conjugate attractor, the anneal step count, the three-conjugate frame label,
and the VOA weight. The finite board receipt is deterministic, has occupied and
rejected rows, has no attacking occupied pairs, and every row closes to an
L-conjugate in at most three steps.

## Definitions

A placement state is a local triple `(L, C, R)`. `C` is the current cell's
occupancy decision. `L` and `R` are opposed approach bits determined by whether
earlier placed knights attack the current cell from the left-approach or
right-approach L-move families. A rejection is a data row, not a deletion.

An L-conjugate state is a state with `L = R`. A frame operator is a tuple of
three-conjugate labels assigned to board axes or move axes. It is an operator
definition, not a proof of a complete game.

## Claims

1. The L-conjugate attractor structure closes.

The centroid substrate proves that all eight chart states reach the four
`L = R` attractors in at most three S3 transposition steps.

2. The chart sectors split as `2 + 6`.

The VOA sector verifier returns `Z(q) = 2q^0 + 6q^5`: two true vacua and six
excited states.

3. A finite greedy knight board can be represented as a local-rule CA receipt.

The verifier sweeps a finite numbered board, emits one row per cell, records
occupied and rejected decisions, and verifies that the occupied set is
non-attacking.

4. The board receipt inherits L-conjugate closure.

Every emitted row carries an `(L, C, R)` state and an annealing receipt. The
maximum step count is at most three.

5. The N-dimensional lift is a frame operator.

The verifier constructs a finite frame-operator row for four axes. It does not
claim that this row is a playable, terminating, or strategically meaningful
N-dimensional chess game.

## Theorem 24

KnightForge is a valid CQE board-automata kernel when it returns a replayable
finite placement receipt whose local states close under L-conjugate centroid
annealing and whose N-dimensional extension is explicitly labeled as a frame
operator rather than a solved game.

## Proof

Run `verify_knightforge_ca.py`. The first three checks verify the substrate:
the L-conjugate closure, the `2 + 6` sector split, and the centroid chain. These
checks prove the chart structure used by the board receipt.

The fourth check constructs the finite greedy knight board. The receipt is
accepted only if the sweep covers all board cells, produces both occupied and
rejected rows, and leaves no occupied pair connected by a knight attack. This
establishes the local-rule CA shadow of the chess example.

The fifth check applies the centroid closure to every board row. A failed
anneal, or a row requiring more than three steps, would falsify the claim that
the board receipt is carried by the L-conjugate chart structure.

The final check builds the N-dimensional frame operator and verifies that it is
not represented as a closed game claim. Thus the paper proves the finite CA and
frame-lift receipt while carrying the game-theoretic obligations.

## Receipt

The formal receipt is generated at:

`production/formal-papers/CQE-paper-24/knightforge_ca_receipt.json`

## Open Obligations

OEIS identity remains open. N-dimensional playability remains open. The
placement-class relation to the `2 + 6` sector split remains open beyond the
local chart receipt. Combinatorial-game expert review remains open.

## Suite Role

Paper 23 supplies the chain/path descriptor discipline. Paper 24 applies that
discipline to board automata. Paper 25 may reuse the board receipt as a
move-cost or traversal ledger, while Paper 28 may develop broader game lattices.

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
| `external_calibration` | 13 |
| `open_next_need` | 6 |
| `claim_guard` | 5 |
| `engineering_gap` | 3 |
| `closed_receipt` | 1 |
| `receipt_integrity` | 1 |

### Routed Lanes

| Source | Obligation | Full lane | Required local action |
|--------|------------|-----------|-----------------------|
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
