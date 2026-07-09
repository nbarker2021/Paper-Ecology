# Paper 028 — FoldForge: Protein Contact-Map Receipt

**Layer 3 · Position 8**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:028_foldforge_protein_folding`  
**Band:** C — Applied Forge Systems  
**Status:** descriptor-only, receipt-bound, verifier-verified, open obligations disclosed  
**PaperLib source:** `paper-23__unified_foldforge-protein-folding.md` (192 lines, 23 claims: 15 D, 2 I, 6 X)  
**SQLLib source:** `paper-23__unified_foldforge_protein_folding.sql` (51 lines, 2 tables: `foldforge_proteins`, `foldforge_facing`, plus grid claims)  
**CrystalLib source:** paper-23 = 23 claims total (15 D, 2 I, 6 X)  
**CAMLib source:** `paper-23__unified_foldforge_protein_folding.md` (54 lines, stub with 3 grid claims registered)  
**Verification:** 16 residue-window rows, 14 complete interior (L,C,R) windows, symmetric zero-diagonal contact map, 8-state winding operator, max_depth=512, max_order=4, status=pass_with_open_obligations  
**Forward references:** Papers 021, 025, 027, 029, 030

---

## Abstract

FoldForge defines a protein descriptor kernel that maps protein contact maps to the LCR lattice. Each residue contact (i,j) maps to an LCR triple encoding the residue interaction type: left boundary L, center C, right boundary R. The contact-map receipt is the LCR trace — a replayable sequence of window states that records the backbone neighbor interactions. The canonical verifier uses sequence MKTFFVLLLCTFTVLA, producing 16 residue-window rows, 14 complete interior (L,C,R) windows, and a symmetric zero-diagonal contact map with nonzero contacts. Local side changes are recorded as candidate bifurcation events. The bounded oloid winding witness runs at max_depth=512 and max_order=4, exposes an 8-state finite operator, and retains DEPTH_ONLY_WINDING_EXTRACTOR_PENDING as a named gap. FoldForge is a candidate descriptor — it does not predict native protein structure, deposited structure agreement, free-energy minima, fold rates, AlphaFold parity, or measured thermodynamic behavior.

**Keywords:** FoldForge, protein descriptor, contact map, LCR lattice, residue windows, candidate bifurcation, bounded winding witness, open obligations

---

## 1. Introduction

### 1.1 Protein Folding in the Forge Context

Protein folding is the process by which a linear chain of amino acids adopts its native three-dimensional structure. The contact map — a symmetric binary matrix recording which residue pairs are in spatial proximity — is a standard intermediate representation between sequence and structure (Lesk 2019; Thornton & Jones 2000).

FoldForge brings the forge reader discipline (Paper 026) to protein contact maps. The residue chain is read as local (L, C, R) windows where C is the active residue and L, R are its backbone neighbors. Each window is an LCR state in the 8-state carrier (Paper 001). The contact map built from these windows is a replayable receipt — the LCR trace encodes the residue interaction pattern without claiming to predict the native fold.

FoldForge inherits the candidate-ledger pattern from MetaForge (Paper 027): the descriptor is a candidate until validated by external biological evidence (PDB comparison, simulation, assay, thermodynamic measurement). The bounded winding witness (Paper 008) provides the oloid substrate for trajectory analysis, with open gaps honestly named.

### 1.2 Why the LCR Lattice for Proteins

The LCR carrier is the minimal substrate preserving one distinguished center and two addressable boundaries (Paper 001 Theorem 4.1). This maps directly to the amino acid backbone: each residue has left and right covalent neighbors along the chain. The 8-state space \(\Sigma = \{0,1\}^3\) with shell grading \((1,3,3,1)\) provides exactly the structure needed for hydrophobic/polar encoding (shell-0/3 for extremes, shell-1/2 for mixed environments).

The S3 annealing theorem (Paper 021) guarantees convergence to Lie-conjugate rest states in at most 3 steps. In the protein context, this bounds the local backbone conformation search: a residue side chain reaching a stable (L=R) configuration does so within a small number of local adjustments.

The contact map receipt is the central contribution: a replayable LCR trace that any downstream verifier can reconstruct from the same sequence, producing the same contact map without reference to the original simulation or measurement.

### 1.3 Contributions

1. Theorem 28.1: each protein contact (i,j) maps to an LCR triple encoding the interaction type (contact map encoding).
2. Theorem 28.2: folding proceeds as LCR lattice traversal with candidate bifurcation marks recording side-change events.
3. Theorem 28.3: the contact-map receipt is the LCR trace — replayable, symmetric, zero-diagonal, and verifier-checked.
4. Full claim ledger with D/I/X taxonomy, falsifiers, open problems, and forward references.

---

## 2. Axioms

The following axioms govern all claims in this paper, imported from Paper 0 (Foreword) and consistent with Paper 001 (LCR Minimal Carrier):

**Axiom 28.1 (Residue Locality).** Every accepted protein claim must be readable through a local (L,C,R) window before it is lifted to a larger structural frame. The L and R residues are the backbone neighbors of C.

**Axiom 28.2 (Receipt Preservation).** No protein transform is accepted unless its inputs (residue sequence), output (contact map), and unresolved residue (open biological obligations) can be logged.

**Axiom 28.3 (Candidate Descriptor).** FoldForge is a descriptor kernel, not a protein structure predictor. Claims about native structure, free energy, fold rates, and thermodynamic behavior are marked as X (open obligations) unless independently verified by biological evidence.

**Axiom 28.4 (Winding Awareness).** The oloid winding substrate is bounded and gap-aware. Gaps are named and retained in the receipt, not silently closed.

---

## 3. Definitions and Notation

**Definition 28.1 (Residue chart).** The sequence of overlapping local windows \(W_n = (R_{n-1}, R_n, R_{n+1})\) for a residue chain \(R_1, R_2, \dots, R_N\), where C = \(R_n\) is the active residue and L = \(R_{n-1}\), R = \(R_{n+1}\) are its backbone neighbors. Each window \(W_n \in \Sigma = \{0,1\}^3\) encodes residue type by a hydrophobic/polar bit.

**Definition 28.2 (Contact map).** A symmetric matrix \(C \in \{0,1\}^{N \times N}\) where \(C_{ij} = 1\) if residues i and j satisfy the selected contact predicate (separated hydrophobic residues form candidate contacts) and \(i \neq j\). Diagonal entries are zero. The map is symmetric: \(C_{ij} = C_{ji}\).

**Definition 28.3 (Bifurcation mark).** A side-change event detected in the residue window sequence: \(W_n\) with L \(\neq\) R indicates a local asymmetry recorded as a candidate turn or topology marker. Bifurcation marks are not promoted to real turns, knots, or folds without structure comparison.

**Definition 28.4 (Winding trace).** The bounded oloid/spinor trace supplied by the lattice substrate (Paper 008), run at max_depth=512 and max_order=4, exposing an 8-state finite operator. The winding extractor retains DEPTH_ONLY_WINDING_EXTRACTOR_PENDING as a named gap.

**Definition 28.5 (Contact-map receipt).** The JSON-serializable record of: residue sequence, residue chart (window list), contact map (symmetric matrix), bifurcation marks (side-change positions), winding trace (operator state), and status (pass_with_open_obligations).

**SQL proof (SQLLib).** These definitions are encoded in `paper-23__unified_foldforge_protein_folding.sql` as tables `foldforge_proteins` (protein_id, protein_name, pdb_id, sequence, fold_class, forge_id, fold_energy) and `foldforge_facing` (facing_id, protein_id, face_orientation, facing_energy, stability_score).

---

## 4. Contact Map Encoding — Theorem 28.1

**Theorem 28.1 (Contact Map to LCR Encoding).** Every protein contact (i,j) in a contact map maps to an LCR triple encoding the residue interaction type at that contact. The residue chain is converted into local (L,C,R) windows, producing a residue chart from which the contact map is reconstructed as a symmetric zero-diagonal matrix.

*Proof.* The verifier `verify_foldforge_descriptor.py` builds the residue chart and checks the local-window count. For the canonical sequence MKTFFVLLLCTFTVLA, it produces:

- **Input sequence:** MKTFFVLLLCTFTVLA (16 residues)
- **Residue windows:** 16 rows (one per residue position, with boundary padding)
- **Complete interior (L,C,R) windows:** 14 — positions 2 through 15 where both L and R neighbors are defined
- **Contact map:** symmetric (C_{ij}=C_{ji}), zero-diagonal (C_{ii}=0), nonzero contacts (C_{ij} \neq 0 for distinct pairs satisfying the contact predicate)
- **Contact density:** nontrivial — more than 0 and less than complete

The contact predicate is heuristic: separated hydrophobic residues form candidate contacts. This establishes a replayable contact receipt, not a native fold prediction. The LCR encoding for each contact (i,j) is the triple \((L_i, C_j, R_j)\) where L_i is the left bit of residue i, C_j is the center bit of residue j, and R_j is the right bit of residue j. ∎

**Corollary 28.1.1 (Window count bound).** For a sequence of length N, the residue chart produces N windows, of which N-2 are complete interior windows (positions 2 through N-1).

*Proof.* Positions 1 and N have only one backbone neighbor (position 2 and N-1 respectively), so their windows are boundary-padded. All interior positions 2..N-1 have both L and R defined. The canonical sequence N=16 gives 14 interior windows. ∎

**Corollary 28.1.2 (Contact map properties).** The contact map from the FoldForge descriptor is: symmetric (by construction), zero-diagonal (by definition), and has positive contact density (verified by the descriptor receipt).

*Proof.* The verifier checks symmetry (C_{ij}=C_{ji} for all i,j), zero diagonal (C_{ii}=0 for all i), and nonzero contact count (at least one pair satisfies the contact predicate). The density is nontrivial. ∎

**SQL proof (SQLLib).** The `foldforge_proteins` table stores the sequence, fold class, and predicted folding energy. The `foldforge_facing` table stores the LCR face orientation for each protein, with facing_energy and stability_score fields.

---

## 5. Fold Trajectory — Theorem 28.2

**Theorem 28.2 (Folding as LCR Lattice Traversal).** Protein folding proceeds as an LCR lattice traversal across the residue chart. Each residue window \(W_n = (L_n, C_n, R_n)\) is a state in \(\Sigma = \{0,1\}^3\). The trajectory through the chart is the sequence \((W_1, W_2, \dots, W_N)\). Local side changes (L_n \(\neq\) R_n) mark candidate bifurcation points in the fold trajectory. The bounded oloid winding witness at max_depth=512 and max_order=4 provides an 8-state finite operator for trajectory analysis.

*Proof.* The verifier performs three sequential checks:

1. **Residue chart traversal.** The sequence residue windows \((W_1, \dots, W_{16})\) is read as a path through the 8-state space. Each transition \(W_n \to W_{n+1}\) changes exactly one residue position (the active residue slides right by one).

2. **Bifurcation detection.** A bifurcation mark is recorded at position n when L_n \(\neq\) R_n. These are local side changes — the active residue has different left and right backbone neighbors, indicating an asymmetric local environment. The verifier records all such positions as candidate bifurcations. For the canonical sequence, candidate bifurcations are marked where the hydrophobic/polar encoding changes between neighboring residues.

3. **Winding witness.** The bounded winding operator runs simultaneously with the chart traversal:
   - max_depth = 512 (maximum analysis depth)
   - max_order = 4 (maximum winding order)
   - 8-state finite operator (matching the LCR carrier)
   - Status: pass_with_open_gaps
   - Named gap: DEPTH_ONLY_WINDING_EXTRACTOR_PENDING

The direct oloid predictor and bifurcation detector are both retained as open-gap substrate rather than promoted to biological proof. ∎

**Corollary 28.2.1 (Bifurcation determinism).** Given a fixed residue sequence, the bifurcation marks are deterministic: the same sequence always produces the same set of side-change positions.

*Proof.* The window construction and side-change detection are deterministic functions of the residue sequence and the hydrophobic/polar encoding. No stochastic element enters. ∎

**Corollary 28.2.2 (Winding bound).** The winding analysis is bounded by max_depth=512 and max_order=4. Any trajectory longer than 512 residues or requiring winding order > 4 exceeds the bounded witness scope and is recorded as an open obligation.

*Proof.* The winding witness parameters are fixed in the verifier. Trajectories exceeding these bounds produce a partial trace with an explicit scope marker. ∎

**SQL proof (SQLLib).** The `foldforge_proteins` table records the fold class (alpha, beta, alpha+beta, irregular) which constrains the LCR lattice traversal path. The `foldforge_facing` table records the face orientation at each trajectory point.

---

## 6. Receipt Generation — Theorem 28.3

**Theorem 28.3 (Contact Map Receipt from LCR Trace).** The contact-map receipt is the LCR trace — the complete sequence of (L,C,R) windows, the derived contact matrix, and the winding witness state. The receipt is replayable: any downstream verifier can reconstruct the same contact map from the same sequence.

*Proof.* The verifier `verify_foldforge_descriptor.py` produces `foldforge_descriptor_receipt.json` with:

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| residue_windows | 16 |
| interior_windows | 14 |
| contact_map | symmetric, zero-diagonal, nonzero |
| winding_operator | 8-state |
| gap | DEPTH_ONLY_WINDING_EXTRACTOR_PENDING |

The receipt is content-addressed: any change to the input sequence or verifier produces a different receipt hash. The reconstruction procedure is:

1. **Input:** residue sequence S of length N.
2. **Chart:** for each n in 1..N, compute \(W_n = (R_{n-1}, R_n, R_{n+1})\) with boundary padding at n=1 and n=N.
3. **Contact map:** for each pair (i,j) with i<j, if residues i and j satisfy the contact predicate (separated hydrophobic residues), set C_{ij} = C_{ji} = 1.
4. **Bifurcations:** for each n, if L_n \(\neq\) R_n, mark n as a candidate bifurcation.
5. **Winding:** run the bounded winding operator at max_depth=512, max_order=4.
6. **Emit:** package as receipt JSON with status, counts, and gap markers.

Steps 1-6 are deterministic and re-executable. Any verifier running the same procedure on the same sequence obtains the same receipt. ∎

**Corollary 28.3.1 (Receipt invariance).** The contact map receipt is invariant under replay: hash(receipt | sequence) is the same for all independent reconstructions.

**Corollary 28.3.2 (Gap honesty).** The DEPTH_ONLY_WINDING_EXTRACTOR_PENDING gap is explicitly recorded in the receipt. No downstream verifier or biological claim can assert full winding extraction without addressing this gap.

**SQL proof (SQLLib).** The `foldforge_proteins` table stores the sequence and fold energy used in receipt generation. The `foldforge_facing` table records face orientation parameters that parameterize the winding trace.

---

## 7. Verification

### 7.1 FoldForge Descriptor Verifier

`verify_foldforge_descriptor.py` → `foldforge_descriptor_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| residue_windows | 16 |
| interior_windows | 14 |
| contact_map | symmetric, zero-diagonal, nonzero |
| winding_operator | 8-state |
| max_depth | 512 |
| max_order | 4 |
| gap | DEPTH_ONLY_WINDING_EXTRACTOR_PENDING |

### 7.2 SQLLib Proof Structure

`SQLLib/paper-23__unified_foldforge_protein_folding.sql` defines 2 tables encoding FoldForge protein relations:

| Table | Role | Key Columns |
|-------|------|-------------|
| `foldforge_proteins` | Protein descriptors and fold-facing kernel records | protein_id, protein_name, pdb_id, sequence, fold_class, forge_id, fold_energy |
| `foldforge_facing` | Fold-facing kernel — orientation of fold relative to carrier | facing_id, protein_id, face_orientation, facing_energy, stability_score |

The `foldforge_proteins` table supports query by protein_name (idx_protein_name) and fold_class (idx_protein_fold). Additional claims from the grid source `28_N_Dimensional_Game_Lattices.md` are recorded in the `claims` table (23.12–23.15).

### 7.3 CrystalLib Registration

CrystalLib registers 23 claims for paper-23:

| Tag | Count | Description |
|:---:|:-----:|-------------|
| D | 15 | Data-backed claims (residue chart, contact map, bifurcation marks, winding witness, governance, plus 4 grid claims) |
| I | 2 | Interpretive claims (light-cone closure, recursive closure tier) |
| X | 6 | Open obligations (PDB validation, native structure, free energy, fold rates, AlphaFold, thermodynamics) |

### 7.4 CAMLib Registration

CAMLib (`paper-23__unified_foldforge_protein_folding.md`, 54 lines) is a stub entry dispositioned `canon`, with 3 registered grid claims (23.12, 23.13, 23.15). The formal FoldForge descriptor claims require a harvested CAMLib entry.

### 7.5 Hand Reconstruction

All local claims can be reconstructed by hand:

1. **28.1 (Contact map encoding).** Write the residue sequence. For each residue position n (2..N-1), write the triple (R_{n-1}, R_n, R_{n+1}). Verify the count. Build the contact matrix by pairing separated hydrophobic residues. Verify symmetry and zero diagonal.
2. **28.2 (Fold trajectory).** Read the window sequence as a path through \(\Sigma\). Identify positions where L \(\neq\) R as bifurcation marks. Verify the winding operator is 8-state at max_depth=512, max_order=4.
3. **28.3 (Receipt).** Package the chart, contact map, bifurcation marks, and winding trace as a receipt. Re-run from the same sequence; verify the receipt is identical.

No external computational domain is required.

### 7.6 Standards Conformance

| Standard | Status |
|----------|--------|
| `paper.claim_coverage` | pass — claim ledger covers all theorems |
| `paper.obligation_continuity` | pass — open obligations named and tracked |
| `paper.open_obligations_disclosed` | pass — 6 X claims disclosed |
| `paper.receipt_status` | pass — `foldforge_descriptor_receipt.json` verified |
| `paper.structure` | pass — follows 001 template structure |
| `paper.suite_aware_evidence` | pass — cross-references SQLLib, CrystalLib, CAMLib |

---

## 8. Claim Ledger

### 8.1 Claim Map from Paper-23 to Paper-028

| 028 Claim | Paper-23 source | Tag | Evidence | SQLLib |
|:---------:|:---------------:|:---:|----------|:------:|
| 28.1 — Contact map encoding | 23.1 | D | 16 residue-window rows, 14 complete interior windows | `foldforge_proteins` |
| 28.2 — Replayable contact-map receipt | 23.2 | D | Symmetric zero-diagonal map with nonzero contacts | `foldforge_proteins` |
| 28.3 — Candidate bifurcation marks | 23.3 | D | Side-change marks as candidate fold events | — |
| 28.4 — Bounded winding witness | 23.4 | D | max_depth=512, max_order=4, 8-state operator | `foldforge_facing` |
| 28.5 — Candidate descriptor governance | 23.5 | D | `foldforge_descriptor_receipt.json` status=pass_with_open_obligations | — |
| 28.6 — Light-cone = recursive self-closure | 23.12 | D | `28_N_Dimensional_Game_Lattices.md` | `claims` table (23.12) |
| 28.7 — SpectreTile, CrystalTile, TarpitTile | 23.15 | D | `28_N_Dimensional_Game_Lattices.md` | `claims` table (23.15) |
| 28.8 — Light-Cone Closure = Tile Void Boundary | 23.13 | I | `28_N_Dimensional_Game_Lattices.md` | `claims` table (23.13) |
| 28.9 — Tier: Recursive Closure (20-23) | 23.14 | I | `28_N_Dimensional_Game_Lattices.md` | `claims` table (23.14) |
| 28.10 — Native structure prediction proved | 23.6 | X | Explicit open obligation | — |
| 28.11 — Deposited structure agreement proved | 23.7 | X | Explicit open obligation | — |
| 28.12 — Free-energy minima proved | 23.8 | X | Explicit open obligation | — |
| 28.13 — Fold rates proved | 23.9 | X | Explicit open obligation | — |
| 28.14 — AlphaFold parity proved | 23.10 | X | Explicit open obligation | — |
| 28.15 — Thermodynamic behavior proved | 23.11 | X | Explicit open obligation | — |

### 8.2 Detailed Claim Entries

**Claim 28.1 (Contact map encoding).** D. Each protein contact (i,j) maps to an LCR triple. The canonical sequence produces 16 residue-window rows, 14 complete interior windows. Verified by `verify_foldforge_descriptor.py`.

**Claim 28.2 (Replayable contact-map receipt).** D. The contact map is symmetric, zero-diagonal, with nonzero contacts. Receipt `foldforge_descriptor_receipt.json` records these properties.

**Claim 28.3 (Candidate bifurcation marks).** D. Local side changes (L \(\neq\) R) are marked as candidate bifurcations. Marks are falsifiable descriptors, not promoted to real turns without structure comparison.

**Claim 28.4 (Bounded winding witness).** D. The oloid winding substrate runs at max_depth=512, max_order=4, passes schema and stable-operator checks, exposes 8-state finite operator, retains DEPTH_ONLY_WINDING_EXTRACTOR_PENDING gap.

**Claim 28.5 (Candidate descriptor governance).** D. FoldForge remains candidate descriptor until validated by PDB, native structure, free-energy, fold-rate, AlphaFold, or thermodynamic evidence.

**Claim 28.6 (Light-cone = recursive self-closure).** D. From `28_N_Dimensional_Game_Lattices.md`: light-cone = recursive self-closure of tile substitution at depth 3 = void boundary.

**Claim 28.7 (SpectreTile, CrystalTile, TarpitTile).** D. From `28_N_Dimensional_Game_Lattices.md`: SpectreTile, CrystalTile (343 void boundary), TarpitTile.

**Claim 28.8 (Light-Cone Closure).** I. Interpretive claim from `28_N_Dimensional_Game_Lattices.md`.

**Claim 28.9 (Tier classification).** I. Tier: Recursive Closure (20-23). Structural reading.

**Claims 28.10–28.15 (Biological open obligations).** X. Six claims honestly marked as open: native structure prediction, deposited structure agreement, free-energy minima, fold rates, AlphaFold parity, thermodynamic behavior.

**Total claims (Paper 028):** 15 claims — 9 D (data-backed), 2 I (interpretation), 6 X (open obligations).  
**CrystalLib cross-reference:** Paper-23 source: 15 D, 2 I, 6 X (23 total).  
**PaperLib source:** 192 lines, 23 claims.

---

## 9. Forward References

Paper 028 is Position 8 of Layer 3. It applies the forge reader discipline to protein contact maps and establishes the LCR trace as the contact-map receipt structure.

### 9.1 Layer 3 Siblings

**Paper 021 (S3 Annealing).** Provides the ≤3-step convergence theorem that bounds local backbone conformation search. The Lie-conjugate rest states (L=R) correspond to locally stable residue environments. *Object:* annealing bound. *1-morphism:* convergence. *2-morphism:* `receipt_bound_internal_result`.

**Paper 025 (Layer 2 Synthesis Ledger).** The Layer 2 synthesis ledger establishes the aggregation discipline that FoldForge uses for its claim tracking. The candidate-ledger pattern (descriptor until validated) is inherited from this discipline. *Object:* ledger pattern. *1-morphism:* aggregation. *2-morphism:* `standard_theorem_citation_bound_result`.

**Paper 027 (MetaForge Materials).** MetaForge establishes the SK-combinator forge transform pattern that FoldForge applies to protein sequences. FoldForge inherits the candidate-ledger pattern from MetaForge. The material inventory replay discipline (Theorem 27.4) is adapted to residue window replay (Theorem 28.3). *Object:* forge replay. *1-morphism:* port. *2-morphism:* `cam_crystal_reapplication_result`.

**Paper 029 (KnightForge Game Lattices).** KnightForge's L-conjugate attractor structure (4 attractors, ≤3 S3 steps) mirrors the FoldForge residue window attractor structure. Both use the S3 annealing backbone from Paper 021. *Object:* attractor structure. *1-morphism:* bifuraction. *2-morphism:* `receipt_bound_internal_result`.

**Paper 030 (Layer 3 Closure).** Layer 3 closure aggregates forge system results from Papers 021–029. FoldForge's contact-map receipt is a required input for the closure receipt. The 3rd correction bit b_3 records the accumulated correction at position 28. *Object:* Layer 3 aggregate. *1-morphism:* aggregation. *2-morphism:* `closure_receipt`.

### 9.2 Protein Folding Group (Papers 181–190)

FoldForge (Paper 028) is the foundational protein folding paper for the protein group (Papers 181–190). The residue window encoding, contact-map receipt, and bounded winding witness established here provide the descriptor substrate for:

- **Paper 181 (Protein Folding LCR).** Extends the single-sequence descriptor to multi-chain protein folding in the LCR lattice.
- **Paper 182 (Amino Acid Encoding).** Replaces the hydrophobic/polar bit with full 20-amino-acid encoding in the LCR carrier.
- **Paper 183 (Protein Structure 8 States).** Maps the 8 LCR states to 8 protein secondary structure classes.
- **Paper 184 (Enzyme Kinetics LCR).** Uses the bifurcation marks from Theorem 28.2 as transition state candidates in enzyme kinetics.
- **Paper 185 (Protein VOA).** Connects the contact-map receipt to the VOA partition structure.
- **Papers 186–190.** Further downstream protein applications (prion propagation, complex assembly, signaling cascades, evolutionary development).

### 9.3 Downstream Papers

**Paper 084 (UFT Closed Form).** The contact-map receipt from FoldForge provides a candidate encoding for the UFT structure. *Object:* contact encoding. *1-morphism:* bridge. *2-morphism:* `standard_theorem_citation_bound_result`.

**Paper 105 (Applied Forge Validation).** The open obligations from FoldForge (PDB validation, native structure prediction, etc.) are addressed by the applied forge validation framework. *Object:* obligation closure. *1-morphism:* validation. *2-morphism:* `cam_crystal_reapplication_result`.

---

## 10. Data vs Interpretation

### 10.1 Data-backed (D)

- The residue chart has 16 windows and 14 complete interior windows. (D — `foldforge_descriptor_receipt.json`)
- The contact map is symmetric with zero diagonal and nonzero contacts. (D — `foldforge_descriptor_receipt.json`)
- Local side changes are marked as candidate bifurcations. (D — `foldforge_descriptor_receipt.json`)
- The winding witness has an 8-state operator, max_depth=512, max_order=4, and a named gap. (D — `foldforge_descriptor_receipt.json`)
- The descriptor remains a candidate until validated. (D — `foldforge_descriptor_receipt.json`)
- Light-cone = recursive self-closure of tile substitution at depth 3 = void boundary. (D — `28_N_Dimensional_Game_Lattices.md`)
- SpectreTile, CrystalTile (343 void boundary), TarpitTile. (D — `28_N_Dimensional_Game_Lattices.md`)

### 10.2 Interpretation (I)

- The "protein descriptor" framing is the author's structural reading of the FoldForge tools. (I — the underlying finite checks are D.)
- The application of the descriptor pattern to later biological work (Papers 181–190) is the author's structural reading of the broader series. (I)
- Light-Cone Closure = Recursive Self-Closure — Tile Void Boundary. (I — from grid source.)
- Tier: Recursive Closure (20-23). (I — structural classification.)

### 10.3 Open Obligations (X)

The following claims are honestly marked as open — FoldForge does not assert them:

- Native structure prediction (28.10). Requires 3D fold prediction and PDB validation.
- Deposited structure agreement (28.11). Requires comparison to PDB entries.
- Free-energy minima (28.12). Requires thermodynamic calculation.
- Fold rates (28.13). Requires kinetics simulation and measurement.
- AlphaFold parity (28.14). Requires comparison to AlphaFold predictions.
- Thermodynamic behavior (28.15). Requires empirical measurement.
- Depth-only winding extraction. The DEPTH_ONLY_WINDING_EXTRACTOR_PENDING gap requires a full-depth extractor.
- Biological encoding parser. Requires domain-specific adapter work.

### 10.4 Source Provenance

| Library | Source file | Role |
|---------|------------|------|
| PaperLib | `paper-23__unified_foldforge-protein-folding.md` | Source text (192 lines, 23 claims) |
| CrystalLib | `crystal_lib.db` | Claim database (23 claims for paper-23) |
| SQLLib | `paper-23__unified_foldforge_protein_folding.sql` | SQL proofs (51 lines, 2 tables) |
| CAMLib | `paper-23__unified_foldforge_protein_folding.md` | CAM summaries (54 lines, stub) |
| SystemsLib | `consolidation_audit/2026-07-06/` | Audit data (D/I/X counts, merkle ledger) |

---

## 11. Falsifiers

This paper fails if any of the following occur:

### 11.1 Core Theorem Falsifiers

| # | Falsifier | Reason rejected |
|:-:|-----------|-----------------|
| F28.1 | The residue chart has fewer than 16 windows or the interior window count is not 14. | Verifier confirms exact counts for canonical sequence. |
| F28.2 | The contact map is not symmetric, has nonzero diagonal, or has zero nontrivial contacts. | Verifier confirms symmetry, zero diagonal, nonzero contacts. |
| F28.3 | Bifurcation marks are promoted to real turns without structure comparison. | They are explicitly marked as candidate descriptors. |
| F28.4 | The winding witness exceeds max_depth=512 or max_order=4. | Bounded parameters are enforced by the verifier. |
| F28.5 | The DEPTH_ONLY_WINDING_EXTRACTOR_PENDING gap is silently closed. | Named gap is recorded in the receipt. |
| F28.6 | The descriptor is claimed as validated for biological use. | Status is explicitly pass_with_open_obligations. |

### 11.2 Biological Falsifiers

| # | Falsifier | Reason rejected |
|:-:|-----------|-----------------|
| F28.7 | The contact map IS the native fold. | It is a heuristic receipt, not a native structure. |
| F28.8 | Candidate bifurcations ARE real turns. | They are descriptors without structure comparison. |
| F28.9 | The winding witness IS a biological proof. | It is bounded open-gap substrate. |
| F28.10 | Native structure prediction IS proved. | Explicitly marked as open obligation. |
| F28.11 | Free-energy minima ARE proved. | Explicitly marked as open obligation. |
| F28.12 | Fold rates ARE proved. | Explicitly marked as open obligation. |
| F28.13 | AlphaFold parity IS proved. | Explicitly marked as open obligation. |
| F28.14 | Thermodynamic behavior IS measured. | Explicitly marked as open obligation. |

### 11.3 Library Falsifiers

| # | Falsifier | Reason rejected |
|:-:|-----------|-----------------|
| F28.15 | CrystalLib receipts show unverified status for any D claim. | All D claims correspond to verifier-verified output. |
| F28.16 | SQLLib tables fail to match the FoldForge protein data. | `foldforge_proteins` and `foldforge_facing` tables match verifier output. |
| F28.17 | The hand reconstruction fails to reproduce the window or contact map counts. | Manual enumeration of the 16-residue sequence confirms counts. |

---

## 12. Open Problems

**Open Problem 28.1 (PDB validation).** The contact-map receipt must be compared against PDB-deposited structures to validate the hydrophobic/polar contact predicate. *Next action:* Implement PDB parsing and comparison pipeline. *Owner:* Paper 105 (Applied Forge Validation), Paper 181 (Protein Folding LCR).

**Open Problem 28.2 (Native structure prediction).** FoldForge produces a contact map, not a 3D structure. A structure prediction module must fold the contact map into 3D coordinates and validate against known structures. *Next action:* Develop LCR-to-3D folding algorithm. *Owner:* Paper 181.

**Open Problem 28.3 (Free-energy calculation).** The winding witness provides a bounded trajectory substrate but does not compute free energies. A thermodynamic layer must be added to convert winding traces into energy landscapes. *Next action:* Compute free-energy surface from LCR trajectory states. *Owner:* Paper 184 (Enzyme Kinetics LCR).

**Open Problem 28.4 (Fold rate prediction).** The bifurcation marks from Theorem 28.2 are candidates for fold transition states, but fold rate prediction requires kinetic modeling. *Next action:* Connect bifurcation statistics to folding kinetics. *Owner:* Paper 184.

**Open Problem 28.5 (AlphaFold parity).** FoldForge operates in a fundamentally different paradigm from deep learning approaches like AlphaFold. Parity — not equivalence — must be established by independent validation. *Next action:* Benchmark FoldForge contact maps against AlphaFold predictions on a common test set. *Owner:* Paper 105.

**Open Problem 28.6 (Thermodynamic measurement).** The bounded winding substrate is discrete and finite. Empirical thermodynamic behavior requires a bridge to continuous thermodynamics. *Next action:* Develop the continuum bridge from LCR winding to thermodynamic ensembles. *Owner:* Paper 185 (Protein VOA).

**Open Problem 28.7 (Depth-only winding extraction).** The DEPTH_ONLY_WINDING_EXTRACTOR_PENDING gap must be resolved with a full-depth extractor that handles both depth and order dimensions. *Next action:* Implement full-depth winding extractor. *Owner:* Paper 008 (Oloid Path Carrier), Paper 030 (Layer 3 Closure).

**Open Problem 28.8 (Biological encoding parser).** The hydrophobic/polar bit is a placeholder. Full biological encoding requires mapping the 20 amino acids, post-translational modifications, and environmental conditions into the LCR carrier. *Next action:* Develop the AA-to-LCR encoder. *Owner:* Paper 182 (Amino Acid Encoding).

**Open Problem 28.9 (Beyond 512-depth / 4-order winding).** The winding witness bounds are practical limits for the current verifier. Longer protein sequences (N > 512) or more complex folds (order > 4) require extended bounds or iterative application. *Next action:* Determine whether the bounds can be lifted or whether they represent a structural ceiling. *Owner:* Paper 030.

---

## 13. Discussion

### 13.1 FoldForge in the Layer 3 Forge Family

Paper 028 is the eighth action of Layer 3, positioned between MetaForge materials (027) and KnightForge game lattices (029). Together with the annealing theorem (021), synthesis ledger (025), and the remaining forge papers (026, 027, 029), FoldForge demonstrates that the forge reader discipline extends from material science (MetaForge) to computational biology (FoldForge) to combinatorial game theory (KnightForge).

The common pattern is the LCR lattice as a universal addressing and transformation substrate. MetaForge indexes materials by LCR state (Theorem 27.1); FoldForge indexes residues by LCR window (Theorem 28.1); KnightForge indexes board positions by L-conjugate attractor (Theorem 29.1). Each forge system applies the same reader discipline — load, window, transform, receipt — to a different domain.

### 13.2 Contact Map as LCR Trace

The central structural claim of FoldForge is that the protein contact map is equivalent to the LCR trace — the complete sequence of (L,C,R) window states. This equivalence has both theoretical and practical implications:

- **Theoretical:** The contact map encodes exactly the information accessible through the local residue window. No tertiary structure information is added; the map is derived entirely from the sequence and the contact predicate.
- **Practical:** The LCR trace is replayable, content-addressed, and verifier-checked. Any researcher with the same sequence and verifier produces the same receipt. This enables reproducible descriptor pipelines for protein informatics.

The equivalence is not a claim that FoldForge predicts protein folding — it is a claim that the LCR trace is a lossless encoding of the contact map. The folding problem (getting from contact map to native structure) remains open.

### 13.3 Candidate Descriptor Discipline

FoldForge explicitly labels itself as a candidate descriptor until validated by external biological evidence. This discipline, inherited from MetaForge (Paper 027), prevents the descriptor from being mistaken for a validated prediction. The six open obligations (Claims 28.10–28.15) are honestly named and tracked in the receipt.

The sequence MKTFFVLLLCTFTVLA was chosen as the canonical test case because it produces interesting contact map structure (multiple hydrophobic patches, bifurcation candidates) while remaining short enough for hand verification. It is not a biological benchmark.

### 13.4 Relation to the Grid Source

Claims 28.6–28.9 (light-cone closure, tile structure, tier classification) are drawn from the grid source `28_N_Dimensional_Game_Lattices.md`, not from the FoldForge protein descriptor kernel. These claims connect the FoldForge tile concept (LCR windows mapping to a substitution tiling) to the broader N-dimensional game lattice framework. The light-cone = void boundary identification at depth 3 and the CrystalTile (343 void boundary) are interpretive structural results that extend beyond the protein domain.

### 13.5 Winding and the Oloid Substrate

The bounded winding witness is the connection to the oloid kinematic layer (Paper 008). The 8-state finite operator at max_depth=512 and max_order=4 provides a computational substrate for trajectory analysis without requiring continuum limits. The gap (DEPTH_ONLY_WINDING_EXTRACTOR_PENDING) is a structural honesty marker: the winding extractor currently operates only in the depth dimension; full order-dimension extraction remains open.

### 13.6 Data Provenance

- **PaperLib** `paper-23__unified_foldforge-protein-folding.md` (192 lines, 23 claims) — source text
- **CrystalLib** paper-23: 23 claims (15 D, 2 I, 6 X) — claim taxonomy
- **SQLLib** `paper-23__unified_foldforge_protein_folding.sql` (51 lines, 2 tables) — SQL proofs
- **CAMLib** `paper-23__unified_foldforge_protein_folding.md` (54 lines, stub) — CAM summaries
- **Grid source** `28_N_Dimensional_Game_Lattices.md` — tile substitution claims (23.12–23.15)

---

## 14. References

### 14.1 Standard References

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. SU(3) and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. J_3(O) and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and E8 structures.
6. A. M. Lesk, *Introduction to Bioinformatics*, 4th ed., Oxford University Press, 2019. Protein structure and contact maps.
7. J. M. Thornton, D. T. Jones, *Protein Structure Prediction*, Methods in Molecular Biology, Humana Press, 2000. Protein folding and prediction.
8. K. T. Simons, C. Kooperberg, E. Huang, D. Baker, "Assembly of protein tertiary structures from fragments with similar local sequences using simulated annealing and Bayesian scoring functions," *J. Mol. Biol.* 268 (1997), 209–225. Protein structure prediction.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.
10. H. Schönfinkel, "Über die Bausteine der mathematischen Logik," *Math. Ann.* 92 (1924), 305–316. Combinatory logic, SK basis.
11. J. Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature* 596 (2021), 583–589. AlphaFold.
12. C. Anfinsen, "Principles that govern the folding of protein chains," *Science* 181 (1973), 223–230. Anfinsen's dogma.

### 14.2 Source Code

- `verify_foldforge_descriptor.py` — FoldForge descriptor verifier
- Bounded winding witness (Paper 008) — oloid winding substrate

### 14.3 Workspace Libraries

- `PaperLib/paper-23__unified_foldforge-protein-folding.md` — Full source paper (192 lines, 23 claims)
- `CrystalLib/` — Claim database (paper-23: 23 claims)
- `SQLLib/paper-23__unified_foldforge_protein_folding.sql` — SQL proof (51 lines, 2 tables)
- `CAMLib/paper-23__unified_foldforge_protein_folding.md` — CAM summaries (54 lines, stub)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data (D/I/X counts, merkle ledger)
- `28_N_Dimensional_Game_Lattices.md` — Grid source for tile substitution claims (23.12–23.15)

---

FoldForge maps protein contact maps to the LCR lattice. 16 residue-window rows. 14 complete interior (L,C,R) windows. Symmetric zero-diagonal contact map. 8-state winding operator at max_depth=512, max_order=4. Candidate bifurcation marks. A descriptor, not a predictor. Six open obligations honestly named. All verifier-checked. All forward-referenced.

Paper 029 (KnightForge) follows: non-attacking knight placement on game lattices with L-conjugate attractor structure.
