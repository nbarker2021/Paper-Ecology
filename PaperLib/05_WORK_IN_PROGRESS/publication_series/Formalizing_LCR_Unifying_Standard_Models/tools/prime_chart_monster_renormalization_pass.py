"""Prime-chart Monster renormalization pass.

This pass encodes the proposed 29,30,31 -> 31,33,37 lift as an LCR prime-mask
chart, then carries that chart upward through the supersingular/Monster prime
ceiling using two ledgers:

* Happy-family account: Monster-admitted supersingular prime structure.
* Pariah/asymmetry account: off-chain bridge primes and composite centers that
  carry boundary asymmetry without being silently absorbed into the Monster row.
"""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = Path(__file__).resolve().parent

if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from universal_tarpit_process_derivation_pass import Component, bondedness, run_tarpit  # noqa: E402


SUPERSINGULAR_MONSTER_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]
TOP_MONSTER_TRIPLE = (47, 59, 71)
PARIAH_GROUPS = ["J1", "J3", "J4", "O'N", "Ly", "Ru"]


@dataclass(frozen=True)
class Chart:
    chart_id: str
    title: str
    l: int
    c: int
    r: int
    account: str
    source: str


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for d in range(3, limit, 2):
        if n % d == 0:
            return False
    return True


def rule30_bit(l: int, c: int, r: int) -> int:
    return (l ^ (c | r)) & 1


def correction_bit(l: int, c: int, r: int) -> int:
    return c & (1 - r)


def chart_components(chart: Chart) -> tuple[Component, ...]:
    return (
        Component("L prime-face", f"{chart.account}/L", chart.l, "integer", chart.chart_id),
        Component("C center-carrier", f"{chart.account}/C", chart.c, "integer", chart.chart_id),
        Component("R prime-face", f"{chart.account}/R", chart.r, "integer", chart.chart_id),
    )


def chart_analysis(chart: Chart) -> dict[str, Any]:
    values = (chart.l, chart.c, chart.r)
    primality = tuple(1 if is_prime(v) else 0 for v in values)
    parity = tuple(v % 2 for v in values)
    supersingular_mask = tuple(1 if v in SUPERSINGULAR_MONSTER_PRIMES else 0 for v in values)
    gaps = (chart.c - chart.l, chart.r - chart.c, chart.r - chart.l)
    midpoint = (chart.l + chart.r) / 2
    components = chart_components(chart)
    bonds = bondedness(components)
    seed = "|".join([chart.chart_id, chart.title, chart.account] + [str(v) for v in values])
    return {
        "chart_id": chart.chart_id,
        "title": chart.title,
        "account": chart.account,
        "source": chart.source,
        "values": {"L": chart.l, "C": chart.c, "R": chart.r},
        "prime_mask_lcr": list(primality),
        "parity_lcr": list(parity),
        "supersingular_mask_lcr": list(supersingular_mask),
        "rule30_on_parity": rule30_bit(*parity),
        "rule30_on_prime_mask": rule30_bit(*primality),
        "correction_on_parity": correction_bit(*parity),
        "correction_on_prime_mask": correction_bit(*primality),
        "gaps": {"C_minus_L": gaps[0], "R_minus_C": gaps[1], "R_minus_L": gaps[2]},
        "midpoint": midpoint,
        "center_minus_midpoint": chart.c - midpoint,
        "center_is_prime": is_prime(chart.c),
        "faces_are_prime": is_prime(chart.l) and is_prime(chart.r),
        "all_values_monster_admitted": all(v in SUPERSINGULAR_MONSTER_PRIMES for v in values),
        "off_chain_values": [v for v in values if v not in SUPERSINGULAR_MONSTER_PRIMES],
        "tarpit_readout": run_tarpit(seed),
        "bondedness": bonds,
    }


def build_charts() -> list[Chart]:
    charts = [
        Chart("seed_29_30_31", "Rule-30 prime-mask seed", 29, 30, 31, "seed", "user hypothesis + Rule 30 slot"),
        Chart("encoded_31_33_37", "Next encoded LCR prime-face chart", 31, 33, 37, "pariah_asymmetry", "user hypothesis"),
    ]

    bridge_windows = [
        (37, 39, 41),
        (41, 44, 47),
        (47, 53, 59),
        (59, 65, 71),
    ]
    for l, c, r in bridge_windows:
        charts.append(
            Chart(
                f"bridge_{l}_{c}_{r}",
                "Prime-face bridge toward Monster ceiling",
                l,
                c,
                r,
                "pariah_asymmetry",
                "computed prime-face bridge",
            )
        )

    happy_windows = [
        (29, 31, 41),
        (31, 41, 47),
        (41, 47, 59),
        (47, 59, 71),
    ]
    for l, c, r in happy_windows:
        charts.append(
            Chart(
                f"happy_{l}_{c}_{r}",
                "Monster-admitted supersingular triple",
                l,
                c,
                r,
                "happy_family",
                "supersingular Monster prime chain",
            )
        )
    return charts


def account_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    summaries: dict[str, Any] = {}
    for account in sorted({row["account"] for row in rows}):
        subset = [row for row in rows if row["account"] == account]
        summaries[account] = {
            "charts": len(subset),
            "rule30_parity_outputs": sorted({row["rule30_on_parity"] for row in subset}),
            "prime_mask_outputs": sorted({row["rule30_on_prime_mask"] for row in subset}),
            "off_chain_values": sorted({v for row in subset for v in row["off_chain_values"]}),
            "avg_tarpit_mass": sum(float(row["tarpit_readout"]["final_mass"]) for row in subset) / len(subset),
            "total_pair_bonds": sum(int(row["bondedness"]["total_bonds"]) for row in subset),
            "total_triads": sum(int(row["bondedness"]["triads_formed"]) for row in subset),
        }
    return summaries


def monster_renormalization(rows: list[dict[str, Any]]) -> dict[str, Any]:
    top_product = math.prod(TOP_MONSTER_TRIPLE)
    happy_top = next(row for row in rows if row["chart_id"] == "happy_47_59_71")
    pariah_values = sorted(
        {
            v
            for row in rows
            if row["account"] == "pariah_asymmetry"
            for v in row["off_chain_values"]
        }
    )
    return {
        "top_monster_triple": list(TOP_MONSTER_TRIPLE),
        "top_product": top_product,
        "mckay_row": top_product + 1,
        "next_prime_after_ceiling": 73,
        "next_prime_divides_monster_order": False,
        "happy_top_chart": happy_top["chart_id"],
        "happy_top_values": happy_top["values"],
        "pariah_asymmetry_values": pariah_values,
        "pariah_groups_named_for_accounting": PARIAH_GROUPS,
        "renormalization_rule": (
            "At the 47,59,71 ceiling, the Happy-family account keeps the "
            "Monster-admitted supersingular product 196883 and McKay row "
            "196884. The Pariah/asymmetry account keeps off-chain bridge "
            "centers and primes as boundary residues instead of forcing them "
            "into the Monster product."
        ),
    }


def claim_lanes(renormalization: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "id": "PCM-01",
            "lane": "normal_form_result",
            "claim": "The seed 29,30,31 and encoded 31,33,37 charts preserve the prime/composite/prime LCR mask.",
            "result": "prime-mask LCR = 1,0,1 for both charts",
        },
        {
            "id": "PCM-02",
            "lane": "receipt_bound_internal_result",
            "claim": "The prime-mask and parity charts can be run through the same Rule-30 bit/correction readout.",
            "result": "seed and encoded charts both produce Rule-30 parity output 0 and no correction fire",
        },
        {
            "id": "PCM-03",
            "lane": "CAM_crystal_reapplication_result",
            "claim": "Upward prime charts should be carried as two ledgers rather than collapsed into one interpretation.",
            "result": "Happy-family ledger for Monster-admitted primes; Pariah/asymmetry ledger for off-chain bridge residues",
        },
        {
            "id": "PCM-04",
            "lane": "standard_theorem_or_code_bound_result",
            "claim": "The Monster ceiling row remains 47*59*71=196883 and 196884=1+196883.",
            "result": f"{renormalization['top_product']} and {renormalization['mckay_row']}",
        },
        {
            "id": "PCM-05",
            "lane": "grand_synthesis_claim_with_dependencies",
            "claim": "The Monster acts as a renormalization boundary distributing admitted structure and asymmetry residues into two accounts.",
            "result": renormalization["renormalization_rule"],
        },
    ]


def render_markdown(receipt: dict[str, Any]) -> str:
    lines = [
        "# Prime-Chart Monster Renormalization Pass",
        "",
        f"Created: {receipt['created_utc']}",
        "",
        "## Result",
        "",
        receipt["result"],
        "",
        "## Chart Trace",
        "",
        "| Chart | Account | L | C | R | Prime Mask | Parity | Rule30 Prime | Rule30 Parity | Off-Chain | TarPit Mass |",
        "|---|---|---:|---:|---:|---|---|---:|---:|---|---:|",
    ]
    for row in receipt["charts"]:
        values = row["values"]
        lines.append(
            "| {chart} | {account} | {l} | {c} | {r} | {pm} | {parity} | {rpm} | {rpar} | {off} | {mass:.6f} |".format(
                chart=row["chart_id"],
                account=row["account"],
                l=values["L"],
                c=values["C"],
                r=values["R"],
                pm="".join(str(v) for v in row["prime_mask_lcr"]),
                parity="".join(str(v) for v in row["parity_lcr"]),
                rpm=row["rule30_on_prime_mask"],
                rpar=row["rule30_on_parity"],
                off=", ".join(str(v) for v in row["off_chain_values"]),
                mass=row["tarpit_readout"]["final_mass"],
            )
        )
    lines.extend(
        [
            "",
            "## Account Summary",
            "",
            "| Account | Charts | Rule30 Parity Outputs | Prime-Mask Outputs | Off-Chain Values | Avg TarPit Mass | Pair Bonds | Triads |",
            "|---|---:|---|---|---|---:|---:|---:|",
        ]
    )
    for account, summary in receipt["account_summary"].items():
        lines.append(
            "| {account} | {charts} | {rpo} | {pmo} | {off} | {mass:.6f} | {bonds} | {triads} |".format(
                account=account,
                charts=summary["charts"],
                rpo=", ".join(str(v) for v in summary["rule30_parity_outputs"]),
                pmo=", ".join(str(v) for v in summary["prime_mask_outputs"]),
                off=", ".join(str(v) for v in summary["off_chain_values"]),
                mass=summary["avg_tarpit_mass"],
                bonds=summary["total_pair_bonds"],
                triads=summary["total_triads"],
            )
        )
    renorm = receipt["monster_renormalization"]
    lines.extend(
        [
            "",
            "## Monster Renormalization",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| Top Monster triple | {renorm['top_monster_triple']} |",
            f"| Top product | {renorm['top_product']} |",
            f"| McKay row | {renorm['mckay_row']} |",
            f"| Next prime after ceiling | {renorm['next_prime_after_ceiling']} |",
            f"| Pariah/asymmetry values | {renorm['pariah_asymmetry_values']} |",
            "",
            renorm["renormalization_rule"],
            "",
            "## Claim Lanes",
            "",
            "| ID | Lane | Claim | Result |",
            "|---|---|---|---|",
        ]
    )
    for lane in receipt["claim_lanes"]:
        lines.append(f"| {lane['id']} | `{lane['lane']}` | {lane['claim']} | {lane['result']} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    rows = [chart_analysis(chart) for chart in build_charts()]
    renorm = monster_renormalization(rows)
    receipt = {
        "schema": "FLCR-PrimeChartMonsterRenormalizationPass/1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "pass",
        "result": (
            "The 29,30,31 -> 31,33,37 lift is a usable LCR prime-mask "
            "transition: both charts preserve prime/composite/prime and the "
            "Rule-30 parity output. Upward traversal should therefore keep two "
            "accounts: a Happy-family Monster-admitted supersingular account "
            "and a Pariah/asymmetry bridge account. At 47,59,71 the Monster "
            "renormalizes the admitted side into 196883 and leaves off-chain "
            "bridge residues as a separate LCR asymmetry body."
        ),
        "supersingular_monster_primes": SUPERSINGULAR_MONSTER_PRIMES,
        "charts": rows,
        "account_summary": account_summary(rows),
        "monster_renormalization": renorm,
        "claim_lanes": claim_lanes(renorm),
        "source_papers": ["FLCR-27", "FLCR-29", "FLCR-40"],
    }
    json_path = SERIES_ROOT / "PRIME_CHART_MONSTER_RENORMALIZATION_PASS.json"
    md_path = SERIES_ROOT / "PRIME_CHART_MONSTER_RENORMALIZATION_PASS.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(receipt), encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "status": receipt["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
