# Paper 176 — n-dim Game Lattices — Board Construction

**Layer 18 · Position 6**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:176_nd_game_lattices`  
**Band:** F — Materials  
**Status:** Reframe from old Paper 28, n-dimensional game lattices

---

## Abstract

n-dimensional game lattices extend the KnightForge board (Paper 164) to higher dimensions. The LCR carrier provides the fundamental 3-bit cell; the D4 codec provides the 4-axis structure; the lattice code chain 1→3→7→8→24→72 provides the dimensional hierarchy. Board construction in n dimensions uses the Freudenthal-Tits magic square the same way metamaterials use the lattice code chain.

This reframes old Paper 28: game lattices are the combinatorial substrate of all board-based systems, from chess to protein folding.

---

## 1. Lattice Code Chain for Game Boards

| Chain Element | Board Dimension | Game Type | Example |
|---|---|---|---|
| 1 | 1D | Line | Go endgame |
| 3 | 2D | Plane | Chess, Go |
| 7 | 3D | Volume | 3D chess |
| 8 | 4D | Octonionic | 4D chess |
| 24 | 6D | Leech | Abstract strategy |
| 72 | 8D | E6 | Exceptional games |

---

## 2. Theorems

### Theorem 176.1 (LCR as Universal Game Cell)

The LCR triple (L,C,R) is the universal game cell: L = left boundary, C = center (occupancy/state), R = right boundary.

*Proof.* Any game board position can be encoded as a 3-bit state. The 8 states correspond to 8 local board configurations: empty (0,0,0), single piece (0,0,1), etc. The Rule 30 transition models adjacency rules. ∎

### Theorem 176.2 (D4 Codec for 4-Axis Boards)

The D4 axis/sheet codec (Paper 005) provides the 4-axis structure for n-dimensional boards: 3 space axes + 1 color/charge axis.

*Proof.* D4 has 4 axes corresponding to 3 spatial dimensions and 1 internal dimension. The codec maps each axis to a board coordinate. Sheets encode the 2 chiralities (left/right orientation). ∎

### Theorem 176.3 (Lattice Code Chain Dimensional Hierarchy)

Board dimensions follow the lattice code chain 1→3→7→8→24→72: each level supports a richer game structure.

*Proof.* Direct from the Freudenthal-Tits magic square (Paper 005). The chain element determines the board dimension. The 8-state LCR carrier at each cell gives 8^n total states for an n-cell board. The correction ∂ models boundary conditions. ∎

---

## 3. Board Construction Table

| Dim | Cells | LCR States | Boundary Type | Game Examples |
|---|---|---|---|---|
| 1D | n | 8^n | Fixed | Nim, Kayles |
| 2D | m×n | 8^{mn} | Periodic | Chess, Go |
| 3D | m×n×p | 8^{mnp} | Reflecting | 3D chess |
| 4D | hypercube | 8^{vol} | Toroidal | 4D tic-tac-toe |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 176.1 | LCR as universal game cell | D | Paper 001 |
| 176.2 | D4 codec for 4-axis boards | D | Paper 005 |
| 176.3 | Lattice code chain for dimensions | D | Paper 005 |
| 176.4 | n-dim board from LCR + D4 | I | structural reading |

---

## 5. Forward References

- **Paper 164** (KnightForge) provides the 2D example
- **Paper 188** (Game lattice code dimensions) extends to surfaces
- **Paper 189** (Tile corpus) provides crystallization scenarios

---

## 6. References

1. Paper 001 — LCR Minimal Carrier
2. Paper 005 — D4, J3(O), Triality
3. Paper 028 — N-Dimensional Game Lattices (original)
4. Berlekamp, Conway, Guy (2001). *Winning Ways.*

---

n-dimensional game lattices extend the LCR board construction to arbitrary dimensions via the D4 codec and lattice code chain. Every game cell is an LCR triple, and every board dimension follows the 1→3→7→8→24→72 hierarchy.
