"""Generate the Standard Model Defining paper layer for the FLCR series.

This is a mechanical artifact generator for a new SMD-01..SMD-12 layer. The
generated papers define the external Standard Model and adjacent standard-model
interfaces before FLCR-31..40 translate those definitions into LCR language.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"D:/Paper Reworks/publication_series/Formalizing_LCR_Unifying_Standard_Models")
SMD_ROOT = ROOT / "standard_model_defining_papers"
FLAT_ROOT = Path(r"D:/Paper Reworks/FINAL_PAPERS_FLCR_UNIFIED")
FLAT_SMD_ROOT = FLAT_ROOT / "STANDARD_MODEL_DEFINING_PAPERS"

LANES = [
    "receipt_bound_internal_result",
    "standard_theorem_citation_bound_result",
    "cam_crystal_reapplication_result",
    "normal_form_result",
    "external_calibration_result",
    "grand_synthesis_claim",
    "falsifier_or_open_obligation",
]

COMMON_SOURCES = {
    "flcr": [
        "FLCR-01",
        "FLCR-12",
        "FLCR-14",
        "FLCR-31",
        "FLCR-32",
        "FLCR-33",
        "FLCR-34",
        "FLCR-35",
        "FLCR-36",
        "FLCR-37",
        "FLCR-38",
        "FLCR-39",
        "FLCR-40",
    ],
    "standards": [
        "D:/DockerContainers/Manny Docker Starter/mannyai/standards/corpus_conformance_report.json",
        "D:/DockerContainers/Manny Docker Starter/mannyai/standards/suite_resolution_report.json",
        "D:/DockerContainers/Manny Docker Starter/mannyai/standards/glue_report.json",
        "D:/DockerContainers/Manny Docker Starter/mannyai/brain/window_summary.json",
        "D:/Paper Reworks/publication_series/Formalizing_LCR_Unifying_Standard_Models/MANNYAI_STANDARDS_WINDOW_APPLICATION_PASS.json",
    ],
    "local_audits": [
        "NSIT_PAPER_EVIDENCE_INVENTORY.json",
        "NSIT_TOOL_CLOSURE_MATRIX.json",
        "NSIT_REASONED_CLOSURE_PASS.json",
        "ORBITAL_DATA_CROSS_POPULATION_AUDIT.json",
        "CAM_CLAIM_100_SCORE_AUDIT.json",
    ],
}

PAPERS = [
    {
        "id": "SMD-01",
        "title": "Standard Model Definition Contract And Evidence Boundary",
        "object": "definition contract",
        "summary": "Defines how external Standard Model content enters the FLCR series: by citation, equation, dataset, calibration rule, and falsifier.",
        "formalism": ["axiomatic field definitions", "claim-lane typing", "citation and calibration protocol"],
        "external_targets": ["Standard Model Lagrangian", "PDG-style parameter tables", "established QFT terminology"],
        "routes_to": ["FLCR-31", "FLCR-39", "FLCR-40"],
        "strong_claim": "A Standard Model claim can enter the FLCR series only when its field, symmetry, equation, parameter, source, and boundary are separately named.",
        "residue": "No LCR translation claim inherits physical validity merely because a Standard Model phrase appears in the source paper.",
    },
    {
        "id": "SMD-02",
        "title": "Gauge Principle, Connections, And Local Symmetry",
        "object": "gauge principle",
        "summary": "Defines local symmetry, gauge transformations, connections, curvature, covariant derivatives, and gauge-invariant observables.",
        "formalism": ["principal bundles", "connections", "curvature two-forms", "covariant derivatives"],
        "external_targets": ["Yang-Mills theory", "U(1), SU(2), SU(3) gauge transformations"],
        "routes_to": ["FLCR-31", "FLCR-35", "FLCR-40"],
        "strong_claim": "Gauge language may be translated into LCR only through an explicit map from local states and transport rules to connection, curvature, and invariant quantities.",
        "residue": "Measured coupling values, gauge fixing choices, and quantum corrections remain citation or calibration lanes.",
    },
    {
        "id": "SMD-03",
        "title": "Gauge Group SU3 SU2 U1 And Representation Content",
        "object": "gauge representation table",
        "summary": "Defines the Standard Model gauge group and the representation assignments that make particle labels mathematically meaningful.",
        "formalism": ["Lie groups", "Lie algebras", "representations", "charge assignments"],
        "external_targets": ["SU(3)xSU(2)xU(1)", "hypercharge", "color triplets", "weak doublets"],
        "routes_to": ["FLCR-31", "FLCR-32", "FLCR-33", "FLCR-40"],
        "strong_claim": "Particle-facing labels require representation rows, not analogies: every LCR face, color, or charge claim must name the corresponding representation field.",
        "residue": "An LCR finite symmetry can be structurally similar to a gauge representation without proving physical particle identity.",
    },
    {
        "id": "SMD-04",
        "title": "Fermion Fields, Generations, Flavor, And Mixing",
        "object": "fermion flavor sector",
        "summary": "Defines quark and lepton fields, generation structure, chirality, flavor mixing, CKM/PMNS matrices, and the data-binding boundary.",
        "formalism": ["spinor fields", "chiral representations", "unitary mixing matrices", "mass eigenstates"],
        "external_targets": ["quark generations", "lepton generations", "CKM", "PMNS"],
        "routes_to": ["FLCR-31", "FLCR-32", "FLCR-33", "FLCR-38", "FLCR-40"],
        "strong_claim": "Flavor and generation claims must distinguish structural indexing from measured mixing angles, phases, and masses.",
        "residue": "Numerical CKM/PMNS agreement is external calibration until the dataset, version, uncertainty, and comparison rule are attached.",
    },
    {
        "id": "SMD-05",
        "title": "QCD Color Dynamics And Hadronic Boundary",
        "object": "QCD color sector",
        "summary": "Defines color charge, gluon self-interaction, asymptotic freedom, confinement boundary language, hadronization, and lattice-QCD style evidence needs.",
        "formalism": ["non-Abelian gauge theory", "SU(3) color", "field strength tensors", "renormalization group"],
        "external_targets": ["QCD", "confinement", "hadrons", "lattice QCD"],
        "routes_to": ["FLCR-32", "FLCR-37", "FLCR-40"],
        "strong_claim": "QCD translation claims must separate finite color-face transport from physical confinement, scattering, and hadronic spectra.",
        "residue": "Confinement and hadron masses are not closed by face algebra alone; they require QCD evidence or calibration.",
    },
    {
        "id": "SMD-06",
        "title": "Electroweak Interaction And Symmetry Breaking",
        "object": "electroweak sector",
        "summary": "Defines SU(2)xU(1), weak isospin, hypercharge, W/Z/photon mixing, charged and neutral currents, and symmetry breaking boundaries.",
        "formalism": ["electroweak gauge theory", "spontaneous symmetry breaking", "current interactions", "mixing angles"],
        "external_targets": ["Glashow-Weinberg-Salam model", "weak currents", "Weinberg angle"],
        "routes_to": ["FLCR-31", "FLCR-33", "FLCR-40"],
        "strong_claim": "Electroweak claims require a bridge from LCR residue or sector accounting to SU(2)xU(1) fields, currents, and broken-phase observables.",
        "residue": "Measured weak parameters, decay rates, and precision electroweak fits remain external calibration lanes.",
    },
    {
        "id": "SMD-07",
        "title": "Higgs Sector, Vacuum Structure, And Mass Terms",
        "object": "Higgs and mass sector",
        "summary": "Defines scalar field content, potential, vacuum expectation value, Yukawa couplings, gauge-boson masses, fermion masses, and residue vocabulary boundaries.",
        "formalism": ["scalar fields", "potential minimization", "Yukawa terms", "mass matrices"],
        "external_targets": ["Higgs mechanism", "vacuum expectation value", "Yukawa sector"],
        "routes_to": ["FLCR-33", "FLCR-34", "FLCR-40"],
        "strong_claim": "Mass-residue translation is admissible only when it names whether the row is scalar-sector, Yukawa-sector, gauge-mass, or LCR bookkeeping.",
        "residue": "The observed Higgs mass and fermion masses require external parameter binding.",
    },
    {
        "id": "SMD-08",
        "title": "Renormalization, Effective Field Theory, And Running Parameters",
        "object": "scale and renormalization sector",
        "summary": "Defines renormalization, running couplings, cutoff/effective theory language, anomaly checks, and scale-dependent claim boundaries.",
        "formalism": ["renormalization group", "effective field theory", "regularization", "anomaly cancellation"],
        "external_targets": ["running couplings", "EFT matching", "anomalies"],
        "routes_to": ["FLCR-31", "FLCR-32", "FLCR-33", "FLCR-37", "FLCR-39", "FLCR-40"],
        "strong_claim": "Any claim that changes by scale must carry its scale, scheme, matching rule, and allowed error or falsifier.",
        "residue": "No zero-cost lookup is a substitute for specifying the renormalization or effective-model context.",
    },
    {
        "id": "SMD-09",
        "title": "Neutrino Sector, Oscillation Evidence, And Beyond-Minimal Residues",
        "object": "neutrino and open-residue sector",
        "summary": "Defines neutrino flavor/mass mismatch, oscillation evidence, PMNS parameters, and which neutrino facts are minimal Standard Model extensions.",
        "formalism": ["flavor states", "mass states", "oscillation probabilities", "matrix mixing"],
        "external_targets": ["neutrino oscillations", "PMNS matrix", "mass splittings"],
        "routes_to": ["FLCR-33", "FLCR-38", "FLCR-39", "FLCR-40"],
        "strong_claim": "Neutrino-facing LCR claims must declare whether they are minimal-SM, experimentally established extension, or speculative residue.",
        "residue": "Absolute mass scale, hierarchy, Majorana/Dirac status, and sterile sectors remain explicit external obligations.",
    },
    {
        "id": "SMD-10",
        "title": "Electron Hole Exciton And Condensed Matter Correspondence",
        "object": "electron-hole-exciton standard model",
        "summary": "Defines hole, vacancy, exciton, band structure, effective mass, screening, recombination, and material-model boundaries.",
        "formalism": ["band theory", "quasiparticles", "effective mass", "screening", "two-body bound states"],
        "external_targets": ["electron-hole pairs", "excitons", "semiconductor models", "material parameters"],
        "routes_to": ["FLCR-34", "FLCR-36", "FLCR-40"],
        "strong_claim": "Electron-hole-exciton language can explain LCR vacancy/residue analogs only when material model, band structure, and parameter boundary are stated.",
        "residue": "Quantitative exciton behavior is material-specific and remains data-bound.",
    },
    {
        "id": "SMD-11",
        "title": "GR Continuum Interface And Units-Bearing Calibration",
        "object": "continuum and gravitational interface",
        "summary": "Defines how Standard Model field claims meet spacetime, curvature, units, stress-energy, and GR/continuum calibration language.",
        "formalism": ["manifolds", "metric tensors", "stress-energy", "continuum limits", "units analysis"],
        "external_targets": ["general relativity interface", "continuum field limits", "calibration datasets"],
        "routes_to": ["FLCR-35", "FLCR-37", "FLCR-40"],
        "strong_claim": "Continuum and curvature translations require a sampling or limit rule plus units-bearing calibration before physical identity is claimed.",
        "residue": "Discrete repair, curvature analogy, and measured gravity claims remain separate lanes.",
    },
    {
        "id": "SMD-12",
        "title": "Standard Model Comparator And Falsifier Protocol",
        "object": "SM comparator protocol",
        "summary": "Defines the comparator table, falsifier rows, required citations, calibration tests, and dependency fields used before any FLCR synthesis claim is promoted.",
        "formalism": ["model comparison", "falsification protocol", "dependency graphs", "validation matrices"],
        "external_targets": ["PDG-like parameter checks", "benchmark calculations", "laboratory or simulation comparators"],
        "routes_to": ["FLCR-39", "FLCR-40"],
        "strong_claim": "A Standard Model synthesis claim is publishable only when the comparator row names source, equation, parameter, uncertainty, LCR mapping, and falsifier.",
        "residue": "A strong narrative correspondence remains an obligation if it lacks a comparator and falsifier row.",
    },
]


def slug(s: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in s).strip("-").replace("--", "-")


def yml_list(items: list[str], indent: int = 2) -> str:
    pad = " " * indent
    return "\n".join(f"{pad}- \"{item}\"" for item in items)


def formal(p: dict[str, object]) -> str:
    return f"""# {p['id']} - {p['title']}

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** formal paper source  
**Status:** first defining draft; final citations, equation numbering, and external references pending.  
**Claim posture:** define the external Standard Model object first; translate only through FLCR claim lanes.

## Abstract

{p['summary']} This paper exists before the corresponding LCR translation paper: it defines the accepted external object, its equations or formal structures, its evidence type, and the boundary that prevents analogy from becoming a physical claim. The operative object is **{p['object']}**. The strongest current result is: {p['strong_claim']}

## Keywords

Standard Model definition; {p['object']}; FLCR; claim lane; external calibration; falsifier.

## 1. Contribution And Scope

- Defines **{p['object']}** as a Standard Model-facing object that later FLCR papers may cite.
- Separates accepted external formalism from LCR interpretation and analogy.
- Assigns every import to a lane: citation-bound, calibration-bound, normal-form, receipt-bound, CAM/crystal, synthesis, or obligation.
- Routes the definition into: {', '.join(p['routes_to'])}.

This paper does not claim that LCR proves the Standard Model. It gives the FLCR suite a clean external reference surface so translation papers can say exactly what they are mapping to.

## 2. Source Routing

Primary FLCR consumers:

{chr(10).join(f'- `{r}`' for r in p['routes_to'])}

Common routed evidence:

- `CLAIM_LANE_SCHEMA.json`
- `MANNYAI_STANDARDS_WINDOW_APPLICATION_PASS.json`
- `NSIT_TOOL_CLOSURE_MATRIX.json`
- `NSIT_REASONED_CLOSURE_PASS.json`
- Kimi standards, glue, and window reports

## 3. Definitions And Notation

- **External definition.** A Standard Model or adjacent standard-physics object as it is used in established physics.
- **Translation target.** The exact field, symmetry, equation, parameter, dataset, or observable that an FLCR paper wants to map into LCR.
- **LCR mapping.** A later correspondence from an FLCR-native object to the external definition.
- **Calibration boundary.** The point at which structural similarity stops and measured physics begins.
- **Falsifier.** A condition, example, dataset, or derivation failure that blocks promotion.

## 4. Accepted External Formalism

The accepted formalism targets for this paper are:

{chr(10).join(f'- {x}' for x in p['formalism'])}

The external Standard Model or standard-physics targets are:

{chr(10).join(f'- {x}' for x in p['external_targets'])}

These targets must be expressed in final publication form with ordinary references, equation labels, and parameter/version information where relevant.

## 5. Formal Claims

| Claim | Lane | Statement |
|---|---|---|
| Theorem {p['id'][-2:]}.1 | `standard_theorem_citation_bound_result` | {p['strong_claim']} |
| Proposition {p['id'][-2:]}.2 | `normal_form_result` | This definition may be translated into LCR only by naming the object, mapping rule, scope boundary, and downstream FLCR paper. |
| Protocol {p['id'][-2:]}.3 | `falsifier_or_open_obligation` | {p['residue']} |

## 6. Construction Method

The construction has five steps:

1. State the accepted external object without LCR relabeling.
2. Identify the mathematical or physical fields that carry the object.
3. State the evidence type: theorem/citation, equation, dataset, calibration, simulation, or receipt.
4. Define the translation aperture used by later FLCR papers.
5. Preserve the falsifier and calibration boundary.

Safe use:

```text
external object -> cited formalism -> boundary -> FLCR mapping -> claim lane
```

Unsafe use:

```text
external word -> LCR identity claim
```

## 7. Standards And Window Binding

This paper inherits the 2026-06-28 standards-window authority rule:

- `corpus_conformance_report.json`: 32 canonical papers, 192/192 PASS.
- `suite_resolution_report.json`: 99 paper/items, 782 total rows, 776 resolved, 6 unresolved.
- `glue_report.json`: 95/95 obligations have continuation candidates.
- `window_summary.json`: 2/4/8/16/32 window hierarchy over papers 00-31.

Legacy verifier rows are evidence artifacts and obligation locators. They do not automatically define pass/fail status for this Standard Model definition layer.

## 8. Crosswalk To FLCR

| Destination | Required use |
|---|---|
{chr(10).join(f'| `{r}` | May cite this definition only with a lane, boundary, and comparator/falsifier row. |' for r in p['routes_to'])}

## 9. Limitations And Falsifiers

- {p['residue']}
- Missing citations block citation-bound claims.
- Missing parameters, units, uncertainty, or dataset version block calibration claims.
- A structural LCR match is not a measured Standard Model result until the external comparator passes.

## 10. Reproducibility And Citation Package

Final publication readiness requires:

- a short bibliography for the external formalism;
- equation labels for the defining Standard Model structures;
- a comparator row where measured quantities appear;
- a mapping table from this SMD paper to its FLCR consumers;
- a falsifier row for each promoted claim.

## 11. Conclusion

{p['id']} gives the FLCR suite a stable definition surface for **{p['object']}**. Later papers may translate this object into LCR only through explicit claim lanes, evidence boundaries, and falsifiers.
"""


def companion(p: dict[str, object]) -> str:
    return f"""# {p['id']} Companion - {p['title']}

## Plain-Language Thesis

This paper says what **{p['object']}** means before the LCR series tries to translate it. It keeps the external physics clean, named, and checkable.

## Why This Paper Exists

The FLCR translation papers should not have to define the Standard Model from scratch while also making LCR correspondences. This defining paper gives them a stable target.

## Why This State Happens Next

FLCR-01..30 build the LCR-native proof stack. FLCR-31..40 translate and synthesize. The SMD layer sits between those moves and prevents the translation band from drifting into analogy-only language.

## Author Interpretation

The author can relabel or reinterpret the external object inside LCR only after the external object has been stated in ordinary terms. The relabeling changes access path, not the outside definition.

## Strongest Claim

{p['strong_claim']}

## What This Does Not Claim

{p['residue']}

## Connections

Routes to: {', '.join(p['routes_to'])}.

## Reviewer Reading Path

Read the formal definitions first, then the crosswalk table, then the workbook comparator exercise. If a translation claim lacks a lane or falsifier, send it back to this paper as an obligation.
"""


def workbook(p: dict[str, object]) -> str:
    return f"""# {p['id']} Workbook - {p['title']}

## Evidence Checklist

- [ ] External object named: {p['object']}
- [ ] Accepted formalism listed.
- [ ] External target rows listed.
- [ ] FLCR consumer papers named.
- [ ] Claim lanes assigned.
- [ ] Falsifier row present.

## Receipt And Verifier Table

| Evidence item | Type | Status |
|---|---|---|
| External definition sources | citation-bound | pending final bibliography |
| FLCR claim-lane schema | internal protocol | present |
| MannyAI standards-window pass | CAM/standards evidence | present |
| Comparator/falsifier row | validation protocol | drafted |

## CAM/Crystal Query Patterns

Use these query templates when binding this paper into CAM:

```text
standard model {p['object']} definition
{p['id']} routes to {' '.join(p['routes_to'])}
external formalism {' '.join(p['formalism'])}
falsifier {p['residue']}
```

## Accepted-Math-To-LCR Correspondence Table

| External formalism | LCR translation aperture | Boundary |
|---|---|---|
{chr(10).join(f'| {x} | To be mapped only in the destination FLCR paper. | Citation/calibration boundary remains external. |' for x in p['formalism'])}

## Analog Exercises

1. Pick one external term from this paper.
2. State it without LCR language.
3. State the LCR analogy.
4. Name the evidence lane.
5. Name what would falsify the translation.

## Falsifier Exercises

- What data would refute the calibration claim?
- What missing citation blocks the definition?
- What LCR mapping would be only analogy and not physics?

## Build/Replay Instructions

1. Check this SMD paper before editing its FLCR consumers.
2. Add a comparator row for every measured or parameterized claim.
3. Route unresolved rows to FLCR-39 or FLCR-40 rather than hiding them.
"""


def manifest(p: dict[str, object]) -> str:
    return f"""publication_id: {p['id']}
title: "{p['title']}"
series: "Formalizing LCR, Unifying Standard Models"
layer: standard_model_defining_papers
status: first_defining_draft
object: "{p['object']}"
triad_role:
  formal: formal.md
  companion: companion.md
  workbook: workbook.md
claim_lanes:
{yml_list(LANES, 2)}
formal_claims:
  - id: "Theorem {p['id'][-2:]}.1"
    lane: "standard_theorem_citation_bound_result"
    statement: "{p['strong_claim']}"
  - id: "Proposition {p['id'][-2:]}.2"
    lane: "normal_form_result"
    statement: "This definition may be translated into LCR only by naming the object, mapping rule, scope boundary, and downstream FLCR paper."
  - id: "Protocol {p['id'][-2:]}.3"
    lane: "falsifier_or_open_obligation"
    statement: "{p['residue']}"
formalism_targets:
{yml_list(p['formalism'], 2)}
external_targets:
{yml_list(p['external_targets'], 2)}
routes_to:
{yml_list(p['routes_to'], 2)}
evidence_inputs:
{yml_list(COMMON_SOURCES['standards'] + COMMON_SOURCES['local_audits'], 2)}
publication_readiness:
  final_citations_required: true
  equation_numbering_required: true
  comparator_rows_required: true
  calibration_rows_required_when_measured: true
"""


def readme() -> str:
    rows = "\n".join(
        f"| `{p['id']}` | {p['title']} | {', '.join(p['routes_to'])} |"
        for p in PAPERS
    )
    return f"""# Standard Model Defining Papers

This directory defines the external Standard Model and adjacent standard-physics
objects used by FLCR-31 through FLCR-40.

The purpose is not to replace the existing FLCR translation papers. The purpose
is to give those papers clean external definition targets so a translation can
distinguish:

- accepted Standard Model formalism;
- LCR-native structure;
- analogy;
- citation-bound result;
- receipt-bound result;
- external calibration;
- falsifier or open obligation.

## Paper Map

| ID | Title | Routes to |
|---|---|---|
{rows}

## Method

Every SMD paper uses the same triad method as FLCR:

- `formal.md`: accepted formalism, claim lanes, boundaries, and crosswalks.
- `companion.md`: why the definition exists and how to read it.
- `workbook.md`: comparator, falsifier, CAM query, and replay exercises.
- `paper.yml`: source and lane manifest.

## Authority

The SMD layer inherits the 2026-06-28 MannyAI/Kimi standards-window rule:
standards reports define suite status; legacy verifier summaries are evidence
artifacts and obligation locators.
"""


def map_json() -> dict[str, object]:
    return {
        "schema": "flcr_standard_model_defining_papers.v1",
        "series": "Formalizing LCR, Unifying Standard Models",
        "layer": "standard_model_defining_papers",
        "paper_count": len(PAPERS),
        "purpose": "Define external Standard Model and adjacent standard-physics objects before FLCR translation and synthesis papers consume them.",
        "authority": "Same claim-lane, standards-window, open-obligation, and triad method used by FLCR-01..40.",
        "common_sources": COMMON_SOURCES,
        "papers": [
            {
                "publication_id": p["id"],
                "title": p["title"],
                "slug": slug(p["title"]),
                "object": p["object"],
                "routes_to": p["routes_to"],
                "formalism_targets": p["formalism"],
                "external_targets": p["external_targets"],
                "triad": {
                    "formal": f"{p['id']}/formal.md",
                    "companion": f"{p['id']}/companion.md",
                    "workbook": f"{p['id']}/workbook.md",
                    "manifest": f"{p['id']}/paper.yml",
                },
                "status": "first_defining_draft",
            }
            for p in PAPERS
        ],
    }


def main() -> None:
    SMD_ROOT.mkdir(parents=True, exist_ok=True)
    FLAT_SMD_ROOT.mkdir(parents=True, exist_ok=True)

    all_formal = ["# All Standard Model Defining Formal Papers\n"]
    for p in PAPERS:
        paper_dir = SMD_ROOT / p["id"]
        paper_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "formal.md": formal(p),
            "companion.md": companion(p),
            "workbook.md": workbook(p),
            "paper.yml": manifest(p),
        }
        for name, text in files.items():
            (paper_dir / name).write_text(text, encoding="utf-8")

        flat_prefix = f"{p['id']}__{slug(p['title']).replace('-', '_')}"
        (FLAT_SMD_ROOT / f"{flat_prefix}__formal.md").write_text(files["formal.md"], encoding="utf-8")
        (FLAT_SMD_ROOT / f"{flat_prefix}__companion.md").write_text(files["companion.md"], encoding="utf-8")
        (FLAT_SMD_ROOT / f"{flat_prefix}__workbook.md").write_text(files["workbook.md"], encoding="utf-8")
        (FLAT_SMD_ROOT / f"{flat_prefix}__paper.yml").write_text(files["paper.yml"], encoding="utf-8")
        all_formal.append("\n---\n")
        all_formal.append(files["formal.md"])

    smd_map = map_json()
    (SMD_ROOT / "README.md").write_text(readme(), encoding="utf-8")
    (SMD_ROOT / "STANDARD_MODEL_DEFINING_MAP.json").write_text(json.dumps(smd_map, indent=2), encoding="utf-8")
    (SMD_ROOT / "ALL_STANDARD_MODEL_DEFINING_FORMAL_PAPERS.md").write_text("\n".join(all_formal), encoding="utf-8")

    (FLAT_SMD_ROOT / "README.md").write_text(readme(), encoding="utf-8")
    (FLAT_SMD_ROOT / "STANDARD_MODEL_DEFINING_MAP.json").write_text(json.dumps(smd_map, indent=2), encoding="utf-8")
    (FLAT_SMD_ROOT / "ALL_STANDARD_MODEL_DEFINING_FORMAL_PAPERS.md").write_text("\n".join(all_formal), encoding="utf-8")

    print(f"Generated {len(PAPERS)} SMD papers in {SMD_ROOT}")
    print(f"Mirrored flat artifacts in {FLAT_SMD_ROOT}")


if __name__ == "__main__":
    main()
