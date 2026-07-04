"""Harvest Claude/Kimi/MannyAI crystal work as orbital evidence.

This report is intentionally an intake and routing artifact. It does not grade
claims. It identifies external-agent work products, crystal/CAM stores, Kimi
paper/window databases, standards reports, and downloaded paper bundles that
must surround the 00-32 spine as orbital data.
"""

from __future__ import annotations

import json
import sqlite3
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
OUT_MD = ROOT / "AGENT_CRYSTAL_WORK_HARVEST.md"
OUT_JSON = ROOT / "AGENT_CRYSTAL_WORK_HARVEST.json"

CLAUDE_MEMORY = Path(r"C:\Users\nbark\.claude\projects\d--CQE-CMPLX\memory")
KIMI_MANNY = Path(r"D:\DockerContainers\Manny Docker Starter\mannyai")
KIMI_DOCKER = Path(r"D:\DockerContainers\Manny Docker Starter")
MANNYAI = Path(r"D:\MannyAI")
REPO_CAM = Path(r"D:\repo_harvest\_CAM")
REPO_HARVEST = Path(r"D:\repo_harvest")
DOWNLOADS = Path(r"C:\Users\nbark\Downloads")
NOTEBOOK_PAPERS = DOWNLOADS / "Papers-20260626T194053Z-3-001" / "Papers"


KEY_TERMS = [
    "crystal",
    "cam",
    "kimi",
    "claude",
    "manny",
    "nsit",
    "claim",
    "standard",
    "receipt",
    "window",
    "paper",
    "forge",
    "lattice",
    "validation",
    "obligation",
]


def iter_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return [p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts]


def suffix_counts(paths: list[Path]) -> dict[str, int]:
    counts = Counter((p.suffix.lower() or "<none>") for p in paths)
    return dict(sorted(counts.items()))


def keyword_files(root: Path) -> list[str]:
    paths = []
    for path in iter_files(root):
        name = str(path).lower()
        if any(term in name for term in KEY_TERMS):
            paths.append(str(path))
    return sorted(paths)


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return {}


def sqlite_counts(path: Path) -> dict:
    if not path.exists():
        return {"exists": False}
    result = {"exists": True, "tables": {}}
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        tables = [row[0] for row in cur.execute("select name from sqlite_master where type='table'")]
        for table in sorted(tables):
            try:
                count = cur.execute(f'select count(*) from "{table}"').fetchone()[0]
            except sqlite3.Error as exc:
                count = f"error: {exc}"
            result["tables"][table] = count
        con.close()
    except sqlite3.Error as exc:
        result["error"] = str(exc)
    return result


def zip_inventory() -> list[dict]:
    patterns = [
        "Kimi*.zip",
        "*MannyAI*.zip",
        "*Crystal*.zip",
    ]
    files: set[Path] = set()
    for pattern in patterns:
        files.update(DOWNLOADS.glob(pattern))
    if NOTEBOOK_PAPERS.exists():
        files.update(NOTEBOOK_PAPERS.glob("*.zip"))

    rows = []
    for path in sorted(files):
        row = {"path": str(path), "name": path.name, "exists": path.exists()}
        try:
            with zipfile.ZipFile(path) as zf:
                names = zf.namelist()
                row["entry_count"] = len(names)
                row["sample"] = names[:20]
                row["keyword_entry_count"] = sum(
                    1 for name in names if any(term in name.lower() for term in KEY_TERMS)
                )
        except (OSError, zipfile.BadZipFile) as exc:
            row["error"] = str(exc)
        rows.append(row)
    return rows


def notebook_paper_inventory() -> dict:
    files = iter_files(NOTEBOOK_PAPERS)
    selected = []
    for path in files:
        rel = str(path.relative_to(NOTEBOOK_PAPERS))
        lower = rel.lower()
        if any(term in lower for term in KEY_TERMS) or path.suffix.lower() in {".pdf", ".md", ".json", ".csv", ".yaml"}:
            selected.append(rel)
    return {
        "root": str(NOTEBOOK_PAPERS),
        "exists": NOTEBOOK_PAPERS.exists(),
        "file_count": len(files),
        "suffix_counts": suffix_counts(files),
        "selected_count": len(selected),
        "selected_files": sorted(selected)[:300],
    }


def standards_summary() -> dict:
    corpus = read_json(KIMI_MANNY / "standards" / "corpus_conformance_report.json")
    glue = read_json(KIMI_MANNY / "standards" / "glue_report.json")
    suite = read_json(KIMI_MANNY / "standards" / "suite_resolution_report.json")
    windows = read_json(KIMI_MANNY / "brain" / "window_summary.json")
    return {
        "corpus_conformance": {
            "canonical_count": corpus.get("canonical_count"),
            "total_verdicts": corpus.get("report", {}).get("total_verdicts"),
            "by_status": corpus.get("report", {}).get("by_status", {}),
        },
        "glue": {
            "total_obligations": glue.get("total_obligations"),
            "obligations_with_candidates": glue.get("obligations_with_candidates"),
            "coverage_ratio": glue.get("coverage_ratio"),
        },
        "suite_resolution": {
            "paper_count": suite.get("paper_count"),
            "total_items": suite.get("total_items"),
            "resolved_items": suite.get("resolved_items"),
            "unresolved_items": suite.get("unresolved_items"),
            "reworks_indexed": suite.get("reworks_indexed"),
        },
        "brain_windows": {
            "root_window_id": windows.get("root_window_id"),
            "levels": windows.get("levels", []),
        },
    }


def build() -> dict:
    claude_files = iter_files(CLAUDE_MEMORY)
    kimi_files = iter_files(KIMI_MANNY)
    manny_files = iter_files(MANNYAI)
    repo_cam_files = iter_files(REPO_CAM)

    kimi_nodes = list((KIMI_MANNY / "papers" / "nodes").glob("*/manifest.json"))
    kimi_node_dbs = list((KIMI_DOCKER / "database" / "nodes").glob("*/node.db"))
    kimi_window_dbs = list((KIMI_DOCKER / "database" / "windows").glob("*/window.db"))

    repo_cam_db = REPO_CAM / "repo_harvest_cam.db"
    kimi_db = KIMI_DOCKER / "database" / "mannyai.db"

    harvest = {
        "schema": "agent_crystal_work_harvest.v1",
        "sources": {
            "claude_memory": {
                "root": str(CLAUDE_MEMORY),
                "file_count": len(claude_files),
                "suffix_counts": suffix_counts(claude_files),
                "keyword_files": keyword_files(CLAUDE_MEMORY),
            },
            "kimi_mannyai": {
                "root": str(KIMI_MANNY),
                "file_count": len(kimi_files),
                "suffix_counts": suffix_counts(kimi_files),
                "keyword_files": keyword_files(KIMI_MANNY)[:500],
                "paper_node_manifest_count": len(kimi_nodes),
                "node_db_count": len(kimi_node_dbs),
                "window_db_count": len(kimi_window_dbs),
                "standards_summary": standards_summary(),
                "mannyai_db": sqlite_counts(kimi_db),
            },
            "mannyai_current_build": {
                "root": str(MANNYAI),
                "file_count": len(manny_files),
                "suffix_counts": suffix_counts(manny_files),
                "keyword_files": keyword_files(MANNYAI)[:500],
            },
            "repo_harvest_cam": {
                "root": str(REPO_CAM),
                "file_count": len(repo_cam_files),
                "suffix_counts": suffix_counts(repo_cam_files),
                "keyword_files": keyword_files(REPO_CAM),
                "repo_harvest_cam_db": sqlite_counts(repo_cam_db),
            },
            "downloads_notebook_papers": notebook_paper_inventory(),
            "downloaded_zip_payloads": zip_inventory(),
        },
        "routing_implications": [
            {
                "target": "00-32 spine",
                "implication": "Kimi's `papers/nodes` and per-paper node DBs are direct orbital data for the numbered papers and should be cited as paper-brain/local-node evidence.",
            },
            {
                "target": "larger reasoning pyramid",
                "implication": "Kimi's window DBs and `window_summary.json` supply a binary 2/4/8/16/32 window lattice that should be cross-read with the 3/5/7/9 reasoning pyramid.",
            },
            {
                "target": "NSIT / standards",
                "implication": "Kimi's standards suite has 192/192 PASS for canonical 32-paper conformance; use as conformance evidence, not as claim-validity grading.",
            },
            {
                "target": "obligation cross-population",
                "implication": "Kimi's glue report maps 142 obligations with 140 candidate routes; this is a high-priority queue for paper edits and orbital backlinks.",
            },
            {
                "target": "CAM/crystal architecture",
                "implication": "Claude memory identifies repo harvest CAM as 18 crystals / 224 atoms and MannyAI as CAM+brain+TMN mint target; repo_harvest_cam.db and CMPLXMCP crystal tools need intake as CAM evidence.",
            },
            {
                "target": "MannyAI crystal paper series",
                "implication": "The Downloads NotebookLM bundle contains MannyAI papers 14-38, CAM address grammar, unified crystal manifest, asset mesh, and CAM crystal service assembly; these are not secondary notes and must orbit Papers 16, 20-23, 30-32 plus NP-05/NP-07/NP-13.",
            },
        ],
    }
    return harvest


def write_md(harvest: dict) -> None:
    lines = [
        "# Agent Crystal Work Harvest",
        "",
        "This harvest adds Claude, Kimi, MannyAI, repo-harvest CAM, and downloaded crystal-paper work to the orbital review surface. It does not grade claims; it identifies work products and where they must be cross-populated.",
        "",
        "## Source Counts",
        "",
        "| Source | Files | Key counts |",
        "|---|---:|---|",
    ]
    sources = harvest["sources"]
    kimi = sources["kimi_mannyai"]
    standards = kimi["standards_summary"]
    lines.append(
        f"| Claude memory | {sources['claude_memory']['file_count']} | keyword files: {len(sources['claude_memory']['keyword_files'])} |"
    )
    lines.append(
        f"| Kimi MannyAI starter | {kimi['file_count']} | paper manifests: {kimi['paper_node_manifest_count']}; node DBs: {kimi['node_db_count']}; window DBs: {kimi['window_db_count']} |"
    )
    lines.append(
        f"| D:/MannyAI current build | {sources['mannyai_current_build']['file_count']} | keyword files: {len(sources['mannyai_current_build']['keyword_files'])} |"
    )
    lines.append(
        f"| Repo harvest CAM | {sources['repo_harvest_cam']['file_count']} | keyword files: {len(sources['repo_harvest_cam']['keyword_files'])} |"
    )
    notebook = sources["downloads_notebook_papers"]
    lines.append(
        f"| Downloads NotebookLM/MannyAI papers | {notebook['file_count']} | selected files: {notebook['selected_count']} |"
    )
    lines.append(
        f"| Downloaded Kimi/Manny/Crystal zip payloads | {len(sources['downloaded_zip_payloads'])} | entries indexed inside archives |"
    )
    lines.append("")

    lines.append("## Kimi Standards And Windows")
    lines.append("")
    lines.append(
        f"- Corpus conformance: canonical papers `{standards['corpus_conformance']['canonical_count']}`, verdicts `{standards['corpus_conformance']['total_verdicts']}`, statuses `{standards['corpus_conformance']['by_status']}`."
    )
    lines.append(
        f"- Glue/obligation coverage: `{standards['glue']['obligations_with_candidates']}` of `{standards['glue']['total_obligations']}` obligations have candidates, coverage `{standards['glue']['coverage_ratio']}`."
    )
    lines.append(
        f"- Suite resolution: `{standards['suite_resolution']['resolved_items']}` of `{standards['suite_resolution']['total_items']}` items resolved across `{standards['suite_resolution']['paper_count']}` papers."
    )
    window_levels = standards["brain_windows"]["levels"]
    if window_levels:
        window_text = ", ".join(
            f"{level.get('count')}x size-{level.get('size')}" for level in window_levels
        )
        lines.append(f"- Brain/window lattice: `{standards['brain_windows']['root_window_id']}` with {window_text}.")
    lines.append("")

    lines.append("## Downloaded Zip Payloads")
    lines.append("")
    lines.append("| Zip | Entries | Keyword entries | Sample |")
    lines.append("|---|---:|---:|---|")
    for row in sources["downloaded_zip_payloads"]:
        sample = "; ".join(row.get("sample", [])[:5])
        lines.append(
            f"| `{row['name']}` | {row.get('entry_count', 0)} | {row.get('keyword_entry_count', 0)} | {sample} |"
        )
    lines.append("")

    lines.append("## Required Routing Implications")
    lines.append("")
    for item in harvest["routing_implications"]:
        lines.append(f"- **{item['target']}:** {item['implication']}")
    lines.append("")

    lines.append("## Immediate Inclusion Queue")
    lines.append("")
    lines.append("- Add `D:\\DockerContainers\\Manny Docker Starter\\mannyai` and the Downloads NotebookLM/MannyAI paper folder to the NSIT inventory roots.")
    lines.append("- Rebuild the NSIT inventory and orbital cross-population audit so these artifacts are counted.")
    lines.append("- Cross-wire Kimi's 2/4/8/16/32 window lattice into the 3/5/7/9 internal reasoning pyramid.")
    lines.append("- Use `glue_report.json` as an obligation candidate queue and `corpus_conformance_report.json` as standards-conformance evidence.")
    lines.append("- Treat downloaded MannyAI papers 14-38 and CAM manifests as orbital papers around the 00-32 spine, especially Papers 16, 20-23, 30-32 and NP-05/NP-07/NP-13.")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    harvest = build()
    OUT_JSON.write_text(json.dumps(harvest, indent=2), encoding="utf-8")
    write_md(harvest)
    print(f"wrote {OUT_MD}")
    print(f"wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
