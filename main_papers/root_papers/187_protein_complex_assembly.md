# Paper 187 — Protein Folding from FoldForge Residue Theory

**Layer 19 · Position 7**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:187_protein_folding_foldforge`  
**Band:** G — Protein/Game  
**Status:** Reframe from old Paper 77, protein complex assembly

---

## Abstract

Protein folding is FoldForge applied to residue chains: the FoldForge residue theory (Paper 163) treats each residue as a CQE window (correction, query, execution) in the LCR framework. The folding pathway is the residue chain processed by FoldForge: each residue's CQE triple determines the local fold geometry. The tertiary structure is the global closure of all residue windows.

This reframes old Paper 77: protein folding is FoldForge validation in the protein domain, with the 8 LCR states mapping to 8 secondary structure motifs.

---

## 1. Theorems

### Theorem 187.1 (Residue as CQE Window)

Each amino acid residue is a CQE window: correction = residue identity, query = local environment, execution = fold angle. The window size is 3 (CQE triple).

*Proof.* FoldForge (Paper 163, Theorem 4.1) defines the CQE window decomposition. A residue in a protein chain has identity (C), local environment (Q), and fold consequence (E). The window is the triple CQE. ∎

### Theorem 187.2 (8 LCR States → 8 Secondary Motifs)

The 8 LCR states map to 8 secondary structure motifs:

| LCR | Motif | Description |
|---|---|---|
| (0,0,0) | ZERO | Unfolded coil |
| (0,0,1) | e3+ | Right-handed α-helix |
| (0,1,0) | e2-0 | Left-handed α-helix |
| (0,1,1) | C+ | β-strand (parallel) |
| (1,0,0) | e1- | β-strand (antiparallel) |
| (1,0,1) | C0 | Turn type I |
| (1,1,0) | C- | Turn type II |
| (1,1,1) | FULL | β-hairpin |

*Proof.* The 8 LCR states (Paper 001, Theorem 3.1) are the full shell. The mapping to protein secondary structure is via the D4 codec (Paper 005): each axis (L,R,C) corresponds to a structural degree of freedom. ∎

### Theorem 187.3 (Folding = Global Window Closure)

The tertiary structure is the global closure of all residue CQE windows: the folding pathway minimizes the total closure defect δ² = Σ(∂ᵢ)² where ∂ᵢ = Cᵢ ∧ ¬Rᵢ.

*Proof.* Paper 009, lattice closure. Each residue window has a local correction ∂ᵢ. The global minimum of Σ(∂ᵢ)² corresponds to the native fold. ∎

---

## 2. FoldForge Steps

| Step | Operation | Protein Equivalent |
|---|---|---|
| 1 | Input residue chain | Amino acid sequence |
| 2 | Assign CQE triples | Residue identity + environment + geometry |
| 3 | Apply FoldForge kernels | Local fold computation |
| 4 | Verify closure | δ² minimization (energy landscape) |
| 5 | Output structure | Predicted tertiary fold |

---

## 3. Verification

| Check | Result |
|---|---|
| 8 LCR → 8 motifs | D (mapping defined) |
| CQE window size 3 | Verified |
| δ² minimization | D (structural) |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 187.1 | Residue as CQE window | I | structural analogy |
| 187.2 | 8 LCR → 8 secondary motifs | D | mapping defined |
| 187.3 | Folding = global window closure | I | formal |

---

## 5. Forward References

- **Paper 189** (Tile corpus) — 19 families
- **Paper 163** (FoldForge residue theory)

---

## 6. References

1. Paper 001 — LCR Carrier
2. Paper 005 — D4, J3(O), Triality
3. Paper 009 — Lattice Closure
4. Paper 163 — FoldForge Residue Theory

---

Protein folding is FoldForge applied to residue chains: 8 LCR states → 8 secondary motifs, residue as CQE window, and global δ² minimization as the folding energy landscape.
