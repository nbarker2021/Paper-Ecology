#!/usr/bin/env python3
"""Audit the Open Obligations Register and mark what is actually closed/solved."""
from __future__ import annotations

import re
from pathlib import Path
from collections import defaultdict

OUT = Path(r"D:\Paper Reworks")
INDEX = OUT / "INDEX.md"

# Mapping: ID -> (actual_status, closed_by, notes)
# actual_status values: closed, partially closed, advanced, guard, out of scope,
#                       documentation, engineering, genuinely open
AUDIT: dict[str, tuple[str, str, str]] = {
    # Paper 00
    "00.1": ("engineering", "", "Wiring Paper 00 verifier into cqe_engine.formal is tooling; no later paper does it."),
    "00.2": ("guard", "", "Ongoing honesty boundary, not a missing proof."),
    "00.3": ("documentation", "", "Bibliography pass remains to be done."),
    "00.4": ("genuinely open", "", "No later unification paper has closed this dual relationship."),
    # Paper 01
    "01.1": ("engineering", "", "Wiring Paper 01 verifiers is still tooling."),
    "01.2": ("documentation", "", "Workbook language cleanup pending."),
    "01.3": ("closed", "CQE-03", "Paper 03 carries the corrected distinction."),
    "01.4": ("guard", "", "O8 spinor double cover is closed in Paper 01; broader physical transport is intentionally scoped."),
    "01.5": ("documentation", "", "Peer-review bibliography pass pending."),
    "01.6": ("out of scope", "", "Explicitly deferred / out of scope."),
    # Paper 02
    "02.1": ("engineering", "", "Wiring Paper 02 verifier is tooling."),
    "02.2": ("closed", "CQE-03", "Paper 03 reconciles D4 axis/sheet labels."),
    "02.3": ("partially closed", "CQE-06 / CQE-10", "Schema exists in Papers 06/10; instantiation across all receipts is still open."),
    "02.4": ("documentation", "", "Citations pending."),
    "02.5": ("out of scope", "", "Product-layer guard, not a theorem gap."),
    "02.6": ("engineering", "", "Tooling cleanup across D-drive copies still needed."),
    "02.7": ("genuinely open", "", "No later paper closes unbounded McKay-Thompson parity (Papers 09, 16, 18 keep it open)."),
    "02.8": ("partially closed", "CQE-08", "Paper 08 closes the O2'' registry core (314 facts); full umbrella population remains open."),
    "02.9": ("genuinely open", "", "No later paper closes the E6→E7→E8 dyadic lift beyond quaternion-sub-algebra."),
    # Paper 03
    "03.1": ("engineering", "", "Wiring Paper 03 verifier is tooling."),
    "03.2": ("guard", "", "Finite reapplication scope is intentionally maintained."),
    "03.3": ("closed", "CQE-13", "Paper 13 provides the S3 group-ring / J3 trace-2 → SU(3) closure."),
    "03.4": ("engineering", "", "Axis naming cleanup across D-drive copies still needed."),
    "03.5": ("closed", "CQE-04", "Paper 04 uses Paper 02 correction coordinates."),
    "03.6": ("out of scope", "", "Explicitly out of scope."),
    "03.7": ("out of scope", "", "Product-layer concern, out of scope."),
    # Paper 04
    "04.1": ("engineering", "", "Wiring Paper 04 verifier is tooling."),
    "04.2": ("closed", "CQE-05", "Paper 05 path carriers close this."),
    "04.3": ("partially closed", "CQE-06", "Shared ledger schema is in Paper 06; full ecology instantiation is open."),
    "04.4": ("genuinely open", "", "No later paper adds the domain example."),
    "04.5": ("genuinely open", "", "No later paper performs the 8-state chart sweep for the bilateral validator."),
    "04.6": ("documentation", "", "Bibliography entries still need insertion."),
    # Paper 05
    "05.1": ("engineering", "", "Wiring Paper 05 verifier is tooling."),
    "05.2": ("partially closed", "CQE-06", "Paper 06 supplies the ledger schema; payload instantiation is open."),
    "05.3": ("genuinely open", "", "No later paper closes the E6→E7→E8 dyadic lift."),
    "05.4": ("guard", "", "Finite vs physical Oloid geometry boundary is maintained."),
    "05.5": ("guard", "", "Cold unbounded extraction is intentionally scoped to downstream papers."),
    "05.6": ("advanced", "CQE-08", "Paper 08 introduces the Nebe K=9 sheet bound; A64/exceedance handling is not fully closed."),
    "05.7": ("documentation", "", "Scope-divergence cleanup between canonical formal and UPGRADED backup still pending."),
    # Paper 06
    "06.1": ("engineering", "", "Wiring Paper 06 verifier is tooling."),
    "06.2": ("genuinely open", "", "The 32-paper causal graph has not been populated yet (skeletons now exist, but graph tooling does not)."),
    "06.3": ("governance", "", "Cycle policy decision still pending."),
    "06.4": ("engineering", "", "Artifact-hash tooling still pending."),
    "06.5": ("guard", "CQE-12", "Paper 12 keeps the cold Problem 3 boundary explicitly open."),
    "06.6": ("genuinely open", "", "8-state chart → tool mapping for bilateral validator is still missing."),
    "06.7": ("documentation", "", "Edge-type schema divergence documentation still pending."),
    # Paper 07
    "07.1": ("engineering", "", "Wiring Paper 07 verifier is tooling."),
    "07.2": ("genuinely open", "", "No later paper proves Hamiltonian/physical-dynamics theorem between samples."),
    "07.3": ("genuinely open", "", "Causal receipt links for interpolated traces not yet enforced."),
    "07.4": ("closed", "CQE-16", "Paper 16 receives bridge residuals as explicit obligations."),
    "07.5": ("out of scope", "", "Product-layer diagnostics, not a formal theorem gap."),
    "07.6": ("genuinely open", "", "General F4 encoder universality theorem remains open."),
    "07.7": ("genuinely open", "", "Sampling-rate vs closure-stability analysis not done."),
    "07.8": ("closed", "CQE-09 / CQE-27", "Paper 09 refutes static Z4 temporal periodicity; Paper 27 reinforces the refutation."),
    "07.9": ("documentation", "", "Reconciliation with R30 umbrella paper still pending."),
    # Paper 08
    "08.1": ("engineering", "", "Wiring Paper 08 verifiers is tooling."),
    "08.2": ("genuinely open", "", "Nontrivial Niemeier/Leech glue-coset representatives are not closed by Paper 17."),
    "08.3": ("genuinely open", "", "Paper 17 explicitly reports `leech_construction_proved = false`."),
    "08.4": ("genuinely open", "", "Paper 17 does not close Gamma72 landing."),
    "08.5": ("genuinely open", "", "No later paper builds a cold-start fingerprint map to Niemeier/Leech."),
    "08.6": ("guard", "", "Physics identifications are intentionally scoped as named bridges in all later papers."),
    "08.7": ("documentation", "", "UPGRADED overclaim reconciliation still pending."),
    "08.8": ("documentation", "", "R30 namespace disambiguation still pending."),
    # Paper 09
    "09.1": ("engineering", "", "Receipt path-normalization bug + McKay promotion need to be reconciled."),
    "09.2": ("genuinely open", "", "Unbounded closed-form McKay arithmetic not available."),
    "09.3": ("genuinely open", "", "O2′ parity remains cross-cutting (Papers 02, 16, 18 also carry it)."),
    "09.4": ("genuinely open", "", "Direct VOA route remains CONJ."),
    # Paper 10
    "10.1": ("engineering", "", "Path-normalization bug in T10 verifier must be fixed."),
    "10.2": ("partially closed", "CQE-13", "Paper 13 provides a bounded G2/F4/T5A route, but not an unconditional cold-start route."),
    "10.3": ("genuinely open", "", "Paper 17 does not close the exceptional→Niemeier landing row."),
    "10.4": ("guard", "CQE-12", "Paper 12 keeps cold Problem 3 extraction explicitly open."),
    # Paper 11
    "11.1": ("engineering", "", "Path-normalization bug in Paper 11 verifier must be fixed."),
    "11.2": ("closed", "CQE-11", "Theorem 11.1 already classifies K>9 candidates as boundary."),
    "11.3": ("genuinely open", "", "Pariah/Happy-Family encoding-invariance not closed by Paper 29."),
    # Paper 12
    "12.1": ("engineering", "", "P3 verifier overclaims cold closure and needs scoping/replacement."),
    "12.2": ("genuinely open", "", "Infinite non-periodicity remains unproven."),
    "12.3": ("genuinely open", "", "EntropyForge extension obligations remain."),
    "12.4": ("guard", "", "Spectral layer is intentionally scoped as non-cold-start."),
    # Paper 13
    "13.1": ("genuinely open", "", "No numeric CKM calibration receipt exists."),
    "13.2": ("genuinely open", "", "Physical quark/color-charge measurement bridge is external."),
    "13.3": ("genuinely open", "", "Paper 13 itself keeps the G2/F4/T5A route bounded."),
    # Paper 14
    "14.1": ("genuinely open", "", "Physical GR curvature measurement bridge is external."),
    "14.2": ("genuinely open", "", "No derivation of Einstein field equations from repair scores."),
    "14.3": ("guard", "", "Oloid normal form is intentionally scoped as not an nth-bit extractor."),
    # Paper 15
    "15.1": ("genuinely open", "", "No physical Higgs/QFT mass calibration."),
    "15.2": ("guard", "", "Internal substrate vs measured mass boundary is maintained."),
    # Paper 16
    "16.1": ("genuinely open", "", "Global continuum limit is not closed."),
    "16.2": ("genuinely open", "", "Correction-sum collapse to O(log N) / O2′ not closed."),
    "16.3": ("guard", "", "Power-of-ten windows are intentionally scoped as samplers."),
    # Paper 17
    "17.1": ("genuinely open", "", "Paper 17 reports `leech_construction_proved = false`."),
    "17.2": ("genuinely open", "", "No Weyl-extractor construction receipt."),
    "17.3": ("closed", "CQE-08", "Paper 08 closes W(E8) construction (`o1_weyl_e8_construction_closed_receipt.json` pass 7/7)."),
    # Paper 18
    "18.1": ("genuinely open", "", "Full Moonshine identification remains open."),
    "18.2": ("genuinely open", "", "O2′ parity remains cross-cutting."),
    "18.3": ("genuinely open", "", "`correction_via_voa` route not completed."),
    # Paper 19
    "19.1": ("out of scope", "", "Physical observer claims are explicitly not made."),
    "19.2": ("genuinely open", "", "SPINOR observation model not built."),
    "19.3": ("genuinely open", "", "Open-gap observer evidence not provided."),
    # Paper 20
    "20.1": ("guard", "", "Preserve unknown reachability is a ledger discipline."),
    "20.2": ("guard", "", "Preserve forbidden rows is a ledger discipline."),
    "20.3": ("engineering", "", "Aggregate ledger tooling across 32 papers not yet wired."),
    # Paper 21
    "21.1": ("genuinely open", "", "Paper 17 does not provide a completed Leech construction to import."),
    "21.2": ("engineering", "", "Expanded morphism witnesses are tooling/research."),
    "21.3": ("engineering", "", "TF1 measurement tooling missing."),
    "21.4": ("guard", "", "Open gaps kept as failure records is a design rule."),
    # Paper 22
    "22.1": ("genuinely open", "", "FE validation is external."),
    "22.2": ("genuinely open", "", "Fabrication/load testing is external."),
    "22.3": ("genuinely open", "", "Manufacturability constraints are external."),
    "22.4": ("genuinely open", "", "Relative-density/Poisson-ratio measurement is external."),
    # Paper 23
    "23.1": ("genuinely open", "", "PDB validation external."),
    "23.2": ("genuinely open", "", "Native structure prediction external."),
    "23.3": ("engineering", "", "Depth-only winding extraction tooling missing."),
    "23.4": ("engineering", "", "Biological parser missing."),
    "23.5": ("genuinely open", "", "Fold-rate/thermodynamic validation external."),
    # Paper 24
    "24.1": ("genuinely open", "", "OEIS identity not verified."),
    "24.2": ("genuinely open", "", "N-dimensional playability not closed."),
    "24.3": ("genuinely open", "", "Placement-class to 2+6 sector split beyond local chart not closed."),
    "24.4": ("genuinely open", "", "Combinatorial-game expert review pending."),
    # Paper 25
    "25.1": ("genuinely open", "", "Joules conversion external."),
    "25.2": ("genuinely open", "", "Absorption measurement external."),
    "25.3": ("genuinely open", "", "Calibrated variational principle not built."),
    "25.4": ("guard", "", "NSL unification intentionally scoped as calibration-level research."),
    # Paper 26
    "26.1": ("genuinely open", "", "Measured Z-pinch witness external."),
    "26.2": ("genuinely open", "", "Plasma-to-shear-bit observable external."),
    "26.3": ("genuinely open", "", "Friction/generation mechanisms external."),
    "26.4": ("genuinely open", "", "Physical collapse calibration external."),
    # Paper 27
    "27.1": ("guard", "", "Human latency intentionally unclaimed."),
    "27.2": ("guard", "", "Shared reality kept as C-agreement."),
    "27.3": ("guard", "", "Consciousness/collapse kept interpretive."),
    "27.4": ("guard", "", "Future Z4 period claims must refute existing counterexamples."),
    # Paper 28
    "28.1": ("genuinely open", "", "General N-dimensional solver not claimed."),
    "28.2": ("out of scope", "", "Dimension 5 is explicitly rejected and documented."),
    "28.3": ("engineering", "", "Real piece geometry tooling missing."),
    "28.4": ("genuinely open", "", "Complete game theory not claimed."),
    "28.5": ("genuinely open", "", "OEIS identity pending."),
    # Paper 29
    "29.1": ("genuinely open", "", "Physical energy-bound witness function external."),
    "29.2": ("genuinely open", "", "Pariah/Happy-Family encoding-invariance not closed."),
    # Paper 30
    "30.1": ("engineering", "", "`cqe_engine.ribbon` module not packaged."),
    "30.2": ("documentation", "", "Legacy '31 beads' language reconciliation pending."),
    "30.3": ("guard", "", "Keep open lifts visible is a design rule."),
    # Paper 31
    "31.1": ("guard", "", "Preserve downstream-of-P30 status is a design rule."),
    "31.2": ("closed", "CQE-32", "Paper 32's packaging theorem preserves proof/open/readout status."),
    "31.3": ("guard", "", "Do not promote retrospective readout is a design rule."),
    # Paper 32
    "32.1": ("genuinely open", "", "Minimality for n≥6 not claimed."),
    "32.2": ("genuinely open", "", "n=8 corridor below 46205 not claimed."),
    "32.3": ("engineering", "", "Product selectors must be wired to preserve status."),
    "32.4": ("documentation", "", "Companion-variant reconciliation pending."),
    # Cross-cutting
    "CC.1": ("engineering", "", "Receipt path normalization in Papers 09-11 still needs fixing."),
    "CC.2": ("documentation", "", "Taxonomy reconciliation still needed."),
    "CC.3": ("documentation", "", "R30 umbrella mismatch documentation still needed."),
    "CC.4": ("engineering", "", "AirLock specs for 06-32 missing."),
    "CC.5": ("documentation", "", "Source-backup variants for 09-32 missing or undocumented."),
    "CC.6": ("genuinely open", "", "Global O2′/O1/Moonshine/energy bridges remain open across papers."),
}


def parse_register(text: str) -> list[dict]:
    rows = []
    for m in re.finditer(r"^\| (\S+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", text, re.MULTILINE):
        id_, src, obligation, closure, status = m.groups()
        if id_ == "ID":
            continue
        rows.append({
            "id": id_,
            "source": src,
            "obligation": obligation,
            "claimed_closure": closure,
            "claimed_status": status,
        })
    return rows


def classify(row: dict) -> tuple[str, str, str]:
    if row["id"] in AUDIT:
        return AUDIT[row["id"]]
    # Fallback inference from claimed status
    status = row["claimed_status"].lower()
    if "closed" in status and "partially" not in status and "schema" not in status:
        return ("closed", row["claimed_closure"], "Claimed closed in original register.")
    if "partially" in status or "schema closed" in status or "advanced" in status:
        return ("partially closed", row["claimed_closure"], "Claimed partial progress in original register.")
    if "guard" in status:
        return ("guard", "", "Ongoing guard.")
    if "out of scope" in status or "deferred" in status:
        return ("out of scope", "", "Explicitly out of scope.")
    return ("genuinely open", "", "No solving paper identified.")


def update_index(rows: list[dict]) -> None:
    text = INDEX.read_text(encoding="utf-8")
    # Replace the register header and every row with expanded columns
    old_header = "| ID | Source | Obligation | Closure | Status |"
    new_header = "| ID | Source | Obligation | Claimed closure | Claimed status | Actual status | Closed / scoped by |"
    text = text.replace(old_header, new_header)
    old_sep = "|---|---|---|---|---|"
    new_sep = "|---|---|---|---|---|---|---|"
    text = text.replace(old_sep, new_sep, 1)  # only the register separator

    for row in rows:
        actual, closed_by, _ = classify(row)
        old_line = f"| {row['id']} | {row['source']} | {row['obligation']} | {row['claimed_closure']} | {row['claimed_status']} |"
        new_line = f"| {row['id']} | {row['source']} | {row['obligation']} | {row['claimed_closure']} | {row['claimed_status']} | {actual} | {closed_by} |"
        text = text.replace(old_line, new_line)

    INDEX.write_text(text, encoding="utf-8")


def write_audit(rows: list[dict]) -> None:
    buckets = defaultdict(list)
    for row in rows:
        actual, closed_by, note = classify(row)
        buckets[actual].append({**row, "actual": actual, "closed_by": closed_by, "note": note})

    order = [
        "closed",
        "partially closed",
        "advanced",
        "guard",
        "out of scope",
        "engineering",
        "documentation",
        "governance",
        "genuinely open",
    ]

    lines = [
        "# Obligation Audit — Actually Open vs. Solved by Other Papers",
        "",
        "This is a reality check on the Open Obligations Register. Each obligation is classified by whether it is:",
        "",
        "- **closed** — solved by a specific later paper or receipt,",
        "- **partially closed / advanced** — a later paper made progress but did not finish,",
        "- **guard** — an ongoing design rule, not a missing proof,",
        "- **out of scope** — explicitly not claimed,",
        "- **engineering / documentation / governance** — tooling, cleanup, or policy, not a theorem gap,",
        "- **genuinely open** — no later paper closes it; this is the real research debt.",
        "",
    ]

    for cat in order:
        items = buckets.get(cat, [])
        if not items:
            continue
        lines.append(f"## {cat.title()} ({len(items)} items)")
        lines.append("")
        lines.append("| ID | Source | Obligation | Closed / scoped by | Note |")
        lines.append("|----|--------|------------|--------------------|------|")
        for row in sorted(items, key=lambda r: r["id"]):
            note = row["note"].replace("|", "\\|")
            lines.append(
                f"| {row['id']} | {row['source']} | {row['obligation']} | {row['closed_by']} | {note} |"
            )
        lines.append("")

    # Summary stats
    counts = {cat: len(buckets.get(cat, [])) for cat in order}
    real_open = counts.get("genuinely open", 0) + counts.get("engineering", 0) + counts.get("documentation", 0) + counts.get("governance", 0)
    lines += [
        "## Summary",
        "",
        f"- **Closed by another paper:** {counts.get('closed', 0)}",
        f"- **Partially closed / advanced:** {counts.get('partially closed', 0) + counts.get('advanced', 0)}",
        f"- **Guards / out-of-scope:** {counts.get('guard', 0) + counts.get('out of scope', 0)}",
        f"- **Tooling / documentation / governance debt:** {counts.get('engineering', 0) + counts.get('documentation', 0) + counts.get('governance', 0)}",
        f"- **Genuinely open research obligations:** {counts.get('genuinely open', 0)}",
        f"- **Total non-trivial remaining work (engineering + docs + genuine open):** {real_open}",
        "",
        "## Highest-priority genuinely open research items",
        "",
    ]
    genuine = buckets.get("genuinely open", [])
    # Pick a curated subset
    highlights = [
        "02.7", "02.9", "05.3", "07.6", "08.2", "08.3", "08.4", "08.5",
        "09.2", "09.3", "10.3", "12.2", "13.1", "13.3", "14.2", "15.1",
        "16.1", "16.2", "17.1", "18.1", "18.3", "21.1", "29.1",
    ]
    for hid in highlights:
        row = next((r for r in genuine if r["id"] == hid), None)
        if row:
            lines.append(f"- **{hid}** ({row['source']}): {row['obligation']}")
    lines.append("")

    (OUT / "OBLIGATION_AUDIT.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = parse_register(INDEX.read_text(encoding="utf-8"))
    update_index(rows)
    write_audit(rows)
    print(f"Audited {len(rows)} obligations; updated INDEX.md and wrote OBLIGATION_AUDIT.md.")


if __name__ == "__main__":
    main()
