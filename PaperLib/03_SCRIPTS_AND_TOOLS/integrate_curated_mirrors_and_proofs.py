#!/usr/bin/env python3
"""Integrate curated mirror/proof papers into active Paper Reworks drafts."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
KERNEL_PAPERS = Path(r"D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\papers_output")
SUMMARY_PAPERS = Path(r"D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers")
R30_PROOF = Path(r"D:\CQE_CMPLX\CMPLX-R30-main\PROOF")
R30_FORMAL = Path(r"D:\CQE_CMPLX\CMPLX-R30-main\FORMALIZATION")
CLAUDE_EVIDENCE = Path(r"D:\CQE_CMPLX\Claude-Codex-Memory\Claude work\CL-Paper-Evidence-DB")

SECTION = "\n## Curated Mirror and Proof Source Integration\n"
WORD_RE = re.compile(r"\S+")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


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


def digest(text: str, limit: int = 950) -> str:
    for heading in ("Abstract", "Purpose", "Summary", "Overview"):
        match = re.search(rf"(?im)^##\s+.*{heading}.*$", text)
        if match:
            rest = text[match.end():].strip()
            para = re.split(r"\n\s*\n", rest, maxsplit=2)[0]
            para = " ".join(para.split())
            if para:
                return para[:limit]
    body = " ".join(
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.startswith("#") and not line.startswith("---")
    )
    return body[:limit]


def signal_lines(text: str, limit: int = 7) -> list[str]:
    found = []
    for line in text.splitlines():
        stripped = " ".join(line.strip().split())
        if not stripped:
            continue
        if re.search(
            r"\b(Theorem|Claim|Obligation|Open|Boundary|Verifier|Receipt|Falsifier|Invariant|Registry|Proof)\b",
            stripped,
        ):
            if stripped.startswith("|") and "---" in stripped:
                continue
            found.append(stripped)
        if len(found) >= limit:
            break
    return found


def card(source: dict) -> list[str]:
    lines = [
        f"### {source['name']}: {source['title']}",
        "",
        f"- **Source family:** {source['family']}.",
        f"- **Source path:** `{source['path']}`",
        f"- **Source size:** {source['words']} words.",
        f"- **What it contributes:** {source['digest']}",
    ]
    if source["signals"]:
        lines.append("- **Signals to preserve:**")
        for signal in source["signals"]:
            lines.append(f"  - {signal}")
    lines.append(
        "- **Integration action:** reconcile this mirror/proof source with the current "
        "formal spine, adding missing theorem registry, receipt, proof-boundary, or "
        "obligation language without overwriting newer claim-strength guards."
    )
    lines.append("")
    return lines


def add_source(sources: list[dict], path: Path, family: str, targets: set[int]) -> None:
    if not path.exists() or not targets:
        return
    text = read(path)
    sources.append(
        {
            "name": path.stem,
            "family": family,
            "path": str(path),
            "title": first_heading(text, path.stem),
            "words": words(text),
            "digest": digest(text),
            "signals": signal_lines(text),
            "targets": sorted(targets),
        }
    )


def build_sources() -> list[dict]:
    sources: list[dict] = []

    if KERNEL_PAPERS.exists():
        for path in sorted(KERNEL_PAPERS.glob("CQE-paper-*.md")):
            match = re.search(r"CQE-paper-(\d{2})", path.name)
            if match:
                add_source(sources, path, "CMPLX-Kernel lib-forge paper output", {int(match.group(1))})

    summary_targets = {
        "SUMMARY-I-Gluon-at-Center.md": set(range(0, 11)),
        "SUMMARY-II-Folded-Strand-Physics.md": set(range(11, 23)),
        "SUMMARY-III-Computational-Substrates.md": set(range(23, 30)),
        "SUMMARY-IV-Meta-Architecture.md": {30, 31, 32},
        "SUMMARY-IX-Open-Obligations.md": set(range(0, 33)),
        "SUMMARY-V-32-Theorems-Registry.md": set(range(1, 33)),
        "SUMMARY-VI-8-Color-Families.md": {1, 3, 8, 13, 15, 18, 19},
        "SUMMARY-VII-Bilateral-Proof-System.md": {6, 7, 10, 20, 30},
        "SUMMARY-VIII-Substitution-Manifest.md": {12, 20, 21, 22, 30},
        "SUMMARY-X-Single-Observation.md": {19, 27, 31, 32},
    }
    for name, targets in summary_targets.items():
        add_source(sources, SUMMARY_PAPERS / name, "CMPLX-Kernel summary paper", targets)

    r30_map = {
        "01_bijective_su2_doublet.md": {1, 13},
        "02_chart_j3o_isomorphism.md": {3, 13, 17},
        "03_n3_su3_weyl_closure.md": {3, 8, 13},
        "03a_f4_zero_weight_bridge.md": {13, 17},
        "04_relational_qubit_frame_inversion.md": {1, 9, 19},
        "05_monster_moonshine_d4.md": {18, 29},
        "06_von_neumann_isa.md": {10, 19, 30},
        "07_universal_n3_closure.md": {3, 8, 12},
        "08_pi_vacuum_parameter.md": {16, 25},
        "09_transformer_worldsheet.md": {9, 19, 30},
        "10_wow_signal_d4_classical.md": {3, 8},
        "11_pariah_monster_boundary.md": {11, 29},
        "12_physical_constants_invariants.md": {15, 25, 26, 29},
        "13_magic_square_f4_g2.md": {13, 17},
        "14_d12_moonshine_chain.md": {17, 18, 29},
        "15_observer_lattice_chain.md": {8, 17, 19, 32},
        "16_the_digit_rollout.md": {12, 20, 30},
    }
    for name, targets in r30_map.items():
        add_source(sources, R30_PROOF / "papers" / name, "CMPLX-R30 proof paper", targets)

    add_source(sources, R30_PROOF / "theorems" / "THEOREM_REGISTRY.md", "CMPLX-R30 theorem registry", set(range(1, 33)))
    add_source(sources, R30_PROOF / "theorems" / "OPEN_OBLIGATIONS.md", "CMPLX-R30 open obligations", set(range(0, 33)))

    r30_formal_targets = {
        "C_LAYER_TERMINOLOGY.md": {1, 6, 19},
        "CAYLEY_DICKSON_OLOID_NORMAL_FORM.md": {5, 13, 17},
        "CMPLX_R30_INTERNAL_FORMALIZATION_SETUP.md": {10, 12, 20},
        "CONTENTIONS_AND_RESOLUTION_PLAN.md": {6, 10, 20},
        "LEECH_ENUMERATED_GLUE_BOUNDARY.md": {8, 17},
        "PARTSFACTORY_PRODUCTION_INTEGRATION.md": {10, 20, 21, 30},
        "RULE30_PLUS_MINUS_ONE_SHELL.md": {12, 16, 20},
        "SESSION3_SOURCE_GROUNDED_LEDGER.md": {6, 10, 20},
        "TRANSPORT_OBLIGATION_LEDGER.md": {10, 13, 17, 20},
    }
    for name, targets in r30_formal_targets.items():
        add_source(sources, R30_FORMAL / name, "CMPLX-R30 formalization note", targets)

    evidence_targets = {
        "CL-CQE-Paper-00-Foundation.md": {0},
        "CL-CQE-Papers-01-05-C-Form-Chain.md": set(range(1, 6)),
        "CL-CQE-Papers-06-10-Mid-Stack.md": set(range(6, 11)),
        "CL-CQE-Papers-11-20-Higher-Stack.md": set(range(11, 21)),
        "CL-CQE-Papers-21-31-Horizon-Meta.md": set(range(21, 32)),
        "CL-Master-Glossary-Formal-Definitions.md": {0, 1, 6, 10},
        "CL-IRL-Glossary-Extended-Terms.md": {13, 15, 19, 22, 25, 26, 27},
        "CL-Rule-30-P1-Centroid-VOA-Prize-Paper.md": {12, 15, 18},
        "CL-Rule-30-P3-Decomposition-Prize-Paper.md": {10, 12, 20},
        "CL_proof-source-verifiers.md": set(range(0, 33)),
        "CL_proof-source-lattice-forge-inventory.md": {8, 10, 17, 20, 21, 30},
        "CL_proof-source-jordan-j3-octonion.md": {3, 13, 17},
        "CL_production-proof-receipts-and-ribbon-schema.md": {6, 10, 20, 30, 32},
        "CL_production-hamiltonian-source-and-c-sequence.md": {9, 10, 16},
        "CL_production-forge-hierarchy-and-lib-forge-map.md": {10, 20, 21, 22, 30},
        "CL_production-shared-memory-fermionic-ledger.md": {6, 13, 15, 20},
        "CL_production-master-paper-index.md": set(range(0, 33)),
        "CL_production-paper-intent-index-json.md": set(range(0, 33)),
        "CL_production-tool-md-all-papers.md": set(range(0, 33)),
        "CL_production-workbook-md-all-papers.md": set(range(0, 33)),
        "CL_airlock-key-verifier-implementations.md": {10, 12, 17, 20, 30},
    }
    for name, targets in evidence_targets.items():
        add_source(sources, CLAUDE_EVIDENCE / name, "Claude/Codex evidence DB", targets)

    return sources


def main() -> None:
    sources = build_sources()
    by_target: dict[int, list[dict]] = defaultdict(list)
    for source in sources:
        for target in source["targets"]:
            if target_file(target) is not None:
                by_target[target].append(source)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"_backup_before_curated_mirrors_{stamp}"
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
            "## Curated Mirror and Proof Source Integration",
            "",
            "This section pulls in curated mirrors, proof papers, theorem registries, "
            "open-obligation ledgers, and evidence-db surveys that were outside the "
            "main production `00-32` formal-paper folder. Each card is a source to "
            "fold into the main exposition during the next prose pass.",
            "",
        ]
        for source in sorted(target_sources, key=lambda item: (item["family"], item["name"])):
            lines.extend(card(source))
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
    (ROOT / "CURATED_MIRROR_PROOF_INTEGRATION.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
