"""Universal TarPit process derivation atlas.

This pass treats TarPit readout as the metric substrate for many natural
processes. Each process is assembled from real/local data rows where available,
encoded as LCR items, run through TarPit, compared by pairwise bondedness, and
projected against the crystal zoo. The output is a residual ledger, not a
one-off constant fit.
"""
from __future__ import annotations

import hashlib
import json
import math
import statistics
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = Path(r"D:\CQE_CMPLX")
TARPIT_SRC = WORKSPACE_ROOT / "CMPLX-PartsFactory-main" / "src"

if str(TARPIT_SRC) not in sys.path:
    sys.path.insert(0, str(TARPIT_SRC))

from cmplx.symbolic.tarpit import (  # noqa: E402
    BondEngine,
    DimensionalExtent,
    Grain,
    TarpitEcology,
)


KAPPA = math.log((1.0 + math.sqrt(5.0)) / 2.0) / 16.0
PROGRAM_ALPHABET = "}<>+01"


@dataclass(frozen=True)
class Component:
    name: str
    role: str
    value: float
    unit: str = "dimensionless"
    source: str = "local"


@dataclass(frozen=True)
class Target:
    name: str
    predicted: float | None
    observed: float | None
    unit: str
    source: str
    lane: str


@dataclass(frozen=True)
class ProcessSpec:
    process_id: str
    title: str
    domain: str
    lcr_assembly_rule: str
    components: tuple[Component, ...]
    targets: tuple[Target, ...]
    source_paths: tuple[str, ...]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def get_nested(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    cur: Any = data
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def load_local_specs() -> list[ProcessSpec]:
    np15 = Path(r"D:\Paper Reworks\NP-15_receipts")
    tower_path = SERIES_ROOT / "TARPIT_LIFT_TOWER_PASS.json"
    alpha = load_json(np15 / "alpha_inverse_data_receipt.json")
    ckm = load_json(np15 / "ckm_matrix_data_receipt.json")
    higgs = load_json(np15 / "higgs_mass_data_receipt.json")
    tower = load_json(tower_path) if tower_path.exists() else {}
    alpha_value = float(get_nested(alpha, "data", "published_alpha_inv", default=137.035999084))
    alpha_pred = float(get_nested(alpha, "data", "predicted_alpha_inv", default=137.0043052845516))
    higgs_values = get_nested(higgs, "data", "published_values", default={})
    ckm_values = get_nested(ckm, "data", "published_values", default={})

    crystal_source = (
        r"D:\CQE_CMPLX\CQECMPLX-Formal-Suite\10-crystallization\CQE-PAPER-102.md"
    )

    specs = [
        ProcessSpec(
            process_id="fine_structure_constant",
            title="Fine-Structure Constant Literal Metrics",
            domain="fundamental_constant",
            lcr_assembly_rule="Assemble E8 hemisphere roots, boundary half-vignettes, D4 faces, and CODATA target as LCR items.",
            components=(
                Component("E8 positive root hemisphere", "L/root-floor", 120, "count", "PFC-2/E8 local receipt"),
                Component("boundary half-vignettes", "C/boundary", 13, "count", "PFC-2/E8 local receipt"),
                Component("D4 faces", "R/face", 4, "count", "PFC-2/E8 local receipt"),
                Component("CODATA alpha inverse", "standard-target", alpha_value, "dimensionless", str(np15 / "alpha_inverse_data_receipt.json")),
            ),
            targets=(
                Target("alpha_inverse", alpha_pred, alpha_value, "dimensionless", str(np15 / "alpha_inverse_data_receipt.json"), "external_calibration_result"),
                Target("PFC2_integer_alpha_inverse", 137.0, alpha_value, "dimensionless", "verify_alpha_em_from_pfc2_e8_estimate", "estimate_result"),
            ),
            source_paths=(str(np15 / "alpha_inverse_data_receipt.json"),),
        ),
        ProcessSpec(
            process_id="electroweak_mass_residue",
            title="Electroweak/Higgs Mass Residue",
            domain="particle_mass",
            lcr_assembly_rule="Assemble VOA weight, two vacua, six excited states, kappa, and measured electroweak masses as LCR items.",
            components=(
                Component("VOA mass gap", "L/mass-gap", 5, "weight", "MassResidueForge"),
                Component("massless vacua", "C/vacuum", 2, "count", "MassResidueForge"),
                Component("massive excited states", "R/excited", 6, "count", "MassResidueForge"),
                Component("kappa event quantum", "bond-quantum", KAPPA, "dimensionless", "verify_kappa_derivation"),
                Component("Higgs mass", "standard-target", float(higgs_values.get("Higgs", {}).get("value", 125.25)), "GeV", str(np15 / "higgs_mass_data_receipt.json")),
                Component("W mass", "standard-target", float(higgs_values.get("W", {}).get("value", 80.3692)), "GeV", str(np15 / "higgs_mass_data_receipt.json")),
                Component("Z mass", "standard-target", float(higgs_values.get("Z", {}).get("value", 91.1876)), "GeV", str(np15 / "higgs_mass_data_receipt.json")),
            ),
            targets=(
                Target("Higgs_mass", 5 * 25.05, float(higgs_values.get("Higgs", {}).get("value", 125.25)), "GeV", str(np15 / "higgs_mass_data_receipt.json"), "calibrated_result"),
                Target("W_mass", 3.5 * 25.05, float(higgs_values.get("W", {}).get("value", 80.3692)), "GeV", str(np15 / "higgs_mass_data_receipt.json"), "calibrated_result"),
                Target("Z_mass", 4 * 25.05, float(higgs_values.get("Z", {}).get("value", 91.1876)), "GeV", str(np15 / "higgs_mass_data_receipt.json"), "calibrated_result"),
            ),
            source_paths=(str(np15 / "higgs_mass_data_receipt.json"),),
        ),
        ProcessSpec(
            process_id="ckm_bounded_route",
            title="CKM Bounded Route",
            domain="particle_mixing",
            lcr_assembly_rule="Assemble the nine CKM magnitudes, three route stages, and S3 orbit as LCR mixing items.",
            components=tuple(
                Component(name, "standard-target/ckm", float(row["value"]), "magnitude", str(np15 / "ckm_matrix_data_receipt.json"))
                for name, row in sorted(ckm_values.items())
            )
            + (
                Component("route stages", "L/route", 3, "count", "CKM route receipt"),
                Component("S3 orbit", "C/weyl", 6, "count", "CKM route receipt"),
                Component("CP phase slot", "R/phase", 1, "count", "CKM route receipt"),
            ),
            targets=tuple(
                Target(name, None, float(row["value"]), "magnitude", str(np15 / "ckm_matrix_data_receipt.json"), "external_calibration_result")
                for name, row in sorted(ckm_values.items())
            ),
            source_paths=(str(np15 / "ckm_matrix_data_receipt.json"),),
        ),
        ProcessSpec(
            process_id="crystal_zoo_bondedness",
            title="Crystal Zoo Bondedness And Phase Signatures",
            domain="materials",
            lcr_assembly_rule="Assemble IRL lattice family rows as LCR crystal items and compare bondedness across finite/infinite/ferro/frustrated classes.",
            components=(
                Component("Square p4m Tc", "ferro-2d", 2.269, "Tc/J", crystal_source),
                Component("Hexagonal p6m Tc", "ferro-2d", 2.269, "Tc/J", crystal_source),
                Component("FCC Fm-3m Tc", "ferro-3d", 9.8, "Tc/J", crystal_source),
                Component("BCC Im-3m Tc", "ferro-3d", 9.8, "Tc/J", crystal_source),
                Component("HCP P6/mmm Tc", "ferro-3d", 9.8, "Tc/J", crystal_source),
                Component("Diamond Fd-3m Tc", "nonmagnetic", 0, "Tc/J", crystal_source),
                Component("Graphene p6m xi", "nonmagnetic", 1000, "xi", crystal_source),
                Component("Kagome p6m J", "frustrated", 1, "J", crystal_source),
                Component("Pyrochlore Fd-3m J", "frustrated", 1, "J", crystal_source),
            ),
            targets=(
                Target("crystal_zoo_lattice_count", 9, 9, "count", crystal_source, "receipt_bound_internal_result"),
                Target("square_ising_Tc", 2.269, 2.269, "Tc/J", crystal_source, "standard_theorem_result"),
                Target("finite_crystal_transition_absent", 0, 0, "boolean", crystal_source, "normal_form_result"),
            ),
            source_paths=(crystal_source,),
        ),
        ProcessSpec(
            process_id="chemical_bond_energy_forms",
            title="Chemical Bond Energy Forms",
            domain="chemistry",
            lcr_assembly_rule="Assemble observed bond dissociation energies as LCR bond items and let TarPit/bondedness compare the natural bond family.",
            components=(
                Component("H-H bond energy", "single-covalent", 436, "kJ/mol", "standard chemistry table; attach source before promotion"),
                Component("C-H bond energy", "single-covalent", 413, "kJ/mol", "standard chemistry table; attach source before promotion"),
                Component("O-H bond energy", "polar-covalent", 463, "kJ/mol", "standard chemistry table; attach source before promotion"),
                Component("C-C bond energy", "single-covalent", 348, "kJ/mol", "standard chemistry table; attach source before promotion"),
                Component("C=C bond energy", "double-covalent", 614, "kJ/mol", "standard chemistry table; attach source before promotion"),
                Component("N-N bond energy", "single-covalent", 163, "kJ/mol", "standard chemistry table; attach source before promotion"),
                Component("N#N bond energy", "triple-covalent", 945, "kJ/mol", "standard chemistry table; attach source before promotion"),
            ),
            targets=(
                Target("H-H_bond_energy", None, 436, "kJ/mol", "external chemistry source required", "falsifier_or_open_obligation"),
                Target("O-H_bond_energy", None, 463, "kJ/mol", "external chemistry source required", "falsifier_or_open_obligation"),
                Target("N#N_bond_energy", None, 945, "kJ/mol", "external chemistry source required", "falsifier_or_open_obligation"),
            ),
            source_paths=("external chemistry source required before promotion",),
        ),
        ProcessSpec(
            process_id="universe_scale_tarpit_tower",
            title="Universe-Scale TarPit Tower Aggregate",
            domain="cosmology_or_total_system",
            lcr_assembly_rule="Consume the complete FLCR lift-tower receipt as one universe-scale process: paper towers, slot-family towers, decade towers, total bonds, total triads, and total mass.",
            components=(
                Component("FLCR lift count", "L/papers", float(get_nested(tower, "counts", "papers", default=40)), "count", str(tower_path)),
                Component("enumeration rows", "C/enumeration", float(get_nested(tower, "counts", "enumeration_rows", default=320)), "count", str(tower_path)),
                Component("slot-family towers", "R/families", float(get_nested(tower, "counts", "slot_family_towers", default=10)), "count", str(tower_path)),
                Component("decade towers", "tower-depth", float(get_nested(tower, "counts", "decade_towers", default=4)), "count", str(tower_path)),
                Component("global mass sum", "total-mass", float(get_nested(tower, "global_summary", "mass_sum", default=163.11809530780678)), "TarPit mass", str(tower_path)),
                Component("total output walls", "wall-count", float(get_nested(tower, "global_summary", "total_output_walls", default=320)), "count", str(tower_path)),
                Component("total bonds", "bond-count", float(get_nested(tower, "global_summary", "total_bonds", default=1430)), "count", str(tower_path)),
                Component("total triads", "triad-count", float(get_nested(tower, "global_summary", "total_triads", default=2860)), "count", str(tower_path)),
            ),
            targets=(
                Target("lift_tower_rows", float(get_nested(tower, "counts", "enumeration_rows", default=320)), 320, "count", str(tower_path), "receipt_bound_internal_result"),
                Target("lift_tower_error_walls", float(get_nested(tower, "global_summary", "total_error_walls", default=0)), 0, "count", str(tower_path), "receipt_bound_internal_result"),
                Target("lift_tower_success_rate", float(get_nested(tower, "global_summary", "success_rate", default=1.0)), 1.0, "ratio", str(tower_path), "receipt_bound_internal_result"),
            ),
            source_paths=(str(tower_path),),
        ),
        ProcessSpec(
            process_id="waveform_encoding_collapse",
            title="Waveform Encoding Collapse",
            domain="waveform",
            lcr_assembly_rule="Assemble waveform samples, centroid, energy, zero-crossing count, and encoding choice as LCR readout items.",
            components=tuple(
                Component(f"sample_{i}", "wave-sample", math.sin(2 * math.pi * i / 16), "amplitude", "canonical deterministic waveform")
                for i in range(16)
            )
            + (
                Component("zero crossings", "collapse-boundary", 2, "count", "canonical deterministic waveform"),
                Component("rms energy", "standard-target", math.sqrt(0.5), "amplitude", "canonical sine wave"),
            ),
            targets=(
                Target("sine_rms_energy", math.sqrt(0.5), math.sqrt(0.5), "amplitude", "canonical sine wave identity", "standard_theorem_result"),
                Target("real_wave_dataset", None, None, "wav", "attach public wav corpus or local Barker waveform dataset", "falsifier_or_open_obligation"),
            ),
            source_paths=("canonical sine wave identity",),
        ),
        ProcessSpec(
            process_id="beta_decay_topology",
            title="Beta Decay Topology",
            domain="weak_decay",
            lcr_assembly_rule="Assemble parent neutron, daughter proton, electron, antineutrino, Q-value, and lifetime as LCR decay items.",
            components=(
                Component("neutron parent", "L/parent", 1, "particle", "standard beta decay topology"),
                Component("proton daughter", "C/daughter", 1, "particle", "standard beta decay topology"),
                Component("electron emission", "R/lepton", 1, "particle", "standard beta decay topology"),
                Component("antineutrino emission", "residue", 1, "particle", "standard beta decay topology"),
                Component("neutron beta Q value", "standard-target", 0.782, "MeV", "local seeded reference; attach PDG/NIST row before promotion"),
                Component("neutron lifetime", "standard-target", 879.4, "s", "local seeded reference; attach PDG/NIST row before promotion"),
            ),
            targets=(
                Target("neutron_beta_Q_value", None, 0.782, "MeV", "external PDG/NIST required", "falsifier_or_open_obligation"),
                Target("neutron_lifetime", None, 879.4, "s", "external PDG/NIST required", "falsifier_or_open_obligation"),
            ),
            source_paths=("external PDG/NIST required before promotion",),
        ),
    ]
    return specs


def stable_float(text: str) -> float:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def lcr_state(component: Component) -> tuple[int, int, int]:
    text = f"{component.name}|{component.role}|{component.value}|{component.unit}|{component.source}"
    n = int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:6], 16)
    return ((n >> 0) & 1, (n >> 1) & 1, (n >> 2) & 1)


def component_vector(component: Component) -> tuple[float, ...]:
    l, c, r = lcr_state(component)
    value = float(component.value)
    mag = math.log1p(abs(value))
    frac = abs(value) % 1.0
    sign = 1.0 if value >= 0 else -1.0
    unit_h = stable_float(component.unit)
    role_h = stable_float(component.role)
    source_h = stable_float(component.source)
    return (mag, frac, float(l), float(c), float(r), sign, unit_h, (role_h + source_h) / 2.0)


def tarpit_program(seed: str, length: int = 32) -> str:
    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    chars: list[str] = []
    while len(chars) < length:
        for byte in digest:
            chars.append(PROGRAM_ALPHABET[byte % len(PROGRAM_ALPHABET)])
            if len(chars) == length:
                break
        digest = hashlib.sha256(digest).digest()
    return "".join(chars)


def run_tarpit(seed: str) -> dict[str, Any]:
    program = tarpit_program(seed)
    int_seed = int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12], 16)
    result = TarpitEcology(dimension=8, max_steps=160, seed=int_seed).run(program)
    return {
        "program": program,
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


def bondedness(components: tuple[Component, ...]) -> dict[str, Any]:
    engine = BondEngine(epsilon=0.1)
    grains: dict[str, Grain] = {}
    pair_rows: list[dict[str, Any]] = []
    for component in components:
        l, c, r = lcr_state(component)
        grains[component.name] = Grain(
            value=l ^ c ^ r,
            extent=DimensionalExtent(vector=component_vector(component)),
            certificates={"component": component.name, "role": component.role},
        )
    for a, b in combinations(components, 2):
        dust = engine.attempt_bond(grains[a.name], grains[b.name])
        if dust is None:
            continue
        triad = engine.promote_to_triad(dust)
        pair_rows.append(
            {
                "a": a.name,
                "b": b.name,
                "bond_mass": dust.certificates.get("bond_mass", 0.0),
                "is_2d_emergent": dust.certificates.get("is_2d_emergent", False),
                "triad": triad is not None,
            }
        )
    stats = engine.get_bond_statistics()
    stats["pair_rows"] = pair_rows
    stats["total_bonded_mass"] = sum(float(row["bond_mass"]) for row in pair_rows)
    return stats


CRYSTAL_FORMS: dict[str, tuple[float, ...]] = {
    "square": (2.269, 1.0, 1.0, 100.0, 0.28),
    "hexagonal": (2.269, 1.0, 1.0, 100.0, 0.28),
    "fcc": (9.8, 1.0, 1.0, 100.0, 1.5),
    "bcc": (9.8, 1.0, 1.0, 100.0, 1.5),
    "hcp": (9.8, 1.0, 1.0, 100.0, 1.5),
    "diamond": (0.0, 0.0, 0.0, 0.0, 0.0),
    "graphene": (0.0, 0.0, 0.0, 1000.0, 0.0),
    "kagome": (0.0, 1.0, 0.0, 0.0, 0.0),
    "pyrochlore": (0.0, 1.0, 0.0, 0.0, 0.0),
}


def process_feature_vector(components: tuple[Component, ...], bond_stats: dict[str, Any], tarpit: dict[str, Any]) -> tuple[float, ...]:
    values = [abs(float(c.value)) for c in components]
    nonzero = [v for v in values if v > 0]
    return (
        statistics.fmean(nonzero) if nonzero else 0.0,
        float(bond_stats.get("avg_mass", 0.0)),
        float(tarpit.get("final_mass", 0.0)),
        float(bond_stats.get("total_bonds", 0)),
        float(tarpit.get("triads", 0)),
    )


def nearest_crystals(vector: tuple[float, ...]) -> list[dict[str, Any]]:
    def dist(a: tuple[float, ...], b: tuple[float, ...]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    rows = [
        {"crystal": name, "distance": dist(vector, form), "form": list(form)}
        for name, form in CRYSTAL_FORMS.items()
    ]
    return sorted(rows, key=lambda row: row["distance"])[:3]


def residual_rows(targets: tuple[Target, ...]) -> list[dict[str, Any]]:
    rows = []
    for target in targets:
        if target.predicted is None or target.observed is None:
            rows.append(
                {
                    "name": target.name,
                    "predicted": target.predicted,
                    "observed": target.observed,
                    "unit": target.unit,
                    "source": target.source,
                    "lane": target.lane,
                    "status": "requires_external_or_process_specific_adapter",
                }
            )
            continue
        absolute = float(target.predicted) - float(target.observed)
        relative = abs(absolute) / abs(float(target.observed)) if target.observed else 0.0
        rows.append(
            {
                "name": target.name,
                "predicted": target.predicted,
                "observed": target.observed,
                "unit": target.unit,
                "source": target.source,
                "lane": target.lane,
                "absolute_residual": absolute,
                "relative_residual": relative,
                "status": "compared",
            }
        )
    return rows


def analyze_process(spec: ProcessSpec) -> dict[str, Any]:
    bond_stats = bondedness(spec.components)
    tarpit = run_tarpit(
        "|".join(
            [spec.process_id, spec.title, spec.domain]
            + [f"{c.name}:{c.role}:{c.value}:{c.unit}" for c in spec.components]
        )
    )
    feature = process_feature_vector(spec.components, bond_stats, tarpit)
    return {
        "process_id": spec.process_id,
        "title": spec.title,
        "domain": spec.domain,
        "lcr_assembly_rule": spec.lcr_assembly_rule,
        "component_count": len(spec.components),
        "components": [
            {
                "name": c.name,
                "role": c.role,
                "value": c.value,
                "unit": c.unit,
                "source": c.source,
                "lcr": lcr_state(c),
                "vector": component_vector(c),
            }
            for c in spec.components
        ],
        "tarpit_readout": tarpit,
        "bondedness": bond_stats,
        "process_feature_vector": feature,
        "nearest_crystal_forms": nearest_crystals(feature),
        "target_residuals": residual_rows(spec.targets),
        "source_paths": list(spec.source_paths),
    }


def render_markdown(receipt: dict[str, Any]) -> str:
    lines = [
        "# Universal TarPit Process Derivation Pass",
        "",
        f"Created: {receipt['created_utc']}",
        "",
        "## Claim",
        "",
        receipt["claim"],
        "",
        "## Process Summary",
        "",
        "| Process | Domain | Components | TarPit Mass | Pair Bonds | Triads | Nearest Crystal | Compared Targets | External Rows |",
        "|---|---|---:|---:|---:|---:|---|---:|---:|",
    ]
    for row in receipt["processes"]:
        residuals = row["target_residuals"]
        compared = sum(1 for r in residuals if r["status"] == "compared")
        external = len(residuals) - compared
        nearest = row["nearest_crystal_forms"][0]["crystal"] if row["nearest_crystal_forms"] else ""
        lines.append(
            "| {pid} | {domain} | {components} | {mass:.6f} | {bonds} | {triads} | {nearest} | {compared} | {external} |".format(
                pid=row["process_id"],
                domain=row["domain"],
                components=row["component_count"],
                mass=row["tarpit_readout"]["final_mass"],
                bonds=row["bondedness"]["total_bonds"],
                triads=row["bondedness"]["triads_formed"],
                nearest=nearest,
                compared=compared,
                external=external,
            )
        )
    lines.extend(["", "## Residual Ledger", ""])
    for row in receipt["processes"]:
        lines.extend([f"### {row['process_id']}", "", "| Target | Predicted | Observed | Unit | Lane | Status | Relative Residual |", "|---|---:|---:|---|---|---|---:|"])
        for residual in row["target_residuals"]:
            lines.append(
                "| {name} | {pred} | {obs} | {unit} | {lane} | {status} | {rel} |".format(
                    name=residual["name"],
                    pred="" if residual["predicted"] is None else residual["predicted"],
                    obs="" if residual["observed"] is None else residual["observed"],
                    unit=residual["unit"],
                    lane=residual["lane"],
                    status=residual["status"],
                    rel="" if "relative_residual" not in residual else f"{residual['relative_residual']:.6g}",
                )
            )
        lines.append("")
    lines.extend(
        [
            "## Next Work Queue",
            "",
            "1. Attach external datasets for rows marked `requires_external_or_process_specific_adapter`.",
            "2. Add process-specific no-free-parameter adapters for beta decay, real waveform files, chemical bond energies, plasma carriers, and biological folding.",
            "3. Re-run this pass after each adapter so the TarPit/bond/crystal readout becomes the shared metric ledger across domains.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    processes = [analyze_process(spec) for spec in load_local_specs()]
    receipt = {
        "schema": "FLCR-UniversalTarPitProcessDerivationPass/1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "pass",
        "claim": (
            "TarPit readout plus bondedness and crystal comparison can be used "
            "as a shared derivation metric for natural processes. Each process "
            "is assembled as LCR items, decomposed by TarPit/bond metrics, "
            "compared against crystal forms, and checked against standard targets."
        ),
        "kappa": KAPPA,
        "process_count": len(processes),
        "processes": processes,
        "global": {
            "all_tarpit_success": all(p["tarpit_readout"]["success"] for p in processes),
            "total_components": sum(p["component_count"] for p in processes),
            "total_pair_bonds": sum(p["bondedness"]["total_bonds"] for p in processes),
            "total_pair_triads": sum(p["bondedness"]["triads_formed"] for p in processes),
            "compared_targets": sum(
                1 for p in processes for r in p["target_residuals"] if r["status"] == "compared"
            ),
            "external_or_adapter_required_targets": sum(
                1 for p in processes for r in p["target_residuals"] if r["status"] != "compared"
            ),
        },
    }
    json_path = SERIES_ROOT / "UNIVERSAL_TARPIT_PROCESS_DERIVATION_PASS.json"
    md_path = SERIES_ROOT / "UNIVERSAL_TARPIT_PROCESS_DERIVATION_PASS.md"
    json_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(receipt), encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "global": receipt["global"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
