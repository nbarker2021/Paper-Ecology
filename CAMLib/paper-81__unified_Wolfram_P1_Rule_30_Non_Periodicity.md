# Paper 81: Wolfram P1: Rule 30 Non-Periodicity

**Domain:** Wolfram P1  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim C1: Non-Periodicity Conjecture
- **Claim Text:** The Rule 30 center column (from single-cell seed) is conjectured non-periodic at all depths.
- **CAM Hash:** `sha256:claim81_c1`
- **CodeLib Source:** `D:/CodeLib/paper-81__unified_Wolfram_P1_Rule_30_Non_Periodicity.py`
- **SQLLib Source:** `D:/SQLLib/paper-81__unified_Wolfram_P1_Rule_30_Non_Periodicity.sql`
- **Status:** `harvested`
- **Verifier:** Wolfram 2002, NKS Chapter 12; conjecture, not theorem.

### Claim C2: 1M-Bit Data File
- **Claim Text:** The 1M-bit center column data file exists and is reproducible.
- **CAM Hash:** `sha256:claim81_c2`
- **Status:** `harvested`
- **Verifier:** `D:/CQE_CMPLX/CMPLX-R30-main/DATA/wolfram-rule30-center/wolfram_rule30_center_1m.json` (2,000,008 bytes, 1,000,000 bits).

### Claim C3: No Period ≤ 100,000
- **Claim Text:** No period p ≤ 100,000 was found in the 1M-bit center column.
- **CAM Hash:** `sha256:claim81_c3`
- **Status:** `harvested`
- **Verifier:** Empirical exhaustive search: for each p ∈ [1, 100,000], verified seq[i] ≠ seq[i+p] for some i.

### Claim C12: Rule 30 Corpus
- **Claim Text:** The Rule 30 function corpus spans 249 verified files across the D:\ drive.
- **CAM Hash:** `sha256:claim81_c12`
- **Status:** `harvested`
- **Verifier:** `gap_analysis.md` (2026-07-03); `rule30.py`, `fast_rule30.py`, `rule30_decomposition.py`, `rule30_block_extractor.py`

### Claim C13: Historical Frozen Dataclass
- **Claim Text:** Historical `rule30.py` (frozen dataclass version, 277.8 KB) exists in drive_audit archives with algebraic Monomial/Poly types, but the active version uses regular classes.
- **CAM Hash:** `sha256:claim81_c13`
- **Status:** `harvested`
- **Verifier:** `bipartite_review_part_a_historical.md` (2026-07-03); frozen dataclass pattern for thread safety

### Claim C14: 1M-Bit File Duplicates
- **Claim Text:** The `wolfram_rule30_center_1m.json` data file (1,000,000 bits) appears in 22 duplicate instances across CQE_CMPLX_main, _Archive, drive_audit, and repo_harvest trees.
- **CAM Hash:** `sha256:claim81_c14`
- **Status:** `harvested`
- **Verifier:** `deduplication_report.md` (2026-07-03); 22 mirrors, 42.0 MB total duplicated

---

## Cross-References
- [Paper 02: Correction Surface](paper-02__unified_correction_surface_and_rule30_decomposition.md)
- [Paper 04: Boundary Repair](paper-04__unified_boundary_repair.md)
- [Paper 05: Oloid Path Carrier](paper-05__unified_oloid_path_carrier.md)
- [Paper 82: Wolfram P2](paper-82__unified_Wolfram_P2_Rule_30_Density_1_2.md)
- [Paper 83: Wolfram P3](paper-83__unified_Wolfram_P3_Rule_30_Sub_O_n_Extraction.md)
- [Paper 86: Riemann Hypothesis](paper-86__unified_Riemann_Hypothesis_Critical_Line_as_Big_Bang_Crease.md)
- [Paper 90: McKay-Thompson Parity](paper-90__unified_McKay_Thompson_Parity_and_Rule_30_Correction_Collapse.md)
- [Paper 100: Capstone](paper-100__unified_Capstone_100_Paper_Series_and_Complete_Framework_Synthesis.md)

---

## Recovery Notes
3LSR Stub: Reference entries pending formal paper harvest. Domain: Wolfram P1.

---




## New Mapped Claims

### Claim 81.1
- **Claim Text:** *Owner:* Paper 2 (Lucas carry closed form) and Paper 81 (Rule 30 non-periodicity)
- **Status:** D
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_1`

### Claim 81.2
- **Claim Text:** *Why not closed:* the unbounded proof is the P1 Millennium-class problem (Paper 81)
- **Status:** D
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_2`

### Claim 81.3
- **Claim Text:** *Next binding action:* Paper 81 must give the unbounded proof via the Lucas carry closed form and the cold-start O(log N) readout
- **Status:** D
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_3`

### Claim 81.4
- **Claim Text:** The verification is closed at depth 1024 by Theorem 7.1; the unbounded extension is the subject of Paper 81 (Wolfram P1, non-periodicity) and Paper 83 (Wolfram P3, sub-O($n$) extraction)
- **Status:** D
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_4`

### Claim 81.5
- **Claim Text:** *Next binding action:* Paper 81 must give the unbounded proof via the Lucas carry closed form and the cold-start readout
- **Status:** D
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_5`

### Claim 81.6
- **Claim Text:** *Next binding action:* Paper 81 (or the McKay-Thompson analysis in Paper 90) must close the firing set density conjecture
- **Status:** I
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_6`

### Claim 81.7
- **Claim Text:** *Owner:* Paper 81 and Paper 90
- **Status:** I
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_7`

### Claim 81.8
- **Claim Text:** *Next binding action:* Paper 81 (Rule 30 non-periodicity) and Paper 90 (McKay-Thompson) must close the firing density conjecture
- **Status:** I
- **Source:** mapped_file_claims_report.md
- **CAM Hash:** `sha256:claim81_8`

## Disposition
This paper is classified as **`canon`**. It is part of the core canonical paper series.
