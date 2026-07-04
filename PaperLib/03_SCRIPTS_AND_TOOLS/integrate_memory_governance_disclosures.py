#!/usr/bin/env python3
"""Integrate memory, governance, disclosure, and whitepaper sources."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
NOTEBOOK = Path(r"D:\CQE_CMPLX\Claude-Codex-Memory\CX-NotebookLM")
MEMOS = Path(r"D:\CQE_CMPLX\Claude-Codex-Memory\Memos between CL_CX_HM")
CODEX_WORK = Path(r"D:\CQE_CMPLX\Claude-Codex-Memory\Codex work")
DISCLOSURES = Path(r"D:\CQE_CMPLX\CMPLX-R30-main\DISCLOSURES")
WHITEPAPERS = Path(r"D:\CQE_CMPLX\git-hosted-roots\CQECMPLX-Production\Whitepapers")
GOVERNANCE = Path(r"D:\CQE_CMPLX\git-hosted-roots\CQECMPLX-Production\governance\legacy-tracking")

SECTION = "\n## Memory, Governance, Disclosure, and Whitepaper Integration\n"


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


def digest(text: str, limit: int = 850) -> str:
    body = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("---"):
            continue
        body.append(stripped)
        if len(" ".join(body)) > limit:
            break
    return " ".join(body)[:limit]


def signal_lines(text: str, limit: int = 6) -> list[str]:
    signals = []
    for line in text.splitlines():
        stripped = " ".join(line.strip().split())
        if not stripped:
            continue
        if re.search(
            r"\b(boundary|claim|policy|obligation|closed|open|proof|verifier|receipt|canonical|honesty|disclosure|whitepaper|queue|evidence|grounding)\b",
            stripped,
            re.IGNORECASE,
        ):
            signals.append(stripped)
        if len(signals) >= limit:
            break
    return signals


def route(path: Path, title: str, text: str) -> set[int]:
    blob = f"{path.name} {title} {text[:2500]}".lower()
    targets: set[int] = set()

    for match in re.finditer(r"paper[-_ ]?(\d{1,2})|p(\d{2})", blob):
        value = match.group(1) or match.group(2)
        if value is not None:
            num = int(value)
            if 0 <= num <= 32:
                targets.add(num)
    for match in re.finditer(r"papers?[-_ ]?(\d{1,2})[-_ ]?(?:to|-)[-_ ]?(\d{1,2})", blob):
        start, end = int(match.group(1)), int(match.group(2))
        if 0 <= start <= end <= 32:
            targets.update(range(start, end + 1))

    if "00-32" in blob or "all papers" in blob or "master-paper" in blob or "paper suite" in blob:
        targets.update(range(0, 33))
    if "glossary" in blob or "grounding" in blob or "claim taxonomy" in blob:
        targets.update([0, 1, 6, 10])
    if "obligation" in blob or "open" in blob or "disclosure" in blob or "does not claim" in blob:
        targets.update([6, 10, 12, 20, 29, 32])
    if "physics link" in blob or "physical" in blob or "irl data" in blob:
        targets.update([13, 15, 19, 25, 26, 27, 29])
    if "rule30" in blob or "rule 30" in blob or "p3" in blob:
        targets.update([10, 12, 20])
    if "mckay" in blob or "voa" in blob or "moonshine" in blob:
        targets.update([9, 15, 18, 29])
    if "d4" in blob or "j3" in blob or "f2" in blob or "quark" in blob:
        targets.update([3, 8, 13, 17])
    if "paper05" in blob or "paper 05" in blob:
        targets.add(5)
    if "paper08" in blob or "paper 08" in blob:
        targets.add(8)
    if "paper13" in blob or "paper 13" in blob:
        targets.add(13)
    if "paper15" in blob or "paper 15" in blob:
        targets.add(15)
    if "paper29" in blob or "paper 29" in blob:
        targets.add(29)
    if "paper0" in blob or "paper 0" in blob:
        targets.add(0)
    if "whitepaper" in blob or path.name.startswith("WP-"):
        targets.update([0, 3, 10, 13, 15, 20, 30])
    if "product" in blob or "cadforge" in blob or "forge" in blob:
        targets.update([21, 22, 30])
    if "supervisor" in blob or "cursor" in blob or "meta" in blob:
        targets.update([30, 31, 32])

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
        lines.append("- **Policy/provenance signals to preserve:**")
        for signal in source["signals"]:
            lines.append(f"  - {signal}")
    lines.append(
        "- **Integration action:** carry this as provenance, claim-policy, disclosure, "
        "or publication-queue context. Use it to tune the paper's status language "
        "without overriding the formal proof and receipt sections."
    )
    lines.append("")
    return lines


def collect() -> list[dict]:
    families = [
        (NOTEBOOK, "NotebookLM source pack", "*.md"),
        (MEMOS, "CL/CX/HM memo", "*.md"),
        (CODEX_WORK, "Codex work memo", "**/*.md"),
        (DISCLOSURES, "CMPLX-R30 disclosure", "*.md"),
        (WHITEPAPERS, "scientific whitepaper queue", "*.md"),
        (GOVERNANCE, "governance legacy tracking", "*.md"),
    ]
    sources = []
    for folder, family, pattern in families:
        if not folder.exists():
            continue
        for path in sorted(folder.glob(pattern)):
            if not path.is_file():
                continue
            text = read(path)
            title = first_heading(text, path.stem)
            targets = route(path, title, text)
            if not targets:
                continue
            sources.append(
                {
                    "name": path.stem,
                    "family": family,
                    "path": str(path),
                    "title": title,
                    "digest": digest(text),
                    "signals": signal_lines(text),
                    "targets": sorted(targets),
                }
            )
    return sources


def main() -> None:
    sources = collect()
    by_target: dict[int, list[dict]] = defaultdict(list)
    for source in sources:
        for target in source["targets"]:
            by_target[target].append(source)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_memory_governance_{stamp}"
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
            "## Memory, Governance, Disclosure, and Whitepaper Integration",
            "",
            "This section integrates memory memos, disclosure files, governance notes, "
            "and whitepaper queue records. These sources define provenance, claim "
            "policy, publication intent, and honesty boundaries around the technical "
            "paper body.",
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
    (ROOT / "MEMORY_GOVERNANCE_DISCLOSURE_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
