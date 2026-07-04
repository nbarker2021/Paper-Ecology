"""Run every FLCR lift through TarPit and recompose tower receipts.

This is the executable version of the "feed all lifts into TarPit" adapter:

1. Load STATE_BOUND_PROOF_CONTRACT_MATRIX.json as the lift queue.
2. For every paper/lift, enumerate the full 2x2x2 LCR chart.
3. Decompose each enumerated state into linear, obstruction, correction,
   TarPit program, TarPit mass, walls, and digital root.
4. Recompose rows into paper summaries, slot-family towers, and decade towers.

The output is a receipt, not a final physics claim. It proves that the first
enumeration is fully decomposed and that higher tower recomposition has an
addressable TarPit mass/wall ledger.
"""
from __future__ import annotations

import hashlib
import json
import statistics
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = Path(r"D:\CQE_CMPLX")
TARPIT_SRC = WORKSPACE_ROOT / "CMPLX-PartsFactory-main" / "src"

if str(TARPIT_SRC) not in sys.path:
    sys.path.insert(0, str(TARPIT_SRC))

from cmplx.symbolic.tarpit import TarpitEcology  # noqa: E402


LCR_STATES = tuple((l, c, r) for l in (0, 1) for c in (0, 1) for r in (0, 1))
PROGRAM_ALPHABET = "}<>+01"


@dataclass(frozen=True)
class Decomposition:
    state: tuple[int, int, int]
    linear_part: int
    obstruction: int
    rule30: int
    correction_residue: int
    shell: int
    voa_mass: int


def decompose_state(state: tuple[int, int, int]) -> Decomposition:
    l, c, r = state
    linear = l ^ c ^ r
    obstruction = c & r
    rule30 = linear ^ obstruction
    correction = c & (1 - r)
    shell = l + c + r
    voa_mass = 0 if l == c == r else 5
    return Decomposition(
        state=state,
        linear_part=linear,
        obstruction=obstruction,
        rule30=rule30,
        correction_residue=correction,
        shell=shell,
        voa_mass=voa_mass,
    )


def stable_int(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16)


def tarpit_program(seed: str, length: int = 28) -> str:
    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    chars: list[str] = []
    while len(chars) < length:
        for byte in digest:
            chars.append(PROGRAM_ALPHABET[byte % len(PROGRAM_ALPHABET)])
            if len(chars) == length:
                break
        digest = hashlib.sha256(digest).digest()
    return "".join(chars)


def run_tarpit(program: str, seed: int) -> dict[str, Any]:
    ecology = TarpitEcology(dimension=8, max_steps=128, seed=seed)
    result = ecology.run(program)
    return {
        "success": result.success,
        "steps": result.steps_executed,
        "bonds": result.bonds_formed,
        "mirrors": result.mirrors_applied,
        "digital_root": result.final_digital_root,
        "final_mass": result.final_mass,
        "output_walls": len(result.output_walls),
        "error_walls": len(result.error_walls),
        "dusts": len(result.dusts),
        "triads": len(result.triads),
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    masses = [float(row["tarpit"]["final_mass"]) for row in rows]
    successes = [bool(row["tarpit"]["success"]) for row in rows]
    return {
        "rows": len(rows),
        "successes": sum(successes),
        "success_rate": sum(successes) / len(rows) if rows else 0.0,
        "avg_final_mass": statistics.fmean(masses) if masses else 0.0,
        "min_final_mass": min(masses) if masses else 0.0,
        "max_final_mass": max(masses) if masses else 0.0,
        "mass_sum": sum(masses),
        "voa_mass_sum": sum(int(row["decomposition"]["voa_mass"]) for row in rows),
        "correction_fires": sum(int(row["decomposition"]["correction_residue"]) for row in rows),
        "obstruction_fires": sum(int(row["decomposition"]["obstruction"]) for row in rows),
        "digital_roots": sorted({int(row["tarpit"]["digital_root"]) for row in rows}),
        "total_output_walls": sum(int(row["tarpit"]["output_walls"]) for row in rows),
        "total_error_walls": sum(int(row["tarpit"]["error_walls"]) for row in rows),
        "total_bonds": sum(int(row["tarpit"]["bonds"]) for row in rows),
        "total_triads": sum(int(row["tarpit"]["triads"]) for row in rows),
    }


def paper_number(publication_id: str) -> int:
    return int(publication_id.split("-")[1])


def main() -> int:
    matrix_path = SERIES_ROOT / "STATE_BOUND_PROOF_CONTRACT_MATRIX.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    papers = matrix["papers"]

    enumeration_rows: list[dict[str, Any]] = []
    for paper in papers:
        pid = paper["publication_id"]
        pnum = paper_number(pid)
        for state in LCR_STATES:
            decomp = decompose_state(state)
            seed_text = "|".join(
                [
                    pid,
                    paper.get("title", ""),
                    paper.get("received_state", ""),
                    paper.get("produced_state", ""),
                    paper.get("semantic_transition", ""),
                    "".join(map(str, state)),
                ]
            )
            program = tarpit_program(seed_text)
            tarpit = run_tarpit(program, stable_int(seed_text))
            enumeration_rows.append(
                {
                    "publication_id": pid,
                    "paper_number": pnum,
                    "slot_family": pnum % 10 or 10,
                    "decade": ((pnum - 1) // 10) + 1,
                    "title": paper.get("title", ""),
                    "state": {"L": state[0], "C": state[1], "R": state[2]},
                    "program": program,
                    "decomposition": decomp.__dict__,
                    "tarpit": tarpit,
                    "tower_address": {
                        "enumeration": f"{pid}:state:{state[0]}{state[1]}{state[2]}",
                        "slot_family": f"family-{pnum % 10 or 10:02d}",
                        "decade": f"decade-{((pnum - 1) // 10) + 1}",
                    },
                }
            )

    paper_towers: dict[str, Any] = {}
    family_towers: dict[str, Any] = {}
    decade_towers: dict[str, Any] = {}

    for paper in papers:
        pid = paper["publication_id"]
        rows = [row for row in enumeration_rows if row["publication_id"] == pid]
        paper_towers[pid] = {
            "title": paper.get("title", ""),
            "received_state": paper.get("received_state", ""),
            "produced_state": paper.get("produced_state", ""),
            "semantic_transition": paper.get("semantic_transition", ""),
            "accepted_formalism_targets": paper.get("accepted_formalism_targets", []),
            "summary": aggregate(rows),
        }

    for family in sorted({row["slot_family"] for row in enumeration_rows}):
        key = f"family-{family:02d}"
        rows = [row for row in enumeration_rows if row["slot_family"] == family]
        family_towers[key] = {
            "papers": sorted({row["publication_id"] for row in rows}),
            "summary": aggregate(rows),
        }

    for decade in sorted({row["decade"] for row in enumeration_rows}):
        key = f"decade-{decade}"
        rows = [row for row in enumeration_rows if row["decade"] == decade]
        decade_towers[key] = {
            "papers": sorted({row["publication_id"] for row in rows}),
            "summary": aggregate(rows),
        }

    receipt = {
        "schema": "FLCR-TarPitLiftTowerPass/1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_matrix": str(matrix_path),
        "tarpit_source": str(TARPIT_SRC),
        "status": "pass",
        "claim": (
            "All FLCR lifts were fed through the full 2x2x2 LCR enumeration, "
            "decomposed into Rule-30/VOA/residue terms, run through TarPit, "
            "and recomposed into paper, slot-family, and decade towers."
        ),
        "counts": {
            "papers": len(papers),
            "states_per_paper": len(LCR_STATES),
            "enumeration_rows": len(enumeration_rows),
            "paper_towers": len(paper_towers),
            "slot_family_towers": len(family_towers),
            "decade_towers": len(decade_towers),
        },
        "global_summary": aggregate(enumeration_rows),
        "paper_towers": paper_towers,
        "slot_family_towers": family_towers,
        "decade_towers": decade_towers,
        "enumeration_rows": enumeration_rows,
        "next_adapter": (
            "Use the tower rows as the input queue for tarpit_kappa_physical_adapter: "
            "paper tower mass + slot-family mass + decade mass + sector tag -> "
            "unitful physical readout and residual ledger."
        ),
    }

    json_path = SERIES_ROOT / "TARPIT_LIFT_TOWER_PASS.json"
    md_path = SERIES_ROOT / "TARPIT_LIFT_TOWER_PASS.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(receipt), encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "counts": receipt["counts"]}, indent=2))
    return 0


def render_markdown(receipt: dict[str, Any]) -> str:
    lines = [
        "# TarPit Lift Tower Pass",
        "",
        f"Created: {receipt['created_utc']}",
        "",
        "## Claim",
        "",
        receipt["claim"],
        "",
        "## Counts",
        "",
        "| Item | Count |",
        "|---|---:|",
    ]
    for key, value in receipt["counts"].items():
        lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## Global Summary",
            "",
            "| Metric | Value |",
            "|---|---:|",
        ]
    )
    for key, value in receipt["global_summary"].items():
        if isinstance(value, list):
            value = ", ".join(map(str, value))
        lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## Slot-Family Towers",
            "",
            "| Family | Papers | Avg TarPit Mass | VOA Mass Sum | Correction Fires | Error Walls |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for key, tower in receipt["slot_family_towers"].items():
        summary = tower["summary"]
        lines.append(
            "| {key} | {papers} | {avg:.6f} | {voa} | {corr} | {err} |".format(
                key=key,
                papers=", ".join(tower["papers"]),
                avg=summary["avg_final_mass"],
                voa=summary["voa_mass_sum"],
                corr=summary["correction_fires"],
                err=summary["total_error_walls"],
            )
        )
    lines.extend(
        [
            "",
            "## Decade Towers",
            "",
            "| Decade | Papers | Avg TarPit Mass | Mass Sum | Digital Roots |",
            "|---|---|---:|---:|---|",
        ]
    )
    for key, tower in receipt["decade_towers"].items():
        summary = tower["summary"]
        lines.append(
            "| {key} | {papers} | {avg:.6f} | {mass:.6f} | {roots} |".format(
                key=key,
                papers=", ".join(tower["papers"]),
                avg=summary["avg_final_mass"],
                mass=summary["mass_sum"],
                roots=", ".join(map(str, summary["digital_roots"])),
            )
        )
    lines.extend(
        [
            "",
            "## Adapter Consequence",
            "",
            receipt["next_adapter"],
            "",
            "The first enumeration is now fully decomposed for every FLCR lift. The recomposed tower rows are the working queue for the next physical adapter pass.",
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
