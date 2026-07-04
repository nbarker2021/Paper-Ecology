# CQE/CMPLX External Literature Mapping Report

## Supplement T — Round 21 | 2026-07-03

**New domains covered:** 5  
**New papers added:** 5  
**Cumulative totals:** 185 papers, 98 domains, 75 draft integration paragraphs, 86 priority actions

---

## 1. New External Papers Catalogued (Round 21)

### T-1. JWST "Little Red Dots" — Primordial Black Hole Seeds for Early SMBHs
- **Reference:** Dayal et al., *A&A* (2024–2026); Zhang et al., *ApJ* 1000, L19 (2026); Carr et al., arXiv:2601.008xx (2026); Chon et al., arXiv:2601.008xx (2026)
- **Key claims:** JWST discovers supermassive black holes (10⁶–10⁹ M⊙) at z ~ 8–10 in unexpectedly small, metal-poor host galaxies ("little red dots" / LRDs); black hole-to-galaxy mass ratio ~10% (vs. 0.005% locally); primordial black holes (PBHs) of 10³–10⁵ M⊙ may serve as seeds; PBH fraction f_PBH ≤ 10⁻² for M ≥ 10⁷ M⊙
- **Date:** 2024–2026 (rapid development)
- **Tier:** A (direct cosmological calibration anchor)
- **CQE relevance:** CQE's cosmological framework must address early-universe structure formation. If CQE predicts primordial black holes from the lattice substrate, it must specify their mass spectrum and abundance. The LRD observations provide a new falsifiability test: CQE must predict SMBH seed masses compatible with JWST z ~ 10 observations.

### T-2. LHC Run 3 Higgs Precision — Higgs→Charm and Di-Higgs Production
- **Reference:** CMS Collaboration (Higgs Hunting Workshop, July 2025/2026); ATLAS Run 3 results; Gallinaro, "Recent results on the Higgs boson" (Cyprus 2025)
- **Key claims:** Run 3 data reduces Higgs→μμ and H→Zγ uncertainties by 30–38%; first sensitivity to Higgs→c-cbar (charm quark coupling) via ttH production; di-Higgs (HH) sensitivity in bbγγ now surpasses all Run 2 channels combined; signal strength μ = 1.01⁺⁰·⁰⁶₋₀.₀₅; Higgs invisible width BR < 11% at 95% CL
- **Date:** 2025–2026
- **Tier:** A (direct HEP calibration anchor)
- **CQE relevance:** CQE Papers 33 and 49 must predict the full set of Higgs couplings including κ_c (charm quark), κ_μ (muon), and κ_λ (self-coupling). Run 3 is rapidly improving these measurements. If CQE cannot predict κ_c, it misses a major SM test. The di-Higgs channel is the gateway to Higgs self-coupling measurement.

### T-3. LHC Run 3 Collider Neutrino Program — FASER/SND@LHC
- **Reference:** Annual Reviews of Nuclear and Particle Science (2026); FASER/SND@LHC Collaborations
- **Key claims:** First collider neutrino observations (2023); ~10,000 neutrinos expected by end of Run 3 (mid-2026); electron neutrino interactions observed; tau neutrino interactions imminent; novel tests of lepton universality; probe of intrinsic charm, gluon saturation, ultralow-x PDFs; constraints on light dark-sector particles
- **Date:** 2023–2026
- **Tier:** B (calibration anchor — neutrino physics)
- **CQE relevance:** CQE's neutrino predictions (P54–P55, P71) must address not only oscillation experiments (JUNO, DUNE, Hyper-K) but also collider neutrino physics. FASERν and SND@LHC measure neutrino cross-sections at TeV energies — a complementary probe of neutrino interactions that CQE should address or explicitly exclude from scope.

### T-4. Long-Horizon AI Autoformalization — LeanMarathon & Munkres Topology
- **Reference:** LeanMarathon (arXiv:2606.05400, June 2026); Munkres Autoformalization (arXiv:2604.07455, April 2026); Vlasov-Maxwell-Landau (arXiv:2603.15929, March 2026)
- **Key claims:** LeanMarathon: first systematic approach to long-horizon (multi-day) Lean 4 autoformalization of entire research papers; addresses dependency tangles, statement drift, stale context; Munkres: 85,472 lines of Isabelle/HOL, 806 theorems, zero sorry's, fully automated in 24 days; VML: complete Lean 4 formalization of plasma equilibrium, $200, 10 days, zero human code
- **Date:** March–June 2026
- **Tier:** B (calibration anchor — formalization methodology)
- **CQE relevance:** CQE's NP-08 formalization backbone (P14, P23, P32, P44) now has proven templates for large-scale autoformalization. The Munkres result (85K lines, zero sorry's) demonstrates that complete textbook formalization is achievable. CQE should adopt the "sorry-first" workflow and dependency-graph management (Lean Atlas) for its own corpus.

### T-5. Quantum Computing Roadmaps 2026–2029 — IBM, Google, IonQ, Quantinuum
- **Reference:** "What quantum computer to buy?" (arXiv:2604.04761, April 2026); Quantum Logical Qubit Leaderboard (June 2026); company roadmaps
- **Key claims:** IBM: Heron R2 (156 qubits, 99.5% 2Q fidelity), Kookaburra qLDPC roadmap, 200 logical qubits by 2029; Google: Willow d=7 surface code, 1M physical qubits by 2029, 1000 logical qubits by 2030; IonQ: 99.99% fidelity, 1024 qubits by 2028; Quantinuum: Helios 48 LQ, 100+ LQ target 2027; QuEra: 96 LQ now, 200+ LQ expected; PsiQuantum: 1M photonic qubits by 2029
- **Date:** 2026
- **Tier:** B (calibration anchor — QEC competitive landscape)
- **CQE relevance:** The quantum computing landscape is now an engineering race with explicit roadmaps. CQE's Leech-lattice QEC claims must be benchmarked against these concrete targets. If CQE cannot specify when its QEC will achieve a comparable logical qubit count, it is not competitive. By 2029, multiple platforms target 200–1000 logical qubits.

---

## 2. External Unification Frameworks — Status Update

| Framework | Status | CQE Action |
|-----------|--------|------------|
| **FIRM** | Active — foundational inference | Compare inference procedures (P5) |
| **MNT** | Active — mirror nucleon theory | Validate phase transitions against MNT predictions (P5) |
| **SRC** | Active — strong reflection principle | Compare reflective closure axioms (P5) |
| **U₂₄** | Repositories private (GitHub takedown) | Content captured; comparison preserved (P25) |

---

## 3. Critical External Anchors — Round 21 Update

| Anchor | Paper | Current Status | Round 21 Update |
|--------|-------|---------------|-----------------|
| Higgs mass | 33, 49 | **P41 open** — derivation needed | **Run 3 improves Higgs→μμ, H→Zγ by 30–38%** |
| Higgs→charm coupling | 33 | **NEW** — Run 3 first sensitivity | **CQE must predict κ_c** |
| Di-Higgs production | 33 | **NEW** — bbγγ sensitivity now exceeds Run 2 combination | **CQE must predict κ_λ before HH observation** |
| Early SMBH seeds | 03, 05, 15 | **NEW** — JWST LRDs suggest PBH seeds | **CQE must address PBH mass spectrum or exclude** |
| Primordial black holes | 01, 03 | **NEW** — Carr 2026 review; f_PBH constraints | **CQE must predict f_PBH or state zero** |
| Collider neutrinos | 04, 13 | **NEW** — FASERν/SND@LHC 10K neutrinos by mid-2026 | **CQE must address or exclude collider ν scope** |
| Long-horizon autoformalization | 09, 10 | **P32, P44 open** | **LeanMarathon + Munkres provide templates** |
| QEC roadmaps 2026–2029 | 02, 11 | **P64, P76–P80 open** | **IBM/Google/IonQ/Quantinuum explicit targets** |

---

## 4. Draft Integration Paragraphs for CQE Papers

### Paragraph T-1 (for CQE Paper 15 / Cosmology — JWST Little Red Dots and PBH Seeds)

> **External calibration anchor:** JWST observations (2024–2026) reveal "little red dots" (LRDs) — supermassive black holes (10⁶–10⁹ M⊙) at z ~ 8–10 in metal-poor, unexpectedly small host galaxies with black hole-to-galaxy mass ratios ~10% (vs. 0.005% locally). Primordial black holes (PBHs) of 10³–10⁵ M⊙ are proposed as seeds. Carr et al. (2026) review PBH constraints; Dayal et al. (2024) and Zhang et al. (2026) model PBH seeding.
>
> **CQE integration:** CQE's cosmological framework (Paper 15, Paper 03) must address early-universe structure formation. If CQE's lattice substrate predicts primordial black holes, it must specify: (a) the PBH mass spectrum, (b) the fraction of dark matter in PBHs (f_PBH), and (c) the seed mass for SMBH formation. Current JWST observations favor massive seeds (≥10⁴ M⊙) and constrain f_PBH ≤ 10⁻² for M ≥ 10⁷ M⊙. **Required CQE prediction:** State the PBH mass spectrum from FLCR lattice fluctuations; predict f_PBH as a function of mass; identify whether CQE predicts LRD-type overmassive black holes at z ~ 10. If CQE predicts no PBHs, state f_PBH = 0 and explain why the lattice substrate does not produce black hole seeds. **Verification:** Compare against JWST LRD observations and Carr et al. (2026) review constraints. **Priority:** P81 (new Round 21 target).

### Paragraph T-2 (for CQE Paper 33 / Higgs Papers — LHC Run 3 Higgs→Charm and Di-Higgs)

> **External calibration anchor:** LHC Run 3 (2022–2026) has achieved major advances in Higgs precision: Higgs→μμ and H→Zγ uncertainties reduced by 30–38%; first sensitivity to Higgs→c-cbar (charm quark coupling) via ttH production; di-Higgs (HH) sensitivity in bbγγ final state now exceeds all Run 2 channels combined; signal strength μ = 1.01⁺⁰·⁰⁶₋₀.₀₅; Higgs invisible width BR < 11% at 95% CL (Gallinaro 2025, CMS/ATLAS 2025–2026).
>
> **CQE integration:** CQE's electroweak sector (Paper 33, Paper 49) must predict the complete set of Higgs couplings. Run 3 is now probing κ_c (charm quark) for the first time — this is a major SM test that CQE cannot ignore. The di-Higgs channel is the gateway to measuring the Higgs trilinear self-coupling κ_λ. If CQE predicts κ_λ = 1 (SM), it must do so before the HH observation, or the prediction becomes post-hoc. **Required CQE prediction:** Predict κ_c, κ_μ, κ_τ, κ_b, κ_t, κ_V, and κ_λ with uncertainty bounds. State the expected HH signal strength σ(pp→HH) / σ_SM. **Verification:** Compare against Run 3 measurements and HL-LHC projections. **Priority:** P41 (Higgs mass), P46 (κ_λ), P74 (HL-LHC calibration) — now MORE URGENT given Run 3 progress.

### Paragraph T-3 (for CQE Paper 13 / Neutrino Papers — FASERν/SND@LHC Collider Neutrinos)

> **External calibration anchor:** FASER and SND@LHC have observed the first collider neutrinos (2023), with ~10,000 neutrinos expected by end of Run 3 (mid-2026). Electron neutrino interactions observed; tau neutrino interactions imminent. These experiments test lepton universality, probe intrinsic charm and gluon saturation, and constrain light dark-sector particles (Annual Reviews 2026).
>
> **CQE integration:** CQE's neutrino predictions (P54–P55, P71) focus on oscillation experiments (JUNO, DUNE, Hyper-K). Collider neutrino physics provides a complementary probe: high-energy neutrino cross-sections at TeV energies, lepton universality tests, and dark-sector constraints. CQE should either: (a) extend its neutrino predictions to collider energies, or (b) explicitly scope-bound its neutrino claims to oscillation physics. **Required CQE action:** State whether CQE neutrino predictions apply to collider neutrino cross-sections. If yes, predict σ(νN) at TeV energies. If no, add a scope boundary statement. **Verification:** Compare against FASERν cross-section measurements. **Priority:** P54 (neutrino predictions) — extend scope or clarify boundary.

### Paragraph T-4 (for CQE NP-08 / Formalization — LeanMarathon & Munkres Autoformalization)

> **External calibration anchor:** LeanMarathon (arXiv:2606.05400, June 2026) — first systematic approach to long-horizon Lean 4 autoformalization of entire research papers, addressing dependency tangles, statement drift, and stale context. Munkres topology autoformalized in Isabelle/HOL: 85,472 lines, 806 theorems, zero sorry's, fully automated in 24 days (arXiv:2604.07455, April 2026). Vlasov-Maxwell-Landau equilibrium in Lean 4: complete plasma physics formalization, $200, 10 days, zero human code (arXiv:2603.15929, March 2026).
>
> **CQE integration:** CQE's formalization backbone (NP-08, P14, P23, P32, P44) now has proven templates for large-scale autoformalization. The Munkres result demonstrates that complete textbook formalization (85K lines, zero sorry's) is achievable with current AI tools. CQE should adopt: (a) the "sorry-first" workflow, (b) dependency-graph management (Lean Atlas), and (c) the generate-check-refine loop. **Required CQE action:** Produce a CQE_Corpus.lean specification building on PhysLean, targeting at least one complete CQE derivation (e.g., D4→E8 embedding) with zero sorry's. Use LeanMarathon methodology for long-horizon formalization. **Verification:** Submit to LeanDojo benchmark; verify zero sorry's. **Priority:** P32 (Goedel-Architect blueprint), P44 (Lean 4 stack) — now achievable with demonstrated methods.

### Paragraph T-5 (for CQE Paper 02 / QEC — Quantum Computing Roadmaps 2026–2029)

> **External calibration anchor:** IBM (Heron R2: 156 qubits, 99.5% fidelity; Kookaburra qLDPC; 200 logical qubits by 2029), Google (Willow d=7 surface code; 1M physical qubits by 2029; 1000 logical qubits by 2030), IonQ (99.99% fidelity; 1024 qubits by 2028), Quantinuum (Helios 48 LQ; 100+ LQ by 2027), QuEra (96 LQ now; 200+ LQ expected), PsiQuantum (1M photonic qubits by 2029) — arXiv:2604.04761 (April 2026), Quantum Logical Qubit Leaderboard (June 2026).
>
> **CQE integration:** The quantum computing industry has published explicit roadmaps to 200–1000 logical qubits by 2029–2030 across multiple platforms. CQE's Leech-lattice QEC must compete with these benchmarks or define a distinct niche. If CQE cannot specify: (a) expected logical qubit count by 2029, (b) encoding ratio, (c) physical platform, and (d) decoder latency, the QEC claims are not actionable. **Required CQE prediction:** State the Leech-lattice QEC roadmap: logical qubit count target, timeline, encoding ratio, physical platform, and decoder technology. If CQE does not target near-term hardware, state explicitly that it is a theoretical framework and identify the experimental milestone that would validate it. **Verification:** Compare against IBM/Google/IonQ/Quantinuum published roadmaps. **Priority:** P77–P80 (Round 20 targets) — now MORE URGENT given explicit industry roadmaps.

---

## 5. Gap-Closure Recommendations

| Priority | Action | Deadline | Owner | Round 21 Relevance |
|----------|--------|----------|-------|-------------------|
| **P81** | Predict primordial black hole mass spectrum and abundance from FLCR, or state f_PBH = 0 | 2026-08-01 | Cosmology lead | **NEW — JWST LRDs demand PBH prediction** |
| **P82** | Predict Higgs→charm coupling κ_c from FLCR | 2026-08-01 | HEP lead | **NEW — Run 3 first sensitivity** |
| **P83** | Predict di-Higgs signal strength from FLCR | 2026-08-01 | HEP lead | **NEW — bbγγ sensitivity now exceeds Run 2** |
| **P84** | Address collider neutrino scope in CQE neutrino predictions | 2026-08-01 | Neutrino lead | **NEW — FASERν 10K neutrinos by mid-2026** |
| **P85** | Adopt LeanMarathon/Munkres autoformalization workflow for CQE_Corpus.lean | 2026-08-15 | Formalization lead | **NEW — 85K lines, zero sorry's demonstrated** |
| P41 | Derive Higgs mass 125.11 ± 0.11 GeV from FLCR | 2026-07-15 | HEP lead | Ongoing — more urgent with Run 3 progress |
| P42 | Derive W-mass 80,360.2 MeV from FLCR | 2026-07-10 | HEP lead | Ongoing |
| P46 | Derive Higgs self-coupling κ_λ from FLCR | 2026-07-25 | HEP lead | Ongoing — di-Higgs channel opening |
| P48 | Remove all muon g−2 "anomaly" language | 2026-07-10 | HEP lead | MOST URGENT |
| P54 | Publish neutrino mass/hierarchy predictions before DUNE 2029 | 2028-06 | Neutrino lead | Time-critical — extend to collider ν? |
| P71 | Derive δ_CP from FLCR E8 discrete symmetry | 2027-12 | Neutrino lead | Round 19 target |
| P72 | Predict proton lifetime or state exact baryon-number conservation | 2026-08-01 | HEP lead | Round 19 target |
| P77 | Benchmark Leech-lattice QEC against QuEra 96-LQ result | 2026-08-01 | QEC lead | Round 20 target — more urgent with roadmaps |
| P78 | Predict dark energy equation of state w(z) before DESI 5σ | 2027-06 | Cosmology lead | Round 20 target |

---

## 6. New Falsifiability Tests (Round 21)

| Test | Experiment/Observation | CQE Prediction Required | If Falsified |
|------|----------------------|------------------------|-------------|
| JWST LRDs | JWST z ~ 10 SMBH observations | PBH seed mass spectrum | Early universe claim fails |
| Higgs→charm | LHC Run 3 ttH→cc̄ | κ_c value | Higgs coupling pattern claim fails |
| Di-Higgs | HL-LHC HH→bbγγ | κ_λ and σ(HH)/σ_SM | Self-coupling claim fails |
| Collider neutrinos | FASERν/SND@LHC | σ(νN) at TeV or scope boundary | Neutrino scope claim inconsistent |
| Autoformalization | LeanDojo/CQE_Corpus.lean | Zero sorry's for D4→E8 derivation | Formalization backbone claim fails |
| QEC roadmap | IBM/Google 2029 targets | Logical qubit count target | QEC competitiveness claim fails |

---

*Supplement T compiled: 2026-07-03*  
*Phase 1 (Cataloguing): ACTIVE — 185 papers, 98 domains*  
*Phase 2 (Derivation): ACTIVE — CQE formal forms generate predictions*
