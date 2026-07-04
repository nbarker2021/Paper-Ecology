# NP-12 — Electron-Hole-Exciton Accounting For Open Math

**Status:** active study / reasoned closure candidate.  
**Purpose:** determine how much CQECMPLX open math is already explained by the
standard electron-hole-exciton process before any new physics language is
allowed to stand.

---

## Publication Draft: Formal Scientific Body

### Abstract

This study asks whether recurring CQECMPLX bridge language around correction,
vacancy, complement, paired residue, excitation, recombination, screening,
transport, band-gap threshold, and bound-state behavior is already accounted
for by standard electron-hole-exciton models. The working hypothesis is not
that the suite has discovered a new exciton theory. The working hypothesis is
that some open physical bridge claims may be ordinary semiconductor or
many-body quasiparticle structure expressed in CQECMPLX vocabulary.

The study will classify each candidate claim into one of four buckets:

```text
standard_explains
analogy_only
requires_cqecmplx_receipt
overclaimed_or_rejected
```

Only the residue after this accounting should remain eligible for new
CQECMPLX-specific mathematics or physics.

### Claim-Strength Correction

This paper is not only a guard against overclaiming. It is also a guard against
underclaiming. If standard condensed-matter formalism already supplies the
exact electron-hole, vacancy, recombination, screening, band-gap, or effective
mass object needed by a CQECMPLX bridge, then that part of the bridge should no
longer be called open. It should be labeled:

```text
standard_model_closed_pending_citation_or_data_bind
```

The remaining CQECMPLX claim is then narrower and stronger:

```text
standard physics supplies the quasiparticle mechanism;
CQECMPLX supplies addressability, obligation state, routing, and receipts.
```

### Keywords

Electron; hole; exciton; quasiparticle; vacancy; correction residue; bound
state; recombination; band gap; physical bridge; claim taxonomy.

### Core Question

```text
How much of the open CQECMPLX math is explained by the standard
electron-hole-exciton process already present in accepted models?
```

### First Research Pass: Standard Formalism

The standard model is already strong enough to explain a large fraction of the
language in the current open bridge layer. Its objects are:

```text
electron: occupied conduction-band quasiparticle state
hole: missing valence-band electron, treated as a positive-charge quasiparticle
exciton: bound neutral electron-hole pair
```

The important point is that a hole already has a name in the standard theory,
but the name is intentionally negative: it names an absence relative to a filled
reference band, not a new elementary particle. That is the conceptual opening
for CQECMPLX. The standard model gives the physics; CQECMPLX may give the
addressing, receipt, and obligation calculus for when an absence becomes an
active carrier.

In effective-mass form, a Wannier-Mott exciton is approximately a screened
two-body problem:

```text
H_X =
  E_g
  - (hbar^2 / 2m_e*) nabla_e^2
  - (hbar^2 / 2m_h*) nabla_h^2
  - e^2 / (4 pi epsilon |r_e - r_h|)
```

With relative coordinate `r = r_e - r_h` and reduced mass

```text
mu = (m_e* m_h*) / (m_e* + m_h*)
```

the bound-state series has the hydrogenic form modified by dielectric screening
and effective mass:

```text
E_n = E_g - R*_X / n^2
R*_X = (mu / m_e) * Rydberg / epsilon_r^2
a*_X = epsilon_r * (m_e / mu) * a_0
```

For strongly bound, local excitons, the Frenkel limit replaces the wide
hydrogenic orbit with a small-radius lattice excitation. For modern optical
spectra, the many-body formalism is usually the Bethe-Salpeter equation (BSE):
an eigenproblem in an electron-hole basis whose kernel includes the attractive
screened electron-hole interaction. In short:

```text
independent particle transition + screened e-h attraction -> excitonic state
```

### What Standard Exciton Theory Solves For Us

| CQECMPLX open language | Standard accounting | Verdict |
|------------------------|---------------------|---------|
| vacancy / missing complement | hole, defect, or vacancy depending on whether the absence is electronic or structural | standard_explains if a band/occupancy model is present |
| Dust pair / paired residue | electron-hole pair | analogy_only until a binding interaction and energy are supplied |
| bound Dust pair | exciton | standard_explains if charge neutrality, binding energy, and screening are specified |
| recombination / closure | electron-hole recombination | standard_explains if an energy relaxation channel is specified |
| bridge threshold | band gap, activation energy, or binding threshold | standard_explains when measured units/material parameters exist |
| mass residue / bondedness | effective mass, binding energy, or polaronic mass renormalization | analogy_only unless the paper explicitly avoids fundamental-mass language |
| interlayer TMD route | interlayer exciton | standard_explains for MoS2/WS2/TMD heterostructure cases with band alignment |
| sample-preserving field | exciton density/wavefunction only after a physical Hamiltonian is declared | requires_cqecmplx_receipt or downgrade |

This means NP-12 should immediately downgrade any claim that treats
`correction`, `Dust`, `hole`, `vacancy`, or `excitation` as physical merely
because the words resemble exciton language. The standard model only explains
the claim when the paper supplies a material, band structure or occupancy
reference, charge assignment, interaction kernel, and energy scale.

### What Remains Open After Standard Accounting

Standard electron-hole-exciton theory does not by itself explain:

- Rule 30/Lucas correction sparsity;
- the typed obligation ledger;
- finite LCR/D4/J3 chart registration;
- no-cost Leech lookup;
- F4 encoder universality;
- Moonshine or sporadic-boundary invariance;
- superpermutation scheduling;
- any claim that a symbolic correction bit is a physical charge carrier.

Those remain CQECMPLX-specific unless a later paper builds a real physical
map. The exciton model can calibrate material/bridge claims, but it does not
close the discrete computational substrate.

### What CQECMPLX May Explain Better

Standard semiconductor theory calls the missing entity a "hole" because the
formal object is an absence relative to a filled band. It is a powerful
calculation device, but the name does not explain when an absence should become
an addressable actor in a broader proof system. CQECMPLX can contribute a
cleaner abstract account:

```text
absence + address + allowed transport + receipt = active complement carrier
```

In that language:

- a hole is not merely a missing electron; it is a missing occupancy with an
  address and admissible transport law;
- an exciton is not merely "electron plus hole"; it is a bound complement pair
  with a conserved relation, interaction energy, and permitted recombination;
- a defect/vacancy is not automatically a carrier; it becomes one only when a
  ledger records its state, coordinate, reason, route, and receipt.

That is the better explanation CQECMPLX can offer without overclaiming
physics: the system names the condition under which absence becomes a real
computational object. The standard model supplies material physics; CQECMPLX
supplies addressability, routing, and falsifier discipline.

### Immediate Claim Reclassification

| Source | Local language | NP-12 action |
|--------|----------------|--------------|
| Paper 05 | physical oloid carrier / gluon worldline | keep as symbolic carrier unless a material Hamiltonian is supplied |
| Paper 07 | between-sample dynamics | downgrade to presentation only until a physical Hamiltonian or exciton density model exists |
| Paper 13 | electron/electron-neutrino vacuum pair and quark-face color language | separate from semiconductor electron-hole theory; do not let exciton analogy support Standard Model claims |
| Paper 15 | mass residue / Higgs language | compare first to effective mass, binding energy, and polaron/exciton renormalization; downgrade any fundamental-mass reading |
| Paper 16 | continuum edge residuals | test against band-edge, defect, and excitation-threshold explanations before new continuum claims |
| Paper 22 | MoS2/TMD/interlayer route | highest-priority empirical exciton accounting target |

### Reasoned Closure Candidates

| Candidate claim family | Standard closure available now | CQECMPLX residue | Action |
|------------------------|--------------------------------|------------------|--------|
| "Hole" as missing complement | A hole is a quasiparticle absence relative to filled-band occupancy. | Define when an absence becomes addressable in CAM/LCR. | cite and promote the standard part; keep addressability as CQE contribution |
| Bound complement pair | Exciton formalism supplies electron-hole bound states with binding energy and screening. | Attach ledger state, route, and recombination receipt. | promote only when material/band/energy terms are named |
| Recombination as closure | Standard recombination explains electron-hole annihilation plus energy relaxation. | CQE closure is typed obligation discharge, not physical recombination unless a channel is supplied. | split terminology in Papers 07/15/16/22 |
| Mass residue language | Effective mass and binding energy explain many apparent "mass residue" phrases. | Fundamental Higgs/rest-mass readings need separate evidence. | downgrade loose mass language; route measured claims to NP-06 |
| Bridge threshold | Band gap, activation energy, and exciton binding threshold are standard. | CAM threshold needs finite address/route criteria. | bind units/material parameters before physics promotion |
| Interlayer route | Interlayer excitons in TMD heterostructures are standard candidates. | MetaForge must bind actual material stack, band alignment, and measured response. | make Paper 22 the primary empirical test case |

### Evaluation Protocol

For each candidate claim, record:

| Field | Meaning |
|-------|---------|
| `paper` | source paper or obligation |
| `local_claim` | CQECMPLX wording to evaluate |
| `standard_model_candidate` | electron, hole, exciton, trion, polariton, screening, recombination, band gap, or none |
| `mapping_strength` | exact, partial, analogy, none |
| `required_equations` | standard equations or conservation relations needed |
| `cqecmplx_residue` | what remains unexplained after standard accounting |
| `classification` | one of the four study buckets |
| `next_action` | cite, downgrade, test, or keep open |

### Initial Target Set

| Source | Why it belongs in NP-12 |
|--------|--------------------------|
| Paper 05 / 05.4 | Physical oloid geometry and carrier transport may overlap with quasiparticle transport language. |
| Paper 07 / 07.2, 07.4, 07.7 | Between-sample dynamics, continuum residuals, and closure stability need comparison to standard excitation propagation and sampling limits. |
| Paper 13 / 13.1 | Quark/color transport language needs guardrails against ordinary carrier/excitation analogies. |
| Paper 15 / 15.1 | Higgs/mass-residue language must be separated from ordinary effective mass, bound-state energy, and excitation gap language. |
| Paper 16 / 16.1 | Continuum edge residuals may be partly explained by ordinary band/defect/excitation behavior. |
| Paper 22 / 22.4 | Material-measurement validation is the strongest applied place to test exciton accounting. |

### Working Correspondence Table

| CQECMPLX term family | Standard-model candidate | Guard |
|----------------------|--------------------------|-------|
| correction residue / missing complement | hole or vacancy | do not identify unless charge, band, or occupancy model is specified |
| paired residue / Dust pair | electron-hole pair | exciton requires bound state and interaction energy |
| carried correction | carrier transport | distinguish symbolic carrier from physical charge carrier |
| recombination / closure | electron-hole recombination | require energy, photon/phonon, or relaxation channel |
| mass residue / bondedness | effective mass or binding energy | do not confuse with Higgs mass or rest mass |
| bridge threshold | band gap or activation threshold | require units and measured/material parameters |
| continuous field presentation | exciton wavefunction or density field | sample-preserving interpolation is not physical dynamics |

### Falsifiers

The study must reject an exciton explanation when:

- no electron/hole occupancy model is specified;
- no band structure or energy-gap condition is available;
- the alleged bound state has no interaction/binding term;
- recombination is claimed without an energy or relaxation channel;
- effective mass is confused with fundamental mass;
- a symbolic correction carrier is treated as a physical charge carrier without measurement.

### Expected Output

The finished paper should produce:

- a claim-by-claim accounting table;
- a citation spine for standard electron-hole-exciton theory;
- a list of claims downgraded to analogy;
- a list of claims fully explained by standard models;
- a remaining-residue list that genuinely requires CQECMPLX-specific receipts;
- verifier or data targets for material cases.

### Initial Source Spine

Use these as the first bibliography anchors:

| Source | Use |
|--------|-----|
| Böer and Pohl, "Excitons", Springer semiconductor reference entry, 2015. https://link.springer.com/rwe/10.1007/978-3-319-06540-3_14-1 | concise standard account of optical creation of electron-hole pairs, exciton binding, Wannier-Mott/Frenkel distinction, effective Rydberg, dielectric/effective-mass dependence |
| Fuchs, Rödl, Schleife, Bechstedt, "Efficient O(N^2) approach to solve the Bethe-Salpeter equation for excitonic bound states", Phys. Rev. B 78, 085103 / arXiv:0805.0659. https://arxiv.org/abs/0805.0659 | BSE as electron-hole Hamiltonian for excitonic bound states |
| Rohlfing and Louie, "Electron-Hole Excitations in Semiconductors and Insulators", Phys. Rev. Lett. 81, 2312, 1998. https://link.aps.org/doi/10.1103/PhysRevLett.81.2312 | first-principles electron-hole interaction and coupled excitations in periodic crystals |
| Onida, Reining, Rubio, "Electronic excitations: density-functional versus many-body Green's-function approaches", Rev. Mod. Phys. 74, 601, 2002. https://link.aps.org/doi/10.1103/RevModPhys.74.601 | broader many-body excitation framework and relation to TDDFT/GW/BSE |
| BSE+ 2D-materials preprint, 2026. https://arxiv.org/html/2606.09192v1 | current 2D/TMD context: BSE captures low-energy excitonic effects while high-energy transitions affect dielectric/plasmonic response |

### Conclusion

NP-12 is a discipline paper. Its job is to prevent novelty inflation. If
standard electron-hole-exciton theory already explains a bridge, the suite
should say so plainly and use the standard model as the base layer. Only the
unexplained residue should remain open CQECMPLX math.

## Appendix A. Source Integration Archive

This proposed study was created during the base-paper formalization pass after
the explicit user hypothesis that much of the open math may already be covered
by the electron-hole-exciton process in standard models. No source clips have
yet been integrated. The first source pass should read Papers 05, 07, 13, 15,
16, and 22, then add a bibliography-backed correspondence table.
