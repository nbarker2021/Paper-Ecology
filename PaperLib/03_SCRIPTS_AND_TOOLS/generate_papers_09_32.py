#!/usr/bin/env python3
"""Generate rework skeletons for CQE-papers 09-32 and refresh INDEX.md."""
from __future__ import annotations

from pathlib import Path
from textwrap import dedent

OUT = Path(r"D:\Paper Reworks")
FORMAL_ROOT = "CQE-CMPLX-1T-Production/src/papers/formal"


def v(name: str, receipt: str, counts: str, result: str) -> dict:
    return {"name": name, "receipt": receipt, "counts": counts, "result": result}


PAPERS = [
    {
        "num": 9,
        "slug": "09_Hamiltonian_Window_Emergence",
        "title": "Hamiltonian Window Emergence",
        "status_short": "IPMC (bounded); McKay promotion open",
        "role_short": "Temporal-emergence layer",
        "abstract": (
            "Paper 09 reads an ordered center-state sequence through finite local Hamiltonian windows "
            "and emits surviving composite centers. It preserves source indices, centers, and forward/backward "
            "receipts, and introduces a conservation timeline governed by κ = ln(φ)/16."
        ),
        "role": (
            "Temporal-emergence layer. It turns the static corpus of Papers 00-08 into an indexed trace, "
            "shows that finite windows produce exactly n-w+1 composite centers, and keeps every unproved "
            "McKay-Thompson promotion as an explicit algebraic boundary."
        ),
        "definitions": [
            "Center state `(paper_id, center)`; Hamiltonian window width `w`.",
            "Forward/backward reads are reverse receipts; no physical time reversal is claimed.",
            "McKay-Thompson exact boundary bands: `1-3, 3-5, 5-7, 7-9, 15-17, 31-35`.",
            "κ = ln(φ)/16 ≈ 0.030075739… per-event Event Law delta.",
        ],
        "claims": [
            "**Theorem 9.1 — Hamiltonian Window Emergence.** For width `w ≤ n`, exactly `n-w+1` composite centers are emitted; source indices, centers, and forward/backward receipts are preserved.",
            "**Theorem 9.1a — Hamiltonian Scalar Sweep.** Every integer width `w ∈ [3, K-1]` is admissible over a carried set of size `K=9`.",
            "**Theorem 9.1b — McKay-Thompson Threshold Stack (bounded).** The declared bands are recorded at `K=9`; the first four bands are candidates for promotion by a light-cone adjugation witness, while `15-17` and `31-35` remain pending.",
            "**Theorem 9.2 — Kappa Conservation Timeline.** `κ = ln(φ)/16`; per-event delta is `-κ`; cumulative ledger is non-increasing.",
        ],
        "verifiers": [
            v("verify_hamiltonian_window_emergence.py", "hamiltonian_window_emergence_receipt.json", "16/19", "fail — McKay closed-band checks pending"),
            v("verify_kappa_conservation_law.py", "kappa_conservation_law_receipt.json", "10/10", "pass"),
            v("verify_u_r30_quantum_circuit.py", "u_r30_quantum_circuit_receipt.json", "5/5", "pass"),
        ],
        "claim_classes": [
            ("Theorem 9.1 — finite Hamiltonian window arithmetic", "internal_physics_map_closed"),
            ("Theorem 9.1a — scalar sweep over [3, K-1]", "internal_physics_map_closed"),
            ("Theorem 9.2 — κ conservation timeline", "internal_physics_map_closed"),
            ("Theorem 9.1b — McKay-Thompson band promotion", "external_calibration_open"),
            ("Unbounded closed-form McKay arithmetic", "external_calibration_open"),
            ("Physical time reversal / static Z4 temporal periodicity", "interpretive_bridge_named — explicitly denied"),
        ],
        "closed": [
            "Uses Paper 06 light-cone decomposition as the adjugation witness base layer.",
            "Cites Paper 10 cold-start bijection and Paper 11 sporadic ledger as audit context.",
        ],
        "not_yet": [
            "Closed-form McKay-Thompson parity for all bands (O2′).",
            "Direct VOA route to threshold promotion (remains CONJ).",
            "Physical interpretation of temporal emergence as physical time.",
        ],
        "conflicts": [
            "The production `hamiltonian_window_emergence_receipt.json` reports `fail` on the McKay-Thompson closed-band checks, while the formal paper presents 9.1b as a promoted bounded result.",
            "The proof cites Paper 10 and Paper 11, which are downstream in the numbering; this is a retrospective audit structure, not a forward dependency.",
            "`CMPLX-R30-main/PROOF/papers/09_transformer_worldsheet.md` is a historical umbrella paper and does not correspond to this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-09/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-09/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-09/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-09/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/09_transformer_worldsheet.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Papers 01-08:** supply the center-state sequence that Paper 09 reads.",
            "**Paper 10:** provides the cold-start bijection cited as audit context.",
            "**Paper 11:** provides the sporadic ledger cited as audit context.",
            "**Paper 16/17:** will receive continuum-edge and lattice-tower obligations derived from the threshold stack.",
        ],
        "obligations": [
            {"id": "09.1", "obligation": "Reconcile/fix `hamiltonian_window_emergence_receipt.json` McKay closed-band mismatch (path normalization / witness promotion)", "closure": "Closed / CQE-09", "status": "closed"},
            {"id": "09.2", "obligation": "Unbounded closed-form McKay-Thompson arithmetic", "closure": "Later formal paper", "status": "open"},
            {"id": "09.3", "obligation": "McKay-Thompson parity obligation (O2′)", "closure": "Cross-cutting / CQE-17", "status": "open"},
            {"id": "09.4", "obligation": "Direct VOA route to threshold promotion", "closure": "CONJ / later paper", "status": "open"},
        ],
    },
    {
        "num": 10,
        "slug": "10_T10_Master_Receipt",
        "title": "T10 Master Receipt",
        "status_short": "IPMC for transport/lookup; receipt binding open",
        "role_short": "Stack-level master receipt",
        "abstract": (
            "Paper 10 binds Paper 00 and Papers 01-09 into one inspectable, replayable audit object. "
            "It demonstrates the transport-obligation row format, an O(log N) readout architecture conditional on prior enumeration, "
            "and a billion-sheet bijection readout surface that does not close Wolfram Rule 30 Problem 3."
        ),
        "role": (
            "First stack-level receipt. It proves master-receipt inspectability and replayability, keeps open lifts visible, "
            "and supplies the trust anchor that later admission gates require."
        ),
        "definitions": [
            "T10 tuple `(C00, E00→1, P00, P01..P09, R, L, V, O)`.",
            "Transport obligation row fields: id, source, target, map, preserved_quantity, failure_condition, witness, classification, proof_boundary.",
            "Lookup cache: `rule30_bits=1,000,000`, `unipotent_orbits=157`, `lattice_forms=24`.",
            "`O(log N)` readout: `LucasBit(N,0) xor lib[N]` after the correction library has been materialized.",
        ],
        "claims": [
            "**Theorem 10.1 — T10 Master Receipt Integrity.** T10 is inspectable and replayable; two transport rows are demonstrated and two remain open.",
            "**Theorem 10.2 — O(log N) Readout Architecture.** Center bit N is read as `LucasBit(N,0) xor lib[N]` with `O(log N)` addressing plus one lookup, after enumeration has accumulated the correction library.",
            "**Theorem 10.3 — Bijection-Chart Readout Extension.** D4/SU(3)/F4 charts give a cold-start addressing architecture over the billion-sheet template, but do not close Problem 3.",
        ],
        "verifiers": [
            v("verify_bijection_cold_start.py", "bijection_cold_start_receipt.json", "41/41", "pass"),
            v("verify_ologn_readout_architecture.py", "ologn_readout_architecture_receipt.json", "10/10", "pass"),
            v("verify_t10_master_receipt.py", "t10_master_receipt.json", "4/8", "fail — Paper-00/Paper-01-09 presence checks"),
        ],
        "claim_classes": [
            ("Theorem 10.1 — master-receipt inspectability/replayability", "internal_physics_map_closed"),
            ("Theorem 10.2 — O(log N) readout architecture (conditional)", "internal_physics_map_closed"),
            ("Theorem 10.3 — billion-sheet chart addressing", "internal_physics_map_closed"),
            ("Cold single-bit extraction of Rule 30 Problem 3", "external_calibration_open"),
            ("Demonstrated transport rows", "internal_physics_map_closed"),
            ("Open transport rows (J3O route, Niemeier landing)", "external_calibration_open"),
        ],
        "closed": [
            "Binds Paper 00 contract and observer enumeration event.",
            "Transport rows are inspectable and replayable with visible open lifts.",
            "Lookup cache materializes with expected counts.",
        ],
        "not_yet": [
            "Full stack receipt binding for Papers 00-09 (engineering path issue in current receipt).",
            "Demonstration of the `J3O_TO_G2_F4_T5A_ROUTE` transport row.",
            "Demonstration of the `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` transport row.",
            "Cold closed-form extraction of the nth Rule 30 center cell (Problem 3).",
        ],
        "conflicts": [
            "`t10_master_receipt.json` reports `fail` on Paper-00 and Paper-01-09 presence checks; the root cause is path normalization in the verifier (it resolves `ROOT` to `src` rather than the repository root).",
            "The formal paper presents T10 as pass-like, while the receipt currently contradicts that.",
            "`CMPLX-R30-main/PROOF/papers/10_wow_signal_d4_classical.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-10/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-10/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-10/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-10/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/10_wow_signal_d4_classical.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Paper 00:** supplies the observer enumeration contract.",
            "**Papers 01-09:** are the receipts T10 is meant to bind.",
            "**Paper 11:** inherits T10 as its required trust anchor.",
            "**Paper 12:** uses the lookup cache and streaming readout surface.",
        ],
        "obligations": [
            {"id": "10.1", "obligation": "Fix T10 receipt path normalization (`ROOT` should be repo root) and regenerate `t10_master_receipt.json`", "closure": "Closed / CQE-10", "status": "closed"},
            {"id": "10.2", "obligation": "Demonstrate or scope the `J3O_TO_G2_F4_T5A_ROUTE` transport row", "closure": "Later paper / CQE-13", "status": "open"},
            {"id": "10.3", "obligation": "Demonstrate or scope the `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` transport row", "closure": "Later paper / CQE-17", "status": "open"},
            {"id": "10.4", "obligation": "Keep cold Rule 30 Problem 3 extraction as an explicit open obligation", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 11,
        "slug": "11_Theory_Admission_Gate",
        "title": "Theory Admission Gate",
        "status_short": "IPMC for admission predicate; T10 anchor open",
        "role_short": "External-theory admission gate",
        "abstract": (
            "Paper 11 defines the admission rule for importing an external theory into the CQE stack. "
            "A candidate is admitted only when signed by T10, its mass matches the trusted spectrum, and `m(T) ≤ K_max = 9`. "
            "Masses above `K=9` receive a boundary receipt; others are rejected or retained as data."
        ),
        "role": (
            "Admission rule. It turns the T10 master receipt into a trust anchor and demonstrates a worked boundary case "
            "using the Happy Family / Pariah sporadic-group encoder."
        ),
        "definitions": [
            "Observer center `C00`; Paper 10 trust anchor `T10`.",
            "Trusted spectrum `S_T10 = {0,…,10}`; sheet boundary `K_max = 9`.",
            "Admission receipt fields: candidate_id, mass, trusted_match, K_max, T10_anchor, verdict.",
            "Encoder `bit_length_parity`: `bit_length(|G|) mod 2` for group orders.",
        ],
        "claims": [
            "**Theorem 11.1 (T_ADMISSION).** A candidate theory `T` is admitted iff `signed_T10(T) ∧ m(T) ∈ S_T10 ∧ m(T) ≤ 9`. If `m(T) ∈ S_T10 ∧ m(T) > 9` the verdict is boundary; otherwise rejected or rejected_as_datum.",
        ],
        "verifiers": [
            v("verify_sporadic_admission_boundary.py", "sporadic_admission_boundary_receipt.json", "12/12", "pass"),
            v("verify_theory_admission_gate.py", "theory_admission_gate_receipt.json", "20/22", "fail — T10 inheritance and T10 pass checks"),
        ],
        "claim_classes": [
            ("Theorem 11.1 — admission predicate", "internal_physics_map_closed"),
            ("Happy Family / Pariah encoder boundary case", "internal_physics_map_closed"),
            ("Physical interpretation of 'Gluon mass'", "external_calibration_open"),
            ("Classification of all candidates above K=9", "external_calibration_open"),
        ],
        "closed": [
            "Binds Paper 10 master receipt as the required trust anchor (modulo receipt path fix).",
            "Uses the `K=9` sheet boundary inherited from Paper 08 lattice closure.",
        ],
        "not_yet": [
            "Full T10 trust-anchor receipt inheritance until the path-normalization bug is fixed.",
            "Encoding-invariance of the Pariah / Happy Family boundary.",
            "External calibration of the mass filter.",
        ],
        "conflicts": [
            "`theory_admission_gate_receipt.json` reports `fail` on T10 inheritance and T10 pass checks because it looks for `t10_master_receipt.json` under `src/src/papers/formal/...`.",
            "`K=9` is used as a hard internal constant; external calibration of 'Gluon mass' is not performed.",
            "`CMPLX-R30-main/PROOF/papers/11_pariah_monster_boundary.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-11/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-11/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-11/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-11/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/11_pariah_monster_boundary.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Paper 10:** supplies the required T10 trust anchor.",
            "**Paper 08:** supplies the `K=9` sheet boundary.",
            "**Paper 29:** will carry the Pariah/Happy-Family encoding-invariance obligation.",
        ],
        "obligations": [
            {"id": "11.1", "obligation": "Fix T10 trust-anchor path normalization in `verify_theory_admission_gate.py` and regenerate receipt", "closure": "Closed / CQE-11", "status": "closed"},
            {"id": "11.2", "obligation": "Classify candidates above K=9 consistently as boundary (not admitted)", "closure": "CQE-11 (closed by Theorem 11.1)", "status": "closed"},
            {"id": "11.3", "obligation": "Pariah / Happy-Family encoding-invariance of the boundary", "closure": "CQE-29", "status": "open"},
        ],
    },
    {
        "num": 12,
        "slug": "12_CA_Prediction_Surface",
        "title": "CA Prediction Surface",
        "status_short": "IPMC finite local CA surface; P3 open",
        "role_short": "Typed CA prediction surface",
        "abstract": (
            "Paper 12 defines a typed, layered prediction surface for deterministic binary cellular automata. "
            "It supplies Rule 30 prize-evidence layers without claiming asymptotic closure, and explicitly scopes "
            "the cold-start Problem 3 extractor as open."
        ),
        "role": (
            "Finite local CA surface. It closes the eight binary LCR states under Rule 30 and Rule90-correction decomposition, "
            "and refuses to promote finite-window evidence into a proof of infinite non-periodicity or cold nth-bit extraction."
        ),
        "definitions": [
            "`Rule30(L,C,R) = L xor (C or R)`.",
            "`T_EMISSION(L,C,R) = not L if C=1 else L xor R`.",
            "VOA partition `Z(q) = 2q^0 + 6q^5`.",
            "1M-bit center column: density `500,768 / 1,000,000 = 0.500768`; no period ≤ 65,536.",
        ],
        "claims": [
            "**Theorem 12.1 — CA Prediction Surface Finite Local Layers.** Rule 30 readout `T_EMISSION` and Rule90-correction decomposition are exact on the eight binary LCR states; 256-rule ECA space contains 64 silent-boundary rules.",
            "**Theorem 12.2 — Bounded EntropyForge Extension.** EntropyForge is a valid product extension when finite, receipt-bound, and explicit about obligations.",
            "**Theorem 12.3 — Rule 30 Prize Evidence Layer.** Finite and large-window evidence is supplied without promoting asymptotic closure.",
        ],
        "verifiers": [
            v("verify_ca_prediction_surface.py", "ca_prediction_surface_receipt.json", "7/7", "pass"),
            v("verify_center_column_entropy.py", "center_column_entropy_receipt.json", "10/10", "pass"),
            v("verify_p1_non_periodicity.py", "p1_non_periodicity_receipt.json", "7/7", "pass"),
            v("verify_p2_density.py", "p2_density_receipt.json", "7/7", "pass"),
            v("verify_p3_closure.py", "p3_closure_receipt.json", "6/7", "fail — `cold_start_bit_exact`"),
            v("verify_rule30_real_dataset_experiment.py", "rule30_real_dataset_experiment_receipt.json", "4/4", "pass"),
            v("verify_wolfram_1m_bit.py", "wolfram_1m_bit_validation_receipt.json", "5/9", "pass (numeric coverage only)"),
        ],
        "claim_classes": [
            ("Theorem 12.1 — finite local CA layers", "internal_physics_map_closed"),
            ("Theorem 12.2 — bounded EntropyForge extension", "internal_physics_map_closed"),
            ("Theorem 12.3 — prize-evidence layer (finite evidence)", "internal_physics_map_closed"),
            ("Rule 30 Problem 3 cold nth-bit extraction", "external_calibration_open"),
            ("Infinite non-periodicity", "external_calibration_open"),
            ("EntropyForge product claims beyond receipt-bound scope", "interpretive_bridge_named"),
        ],
        "closed": [
            "Uses Rule 30 local truth table and correction decomposition from earlier carrier/correction layers.",
            "Uses Paper 10 lookup cache and streaming readout surface.",
        ],
        "not_yet": [
            "Cold closed-form single-bit extraction (Problem 3).",
            "Proof of infinite non-periodicity.",
            "Unbounded EntropyForge extension without explicit obligations.",
            "Spectral layer as a cold-start predictor.",
        ],
        "conflicts": [
            "`p3_closure_receipt.json` fails on `cold_start_bit_exact`, and `wolfram_1m_bit_validation_receipt.json` is only a partial numeric receipt, yet the formal paper presents a coherent prize-evidence layer.",
            "`CMPLX-R30-main/PROOF/papers/12_physical_constants_invariants.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-12/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-12/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-12/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-12/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/12_physical_constants_invariants.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Papers 01-06:** supply the local truth table and correction decomposition.",
            "**Paper 10:** supplies the lookup cache and streaming readout surface.",
            "**Paper 13:** uses the shell-2 correction surface for quark-face transport.",
        ],
        "obligations": [
            {"id": "12.1", "obligation": "Scope or replace `verify_p3_closure.py` so it does not overclaim cold Problem 3 closure", "closure": "Engineering / CQE-12", "status": "open"},
            {"id": "12.2", "obligation": "Infinite non-periodicity proof or explicit horizon status", "closure": "Later formal paper", "status": "open"},
            {"id": "12.3", "obligation": "EntropyForge extension obligations", "closure": "Product / later paper", "status": "open"},
            {"id": "12.4", "obligation": "Keep spectral layer scoped as non-cold-start predictor", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 13,
        "slug": "13_Standard_Model_Quark_Face_Transport",
        "title": "Standard-Model Quark-Face Transport",
        "status_short": "IPMC algebraic SU(3); CKM ECO",
        "role_short": "Algebraic quark-face transport",
        "abstract": (
            "Paper 13 maps shell-2 LCR states to the three trace-2 idempotents of `J_3(𝕆)` and proves an exact `SU(3)` group-ring closure. "
            "The CKM structure is derived structurally; numeric calibration and physical quark identification remain external."
        ),
        "role": (
            "Algebraic transport layer. It closes the quark-face layer internally and explicitly labels the CKM bridge as external calibration."
        ),
        "definitions": [
            "Shell-2 LCR triple, trace-2 idempotents of `J_3(𝕆)`, `S_3` Weyl orbit of size 6.",
            "Bounded route classifier `G2 → F4 → T5A` in at most three stages.",
            "CKM structure: 3 angles + 1 CP phase from the bounded route.",
        ],
        "claims": [
            "**Theorem 13.** The CQECMPLX quark-face layer is closed: `shell-2 LCR triple → trace-2 J_3(𝕆) idempotent triple → closed S_3 Weyl action → exact n=3 SU(3) group-ring closure`.",
        ],
        "verifiers": [
            v("verify_invariant_transfer_su2u1_in_su3.py", "invariant_transfer_su2u1_in_su3_receipt.json", "7/7", "pass"),
            v("verify_quark_face_transport.py", "quark_face_transport_receipt.json", "9/9", "pass"),
            v("verify_quark_face_transport_literalized.py", "quark_face_transport_literalized_receipt.json", "10/10", "pass"),
            v("verify_rule30_shell_verification_ledger.py", "rule30_shell_verification_ledger_receipt.json", "13/13", "pass"),
            v("verify_standard_model_real_comparison.py", "standard_model_real_comparison_receipt.json", "8/8", "pass"),
            v("ckm_calibration_receipt.json", "ckm_calibration_receipt.json", "—", "template / numeric calibration pending"),
        ],
        "claim_classes": [
            ("Theorem 13 — algebraic SU(3) closure", "internal_physics_map_closed"),
            ("CKM structural derivation (3 angles + 1 phase)", "internal_physics_map_closed"),
            ("CKM numeric values", "external_calibration_open"),
            ("Physical quark / color-charge identification", "external_calibration_open"),
            ("Cold-start unconditional G2/F4/T5A route", "external_calibration_open"),
        ],
        "closed": [
            "Uses Paper 12 shell-2 correction surface and finite local states.",
            "Uses `J_3(𝕆)` carrier and triality substrate from earlier papers.",
        ],
        "not_yet": [
            "Exact numeric CKM calibration.",
            "Physical quark/color-charge measurement bridge.",
            "Unconditional cold-start derivation of the G2/F4/T5A route.",
        ],
        "conflicts": [
            "`CQE-paper-formal-CLAIM` lists `CQE-09` to `CQE-18` as `0 ECO`, yet this paper contains a CKM calibration bridge. Per-paper classification must retain both IPMC and ECO labels.",
            "`CMPLX-R30-main/PROOF/papers/13_magic_square_f4_g2.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-13/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-13/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-13/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-13/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/13_magic_square_f4_g2.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Paper 12:** supplies the shell-2 correction surface.",
            "**Papers 03/08:** supply the `J_3(𝕆)` carrier and lattice closure substrate.",
            "**Paper 14:** uses the SU(3) closure as the zero-repair reference for curvature.",
        ],
        "obligations": [
            {"id": "13.1", "obligation": "Exact numeric CKM calibration (`ckm_calibration_receipt.json`)", "closure": "External calibration / CQE-13", "status": "open"},
            {"id": "13.2", "obligation": "Physical quark / color-charge measurement bridge", "closure": "External calibration", "status": "open"},
            {"id": "13.3", "obligation": "Unconditional cold-start G2/F4/T5A route", "closure": "Later formal paper", "status": "open"},
        ],
    },
    {
        "num": 14,
        "slug": "14_GR_Boundary_Repair_Curvature",
        "title": "GR Boundary-Repair Curvature",
        "status_short": "IPMC internal repair score; GR ECO",
        "role_short": "Curvature as boundary-repair demand",
        "abstract": (
            "Paper 14 defines curvature inside the CQE substrate as a boundary-repair demand. "
            "The Paper 13 `SU(3)` closure serves as the zero-repair reference; positive repair scores appear on visible non-closed lifts."
        ),
        "role": (
            "Internal curvature accounting layer. It gives a precise repair-score definition and explicitly scopes the mapping to physical GR curvature as an external bridge."
        ),
        "definitions": [
            "`curvature_CQE(route) = repair_score(route.classification)`.",
            "Zero repair exactly on demonstrated rows; positive on visible non-closed lifts.",
            "Oloid modules: Cayley-Dickson/Oloid normal form `1,8,8,1`; dual-path oloid three-dyad closure.",
        ],
        "claims": [
            "**Theorem 14.** For the promoted transport ledger, `curvature_CQE(route) = repair_score(route.classification)`; zero exactly on demonstrated rows, positive on visible non-closed lifts.",
        ],
        "verifiers": [
            v("verify_boundary_repair_curvature.py", "boundary_repair_curvature_receipt.json", "9/9", "pass"),
            v("verify_curvature_is_correction.py", "curvature_is_correction_receipt.json", "5/5", "pass"),
        ],
        "claim_classes": [
            ("Theorem 14 — internal repair-score definition", "internal_physics_map_closed"),
            ("Mapping to physical GR curvature / Einstein field equations", "external_calibration_open"),
            ("Oloid normal form as nth-bit extractor", "interpretive_bridge_named — not claimed"),
        ],
        "closed": [
            "Uses Paper 13 SU(3) closure as the zero-repair reference.",
            "Uses oloid path carrier from earlier papers.",
        ],
        "not_yet": [
            "Physical GR curvature measurement.",
            "Derivation of Einstein field equations from repair scores.",
        ],
        "conflicts": [
            "None beyond the expected ECO boundary.",
            "`CMPLX-R30-main/PROOF/papers/14_d12_moonshine_chain.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-14/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-14/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-14/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-14/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/14_d12_moonshine_chain.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Paper 13:** supplies the zero-repair SU(3) reference.",
            "**Paper 05:** supplies the oloid path carrier substrate.",
            "**Paper 26:** will reuse carrier residue/shear boundary language.",
        ],
        "obligations": [
            {"id": "14.1", "obligation": "Physical GR curvature measurement bridge", "closure": "External calibration", "status": "open"},
            {"id": "14.2", "obligation": "Derivation of Einstein field equations from repair-score accounting", "closure": "Later physics paper", "status": "open"},
            {"id": "14.3", "obligation": "Keep oloid normal form scoped as not an nth-bit extractor", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 15,
        "slug": "15_QFT_Higgs_Mass_Residue_Carrier",
        "title": "QFT/Higgs Mass-Residue Carrier",
        "status_short": "IPMC internal mass-residue; Higgs ECO",
        "role_short": "Finite mass-residue carrier",
        "abstract": (
            "Paper 15 defines a finite mass-residue carrier: Rule 30 splits over `F2` into linear and bilinear parts, "
            "Arf-matching gluing accepts, and VOA weight splits as `2q^0 + 6q^5`. The mapping to the measured Higgs mass is named and scoped as external calibration."
        ),
        "role": (
            "Internal mass-residue layer. It builds a finite substrate for mass-like residues and refuses to derive a measured particle mass from the substrate alone."
        ),
        "definitions": [
            "Rule 30 split over `F2`: linear part + bilinear obstruction.",
            "Arf invariant `0`; Arf mismatch rejects gluing.",
            "Correction residue `C AND NOT R` fires on `(0,1,0)` and `(1,1,0)`.",
            "VOA weight split `2q^0 + 6q^5`.",
        ],
        "claims": [
            "**Theorem 15.** The CQECMPLX mass-residue carrier is a finite substrate layer: `F2 obstruction → Arf gluing receipt → correction-residue local states → VOA weight split 2q^0 + 6q^5`.",
        ],
        "verifiers": [
            v("verify_eight_states_one_dual_reading.py", "eight_states_one_dual_reading_receipt.json", "7/7", "pass"),
            v("verify_mass_framing_2x2x2_vs_3x3.py", "mass_framing_2x2x2_vs_3x3_receipt.json", "7/7", "pass"),
            v("verify_mass_gravity_drive.py", "mass_gravity_drive_receipt.json", "7/7", "pass"),
            v("verify_mass_residue_carrier.py", "mass_residue_carrier_receipt.json", "10/10", "pass"),
            v("verify_mass_residue_literalized.py", "mass_residue_literalized_receipt.json", "10/10", "pass"),
            v("verify_ninth_is_forced_printout.py", "ninth_is_forced_printout_receipt.json", "6/6", "pass"),
        ],
        "claim_classes": [
            ("Theorem 15 — internal mass-residue layer", "internal_physics_map_closed"),
            ("Higgs mass 125.25 GeV mapping", "external_calibration_open"),
            ("QFT mass derivation from substrate", "interpretive_bridge_named"),
        ],
        "closed": [
            "Uses Rule 30 local split and correction residue from earlier carrier/correction layers.",
            "Uses Arf gluing and VOA weight split from Paper 18 / earlier VOA work.",
        ],
        "not_yet": [
            "Physical Higgs/QFT mass calibration.",
            "Claim of a measured particle mass derivation.",
        ],
        "conflicts": [
            "`CQE-paper-formal-CLAIM` lists `CQE-09` to `CQE-18` as `0 ECO`, yet this paper maps to Higgs mass calibration. Per-paper classification must retain both IPMC and ECO labels.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-15/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-15/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-15/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-15/` — cached SHA receipts.",
        ],
        "relations": [
            "**Papers 01-06:** supply the Rule 30 split and correction residue.",
            "**Paper 18:** supplies the VOA weight split.",
            "**Paper 26:** will reuse mass residue for Z-pinch/shear horizon.",
        ],
        "obligations": [
            {"id": "15.1", "obligation": "Physical Higgs / QFT mass calibration", "closure": "External calibration", "status": "open"},
            {"id": "15.2", "obligation": "Keep internal substrate claim separate from measured particle mass derivation", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 16,
        "slug": "16_Continuum_Edge_Residuals",
        "title": "Continuum Edge Residuals",
        "status_short": "IPMC local anneal; global continuum ECO",
        "role_short": "Local continuum-edge residual windows",
        "abstract": (
            "Paper 16 treats continuum edge residuals through finite local windows. Every 3-bit chart state anneals to a Lie-conjugate rest state in ≤3 `S3` steps; "
            "the global continuum limit is explicitly left open."
        ),
        "role": (
            "Local window treatment of continuum residuals. It closes finite anneal receipts and scopes the global continuum limit as a horizon obligation."
        ),
        "definitions": [
            "Lie-conjugate rest states; `anneal_to_lie_conjugate` in ≤3 steps.",
            "Edge residue `C AND NOT R`.",
            "Power-of-ten windows `10, 100, 1000` as practical boundary samplers.",
        ],
        "claims": [
            "**Theorem 16.** Continuum edge residuals are locally well-defined window receipts: `local state → ≤3-step rest closure → edge_residue = C AND NOT R`; global continuum claims remain obligations.",
        ],
        "verifiers": [
            v("verify_continuum_edge_residuals.py", "continuum_edge_residuals_receipt.json", "7/7", "pass (wraps `centroid_voa` and `rule30_nth_bit` support checks)"),
        ],
        "claim_classes": [
            ("Theorem 16 — local anneal closure and residue identification", "internal_physics_map_closed"),
            ("Global continuum limit", "external_calibration_open"),
            ("Collapse of propagating correction sum from O(N) to O(log N)", "external_calibration_open"),
        ],
        "closed": [
            "Uses local chart states and correction residue from earlier carrier/correction papers.",
            "Uses `centroid_voa` supporting verifiers.",
        ],
        "not_yet": [
            "Global continuum limit.",
            "Closed-form collapse of propagating correction sum (McKay-Thompson parity, O2′).",
            "Proof that power-of-ten windows complete the continuum limit.",
        ],
        "conflicts": [
            "The Lane-A dyad brief noted no dedicated promoted verifier; the production repo now contains `verify_continuum_edge_residuals.py`, but it delegates to supporting package checks.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-16/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-16/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-16/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-16/` — cached SHA receipts.",
        ],
        "relations": [
            "**Papers 01-06:** supply local chart states and correction residue.",
            "**Paper 07:** supplies bridge residuals carried here as obligations.",
            "**Paper 17:** will advance the lattice tower that underlies the continuum limit.",
        ],
        "obligations": [
            {"id": "16.1", "obligation": "Global continuum limit", "closure": "Later physics paper", "status": "open"},
            {"id": "16.2", "obligation": "Collapse of propagating correction sum from O(N) to O(log N) (McKay-Thompson parity O2′)", "closure": "Cross-cutting / CQE-17", "status": "open"},
            {"id": "16.3", "obligation": "Power-of-ten windows as methodology, not completed limit", "closure": "Documentation cleanup", "status": "open"},
        ],
    },
]

PAPERS += [
    {
        "num": 17,
        "slug": "17_E6_E8_Error_Correction_Tower",
        "title": "E6–E8 Error-Correction Tower",
        "status_short": "IPMC code-tower backbone; Leech/Gamma72 ECO",
        "role_short": "Bounded error-correction/code tower",
        "abstract": (
            "Paper 17 proves a bounded error-correction/code tower as a forced transport backbone: "
            "`1 → 3 → 7 → 8 → 24 → 72`. It closes the local rungs and preserves the rootless Leech and Gamma72 landings as explicit obligations."
        ),
        "role": (
            "Code-tower backbone. It supplies the finite algebraic ladder that later VOA, Moonshine, and applied-lattice papers reuse, without overstating the Leech construction."
        ),
        "definitions": [
            "Rung dimensions `{1,3,7,8,24,72}`.",
            "Hamming `(7,4,3)` weight distribution `{0:1, 3:7, 4:7, 7:1}`.",
            "Extended Hamming self-dual `[8,4,4]`; Golay ingredients `[24,12,8]`.",
            "`E6/E7/E8` interpretation is admissible only as bounded/exceptional reading.",
        ],
        "claims": [
            "**Theorem 17.** The CQE error-correction tower has a verified bounded backbone: `local bit → S3 neighborhood → Hamming/Fano → extended Hamming/E8 → Golay ingredients → Nebe-72 sheet bound`.",
        ],
        "verifiers": [
            v("verify_error_correction_tower.py", "error_correction_tower_receipt.json", "10/10", "pass"),
            v("verify_golay_leech_tower.py", "golay_leech_tower_receipt.json", "10/10", "pass"),
            v("verify_leech_kissing_published_decomposition.py", "leech_kissing_published_decomposition_receipt.json", "9/9", "pass"),
        ],
        "claim_classes": [
            ("Theorem 17 — code-tower backbone", "internal_physics_map_closed"),
            ("E6/E7/E8 exceptional-algebra interpretation of rungs", "interpretive_bridge_named"),
            ("Completed Leech lattice construction", "external_calibration_open"),
            ("Weyl-extractor construction", "external_calibration_open"),
            ("W(E8) lookup table O1 — construction level", "internal_physics_map_closed"),
            ("W(E8) lookup table O1 — full materialized table", "external_calibration_open"),
        ],
        "closed": [
            "Uses local Z/2 bit, S3 neighborhood, and lattice closure template from earlier papers.",
        ],
        "not_yet": [
            "Completed Leech lattice construction (`leech_construction_proved = false`).",
            "Weyl-extractor construction.",
            "Full W(E8) lookup table (O1) — construction closed by Paper 08; full materialized table remains open."
        ],
        "conflicts": [
            "The Golay-Leech receipt passes but explicitly does not prove a completed Leech construction.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-17/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-17/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-17/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-17/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 08:** supplies the local lattice closure template.",
            "**Paper 18:** will use the VOA/Moonshine route seed.",
            "**Papers 21-32:** will reuse the tower dimensions as admissible code-tower dimensions.",
        ],
        "obligations": [
            {"id": "17.1", "obligation": "Completed Leech lattice construction", "closure": "Later formal paper / PFC", "status": "open"},
            {"id": "17.2", "obligation": "Weyl-extractor construction", "closure": "Tooling / later paper", "status": "open"},
            {"id": "17.3", "obligation": "W(E8) lookup table O1 (full materialized table)", "closure": "Partially closed by Paper 08 construction; full table remains open", "status": "partially closed"},
        ],
    },
    {
        "num": 18,
        "slug": "18_VOA_Moonshine_Representation_Routes",
        "title": "VOA / Moonshine Representation Routes",
        "status_short": "IPMC finite VOA seed; full Moonshine ECO",
        "role_short": "Finite VOA seed and bounded Moonshine bootstrap",
        "abstract": (
            "Paper 18 provides a finite chart VOA seed and a bounded Moonshine-route bootstrap. "
            "It explicitly states that `finite seed + static Z4 template + bounded McKay tables ≠ full correction_via_voa route`."
        ),
        "role": (
            "VOA/Moonshine seed paper. It rejects over-promotion to a full Rule 30/Moonshine extractor and keeps the full identification as a horizon bridge."
        ),
        "definitions": [
            "Chart states split `Z(q) = 2q^0 + 6q^5`.",
            "Static `Z4` template: 2 fixed points + 6 period-4 states.",
            "Monster scalar `196883 = 47 × 59 × 71`.",
            "Bounded McKay bootstrap for classes `1A, 2A, 3A, 5A, 7A`.",
        ],
        "claims": [
            "**Theorem 18.** The CQE suite has a verified finite VOA route seed and bounded Moonshine-route bootstrap, but `finite seed + static Z4 template + bounded McKay tables ≠ full correction_via_voa route`.",
        ],
        "verifiers": [
            v("verify_centroid_voa_chain.py", "centroid_voa_chain_receipt.json", "5/5", "pass"),
            v("verify_voa_moonshine_routes.py", "voa_moonshine_routes_receipt.json", "9/9", "pass"),
        ],
        "claim_classes": [
            ("Theorem 18 — finite VOA seed and bounded McKay bootstrap", "internal_physics_map_closed"),
            ("Full Monster / Moonshine identification", "interpretive_bridge_named"),
            ("`correction_via_voa` route completion", "external_calibration_open"),
        ],
        "closed": [
            "Uses the VOA partition and centroid structure from earlier carrier/VOA work.",
        ],
        "not_yet": [
            "Full Moonshine identification.",
            "McKay-Thompson fingerprint (O2′).",
            "`correction_via_voa` route completion.",
        ],
        "conflicts": [
            "The formal result is a non-equality: it rejects over-promotion to a full VOA extractor.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-18/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-18/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-18/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-18/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 17:** supplies the code-tower backbone.",
            "**Paper 19:** uses the static Z4 template.",
            "**Paper 29:** will use the Monster prime-tower ceiling identity.",
        ],
        "obligations": [
            {"id": "18.1", "obligation": "Full Moonshine identification", "closure": "Later formal paper", "status": "open"},
            {"id": "18.2", "obligation": "McKay-Thompson fingerprint O2′", "closure": "Cross-cutting", "status": "open"},
            {"id": "18.3", "obligation": "`correction_via_voa` route completion", "closure": "Later formal paper", "status": "open"},
        ],
    },
    {
        "num": 19,
        "slug": "19_Observer_Face_Selection",
        "title": "Observer Face-Selection",
        "status_short": "IPMC finite face selection",
        "role_short": "Observer frame as finite face selection",
        "abstract": (
            "Paper 19 defines observation as finite face selection: one face is selected, three latent faces are retained, "
            "and center `C` is invariant under `L↔R` reversal. Physical or psychological observer claims are explicitly not made."
        ),
        "role": (
            "Internal observer-frame theorem. It gives a minimal, receiptable model of observation and scopes all physical/psychological readings as interpretive."
        ),
        "definitions": [
            "Four frame faces; antipodal reversal `L↔R` leaves `C` invariant.",
            "Static `Z4` face template: 2 fixed points + 6 period-4 states.",
            "Bounded Monster-D4 route evidence.",
        ],
        "claims": [
            "**Theorem 19.** Observation in the CQE suite is admissible as finite face selection with retained latent alternatives: `select one face → keep three latent faces → preserve C → record residue`.",
        ],
        "verifiers": [
            v("verify_observation_is_face_selection.py", "observation_is_face_selection_receipt.json", "5/5", "pass"),
            v("verify_observer_face_selection.py", "observer_face_selection_receipt.json", "7/7", "pass"),
        ],
        "claim_classes": [
            ("Theorem 19 — finite face-selection observer frame", "internal_physics_map_closed"),
            ("Physical/psychological observer claims", "interpretive_bridge_named — not made"),
        ],
        "closed": [
            "Uses Paper 18 static Z4 template and bounded Moonshine-D4 route evidence.",
        ],
        "not_yet": [
            "Physical observer claims.",
            "SPINOR observation model.",
            "Open-gap observer evidence.",
        ],
        "conflicts": [
            "`CMPLX-R30-main/PROOF/papers/15_observer_lattice_chain.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-19/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-19/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-19/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-19/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/15_observer_lattice_chain.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Paper 18:** supplies the static Z4 template.",
            "**Paper 27:** will extend the observer-frame theorem to delay and shared reality.",
        ],
        "obligations": [
            {"id": "19.1", "obligation": "Physical observer claims (out of scope unless new receipt)", "closure": "External calibration", "status": "open"},
            {"id": "19.2", "obligation": "SPINOR observation model", "closure": "Later formal paper", "status": "open"},
            {"id": "19.3", "obligation": "Open-gap observer evidence", "closure": "Later formal paper", "status": "open"},
        ],
    },
    {
        "num": 20,
        "slug": "20_Layer_2_Synthesis_Ledger",
        "title": "Layer-2 Synthesis Ledger",
        "status_short": "IPMC ledger accounting",
        "role_short": "Aggregate ledger for Papers 17-19",
        "abstract": (
            "Paper 20 aggregates solved, open, failed, forbidden, and transported rows from Papers 17-19 without changing their source-paper status. "
            "It is a verified accounting surface for the layer-2 cluster."
        ),
        "role": (
            "Accounting surface. It preserves the original status of every row and prevents `unknown` reachability from being silently promoted to `solved`."
        ),
        "definitions": [
            "Ledger statuses: solved, open, failed, forbidden, transported.",
            "Reachability verdicts: `yes_with_template_glue`, `no`, `unknown`.",
            "Rank-24 terminal registry.",
        ],
        "claims": [
            "**Theorem 20.** The Layer-2 synthesis ledger is a verified accounting surface: `source receipt → ledger row → preserved status → aggregate report`.",
        ],
        "verifiers": [
            v("verify_layer2_synthesis_ledger.py", "layer2_synthesis_ledger_receipt.json", "8/8", "pass"),
            v("verify_solution_ledger_affirmed.py", "solution_ledger_affirmed_receipt.json", "5/5", "pass"),
        ],
        "claim_classes": [
            ("Theorem 20 — ledger accounting closure", "internal_physics_map_closed"),
        ],
        "closed": [
            "Binds Papers 17-19 source receipts into one aggregate surface.",
        ],
        "not_yet": [
            "Closure of the open lifts themselves (those remain obligations of their source papers).",
        ],
        "conflicts": [
            "None beyond carried-forward open lifts.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-20/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-20/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-20/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-20/` — cached SHA receipts.",
        ],
        "relations": [
            "**Papers 17-19:** are the source receipts aggregated here.",
            "**Paper 21:** uses the solution ledger as an admission rule.",
        ],
        "obligations": [
            {"id": "20.1", "obligation": "Preserve `unknown` reachability as open (do not promote to solved)", "closure": "Ongoing guard", "status": "open"},
            {"id": "20.2", "obligation": "Preserve forbidden rows (do not discard)", "closure": "Ongoing guard", "status": "open"},
            {"id": "20.3", "obligation": "Expose aggregate ledger tooling across all 32 papers", "closure": "Engineering / CQE-06", "status": "open"},
        ],
    },
    {
        "num": 21,
        "slug": "21_MorphForge_PolyForge_MorphoniX",
        "title": "MorphForge / PolyForge / MorphoniX",
        "status_short": "IPMC reader kernel; applied scope open",
        "role_short": "Applied Forge reader",
        "abstract": (
            "Paper 21 converts an observation event into a grid-swept ribbon, a lossless symmetric-group word, a morphon ledger, "
            "and a terminal landing template. It explicitly does not claim to solve arbitrary symbols, materials, organisms, or CAD objects."
        ),
        "role": (
            "Applied Forge reader. It supplies the reader accounting kernel and keeps every applied-domain claim bounded by explicit open obligations."
        ),
        "definitions": [
            "Ribbon word over shell-2 transitions; morphon records; 24-dim terminal `Niemeier:E8^3` tree.",
            "Golden-ratio identities; three-gap theorem; Steinhaus largest-gap relation.",
        ],
        "claims": [
            "**Theorem 21.** The MorphForge reader is valid when it returns (1) a lossless ribbon word, (2) a morphon ledger with explicit closure/failure statuses, and (3) a terminal landing template whose strength is not overstated.",
            "**Theorem 21.2 — AGRM Golden Sweep Reader.**",
        ],
        "verifiers": [
            v("verify_agrm_golden_sweep.py", "agrm_golden_sweep_receipt.json", "10/10", "pass"),
            v("verify_morphforge_ribbon.py", "morphforge_ribbon_receipt.json", "—", "pass_with_open_obligations"),
            v("verify_three_gap_golden_sweep.py", "three_gap_golden_sweep_receipt.json", "—", "companion verifier"),
        ],
        "claim_classes": [
            ("Theorem 21 — reader accounting kernel", "internal_physics_map_closed"),
            ("Arbitrary symbol/material/organism/CAD solving", "interpretive_bridge_named — not claimed"),
            ("Leech import and expanded morphism witnesses", "external_calibration_open"),
        ],
        "closed": [
            "Uses Paper 20 solution ledger as admission rule.",
        ],
        "not_yet": [
            "Missing Leech import.",
            "Expanded morphism witnesses.",
            "TF1 measurement.",
        ],
        "conflicts": [
            "`morphforge_ribbon_receipt.json` reports `pass_with_open_obligations`, not a clean pass.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-21/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-21/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-21/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-21/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 20:** supplies the solution ledger admission rule.",
            "**Papers 22-26:** use the MorphForge reader as their input stage.",
        ],
        "obligations": [
            {"id": "21.1", "obligation": "Missing Leech import", "closure": "Tooling / CQE-17", "status": "open"},
            {"id": "21.2", "obligation": "Expanded morphism witnesses", "closure": "Engineering", "status": "open"},
            {"id": "21.3", "obligation": "TF1 measurement", "closure": "Tooling", "status": "open"},
            {"id": "21.4", "obligation": "Keep open gaps as named failure records", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 22,
        "slug": "22_MetaForge_Applied_Materials",
        "title": "MetaForge Applied Materials",
        "status_short": "IPMC candidate ledger; performance ECO",
        "role_short": "Applied metamaterials candidate-generation kernel",
        "abstract": (
            "Paper 22 moves the Forge family into applied materials: replayable candidate-generation ledger from a finite inventory, "
            "Pareto partner search, ten-fold evaluation, seam mitigation, and production accounting. Materials-performance claims are scoped as external calibration."
        ),
        "role": (
            "Applied-materials kernel. It returns a replayable candidate ledger and explicitly warns against promoting the result to a completed metamaterials-performance theorem."
        ),
        "definitions": [
            "Pareto partner selection; ten-fold deterministic evaluation; error walls; seam/interlayer candidates.",
        ],
        "claims": [
            "**Theorem 22.** MetaForge is a valid applied-materials kernel when it maps an admitted MorphForge observation into a replayable candidate ledger containing inventory evidence, partner-selection scores, fold-evaluation output, seam mitigation rows, production accounting, and explicit open obligations.",
        ],
        "verifiers": [
            v("verify_astro_metaforge_package.py", "astro_metaforge_package_receipt.json", "—", "pass_with_validation_obligations"),
            v("verify_metaforge_materials.py", "metaforge_materials_receipt.json", "—", "pass_with_open_obligations"),
        ],
        "claim_classes": [
            ("Theorem 22 — candidate-generation ledger", "internal_physics_map_closed"),
            ("Materials performance / fabrication claims", "external_calibration_open"),
        ],
        "closed": [
            "Uses Paper 21 MorphForge reader.",
        ],
        "not_yet": [
            "Finite-element validation.",
            "Fabrication and load testing.",
            "Manufacturability constraints.",
            "Relative-density and Poisson-ratio measurement.",
        ],
        "conflicts": [
            "Both receipts carry open/validation obligations; the paper explicitly warns against promoting to a completed metamaterials-performance theorem.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-22/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-22/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-22/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-22/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 21:** supplies the MorphForge reader.",
        ],
        "obligations": [
            {"id": "22.1", "obligation": "Finite-element validation", "closure": "External calibration", "status": "open"},
            {"id": "22.2", "obligation": "Fabrication and load testing", "closure": "External calibration", "status": "open"},
            {"id": "22.3", "obligation": "Manufacturability constraints", "closure": "External calibration", "status": "open"},
            {"id": "22.4", "obligation": "Relative-density and Poisson-ratio measurement", "closure": "External calibration", "status": "open"},
        ],
    },
    {
        "num": 23,
        "slug": "23_FoldForge_Protein_Folding",
        "title": "FoldForge Protein Folding",
        "status_short": "IPMC descriptor kernel; biology ECO",
        "role_short": "Protein-fold descriptor kernel",
        "abstract": (
            "Paper 23 applies Forge reading discipline to protein-chain descriptors: local `(L,C,R)` windows, contact-map receipt, "
            "candidate bifurcations, bounded oloid winding, and explicit validation gaps. Native structure prediction and thermodynamics remain external."
        ),
        "role": (
            "Protein-fold descriptor kernel. It returns a replayable residue-window chart and contact-map receipt and scopes all biological predictions as external calibration."
        ),
        "definitions": [
            "Residue-chain LCR windows; contact map; side-change bifurcations; oloid winding substrate.",
        ],
        "claims": [
            "**Theorem 23.** FoldForge is a valid protein-fold descriptor kernel when it returns a replayable residue-window chart, contact-map receipt, candidate bifurcation list, bounded winding witness, and explicit validation obligations.",
        ],
        "verifiers": [
            v("verify_foldforge_descriptor.py", "foldforge_descriptor_receipt.json", "—", "pass_with_open_obligations"),
            v("calibration_plan.json", "calibration_plan.json", "—", "template_ready_needs_bioparser"),
        ],
        "claim_classes": [
            ("Theorem 23 — descriptor receipt", "internal_physics_map_closed"),
            ("Native structure / folding energies / thermodynamics", "external_calibration_open"),
        ],
        "closed": [
            "Uses Paper 21 reader; Paper 14/16 oloid winding; Paper 06 correction.",
        ],
        "not_yet": [
            "PDB validation.",
            "Native structure prediction.",
            "Depth-only winding extraction.",
            "Biological encoding parser.",
            "Fold-rate and thermodynamic validation.",
        ],
        "conflicts": [
            "`calibration_plan.json` status is `template_ready_needs_bioparser`; no promoted biological parser verifier is present.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-23/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-23/verify_*.py`, `*_receipt.json`, `calibration_plan.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-23/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-23/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 21:** supplies the MorphForge reader.",
            "**Papers 14/16:** supply oloid winding and local chart anneal.",
        ],
        "obligations": [
            {"id": "23.1", "obligation": "PDB validation", "closure": "External calibration", "status": "open"},
            {"id": "23.2", "obligation": "Native structure prediction", "closure": "External calibration", "status": "open"},
            {"id": "23.3", "obligation": "Depth-only winding extraction", "closure": "Tooling", "status": "open"},
            {"id": "23.4", "obligation": "Biological encoding parser", "closure": "Engineering", "status": "open"},
            {"id": "23.5", "obligation": "Fold-rate and thermodynamic validation", "closure": "External calibration", "status": "open"},
        ],
    },
    {
        "num": 24,
        "slug": "24_KnightForge_N_Dimensional_Chess_Automata",
        "title": "KnightForge / N-Dimensional Chess Automata",
        "status_short": "IPMC finite placement; N-dim chess IBN",
        "role_short": "Finite knight-placement CA kernel",
        "abstract": (
            "Paper 24 registers greedy non-attacking knight placement as a finite local-rule CA. N-dimensional chess is treated as a horizon lift, not a core proof claim."
        ),
        "role": (
            "Board-automata kernel. It returns a replayable finite placement receipt and keeps N-dimensional game theory as a named interpretive bridge."
        ),
        "definitions": [
            "Greedy knight placement on `8×8`; left/right approach classification.",
            "L-conjugate centroid attractors; `S3` anneal in ≤3 steps.",
            "VOA sector split `2 + 6`.",
        ],
        "claims": [
            "**Theorem 24.** KnightForge is a valid board-automata kernel when it returns a replayable finite placement receipt whose local states close under L-conjugate centroid annealing and whose N-dimensional extension is explicitly a frame operator.",
        ],
        "verifiers": [
            v("verify_knightforge_ca.py", "knightforge_ca_receipt.json", "—", "pass_with_open_obligations (wraps `centroid_voa`)"),
        ],
        "claim_classes": [
            ("Theorem 24 — finite placement receipt", "internal_physics_map_closed"),
            ("N-dimensional chess solution / game theory", "interpretive_bridge_named — not claimed"),
        ],
        "closed": [
            "Uses Paper 21 ribbon discipline; Paper 16 local chart anneal; Paper 18 static Z4.",
        ],
        "not_yet": [
            "OEIS identity.",
            "N-dimensional playability.",
            "Placement-class relation to `2+6` sector split beyond local chart.",
            "Combinatorial-game expert review.",
        ],
        "conflicts": [
            "The Lane-A dyad brief noted no dedicated promoted verifier; the production repo now contains `verify_knightforge_ca.py`, but it delegates to `centroid_voa`.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-24/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-24/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-24/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-24/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 21:** supplies the ribbon discipline.",
            "**Paper 28:** will extend the knight frame to N-dimensional game lattices.",
        ],
        "obligations": [
            {"id": "24.1", "obligation": "OEIS identity", "closure": "External verification", "status": "open"},
            {"id": "24.2", "obligation": "N-dimensional playability", "closure": "Later applied paper", "status": "open"},
            {"id": "24.3", "obligation": "Placement-class relation to `2+6` sector split", "closure": "Later formal paper", "status": "open"},
            {"id": "24.4", "obligation": "Combinatorial-game expert review", "closure": "Peer review", "status": "open"},
        ],
    },
    {
        "num": 25,
        "slug": "25_Energetic_Traversal_Maps",
        "title": "Energetic Traversal Maps",
        "status_short": "IPMC internal NSL accounting; units ECO",
        "role_short": "Unit-agnostic energy/accounting kernel",
        "abstract": (
            "Paper 25 defines a unit-agnostic energy/accounting kernel. Each transport emits a replayable Noether-Shannon-Landauer (NSL) boundary row; "
            "physical unit conversion to joules and absorption measurement remain external calibration."
        ),
        "role": (
            "NSL accounting layer. It provides an internal replayable energy ledger and scopes all physical-unit bridges as named external obligations."
        ),
        "definitions": [
            "`θ = α·N + β·S + γ·L − absorption`.",
            "Closure when `θ ≤ 0`; residue carried as obligation.",
            "NSL boundary row fields: `N` (action/count), `S` (Shannon entropy), `L` (Landauer cost), absorption capacity.",
        ],
        "claims": [
            "**Theorem 25.** An energetic traversal is valid exactly when it emits a replayable NSL boundary row for each step, sums rows into a path total, marks closure or obligation, and declares whether units are analog-normalized or physically calibrated.",
        ],
        "verifiers": [
            v("verify_energetic_traversal.py", "energetic_traversal_receipt.json", "—", "pass_with_open_obligations"),
            v("verify_energy_ledger_affirmed.py", "energy_ledger_affirmed_receipt.json", "5/5", "pass"),
            v("physical_units_calibration_receipt.json", "physical_units_calibration_receipt.json", "—", "template / hypothesized VOA weights"),
        ],
        "claim_classes": [
            ("Theorem 25 — internal NSL accounting", "internal_physics_map_closed"),
            ("Physical unit conversion to joules", "external_calibration_open"),
            ("Absorption measurement", "external_calibration_open"),
            ("NSL unification / least-action / geodesic readings", "interpretive_bridge_named"),
        ],
        "closed": [
            "Uses Paper 21 ledger/transport obligation discipline.",
        ],
        "not_yet": [
            "Physical unit calibration (joules conversion).",
            "Absorption measurement.",
            "Calibrated variational principle for least-action/geodesic/thermodynamic-optimum readings.",
        ],
        "conflicts": [
            "`physical_units_calibration_receipt.json` predicts SM particle masses from hypothesized VOA weights; relative errors for W/Z are ~9-10%, and the note states 'VOA weights are hypothesized; physical calibration needed.'",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-25/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-25/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-25/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-25/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 21:** supplies ledger/transport discipline.",
            "**Paper 26:** will use energetic traversal language for Z-pinch/shear horizon.",
        ],
        "obligations": [
            {"id": "25.1", "obligation": "Physical unit calibration (joules conversion)", "closure": "External calibration", "status": "open"},
            {"id": "25.2", "obligation": "Absorption measurement", "closure": "External calibration", "status": "open"},
            {"id": "25.3", "obligation": "Calibrated variational principle for least-action/geodesic/thermo readings", "closure": "Later physics paper", "status": "open"},
            {"id": "25.4", "obligation": "Keep NSL unification as a calibration-level research claim", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 26,
        "slug": "26_Z_Pinch_and_Shear_Horizon",
        "title": "Z-Pinch and Shear Horizon",
        "status_short": "IPMC carrier algebra; plasma ECO",
        "role_short": "Z-pinch/shear physics map at carrier layer",
        "abstract": (
            "Paper 26 states the CQE Z-pinch/shear physics map at the carrier layer and separates closed carrier algebra from external plasma/energy claims. "
            "Period, octonion grounding, carrier residue, shear analog, and pinch reclassification are claimed; plasma/energy mechanisms require measured observables."
        ),
        "role": (
            "Horizon kernel. It separates closed carrier algebra from the external physical measurement bridge and lists the required measured observables."
        ),
        "definitions": [
            "Integer Oloid carrier period-4 rolling closure.",
            "Octonion carrier realization of period-4 closure.",
            "Pinch = reclassification toward residue or open lift; shear = carrier boundary event.",
        ],
        "claims": [
            "**Theorem 26.** Paper 26 is valid as a CQE horizon kernel when it separates closed carrier algebra from the external physical measurement bridge: period, octonion grounding, carrier residue, shear analog, and pinch reclassification are claimed; plasma/energy mechanisms require measured observables.",
        ],
        "verifiers": [
            v("verify_pinch_driven_roll.py", "pinch_driven_roll_receipt.json", "7/7", "pass"),
            v("verify_zpinch_shear_horizon.py", "zpinch_shear_horizon_receipt.json", "—", "pass_with_open_obligations"),
        ],
        "claim_classes": [
            ("Theorem 26 — carrier-algebra closure", "internal_physics_map_closed"),
            ("Z-pinch / plasma / energy-generation claims", "external_calibration_open"),
        ],
        "closed": [
            "Uses octonion carrier from earlier algebra; Paper 15 mass residue; Paper 21 ledger.",
        ],
        "not_yet": [
            "Measured Z-pinch witness.",
            "Controlled plasma observable connected to carrier shear bit.",
            "Friction and generation mechanisms.",
            "Physical collapse calibration.",
        ],
        "conflicts": [
            "None beyond the expected ECO boundary.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-26/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-26/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-26/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-26/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 05:** supplies the oloid carrier substrate.",
            "**Paper 15:** supplies mass residue.",
            "**Paper 25:** supplies NSL accounting language.",
        ],
        "obligations": [
            {"id": "26.1", "obligation": "Measured Z-pinch witness", "closure": "External calibration", "status": "open"},
            {"id": "26.2", "obligation": "Controlled plasma observable connected to carrier shear bit", "closure": "External calibration", "status": "open"},
            {"id": "26.3", "obligation": "Friction and generation mechanisms", "closure": "External calibration", "status": "open"},
            {"id": "26.4", "obligation": "Physical collapse calibration", "closure": "External calibration", "status": "open"},
        ],
    },
    {
        "num": 27,
        "slug": "27_Observer_Delay_and_Shared_Reality",
        "title": "Observer Delay and Shared Reality",
        "status_short": "IPMC finite observer frame; consciousness IBN",
        "role_short": "Finite observer-frame theorem",
        "abstract": (
            "Paper 27 is a finite observer-frame theorem. It preserves human-observer language as explicitly interpretive: "
            "static frame labels, shared-center equality, bounded anneal delay, and explicit temporal-period refutation."
        ),
        "role": (
            "Observer-frame paper. It makes the minimal finite claims that can be receipted and scopes consciousness, collapse, simultaneity, and latency as interpretive bridges."
        ),
        "definitions": [
            "Static four-frame `Z4` template exact; opposite-boundary reads share center `C`.",
            "Read-then-anneal delay bounded by finite chart.",
            "Temporal `Z4` period refuted over the tested trace.",
        ],
        "claims": [
            "**Theorem 27.** Observer delay and shared reality are admissible only as finite receipts: static frame labels, shared-center equality, bounded anneal delay, and explicit temporal-period refutation.",
        ],
        "verifiers": [
            v("verify_observer_delay_shared_reality.py", "observer_delay_shared_reality_receipt.json", "—", "pass_with_interpretive_obligations"),
            v("verify_waveform_collapse_mechanism.py", "waveform_collapse_mechanism_receipt.json", "6/6", "pass"),
        ],
        "claim_classes": [
            ("Theorem 27 — finite observer-frame theorem", "internal_physics_map_closed"),
            ("Consciousness / measurement collapse / relativistic simultaneity / human latency", "interpretive_bridge_named — not promoted"),
        ],
        "closed": [
            "Uses Paper 18 static Z4 template, Paper 19 face selection, Paper 16 anneal delay.",
        ],
        "not_yet": [
            "Human latency as a claimed response time.",
            "Shared reality as physical simultaneity.",
            "Consciousness or collapse as physical mechanisms.",
        ],
        "conflicts": [
            "Receipt status is `pass_with_interpretive_obligations`, not a clean pass.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-27/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-27/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-27/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-27/` — cached SHA receipts.",
            "`CQE-paper-formal-CLAIM` — IBN taxonomy reference.",
        ],
        "relations": [
            "**Paper 18:** supplies the static Z4 template.",
            "**Paper 19:** supplies face selection.",
            "**Paper 16:** supplies anneal delay bounds.",
        ],
        "obligations": [
            {"id": "27.1", "obligation": "Keep human latency unclaimed (anneal steps ≠ response time)", "closure": "Ongoing guard", "status": "open"},
            {"id": "27.2", "obligation": "Keep shared reality as agreement on `C`, not physical simultaneity", "closure": "Ongoing guard", "status": "open"},
            {"id": "27.3", "obligation": "Keep consciousness / collapse interpretive", "closure": "Ongoing guard", "status": "open"},
            {"id": "27.4", "obligation": "Any future temporal Z4 period claim must overcome recorded counterexamples", "closure": "Empirical guard", "status": "open"},
        ],
    },
    {
        "num": 28,
        "slug": "28_N_Dimensional_Game_Lattices",
        "title": "N-Dimensional Game Lattices",
        "status_short": "IPMC finite orbit closure; game theory IBN",
        "role_short": "Finite local-rule game-lattice operator",
        "abstract": (
            "Paper 28 is a finite local-rule game-lattice operator. It proves forced code-tower dimensions and orbit closure on admissible dimensions "
            "and explicitly does not claim general game solvability."
        ),
        "role": (
            "Game-lattice operator. It supplies replayable finite orbit receipts on the code-tower dimensions and scopes strategy/termination/winning as horizon items."
        ),
        "definitions": [
            "Forced code-tower dimensions `{1,3,7,8,24,72}`.",
            "Dimension-8 extended Hamming board; six-row `S3` move orbit.",
            "`L(d) = 4·d·(d−1)` for knight-move counts in dimensions 2-5.",
        ],
        "claims": [
            "**Theorem 28.** An N-dimensional game lattice is valid when presented as a finite local-rule receipt on an admissible code-tower dimension: move orbit enumerated, emissions replayable, forbidden carriers logged, every row carries closure/obligation status.",
        ],
        "verifiers": [
            v("verify_conway_glider_oloid.py", "conway_glider_oloid_receipt.json", "6/6", "pass"),
            v("verify_glider_collision_cascade.py", "glider_collision_cascade_receipt.json", "6/6", "pass"),
            v("verify_gosper_gun_emitter.py", "gosper_gun_emitter_receipt.json", "6/6", "pass"),
            v("verify_nd_game_lattices.py", "nd_game_lattices_receipt.json", "—", "pass_with_open_obligations"),
            v("verify_ndim_knight_ca_affirmed.py", "ndim_knight_ca_affirmed_receipt.json", "5/5", "pass"),
            v("calibration_plan.json", "calibration_plan.json", "—", "formula_verified_oeis_query_ready"),
        ],
        "claim_classes": [
            ("Theorem 28 — finite orbit closure on admissible dimensions", "internal_physics_map_closed"),
            ("General game theory / strategy / termination / winning states", "interpretive_bridge_named — not claimed"),
        ],
        "closed": [
            "Uses Paper 12 CA prediction surface; Paper 17 code tower; Paper 24 knight frame.",
        ],
        "not_yet": [
            "General N-dimensional game solver.",
            "Non-code-tower dimensions (dimension 5 explicitly rejected).",
            "Real game-piece geometry per piece type.",
            "Complete game theory (strategy, termination, winning states, fairness).",
            "OEIS identity.",
        ],
        "conflicts": [
            "`calibration_plan.json` reports the formula verified but OEIS query and CGS validation pending.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-28/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-28/verify_*.py`, `*_receipt.json`, `calibration_plan.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-28/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-28/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 12:** supplies the CA prediction surface.",
            "**Paper 17:** supplies the code-tower dimensions.",
            "**Paper 24:** supplies the knight frame.",
        ],
        "obligations": [
            {"id": "28.1", "obligation": "General N-dimensional game solver", "closure": "Later applied paper", "status": "open"},
            {"id": "28.2", "obligation": "Non-code-tower dimensions (dimension 5 rejected)", "closure": "Out of scope / documented", "status": "open"},
            {"id": "28.3", "obligation": "Real game-piece geometry per piece type", "closure": "Tooling", "status": "open"},
            {"id": "28.4", "obligation": "Complete game theory (strategy, termination, winning, fairness)", "closure": "External / later paper", "status": "open"},
            {"id": "28.5", "obligation": "OEIS identity", "closure": "External verification", "status": "open"},
        ],
    },
    {
        "num": 29,
        "slug": "29_Monster_Universal_Energy_Bound_Hypotheses",
        "title": "Monster / Universal Energy-Bound Hypotheses",
        "status_short": "IPMC prime-tower ceiling; energy ECO",
        "role_short": "Monster prime-tower ceiling identity",
        "abstract": (
            "Paper 29 states the Monster prime-tower ceiling identity `196883 = 47 × 59 × 71` and separates closed structural evidence from the physical energy-unit bridge. "
            "Physical energy-bound readings remain falsifiable horizon hypotheses until a witness function exists."
        ),
        "role": (
            "Structural ceiling paper. It affirms the Monster scalar and supersingular prime identity as internal proof rows and scopes the units bridge as a horizon hypothesis."
        ),
        "definitions": [
            "`196883 = 47 × 59 × 71` (three largest supersingular primes; top of Monster prime tower).",
            "VOA weight beneath the ceiling.",
            "LMFDB/real-data anchors.",
        ],
        "claims": [
            "**Theorem 29.** A Monster/energy-bound statement is valid only when finite arithmetic/VOA rows pass as proof rows and physical energy-bound readings remain falsifiable horizon hypotheses until a witness function exists.",
        ],
        "verifiers": [
            v("verify_lmfdb_moonshine_anchor_real_data.py", "lmfdb_moonshine_anchor_real_data_receipt.json", "13/13", "pass"),
            v("verify_monster_energy_bound_hypotheses.py", "monster_energy_bound_hypotheses_receipt.json", "—", "pass_with_quarantined_hypotheses"),
            v("verify_monster_internal_map.py", "monster_internal_map_receipt.json", "5/5", "pass"),
            v("verify_moonshine_real_data_experiment.py", "moonshine_real_data_experiment_receipt.json", "6/6", "pass"),
            v("verify_supersingular_prime_ceiling.py", "supersingular_prime_ceiling_receipt.json", "12/12", "pass"),
        ],
        "claim_classes": [
            ("Structural prime-tower ceiling identity and finite VOA rows", "internal_physics_map_closed"),
            ("Physical energy-bound witness function (units bridge)", "external_calibration_open"),
        ],
        "closed": [
            "Uses Paper 17 code tower, Paper 18 VOA routes, Paper 11 Monster/Pariah boundary.",
        ],
        "not_yet": [
            "Witness function mapping `196883`/VOA weight to measured physical energy.",
            "Pariah/Happy-Family encoding-invariance of the boundary.",
        ],
        "conflicts": [
            "Prior drafts hedged the ceiling as an 'analog'; the current paper affirms the prime-tower identity as closed structural evidence while keeping the units bridge open.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-29/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-29/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-29/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-29/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 17:** supplies the code tower.",
            "**Paper 18:** supplies VOA routes.",
            "**Paper 11:** supplies the Monster/Pariah boundary.",
        ],
        "obligations": [
            {"id": "29.1", "obligation": "Physical energy-bound witness function (units bridge)", "closure": "External calibration", "status": "open"},
            {"id": "29.2", "obligation": "Pariah/Happy-Family encoding-invariance of the boundary", "closure": "CQE-11 / CQE-29", "status": "open"},
        ],
    },
    {
        "num": 30,
        "slug": "30_Grand_Ribbon_Meta_Framer",
        "title": "Grand Ribbon Meta-Framer",
        "status_short": "IPMC ribbon framing; packaging open",
        "role_short": "Eight-slot ribbon sweep over Papers 00-29",
        "abstract": (
            "Paper 30 frames Papers 00-29 as one eight-slot swept local-rule ribbon (`C, L, R, B, T, O, W, A`). "
            "It uses Papers 00-29 only, the canonical terminal route, and visible open lifts."
        ),
        "role": (
            "Meta-framing paper. It provides a structural readout of the entire corpus and scopes packaging obligations honestly."
        ),
        "definitions": [
            "Eight slots: Center, Left boundary, Right boundary, Boundary rule, Tool transform, Obligation set, Workbook analogue, Citation/provenance Anchor.",
            "30-position proof sweep `00-29`; Paper 31 as downstream readout.",
        ],
        "claims": [
            "**Theorem 30.** The production corpus through Paper 29 can be represented as one provenance-filled eight-slot ribbon sweep, using Papers 00-29 only, canonical terminal route, and visible open lifts.",
        ],
        "verifiers": [
            v("verify_grand_ribbon_meta_framer.py", "grand_ribbon_meta_framer_receipt.json", "—", "pass_with_open_packaging_obligations"),
            v("verify_rule30_corpus_provenance.py", "rule30_corpus_provenance_receipt.json", "19/19", "pass"),
        ],
        "claim_classes": [
            ("Theorem 30 — structural ribbon framing", "internal_physics_map_closed"),
            ("`cqe_engine.ribbon` module packaging", "external_calibration_open"),
        ],
        "closed": [
            "Aggregates Papers 00-29 as ribbon positions.",
        ],
        "not_yet": [
            "`cqe_engine.ribbon` module packaged in this git-hosted production root.",
            "Reconciliation of legacy '31 beads' workbook language with `00-29` + Paper 31 readout.",
        ],
        "conflicts": [
            "Legacy workbook says '31 beads'; production Paper 30 uses 30 positions plus Paper 31 readout.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-30/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-30/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-30/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-30/` — cached SHA receipts.",
        ],
        "relations": [
            "**Papers 00-29:** are the positions in the ribbon.",
            "**Paper 31:** is the downstream LCR readout.",
        ],
        "obligations": [
            {"id": "30.1", "obligation": "Package `cqe_engine.ribbon` module in production root", "closure": "Engineering", "status": "open"},
            {"id": "30.2", "obligation": "Reconcile legacy '31 beads' workbook language with `00-29` + Paper 31 readout", "closure": "Documentation cleanup", "status": "open"},
            {"id": "30.3", "obligation": "Keep transport ledger open lifts visible in ribbon framing", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 31,
        "slug": "31_It_Was_Still_Just_LCR",
        "title": "It Was Still Just LCR",
        "status_short": "IPMC retrospective readout",
        "role_short": "Retrospective LCR readout",
        "abstract": (
            "Paper 31 is a retrospective readout: the corpus through Paper 30 can be described as an enacted local `(L,C,R)` process. "
            "It is downstream of Paper 30, not an upstream premise."
        ),
        "role": (
            "Retrospective readout. It re-expresses the completed corpus as an LCR process and scopes all earlier obligations as unchanged."
        ),
        "definitions": [
            "Center coordinate `C` is the LR-invariant gluon coordinate.",
            "Boundary rule remains Rule 30 readout.",
            "Paper 31 is downstream of Paper 30.",
        ],
        "claims": [
            "**Theorem 31.** The corpus through Paper 30 admits a valid retrospective LCR readout: same center coordinate, boundary rule, residue discipline, and dependency direction.",
        ],
        "verifiers": [
            v("verify_meta_lcr_readout.py", "meta_lcr_readout_receipt.json", "—", "pass_as_retrospective_readout"),
        ],
        "claim_classes": [
            ("Theorem 31 — retrospective structural readout", "internal_physics_map_closed"),
        ],
        "closed": [
            "Uses Paper 30 ribbon and all earlier receipts.",
        ],
        "not_yet": [
            "Earlier paper obligations remain open unless their own receipts close them.",
            "Paper 32 must preserve the readout status.",
        ],
        "conflicts": [
            "Receipt status is `pass_as_retrospective_readout`, not a standard `pass`.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-31/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-31/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-31/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-31/` — cached SHA receipts.",
        ],
        "relations": [
            "**Paper 30:** supplies the ribbon framing that Paper 31 reads out as LCR.",
            "**Paper 32:** must preserve the retrospective readout status.",
        ],
        "obligations": [
            {"id": "31.1", "obligation": "Preserve Paper 31 as downstream of Paper 30", "closure": "Ongoing guard", "status": "open"},
            {"id": "31.2", "obligation": "Ensure Paper 32 preserves readout status", "closure": "CQE-32 (closed by Theorem 32)", "status": "closed"},
            {"id": "31.3", "obligation": "Do not promote retrospective readout to an upstream premise", "closure": "Ongoing guard", "status": "open"},
        ],
    },
    {
        "num": 32,
        "slug": "32_The_Supervisor_Cursor",
        "title": "The Supervisor Cursor",
        "status_short": "IPMC coverage packaging; minimality ECO",
        "role_short": "Superpermutation schedule cursor",
        "abstract": (
            "Paper 32 packages superpermutation schedules as supervisor cursors: compressed request schedules over validated coverage rows. "
            "It reuses known coverage records and E8 constructors and scopes minimality claims as obligations."
        ),
        "role": (
            "Packaging paper. It demonstrates coverage-record packaging and algebraic constructors and keeps minimality for `n≥6` as an open obligation."
        ),
        "definitions": [
            "Superpermutation coverage for `n = 4…8`; validated records: `n=4 length 33`, `n=5 153`, `n=6 873`, `n=7 5908`, `n=8 46205`.",
            "Recursive construction `n=8` length `46233`; Egan upper bound `46205`.",
            "E8/octad/pyramid/Cayley-Dickson constructors as supporting algebraic receipts.",
        ],
        "claims": [
            "**Theorem 32.** The suite can be packaged with a supervisor cursor when the cursor is treated as a compressed request schedule over validated coverage rows and each paper's proof/open/readout status stays attached to its receipt.",
        ],
        "verifiers": [
            v("verify_120_e8_cayley_dickson_doubling.py", "p120_e8_cayley_dickson_doubling_receipt.json", "10/10", "pass"),
            v("verify_43200_pyramid_structure.py", "43200_pyramid_structure_receipt.json", "10/10", "pass"),
            v("verify_alena_morph_e8_kit.py", "alena_morph_e8_kit_receipt.json", "11/11", "pass"),
            v("verify_e8_routed_constructor.py", "e8_routed_constructor_receipt.json", "7/7", "pass"),
            v("verify_higher_order_superperm_manager.py", "higher_order_superperm_manager_receipt.json", "15/15", "pass"),
            v("verify_houston_872_attempt.py", "houston_872_attempt_receipt.json", "5/5", "pass"),
            v("verify_hyperpermutation_audit.py", "hyperpermutation_audit_receipt.json", "11/11", "pass"),
            v("verify_lcr_superperm_handbuild.py", "lcr_superperm_handbuild_receipt.json", "18/18", "pass"),
            v("verify_n6_871_reduction.py", "n6_871_reduction_receipt.json", "9/9", "pass"),
            v("verify_octad_e8_structure.py", "octad_e8_structure_receipt.json", "17/17", "pass"),
            v("verify_supervisor_cursor_schedule.py", "supervisor_cursor_schedule_receipt.json", "—", "pass_with_open_minimality_obligations"),
        ],
        "claim_classes": [
            ("Theorem 32 — coverage-record packaging and E8/octad constructors", "internal_physics_map_closed"),
            ("Minimality for `n≥6`", "external_calibration_open"),
            ("Older 'final observation' language", "interpretive_bridge_named — reflective only"),
        ],
        "closed": [
            "Uses Paper 30/Paper 31 status labels.",
            "Reuses known superpermutation coverage records and E8 constructors.",
        ],
        "not_yet": [
            "Minimality for `n ≥ 6` without independent exclusion proofs.",
            "`n=8` corridor below `46205`.",
            "Reconciliation of companion variants (`CQE-paper-32.md` vs `32-obs.md`).",
        ],
        "conflicts": [
            "`supervisor_cursor_schedule_receipt.json` is `pass_with_open_minimality_obligations`.",
            "Some companion variants exist in production mirrors; `lib-forge/papers_output` also contains a separate `CQE-paper-32.md`.",
            "`CMPLX-R30-main/PROOF/papers/16_the_digit_rollout.md` is a historical umbrella, not this production paper.",
        ],
        "related": [
            f"`{FORMAL_ROOT}/CQE-paper-32/FORMAL_PAPER.md` — canonical theorem/proof.",
            f"`{FORMAL_ROOT}/CQE-paper-32/verify_*.py` and `*_receipt.json` — evidence.",
            "`CQECMPLX-Production/papers/CQE-paper-32/` — historical mirror.",
            "`Claude-Codex-Memory/.cqe/receipts/CQE-paper-32/` — cached SHA receipts.",
            "`CMPLX-R30-main/PROOF/papers/16_the_digit_rollout.md` — older umbrella cross-reference only.",
        ],
        "relations": [
            "**Papers 30-31:** supply status labels that the cursor must preserve.",
            "**Paper 17/08:** supply E8 constructors reused here.",
        ],
        "obligations": [
            {"id": "32.1", "obligation": "Minimality for `n ≥ 6` without independent exclusion proofs", "closure": "External / later paper", "status": "open"},
            {"id": "32.2", "obligation": "`n=8` corridor below `46205`", "closure": "External / later paper", "status": "open"},
            {"id": "32.3", "obligation": "Product selectors must preserve proof/open/readout status", "closure": "Engineering", "status": "open"},
            {"id": "32.4", "obligation": "Reconcile companion variants (`CQE-paper-32.md` vs `32-obs.md`) and `lib-forge/papers_output` copy", "closure": "Documentation cleanup", "status": "open"},
        ],
    },
]

CROSS_CUTTING = [
    {
        "id": "CC.1",
        "obligation": "Fix receipt path normalization in Papers 09-11 verifiers and regenerate failing receipts (or scope claims if failures are substantive)",
        "closure": "Closed / CQE-09 / CQE-10 / CQE-11",
        "status": "closed",
    },
    {
        "id": "CC.2",
        "obligation": "Reconcile `CQE-paper-formal-CLAIM` taxonomy: per-paper classification must retain both IPMC and ECO labels (e.g., Papers 13 and 15)",
        "closure": "Documentation / taxonomy",
        "status": "open",
    },
    {
        "id": "CC.3",
        "obligation": "Document R30 umbrella mismatch: `CMPLX-R30-main/PROOF/papers/09_*.md`–`16_*.md` are historical cross-references only",
        "closure": "Documentation cleanup",
        "status": "open",
    },
    {
        "id": "CC.4",
        "obligation": "Provide AirLock specs for Papers 06-32 (`CQECMPLX-AirLock/cqe-production-v0.1/papers/` currently has only 01-05)",
        "closure": "AirLock / documentation",
        "status": "open",
    },
    {
        "id": "CC.5",
        "obligation": "Locate or recreate `.25/.50/.75/_UPGRADED.md` companion variants for Papers 09-32 in primary repo or document them as missing",
        "closure": "Archive / documentation",
        "status": "open",
    },
    {
        "id": "CC.6",
        "obligation": "Close or carry global obligations: McKay-Thompson parity O2′, W(E8) lookup table O1, full Moonshine identification, physical-unit/energy bridges",
        "closure": "Cross-cutting / later papers",
        "status": "open",
    },
]


def _ul(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- (none recorded)"


def _table(rows: list[tuple[str, str]]) -> str:
    lines = ["| Claim | Classification |", "|-------|----------------|"]
    for claim, cls in rows:
        lines.append(f"| {claim} | {cls} |")
    return "\n".join(lines)


def _verifier_table(verifiers: list[dict]) -> str:
    lines = ["| Verifier | Receipt | Checks | Result |", "|----------|---------|--------|--------|"]
    for v in verifiers:
        lines.append(f"| `{v['name']}` | `{v['receipt']}` | {v['counts']} | {v['result']} |")
    return "\n".join(lines)


def _obligation_table(obligations: list[dict]) -> str:
    lines = ["| ID | Obligation | Likely closure |", "|----|------------|----------------|"]
    for o in obligations:
        lines.append(f"| {o['id']} | {o['obligation']} | {o['closure']} |")
    return "\n".join(lines)


def render(p: dict) -> str:
    num = p["num"]
    slug = p["slug"]
    title = p["title"]
    status = p["status_short"]
    src = p.get("sources", f"CQE-paper-{num:02d}, CQECMPLX-Production mirror, Claude-Codex-Memory receipts")
    canonical = f"`{FORMAL_ROOT}/CQE-paper-{num:02d}/FORMAL_PAPER.md`"
    verifiers_summary = f"{len(p['verifiers'])} verifier(s); see table below."

    sections = [
        f"# Paper {num:02d} — {title}",
        "",
        f"**Status:** {status}",
        f"**Source papers:** {src}",
        f"**Canonical formal paper:** {canonical}",
        f"**Verifiers:** {verifiers_summary}",
        "",
        "---",
        "",
        "## Abstract",
        "",
        p["abstract"],
        "",
        "---",
        "",
        "## Role in the suite",
        "",
        p["role"],
        "",
        "---",
        "",
        "## Definitions",
        "",
        _ul(p["definitions"]),
        "",
        "---",
        "",
        "## Main claims",
        "",
        _ul(p["claims"]),
        "",
        "---",
        "",
        "## Verifiers / receipts",
        "",
        _verifier_table(p["verifiers"]),
        "",
        "---",
        "",
        "## Claim-strength classification",
        "",
        _table(p["claim_classes"]),
        "",
        "---",
        "",
        "## Closure of earlier obligations",
        "",
        _ul(p["closed"]),
        "",
        "---",
        "",
        "## What this paper does not yet prove",
        "",
        _ul(p["not_yet"]),
        "",
        "---",
        "",
        "## Conflicts / integrity notes",
        "",
        _ul(p["conflicts"]),
        "",
        "---",
        "",
        "## Related files consulted",
        "",
        _ul(p["related"]),
        "",
        "---",
        "",
        "## Relation to other papers",
        "",
        _ul(p["relations"]),
        "",
        "---",
        "",
        "## Open obligations",
        "",
        _obligation_table(p["obligations"]),
        "",
        "---",
        "",
        "## Conclusion",
        "",
        f"Paper {num:02d} {p['role_short'].lower()} and preserves all unclosed lifts as explicit obligations. "
        "Physics and applied-domain identifications remain named interpretive or external-calibration bridges where scoped.",
        "",
    ]
    return "\n".join(sections)


def update_index() -> None:
    index_path = OUT / "INDEX.md"
    index = index_path.read_text(encoding="utf-8")

    # Extend the reworked-papers table after the Paper 08 row.
    row08 = "| `08_Lattice_Closure.md` | CQE-paper-08, 08.25, 08.50, 08.75, 08_UPGRADED | Local lattice closure template | IPMC |"
    new_rows = "\n".join(
        f"| `{p['slug']}.md` | CQE-paper-{p['num']:02d}, CQECMPLX-Production mirror | {p['role_short']} | {p['status_short']} |"
        for p in PAPERS
    )
    index = index.replace(row08, row08 + "\n" + new_rows)

    # Append new register obligations before the "Next papers in progress" section.
    new_register_rows = "\n".join(
        f"| {o['id']} | Paper {p['num']:02d} | {o['obligation']} | {o['closure']} | {o['status']} |"
        for p in PAPERS
        for o in p["obligations"]
    )
    cross_rows = "\n".join(
        f"| {o['id']} | Cross-cutting | {o['obligation']} | {o['closure']} | {o['status']} |"
        for o in CROSS_CUTTING
    )
    index = index.replace(
        "## Next papers in progress\n\n**CQE-papers 09–32** are being read in batch across their formal papers, companion papers, dyad briefs, R30 proof layer, AirLock specs, production kits, and cached receipts.",
        new_register_rows + "\n" + cross_rows + "\n\n## Next papers in progress\n\nInitial skeletons for CQE-papers 09–32 are now in place. Remaining work is to close obligations, fix receipt path normalization, reconcile the claim taxonomy, and reconcile R30 / AirLock / source-backup gaps.",
    )

    index_path.write_text(index, encoding="utf-8")


def write_cross_cutting() -> None:
    lines = [
        "# Cross-Cutting Integrity Notes — CQE-Papers 09–32",
        "",
        "This file collects the integrity issues that span multiple papers after the batch read of the production corpus.",
        "",
        "## 1. Receipt-status mismatches",
        "",
        "Several formal papers claim pass-like status while their production receipts report `fail` or `pass_with_*_obligations`:",
        "",
        "- **Paper 09:** `hamiltonian_window_emergence_receipt.json` reports `fail` on McKay-Thompson closed-band checks. The failure cascades from the path-normalization issue in Paper 11 / T10 inheritance; even after path fixes, the McKay promotion must be kept as a bounded internal boundary.",
        "- **Paper 10:** `t10_master_receipt.json` reports `fail` because the verifier resolves `ROOT` to `src` rather than the repository root, so Paper-00 source and Paper-01-09 receipts are reported missing.",
        "- **Paper 11:** `theory_admission_gate_receipt.json` reports `fail` on T10 inheritance and T10 pass checks for the same path-normalization reason.",
        "- **Paper 12:** `p3_closure_receipt.json` reports `fail` on `cold_start_bit_exact`. This is a substantive open obligation, not a path bug: cold Rule 30 Problem 3 extraction remains unclosed.",
        "- **Papers 21–32:** multiple receipts report `pass_with_open_*` or interpretive statuses. These are correctly scoped in the skeletons.",
        "",
        "## 2. Claim-taxonomy tension",
        "",
        "`CQE-paper-formal-CLAIM` lists `CQE-09` to `CQE-18` as having `0 ECO`, yet:",
        "",
        "- **Paper 13** contains a CKM calibration bridge (physical quark/color-charge identification).",
        "- **Paper 15** maps the internal mass-residue carrier to the Higgs mass `125.25 GeV`.",
        "",
        "The taxonomy's 'Calibration layer' separately lists Higgs and CKM, but per-paper classification must retain **both** IPMC and ECO labels. The skeletons mark the internal algebraic parts as IPMC and the physical calibrations as ECO.",
        "",
        "## 3. R30 umbrella mismatch",
        "",
        "`CMPLX-R30-main/PROOF/papers/09_*.md`–`16_*.md` are older umbrella papers (transformer worldsheet, Wow signal, Pariah boundary, physical constants, observer lattice chain, magic square, D12 Moonshine chain, digit rollout). They **do not** align 1:1 with the production `CQE-paper-09`–`CQE-paper-16`. They should be treated as historical cross-references only.",
        "",
        "## 4. Missing promoted verifiers",
        "",
        "The Lane-A dyad brief noted Papers 16 and 24 lacked dedicated promoted verifiers. The production repo now contains `verify_continuum_edge_residuals.py` and `verify_knightforge_ca.py`, but both heavily wrap `lattice_forge.centroid_voa` package checks. Future work may promote stronger, paper-specific verifiers.",
        "",
        "## 5. No AirLock specs for 09–32",
        "",
        "`CQECMPLX-AirLock/cqe-production-v0.1/papers/` contains only `CQE-paper-01` through `CQE-paper-05`. Specifications for Papers 06–32 are missing from the AirLock layer.",
        "",
        "## 6. Source-backup variants",
        "",
        "The `.25/.50/.75/_UPGRADED.md` companion variants were not found in the primary production repo for Papers 09–32. Only single historical mirrors (`PAPER-BODY.md`, `SOURCE.md`, `01-CQE-formal/FORMAL.md`) were located under `CQECMPLX-Production/papers/CQE-paper-NN/`.",
        "",
        "## 7. Global open obligations carried forward",
        "",
        "These obligations appear across multiple papers:",
        "",
        "- **McKay-Thompson parity (O2′):** Papers 02, 09, 16, 18.",
        "- **`W(E8)` lookup table (O1):** Papers 08, 17.",
        "- **Full Moonshine identification:** Papers 18, 29.",
        "- **Physical-unit / energy bridges:** Papers 25, 26, 29.",
        "",
        "These remain open until their respective source papers produce receipts that close them.",
        "",
    ]
    (OUT / "CROSS_CUTTING_INTEGRITY_NOTES.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for p in PAPERS:
        (OUT / f"{p['slug']}.md").write_text(render(p), encoding="utf-8")
    update_index()
    write_cross_cutting()
    print(f"Wrote {len(PAPERS)} skeletons, refreshed INDEX.md, and wrote CROSS_CUTTING_INTEGRITY_NOTES.md.")


if __name__ == "__main__":
    main()
