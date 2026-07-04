#!/usr/bin/env python3
"""Generate virtuous merged drafts for CQE Papers 10-32.

Each draft treats the available sources as faces of one paper crystal:
current rework, canonical formal paper, companion source-backup variants,
verifier/receipt rows, and saved CAM/GLM closure data.
"""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
OUT = ROOT / "virtuous"
FORMAL_ROOT = Path(r"D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal")
SOURCE_BACKUP = Path(r"D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\source_backup")
CAM_NODES = Path(r"D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json")
CAM_CLOSURE = Path(r"D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json")

WORD_RE = re.compile(r"\S+")
HEADING_RE = re.compile(r"(?m)^#{1,6}\s+(.+)$")
OBLIGATION_ROW_RE = re.compile(r"(?m)^\|\s*(?P<id>\d{2}\.\d+|CC\.\d+)\s*\|(?P<body>.+)$")
PAPER_REF_RE = re.compile(r"(?:paper|CQE-paper-|obligation-)?(?P<num>\d{2})(?:\.\d+)?", re.IGNORECASE)


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def title_from(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def first_paragraph_after_heading(text: str, heading: str) -> str:
    marker = f"## {heading}"
    idx = text.find(marker)
    if idx < 0:
        return ""
    rest = text[idx + len(marker):].strip()
    parts = re.split(r"\n\s*\n", rest, maxsplit=2)
    return parts[0].strip() if parts else ""


def strip_title(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip()
    return text.strip()


def obligation_rows(text: str) -> list[dict[str, str]]:
    rows = []
    for match in OBLIGATION_ROW_RE.finditer(text):
        rows.append(
            {
                "id": match.group("id"),
                "body": match.group("body").strip(),
                "row": match.group(0).strip(),
            }
        )
    return rows


def paper_number_from_obligation(oid: str, fallback: int) -> int:
    if re.match(r"^\d{2}\.", oid):
        return int(oid.split(".", 1)[0])
    return fallback


def referenced_papers(*parts: str) -> list[int]:
    found = set()
    for part in parts:
        for match in PAPER_REF_RE.finditer(part or ""):
            num = int(match.group("num"))
            if 0 <= num <= 99:
                found.add(num)
    return sorted(found)


def lane_start_for(num: int, obligation: dict[str, str], related_rows: list[dict]) -> int:
    """Return the paper-sequence floor this obligation should spring back through."""
    row_blob = " ".join(
        [obligation.get("id", ""), obligation.get("body", ""), obligation.get("row", "")]
        + [json.dumps(row, sort_keys=True) for row in related_rows]
    )
    candidates = [
        paper
        for paper in referenced_papers(row_blob)
        if 9 <= paper < num
    ]
    if candidates:
        return min(9, min(candidates))
    return 9


def lane_action(obligation: dict[str, str], related_rows: list[dict]) -> str:
    body = obligation.get("body", "").lower()
    if related_rows:
        statuses = ", ".join(
            f"{row.get('finding_id')}:{row.get('proposed_status')}" for row in related_rows
        )
        return f"re-enter through saved CAM/GLM closure evidence ({statuses})"
    if "verifier" in body or "verify" in body:
        return "re-enter through verifier reconciliation before strengthening the claim"
    if "receipt" in body or "ledger" in body:
        return "re-enter through receipt/ledger alignment before synthesis"
    if "adapter" in body or "api" in body or "interface" in body:
        return "re-enter through adapter/interface wording and proof boundary"
    if "calibration" in body or "parameter" in body:
        return "re-enter through calibration guard and evidence threshold"
    return "re-enter as an explicit next-need and propagate upward"


def classify_obligation(obligation: dict[str, str], related_rows: list[dict]) -> str:
    body = " ".join([obligation.get("body", ""), obligation.get("row", "")]).lower()
    if related_rows:
        statuses = {str(row.get("proposed_status", "")).lower() for row in related_rows}
        if "partially_closed" in statuses:
            return "partial_closure"
        if "engineering" in statuses:
            return "engineering_evidence"
        return "saved_cam_glm_evidence"
    if "closed" in body and "open" not in body and "not closed" not in body:
        return "closed_receipt"
    if "receipt" in body or "ledger" in body or "path normalization" in body:
        return "receipt_integrity"
    if "calibration" in body or "measurement" in body or "physical" in body or "external" in body:
        return "external_calibration"
    if "rule 30" in body or "cold" in body or "closed form" in body or "nth-bit" in body:
        return "rule30_boundary"
    if "transport" in body or "route" in body or "niemeier" in body or "g2" in body or "f4" in body:
        return "transport_scope"
    if "leech" in body or "moonshine" in body or "mckay" in body or "weyl" in body:
        return "exceptional_lift"
    if "tooling" in body or "engineering" in body or "parser" in body or "package" in body:
        return "engineering_gap"
    if "guard" in body or "do not" in body or "keep" in body or "preserve" in body:
        return "claim_guard"
    return "open_next_need"


def reasoning_for_lane(lane: dict) -> str:
    category = lane.get("category", "open_next_need")
    text = {
        "closed_receipt": (
            "Treat the item as closed evidence, but only at the receipt layer; "
            "do not let the closure silently upgrade neighboring mathematical claims."
        ),
        "receipt_integrity": (
            "Strengthen receipt/path language and ensure any downstream theorem depends "
            "on replayable receipts rather than assumed file layout."
        ),
        "partial_closure": (
            "Promote only the bounded or verifier-backed portion; leave the unbounded "
            "claim as an explicit obligation with the verifier named."
        ),
        "engineering_evidence": (
            "Accept this as an engineering or implementation witness, not as a full "
            "mathematical closure theorem."
        ),
        "saved_cam_glm_evidence": (
            "Import the saved CAM/GLM evidence as status-bearing data and state exactly "
            "which part of the original obligation it affects."
        ),
        "external_calibration": (
            "Push physical, experimental, or unit-bearing claims behind a calibration "
            "gate; the internal formal result may survive, but measured-world language "
            "must remain conditional."
        ),
        "rule30_boundary": (
            "Separate enumerated/readout architecture from cold-start Rule 30 closure; "
            "never phrase cached or accumulated access as a solved cold extractor."
        ),
        "transport_scope": (
            "Downgrade route language to demonstrated, bounded, registered, or open "
            "according to its witness surface."
        ),
        "exceptional_lift": (
            "Keep exceptional-lattice and Moonshine language as a structured lift unless "
            "the specific construction, table, or identification is present."
        ),
        "engineering_gap": (
            "Route this into tooling or adapter work before using it as a premise in the "
            "paper's theorem."
        ),
        "claim_guard": (
            "Rewrite surrounding prose so the guard is visible at the point where a reader "
            "might otherwise infer a stronger claim."
        ),
        "open_next_need": (
            "Leave the obligation live and convert it into the next verifier, witness, "
            "adapter, or documentation action."
        ),
    }
    return text.get(category, text["open_next_need"])


def obligation_springboards(num: int, obligations: list[dict[str, str]], closures: list[dict]) -> list[dict]:
    lanes = []
    for obligation in obligations:
        oid = obligation["id"]
        paper = paper_number_from_obligation(oid, num)
        related = [row for row in closures if str(row.get("obligation_id", "")).endswith(oid)]
        start = lane_start_for(paper, obligation, related)
        lane = list(range(start, paper + 1))
        lanes.append(
            {
                "obligation_id": oid,
                "source_paper": paper,
                "paper": paper,
                "return_start": start,
                "upward_lane": lane,
                "category": classify_obligation(obligation, related),
                "action": lane_action(obligation, related),
                "reasoned_update": "",
                "row": obligation["row"],
                "related_findings": [
                    {
                        "finding_id": row.get("finding_id", ""),
                        "proposed_status": row.get("proposed_status", ""),
                        "verifier": row.get("verifier", ""),
                    }
                    for row in related
                ],
            }
        )
        lanes[-1]["reasoned_update"] = reasoning_for_lane(lanes[-1])
    return lanes


def lane_text(lane: list[int]) -> str:
    return " -> ".join(f"{paper:02d}" for paper in lane)


def category_counts(lanes: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for lane in lanes:
        category = lane.get("category", "open_next_need")
        counts[category] = counts.get(category, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def pressure_summary_for_paper(paper: int, inbound: list[dict]) -> list[str]:
    counts = category_counts(inbound)
    categories = set(counts)
    notes: list[str] = []
    if paper == 9:
        notes.append(
            "Paper 09 is now the return floor for the second-block rework. Its "
            "Hamiltonian-window theorem must be framed as the suite's finite "
            "receipt-preserving temporal substrate, not as permission to promote "
            "later physical, exceptional, or product claims."
        )
    if {"receipt_integrity", "closed_receipt"} & categories:
        notes.append(
            "Receipt-closed items may strengthen replayability and audit language, "
            "but they do not close unrelated transport, physical, or cold-start "
            "mathematical obligations."
        )
    if "partial_closure" in categories:
        notes.append(
            "Partial CAM/GLM closures should be imported as bounded progress: name "
            "the verifier, state the portion advanced, and keep the residual claim "
            "visible."
        )
    if "external_calibration" in categories:
        notes.append(
            "All physical or unit-bearing readings must pass through an external "
            "calibration gate before appearing as more than conditional interface "
            "language."
        )
    if "rule30_boundary" in categories:
        notes.append(
            "Rule 30 language must distinguish cached/enumerated readout from cold "
            "closed-form extraction."
        )
    if "transport_scope" in categories or "exceptional_lift" in categories:
        notes.append(
            "Transport, exceptional algebra, lattice, and Moonshine routes must be "
            "graded by witness status instead of narrated as completed bridges."
        )
    if "engineering_gap" in categories:
        notes.append(
            "Engineering and adapter gaps should be promoted to work items, not used "
            "as theorem premises."
        )
    if "claim_guard" in categories:
        notes.append(
            "Guard obligations must appear next to the claims they constrain, so the "
            "reader cannot miss the boundary."
        )
    if not notes:
        notes.append(
            "Carry these obligations as live next-needs and avoid claim promotion "
            "until a verifier, receipt, calibration, or explicit guard resolves them."
        )
    return notes


def write_reasoning_audit(lane_index: list[dict]) -> None:
    counts = category_counts(lane_index)
    lines = [
        "# Obligation Reasoning Audit",
        "",
        "This file is the non-mechanical pass over the springboard lanes. It records "
        "what the obligations force us to change in the papers, not only where they "
        "route.",
        "",
        "## Category Counts",
        "",
        "| Category | Count |",
        "|----------|------:|",
    ]
    for category, count in counts.items():
        lines.append(f"| `{category}` | {count} |")

    lines.extend(["", "## Rewrite Decisions", ""])
    for lane in lane_index:
        lines.append(f"### {lane['obligation_id']} from Paper {lane['source_paper']:02d}")
        lines.append("")
        lines.append(f"- Category: `{lane['category']}`")
        lines.append(f"- Lane: `{lane_text(lane['upward_lane'])}`")
        lines.append(f"- Row: {lane['row']}")
        lines.append(f"- Decision: {lane['reasoned_update']}")
        if lane.get("related_findings"):
            findings = ", ".join(
                f"{finding.get('finding_id')}:{finding.get('proposed_status')}"
                for finding in lane["related_findings"]
            )
            lines.append(f"- Saved evidence: {findings}")
        lines.append("")

    (OUT / "OBLIGATION_REASONING_AUDIT.md").write_text(
        "\n".join(lines).rstrip() + "\n", encoding="utf-8"
    )


def write_springboard_markdown(lane_index: list[dict]) -> None:
    lines = [
        "# Obligation Springboard Index",
        "",
        "Every obligation is treated as a return lane: it springs back to the earliest "
        "paper it can affect, then moves upward through the paper sequence until the "
        "originating paper can be strengthened or explicitly guarded.",
        "",
        "## All Lanes",
        "",
        "| Obligation | Source paper | Category | Return start | Upward lane | Rework instruction |",
        "|------------|--------------|----------|--------------|-------------|--------------------|",
    ]
    for lane in lane_index:
        lines.append(
            f"| `{lane['obligation_id']}` | `{lane['source_paper']:02d}` | "
            f"`{lane['category']}` | "
            f"`{lane['return_start']:02d}` | `{lane_text(lane['upward_lane'])}` | "
            f"{lane['reasoned_update']} |"
        )

    lines.extend(["", "## Intake by Paper", ""])
    for paper in range(9, 33):
        inbound = [
            lane
            for lane in lane_index
            if paper in lane["upward_lane"] and lane["source_paper"] != paper
        ]
        if not inbound:
            continue
        lines.append(f"### Paper {paper:02d}")
        lines.append("")
        for lane in inbound:
            lines.append(
                f"- `{lane['obligation_id']}` from Paper {lane['source_paper']:02d}: "
                f"{lane['reasoned_update']}"
            )
        lines.append("")

    (OUT / "OBLIGATION_SPRINGBOARD_INDEX.md").write_text(
        "\n".join(lines).rstrip() + "\n", encoding="utf-8"
    )


def remove_generated_intake(text: str) -> str:
    marker = "\n## Upward Rework Intake\n"
    idx = text.find(marker)
    if idx < 0:
        return text.rstrip()
    return text[:idx].rstrip()


def write_upward_intake_sections(manifest: list[dict], lane_index: list[dict]) -> None:
    paths_by_paper = {entry["paper"]: Path(entry["path"]) for entry in manifest}
    paths_by_paper[9] = next(OUT.glob("09_*_VIRTUOUS.md"), None)
    for paper, path in sorted(paths_by_paper.items()):
        if path is None or not path.exists():
            continue
        inbound = [
            lane
            for lane in lane_index
            if paper in lane["upward_lane"] and lane["source_paper"] != paper
        ]
        if not inbound:
            continue
        text = remove_generated_intake(read(path))
        lines = [
            "",
            "## Upward Rework Intake",
            "",
            "Downstream obligations now spring back through this paper. Rework this paper's "
            "definitions, receipts, guards, and claim-strength language before carrying "
            "the lane upward.",
            "",
            "### Reasoned Claim Pressure",
            "",
        ]
        for note in pressure_summary_for_paper(paper, inbound):
            lines.append(f"- {note}")
        lines.extend(
            [
                "",
                "### Intake Category Counts",
                "",
                "| Category | Count |",
                "|----------|------:|",
            ]
        )
        for category, count in category_counts(inbound).items():
            lines.append(f"| `{category}` | {count} |")
        lines.extend(
            [
                "",
                "### Routed Lanes",
                "",
            ]
        )
        lines.extend([
            "| Source | Obligation | Full lane | Required local action |",
            "|--------|------------|-----------|-----------------------|",
        ])
        for lane in inbound:
            lines.append(
                f"| `{lane['source_paper']:02d}` | `{lane['obligation_id']}` | "
                f"`{lane_text(lane['upward_lane'])}` | {lane['reasoned_update']} |"
            )
        path.write_text(text + "\n".join(lines).rstrip() + "\n", encoding="utf-8")


def source_variants(num: int) -> list[Path]:
    names = [
        f"CQE-paper-{num:02d}.25.md",
        f"CQE-paper-{num:02d}.50.md",
        f"CQE-paper-{num:02d}.75.md",
        f"CQE-paper-{num:02d}_UPGRADED.md",
        f"CQE-paper-{num:02d}_RECURSIVE_CLOSE.md",
    ]
    return [SOURCE_BACKUP / name for name in names if (SOURCE_BACKUP / name).exists()]


def formal_dir(num: int) -> Path:
    return FORMAL_ROOT / f"CQE-paper-{num:02d}"


def rework_path(num: int) -> Path:
    matches = sorted(ROOT.glob(f"{num:02d}_*.md"))
    if not matches:
        raise FileNotFoundError(f"No rework file for paper {num:02d}")
    return matches[0]


def receipt_files(num: int) -> list[Path]:
    directory = formal_dir(num)
    if not directory.exists():
        return []
    receipts = sorted(directory.glob("*receipt*.json"))
    calibration = sorted(directory.glob("calibration_plan.json"))
    return receipts + calibration


def verifier_files(num: int) -> list[Path]:
    directory = formal_dir(num)
    if not directory.exists():
        return []
    return sorted(directory.glob("verify_*.py"))


def receipt_summary(path: Path) -> str:
    try:
        data = json.loads(read(path))
    except Exception:
        return "unreadable JSON"
    status = data.get("status") or data.get("PASS") or data.get("result") or data.get("verdict")
    passed = data.get("passed")
    total = data.get("total")
    checks = data.get("checks")
    if passed is None and isinstance(checks, dict):
        passed = sum(1 for value in checks.values() if value is True)
        total = len(checks)
    bits = []
    if status is not None:
        bits.append(f"status={status}")
    if passed is not None and total is not None:
        bits.append(f"checks={passed}/{total}")
    if not bits and isinstance(data, dict):
        bits.append(f"keys={','.join(list(data)[:5])}")
    return "; ".join(bits) if bits else "JSON receipt"


def closure_rows_for(num: int, closure: dict) -> list[dict]:
    rows = closure.get("closure_rows", [])
    prefix = f"obligation-{num:02d}."
    return [row for row in rows if str(row.get("obligation_id", "")).startswith(prefix)]


def cam_nodes_for(num: int, nodes: list[dict]) -> list[dict]:
    paper_id = f"CQE-paper-{num:02d}"
    prefix = f"obligation-{num:02d}."
    selected = []
    for node in nodes:
        blob = json.dumps(node, ensure_ascii=False)
        if node.get("node_id") == paper_id or prefix in blob:
            selected.append(node)
    return selected


def variant_digest(path: Path) -> str:
    text = read(path)
    heading = title_from(text, path.stem)
    purpose = first_paragraph_after_heading(text, "Purpose")
    claims = first_paragraph_after_heading(text, "Claims")
    abstract = first_paragraph_after_heading(text, "Abstract")
    digest = purpose or claims or abstract
    if not digest:
        digest = " ".join(text.split())[:900]
    return f"**{heading}.** {digest}"


def claim_lines(text: str) -> list[str]:
    claims = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^\*\*(Claim|Theorem|Lemma|Proposition)\s+[^*]+\*\*", stripped):
            claims.append(stripped)
    return claims


def paper_role(num: int) -> str:
    roles = {
        9: "finite Hamiltonian-window substrate and receipt-preserving temporal readout",
        10: "master receipt, replay boundary, and open-lift visibility layer",
        11: "theory-admission gate and boundary classifier",
        12: "cellular-automaton prediction surface and Rule 30 scope boundary",
        13: "Standard-Model quark-face transport and calibration boundary",
        14: "GR boundary-repair curvature map and physical-curvature guard",
        15: "QFT/Higgs mass-residue carrier and measured-mass calibration guard",
        16: "continuum-edge residual layer and finite-window-to-limit boundary",
        17: "E6/E8 correction tower and exceptional-lattice lift surface",
        18: "VOA/Moonshine representation route and identification guard",
        19: "observer face-selection and physical-observer boundary",
        20: "layer-2 synthesis ledger and reachability status surface",
        21: "MorphForge/PolyForge/MorphoniX engineering bridge",
        22: "MetaForge applied-materials calibration bridge",
        23: "FoldForge protein-folding calibration bridge",
        24: "KnightForge combinatorial-game surface",
        25: "energetic traversal and unit-calibration bridge",
        26: "Z-pinch/shear-horizon physical-witness bridge",
        27: "observer-delay/shared-reality guard layer",
        28: "N-dimensional game-lattice applied surface",
        29: "Monster/energy-bound hypothesis and encoding-invariance boundary",
        30: "grand ribbon meta-framer and transport-ledger framing layer",
        31: "retrospective LCR readout and downstream-status guard",
        32: "supervisor cursor and final selector/readout-status guard",
    }
    return roles.get(num, "paper-sequence bridge")


def category_status(category: str) -> str:
    status = {
        "closed_receipt": "closed at receipt/replay level",
        "receipt_integrity": "strengthenable after receipt path and replay language are explicit",
        "partial_closure": "partially closed by bounded verifier evidence",
        "engineering_evidence": "engineering witness only",
        "saved_cam_glm_evidence": "status-bearing CAM/GLM evidence",
        "external_calibration": "conditional until external calibration exists",
        "rule30_boundary": "guarded against cold-start overclaim",
        "transport_scope": "must be graded by witness classification",
        "exceptional_lift": "structured lift, not completed identification",
        "engineering_gap": "requires tooling/adapter work before theorem use",
        "claim_guard": "guard must sit beside the claim it limits",
        "open_next_need": "open next-need",
    }
    return status.get(category, "open next-need")


def obligation_workup(lane: dict) -> list[str]:
    oid = lane["obligation_id"]
    category = lane.get("category", "open_next_need")
    row = lane.get("row", "")
    source = lane.get("source_paper")
    base = [
        f"**{oid}.** {row}",
        "",
        f"- **Status reading:** {category_status(category)}.",
        f"- **Springboard lane:** `{lane_text(lane['upward_lane'])}`.",
        f"- **Paper-local consequence:** {lane['reasoned_update']}",
    ]
    if lane.get("related_findings"):
        evidence = ", ".join(
            f"`{item.get('finding_id')}` via `{item.get('verifier')}` "
            f"({item.get('proposed_status')})"
            for item in lane["related_findings"]
        )
        base.append(f"- **Saved evidence to import:** {evidence}.")
    if category == "external_calibration":
        base.append(
            "- **Rewrite requirement:** keep the internal construction as the theorem "
            "and move all measured-world, unit-bearing, experimental, or physical "
            "identification language into a calibration paragraph."
        )
    elif category == "partial_closure":
        base.append(
            "- **Rewrite requirement:** add a bounded-progress sentence naming the "
            "verifier and a residual-open sentence naming the part not yet closed."
        )
    elif category == "rule30_boundary":
        base.append(
            "- **Rewrite requirement:** separate enumerated cache/readout claims from "
            "cold-start closed-form extraction in the theorem statement and falsifier."
        )
    elif category in {"transport_scope", "exceptional_lift"}:
        base.append(
            "- **Rewrite requirement:** classify each route as demonstrated, bounded, "
            "registered, or open before using it as a bridge in later papers."
        )
    elif category in {"closed_receipt", "receipt_integrity"}:
        base.append(
            "- **Rewrite requirement:** use the item to strengthen auditability, not to "
            "promote mathematical or physical scope beyond the receipt."
        )
    elif category == "engineering_gap":
        base.append(
            "- **Rewrite requirement:** turn the gap into an adapter/tooling task and "
            "avoid depending on it as a completed premise."
        )
    elif category == "claim_guard":
        base.append(
            "- **Rewrite requirement:** place the guard immediately after the strongest "
            "nearby claim, where a reader would otherwise overgeneralize."
        )
    else:
        base.append(
            "- **Rewrite requirement:** leave the item live as the next verifier, "
            "witness, adapter, calibration, or documentation pass."
        )
    base.append(
        f"- **Upward effect:** Papers in the lane must preserve the `{paper_role(source)}` "
        "boundary before this obligation can strengthen the source paper."
    )
    return base


def build_detailed_expansion(
    num: int,
    formal: str,
    variants: list[Path],
    springboards: list[dict],
    receipts: list[Path],
    verifiers: list[Path],
) -> list[str]:
    lines: list[str] = []
    lines.append("## Detailed Expansion Pass")
    lines.append("")
    lines.append("### Paper-Level Thesis")
    lines.append("")
    lines.append(
        f"Paper {num:02d} functions as the suite's {paper_role(num)}. Its virtuous "
        "version should therefore make three layers visible at once: the formal "
        "claim that is actually proved, the receipt or verifier evidence that lets "
        "the claim be replayed, and the explicit boundary that prevents the reader "
        "from promoting an open lift into a closed theorem."
    )
    lines.append("")
    if variants:
        lines.append(
            "The companion variants are used as exposition and interface contracts. "
            "They may contribute terminology, examples, and downstream preconditions, "
            "but the canonical formal paper remains the proof spine."
        )
        lines.append("")

    claims = claim_lines(formal)
    lines.append("### Claim Status Ledger")
    lines.append("")
    if claims:
        lines.append("| Claim/Theorem | Working status | Required paper treatment |")
        lines.append("|---------------|----------------|--------------------------|")
        local_categories = {lane.get("category", "open_next_need") for lane in springboards}
        for claim in claims[:18]:
            lowered = claim.lower()
            if "physical" in lowered or "mass" in lowered or "calibration" in lowered:
                status = "conditional on calibration"
                treatment = "state internal result first; keep physical reading guarded"
            elif "rule 30" in lowered or "nth-bit" in lowered or "closed-form" in lowered:
                status = "readout architecture unless cold proof is named"
                treatment = "separate cached/enumerated readout from cold extraction"
            elif "receipt" in lowered or "ledger" in lowered:
                status = "receipt/replay claim"
                treatment = "promote auditability, not neighboring mathematical closure"
            elif local_categories & {"partial_closure", "engineering_evidence"}:
                status = "bounded or engineering-backed"
                treatment = "name verifier-backed portion and keep residual open"
            else:
                status = "internal formal claim"
                treatment = "keep proof-local and preserve falsifier boundary"
            safe_claim = claim.replace("|", "\\|")
            lines.append(f"| {safe_claim} | {status} | {treatment} |")
    else:
        lines.append(
            "No explicit claim/theorem lines were extracted from the formal spine. "
            "Use the abstract, proof, receipts, and obligation table to reconstruct "
            "the claim ledger before publication."
        )
    lines.append("")

    lines.append("### Evidence and Receipt Detail")
    lines.append("")
    if receipts:
        lines.append(
            "The receipt surface should be discussed in prose, not only listed. "
            "Passing receipts make the paper replayable; failed, partial, or missing "
            "checks become local boundaries."
        )
        for receipt in receipts[:10]:
            lines.append(f"- `{receipt.name}`: {receipt_summary(receipt)}.")
    else:
        lines.append(
            "No receipt JSON files were found, so this paper needs either a receipt "
            "generation task or a clear explanation that the current version is "
            "documentation-only."
        )
    if verifiers:
        lines.append(
            "Verifier files are the strongest executable surface. The paper should "
            "name the verifier next to any claim it supports."
        )
        for verifier in verifiers[:12]:
            lines.append(f"- `{verifier.name}` should be mapped to the claim or obligation it checks.")
    lines.append("")

    if springboards:
        lines.append("### Obligation Workups")
        lines.append("")
        for lane in springboards:
            lines.extend(obligation_workup(lane))
            lines.append("")

        lines.append("### Cross-Paper Inheritance")
        lines.append("")
        lines.append(
            "The springboard lane means this paper cannot be revised in isolation. "
            "The upstream papers in the lane must preserve the following inherited "
            "roles before the local claim can be strengthened:"
        )
        lines.append("")
        seen: set[int] = set()
        for lane in springboards:
            for paper in lane["upward_lane"]:
                if paper in seen:
                    continue
                seen.add(paper)
                lines.append(f"- Paper {paper:02d}: {paper_role(paper)}.")
        lines.append("")

    lines.append("### Publication-Grade Rewrite Targets")
    lines.append("")
    lines.append(
        "For the next manual/editorial pass, expand the paper body around these "
        "targets:"
    )
    lines.append("")
    lines.append(
        "1. Put the strongest closed theorem in the opening synthesis, then immediately "
        "state the largest thing it does not prove."
    )
    lines.append(
        "2. Move every calibration, physical-identification, and external-validation "
        "claim into a guarded paragraph with its required witness named."
    )
    lines.append(
        "3. Place verifier and receipt names beside the exact claims they support."
    )
    lines.append(
        "4. Preserve open lifts as first-class obligations rather than treating them "
        "as editorial TODOs."
    )
    lines.append("")
    return lines


def build(num: int, nodes: list[dict], closure: dict) -> str:
    rpath = rework_path(num)
    fpath = formal_dir(num) / "FORMAL_PAPER.md"
    rework = read(rpath)
    formal = read(fpath) if fpath.exists() else ""
    title = title_from(formal or rework, f"Paper {num:02d}")
    variants = source_variants(num)
    receipts = receipt_files(num)
    verifiers = verifier_files(num)
    closures = closure_rows_for(num, closure)
    cam = cam_nodes_for(num, nodes)
    obligations = obligation_rows(rework)
    springboards = obligation_springboards(num, obligations, closures)
    missing_verifiers = [v.name for v in verifiers if v.name not in rework]

    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(
        "**Virtuous rework status:** merged from current rework, canonical formal "
        "paper, companion variants, verifier receipts, and saved CAM/GLM crystal data."
    )
    lines.append("")
    lines.append("**Method:** preserve the strongest representation of each source face; when")
    lines.append("sources disagree, keep the disagreement as a named boundary or next-need.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Source Faces")
    lines.append("")
    lines.append("| Face | Path | Words / count | Contribution |")
    lines.append("|------|------|---------------|--------------|")
    lines.append(
        f"| Current rework | `{rpath}` | {words(rework)} words | Existing skeleton, "
        "current status, obligations. |"
    )
    if formal:
        lines.append(
            f"| Canonical formal paper | `{fpath}` | {words(formal)} words | Main theorem, "
            "proof, receipt, falsifier spine. |"
        )
    for variant in variants:
        lines.append(
            f"| Companion variant | `{variant.name}` | {words(read(variant))} words | "
            "Alternate toolkit/contract/bridge phrasing. |"
        )
    lines.append(f"| Formal verifiers | `{formal_dir(num)}` | {len(verifiers)} files | Executable evidence surface. |")
    lines.append(f"| Formal receipts | `{formal_dir(num)}` | {len(receipts)} files | Receipt status and check counts. |")
    lines.append(f"| Saved CAM nodes | `{CAM_NODES}` | {len(cam)} relevant nodes | Prior crystal evidence and obligation nodes. |")
    lines.append(f"| Saved GLM closure rows | `{CAM_CLOSURE}` | {len(closures)} relevant rows | Closure/partial-closure status updates. |")
    lines.append("")

    lines.append("## Virtuous Synthesis")
    lines.append("")
    abstract = first_paragraph_after_heading(formal, "Abstract") or first_paragraph_after_heading(rework, "Abstract")
    if abstract:
        lines.append(abstract)
        lines.append("")
    lines.append(
        "This version treats the formal paper as the proof spine, the companion "
        "variants as interface contracts, and the CAM/GLM rows as status-bearing "
        "crystal data. The paper's open obligations are not deleted; they are the "
        "next work items required before stronger claims can be promoted."
    )
    lines.append("")

    if closures:
        lines.append("## Saved CAM / GLM Updates")
        lines.append("")
        lines.append("| Finding | Obligation | Old status | Proposed status | Verifier | Meaning |")
        lines.append("|---------|------------|------------|-----------------|----------|---------|")
        for row in closures:
            lines.append(
                f"| `{row.get('finding_id','')}` | `{row.get('obligation_id','')}` | "
                f"{row.get('obligation_old_status','')} | {row.get('proposed_status','')} | "
                f"`{row.get('verifier','')}` | {row.get('closure_tag','')} |"
            )
        lines.append("")

    lines.append("## Companion Face Digest")
    lines.append("")
    if variants:
        for variant in variants:
            lines.append(f"- {variant_digest(variant)}")
    else:
        lines.append("- No source-backup companion variants found.")
    lines.append("")

    if missing_verifiers:
        lines.append("## Missed Verifier Rows to Reconcile")
        lines.append("")
        for verifier in missing_verifiers:
            lines.append(f"- `{verifier}`")
        lines.append("")

    lines.append("## Receipt Surface")
    lines.append("")
    if receipts:
        lines.append("| Receipt | Summary |")
        lines.append("|---------|---------|")
        for receipt in receipts:
            lines.append(f"| `{receipt.name}` | {receipt_summary(receipt)} |")
    else:
        lines.append("No formal receipt JSON files found.")
    lines.append("")

    if obligations:
        lines.append("## Open Obligations as Next Needs")
        lines.append("")
        lines.append("| ID | Current row | CAM/GLM status |")
        lines.append("|----|-------------|----------------|")
        for obligation in obligations:
            oid = obligation["id"]
            related = [row for row in closures if str(row.get("obligation_id", "")).endswith(oid)]
            if related:
                status = "; ".join(
                    f"{row.get('finding_id')} -> {row.get('proposed_status')}"
                    for row in related
                )
            else:
                status = "carry as next need"
            safe_row = obligation["row"].replace("|", "\\|")
            lines.append(f"| `{oid}` | {safe_row} | {status} |")
        lines.append("")

    if springboards:
        lines.append("## Obligation Springboard Lanes")
        lines.append("")
        lines.append(
            "Obligations return to the earliest paper they can affect, then rework "
            "upward through each paper in the lane before the local claim is promoted."
        )
        lines.append("")
        lines.append("### Local Claim Pressure")
        lines.append("")
        for note in pressure_summary_for_paper(num, springboards):
            lines.append(f"- {note}")
        lines.append("")
        lines.append("### Local Lane Table")
        lines.append("")
        lines.append("| Obligation | Return start | Upward lane | Rework instruction |")
        lines.append("|------------|--------------|-------------|--------------------|")
        for lane in springboards:
            lines.append(
                f"| `{lane['obligation_id']}` | `{lane['return_start']:02d}` | "
                f"`{lane_text(lane['upward_lane'])}` | {lane['reasoned_update']} |"
            )
        lines.append("")

    lines.extend(
        build_detailed_expansion(
            num,
            formal,
            variants,
            springboards,
            receipts,
            verifiers,
        )
    )
    lines.append("")

    lines.append("## Canonical Formal Spine")
    lines.append("")
    if formal:
        lines.append(strip_title(formal))
    else:
        lines.append("_Canonical formal paper was not found._")
    lines.append("")

    lines.append("## Rework Integration Notes")
    lines.append("")
    lines.append("- Keep the claim-strength tags attached to each theorem or bridge.")
    lines.append("- Import companion variant language only when it strengthens exposition without")
    lines.append("  promoting an open bridge.")
    lines.append("- Treat every obligation row as a routed next-need: verifier, witness, adapter,")
    lines.append("  calibration, documentation pass, or explicit guard.")
    lines.append("- If a CAM/GLM row proposes `partially_closed`, update the paper body and")
    lines.append("  obligation audit together; do not silently mark it closed.")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    nodes = json.loads(read(CAM_NODES)) if CAM_NODES.exists() else []
    closure = json.loads(read(CAM_CLOSURE)) if CAM_CLOSURE.exists() else {}
    manifest = []
    lane_index = []
    for num in range(10, 33):
        fpath = formal_dir(num) / "FORMAL_PAPER.md"
        if not fpath.exists():
            continue
        rework = read(rework_path(num))
        lanes = obligation_springboards(
            num,
            obligation_rows(rework),
            closure_rows_for(num, closure),
        )
        text = build(num, nodes, closure)
        out = OUT / f"{num:02d}_{title_from(read(fpath), f'Paper_{num:02d}').split('-', 1)[-1].strip().replace('/', '_').replace(' ', '_')}_VIRTUOUS.md"
        out.write_text(text, encoding="utf-8")
        manifest.append(
            {
                "paper": num,
                "path": str(out),
                "words": words(text),
                "obligation_springboards": len(lanes),
            }
        )
        lane_index.extend(lanes)
    (OUT / "VIRTUOUS_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    (OUT / "OBLIGATION_SPRINGBOARD_INDEX.json").write_text(
        json.dumps(lane_index, indent=2), encoding="utf-8"
    )
    write_springboard_markdown(lane_index)
    write_reasoning_audit(lane_index)
    write_upward_intake_sections(manifest, lane_index)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
