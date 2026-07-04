"""Build an orbital-data cross-population audit for the 00-32 paper spine.

This script treats the numbered 00-32 papers as the canonical spine and every
other paper-like, supplement, CAM/memory, receipt/data, and validator artifact
as orbital data. It does not grade claims. It finds where orbital material is
present but not yet routed back into the owning spine paper.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
INVENTORY_PATH = ROOT / "NSIT_PAPER_EVIDENCE_INVENTORY.json"
SUPPLEMENT_INDEX = ROOT / "supplements" / "SUPPLEMENT_INDEX.md"
OUT_MD = ROOT / "ORBITAL_DATA_CROSS_POPULATION_AUDIT.md"
OUT_JSON = ROOT / "ORBITAL_DATA_CROSS_POPULATION_AUDIT.json"
SPINE_NUMBERS = [f"{i:02d}" for i in range(33)]


CLAIM_NATURE_LANES = [
    {
        "lane_id": "lookup_vs_invariant",
        "name": "Lookup, construction, and invariant-scope split",
        "papers": ["08", "17", "21", "29"],
        "why_missing": (
            "Library-action lookup evidence can be present while stronger invariant, "
            "glue-coset, Gamma72, or physical interpretation claims still need their "
            "own receipts."
        ),
        "populate": (
            "Route lattice-forge APIs and receipt paths into the local burden table, "
            "then keep expanded invariants as separate next needs."
        ),
    },
    {
        "lane_id": "standard_physics_formalism",
        "name": "Standard physics formalism not attached",
        "papers": ["07", "13", "15", "16", "22", "25", "26"],
        "why_missing": (
            "Carrier, vacancy, excitation, energy, and material terms are often treated "
            "as novel because the standard electron-hole-exciton or calibration formalism "
            "is not quoted beside the CQE statement."
        ),
        "populate": (
            "Attach NP-12/NP-13 correspondence rows and separate addressability claims "
            "from calibrated physical claims."
        ),
    },
    {
        "lane_id": "formal_methods_as_math",
        "name": "Receipts and governance treated as non-mathematical",
        "papers": ["00", "04", "06", "10", "11", "20", "30", "31", "32"],
        "why_missing": (
            "Schemas, ledgers, reproducibility locks, admission filters, and status "
            "preservation are formal-methods evidence, but some papers still carry them "
            "as prose obligations."
        ),
        "populate": (
            "Attach NSIT, receipt catalog, CAM, and standards-board evidence as formal "
            "artifacts instead of leaving them as loose editorial notes."
        ),
    },
    {
        "lane_id": "negative_receipt_reuse",
        "name": "Negative and failed-route receipts not reused",
        "papers": ["06", "11", "12", "20", "27", "32"],
        "why_missing": (
            "Failed verifier routes and rejected data are useful constraints, but they "
            "are often stranded outside the paper that needs the exclusion boundary."
        ),
        "populate": (
            "Route negative receipts into burden tables as exclusion evidence and "
            "counterexample guards."
        ),
    },
    {
        "lane_id": "finite_vs_unbounded",
        "name": "Finite verification mixed with unbounded claim language",
        "papers": ["01", "02", "12", "24", "28", "32"],
        "why_missing": (
            "Finite-state, bounded-search, and local-rule checks are real closures, but "
            "they become invisible when the row is phrased as an unbounded theorem."
        ),
        "populate": (
            "Split bounded computational receipts from unbounded/minimality/generalization "
            "burdens."
        ),
    },
    {
        "lane_id": "static_temporal_split",
        "name": "Static structure mixed with temporal protocol",
        "papers": ["05", "09", "18", "19", "27", "31"],
        "why_missing": (
            "Static templates, observer rows, and retrospective readouts need separate "
            "lanes from temporal evolution, simultaneity, or causal protocol claims."
        ),
        "populate": (
            "Add explicit static/protocol slots and route later temporal receipts back "
            "through those slots."
        ),
    },
    {
        "lane_id": "applied_forge_internal_external",
        "name": "Applied forge internal/external validation split",
        "papers": ["21", "22", "23", "24", "25", "26", "28", "30"],
        "why_missing": (
            "Descriptor generation, candidate ranking, and lookup surfaces can be internal "
            "tool claims while wet-lab, fabrication, biological, or calibrated energy "
            "claims remain external-validation needs."
        ),
        "populate": (
            "Attach applied-forge workbook rows and split internal descriptors from "
            "external validation requirements."
        ),
    },
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def expand_paper_field(field: str) -> set[str]:
    field = field.strip().lower()
    if field in {"all papers", "all batches", "00-32"}:
        return set(SPINE_NUMBERS)

    found: set[str] = set()
    for start, end in re.findall(r"(\d{2})\s*-\s*(\d{2})", field):
        for num in range(int(start), int(end) + 1):
            if 0 <= num <= 32:
                found.add(f"{num:02d}")
    for num in re.findall(r"\b\d{2}\b", field):
        if num in SPINE_NUMBERS:
            found.add(num)
    return found


def parse_supplement_index() -> dict[str, list[dict[str, str]]]:
    by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
    text = read_text(SUPPLEMENT_INDEX)
    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        match = re.search(r"`([^`]+)`", cells[0])
        if not match:
            continue
        name = match.group(1)
        papers = expand_paper_field(cells[1])
        for paper in papers:
            by_paper[paper].append({"name": name, "job": cells[2]})
    return by_paper


def spine_paths() -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for num in SPINE_NUMBERS:
        matches = sorted(ROOT.glob(f"{num}_*.md"))
        if matches:
            paths[num] = matches[0]
    return paths


def is_spine_artifact(artifact: dict, spine: dict[str, Path]) -> bool:
    num = artifact.get("paper_number")
    if num not in spine:
        return False
    try:
        return Path(artifact["path"]).resolve() == spine[num].resolve()
    except OSError:
        return False


def basename_mentioned(spine_text: str, orbital_name: str) -> bool:
    lower = spine_text.lower()
    stem = Path(orbital_name).stem.lower()
    spaced = stem.replace("_", " ").replace("-", " ")
    return orbital_name.lower() in lower or stem in lower or spaced in lower


def compact_counter(counter: Counter) -> dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def build_audit() -> dict:
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    artifacts = inventory["artifacts"]
    spine = spine_paths()
    indexed_supplements = parse_supplement_index()

    orbital_by_paper: dict[str, list[dict]] = defaultdict(list)
    unnumbered_orbitals: list[dict] = []
    cross_cutting_orbitals: list[dict] = []
    global_classes = {"supplement", "memory_or_cam", "validator", "receipt_or_data", "formal_paper"}

    for artifact in artifacts:
        if is_spine_artifact(artifact, spine):
            continue
        paper_num = artifact.get("paper_number")
        keys = set(artifact.get("attachment_keys", []))
        if paper_num in SPINE_NUMBERS:
            orbital_by_paper[paper_num].append(artifact)
        elif artifact.get("artifact_class") in global_classes:
            if any(key.startswith("paper:") for key in keys):
                cross_cutting_orbitals.append(artifact)
            else:
                unnumbered_orbitals.append(artifact)

    lane_by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
    for lane in CLAIM_NATURE_LANES:
        for paper in lane["papers"]:
            lane_by_paper[paper].append(lane)

    per_paper = {}
    total_missing_backlinks = 0
    total_indexed_supplement_routes = 0

    for num in SPINE_NUMBERS:
        paper_path = spine.get(num)
        spine_text = read_text(paper_path).lower() if paper_path else ""
        orbitals = orbital_by_paper.get(num, [])
        class_counts = Counter(a["artifact_class"] for a in orbitals)

        supplement_routes = indexed_supplements.get(num, [])
        total_indexed_supplement_routes += len(supplement_routes)
        missing_supplement_backlinks = [
            route for route in supplement_routes if not basename_mentioned(spine_text, route["name"])
        ]
        total_missing_backlinks += len(missing_supplement_backlinks)

        explicit_internal = f"{num}_INTERNAL_REASONING_SUPPLEMENT.md"
        internal_exists = (ROOT / "supplements" / explicit_internal).exists()
        internal_backlinked = basename_mentioned(spine_text, explicit_internal)

        lanes = lane_by_paper.get(num, [])
        lane_backlinks = []
        for lane in lanes:
            terms = [lane["lane_id"].replace("_", " "), lane["name"].lower()]
            lane_backlinks.append(
                {
                    "lane_id": lane["lane_id"],
                    "name": lane["name"],
                    "appears_backlinked": any(term in spine_text for term in terms),
                    "populate": lane["populate"],
                }
            )

        per_paper[num] = {
            "paper_path": str(paper_path) if paper_path else None,
            "orbital_artifact_count": len(orbitals),
            "orbital_class_counts": compact_counter(class_counts),
            "indexed_supplement_routes": supplement_routes,
            "missing_supplement_backlinks": missing_supplement_backlinks,
            "internal_reasoning_supplement_exists": internal_exists,
            "internal_reasoning_backlinked": internal_backlinked,
            "claim_nature_lanes": lane_backlinks,
            "claim_nature_lane_count": len(lanes),
        }

    class_totals = Counter(a["artifact_class"] for a in artifacts)
    orbital_class_totals = Counter()
    for rows in orbital_by_paper.values():
        orbital_class_totals.update(a["artifact_class"] for a in rows)

    return {
        "schema": "orbital_data_cross_population_audit.v1",
        "spine_range": "00-32",
        "source_inventory": str(INVENTORY_PATH),
        "inventory_artifact_count": inventory["artifact_count"],
        "inventory_class_totals": compact_counter(class_totals),
        "numbered_orbital_artifact_count": sum(len(v) for v in orbital_by_paper.values()),
        "numbered_orbital_class_totals": compact_counter(orbital_class_totals),
        "unnumbered_orbital_artifact_count": len(unnumbered_orbitals),
        "cross_cutting_orbital_artifact_count": len(cross_cutting_orbitals),
        "indexed_supplement_route_count": total_indexed_supplement_routes,
        "missing_indexed_supplement_backlink_count": total_missing_backlinks,
        "claim_nature_lanes": CLAIM_NATURE_LANES,
        "per_paper": per_paper,
        "global_findings": [
            {
                "finding": "Most supplements are orbital to the spine but are not yet cited inside the owning paper bodies.",
                "action": "Add an Orbital Data / Supplement Routing section to each spine paper that cites indexed supplements and internal reasoning supplement.",
            },
            {
                "finding": "Many paper-local obligations are likely under-populated because the obligation is claim-nature dependent.",
                "action": "Split rows by claim nature before sending them to NSIT or grading tools: lookup vs invariant, symbolic vs physical, finite vs unbounded, static vs temporal, internal forge vs external validation.",
            },
            {
                "finding": "Unnumbered formal papers, CAM/memory artifacts, receipts, and validators exist but are not yet forced through a paper-number lane.",
                "action": "Create a second pass that assigns each unnumbered orbital artifact to one or more paper lanes or marks it as corpus-level background.",
            },
        ],
    }


def write_markdown(audit: dict) -> None:
    lines: list[str] = []
    lines.append("# Orbital Data Cross-Population Audit")
    lines.append("")
    lines.append(
        "This audit surrounds the `00-32` spine with supplements and all other "
        "paper-like artifacts not named as the canonical spine. It measures missing "
        "routing. It does not grade validity or assign open/closed states."
    )
    lines.append("")
    lines.append("## Corpus Counts")
    lines.append("")
    lines.append(f"- Inventory artifacts: {audit['inventory_artifact_count']}")
    lines.append(f"- Numbered orbital artifacts attached to 00-32: {audit['numbered_orbital_artifact_count']}")
    lines.append(f"- Unnumbered orbital artifacts needing lane assignment: {audit['unnumbered_orbital_artifact_count']}")
    lines.append(f"- Cross-cutting orbital artifacts: {audit['cross_cutting_orbital_artifact_count']}")
    lines.append(f"- Indexed supplement routes into 00-32: {audit['indexed_supplement_route_count']}")
    lines.append(
        "- Indexed supplement routes not backlinked from owning spine papers: "
        f"{audit['missing_indexed_supplement_backlink_count']}"
    )
    lines.append("")
    lines.append("### Numbered Orbital Class Totals")
    lines.append("")
    lines.append("| Class | Count |")
    lines.append("|---|---:|")
    for cls, count in audit["numbered_orbital_class_totals"].items():
        lines.append(f"| {cls} | {count} |")
    lines.append("")

    lines.append("## Claim-Nature Lanes")
    lines.append("")
    lines.append(
        "These are the main ways data appears to be ignored because the claim type "
        "is not split finely enough before routing."
    )
    lines.append("")
    lines.append("| Lane | Papers | Missing pattern | Cross-population action |")
    lines.append("|---|---|---|---|")
    for lane in audit["claim_nature_lanes"]:
        papers = ", ".join(lane["papers"])
        lines.append(
            f"| {lane['name']} | {papers} | {lane['why_missing']} | {lane['populate']} |"
        )
    lines.append("")

    lines.append("## Per-Paper Orbital Pressure")
    lines.append("")
    lines.append(
        "| Paper | Orbital artifacts | Formal | Receipts/data | Validators | Supplements | "
        "Memory/CAM | Indexed supplement routes | Missing supplement backlinks | Claim-nature lanes |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for num, row in audit["per_paper"].items():
        counts = row["orbital_class_counts"]
        lines.append(
            f"| {num} | {row['orbital_artifact_count']} | "
            f"{counts.get('formal_paper', 0)} | "
            f"{counts.get('receipt_or_data', 0)} | "
            f"{counts.get('validator', 0)} | "
            f"{counts.get('supplement', 0)} | "
            f"{counts.get('memory_or_cam', 0)} | "
            f"{len(row['indexed_supplement_routes'])} | "
            f"{len(row['missing_supplement_backlinks'])} | "
            f"{row['claim_nature_lane_count']} |"
        )
    lines.append("")

    lines.append("## Immediate Cross-Population Queue")
    lines.append("")
    for num, row in audit["per_paper"].items():
        missing = row["missing_supplement_backlinks"]
        lanes = [lane for lane in row["claim_nature_lanes"] if not lane["appears_backlinked"]]
        if not missing and not lanes:
            continue
        paper_name = Path(row["paper_path"]).name if row["paper_path"] else f"{num}_missing"
        lines.append(f"### Paper {num}: `{paper_name}`")
        if missing:
            supplements = ", ".join(f"`{item['name']}`" for item in missing[:12])
            if len(missing) > 12:
                supplements += f", +{len(missing) - 12} more"
            lines.append(f"- Add orbital backlinks for: {supplements}.")
        if lanes:
            lane_names = "; ".join(f"{lane['name']}: {lane['populate']}" for lane in lanes)
            lines.append(f"- Split and populate claim-nature lanes: {lane_names}")
        if row["internal_reasoning_supplement_exists"] and not row["internal_reasoning_backlinked"]:
            lines.append(f"- Backlink `{num}_INTERNAL_REASONING_SUPPLEMENT.md` as reasoning-only orbital data.")
        lines.append("")

    lines.append("## Global Findings")
    lines.append("")
    for finding in audit["global_findings"]:
        lines.append(f"- {finding['finding']} {finding['action']}")
    lines.append("")

    lines.append("## Next Pass")
    lines.append("")
    lines.append(
        "Use this audit as the queue for adding `Orbital Data / Cross-Population` "
        "sections to the spine papers. The section should cite supplements, receipts, "
        "validators, and external formal papers, then hand claim classification to "
        "NSIT/grading tools."
    )
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    audit = build_audit()
    OUT_JSON.write_text(json.dumps(audit, indent=2), encoding="utf-8")
    write_markdown(audit)
    print(f"wrote {OUT_MD}")
    print(f"wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
