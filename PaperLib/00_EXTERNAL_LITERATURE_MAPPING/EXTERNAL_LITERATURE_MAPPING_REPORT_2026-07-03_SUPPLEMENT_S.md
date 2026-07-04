# CQE/CMPLX External Literature Mapping Report

## Supplement S — Round 20 | 2026-07-03

**New domains covered:** 5  
**New papers added:** 5  
**Cumulative totals:** 180 papers, 93 domains, 70 draft integration paragraphs, 81 priority actions

---

## 1. New External Papers Catalogued (Round 20)

### S-1. QuEra 96 Logical Qubits with [[16,6,4]] High-Rate Codes
- **Reference:** QuEra Computing / Harvard, *Nature* (January 2026)
- **Key claims:** 96 logical qubits from 448 physical atoms using [[16,6,4]] high-rate quantum error correction code; 4.7:1 encoding ratio; below-threshold error suppression demonstrated
- **Date:** 2026-01
- **Tier:** A (direct calibration anchor for QEC)
- **CQE relevance:** Directly challenges CQE's Leech-lattice QEC claims — QuEra achieves 96 logical qubits with dramatically lower overhead than surface codes. CQE must benchmark Leech-lattice overhead against QuEra's high-rate LDPC approach.

### S-2. DESI 2026: Evolving Dark Energy Strengthened to 2.8–4.2σ
cosmology
- **Reference:** DESI Collaboration, DESI DR2 results (June 2026); Percival et al., "DESI 2026: Evolving Dark Energy"
- **Key claims:** Combination of DESI BAO with CMB, weak lensing, and supernovae yields 2.8–4.2σ preference for evolving dark energy (w ≠ −1); not yet at 5σ discovery threshold; Occam's razor shifting toward dynamical dark energy
- **Date:** 2026-06
- **Tier:** A (direct cosmological calibration anchor)
- **CQE relevance:** CQE must predict dark energy equation of state w(z) before DESI reaches 5σ. If CQE predicts w = −1 (cosmological constant), it will be falsified if DESI confirms evolving dark energy.

### S-3. Atom Computing Toric Code with Sub-Threshold Scaling on Neutral Atoms
- **Reference:** Atom Computing, *Quantum Computing Report* (June 2026)
- **Key claims:** First sustained multi-round QEC on neutral-atom architecture; toric code with dynamic qubit rearrangement; distance-4 vs distance-6 codes show sub-threshold scaling; 90 successive stabilizer measurement rounds; continuous atom reloading
- **Date:** 2026-06
- **Tier:** A (direct QEC calibration anchor)
- **CQE relevance:** Competing paradigm to CQE Leech-lattice QEC. Atom Computing's neutral-atom approach with all-to-all connectivity and erasure-error mitigation is a viable alternative. CQE must demonstrate Leech-lattice advantages in overhead, latency, or logical error rate.

### S-4. Riverlane Real-Time Decoding 10× Faster than Google Surface Code
- **Reference:** Riverlane (April 2026)
- **Key claims:** Real-time quantum error correction decoding demonstrated 10× faster than Google's surface-code approach; addresses decoder latency bottleneck for feedback-based QEC
- **Date:** 2026-04
- **Tier:** B (calibration anchor — decoder technology)
- **CQE relevance:** Decoder latency is the critical bottleneck for fault-tolerant quantum computing. CQE's Leech-lattice codes require a decoder. If CQE cannot specify decoder architecture and latency, the QEC claims are incomplete.

### S-5. "A Busy Higgs Signal" — Higgs Phenomenology at Colliders
- **Reference:** Zhen Liu et al., arXiv:2604.14284 (April 2026)
- **Key claims:** Comprehensive Higgs phenomenology analysis; explores multi-Higgs production channels and their detectability at current and future colliders
- **Date:** 2026-04
- **Tier:** B (calibration anchor — Higgs physics)
- **CQE relevance:** Higgs phenomenology is central to CQE Papers 33 and 49. CQE must predict Higgs couplings, self-coupling κ_λ, and CP-violation parameters. This paper provides the experimental context for what signals are being searched for.

---

## 2. External Unification Frameworks — Status Update

| Framework | Status | CQE Action |
|-----------|--------|------------|
| **FIRM** | Active — foundational inference | Compare inference procedures (P5) |
| **MNT** | Active — mirror nucleon theory | Validate phase transitions against MNT predictions (P5) |
| **SRC** | Active — strong reflection principle | Compare reflective closure axioms (P5) |
| **U₂₄** | **Repositories now private** (GitHub org `OriginNeuralAI` takedown) | Content captured before takedown; comparison preserved for reference (P25) |

**Note:** U₂₄ repositories are now private. CQE has captured the content from before the takedown. The comparison in P25 remains valid as a reference document but cannot be updated from live sources.

---

## 3. Critical External Anchors — Round 20 Update

The following 24 external anchors are the most important for CQE verification:

| Anchor | Paper | Current Status | Round 20 Update |
|--------|-------|---------------|-----------------|
| Higgs mass | 33, 49 | **P41 open** — derivation needed | No new data |
| W mass | 33 | **P42 open** — derivation needed | No new data |
| α_EM at 0 energy | 01, 33 | **P27 open** — derivation needed | No new data |
| Quark masses | 14, 49 | **P28 open** — derivation needed | No new data |
| Proton lifetime | 15 | **P72 open** — Round 19 target | No new data |
| Dark energy equation of state | 03, 05 | **P51 open** — DESI 2026 now at 2.8–4.2σ | **DESI 2026 strengthens evolving DE hints** |
| Neutrino masses / hierarchy | 04, 49 | **P54 open** — time-critical | No new data |
| CKM matrix / CP violation | 14, 49 | **P71 open** — Round 19 target | No new data |
| Muon g−2 | 14 | **P48 CRITICAL** — update by 2026-07-10 | **Nature 2026 resolved anomaly; SM agrees** |
| Axion mass / coupling | 01 | **P15, P16 open** — scope and mass | No new data |
| Higgs self-coupling κ_λ | 33 | **P46 open** — derivation needed | No new data |
| Higgs CP violation | 33 | **P47 open** — prediction needed | No new data |
| Strong coupling α_s | 33 | P34 closed | — |
| QCD crossover T_c | 49 | **P56, P57 open** — QCD critical point | No new data |
| Reionization redshift | 05 | **P52 open** — JWST early galaxies | **JWST pushing reionization to z > 10** |
| CMB B-mode (r) | 05 | **P58, P59 open** — LiteBIRD/Simons | **Simons Observatory/CMB-S4 can distinguish models at 10.4σ** |
| GW stochastic background | 05 | P60 open | No new data |
| GR polarization / memory | 07 | P22 open — numerical relativity mapping | No new data |
| Spinor phase / Berry | 07, 08 | P30 open — derive phase from FLCR | No new data |
| Game complexity lower bounds | 08 | P31 open — formalize games in Lean | No new data |
| Energy landscape / NK model | 08 | P32 open — derive from FLCR | No new data |
| QEC threshold / overhead | 02, 11 | **P64 open** — ultra-high-rate QEC; **P76 open** — topological QEC benchmark | **QuEra 96 LQ at 4.7:1 ratio; Atom Computing toric code** |
| Agent verification | 09, 10 | P24 open — formal workflow spec | No new data |
| Lean 4 / PhysLean | 09, 10 | **P23, P44 open** — formalization stack | **PhysLean expanding; autoformalization advancing** |
| FCC-ee Higgs precision | 33 | **P61, P68 open** — long-horizon targets | No new data |

---

## 4. Draft Integration Paragraphs for CQE Papers

### Paragraph S-1 (for CQE Paper 02 / QEC papers — QuEra 96 Logical Qubits)

> **External calibration anchor:** QuEra Computing / Harvard, *Nature* (January 2026) — 96 logical qubits from 448 physical atoms using [[16,6,4]] high-rate codes, achieving a 4.7:1 encoding ratio with below-threshold error suppression.
>
> **CQE integration:** CQE's Leech-lattice quantum error correction must demonstrate comparable or superior performance metrics. The QuEra result establishes a benchmark: 96 logical qubits with ~4.7 physical qubits per logical qubit. If CQE's 24-dimensional Leech lattice cannot achieve an encoding ratio competitive with QuEra's [[16,6,4]] LDPC code, the overhead argument fails. **Required CQE prediction:** State the expected encoding ratio, logical error rate, and decoder latency for Leech-lattice QEC. If CQE predicts an encoding ratio > 10:1, it is not competitive with 2026 state-of-the-art. **Verification:** Compare CQE overhead prediction against QuEra's published 4.7:1 ratio. **Priority:** P64 (ultra-high-rate QEC benchmark) and P76 (topological QEC benchmark).

### Paragraph S-2 (for CQE Paper 03 / Cosmology — DESI 2026 Evolving Dark Energy)

> **External calibration anchor:** DESI Collaboration, DESI DR2 results (June 2026) — combination of DESI BAO with CMB, weak lensing, and supernovae yields 2.8–4.2σ preference for evolving dark energy (w ≠ −1), not yet at 5σ discovery threshold.
>
> **CQE integration:** CQE's cosmological framework must predict the dark energy equation of state w(z) before DESI reaches 5σ significance (expected by 2028-2029 with full 5-year data). If CQE predicts w = −1 (cosmological constant, ΛCDM), it risks falsification if DESI confirms evolving dark energy. If CQE predicts w(z) ≠ −1, it must specify the functional form and redshift evolution. **Required CQE prediction:** State w₀ and w_a (CPL parameterization) or equivalent, with uncertainty bounds. If CQE predicts dynamical dark energy, the prediction must pre-date the 5σ confirmation to count as a true prediction. **Verification:** Compare CQE w(z) prediction against DESI 2028-2029 final results. **Priority:** P51 (DESI BAO calibration) — NOW TIME-CRITICAL.

### Paragraph S-3 (for CQE Paper 02 / QEC papers — Atom Computing Toric Code)

> **External calibration anchor:** Atom Computing (June 2026) — first sustained multi-round QEC on neutral-atom architecture using toric code with dynamic qubit rearrangement; sub-threshold scaling verified over 90 stabilizer rounds; continuous atom reloading for erasure-error mitigation.
>
> **CQE integration:** Atom Computing's neutral-atom approach with all-to-all connectivity and erasure-error mitigation represents a competing fault-tolerance paradigm to CQE's Leech-lattice approach. CQE must demonstrate that Leech-lattice codes offer advantages in: (a) encoding ratio, (b) logical error rate, (c) decoder latency, or (d) physical hardware requirements. If CQE cannot specify these metrics, the QEC claims remain ungrounded. **Required CQE prediction:** State the expected physical platform (neutral atom, superconducting, trapped ion, or other) for Leech-lattice QEC implementation; specify encoding ratio, logical error rate per round, and decoder latency. **Verification:** Benchmark against Atom Computing's published toric code metrics. **Priority:** P76 (topological QEC benchmark).

### Paragraph S-4 (for CQE Paper 02 / QEC papers — Riverlane Real-Time Decoding)

> **External calibration anchor:** Riverlane (April 2026) — real-time QEC decoding demonstrated 10× faster than Google's surface-code approach, addressing the decoder latency bottleneck.
>
> **CQE integration:** Decoder latency, not throughput, is the critical bottleneck for feedback-based fault-tolerant quantum computing. CQE's Leech-lattice QEC requires a decoder architecture. If CQE cannot specify decoder technology (software, FPGA, ASIC), latency bounds, and syndrome processing rate, the QEC claims are incomplete. **Required CQE prediction:** Specify decoder architecture, expected latency (μs per syndrome round), and throughput (syndromes/second). **Verification:** Compare against Riverlane's published decoder latency and Google's surface-code baseline. **Priority:** P64 (ultra-high-rate QEC benchmark).

### Paragraph S-5 (for CQE Paper 33 / Higgs papers — "A Busy Higgs Signal")

> **External calibration anchor:** Zhen Liu et al., arXiv:2604.14284 (April 2026) — comprehensive Higgs phenomenology analysis exploring multi-Higgs production channels at current and future colliders.
>
> **CQE integration:** Higgs phenomenology is central to CQE's electroweak sector (Paper 33) and mass hierarchy framework (Paper 49). CQE must predict not only the Higgs mass (125.11 GeV, P41) and self-coupling (κ_λ, P46), but also the full set of Higgs couplings to fermions and gauge bosons, and CP-violation parameters (c_H~W, P47). This paper provides the experimental context for what signals HL-LHC and FCC-ee will search for. **Required CQE prediction:** Provide complete Higgs coupling predictions (κ_V, κ_f, κ_λ, c_H~W) with uncertainty bounds compatible with HL-LHC and FCC-ee precision targets. **Verification:** Compare against ATLAS/CMS combined measurements and FCC-ee projections. **Priority:** P41 (Higgs mass), P46 (κ_λ), P47 (CP), P74 (HL-LHC/FCC-ee calibration).

---

## 5. Gap-Closure Recommendations

| Priority | Action | Deadline | Owner | Round 20 Relevance |
|----------|--------|----------|-------|-------------------|
| **P77** | Benchmark Leech-lattice QEC against QuEra 96-LQ result | 2026-08-01 | QEC lead | **NEW — QuEra sets 96-LQ benchmark** |
| **P78** | Predict dark energy equation of state w(z) before DESI 5σ | 2027-06 | Cosmology lead | **NEW — DESI at 2.8–4.2σ, approaching discovery** |
| **P79** | Specify decoder architecture and latency for Leech-lattice QEC | 2026-08-01 | QEC lead | **NEW — decoder is critical bottleneck** |
| **P80** | State physical platform for Leech-lattice QEC implementation | 2026-08-01 | QEC lead | **NEW — Atom Computing shows neutral-atom viability** |
| P41 | Derive Higgs mass 125.11 ± 0.11 GeV from FLCR | 2026-07-15 | HEP lead | Ongoing |
| P42 | Derive W-mass 80,360.2 MeV from FLCR | 2026-07-15 | HEP lead | Ongoing |
| P46 | Derive Higgs self-coupling κ_λ from FLCR | 2026-07-15 | HEP lead | Ongoing |
| P47 | Predict Higgs CP-violation parameter c_H~W = 0 | 2026-07-15 | HEP lead | Ongoing |
| P48 | **CRITICAL: Remove all muon g−2 "anomaly" language** | 2026-07-10 | HEP lead | MOST URGENT |
| P54 | Publish neutrino mass/hierarchy predictions before DUNE 2029 | 2028-06 | Neutrino lead | Time-critical |
| P56–P57 | Predict QCD crossover temperature and critical point | 2026-08-01 | QCD lead | Ongoing |
| P71 | Derive δ_CP from FLCR E8 discrete symmetry | 2027-12 | Neutrino lead | Round 19 target |
| P72 | Predict proton lifetime or state exact baryon-number conservation | 2026-08-01 | HEP lead | Round 19 target |
| P73 | Publish complete flavor observable predictions | 2026-08-01 | Flavor lead | Round 19 target |
| P74 | Calibrate Higgs predictions to HL-LHC and FCC-ee targets | 2028-12 | HEP lead | Round 19 target |
| P75 | State SUSY prediction explicitly (masses or "no SUSY") | 2026-08-01 | HEP lead | Round 19 target |
| P76 | Benchmark Leech-lattice QEC against topological qubit paradigm | 2026-08-01 | QEC lead | Round 19 target |

---

## 6. New Falsifiability Tests (Round 20)

| Test | Experiment/Observation | CQE Prediction Required | If Falsified |
|------|----------------------|------------------------|-------------|
| QuEra benchmark | QuEra 96 LQ at 4.7:1 ratio | Leech-lattice encoding ratio < 5:1 | QEC overhead claim fails |
| DESI evolving DE | DESI 5-year data (2028-2029) | w(z) functional form | Cosmological constant claim fails |
| Atom Computing neutral-atom QEC | Atom Computing toric code | Leech-lattice on specified platform | Platform viability claim fails |
| Decoder latency | Riverlane real-time decoding | Latency < 1μs per round | Fault-tolerance claim fails |

---

*Supplement S compiled: 2026-07-03*  
*Phase 1 (Cataloguing): ACTIVE — 180 papers, 93 domains*  
*Phase 2 (Derivation): ACTIVE — CQE formal forms generate predictions*
