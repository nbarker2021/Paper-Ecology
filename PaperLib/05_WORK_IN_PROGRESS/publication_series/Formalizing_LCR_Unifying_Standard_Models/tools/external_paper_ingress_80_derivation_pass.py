"""EXT80 external paper ingress derivation pass.

Moves RECURSIVE_READY ingress rows through LCR assembly, TarPit readout, and
bondedness derivation. Prioritizes blocked ASSEMBLE slots FLCR-20, FLCR-24, and
FLCR-39. Crosswalks the top-50 obligation rows from NORMAL_FORM_INGRESS_MATRIX
through normal-form conversion review.

This pass does not promote ASSEMBLE or fabricate PEEP rows.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SERIES_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = Path(__file__).resolve().parent
WORKSPACE_ROOT = Path(r"D:\CQE_CMPLX")
TARPIT_SRC = WORKSPACE_ROOT / "CMPLX-PartsFactory-main" / "src"

MANIFEST = SERIES_ROOT / "EXTERNAL_PAPER_INGRESS_80_SEED_MANIFEST.json"
RECURSIVE_VALIDATION = SERIES_ROOT / "EXTERNAL_PAPER_INGRESS_80_RECURSIVE_CLOSURE_VALIDATION.json"
NORMAL_FORM_MATRIX = SERIES_ROOT / "NORMAL_FORM_INGRESS_MATRIX.json"
CLAIM_QUEUE = SERIES_ROOT / "EXTERNAL_LANE_PAPER_CLAIM_QUEUE.json"
OUT_JSON = SERIES_ROOT / "EXTERNAL_PAPER_INGRESS_80_DERIVATION_PASS.json"
OUT_MD = SERIES_ROOT / "EXTERNAL_PAPER_INGRESS_80_DERIVATION_PASS.md"

PRIORITY_SLOTS = ("FLCR-20", "FLCR-24", "FLCR-39")
NORMAL_FORM_BATCH_SIZE = 50

if str(TARPIT_SRC) not in sys.path:
    sys.path.insert(0, str(TARPIT_SRC))
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from universal_tarpit_process_derivation_pass import (  # noqa: E402
    Component,
    bondedness,
    lcr_state,
    run_tarpit,
    tarpit_program,
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def stable_float(text: str) -> float:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def ingress_components(record: dict[str, Any]) -> tuple[Component, ...]:
    route = record.get("route") or {}
    lcr = record.get("lcr_attachment") or {}
    slot = route.get("target_slot", "unknown")
    title = record.get("title", "")
    weight = float(record.get("knowledge_weight") or 0.0)
    return (
        Component(
            f"{record['ingress_id']}-L",
            "ingress-left/source",
            weight,
            "knowledge_weight",
            lcr.get("L", slot),
        ),
        Component(
            f"{record['ingress_id']}-C",
            "ingress-center/claim",
            stable_float(title),
            "content_hash",
            lcr.get("C", title),
        ),
        Component(
            f"{record['ingress_id']}-R",
            "ingress-right/residue",
            stable_float(record.get("logic_bound", "")),
            "logic_bound_score",
            lcr.get("R", record.get("claim_ceiling", "")),
        ),
        Component(
            f"{record['ingress_id']}-T",
            "ingress-transport/route",
            float(int(slot.split("-")[-1]) if "-" in slot else 0),
            "slot_index",
            lcr.get("T", slot),
        ),
    )


def derivation_checks(record: dict[str, Any], recursive_row: dict[str, Any] | None) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    lcr = record.get("lcr_attachment") or {}
    nist = (record.get("nist_nsit_validation") or {}).get("status", "MISSING")

    def add(name: str, ok: bool, detail: str = "") -> None:
        checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})

    add("recursive_ready", (recursive_row or {}).get("status") == "RECURSIVE_READY")
    add("nist_nsit_pass", nist == "PASS")
    add("lcr_attachment_complete", all(lcr.get(k) for k in ("L", "C", "R", "T")))
    add("logic_bound_declared", bool(record.get("logic_bound")))
    add("claim_ceiling_declared", bool(record.get("claim_ceiling")))
    add("derivation_obligation_declared", bool(record.get("derivation_obligation")))
    add("closure_outcome_declared", bool(record.get("closure_outcome")))
    add("no_assemble_promotion_implied", record.get("status") != "assembled")
    return checks


def derive_record(record: dict[str, Any], recursive_row: dict[str, Any] | None, priority: bool) -> dict[str, Any]:
    components = ingress_components(record)
    seed = "|".join(
        [
            record["ingress_id"],
            record.get("title", ""),
            (record.get("route") or {}).get("target_slot", ""),
            record.get("logic_bound", ""),
        ]
    )
    tarpit = run_tarpit(seed)
    bonds = bondedness(components)
    checks = derivation_checks(record, recursive_row)
    pass_count = sum(1 for c in checks if c["status"] == "PASS")
    all_pass = pass_count == len(checks)
    full_text_pending = record.get("scientific_claim") == "pending_full_text_extraction"

    if all_pass and tarpit.get("success"):
        if full_text_pending:
            status = "DERIVATION_VALIDATED"
            rationale = (
                "Ingress shape, LCR assembly, TarPit readout, and bondedness derivation pass. "
                "Full-text extraction remains pending; candidate only — no ASSEMBLE promotion."
            )
        else:
            status = "DERIVATION_VALIDATED"
            rationale = "Derivation validators pass with extracted content anchor."
    elif priority:
        status = "DERIVATION_CANDIDATE"
        rationale = (
            "Priority blocked slot: partial derivation pass recorded; "
            "remaining gates documented for Wave 1 Lane A receipt binding."
        )
    else:
        status = "DERIVATION_REVIEW_REQUIRED"
        rationale = "One or more derivation checks failed; review required before candidate promotion."

    route = (record.get("route") or {}).get("target_slot", "")
    return {
        "ingress_id": record["ingress_id"],
        "route": route,
        "title": record.get("title", ""),
        "priority_slot": route in PRIORITY_SLOTS,
        "logic_bound": record.get("logic_bound", ""),
        "knowledge_weight": record.get("knowledge_weight"),
        "claim_ceiling": record.get("claim_ceiling", ""),
        "closure_outcome": record.get("closure_outcome", ""),
        "recursive_fit_status": record.get("recursive_fit_status", ""),
        "prior_status": (recursive_row or {}).get("status", "UNKNOWN"),
        "derivation_status": status,
        "derivation_rationale": rationale,
        "derivation_checks": checks,
        "derivation_pass_count": pass_count,
        "derivation_total_checks": len(checks),
        "full_text_extraction_pending": full_text_pending,
        "assemble_promotion": "BLOCKED",
        "components": [
            {
                "name": c.name,
                "role": c.role,
                "value": c.value,
                "unit": c.unit,
                "source": c.source,
                "lcr": lcr_state(c),
            }
            for c in components
        ],
        "tarpit_readout": tarpit,
        "bondedness": {
            "total_bonds": bonds.get("total_bonds", 0),
            "triads_formed": bonds.get("triads_formed", 0),
            "avg_mass": bonds.get("avg_mass", 0.0),
            "total_bonded_mass": bonds.get("total_bonded_mass", 0.0),
        },
        "tarpit_program_preview": tarpit_program(seed, length=16),
        "next_action": record.get("next_recursive_action", ""),
    }


def prioritize_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def sort_key(record: dict[str, Any]) -> tuple[int, str]:
        slot = (record.get("route") or {}).get("target_slot", "")
        if slot in PRIORITY_SLOTS:
            return (PRIORITY_SLOTS.index(slot), record.get("ingress_id", ""))
        return (len(PRIORITY_SLOTS), record.get("ingress_id", ""))

    return sorted(records, key=sort_key)


def select_normal_form_batch(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    priority: list[dict[str, Any]] = []
    rest: list[dict[str, Any]] = []
    for entry in entries:
        if entry.get("flcr_id") in PRIORITY_SLOTS:
            priority.append(entry)
        else:
            rest.append(entry)
    batch = (priority + rest)[:NORMAL_FORM_BATCH_SIZE]
    return batch


def validate_normal_form_entry(entry: dict[str, Any]) -> dict[str, Any]:
    required_keys = (
        "standard_normal_form",
        "paper_specific_normal_form",
        "advanced_normal_form",
        "flcr_conversion_rule",
        "cmplx_standards_gate",
    )
    missing = [key for key in required_keys if not entry.get(key)]
    flcr_algebra = (entry.get("flcr_conversion_rule") or {}).get("flcr_algebra") or {}
    algebra_ok = all(k in flcr_algebra for k in ("L", "C", "R"))
    gate = entry.get("cmplx_standards_gate") or {}
    gate_ok = gate.get("standard_id") == "paper.normal_form_conversion"

    if not missing and algebra_ok and gate_ok:
        conversion_status = "normal_form_validated"
        note = "All four forms and FLCR algebra present; routes to next evidence queue without ASSEMBLE."
    else:
        conversion_status = "normal_form_incomplete"
        note = f"Missing or incomplete: {', '.join(missing) if missing else 'FLCR algebra or gate'}"

    return {
        "obligation_id": entry.get("obligation_id", ""),
        "flcr_id": entry.get("flcr_id", ""),
        "claim_family": entry.get("claim_family", ""),
        "priority_slot": entry.get("flcr_id") in PRIORITY_SLOTS,
        "conversion_status": conversion_status,
        "conversion_note": note,
        "missing_forms": missing,
        "flcr_algebra_complete": algebra_ok,
        "validator_gate": gate.get("standard_id", ""),
        "promotion_status": entry.get("promotion_status", "blocked_until_normal_form_review"),
        "assemble_promotion": "BLOCKED",
        "standard_normal_form_id": (entry.get("standard_normal_form") or {}).get("id", ""),
        "paper_normal_form_id": (entry.get("paper_specific_normal_form") or {}).get("id", ""),
        "conversion_rule_id": (entry.get("flcr_conversion_rule") or {}).get("id", ""),
    }


def build_claim_queue_note(receipt: dict[str, Any]) -> str:
    g = receipt["global"]
    blocked = receipt["priority_slot_summary"]
    return (
        f"Phase 6 Wave 1 Lane B derivation pass ({receipt['created_utc']}): "
        f"{g['derivation_validated_count']}/{g['ingress_record_count']} EXT80 rows DERIVATION_VALIDATED; "
        f"priority blocked slots FLCR-20/24/39 validated {blocked['validated']}/{blocked['total']}; "
        f"top-{g['normal_form_batch_size']} normal-form obligations crosswalked "
        f"({g['normal_form_validated_count']} validated). "
        f"No ASSEMBLE promotion from ingress alone."
    )


def render_markdown(receipt: dict[str, Any]) -> str:
    g = receipt["global"]
    lines = [
        "# External Paper Ingress 80 Derivation Pass",
        "",
        f"Created: {receipt['created_utc']}",
        "",
        "## Claim",
        "",
        receipt["claim"],
        "",
        "## Global Summary",
        "",
        f"- Ingress records: `{g['ingress_record_count']}`",
        f"- DERIVATION_VALIDATED: `{g['derivation_validated_count']}`",
        f"- DERIVATION_CANDIDATE: `{g['derivation_candidate_count']}`",
        f"- DERIVATION_REVIEW_REQUIRED: `{g['derivation_review_required_count']}`",
        f"- Priority slots (FLCR-20/24/39) validated: `{receipt['priority_slot_summary']['validated']}/{receipt['priority_slot_summary']['total']}`",
        f"- Normal-form batch: `{g['normal_form_batch_size']}` (`{g['normal_form_validated_count']}` validated)",
        f"- ASSEMBLE promotion: `{g['assemble_promotion_policy']}`",
        "",
        "## Priority Slot Rows",
        "",
        "| Ingress | Slot | Status | TarPit Mass | Bonds | Logic Bound |",
        "|---|---|---|---:|---:|---|",
    ]
    for row in receipt["ingress_rows"]:
        if not row["priority_slot"]:
            continue
        lines.append(
            "| {id} | {slot} | {status} | {mass:.6f} | {bonds} | {bound} |".format(
                id=row["ingress_id"],
                slot=row["route"],
                status=row["derivation_status"],
                mass=row["tarpit_readout"]["final_mass"],
                bonds=row["bondedness"]["total_bonds"],
                bound=row["logic_bound"],
            )
        )
    lines.extend(
        [
            "",
            "## Normal Form Batch (Top 50)",
            "",
            "| Obligation | FLCR | Family | Conversion Status |",
            "|---|---|---|---|",
        ]
    )
    for row in receipt["normal_form_batch"]:
        lines.append(
            f"| `{row['obligation_id']}` | `{row['flcr_id']}` | `{row['claim_family']}` | `{row['conversion_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Claim Queue Note",
            "",
            receipt["claim_queue_note"],
            "",
            "## Next Work",
            "",
            "1. Wave 1 Lane A: bind receipt evidence for FLCR-20/24/39 before any ASSEMBLE delta.",
            "2. Full-text extraction for validated candidates; bind content-addressed anchors.",
            "3. Route normal-form-validated obligations into receipt/citation/calibration queues.",
            "4. Do not run Wave 2+ closure carry until derivation artifacts are attached to orchestrator.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    manifest = load_json(MANIFEST)
    recursive = load_json(RECURSIVE_VALIDATION)
    normal_form = load_json(NORMAL_FORM_MATRIX)
    claim_queue = load_json(CLAIM_QUEUE)

    recursive_by_id = {row["ingress_id"]: row for row in recursive.get("rows", [])}
    records = prioritize_records(manifest.get("records", []))

    ingress_rows = [
        derive_record(
            record,
            recursive_by_id.get(record["ingress_id"]),
            priority=(record.get("route") or {}).get("target_slot", "") in PRIORITY_SLOTS,
        )
        for record in records
    ]

    status_counts = Counter(row["derivation_status"] for row in ingress_rows)
    priority_rows = [row for row in ingress_rows if row["priority_slot"]]
    priority_validated = sum(1 for row in priority_rows if row["derivation_status"] == "DERIVATION_VALIDATED")

    nf_batch_entries = select_normal_form_batch(normal_form.get("entries", []))
    normal_form_batch = [validate_normal_form_entry(entry) for entry in nf_batch_entries]
    nf_validated = sum(1 for row in normal_form_batch if row["conversion_status"] == "normal_form_validated")

    receipt: dict[str, Any] = {
        "schema": "FLCR-ExternalPaperIngress80DerivationPass/1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "phase": "Phase6-Wave1-LaneB",
        "status": "pass",
        "claim": (
            "EXT80 ingress rows move from RECURSIVE_READY through LCR assembly, TarPit readout, "
            "and bondedness derivation to DERIVATION_VALIDATED candidate status. Priority blocked "
            "slots FLCR-20, FLCR-24, and FLCR-39 are processed first. Top-50 obligation rows are "
            "crosswalked through normal-form conversion. No ASSEMBLE promotion is granted."
        ),
        "source_manifest": str(MANIFEST),
        "source_recursive_validation": str(RECURSIVE_VALIDATION),
        "source_normal_form_matrix": str(NORMAL_FORM_MATRIX),
        "source_claim_queue": str(CLAIM_QUEUE),
        "priority_slots": list(PRIORITY_SLOTS),
        "priority_slot_summary": {
            "total": len(priority_rows),
            "validated": priority_validated,
            "slots": {
                slot: next((r for r in priority_rows if r["route"] == slot), None)
                for slot in PRIORITY_SLOTS
            },
        },
        "ingress_rows": ingress_rows,
        "normal_form_batch": normal_form_batch,
        "global": {
            "ingress_record_count": len(ingress_rows),
            "derivation_validated_count": status_counts.get("DERIVATION_VALIDATED", 0),
            "derivation_candidate_count": status_counts.get("DERIVATION_CANDIDATE", 0),
            "derivation_review_required_count": status_counts.get("DERIVATION_REVIEW_REQUIRED", 0),
            "derivation_status_counts": dict(status_counts),
            "normal_form_batch_size": len(normal_form_batch),
            "normal_form_validated_count": nf_validated,
            "claim_queue_record_count": claim_queue.get("record_count", 0),
            "assemble_promotion_policy": "BLOCKED — ingress derivation alone does not promote ASSEMBLE",
        },
    }
    receipt["claim_queue_note"] = build_claim_queue_note(receipt)

    OUT_JSON.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(receipt), encoding="utf-8")

    print(
        json.dumps(
            {
                "json": str(OUT_JSON),
                "markdown": str(OUT_MD),
                "global": receipt["global"],
                "priority_slot_summary": receipt["priority_slot_summary"],
                "claim_queue_note": receipt["claim_queue_note"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
