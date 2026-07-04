#!/usr/bin/env python3
"""Integrate the first high-signal unread paper/source tranche."""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
WORKSPACE = Path(r"D:\CQE_CMPLX")

SECTION = "\n## High-Signal Remaining Source Integration\n"

SOURCE_GROUPS = [
    (WORKSPACE / r"kernel\staging\codex\catalog", "kernel catalog and distilled claims", ["**/*.md"]),
    (
        WORKSPACE
        / r"CQE-CMPLX-1T-Production\src\corpus\extracts\promoted-2026-06-19\current-governance",
        "promoted current-governance extract",
        ["**/*.md", "**/*.csv", "**/*.json"],
    ),
    (WORKSPACE / "gap_analysis", "gap-analysis registry and audit", ["**/*.md", "**/*.csv", "**/*.json"]),
    (
        WORKSPACE / r"CQECMPLX-ProofValidatedSuite\EXPOSE-PAPERS",
        "proof-validated expose paper",
        ["*.md", "meta_material_system/*.md", "meta_material_system/*.json"],
    ),
    (WORKSPACE / "CQECMPLX-Formal-Suite", "formal-suite paper ontology", ["*.md", "*/*.md"]),
]

SKIP_PARTS = {
    ".git",
    "__pycache__",
    "receipts",
    "node_modules",
    ".venv",
    "venv",
    "build",
    "dist",
}


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
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ").strip() or fallback
    return fallback


def normalize(text: str) -> str:
    return " ".join(text.replace("\x00", " ").split())


def csv_digest(path: Path, limit: int = 900) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.reader(handle)
            rows = []
            for index, row in enumerate(reader):
                rows.append(" | ".join(cell.strip() for cell in row[:8]))
                if index >= 6:
                    break
    except OSError:
        return ""
    return normalize("; ".join(rows))[:limit]


def json_digest(path: Path, limit: int = 900) -> str:
    try:
        data = json.loads(read(path))
    except (OSError, json.JSONDecodeError):
        return ""
    if isinstance(data, dict):
        keys = ", ".join(str(key) for key in list(data.keys())[:14])
        payload = json.dumps(data, ensure_ascii=False)[:limit]
        return normalize(f"JSON object keys: {keys}. Sample: {payload}")[:limit]
    if isinstance(data, list):
        payload = json.dumps(data[:4], ensure_ascii=False)[:limit]
        return normalize(f"JSON list length {len(data)}. Sample: {payload}")[:limit]
    return normalize(str(data))[:limit]


def digest(path: Path, text: str, limit: int = 900) -> str:
    if path.suffix.lower() == ".csv":
        return csv_digest(path, limit)
    if path.suffix.lower() == ".json":
        return json_digest(path, limit)

    headings = (
        "Executive conclusion",
        "Executive Summary",
        "Abstract",
        "Summary",
        "Closure status",
        "Verification Status",
        "Open Obligations",
        "Statement",
    )
    for heading in headings:
        match = re.search(rf"(?im)^##\s+.*{re.escape(heading)}.*$", text)
        if match:
            rest = text[match.end() :].strip()
            para = re.split(r"\n\s*\n", rest, maxsplit=2)[0]
            clean = normalize(para)
            if clean:
                return clean[:limit]
    body = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("---"):
            continue
        body.append(stripped)
        if len(" ".join(body)) > limit + 200:
            break
    return normalize(" ".join(body))[:limit]


def signal_lines(text: str, limit: int = 8) -> list[str]:
    signals = []
    for line in text.splitlines():
        stripped = normalize(line)
        if not stripped:
            continue
        if re.search(
            r"\b(closed|open|partial|proof|receipt|verif|claim|obligation|gap|"
            r"standard model|su\(5\)|su\(3\)|u\(1\)|e8|lcr|crystal|spectre|"
            r"ontology|expose|formal|boundary|observer|rule 30|t10)\b",
            stripped,
            re.IGNORECASE,
        ):
            signals.append(stripped[:500])
        if len(signals) >= limit:
            break
    return signals


def explicit_paper_targets(blob: str) -> set[int]:
    targets: set[int] = set()
    for match in re.finditer(r"\bP(?:aper)?[-_ ]?0?(\d{1,2})\b", blob, re.IGNORECASE):
        num = int(match.group(1))
        if 0 <= num <= 32:
            targets.add(num)
    for match in re.finditer(r"\bCQE[-_ ]?PAPER[-_ ]?0?(\d{1,3})\b", blob, re.IGNORECASE):
        num = int(match.group(1))
        if 0 <= num <= 32:
            targets.add(num)
        elif num > 32:
            targets.update(formal_suite_map(num))
    for match in re.finditer(r"\bEXPOSE[-_ ]?0?(\d{1,2})\b", blob, re.IGNORECASE):
        num = int(match.group(1))
        if num == 1:
            targets.add(0)
        elif 2 <= num <= 31:
            targets.add(num - 1)
        elif num == 32:
            targets.add(32)
    for match in re.finditer(r"\bP(?:apers?)?[-_ ]?0?(\d{1,2})\s*(?:-|to|–)\s*0?(\d{1,2})\b", blob, re.IGNORECASE):
        start, end = int(match.group(1)), int(match.group(2))
        if 0 <= start <= end <= 32:
            targets.update(range(start, end + 1))
    return targets


def formal_suite_map(num: int) -> set[int]:
    if 0 <= num <= 3:
        return {0, 1, 2, 3}
    if 10 <= num <= 13:
        return {1, 3, 19, 27}
    if 20 <= num <= 23:
        return {4, 8, 12, 20}
    if 30 <= num <= 33:
        return {15, 22, 25, 29}
    if 40 <= num <= 43:
        return {20, 21, 22, 24, 26}
    if 50 <= num <= 53:
        return {19, 27, 32}
    if 60 <= num <= 63:
        return {30, 31, 32}
    if num == 70:
        return {8, 10, 20, 30}
    if 80 <= num <= 83:
        return {3, 13, 14, 15, 19, 30}
    if 90 <= num <= 97:
        return {12, 17, 22, 24, 28}
    if 100 <= num <= 103:
        return {22, 23, 25, 26, 28}
    return set()


def route(path: Path, title: str, text: str, family: str) -> set[int]:
    blob = f"{path.name} {path.parent.name} {family} {title} {text[:5000]}".lower()
    targets = explicit_paper_targets(blob)

    if "00-32" in blob or "all 32" in blob or "paper suite" in blob or "complete index" in blob:
        targets.update([0, 6, 10, 20, 30, 32])
    if "axiom" in blob or "primitive" in blob or "foundation" in blob or "grounding" in blob:
        targets.update([0, 1, 10])
    if "lcr" in blob or "left-center-right" in blob or "triality" in blob:
        targets.update([1, 3, 19, 31])
    if "correction" in blob or "rule 90" in blob or "c ∧" in blob or "c &" in blob:
        targets.update([2, 4, 12])
    if "rule 30" in blob or "rule30" in blob or "center column" in blob:
        targets.update([1, 2, 9, 10, 12, 20])
    if "open obligation" in blob or "gap" in blob or "disclaimer" in blob or "partial" in blob:
        targets.update([6, 10, 11, 12, 20, 29, 32])
    if "receipt" in blob or "verifier" in blob or "verification" in blob or "proof kernel" in blob:
        targets.update([6, 10, 11, 20])
    if "standard model" in blob or "u(1)" in blob or "su(2)" in blob or "su(3)" in blob:
        targets.update([3, 13, 15, 19])
    if "su(5)" in blob or "charge table" in blob or "anomaly cancellation" in blob:
        targets.update([13, 15, 17, 19, 29])
    if "higgs" in blob or "mass residue" in blob or "ckm" in blob or "pmns" in blob:
        targets.update([15, 25, 29])
    if "e8" in blob or "e6" in blob or "e7" in blob or "niemeier" in blob or "leech" in blob:
        targets.update([8, 17, 18, 29])
    if "voa" in blob or "moonshine" in blob or "mckay" in blob or "monster" in blob:
        targets.update([18, 29])
    if "observer" in blob or "measurement" in blob or "face selection" in blob:
        targets.update([19, 27, 32])
    if "hamiltonian" in blob or "time" in blob:
        targets.update([9, 25])
    if "curvature" in blob or "gravity" in blob or "einstein" in blob:
        targets.update([14, 26])
    if "spectre" in blob or "tiling" in blob or "tile" in blob:
        targets.update([12, 22, 24, 28])
    if "crystal" in blob or "crystallization" in blob or "phase transition" in blob:
        targets.update([22, 25, 26, 28, 30])
    if "metaforge" in blob or "material" in blob or "pareto" in blob:
        targets.update([21, 22, 25, 30])
    if "foldforge" in blob or "protein" in blob:
        targets.update([23, 25])
    if "knight" in blob or "game" in blob:
        targets.update([24, 28])
    if "supervisor" in blob or "cursor" in blob or "meta corpus" in blob or "grand ribbon" in blob:
        targets.update([30, 31, 32])
    if "database" in blob or "inventory" in blob or "corpus" in blob or "catalog" in blob:
        targets.update([6, 10, 20, 30, 32])

    return {target for target in targets if 0 <= target <= 32 and target_file(target) is not None}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def collect() -> list[dict]:
    seen: set[Path] = set()
    sources = []
    for folder, family, patterns in SOURCE_GROUPS:
        if not folder.exists():
            continue
        for pattern in patterns:
            for path in sorted(folder.glob(pattern)):
                if not path.is_file() or should_skip(path):
                    continue
                if path.suffix.lower() not in {".md", ".csv", ".json"}:
                    continue
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                text = read(path)
                title = first_heading(text, path.stem) if path.suffix.lower() == ".md" else path.stem
                targets = route(path, title, text, family)
                if not targets:
                    continue
                sources.append(
                    {
                        "name": path.stem,
                        "family": family,
                        "path": str(path),
                        "title": title,
                        "digest": digest(path, text),
                        "signals": signal_lines(text),
                        "targets": sorted(targets),
                    }
                )
    return sources


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
        "- **Integration action:** use this source as a routed springboard for the paper's "
        "claim status, evidence chain, missing-detail repair, and next-obligation language. "
        "Where the source is a registry or audit, prefer its explicit closed/partial/open "
        "status over broader narrative claims."
    )
    lines.append("")
    return lines


def main() -> None:
    sources = collect()
    by_target: dict[int, list[dict]] = defaultdict(list)
    for source in sources:
        for target in source["targets"]:
            by_target[target].append(source)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_high_signal_remaining_{stamp}"
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
            "## High-Signal Remaining Source Integration",
            "",
            "This section integrates the first high-signal tranche of previously unread "
            "paper sources: kernel catalogs, promoted governance extracts, gap audits, "
            "proof-validated EXPOSE papers, and the Formal-Suite ontology. The section "
            "acts as a CAM/crystal springboard: each source is routed to the paper faces "
            "where it can improve claim status, evidence detail, and next-obligation "
            "language.",
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
    (ROOT / "HIGH_SIGNAL_REMAINING_SOURCE_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
