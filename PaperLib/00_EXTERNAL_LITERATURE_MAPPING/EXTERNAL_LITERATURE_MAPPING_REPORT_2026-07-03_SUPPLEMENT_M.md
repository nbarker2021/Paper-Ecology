# CQE/CMPLX External Literature Mapping — Supplement M
## Round 14 | 2026-07-03

---

## 1. Scope

Supplement M catalogues **5 papers** discovered in the July 3 2026 sweep, focusing on:
- **Neutrino physics** (JUNO first θ₁₂ measurement, operational status)
- **Cosmology** (Radiative SIDM Dilution framework for NANOGrav excess)
- **Fundamental physics constraints** (Lorentz violation from PTA data)
- **Formal verification** (MerLean QEC formalization in Lean 4)

All papers were published or preprinted between **January–June 2026**.

---

## 2. Papers

### 2.1 JUNO First Measurement of θ₁₂

| Field | Value |
|-------|-------|
| **Title** | Modified tri-bimaximal neutrino mixing confronted by JUNO θ₁₂ measurement |
| **Authors** | Xiao-Gang He et al. |
| **Year** | 2026 |
| **Access** | Physics Letters B 874, 140270 (2026); arXiv:2511.15978 |
| **Tier** | **A** — direct calibration anchor for CQE neutrino predictions |
| **CQE paper(s)** | Paper 13 / NP-04 |
| **Domain** | Neutrino physics / flavor physics |

**What it says:**
The JUNO collaboration released its **first measurement of reactor neutrino oscillations**, obtaining:
- **sin²θ₁₂ = 0.3092 ± 0.0087**
- This is a **1.6× improvement in precision** over previous combined results
- The measurement constrains neutrino mixing models, excluding some modified tri-bimaximal patterns at >3.5σ
- Pattern (c) with V_e2 = cos(τ/3) agrees within 1σ, implying sin²θ₁₂ = (1−3sin²θ₁₃)/3(1−sin²θ₁₃) and sin δ_CP ∼ ±1
- Current data favor **sin δ_CP ≈ −1**, which requires **inverted hierarchy** in this model

**Why it matters for CQE:**
This is the **first physics result from JUNO** — the world's largest liquid scintillator detector, which started data-taking in August 2025. CQE Paper 13's neutrino predictions must calibrate to this measurement immediately. The precision of Δ(sin²θ₁₂) ≈ 0.009 sets the calibration target for any CQE-derived neutrino mixing formula.

**Gap-closure recommendation:**
CQE Paper 13 must:
1. State predicted values for sin²θ₁₂, sin²θ₁₃, and δ_CP
2. Compare to JUNO 2026 measurement: sin²θ₁₂ = 0.3092 ± 0.0087
3. If CQE predicts normal hierarchy, explain why the sin δ_CP ≈ −1 preference for inverted hierarchy does not falsify the model
4. If CQE predicts inverted hierarchy, cite this as supporting evidence

**Integration paragraph (copy-paste ready):**
> The JUNO reactor neutrino experiment has released its first physics measurement, obtaining sin²θ₁₂ = 0.3092 ± 0.0087 with a precision improved by a factor of 1.6 over previous combined results (He et al., Physics Letters B 874, 140270, 2026). This measurement provides the most precise determination of the solar mixing angle to date. CQE's neutrino sector predictions must be calibrated against this value. [INSERT CQE PREDICTION for sin²θ₁₂] should lie within the JUNO 1σ bound of [0.3005, 0.3179]. If CQE predicts a specific value for the CP-violating phase δ_CP, it must also address the emerging preference from global fits for sin δ_CP ≈ −1, which in some mixing models favors the inverted hierarchy.

---

### 2.2 JUNO Operational Status (Neutrino 2026)

| Field | Value |
|-------|-------|
| **Title** | Neutrino 2026: XXXII International Conference on Neutrino Physics and Astrophysics |
| **Authors** | JUNO Collaboration |
| **Year** | 2026 |
| **Access** | Conference proceedings, June 2026 |
| **Tier** | **B** — calibration anchor |
| **CQE paper(s)** | Paper 13 / NP-04 |
| **Domain** | Neutrino physics |

**What it says:**
JUNO started physics data-taking on **August 26, 2025**. The detector is the world's largest liquid scintillator with unprecedented energy resolution. First results on mass hierarchy are expected within the next 1–2 years. The experiment has 3σ+ sensitivity to mass hierarchy and 1% precision on solar parameters.

**Why it matters for CQE:**
JUNO is now a **live experiment** producing data. CQE can no longer treat neutrino hierarchy as a purely theoretical prediction — it must state a testable prediction before JUNO announces hierarchy determination (expected 2027–2028).

---

### 2.3 Radiative SIDM Dilution: NANOGrav Excess as Dark Sector Phase Transition

| Field | Value |
|-------|-------|
| **Title** | Diluting the Dark Sector: A Common Origin for the PTA Signal and Inelastic SIDM |
| **Authors** | Wang et al. |
| **Year** | 2026 |
| **Access** | arXiv:2601.04340 |
| **Tier** | **A** — direct competitor/alternative cosmological framework |
| **CQE paper(s)** | Paper 14 / NP-06 / Paper 100 |
| **Domain** | Cosmology / dark matter / gravitational waves |

**What it says:**
The observed NANOGrav nHz gravitational-wave background amplitude exceeds predictions from standard supermassive black hole binary populations. This paper proposes the **Radiative SIDM Dilution framework**:
- The PTA signal is a **hybrid**: astrophysical floor (suppressed by cored halos of self-interacting dark matter) + cosmological peak from a **supercooled phase transition in the dark sector**
- Transition parameters: T_* ≈ 1.24 MeV, β/H_* ≈ 150
- Statistical evidence: **ΔBIC ≈ 15** over purely astrophysical interpretations
- The entropy injection from the transition provides dilution factor D ≈ 100, resolving thermal overproduction of resonant SIDM
- Residual dark radiation alleviates Hubble tension: ΔN_eff ∼ 0.3
- Bubble collisions seed primordial magnetic fields B₀ ∼ 10⁻¹³ G

**Why it matters for CQE:**
This is a **competing cosmological framework** that uses the same observational data (NANOGrav PTA) that CQE must address. Unlike CQE's lattice-substrate approach, this model invokes:
- Dark sector phase transitions
- Self-interacting dark matter
- Entropy injection

CQE must either:
(a) Show that its lattice substrate naturally produces similar phenomenology, or
(b) Explicitly differentiate its GW predictions from this framework's predictions

**Gap-closure recommendation:**
Paper 14 should add a comparison section: "Alternative cosmological frameworks for the NANOGrav excess." Cite Radiative SIDM Dilution and state why CQE's lattice-substrate cosmogenesis predicts a different GW spectral shape or amplitude.

**Integration paragraph:**
> Multiple frameworks now compete to explain the NANOGrav nHz gravitational-wave background. The Radiative SIDM Dilution model (arXiv:2601.04340, 2026) proposes a hybrid signal from an astrophysical floor plus a cosmological peak generated by a supercooled dark-sector phase transition at T_* ≈ 1.24 MeV, with ΔBIC ≈ 15 over standard astrophysical interpretations. CQE's lattice-substrate cosmogenesis (Paper 14) must either reproduce similar phenomenology from first principles or explicitly predict a GW spectral shape distinguishable from the SIDM+Dilution model. The key discriminator is the spectral index and amplitude at frequencies probed by SKA-era PTA (2030s).

---

### 2.4 Lorentz Violation Constraints from PTA Data

| Field | Value |
|-------|-------|
| **Title** | Lorentz violation with gravitational waves: Constraints from NANOGrav and IPTA data |
| **Authors** | Abdalla et al. |
| **Year** | 2026 |
| **Access** | JHEAp 49, 100448 (2026); arXiv:2505.22736 |
| **Tier** | **B** — calibration anchor |
| **CQE paper(s)** | Paper 14 |
| **Domain** | Fundamental physics / GR modifications |

**What it says:**
The authors constrain Lorentz-violating modifications to GR using NANOGrav 15-year and IPTA DR2 data. In a framework with explicit Lorentz breaking via extrinsic curvature derivatives, the characteristic energy scale is bounded:
- **M_LV > 10⁻¹⁹ GeV at 68% CL** (assuming primordial GW origin)
- This significantly improves upon LIGO/Virgo binary merger constraints

**Why it matters for CQE:**
If CQE's "repair curvature" mechanism (Papers 33–35) modifies GR at any scale, it must be consistent with this bound. M_LV > 10⁻¹⁹ GeV ≈ 10⁻⁸ eV means any GR modification must be suppressed below this energy scale or apply only in specific regimes (e.g., lattice-scale physics far below this bound).

---

### 2.5 MerLean Formalization of Balanced Product Quantum Codes

| Field | Value |
|-------|-------|
| **Title** | Formalizing Balanced Product Quantum Codes with MerLean |
| **Authors** | MerLean team |
| **Year** | 2026 |
| **Access** | MerLean blog, March 2026; arXiv:2602.16554 |
| **Tier** | **A** — direct validation of CQE formalization strategy |
| **CQE paper(s)** | NP-08 / Paper 17 / Papers 29–32 |
| **Domain** | Formal verification / quantum error correction |

**What it says:**
MerLean has formalized the paper "Balanced Product Quantum Codes" in Lean 4, producing:
- **1,450 Lean declarations** from 48 original theorem statements
- Coverage: chain complexes, cohomology, CSS & LDPC codes, expander graphs, Cayley graphs, LPS construction
- MerLean-Prover achieves 12/12 on Putnam 2025 problems using recursive proof harness without fine-tuning
- FormalQualBench: 10/23 problems closed

**Why it matters for CQE:**
This proves that **quantum error correction can be formalized in Lean 4 at scale**. CQE's lattice code chain (D4→E8→Leech→Monster) is structurally similar to the balanced product code construction (chain complexes → code spaces). If MerLean can formalize 1,450 declarations for QEC, CQE's formalization target is achievable. The MerLean blog post (March 2026) explicitly describes their dual-engine architecture for handling mathematical physics formalization.

**Gap-closure recommendation:**
CQE should contact the MerLean team to explore collaboration on formalizing the D4→E8 embedding chain. The MerLean codebase already has the infrastructure for lattice-based code formalization.

---

## 3. Draft Integration Paragraphs (2 Total)

### §3.1 JUNO θ₁₂ as Calibration Target for CQE Neutrino Predictions

**Target:** Paper 13 / NP-04  
**Placement:** §5.4 (neutrino masses)  
**Source:** Supp M §2.1

The JUNO reactor neutrino experiment has released its first physics measurement, obtaining sin²θ₁₂ = 0.3092 ± 0.0087 with a precision improved by a factor of 1.6 over previous combined results (He et al., Physics Letters B 874, 140270, 2026). This measurement provides the most precise determination of the solar mixing angle to date. CQE's neutrino sector predictions must be calibrated against this value. [INSERT CQE PREDICTION for sin²θ₁₂] should lie within the JUNO 1σ bound of [0.3005, 0.3179]. If CQE predicts a specific value for the CP-violating phase δ_CP, it must also address the emerging preference from global fits for sin δ_CP ≈ −1, which in some mixing models favors the inverted hierarchy.

### §3.2 NANOGrav Excess: Competing Cosmological Frameworks

**Target:** Paper 14 / NP-06  
**Placement:** §5 (cosmological GW predictions)  
**Source:** Supp M §2.3

Multiple frameworks now compete to explain the NANOGrav nHz gravitational-wave background. The Radiative SIDM Dilution model (arXiv:2601.04340, 2026) proposes a hybrid signal from an astrophysical floor plus a cosmological peak generated by a supercooled dark-sector phase transition at T_* ≈ 1.24 MeV, with ΔBIC ≈ 15 over standard astrophysical interpretations. CQE's lattice-substrate cosmogenesis (Paper 14) must either reproduce similar phenomenology from first principles or explicitly predict a GW spectral shape distinguishable from the SIDM+Dilution model. The key discriminator is the spectral index and amplitude at frequencies probed by SKA-era PTA (2030s).

---

## 4. Priority Actions Added by This Round

| Priority | Action | Owner | Deadline | Dependencies | Source |
|---|---|---|---|---|---|
| **P37** | **Calibrate CQE neutrino predictions to JUNO θ₁₂**: State predicted sin²θ₁₂, sin²θ₁₃, δ_CP; compare to JUNO 2026 value 0.3092 ± 0.0087; address hierarchy preference | Paper 13/NP-04 Author | 2026-07-15 | Physics Letters B 874, 140270 (2026) | Supp M §2.1 |
| **P38** | **Differentiate CQE cosmology from Radiative SIDM Dilution**: State GW spectral prediction; explain why lattice substrate ≠ dark sector phase transition | Paper 14/NP-06 Author | 2026-07-20 | arXiv:2601.04340 | Supp M §2.3 |
| **P39** | **Check GR modification scale against Lorentz violation bound**: Ensure any CQE "repair curvature" mechanism satisfies M_LV > 10⁻¹⁹ GeV | Papers 33–35 Author | 2026-07-15 | JHEAp 49, 100448 (2026) | Supp M §2.4 |
| **P40** | **Contact MerLean team for QEC formalization collaboration**: Explore joint formalization of D4→E8 embedding chain | NP-08 Author | 2026-08-01 | MerLean blog, March 2026 | Supp M §2.5 |

---

*Supplement M compiled: 2026-07-03*  
*Papers: 5 | Domains: 4 | Paragraphs: 2 | New priority actions: 4*
