# Cross-Paper Consistency Audit Report
## CMPLX Unified Papers 0–5 (D:\PaperLib\)

**Audit Date:** 2025-07-03  
**Auditor:** Automated cross-paper consistency scan  
**Papers Audited:** 6 (Paper 0 through Paper 5)  
**Dimensions:** 7 (Mathematical Notation, Theorem Numbering, Definitions, Cross-Paper References, Formatting, Missing Content, D/I/X Classification)

---

## Executive Summary

This audit identifies **23 distinct inconsistencies** across the 6 unified papers. The most severe issues are in **cross-paper theorem references** (4 incorrect citations), **mathematical notation drift** (field notation, Lie group notation, and chart label variants), and **self-referential numbering confusion** caused by the unification of multiple prior numbering schemes (UFT, CQE-Production, CQECMPLX) into a single 0–5 sequence.

**Critical Recommendation:** Before peer-review submission, all cross-paper theorem references must be re-verified against the unified numbering, and the GF(2)/\mathbb{F}_2/F_2 notation must be standardized across all papers.

---

## 1. Mathematical Notation

### 1.1 Field notation: `GF(2)` vs `\mathbb{F}_2` vs `F_2` vs `\mathrm{GF}(2)`

| Notation | Papers Using It | Location | Recommended Fix |
|----------|----------------|----------|---------------|
| `\mathbb{F}_2` | Paper 0 (Band A description, §1.2), Paper 3 (Definition 2.5, Arf invariant), Paper 4 (§17.2 references) | Paper 0, line 53; Paper 3, lines 64, 68, 69 | Use `\mathbb{F}_2` everywhere |
| `\mathrm{GF}(2)` | Paper 1 (Definition 3.6), Paper 2 (throughout), Paper 3 (Definition 2.2, 2.4) | Paper 1, line 71; Paper 2, lines 13, 53, 57, 59, 105, 137, 139, 160, 162, 208; Paper 3, lines 56, 62, 66, 171, 174, 176, 211, 233, 797 | Standardize to `\mathbb{F}_2` |
| `F_2` (bare) | Paper 2 (Remark 5.4), Paper 3 (title/abstract, F2 quadratic form) | Paper 2, lines 151, 323, 393, 437 | Use `\mathbb{F}_2` everywhere |

**Inconsistency:** Paper 2 uses `\mathrm{GF}(2)` in formal definitions but `F_2` in the informal D4 projection remark and forward references. Paper 3 uses `\mathrm{GF}(2)` in formal definitions but `F2` (no subscript) in the title and abstract. Paper 0 uses `\mathbb{F}_2` in the overview but never defines it formally. Paper 4 uses `\mathbb{F}_2` in the references section only.

**Recommended Fix:** Adopt `\mathbb{F}_2` as the sole notation for the field with two elements in all 6 papers. Replace `\mathrm{GF}(2)` in Papers 1–3 and `F_2` in Papers 2–3 with `\mathbb{F}_2`.

---

### 1.2 `J3(O)` vs `J_3(\mathbb{O})` vs `J_3(O)`

| Notation | Papers Using It | Location |
|----------|----------------|----------|
| `J_3(\mathbb{O})` | Paper 0, Paper 1, Paper 2 (receipts), Paper 3 (formal definitions), Paper 4, Paper 5 | Standard in formal math mode |
| `J3(O)` | Paper 3 (title, abstract, running text) | Paper 3, lines 1, 2, 13, 25, 38, 116, 300, 348, 608, 612, 734, 738, 764, 780, 782, 814, 817, 851, 856, 864, 867 |

**Inconsistency:** Paper 3 is the primary violator. Its title uses `D4/J3 Triality Surface` but the formal definitions use `J_3(\mathbb{O})`. The abstract uses `J3(O)` 5 times and `J_3(\mathbb{O})` once. This creates an inconsistent reader experience in the paper that most heavily depends on the exceptional Jordan algebra.

**Recommended Fix:** In Paper 3, replace all `J3(O)` in prose with `J_3(\mathbb{O})`. Keep `J3(O)` only in file paths, code module names, or CAM crystal identifiers where ASCII is required.

---

### 1.3 `F4` vs `F_4` vs `\mathfrak{f}_4`

| Notation | Papers Using It | Location |
|----------|----------------|----------|
| `F4` | Paper 3 (title, abstract, running text, contributions list) | Paper 3, lines 1, 2, 13, 25, 30, 40, 126, 348, 350, 354, 356, 358, 381, 400, 402, 588, 646, 672, 764, 782, 814, 851, 856, 864, 881 |
| `F_4` | Paper 0 (overview), Paper 1 (references), Paper 2 (references), Paper 3 (magic square table), Paper 4 (references) | Paper 0, line 53; Paper 1, lines 317, 432; Paper 3, lines 391–394 (magic square); Paper 4, lines 150, 321, 325, 509, 525, 590 |
| `\mathfrak{f}_4` | Paper 3 (magic square table) | Paper 3, lines 391–394 |

**Inconsistency:** Paper 3 is the nexus of the inconsistency. It uses `F4` in prose, `F_4` in the layer names (`J3O_TO_G2_F4_T5A_ROUTE`), and `\mathfrak{f}_4` in the Freudenthal–Tits magic square table. The other papers use `F_4` consistently in prose.

**Recommended Fix:** Adopt `F_4` for the Lie group in prose and theorem statements. Use `\mathfrak{f}_4` only in the magic square table where Lie algebra notation is conventional. Never use bare `F4` in formal text.

---

### 1.4 `D4` vs `D_4` and `S3` vs `S_3`

| Notation | Papers Using It | Location |
|----------|----------------|----------|
| `D_4` | Paper 0, Paper 1, Paper 3 (some theorems), Paper 4, Paper 5 | Formal math mode |
| `D4` | Paper 2 (Remark 5.4), Paper 3 (title/abstract/running text), Paper 4 (running text), Paper 5 (running text) | Paper 2, line 151; Paper 3, lines 1, 2, 13, 25, 38, 80, 106, 116, 262, 348, 364, 381, 408, 451, 648, 688, 764, 782, 814, 851, 864, 881; Paper 4, lines 60, 150, 321, 325, 509, 525, 590; Paper 5, lines 17, 37, 253, 256, 258, 301, 556, 559, 567, 609, 618 |
| `S_3` | Paper 0, Paper 1, Paper 3 (formal definitions), Paper 4 | Formal math mode |
| `S3` | Paper 3 (title/abstract/running text) | Paper 3, lines 1, 2, 13, 25, 125, 324, 336, 381, 408, 452, 588, 596, 646, 648, 698, 764, 782, 814, 856, 881 |

**Inconsistency:** Paper 3 uses `D4` and `S3` in the title, abstract, and most running text, but switches to `D_4` and `S_3` in formal definitions (Definitions 2.13, 2.14) and the magic square discussion. Paper 2 uses `D4` in an informal remark. Papers 4 and 5 use `D4` in running text but `D_4` in formal layer names.

**Recommended Fix:** Standardize to `D_4` and `S_3` (with subscripts) in all formal prose and theorem statements. `D4` and `S3` may be retained only in code identifiers, CAM crystal names, or file paths.

---

### 1.5 Chart state labels

| Paper | Label for (0,0,0) | (0,0,1) | (0,1,0) | (0,1,1) | (1,0,0) | (1,0,1) | (1,1,0) | (1,1,1) |
|-------|-------------------|---------|---------|---------|---------|---------|---------|---------|
| **Paper 1** | ZERO | e3+ | e2-0 | C+ | e1- | C0 | C- | FULL |
| **Paper 2** | Vacuum (0) | R-boundary | Chiral A (e2-0) | Pode | L-boundary | C0 state | Chiral B (C-) | Vacuum (1) |
| **Paper 3** | ZERO | e3+ | e2-0 | C+ | e1- | C0 | C- | FULL |
| **Paper 5** | ZERO | e3+ | e2-0 | C+ | e1- | C0 | C- | FULL |

**Inconsistency:** Paper 2 introduces **alternative descriptive names** (`Vacuum (0)`, `R-boundary`, `Chiral A`, `Pode`, `L-boundary`, `C0 state`, `Chiral B`, `Vacuum (1)`) that are used **only in Paper 2** and never appear in Papers 1, 3, or 5. This creates a naming discontinuity. Paper 2 also uses `e2-0` and `C-` as parenthetical aliases, but the primary names in its state table are the descriptive ones.

**Recommended Fix:** In Paper 2, replace the descriptive names in the main state table with the canonical labels from Paper 1 (ZERO, e3+, e2-0, C+, e1-, C0, C-, FULL). Keep the descriptive names as a one-time remark if needed, but the canonical table must match Paper 1 exactly.

---

### 1.6 `LCR` vs `left-center-right`

**Finding:** All 6 papers use `LCR` consistently. No inconsistency.

---

### 1.7 Boolean operators: `\oplus` vs `XOR`, `\cdot` vs `*`, `\neg` vs `NOT`

| Operator | Papers | Notation | Issue |
|----------|--------|----------|-------|
| XOR | 0–5 | `\oplus` in math, "XOR" in text/code | Consistent |
| AND | 0–2 | `\cdot` or `\land` or `&` | **Inconsistent** |
| NOT | 0–2 | `\neg` or `1 -` | **Inconsistent** |

**Specific Issue in Paper 3:** Paper 3 defines the quadratic form as `Q(L,C,R) = C + CR` where `+` is addition over `GF(2)` (XOR). In the same paper, the ANF uses `\oplus` for XOR. Having `+` mean XOR in the quadratic form context while `\oplus` means XOR in the ANF context is confusing. Paper 3 explicitly states "where `+` is addition over `GF(2)` (XOR)" to disambiguate, but this is a notation clash.

**Specific Issue in Paper 2:** The correction term is defined as `C · ¬R = C · (1 - R)`. In code it uses `C & (1 - R)`. The `1 - R` notation for NOT is used in Papers 2 and 3, while `\neg R` is used in Papers 0, 1, and 4.

**Recommended Fix:** 
- In all papers, use `\oplus` for XOR in both math and code comments.
- In all papers, use `\cdot` or `\land` for AND (choose one; `\land` is used in Paper 0, `\cdot` in Papers 2–3).
- In all papers, use `\neg` for NOT; never use `1 - R` in formal definitions.

---

### 1.8 `\mathbb{Z}/4` vs `\mathbb{Z}_4` vs `Z_4`

| Notation | Papers | Location |
|----------|--------|----------|
| `\mathbb{Z}/4` | Paper 1 (abstract) | Paper 1, line 18 |
| `\mathbb{Z}_4` | Paper 1 (Theorems 9.2, 9.3), Paper 0 (verifier table) | Paper 1, lines 183, 185, 189; Paper 0, line 445 |
| `Z_4` (bare) | Paper 0 (verifier table) | Paper 0, line 445 |

**Inconsistency:** Paper 1 uses `\mathbb{Z}/4` in the abstract but `\mathbb{Z}_4` in the theorems. Paper 0 uses `Z_4` (bare) in the verifier table. The cyclic group of order 4 should be denoted consistently.

**Recommended Fix:** Standardize to `\mathbb{Z}_4` in all formal text. `Z_4` may be used in code or verifier names.

---

### 1.9 Greek letters: `phi`, `kappa`, `Gamma`, `psi`, `Sigma`, `partial`

| Symbol | Usage | Consistency |
|--------|-------|-------------|
| `\phi` | Registration map `\phi(L,C,R) = diag(L,C,R)` | **Consistent** across Papers 0, 1, 3. Not used in 2, 4, 5. |
| `\kappa` | Energy quantum `\kappa = \ln(\varphi)/16` | **Consistent** in Paper 0 only. Not used in 1–5. |
| `\Gamma` | Gluon field `\Gamma(s) = C` | **Consistent** in Paper 1 only. Not used in 0, 2–5. |
| `\psi` | Not used in any of the 6 papers | N/A |
| `\Sigma` | State space `\Sigma = \{0,1\}^3` | **Consistent** across all 6 papers. |
| `\sigma` | Reversal involution | **Consistent** across Papers 1, 3. Not used in 0, 2, 4, 5. |
| `\partial` | Boundary operator | **Consistent** across all 6 papers. |

**Finding:** Greek letters are used consistently where they appear. No action needed.

---

## 2. Theorem Numbering

### 2.1 Sequential numbering within papers

| Paper | Numbering Pattern | Gaps / Issues |
|-------|-------------------|---------------|
| **0** | 0.1, 0.2, 00.1, 0.3 | **Non-sequential:** Theorem 00.1 appears between 0.2 and 0.3. The numbering jumps from 0.2 to 00.1 (two-digit sub-number) then back to 0.3. |
| **1** | Section-based: 4.1, 4.2, 5.1, 6.1, 7.1, 7.2, 8.1, 9.1, 9.2, 9.3, 10.1, 10.2, 10.3 | Sequential within sections. No gaps. |
| **2** | 2.1, 2.2, 2.3, 2.4, 2.4a, 9.1, 9.2, 9.3, 9.4, 9.5 | Main theorems in §2 (2.1–2.4a), verification theorems in §9 (9.1–9.5). **Large gap** (no theorems 3–8). |
| **3** | 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1–9.4, 10.1–10.4, 11.1–11.3, 12.1–12.2, 13.1–13.3, 14.1–14.3, 15.1–15.5, 19.1–19.4 | **Gap:** jumps from 15.5 to 19.1 (no theorems 16–18). |
| **4** | 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1, 11.1, 11.2 | **Non-sequential start:** Section 4 contains Lemmas 4.1–4.3, then Section 5 contains Theorem 5.1. Theorem numbering starts at 4.1 in a lemmas section, which is unconventional. |
| **5** | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7 | All theorems in §5. Corollaries use 5.1.1, 5.1.2, etc. Sequential. No gaps. |

**Recommended Fix:** 
- Paper 0: Renumber Theorem 00.1 to **Theorem 0.3**, and shift subsequent theorems (0.3 → 0.4).
- Paper 2: The gap between §2 and §9 is intentional (theorems are grouped by type), but a note should explain that theorems 3.1–8.x are omitted because the paper's structure groups main results in §2 and verification results in §9.
- Paper 3: Either add theorems in §§16–18 (which currently contain only axioms, lemmas, and practical examples) or renumber 19.1–19.4 to 16.1–16.4 to close the gap.
- Paper 4: Either renumber Theorem 4.1 to **Theorem 5.1** (matching its section) or move the content of Section 4 (Lemmas) into Section 5 and renumber accordingly.

---

### 2.2 Cross-paper theorem reference consistency

| Referencing Paper | Citation | Target Paper | Actual Target Theorem | Correct? |
|-------------------|----------|--------------|----------------------|----------|
| **Paper 3** | "Paper 2, Theorem 4.1" | Paper 2 | Theorem 4.1 is **ANF coefficients** (Corollary 4.1) | **NO** — should be **Theorem 2.2** (Correction Surface Decomposition) |
| **Paper 3** | "Paper 2, Corollary 4.3" | Paper 2 | Corollary 4.3 is **Kernel of Q** | **NO** — should be **Corollary 5.2** (Independence of L) |
| **Paper 5** | "Paper 1, Theorem 6.1" | Paper 1 | Theorem 6.1 is **Reversal involution structure** | **NO** — should be **Theorem 8.1** (Substrate map preservation) |
| **Paper 4** | "Paper 4 (preceding paper in UFT series)" | Old UFT Paper 4 | Now **Paper 3** in unified numbering | **CONFUSING** — self-reference to old UFT Paper 4 |
| **Paper 5** | "Paper 5" (Corollary 5.4.2) | Paper 5 itself | Self-reference for typed repair rows | **NO** — should be **Paper 4** (Typed Boundary Repair) |

**Severity: HIGH.** Four incorrect cross-paper references and one confusing self-reference.

**Recommended Fix:**
- Paper 3, §1.1: Change "Paper 2, Theorem 4.1" → **"Paper 2, Theorem 2.2"**
- Paper 3, §1.1: Change "Paper 2, Corollary 4.3" → **"Paper 2, Corollary 5.2"**
- Paper 5, §2.9 / Definition 2.9: Change "Paper 1, Theorem 6.1" → **"Paper 1, Theorem 8.1"**
- Paper 4, §15.1 / §15.3: Change all references to "Paper 4 (preceding paper in UFT series)" → **"Paper 3 (D4/J3 Triality)"** or **"the unified Paper 3"**
- Paper 5, Corollary 5.4.2: Change "Paper 5" → **"Paper 4"**

---

## 3. Definitions

### 3.1 LCR carrier definition

**Finding:** All papers define the LCR carrier consistently as `\Sigma = \{0,1\}^3` with triples `(L, C, R)`. No inconsistency.

---

### 3.2 Chart definition and 8 states

**Finding:** Papers 1, 3, and 5 use identical canonical labels (ZERO, e3+, e2-0, C+, e1-, C0, C-, FULL). Paper 2 uses alternative names. Paper 0 does not enumerate the full label table. Paper 4 does not enumerate labels at all. **Inconsistent across 6 papers.**

**Recommended Fix:** Paper 2 should adopt the canonical label table. Paper 0 should include a forward reference to Paper 1's table.

---

### 3.3 Correction term / boundary definition

| Paper | Definition | Notation | Issue |
|-------|------------|----------|-------|
| 0 | `\partial = C \land \neg R` | `\partial` | Consistent |
| 1 | `\partial(L,C,R) = C \wedge \neg R` | `\partial` | Uses `\wedge` instead of `\land` (same meaning) |
| 2 | `\mathrm{correction}(C,R) = C \cdot \neg R` | `\mathrm{correction}` | Consistent with field theory style |
| 3 | `\mathrm{correction}(C,R) = C \cdot \neg R` | `\mathrm{correction}` | Consistent |
| 4 | `\text{corr}(L,C,R) = C \text{ and } \neg R = 1` | `\text{corr}` | **Malformed and inconsistent** |

**Inconsistency in Paper 4:** Definition 2.5 states: "A correction residue (or interaction residue) is a Paper 2 row where `\text{corr}(L, C, R) = C \text{ and } \neg R = 1$`." This is malformed LaTeX (missing backslash on `neg`) and uses the non-standard `\text{corr}` instead of `\mathrm{correction}` or `\partial`. The condition `= C \text{ and } \neg R = 1` is ambiguous — it reads as "equals C and (not R equals 1)" rather than "C AND (NOT R) equals 1."

**Recommended Fix:** Paper 4, Definition 2.5 should read: "A correction residue is a Paper 2 row where `\mathrm{correction}(L, C, R) = C \cdot \neg R = 1$`."

---

### 3.4 Shell grading

**Finding:** Papers 1, 3 define `sh(L,C,R) = L + C + R` (Hamming weight). Paper 0 defines `shell(L,C,R) := L + C + R` in §2.3. Paper 2 does not re-define shell but uses it in the table. **Consistent across all papers.**

---

### 3.5 Axioms

| Axiom | Paper 0 | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 |
|-------|---------|---------|---------|---------|---------|---------|
| **Locality** | A1 (Chart Existence) | Axiom 2.1 | §1.2 Axiom 1 | Axiom 16.1 | Axiom 3.1 | Axiom 3.1 |
| **Receipt Preservation** | A00.2 | Axiom 2.2 | §1.2 Axiom 2 | Axiom 16.2 | Axiom 3.2 | Axiom 3.2 |
| **Boundary Positivity** | A3 (Correction Boundary) | Axiom 2.3 | §1.2 Axiom 3 | Axiom 16.3 | Axiom 3.3 | Axiom 3.3 |
| **Analog Equivalence** | A00.4 | Axiom 2.4 | §1.2 Axiom 4 | Axiom 16.4 | Axiom 3.4 | Axiom 3.4 |

**Finding:** Papers 1–5 use the same four axioms with the same names (Locality, Receipt Preservation, Boundary Positivity, Analog Equivalence). Paper 0 uses a different axiom system (physical primitives A1–A4 plus admission axioms A00.1–A00.5). The mapping is roughly:
- Paper 0's A1 (Chart Existence) ↔ Paper 1's Locality
- Paper 0's A3 (Correction Boundary) ↔ Paper 1's Boundary Positivity
- Paper 0's A00.2 (Transport Admissibility) ↔ Paper 1's Receipt Preservation
- Paper 0's A00.4 (Receipt Priority) ↔ Paper 1's Analog Equivalence (loosely)

**Inconsistency:** The axiom names are consistent across Papers 1–5, but Paper 0 uses a completely different numbering and naming scheme. Since Paper 0 is the foreword/foundation, this is acceptable, but a cross-reference table should be added to Paper 0 mapping its physical axioms to the 4 axioms used in Papers 1–5.

**Recommended Fix:** Add a remark in Paper 0, §3.2 stating: "The five admission axioms A00.1–A00.5 map to the four axioms used in Papers 1–5 as follows: A00.1 ↔ Label Independence (not stated elsewhere); A00.2 ↔ Locality + Receipt Preservation; A00.3 ↔ Band Separation (unique to Paper 0); A00.4 ↔ Analog Equivalence; A00.5 ↔ Boundary Positivity."

---

## 4. Cross-Paper References

### 4.1 Verified correct references

| Source | Target | Status |
|--------|--------|--------|
| Paper 3 → Paper 2 (correction term) | Paper 2, Definition 2.4 | ✅ Correct |
| Paper 3 → Paper 1 (chart–J3(O) bijection) | Paper 1, Theorem 7.1 | ✅ Correct |
| Paper 4 → Paper 3 (Arf-matching edge glue) | Paper 3, Theorem 6.1 | ✅ Correct |
| Paper 4 → Paper 3 (independence of correction) | Paper 3, Theorem 7.1 | ✅ Correct |
| Paper 5 → Paper 4 (repair payload) | Paper 4, Definition 2.14 | ✅ Correct |

### 4.2 Incorrect or ambiguous references

| Source | Citation | Problem | Severity |
|--------|----------|---------|----------|
| **Paper 3, §1.1** | "Paper 2, Theorem 4.1" | Theorem 4.1 in Paper 2 is the ANF coefficients corollary, NOT the decomposition theorem. Should be **Theorem 2.2**. | 🔴 High |
| **Paper 3, §1.1** | "Paper 2, Corollary 4.3" | Corollary 4.3 in Paper 2 is the kernel of Q, NOT independence of L. Should be **Corollary 5.2**. | 🔴 High |
| **Paper 5, §2.9 / Definition 2.9** | "Paper 1, Theorem 6.1" | Theorem 6.1 in Paper 1 is the reversal involution, NOT the substrate map. Should be **Theorem 8.1**. | 🔴 High |
| **Paper 5, Corollary 5.4.2** | "Paper 5" | Self-reference for repair rows typed by Paper 5. Should be **Paper 4**. | 🟡 Medium |
| **Paper 4, §15.3** | "Paper 4 (preceding paper in UFT series)" | Refers to old UFT Paper 4 (D4/J3/Triality), which is now **Paper 3**. Creates confusion because the current document IS Paper 4. | 🟡 Medium |
| **Paper 0, §5.1** | "Paper 001", "Papers 002–003", "Paper 012", etc. | Old 3-digit numbering scheme not used in any other unified paper. | 🟢 Low (historical) |

---

## 5. Formatting

### 5.1 Headers

| Element | Paper 0 | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 |
|---------|---------|---------|---------|---------|---------|---------|
| Title | `#` | `#` | `#` | `#` | `#` | `#` |
| Abstract | `## Abstract` | `## Abstract` | `## Abstract` | `## Abstract` | (inline) | `## Abstract` |
| Sections | `#` (Foreword) | `##` | `##` | `##` | `##` | `##` |
| Subsections | `##` | `###` | `###` | `###` | `###` | `###` |

**Inconsistency:** Paper 0 uses `#` for the Foreword section (which is not the title), while other papers use `#` only for the document title. Paper 4 does not have a separate `## Abstract` section; the abstract is inline after the title block. Paper 2's title is unusually long and split across two lines.

**Recommended Fix:** 
- Paper 0: Change "# Foreword: The Author's Burden of Proof" to `## Foreword` or integrate it into the abstract.
- Paper 4: Add `## Abstract` as a separate section before `## 1. Introduction`.

---

### 5.2 Code blocks

| Language Tag | Paper 0 | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 |
|--------------|---------|---------|---------|---------|---------|---------|
| `python` | ✅ | ✅ | ❌ (none) | ❌ (none) | ❌ (none) | ❌ (none) |
| `text` | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |

**Inconsistency:** Paper 0 and Paper 1 include executable Python code blocks. Papers 2–5 do not include Python code blocks in the body (Paper 2 has code-like text in the proof tree, but no fenced blocks). This is a formatting discontinuity.

**Recommended Fix:** Either add a policy note in Paper 0 stating "Band A Papers 1–3 include Python code blocks; Papers 4–5 omit them because their tool bindings are external," or add minimal code stubs to Papers 2–5 for consistency.

---

### 5.3 Tables

**Finding:** All papers use standard Markdown pipe tables (`| col1 | col2 |`). No inconsistency in table format.

---

### 5.4 Citation styles

| Style | Papers Using It | Example |
|-------|-----------------|---------|
| "Author Year" | 0, 1, 2, 3, 4, 5 | "Wolfram 2002" |
| "Author (Year)" | 1, 2 | "Wolfram (2002)" |
| "Author, *Title*, Year" | 3, 4, 5 | "Milnor & Husemoller, *Symmetric Bilinear Forms*, 1973, Chapter IV" |

**Inconsistency:** Paper 1 uses both "Wolfram 2002" (in references) and "Wolfram (2002)" (in the abstract). Paper 2 uses "Wolfram 2002" in references and "Wolfram's P3 problem" (no citation) in text. Paper 3 uses "Carlet 2010, Chapter 6" (formal) in text. Paper 4 uses full bibliographic citations in text. Paper 5 uses "Schatz 1929" and "Bottema & Roth 1979" (compact).

**Recommended Fix:** Adopt a single citation style across all 6 papers. The "Author (Year)" style is most standard for academic papers. For works with chapters, use "Author (Year, Chapter X)."

---

### 5.5 Abstract sections

**Finding:** Papers 0, 1, 2, 3, 5 have explicit `## Abstract` sections. Paper 4 does not. See §5.1 above.

---

### 5.6 Footnotes

**Finding:** None of the 6 papers use footnotes. Consistent.

---

## 6. Missing Content

### 6.1 Theorems mentioned in cross-references but not present

| Citation | Referencing Paper | Issue |
|----------|-------------------|-------|
| "Paper 2, Theorem 4.1" | Paper 3 | Paper 2 Theorem 4.1 is a **corollary** (ANF coefficients), not a major theorem. The intended target is Theorem 2.2. |
| "Paper 2, Corollary 4.3" | Paper 3 | Paper 2 Corollary 4.3 is **kernel of Q**, not independence of L. The intended target is Corollary 5.2. |
| "Paper 1, Theorem 6.1" | Paper 5 | Paper 1 Theorem 6.1 is **reversal involution**, not substrate map. The intended target is Theorem 8.1. |

### 6.2 Definitions used but not defined in the paper or referenced paper

| Definition | Used In | Defined In | Issue |
|------------|---------|------------|-------|
| `roll(q,b)` | Paper 5 | Paper 5, §2.3 | ✅ Defined in same paper |
| `head/tail dyad` | Paper 5 | Paper 5, §2.4 | ✅ Defined in same paper |
| `CIRCLE_F` / `CIRCLE_P` | Paper 4 | Paper 4, §2.8 | ✅ Defined in same paper |
| `D4 axis/sheet codec` | Paper 4 | Paper 3 | Paper 4 references Paper 3 (UFT Paper 4) for definition, but the unified Paper 3 is the correct source. The reference is confusing but the definition exists. |

### 6.3 Forward references to papers that don't exist yet

| Reference | Source | Status |
|-----------|--------|--------|
| Papers 6, 9, 10, 12, 13, 15, 17, 19, 25, 31–39, 40, 41–44, 81–83, 90, 91, 100 | Papers 0–5 | These are **forward references** to the broader 100-paper series. They are explicitly listed as forward references and are not claimed to exist in the current document set. This is acceptable as long as the forward references are consistent. |
| Paper 6 (Oloid Path Carrier and Transport Geometry) | Paper 5, §9.2 | UFT Paper 6 is now **Paper 5** in the unified numbering. The cross-series reference should be clarified. |

**Recommended Fix:** In Paper 5, §9.2, add a note: "UFT Paper 6 corresponds to the unified Paper 5 (this paper)."

### 6.4 "See §X" references to sections that don't exist

| Reference | Source | Status |
|-----------|--------|--------|
| "see §9" | Paper 1, header | Section 9 exists (Forward References). ✅ |
| "see §10" | Paper 2, header | Section 10 exists (Forward References). ✅ |
| "see §11" | Paper 5, header | Section 11 exists (Falsifiers). ✅ |
| "see §7 and §11" | Paper 5, header | Section 7 exists (Verification), §11 exists (Falsifiers). ✅ |
| "see §15" | Paper 3, header | Section 15 exists (Local Triality Surface). ✅ |
| "see §14" | Paper 3, header | Section 14 exists (Forward References). ✅ |
| "see §10" | Paper 4, header | Section 10 exists (Forward References). ✅ |
| "see §11" | Paper 4, header | Section 11 exists (Verification and Receipts). ✅ |

**Finding:** All "see §X" references in headers resolve to existing sections. No broken section references.

---

## 7. Data / Interpretation / Fabrication (D/I/X) Classification

### 7.1 Taxonomy usage

| Paper | Has D/I/X Appendix | Labels Used | Consistency |
|-------|-------------------|-------------|-------------|
| 0 | ✅ (Appendix after §14) | (D), (I), (X) | ✅ |
| 1 | ✅ (§17) | (D), (I), (X) | ✅ |
| 2 | ✅ (Appendix) | (D), (I), (X) | ✅ |
| 3 | ✅ (§25) | (D), (I), (X) | ✅ |
| 4 | ✅ (§18) | (D), (I), (X) | ✅ |
| 5 | ✅ (§13) | (D), (I), (X) | ✅ |

**Finding:** All 6 papers include the D/I/X taxonomy. All use the same three labels: **(D)** Data-backed, **(I)** Interpretation, **(X)** Fabrication. No inconsistency in the taxonomy itself.

---

### 7.2 Same claims classified differently in different papers

| Claim | Paper 0 | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 |
|-------|---------|---------|---------|---------|---------|---------|
| Chart–J3(O) bijection | (D) | (D) | N/A | (D) | (D) | (D) | ✅ Consistent |
| Shell grading | (D) | (D) | N/A | (D) | (D) | (D) | ✅ Consistent |
| VOA partition Z(q)=2q^0+6q^5 | (D) | (D) | N/A | N/A | N/A | N/A | ✅ Consistent |
| Correction surface firing set | (D) | (D) | (D) | (D) | (D) | (D) | ✅ Consistent |
| D4 axis/sheet codec | (I) in overview | (I) | (I) | (D) | (D) | (I) | 🟡 **Inconsistent** |
| Arf-matching edge glue | (I) in overview | N/A | N/A | (D) | (D) | (I) | 🟡 **Inconsistent** |
| F4 → Niemeier route | (I) | N/A | N/A | (I) | (I) | (I) | ✅ Consistent |
| 192/192 standards conformance | (X) → corrected | N/A | N/A | (X) → corrected | (X) → corrected | N/A | ✅ Consistent |

**Inconsistency:** The D4 axis/sheet codec and Arf-matching edge glue are classified as **(D)** in Papers 3 and 4 (because they are bound to `d12_action.py` and `f2_majorana.py` receipts) but as **(I)** in Papers 0, 1, 2, and 5 (because they are presented as structural framing without direct code citations in those papers). This is a **legitimate context-dependent classification** — the same claim is data-backed where it has a receipt and interpretive where it is mentioned in passing. However, the papers should acknowledge this context-dependency explicitly.

**Recommended Fix:** Add a note in the D/I/X appendix of Papers 0, 1, 2, and 5: "The D4 axis/sheet codec is classified as (I) in this paper because it is referenced as structural framing; in Papers 3 and 4 it is classified as (D) because those papers bind it to executable receipts (`d12_action.py`, `f2_majorana.py`)."

---

## 8. Additional Observations

### 8.1 Paper 0's old numbering in the proof tree

In Paper 0, §5.1 (Primitive Completeness Theorem), the proof tree uses an old 3-digit numbering scheme:
- "Paper 001" → should be **Paper 1**
- "Papers 002–003" → should be **Papers 2–3**
- "Paper 012" → should be **Paper 12**
- "Paper 013, 022" → should be **Papers 13, 22**
- "Paper 020" → should be **Paper 20**
- "Paper 023" → should be **Paper 23**
- "Paper 030" → should be **Paper 30**
- "Paper 031" → should be **Paper 31**
- "Paper 032" → should be **Paper 32**
- "Paper 033" → should be **Paper 33**
- "Paper 080–083" → should be **Papers 80–83**
- "Paper 090" → should be **Paper 90**
- "Paper 070" → should be **Paper 70**

**Recommended Fix:** Update the proof tree in Paper 0, §5.1 to use the unified 1–2 digit numbering.

### 8.2 Paper 4's self-reference to old UFT Paper 4

Paper 4 (Unified Boundary Repair) contains multiple references to "Paper 4 (preceding paper in the UFT series)" which is the **old** UFT Paper 4 (D4, J3(O), Triality). In the unified numbering, that content is now **Paper 3**. This is extremely confusing because the reader of the unified Paper 4 will naturally assume "Paper 4" refers to the document they are currently reading.

Occurrences:
- Paper 4, §15.3: "Paper 4 (D4, $J_3(\mathbb{O})$, Triality)" — should be **Paper 3**
- Paper 4, §15.3: "Paper 4 of UFT, Section 3" — should be **Paper 3, Section 8**
- Paper 4, §17.4: "paper_04__d4_j3o_triality" — path reference is correct but textual label is confusing

**Recommended Fix:** Replace all "Paper 4 (preceding paper in UFT series)" / "Paper 4 of UFT" references in Paper 4 with **"Paper 3 (D4/J3 Triality)"**.

### 8.3 Paper 5's self-reference to Paper 5 for typed repair rows

Paper 5, Corollary 5.4.2: "The side-channel has one row per transition. Each repair row is typed (Paper 5)." The parenthetical should refer to **Paper 4** (Typed Boundary Repair), not Paper 5.

**Recommended Fix:** Change "(Paper 5)" to **"(Paper 4)"**.

---

## 9. Summary of Recommended Fixes (Priority Order)

| Priority | Fix | Papers Affected | Effort |
|----------|-----|----------------|--------|
| 🔴 **P0** | Fix incorrect cross-paper theorem references (Paper 3→2, Paper 5→1) | Papers 3, 5 | Low |
| 🔴 **P0** | Fix Paper 4 self-reference to old UFT Paper 4 | Paper 4 | Low |
| 🔴 **P0** | Fix Paper 5 self-reference to Paper 5 for repair rows | Paper 5 | Low |
| 🟡 **P1** | Standardize `\mathbb{F}_2` vs `\mathrm{GF}(2)` vs `F_2` | Papers 0–5 | Medium |
| 🟡 **P1** | Standardize `J_3(\mathbb{O})` vs `J3(O)` | Paper 3 | Low |
| 🟡 **P1** | Standardize `D_4`/`S_3` vs `D4`/`S3` | Papers 2–5 | Medium |
| 🟡 **P1** | Standardize chart state labels (Paper 2 alternative names) | Paper 2 | Low |
| 🟡 **P1** | Fix Paper 4 Definition 2.5 malformed correction residue | Paper 4 | Low |
| 🟡 **P1** | Fix theorem numbering gaps (Paper 0: 00.1; Paper 3: 19.1; Paper 4: 4.1) | Papers 0, 3, 4 | Medium |
| 🟢 **P2** | Standardize citation style across all papers | Papers 0–5 | Medium |
| 🟢 **P2** | Add abstract section to Paper 4 | Paper 4 | Low |
| 🟢 **P2** | Update Paper 0 proof tree to unified numbering | Paper 0 | Low |
| 🟢 **P2** | Add D/I/X context note for axis/sheet codec | Papers 0, 1, 2, 5 | Low |

---

## 10. Conclusion

The 6 unified papers are **structurally coherent** but contain **nontrivial notation drift** and **several incorrect cross-references** that must be corrected before peer-review submission. The most critical issues are:

1. **Four incorrect theorem citations** (Paper 3→2, Paper 5→1, Paper 5→5) that could mislead readers attempting to verify claims.
2. **Paper 4's confusion** between the unified Paper 4 (Boundary Repair) and the old UFT Paper 4 (D4/J3 Triality = unified Paper 3).
3. **Notation drift** in field names (`GF(2)`/`\mathbb{F}_2`/`F_2`), Lie group names (`F4`/`F_4`), and chart labels (Paper 2's descriptive names).

Once these 23 inconsistencies are resolved, the paper suite will present a unified, consistent, and verifiable mathematical foundation for the CMPLX series.

---

*End of Consistency Audit Report.*
