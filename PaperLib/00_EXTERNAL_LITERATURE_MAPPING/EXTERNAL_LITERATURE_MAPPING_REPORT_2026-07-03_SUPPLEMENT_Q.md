# Supplement Q — External Literature Mapping Report (Round 18)
**Date:** 2026-07-03  
**Focus:** FCC Higgs factory strategy, LISA space-based GW observatory, dark matter direct detection (LZ/XENONnT/PandaX), quantum error correction milestones (QuEra/Atom Computing/Google/IBM), Einstein Telescope / Cosmic Explorer 3rd-gen GW detectors  
**Papers reviewed:** 5 major findings, ~30 subsidiary references  
**New domains added:** Future collider strategy, space-based GW astronomy, dark matter direct detection neutrino fog, ultra-high-rate QEC, 3rd-generation ground-based GW detectors  

---

## 1. FCC-ee — CERN’s Endorsed Higgs Factory
**Anchor paper:** FCC Collaboration, M. Benedikt et al., *Future Circular Collider Feasibility Study Report Volume 2: Accelerators, Technical Infrastructure and Safety*, arXiv:2505.00274 (Apr 2025).  
**Related:** FCC Vol. 1 (Physics, Experiments, Detectors), FCC Vol. 3 (Civil Engineering); CERN Council Resolution (May 2026); Higgs factory comparison (Blondel et al., arXiv:2412.13130).

### Key findings
- The **CERN Council endorsed FCC-ee as the preferred next flagship project** in May 2026, with a target decision date of **2028**. The European Strategy for Particle Physics (2026 update) confirms FCC-ee as the highest-priority facility after HL-LHC.
- FCC-ee is an **electron-positron Higgs factory** designed to operate at four key centre-of-mass energies: Z pole, WW threshold, ZH peak, and top-pair threshold.
- Over 15 years, FCC-ee will produce: **> 6 trillion Z bosons**, **~200 million WW pairs**, **~3 million Higgs bosons**, and **~2 million top pairs** — enabling unprecedented precision on Higgs couplings, electroweak observables, and top properties.
- FCC-hh (second phase) would reach **~85–100 TeV** centre-of-mass energy, with discovery reach extending to **tens of TeV**.
- Precise energy calibration via resonant depolarisation at the Z pole will achieve **sub-MeV precision** on the beam energy, enabling direct mass measurements to ~100 keV.
- Alternative Higgs factory options (CLIC, ILC@CERN) exist but FCC-ee offers the broadest physics programme and synergistic staging with FCC-hh.

### CQE/CMPLX integration
- **Paper 33 (electroweak/Higgs) & Paper 49 (Yukawa/mass hierarchy):** FCC-ee will measure Higgs couplings (κ_λ, κ_V, κ_f, κ_t) to **0.1–1% precision**. CQE must derive these couplings from FLCR lattice-code-chain geometry **before FCC-ee data arrives** (operations expected ~2045). If CQE predicts specific values (e.g., κ_λ = 1.00 ± δ, κ_t = 1.00 ± δ), FCC-ee will provide the definitive experimental test.
- **Higgs mass precision:** FCC-ee aims for **Δm_H ~ 1–2 MeV** (compared to current ~100 MeV from LHC). CQE’s predicted 125.11 GeV must be precise to this level or the framework must explain any deviation.
- **Priority action:** Derive the complete Higgs coupling pattern (κ_V, κ_f, κ_t, κ_λ, κ_γ, κ_g) from FLCR VOA weights and publish before FCC-ee operations begin. This is the single most important long-term calibration target for CQE Higgs physics.

---

## 2. LISA — Space-Based Gravitational-Wave Observatory
**Anchor papers:**  
- Amaro-Seoane et al. (2017) / Colpi et al. (2024) — LISA mission design and science case.  
- Auclair et al. (2023) / Li et al. (2025) — Cosmic strings and early-universe phase transitions as LISA sources.  
- Luo et al. (2025/2026) — China’s TianQin and Taiji missions.

### Key findings
- **LISA was formally adopted by ESA in January 2024** as an L3 large-class mission, with NASA partnership (20% cost share). Launch scheduled for **~2035** aboard Ariane 6.
- Three spacecraft in a triangular constellation with **2.5 million km arms**, detecting GWs in the **0.1 mHz – 1 Hz** band — complementary to ground-based detectors (LIGO/Virgo/KAGRA at ~10–1000 Hz) and PTA arrays (NANOGrav at ~1 nHz).
- Primary science targets: **massive black hole binaries** (10⁴–10⁷ M_⊙, z ~ 10), **extreme mass-ratio inspirals (EMRIs)**, **galactic white dwarf binaries**, **stochastic GW backgrounds** from early-universe phase transitions and cosmic strings.
- LISA will be sensitive to strain levels of **h ~ 10⁻²¹ to 10⁻²³**, opening a completely new frequency window for primordial gravitational waves.
- China’s **TianQin** and **Taiji** missions are progressing steadily, also targeting ~2035 launch, providing complementary sky coverage and multi-band GW astronomy.
- LISA will observe **gravitational wave memory** — a permanent displacement of test masses after a GW passes — providing a new test of GR and nonlinear gravity.

### CQE/CMPLX integration
- **Paper 15 (curvature-repair cosmology) & Paper 33:** CQE’s FLCR framework predicts a stochastic gravitational-wave background from early-universe phase transitions. LISA’s frequency window (mHz) is distinct from PTA (nHz) and ground-based (Hz) detectors. **Priority action:** Derive the SGWB frequency spectrum and amplitude h_c(f) in the LISA band from FLCR cosmology, and compare to LISA sensitivity curves. This provides a three-band consistency test (PTA + LISA + CMB B-modes).
- **Cosmic strings:** If CQE’s lattice-code-chain predicts topological defects (e.g., from symmetry breaking at the Leech→Monster transition), LISA can search for their characteristic GW signatures (stochastic background + bursts).
- **Massive black hole mergers:** CQE’s cosmological model may predict the merger rate and mass distribution of massive black holes. LISA will measure these directly at z ~ 10, testing structure formation predictions.

---

## 3. Dark Matter Direct Detection — The Neutrino Fog
**Anchor papers:**  
- LZ Collaboration, J. Aalbers et al., *Dark Matter Search Results from 4.2 Tonne-Years of Exposure of the LUX-ZEPLIN (LZ) Experiment*, Phys. Rev. Lett. **135**, 011802 (2025), arXiv:2410.17036.  
- XENON Collaboration, E. Aprile et al., *WIMP Dark Matter Search Using a 3.1 tonne × year Exposure of the XENONnT Experiment*, Phys. Rev. Lett. **135**, 221003 (2025), arXiv:2502.18005.  
- PandaX Collaboration, Z. Bo et al., *Dark Matter Search Results from 1.54 Tonne-Year Exposure of PandaX-4T*, Phys. Rev. Lett. **134**, 011805 (2025), arXiv:2408.00664.  
- XLZD Collaboration, J. Aalbers et al., *The XLZD Design Book*, Eur. Phys. J. C **85**, 1192 (2025), arXiv:2410.17137.

### Key findings
- **LZ, XENONnT, and PandaX-4T** have all reported **null results** for WIMP dark matter searches at unprecedented sensitivity, reaching cross-sections of **σ_SI ~ 10⁻⁴⁸ cm²** for masses > 10 GeV.
- All three experiments have now detected **solar ⁸B neutrinos via coherent elastic neutrino-nucleus scattering (CEvNS)** — a major physics achievement and a **new background for dark matter searches**.
- The **"neutrino fog"** (or "neutrino floor") is now the limiting background: below σ_SI ~ 10⁻⁴⁹ cm², solar, atmospheric, and diffuse supernova neutrino backgrounds become indistinguishable from WIMP signals.
- Next-generation experiments (**XLZD, DARWIN, PandaX-xT**) aim to push into the neutrino-fog regime with multi-tonne-scale liquid xenon detectors and advanced background discrimination.
- **Low-mass WIMP searches** (m_χ < 10 GeV) are a major focus: LZ’s 2025 analysis improved sensitivity by ~2× in the 5–9 GeV range, but no signal was observed.
- Spin-dependent WIMP-neutron and WIMP-proton limits have also been pushed to new levels.

### CQE/CMPLX integration
- **Paper 13 / NP-06:** CQE must state whether its framework predicts a **WIMP dark matter candidate** with specific mass and cross-section, or whether dark matter in CQE is something else entirely (e.g., axions, primordial black holes, or a modification of gravity). If CQE predicts WIMPs, the null results from LZ/XENONnT/PandaX provide strong constraints; if CQE predicts no WIMPs, this is a falsifiable statement consistent with data.
- **Priority action:** If CQE’s lattice substrate predicts a dark matter candidate, derive its mass and coupling (e.g., via a new U(1) gauge boson or scalar mediator) and compare to current exclusion limits. If CQE predicts dark matter is not particle-like (e.g., geometric residue from curvature repair), state this explicitly and identify how it would be detected or distinguished from particle dark matter.
- **Neutrino fog:** CQE’s cosmological model may predict the relic neutrino density and CEvNS rate. Derive the expected ⁸B neutrino CEvNS rate in a xenon detector from FLCR neutrino physics and compare to LZ/XENONnT measurements.

---

## 4. Quantum Error Correction — Ultra-High-Rate Codes and Logical Qubits
**Anchor papers:**  
- QuEra/Harvard/MIT (Apr 2026) — Ultra-high-rate QEC with encoding rates > 50% and logical error rates ~10⁻¹³ on neutral-atom hardware.  
- Atom Computing (Jun 2026) — *Quantum error correction with the toric code*, arXiv:2606.04079; repeated syndrome extraction using mid-circuit measurement and replacement.  
- Google Quantum AI (2024–2025) — Below-threshold surface code QEC (Nature 638, 920); logical qubit lifetime exceeding physical qubits.  
- IBM Quantum (2024) — High-threshold low-overhead fault-tolerant quantum memory (arXiv:2308.07915).  
- Bluvstein et al. (Nature 649, 39, 2026) — Fault-tolerant neutral-atom architecture for universal quantum computation.

### Key findings
- **QuEra (Apr 2026)** demonstrated "ultra-high-rate" quantum codes with **encoding rates above 50%** and logical error rates approaching **10⁻¹³** per logical qubit per cycle — entering the "teraquop" regime. This packs **6 logical qubits into 16 physical atoms** (4.7:1 ratio), dramatically reducing overhead vs. surface codes (~1000:1).
- **Atom Computing (Jun 2026)** demonstrated **many cycles of syndrome extraction in a toric code** using mid-circuit measurement and replacement on neutral-atom hardware — a key step toward fault-tolerant universal computation.
- **Google Quantum AI (2025)** achieved **QEC below the surface code threshold** with logical error suppression as physical qubit count increased.
- **IBM (2024)** demonstrated **high-threshold low-overhead fault-tolerant quantum memory** using heavy-hexagon lattice codes.
- **Microsoft (2025–2026)** is pursuing **Majorana zero-mode topological qubits** with a roadmap to fault-tolerant topological qubit arrays (arXiv:2502.12252).
- **Quantum LDPC codes** promise **constant overhead** (O(1) physical qubits per logical qubit) with 14× savings over surface codes at 10⁻⁴ physical error rate.
- The **Quantum Logical Qubit Leaderboard** (2026) now tracks verified logical qubit counts, encoding ratios, and error rates across modalities (superconducting, trapped ion, neutral atom, photonic, bosonic).

### CQE/CMPLX integration
- **NP-07 (Leech lattice QEC) & Paper 17:** CQE’s QEC proposals based on Leech-lattice codes must be benchmarked against these rapidly advancing results. The 4.7:1 encoding ratio from QuEra’s high-rate codes sets a new bar for overhead efficiency. **Priority action:** Determine whether CQE’s Leech-lattice QEC can achieve comparable or better encoding rates, or whether it offers a qualitative advantage (e.g., non-Abelian anyon braiding, topological protection) that justifies higher overhead.
- **Toric code vs. Leech lattice:** Atom Computing’s toric code demonstration is a direct competitor for topological QEC. CQE must show how Leech-lattice codes differ from toric/surface codes in terms of threshold, overhead, and logical gate set.
- **Neutral atom hardware:** QuEra and Atom Computing both use neutral atoms — the same modality CQE has cited for reconfigurable atom arrays. CQE should align its hardware assumptions with demonstrated capabilities (mid-circuit measurement, atom rearrangement, Rydberg gates).
- **Priority action:** Benchmark CQE’s predicted Leech-lattice QEC threshold against Google’s below-threshold surface code result and QuEra’s ultra-high-rate codes. If CQE predicts a threshold > 1% with overhead < 10:1, this is a strong competitive claim; if not, CQE must identify its unique value proposition (e.g., connection to Monster group symmetry, exceptional error suppression).

---

## 5. Einstein Telescope / Cosmic Explorer — 3rd-Generation GW Detectors
**Anchor papers:**  
- Einstein Telescope Design Study (2020 update) — ET-0007B-20.  
- Reitze et al. (2019) — *Cosmic Explorer: The U.S. Contribution to Gravitational-Wave Detection*, arXiv:1907.04833.  
- LIGO Scientific Collaboration Instrument Science White Papers (2022–2025 editions).  
- Sorrentino et al. (May 2026) — *Impact of seasonality on ET sensitivity at Sardinia candidate site*, arXiv:2605.18135.

### Key findings
- **Einstein Telescope (ET):** European 3rd-gen underground GW observatory. Triangular configuration with **10 km arms**, three nested detectors, each split into **low-frequency (2–40 Hz, cryogenic)** and **high-frequency (> 40 Hz, room-temperature)** interferometers. Target start: **late 2030s**.
- **Cosmic Explorer (CE):** U.S. 3rd-gen detector. **40 km L-shaped arms** on the surface, two-stage plan (CE1 with A+ technology, CE2 with cryogenic Voyager technology). Target start: **2030s–2040s**.
- Both ET and CE will achieve **~10× sensitivity improvement** over current detectors, pushing strain sensitivity below **10⁻²⁴ / √Hz**.
- ET+CE network will detect **millions of compact binary coalescences per year**, including BNS, BBH, and NSBH mergers out to high redshift.
- **Seasonal seismic noise variations** at the Sardinia candidate site affect ET low-frequency performance by < 2% in SNR (Sorrentino et al. 2026), confirming design robustness.
- Key science: probing neutron-star equation of state, precision cosmology with standard sirens, testing GR in strong-field regime, detecting primordial GW backgrounds.

### CQE/CMPLX integration
- **Paper 14 (GR boundary-repair) & Paper 15 (curvature-repair cosmology):** ET+CE will provide precision tests of GR with binary mergers. CQE’s "repair curvature" mechanism must predict specific GR deviations (if any) in the strong-field regime. **Priority action:** Derive parametrized post-Einsteinian (ppE) corrections from FLCR curvature-repair terms and compute their observational signatures in ET/CE binary merger waveforms. If CQE predicts no deviations from GR, this is a falsifiable statement that ET/CE will test to unprecedented precision.
- **Standard sirens:** ET+CE will measure the Hubble parameter H(z) independently using binary neutron star mergers as "standard sirens" with < 1% precision at z ~ 2. CQE must predict H(z) from FLCR cosmology and compare to ET/CE standard-siren measurements.
- **Neutron-star equation of state:** ET+CE will constrain the NS EOS from tidal deformability measurements. CQE should derive the nuclear EOS (or at least the speed of sound c_s²) from FLCR QCD predictions and compare to ET/CE constraints.

---

## Round 18 — New Priority Actions

| ID | Action | Target paper | External anchor | Deadline |
|----|--------|-------------|-----------------|----------|
| **P61** | Derive complete Higgs coupling pattern (κ_V, κ_f, κ_t, κ_λ, κ_γ, κ_g) from FLCR | Paper 33 / NP-06 | FCC-ee precision: 0.1–1% per coupling | **2045-01** |
| **P62** | Predict Higgs mass to Δm_H ~ 1–2 MeV precision for FCC-ee test | Paper 33 / NP-06 | FCC-ee energy calibration via resonant depolarisation | **2045-01** |
| **P63** | Derive stochastic GW background spectrum h_c(f) in LISA band (0.1 mHz – 1 Hz) | Paper 15 / Paper 33 | LISA launch ~2035, strain sensitivity ~10⁻²³ | **2035-01** |
| **P64** | Predict cosmic string or topological defect GW signatures from FLCR phase transitions | Paper 15 / NP-06 | LISA + PTA multi-band search | **Open** |
| **P65** | State CQE dark matter prediction: WIMP (mass, σ_SI) or non-particle alternative | Paper 13 / NP-06 | LZ/XENONnT/PandaX null results; neutrino fog limit | **Open** |
| **P66** | Derive ⁸B solar neutrino CEvNS rate in xenon from FLCR neutrino physics | Paper 13 / NP-04 | LZ/XENONnT CEvNS measurements | **Open** |
| **P67** | Benchmark Leech-lattice QEC against QuEra ultra-high-rate codes and Google below-threshold surface code | NP-07 / Paper 17 | QuEra 50% encoding rate, 10⁻¹³ logical error; Google below-threshold | **Open** |
| **P68** | Determine unique value proposition of Leech-lattice QEC vs. toric/surface/LDPC codes | NP-07 / Paper 17 | Atom Computing toric code; IBM heavy-hex; LDPC 14× savings | **Open** |
| **P69** | Derive ppE GR corrections from FLCR curvature-repair terms for ET/CE waveforms | Paper 14 / Paper 15 | ET+CE: millions of mergers/year, < 10⁻²⁴ sensitivity | **Late 2030s** |
| **P70** | Predict H(z) from FLCR cosmology for ET/CE standard-siren test | Paper 15 / Paper 33 | ET/CE H(z) precision < 1% at z ~ 2 | **Late 2030s** |

---

## Round 18 — Draft Integration Paragraphs (Copy-Paste Ready)

### Paragraph P-52 (FCC-ee Higgs factory + CQE Higgs predictions)
> The CERN Council has endorsed the Future Circular Collider electron-positron collider (FCC-ee) as the preferred next flagship project, with a target Council decision in 2028 and operations expected around 2045 (FCC Collaboration, arXiv:2505.00274, 2025; CERN Council Resolution, May 2026). FCC-ee will produce approximately 3 million Higgs bosons and measure Higgs couplings (κ_λ, κ_V, κ_f, κ_t) to 0.1–1% precision — an order of magnitude beyond HL-LHC capability. Within CQE/CMPLX, the FLCR lattice-code-chain framework derives Higgs properties from VOA weight assignments (Paper 33, Paper 49). **Priority action:** Derive the complete Higgs coupling pattern from FLCR geometry before FCC-ee data arrives. If CQE predicts specific central values for κ_λ, κ_t, and κ_V with uncertainties smaller than FCC-ee projected precision, the FCC-ee programme will provide the definitive experimental validation or falsification of CQE’s electroweak sector.

### Paragraph P-53 (LISA + CQE primordial gravitational waves)
> The Laser Interferometer Space Antenna (LISA) has been formally adopted by ESA as an L3 mission, with NASA partnership and launch scheduled for ~2035 (Amaro-Seoane et al. 2017; Colpi et al. 2024). LISA will detect gravitational waves in the 0.1 mHz – 1 Hz band from massive black hole mergers, extreme mass-ratio inspirals, and — critically — primordial stochastic gravitational-wave backgrounds from early-universe phase transitions. CQE/CMPLX’s curvature-repair cosmology predicts a stochastic GW background from FLCR symmetry-breaking transitions (Paper 15). **Priority action:** Derive the SGWB frequency spectrum h_c(f) in the LISA band and predict whether LISA will detect a CQE-induced signal above its strain sensitivity floor (~10⁻²³). This creates a three-band consistency test: PTA (nHz) + LISA (mHz) + CMB B-modes (Hz).

### Paragraph P-54 (Dark matter direct detection + CQE dark matter prediction)
> The LZ, XENONnT, and PandaX-4T experiments have all reported null results for WIMP dark matter at unprecedented sensitivity (σ_SI ~ 10⁻⁴⁸ cm²), and have detected solar ⁸B neutrinos via coherent elastic neutrino-nucleus scattering (LZ: Phys. Rev. Lett. 135, 011802 (2025); XENONnT: Phys. Rev. Lett. 135, 221003 (2025); PandaX-4T: Phys. Rev. Lett. 134, 011805 (2025)). The "neutrino fog" now limits direct detection reach. CQE/CMPLX must state whether its framework predicts a WIMP dark matter candidate with specific mass and cross-section, or whether dark matter is a non-particle phenomenon (e.g., geometric residue from curvature repair). **Priority action:** If CQE predicts WIMPs, derive m_χ and σ_SI and compare to LZ/XENONnT exclusion limits. If CQE predicts no WIMPs, state this as a falsifiable prediction consistent with current null results, and identify the CQE dark matter detection strategy.

### Paragraph P-55 (Ultra-high-rate QEC + CQE Leech-lattice codes)
> QuEra, Harvard, and MIT have demonstrated ultra-high-rate quantum error-correcting codes with encoding rates above 50% and logical error rates approaching 10⁻¹³ on neutral-atom hardware (Apr 2026), packing 6 logical qubits into 16 physical atoms (4.7:1 ratio). Atom Computing has demonstrated repeated toric-code syndrome extraction (Jun 2026, arXiv:2606.04079). Google Quantum AI has achieved below-threshold surface-code QEC (Nature 638, 920, 2025). CQE/CMPLX’s NP-07 proposes Leech-lattice-based quantum error correction. **Priority action:** Benchmark CQE’s Leech-lattice QEC against these demonstrated results: state the predicted threshold, encoding ratio, and logical error rate; identify whether Leech-lattice codes offer unique advantages (e.g., Monster-group symmetry protection, non-Abelian anyons) that justify any overhead disadvantage relative to ultra-high-rate LDPC or surface codes.

### Paragraph P-56 (Einstein Telescope / Cosmic Explorer + CQE GR tests)
> The Einstein Telescope (ET, Europe) and Cosmic Explorer (CE, U.S.) are planned 3rd-generation ground-based gravitational-wave detectors with ~10× sensitivity improvement over LIGO/Virgo, targeting late-2030s operation (ET Design Study 2020; Reitze et al., arXiv:1907.04833, 2019). ET’s triangular underground configuration with 10 km arms and cryogenic interferometers will detect millions of compact binary mergers per year. CQE/CMPLX’s Paper 14 proposes GR "boundary-repair" corrections. **Priority action:** Derive parametrized post-Einsteinian (ppE) waveform corrections from FLCR curvature-repair terms, compute their observational signatures in ET/CE binary merger data, and predict whether CQE’s GR modifications are detectable at ET/CE sensitivity. If CQE predicts no deviation from GR, this is an equally falsifiable statement that ET/CE will test to unprecedented precision.

---

*End of Supplement Q*
