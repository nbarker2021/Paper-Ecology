"""Damascus TarPit folding pass.

The universal process atlas emits forms. This pass treats those emitted forms
as the next input layer, folds them back through TarPit, and repeats. Each fold
records TarPit readout, bondedness, crystal nearest-neighbor, and residual/load
metadata so the emitted form can be used again.
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = Path(__file__).resolve().parent

if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from universal_tarpit_process_derivation_pass import (  # noqa: E402
    Component,
    bondedness,
    nearest_crystals,
    process_feature_vector,
    run_tarpit,
)


@dataclass(frozen=True)
class EmittedForm:
    form_id: str
    title: str
    fold_index: int
    source_ids: tuple[str, ...]
    components: tuple[Component, ...]


def load_seed_forms() -> list[EmittedForm]:
    path = SERIES_ROOT / "UNIVERSAL_TARPIT_PROCESS_DERIVATION_PASS.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    forms: list[EmittedForm] = []
    for process in data["processes"]:
        residuals = process["target_residuals"]
        compared = sum(1 for row in residuals if row["status"] == "compared")
        external = len(residuals) - compared
        nearest = process["nearest_crystal_forms"][0] if process["nearest_crystal_forms"] else {"distance": 0.0}
        components = (
            Component("process_tarpit_mass", "emission/mass", float(process["tarpit_readout"]["final_mass"]), "TarPit mass", process["process_id"]),
            Component("process_pair_bonds", "emission/bonds", float(process["bondedness"]["total_bonds"]), "count", process["process_id"]),
            Component("process_pair_triads", "emission/triads", float(process["bondedness"]["triads_formed"]), "count", process["process_id"]),
            Component("nearest_crystal_distance", "emission/crystal-distance", float(nearest["distance"]), "distance", process["process_id"]),
            Component("compared_targets", "emission/closed-targets", float(compared), "count", process["process_id"]),
            Component("external_adapter_rows", "emission/open-targets", float(external), "count", process["process_id"]),
        )
        forms.append(
            EmittedForm(
                form_id=f"seed::{process['process_id']}",
                title=process["title"],
                fold_index=0,
                source_ids=(process["process_id"],),
                components=components,
            )
        )
    return forms


def analyze_form(form: EmittedForm) -> dict[str, Any]:
    seed = "|".join(
        [form.form_id, form.title, str(form.fold_index)]
        + [f"{c.name}:{c.role}:{c.value}:{c.unit}:{c.source}" for c in form.components]
    )
    tarpit = run_tarpit(seed)
    bonds = bondedness(form.components)
    feature = process_feature_vector(form.components, bonds, tarpit)
    nearest = nearest_crystals(feature)
    emission_mass = float(tarpit["final_mass"]) + float(bonds["avg_mass"]) + float(bonds["triads_formed"]) / max(1, len(form.components))
    open_load = sum(c.value for c in form.components if "open" in c.role or "external" in c.role)
    closed_load = sum(c.value for c in form.components if "closed" in c.role or "triad" in c.role or "bond" in c.role)
    return {
        "form_id": form.form_id,
        "title": form.title,
        "fold_index": form.fold_index,
        "source_ids": list(form.source_ids),
        "component_count": len(form.components),
        "components": [c.__dict__ for c in form.components],
        "tarpit_readout": tarpit,
        "bondedness": bonds,
        "feature_vector": feature,
        "nearest_crystal_forms": nearest,
        "emission_mass": emission_mass,
        "open_load": open_load,
        "closed_load": closed_load,
    }


def emit_next_forms(rows: list[dict[str, Any]], fold_index: int) -> list[EmittedForm]:
    next_forms: list[EmittedForm] = []
    for row in rows:
        nearest = row["nearest_crystal_forms"][0] if row["nearest_crystal_forms"] else {"crystal": "none", "distance": 0.0}
        components = (
            Component("fold_tarpit_mass", "fold/mass", float(row["tarpit_readout"]["final_mass"]), "TarPit mass", row["form_id"]),
            Component("fold_emission_mass", "fold/emission", float(row["emission_mass"]), "fold mass", row["form_id"]),
            Component("fold_pair_bonds", "fold/bonds", float(row["bondedness"]["total_bonds"]), "count", row["form_id"]),
            Component("fold_triads", "fold/triads", float(row["bondedness"]["triads_formed"]), "count", row["form_id"]),
            Component("fold_open_load", "fold/open-load", float(row["open_load"]), "count", row["form_id"]),
            Component("fold_closed_load", "fold/closed-load", float(row["closed_load"]), "count", row["form_id"]),
            Component(f"nearest_crystal::{nearest['crystal']}", "fold/crystal", float(nearest["distance"]), "distance", row["form_id"]),
        )
        next_forms.append(
            EmittedForm(
                form_id=f"fold-{fold_index:02d}::{row['form_id']}",
                title=f"Fold {fold_index} emission of {row['title']}",
                fold_index=fold_index,
                source_ids=tuple(row["source_ids"] + [row["form_id"]]),
                components=components,
            )
        )
    return next_forms


def fold_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    masses = [float(row["tarpit_readout"]["final_mass"]) for row in rows]
    emission = [float(row["emission_mass"]) for row in rows]
    opens = [float(row["open_load"]) for row in rows]
    return {
        "forms": len(rows),
        "successes": sum(1 for row in rows if row["tarpit_readout"]["success"]),
        "avg_tarpit_mass": statistics.fmean(masses) if masses else 0.0,
        "min_tarpit_mass": min(masses) if masses else 0.0,
        "max_tarpit_mass": max(masses) if masses else 0.0,
        "avg_emission_mass": statistics.fmean(emission) if emission else 0.0,
        "total_pair_bonds": sum(int(row["bondedness"]["total_bonds"]) for row in rows),
        "total_pair_triads": sum(int(row["bondedness"]["triads_formed"]) for row in rows),
        "open_load_sum": sum(opens),
        "nearest_crystals": sorted({row["nearest_crystal_forms"][0]["crystal"] for row in rows if row["nearest_crystal_forms"]}),
    }


def run_folds(iterations: int = 5) -> dict[str, Any]:
    forms = load_seed_forms()
    folds: list[dict[str, Any]] = []
    previous_summary: dict[str, Any] | None = None
    for fold_index in range(iterations + 1):
        rows = [analyze_form(form) for form in forms]
        summary = fold_summary(rows)
        if previous_summary:
            summary["delta_avg_tarpit_mass"] = summary["avg_tarpit_mass"] - previous_summary["avg_tarpit_mass"]
            summary["delta_avg_emission_mass"] = summary["avg_emission_mass"] - previous_summary["avg_emission_mass"]
            summary["delta_open_load_sum"] = summary["open_load_sum"] - previous_summary["open_load_sum"]
        else:
            summary["delta_avg_tarpit_mass"] = 0.0
            summary["delta_avg_emission_mass"] = 0.0
            summary["delta_open_load_sum"] = 0.0
        folds.append(
            {
                "fold_index": fold_index,
                "meaning": "seed process forms" if fold_index == 0 else "emitted forms folded back through TarPit",
                "summary": summary,
                "forms": rows,
            }
        )
        previous_summary = summary
        forms = emit_next_forms(rows, fold_index + 1)
    return {
        "schema": "FLCR-DamascusTarPitFoldingPass/1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "pass",
        "iterations_after_seed": iterations,
        "claim": (
            "TarPit emissions are recursively re-readable forms. The Damascus pass "
            "folds emitted process forms back through TarPit repeatedly, preserving "
            "lineage while measuring mass, bondedness, crystal proximity, open load, "
            "and closed load at every fold."
        ),
        "folds": folds,
        "global": {
            "fold_layers": len(folds),
            "forms_per_fold": len(folds[0]["forms"]) if folds else 0,
            "total_form_analyses": sum(len(fold["forms"]) for fold in folds),
            "all_success": all(row["tarpit_readout"]["success"] for fold in folds for row in fold["forms"]),
            "final_fold_summary": folds[-1]["summary"] if folds else {},
        },
    }


def render_markdown(receipt: dict[str, Any]) -> str:
    lines = [
        "# Damascus TarPit Folding Pass",
        "",
        f"Created: {receipt['created_utc']}",
        "",
        "## Claim",
        "",
        receipt["claim"],
        "",
        "## Fold Summary",
        "",
        "| Fold | Forms | Avg TarPit Mass | Avg Emission Mass | Pair Bonds | Triads | Open Load | Delta Mass | Crystals |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for fold in receipt["folds"]:
        summary = fold["summary"]
        lines.append(
            "| {fold} | {forms} | {avg:.6f} | {emit:.6f} | {bonds} | {triads} | {open_load:.6f} | {delta:.6f} | {crystals} |".format(
                fold=fold["fold_index"],
                forms=summary["forms"],
                avg=summary["avg_tarpit_mass"],
                emit=summary["avg_emission_mass"],
                bonds=summary["total_pair_bonds"],
                triads=summary["total_pair_triads"],
                open_load=summary["open_load_sum"],
                delta=summary["delta_avg_tarpit_mass"],
                crystals=", ".join(summary["nearest_crystals"]),
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Fold 0 is the emitted universal process atlas. Each later fold converts the previous emissions into new LCR items and reads them again through TarPit. This is the Damascus operation: the same material is folded, bonded, compressed, and re-read while lineage is preserved.",
            "",
            "The result is not a terminal proof by itself. It is the recursive metric surface needed before process-specific physical adapters can claim no-free-parameter predictions.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    receipt = run_folds(iterations=5)
    json_path = SERIES_ROOT / "DAMASCUS_TARPIT_FOLDING_PASS.json"
    md_path = SERIES_ROOT / "DAMASCUS_TARPIT_FOLDING_PASS.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(receipt), encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "global": receipt["global"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
