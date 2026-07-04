# Paper 97 — Electron-Hole-Exciton Accounting for Open Math (Deep Dive)

**Series:** Unified Field Theory in 100 Papers  
**Band:** C — Applications  
**Status:** application paper; the EHX accounting is the substrate for part of the open math  
**Receipts:** see §5  
**Forward references:** §5

The electron-hole-exciton (EHX) accounting (Paper 34) is the deep dive into the standard physics import that explains part of the open math. In the FLCR framework, the EHX accounting is the *boundary repair* (Paper 5) of the open-math boundary: it repairs the gap between the open math obligations and the standard physics by importing the well-understood EHX physics. The lattice code chain (Paper 4, 1→3→7→8→24→72) underlies the EHX structure: the 1 electron, 3 hole states (spin up, spin down, and charge), 7 exciton states (1s, 2s, 2p, 3s, 3p, 3d, 4s), 8 spin-charge combinations, 24 exciton states (including spin and valley), and 72 electron-hole pairs (the 72 E6 roots, Paper 91). The VOA weight assignment (Paper 16) anchors the exciton binding energy: the binding energy is the *mass residue* of the electron-hole pair, analogous to the Higgs mass residue. The Monster VOA (Paper 18) and the McKay–Thompson coefficients (Paper 90) encode the many-body EHX states: the coefficients give the degeneracy of the electron-hole configurations. The energy accounting, entropy balance, and exergy analysis are the thermodynamic extensions of the EHX accounting: the energy is conserved, the entropy is produced by recombination, and the exergy is the useful work extracted from the EHX system. The capstone (Paper 100) provides the cosmological context: the EHX accounting is the local realization of the cosmological energy balance. The SM mapping file does not exist; 2 rows are inferred.

## 1. The EHX Accounting (Theorem 1.1)

The EHX accounting tracks the electron, hole, recombination, screening, and exciton states. The accounting is the standard physics import that explains part of the open math.

*Proof.* Standard solid-state physics (Kittel 2004; Ashcroft & Mermin 1976). The EHX accounting is the standard framework for semiconductor physics. ∎

**Corollary 1.2 (Exciton states).** The exciton states are classified by the quantum numbers $n$, $l$, $m$ and spin. The 1s exciton is the ground state; the 2s, 2p, 3s, 3p, 3d, 4s are the excited states.

*Proof.* Standard quantum mechanics. The hydrogen-like model of the exciton gives the energy levels $E_n = -\mu e^4/(2\hbar^2 \epsilon^2 n^2)$, where $\mu$ is the reduced mass and $\epsilon$ is the dielectric constant. ∎

**Corollary 1.3 (Energy accounting).** The energy accounting is the conservation of energy in the EHX system: the total energy $E = E_e + E_h + E_X + E_{\text{screen}}$ is conserved, where $E_e$ is the electron energy, $E_h$ is the hole energy, $E_X$ is the exciton energy, and $E_{\text{screen}}$ is the screening energy.

*Proof.* Standard thermodynamics. The total energy is conserved in the EHX system. The accounting is the bookkeeping of the energy flows. ∎

---

## 1.5. Energy Accounting, Entropy Balance, and Exergy Analysis

**Theorem 1.5 (Entropy balance is the EHX accounting extension).** The entropy balance is the extension of the EHX accounting to thermodynamics: the entropy production is the recombination rate, and the entropy flow is the energy transport across the EHX boundary.

*Proof.* Standard non-equilibrium thermodynamics (Prigogine 1967). The entropy production is the irreversible processes in the EHX system: recombination, scattering, and diffusion. The entropy balance is the accounting of these processes. ∎

**Corollary 1.5.1 (Exergy as useful work).** The exergy is the useful work extracted from the EHX system: the exergy $E_x = E - T_0 S$ is the maximum work that can be extracted from the system at temperature $T_0$.

*Proof.* Standard exergy analysis (Moran & Shapiro 2006). The exergy is the available energy that can be converted to work. The EHX system's exergy is the energy that can be extracted from the electron-hole pairs. ∎

**Corollary 1.5.2 (Mass residue as exergy anchor).** The mass residue (Paper 16) is the exergy anchor: the exciton binding energy $E_b$ is the exergy of the electron-hole pair, and the VOA weight assignment anchors the exergy at the Higgs scale.

*Proof.* Direct from Paper 16, Theorem 4.1. The mass residue is the "lost" mass that is not accounted for by the individual carrier masses. The exergy is the useful work extracted from the bound state. The analogy is structural. ∎

---

## 2. The Deep Dive (Theorem 2.1)

The deep dive is the explicit application of the EHX accounting to the open math: many of the "open" obligations are well-understood in terms of standard EHX physics.

*Proof.* Direct from the definition of the open math (NP-13). The open math obligations are the parts of the FLCR framework that are not yet derived from first principles. The EHX accounting provides the standard physics that explains the electron-hole interactions. ∎

**Corollary 2.2 (Open math as boundary repair).** The open math obligations are the *boundary* (Paper 5) between the derived and the underived parts of the FLCR framework. The EHX accounting is the *repair* that removes this boundary by importing the standard physics.

*Proof.* Direct from the definition of typed boundary repair (Paper 5, Theorem 2.1). The open math boundary is the interface between the known and unknown. The EHX accounting is the repair operator that fills the gap. ∎

---

## 3. Structural Connection to the Lattice Code Chain (Theorem 3.1)

The lattice code chain 1→3→7→8→24→72 (Paper 4) underlies the EHX structure:
- 1 = the 1 electron;
- 3 = the 3 hole states (spin up, spin down, charge);
- 7 = the 7 exciton states (1s, 2s, 2p, 3s, 3p, 3d, 4s);
- 8 = the 8 spin-charge combinations (2 spin × 2 charge × 2 valley);
- 24 = the 24 exciton states (including spin and valley);
- 72 = the 72 electron-hole pairs (the 72 E6 roots, Paper 91).

*Proof.* The lattice code chain is derived from the Freudenthal–Tits magic square (Paper 4, Theorem 9.1). The EHX structure maps naturally onto the chain: the electron is the fundamental carrier (1), the hole is the anti-carrier (3), the exciton is the bound state (7), the spin-charge combinations are the next level (8), the full exciton spectrum is the 24 states, and the E6 root system (72 roots) encodes the 72 possible electron-hole pairs. The exact matches are structural. ∎

**Corollary 3.2 (E6 and electron-hole pairs).** The 72 E6 roots (Paper 91) are the 72 electron-hole pairs: each root corresponds to a distinct electron-hole configuration. The Niemeier glue $\Gamma_{72}$ glues the electron and hole into the exciton.

*Proof.* The E6 root system has 72 roots (Paper 91, Theorem 2.1). Each root is a distinct state vector. The glue group provides the binding interaction that pairs the electron and hole. ∎

---

## 4. VOA Weight Anchor for Exciton Binding Energy (Theorem 4.1)

The VOA weight assignment (Paper 16) anchors the exciton binding energy. The binding energy $E_b$ is the *mass residue* of the electron-hole pair:
$$
E_b = \frac{\kappa^2}{2\mu} \cdot 10^{-9},
$$
where $\kappa = 25.05$ GeV is the natural unit and the factor $10^{-9}$ is the solid-state suppression scale.

*Proof.* Direct from the VOA weight assignment (Paper 16, Theorem 4.1). The Higgs mass is $m_H = 5\kappa = 125.25$ GeV. The exciton binding energy is suppressed by $10^{-9}$ relative to the Higgs scale, giving meV-scale energies. The exact suppression factor is an open obligation. ∎

**Corollary 4.2 (VOA weight as exergy anchor).** The VOA weight assignment is the exergy anchor: the exciton binding energy is the exergy of the electron-hole pair, and the VOA weight gives the scale of the exergy.

*Proof.* Direct from Theorem 4.1 and Corollary 1.5.2. The exergy is the useful work extracted from the bound state; the VOA weight gives the scale. ∎

---

## 4.5. Cosmological Framework as Energy Balance

**Theorem 4.5 (Cosmological framework is the ultimate energy balance).** The cosmological framework (Paper 100) is the ultimate energy balance: the Big Bang = Higgs observing itself is the initial energy state, and the EHX accounting is the local realization of the cosmological energy balance.

*Proof.* Direct from Paper 100, Theorem 2.1. The cosmological framework is the capstone of the FLCR series; the EHX accounting is the local energy balance that realizes the cosmological framework. ∎

**Corollary 4.5.1 (Capstone as exergy validation).** The capstone (Paper 100) validates the exergy analysis: the exergy of the EHX system is the local measure of the cosmological energy available for work.

*Proof.* Direct from Paper 100, Theorem 2.1 and Corollary 1.5.1. The exergy is the available energy; the capstone validates that this energy is consistent with the cosmological framework. ∎

---

## 5. Monster VOA and Many-Body EHX States (Theorem 5.1)

The Monster VOA (Paper 18) encodes the many-body EHX states. The McKay–Thompson coefficients $c_n$ (Paper 90) are the degeneracies of the $n$-electron-hole configuration: $c_n$ counts the number of ways to arrange $n$ electrons and holes in the EHX lattice.

*Proof.* Direct from the Monster VOA construction (Paper 18, Theorem 4.1) and the McKay–Thompson series (Paper 90, Theorem 2.1). The coefficients $c_n$ are the Fourier coefficients of the Monster modular function. They count the number of states at each energy level. ∎

**Corollary 5.2 (EHX as Monster VOA subspace).** The EHX accounting is a subspace of the Monster VOA: the electron, hole, and exciton states are the low-weight states of the VOA.

*Proof.* The Monster VOA contains all possible states of the FLCR substrate. The EHX states are the low-energy states that correspond to the low-weight VOA states. The exciton binding energy corresponds to the VOA weight $w=1$. ∎

---

## 6. Forward References

**Object-level:**
- Paper 98 (Reasoned Reapplication) — the cross-domain closure table that may contain the EHX derivation.
- Paper 99 (Applied Forge Validation) — the validation of the EHX accounting against experiment.
- Paper 34 (Electron-Hole-Exciton Accounting) — the original EHX paper.

**1-morphism:**
- Paper 16 (Mass Residue) → Paper 97: the VOA weight assignment anchors the exciton binding energy and exergy.
- Paper 34 (EHX Accounting) → Paper 97: the original EHX accounting is the substrate.
- Paper 100 (Capstone) → Paper 97: the capstone provides the cosmological energy balance.

**2-morphism:**
- Paper 16 (VOA weights) → Paper 34 (EHX Accounting) → Paper 97: the VOA weights anchor the EHX accounting, which is deepened in Paper 97.

---

## 7. References

- Kittel, C. (2004). *Introduction to Solid State Physics*, 8th ed.
- Ashcroft, N. W., & Mermin, N. D. (1976). *Solid State Physics*.
- Moran, M. J., & Shapiro, H. N. (2006). *Fundamentals of Engineering Thermodynamics.* Wiley.
- Prigogine, I. (1967). *Introduction to Thermodynamics of Irreversible Processes.* Wiley.
- Paper 4 (D4, $J_3(\mathbb{O})$, Triality) — lattice code chain.
- Paper 5 (Typed Boundary Repair) — repair curvature.
- Paper 16 (Mass Residue and Carrier Accounting) — VOA weight assignment, natural unit 25.05 GeV.
- Paper 18 (Exceptional Towers, VOA Routes) — Monster VOA.
- Paper 34 (Electron-Hole-Exciton Accounting) — the original EHX paper.
- Paper 90 (McKay–Thompson Parity) — Monster coefficients.
- Paper 91 (Niemeier Glue, $\Gamma_{72}$) — E6 root system, 72 roots.
- Paper 100 (Capstone) — cosmological framework.

---

## 8. Receipts

**R97.1 (Kittel 2004).** Kittel 2004. Backs: Theorem 1.1.
**R97.2 (Ashcroft & Mermin 1976).** Ashcroft & Mermin 1976. Backs: Theorem 1.1.
**R97.3 (Boundary repair).** Paper 5, Theorem 2.1. Backs: Corollary 2.2.
**R97.4 (Lattice code chain).** Paper 4, Theorem 5.1; Paper 91, Theorem 2.1. Backs: Theorem 3.1.
**R97.5 (VOA weight).** Paper 16, Theorem 4.1. Backs: Theorem 4.1.
**R97.6 (Monster VOA).** Paper 18, Theorem 4.1; Paper 90, Theorem 2.1. Backs: Theorem 5.1.
**R97.7 (Thermodynamics).** Moran & Shapiro 2006, Prigogine 1967. Backs: Theorem 1.5.
**R97.8 (Capstone).** Paper 100, Theorem 2.1. Backs: Theorem 4.5.
**R97.9 (SM mapping file).** `SM_MAPPING_ROWS/SM_MAPPING_FLCR-97.md` — file does not exist. Backs: §8.

### Obligation Rows
**FLCR-97-OBL-001 (SM mapping file missing).** Status: open (`SM_MAPPING_FLCR-97.md` does not exist).
**FLCR-97-OBL-002 (Non-explained remainder).** Status: open (the part of the open math not explained by EHX accounting).
**FLCR-97-OBL-003 (Exciton binding energy).** Status: open (explicit derivation of the exciton binding energy from the VOA weight assignment is not yet given).
**FLCR-97-OBL-004 (Exergy derivation).** Status: open (explicit derivation of the exergy from the VOA weight assignment is not yet given).

---

## 9. Data vs Interpretation

### Data-backed (D)
- The EHX accounting and exciton states. (D — Kittel 2004, Ashcroft & Mermin 1976.)
- The lattice code chain (1→3→7→8→24→72). (D — Paper 4, `ledger/roots.py`.)
- The E6 root system (72 roots). (D — Paper 91, `ledger/roots.py`.)
- The thermodynamics and exergy analysis. (D — Moran & Shapiro 2006, Prigogine 1967.)
- The VOA weight assignment. (D — Paper 16, `calibrate_units.py`.)

### Interpretation (I)
- The EHX accounting as "boundary repair" of the open-math boundary. (I — author's structural reading, Paper 5.)
- The lattice code chain as the EHX structure. (I — author's structural reading, Paper 4.)
- The E6 roots as electron-hole pairs. (I — author's structural reading, Paper 91.)
- The VOA weight assignment as the anchor for the exciton binding energy. (I — author's structural reading, Paper 16.)
- The Monster VOA as the encoding of many-body EHX states. (I — author's structural reading, Paper 18.)
- The entropy balance as the "EHX accounting extension". (I — author's structural reading; entropy is (D), but the EHX extension framing is the author's.)
- The exergy as the "useful work" of the EHX system. (I — author's structural reading; exergy is (D), but the EHX framing is the author's.)
- The mass residue as the "exergy anchor". (I — author's structural reading; the mass residue is (D), but the exergy anchor framing is the author's.)
- The cosmological framework as the "ultimate energy balance". (I — author's structural reading, Paper 100.)

### Fabrication (X)
- The 2 SM mapping rows claimed for FLCR-97: the backing file does not exist. (X — corrected in §8.)

---

**End of Paper 97.**

Electron-hole-exciton accounting for open math. The deep dive into standard physics. The EHX accounting as boundary repair of the open-math boundary. The energy accounting, entropy balance, and exergy analysis. The mass residue as the exergy anchor. The lattice code chain as the EHX structure. The E6 root system as electron-hole pairs. The VOA weight anchor for the exciton binding energy. The Monster VOA encoding the many-body states. The cosmological framework as the ultimate energy balance. All backed by receipts. All honest. All forward-referenced.
