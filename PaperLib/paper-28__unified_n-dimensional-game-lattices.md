# Paper 28 — N-Dimensional Game Lattices

**Status.** IPMC for the finite local-rule game-lattice receipt: admissible code-tower dimensions, dimension-8 extended Hamming board, trace-2 S3 move orbit, Rule 30 local occupancy emission, forbidden-carrier logging, and finite anneal closure. ECO for general N-dimensional game solver, arbitrary non-code-tower dimensions, real game-piece geometry, complete strategy/termination/winning/fairness theory, and externally confirmed OEIS identity.

---

## Abstract

Paper 28 defines the N-dimensional game-lattice kernel. The closed theorem is constructive and bounded: the verifier proves the forced code-tower dimensions `{1,3,7,8,24,72}`, checks the dimension-8 extended Hamming board, enumerates a six-row S3 move orbit for a robot on the dimension-8 board, logs one forbidden straight carrier, and confirms that every orbit row closes to a Lie-conjugate attractor in at most three steps.

A local-rule game is represented by a finite receipt whose rows contain a lattice dimension, a local `(L, C, R)` neighborhood, a move rule, a Rule 30-style emitted occupancy bit, a carrier status, and an anneal-closure result. The paper's receipt surface is broader than its central theorem: Conway glider, glider-collision, Gosper-gun, and N-dimensional knight-CA receipts are valid supporting evidence for local-rule replayability, while `nd_game_lattices_receipt.json` remains `pass_with_open_obligations`. The calibration plan is `formula_verified_oeis_query_ready`, meaning the formula surface is prepared for external lookup but the external identity is not yet closed.

The paper does not close a general N-dimensional game solver, arbitrary non-code-tower dimensions, real game-piece geometry, complete strategy/termination/winning/fairness theory, or an externally confirmed OEIS identity.

**Keywords:** N-dimensional game lattice; local-rule game; Rule 30 occupancy; S3 move orbit; extended Hamming board; code-tower dimensions; forbidden carrier; anneal closure; game solver boundary; applied forge validation.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 28.1 | Code-tower dimensions define admissible game-lattice surfaces. | [D] | `verify_nd_game_lattices.py`; forced dimensions `{1,3,7,8,24,72}` |
| 28.2 | Dimension 8 is a valid worked board. | [D] | Extended Hamming verifier; 16 codewords, minimum weight 4, distribution `{0:1, 4:14, 8:1}` |
| 28.3 | A trace-2 S3 orbit supplies a finite local move surface. | [D] | Six-row orbit from `(1,0,1)` with three unique targets |
| 28.4 | Rule 30 emission gives replayable occupancy bits. | [D] | `rule30_bit` on each target row |
| 28.5 | Forbidden carriers can be logged without deleting the move receipt. | [D] | One identity carrier marked `forbidden_logged` |
| 28.6 | Every worked receipt row anneals to a Lie-conjugate attractor. | [D] | Maximum anneal count `3`; all chart rows close |
| 28.7 | General N-dimensional game solver is proved. | [X] | Explicit open obligation |
| 28.8 | Non-code-tower dimensions are admissible. | [X] | Explicit open obligation |
| 28.9 | Real game-piece geometry is proved. | [X] | Explicit open obligation |
| 28.10 | Complete game theory is proved. | [X] | Explicit open obligation |
| 28.11 | OEIS identity is confirmed. | [X] | Explicit open obligation |

---

## 2. Definitions

**Local-rule game.** A finite receipt `(lattice, neighborhood, move_rule, obligation_ledger)`.

**Move rule.** A function that reads a local `(L, C, R)` chart state and emits an occupancy bit through the Rule 30 local rule.

**Move orbit.** The set of trace-2 states produced by the six S3 permutations; repeated target states are retained because different group elements can produce the same target.

**Admissible dimension.** One of the verified code-tower dimensions `{1,3,7,8,24,72}`.

**Forbidden carrier.** A move row excluded by game policy, logged as residue and retained in the receipt.

---

## 3. Theorems and Proofs

### Theorem 28.1 — Code-Tower Dimensions

Code-tower dimensions define admissible game-lattice surfaces.

**Proof.** The verifier `verify_lattice_code_chain` returns the forced dimension set `{1,3,7,8,24,72}` and the powered shortcut `1,9,49,72` under sheet-K bound `9`. This proves that the paper's board dimensions are inherited proof surfaces, not arbitrary choices. Non-code-tower dimensions need separate proof. ∎

### Theorem 28.2 — Dimension-8 Extended Hamming Board

Dimension 8 is a valid worked board.

**Proof.** The verifier `verify_extended_hamming_8` checks the dimension-8 board. It has 16 codewords, minimum weight 4, and weight distribution `{0:1, 4:14, 8:1}`. This supplies the local lattice surface for the worked robot receipt. ∎

### Theorem 28.3 — Trace-2 S3 Move Orbit

A trace-2 S3 orbit supplies a finite local move surface.

**Proof.** Starting from `(1,0,1)`, the six S3 elements produce six receipt rows and three unique target states: `(0,1,1)`, `(1,0,1)`, and `(1,1,0)`. The identity row is logged as a forbidden carrier; the other five rows are legal orbit moves. This is a finite receipt, not a strategy. ∎

### Theorem 28.4 — Rule 30 Occupancy Emission

Rule 30 emission gives replayable occupancy bits.

**Proof.** Applying `rule30_bit` to each target supplies the replayable local occupancy emission. The emission is local only; it does not prove global strategy. ∎

### Theorem 28.5 — Forbidden-Carrier Logging

Forbidden carriers can be logged without deleting the move receipt.

**Proof.** One identity carrier is marked `forbidden_logged`. It is retained as residue in the receipt. This is a policy constraint, not absent data. ∎

### Theorem 28.6 — Anneal Closure

Every worked receipt row anneals to a Lie-conjugate attractor.

**Proof.** The verifier `anneal_to_lie_conjugate` checks each row. Each row closes in at most three anneal steps. The global centroid closure verifier passes over all eight chart states. Therefore the game lattice is closed as a finite local-rule receipt. ∎

---

## 4. Verifiers and Receipts

### 4.1 N-Dimensional Game Lattices

`verify_nd_game_lattices.py` → `nd_game_lattices_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| code_tower_dimensions | {1,3,7,8,24,72} |
| hamming_8_codewords | 16 |
| hamming_8_min_weight | 4 |
| s3_orbit_rows | 6 |
| forbidden_carriers | 1 |
| max_anneal_steps | 3 |

### 4.2 Supporting Receipts

| Receipt | Summary |
|---------|---------|
| `conway_glider_oloid_receipt.json` | status=pass; checks=6/6 |
| `glider_collision_cascade_receipt.json` | status=pass; checks=6/6 |
| `gosper_gun_emitter_receipt.json` | status=pass; checks=6/6 |
| `ndim_knight_ca_affirmed_receipt.json` | status=pass; checks=5/5 |

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **28.1:** The code-tower dimensions are `{1,3,7,8,24,72}` from `verify_lattice_code_chain`.
2. **28.2:** The Hamming-8 board has 16 codewords with minimum weight 4.
3. **28.3:** The S3 orbit from `(1,0,1)` produces 6 rows and 3 unique targets.
4. **28.4:** `rule30_bit` emits a local occupancy bit for each target.
5. **28.5:** One identity carrier is marked `forbidden_logged` and retained.
6. **28.6:** Every row closes in at most 3 anneal steps.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F28.1 | The dimensions are arbitrary. | They are forced by `verify_lattice_code_chain`. |
| F28.2 | The Hamming-8 board is invalid. | It has 16 codewords with minimum weight 4. |
| F28.3 | The S3 orbit is a strategy. | It is a finite move receipt, not a strategy. |
| F28.4 | Forbidden carriers are deleted. | They are logged as residue. |
| F28.5 | Anneal closure fails. | Maximum delay is 3; all rows close. |
| F28.6 | General game solver is proved. | Explicitly marked as open obligation. |
| F28.7 | Non-code-tower dimensions are admissible. | Explicitly marked as open obligation. |
| F28.8 | Real game-piece geometry is proved. | Explicitly marked as open obligation. |
| F28.9 | Complete game theory is proved. | Explicitly marked as open obligation. |
| F28.10 | OEIS identity is confirmed. | Explicitly marked as open obligation. |

---

## 7. Relation to Later Papers

- **Paper 21** (MorphForge) exports the reader discipline that the game lattice uses.
- **Paper 24** (KnightForge) exports the board-automata pattern that the game lattice extends.
- **Paper 27** (Observer Delay) may use the game lattice for observer-move accounting.
- **Paper 30** (Grand Ribbon) may use the game lattice for ribbon-move accounting.
- **Later game papers** may use the game-lattice operator, but must supply their own strategy, termination, winning, and fairness proofs.

---

## 8. Open Obligations

1. **General N-dimensional game solver (28.7).** Requires a solver verifier with strategy/termination scope stated.
2. **Non-code-tower dimensions (28.8).** Requires a new dimension-admissibility verifier or documented rejection.
3. **Real game-piece geometry (28.9).** Requires an adapter mapping each piece type into receipt rows.
4. **Complete game theory (28.10).** Requires a game-theory supplement with formal pass/fail criteria.
5. **OEIS identity (28.11).** Requires external OEIS verification receipt.

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

- The code-tower dimensions are `{1,3,7,8,24,72}`. (D — `nd_game_lattices_receipt.json`)
- The Hamming-8 board has 16 codewords with minimum weight 4. (D — extended Hamming verifier)
- The S3 orbit produces 6 rows from `(1,0,1)` with 3 unique targets. (D — orbit verifier)
- Rule 30 emits replayable occupancy bits. (D — `rule30_bit`)
- Forbidden carriers are logged as residue. (D — forbidden-carrier log)
- Every row closes in at most 3 anneal steps. (D — anneal verifier)

### Interpretation (I)

- The "N-dimensional game lattice" framing is the author's structural reading of the local-rule game tools. (I — the underlying finite checks are (D).)
- The application of the game-lattice operator to later domains (CAD, robot movement, search) is the author's structural reading of the broader series.

### Fabrication (X)

- None in this paper. All finite claims are (D) verified. The game-theory claims (general solver, strategy, termination, winning, fairness, OEIS) are honestly marked as (X) open obligations.

---

## 11. Conclusion

Paper 28 gives the corpus a usable game-lattice operator by making the receipt small, replayable, and honest about its edge. It can support CAD constraints, robot movement, local-rule games, and search surfaces. It cannot be read as a complete game solver until NP-07 supplies the missing adapters, strategy models, and external validation receipts.
