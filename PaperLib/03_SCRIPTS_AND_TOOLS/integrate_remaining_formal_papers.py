#!/usr/bin/env python3
"""Integrate remaining formal papers into the active Paper Reworks drafts.

This pass reads every non-00..32 formal paper and appends source-integration
cards to the main paper(s) that need the material. It is intentionally
conservative: the source card records what the source shows, what the active
paper must import, and which claim boundary must remain visible.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
FORMAL_ROOT = Path(r"D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal")

WORD_RE = re.compile(r"\S+")
NUMBERED_FORMAL_RE = re.compile(r"^CQE-paper-\d{2}$")
SOURCE_SECTION = "\n## Remaining Formal Source Integration\n"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def first_heading(text: str) -> str:
    headings = [line.strip() for line in text.splitlines() if line.startswith("#")]
    if not headings:
        return "Untitled formal source"
    if len(headings) > 1:
        return f"{headings[0].lstrip('# ').strip()} / {headings[1].lstrip('# ').strip()}"
    return headings[0].lstrip("# ").strip()


def section_paragraph(text: str, name: str) -> str:
    match = re.search(rf"(?im)^##\s+.*{re.escape(name)}.*$", text)
    if not match:
        return ""
    rest = text[match.end():].strip()
    chunks = re.split(r"\n\s*\n", rest, maxsplit=2)
    return " ".join(chunks[0].split()) if chunks else ""


def extract_claimish_lines(text: str, limit: int = 5) -> list[str]:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.search(r"\b(Theorem|Claim|Falsifier|Verifier|Open|Prediction|Receipt)\b", stripped):
            if stripped.startswith("|") and "---" in stripped:
                continue
            lines.append(stripped)
        if len(lines) >= limit:
            break
    return lines


def extract_verifier_targets(text: str, limit: int = 6) -> list[str]:
    targets = []
    for match in re.finditer(r"`([^`]*(?:verify|receipt|test|audit)[^`]*)`", text, re.IGNORECASE):
        value = match.group(1)
        if value not in targets:
            targets.append(value)
        if len(targets) >= limit:
            break
    if targets:
        return targets
    for line in text.splitlines():
        if re.search(r"verify|receipt|test|audit", line, re.IGNORECASE):
            compact = " ".join(line.strip().split())
            if compact and compact not in targets:
                targets.append(compact)
            if len(targets) >= limit:
                break
    return targets


def explicit_targets(source_name: str, title: str) -> set[int]:
    targets: set[int] = set()
    m = re.match(r"CQE-paper-formal-(\d{2})$", source_name)
    if m:
        targets.add(int(m.group(1)))

    name = source_name.lower()
    blob = f"{source_name} {title}".lower()

    if "formal-01" in name or "lcr triality" in blob:
        targets.add(1)
    if "formal-02" in name or "exceptional ladder" in blob:
        targets.update([3, 8, 17])
    if "formal-03" in name or "recursive closure" in blob:
        targets.update([4, 6, 20])
    if "formal-04" in name or "energy triality" in blob:
        targets.update([15, 18, 25, 29])
    if "formal-05" in name or "computational substrate" in blob or "tarpit" in blob:
        targets.update([6, 10, 20, 30])
    if "formal-06" in name or "observer frame" in blob:
        targets.update([19, 27])
    if "formal-07" in name or "meta corpus" in blob or "supervisor cursor" in blob:
        targets.update([30, 31, 32])
    if "formal-08" in name or "completion" in blob:
        targets.update([31, 32])

    if "formal-b" in name or "braid" in blob or "jacobian" in blob:
        targets.update([15, 18, 24, 29])
    if "claim strength" in blob:
        targets.update([0, 6, 10])
    if "glossary" in blob or "notation" in blob:
        targets.update([0])
    if "formal-o" in name or "observer" in blob or "holograph" in blob:
        targets.update([19, 27, 32])
    if "formal-ph" in name or "physicist" in blob or "qcd" in blob:
        targets.update([13, 15, 16, 19, 25, 26, 27, 32])
    if "formal-u" in name or "unification" in blob or "3×3" in blob or "3x3" in blob:
        targets.update([13, 15, 29, 30, 32])
    if "formal-t1" in name or "tiling" in blob:
        targets.update([22, 24, 28])

    if "spectre" in blob:
        targets.update([12, 15, 22])
    if "rule 30" in blob or "r30" in blob or "period-4" in blob:
        targets.update([12, 20])
    if "moonshine" in blob or "voa" in blob or "mckay" in blob:
        targets.update([15, 18, 29])
    if "market" in blob or "strategy" in blob or "trade" in blob:
        targets.update([20, 25, 30])
    if "protein" in blob:
        targets.add(23)
    if "knight" in blob or "game" in blob or "oeis" in blob:
        targets.update([24, 28])
    if "riemann" in blob:
        targets.update([20, 29])
    if "sidecar" in blob or "kernel" in blob or "airlock" in blob or "forgefactory" in blob:
        targets.update([10, 20, 21, 30])

    return {target for target in targets if 0 <= target <= 32}


def target_file(num: int) -> Path | None:
    matches = sorted(ROOT.glob(f"{num:02d}_*.md"))
    return matches[0] if matches else None


def remove_prior_section(text: str) -> str:
    idx = text.find(SOURCE_SECTION)
    if idx < 0:
        return text.rstrip()
    return text[:idx].rstrip()


def source_card(source: dict) -> list[str]:
    lines = [
        f"### {source['name']}: {source['title']}",
        "",
        f"- **Source path:** `{source['path']}`",
        f"- **Source size:** {source['words']} words.",
    ]
    if source["abstract"]:
        lines.append(f"- **What it shows:** {source['abstract']}")
    else:
        lines.append(
            "- **What it shows:** No clean abstract was found; use the title, headings, "
            "claim lines, and verifier surface below as the integration handle."
        )
    if source["claim_lines"]:
        lines.append("- **Claim/guard lines to import:**")
        for claim in source["claim_lines"]:
            lines.append(f"  - {claim}")
    if source["verifiers"]:
        lines.append("- **Verifier/receipt targets:**")
        for verifier in source["verifiers"]:
            lines.append(f"  - `{verifier}`")
    lines.append(
        "- **Integration action:** fold this source into the local definitions, "
        "claim-status ledger, and obligation workups only where it strengthens "
        "the paper without erasing open boundaries."
    )
    lines.append("")
    return lines


def main() -> None:
    sources = []
    for directory in sorted(FORMAL_ROOT.iterdir(), key=lambda path: path.name):
        if not directory.is_dir() or directory.name == "tools":
            continue
        if NUMBERED_FORMAL_RE.match(directory.name):
            continue
        paper = directory / "FORMAL_PAPER.md"
        if not paper.exists():
            continue
        text = read(paper)
        title = first_heading(text)
        source = {
            "name": directory.name,
            "path": str(paper),
            "title": title,
            "words": words(text),
            "abstract": section_paragraph(text, "Abstract"),
            "claim_lines": extract_claimish_lines(text),
            "verifiers": extract_verifier_targets(text),
            "targets": sorted(explicit_targets(directory.name, title)),
        }
        sources.append(source)

    by_target: dict[int, list[dict]] = defaultdict(list)
    for source in sources:
        for target in source["targets"]:
            if target_file(target) is not None:
                by_target[target].append(source)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_remaining_sources_{stamp}"
    backup.mkdir(parents=True, exist_ok=True)

    written = []
    for target, target_sources in sorted(by_target.items()):
        path = target_file(target)
        if path is None:
            continue
        original = read(path)
        (backup / path.name).write_text(original, encoding="utf-8")
        lines = [
            "",
            "## Remaining Formal Source Integration",
            "",
            "This section was added by the remaining-source reading pass. It records "
            "formal papers outside the main `00-32` sequence that contribute "
            "definitions, guards, verifier surfaces, or alternate representations "
            "that the current paper must now carry.",
            "",
        ]
        for source in sorted(target_sources, key=lambda item: item["name"]):
            lines.extend(source_card(source))
        updated = remove_prior_section(original) + "\n" + "\n".join(lines).rstrip() + "\n"
        path.write_text(updated, encoding="utf-8")
        written.append(
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
        "papers_updated": len(written),
        "updates": written,
    }
    (ROOT / "REMAINING_FORMAL_SOURCE_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
