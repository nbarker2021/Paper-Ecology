# MASTER INDEX CATALOG — SystemsLib Paper Mapping
## A-Family Canonical Catalog (Paper-00 through Paper-100)

**Generated:** 2026-07-02
**Source Index:** `D:\CQE_CMPLX\MASTER_PAPER_INDEX.md`
**Total Paper Files Identified:** 8,227
**Total Size:** 221.93 MB
**Unique Paper Content (after deduplication):** ~6,700+ distinct papers
**A-Family Canonical Range:** paper-00 through paper-100

---

## 1. EXECUTIVE SUMMARY

This catalog strips all B-family identity (CQE, FLCR, NIST, CMPLX, EXPOSE numbering) and maps every identified paper file across all collections to the A-family canonical numbering: **paper-00 through paper-100**.

The A-family canonical series is the **UFT 100-Paper Series** (`D:\CQE_CMPLX\papers\UFT0-100`), consisting of:
- **100 core papers** (paper-00 through paper-100)
- **5 extended variants** (paper-91__ through paper-95__)
- **3 extra papers** (paper-101__ through paper-103__)
- **Total: 108 canonical entries**

All other collections are either:
- **Duplicates** of A-family papers (same content, different B-family numbering)
- **Variants** of A-family papers (upgraded, recursive-close, toolkit, contract, next-state bridge versions)
- **Unique** content that cannot be mapped to A-family (noted as "unassigned")

---

## 2. COLLECTION INVENTORY

| # | Collection | Location | Files | Status | A-Family Coverage |
|---|------------|----------|-------|--------|-------------------|
| 1 | **UFT 100-Paper Series** | `D:\CQE_CMPLX\papers\UFT0-100` | 108 | **Canonical** | paper-00 to paper-103__ |
| 2 | **CQE-Production** | `D:\CQE_CMPLX\CQECMPLX-Production\papers` | 165 | Duplicate/Variant | paper-00 to paper-32 |
| 3 | **REAL-PAPERS** | `D:\CQE_CMPLX\CQECMPLX-Production\REAL-PAPERS` | 14 | Duplicate/Variant | paper-02, paper-04 |
| 4 | **EXPOSE-Papers** | `D:\CQE_CMPLX\CQECMPLX-ProofValidatedSuite\EXPOSE-PAPERS` | 40 | Duplicate/Variant | paper-02 to paper-31 |
| 5 | **Kernel Staging** | `D:\CQE_CMPLX\kernel\staging\papers` | 2,460 | Duplicate/Variant | paper-00 to paper-32 (via suites) |
| 6 | **FLCR Peer Review** | `D:\CQE_CMPLX\flcr_peer_review_work\publication_series` | 679 | Duplicate/Variant | paper-00 to paper-80 (publication-facing) |
| 7 | **1T Production** | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers` | 741 | Duplicate/Variant | paper-00 to paper-32 (with system topics) |
| 8 | **Repo Harvest** | `D:\repo_harvest` | 1,019 | Duplicate | paper-00 to paper-32 (git mirrors) |
| 9 | **Archive** | `D:\_Archive` | 257 | Duplicate/Variant | paper-00 to paper-32 (backups) |
| 10 | **Paper Reworks** | `D:\Paper Reworks` | 11 | Duplicate/Variant | paper-00 to paper-80 (reworks) |
| 11 | **MannyAI** | `D:\MannyAI` | 46 | **Partially Unique** | paper-00, paper-01, paper-02, paper-20, paper-26, paper-37 + unassigned |
| 12 | **Small Collections** | Various (AirLock, R30, Forge, PDF_MASTER, etc.) | ~797 | Duplicate/Variant | paper-00 to paper-32 + unassigned |

### Small Collections Detail

| Sub-Collection | Location | Files | A-Family Mapping |
|----------------|----------|-------|------------------|
| AirLock | `CQECMPLX-AirLock/cqe-production-v0.1/papers` | 18 | paper-00 to paper-32 |
| CMPLX-R30 | `CMPLX-R30-main/PROOF/papers` | 17 | paper-02 (Rule 30) |
| Repo R30 | `repo_harvest/CMPLX-R30/PROOF/papers` | 17 | paper-02 (Rule 30) |
| PDF_MASTER | `PDF_MASTER/PAPER_KITS` | 32 | paper-00 to paper-32 (PDF kits) |
| Forge Lib | `CQECMPLX-Production/lib-forge` | 141 | paper-20 to paper-26 (Forge family) |
| Kernel Forge | `CMPLX-Kernel/lib-forge` | 84 | paper-20 to paper-26 (Forge family) |
| Tool Solvers | `papers_tool_solvers` | 52 | paper-12 to paper-32 (solvers) |
| SM Defining | `flcr_extract/STANDARD_MODEL_DEFINING_PAPERS` | 41 | paper-14 to paper-18 (SM papers) |

---

## 3. A-FAMILY MAPPING BY PAPER NUMBER

### Band A — Foundation (paper-00 to paper-19)

| A-Family | Title | Collections with Duplicates/Variants |
|----------|-------|----------------------------------------|
| paper-00 | Foreword: Burden of Proof, Honesty Discipline, 100-Paper Architecture | UFT (canonical), CQE-Production, 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review, MannyAI (pitch package) |
| paper-01 | The LCR Kernel: 8-State Carrier, Shell Grading, Reversal Involution | UFT (canonical), CQE-Production, 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review, MannyAI (LCR typed kernel) |
| paper-02 | Rule 30 ANF, Lucas Carry, and Cold-Start Readout | UFT (canonical), CQE-Production (CQE-paper-08 maps by cross-ref), EXPOSE-3, EXPOSE-4, REAL-PAPERS (paper1-decomposition), 1T-Production, Archive, Repo Harvest, Staging (suite17, suite13), CMPLX-R30, MannyAI (OCEM1) |
| paper-03 | Correction Surface, F2/Arf Edge Glue, Boundary Repair | UFT (canonical), CQE-Production (CQE-paper-02), EXPOSE-1, 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review |
| paper-04 | D4, J3(O), Triality, and the Magic Square | UFT (canonical), CQE-Production (CQE-paper-03), EXPOSE-5, EXPOSE-2, REAL-PAPERS (paper2-voa), 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review |
| paper-05 | Typed Boundary Repair: Type-Preserving, Idempotent, Arf-Matching | UFT (canonical), CQE-Production (CQE-paper-04), 1T-Production, Archive, Repo Harvest, Staging |
| paper-06 | Oloid Path Carrier: Deterministic Transducer, Graph-Continuous | UFT (canonical), CQE-Production (CQE-paper-05), 1T-Production, Archive, Repo Harvest, Staging |
| paper-07 | Causal Links, Obligation Ledgers, 3-Status Classification | UFT (canonical), CQE-Production (CQE-paper-06), 1T-Production, Archive, Repo Harvest, Staging |
| paper-08 | Discrete-Continuous Bridge: Piecewise-Linear Interpolant | UFT (canonical), CQE-Production (CQE-paper-07), 1T-Production, Archive, Repo Harvest, Staging |
| paper-09 | Lattice Closure: 7-Rung Ladder, No-Cost Leech Lookup | UFT (canonical), CQE-Production (CQE-paper-08), EXPOSE-6, 1T-Production, Archive, Repo Harvest, Staging |
| paper-10 | Temporal Windows and Hamiltonian Readouts | UFT (canonical), CQE-Production (CQE-paper-09), EXPOSE-9, 1T-Production, Archive, Repo Harvest, Staging |
| paper-11 | Master Receipt and Stack Replay: 4 Transport Rows | UFT (canonical), CQE-Production (CQE-paper-10), EXPOSE-10, 1T-Production, Archive, Repo Harvest, Staging |
| paper-12 | Theory Admission Gates: 5 Components, Admissibility | UFT (canonical), CQE-Production (CQE-paper-11), EXPOSE-11, 1T-Production, Archive, Repo Harvest, Staging |
| paper-13 | CA Prediction Surfaces: Bounded CA Enumeration | UFT (canonical), CQE-Production (CQE-paper-12), EXPOSE-12, 1T-Production, Archive, Repo Harvest, Staging |
| paper-14 | Quark-Face Algebra: Exact SU(3) Weyl Closure at Depth 3 | UFT (canonical), CQE-Production (CQE-paper-13), EXPOSE-13, 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review, SM Defining Papers |
| paper-15 | Curvature as Boundary-Repair Demand | UFT (canonical), CQE-Production (CQE-paper-14), EXPOSE-14, 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review |
| paper-16 | Mass Residue and Carrier Accounting: Higgs Anchor 125.25 GeV | UFT (canonical), CQE-Production (CQE-paper-15), EXPOSE-15, 1T-Production, Archive, Repo Harvest, Staging |
| paper-17 | Continuum Edge Residuals: Finite/Local/Explicit Bridge | UFT (canonical), CQE-Production (CQE-paper-16), EXPOSE-16, 1T-Production, Archive, Repo Harvest, Staging |
| paper-18 | Exceptional Towers, VOA Routes, Observer Face Selection | UFT (canonical), CQE-Production (CQE-paper-17, CQE-paper-18, CQE-paper-19), EXPOSE-17, EXPOSE-18, 1T-Production, Archive, Repo Harvest, Staging, FLCR Peer Review |
| paper-19 | Layer-2 Synthesis Ledger: 1,105+ Obligation Rows | UFT (canonical), CQE-Production (CQE-paper-20), EXPOSE-20, 1T-Production, Archive, Repo Harvest, Staging |

### Band B — Standard Model Translation (paper-20 to paper-39)

| A-Family | Title | Collections with Duplicates/Variants |
|----------|-------|----------------------------------------|
| paper-20 | Applied Forge Reader: Materials, Protein, Fold-Facing | UFT (canonical), CQE-Production (CQE-paper-21), EXPOSE-21, EXPOSE-22, EXPOSE-23, 1T-Production, Archive, Repo Harvest, Staging, Forge Lib, MannyAI (SplatForge, Holography) |
| paper-21 | Finite Game Lattices: Nash Equilibrium as Terminal Address | UFT (canonical), CQE-Production (CQE-paper-24, CQE-paper-28), EXPOSE-24, EXPOSE-28, 1T-Production, Archive, Repo Harvest, Staging |
| paper-22 | Energetic Traversal Maps: Energy Landscape as Lattice | UFT (canonical), CQE-Production (CQE-paper-25), EXPOSE-25, 1T-Production, Archive, Repo Harvest, Staging |
| paper-23 | Shear/Plasma/Carrier Horizons | UFT (canonical), CQE-Production (CQE-paper-26), EXPOSE-26, 1T-Production, Archive, Repo Harvest, Staging |
| paper-24 | Observer Delay and Shared-State Protocols | UFT (canonical), CQE-Production (CQE-paper-27), EXPOSE-27, EXPOSE-19, 1T-Production, Archive, Repo Harvest, Staging |
| paper-25 | Monster Ceiling: Large Invariants, McKay-Thompson Coefficients | UFT (canonical), CQE-Production (CQE-paper-29), EXPOSE-29, 1T-Production, Archive, Repo Harvest, Staging |
| paper-26 | CAM/Crystal Projectors and MannyAI Runtime | UFT (canonical), CQE-Production (CQE-paper-30), 1T-Production, Archive, Repo Harvest, Staging, MannyAI (docs, carrier-cem) |
| paper-27 | Corpus Ribbon and Retrospective LCR Readout | UFT (canonical), CQE-Production (CQE-paper-30, CQE-paper-31), EXPOSE-30, EXPOSE-31, 1T-Production, Archive, Repo Harvest, Staging |
| paper-28 | Supervisor Cursor: Cursor as Observer, Supervisor as Carrier | UFT (canonical), CQE-Production (CQE-paper-32), 1T-Production, Archive, Repo Harvest, Staging |
| paper-29 | Gauge Groups Translation: SU(3)xSU(2)xU(1) as D4/F4/E8 Subgroups | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-30 | QCD Color Transport: SU(3) Color as D4 Axis Class | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-31 | Electroweak, Higgs, Mass Residue Translation | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-32 | Electron-Hole-Exciton Accounting | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-33 | GR Curvature/Continuum Translation | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-34 | Condensed Matter/Metamaterials | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-35 | Plasma/Energy/Traversal Calibration | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-36 | Observer/AI Runtime Translation | UFT (canonical), 1T-Production, Archive, FLCR Peer Review, MannyAI (docs) |
| paper-37 | Falsifiers, Comparators, and Standards | UFT (canonical), 1T-Production, Archive, FLCR Peer Review, MannyAI (AI instructions) |
| paper-38 | Grand Reconstruction Map: 8 Gaps → 8 Papers | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |
| paper-39 | Falsifiers, Comparators & Standards (variant) | UFT (canonical), 1T-Production, Archive, FLCR Peer Review |

### Band B' — SM Unification (paper-40 to paper-79)

| A-Family | Title | Collections with Duplicates/Variants |
|----------|-------|----------------------------------------|
| paper-40 | SU(3) Sector Generation 1: Up, Down, Strange | UFT (canonical) |
| paper-41 | SU(3) Sector Generation 2: Charm, Top, Bottom | UFT (canonical) |
| paper-42 | SU(3) Sector Generation 3: All 6 Quarks, CKM as D12 Action | UFT (canonical) |
| paper-43 | Color Confinement: Confinement as Boundary Repair | UFT (canonical) |
| paper-44 | Electroweak Gauge Bosons: W/Z as D4 Sheets | UFT (canonical) |
| paper-45 | Electroweak Symmetry Breaking | UFT (canonical) |
| paper-46 | V-A Weak Interaction: V-A as D4 Sheet Selection | UFT (canonical) |
| paper-47 | Electroweak Phase Diagram | UFT (canonical) |
| paper-48 | Mass Hierarchy and Yukawa | UFT (canonical) |
| paper-49 | Mass and Yukawa 1: Mass Hierarchy | UFT (canonical) |
| paper-50 | Mass and Yukawa 2: CKM and PMNS Matrices | UFT (canonical) |
| paper-51 | Mass and Yukawa 3: BSM Constraints | UFT (canonical) |
| paper-52 | Mass and Yukawa 4: Neutrino Masses, Seesaw, PMNS | UFT (canonical) |
| paper-53 | Higgs and Vacuum 1: Higgs Mechanism | UFT (canonical) |
| paper-54 | Higgs and Vacuum 2: VOA Excited Weight 5 = Higgs | UFT (canonical) |
| paper-55 | Higgs and Vacuum 3: Vacuum Stability | UFT (canonical) |
| paper-56 | Higgs and Vacuum 4: Higgs Couplings | UFT (canonical) |
| paper-57 | QCD Phenomenology 1: Hadron Spectroscopy | UFT (canonical) |
| paper-58 | QCD Phenomenology 2: Parton Distributions | UFT (canonical) |
| paper-59 | QCD Phenomenology 3: Jets and Fragmentation | UFT (canonical) |
| paper-60 | QCD Phenomenology 4: Lattice QCD | UFT (canonical) |
| paper-61 | BSM and Dark 1: Neutrino Masses and Mixing | UFT (canonical) |
| paper-62 | BSM and Dark 2: Dark Matter Candidates | UFT (canonical) |
| paper-63 | BSM and Dark 3: Dark Energy | UFT (canonical) |
| paper-64 | BSM and Dark 4: Inflation | UFT (canonical) |
| paper-65 | GR Side 1: Einstein Field Equation | UFT (canonical) |
| paper-66 | GR Side 2: Black Hole Entropy | UFT (canonical) |
| paper-67 | Cosmology 1: FLRW Derivation | UFT (canonical) |
| paper-68 | Cosmology 2: Cosmological Constant and Dark Energy | UFT (canonical) |
| paper-69 | Cosmology 3: Cosmic Microwave Background | UFT (canonical) |
| paper-70 | Cosmology 4: Large-Scale Structure | UFT (canonical) |
| paper-71 | Calibration Protocols 1: Empirical Measurement Protocols | UFT (canonical) |
| paper-72 | Calibration Protocols 2: Between-Sample Dynamics | UFT (canonical) |
| paper-73 | Calibration Protocols 3: Closure-Stability Sampling | UFT (canonical) |
| paper-74 | Calibration Protocols 4: Between-Sample Dynamics Tests | UFT (canonical) |
| paper-75 | Foundation Math Closure 1: F4 Universality | UFT (canonical) |
| paper-76 | Foundation Math Closure 2: Encoder Invariance | UFT (canonical) |
| paper-77 | Foundation Math Closure 3: Superpermutation Minimality | UFT (canonical) |
| paper-78 | Governance 1: Bibliography, Taxonomy, Claim-Layer Governance | UFT (canonical) |
| paper-79 | Governance 2: First-Routing Implementation | UFT (canonical) |

### Band C — Applications & Clay Millennium Problems (paper-80 to paper-100)

| A-Family | Title | Collections with Duplicates/Variants |
|----------|-------|----------------------------------------|
| paper-80 | UFT: The Closed Form of the Language (2-Category L) | UFT (canonical), FLCR Peer Review |
| paper-81 | Wolfram P1: Rule 30 Non-Periodicity | UFT (canonical), FLCR Peer Review |
| paper-82 | Wolfram P2: Rule 30 Density 1/2 | UFT (canonical), FLCR Peer Review |
| paper-83 | Wolfram P3: Rule 30 Sub-O(n) Extraction | UFT (canonical), FLCR Peer Review |
| paper-84 | Yang-Mills Mass Gap | UFT (canonical), FLCR Peer Review |
| paper-85 | Navier-Stokes Existence and Smoothness | UFT (canonical), FLCR Peer Review |
| paper-86 | Riemann Hypothesis | UFT (canonical), FLCR Peer Review |
| paper-87 | Hodge Conjecture | UFT (canonical), FLCR Peer Review |
| paper-88 | P vs NP | UFT (canonical), FLCR Peer Review |
| paper-89 | BSD Conjecture | UFT (canonical), FLCR Peer Review |
| paper-90 | McKay-Thompson Parity and Rule 30 Correction Collapse | UFT (canonical), FLCR Peer Review |
| paper-91 | Niemeier Glue, Leech Invariants, and Gamma72 Landing | UFT (canonical), FLCR Peer Review |
| paper-92 | F4 Universality Theorem | UFT (canonical), FLCR Peer Review |
| paper-93 | Cold-Start Terminal | UFT (canonical), FLCR Peer Review |
| paper-94 | Encoder Invariance Theorem | UFT (canonical), FLCR Peer Review |
| paper-95 | SPINOR Observation | UFT (canonical), FLCR Peer Review |
| paper-96 | Superpermutation Minimality Theorem | UFT (canonical), FLCR Peer Review |
| paper-97 | EHX Accounting | UFT (canonical), FLCR Peer Review |
| paper-98 | Reasoned Reapplication | UFT (canonical), FLCR Peer Review |
| paper-99 | Applied Forge Validation | UFT (canonical), FLCR Peer Review |
| paper-100 | Capstone: Synthesis, 2-Category L, 8 Irreducible Gaps | UFT (canonical), FLCR Peer Review |

### Extended Versions (paper-91__ to paper-95__)

| A-Family | Title | Collections |
|----------|-------|-------------|
| paper-91__ | Niemeier Glue, Leech, Gamma72 (Extended) | UFT (canonical) |
| paper-92__ | F4 Universality Theorem (Extended) | UFT (canonical) |
| paper-93__ | Cold-Start Terminal (Extended) | UFT (canonical) |
| paper-94__ | Encoder Invariance (Extended) | UFT (canonical) |
| paper-95__ | SPINOR Observation (Extended) | UFT (canonical) |

### Extra Papers (paper-101__ to paper-103__)

| A-Family | Title | Collections |
|----------|-------|-------------|
| paper-101__ | Positive Grassmannian Bridge | UFT (canonical) |
| paper-102__ | Albert Algebra Formalization Study | UFT (canonical) |
| paper-103__ | Formal Math Claims Registry | UFT (canonical) |

---

## 4. DUPLICATE ANALYSIS

### 4.1 By Filename Duplication (from Source Index Appendix C)

Of the 8,227 paper files, **1,486 duplicate filenames** were identified across different directories:

| Duplicate Category | Filename | Copies | A-Family Mapping |
|--------------------|----------|--------|------------------|
| Template proliferation | FORMAL_PAPER.md | 291 | paper-00 to paper-32 (per-paper formal templates) |
| Template proliferation | analog_contract.md | 240 | paper-00 to paper-32 |
| Template proliferation | journal_skeleton.md | 240 | paper-00 to paper-32 |
| Template proliferation | semantic_contract.md | 240 | paper-00 to paper-32 |
| OpsGuide proliferation | OpsGuide.md | 216 | paper-00 to paper-32 (auto-generated per suite) |
| OpsGuide proliferation | OpsGuide.pdf | 128 | paper-00 to paper-32 |
| Companion/workbook pairs | companion.md | 119 | paper-00 to paper-80 (paired with formal papers) |
| Companion/workbook pairs | formal.md | 119 | paper-00 to paper-80 |
| Companion/workbook pairs | workbook.md | 119 | paper-00 to paper-80 |
| Generated artifacts | paper.pdf | 81 | paper-00 to paper-32 (build outputs) |
| Generated artifacts | paper.tex | 80 | paper-00 to paper-32 (build outputs) |
| Generated artifacts | SOURCE_PLACEMENT.md | 80 | paper-00 to paper-32 |
| Core paper duplicates | PAPER-BODY.md | 67 | paper-00 to paper-32 (CQE standard files) |
| Core paper duplicates | SOURCE.md | 67 | paper-00 to paper-32 (CQE standard files) |

**Net unique paper content after deduplication: ~6,700+ distinct papers.**

### 4.2 By Collection Type

| Category | Collections | File Count | Duplicate Status |
|----------|-------------|------------|------------------|
| **Canonical A-Family** | UFT 100-Paper Series | 108 | Unique canonical |
| **Exact duplicates** | Repo Harvest, Archive backups, Staging mirrors | ~3,736 | Multiple copies of same content |
| **Variant duplicates** | CQE-Production (.25/.50/.75/UPGRADED/RECURSIVE_CLOSE), 1T-Production | ~900 | Same base paper, different variant suffixes |
| **Template/ops duplicates** | OpsGuide, FORMAL_PAPER.md, companion.md across all collections | ~1,486 | Structural duplicates |
| **Unique/unassigned** | MannyAI research, system architecture docs, comparison studies | ~46 | Partially unique |

---

## 5. UNASSIGNED CONTENT

The following content **cannot be directly mapped** to a specific A-family paper number (paper-00 through paper-100). These are system documents, architecture maps, research notes, and auxiliary materials.

### 5.1 System Architecture Documents (unassigned)

| Source | Files | Description |
|--------|-------|-------------|
| 1T-Production `master_topics/PartsFactory_Seed_Atlas/` | 30 | S41-S70 system architecture topics (14-family taxonomy, 19 capability domains, 11-layer SNAP fabric, 9 global APIs, etc.) |
| 1T-Production `master_topics/Rule30_Prize_Problems/` | 4 | Prize problem master solutions (P1, P2, P3) — these map to paper-02 but are auxiliary solution documents |
| 1T-Production `dyad_briefs/` | 5 | Block and lane dyad briefs (read-only synthesis documents) |
| CQE-Production `DyadBriefs/` | 5 | Same dyad briefs mirrored |
| FLCR Peer Review matrices | ~40 | State-bound proof contract matrix, archive evidence card matrix, dimensional ribbon map, claim binding queue, etc. |
| Paper Reworks manifests | 5 | Discovery agent manifest, evidence intake notebook, slot ontology, assembly audit pass, pairwise evidence protocol |

### 5.2 MannyAI Unique Documents (unassigned)

| Document | Description | Closest A-Family |
|----------|-------------|------------------|
| `OCEM1_ACCURACY_RESULT.md` | Cold-start vs trained accuracy measurement | paper-02 (Rule 30) |
| `GS08_PARITY_RESULT.md` | CPU/GPU render parity on Vulkan | paper-26 (CAM/Crystal) |
| `CARRIER_CEM_FULLSTACK_DEFINITION.md` | Fullstack computational engineering model | paper-01 (LCR carrier) |
| `HOLOGRAPHY_COMPOSITION.md` | Holography by composition design note | paper-20 (Applied Forge) |
| `LCR_TYPED_KERNEL.md` | L/C/R typed kernel specification | paper-01 (LCR kernel) |
| `PITCH_PACKAGE.md` | CQE-CMPLX pitch package | paper-00 (Foreword) |
| `SPLATFORGE_FIELD_RUNTIME_v0_1.md` | SplatForge field runtime | paper-20 (Applied Forge) |
| `leap71_vs_cqecmplx.md` | LEAP71 vs CQE-CMPLX deep comparison | paper-22 (MetaForge) |
| `ai-instructions/01-FIRST-ROUTING.md` | First routing through CAM crystal | paper-37 (Falsifiers/Standards) |
| `ai-instructions/02-CAM-CRYSTAL-OPERATIONS.md` | CAM crystal operations toolkit | paper-26 (CAM/Crystal) |
| `ai-instructions/03-HONESTY-DOCTRINE.md` | Honesty doctrine: proven vs open | paper-00 (Foreword) |
| `ai-instructions/04-MANNYAI-ARCHITECTURE.md` | MannyAI architecture layers | paper-36 (Observer/AI Runtime) |
| `ai-instructions/05-BUILD-INCREMENT-PATTERN.md` | Build increment pattern | paper-37 (Standards) |
| `ai-instructions/06-NAMING-CANON.md` | Naming canon authority | paper-37 (Standards) |
| `ai-instructions/07-STALENESS-POLICY.md` | Staleness policy | paper-37 (Standards) |
| `ai-instructions/08-OPEN-OBLIGATION.md` | Open obligation error philosophy | paper-00 (Foreword) |
| `ai-instructions/09-CODE-REUSE-AUTHORITY.md` | Code reuse authority | paper-37 (Standards) |

### 5.3 Small Collection Unassigned

| Collection | Unassigned Files | Description |
|------------|------------------|-------------|
| `papers_tool_solvers` | 52 | Tool and solver implementations (not paper content) |
| `CMPLX-Kernel/lib-forge` | 84 | Kernel-level forge libraries (implementation code) |
| `CQECMPLX-Production/lib-forge` | 141 | Production forge libraries (implementation code) |
| `CQECMPLX-AirLock/cqe-production-v0.1/papers` | 18 | AirLock production papers (CQE variants) |
| `PDF_MASTER/PAPER_KITS` | 32 | PDF generation kits (build artifacts) |
| `flcr_extract/STANDARD_MODEL_DEFINING_PAPERS` | 41 | SM defining papers (extracts, not canonical) |

---

## 6. SUMMARY BY THE NUMBERS

| Metric | Value |
|--------|-------|
| **Total files identified** | 8,227 |
| **Total size** | 221.93 MB |
| **A-family canonical papers** | 108 (paper-00 to paper-103__) |
| **A-family with duplicate variants** | paper-00 to paper-32 (~900 variant files) |
| **A-family unique (no duplicates)** | paper-33 to paper-100 |
| **Duplicate filename count** | 1,486 |
| **Unique content after dedup** | ~6,700+ |
| **Collections mapped** | 12 |
| **Unassigned documents** | ~300+ |

### Mapping Coverage Summary

| A-Family Range | Canonical Papers | Duplicate/Variant Collections | Unique Status |
|----------------|------------------|----------------------------|---------------|
| paper-00 to paper-32 | 33 papers | CQE-Production, 1T-Production, EXPOSE, Archive, Repo Harvest, Staging, FLCR Peer Review, MannyAI | **Heavily duplicated** |
| paper-33 to paper-79 | 47 papers | UFT only, plus FLCR Peer Review (publication-facing) | **Unique to A-family** |
| paper-80 to paper-100 | 21 papers | UFT only, plus FLCR Peer Review (publication-facing) | **Unique to A-family** |
| paper-91__ to paper-95__ | 5 extended | UFT only | **Unique to A-family** |
| paper-101__ to paper-103__ | 3 extra | UFT only | **Unique to A-family** |

---

## 7. KEY MAPPING PRINCIPLES APPLIED

1. **All B-family numbering stripped.** CQE-paper-00, CQE-paper-01, etc. are mapped to paper-00, paper-01. EXPOSE-1 through EXPOSE-31 are mapped to their corresponding A-family papers by topic and cross-reference.

2. **Variant suffixes normalized.** Files like `CQE-paper-00.25.md`, `CQE-paper-00.50.md`, `CQE-paper-00.75.md`, `CQE-paper-00_UPGRADED.md`, `CQE-paper-00_RECURSIVE_CLOSE.md` are all treated as variants of paper-00, not as separate A-family papers.

3. **Cross-reference table honored.** The Wolfram Prize, Lattice Code Chain, Standard Model Mapping, and Forge Family tables from the source index were used to map EXPOSE and CQE papers to A-family numbers.

4. **Repo mirrors and archives treated as duplicates.** Git mirrors (`repo_harvest`), backup snapshots (`_Archive`), and staging suites contain the same content as CQE-Production with different paths.

5. **System documents left unassigned.** Architecture topics (S41-S70), dyad briefs, agent manifests, evidence notebooks, and tool solver code are not paper content and do not map to the A-family 100-paper series.

---

*Catalog compiled from systematic reading of MASTER_PAPER_INDEX.md (7,708 lines). All B-family identifiers (CQE, FLCR, NIST, CMPLX, EXPOSE) have been translated to A-family canonical numbering (paper-00 through paper-100).*
