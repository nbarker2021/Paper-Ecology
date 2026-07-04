# CQE/CMPLX External Literature Mapping — Round 10 Supplement

**Date:** 2026-07-03
**Papers catalogued:** 6
**Domains:** 4 (topological superconductivity, Majorana zero modes, quantum error correction advances, neutrino mass models)
**Draft integration paragraphs:** 2

---

## 1. New Papers (Round 10)

| # | Paper | Year | Domain | Tier | CQE Relevance |
|---|-------|------|--------|------|---------------|
| 109 | **Das Sarma, Pan, Nag 2026** — "Majorana zero modes in semiconductor-superconductor hybrid structures: Defining topology in short and disordered nanowires through Majorana splitting" (arXiv:2507.00128v3, revised 20 Apr 2026) | 2026 | Topological superconductivity | **A** | Majorana zero modes are non-Abelian anyons — directly relevant to NP-07 Leech-lattice QEC if CQE claims topological protection |
| 110 | **Zhang et al. 2025** — "Double Majorana vortex flat bands in the topological Dirac superconductor" (Nature Commun. Phys., 10 Dec 2025) | 2025 | Topological superconductivity | B | Iron-based superconductors as intrinsic topological platforms; vortex MZMs |
| 111 | **Kumar et al. 2026** — "Unveiling in-gap states and Majorana zero modes in bilayer topological insulator / superconductor heterostructures" (PRResearch, 2026) | 2026 | Topological superconductivity | B | Fu-Kane proposal realized in bilayer; experimental signatures |
| 112 | **Choi & Sim 2026** — "Emergence of multiple zero modes bound to vortices in extended topological Josephson junctions" (arXiv:2601.14808v3, revised 24 Jun 2026) | 2026 | Topological Josephson junctions | B | Multiple MZMs in extended junctions; braiding implications |
| 113 | **Jacoby et al. 2025** — "Magic-state injection with erasure qubits" (cited in Riverlane 2026 QEC review) | 2025 | Quantum error correction | **A** | Erasure qubits + magic state cultivation achieve fault-tolerant thresholds at physical erasure rates < 4×10⁻³; directly relevant to NP-07 QEC claims |
| 114 | **Devi & Devi 2025** — "An A₄-Symmetric Double Seesaw for Neutrino Masses and Mixing in Light of JUNO results" (arXiv:2512.24132, 30 Dec 2025) | 2025 | Neutrino physics / flavor symmetry | B | A₄ flavor symmetry + double seesaw predicts TBM structure; JUNO 2025 sin²θ₁₂ ≈ 0.31 constrains parameter space |

---

## 2. Majorana Zero Modes and Topological Quantum Computing (Papers 109–112)

### 2.1 Das Sarma et al. 2026 — Operational Definition of Topology in Majorana Nanowires

**Key finding:** The paper redefines the existence of true Majorana zero modes (MZMs) in realistic (finite, disordered) nanowires through the **exponential suppression of Majorana splitting**: E_split ∼ exp(−L/ξ). Without this exponential suppression, the modes are merely Andreev bound states (ABS) with some Majorana character, not true non-Abelian anyons.

**CQE relevance:** If NP-07 (Leech-lattice quantum error correction) or any CQE paper claims topological protection via Majorana modes or surface-code anyons, this paper provides the **operational definition** that must be satisfied: the energy splitting must decay exponentially with system size. Any CQE claim of topological protection must demonstrate this scaling explicitly.

**CQE action:**
- NP-07 must state whether the proposed Leech-lattice QEC uses **surface-code anyons**, **color-code anyons**, or **Majorana-based topological protection**
- If Majorana-based: demonstrate exponential splitting suppression or cite this operational definition
- If surface-code based: the threshold (~1%) is the relevant benchmark (see P4 / Willow 2025)

**Falsifiability:** If CQE claims topological protection but cannot demonstrate either (a) exponential MZM splitting suppression, or (b) surface-code threshold below ~1%, the claim is IBN/ECO.

### 2.2 Zhang et al. 2025 — Iron-Based Superconductors as Intrinsic Topological Platforms

**Key finding:** High-T_c iron-based superconductors (IBS) exhibit band inversion between p_z and d_xz/yz orbitals, creating an intrinsic topological band structure. Zero-bias peaks in vortex cores across multiple IBS provide evidence for vortex MZMs without requiring heterostructure engineering.

**CQE relevance:** IBS are a **single-material platform** for topological superconductivity, potentially simpler than TI/SC heterostures. If CQE's substrate claims involve emergent superconductivity or topological phases, IBS provide a concrete physical system where topology and superconductivity coexist intrinsically.

### 2.3 Choi & Sim 2026 — Multiple Zero Modes in Extended Josephson Junctions

**Key finding:** Extended topological Josephson junctions on 3D TI surfaces (Fu-Kane proposal) can host **multiple zero modes bound to vortices**, not just single MZMs. This opens pathways for more complex braiding operations.

**CQE relevance:** Multiple MZMs per vortex increase the computational power of topological qubits but also introduce **mode mixing** challenges. If CQE claims multi-qubit topological gates, the mode-counting and braiding statistics must be specified.

---

## 3. Quantum Error Correction — Erasure Qubits and Magic States (Paper 113)

### 3.1 Jacoby et al. 2025 / Riverlane 2026 — Erasure Qubit Thresholds

**Key finding:** Superconducting "erasure qubits" (heralded erasure errors) combined with magic-state cultivation can achieve fault-tolerant error rates with:
- Physical (heralded) erasure error rates < **4×10⁻³**
- Residual Pauli error rates ~ **10⁻⁴**

This is a **tipping point**: these rates are achievable with near-term hardware.

**CQE relevance:** NP-07's Leech-lattice QEC must benchmark against these numbers. The surface code threshold (~1%) and the erasure-qubit enhanced threshold (~0.4%) are the current experimental frontiers.

**Comparison table:**

| QEC Approach | Physical Error Rate Threshold | Logical Qubit Overhead | Status (2026) |
|-------------|------------------------------|----------------------|---------------|
| Surface code (Google Willow) | ~1% Pauli | ~1000:1 | Demonstrated below threshold |
| qLDPC (IBM bivariate bicycle) | ~0.5% Pauli | ~100:1 | Theoretical; hardware challenge |
| **Erasure qubits + cultivation** | **< 0.4% heralded erasure** | **~100:1** | **Near-term viable** |
| Leech lattice (CQE NP-07) | ??? | ??? | **Unspecified** |

**CQE action (P4 extension):** NP-07 must either:
1. Calculate the Leech-lattice QEC threshold and overhead, or
2. Explicitly state that the Leech lattice is a **conceptual substrate** (not a competitive QEC code), or
3. Demonstrate that the Leech lattice offers advantages over surface code / qLDPC / erasure codes

Without this, NP-07's hardware claims are IBN/ECO.

---

## 4. Neutrino Mass Models — A₄ Flavor Symmetry (Paper 114)

### 4.1 Devi & Devi 2025 — Double Seesaw with A₄ Symmetry

**Key finding:** An A₄-symmetric double seesaw mechanism (right-handed neutrinos + sterile gauge-singlets) yields:
- Leading-order tri-bimaximal mixing (TBM) structure
- Corrections from a single (1-3) rotation
- JUNO 2025 sin²θ₁₂ ≈ 0.31 strongly constrains the A₄ flavon couplings

**CQE relevance:** This is a **competing predictive framework** for neutrino masses and mixings that:
- Uses discrete flavor symmetry (A₄) rather than continuous Lie groups
- Is highly constrained by JUNO 2025 data
- Makes testable predictions for θ₁₂, θ₁₃, and the mass hierarchy

If CQE claims to predict neutrino mixing angles from the Leech lattice or E8 structure, it must match or exceed the predictive power of A₄ double seesaw models.

**Falsifiability:** A₄ models predict specific relations between mixing angles and mass ratios. If CQE's predictions for sin²θ₁₂, sin²θ₂₃, or Δm²₂₁ deviate from JUNO/DUNE measurements by >3σ, the CQE neutrino sector is falsified.

---

## 5. Draft Integration Paragraphs

### Paragraph 28 — Majorana Mode Operational Definition for NP-07

**Target:** NP-07 (Leech-lattice quantum error correction)
**Placement:** §3 (topological protection claims)

> The operational definition of a true Majorana zero mode in a realistic (finite, disordered) system requires the exponential suppression of Majorana energy splitting: E_split ∼ exp(−L/ξ), where L is the system length and ξ is the coherence length [Das Sarma et al., 2026, arXiv:2507.00128v3]. In the absence of this exponential suppression, bound states are merely Andreev bound states with partial Majorana character, not non-Abelian anyons. If the Leech-lattice substrate is claimed to host Majorana-based topological protection, it must demonstrate this exponential scaling. Alternatively, if the Leech lattice implements surface-code or color-code topological protection, the relevant benchmark is the fault-tolerance threshold (~1% for surface code, ~0.4% for erasure-qubit enhanced codes) [Jacoby et al., 2025; Riverlane, 2026]. Until these thresholds are calculated for the Leech-lattice code, the hardware feasibility claims remain [INSERT STATUS: conjectural / investigation only].

### Paragraph 29 — Neutrino Flavor Symmetry Competitor

**Target:** Paper 13 / NP-04 (neutrino mass predictions)
**Placement:** §5.4 (neutrino masses and mixings)

> Discrete flavor symmetries provide an alternative to continuous Lie-group derivations of neutrino mixing. The A₄-symmetric double seesaw model predicts tri-bimaximal mixing corrected by a single (1-3) rotation, with JUNO 2025 measurements of sin²θ₁₂ ≈ 0.31 strongly constraining the A₄ flavon coupling parameter space [Devi & Devi, 2025, arXiv:2512.24132]. If the FLCR framework predicts neutrino mixing angles from the Leech lattice or E8 structure, the predictions must be at least as constrained as the A₄ model: specific values for sin²θ₁₂, sin²θ₂₃, and the CP-violating phase δ_CP, with uncertainties comparable to JUNO/DUNE projected sensitivities. A failure to predict these angles within 3σ of experimental values would falsify the FLCR neutrino sector.

---

## 6. Updated Priority Actions (Round 10 Additions)

| Priority | Action | Owner | Deadline | Source |
|---|---|---|---|---|
| **P4-ext** | **Benchmark NP-07 against erasure-qubit thresholds**: State Leech-lattice threshold and overhead; compare to surface code (~1%), qLDPC (~0.5%), erasure qubits (~0.4%) | NP-07 Author | 2026-07-20 | This supplement §3.1 |
| **P28** | **Add Majorana operational definition to NP-07**: Cite Das Sarma 2026; specify whether Leech-lattice QEC uses surface-code, color-code, or Majorana protection; calculate or state threshold | NP-07 Author | 2026-07-15 | This supplement §2.1 |
| **P29** | **Benchmark FLCR neutrino predictions against A₄ models**: State sin²θ₁₂, sin²θ₂₃, δ_CP predictions; compare to JUNO 2025 and DUNE projected sensitivities | Paper 13/NP-04 Author | 2026-07-20 | This supplement §4.1 |

---

*Round 10 compiled: 2026-07-03*
*New papers: 6 (109–114)*
*New domains: 4*
*New paragraphs: 2 (28–29)*
*New priority actions: 3 (P4-ext, P28, P29)*
