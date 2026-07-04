#!/usr/bin/env python3
"""Phase 14 apply: receipt lane closure, obligation derivation for 8 papers, manifest gates."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

SERIES_ROOT = Path(__file__).resolve().parents[1]
OBLIGATION_PATH = SERIES_ROOT / "OBLIGATION_ROWS.json"
MANIFEST_PATH = SERIES_ROOT / "EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json"

RECEIPT_T10 = (
    "CQECMPLX-Formal-Suite/lib/lattice_forge/receipts/CQE-paper-10-t10_master_receipt.json"
)
RECEIPT_PRIME_CHART = "PRIME_CHART_MONSTER_RENORMALIZATION_PASS.json"
RECEIPT_GRAND_RIBBON = (
    "CQECMPLX-Formal-Suite/lib/lattice_forge/receipts/CQE-paper-30-grand_ribbon_meta_framer_receipt.json"
)

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def _row(
    oid: str,
    flcr: str,
    section: str,
    claim: str,
    evidence: str,
    status: str,
    deps: list[str] | None = None,
    receipt_path: str | None = None,
    receipt_verifier: str | None = None,
) -> dict:
    row: dict = {
        "obligation_id": oid,
        "flcr_id": flcr,
        "source_section": section,
        "claim_text": claim,
        "evidence_type_needed": evidence,
        "prior_paper_deps": deps or [],
        "status": status,
    }
    if receipt_path:
        row["receipt_path"] = receipt_path
        row["receipt_verifier"] = receipt_verifier
        row["receipt_bound_utc"] = NOW
    return row


def derive_nonheld_rows() -> list[dict]:
    """Content-derived obligation rows for FLCR-01/04/05/14/15/18/19/25."""
    rows: list[dict] = []

    # --- FLCR-01 (16 rows) ---
    f = "FLCR-01"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 1.1",
             "The FLCR corpus is admissible only as a typed extension stack: every promoted claim must declare its lane, source, evidence, and boundary.",
             "normal_form_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 1.2",
             "For finite domains such as the eight binary LCR states, exhaustive enumeration is complete proof of the enumerated property.",
             "standard_theorem_citation_bound_result", "derived_pending_citation", ["FLCR-02"]),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 1.3",
             "A claim without a receipt, citation, calibration datum, CAM route, or falsifier boundary remains a staged obligation.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Formal-Methods Receipt And Governance Closure",
             "Attach NSIT standards report, content-addressed receipt, lane grant, replay path, and dependency graph row.",
             "normal_form_result", "staged_open", []),
        _row(f"{f}-OBL-005", f, "Claim Delta Ledger / Formal Methods Receipt Closure",
             "Promote form, receipt, lane, and governance obligations to formal-methods closures when the standard report or artifact is attached.",
             "normal_form_result", "staged_open", []),
        _row(f"{f}-OBL-006", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer can accept formal contribution.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-007", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-008", f, "State-Bound Proof Contract",
             "Bind state emitted by prior slot 00 and reopened at original slot 00 with receipt replay.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-009", f, "Source-Backed Evidence / CQE-paper-10",
             "T10 master receipt toolkit exposes transport obligations; bind verify_transport_obligations receipt before hub promotion.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-10"],
             RECEIPT_T10, "verify_transport_obligations"),
        _row(f"{f}-OBL-010", f, "Major Revision Requests",
             "Replace placeholder source classes with final citation keys, receipt hashes, or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-011", f, "Research Posture / Physics direction",
             "Later translation papers expected to make machinery literal to physics through adapters, calibration, and falsifiers.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-39"]),
        _row(f"{f}-OBL-012", f, "§9 Limitations And Falsifiers",
             "Conservative extension contract: imported theories are not modified by FLCR prose without declared bridges.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-013", f, "Publication Readiness Tasks",
             "External theorems require final citation entries before journal submission.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-014", f, "Worked Example / FLCR-01-T1",
             "Workbook replay and falsifier table must demonstrate grounding contract with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-015", f, "Appendix A / REAPPLY-GLM-OBLIGATION-CLOSURE",
             "CKM, quark/color measurement, Higgs/QFT mass calibration, GR curvature bridges remain separate dependency lanes.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-14", "FLCR-15", "FLCR-18"]),
        _row(f"{f}-OBL-016", f, "Journal Apparatus / Claim-Evidence Table",
             "Every formal claim row requires manifest-bound receipt, source card, validator, citation, or CAM route.",
             "receipt_bound_internal_result", "staged_open", []),
    ]

    # --- FLCR-04 (14 rows) ---
    f = "FLCR-04"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 4.1",
             "The eight binary LCR states admit a lossless finite atlas across LCR, axis/sheet, and diagonal carrier coordinates.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-02", "FLCR-03"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 4.2",
             "The axis/sheet codec is an antipodal quotient followed by a sheet lift.",
             "normal_form_result", "derived_pending_receipt", ["FLCR-02"]),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 4.3",
             "Full D4, F4, or off-diagonal J3(O) assertions are downstream claims unless a separate action receipt is attached.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-17", "FLCR-18"]),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Search By Object Name",
             "Create specific binding queue when object-name match finds validator, receipt, theorem, or calibration route.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-005", f, "Claim Binding Queue residue / Binary invariance",
             "Map binary-invariance falsifier rows to existing PEEP-002/010 before slot promotion.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-006", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-007", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-008", f, "Evidence And Receipts / NSIT tool matrix",
             "T1-T4 algebra foundation, T5-T7 closure, D12 idempotent chain, D4 block tower receipts must be manifest-bound.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-03"]),
        _row(f"{f}-OBL-009", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-010", f, "§9 Limitations And Falsifiers",
             "Diagonal J3(O) registration must not silently import full off-diagonal exceptional algebra.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-011", f, "State-Bound Proof Contract",
             "Bind state from slot 02 reopened at slot 03 with atlas round-trip receipt.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-02"]),
        _row(f"{f}-OBL-012", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-013", f, "Appendix C / Implementation Intake",
             "Implementation-lane imports change claim posture only when bound to claim lane and boundary.",
             "ledger_action", "staged_open", []),
        _row(f"{f}-OBL-014", f, "Worked Example / FLCR-04-T3",
             "Workbook replay must demonstrate atlas readout with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
    ]

    # --- FLCR-05 (13 rows) ---
    f = "FLCR-05"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 5.1",
             "A valid boundary repair converts a failed join into a typed proof-obligation row while preserving coordinates.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-04"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 5.2",
             "Repair is idempotent on already-normalized rows.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-04"]),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 5.3",
             "Untyped failure cannot be consumed by later papers as repair evidence.",
             "normal_form_result", "staged_open", []),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Oloid-path obligations",
             "Wire FLCR-01/11 upstream bindings; oloid-path geometry comparator remains BLOCKED.",
             "external_calibration_result", "staged_open", ["FLCR-01", "FLCR-11"]),
        _row(f"{f}-OBL-005", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-006", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-007", f, "§9 Limitations And Falsifiers",
             "Physical curvature, dust, oloid, and material readings routed downstream — not closed here.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-14", "FLCR-15"]),
        _row(f"{f}-OBL-008", f, "State-Bound Proof Contract",
             "Bind state from slot 03 reopened at slot 04 with repair-row receipt replay.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-04"]),
        _row(f"{f}-OBL-009", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-010", f, "Appendix D / Resolved-State Closure Pass",
             "Satisfied lane closed now; stronger claims lacking adapter/comparator remain residue.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-011", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-012", f, "Worked Example / FLCR-05-T2",
             "Workbook replay must demonstrate repair normalization with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-013", f, "Slot 05 partial wiring (Phase 12)",
             "PEEP-017 transport lane only; oloid geometry comparator blocked per CAR-ROUTE-017 slot exception.",
             "external_calibration_result", "staged_open", []),
    ]

    # --- FLCR-14 (14 rows) ---
    f = "FLCR-14"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 14.1",
             "Six excited chart faces admit exact internal transport under the declared finite atlas and closure receipts.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-04", "FLCR-13"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 14.2",
             "Quark-face algebra can be imported by later papers only through declared source, receipt, and lane.",
             "normal_form_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 14.3",
             "Measured quark identity, CKM data, and physical color calibration deferred to translation papers.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-31", "FLCR-32"]),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Symbolic Carrier Versus Physical Carrier",
             "Map every physical carrier phrase to standard physics object, Hamiltonian/model, dataset, or calibration route.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-005", f, "Claim Binding Queue / CKM-SM Structural Transport Split",
             "Attach quark-face transport receipt; keep CKM/PDG numerical values as data-binding requirements.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-006", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-007", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-008", f, "Source-Backed Evidence / CQE-paper-13.50",
             "Quark-face transport claim contract keeps physical identification separate from finite algebraic closure.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-009", f, "PEEP-027 boundary comparator scope",
             "Attach PEEP-027 boundary comparator scope only — no GR/curvature promotion without unit-bearing rows.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-010", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-011", f, "§9 Limitations And Falsifiers",
             "Structural SU(3)/D12/J3 face transport does not imply measured CKM agreement.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-012", f, "State-Bound Proof Contract",
             "Bind state from slot 12 reopened at slot 13 with quark-face transport receipt.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-13"]),
        _row(f"{f}-OBL-013", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-014", f, "Worked Example / FLCR-14-T4",
             "Workbook replay must demonstrate face transport readout with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
    ]

    # --- FLCR-15 (14 rows) ---
    f = "FLCR-15"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 15.1",
             "Boundary repair demand can be represented as a structured curvature-like ledger over discrete transitions.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-05", "FLCR-14"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 15.2",
             "Repair-curvature map can be imported by later papers only through declared source, receipt, and lane.",
             "normal_form_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 15.3",
             "Einstein-equation identity, measured curvature, and physical spacetime calibration remain downstream.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-35"]),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Continuum Edge And Sampling-Stability Bridge",
             "Attach sampling rule, interpolation/limit statement, norm, error bound, units, and boundary condition.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-005", f, "Higgs mass calibration (Protocol 16.3 residue)",
             "Higgs mass calibration not closed; PEEP-001 deferred; derive residue obligations before physics promotion.",
             "external_calibration_result", "staged_open", ["FLCR-16"]),
        _row(f"{f}-OBL-006", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-007", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-008", f, "Source-Backed Evidence / CQE-paper-14.50",
             "Boundary-repair curvature claim contract: repair is substrate quantity; physical curvature is interpretation until proven.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-009", f, "Slot 15 partial wiring (Phase 12)",
             "PEEP-017 transport lane; PEEP-001 occupancy/residue lane for Higgs mass deferred per CAR-ROUTE-005.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-010", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-011", f, "§9 Limitations And Falsifiers",
             "Discrete repair-curvature ledger does not imply Einstein-field-equation identity.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-012", f, "State-Bound Proof Contract",
             "Bind state from slot 13 reopened at slot 14 with curvature-ledger receipt.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-14"]),
        _row(f"{f}-OBL-013", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-014", f, "Worked Example / FLCR-15-T3",
             "Workbook replay must demonstrate repair-curvature readout with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
    ]

    # --- FLCR-18 (25 rows) ---
    f = "FLCR-18"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 18.1",
             "Bounded exceptional, VOA, and observer-face readouts can be staged as receipt-bearing routes over the prior LCR carrier.",
             "cam_crystal_reapplication_result", "derived_pending_receipt", ["FLCR-17"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 18.2",
             "Exceptional observer route can be imported by later papers only through declared source, receipt, and lane.",
             "normal_form_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 18.3",
             "Full Moonshine identification, measured observer physics, and unbounded exceptional closure remain separate obligations.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-29", "FLCR-10"]),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Leech-E8-Golay Operational Lookup",
             "Attach exact lattice-forge API path, construction parameters, receipt JSON, and lookup vs construction vs invariant-scope boundary.",
             "receipt_bound_internal_result", "staged_open", ["FLCR-07", "FLCR-17"]),
        _row(f"{f}-OBL-005", f, "Claim Binding Queue / Spinor-SU(2) Double-Cover Local Semantics",
             "Bind O8 receipt and cite standard SU(2)->SO(3) double-cover semantics as standard analogy/support.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-04"]),
        _row(f"{f}-OBL-006", f, "Claim Binding Queue / Moonshine-VOA Finite Sector Split",
             "Attach centroid/VOA receipt, finite sector count, and theorem/citation route for any moonshine identification.",
             "receipt_bound_internal_result", "staged_open", ["FLCR-10", "FLCR-17"]),
        _row(f"{f}-OBL-007", f, "Claim Delta Ledger / Leech E8 Golay Lookup",
             "Do not promote lookup into uniqueness, full invariant classification, Gamma72 closure, or physical interpretation without separate evidence.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-07"]),
        _row(f"{f}-OBL-008", f, "Claim Delta Ledger / Spinor Double Cover Local",
             "Do not promote to empirical spin, quantum measurement, or physical observer claims without external physics calibration.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-009", f, "Claim Delta Ledger / Moonshine VOA Finite Sector",
             "Full Moonshine identity, McKay parity, and unbounded identification remain theorem/data-bound.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-29"]),
        _row(f"{f}-OBL-010", f, "FLCR-17 dependency (Phase 13 wiring)",
             "E6/E8 error-correction tower receipt rows required before exceptional closure promotion.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-17"]),
        _row(f"{f}-OBL-011", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-012", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-013", f, "Source-Backed Evidence / CQE-paper-18.50",
             "VOA/Moonshine route claim contract keeps bounded route evidence from becoming hidden global proof claim.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-014", f, "Source-Backed Evidence / CQE-paper-17.50",
             "Error-correction tower claim contract refuses to let verified rungs hide remaining obligations.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-17"]),
        _row(f"{f}-OBL-015", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-016", f, "§9 Limitations And Falsifiers",
             "Bounded exceptional routes do not close full Moonshine or measured observer physics.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-017", f, "State-Bound Proof Contract",
             "Bind state from slot 16 reopened at slot 17 with E6/E8 tower receipt replay.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-17"]),
        _row(f"{f}-OBL-018", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-019", f, "Worked Example / FLCR-18-T5",
             "Workbook replay must demonstrate observer-face route with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-020", f, "Appendix A / REAPPLY-GLM-CAM-CRYSTAL",
             "Local crystal is not exhaustive intake; projection resonance is routing not proof.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-28"]),
        _row(f"{f}-OBL-021", f, "Appendix A / REAPPLY-PROCESS-CENTROID-AUDIT",
             "Future forge claiming closed CAM action must return through centroid, receipt, and project-crystal update.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-28"]),
        _row(f"{f}-OBL-022", f, "Journal Apparatus / Claim-Evidence Table",
             "Every formal claim row requires manifest-bound receipt, source card, validator, citation, or CAM route.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-023", f, "MOTIF-MOONSHINE-02-17-18 bridge",
             "Shared moonshine motif bridge wired Phase 13; receipt paths via PEEP-005/006 still required per row.",
             "receipt_bound_internal_result", "staged_open", ["FLCR-02", "FLCR-17"]),
        _row(f"{f}-OBL-024", f, "DEP-FLCR-18-17 workbook dependency",
             "Theorem dependency table DEP-FLCR-18-17 must attach receipt before downstream exceptional closure.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-17"]),
        _row(f"{f}-OBL-025", f, "Crystal And Standards Evidence To Bind",
             "Observer-face and VOA routes require per-row receipt for unmatched obligation routes.",
             "receipt_bound_internal_result", "staged_open", []),
    ]

    # --- FLCR-19 (18 rows) ---
    f = "FLCR-19"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 19.1",
             "Prior receipt-bearing claims can be assembled into a monotone ledger when edge type and claim lane are preserved.",
             "receipt_bound_internal_result", "derived_pending_receipt", ["FLCR-01", "FLCR-09", "FLCR-11"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 19.2",
             "Layer-2 synthesis ledger can be imported by later papers only through declared source, receipt, and lane.",
             "normal_form_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 19.3",
             "Unknown and forbidden reachability must remain explicit rather than hidden in summary prose.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Formal-Methods Receipt And Governance Closure",
             "Attach NSIT standards report, content-addressed receipt, lane grant, replay path, and dependency graph row.",
             "normal_form_result", "staged_open", []),
        _row(f"{f}-OBL-005", f, "Claim Binding Queue / Negative And Failed-Route Receipts As Guards",
             "Attach negative receipt path, rejected candidate, failure mode, and the promotion it blocks.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-006", f, "Citation bindings CITE-FLCR-19 (Phase 12)",
             "FLCR-01/09/11 citation bindings wired; obligation rows remain staged until receipt lane per row.",
             "standard_theorem_citation_bound_result", "derived_pending_citation", ["FLCR-01", "FLCR-09", "FLCR-11"]),
        _row(f"{f}-OBL-007", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-008", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-009", f, "Source-Backed Evidence / CQE-paper-20",
             "Layer-2 synthesis ledger aggregates solved/open/failed/forbidden rows without changing source-paper status.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-010", f, "Layer-2 synthesis ledger import rule",
             "Unknown/forbidden reachability must remain explicit in layer-2 synthesis ledger import rows.",
             "ledger_action", "staged_open", []),
        _row(f"{f}-OBL-011", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-012", f, "§9 Limitations And Falsifiers",
             "Ledger aggregation does not silently promote upstream open obligations to closed.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-013", f, "State-Bound Proof Contract",
             "Bind state from slot 19 reopened at slot 20 with ledger import receipt replay.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-014", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-015", f, "Worked Example / FLCR-19-T4",
             "Workbook replay must demonstrate ledger assembly with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-016", f, "SUMMARY-IX-Open-Obligations crosswalk",
             "Open obligations manifest must be cross-walked to per-paper obligation rows without rhetorical closure.",
             "ledger_action", "staged_open", ["FLCR-39"]),
        _row(f"{f}-OBL-017", f, "Appendix A / REAPPLY-PROOFVALIDATED-PAPER-ASSEMBLY",
             "Not every FLCR paper currently has a bespoke runnable verifier matching the older protocol.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-39"]),
        _row(f"{f}-OBL-018", f, "Bridge to FLCR-20 forge ledger",
             "Layer-2 ledger becomes bridge to applied forge papers; forge rows need validator receipts.",
             "ledger_action", "staged_open", ["FLCR-20"]),
    ]

    # --- FLCR-25 (14 rows) ---
    f = "FLCR-25"
    rows += [
        _row(f"{f}-OBL-001", f, "§4 Formal Claims / Theorem 25.1",
             "Pinch, shear, and horizon conditions can be represented as internal carrier threshold events.",
             "cam_crystal_reapplication_result", "derived_pending_receipt", ["FLCR-05"]),
        _row(f"{f}-OBL-002", f, "§4 Formal Claims / Proposition 25.2",
             "Carrier horizon can be imported by later papers only through declared source, receipt, and lane.",
             "normal_form_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-003", f, "§4 Formal Claims / Protocol 25.3",
             "Measured Z-pinch observables, plasma identity, and laboratory calibration remain external.",
             "falsifier_or_open_obligation", "staged_open", ["FLCR-37"]),
        _row(f"{f}-OBL-004", f, "Claim Binding Queue / Symbolic Carrier Versus Physical Carrier",
             "Map every physical carrier phrase to standard physics object, Hamiltonian/model, dataset, or calibration route.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-005", f, "Slot 25 CKM comparator (deferred Phase 12)",
             "CKM unitarity/alpha review comparator deferred; PEEP-017 transport lane only per CAR-ROUTE-017 slot exception.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-006", f, "Acceptance Blockers",
             "Final citations and receipt identifiers must be attached before reviewer acceptance.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-007", f, "Acceptance Blockers",
             "Proof sketch must be promoted into formal proof or labeled construction argument.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-008", f, "Source-Backed Evidence / CQE-paper-26",
             "Z-pinch/shear physics map at carrier layer; physical Z-pinch reading not discharged without calibration.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-009", f, "Slot 25 partial wiring (Phase 12)",
             "PEEP-017 quasicrystal transport comparator reuse; no new external comparator; CKM deferred.",
             "external_calibration_result", "staged_open", []),
        _row(f"{f}-OBL-010", f, "Major Revision Requests",
             "Replace placeholder source classes with receipt hashes or dataset identifiers.",
             "standard_theorem_citation_bound_result", "staged_open", []),
        _row(f"{f}-OBL-011", f, "§9 Limitations And Falsifiers",
             "Internal carrier threshold events do not imply measured Z-pinch observables.",
             "falsifier_or_open_obligation", "staged_open", []),
        _row(f"{f}-OBL-012", f, "State-Bound Proof Contract",
             "Bind state from slot 25 reopened at slot 26 with pinch/shear receipt replay.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
        _row(f"{f}-OBL-013", f, "Publication Readiness Tasks",
             "Validator identities and receipt hashes recorded in manifest or receipt appendix.",
             "receipt_bound_internal_result", "staged_open", []),
        _row(f"{f}-OBL-014", f, "Worked Example / FLCR-25-T3",
             "Workbook replay must demonstrate carrier horizon readout with named falsifier per claim lane.",
             "receipt_bound_internal_result", "derived_pending_receipt", []),
    ]

    return rows


def bind_held_receipts(rows: list[dict]) -> int:
    """Close receipt lanes for held papers where pass receipts exist."""
    bindings = {
        "FLCR-10-OBL-002": (RECEIPT_T10, "verify_transport_obligations"),
        "FLCR-10-OBL-008": (RECEIPT_T10, "verify_transport_obligations"),
        "FLCR-10-OBL-010": (RECEIPT_T10, "verify_transport_obligations"),
        "FLCR-10-OBL-015": (RECEIPT_T10, "verify_transport_obligations"),
        "FLCR-29-OBL-004": (RECEIPT_PRIME_CHART, "prime_chart_monster_renormalization_pass"),
        "FLCR-29-OBL-014": (RECEIPT_PRIME_CHART, "prime_chart_monster_renormalization_pass"),
        "FLCR-30-OBL-001": (RECEIPT_GRAND_RIBBON, "verify_grand_ribbon_meta_framer"),
        "FLCR-30-OBL-014": (RECEIPT_GRAND_RIBBON, "verify_grand_ribbon_meta_framer"),
    }
    bound = 0
    for row in rows:
        oid = row["obligation_id"]
        if oid not in bindings:
            continue
        path, verifier = bindings[oid]
        row["status"] = "receipt_bound"
        row["receipt_path"] = path
        row["receipt_verifier"] = verifier
        row["receipt_bound_utc"] = NOW
        bound += 1
    # Also bind FLCR-30-OBL-004 (staged_open grand-ribbon verifier path)
    for row in rows:
        if row["obligation_id"] == "FLCR-30-OBL-004":
            row["status"] = "receipt_bound"
            row["receipt_path"] = RECEIPT_GRAND_RIBBON
            row["receipt_verifier"] = "verify_grand_ribbon_meta_framer"
            row["receipt_bound_utc"] = NOW
            bound += 1
            break
    return bound


def summarize_by_flcr(rows: list[dict]) -> dict:
    summary: dict = {}
    for row in rows:
        flcr = row["flcr_id"]
        if flcr not in summary:
            summary[flcr] = {"row_count": 0, "staged_open": 0, "derived_pending": 0, "receipt_bound": 0}
        summary[flcr]["row_count"] += 1
        status = row["status"]
        if status == "staged_open":
            summary[flcr]["staged_open"] += 1
        elif status == "receipt_bound":
            summary[flcr]["receipt_bound"] += 1
        elif status.startswith("derived_pending"):
            summary[flcr]["derived_pending"] += 1
    return summary


def update_manifest() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    gates = manifest.setdefault("slot_promotion_gates", [])
    # Slot 24 — re-evaluated: PEEP-017 obligations still lack unit-bearing resistivity rows
    slot24 = next((g for g in gates if g.get("slot") == "24"), None)
    if slot24:
        slot24["phase14_re_eval"] = NOW
        slot24["decision"] = "DEFER_ASSEMBLE"
        slot24["reason"] = (
            "PEEP-017 comparator table obligations remain open: no unit-bearing resistivity/"
            "magnetoresistance rows attached; Protocol 24.3 joule/thermodynamic calibration blocked."
        )
    else:
        gates.append({
            "slot": "24",
            "flcr_id": "FLCR-24",
            "peep_candidates": ["PEEP-2026-017", "PEEP-2026-016"],
            "decision": "DEFER_ASSEMBLE",
            "phase14_re_eval": NOW,
            "reason": "Protocol 24.3 joule calibration blocked; PEEP-017 transport only.",
        })
    # Slot 25 CKM — document defer
    if not any(g.get("slot") == "25" for g in gates):
        gates.append({
            "slot": "25",
            "flcr_id": "FLCR-25",
            "peep_candidates": ["PEEP-2026-017"],
            "decision": "DEFER_ASSEMBLE",
            "phase14_eval": NOW,
            "reason": (
                "CKM unitarity/alpha review comparator deferred per deep review; "
                "PEEP-017 scoped transport_lane_only; no honest external CKM comparator paired."
            ),
            "honest_next": (
                "Pair slot 25 with unit-bearing CKM/PDG comparator or explicit falsifier row "
                "before ASSEMBLE promotion; transport lane via PEEP-017 remains REROUTE_OR_REPAIR only."
            ),
        })
    receipt_wiring = manifest.setdefault("receipt_lane_wiring", [])
    for wire in [
        {
            "wiring_id": "RECEIPT-T10-HELD",
            "target_flcr": "FLCR-10",
            "receipt_path": RECEIPT_T10,
            "verifier": "verify_transport_obligations",
            "obligation_ids": ["FLCR-10-OBL-002", "FLCR-10-OBL-008", "FLCR-10-OBL-010", "FLCR-10-OBL-015"],
        },
        {
            "wiring_id": "RECEIPT-PRIME-CHART-29",
            "target_flcr": "FLCR-29",
            "receipt_path": RECEIPT_PRIME_CHART,
            "verifier": "prime_chart_monster_renormalization_pass",
            "obligation_ids": ["FLCR-29-OBL-004", "FLCR-29-OBL-014"],
        },
        {
            "wiring_id": "RECEIPT-GRAND-RIBBON-30",
            "target_flcr": "FLCR-30",
            "receipt_path": RECEIPT_GRAND_RIBBON,
            "verifier": "verify_grand_ribbon_meta_framer",
            "obligation_ids": ["FLCR-30-OBL-001", "FLCR-30-OBL-004", "FLCR-30-OBL-014"],
        },
    ]:
        if not any(w.get("wiring_id") == wire["wiring_id"] for w in receipt_wiring):
            receipt_wiring.append(wire)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    data = json.loads(OBLIGATION_PATH.read_text(encoding="utf-8"))
    held = data.get("hold_papers", [])
    existing = data["rows"]
    bound_count = bind_held_receipts(existing)
    new_rows = derive_nonheld_rows()
    data["rows"] = existing + new_rows
    data["generated_utc"] = NOW
    data["source"] = (
        "formal.md §4, Reviewer Claim Ledger, Claim Binding Queue, Acceptance Blockers — "
        "Phase 13 + Phase 14 derivation pass"
    )
    data["nonheld_papers"] = ["FLCR-01", "FLCR-04", "FLCR-05", "FLCR-14", "FLCR-15", "FLCR-18", "FLCR-19", "FLCR-25"]
    data["summary_by_flcr"] = summarize_by_flcr(data["rows"])
    data["phase14_receipt_bindings"] = bound_count
    OBLIGATION_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    update_manifest()
    print(f"Phase 14 apply: +{len(new_rows)} obligation rows, {bound_count} receipt bindings")
    print(f"Total rows: {len(data['rows'])}")


if __name__ == "__main__":
    main()
