# PAPER ROOTS CATALOG
## A-Family Unified Canon Mapping

**Date:** 2026-07-01  
**Scope:** All paper numbering schemes discovered across the D drive, stripped of B-family identity and mapped to A-family conventions (`paper-00` through `paper-100`).  
**Method:** Complete read of the master inventory; cross-reference mapping by theorem name, content description, and explicit cross-root tables.  

---

## 1. Numbering Schemes Cataloged

Ten independent schemes were identified. All are described below in neutral, de-branded terms.

| Scheme | Neutral Label | Range | Nature | Estimated Volume |
|--------|---------------|-------|--------|------------------|
| A | Kernel Stubs | 00–32 | Minimal theorem stubs (one-line statement, physical operation, validation flag) | 33 papers + 10 summaries |
| B | Legacy Drafts | 00–33 + fractions | Iterative draft archive with `.25`, `.50`, `.75` increments; appendix and glossary documents | ~200 files |
| C | Deep Proof Papers | 01–16 (+ 03a variant) | Full formal mathematical proofs with theorem registries, open obligations, and abstracts | 17 papers |
| D | Extracted Texts | 026–100 (non-contiguous) | Raw mathematical explorations, prototype formalizations, boundary documents, and early claim versions | ~75 texts |
| E | Parallel Interpretive Track | 0–14 | Alternate-angle philosophical/interpretive papers using claim-class taxonomy | 15 papers |
| F | Submission Papers | 1–5 | Target-quality documents intended for external journals and prizes | 5 papers |
| G | Whitepapers | 00–31 and 00–13 | Packaged, formatted versions for external consumption | ~45 files |
| H | Split-Format Papers | 01–05 | Each paper divided into formal, tool, and workbook components | ~15 files |
| I | Thematic Suite | 00–10 | Code substrate and implementation modules (non-sequential) | ~11 sections + 40+ modules |
| J | Archive | Versioned | Historical evidence, source cards, versioned releases, and prior unified visions | ~100+ files |

**Critical observation:** No single scheme is canonical. The same theorem appears in multiple schemes with different packaging depths. The A-family canon is constructed by **content-based merging**, not by selecting one scheme as master.

---

## 2. Source-of-Truth Hierarchy

The hierarchy below determines which source takes precedence when the same mathematical content appears in multiple schemes.

| Tier | Role | Precedence | Maps To A-Family |
|------|------|------------|------------------|
| 1 | **Mathematical Backbone** — Deep Proof Papers | Highest. Full proofs, theorem registries, open obligations. | `paper-00` through `paper-17` (core theorems) |
| 2 | **Scope Index** — Kernel Stubs | Complete map of claimed coverage. Identifies what the corpus asserts it can prove. | `paper-00` through `paper-32` (completeness check) |
| 3 | **Verification Layer** — Production Formal | Receipts, code verifiers, and checked derivations. | `paper-00` through `paper-20` (verified claims) |
| 4 | **Provenance Record** — Extracted Texts | Evolutionary history of claims: early versions, abandoned strategies, open obligations. | All slots (annotation layer) |
| 5 | **Target Quality + Interpretation** — Submission Papers + Parallel Track | External-submission benchmarks and philosophical bridges. | `paper-48` through `paper-52` (submissions); `paper-33` through `paper-47` (interpretive) |
| 6 | **Historical Evidence** — Archive | Dropped claims, source cards, versioned releases. | Metadata for all slots |

**Rule of precedence:** When content conflicts, Tier 1 wins. When Tier 1 is silent, Tier 2 defines scope. When Tier 2 is silent, Tier 3 provides verification. Tiers 4–6 are non-canonical but required for integrity and provenance.

---

## 3. A-Family Master Mapping

### 3.1 Core Mathematical Papers (paper-00 through paper-17)

These slots are populated by the Deep Proof Papers (Tier 1), which provide the most rigorous derivations. Production and Kernel sources are mapped to the same slots by theorem content.

| A-Family | Content Title | Tier 1 Proof | Tier 2 Kernel | Tier 3 Production | Tier 4 Extracted | Tier 5 Submission |
|----------|---------------|--------------|---------------|---------------------|------------------|-------------------|
| `paper-00` | Chart↔J₃(O) Isomorphism (T3) | Proof 02 | 00 | 00 | 039 | — |
| `paper-01` | Bijective SU(2) Doublet (T_BIJECTIVE) | Proof 01 | 01 | 01 | 040 | — |
| `paper-02` | Foundation / Recursive Closure | — | 02 | 02 | — | — |
| `paper-03` | N=3 SU(3) Weyl Closure (T4) | Proof 03 | 00 / 03 | 03 | 038 | — |
| `paper-04` | F4 Zero-Weight Bridge | Proof 03a | — | — | 037 | — |
| `paper-05` | Relational Qubit Frame Inversion (T_INV_1) | Proof 04 | 04 | 04 | 036 | — |
| `paper-06` | Monster Moonshine and D4 Geometry | Proof 05 | 18 | 18 | 035 | Real-Paper 5 (overlap) |
| `paper-07` | Von Neumann ISA | Proof 06 | 06 | 06 | 034 | — |
| `paper-08` | Universal N=3 Closure | Proof 07 | 07 | 07 | 033 | — |
| `paper-09` | Pi Vacuum Parameter | Proof 08 | 08 | 08 | 032 | — |
| `paper-10` | Transformer Worldsheet (T_EMISSION) | Proof 09 | 09 | 09 | 031 | — |
| `paper-11` | Wow Signal D4 Classical (T_DYAD) | Proof 10 | 10 | 10 | 030 | — |
| `paper-12` | Pariah Groups as Monster Boundary | Proof 11 | 11 | 11 | 029 | — |
| `paper-13` | Physical Constants Invariants | Proof 12 | 12 | 12 | 028 | — |
| `paper-14` | Magic Square F4→G2 | Proof 13 | 13 | 13 | 027 | — |
| `paper-15` | D12 Moonshine Chain (T_D12_CHAIN) | Proof 14 | 17 | 17 | 046 | — |
| `paper-16` | Observer Lattice Chain (T_WRAP, T_T10_CENTROID) | Proof 15 | 15 | 15 | 026 | — |
| `paper-17` | The Digit Rollout | Proof 16 | 16 | 16 | — | — |

**Notes on core mapping:**
- `paper-00` and `paper-03` both draw on Kernel 00, which contains two theorems (T3 and T4). The Kernel is an index layer; the A-family separates them into distinct papers based on the Proof Paper structure.
- `paper-04` (F4 Bridge) has no corresponding Kernel or Production entry; it exists only as Proof 03a and Extracted 037. It is retained as a distinct slot because it is a formal proof with a unique theorem.
- `paper-06` (Monster Moonshine) maps to Production 18 and Kernel 18 in the B-family, but in A-family it occupies slot `paper-06` based on the Proof Paper ordering.
- `paper-15` (D12 Moonshine) maps to Production 17 and Kernel 17 in the B-family, but in A-family it occupies slot `paper-15` based on Proof 14.
- `paper-16` (Observer Lattice) consolidates content that was distributed across B-family Production 09, 10, and 15.

### 3.2 Scope-Index Papers (paper-18 through paper-32)

These slots are defined by the Kernel Stubs (Tier 2), which identify theorems that have **no corresponding Deep Proof Paper**. They are application/interpretation papers or stubs awaiting formal derivation.

| A-Family | Content Title | Tier 2 Kernel | Tier 3 Production | Tier 4 Extracted | Status |
|----------|---------------|---------------|---------------------|------------------|--------|
| `paper-18` | (Reserved: Production 19 territory) | 19 | 19 | — | Gap — no Proof Paper |
| `paper-19` | (Reserved: Production 20 territory) | 20 | 20 | — | Gap — no Proof Paper |
| `paper-20` | (Reserved: Production 20+ / transition) | — | — | — | Buffer slot |
| `paper-21` | MorphForge / PolyForge / MorphoniX (T_MORPHIC) | 21 | — | — | Kernel only — needs derivation |
| `paper-22` | Astro-MetaForge (T_ASTRO) | 22 | — | — | Kernel only — needs derivation |
| `paper-23` | FoldForge (T_FOLD) | 23 | — | — | Kernel only — needs derivation |
| `paper-24` | KnightForge CA / Spinor Walk (T_KNIGHT) | 24 | — | — | Kernel only — needs derivation |
| `paper-25` | Energetic Traversal (T_ENERGY) | 25 | — | — | Kernel only — needs derivation |
| `paper-26` | Z-Pinch Shear Horizon (T_ZPINCH) | 26 | — | — | Kernel only — needs derivation |
| `paper-27` | Observer Delay / Shared Reality (T_DELAY) | 27 | — | — | Kernel only — needs derivation |
| `paper-28` | Conway Glider / Oloid Emitter (T_GLIDER) | 28 | — | — | Kernel only — needs derivation |
| `paper-29` | LMFDB Moonshine Anchor (T_LMFDB) | 29 | — | — | Kernel only — needs derivation |
| `paper-30` | Grand Ribbon Meta-Framer (T_GRAND_RIBBON) | 30 | — | — | Kernel only — needs derivation |
| `paper-31` | Meta LCR Readout (T_META_LCR) | 31 | — | — | Kernel only — needs derivation |
| `paper-32` | Supervisor Cursor (T_SUPERVISOR / T_OBSERVATION) | 32 | — | — | Kernel only — needs derivation |

**Assessment:** Slots `paper-21` through `paper-32` contain **theorem stubs only**. They have no Tier 1 Deep Proof Paper. The canon-building effort must either:
- Derive formal proofs for them from Tier 4 archaeological sources and Tier 5 submission papers;
- Demote them to the Application Layer (`paper-81`–`paper-100` territory) if they lack mathematical substance;
- Or reject them if no derivable content exists.

### 3.3 Interpretive Layer (paper-33 through paper-47)

The Parallel Interpretive Track (15 papers) is mapped sequentially into A-family slots. These papers explore the same framework from alternate philosophical angles and use a claim-class taxonomy distinct from the theorem registry.

| A-Family | Source | Content Type |
|----------|--------|--------------|
| `paper-33` | Parallel Track 0 | Interpretive / foundational |
| `paper-34` | Parallel Track 1 | Interpretive / triality |
| `paper-35` | Parallel Track 2 | Interpretive / recursive closure |
| `paper-36` | Parallel Track 3 | Interpretive / energy transport |
| `paper-37` | Parallel Track 4 | Interpretive / tarpit ecology |
| `paper-38` | Parallel Track 5 | Interpretive / observer frame |
| `paper-39` | Parallel Track 6 | Interpretive / meta-corpus |
| `paper-40` | Parallel Track 7 | Interpretive / completion |
| `paper-41` | Parallel Track 8 | Interpretive / unification |
| `paper-42` | Parallel Track 9 | Interpretive / spectre geometry |
| `paper-43` | Parallel Track 10 | Interpretive / crystallization |
| `paper-44` | Parallel Track 11 | Interpretive / extended claim class |
| `paper-45` | Parallel Track 12 | Interpretive / extended claim class |
| `paper-46` | Parallel Track 13 | Interpretive / extended claim class |
| `paper-47` | Parallel Track 14 | Interpretive / extended claim class |

### 3.4 Submission-Quality Papers (paper-48 through paper-52)

The five Submission Papers are mapped to dedicated A-family slots as target-quality benchmarks.

| A-Family | Content Title | Source |
|----------|---------------|--------|
| `paper-48` | Decomposition Theory | Submission Paper 1 |
| `paper-49` | Vertex Operator Algebra | Submission Paper 2 |
| `paper-50` | Lattice Theory | Submission Paper 3 |
| `paper-51` | Prize Submissions | Submission Paper 4 |
| `paper-52` | Moonshine Deep Dive | Submission Paper 5 |

### 3.5 Extracted-Text Unique Content (paper-53 through paper-88)

The Extracted Texts (026–100) contain ~75 texts. Many overlap with `paper-00`–`paper-17` and are mapped there as Tier 4 provenance. The remaining texts — those with no overlap to the core theorems — are mapped to A-family slots `paper-53` through `paper-88` by thematic group.

| A-Family | Thematic Group | Source Range | Description |
|----------|---------------|--------------|-------------|
| `paper-53` | Boundary / Quasi-Crystal | Extracted 047 | Boundary-cqe: quasi-crystal |
| `paper-54` | Boundary / Lie Conjugation | Extracted 048 | Boundary-cqe: lie conjugation |
| `paper-55` | Boundary / Proof of Transport | Extracted 049 | Boundary-cqe: proof-of-transport |
| `paper-56` | Boundary / AN-Spine | Extracted 050 | Boundary-cqe: an-spine |
| `paper-57` | Identity / Solved Form | Extracted 051 | Identity-review: solved-form |
| `paper-58` | Identity / Embodied Centroid | Extracted 052 | Identity-review: embodied-centroid |
| `paper-59` | Prototype Runtime / Unified Tool | Extracted 053 | Prototype-runtime: unified-tool |
| `paper-60` | Prototype Runtime / Pipeline Spec | Extracted 054 | Prototype-runtime: pipeline-spec |
| `paper-61` | Prototype Runtime / Unified Architecture | Extracted 055 | Prototype-runtime: unified-architecture |
| `paper-62` | Prototype Runtime / Unified Spec | Extracted 056 | Prototype-runtime: unified-spec |
| `paper-63` | Prototype Formalization / V5 Whitepaper | Extracted 059 | Prototype-formalization: v5-whitepaper |
| `paper-64` | Prototype Formalization / V5 Skeleton | Extracted 060 | Prototype-formalization: v5-skeleton |
| `paper-65` | Prototype Formalization / Atomic Knowledge | Extracted 061 | Prototype-formalization: atomic-knowledge |
| `paper-66` | Prototype Formalization / Emergent Analysis | Extracted 062 | Prototype-formalization: emergent-analysis |
| `paper-67` | Prototype Formalization / Formalizations Full | Extracted 063 | Prototype-formalization: formalizations-full |
| `paper-68` | Prototype Formalization / CMPLX Expanded | Extracted 064 | Prototype-formalization: cmplx-expanded |
| `paper-69` | Prototype Formalization / CQE Definitions | Extracted 065 | Prototype-formalization: cqe-definitions |
| `paper-70` | Prototype Formalization / CQE Formalization | Extracted 066 | Prototype-formalization: cqe-formalization |
| `paper-71` | LCR PDF / Expanded Treatise | Extracted 068 | LCR-pdf: expanded-treatise |
| `paper-72` | LCR PDF / Rule 30 Synthesis | Extracted 070 | LCR-pdf: rule30-synthesis |
| `paper-73` | LCR PDF / Comprehensive Papers | Extracted 072 | LCR-pdf: comprehensive-papers |
| `paper-74` | LCR Rule 30 / Mophonics Summary | Extracted 074 | LCR-rule30: mophonics-summary |
| `paper-75` | LCR Rule 30 / Prize Submission | Extracted 076 | LCR-rule30: prize-submission |
| `paper-76` | LCR Rule 30 / Agent Outline | Extracted 078 | LCR-rule30: rule30-agent-outline |
| `paper-77` | LCR Rule 30 / Agent Final | Extracted 080 | LCR-rule30/prior: agent-final-paper |
| `paper-78` | LCR Rule 30 / Initial Overclaim | Extracted 081 | LCR-rule30/prior: initial-overclaim |
| `paper-79` | LCR Rule 30 / Spinor Oloid | Extracted 082 | LCR-rule30/prior: spinor-oloid |
| `paper-80` | LCR Rule 30 / Lambda Equivalence | Extracted 083 | LCR-rule30/prior: lambda-rule30-equivalence |
| `paper-81` | Lattice Forge Core / Aletheia Generative | Extracted 084 | Lattice-forge-core: aletheia-generative |
| `paper-82` | Lattice Forge Core / Witness | Extracted 086 | Lattice-forge-core: witness |
| `paper-83` | Lattice Forge Core / Regimes ABC D4 | Extracted 088 | Lattice-forge-core: regimes-abc-d4 |
| `paper-84` | Lattice Forge Core / Open Obligations | Extracted 092 | Lattice-forge-core: open-obligations |
| `paper-85` | Lattice Forge Core / Umbrella Formalization | Extracted 095 | Lattice-forge-core: umbrella-formalization |
| `paper-86` | Lattice Forge Core / Invariant Core Field | Extracted 100 | Lattice-forge-core: invariant-core-field |
| `paper-87` | (Reserved: extracted gap) | — | Buffer |
| `paper-88` | (Reserved: extracted gap) | — | Buffer |

**Note:** The Extracted Text range is non-contiguous. The mapping above assigns the named texts to A-family slots. Any unlisted extracted numbers (e.g., 067, 069, 071, 073, 075, 077, 079, 085, 087, 089, 090, 091, 093, 094, 096, 097, 098, 099) are either absorbed into the core overlap (`paper-00`–`paper-17`) or are gaps in the extracted sequence. They are treated as **provenance annotations** rather than standalone A-family papers.

### 3.6 Whitepaper and Split-Format Overlaps

| A-Family | Mapping |
|----------|---------|
| Whitepapers 00–13 | Redundant with `paper-00`–`paper-13`. Absorbed as Tier 5 packaging variants. |
| Whitepapers 14–31 | Redundant with `paper-14`–`paper-31`. Absorbed as Tier 5 packaging variants. |
| Split-Format 01–05 | Redundant with `paper-01`–`paper-05`. The formal/tool/workbook split is an **architectural pattern**, not a new numbering scheme. If adopted, it becomes a structural convention within each A-family paper. |

### 3.7 Buffer and Reserved Slots (paper-89 through paper-100)

| A-Family | Status |
|----------|--------|
| `paper-89` | Reserved — buffer for core expansion |
| `paper-90` | Reserved — buffer for core expansion |
| `paper-91` | Reserved — buffer for core expansion |
| `paper-92` | Reserved — buffer for core expansion |
| `paper-93` | Reserved — buffer for core expansion |
| `paper-94` | Reserved — buffer for core expansion |
| `paper-95` | Reserved — buffer for core expansion |
| `paper-96` | Reserved — buffer for core expansion |
| `paper-97` | Reserved — buffer for core expansion |
| `paper-98` | Reserved — buffer for core expansion |
| `paper-99` | Reserved — buffer for core expansion |
| `paper-100` | Reserved — canonical capstone / meta-index |

---

## 4. Unassigned Content

The following content types **cannot be mapped** to individual A-family paper slots because they are infrastructure, navigation, or aggregate documents rather than sequential papers.

| Content Type | Reason for Unassignment | Disposition |
|--------------|------------------------|-------------|
| **Thematic Suite (Sections 00–10)** | Code substrate and implementation modules, not exposition. Contains 40+ forge modules (CADForge, E8Forge, MorphForge, etc.). | Treated as **implementation infrastructure** supporting all A-family papers. |
| **Navigation Documents (Showroom)** | `AGENTS.md` files across multiple directories. Machine-readable navigation hubs. | Treated as **corpus metadata**, not paper content. |
| **Catalog Summary** | 1173 inventory rows, 81283 evidence rows, 424 distilled block claims. | Treated as **machine-readable index** for the entire A-family. |
| **Summary Papers (I–X)** | 10 cross-cutting overview documents. | Treated as **meta-papers**; could be assigned to `paper-100` as capstone supplements or kept as unassigned overviews. |
| **Legacy Appendix Papers** | Glossary, cross-disciplinary, prior-art, toolkit-application, code-details, forge-completion. | Absorbed as **appendices** to relevant A-family papers, not standalone slots. |
| **Open Obligations Registry** | PFC-1 through PFC-5, O1, O2, O2'. | Treated as **canonical obligation list** referenced by all A-family papers. |
| **Archive Source Cards** | Dark energy, Higgs mass, oloid global path, idempotent DNA quark, etc. | Mined for claims; if a claim is promoted, it is absorbed into the relevant A-family paper. If not, it remains in the archive. |
| **Versioned Forge Releases** | 0.1.0 through 0.9.0 | Historical evidence; unassigned. |
| **Fractional Drafts (.25, .50, .75)** | Iterative versions of legacy papers. | Absorbed as **provenance** for the corresponding A-family paper (e.g., `paper-03.25` is a draft of `paper-03`). Not given separate A-family slots. |

---

## 5. Cannibalization Strategy Tiers — A-Family Mapping

The original six-tier strategy is preserved but re-expressed entirely in A-family terms.

### Tier 1: Mathematical Backbone → `paper-00` through `paper-17`
**Source:** Deep Proof Papers  
**Action:** These 17 papers are the **canonical mathematical source**. Every theorem in the A-family canon must trace back to one of these slots or be explicitly marked as new.  
**A-Family deliverable:** Best-form versions of `paper-00` through `paper-17` with full proofs, definitions, and references.

### Tier 2: Scope Index → `paper-00` through `paper-32`
**Source:** Kernel Stubs 00–32  
**Action:** The 32 theorems in the kernel index define the **complete claimed scope**. The gap between Tier 1 (`paper-00`–`paper-17`) and Tier 2 (`paper-18`–`paper-32`) is the **work surface** for the canon-building effort.  
**A-Family deliverable:**
- Verified: `paper-00`–`paper-17` (have Tier 1 proofs).
- Unverified stubs: `paper-18`–`paper-32` (need derivation or demotion).

### Tier 3: Verification Layer → `paper-00` through `paper-20`
**Source:** Production Formal 00–20  
**Action:** Receipts and code verifiers connect claims to running code. This layer ensures the canon is **checked mathematics**, not just abstract proof.  
**A-Family deliverable:** Attach verifier receipts to `paper-00`–`paper-20`. For `paper-21`–`paper-32`, build new verifiers or mark as unverified.

### Tier 4: Provenance Record → Annotation layer for all `paper-00`–`paper-100`
**Source:** Extracted Texts 026–100  
**Action:** Mine for:
- Early versions of theorems (to show evolution);
- Claims that were dropped or modified;
- Proof strategies abandoned;
- Open obligations closed or remaining.  
**A-Family deliverable:** Provenance appendix for each A-family paper, citing extracted-text sources where applicable.

### Tier 5: Target Quality + Interpretation → `paper-33` through `paper-52`
**Source:** Parallel Interpretive Track (0–14) + Submission Papers (1–5)  
**Action:** These provide the **external-facing** and **philosophical** layers of the canon.  
**A-Family deliverable:**
- `paper-33`–`paper-47`: Best-form interpretive papers bridging formal mathematics to claim-class taxonomy.
- `paper-48`–`paper-52`: Journal-ready submission versions of selected core content.

### Tier 6: Historical Evidence → Metadata for all `paper-00`–`paper-100`
**Source:** Archive (versioned releases, source cards, prior whitepaper suites)  
**Action:** Preserve evidence of how claims evolved. Do not publish as canon, but maintain for internal integrity and external audit.  
**A-Family deliverable:** Archive metadata registry linked to each A-family paper.

---

## 6. Gaps and Action Items

| Gap | A-Family Impact | Recommended Action |
|-----|-----------------|--------------------|
| `paper-02` has no Tier 1 proof | Foundation slot is unproven | Mine Tier 4 (Extracted) and Tier 6 (Archive) for derivable material; if none, demote to `paper-89`+ or merge with `paper-00` |
| `paper-18` and `paper-19` have only Production stubs | No Deep Proof, no Kernel stub beyond Production | Evaluate whether they contain substantive theorems; if not, absorb into `paper-17` or demote |
| `paper-21` through `paper-32` have only Kernel stubs | 12 papers with no formal proof | Each must be either: (a) derived from Tier 4 archaeological sources, (b) demoted to Application Layer (`paper-81`–`paper-100`), or (c) rejected |
| Fractional legacy drafts (.25, .50, .75) | Iterative noise | Absorb as drafts of corresponding A-family paper; do not give separate slots |
| Thematic Suite code modules | 40+ modules, no paper mapping | Keep as implementation infrastructure; do not force into A-family sequence |
| `paper-89` through `paper-99` | 11 empty slots | Reserved for expansion, merged content, or demoted Kernel stubs |
| `paper-100` | Capstone slot | Assign as meta-index, catalog, or master showroom document |

---

## 7. Summary Statistics

| A-Family Range | Content Source | Count | Status |
|----------------|---------------|-------|--------|
| `paper-00` – `paper-17` | Deep Proof Papers + Production / Kernel | 18 | Core canon — mathematically rigorous |
| `paper-18` – `paper-20` | Production stubs only | 3 | Gaps — need verification or demotion |
| `paper-21` – `paper-32` | Kernel stubs only | 12 | High risk — need derivation or demotion |
| `paper-33` – `paper-47` | Parallel Interpretive Track | 15 | Interpretive layer — philosophical bridges |
| `paper-48` – `paper-52` | Submission Papers | 5 | Target quality — external benchmarks |
| `paper-53` – `paper-88` | Extracted Texts (unique) | 36 | Provenance / prototype / boundary content |
| `paper-89` – `paper-99` | Reserved | 11 | Buffer for expansion |
| `paper-100` | Capstone / Meta-index | 1 | Canonical closing document |
| **Unassigned** | Infrastructure, navigation, archive, fractional drafts | ~500+ files | Metadata and provenance, not sequential papers |

**Total A-family slots assigned:** 89 of 101 (`paper-00` through `paper-88`).  
**Total A-family slots reserved:** 12 (`paper-89` through `paper-100`).  
**B-family identity:** Fully stripped. No CQE-paper, CMPLX, R30, FLCR, NIST, or other B-family numbering appears in the A-family canon.

---

*Catalog compiled from master inventory. All mappings are content-based, not scheme-based. Last updated: 2026-07-01.*
