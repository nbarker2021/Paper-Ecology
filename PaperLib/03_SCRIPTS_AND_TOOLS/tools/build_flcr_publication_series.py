"""Build the FLCR publication-series blueprint and triad skeletons.

The series root is:
    D:/Paper Reworks/publication_series/Formalizing_LCR_Unifying_Standard_Models

This is a milestone-1/2 scaffold:
  * machine-readable 40-paper map;
  * claim-lane schema;
  * source-routing matrix;
  * triad templates;
  * 40 paper folders with formal/companion/workbook/manifest/tex/pdf skeletons.

The generated PDFs are deliberately minimal placeholder PDFs because this
environment does not provide a LaTeX engine. The build protocol records the
final arXiv-style PDF pass as a later toolchain step.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
SERIES_ROOT = ROOT / "publication_series" / "Formalizing_LCR_Unifying_Standard_Models"


CLAIM_LANES = [
    {
        "id": "receipt_bound_internal_result",
        "name": "Receipt-bound internal result",
        "description": "Executable or enumerated result with named verifier/receipt inside the corpus.",
        "requires": ["claim_text", "scope_boundary", "receipt_or_validator", "falsifier"],
    },
    {
        "id": "standard_theorem_citation_bound_result",
        "name": "Standard theorem / citation-bound result",
        "description": "Result imported from established mathematics, physics, CS, or formal methods.",
        "requires": ["claim_text", "object_mapping", "citation_or_theorem", "scope_boundary"],
    },
    {
        "id": "cam_crystal_reapplication_result",
        "name": "CAM/crystal reapplication result",
        "description": "Result obtained by applying Claude/Kimi/MannyAI CAM, crystal, node, or window data.",
        "requires": ["claim_text", "cam_source", "routing_path", "attached_data", "scope_boundary"],
    },
    {
        "id": "normal_form_result",
        "name": "Normal-form result",
        "description": "Result expressed through LCR/J3(O)/Rule30/algebraic/canonical normal form.",
        "requires": ["claim_text", "normal_form_definition", "conversion_rule", "receipt_or_pending_gate"],
    },
    {
        "id": "external_calibration_result",
        "name": "External calibration result",
        "description": "Claim requiring measured data, benchmark data, lab result, PDG/material/PDB source, or external comparator.",
        "requires": ["claim_text", "external_dataset", "calibration_protocol", "pass_fail_criteria"],
    },
    {
        "id": "grand_synthesis_claim",
        "name": "Grand synthesis claim",
        "description": "Cross-paper unification claim depending on multiple prior lanes and explicit dependencies.",
        "requires": ["claim_text", "dependency_papers", "dependency_lanes", "falsifier", "residual_obligations"],
    },
    {
        "id": "falsifier_or_open_obligation",
        "name": "Falsifier / open obligation",
        "description": "Explicit limitation, counterexample, missing proof, missing data, or required next test.",
        "requires": ["claim_text", "why_not_closed", "next_binding_action", "owner"],
    },
]


COMMON_SOURCES = {
    "audits": [
        "NSIT_PAPER_EVIDENCE_INVENTORY.json",
        "ORBITAL_DATA_CROSS_POPULATION_AUDIT.json",
        "AGENT_CRYSTAL_WORK_HARVEST.json",
        "NSIT_REASONED_CLOSURE_PASS.json",
        "NSIT_TOOL_CLOSURE_MATRIX.json",
        "CAM_CLAIM_100_SCORE_AUDIT.json",
    ],
    "supplements": [
        "supplements/SUPPLEMENT_INDEX.md",
        "supplements/INTERNAL_REASONING_PYRAMID_INDEX.md",
        "supplements/RECEIPT_VERIFIER_CATALOG.md",
        "supplements/LATTICE_FORGE_UNIFICATION_SUPPLEMENT.md",
        "supplements/CRYSTAL_CAM_PROJECTOR_SUPPLEMENT.md",
        "supplements/APPLIED_FORGES_WORKBOOK.md",
    ],
    "kimi": [
        r"D:\DockerContainers\Manny Docker Starter\mannyai\standards\corpus_conformance_report.json",
        r"D:\DockerContainers\Manny Docker Starter\mannyai\standards\suite_resolution_report.json",
        r"D:\DockerContainers\Manny Docker Starter\mannyai\standards\glue_report.json",
        r"D:\DockerContainers\Manny Docker Starter\mannyai\brain\window_summary.json",
        r"D:\DockerContainers\Manny Docker Starter\mannyai\papers\nodes",
        r"D:\DockerContainers\Manny Docker Starter\database\nodes",
        r"D:\DockerContainers\Manny Docker Starter\database\windows",
    ],
    "downloads": [
        r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\NOTEBOOKLM_REVIEW_PROMPTS.md",
        r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\SERIES_INDEX.csv",
        r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\CAM_ADDRESS_GRAMMAR.md",
        r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\MannyAI_Unified_Crystal_Manifest_v0.yaml",
        r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\ANALOG_WORKBOOK_ASSEMBLY.json",
        r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\asset_mesh_manifest.json",
    ],
}


PAPERS = [
    ("FLCR-01", "Grounding Contract And Axiom Discipline", "lcr_native", ["00"], "Establishes the burden contract, only-addition rule, and claim-lane discipline."),
    ("FLCR-02", "The LCR Carrier", "lcr_native", ["01"], "Defines the L/C/R carrier as the first active state surface."),
    ("FLCR-03", "Correction Surface And Residual Accounting", "lcr_native", ["02"], "Formalizes Rule30 correction, residuals, and repairable mismatch."),
    ("FLCR-04", "D4, J3(O), Triality, And Representation Transport", "lcr_native", ["03"], "Places representation changes into finite chart and J3(O) transport discipline."),
    ("FLCR-05", "Typed Boundary Repair", "lcr_native", ["04"], "Turns failed joins and boundary mismatches into typed repair data."),
    ("FLCR-06", "Oloid Path Carrier And Transport Geometry", "lcr_native", ["05"], "Defines curved/path transport without importing physical calibration language."),
    ("FLCR-07", "Causal Links And Obligation Ledgers", "lcr_native", ["06"], "Makes dependencies, receipts, and open obligations formal corpus objects."),
    ("FLCR-08", "Discrete-Continuous Bridge Without Physical Overclaim", "lcr_native", ["07"], "Defines presentation bridges, sampling obligations, and continuum guards."),
    ("FLCR-09", "Lattice Closure And Terminal Addresses", "lcr_native", ["08"], "Binds code/lattice ladders, no-cost lookup surfaces, and invariant boundaries."),
    ("FLCR-10", "Temporal Windows And Hamiltonian Readouts", "lcr_native", ["09"], "Defines temporal windowing over transported centers."),
    ("FLCR-11", "Master Receipt And Stack Replay", "lcr_native", ["10"], "Turns stack-level replay, import, and receipt discipline into a formal result."),
    ("FLCR-12", "Theory Admission Gates", "lcr_native", ["11"], "Defines admission, rejection, and no-silent-extension gates."),
    ("FLCR-13", "Cellular Automata Prediction Surfaces", "lcr_native", ["12"], "Separates finite CA verification from unbounded Rule30 extraction claims."),
    ("FLCR-14", "Quark-Face Algebra Before Standard-Model Translation", "lcr_native", ["13"], "Keeps SU(3)/face transport algebraic before later measured-physics translation."),
    ("FLCR-15", "Curvature As Boundary-Repair Demand", "lcr_native", ["14"], "Defines curvature vocabulary internally as repair pressure and route status."),
    ("FLCR-16", "Mass Residue And Carrier Accounting", "lcr_native", ["15"], "Formalizes finite mass-residue carrier language without measured Higgs claims."),
    ("FLCR-17", "Continuum Edge Residuals", "lcr_native", ["16"], "Treats continuum edge behavior as sampled residual and numerical-analysis burden."),
    ("FLCR-18", "Exceptional Towers, VOA Routes, And Observer Face Selection", "lcr_native", ["17", "18", "19"], "Combines E6/E8 tower scope, VOA finite seed scope, and observer-face selection."),
    ("FLCR-19", "Layer-2 Synthesis Ledger", "lcr_native", ["20"], "Aggregates prior layers while preserving unknown, forbidden, and deferred rows."),
    ("FLCR-20", "Applied Forge Reader And Descriptor Kernel", "lcr_native", ["21"], "Defines the shared applied-forge reader before domain validation."),
    ("FLCR-21", "Materials Candidate Generation", "lcr_native", ["22"], "Keeps material candidate generation separate from fabrication performance claims."),
    ("FLCR-22", "Protein Descriptor And Fold-Facing Kernel", "lcr_native", ["23"], "Defines protein descriptor routing and benchmark obligations."),
    ("FLCR-23", "Finite Game Lattices And Local Rule Automata", "lcr_native", ["24", "28"], "Combines board/game finite-rule surfaces and bounded search claims."),
    ("FLCR-24", "Energetic Traversal Maps", "lcr_native", ["25"], "Defines internal normalized energy/action accounting and unit-calibration gates."),
    ("FLCR-25", "Shear, Plasma, And Carrier Horizons", "lcr_native", ["26"], "Separates carrier/shear algebra from measured plasma claims."),
    ("FLCR-26", "Observer Delay And Shared-State Protocols", "lcr_native", ["27"], "Defines finite observer-delay protocols and interpretation guards."),
    ("FLCR-27", "Monster Ceiling And Large-Invariant Boundaries", "lcr_native", ["29"], "Separates finite identities and lookup surfaces from invariant/witness burdens."),
    ("FLCR-28", "CAM, Crystal Projectors, And MannyAI Runtime", "lcr_native", [], "Formalizes CAM/crystal projector architecture, MannyAI task crystals, and agent evidence."),
    ("FLCR-29", "Corpus Ribbon And Retrospective LCR Readout", "lcr_native", ["30", "31"], "Turns corpus ribbon storage and retrospective readout into publication infrastructure."),
    ("FLCR-30", "Supervisor Cursor And Universal Normal-Form Intake", "lcr_native", ["32"], "Schedules the corpus, Kimi windows, and incoming universal normal-form work."),
    ("FLCR-31", "Gauge Groups Translated Into LCR", "standard_model_translation", ["13"], "Translates gauge-group language into mature LCR-native terms."),
    ("FLCR-32", "QCD And Color Transport In LCR", "standard_model_translation", ["13"], "Maps QCD/color transport after algebraic face transport is established."),
    ("FLCR-33", "Electroweak, Higgs, And Mass Residue Translation", "standard_model_translation", ["15"], "Maps electroweak/Higgs language onto residue/carrier structures."),
    ("FLCR-34", "Electron-Hole-Exciton Accounting", "standard_model_translation", [], "Asks how much open CQE math is standard electron-hole-exciton formalism."),
    ("FLCR-35", "GR, Curvature, And Continuum Translation", "standard_model_translation", ["14", "16"], "Translates GR/continuum language through repair and sampling gates."),
    ("FLCR-36", "Condensed Matter, Materials, And Metamaterials", "standard_model_translation", ["22"], "Maps materials and condensed-matter claims through calibration protocols."),
    ("FLCR-37", "Plasma, Energy, And Traversal Calibration", "standard_model_translation", ["25", "26", "29"], "Maps plasma/energy claims to unit, witness, and calibration requirements."),
    ("FLCR-38", "Observer, Computation, And AI Runtime Translation", "standard_model_translation", ["19", "27", "28", "30", "31"], "Connects observer protocols, computation, AI, and crystal-runtime evidence."),
    ("FLCR-39", "Falsifiers, Comparators, And Standards Of Evidence", "standard_model_translation", ["06", "10", "11", "20", "32"], "Consolidates falsifier, comparator, and standards-board evidence."),
    ("FLCR-40", "Grand Unification In LCR Normal Form", "grand_unification", [], "States the integrated unification claims with dependencies, normal forms, receipts, and falsifiers."),
]


LEGACY_FILE_MAP = {
    "00": "00_Established_Grounding_and_Axiom_Contract.md",
    "01": "01_LCR_Chain_Carrier.md",
    "02": "02_Correction_Surface.md",
    "03": "03_D4_J3_Triality_Surface.md",
    "04": "04_Boundary_Repair.md",
    "05": "05_Oloid_Path_Carrier.md",
    "06": "06_Causal_Link_and_Obligation_Ledger.md",
    "07": "07_Discrete_Continuous_Bridge.md",
    "08": "08_Lattice_Closure.md",
    "09": "09_Hamiltonian_Window_Emergence.md",
    "10": "10_T10_Master_Receipt.md",
    "11": "11_Theory_Admission_Gate.md",
    "12": "12_CA_Prediction_Surface.md",
    "13": "13_Standard_Model_Quark_Face_Transport.md",
    "14": "14_GR_Boundary_Repair_Curvature.md",
    "15": "15_QFT_Higgs_Mass_Residue_Carrier.md",
    "16": "16_Continuum_Edge_Residuals.md",
    "17": "17_E6_E8_Error_Correction_Tower.md",
    "18": "18_VOA_Moonshine_Representation_Routes.md",
    "19": "19_Observer_Face_Selection.md",
    "20": "20_Layer_2_Synthesis_Ledger.md",
    "21": "21_MorphForge_PolyForge_MorphoniX.md",
    "22": "22_MetaForge_Applied_Materials.md",
    "23": "23_FoldForge_Protein_Folding.md",
    "24": "24_KnightForge_N_Dimensional_Chess_Automata.md",
    "25": "25_Energetic_Traversal_Maps.md",
    "26": "26_Z_Pinch_and_Shear_Horizon.md",
    "27": "27_Observer_Delay_and_Shared_Reality.md",
    "28": "28_N_Dimensional_Game_Lattices.md",
    "29": "29_Monster_Universal_Energy_Bound_Hypotheses.md",
    "30": "30_Grand_Ribbon_Meta_Framer.md",
    "31": "31_It_Was_Still_Just_LCR.md",
    "32": "32_The_Supervisor_Cursor.md",
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def paper_record(item: tuple[str, str, str, list[str], str]) -> dict:
    pid, title, band, legacy, summary = item
    legacy_paths = [LEGACY_FILE_MAP[n] for n in legacy if n in LEGACY_FILE_MAP]
    return {
        "publication_id": pid,
        "title": title,
        "slug": slug(title),
        "series": "Formalizing LCR, Unifying Standard Models",
        "band": band,
        "legacy_papers": legacy,
        "legacy_paths": legacy_paths,
        "summary": summary,
        "triad": {
            "formal": f"{pid}/formal.md",
            "companion": f"{pid}/companion.md",
            "workbook": f"{pid}/workbook.md",
            "manifest": f"{pid}/paper.yml",
            "latex": f"{pid}/paper.tex",
            "pdf": f"{pid}/paper.pdf",
        },
        "claim_lanes": [lane["id"] for lane in CLAIM_LANES],
        "status": "blueprint_skeleton",
    }


def yaml_list(values: list[str], indent: int = 2) -> str:
    pad = " " * indent
    if not values:
        return f"{pad}[]"
    return "\n".join(f"{pad}- {json.dumps(v)}" for v in values)


def render_manifest(record: dict) -> str:
    return f"""publication_id: {record['publication_id']}
title: {json.dumps(record['title'])}
series: "Formalizing LCR, Unifying Standard Models"
band: {record['band']}
status: blueprint_skeleton
legacy_papers:
{yaml_list(record['legacy_papers'])}
legacy_paths:
{yaml_list(record['legacy_paths'])}
triad_role:
  formal: formal.md
  companion: companion.md
  workbook: workbook.md
generated_outputs:
  latex: paper.tex
  pdf: paper.pdf
claim_lanes:
{yaml_list(record['claim_lanes'])}
evidence_inputs:
{yaml_list(COMMON_SOURCES['audits'])}
receipts: []
validators: []
cam_crystal_sources:
{yaml_list(COMMON_SOURCES['kimi'] + COMMON_SOURCES['downloads'])}
kimi_window_inputs:
  - "window_summary.json"
  - "node DBs"
  - "window DBs"
companion_targets:
  - explain the formal result without weakening it
  - name the strongest claim and its boundary
  - show how later papers reuse the result
workbook_targets:
  - reproduce receipt/validator paths
  - list CAM/crystal queries
  - list analog workbook exercises
normal_form_gate:
  required_for_finalization: {str(record['publication_id'] >= 'FLCR-28').lower()}
  status: incoming_kimi_universal_normal_form_reserved
"""


def render_formal(record: dict) -> str:
    return f"""# {record['publication_id']} - {record['title']}

**Series:** Formalizing LCR, Unifying Standard Models  
**Artifact:** formal paper source  
**Status:** blueprint skeleton; not publication-ready body text yet.  
**Claim posture:** maximal claims allowed only through explicit claim lanes.

## Abstract

This paper will formalize: {record['summary']}

## Keywords

LCR; CQECMPLX; receipt-bound formalization; CAM; crystal memory; normal form.

## Contribution And Scope

- Primary contribution: to be rewritten from assigned legacy sources and orbital data.
- LCR-native boundary: {'required' if record['band'] == 'lcr_native' else 'not primary'}.
- Standard-model translation boundary: {'required' if record['band'] != 'lcr_native' else 'deferred unless explicitly marked'}.

## Claim Lanes

Every theorem, proposition, empirical claim, and synthesis claim must be assigned
to one of the claim lanes in `../CLAIM_LANE_SCHEMA.json`.

## Methods / Construction

To be populated from legacy papers, supplements, Kimi node/window data, CAM
harvests, receipts, validators, and standard citations.

## Results And Evidence

To be populated with exact receipt, validator, standards, CAM/crystal, or
normal-form evidence.

## Limitations And Falsifiers

To be populated before any publication-ready status is assigned.

## Reproducibility Package

See `paper.yml` and `workbook.md`.
"""


def render_companion(record: dict) -> str:
    return f"""# {record['publication_id']} Companion - {record['title']}

This companion is the conversational bridge for the formal paper. It should
explain what the paper proves, what it does not prove, why the result matters,
and how a reader should inspect the attached evidence.

## Plain-Language Thesis

{record['summary']}

## What To Read First

- `formal.md`
- `workbook.md`
- assigned legacy papers listed in `paper.yml`
- related CAM/crystal and Kimi window evidence listed in `paper.yml`

## Strongest Claim

To be filled during rewrite. The strongest claim must match a claim lane in the
formal paper.

## What This Does Not Claim

To be filled during rewrite. This section prevents the companion from outrunning
the formal evidence.
"""


def render_workbook(record: dict) -> str:
    return f"""# {record['publication_id']} Workbook - {record['title']}

This workbook binds the formal paper to executable evidence, CAM/crystal
queries, analog examples, validators, receipts, and review prompts.

## Evidence Checklist

- Legacy paper sources from `paper.yml`
- NSIT and orbital audit rows
- Kimi node/window data where applicable
- Claude/MannyAI CAM/crystal harvest rows
- Receipt and verifier paths
- Analog workbook exercises

## CAM / Crystal Queries

- Query assigned legacy paper IDs.
- Query claim-lane evidence.
- Query Kimi window coverage.
- Query normal-form intake status for `FLCR-28..FLCR-40`.

## Reviewer Exercises

1. Identify the strongest claim and its lane.
2. Locate the receipt, citation, CAM data, or normal-form gate.
3. State the falsifier or remaining obligation.
"""


def render_tex(record: dict) -> str:
    title = record["title"].replace("&", r"\&")
    return rf"""\documentclass[11pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{hyperref}}
\title{{{record['publication_id']}: {title}}}
\author{{CQECMPLX Publication Series}}
\date{{Blueprint skeleton}}
\begin{{document}}
\maketitle
\begin{{abstract}}
{record['summary']}
\end{{abstract}}
\section*{{Status}}
This is a generated blueprint skeleton for the series \emph{{Formalizing LCR, Unifying Standard Models}}.
Publication-ready body text, citations, figures, and final receipt tables will be added in later rewrite passes.
\section*{{Claim Lanes}}
All strong claims must be assigned to the claim-lane schema in the series root.
\end{{document}}
"""


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def write_minimal_pdf(path: Path, title: str, summary: str) -> None:
    lines = [
        "BT",
        "/F1 16 Tf",
        "72 760 Td",
        f"({pdf_escape(title[:72])}) Tj",
        "/F1 10 Tf",
        "0 -28 Td",
        "(Blueprint skeleton PDF placeholder.) Tj",
        "0 -18 Td",
        f"({pdf_escape(summary[:95])}) Tj",
        "ET",
    ]
    stream = "\n".join(lines).encode("latin-1", errors="replace")
    objects = []
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    objects.append(
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>"
    )
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects.append(b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream")
    content = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(content))
        content.extend(f"{i} 0 obj\n".encode())
        content.extend(obj)
        content.extend(b"\nendobj\n")
    xref = len(content)
    content.extend(f"xref\n0 {len(objects)+1}\n".encode())
    content.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        content.extend(f"{off:010d} 00000 n \n".encode())
    content.extend(
        f"trailer << /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    path.write_bytes(content)


def write_series_blueprint(records: list[dict]) -> None:
    lines = [
        "# Formalizing LCR, Unifying Standard Models",
        "",
        "This directory is the publication-series blueprint for converting the existing CQECMPLX paper corpus into a 40-paper journal/arXiv-style series.",
        "",
        "Each topic is represented as a triad:",
        "",
        "- `formal.md`: formal submission-style paper source.",
        "- `companion.md`: conversational/explanatory bridge.",
        "- `workbook.md`: analog and evidence workbook.",
        "",
        "The first thirty papers are LCR-native formalization papers. The last ten translate mature LCR structures into Standard Model and grand-unification claims.",
        "",
        "## Paper Map",
        "",
        "| ID | Title | Band | Legacy papers |",
        "|---|---|---|---|",
    ]
    for record in records:
        legacy = ", ".join(record["legacy_papers"]) or "new/orbital"
        lines.append(f"| `{record['publication_id']}` | {record['title']} | {record['band']} | {legacy} |")
    lines.extend(
        [
            "",
            "## Required Inputs",
            "",
            "- Current `D:/Paper Reworks` papers and supplements.",
            "- NSIT inventories, closure matrices, orbital audits, and CAM claim audits.",
            "- Claude memory, Kimi MannyAI nodes/windows/standards, D:/MannyAI crystals, repo-harvest CAM, and NotebookLM/MannyAI bundle.",
            "- Incoming Kimi universal normal form, reserved especially for `FLCR-28..FLCR-40`.",
            "",
            "## Build Status",
            "",
            "This milestone creates the blueprint and triad skeletons. The generated PDFs are placeholder PDFs until the final LaTeX build toolchain is installed and the formal bodies are rewritten.",
            "",
        ]
    )
    (SERIES_ROOT / "SERIES_BLUEPRINT.md").write_text("\n".join(lines), encoding="utf-8")


def write_template() -> None:
    template = """# Triad Template

Every FLCR paper must maintain these three synchronized artifacts.

## formal.md

Required sections:

1. Title/status/source block.
2. Abstract.
3. Keywords.
4. Contribution and scope.
5. Background and related work.
6. Definitions and notation.
7. Theorems/claims with claim lanes.
8. Methods/construction.
9. Results and evidence.
10. Proof/proof sketch.
11. Limitations, falsifiers, and open obligations.
12. Reproducibility package.
13. Cross-paper dependencies.
14. Conclusion.

## companion.md

Required sections:

1. Plain-language thesis.
2. Why this paper exists.
3. Strongest claim.
4. What this does not claim.
5. How it connects to prior and later papers.
6. Reviewer reading path.

## workbook.md

Required sections:

1. Evidence checklist.
2. Receipt and verifier table.
3. CAM/crystal query patterns.
4. Kimi node/window references.
5. Analog exercises.
6. Falsifier exercises.
7. Build/replay instructions.
"""
    (SERIES_ROOT / "TRIAD_TEMPLATE.md").write_text(template, encoding="utf-8")


def write_protocol() -> None:
    protocol = """# Build And Submission Protocol

## Canonical Source

Markdown is the editable source. `paper.tex` and `paper.pdf` are generated outputs.

## Current Toolchain Status

This environment did not expose `pdflatex` or `pandoc` when the blueprint was created. The generated PDFs are minimal placeholders so every triad has the contracted output files. Final arXiv-style PDFs require a later LaTeX build pass.

## Rewrite Passes

1. Assign sources and claim lanes in `SERIES_MAP.json` and `SOURCE_ROUTING_MATRIX.json`.
2. Fill all 120 triad Markdown files from assigned source material.
3. Rewrite `FLCR-01..FLCR-30` in LCR-native language, moving Standard Model language to deferred mapping slots.
4. Rewrite `FLCR-31..FLCR-40` as Standard Model translation and grand-unification papers.
5. Generate final LaTeX/PDF outputs.
6. Run publication readiness checks.

## Publication Readiness Checks

- JSON and YAML parse.
- Every formal claim has a lane, evidence source, and boundary.
- `FLCR-01..FLCR-30` avoid Standard Model language except deferred mapping notes.
- `FLCR-31..FLCR-40` cite prior LCR-native papers before translation claims.
- Every paper has formal, companion, workbook, manifest, LaTeX, and PDF artifacts.
- Every receipt/path/citation exists or is explicitly marked external-required.
- Pilot build passes for `FLCR-01`, `FLCR-08`, `FLCR-28`, and `FLCR-40`.
"""
    (SERIES_ROOT / "BUILD_AND_SUBMISSION_PROTOCOL.md").write_text(protocol, encoding="utf-8")


def write_routing_matrix(records: list[dict]) -> None:
    matrix = {
        "schema": "flcr_source_routing_matrix.v1",
        "series": "Formalizing LCR, Unifying Standard Models",
        "common_sources": COMMON_SOURCES,
        "papers": [
            {
                "publication_id": r["publication_id"],
                "legacy_paths": r["legacy_paths"],
                "audit_sources": COMMON_SOURCES["audits"],
                "supplement_sources": COMMON_SOURCES["supplements"],
                "kimi_sources": COMMON_SOURCES["kimi"],
                "download_sources": COMMON_SOURCES["downloads"],
                "normal_form_intake_required": r["publication_id"] >= "FLCR-28",
            }
            for r in records
        ],
    }
    (SERIES_ROOT / "SOURCE_ROUTING_MATRIX.json").write_text(json.dumps(matrix, indent=2), encoding="utf-8")


def main() -> None:
    SERIES_ROOT.mkdir(parents=True, exist_ok=True)
    records = [paper_record(item) for item in PAPERS]
    (SERIES_ROOT / "SERIES_MAP.json").write_text(
        json.dumps(
            {
                "schema": "flcr_series_map.v1",
                "series": "Formalizing LCR, Unifying Standard Models",
                "paper_count": len(records),
                "triad_artifacts_per_paper": 3,
                "generated_outputs_per_paper": ["paper.tex", "paper.pdf"],
                "papers": records,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (SERIES_ROOT / "CLAIM_LANE_SCHEMA.json").write_text(
        json.dumps({"schema": "flcr_claim_lane_schema.v1", "lanes": CLAIM_LANES}, indent=2),
        encoding="utf-8",
    )
    write_series_blueprint(records)
    write_template()
    write_protocol()
    write_routing_matrix(records)

    for record in records:
        paper_dir = SERIES_ROOT / record["publication_id"]
        paper_dir.mkdir(parents=True, exist_ok=True)
        (paper_dir / "paper.yml").write_text(render_manifest(record), encoding="utf-8")
        (paper_dir / "formal.md").write_text(render_formal(record), encoding="utf-8")
        (paper_dir / "companion.md").write_text(render_companion(record), encoding="utf-8")
        (paper_dir / "workbook.md").write_text(render_workbook(record), encoding="utf-8")
        (paper_dir / "paper.tex").write_text(render_tex(record), encoding="utf-8")
        write_minimal_pdf(
            paper_dir / "paper.pdf",
            f"{record['publication_id']}: {record['title']}",
            record["summary"],
        )

    print(f"wrote {SERIES_ROOT}")
    print(f"papers {len(records)}")
    print(f"triad markdown files {len(records) * 3}")
    print(f"manifests {len(records)}")
    print(f"tex files {len(records)}")
    print(f"pdf placeholders {len(records)}")


if __name__ == "__main__":
    main()
