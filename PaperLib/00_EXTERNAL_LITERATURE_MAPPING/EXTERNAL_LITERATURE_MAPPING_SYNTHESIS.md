# CQE/CMPLX External Literature Mapping — Master Synthesis Report
## Nine-Round Comprehensive Sweep | 2026-07-03

**Compiled by:** CQE/CMPLX active-rework lead  
**Scope:** 108 papers, preprints, white papers, and technical reports mapped to the CQE 00–32 + UFT 0–100 paper corpus  
**Coverage:** 36 domains, 27 copy-paste-ready integration paragraphs, 27 priority actions with deadlines  
**Competing frameworks identified:** 5 (FIRM, MNT, SRC, U₂₄, J₃(𝕆) mass-ratio models)  
**Critical obsolete findings:** 1 (Papers 33–40, Spectre tile)  

---

## Executive Summary

A systematic nine-round literature sweep working backward from 2026-07-03 has catalogued 108 cutting-edge publications that intersect with the CQE/CMPLX paper corpus. The sweep covered:

- **Pure mathematics:** Moonshine/VOA, E8 bracket derivation, Kakeya 3D geometry, positive Grassmannian/amplituhedron, Albert algebra formalization
- **Particle physics:** Higgs precision (125.11 GeV), W-mass resolution (80360.2 MeV), neutrino hierarchy (JUNO), CKM unitarity anomaly, QCD phase diagram, axion dark matter (ADMX), NANOGrav nHz GW background
- **Gravity/GR:** Numerical relativity (EFE on lattice), GWTC-4.0 precision tests, LIGO/Virgo/KAGRA constraints
- **Quantum computing:** Google Willow below-threshold QEC, D4/E8 lattice gauge theory for quantum simulation
- **AI/Formal verification:** DeepMind Aletheia (autonomous math research), DeepSeek-Prover-V2, Goedel-Prover-V2, LEGO-Prover, LeanDojo, TLA⁺/TLAPS LLM automation, PhysLean, SU(5) Lean API, MerLean, Lean4Agent
- **Materials/biology:** AlphaFold3, Boltz-2, Protenix-v1, superpermutations, topological materials
- **Competing frameworks:** FIRM (E8 unification), MNT (preprint), SRC (cosmological lattice), U₂₄ (Ω=24 universality), J₃(𝕆) mass-ratio models

**Key existential findings:**
1. **Papers 33–40 are obsolete** — Smith et al. 2023 proved the Spectre tile, making CQE's aperiodic tiling claims redundant. Action: demote to ECO/IBN by 2026-07-05.
2. **U₂₄ Universality Programme** (GitHub 2026) is a critical competitor using identical core objects (Leech lattice, Monster, 24) and claiming all Clay problems. Action: differentiate immediately (P25, deadline 2026-07-05).
3. **Singh 2020/2021** derives α = 1/137.04006 from the Albert algebra — a benchmark CQE must match or explain.
4. **Numerical relativity** validates GR on a lattice as canonical physics — CQE must acknowledge this and map "repair curvature" to "constraint damping."
5. **PhysLean + SU(5) Lean API** prove that physics formalization in Lean 4 is achievable in 2026 — CQE should adopt this as its formal verification target.

---

## 1. Deliverables Inventory

### Reports (8 documents)

| Document | Papers | Domains | Paragraphs | File |
|----------|--------|---------|------------|------|
| Main Report (Round 1) | 34 | 13 | 0 | `EXTERNAL_LITERATURE_MAPPING_REPORT_2026-07-03.md` |
| Supplement A (Round 2) | 22 | 5 | 5 | `..._SUPPLEMENT_A.md` |
| Supplement B (Round 3) | 8 | 5 | 5 | `..._SUPPLEMENT_B.md` |
| Supplement C (Round 4) | 9 | 3 | 3 | `..._SUPPLEMENT_C.md` |
| Supplement D (Round 5) | 5 | 3 | 2 | `..._SUPPLEMENT_D.md` |
| Supplement E (Round 6) | 8 | 4 | 3 | `..._SUPPLEMENT_E.md` |
| Supplement F (Round 7) | 8 | 4 | 3 | `..._SUPPLEMENT_F.md` |
| Supplement G (Round 8) | 7 | 3 | 3 | `..._SUPPLEMENT_G.md` |
| Supplement H (Round 9) | 7 | 4 | 3 | `..._SUPPLEMENT_H.md` |
| **Master Index** | — | — | — | `EXTERNAL_LITERATURE_MAPPING_INDEX.md` |
| **This Synthesis** | — | — | — | `EXTERNAL_LITERATURE_MAPPING_SYNTHESIS.md` |

### Priority Actions (27 items with deadlines)

| Tier | Actions | Deadline Range | Description |
|------|---------|---------------|-------------|
| **CRITICAL** | P2, P15, P25 | 2026-07-05 | Spectre obsolescence, Rule 30 irreducibility, U₂₄ differentiation |
| **HIGH** | P1, P3, P6, P16, P19, P20, P22, P27 | 2026-07-10 to 2026-07-20 | W-mass update, E8 derivation, Higgs calibration, axion prediction, AI ATP validation, D4 LGT, GR mapping, α derivation |
| **MEDIUM** | P4, P5, P7, P8, P9, P10, P11, P12, P13, P14, P17, P18, P21, P23, P24, P26 | 2026-07-15 to 2026-07-25 | QEC benchmark, competitor comparison, neutrino/CKM predictions, receipt standardization, game verification, GR calibration, complexity class, energy landscape, formal verification backbone, cosmological GW, QCD phase, agent architecture, Lean adoption, agent workflow, positive geometry |

### Draft Integration Paragraphs (27 copy-paste-ready)

Each paragraph is ready to insert into the target CQE paper with `[INSERT VALUE]` placeholders for CQE-specific predictions. See the Master Index §4 for the full table mapping paragraph # → topic → target paper → placement → source file.

---

## 2. Domain Coverage Matrix

| Domain | Papers | Tier A | CQE Papers Served | Status |
|--------|--------|--------|-------------------|--------|
| Moonshine / VOA | 5 | 3 | 18, 25, Paper 00 | Gap-closure candidate |
| E8 / Exceptional groups | 6 | 4 | 04, 29, 30, NP-04 | Gap-closure candidate |
| Higgs physics | 4 | 3 | 15, 16, NP-06 | Calibration anchor |
| W-boson / Electroweak | 3 | 2 | 13, 31, 44–47 | Calibration anchor |
| Neutrino physics | 3 | 2 | 13, NP-04 | Gap-closure candidate |
| CKM / Flavor physics | 3 | 2 | 13, 42, NP-04 | Gap-closure candidate |
| QCD / Lattice gauge theory | 5 | 3 | 29, 30, 43, Paper 13 | Gap-closure candidate |
| GR / Numerical relativity | 4 | 3 | 33–35, 17 | Gap-closure candidate |
| GW physics | 4 | 2 | 14, NP-06 | Calibration anchor |
| Axion / Dark matter | 2 | 1 | 13, NP-06 | Calibration anchor |
| Cosmology / Early universe | 4 | 2 | 14, NP-06, Paper 100 | Calibration anchor |
| Quantum computing / QEC | 3 | 2 | NP-07 | Calibration anchor |
| AI / Automated theorem proving | 10 | 6 | NP-08, NP-13, Paper 28, 36 | Gap-closure candidate |
| Formal verification / Lean | 6 | 4 | NP-08, Papers 29–32 | Gap-closure candidate |
| Positive geometry / Grassmannian | 4 | 1 | Paper 101__ | Gap-closure candidate |
| Albert algebra / J₃(𝕆) | 4 | 2 | Papers 4, 14, 16, 102__ | Calibration anchor |
| Aperiodic tilings | 3 | 1 | Papers 33–40 | **OBSOLETE** |
| Game theory / Complexity | 4 | 2 | Papers 21, 24, 28, NP-11 | Gap-closure candidate |
| Proteins / Structural biology | 3 | 2 | Paper 20, 23 | Benchmark required |
| Metamaterials / Condensed matter | 3 | 1 | Paper 34 | Analogical support |
| Thermodynamics / Active matter | 3 | 1 | Papers 20, 25, 29 | Analogical support |
| Receipt ecology / SBOM | 3 | 1 | NP-05 | Standardization required |
| Agent verification | 4 | 2 | Papers 28, 36 | Gap-closure candidate |
| Discrete geometry / Kakeya | 2 | 1 | Paper 09, NP-03 | Analogical support |
| Spinor gases / Observer physics | 3 | 1 | Papers 24, 36, NP-10 | Analogical support |
| Computational complexity | 3 | 1 | Papers 21, 24, 28, NP-11 | Analogical support |
| Non-commutative geometry | 2 | 1 | NP-04 | Analogical support |
| Competing frameworks | 5 | 5 | Paper 00, Meta | **EXISTENTIAL** |
| Clay Millennium Problems | 3 | 1 | Papers 80–100 | Contextual |
| Primordial physics / Inflation | 2 | 1 | Paper 14, NP-06 | Calibration anchor |
| Topological materials | 2 | 1 | Paper 34 | Analogical support |
| SPINOR / Quantum information | 2 | 1 | Papers 24, 36, NP-10 | Analogical support |
| Wolfram Physics Project | 2 | 1 | Papers 80–100 | Contextual |
| Quantum simulation | 3 | 2 | Papers 29–30, NP-07 | Gap-closure candidate |
| **TOTAL** | **108** | **~43** | **All 32 + UFT 0–100** | **Comprehensive** |

---

## 3. The Five Competing Frameworks — Detailed Comparison

### 3.1 FIRM (ktynski, 2025, GitHub)
- **Core claim:** E8-based unification using lattice-QCD-inspired numerical methods
- **Overlap with CQE:** E8, lattice structures, gauge group embedding
- **Differentiation:** FIRM is a computational/numerical approach; CQE is algebraic/formal. FIRM does not use the FLCR substrate or receipt discipline.
- **Threat level:** MEDIUM — different methodology, same target

### 3.2 MNT (2025, Preprint)
- **Core claim:** Mathematical unification theory using exceptional Lie algebras
- **Overlap with CQE:** E8, F4, D4, triality, magic square
- **Differentiation:** MNT is a preprint with limited formalization; CQE has explicit receipt structure and calibration to physical data.
- **Threat level:** MEDIUM — similar vocabulary, weaker evidence standards

### 3.3 Scalar Relaxation Cosmology (SRC, warpXspeed, 2025–2026, GitHub)
- **Core claim:** Cosmological evolution via scalar field relaxation on a lattice substrate
- **Overlap with CQE:** "Lattice substrate" vocabulary, cosmological predictions, discrete spacetime
- **Differentiation:** SRC is a cosmology-only framework; CQE spans all physics scales. SRC does not use exceptional algebras or the FLCR receipt system.
- **Threat level:** MEDIUM — vocabulary overlap, different scope

### 3.4 U₂₄ Universality Programme (OriginNeuralAI, 2026, GitHub) — **CRITICAL**
- **Core claim:** Ω = 24 governs all six remaining Clay Millennium Problems via G₂₄ → Leech → Monster
- **Overlap with CQE:** Leech lattice Λ₂₄, Monster group, the number 24, all Clay problems, Golay code
- **Differentiation:** U₂₄ postulates 24 as a constant; CQE derives 24 from the Freudenthal–Tits magic square (1→3→7→8→24→72). U₂₄ uses self-verified checks; CQE requires independent falsifiers.
- **Threat level:** **CRITICAL** — identical core objects, broader claims, weaker standards

### 3.5 J₃(𝕆) Mass-Ratio Models (Singh 2020/2021, TIFR; Emergent Mind 2025)
- **Core claim:** Albert algebra eigenvalues reproduce quark mass ratios and α = 1/137.04006
- **Overlap with CQE:** J₃(𝕆), F4 symmetry, quark masses, three generations, CKM
- **Differentiation:** Singh uses characteristic equation eigenvalues; CQE uses VOA weight assignment (κ = 25.05 GeV). Singh derives α; CQE does not currently.
- **Threat level:** HIGH — direct quantitative competition for core predictions

---

## 4. Gap-Closure Status by CQE Paper

| CQE Paper | External Anchors | Gap Status | Priority Actions |
|-----------|-----------------|------------|----------------|
| Paper 00 (Foreword) | FIRM, MNT, SRC, U₂₄ | **Open** | P5, P25 |
| Paper 01 (LCR Kernel) | Rule 30 status | **Open** | P15 |
| Paper 02 (Rule 30) | DeepSeek-Prover-V2 cold-start | **Partial** | P15 |
| Paper 03 (Correction surface) | — | No direct anchors | — |
| Paper 04 (D4/J₃(𝕆)/F4/E8) | Kollross 2025, Singh 2020, Emergent Mind 2025, SageMath | **Open** | P3, P27 |
| Paper 05 (Boundary repair) | — | No direct anchors | — |
| Paper 06 (Oloid path) | — | No direct anchors | — |
| Paper 07 (Causal links) | — | No direct anchors | — |
| Paper 08 (Discrete-continuous bridge) | — | No direct anchors | — |
| Paper 09 (Lattice closure) | Kakeya 3D, KakeyaLattice 2026 | **Partial** | P20 |
| Paper 10 (Temporal windows) | — | No direct anchors | — |
| Paper 11 (Master receipt) | SBOM/SLSA, LeanListener | **Partial** | P9 |
| Paper 12 (Theory admission) | — | No direct anchors | — |
| Paper 13 (CA prediction) | CMS 2026, JUNO 2025, CKM 2026, ADMX 2025, QCD phase 2025 | **Open** | P1, P7, P8, P16, P18 |
| Paper 14 (Quark-face algebra) | Singh 2020, Emergent Mind 2025 | **Open** | P27 |
| Paper 15 (Curvature) | GWTC-4.0 2026 | **Partial** | P11 |
| Paper 16 (Mass residue) | ATLAS 2026, Singh 2020 | **Open** | P6, P27 |
| Paper 17 (Continuum edge) | Numerical relativity | **Partial** | P22 |
| Paper 18 (Exceptional towers) | — | No direct anchors | — |
| Paper 19 (Synthesis ledger) | — | No direct anchors | — |
| Papers 20–23 (Applied forge) | AlphaFold3, Boltz-2, Protenix-v1 | **Open** | Benchmark required |
| Papers 24 (Observer delay) | Unruh effect 2026, de Sitter observer 2025 | **Partial** | — |
| Papers 25 (Monster ceiling) | — | No direct anchors | — |
| Paper 26 (CAM/Crystal) | LEGO-Prover | **Partial** | — |
| Papers 28 (Supervisor cursor) | Aletheia, Cursor, LeanListener, MerLean, Lean4Agent | **Open** | P21, P24 |
| Papers 29–32 (Gauge/QCD/EM) | Pradhan 2023 D4 LGT, KakeyaLattice 2026, PhysLean, SU(5) API | **Open** | P20, P23 |
| Papers 33–35 (GR/EFE/Plasma) | Numerical relativity | **Open** | P22 |
| Papers 36 (Observer/AI) | MerLean, Lean4Agent | **Open** | P24 |
| Papers 37–39 (Falsifiers/Standards) | SBOM/SLSA | **Partial** | P9 |
| Papers 40–79 (SM Unification) | PhysLean, SU(5) API, Singh 2020 | **Open** | P23, P27 |
| Papers 80–100 (Band C) | U₂₄, Clay lectures, Wolfram Physics | **Open** | P25, P26 |
| Paper 101__ (Grassmannian) | Amplituhedron, Speyer-Williams, Even-Zohar 2025 | **Open** | P26 |
| Paper 102__ (Albert algebra) | Singh 2020, SageMath, nLab | **Open** | P27 |
| Paper 103__ (Claims registry) | — | No direct anchors | — |
| NP-03 (Terminal selection) | KakeyaLattice 2026 | **Partial** | — |
| NP-04 (E8 derivation) | Kollross 2025 | **Open** | P3 |
| NP-05 (Receipt ecology) | SBOM/SLSA, TLA⁺/TLAPS | **Open** | P9, P14 |
| NP-06 (Cosmology) | ADMX 2025, NANOGrav, QCD phase 2025 | **Open** | P16, P17, P18 |
| NP-07 (QEC) | Google Willow 2025 | **Open** | P4 |
| NP-08 (Formal verification) | TLA⁺/TLAPS, PhysLean, SU(5) API, QFT Lean | **Open** | P14, P23 |
| NP-10 (Observer model) | Unruh effect 2026, de Sitter observer 2025 | **Partial** | — |
| NP-11 (Game theory) | Walnut, complexity classes | **Open** | P10, P12 |
| NP-12 (Electron-hole) | Exciton EFKM model | **Partial** | — |
| NP-13 (Reapplication) | Aletheia, LEGO-Prover, Goedel-Prover-V2, DeepSeek-Prover-V2 | **Open** | P19 |

---

## 5. The 27 Priority Actions — Consolidated Roadmap

### Phase 1: Existential Risk (Execute by 2026-07-05)
- **P2:** Demote Papers 33–40 (Spectre is obsolete)
- **P15:** Demote Paper 01 irreducibility claims (Rule 30 is conjectural)
- **P25:** Differentiate from U₂₄ (48-hour critical action)

### Phase 2: Physical Calibration (Execute by 2026-07-15)
- **P1:** Rewrite Paper 13 (W-mass, JUNO, CKM, Higgs)
- **P3:** Derive E8 bracket or cite Kollross 2025
- **P6:** Calibrate Higgs to ATLAS 125.11 GeV
- **P7:** Add neutrino predictions
- **P8:** Address CKM unitarity anomaly
- **P11:** Calibrate Paper 14 to GWTC-4.0
- **P16:** Add axion prediction
- **P17:** Add NANOGrav/IPTA GW prediction
- **P18:** Predict QCD critical point
- **P20:** Add D4 LGT citations
- **P22:** Add numerical relativity mapping

### Phase 3: Formalization & Validation (Execute by 2026-07-25)
- **P4:** Benchmark NP-07 against Willow
- **P5:** Add falsifiability comparison (FIRM, MNT)
- **P9:** Standardize receipts (SBOM/SLSA)
- **P10:** Verify NP-11 with Walnut
- **P12:** State game complexity class
- **P13:** Classify energy landscape regime
- **P14:** Adopt TLA⁺/TLAPS backbone
- **P19:** Add AI ATP citations to NP-13
- **P21:** Add agent architecture citations
- **P23:** Adopt Lean 4 formalization
- **P24:** Add agent verification citations
- **P26:** Add positive geometry to Paper 101__
- **P27:** Derive α or address Singh's result

---

## 6. Recommendations

### Immediate (Next 48 Hours)
1. **Execute P25:** Write U₂₄ differentiation paragraph and add to Paper 00. This is existential.
2. **Execute P2:** Mark Papers 33–40 as ECO/IBN. Do not let obsolete claims propagate.
3. **Execute P15:** Update Paper 01 to state Rule 30 irreducibility is conjectural.

### Short-Term (Next 2 Weeks)
4. **Execute P1, P3, P6, P27:** Physical calibration is the highest-value differentiator. CQE's claims must have explicit numerical predictions with error bars.
5. **Execute P14, P23:** Formalization in Lean 4 (building on PhysLean) is the highest-opportunity item. A formalized CQE would be unique among competing frameworks.
6. **Execute P19, P21, P24:** The AI/ATP literature validates CQE's reapplication and cursor concepts. Cite these to show CQE is ahead of the curve, not behind it.

### Medium-Term (Next Month)
7. **Execute P4, P9, P10, P11, P12, P13:** Benchmarking and standardization transform CQE from a theoretical framework into a verifiable, reproducible system.
8. **Register all 108 papers in `.cqe/` CAM** with tags for traceability.
9. **Create `CQE_Corpus.lean`** building on PhysLean definitions. Even partial formalization (D4 codec, lattice code chain) would be a significant achievement.

### Ongoing
10. **Monitor U₂₄, FIRM, MNT, SRC developments.** Set up automated alerts (arXiv, GitHub) for new publications from these competitors.
11. **Maintain the priority action tracker.** Update the Master Index as actions are completed and new papers are discovered.

---

## 7. Conclusion

The nine-round literature sweep has produced a comprehensive, actionable mapping of 108 cutting-edge publications to the CQE/CMPLX corpus. The findings reveal both significant opportunities (formalization in Lean 4, AI/ATP validation, numerical relativity precedent) and critical risks (U₂₄ competitor, obsolete Spectre claims, unmet α prediction). The 27 priority actions provide a clear, deadline-driven roadmap for closing gaps and differentiating CQE from competitors. The corpus is now sufficiently comprehensive that further rounds should be targeted at specific emerging areas (e.g., new LHC results, quantum computing milestones, AI math breakthroughs) rather than broad sweeps.

**The most important next step is execution of P25 (U₂₄ differentiation) within 48 hours, followed by P1–P3 (physical calibration) within two weeks.**

---

*Synthesis compiled: 2026-07-03*  
*Total rounds: 9*  
*Total papers: 108*  
*Total domains: 36*  
*Total paragraphs: 27*  
*Total actions: 27*  
*Critical competitors: 5*  
*Existential risks: 2 (U₂₄, Spectre obsolescence)*
