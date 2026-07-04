"""Build the NSIT paper/evidence inventory for Paper Reworks.

The inventory records artifacts and attachment candidates without trusting
legacy open/closed labels as verdicts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


DEFAULT_ROOTS = [
    Path(r"D:\Paper Reworks"),
    Path(r"D:\CQE_CMPLX\CQE-CMPLX-1T-Production"),
    Path(r"D:\CQE_CMPLX\CMPLX-R30-main\PROOF"),
    Path(r"D:\CQE_CMPLX\historical_pastworks"),
    Path(r"D:\MannyAI"),
    Path(r"D:\DockerContainers\Manny Docker Starter\mannyai"),
    Path(r"C:\Users\nbark\.claude\projects\d--CQE-CMPLX\memory"),
    Path(r"D:\repo_harvest\_CAM"),
    Path(r"C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers"),
]

TEXT_EXTS = {".md", ".txt", ".rst"}
DATA_EXTS = {".json", ".jsonl", ".csv", ".db", ".sqlite", ".sqlite3", ".yaml", ".yml"}
PAPER_EXTS = TEXT_EXTS | {".pdf", ".docx"}
SCRIPT_EXTS = {".py", ".ps1", ".sh"}

SKIP_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    "_backup_before_archive_supplement_20260626_212559",
    "_backup_before_archive_supplement_20260626_212645",
}


@dataclass
class Artifact:
    artifact_id: str
    path: str
    root: str
    name: str
    suffix: str
    size_bytes: int
    sha256: str
    artifact_class: str
    paper_number: str | None = None
    title_hint: str | None = None
    legacy_label_hits: dict[str, int] = field(default_factory=dict)
    attachment_keys: list[str] = field(default_factory=list)


def iter_files(roots: Iterable[Path]) -> Iterable[tuple[Path, Path]]:
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            yield root.parent, root
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            parts = set(path.parts)
            if parts & SKIP_PARTS:
                continue
            yield root, path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(path: Path) -> str:
    name = path.name.lower()
    suffix = path.suffix.lower()
    parent_text = str(path.parent).lower()
    if suffix in SCRIPT_EXTS and path.name.startswith("verify_"):
        return "validator"
    if "validator" in name or "validation" in parent_text:
        return "validator"
    if suffix in DATA_EXTS or "receipt" in name or "receipt" in parent_text:
        return "receipt_or_data"
    if ".claude" in parent_text or "_cam" in parent_text or "crystal" in name:
        return "memory_or_cam"
    if suffix in PAPER_EXTS:
        if re.match(r"^\d{2}[_-]", path.name):
            return "main_line_paper"
        if "supplement" in name or "appendix" in name or "bridge" in name:
            return "supplement"
        if "paper" in name or "formal" in name or "source" in name:
            return "formal_paper"
    return "other"


def paper_number(path: Path) -> str | None:
    text = path.name
    patterns = [
        r"^(?P<n>\d{2})[_-]",
        r"[Pp]aper[_ -]?(?P<n>\d{1,2})\b",
        r"CQE-paper-(?P<n>\d{1,2})\b",
        r"\bP(?P<n>\d{1,2})\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return f"{int(match.group('n')):02d}"
    return None


def title_hint(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_EXTS:
        return None
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for _ in range(40):
                line = f.readline()
                if not line:
                    break
                stripped = line.strip()
                if stripped.startswith("#"):
                    return stripped.lstrip("#").strip()[:180]
    except OSError:
        return None
    return None


def legacy_label_hits(path: Path) -> dict[str, int]:
    if path.suffix.lower() not in TEXT_EXTS | {".json", ".jsonl", ".yaml", ".yml"}:
        return {}
    labels = ["open", "closed", "proved", "pending", "complete", "external_required"]
    try:
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
    except OSError:
        return {}
    hits = {}
    for label in labels:
        count = len(re.findall(rf"\b{re.escape(label)}\b", text))
        if count:
            hits[label] = count
    return hits


def attachment_keys(path: Path, number: str | None, title: str | None) -> list[str]:
    keys = set()
    if number:
        keys.add(f"paper:{number}")
    stem = re.sub(r"[^a-z0-9]+", " ", path.stem.lower())
    for token in stem.split():
        if len(token) >= 5 and token not in {"paper", "source", "formal", "claim"}:
            keys.add(f"token:{token}")
    if title:
        title_norm = re.sub(r"[^a-z0-9]+", " ", title.lower())
        for token in title_norm.split():
            if len(token) >= 5 and token not in {"paper", "source", "formal", "claim"}:
                keys.add(f"token:{token}")
    return sorted(keys)


def build_inventory(roots: list[Path]) -> dict:
    artifacts: list[Artifact] = []
    for root, path in iter_files(roots):
        suffix = path.suffix.lower()
        if suffix not in PAPER_EXTS | DATA_EXTS | SCRIPT_EXTS:
            continue
        try:
            size = path.stat().st_size
            digest = sha256_file(path)
        except OSError:
            continue
        cls = classify(path)
        num = paper_number(path)
        title = title_hint(path)
        artifact_id = digest[:16]
        artifacts.append(
            Artifact(
                artifact_id=artifact_id,
                path=str(path),
                root=str(root),
                name=path.name,
                suffix=suffix,
                size_bytes=size,
                sha256=digest,
                artifact_class=cls,
                paper_number=num,
                title_hint=title,
                legacy_label_hits=legacy_label_hits(path),
                attachment_keys=attachment_keys(path, num, title),
            )
        )

    by_class: dict[str, int] = {}
    by_paper: dict[str, int] = {}
    for artifact in artifacts:
        by_class[artifact.artifact_class] = by_class.get(artifact.artifact_class, 0) + 1
        if artifact.paper_number:
            by_paper[artifact.paper_number] = by_paper.get(artifact.paper_number, 0) + 1

    return {
        "schema": "NSIT_PAPER_EVIDENCE_INVENTORY_v0_1",
        "root_count": len(roots),
        "artifact_count": len(artifacts),
        "by_class": dict(sorted(by_class.items())),
        "by_paper_number": dict(sorted(by_paper.items())),
        "legacy_label_policy": "legacy labels are text signals only, not validity verdicts",
        "artifacts": [asdict(a) for a in artifacts],
    }


def write_markdown(inventory: dict, output: Path) -> None:
    lines = [
        "# NSIT Paper Evidence Inventory",
        "",
        f"Artifacts: {inventory['artifact_count']}",
        "",
        "## By Class",
        "",
        "| Class | Count |",
        "|-------|------:|",
    ]
    for key, value in inventory["by_class"].items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## By Paper Number", "", "| Paper | Artifact count |", "|-------|---------------:|"])
    for key, value in inventory["by_paper_number"].items():
        lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## Policy",
            "",
            inventory["legacy_label_policy"],
            "",
            "See `NSIT_PAPER_EVIDENCE_INVENTORY.json` for the full artifact list.",
            "",
        ]
    )
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", action="append", default=[], help="Additional or replacement root")
    parser.add_argument("--output-json", default=r"D:\Paper Reworks\NSIT_PAPER_EVIDENCE_INVENTORY.json")
    parser.add_argument("--output-md", default=r"D:\Paper Reworks\NSIT_PAPER_EVIDENCE_INVENTORY.md")
    parser.add_argument("--default-roots", action="store_true", help="Include default roots")
    args = parser.parse_args()

    roots = [Path(p) for p in args.root]
    if args.default_roots or not roots:
        roots = DEFAULT_ROOTS + roots

    inventory = build_inventory(roots)
    output_json = Path(args.output_json)
    output_md = Path(args.output_md)
    output_json.write_text(json.dumps(inventory, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(inventory, output_md)
    print(json.dumps({k: inventory[k] for k in ("artifact_count", "by_class")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
