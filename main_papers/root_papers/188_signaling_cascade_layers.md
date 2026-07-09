# Paper 188 — Game Lattice Code Dimensions — 7 Regions, 3 Axes

**Layer 19 · Position 8**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:188_game_lattice_code`  
**Band:** G — Protein/Game  
**Status:** Reframe from old Papers 28+77, signaling cascade layers as game lattice

---

## Abstract

The game lattice code dimensions define 7 regions × 3 axes = 21 inhabited cells for a Markov board at dimension n. The 3 axes (L, C, R) define the LCR coordinates; the 7 regions are the nonzero shell states. The board is the Cartesian product of axis ranges up to closure depth. Each cell records the game state at that LCR coordinate. The supervisor cursor (Paper 178) is the game piece moving across the board.

This reframes old Papers 28 (game lattice) and 77 (signaling cascade): the game lattice code is the control plane for all Protein/Game layer operations, with 21 inhabited cells encoding signaling cascade states.

---

## 1. Theorems

### Theorem 188.1 (7 Regions × 3 Axes Board)

A Markov board at dimension n has 7 regions × 3 axes = 21 inhabited cells, where the 7 regions are the nonzero LCR shell states {L, C, R, LC, LR, CR, LCR} and the 3 axes are the axis classes.

*Proof.* The 8 LCR states include ZERO (0,0,0) and 7 nonzero states (Paper 001). The 3 axes L, C, R are the basis directions. The board maps each nonzero state to an axis class, giving 7 × 3 = 21 inhabited cells. The regions are the shell partitions: sh=1 (3 states: L, C, R), sh=2 (3 states: LC, LR, CR), sh=3 (1 state: LCR). ∎

### Theorem 188.2 (Game Piece = Supervisor Cursor)

The game piece moving across the board is the supervisor cursor (Paper 178): a finite-state machine that dispatches requests at board positions.

*Proof.* The supervisor cursor (Paper 178, Theorem 3.1) dispatches proof/readout requests. On the game board, each cell is a request destination. The cursor position encodes the current request. ∎

### Theorem 188.3 (Signaling Cascade as Board Traversal)

A signaling cascade (Paper 77) is a traversal of the 21-cell board: each signal step moves the cursor to an adjacent cell, following LCR correction paths.

*Proof.* The correction paths (Paper 004) connect adjacent LCR states. A signaling cascade (e.g., MAP kinase cascade) traverses the board from the ZERO state through intermediate states to the FULL terminal state. ∎

---

## 2. Board Structure

| Shell | States | Cells per Axis | Total |
|---|---|---|---|
| sh=1 | L, C, R | 3 | 9 |
| sh=2 | LC, LR, CR | 3 | 9 |
| sh=3 | LCR | 3 | 3 |
| | | **Total** | **21** |

---

## 3. Verification

| Check | Result |
|---|---|
| 7 nonzero states | D (Paper 001) |
| 3 axes | D |
| 21 cells | Computed |
| Cursor = supervisor | D (Paper 178) |
| Cascade = traversal | Interpretive |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 188.1 | 7 × 3 = 21 board cells | D | computed |
| 188.2 | Game piece = supervisor cursor | D | Paper 178 |
| 188.3 | Signaling cascade = board traversal | I | structural analogy |

---

## 5. Forward References

- **Paper 189** (Tile corpus) — 19 families
- **Paper 190** (Layer 19 closure)

---

## 6. References

1. Paper 001 — LCR Carrier (8 states, shell grading)
2. Paper 004 — Correction and Closure
3. Paper 028 — n-Dimensional Game Lattices (original)
4. Paper 077 — Superpermutation Minimality

---

The game lattice code defines a 21-cell board (7 nonzero LCR states × 3 axes). The supervisor cursor traverses the board, encoding signaling cascades as LCR correction paths.
