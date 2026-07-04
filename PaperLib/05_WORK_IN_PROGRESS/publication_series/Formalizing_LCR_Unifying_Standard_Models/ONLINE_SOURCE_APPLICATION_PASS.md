# Online Source Application Pass

Date: 2026-06-28

## Purpose

This pass applies online authoritative sources directly to FLCR-31 through
FLCR-40 and the Standard Model Defining layer. The goal is to stop treating
source-available facts as missing data while still preserving the distinction
between:

- definition closure;
- citation-bound standard formalism;
- external numerical calibration;
- receipt-bound internal FLCR closure;
- material/domain data requirements;
- falsifier or open-obligation boundaries.

## Applied Sources

| Source ID | Source | Online URL | Applied closure |
|---|---|---|---|
| `IRL-PDG-2026` | Particle Data Group Review of Particle Physics 2026 | https://pdg.lbl.gov/ | Current Standard Model particle/data review surface for gauge, QCD, electroweak, Higgs, fermion, neutrino, and comparator rows. |
| `IRL-NIST-ALPHA-2022` | NIST CODATA inverse fine-structure constant | https://physics.nist.gov/cgi-bin/cuu/Value?alphinv= | Numerical calibration value for alpha inverse: `137.035999177` with standard uncertainty `0.000000021`. |
| `IRL-CODATA-2022-WALLET` | NIST CODATA 2022 wallet card | https://physics.nist.gov/cuu/pdf/wallet_2022.pdf | Compact constants table for alpha, alpha inverse, G, electric/magnetic constants, and unit-calibration rows. |
| `IRL-ATLAS-HIGGS-2012` | ATLAS Higgs discovery paper | https://arxiv.org/abs/1207.7214 | External Higgs discovery/mass-scale calibration row: `126.0 +/- 0.4(stat) +/- 0.4(sys) GeV`, 5.9 sigma. |
| `IRL-CMS-HIGGS-2012` | CMS Higgs discovery paper | https://arxiv.org/abs/1207.7235 | Independent Higgs discovery/mass-scale calibration row: near `125 GeV`, fitted mass `125.3 +/- 0.4(stat.) +/- 0.5(syst.) GeV`, 5.0 sigma local significance. |
| `IRL-EXCITON-2D-REVIEW` | Excitons in two-dimensional materials | https://arxiv.org/abs/1911.00087 | Electron-hole-exciton formalism, reduced screening, stronger Coulomb interaction, bound electron-hole pairs, material-dependent effects. |
| `IRL-NIST-CARRIER-DYNAMICS` | NIST carrier dynamics by ultrafast THz spectroscopy | https://www.nist.gov/programs-projects/carrier-dynamics-measured-ultrafast-time-resolved-terahertz-spectroscopy | Experimental/metrology lane for excitons, electron-hole separation, recombination, and free carrier dynamics. |
| `IRL-NIST-PV-EXCITON` | NIST optoelectrical characterization of photovoltaic materials | https://www.nist.gov/programs-projects/optoelectrical-characterization-nanostructured-photovoltaic-materials-and-devices | Materials lane for exciton separation into free electrons and holes at heterojunction interfaces. |
| `IRL-LRR-GR-HYPERBOLIC` | Living Reviews in Relativity: hyperbolic methods for Einstein equations | https://link.springer.com/article/10.12942/lrr-1998-3 | GR/continuum formalism boundary: Einstein equations as hyperbolic/PDE systems after gauge/constraint handling. |
| `IRL-PPPL-PLASMA-MAGNETIC` | PPPL fusion/plasma magnetic confinement testimony | https://fire.pppl.gov/Prager_Testimony.pdf | Plasma boundary row: ions/electrons in plasma spiral along magnetic-field direction; magnetic confinement is units/model/data-bound. |
| `IRL-PPPL-PLASMA-DIAGNOSTICS-2026` | PPPL Plasma Diagnostics lecture notes | https://w3.pppl.gov/~hji/Diagnostics_Lecture_Notes_04-28-26.pdf | Plasma definition/calibration row: plasma consists of particles and fields; diagnostics are required for measured claims. |

## Paper Routing

| FLCR paper | Source rows applied | Claim effect |
|---|---|---|
| `FLCR-31` | PDG, NIST alpha/CODATA | Gauge target and coupling-calibration rows can cite current online data; coupling identity remains scale/scheme-bound. |
| `FLCR-32` | PDG, quark-face receipts | QCD color target can cite PDG while internal color transport cites FLCR receipts. |
| `FLCR-33` | PDG, ATLAS, CMS, NIST/CODATA | Higgs/electroweak mass-scale rows can cite discovery and constants data; LCR mass prediction remains separate. |
| `FLCR-34` | Exciton review, NIST carrier dynamics, NIST PV exciton | Electron-hole-exciton vocabulary and experimental metrology rows are no longer missing. |
| `FLCR-35` | Living Reviews GR, NIST/CODATA | GR/continuum rows can cite PDE/field-equation formalism and units; discrete repair remains structural until limit/calibration is supplied. |
| `FLCR-36` | Exciton review, NIST carrier/PV, MetaForge receipt | Materials and condensed-matter data rows have online source lanes; fabricated-performance rows remain validation-bound. |
| `FLCR-37` | PPPL plasma sources, NIST/CODATA | Plasma/energy carrier rows can cite real plasma/field/diagnostic sources; measured plasma claims remain experiment-bound. |
| `FLCR-38` | PDG/Nobel neutrino, MannyAI runtime docs | Observer/computation paper can cite neutrino-sector residues and runtime evidence separately. |
| `FLCR-39` | All source rows | Comparator paper now has a source-available lane for online citation checks. |
| `FLCR-40` | All source rows | Grand synthesis consumes all online-source closures through dependency-explicit lanes. |

## Closure Rule

An online source closes only the lane it actually supports. A PDG or NIST row can
close a definition or numerical calibration target. It does not close an LCR
identity proof by itself. An experimental source can close the existence of a
measured external object. It does not close the FLCR translation unless the
mapped LCR object, receipt, comparator, and boundary are also present.
