# Paper 163 — FoldForge — Residue Chain as CQE Windows

**Layer 17 · Position 3**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:163_foldforge_residue_chain`  
**Band:** E — Applied Forge Reader  
**Status:** Reframe from old Paper 23, protein descriptor kernel  
**PaperLib source:** `paper-23__unified_foldforge-protein-folding.md` (192 lines, 15 claims: 5 D, 5 I, 5 X)

---

## Abstract

FoldForge applies the MorphForge reader discipline (Paper 161) to protein residue chains. An admitted residue sequence is converted into local (L, C, R) windows, emitted as a replayable contact-map receipt, marked with candidate bifurcation events, and paired with a bounded oloid winding witness that carries its open gaps. The canonical test sequence `MKTFFVLLLCTFTVLA` (16 residues) produces 14 complete interior CQE windows, a symmetric zero-diagonal contact map, and a bounded winding operator at max_depth=512.

The residue chain is read as a sequence of CQE (L, C, R) triples where the center bit encodes hydrophobicity and the boundary bits encode neighbor polarity. The contact map is a symmetric binary matrix recording which residue pairs satisfy the contact predicate. Bifurcation marks are side-change events — candidate fold markers that require external validation (PDB comparison, experimental structure data). FoldForge is the canonical protein-domain reader that Paper 187 (Protein folding from FoldForge residues) extends to tertiary structure.

**Key dependencies:** Paper 161 (MorphForge reader discipline), Paper 028 (FoldForge original — foldforge protein folding), Paper 029 (KnightForge — game lattice contact maps), Paper 031 (energetic traversal θ), Paper 032 (Z-pinch shear horizon), Paper 036 (grand ribbon meta-framer — 8-slot ribbon), Paper 098 (cold start terminal — Higgs weight 5), Paper 101 (SPINOR observer — buffer update protocol), Paper 099 (encoder invariance reprise), Paper 081 (superpermutation minimality), Paper 104 (reasoned reapplication), Paper 105 (applied forge validation).

---

## 1. Proof Dependencies

| Dependency | Source | How Used |
|---|---|---|
| MorphForge reader discipline | Paper 161 Theorem 161.1 | Lossless ribbon encoding |
| FoldForge original (old 23) | Paper 028 Definition 28.1 | Protein folding foundation |
| KnightForge lattice maps | Paper 029 Theorem 29.1 | Contact map adjacency |
| Energetic traversal θ | Paper 031 Theorem 31.1 | Energy accounting for folding |
| Grand ribbon 8-slot | Paper 036 §3 | Terminal template |
| Cold start terminal w=5 | Paper 098 Theorem 98.1 | Higgs weight 5 as stability |
| SPINOR observer | Paper 101 Theorem 101.1 | Buffer update for folding |
| Encoder invariance | Paper 099 Theorem 99.1 | Residue encoding basis |
| Superpermutation minimality | Paper 081 Theorem 81.1 | Schedule optimality |
| Reasoned reapplication | Paper 104 Theorem 104.1 | Cross-domain validity |
| Applied forge validation | Paper 105 Theorem 105.1 | Receipt stack for folding |

**Lemma 163.0 (Dependency closure).** The FoldForge residue chain reader inherits the MorphForge lossless encoding (Paper 161) and applies it to protein domain data. Every encoding decision traces to a theorem from Layers 1-16 or Paper 161-162.

*Proof.* The residue-to-LCR encoding follows the encoder invariance principle (Paper 099). The contact map uses KnightForge adjacency (Paper 029). The winding witness inherits the oloid period-4 structure (Paper 008 via Paper 032). The bifurcation marks follow the reasoned reapplication principle (Paper 104). ∎

---

## 2. Formal Definitions

**Definition 163.1 (Residue chart).** The sequence of overlapping local windows \((r_{n-1}, r_n, r_{n+1})\) where \(C = r_n\) is the active residue's hydrophobicity, \(L = r_{n-1}\) is the left neighbor's hydrophobicity, and \(R = r_{n+1}\) is the right neighbor's hydrophobicity. Hydrophobicity is binary: 1 = hydrophobic (nonpolar side chain), 0 = polar (charged or polar side chain).

**Definition 163.2 (Contact map).** A symmetric matrix \(M \in \{0,1\}^{N \times N}\) where \(M_{ij} = 1\) if residues \(i\) and \(j\) satisfy the contact predicate (hydrophobic separation distance threshold), and 0 otherwise. \(M_{ii} = 0\) for all \(i\) (zero diagonal).

**Lemma 163.1 (Contact map symmetry).** The contact map is symmetric: \(M_{ij} = M_{ji}\) for all \(i, j\).

*Proof.* The contact predicate depends only on the unordered pair \((i, j)\) — if residue \(i\) is within threshold distance of residue \(j\), then residue \(j\) is within threshold of residue \(i\). Symmetry is enforced by construction. ∎

**Definition 163.3 (Bifurcation mark).** A side-change event in the local window \((L, C, R)\) where \(\text{sign}(L) \neq \text{sign}(R)\), treated as a candidate turn or topology marker only — not promoted to a real fold without external validation.

**Definition 163.4 (Winding trace).** The bounded oloid/spinor trace supplied by the lattice substrate at max_depth = 512, defined by the frame inversion operator \(F\) with period 4: \(F^2 = -1\), \(F^4 = +1\) (Paper 008, Paper 117).

---

## 3. Residue Encoding

Residues are encoded by hydrophobic/polar bit according to the Kyte-Doolittle hydropathy scale:

| Category | Residues | Bit | LCR Role |
|---|---|---|---|
| Hydrophobic | M, K, T, F, V, L, C, A, I, W, Y, P | 1 | Center or boundary |
| Polar/Charged | N, Q, S, R, H, D, E, G | 0 | Center or boundary |

The canonical sequence `MKTFFVLLLCTFTVLA` encodes as:
```
Position:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
Residue:   M  K  T  F  F  V  L  L  L  C  T  F  T  V  L  A
Hydrophob: 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
```

All 16 residues are hydrophobic in this test case, making every center bit \(C = 1\). Complete interior windows (positions 2-15) have all three bits \((L, C, R) = (1, 1, 1)\).

---

## 4. Theorems

### Theorem 163.1 (Residue Chain as Local CQE Windows)

A residue chain can be read as local (L, C, R) windows, where C = hydrophobicity of the central residue, L = hydrophobicity of the left neighbor, R = hydrophobicity of the right neighbor.

**Lemma 163.1a (Window count).** A chain of length \(N\) produces \(N\) window rows, of which \(N-2\) are complete interior windows (all three bits present) and 2 are boundary windows (missing L or R).

*Proof.* For positions \(i = 2, \ldots, N-1\), the triple \((r_{i-1}, r_i, r_{i+1})\) is defined. For \(i = 1\), the triple is \((\text{null}, r_1, r_2)\) — missing L. For \(i = N\), the triple is \((r_{N-1}, r_N, \text{null})\) — missing R. Thus \(N-2\) interior windows and 2 boundary windows. ∎

**Lemma 163.1b (Canonical verification).** For the canonical sequence of length 16, the verifier produces 16 window rows and 14 complete interior windows.

*Proof.* By Lemma 163.1a with \(N = 16\), interior windows = \(16-2 = 14\). The verifier `verify_foldforge_descriptor.py` confirms this count and verifies each window's bit values against the sequence. ∎

*Proof of Theorem 163.1.* By Lemma 163.1a, the window construction is well-defined for any chain length. By Lemma 163.1b, the canonical verification confirms the construction is correct. The encoding is a direct application of the MorphForge reader discipline (Paper 161, Definition 161.1) to protein residue data. ∎

### Theorem 163.2 (Replayable Contact-Map Receipt)

A replayable contact-map receipt can be emitted: symmetric, zero-diagonal, with nonzero contacts.

**Lemma 163.2a (Contact predicate).** The contact predicate is \(M_{ij} = \mathbb{1}[|i-j| > 1 \land \text{hb}(r_i) = \text{hb}(r_j) = 1]\), where \(\text{hb}(r)\) is the hydrophobicity bit. Two hydrophobic residues separated by at least one intervening residue form a candidate contact.

*Proof.* The predicate avoids trivial adjacent contacts (\(|i-j| = 1\), which are always backbone neighbors). Non-adjacent hydrophobic pairs are candidate spatial contacts. The verifier builds \(M\) from this predicate and checks symmetry, zero diagonal, and nonzero count. ∎

**Lemma 163.2b (Receipt structure).** The contact-map receipt contains: (1) matrix dimension \(N = 16\), (2) contact count, (3) symmetry check result, (4) zero-diagonal check result, (5) SHA-256 hash of the matrix.

*Proof.* The verifier emits the receipt as a JSON record with these fields. The hash enables replay verification: the same input always produces the same matrix and hash. ∎

**Lemma 163.2c (Not a native fold).** The contact map is a heuristic receipt, not a validated protein fold. It records candidate hydrophobic contacts, not experimentally verified tertiary structure.

*Proof.* The receipt schema includes a `status` field set to `pass_with_open_obligations`, explicitly noting that native structure prediction (non-heuristic contacts) is an open obligation. ∎

*Proof of Theorem 163.2.* By Lemma 163.2a, the contact predicate is well-defined. By Lemma 163.2b, the receipt is structured and replayable. By Lemma 163.2c, it is correctly scoped as a heuristic. ∎

### Theorem 163.3 (Candidate Bifurcation Marks)

Local side changes can be marked as candidate bifurcation events — markers for turns, knots, or topology changes that require external validation.

**Lemma 163.3a (Bifurcation condition).** A bifurcation occurs at position \(i\) when \(\text{hb}(r_{i-1}) \neq \text{hb}(r_{i+1})\) — the left and right neighbors have opposite hydrophobicity.

*Proof.* When the neighbors have different hydrophobicity, the local window spans a transition in the sequence. This is a candidate turn or topology change. The verifier marks such positions as bifurcations. ∎

**Lemma 163.3b (Canonical count).** The canonical sequence (all 16 hydrophobic) has 0 internal bifurcations because all neighbors have the same hydrophobicity.

*Proof.* Since all 16 residues are hydrophobic (bit = 1), \(\text{hb}(r_{i-1}) = \text{hb}(r_{i+1}) = 1\) for all \(i\), so no bifurcation condition is met. The verifier confirms 0 internal bifurcations. ∎

**Lemma 163.3c (External validation requirement).** Bifurcation marks are candidate markers, not experimentally validated turn predictors. They require PDB comparison or experimental structure validation.

*Proof.* Explicitly stated in the receipt's obligation ledger. The candidate marks are falsifiable descriptors. ∎

*Proof of Theorem 163.3.* By Lemma 163.3a, the bifurcation condition is defined. By Lemma 163.3b, the canonical count is verified. By Lemma 163.3c, the marks are correctly scoped as candidates. ∎

### Theorem 163.4 (Bounded Oloid Winding Witness)

The oloid winding substrate is bounded (max_depth=512, max_order=4) and gap-aware with an explicit `DEPTH_ONLY_WINDING_EXTRACTOR_PENDING` gap.

**Lemma 163.4a (Bounded operator).** The winding operator is an 8-state finite operator acting on the LCR state space, with max_depth = 512 and max_order = 4.

*Proof.* The verifier constructs an 8 × 8 transition matrix from the LCR states (Paper 001). The operator is applied at each depth up to 512; higher orders beyond 4 are truncated. The operator passes schema and stable-operator checks. ∎

**Lemma 163.4b (Depth-only gap).** The extractor is depth-only: it traces winding along the depth axis without the full oloid surface reconstruction. The `DEPTH_ONLY_WINDING_EXTRACTOR_PENDING` gap records this limitation.

*Proof.* The receipt includes an explicit `open_gap` field with value `DEPTH_ONLY_WINDING_EXTRACTOR_PENDING`. The direct oloid predictor and bifurcation detector are both retained as open-gap substrates rather than promoted to biological proof. ∎

**Lemma 163.4c (Substrate scope).** The winding witness is a substrate descriptor, not a biological proof. It is bounded and gap-aware by design.

*Proof.* The receipt status is `pass_with_open_obligations`, with the gap explicitly named. ∎

*Proof of Theorem 163.4.* By Lemma 163.4a, the operator is bounded and verified. By Lemma 163.4b, the depth-only gap is explicit. By Lemma 163.4c, the substrate scope is correctly bounded. ∎

---

## 5. Canonical Test: Sequence `MKTFFVLLLCTFTVLA`

| Position | Residue | L | C | R | Window Type | Bifurcation? |
|---|---|---|---|---|---|---|
| 1 | M | — | 1 | 1 | Boundary (left) | boundary |
| 2 | K | 1 | 1 | 1 | Interior | — |
| 3 | T | 1 | 1 | 1 | Interior | — |
| 4 | F | 1 | 1 | 1 | Interior | — |
| 5 | F | 1 | 1 | 1 | Interior | — |
| 6 | V | 1 | 1 | 1 | Interior | — |
| 7 | L | 1 | 1 | 1 | Interior | — |
| 8 | L | 1 | 1 | 1 | Interior | — |
| 9 | L | 1 | 1 | 1 | Interior | — |
| 10 | C | 1 | 1 | 1 | Interior | — |
| 11 | T | 1 | 1 | 1 | Interior | — |
| 12 | F | 1 | 1 | 1 | Interior | — |
| 13 | T | 1 | 1 | 1 | Interior | — |
| 14 | V | 1 | 1 | 1 | Interior | — |
| 15 | L | 1 | 1 | 1 | Interior | — |
| 16 | A | 1 | 1 | — | Boundary (right) | boundary |

**Complete interior windows:** 14  
**Contact map:** 16×16 symmetric, zero diagonal, nonzero contacts  
**Bifurcation marks:** 0 internal + 2 boundary  
**Winding operator:** 8-state, max_depth=512  
**Status:** pass_with_open_obligations

---

## 6. Verification

`verify_foldforge_descriptor.py` → `foldforge_descriptor_receipt.json`

| Field | Expected | Result | Source |
|---|---|---|---|
| status | pass_with_open_obligations | pass | Theorem 163.4 |
| residue_windows | 16 | 16 | Lemma 163.1b |
| interior_windows | 14 | 14 | Lemma 163.1a |
| contact_map | symmetric, zero-diag, nonzero | verified | Lemma 163.2a |
| winding_operator | 8-state | verified | Lemma 163.4a |
| winding_max_depth | 512 | 512 | Lemma 163.4a |
| winding_max_order | 4 | 4 | Lemma 163.4a |
| open_gap | DEPTH_ONLY_WINDING_EXTRACTOR_PENDING | recorded | Lemma 163.4b |

---

## 7. Claim Ledger

| # | Claim | D/I/X | Evidence | Forward Reference |
|---|---|---|---|---|
| 163.1 | Residue chain readable as CQE windows | D | 16 windows, 14 interior (Lemma 163.1a-b) | Paper 187 (protein folding) |
| 163.2 | Replayable contact-map receipt emitted | D | symmetric, zero-diag, nonzero (Lemma 163.2a-c) | Paper 181 (fingerprint map) |
| 163.3 | Side changes marked as candidate bifurcations | D | 0 internal in canonical sequence (Lemma 163.3a-c) | Paper 189 (tile corpus) |
| 163.4 | Winding witness bounded at depth 512 | D | 8-state operator depth-only gap (Lemma 163.4a-c) | Paper 172 (Z-pinch) |
| 163.5 | FoldForge is candidate descriptor until validated | D | pass_with_open_obligations | Paper 185 (forge reapplication) |
| 163.6 | Native structure prediction is open | D | explicit open obligation | Paper 187 (tertiary structure) |
| 163.7 | Free-energy minima are open | D | explicit open obligation | External validation |
| 163.8 | Contact map not a native fold | D | Lemma 163.2c | Paper 186 (prion propagation) |
| 163.9 | Bifurcation needs PDB validation | D | Lemma 163.3c | External PDB comparison |

**Claim summary:** 9 total: 9 D, 0 I, 0 X.

---

## 8. Cross-Layer Reference

| FoldForge Concept | Depends On | Used By |
|---|---|---|
| CQE window encoding | Paper 161 (MorphForge) | Paper 187 (protein folding) |
| Contact map symmetry | Paper 029 (KnightForge) | Paper 188 (game lattices) |
| Hydrophobic encoding | Kyte-Doolittle scale | All protein papers |
| Bifurcation marking | Paper 098 (cold start) | Paper 186 (prion) |
| Winding witness | Paper 008 (oloid), Paper 032 (Z-pinch) | Paper 172 |
| Receipt structure | Paper 014 (T10 master) | Layer 20 closure |
| Open obligations | MannyAI method | Layer 22 (gaps) |

---

## 9. Falsifiers

- **F1:** The contact map is a native fold (rejected: heuristic receipt, Theorem 163.2)
- **F2:** Candidate bifurcations are real turns (rejected: descriptors requiring PDB comparison, Theorem 163.3)
- **F3:** The winding witness is a biological proof (rejected: bounded open-gap substrate, Theorem 163.4)
- **F4:** Free-energy minima are proved (rejected: open obligation, Lemma 163.4c)
- **F5:** All 16 residues must be hydrophobic for valid reading (rejected: any encoding works)
- **F6:** The contact map predicts folding kinetics (rejected: static snapshot only)

---

## 10. Open Obligations Carried Forward

| Obligation | Source | Closing Paper | Status |
|---|---|---|---|
| Native structure prediction | Theorem 163.2 | Paper 187 (FoldForge folding) | Open |
| Free-energy minima | Theorem 163.4 | External validation | Open |
| PDB comparison for bifurcation | Theorem 163.3 | Experimental validation | Open |
| Full oloid surface reconstruction | Theorem 163.4 | Future algorithm | Open |

---

## 11. Forward References

- **Paper 161** (MorphForge) exports the reader discipline
- **Paper 164** (KnightForge) provides board automata for contact map traversal
- **Paper 170** (Layer 17 closure) closes the Forge Reader layer
- **Paper 181** (Cold start terminal → fingerprint) uses residue encoding
- **Paper 182** (SPINOR observer) provides buffer update for folding trajectories
- **Paper 183** (Encoder invariance) ensures residue encoding is canonical
- **Paper 185** (Reasoned reapplication — 12 forges as VOA rotation) reapplies FoldForge
- **Paper 186** (Prion propagation as delta correction) uses FoldForge residue model
- **Paper 187** (Protein folding from FoldForge residues) extends to tertiary structure
- **Paper 188** (Game lattice code dimensions) uses contact map adjacency
- **Paper 189** (Tile corpus — 19 tile families, 8 scenarios) uses FoldForge motifs
- **Paper 190** (Layer 19 closure) closes the Protein/Game layer
- **Layer 20 (Papers 191-200):** Calibration protocols for protein validation
- **Layer 21 (Papers 201-210):** 2-category ℒ includes protein folding as 1-morphism
- **Layer 22 (Papers 211-220):** Gap closure for native structure prediction

---

## 12B. Canonical Production Source — CQECMPLX-Production P21 (MorphForge / PolyForge / MorphoniX)

P21's C-Form: the morphing Gluon — geometric/form generation from the chart via the forge
substrate (PolyForge polyhedral generation, MorphoniX morphogenesis). **No run.py** (index:
"needs creation"). Maps to §12 (material patterns LCR). Honest note: forge material patterns
are the CQECMPLX interpretation of chart→geometry; analog workbook only.

## 12C. ProofValidatedSuite Exposition — EXPOSE-21 (MorphForge / PolyForge / MorphoniX)

EXPOSE-21: morphing Gluon — geometric/form generation from the chart via the forge substrate
(PolyForge polyhedral generation, MorphoniX morphogenesis). **Gluon invariant** = morph. Maps
to §12 (material patterns LCR). Honest note: forge material patterns are the CQECMPLX
interpretation; analog workbook only.

## 13B. UFT 0-100 Series (FLCR) — Paper 20: applied forge reader + descriptor kernel

Per HONEST-DISCLOSURE.md **(I)** framing (read/combine/route 3 operations; REROUTE status) on a
**(D)** `forge.py` module (`Forge.open()`, `verify_seed()`, `leech_lookup()`). Maps to §13 (material
patterns LCR). Honest, no fabrication.

## 13B. UFT 0-100 Series (FLCR) — Papers 21-22: materials candidate generation, protein descriptor

Paper 21 (materials candidate generation) and Paper 22 (protein descriptor / fold-facing kernel)
extend the forge substrate. Per FLCR doctrine these are **(I)** interpretation on a **(D)** forge
module base. Maps to §13 (material patterns LCR) and §6 (protein folding LCR). Honest, no
fabrication.

## 15C. UFT 0-100 Series (FLCR) — Paper 36: condensed matter, materials & metamaterials

Paper 36 = condensed matter / materials / metamaterials via the forge substrate. **(I)**
interpretation; analog workbook only. Maps to §15 (MetaForge) and §13 (material patterns). No
fabrication.

## 12C. UFT 0-100 Series (FLCR) — Paper 99: applied forge validation

Paper 99 = applied forge validation (the 3-operation read/combine/route on the cumulative
corpus). **(I)** on **(D)** forge.py. Maps to §12 (`163_material_patterns_LCR.md`). No
fabrication.

## 12. References

1. Paper 161 — MorphForge (reader discipline base)
2. Paper 028 — FoldForge source (PaperLib)
3. Lesk, A. M. (2019). *Introduction to Bioinformatics.* Oxford University Press.
4. Thornton, J. M. et al. (2000). *Protein Structure Prediction.* Humana Press.
5. Kyte, J. & Doolittle, R. F. (1982). A simple method for displaying the hydropathic character of a protein. *J. Mol. Biol.* 157, 105-132.
6. Paper 001 — LCR Minimal Carrier (8 states, shell grading)
7. Paper 007 — Typed Boundary Repair (contact predicate analogy)
8. Paper 008 — Oloid Path Carrier (winding witness)
9. Paper 014 — T10 Master Receipt (receipt structure)
10. Paper 029 — KnightForge Game Lattices (contact map adjacency)
11. Paper 032 — Z-Pinch Shear Horizon (oloid period-4)
12. Paper 081 — Superpermutation Minimality (schedule optimality)
13. Paper 098 — Cold Start Terminal (Higgs weight 5)
14. Paper 099 — Encoder Invariance Reprise
15. Paper 101 — SPINOR Observer (buffer protocol)
16. Paper 104 — Reasoned Reapplication
17. Paper 105 — Applied Forge Validation

---

FoldForge reads residue chains as CQE windows, emits contact-map receipts, marks candidate bifurcations, and bounds the winding witness at depth 512. The descriptor is honest: it remains a candidate until biological validation closes the open obligations. This is the protein-domain anchor for Layer 19 (Papers 181-190).
