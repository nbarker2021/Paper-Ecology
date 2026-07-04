# Paper 23 — FoldForge Protein Folding

**Status.** IPMC for the protein-chain descriptor kernel: residue sequence as local `(L, C, R)` windows, replayable contact-map receipt, candidate bifurcation marks, and bounded oloid winding witness with open gaps. ECO for native structure prediction, deposited structure agreement, free-energy minima, fold rates, AlphaFold parity, and measured thermodynamic behavior.

---

## Abstract

Paper 23 defines the FoldForge protein descriptor kernel. The closed result is that an admitted residue sequence can be converted into local `(L, C, R)` windows, emitted as a replayable contact-map receipt, marked with candidate bifurcation events, and paired with a bounded oloid winding witness that carries its open gaps.

The canonical verifier uses the compact sequence `MKTFFVLLLCTFTVLA`. It encodes residues by a hydrophobic/polar bit, produces 16 residue-window rows, verifies 14 complete interior `(L, C, R)` windows, emits a symmetric zero-diagonal contact map with nonzero contacts, and marks local side changes as candidate bifurcations. The bounded winding witness runs at `max_depth = 512` and `max_order = 4`; it passes its schema and stable-operator checks, exposes an 8-state finite operator, and retains `DEPTH_ONLY_WINDING_EXTRACTOR_PENDING` as a named gap.

The paper does not prove native structure prediction, deposited structure agreement, free-energy minima, fold rates, AlphaFold parity, or measured thermodynamic behavior. The biological validation burden remains external.

**Keywords:** FoldForge; protein descriptor; residue windows; contact map; candidate bifurcation; bounded winding witness; biological validation; PDB comparison.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 23.1 | A residue chain can be read as local CQE windows. | [D] | `verify_foldforge_descriptor.py`; 16 chart rows; 14 complete interior windows |
| 23.2 | A replayable contact-map receipt can be emitted. | [D] | Symmetric zero-diagonal map with nonzero contacts |
| 23.3 | Local side changes can be marked as candidate fold events. | [D] | Side-change/bifurcation marks |
| 23.4 | The oloid winding substrate is bounded and gap-aware. | [D] | `pass_with_open_gaps`; 8-state operator; depth-only extractor gap |
| 23.5 | FoldForge remains a candidate descriptor until validated. | [D] | `foldforge_descriptor_receipt.json`; `calibration_plan.json` |
| 23.6 | Native structure prediction is proved. | [X] | Explicit open obligation |
| 23.7 | Deposited structure agreement is proved. | [X] | Explicit open obligation |
| 23.8 | Free-energy minima are proved. | [X] | Explicit open obligation |
| 23.9 | Fold rates are proved. | [X] | Explicit open obligation |
| 23.10 | AlphaFold parity is proved. | [X] | Explicit open obligation |
| 23.11 | Measured thermodynamic behavior is proved. | [X] | Explicit open obligation |
| 23.12 | Light-cone = recursive self-closure of tile substitution at depth 3 = void boundary | [D] | `28_N_Dimensional_Game_Lattices.md` |
| 23.13 | Light-Cone Closure = Recursive Self-Closure — Tile Void Boundary | [I] | `28_N_Dimensional_Game_Lattices.md` |
| 23.14 | Tier: Recursive Closure (20-23) | [I] | `28_N_Dimensional_Game_Lattices.md` |
| 23.15 | SpectreTile, CrystalTile (343 void boundary), TarpitTile | [D] | `28_N_Dimensional_Game_Lattices.md` |

---

## 2. Definitions

**Residue chart.** The sequence of overlapping local windows `(residue[n-1], residue[n], residue[n+1])`, where `C` is the active residue and `L` and `R` are its backbone neighbors.

**Contact map.** A symmetric matrix recording which residue pairs satisfy the selected contact predicate.

**Bifurcation mark.** A side-change event in the local window, treated only as a candidate turn or topology marker.

**Winding trace.** The bounded oloid/spinor trace supplied by the lattice substrate.

---

## 3. Theorems and Proofs

### Theorem 23.1 — Residue Chain as Local Windows

A residue chain can be read as local CQE windows.

**Proof.** The verifier `verify_foldforge_descriptor.py` builds the residue chart and checks the local-window count. For the canonical sequence `MKTFFVLLLCTFTVLA`, it produces 16 residue-window rows and verifies 14 complete interior `(L, C, R)` windows. This imports the applied-reader kernel into a protein-chain setting. ∎

### Theorem 23.2 — Replayable Contact-Map Receipt

A replayable contact-map receipt can be emitted.

**Proof.** The verifier builds the contact map and checks symmetry, zero diagonal, nonzero contacts, and nontrivial density. These checks establish a replayable contact receipt, not a native fold. The contact predicate is heuristic: separated hydrophobic residues form candidate contacts. ∎

### Theorem 23.3 — Candidate Bifurcation Marks

Local side changes can be marked as candidate fold events.

**Proof.** The verifier marks local side changes as candidate bifurcations. The marks are falsifiable descriptors: a later validation pass may compare them to PDB structures, experimental structures, or validated simulations. They are not promoted to real turns, knots, or folds without structure comparison. ∎

### Theorem 23.4 — Bounded Oloid Winding Witness

The oloid winding substrate is bounded and gap-aware.

**Proof.** The bounded winding witness runs at `max_depth = 512` and `max_order = 4`. It passes its schema and stable-operator checks, exposes an 8-state finite operator, and retains `DEPTH_ONLY_WINDING_EXTRACTOR_PENDING` as a named gap. The direct oloid predictor and bifurcation detector are both retained as open-gap substrate rather than promoted to biological proof. ∎

### Theorem 23.5 — Governance: Candidate Descriptor Until Validated

FoldForge remains a candidate descriptor until validated.

**Proof.** The receipt `foldforge_descriptor_receipt.json` reports `status=pass_with_open_obligations`. The `calibration_plan.json` records the open biological obligations. PDB, native structure, parser, fold-rate, and thermodynamic claims remain open. ∎

---

## 4. Verifiers and Receipts

### 4.1 FoldForge Descriptor

`verify_foldforge_descriptor.py` → `foldforge_descriptor_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| residue_windows | 16 |
| interior_windows | 14 |
| contact_map | symmetric, zero-diagonal, nonzero |
| winding_operator | 8-state |

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **23.1:** The residue chart has 16 windows; 14 are complete interior.
2. **23.2:** The contact map is symmetric with zero diagonal and nonzero contacts.
3. **23.3:** Side changes are marked as candidate bifurcations, not real turns.
4. **23.4:** The winding witness has an 8-state operator and a depth-only gap.
5. **23.5:** The descriptor is explicitly labeled as candidate until validated.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F23.1 | The contact map is a native fold. | It is a heuristic receipt, not a native structure. |
| F23.2 | Candidate bifurcations are real turns. | They are descriptors without structure comparison. |
| F23.3 | The winding witness is a biological proof. | It is bounded open-gap substrate. |
| F23.4 | Native structure prediction is proved. | Explicitly marked as open obligation. |
| F23.5 | Free-energy minima are proved. | Explicitly marked as open obligation. |
| F23.6 | Fold rates are proved. | Explicitly marked as open obligation. |
| F23.7 | AlphaFold parity is proved. | Explicitly marked as open obligation. |
| F23.8 | Thermodynamic behavior is measured. | Explicitly marked as open obligation. |

---

## 7. Relation to Later Papers

- **Paper 21** (MorphForge) exports the reader discipline that FoldForge applies. The residue-window discipline is inherited from the MorphForge kernel.
- **Paper 22** (MetaForge) exports the candidate-ledger pattern that FoldForge uses. The descriptor is a candidate until validated.
- **Paper 24** (KnightForge) may translate the chain and contact-map idea into paths on a board or automaton lattice. A game-state path may be read as a local sequence with adjacency receipts, but must prove its own rules and reachability.
- **Later biological papers** may use the FoldForge pattern when an object has a sequential structure, but must supply their own PDB, simulation, assay, parser, and thermodynamic receipts.

---

## 8. Open Obligations

1. **PDB validation (23.6).** Requires comparison to deposited structures.
2. **Native structure prediction (23.7).** Requires 3D fold prediction and validation.
3. **Free-energy minima (23.8).** Requires thermodynamic calculation and validation.
4. **Fold rates (23.9).** Requires kinetics simulation and measurement.
5. **AlphaFold parity (23.10).** Requires comparison to AlphaFold predictions.
6. **Measured thermodynamic behavior (23.11).** Requires empirical measurement.
7. **Depth-only winding extraction.** The `DEPTH_ONLY_WINDING_EXTRACTOR_PENDING` gap requires a full-depth extractor.
8. **Biological encoding parser.** Requires domain-specific adapter work.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and `E8` structures.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
7. A. M. Lesk, *Introduction to Bioinformatics*, 4th ed., Oxford University Press, 2019. Protein structure and contact maps.
8. J. M. Thornton, D. T. Jones, *Protein Structure Prediction*, Methods in Molecular Biology, Humana Press, 2000. Protein folding and prediction.
9. K. T. Simons, C. Kooperberg, E. Huang, D. Baker, "Assembly of protein tertiary structures from fragments with similar local sequences using simulated annealing and Bayesian scoring functions," *J. Mol. Biol.* 268 (1997), 209–225. Protein structure prediction.
10. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.

---

## 10. Data vs Interpretation

### Data-backed (D)

- The residue chart has 16 windows and 14 complete interior windows. (D — `foldforge_descriptor_receipt.json`)
- The contact map is symmetric with zero diagonal and nonzero contacts. (D — `foldforge_descriptor_receipt.json`)
- Local side changes are marked as candidate bifurcations. (D — `foldforge_descriptor_receipt.json`)
- The winding witness has an 8-state operator and a named gap. (D — `foldforge_descriptor_receipt.json`)
- The descriptor remains a candidate until validated. (D — `foldforge_descriptor_receipt.json`)

### Interpretation (I)

- The "protein descriptor" framing is the author's structural reading of the FoldForge tools. (I — the underlying finite checks are (D).)
- The application of the descriptor pattern to later biological work is the author's structural reading of the broader series.

### Fabrication (X)

- None in this paper. All finite claims are (D) verified. The biological validation claims (PDB, native structure, free energy, fold rates, AlphaFold, thermodynamics) are honestly marked as (X) open obligations.

---

## 11. Conclusion

Paper 23 gives FoldForge a real scientific shape: it is a descriptor and receipt kernel for protein-chain observations. The CAM-facing library can make the descriptor lookup immediate, but the descriptor is not the protein. Biological truth begins at the next layer, where PDB, simulation, assay, parser, and thermodynamic receipts are attached.
