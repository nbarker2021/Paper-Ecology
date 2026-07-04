#!/usr/bin/env python3
"""Generate a working SYNTHESIS_DRAFT.md from the PAPERS data."""
from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from generate_papers_09_32 import PAPERS, CROSS_CUTTING, OUT


def cluster(name: str, nums: list[int]) -> str:
    selected = [p for p in PAPERS if p["num"] in nums]
    lines = [f"## {name}", ""]
    if not selected:
        lines.append("See the individual rework skeletons for these papers; they were finalized before the 09–32 batch sweep.")
        lines.append("")
        return "\n".join(lines)
    for p in selected:
        lines.append(
            f"**Paper {p['num']:02d} — {p['title']}** (`{p['slug']}.md`) — {p['status_short']}.\n"
        )
        lines.append(f"- Role: {p['role_short']}.")
        lines.append(f"- Main claim(s): {'; '.join(p['claims'])}")
        fail = [v for v in p['verifiers'] if 'fail' in v['result']]
        if fail:
            lines.append(
                f"- Failing/partial receipt(s): {', '.join(f'`{v['receipt']}` ({v['result']})' for v in fail)}"
            )
        eco = [c for c in p['claim_classes'] if 'external_calibration_open' in c[1]]
        if eco:
            lines.append(
                f"- ECO bridges: {', '.join(c[0] for c in eco)}"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    sections = [
        "# CQECMPLX Proper Papers — Synthesis Draft",
        "",
        "This draft is a high-level narrative view of the reworked CQE paper corpus. "
        "For full claim-strength tables, verifier results, and per-paper obligations, see the individual skeletons and `INDEX.md`.",
        "",
        "## 0. Grounding and honesty rule",
        "",
        "Paper 00 establishes the honesty contract: the corpus is a restatement of established mathematics plus one verified connection "
        "(chart → `J_3(𝕆)` T3). Every later claim must be tagged `internal_physics_map_closed`, `external_calibration_open`, or "
        "`interpretive_bridge_named`; no silent promotion is allowed. See `00_Established_Grounding_and_Axiom_Contract.md`.",
        "",
    ]

    sections.append(cluster("1. Core algebraic stack (Papers 01–08)", list(range(1, 9))))
    sections.append(cluster("2. Temporal emergence, master receipt, and CA surface (Papers 09–12)", list(range(9, 13))))
    sections.append(cluster("3. Physical calibration bridges (Papers 13–18)", list(range(13, 19))))
    sections.append(cluster("4. Observer frame, applied Forges, and energy accounting (Papers 19–27)", list(range(19, 28))))
    sections.append(cluster("5. Game lattices, Monster ceiling, and meta-packaging (Papers 28–32)", list(range(28, 33))))

    sections += [
        "## Cross-cutting integrity notes",
        "",
        "The integrity findings from the Papers 09–32 batch read are recorded in `CROSS_CUTTING_INTEGRITY_NOTES.md`. Key items:",
        "",
    ]
    for note in [
        "Receipt-status mismatches: Papers 09–12 have failing or obligation-laden receipts.",
        "Claim-taxonomy tension: `CQE-paper-formal-CLAIM` lists 09–18 as `0 ECO`, but Papers 13 (CKM) and 15 (Higgs mass) contain external-calibration bridges.",
        "R30 umbrella mismatch: `CMPLX-R30-main/PROOF/papers/09_*.md`–`16_*.md` are historical cross-references only.",
        "No AirLock specs for 06–32; source-backup `.25/.50/.75/_UPGRADED.md` variants missing for 09–32.",
    ]:
        sections.append(f"- {note}")
    sections.append("")

    sections += [
        "## Open Obligations Register (summary)",
        "",
        "The full register lives in `INDEX.md`. It currently tracks obligations 00.1–32.4 plus the following cross-cutting items:",
        "",
        "| ID | Obligation | Closure | Status |",
        "|----|------------|---------|--------|",
    ]
    for o in CROSS_CUTTING:
        sections.append(f"| {o['id']} | {o['obligation']} | {o['closure']} | {o['status']} |")
    sections += [
        "",
        "## Next steps",
        "",
        "1. Fix receipt path normalization in Papers 09–11 and decide whether to regenerate or further scope the McKay/P3 claims.",
        "2. Reconcile `CQE-paper-formal-CLAIM` taxonomy so Papers 13 and 15 keep their ECO labels.",
        "3. Close or carry global obligations: O2′ McKay-Thompson parity, O1 W(E8) lookup table, full Moonshine identification, physical-unit/energy bridges.",
        "4. Populate AirLock specs and document missing source-backup variants for Papers 09–32.",
        "",
    ]

    (OUT / "SYNTHESIS_DRAFT.md").write_text("\n".join(sections), encoding="utf-8")
    print("Wrote SYNTHESIS_DRAFT.md.")


if __name__ == "__main__":
    main()
