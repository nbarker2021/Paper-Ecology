# Paper 24 — KnightForge / N-Dimensional Chess Automata

**Status.** IPMC for the board-automata kernel: L-conjugate attractor closure, `2 + 6` VOA sector split, finite greedy knight-placement receipt, and N-dimensional frame operator. ECO for chess solvability, N-dimensional playability, OEIS sequence identity, general game solver, and strategic playability.

---

## Abstract

Paper 24 defines the KnightForge board-automata kernel. The closed result is that greedy non-attacking knight placement can be represented as a replayable local-rule cellular automaton whose `(L, C, R)` rows close under the L-conjugate centroid structure, and that the N-dimensional extension is properly labeled as a frame operator.

The verifier calls the promoted `centroid_voa.py` substrate. It confirms four L-conjugate attractors, closure of all eight chart states to the `L = R` plane in at most three S3 transposition steps, the sector partition `Z(q) = 2q^0 + 6q^5`, and a centroid-chain split into two fixed points and six period-4 states. The board verifier then sweeps an 8 by 8 board in numbered boustrophedon order, records occupied and rejected rows, verifies that no occupied pair attacks another by a knight move, and verifies that every emitted row anneals to an L-conjugate state in at most three steps.

The paper does not solve chess, N-dimensional chess, a general game solver, OEIS sequence identity, or strategic playability. Those items remain open obligations.

**Keywords:** KnightForge; board automata; L-conjugate closure; finite greedy placement; VOA sector split; frame operator; combinatorial-game validation.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 24.1 | The L-conjugate attractor structure closes. | [D] | `centroid_voa.py`; four `L = R` attractors; at most three S3 steps |
| 24.2 | The chart sectors split as `2 + 6`. | [D] | `Z(q) = 2q^0 + 6q^5` |
| 24.3 | A finite greedy knight board can be emitted as a local-rule CA receipt. | [D] | `verify_knightforge_ca.py`; 8 by 8 sweep; occupied/rejected rows |
| 24.4 | The board receipt inherits L-conjugate closure. | [D] | Every row carries state and anneal receipt |
| 24.5 | The N-dimensional lift is a frame operator. | [D] | Frame-operator row with open obligations |
| 24.6 | Chess is solved. | [X] | Explicit open obligation |
| 24.7 | N-dimensional chess is playable. | [X] | Explicit open obligation |
| 24.8 | OEIS sequence identity is proved. | [X] | Explicit open obligation |
| 24.9 | General game solver is proved. | [X] | Explicit open obligation |
| 24.10 | Strategic playability is proved. | [X] | Explicit open obligation |

---

## 2. Definitions

**Placement state.** A local triple `(L, C, R)` where `C` is the occupancy decision for the current cell, and `L` and `R` record whether earlier placed knights attack the current cell from opposed L-move approach families.

**Rejection.** A retained row rather than a deleted state.

**L-conjugate state.** A state satisfying `L = R`.

**Frame operator.** A label assigning three-conjugate labels to board or move axes without claiming full game semantics.

---

## 3. Theorems and Proofs

### Theorem 24.1 — L-Conjugate Attractor Closure

The L-conjugate attractor structure closes.

**Proof.** The verifier `centroid_voa.py` confirms four `L = R` attractors. All eight chart states close to the `L = R` plane in at most three S3 transposition steps. This is a finite 8-state chart property. ∎

### Theorem 24.2 — VOA Sector Split `2 + 6`

The chart sectors split as `2 + 6`.

**Proof.** The sector partition is `Z(q) = 2q^0 + 6q^5`. The centroid-chain splits into two fixed points and six period-4 states. This is a VOA sector split, not yet a placement-class theorem. ∎

### Theorem 24.3 — Finite Greedy Knight Board Receipt

A finite greedy knight board can be emitted as a local-rule CA receipt.

**Proof.** The verifier `verify_knightforge_ca.py` sweeps an 8 by 8 board in numbered boustrophedon order, records occupied and rejected rows, and verifies that no occupied pair attacks another by a knight move. The result is a finite placement receipt, not a solved chess theorem. ∎

### Theorem 24.4 — L-Conjugate Closure Inheritance

The board receipt inherits L-conjugate closure.

**Proof.** Every emitted row carries a state and anneal receipt. The verifier checks that every row anneals to an L-conjugate state in at most three steps. This applies to the finite emitted rows only. ∎

### Theorem 24.5 — N-Dimensional Frame Operator

The N-dimensional lift is a frame operator.

**Proof.** The final check constructs the N-dimensional frame operator and keeps it explicitly below game-theoretic closure. The frame operator is a labeling discipline, not a playable N-dimensional chess proof. ∎

---

## 4. Verifiers and Receipts

### 4.1 KnightForge CA

`verify_knightforge_ca.py` → `knightforge_ca_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| board_size | 8 by 8 |
| sweep_order | boustrophedon |
| l_conjugate_attractors | 4 |
| max_anneal_steps | 3 |

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **24.1:** Four `L = R` attractors; at most three S3 steps for all eight states.
2. **24.2:** The sector partition is `Z(q) = 2q^0 + 6q^5`.
3. **24.3:** The 8 by 8 board sweep produces occupied and rejected rows with no attacking pairs.
4. **24.4:** Every row anneals to `L = R` in at most three steps.
5. **24.5:** The N-dimensional extension is labeled as a frame operator.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F24.1 | The board solves chess. | It is a finite greedy placement, not solved chess. |
| F24.2 | The frame operator is a playable game. | It is a labeling discipline, not a game proof. |
| F24.3 | OEIS identity is proved. | Explicitly marked as open obligation. |
| F24.4 | General game solvability is proved. | Explicitly marked as open obligation. |
| F24.5 | Strategic playability is proved. | Explicitly marked as open obligation. |

---

## 7. Relation to Later Papers

- **Paper 21** (MorphForge) exports the reader discipline that KnightForge applies. The board is a concrete automaton surface of the reader kernel.
- **Paper 23** (FoldForge) exports the chain-descriptor pattern. Paper 24 translates the chain and contact-map idea into paths on a board or automaton lattice.
- **Paper 25** (Energetic Traversal Maps) may treat occupied moves, rejected moves, and frame labels as traversal cost rows. It must still prove its own energy or action ledger.
- **Paper 28** (N-Dimensional Game Lattices) may extend the board-local rule to broader game lattices. It must separate finite reachability proof from general game solvability.

---

## 8. Open Obligations

1. **OEIS identity (24.8).** Requires external search evidence.
2. **N-dimensional playability (24.7).** Requires a separate game model and verifier.
3. **Placement-class relation to `2+6` sector split (24.3).** Requires its own formal theorem.
4. **Combinatorial-game expert review (24.4).** Requires peer review.
5. **Chess solvability (24.6).** No receipt is attached.
6. **General game solver (24.9).** No receipt is attached.
7. **Strategic playability (24.10).** No receipt is attached.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and `E8` structures.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
7. E. R. Berlekamp, J. H. Conway, R. K. Guy, *Winning Ways for Your Mathematical Plays*, 2nd ed., A K Peters, 2001. Combinatorial game theory.
8. J. H. Conway, *On Numbers and Games*, 2nd ed., A K Peters, 2001. Surreal numbers and game theory.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.
10. D. E. Knuth, *The Art of Computer Programming, Volume 4A: Combinatorial Algorithms*, Addison-Wesley, 2011. Combinatorial enumeration.

---

## 10. Data vs Interpretation

### Data-backed (D)

- The L-conjugate attractor structure closes in at most three S3 steps. (D — `centroid_voa.py`)
- The chart sectors split as `2 + 6`. (D — `Z(q) = 2q^0 + 6q^5`)
- The 8 by 8 greedy knight board produces a finite CA receipt. (D — `knightforge_ca_receipt.json`)
- Every board row inherits L-conjugate closure. (D — anneal receipts for all rows)
- The N-dimensional extension is a frame operator. (D — frame-operator check)

### Interpretation (I)

- The "board automata" framing is the author's structural reading of the KnightForge tools. (I — the underlying finite checks are (D).)
- The application of the board-automata pattern to later game papers is the author's structural reading of the broader series.

### Fabrication (X)

- None in this paper. All finite claims are (D) verified. The game-theoretic claims (chess solvability, playability, OEIS, general solver, strategy) are honestly marked as (X) open obligations.

---

## 11. Conclusion

Paper 24 gives the Forge system a precise game-scale automaton surface. The CAM can instantly look up the finite placement receipt, local closure, sector label, and frame row. It cannot, from this paper alone, decide generalized game solvability or strategic meaning. That boundary is what makes the result useful instead of theatrical.
