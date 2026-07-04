"""Expand SMD papers and add the Standard Model closure bridge paper.

This pass makes the SMD layer richer by adding:
- IRL source registry with primary/reference URLs.
- equation/formalism blocks per SMD paper.
- closure-by-lane sections explaining what can be closed now.
- bridge paper explaining how FLCR stops treating everything as unsolved.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"D:/Paper Reworks/publication_series/Formalizing_LCR_Unifying_Standard_Models")
SMD_ROOT = ROOT / "standard_model_defining_papers"
FLAT_ROOT = Path(r"D:/Paper Reworks/FINAL_PAPERS_FLCR_UNIFIED")
FLAT_SMD_ROOT = FLAT_ROOT / "STANDARD_MODEL_DEFINING_PAPERS"

SOURCE_REGISTRY = [
    {
        "id": "IRL-PDG-2026",
        "title": "Particle Data Group Review of Particle Physics 2026",
        "url": "https://pdg.lbl.gov/",
        "use": "Particle properties, Standard Model reviews, summary tables, gauge boson/Higgs/lepton/quark data.",
        "lane": "standard_theorem_citation_bound_result",
    },
    {
        "id": "IRL-PDG-2024",
        "title": "Review of Particle Physics 2024/2025, Phys. Rev. D 110, 030001",
        "url": "https://link.aps.org/doi/10.1103/PhysRevD.110.030001",
        "use": "Stable citable PDG review for particle data and evaluated measurements.",
        "lane": "standard_theorem_citation_bound_result",
    },
    {
        "id": "IRL-CODATA-2022",
        "title": "NIST CODATA Recommended Values of the Fundamental Physical Constants: 2022",
        "url": "https://physics.nist.gov/cuu/pdf/wall_2022.pdf",
        "use": "Units-bearing constants and exact SI constants for calibration rows.",
        "lane": "external_calibration_result",
    },
    {
        "id": "IRL-ATLAS-HIGGS-2012",
        "title": "ATLAS observation of a new particle in the search for the Standard Model Higgs boson",
        "url": "https://arxiv.org/abs/1207.7214",
        "use": "Higgs discovery evidence and mass-scale calibration surface.",
        "lane": "external_calibration_result",
    },
    {
        "id": "IRL-CMS-HIGGS-2012",
        "title": "CMS observation of a new boson at a mass of 125 GeV",
        "url": "https://arxiv.org/abs/1207.7235",
        "use": "Independent Higgs discovery evidence and mass-scale calibration surface.",
        "lane": "external_calibration_result",
    },
    {
        "id": "IRL-NOBEL-NEUTRINO-2015",
        "title": "Nobel advanced information: Neutrino Oscillations",
        "url": "https://www.nobelprize.org/uploads/2017/09/advanced-physicsprize2015.pdf",
        "use": "Neutrino oscillation evidence and beyond-minimal Standard Model boundary.",
        "lane": "standard_theorem_citation_bound_result",
    },
    {
        "id": "IRL-NIST-CONSTANTS",
        "title": "NIST Fundamental Physical Constants extensive listing",
        "url": "https://physics.nist.gov/cuu/pdf/all.pdf",
        "use": "Numerical constants, units, and uncertainty metadata for calibration tables.",
        "lane": "external_calibration_result",
    },
    {
        "id": "IRL-EXCITON-SPRINGER",
        "title": "Excitons reference entry, Springer Nature",
        "url": "https://link.springer.com/rwe/10.1007/978-3-319-06540-3_14-1",
        "use": "Electron-hole, exciton, Wannier-Mott/Frenkel, binding-energy and dielectric/effective-mass formalism.",
        "lane": "standard_theorem_citation_bound_result",
    },
    {
        "id": "IRL-EXCITON-2D-REVIEW",
        "title": "Excitons in two-dimensional materials, arXiv:1911.00087",
        "url": "https://arxiv.org/pdf/1911.00087",
        "use": "Modern exciton review and material-dependent exciton evidence boundary.",
        "lane": "standard_theorem_citation_bound_result",
    },
]

SOURCES_BY_ID = {s["id"]: s for s in SOURCE_REGISTRY}

PAPERS = [
    {
        "id": "SMD-01",
        "title": "Standard Model Definition Contract And Evidence Boundary",
        "object": "definition contract",
        "routes_to": ["FLCR-31", "FLCR-39", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-CODATA-2022"],
        "core_formalism": [
            "External object O_ext must be named before any LCR object O_lcr is mapped to it.",
            "A mapping row has the form (O_ext, equation/source, O_lcr, lane, boundary, falsifier).",
            "A measured row additionally requires (dataset, units, uncertainty, version, pass/fail rule).",
        ],
        "closure_now": [
            "Close definition status when the external object, source, lane, and boundary are named.",
            "Close citation-bound use when PDG or another accepted reference supplies the field/parameter/definition.",
            "Close internal use when FLCR-01..40 supplies the receipt or normal-form dependency.",
        ],
        "still_open": [
            "Measured agreement remains open until a calibration row names values, units, uncertainty, and comparator.",
            "LCR identity claims remain open if only wording similarity is supplied.",
        ],
        "strong_claim": "A Standard Model claim can enter the FLCR series only when its field, symmetry, equation, parameter, source, and boundary are separately named.",
    },
    {
        "id": "SMD-02",
        "title": "Gauge Principle, Connections, And Local Symmetry",
        "object": "gauge principle",
        "routes_to": ["FLCR-31", "FLCR-35", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024"],
        "core_formalism": [
            "Gauge group G acts locally on fields psi(x): psi(x) -> U(x) psi(x).",
            "Covariant derivative: D_mu = partial_mu + i g A_mu, with representation-dependent generators.",
            "Field strength: F_mu_nu = partial_mu A_nu - partial_nu A_mu + i g [A_mu, A_nu].",
            "Gauge-invariant dynamics are built from contractions such as Tr(F_mu_nu F^mu_nu) and covariant matter terms.",
        ],
        "closure_now": [
            "Close the definition of gauge transport as local symmetry plus connection/covariant derivative.",
            "Close an LCR structural mapping only when it names the transported object, local action, invariant, and boundary.",
        ],
        "still_open": [
            "Physical gauge identity remains open without representation assignment, coupling, and standard citation.",
            "Measured coupling values require calibration rows.",
        ],
        "strong_claim": "Gauge language may be translated into LCR only through an explicit map from local states and transport rules to connection, curvature, and invariant quantities.",
    },
    {
        "id": "SMD-03",
        "title": "Gauge Group SU3 SU2 U1 And Representation Content",
        "object": "gauge representation table",
        "routes_to": ["FLCR-31", "FLCR-32", "FLCR-33", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024"],
        "core_formalism": [
            "Minimal Standard Model gauge group is SU(3)_C x SU(2)_L x U(1)_Y.",
            "Electric charge relation: Q = T3 + Y/2 in a common convention.",
            "Representation rows distinguish color triplets/singlets, weak doublets/singlets, and hypercharge assignments.",
            "A label such as color, weak, charge, or generation is meaningful only after its representation row is named.",
        ],
        "closure_now": [
            "Close structural representation claims when the group, representation, and transformation rule are stated.",
            "Close LCR face/color correspondence only at the structural level unless measured particle data are added.",
        ],
        "still_open": [
            "Particle identity remains open without field assignment and data/citation binding.",
            "Numerical parameter agreement is calibration-bound.",
        ],
        "strong_claim": "Particle-facing labels require representation rows, not analogies: every LCR face, color, or charge claim must name the corresponding representation field.",
    },
    {
        "id": "SMD-04",
        "title": "Fermion Fields, Generations, Flavor, And Mixing",
        "object": "fermion flavor sector",
        "routes_to": ["FLCR-31", "FLCR-32", "FLCR-33", "FLCR-38", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024"],
        "core_formalism": [
            "Fermions are organized by chirality, gauge representation, and generation.",
            "Flavor and mass bases are related by unitary mixing matrices.",
            "Quark charged-current mixing is summarized by the CKM matrix.",
            "Lepton/neutrino mixing is summarized by the PMNS matrix when neutrino masses are admitted.",
        ],
        "closure_now": [
            "Close generation indexing only as an indexing/representation statement.",
            "Close mixing formalism when a unitary matrix relation is stated and sourced.",
        ],
        "still_open": [
            "Numerical CKM/PMNS agreement is open until values, uncertainties, dataset version, and comparator are attached.",
            "A threefold LCR structure is not automatically a physical generation structure.",
        ],
        "strong_claim": "Flavor and generation claims must distinguish structural indexing from measured mixing angles, phases, and masses.",
    },
    {
        "id": "SMD-05",
        "title": "QCD Color Dynamics And Hadronic Boundary",
        "object": "QCD color sector",
        "routes_to": ["FLCR-32", "FLCR-37", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024"],
        "core_formalism": [
            "QCD is the SU(3)_C non-Abelian gauge sector.",
            "Gluon self-interaction enters through the non-Abelian commutator term in F_mu_nu.",
            "Running coupling and asymptotic freedom are scale-dependent QCD properties.",
            "Confinement and hadronization are physical/nonperturbative boundaries, not face-label identities.",
        ],
        "closure_now": [
            "Close structural color translation when finite face transport maps to SU(3)-type representation behavior with scope boundary.",
            "Close QCD definition by citation to established QCD/PDG material.",
        ],
        "still_open": [
            "Confinement, scattering, and hadron masses require QCD-specific evidence or calibration.",
            "Face algebra alone does not close hadronic physics.",
        ],
        "strong_claim": "QCD translation claims must separate finite color-face transport from physical confinement, scattering, and hadronic spectra.",
    },
    {
        "id": "SMD-06",
        "title": "Electroweak Interaction And Symmetry Breaking",
        "object": "electroweak sector",
        "routes_to": ["FLCR-31", "FLCR-33", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-ATLAS-HIGGS-2012", "IRL-CMS-HIGGS-2012"],
        "core_formalism": [
            "Electroweak gauge sector uses SU(2)_L x U(1)_Y.",
            "Charged and neutral currents distinguish W^+/W^- and Z/photon structures after mixing.",
            "Broken-phase observables depend on Higgs-sector vacuum structure and mixing parameters.",
            "Precision values require data-source, scheme, and uncertainty fields.",
        ],
        "closure_now": [
            "Close electroweak definition as the accepted SU(2)_L x U(1)_Y sector.",
            "Close structural translation only when field/current/mixing target is named.",
        ],
        "still_open": [
            "Decay rates, weak mixing angle, and precision fits require calibration data.",
            "LCR sector accounting does not by itself close electroweak phenomenology.",
        ],
        "strong_claim": "Electroweak claims require a bridge from LCR residue or sector accounting to SU(2)xU(1) fields, currents, and broken-phase observables.",
    },
    {
        "id": "SMD-07",
        "title": "Higgs Sector, Vacuum Structure, And Mass Terms",
        "object": "Higgs and mass sector",
        "routes_to": ["FLCR-33", "FLCR-34", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-ATLAS-HIGGS-2012", "IRL-CMS-HIGGS-2012"],
        "core_formalism": [
            "A schematic Higgs potential is V(phi) = -mu^2 phi^dagger phi + lambda (phi^dagger phi)^2.",
            "Vacuum expectation value and Yukawa couplings produce mass terms in the broken phase.",
            "Gauge boson and fermion mass claims are not the same type of claim as LCR residue accounting.",
            "Observed Higgs evidence is calibration-bound to collider data and evaluated particle properties.",
        ],
        "closure_now": [
            "Close Higgs-sector definition and the distinction between scalar, Yukawa, and gauge-mass rows.",
            "Close LCR mass-residue bookkeeping as internal structure when FLCR receipts are cited.",
        ],
        "still_open": [
            "Observed Higgs mass and coupling modifiers require external collider data.",
            "Mass residue is not a measured Higgs mechanism unless the bridge supplies data and equations.",
        ],
        "strong_claim": "Mass-residue translation is admissible only when it names whether the row is scalar-sector, Yukawa-sector, gauge-mass, or LCR bookkeeping.",
    },
    {
        "id": "SMD-08",
        "title": "Renormalization, Effective Field Theory, And Running Parameters",
        "object": "scale and renormalization sector",
        "routes_to": ["FLCR-31", "FLCR-32", "FLCR-33", "FLCR-37", "FLCR-39", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-CODATA-2022"],
        "core_formalism": [
            "A running parameter depends on scale and scheme, e.g. g = g(mu).",
            "Effective field theories require a cutoff or matching scale and a domain of validity.",
            "Anomaly and consistency checks are separate closure rows from phenomenological fit.",
            "Units-bearing comparisons require constants, units, uncertainty, and convention fields.",
        ],
        "closure_now": [
            "Close scale-dependence as a definition when scale, scheme, and domain are stated.",
            "Close zero-cost lookup only as an internal retrieval claim, not as a substitute for renormalization context.",
        ],
        "still_open": [
            "Running-coupling agreement remains open without scale/scheme/value/uncertainty.",
            "Cross-scale synthesis claims need matching rules.",
        ],
        "strong_claim": "Any claim that changes by scale must carry its scale, scheme, matching rule, and allowed error or falsifier.",
    },
    {
        "id": "SMD-09",
        "title": "Neutrino Sector, Oscillation Evidence, And Beyond-Minimal Residues",
        "object": "neutrino and open-residue sector",
        "routes_to": ["FLCR-33", "FLCR-38", "FLCR-39", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-NOBEL-NEUTRINO-2015"],
        "core_formalism": [
            "Neutrino oscillation requires flavor states and mass states not to be identical.",
            "Oscillation probabilities depend on mass-squared differences, mixing angles, baseline, and energy.",
            "The discovery of oscillations implies nonzero neutrino masses and therefore a beyond-minimal-SM boundary.",
            "Absolute mass scale, ordering, CP phase, and Majorana/Dirac status are distinct evidence rows.",
        ],
        "closure_now": [
            "Close the statement that oscillation evidence requires nonzero masses by citation.",
            "Close LCR observer/flavor analogy only as a mapping row until a neutrino model is attached.",
        ],
        "still_open": [
            "Absolute mass hierarchy and Majorana/Dirac status remain open or externally constrained.",
            "LCR observer decomposition does not by itself prove a neutrino-sector claim.",
        ],
        "strong_claim": "Neutrino-facing LCR claims must declare whether they are minimal-SM, experimentally established extension, or speculative residue.",
    },
    {
        "id": "SMD-10",
        "title": "Electron Hole Exciton And Condensed Matter Correspondence",
        "object": "electron-hole-exciton standard model",
        "routes_to": ["FLCR-34", "FLCR-36", "FLCR-40"],
        "sources": ["IRL-EXCITON-SPRINGER", "IRL-EXCITON-2D-REVIEW", "IRL-NIST-CONSTANTS"],
        "core_formalism": [
            "A hole is an unoccupied state in a filled band that behaves as a positive charge carrier in the effective theory.",
            "An exciton is an electron-hole bound state, often modeled with screened Coulomb interaction and effective masses.",
            "Reduced effective mass: 1/mu = 1/m_e^* + 1/m_h^*.",
            "Wannier-Mott/Frenkel distinctions depend on dielectric screening, effective mass, and localization scale.",
        ],
        "closure_now": [
            "Close the electron-hole-exciton vocabulary as a standard condensed-matter correspondence.",
            "Close LCR vacancy/residue analogy when it is explicitly declared as addressability/bookkeeping.",
        ],
        "still_open": [
            "Material-specific exciton binding, recombination, and transport require material parameters and data.",
            "A hole analogy does not prove a particle-physics hole or absence ontology beyond the model.",
        ],
        "strong_claim": "Electron-hole-exciton language can explain LCR vacancy/residue analogs only when material model, band structure, and parameter boundary are stated.",
    },
    {
        "id": "SMD-11",
        "title": "GR Continuum Interface And Units-Bearing Calibration",
        "object": "continuum and gravitational interface",
        "routes_to": ["FLCR-35", "FLCR-37", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-CODATA-2022", "IRL-NIST-CONSTANTS"],
        "core_formalism": [
            "Continuum field claims require a manifold/limit/sampling statement.",
            "GR-facing claims require metric, curvature, stress-energy, and units-bearing interpretation.",
            "Discrete repair curvature is a structural claim until a continuum limit and calibration are supplied.",
            "Units-bearing comparison requires constants, dimensions, and uncertainty.",
        ],
        "closure_now": [
            "Close the boundary between discrete structural curvature and continuum/GR curvature.",
            "Close internal repair-ledger claims when FLCR receipts are cited.",
        ],
        "still_open": [
            "Measured gravity, energy, or plasma claims require units and external data.",
            "No continuum identity follows from a discrete analogy alone.",
        ],
        "strong_claim": "Continuum and curvature translations require a sampling or limit rule plus units-bearing calibration before physical identity is claimed.",
    },
    {
        "id": "SMD-12",
        "title": "Standard Model Comparator And Falsifier Protocol",
        "object": "SM comparator protocol",
        "routes_to": ["FLCR-39", "FLCR-40"],
        "sources": ["IRL-PDG-2026", "IRL-PDG-2024", "IRL-CODATA-2022", "IRL-NIST-CONSTANTS"],
        "core_formalism": [
            "Comparator row: (claim, external object, LCR object, source, equation, parameter/data, uncertainty, pass/fail, falsifier).",
            "Closure row: (closed_by_citation | closed_by_receipt | closed_by_normal_form | closed_by_calibration | remains_obligation).",
            "Synthesis claims must list dependencies and unresolved rows.",
            "A claim without a falsifier is not publication-ready.",
        ],
        "closure_now": [
            "Close standards/comparator governance as a formal protocol.",
            "Close any claim whose lane has all required fields and no unresolved blocker.",
        ],
        "still_open": [
            "A claim with missing comparator/falsifier fields remains an obligation even if rhetorically strong.",
            "Grand synthesis remains blocked by any dependency that lacks its required lane evidence.",
        ],
        "strong_claim": "A Standard Model synthesis claim is publishable only when the comparator row names source, equation, parameter, uncertainty, LCR mapping, and falsifier.",
    },
]


def slug(s: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "-" for ch in s)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


def source_table(ids: list[str]) -> str:
    rows = []
    for sid in ids:
        s = SOURCES_BY_ID[sid]
        rows.append(f"| `{sid}` | {s['title']} | `{s['lane']}` | {s['url']} |")
    return "\n".join(rows)


def formal(p: dict[str, object]) -> str:
    source_ids = p["sources"]
    return f"""# {p['id']} - {p['title']}

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** formal paper source  
**Status:** expanded defining draft with IRL source registry; final equation/citation polishing pending.  
**Claim posture:** close what standard formalism and FLCR receipts can close; route remaining physical claims to calibration or falsifier lanes.

## Abstract

This paper defines **{p['object']}** as an external Standard Model or standard-physics object before any LCR translation is attempted. It binds accepted formalism, IRL sources, FLCR claim lanes, and falsifier boundaries. The strongest current claim is: {p['strong_claim']} The paper also identifies what can be treated as closed now and what remains data-bound, calibration-bound, or unresolved.

## Keywords

Standard Model definition; {p['object']}; FLCR; claim lane; calibration; falsifier; closure bridge.

## 1. Contribution And Scope

- Defines **{p['object']}** as an external target for later LCR translation.
- Imports IRL formalism by citation/source lane rather than by analogy.
- States which rows can be closed now using accepted formalism and FLCR-01..40 proof infrastructure.
- Routes unresolved or measured claims to explicit comparator, calibration, or falsifier rows.
- Routes this definition into: {', '.join(p['routes_to'])}.

This paper is a definition surface. It does not replace FLCR-31..40; it gives those papers the external object they must cite before making Standard Model-facing translation claims.

## 2. IRL Source Registry

| Source | Description | Lane | URL |
|---|---|---|---|
{source_table(source_ids)}

## 3. Definitions And Notation

- **External object.** The accepted physics object as used in the Standard Model or adjacent standard formalism.
- **LCR object.** The FLCR-native object to be mapped, usually a carrier, face, residue, window, receipt, or normal-form row.
- **Closure by formalism.** A row is closed because the external definition is standard and properly cited.
- **Closure by FLCR proof.** A row is closed because FLCR-01..40 supplies a receipt, finite enumeration, normal form, or standards result.
- **Closure by calibration.** A row is closed only after a dataset, value, unit, uncertainty, and comparator pass/fail criterion are attached.
- **Open obligation.** A row that lacks required lane fields. It is a next work item, not a rhetorical weakness.

## 4. Accepted Formalism

The formalism that this paper imports is:

{chr(10).join(f'- {x}' for x in p['core_formalism'])}

## 5. Formal Claims

| Claim | Lane | Statement |
|---|---|---|
| Theorem {p['id'][-2:]}.1 | `standard_theorem_citation_bound_result` | {p['strong_claim']} |
| Proposition {p['id'][-2:]}.2 | `normal_form_result` | This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named. |
| Protocol {p['id'][-2:]}.3 | `falsifier_or_open_obligation` | Claims outside the closure rows remain obligations until their missing citation, receipt, normal-form, or calibration field is supplied. |

## 6. What This Paper Closes Now

These rows can be treated as closed for publication routing:

{chr(10).join(f'- {x}' for x in p['closure_now'])}

The closure rule is conservative: a closed external definition does not automatically close a measured LCR-to-physics identity. It closes the definition target and permits later papers to ask a precise translation question.

## 7. What Remains Open Or Calibration-Bound

{chr(10).join(f'- {x}' for x in p['still_open'])}

## 8. Bridge To FLCR-01..40

The first forty FLCR papers provide the internal side of the bridge:

- FLCR-01 supplies the claim-lane and conservative-extension discipline.
- FLCR-02 through FLCR-18 supply LCR carrier, correction, atlas, repair, path, ledger, window, receipt, admission, CA, face algebra, curvature, residue, continuum, and exceptional machinery.
- FLCR-19 through FLCR-30 supply synthesis, applied forge readers, energetic/plasma/observer/game/Monster/CAM/runtime/cursor evidence.
- FLCR-31 through FLCR-40 consume this SMD definition layer for Standard Model translation and synthesis.

This paper therefore stops treating the relevant object as unsolved when one of the allowed closure paths is present:

```text
standard formalism + citation
or FLCR receipt/normal form
or CAM/crystal reapplication
or external calibration pass
```

Rows not satisfying one of those paths stay as obligations, but obligations now have named owners and lane requirements.

## 9. Crosswalk To Destination Papers

| Destination | Required use |
|---|---|
{chr(10).join(f'| `{r}` | Cite {p["id"]}, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |' for r in p['routes_to'])}

## 10. Comparator And Falsifier Template

| Field | Required value |
|---|---|
| External object | `{p['object']}` |
| External source | one or more rows from the IRL source registry |
| LCR object | named FLCR carrier/face/residue/window/receipt/normal form |
| Claim lane | one of the FLCR claim lanes |
| Closure route | citation, receipt, normal form, CAM/crystal reapplication, calibration, or obligation |
| Falsifier | missing source, failed comparator, incompatible mapping, or out-of-scope physical claim |

## 11. Conclusion

{p['id']} makes **{p['object']}** usable by the FLCR suite without blurring definition, analogy, proof, and calibration. It closes the rows that standard formalism or FLCR receipts can actually close, and it names the rows that still require data.
"""


def companion(p: dict[str, object]) -> str:
    return f"""# {p['id']} Companion - {p['title']}

## Plain-Language Thesis

This paper defines **{p['object']}** clearly enough that FLCR can stop treating it as a vague unresolved idea. Some parts are already standard physics. Some parts are already closed inside FLCR. The remaining parts need data, citations, or calibration.

## Why This Paper Exists

The translation papers need a clean target. If we skip this layer, every Standard Model word becomes a moving target and every strong claim looks open forever.

## What We Can Close Now

{chr(10).join(f'- {x}' for x in p['closure_now'])}

## What Still Needs Work

{chr(10).join(f'- {x}' for x in p['still_open'])}

## How To Read The Claim

Strong claim: {p['strong_claim']}

Routes to: {', '.join(p['routes_to'])}.

## Reviewer Rule

Do not ask whether the entire universe is solved by this paper. Ask which row is closed by standard formalism, which row is closed by FLCR proof, which row is calibration-bound, and which row remains an obligation.
"""


def workbook(p: dict[str, object]) -> str:
    return f"""# {p['id']} Workbook - {p['title']}

## Evidence Checklist

- [ ] External object named: {p['object']}
- [ ] IRL source rows attached.
- [ ] Accepted formalism listed.
- [ ] Closure-now rows identified.
- [ ] Open/calibration rows identified.
- [ ] Destination FLCR papers named.
- [ ] Comparator/falsifier row prepared.

## IRL Source Rows

| Source | Use |
|---|---|
{chr(10).join(f'| `{sid}` | {SOURCES_BY_ID[sid]["use"]} |' for sid in p['sources'])}

## CAM/Crystal Query Patterns

```text
{p['id']} {p['object']} source registry
{p['id']} closure now {' '.join(p['closure_now'])}
{p['id']} routes to {' '.join(p['routes_to'])}
{p['id']} falsifier {' '.join(p['still_open'])}
```

## Closure Exercise

For each claim in the destination FLCR paper:

1. Name the external object.
2. Name the FLCR object.
3. Pick the lane.
4. Decide closure route: citation, receipt, normal form, CAM, calibration, or obligation.
5. Write the falsifier.

## Comparator Template

| Claim | External object | FLCR object | Lane | Evidence | Pass/fail | Falsifier |
|---|---|---|---|---|---|---|
| pending | {p['object']} | pending | pending | pending | pending | pending |
"""


def manifest(p: dict[str, object]) -> str:
    return f"""publication_id: {p['id']}
title: "{p['title']}"
series: "Formalizing LCR, Unifying Standard Models"
layer: standard_model_defining_papers
status: expanded_defining_draft
object: "{p['object']}"
routes_to:
{chr(10).join(f'  - "{r}"' for r in p['routes_to'])}
irl_sources:
{chr(10).join(f'  - "{sid}"' for sid in p['sources'])}
closure_now:
{chr(10).join(f'  - "{x}"' for x in p['closure_now'])}
still_open:
{chr(10).join(f'  - "{x}"' for x in p['still_open'])}
formal_claims:
  - id: "Theorem {p['id'][-2:]}.1"
    lane: "standard_theorem_citation_bound_result"
    statement: "{p['strong_claim']}"
  - id: "Proposition {p['id'][-2:]}.2"
    lane: "normal_form_result"
    statement: "This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named."
  - id: "Protocol {p['id'][-2:]}.3"
    lane: "falsifier_or_open_obligation"
    statement: "Claims outside the closure rows remain obligations until their missing citation, receipt, normal-form, or calibration field is supplied."
"""


BRIDGE_ID = "SMB-01"
BRIDGE_TITLE = "Standard Model Closure Bridge From Definition To FLCR Synthesis"


def bridge_formal() -> str:
    rows = "\n".join(
        f"| `{p['id']}` | {p['title']} | {', '.join(p['routes_to'])} |" for p in PAPERS
    )
    src_rows = "\n".join(
        f"| `{s['id']}` | {s['title']} | `{s['lane']}` | {s['url']} |" for s in SOURCE_REGISTRY
    )
    return f"""# {BRIDGE_ID} - {BRIDGE_TITLE}

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** bridge formal paper source  
**Status:** first bridge draft; final citations and equations pending.  
**Claim posture:** stop treating every Standard Model-facing row as unresolved; close rows whose required evidence already exists.

## Abstract

This bridge paper defines the transition from open-ended interpretation to closure-by-lane. The first forty FLCR papers build the LCR proof stack: carrier, correction, atlas, repair, ledger, receipts, admission, face algebra, curvature, residue, continuum, exceptional machinery, applied forges, CAM/crystal runtime, standards, and synthesis. The SMD papers define the external Standard Model and adjacent physics objects. From this point forward, a claim is not left open merely because it is large. It is evaluated by whether its lane requirements are present. Standard formalism, FLCR receipts, CAM/crystal reapplication, normal-form translation, external calibration, and falsifier rows together decide how much is solved now.

## Keywords

Standard Model bridge; FLCR; closure by lane; evidence boundary; synthesis; falsifier.

## 1. Thesis

The FLCR series should stop treating all Standard Model-facing claims as generically unsolved. Instead, each row is assigned one of five closure states:

1. **closed by standard formalism** when the external object is already established and cited;
2. **closed by FLCR proof** when FLCR-01..40 supplies a receipt, finite enumeration, normal form, or standards result;
3. **closed by CAM/crystal reapplication** when a routed standards/window/CAM artifact supplies the dependency;
4. **closed by external calibration** when data, units, uncertainty, and comparator pass;
5. **open obligation** when a required field is missing.

This is the bridge from "everything is open" to "the row says exactly what is solved and why."

## 2. Source Registry

| Source | Description | Lane | URL |
|---|---|---|---|
{src_rows}

## 3. SMD Definition Layer

| Paper | Definition surface | Routes to |
|---|---|---|
{rows}

## 4. FLCR Proof Stack Consumed By This Bridge

| FLCR band | What it contributes to closure |
|---|---|
| `FLCR-01..10` | claim-lane discipline, LCR carrier, correction, D4/J3/triality, repair, path, ledger, bridge, lattice closure, temporal windows |
| `FLCR-11..20` | receipts, admission, CA prediction, face algebra, curvature, mass residue, continuum edge, exceptional/VOA/observer machinery, synthesis ledger |
| `FLCR-21..30` | applied forge readers, materials/protein/game/energy/plasma/observer/Monster/CAM/runtime/cursor evidence |
| `FLCR-31..40` | Standard Model translation, evidence standards, and dependency-explicit grand synthesis |

## 5. Closure Rule

For every Standard Model-facing claim, fill this row:

```text
claim -> SMD definition -> FLCR dependency -> lane -> evidence -> boundary -> falsifier
```

Then classify:

| Classification | Required evidence |
|---|---|
| closed by standard formalism | SMD source row and accepted equation/definition |
| closed by FLCR proof | FLCR paper, receipt, finite proof, normal form, or standards result |
| closed by CAM/crystal reapplication | CAM/window/glue/standards source and routing path |
| closed by calibration | dataset, unit, uncertainty, comparator, pass/fail criterion |
| open obligation | named missing field and owner |

## 6. Immediate Rows We Can Stop Calling Unsolved

These are not final grand-unification claims. They are rows that can be closed now at their correct scope:

| Row | Closure |
|---|---|
| Standard Model gauge group exists as an external definition target | closed by SMD-03 and PDG-style citation |
| Gauge transport as local symmetry/connection formalism | closed by SMD-02 as external formalism |
| QCD color as SU(3)_C formalism | closed by SMD-05 as external formalism; LCR face transport remains a separate mapping row |
| Higgs discovery as an IRL observed boson near 125 GeV | closed as external calibration source by ATLAS/CMS/PDG rows; LCR mass-residue identity remains mapping/calibration-bound |
| Neutrino oscillation implies beyond-minimal-SM mass residue | closed by SMD-09 citation row; LCR observer/flavor mapping remains a normal-form question |
| Electron-hole-exciton vocabulary | closed by SMD-10 as condensed-matter formalism; quantitative material behavior remains data-bound |
| FLCR standards conformance for canonical 32-paper corpus | closed by MannyAI standards report: 192/192 PASS |
| Obligation routing availability | closed by glue report: 95/95 obligations have candidates |
| Larger paper-window review path | closed by window summary: 2/4/8/16/32 hierarchy |

## 7. Rows Still Not Closed By This Bridge

- Measured equality between an LCR-derived value and a Standard Model parameter without a comparator.
- Physical identity of an LCR carrier with a particle, field, or force without representation, equation, data, and falsifier.
- Grand unification as a single final physical theorem until every dependency row is either closed or named as an obligation.
- Material, plasma, GR, and exciton quantitative predictions without units, model parameters, and datasets.

## 8. Downstream Use

FLCR-31 through FLCR-40 must cite the relevant SMD paper before using Standard Model-facing terms. FLCR-40 must cite this bridge when it turns multiple closed rows into synthesis claims.

## 9. Conclusion

This bridge paper is the publication switch: the corpus no longer says "open" by default. It asks what kind of evidence a row needs, checks whether that evidence already exists in standard physics or FLCR-01..40, and closes as much as the lane allows.
"""


def bridge_companion() -> str:
    return f"""# {BRIDGE_ID} Companion - {BRIDGE_TITLE}

## Plain-Language Thesis

This is the paper that changes the working mode. We stop treating every large claim as unsolved just because it touches the Standard Model. Some parts are standard physics already. Some parts are proven inside FLCR already. Some parts need calibration. The row itself tells us which is which.

## Why This Bridge Exists

Without this bridge, the series keeps carrying all claims as open. With this bridge, each claim gets a lane and a closure test.

## What It Lets Us Do

- Use Standard Model definitions as real external facts.
- Use FLCR receipts and normal forms as real internal facts.
- Use CAM/window/glue reports as routing evidence.
- Keep measured physics honest by requiring datasets, units, uncertainties, and falsifiers.

## Strongest Claim

The strongest claim is not "everything is solved." The strongest claim is better: every row now has a closure procedure, and many rows close immediately at their correct scope.
"""


def bridge_workbook() -> str:
    return f"""# {BRIDGE_ID} Workbook - {BRIDGE_TITLE}

## Closure Worksheet

For each Standard Model-facing claim:

| Field | Fill |
|---|---|
| Claim | pending |
| SMD definition | pending |
| FLCR dependency | pending |
| Lane | pending |
| Evidence | pending |
| Boundary | pending |
| Falsifier | pending |
| Closure state | closed by standard formalism / FLCR proof / CAM / calibration / obligation |

## Exercises

1. Take a claim from FLCR-32 about QCD color. Route it through SMD-05.
2. Take a claim from FLCR-33 about mass residue. Route it through SMD-07.
3. Take a claim from FLCR-34 about holes/excitons. Route it through SMD-10.
4. Take a claim from FLCR-40 and list every dependency row.
"""


def bridge_manifest() -> str:
    return f"""publication_id: {BRIDGE_ID}
title: "{BRIDGE_TITLE}"
series: "Formalizing LCR, Unifying Standard Models"
layer: standard_model_defining_papers
status: first_bridge_draft
routes_to:
  - "FLCR-31"
  - "FLCR-32"
  - "FLCR-33"
  - "FLCR-34"
  - "FLCR-35"
  - "FLCR-36"
  - "FLCR-37"
  - "FLCR-38"
  - "FLCR-39"
  - "FLCR-40"
claim_lanes:
  - "standard_theorem_citation_bound_result"
  - "receipt_bound_internal_result"
  - "cam_crystal_reapplication_result"
  - "normal_form_result"
  - "external_calibration_result"
  - "grand_synthesis_claim"
  - "falsifier_or_open_obligation"
formal_claims:
  - id: "Theorem SMB.1"
    lane: "grand_synthesis_claim"
    statement: "The FLCR Standard Model band should close claims by lane rather than treating all large claims as unresolved."
  - id: "Protocol SMB.2"
    lane: "falsifier_or_open_obligation"
    statement: "A row remains open only when a required citation, receipt, normal form, CAM route, calibration, or falsifier field is missing."
"""


def write_paper(base: Path, pid: str, title: str, formal_text: str, companion_text: str, workbook_text: str, yml_text: str) -> None:
    d = base / pid
    d.mkdir(parents=True, exist_ok=True)
    (d / "formal.md").write_text(formal_text, encoding="utf-8")
    (d / "companion.md").write_text(companion_text, encoding="utf-8")
    (d / "workbook.md").write_text(workbook_text, encoding="utf-8")
    (d / "paper.yml").write_text(yml_text, encoding="utf-8")

    prefix = f"{pid}__{slug(title).replace('-', '_')}"
    (FLAT_SMD_ROOT / f"{prefix}__formal.md").write_text(formal_text, encoding="utf-8")
    (FLAT_SMD_ROOT / f"{prefix}__companion.md").write_text(companion_text, encoding="utf-8")
    (FLAT_SMD_ROOT / f"{prefix}__workbook.md").write_text(workbook_text, encoding="utf-8")
    (FLAT_SMD_ROOT / f"{prefix}__paper.yml").write_text(yml_text, encoding="utf-8")


def readme() -> str:
    rows = "\n".join(f"| `{p['id']}` | {p['title']} | {', '.join(p['routes_to'])} |" for p in PAPERS)
    return f"""# Standard Model Defining Papers

This directory defines the external Standard Model and adjacent standard-physics
objects used by FLCR-31 through FLCR-40.

The layer now includes a bridge paper:

- `{BRIDGE_ID}` - {BRIDGE_TITLE}

The bridge paper explains the change in method: the series stops treating every
large Standard Model-facing row as unresolved and instead closes each row by the
evidence lane it actually satisfies.

## Paper Map

| ID | Title | Routes to |
|---|---|---|
{rows}
| `{BRIDGE_ID}` | {BRIDGE_TITLE} | FLCR-31 through FLCR-40 |

## IRL Source Registry

See `IRL_STANDARD_MODEL_SOURCE_REGISTRY.md/json`.
"""


def source_registry_md() -> str:
    rows = "\n".join(f"| `{s['id']}` | {s['title']} | `{s['lane']}` | {s['url']} | {s['use']} |" for s in SOURCE_REGISTRY)
    return f"""# IRL Standard Model Source Registry

These sources are the first-pass IRL source registry for the Standard Model
Defining layer. They are used to close definition rows, citation-bound rows, and
calibration-bound rows where appropriate.

| ID | Source | Lane | URL | Use |
|---|---|---|---|---|
{rows}
"""


def main() -> None:
    SMD_ROOT.mkdir(parents=True, exist_ok=True)
    FLAT_SMD_ROOT.mkdir(parents=True, exist_ok=True)

    all_formal = ["# All Standard Model Defining Formal Papers\n"]
    for p in PAPERS:
        f = formal(p)
        c = companion(p)
        w = workbook(p)
        y = manifest(p)
        write_paper(SMD_ROOT, p["id"], p["title"], f, c, w, y)
        all_formal.append("\n---\n")
        all_formal.append(f)

    bf = bridge_formal()
    bc = bridge_companion()
    bw = bridge_workbook()
    by = bridge_manifest()
    write_paper(SMD_ROOT, BRIDGE_ID, BRIDGE_TITLE, bf, bc, bw, by)
    all_formal.append("\n---\n")
    all_formal.append(bf)

    registry = {
        "schema": "flcr_irl_standard_model_source_registry.v1",
        "date": "2026-06-28",
        "sources": SOURCE_REGISTRY,
    }
    smd_map = {
        "schema": "flcr_standard_model_defining_papers.v2",
        "series": "Formalizing LCR, Unifying Standard Models",
        "layer": "standard_model_defining_papers",
        "paper_count": len(PAPERS),
        "bridge_paper": BRIDGE_ID,
        "total_with_bridge": len(PAPERS) + 1,
        "purpose": "Define external Standard Model objects and bridge them to FLCR closure-by-lane.",
        "papers": [
            {
                "publication_id": p["id"],
                "title": p["title"],
                "object": p["object"],
                "routes_to": p["routes_to"],
                "irl_sources": p["sources"],
                "status": "expanded_defining_draft",
            }
            for p in PAPERS
        ],
    }

    for base in (SMD_ROOT, FLAT_SMD_ROOT):
        (base / "README.md").write_text(readme(), encoding="utf-8")
        (base / "IRL_STANDARD_MODEL_SOURCE_REGISTRY.md").write_text(source_registry_md(), encoding="utf-8")
        (base / "IRL_STANDARD_MODEL_SOURCE_REGISTRY.json").write_text(json.dumps(registry, indent=2), encoding="utf-8")
        (base / "STANDARD_MODEL_DEFINING_MAP.json").write_text(json.dumps(smd_map, indent=2), encoding="utf-8")
        (base / "ALL_STANDARD_MODEL_DEFINING_FORMAL_PAPERS.md").write_text("\n".join(all_formal), encoding="utf-8")

    print(f"Expanded {len(PAPERS)} SMD papers plus {BRIDGE_ID}")


if __name__ == "__main__":
    main()
