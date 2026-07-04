#!/usr/bin/env python3
"""Integrate source_backup paper variants into active Paper Reworks drafts."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
SOURCE_BACKUP = Path(r"D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\source_backup")
SECTION = "\n## Source Backup Variant Integration\n"
VARIANT_RE = re.compile(
    r"^CQE-paper-(?P<num>\d{2})(?P<variant>(?:\.\d+)?|_UPGRADED|_RECURSIVE_CLOSE)?\.md$"
)


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
        if line.startswith("#"):
            return line.lstrip("# ").strip()
    return fallback


def paragraph_after(text: str, heading: str) -> str:
    match = re.search(rf"(?im)^##\s+.*{re.escape(heading)}.*$", text)
    if not match:
        return ""
    rest = text[match.end():].strip()
    chunks = re.split(r"\n\s*\n", rest, maxsplit=2)
    return " ".join(chunks[0].split()) if chunks else ""


def compact_digest(text: str) -> str:
    for heading in ("Purpose", "Claims", "Abstract", "Next-State Precondition"):
        para = paragraph_after(text, heading)
        if para:
            return para
    body = " ".join(
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.startswith("#")
    )
    return body[:900]


def claim_rows(text: str, limit: int = 6) -> list[str]:
    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if re.search(r"\b(Claim|Theorem|Boundary|Precondition|Obligation|Falsifier|Guard)\b", stripped):
            rows.append(stripped)
        if len(rows) >= limit:
            break
    return rows


def variant_kind(variant: str | None) -> str:
    if not variant:
        return "base alternate source"
    if variant == ".25":
        return "toolkit / operational surface"
    if variant == ".50":
        return "claim contract / boundary surface"
    if variant == ".75":
        return "next-state precondition"
    if variant == "_UPGRADED":
        return "affirmative upgraded phrasing"
    if variant == "_RECURSIVE_CLOSE":
        return "recursive closure pass"
    return variant


def card(path: Path, variant: str | None) -> list[str]:
    text = read(path)
    lines = [
        f"### {path.name}: {first_heading(text, path.stem)}",
        "",
        f"- **Variant role:** {variant_kind(variant)}.",
        f"- **Source path:** `{path}`",
        f"- **Digest to import:** {compact_digest(text)}",
    ]
    rows = claim_rows(text)
    if rows:
        lines.append("- **Claim/boundary lines to preserve:**")
        for row in rows:
            lines.append(f"  - {row}")
    lines.append(
        "- **Integration action:** use this variant to enrich the body language, "
        "examples, preconditions, and boundary statements while preserving the "
        "claim-strength status already established in the main paper."
    )
    lines.append("")
    return lines


def main() -> None:
    variants_by_paper: dict[int, list[tuple[Path, str | None]]] = defaultdict(list)
    for path in sorted(SOURCE_BACKUP.glob("CQE-paper-*.md")):
        match = VARIANT_RE.match(path.name)
        if not match:
            continue
        num = int(match.group("num"))
        variant = match.group("variant") or None
        variants_by_paper[num].append((path, variant))

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_source_backup_variants_{stamp}"
    backup.mkdir(parents=True, exist_ok=True)

    updates = []
    for num, variants in sorted(variants_by_paper.items()):
        target = target_file(num)
        if target is None:
            continue
        original = read(target)
        (backup / target.name).write_text(original, encoding="utf-8")
        lines = [
            "",
            "## Source Backup Variant Integration",
            "",
            "This section imports the remaining source-backup variants for this paper. "
            "The variants are not treated as stronger proof by default; they supply "
            "tooling language, claim contracts, next-state preconditions, upgraded "
            "phrasing, and recursive-closure notes that must be reconciled with the "
            "formal spine and obligation ledger.",
            "",
        ]
        for path, variant in variants:
            lines.extend(card(path, variant))
        updated = remove_prior_section(original) + "\n" + "\n".join(lines).rstrip() + "\n"
        target.write_text(updated, encoding="utf-8")
        updates.append(
            {
                "paper": num,
                "path": str(target),
                "variant_count": len(variants),
                "variants": [path.name for path, _ in variants],
            }
        )

    manifest = {
        "backup": str(backup),
        "papers_updated": len(updates),
        "updates": updates,
    }
    (ROOT / "SOURCE_BACKUP_VARIANT_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
