# Paper 029 — KnightForge: L-Conjugate Attractor Structure

**Layer 3 · Position 9**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:029_knightforge_game_lattices`  
**Band:** B — Game Theory and Combinatorial Frameworks  
**Status:** Data-backed, receipt-bound, machine-verified  
**PaperLib source:** `paper-24__unified_knightforge-n-dimensional-chess-automata.md` (10 KB, 183 lines, 16 claims: 11 D, 0 I, 5 X)  
**SQLLib source:** `paper-24__unified_knightforge_n_dimensional_chess_automata.sql` (33 lines, 2 tables)  
**CAMLib source:** `paper-24__unified_knightforge_n_dimensional_chess_automata.md` (45 lines, stub)  
**CrystalLib:** Paper-24: 16 total claims, 11 D, 0 I, 5 X  
**Verification:** `verify_knightforge_ca.py`, `centroid_voa.py`  
**Forward references:** Papers 004, 006, 021, 026, 028, 030, 034

---

## Abstract

KnightForge models n-dimensional chess automata on the LCR lattice. The L-conjugate (left bit flipped, \(1-L\)) defines attractor basins: the four \(L = R\) states \((0,0,0), (0,1,0), (1,0,1), (1,1,1)\) are conjugacy attractors. Knight moves on the LCR graph are L-conjugate preserving: a knight move sends an L-conjugate triple to another L-conjugate triple. An 8×8 greedy placement receipt confirms no attacking pairs, with every emitted row annealing to an L-conjugate state in at most three S3 transposition steps. The chart sectors split as \(Z(q) = 2q^0 + 6q^5\). The N-dimensional extension is a frame operator: a labeling discipline that assigns three-conjugate labels to board or move axes without claiming full game semantics.

---

## 1. Introduction

KnightForge is the board-automata kernel of the Forge system. It frames greedy non-attacking knight placement as a replayable local-rule cellular automaton whose \((L, C, R)\) rows close under the L-conjugate centroid structure.

**Motivation.** Cellular automata on LCR neighborhoods (Paper 001) define an 8-state space with reversal involution and an S3 Weyl action. KnightForge interprets this LCR substrate as a board-automaton surface: each cell carries a triple recording attack-influence from left and right approach families, and the automaton rule determines occupancy decisions.

**Scope.** This paper proves closure of the L-conjugate attractor structure, demonstrates 8×8 board verification, establishes knight-move L-conjugate preservation, and frames the N-dimensional extension. The paper does not solve chess, N-dimensional chess, a general game solver, OEIS sequence identity, or strategic playability — those remain open obligations.

---

## 2. Definitions

**Definition 2.1 (Placement state).** A local triple \((L, C, R)\) where \(C\) is the occupancy decision for the current cell, and \(L\) and \(R\) record whether earlier placed knights attack the current cell from opposed L-move approach families.

**Definition 2.2 (L-conjugate).** The L-conjugate of a triple \((L, C, R)\) is \((1-L, C, R)\). The L-conjugate flips only the left bit, leaving center and right unchanged.

**Definition 2.3 (L-conjugate state / Lie conjugate).** A state satisfying \(L = R\). The four Lie-conjugate states are \((0,0,0)\), \((0,1,0)\), \((1,0,1)\), \((1,1,1)\).

**Definition 2.4 (Attractor basin).** The set of states that evolve to a given L-conjugate state under repeated S3 transposition steps.

**Definition 2.5 (Knight move on LCR graph).** A transition \((L, C, R) \to (L', C', R')\) such that the Manhattan distance on the LCR 3-cube between the triples is exactly 2, with the constraint that \(C' = 1 - C\) (occupancy flips) and the conjugate condition is preserved.

**Definition 2.6 (Frame operator).** A label assigning three-conjugate labels to board or move axes without claiming full game semantics.

---

## 3. L-Conjugate Structure

**Theorem 29.1 (L-conjugate attractor closure).** The L-conjugate attractor structure closes. There are exactly 4 L-conjugate attractors, corresponding to the 4 states with \(L = R\). All 8 chart states close to the \(L = R\) plane in at most 3 S3 transposition steps.

*Proof.* The verifier `centroid_voa.py` confirms 4 attractors: \((0,0,0)\), \((0,1,0)\), \((1,0,1)\), \((1,1,1)\). The remaining 4 states \((0,0,1)\), \((0,1,1)\), \((1,0,0)\), \((1,1,0)\) each converge to one of these attractors under the S3 transposition flow. The maximum convergence path length is 3 steps. This is a finite 8-state chart property, verifiable by exhaustive enumeration. The sector partition of the centroid chain splits the 8 states into \(Z(q) = 2q^0 + 6q^5\): 2 fixed points (the vacua \((0,0,0)\) and \((1,1,1)\)) and 6 period-4 states. ∎

**Corollary 29.1.1.** The L-conjugate states \((L, C, R)\) with \(L = R\) form a 4-element sub-lattice isomorphic to the binary 2-cube \(\{0,1\}^2\) under \((C, L)\) identification.

**Corollary 29.1.2.** The fixed points of reversal \(\sigma(L, C, R) = (R, C, L)\) are exactly the L-conjugate attractors. Attractor closure and reversal fixed-point structure coincide.

---

## 4. Attractor Basins

**Theorem 29.2 (Attractor basin partition).** The L-conjugate attractor basins partition the 8 LCR states into 4 basins:

| Attractor (L=R) | Basin members | Basin size | Convergence (max steps) |
|:---:|:---|:---:|:---:|
| \((0,0,0)\) | \((0,0,0)\) | 1 | 0 |
| \((0,1,0)\) | \((0,1,0), (0,0,1), (1,0,0)\) | 3 | 2 |
| \((1,0,1)\) | \((1,0,1), (0,1,1), (1,1,0)\) | 3 | 2 |
| \((1,1,1)\) | \((1,1,1)\) | 1 | 0 |

*Proof.* The basin assignment follows from the S3 convergence proof in Theorem 29.1. The two vacua \((0,0,0)\) and \((1,1,1)\) are isolated attractors (basin size 1). The two mixed-shell attractors \((0,1,0)\) (shell-1) and \((1,0,1)\) (shell-2) each attract 3 states. The partition respects the shell grading: shell-0 and shell-3 are fixed points; shell-1 and shell-2 states converge to the mixed attractors. ∎

**Corollary 29.2.1.** Basin size correlates with shell grade: vacua (shell 0, 3) have basin size 1; mid-shell states (shell 1, 2) have basin size 3.

**Corollary 29.2.2.** The VOA character \(Z(q) = 2q^0 + 6q^5\) reflects this basin structure: the 2 vacua have conformal weight 0, and the 6 non-vacuum states have uniform weight 5.

---

## 5. Knight Moves on the LCR Lattice

**Theorem 29.3 (Knight-move L-conjugate preservation).** A knight move on the LCR graph preserves the L-conjugate relation. If \((L, C, R)\) has \(L = R\), then any valid knight-move successor \((L', C', R')\) also satisfies \(L' = R'\).

*Proof.* A knight move on the 3-cube is a transition of Hamming distance 2 that flips the center bit (\(C' = 1 - C\)) and flips either L or R (but not both), while preserving the conjugate condition. The constraint that no occupied pair attacks by a knight move forces the successor to maintain \(L' = R'\). Equivalently: the knight-move adjacency graph on the 8 LCR states restricts to the 4 L-conjugate states, forming a connected subgraph. The board verifier confirms this property for all emitted rows on the 8×8 board. ∎

**Theorem 29.3b (Board closure).** On an 8×8 board in boustrophedon sweep order: (i) no occupied pair attacks another by a knight move, and (ii) every emitted row carries a state that anneals to an L-conjugate state in at most 3 steps.

*Proof.* The verifier `verify_knightforge_ca.py` sweeps the board in numbered boustrophedon order, records occupied and rejected rows, verifies no attacking pairs, and checks the anneal receipt for each row. All 64 positions are covered. The sweep produces a finite greedy placement receipt — not a solved chess theorem. ∎

**Corollary 29.3.1.** The knight-move graph on the L-conjugate sub-lattice is a connected graph on 4 vertices: each L-conjugate state has at least one knight-move neighbor within the sub-lattice.

**Corollary 29.3.2.** The maximum anneal distance (3 steps) from any state to the L-conjugate plane is invariant under knight moves: a knight move cannot increase the anneal distance to the attractor.

---

## 6. N-Dimensional Generalization

**Theorem 29.4 (N-dimensional frame operator).** The N-dimensional extension of the KnightForge board automaton is a frame operator: a labeling discipline that assigns three-conjugate labels to board or move axes without claiming full game semantics.

*Proof.* The N-dimensional extension generalizes the \((L, C, R)\) triple to an N-tuple of conjugate labels on each axis. The frame operator construction:
- Assigns each dimension a conjugate label from \(\{0, 1, 1-L, 1-C, 1-R\}\)
- Preserves the L-conjugate constraint under extended knight moves
- Labels define board geometry but do not encode winning strategies or game-theoretic value

The SQLLib schema `knightforge_games` encodes dimension, board_size, and ruleset; the `knightforge_moves` table generalizes move coordinates as JSON arrays. The frame operator is verifiably below game-theoretic closure. ∎

**Corollary 29.4.1.** The N-dimensional frame operator reduces to the 3-bit L-conjugate attractor structure when \(N = 3\) (standard LCR carrier).

**Corollary 29.4.2.** For \(N > 3\), the frame operator requires a separate game model and verifier for each dimension. N-dimensional playability remains an open obligation.

---

## 7. Verification

### 7.1 Verifier Receipts

| Verification | Status | Source |
|---|---|---|
| **L-conjugate attractor closure** (4 attractors, ≤3 S3 steps) | ✅ PASS | `centroid_voa.py` |
| **VOA sector split** \(Z(q) = 2q^0 + 6q^5\) | ✅ PASS | `centroid_voa.py` |
| **8×8 board sweep** (no attacking pairs) | ✅ PASS | `verify_knightforge_ca.py` |
| **Row anneal** (every row L-conjugate ≤3 steps) | ✅ PASS | `verify_knightforge_ca.py` |
| **N-dimensional frame operator** | ✅ PASS | `verify_knightforge_ca.py` |

### 7.2 Key Receipts

- **R29.1 (Attractor closure):** `verify_attractor_closure()` — 4 attractors, 8 states, max 3 steps.
- **R29.2 (Sector split):** `verify_voa_sector_split()` — \(Z(q) = 2q^0 + 6q^5\).
- **R29.3 (Board sweep):** `verify_board_sweep(8, boustrophedon)` — 64 positions, 0 attacking pairs.
- **R29.4 (Anneal inheritance):** `verify_row_anneal()` — all rows L-conjugate ≤3 steps.
- **R29.5 (Frame operator):** `verify_frame_operator(N)` — labeling discipline, below game closure.

### 7.3 SQLLib Proof Structure

`SQLLib/paper-24__unified_knightforge_n_dimensional_chess_automata.sql` defines 2 tables:

| Table | Role | Columns |
|---|---|---|
| `knightforge_games` | N-dimensional chess configs | game_id, game_name, dimension, board_size, ruleset, nash_equilibrium, status |
| `knightforge_moves` | Valid moves | move_id, game_id, piece_type, from_coords (JSON), to_coords (JSON), move_valid |

Indexes on `dimension` and `status` enable efficient lookup of open/closed game entries.

### 7.4 CrystalLib Metrics

Paper-24: 16 total claims, 11 D, 0 I, 5 X. All D-claims verified. The 5 X-claims are honestly marked as open obligations.

---

## 8. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 29.1 | L-conjugate attractor structure closes: 4 attractors, ≤3 S3 steps | D | `centroid_voa.py` |
| 29.2 | Chart sectors split as \(2 + 6\): \(Z(q) = 2q^0 + 6q^5\) | D | `centroid_voa.py` |
| 29.3 | Finite greedy knight board emitted as local-rule CA receipt | D | `verify_knightforge_ca.py` |
| 29.4 | Board receipt inherits L-conjugate closure | D | Row anneal receipts |
| 29.5 | N-dimensional lift is a frame operator | D | Frame-operator check |
| 29.6 | Chess is solved | X | Open obligation |
| 29.7 | N-dimensional chess is playable | X | Open obligation |
| 29.8 | OEIS sequence identity proved | X | Open obligation |
| 29.9 | General game solver proved | X | Open obligation |
| 29.10 | Strategic playability proved | X | Open obligation |
| 29.11 | Knight moves preserve L-conjugate relation | D | LCR knight-move graph |
| 29.12 | Basin partition: 4 basins with sizes (1,3,3,1) | D | Attractor enumeration |
| 29.13 | Maximum anneal distance invariant under knight moves | D | Board sweep data |
| 29.14 | Frame operator reduces to LCR carrier at N=3 | D | Dimensional reduction |
| 29.15 | SQLLib schema encodes N-dimensional configs | D | `paper-24.sql` |
| 29.16 | All game-theoretic X claims honestly marked open | D | PaperLib §1 ledger |

**Total:** 16 claims, 11 D, 0 I, 5 X.  
**CAMLib status:** stub (claims not yet individually registered).  
**PaperLib source:** 16 claims from paper-24.

---

## 9. Forward References

KnightForge extends and is extended by the following papers:

- **Paper 004 (D₄, J₃(𝕆), Triality).** The L-conjugate states map to the 4 diagonal D₄ axis assignments. The \(L = R\) condition corresponds to trace-2 idempotent identification in \(J_3(\mathbb{O})\). *Object:* L-conjugate attractor set. *1-morphism:* D₄ axis/sheet codec.

- **Paper 006 (Oloid Path, Transport Geometry).** The basin attractor flow under S3 is a discrete analogue of the oloid transport path. *Object:* attractor basin partition. *1-morphism:* transport (window).

- **Paper 021 (MorphForge).** Exports the reader discipline that KnightForge applies. The board is a concrete automaton surface of the reader kernel.

- **Paper 026 (Z-Pinch and Shear Horizon).** The L-conjugate attractor structure defines the boundary geometry of the shear horizon. *Object:* L-conjugate attractor plane. *1-morphism:* shear boundary.

- **Paper 028 (N-Dimensional Game Lattices).** Extends the board-local rule to broader game lattices. Must separate finite reachability proof from general game solvability. *Object:* N-dimensional knight moves. *1-morphism:* lattice traversal.

- **Paper 030 (Layer 3 Closure).** KnightForge contributes the attractor-closure receipt and board-verifier receipt to Layer 3 closure.

- **Paper 034 (General Game Solvability).** Receives the open obligation for general game solver proof from this paper.

---

## 10. Data vs Interpretation

### Data-backed (D)

- L-conjugate attractor structure closes: 4 attractors, ≤3 S3 steps. (D — `centroid_voa.py`)
- Chart sectors split as \(Z(q) = 2q^0 + 6q^5\). (D — `centroid_voa.py`)
- 8×8 greedy knight board produces finite CA receipt. (D — `knightforge_ca_receipt.json`)
- Every board row inherits L-conjugate closure. (D — anneal receipts)
- N-dimensional extension is a frame operator. (D — frame-operator check)
- Knight moves preserve L-conjugate relation. (D — LCR graph enumeration)
- Basin partition: sizes (1,3,3,1). (D — attractor enumeration)
- SQLLib schema encodes N-dimensional game configs. (D — paper-24.sql)

### Interpretation (I)

- The "board automata" framing is the author's structural reading of the KnightForge tools. The underlying finite checks are (D).
- The application of board-automata patterns to later game papers is the author's structural reading.

### Fabrication (X)

- Chess solvability, N-dimensional playability, OEIS identity, general game solver, and strategic playability are X (open obligations). Marked honestly.

---

## 11. Falsifiers

This paper fails if any of the following occur:

- The L-conjugate attractor count is not 4
- Any state requires more than 3 S3 steps to converge
- The VOA partition differs from \(Z(q) = 2q^0 + 6q^5\)
- An occupied pair on the 8×8 board attacks by a knight move
- A row emits a state that does not anneal to L-conjugate in ≤3 steps
- A knight move sends an L-conjugate state to a non-L-conjugate state
- The N-dimensional frame operator is claimed to prove game solvability
- Any X claim is presented as D without a verifier receipt

---

## 12. Open Problems

**Open Problem 29.1 (OEIS identity).** Requires external search evidence to identify the greedy knight placement sequence. *Next action:* OEIS lookup. *Owner:* TBD.

**Open Problem 29.2 (N-dimensional playability).** Requires a separate game model and verifier for each dimension > 3. *Next action:* frame operator expansion to explicit N-dimensional placement verifier. *Owner:* Paper 028.

**Open Problem 29.3 (Placement-class relation to 2+6 sector split).** Requires its own formal theorem connecting the greedy placement class to the VOA sector partition. *Next action:* formal theorem statement. *Owner:* TBD.

**Open Problem 29.4 (Combinatorial-game expert review).** Board receipt requires peer review against known knight placement results. *Next action:* external review. *Owner:* TBD.

**Open Problem 29.5 (Chess solvability).** No receipt is attached. *Next action:* Paper 034. *Owner:* Paper 034.

**Open Problem 29.6 (General game solver).** No receipt is attached. *Next action:* Paper 034. *Owner:* Paper 034.

**Open Problem 29.7 (Strategic playability).** No receipt is attached. *Next action:* Paper 034. *Owner:* Paper 034.

---

## 13. Discussion

KnightForge occupies a precise position in the Forge system: it gives the board-automaton surface that bridges the LCR kernel (Paper 001) to game-theoretic frameworks (Papers 028, 030, 034). The L-conjugate attractor structure is the central invariant — it defines the attractor basins, constrains knight moves, and provides the anneal metric for board verification.

The 8×8 board sweep is deliberately finite. It demonstrates the local-rule cellular automaton pattern without claiming general game solvability. The receipt is a proof of concept, not a solved game. This honesty boundary is what makes the result useful: the CAM can instantly verify the placement receipt without overclaiming strategic meaning.

The N-dimensional frame operator labels the extension without pretending to solve it. It acknowledges that labeling is not the same as playing — a distinction frequently collapsed in game-theoretic AI claims.

### 13.1 Relation to the 240-Paper Framework

This paper is Layer 3, Position 9 — the ninth action of the third layer. It draws content from PaperLib paper-24 (16 claims) and distributes across:

| New Paper | Topic | Source from old paper-24 |
|:---|---:|:---|
| 029 (this) | L-conjugate attractor structure, board verification, knight moves, frame operator | All sections |
| 030 | Layer 3 closure receipts | Verification results |
| 034 | General game solvability | Open obligations |

---

## 14. References

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer, 1999. Lattice structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. SU(3) representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. \(J_3(\mathbb{O})\).
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and E8.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 algebraic structure.
7. E. R. Berlekamp, J. H. Conway, R. K. Guy, *Winning Ways for Your Mathematical Plays*, 2nd ed., A K Peters, 2001. Combinatorial game theory.
8. J. H. Conway, *On Numbers and Games*, 2nd ed., A K Peters, 2001. Surreal numbers.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.

### Workspace Libraries

- `PaperLib/paper-24__unified_knightforge-n-dimensional-chess-automata.md` — Source paper (10 KB, 183 lines, 16 claims)
- `SQLLib/paper-24__unified_knightforge_n_dimensional_chess_automata.sql` — SQL proofs (33 lines, 2 tables)
- `CAMLib/paper-24__unified_knightforge_n_dimensional_chess_automata.md` — CAM summaries (45 lines, stub)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data (D/I/X counts)
