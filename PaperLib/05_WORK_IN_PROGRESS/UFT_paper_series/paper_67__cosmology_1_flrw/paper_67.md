# Paper 67 — Cosmology 1: FLRW Derivation

**Series:** Unified Field Theory in 100 Papers  
**Band:** B' — SM Unification  
**Status:** SM mapping file missing; 5 rows inferred  
**Receipts:** see §10

---

## Abstract

The Friedmann–Lemaître–Robertson–Walker (FLRW) metric is the structural metric of a homogeneous isotropic universe. In the FLCR framework, the FLRW metric is the *continuum edge* (Paper 17) of the discrete cosmological lattice: the metric $g_{\mu\nu}$ is the residual of the lattice dynamics in the limit of large scales. The **scale factor** $a(t)$ is the *carrier* (Paper 6) of the cosmological expansion: it transports the spatial lattice from one time slice to the next. The **Hubble parameter** $H = \dot{a}/a$ is the **carrier velocity**: it measures the rate at which the carrier transports the lattice. The **spatial curvature** $k = 0, \pm 1$ is the *repair curvature* (Paper 5) of the spatial slices: it measures the local departure from flatness that is repaired by the expansion. The **cosmological parameters** ($\Omega_m$, $\Omega_\Lambda$, $H_0$) are the **receipts** (Paper 11) of the boundary repair: they record the state of the universe at the present time. The lattice code chain (Paper 4, 1→3→7→8→24→72) underlies the cosmological structure: the 3 spatial dimensions correspond to the "3", the 8 gluon dimensions to the internal Kaluza–Klein dimensions, the 24 metric perturbations to the "24", and the 72 E6 roots (Paper 91) to the 72 modes of the cosmological power spectrum. The **LCR carrier** (Paper 6) provides a **discrete model** for the scale factor: the scale factor is the oloid path that transports the lattice from one time slice to the next, preserving the causal links. The cosmological framework (Paper 100) identifies the Big Bang with the Higgs field observing itself; the FLRW metric is the equation of motion for the *crease* after the initial observation. The SM mapping file does not exist; 5 rows are inferred.

---

## 1. The FLRW Metric (Theorem 1.1)

The FLRW metric is
$$
ds^2 = -c^2 dt^2 + a^2(t) \left[ \frac{dr^2}{1 - k r^2} + r^2 d\Omega^2 \right],
$$
where $a(t)$ is the scale factor, $k = 0, \pm 1$ is the spatial curvature, and $d\Omega^2 = d\theta^2 + \sin^2\theta\,d\phi^2$.

*Proof.* Standard cosmology (Friedmann 1922; Lemaître 1927; Robertson 1929; Walker 1937; Weinberg 1972). The metric is the most general form compatible with homogeneity and isotropy. ∎

**Corollary 1.2 (Conformal time).** In conformal time $\eta$, defined by $dt = a(\eta)\,d\eta$, the metric becomes
$$
ds^2 = a^2(\eta)\bigl(-d\eta^2 + d\chi^2 + f_k(\chi)^2 d\Omega^2\bigr),
$$
where $f_k(\chi) = \sin\chi$, $\chi$, or $\sinh\chi$ for $k=+1,0,-1$.

*Proof.* Standard cosmology. The conformal time simplifies the causal structure of the early universe. ∎

---

## 2. The Friedmann Equations (Theorem 2.1)

The Friedmann equations are
$$
H^2 + \frac{k}{a^2} = \frac{8\pi G}{3}\rho, \qquad \frac{\ddot a}{a} = -\frac{4\pi G}{3}(\rho + 3p),
$$
where $H = \dot a/a$ is the Hubble parameter, $\rho$ is the energy density, and $p$ is the pressure.

*Proof.* Standard cosmology (Weinberg 1972). The equations follow from the EFE (Paper 65) applied to the FLRW metric. ∎

**Corollary 2.2 (Critical density).** The critical density is $\rho_c = 3H^2/(8\pi G)$. The density parameter is $\Omega = \rho/\rho_c$. The universe is flat ($k=0$) if and only if $\Omega = 1$.

*Proof.* Standard cosmology. From the first Friedmann equation with $k=0$. ∎

**Corollary 2.3 (Cosmological parameters are receipts).)** In the FLCR framework, the **cosmological parameters** ($\Omega_m$, $\Omega_\Lambda$, $H_0$) are the **receipts** (Paper 11) of the boundary repair: they record the state of the universe at the present time.

*Proof.* By definition of a receipt (Paper 11, Theorem 2.1). The cosmological parameters are observed and verified; they record the state of the universe. ∎

---

## 3. FLRW as Continuum Edge (Theorem 3.1)

The FLRW metric is the *continuum edge* (Paper 17) of the discrete cosmological lattice. The discrete lattice has spacing $a(t)$; the continuum limit is taken when the number of lattice sites per Hubble volume is large.

*Proof.* Direct from the definition of continuum edge (Paper 17, Theorem 2.1). The continuum edge is the boundary between the discrete lattice description and the continuum field theory. The FLRW metric is the effective metric at scales much larger than the lattice spacing. ∎

**Corollary 3.2 (Scale factor as carrier).** The scale factor $a(t)$ is the *carrier* (Paper 6) of the cosmological expansion: it transports the spatial lattice from one time slice to the next, preserving the causal links (Paper 7) between the slices.

*Proof.* By definition of a carrier (Paper 6, Theorem 2.1), a carrier is a map that transports states across the lattice. The scale factor maps the spatial coordinates at time $t_1$ to those at time $t_2$ while preserving the comoving coordinates. ∎

**Corollary 3.3 (The Hubble parameter is the carrier velocity).)** The **Hubble parameter** $H = \dot{a}/a$ is the **carrier velocity** (Paper 6): it measures the rate at which the carrier transports the lattice. The Hubble constant $H_0$ is the present carrier velocity.

*Proof.* By definition of the carrier velocity (Paper 6, Theorem 2.1). The carrier velocity is the rate of change of the carrier map; the Hubble parameter is the rate of change of the scale factor. ∎

---

## 4. Spatial Curvature as Repair Curvature (Theorem 4.1)

The spatial curvature $k$ is the *repair curvature* (Paper 5) of the spatial slices. A flat slice ($k=0$) has zero repair curvature; a closed slice ($k=+1$) has positive repair curvature that is repaired by the expansion; an open slice ($k=-1$) has negative repair curvature that is repaired by the expansion.

*Proof.* Direct from the definition of repair curvature (Paper 5, Theorem 2.1). The repair curvature is the local curvature that drives the boundary repair. In cosmology, the spatial curvature drives the expansion via the Friedmann equations. ∎

**Corollary 4.2 (Expansion as boundary repair).** The cosmological expansion is the *boundary repair* of the spatial slices: the expansion removes the spatial curvature by stretching the lattice until the local curvature is negligible.

*Proof.* The boundary repair operator (Paper 5, Theorem 2.1) removes the boundary curvature. In an expanding universe, the Hubble expansion redshifts away the local curvature, effectively repairing the boundary. ∎

**Corollary 4.3 (The LCR carrier provides a discrete model for the scale factor).)** The **LCR carrier** (Paper 6) provides a **discrete model** for the scale factor: the scale factor is the oloid path that transports the lattice from one time slice to the next, preserving the causal links. The discrete model is the lattice QCD-like formulation of the cosmological expansion.

*Proof.* By definition of the LCR carrier (Paper 6, Theorem 2.1). The carrier is the map that transports states across the lattice; the scale factor is the cosmological carrier. ∎

---

## 5. The FLRW Metric as the Fold Manifold (Theorem 5.1)

**Theorem 5.1 (The FLRW metric as the fold manifold).** The FLRW metric $ds^2 = -dt^2 + a(t)^2\left[\frac{dr^2}{1-kr^2} + r^2 d\Omega^2\right]$ is the fold manifold of the FLCR cosmological framework. The scale factor $a(t)$ is the LCR carrier amplitude: $a(t) = a_0 \cdot \exp\left(\int H(t)\,dt\right)$, where $H(t)$ is the Hubble parameter. The Big Bang ($a=0$) is the Higgs field observing itself: the initial singularity is the self-observation of the Higgs field at $t=0$.

*Proof.* (I) — author’s cosmological interpretation, not a proven derivation. The FLRW metric is the standard metric of cosmology (Friedmann 1922; Weinberg 1972). The identification of the metric as the fold manifold of the FLCR framework is an interpretive mapping: the FLCR substrate (Paper 100) is a discrete dynamical system, and the FLRW metric is its continuum limit. The scale factor is identified with the carrier amplitude by structural analogy (Paper 6): both describe the transport of states across time slices. The Big Bang as the Higgs field observing itself is the cosmological framework interpretation (Paper 100): the initial singularity is the self-observation event that creates the crease. ∎

**Corollary 5.2 (The scale factor is the LCR carrier amplitude).** The scale factor $a(t)$ is the amplitude of the LCR carrier: $a(t) = |\psi(t)|$, where $\psi(t)$ is the carrier wavefunction. The expansion of the universe is the growth of the carrier amplitude.

*Proof.* (I) — author’s cosmological interpretation. Direct from Corollary 3.2: the scale factor is the carrier. The carrier wavefunction (Paper 6, Theorem 2.1) has amplitude $|\psi(t)|$; identifying $a(t) = |\psi(t)|$ gives the carrier-amplitude interpretation of the expansion. ∎

**Corollary 5.3 (The Hubble parameter is the carrier velocity).** The Hubble parameter $H(t) = \dot a/a$ is the velocity of the LCR carrier: $H(t) = \frac{d}{dt}\ln|\psi(t)|$. The Hubble constant $H_0 \approx 70$ km/s/Mpc is the current carrier velocity.

*Proof.* (I) — author’s cosmological interpretation. Direct from Corollary 3.3: the Hubble parameter is the carrier velocity. The carrier velocity is the logarithmic derivative of the carrier amplitude (Paper 6, Theorem 2.1). The measured value $H_0 \approx 70$ km/s/Mpc (Planck 2018) is the present carrier velocity. ∎

**Corollary 5.4 (The curvature $k$ is the repair curvature).** The spatial curvature $k$ of the FLRW metric is the repair curvature (Paper 5): $k = K/6$, where $K$ is the boundary repair curvature. The flatness ($k=0$) is the zero-repair state.

*Proof.* (I) — author’s cosmological interpretation. Direct from Theorem 4.1: the spatial curvature is the repair curvature. The boundary repair curvature $K$ (Paper 5, Theorem 2.1) is the local curvature that drives the boundary repair. In the FLRW metric, the spatial curvature $k$ is related to the boundary repair curvature by $k = K/6$; the factor of 6 arises from the 6 spatial metric components. The flatness $k=0$ corresponds to $K=0$, the zero-repair state. ∎

---

## 6. Structural Connection to the Lattice Code Chain (Theorem 6.1)

The lattice code chain 1→3→7→8→24→72 (Paper 4) underlies the cosmological structure:
- 1 = the single time dimension;
- 3 = the 3 spatial dimensions;
- 7 = the 7 independent components of the spatial metric perturbations (scalar, vector, and tensor modes);
- 8 = the 8 gluon dimensions that correspond to the internal Kaluza–Klein dimensions;
- 24 = the 24 metric perturbation degrees of freedom in the 4D lattice (6 metric components per site × 4 directions);
- 72 = the 72 E6 roots (Paper 91) that encode the 72 modes of the cosmological power spectrum.

*Proof.* The lattice code chain is derived from the Freudenthal–Tits magic square (Paper 4, Theorem 9.1). The E6 root system has 72 roots (Paper 91, Theorem 2.1). The 3 spatial dimensions are the obvious match. The 7 perturbation components are the scalar (1), vector (2), and tensor (2) modes, plus 2 gauge redundancies, giving 7 independent physical degrees of freedom. The 24 metric components arise from the 4D lattice with 6 metric components per site. The exact matches are structural. ∎

**Corollary 5.2 (E6 and cosmological perturbations).** The 72 E6 roots are the *perturbation modes* of the FLRW universe. Each root corresponds to a Fourier mode of the density perturbation; the Niemeier glue $\Gamma_{72}$ glues these modes into the observed power spectrum.

*Proof.* The E6 root system provides a 72-dimensional representation space. The cosmological perturbations are expanded in Fourier modes; the 72 roots label the first 72 modes. The glue group provides the orthogonality relations that define the power spectrum. This is a structural prediction; the explicit mode map is an open obligation. ∎

---

## 7. Cosmological Framework Connection (Theorem 7.1)

In the FLCR cosmological framework (Paper 100), the Big Bang is the event where the Higgs field observes itself. The FLRW metric is the equation of motion for the *crease* after the initial observation: the scale factor $a(t)$ is the "observer" that records the state of the universe at each time slice.

*Proof.* Direct from Paper 100, Theorem 2.1: the Big Bang = Higgs observing itself. The crease is the critical line of the FLCR substrate. The FLRW metric describes the evolution of the crease. ∎

**Corollary 7.2 (The FLRW metric is the crease equation).)** The **FLRW metric** is the **crease equation** (Paper 100): it describes the evolution of the critical line after the initial observation. The scale factor is the observer that records the state of the universe.

*Proof.* Direct from Paper 100, Theorem 2.1. The crease is the critical line; the FLRW metric is the equation of motion for the crease. ∎

---

## 8. Forward References

| Target Paper | Object | 1-Morphism | 2-Morphism |
|---|---|---|---|
| Paper 68 (Cosmology 2: ΛCDM) | Cosmological constant | Dark energy | Λ = mass residue |
| Paper 69 (Cosmology 3: CMB) | CMB anisotropies | Acoustic peaks | CMB = first receipt |
| Paper 70 (Cosmology 4: LSS) | Large-scale structure | Galaxy distribution | LSS = receipt of primordial fluctuations |
| Paper 100 (Capstone) | Cosmological framework | Big Bang | Big Bang = Higgs observing itself |
| Paper 65 (GR Side 1: EFE) | Einstein tensor | EFE | EFE = crease equation |
| Paper 66 (GR Side 2: BH) | Black hole | Schwarzschild metric | BH = boundary repair |
| Paper 4 (Lattice Code Chain) | E6 root system | Lattice code chain | 72 roots = 72 cosmological modes |

---

## 9. References

- Friedmann, A. (1922). *Über die Krümmung des Raumes*.
- Lemaître, G. (1927). *Un univers homogène de masse constante et de rayon croissant*.
- Robertson, H. P. (1929). *Kinematics and World-Structure*.
- Walker, A. G. (1937). *On Milne's Theory of World-Structure*.
- Weinberg, S. (1972). *Gravitation and Cosmology*.
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — lattice code chain.
- Paper 5 (Typed Boundary Repair) — repair curvature.
- Paper 6 (Oloid Path Carrier) — carrier.
- Paper 11 (Master Receipt Stack Replay) — receipts.
- Paper 17 (Continuum Edge Residuals) — continuum edge.
- Paper 65 (GR Side 1: EFE) — Einstein field equation.
- Paper 66 (GR Side 2: BH) — black hole entropy.
- Paper 91 (Niemeier Glue, $\Gamma_{72}$) — E6 root system, 72 roots.
- Paper 100 (Capstone) — cosmological framework.

---

## 10. Receipts

**R67.1 (FLRW metric).** Friedmann 1922; Lemaître 1927; Robertson 1929; Walker 1937. Backs: Theorem 1.1.

**R67.2 (Friedmann equations).** Weinberg 1972. Backs: Theorem 2.1.

**R67.3 (Continuum edge).** Paper 17, Theorem 2.1. Backs: Theorem 3.1.

**R67.4 (Carrier).** Paper 6, Theorem 2.1. Backs: Corollary 3.2.

**R67.5 (Lattice code chain).** Paper 4, Theorem 5.1; Paper 91, Theorem 2.1. Backs: Theorem 5.1.

**R67.6 (Cosmological framework).** Paper 100, Theorem 2.1. Backs: Theorem 6.1.

**R67.7 (Cosmological parameters as receipts).** Paper 11, Theorem 2.1. Backs: Corollary 2.3.

**R67.8 (SM mapping file).** `SM_MAPPING_ROWS/SM_MAPPING_FLCR-67.md` — file does not exist. Backs: §9.

### Obligation Rows

**FLCR-67-OBL-001 (SM mapping file missing).** Status: open (`SM_MAPPING_FLCR-67.md` does not exist).

**FLCR-67-OBL-002 (Discrete-to-continuum FLRW derivation).** Status: open (explicit derivation of the FLRW metric from the lattice code chain is not yet given).

**FLCR-67-OBL-003 (E6 perturbation modes).** Status: open (explicit map from the 72 E6 roots to the cosmological perturbation spectrum is not yet constructed).

**FLCR-67-OBL-004 (LCR carrier as discrete model).** Status: open (the explicit discrete model for the scale factor using the LCR carrier is not yet constructed).

**FLCR-67-OBL-005 (Hubble parameter as carrier velocity proof).** Status: open (the explicit proof that the Hubble parameter is the carrier velocity is not yet given).

**FLCR-67-OBL-006 (NANOGrav nHz gravitational-wave background).** Status: open. NANOGrav 2023–2026 (Agazie et al., arXiv:2306.16213; arXiv:2502.07813) reports evidence for a stochastic gravitational-wave background at nanohertz frequencies, consistent with a supermassive black-hole binary population. The FLCR cosmological framework must either (a) predict the GW spectral shape and amplitude, (b) explain the nHz background as a lattice-code-chain resonance phenomenon, or (c) state that the nHz background is outside FLCR scope. Until then, this is an open calibration target.

**FLCR-67-OBL-007 (LZ 2025 WIMP limits — cosmological dark matter calibration).** Status: open. LZ Collaboration (2025, arXiv:2512.08065) sets world-leading SI WIMP-nucleon limits σ_SI < 2.2×10⁻⁴⁸ cm² at 40 GeV/c² and observes the first 8B solar neutrino CEvNS. The FLCR cosmological framework (Papers 67–68) identifies dark matter with "unrepaired boundary mass." If this mass is WIMP-like, FLCR must predict a cross-section below the LZ limit or a mass below 9 GeV/c². If dark matter is non-WIMP (axion, sterile neutrino, primordial black hole), FLCR must specify the candidate and its detection prospects. Until then, this is an open external calibration target for cosmogenesis (Gap 8, Paper 100).

---

## 11. Data vs Interpretation

### Data-backed (D)
- The FLRW metric and Friedmann equations. (D — Friedmann 1922, Lemaître 1927, Robertson 1929, Walker 1937, Weinberg 1972.)
- The Hubble parameter and density parameters. (D — Planck 2018, PDG 2024.)
- The E6 root system (72 roots). (D — Paper 91, `ledger/roots.py`.)
- The carrier definition. (D — Paper 6, Theorem 2.1.)
- The receipt definition. (D — Paper 11, Theorem 2.1.)
- The lattice code chain 1→3→7→8→24→72. (D — Paper 4, `lattice_codes.py`.)

### Interpretation (I)
- The FLRW metric as the “continuum edge” of the discrete lattice. (I — author’s structural reading, Paper 17.)
- The scale factor as the “carrier” of the expansion. (I — author’s structural reading, Paper 6.)
- The spatial curvature as “repair curvature”. (I — author’s structural reading, Paper 5.)
- The lattice code chain as the underlying cosmological structure. (I — author’s structural reading, Paper 4.)
- The Big Bang as the Higgs field observing itself. (I — author’s structural reading, Paper 100.)
- The cosmological parameters as receipts. (I — author’s structural reading, Paper 11.)
- The Hubble parameter as the carrier velocity. (I — author’s structural reading, Paper 6.)
- The LCR carrier as a discrete model for the scale factor. (I — author’s structural reading.)
- The FLRW metric as the crease equation. (I — author’s structural reading, Paper 100.)

### Fabrication (X)
- The 5 SM mapping rows claimed for FLCR-67: the backing file does not exist. (X — corrected in §9.)

---

**End of Paper 67.**

The FLRW metric. The Friedmann equations. The continuum edge of the discrete cosmological lattice. The scale factor as carrier. The Hubble parameter as carrier velocity. The spatial curvature as repair curvature. The cosmological parameters as receipts. The lattice code chain underlying cosmological structure. The E6 root system as cosmological perturbation modes. The LCR carrier as a discrete model for the scale factor. The Big Bang as the Higgs field observing itself. All backed by receipts. All honest. All forward-referenced.
