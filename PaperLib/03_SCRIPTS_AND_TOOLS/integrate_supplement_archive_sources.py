#!/usr/bin/env python3
"""Read the next archive/mirror tranche into supplements and spine references."""
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
SUPPLEMENTS = ROOT / "supplements"
WORKSPACE = Path(r"D:\CQE_CMPLX")
SECTION = "\n## Archive/Mirror Supplement Intake\n"
MAX_SOURCES = 320

ARCHIVE_ROOTS = [
    WORKSPACE / "git-hosted-roots",
    WORKSPACE / "CQECMPLX-Production",
    WORKSPACE / "CMPLX-Kernel",
    WORKSPACE / "g",
    WORKSPACE / "historical_pastworks",
]

PRIORITY_NAME_RE = re.compile(
    r"(paper|whitepaper|proof|formal|claim|receipt|obligation|audit|gap|closure|"
    r"supplement|workbook|summary|ontology|ledger|standard_model|metaforge|"
    r"spectre|crystal|cam|projector)",
    re.IGNORECASE,
)

SUPPLEMENT_MAP = {
    "SM_BRIDGE_SUPPLEMENT.md": {
        "targets": [3, 13, 15, 17, 19, 29],
        "keywords": [
            "standard model",
            "su(5)",
            "su5",
            "u(1)",
            "su(2)",
            "su(3)",
            "charge",
            "anomaly",
            "ckm",
            "pmns",
            "higgs",
            "electroweak",
            "quark",
        ],
    },
    "CRYSTAL_CAM_PROJECTOR_SUPPLEMENT.md": {
        "targets": [6, 10, 12, 20, 30, 32],
        "keywords": [
            "cam",
            "crystal",
            "projector",
            "vignette",
            "memory",
            "receipt",
            "ledger",
            "content address",
            "supervisor",
            "cursor",
            "catalog",
        ],
    },
    "METAFORGE_MATERIALS_SUPPLEMENT.md": {
        "targets": [21, 22, 25, 26, 28, 30],
        "keywords": [
            "metaforge",
            "material",
            "materials",
            "pareto",
            "fabrication",
            "manufactur",
            "production",
            "seam",
            "shear",
            "pinch",
            "energy",
        ],
    },
    "SPECTRE_TILING_SUPPLEMENT.md": {
        "targets": [8, 12, 22, 24, 28],
        "keywords": [
            "spectre",
            "tile",
            "tiling",
            "substitution",
            "aperiodic",
            "knight",
            "game",
            "lattice",
            "correction firing",
        ],
    },
    "OBLIGATION_LEDGER_SUPPLEMENT.md": {
        "targets": [6, 10, 11, 20, 29, 32],
        "keywords": [
            "obligation",
            "open",
            "gap",
            "audit",
            "disclaimer",
            "boundary",
            "claim",
            "partial",
            "rejected",
            "honesty",
            "closure",
        ],
    },
    "RECEIPT_VERIFIER_CATALOG.md": {
        "targets": [6, 10, 20, 32],
        "keywords": [
            "receipt",
            "verifier",
            "verify_",
            "proof",
            "formal",
            "theorem",
            "registry",
            "pass",
            "fail",
        ],
    },
    "APPLIED_FORGES_WORKBOOK.md": {
        "targets": [21, 22, 23, 24, 25, 26, 27, 28, 30],
        "keywords": [
            "forge",
            "workbook",
            "protocol",
            "foldforge",
            "knightforge",
            "morphforge",
            "polyforge",
            "candidate",
            "experiment",
            "test ledger",
        ],
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def normalize(text: str) -> str:
    return " ".join(text.replace("\x00", " ").split())


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ").strip() or fallback
    return fallback


def digest(path: Path, text: str, limit: int = 800) -> str:
    if path.suffix.lower() in {".json", ".csv"}:
        return normalize(text[:limit])
    for heading in (
        "Executive Summary",
        "Executive conclusion",
        "Abstract",
        "Summary",
        "Conclusion",
        "Status",
        "Open Obligations",
    ):
        match = re.search(rf"(?im)^##\s+.*{re.escape(heading)}.*$", text)
        if match:
            rest = text[match.end() :].strip()
            para = re.split(r"\n\s*\n", rest, maxsplit=2)[0]
            clean = normalize(para)
            if clean:
                return clean[:limit]
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith("---"):
            lines.append(stripped)
        if len(" ".join(lines)) > limit + 100:
            break
    return normalize(" ".join(lines))[:limit]


def integrated_paths() -> set[str]:
    paths: set[str] = set()
    for manifest in ROOT.glob("*INTEGRATION.json"):
        try:
            data = json.loads(read(manifest))
        except json.JSONDecodeError:
            continue
        for update in data.get("updates", []):
            for source in update.get("sources", []):
                if isinstance(source, dict) and "path" in source:
                    paths.add(str(Path(source["path"]).resolve()).lower())
        for source in data.get("sources", []):
            if isinstance(source, dict) and "path" in source:
                paths.add(str(Path(source["path"]).resolve()).lower())
    for paper in ROOT.glob("*.md"):
        text = read(paper)
        for match in re.finditer(r"`([A-Z]:\\[^`]+)`", text):
            paths.add(str(Path(match.group(1)).resolve()).lower())
    return paths


def candidate_score(path: Path, text: str) -> int:
    blob = f"{path.name} {path.parent.name} {text[:3000]}".lower()
    score = 0
    for terms in SUPPLEMENT_MAP.values():
        for keyword in terms["keywords"]:
            if keyword in blob:
                score += 4
    if re.search(r"\b(paper|whitepaper|proof|formal|claim|receipt|obligation|audit|gap|closure)\b", path.name, re.I):
        score += 10
    if path.suffix.lower() == ".md":
        score += 4
    if "node_modules" in path.parts or "__pycache__" in path.parts:
        score -= 100
    # Prefer human-scale evidence docs over generated megafiles in this pass.
    try:
        size = path.stat().st_size
    except OSError:
        size = 0
    if 500 <= size <= 180_000:
        score += 3
    elif size > 500_000:
        score -= 8
    return score


def route_supplements(path: Path, title: str, text: str) -> set[str]:
    blob = f"{path.name} {path.parent.name} {title} {text[:4000]}".lower()
    routed = set()
    for supplement, spec in SUPPLEMENT_MAP.items():
        if any(keyword in blob for keyword in spec["keywords"]):
            routed.add(supplement)
    if not routed:
        routed.add("OBLIGATION_LEDGER_SUPPLEMENT.md")
    return routed


def route_papers(supplements: set[str], path: Path, title: str, text: str) -> set[int]:
    targets: set[int] = set()
    blob = f"{path.name} {title} {text[:2500]}".lower()
    for match in re.finditer(r"\b(?:paper|p)[-_ ]?0?(\d{1,2})\b", blob):
        num = int(match.group(1))
        if 0 <= num <= 32:
            targets.add(num)
    if targets:
        return {target for target in targets if target_file(target) is not None}

    # Without explicit paper numbers, route only to the most relevant spine owners.
    for supplement in supplements:
        targets.update(SUPPLEMENT_MAP[supplement]["targets"])
    if len(targets) > 12:
        priority = {6, 10, 20, 30, 32}
        targets = targets & priority or set(sorted(targets)[:8])
    return {target for target in targets if target_file(target) is not None}


def collect() -> tuple[list[dict], int]:
    already = integrated_paths()
    candidates = []
    considered = 0
    for archive_root in ARCHIVE_ROOTS:
        if not archive_root.exists():
            continue
        for path in archive_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".csv", ".json"}:
                continue
            if any(part in {".git", "__pycache__", "node_modules", ".venv", "venv"} for part in path.parts):
                continue
            rel = str(path.relative_to(archive_root))
            if not PRIORITY_NAME_RE.search(rel):
                continue
            considered += 1
            resolved = str(path.resolve()).lower()
            if resolved in already:
                continue
            try:
                text = read(path)
            except OSError:
                continue
            score = candidate_score(path, text)
            if score <= 15:
                continue
            title = first_heading(text, path.stem)
            candidates.append((score, path.stat().st_size, path, title, text))
    candidates.sort(key=lambda item: (-item[0], item[1], str(item[2]).lower()))
    sources = []
    seen_payloads: set[str] = set()
    for score, _size, path, title, text in candidates:
        sig = normalize(text[:1200]).lower()
        if sig in seen_payloads:
            continue
        seen_payloads.add(sig)
        supplements = route_supplements(path, title, text)
        targets = route_papers(supplements, path, title, text)
        sources.append(
            {
                "name": path.stem,
                "path": str(path),
                "title": title,
                "score": score,
                "digest": digest(path, text),
                "supplements": sorted(supplements),
                "targets": sorted(targets),
            }
        )
        if len(sources) >= MAX_SOURCES:
            break
    return sources, considered


def card(source: dict) -> list[str]:
    return [
        f"### {source['name']}: {source['title']}",
        "",
        f"- **Source path:** `{source['path']}`",
        f"- **Archive score:** {source['score']}",
        f"- **What it contributes:** {source['digest']}",
        f"- **Routed spine papers:** {', '.join(f'{num:02d}' for num in source['targets'])}",
        "- **Integration action:** keep this as supplement evidence unless it upgrades a "
        "specific spine-paper claim status with a receipt-backed boundary.",
        "",
    ]


def target_file(num: int) -> Path | None:
    matches = sorted(ROOT.glob(f"{num:02d}_*.md"))
    return matches[0] if matches else None


def main() -> None:
    SUPPLEMENTS.mkdir(exist_ok=True)
    sources, considered = collect()
    by_supplement: dict[str, list[dict]] = defaultdict(list)
    by_paper: dict[int, list[dict]] = defaultdict(list)
    for source in sources:
        for supplement in source["supplements"]:
            by_supplement[supplement].append(source)
        for target in source["targets"]:
            by_paper[target].append(source)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_archive_supplement_{stamp}"
    backup.mkdir(parents=True, exist_ok=True)

    for supplement, supplement_sources in sorted(by_supplement.items()):
        path = SUPPLEMENTS / supplement
        if path.exists():
            shutil.copy2(path, backup / supplement)
            original = read(path)
        else:
            original = f"# {Path(supplement).stem.replace('_', ' ').title()}\n"
        section = [
            "",
            "## Archive/Mirror Supplement Intake",
            "",
            "This section records the current controlled archive/mirror read pass. "
            "Cards are intentionally compact: each source remains in its original file, "
            "while this supplement preserves routing, contribution, and claim-boundary use.",
            "",
        ]
        for source in sorted(supplement_sources, key=lambda item: (-item["score"], item["path"])):
            section.extend(card(source))
        idx = original.find(SECTION)
        updated = original[:idx].rstrip() if idx >= 0 else original.rstrip()
        path.write_text(updated + "\n" + "\n".join(section).rstrip() + "\n", encoding="utf-8")

    paper_updates = []
    for target, paper_sources in sorted(by_paper.items()):
        path = target_file(target)
        if path is None:
            continue
        shutil.copy2(path, backup / path.name)
        original = read(path)
        section = [
            "",
            "## Supplement Routing Intake",
            "",
            "This compact routing section points to supplement evidence added during "
            "the archive/mirror read pass. Detailed source cards live in "
            "`D:\\Paper Reworks\\supplements`.",
            "",
        ]
        for source in sorted(paper_sources, key=lambda item: (-item["score"], item["path"]))[:40]:
            section.append(
                f"- `{Path(source['path']).name}` -> "
                f"{', '.join(source['supplements'])}: {source['digest'][:220]}"
            )
        idx = original.find("\n## Supplement Routing Intake\n")
        updated = original[:idx].rstrip() if idx >= 0 else original.rstrip()
        path.write_text(updated + "\n" + "\n".join(section).rstrip() + "\n", encoding="utf-8")
        paper_updates.append({"paper": target, "path": str(path), "source_count": len(paper_sources)})

    manifest = {
        "backup": str(backup),
        "archive_roots": [str(path) for path in ARCHIVE_ROOTS],
        "candidates_considered": considered,
        "sources_read": len(sources),
        "supplements_updated": {name: len(items) for name, items in sorted(by_supplement.items())},
        "papers_updated": paper_updates,
        "sources": sources,
    }
    (ROOT / "ARCHIVE_SUPPLEMENT_SOURCE_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in manifest.items() if k != "sources"}, indent=2))


if __name__ == "__main__":
    main()
