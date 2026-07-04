#!/usr/bin/env python3
"""Integrate papers_tool_solvers sources into active Paper Reworks drafts."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
SOLVERS = Path(r"D:\CQE_CMPLX\papers_tool_solvers")
TILES = SOLVERS / "integration_papers"
SECTION = "\n## Tool-Solver and Tile Integration Sources\n"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def target_file(num: int) -> Path | None:
    matches = sorted(ROOT.glob(f"{num:02d}_*.md"))
    return matches[0] if matches else None


def remove_prior_section(text: str) -> str:
    idx = text.find(SECTION)
    if idx < 0:
        return text.rstrip()
    return text[:idx].rstrip()


def first_heading(text: str, fallback: str) -> str:
    headings = [line.strip() for line in text.splitlines() if line.startswith("#")]
    if not headings:
        return fallback
    if len(headings) > 1:
        return f"{headings[0].lstrip('# ').strip()} / {headings[1].lstrip('# ').strip()}"
    return headings[0].lstrip("# ").strip()


def digest(text: str) -> str:
    for heading in ("Abstract", "Executive Summary", "Summary", "Foundation", "SECTION"):
        match = re.search(rf"(?im)^##\s+.*{heading}.*$", text)
        if match:
            rest = text[match.end():].strip()
            para = re.split(r"\n\s*\n", rest, maxsplit=2)[0]
            para = " ".join(para.split())
            if para:
                return para[:1000]
    body = " ".join(
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.startswith("#") and not line.startswith("---")
    )
    return body[:1000]


def signal_lines(text: str, limit: int = 8) -> list[str]:
    signals = []
    for line in text.splitlines():
        stripped = " ".join(line.strip().split())
        if not stripped:
            continue
        if re.search(
            r"\b(Axiom|Claim|Theorem|Verification|Boundary|Integration|Tile|κ|Spectre|J₃|SU\\(3\\)|Rule 30|Closure|Mass|Observer)\b",
            stripped,
            re.IGNORECASE,
        ):
            signals.append(stripped)
        if len(signals) >= limit:
            break
    return signals


def route_by_keywords(name: str, title: str, text: str) -> set[int]:
    blob = f"{name} {title} {text[:2500]}".lower()
    targets: set[int] = set()
    if "axiom" in blob or "primitive" in blob or "foundation" in blob:
        targets.add(0)
    if "lcr" in blob or "triality" in blob or "chart completeness" in blob or "su(2)" in blob:
        targets.update([1, 3])
    if "correction" in blob or "c ∧" in blob or "c &" in blob:
        targets.update([2, 12])
    if "j₃" in blob or "j3" in blob or "su(3)" in blob or "quark" in blob or "qcd" in blob:
        targets.update([3, 13])
    if "recursive closure" in blob or "depth ceiling" in blob or "light-cone" in blob:
        targets.update([4, 12, 20])
    if "claim taxonomy" in blob or "gap registry" in blob:
        targets.update([6, 10, 20])
    if "master equation" in blob or "solve operator" in blob:
        targets.update([10, 20, 30])
    if "strong sector" in blob or "lattice tower" in blob:
        targets.update([13, 17])
    if "electroweak" in blob or "higgs" in blob or "mass residue" in blob or "mass =" in blob:
        targets.update([15, 25])
    if "gravity" in blob or "curvature" in blob or "cosmos" in blob:
        targets.update([14, 26])
    if "lattice closure" in blob or "e8" in blob or "leech" in blob:
        targets.update([8, 17])
    if "spectre" in blob or "tile" in blob or "tiling" in blob or "crystal" in blob:
        targets.update([12, 22, 24, 28])
    if "energy" in blob or "κ" in blob or "coupling" in blob:
        targets.update([15, 25, 29])
    if "tarpit" in blob or "computer" in blob or "substitution" in blob:
        targets.update([20, 21, 30])
    if "observer" in blob or "measurement" in blob or "shared center" in blob:
        targets.update([19, 27, 32])
    if "supervisor" in blob or "grand ribbon" in blob or "meta corpus" in blob:
        targets.update([30, 31, 32])
    if "standard model" in blob or "sm =" in blob:
        targets.update([13, 15])
    if "thermodynamics" in blob or "phase transition" in blob or "origami" in blob:
        targets.update([22, 25, 26])
    return {target for target in targets if target_file(target) is not None}


def source_card(source: dict) -> list[str]:
    lines = [
        f"### {source['name']}: {source['title']}",
        "",
        f"- **Source family:** {source['family']}.",
        f"- **Source path:** `{source['path']}`",
        f"- **What it contributes:** {source['digest']}",
    ]
    if source["signals"]:
        lines.append("- **Signals to preserve:**")
        for signal in source["signals"]:
            lines.append(f"  - {signal}")
    lines.append(
        "- **Integration action:** use this source to enrich examples, operational "
        "tooling, tile/crystal correspondences, and applied interpretations while "
        "keeping formal proof boundaries explicit."
    )
    lines.append("")
    return lines


def build_sources() -> list[dict]:
    sources = []
    for path in sorted(SOLVERS.glob("CQE-PAPER-*-ENHANCED.md")):
        text = read(path)
        title = first_heading(text, path.stem)
        targets = route_by_keywords(path.name, title, text)
        sources.append(
            {
                "name": path.stem,
                "family": "papers_tool_solvers enhanced paper",
                "path": str(path),
                "title": title,
                "digest": digest(text),
                "signals": signal_lines(text),
                "targets": sorted(targets),
            }
        )
    for path in sorted(TILES.glob("*.md")):
        text = read(path)
        title = first_heading(text, path.stem)
        targets = route_by_keywords(path.name, title, text)
        sources.append(
            {
                "name": path.stem,
                "family": "universal tile integration paper",
                "path": str(path),
                "title": title,
                "digest": digest(text),
                "signals": signal_lines(text),
                "targets": sorted(targets),
            }
        )
    return sources


def main() -> None:
    sources = build_sources()
    by_target: dict[int, list[dict]] = defaultdict(list)
    for source in sources:
        for target in source["targets"]:
            by_target[target].append(source)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_tool_solver_sources_{stamp}"
    backup.mkdir(parents=True, exist_ok=True)

    updates = []
    for target, target_sources in sorted(by_target.items()):
        path = target_file(target)
        if path is None:
            continue
        original = read(path)
        (backup / path.name).write_text(original, encoding="utf-8")
        lines = [
            "",
            "## Tool-Solver and Tile Integration Sources",
            "",
            "This section integrates enhanced solver papers and universal tile-system "
            "crosswalks. These sources are especially useful for operational examples, "
            "tile/crystal analogies, applied geometry, and concrete tool obligations.",
            "",
        ]
        for source in sorted(target_sources, key=lambda item: (item["family"], item["name"])):
            lines.extend(source_card(source))
        updated = remove_prior_section(original) + "\n" + "\n".join(lines).rstrip() + "\n"
        path.write_text(updated, encoding="utf-8")
        updates.append(
            {
                "paper": target,
                "path": str(path),
                "source_count": len(target_sources),
                "sources": [source["name"] for source in target_sources],
            }
        )

    manifest = {
        "backup": str(backup),
        "sources_read": len(sources),
        "papers_updated": len(updates),
        "updates": updates,
    }
    (ROOT / "TOOL_SOLVER_TILE_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
