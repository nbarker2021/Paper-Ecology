"""Generate the 5/7/9-paper internal reasoning pyramid supplements.

The numbered 00-32 internal reasoning supplements are the fine-grain layer.
This builder adds larger concurrent windows underneath them so repeated patterns,
return lanes, and orbital-data gaps can be reasoned over without assigning
validity labels. NSIT and grading tools remain responsible for classification.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"D:\Paper Reworks")
SUPP = ROOT / "supplements"


LAYERS = {
    "5P": {
        "title": "Internal Reasoning 5-Paper Window Supplement",
        "path": SUPP / "INTERNAL_REASONING_5P_WINDOW_SUPPLEMENT.md",
        "purpose": (
            "The five-paper layer reads adjacent local supplements as medium-range "
            "connected states. It catches structures too wide for a three-paper pass "
            "but still close enough to send back into specific spine papers."
        ),
        "windows": [
            {
                "id": "5P.00-04",
                "papers": "00-04",
                "focus": "grounding, carrier, correction, registration, repair",
                "top_inputs": ["00", "01", "02", "03", "04"],
                "reasoning": [
                    "The base system is not only a set of definitions; it is a typed admission machine. Paper 00 defines the contract, Paper 01 supplies the carrier, Paper 02 supplies residual/correction language, Paper 03 gives representation transport, and Paper 04 turns failed joins into explicit repair demands.",
                    "The repeated hidden object is a typed boundary: data must enter through a carrier, survive correction accounting, remain representation-stable, and expose its failures as obligations instead of prose exceptions.",
                    "A large part of the later corpus should be able to cite this block as the source of the claim-envelope contract: no later physics, lattice, or forge claim should be treated as valid merely because it is expressible; it must also pass the typed boundary route.",
                ],
                "cross_population": [
                    "Back-populate Paper 00 with the fact that the axiom contract is operationally completed only when Papers 01-04 are available as the first executable admission loop.",
                    "Back-populate Paper 02 with Paper 04's repair language so correction terms are not just residuals but routeable obligations.",
                    "Back-populate Paper 03 with Paper 01/02 carrier and correction invariants so representation transport names what must survive transport.",
                ],
                "return_slots": [
                    "5P.00-04.R1: return every later verifier or NSIT row to this admission loop before using it as evidence.",
                    "5P.00-04.R2: route all later representation changes through Paper 03 while preserving Paper 01 carrier identity and Paper 02 residual accounting.",
                    "5P.00-04.R3: treat failed joins as Paper 04 data, not as editorial uncertainty.",
                ],
                "attachments": [
                    "RECEIPT_VERIFIER_CATALOG.md",
                    "NSIT_VALIDITY_REBUILD_PROTOCOL.md",
                    "ORBITAL_DATA_CROSS_POPULATION_AUDIT.md",
                ],
                "handoff": [
                    "Which claims in later papers can be reduced to this typed admission loop?",
                    "Which repair rows need explicit schema fields before NSIT can score them?",
                ],
            },
            {
                "id": "5P.05-09",
                "papers": "05-09",
                "focus": "transport, ledger, bridge, lattice, temporal windows",
                "top_inputs": ["05", "06", "07", "08", "09"],
                "reasoning": [
                    "This block is the first full transport stack: oloid/path carrier, obligation ledger, discrete-continuous bridge, lattice closure, and temporal/Hamiltonian windowing.",
                    "The key missed connection is that Paper 08 should not be read as an isolated lattice paper. It is the address/terminal layer for transports and ledgers that begin in Papers 05-07 and then become time-windowed in Paper 09.",
                    "Continuum language in Paper 07 and temporal language in Paper 09 should be split from finite carrier/lattice addressability. The finite route can often be supported now; the continuum or unbounded route needs separate sampling, norm, and error receipts.",
                ],
                "cross_population": [
                    "Back-populate Paper 05 with lattice terminal addresses as possible path endpoints, while preserving the physical oloid calibration boundary.",
                    "Back-populate Paper 06 with lookup-vs-invariant distinctions so the obligation ledger can store a library-action close separately from stronger mathematical residues.",
                    "Back-populate Papers 07 and 09 with sampling-window obligations instead of leaving continuum/temporal language as broad prose.",
                ],
                "return_slots": [
                    "5P.05-09.R1: every Leech/E8/Golay import must identify lookup, construction, invariant, or physical-mapping scope.",
                    "5P.05-09.R2: every continuum bridge must name the discrete sampling window and the error/stability object.",
                    "5P.05-09.R3: every temporal claim must identify whether it is a static template readout or a dynamic protocol.",
                ],
                "attachments": [
                    "LATTICE_FORGE_UNIFICATION_SUPPLEMENT.md",
                    "SPECTRE_TILING_SUPPLEMENT.md",
                    "NSIT_REASONED_CLOSURE_PASS.md",
                ],
                "handoff": [
                    "Which finite lattice/transport claims can be routed to existing lattice-forge receipts?",
                    "Which continuum statements need NP-06 numerical-analysis treatment?",
                ],
            },
            {
                "id": "5P.10-14",
                "papers": "10-14",
                "focus": "master receipt, admission, prediction, quark-face transport, repair curvature",
                "top_inputs": ["10", "11", "12", "13", "14"],
                "reasoning": [
                    "This block is an evidence-control layer. Paper 10 locks receipts, Paper 11 controls admission, Paper 12 tests prediction surfaces, Paper 13 admits Standard Model-facing transport, and Paper 14 reframes curvature as boundary repair demand.",
                    "The missed data is mostly governance-as-math: receipt locks, admission predicates, finite CA checks, and quark-face transport rows should feed each other as formal constraints rather than sit as separate topics.",
                    "Paper 13 and Paper 14 should not carry physics claims alone; they should import the admission and receipt rules from Papers 10-12 and send calibration burdens to NP-06/NP-12.",
                ],
                "cross_population": [
                    "Back-populate Paper 10 with the exact import needs of Papers 12-14, especially finite CA receipts and physics-bridge receipts.",
                    "Back-populate Paper 11 with negative/admission evidence from Papers 12-14, so rejected routes become reusable exclusion data.",
                    "Back-populate Paper 13 with standard-representation hygiene from NP-12 and with Paper 10 receipt binding requirements.",
                ],
                "return_slots": [
                    "5P.10-14.R1: finite CA evidence from Paper 12 returns to Paper 10 as receipt-template requirements.",
                    "5P.10-14.R2: physics-facing rows in Papers 13-14 return to Paper 11 admission tests before promotion.",
                    "5P.10-14.R3: curvature/repair claims return to Paper 04 as repair-demand examples.",
                ],
                "attachments": [
                    "SM_BRIDGE_SUPPLEMENT.md",
                    "NP-12_Electron_Hole_Exciton_Accounting_For_Open_Math.md",
                    "NSIT_TOOL_CLOSURE_MATRIX.md",
                ],
                "handoff": [
                    "Which Standard Model rows are algebraic transport rows versus calibrated physics rows?",
                    "Which finite prediction claims can be exhaustively verified now?",
                ],
            },
            {
                "id": "5P.15-19",
                "papers": "15-19",
                "focus": "mass residue, continuum edge, lattice tower, VOA/Moonshine, observer selection",
                "top_inputs": ["15", "16", "17", "18", "19"],
                "reasoning": [
                    "This block is where symbolic residue, continuum edge behavior, code/lattice towers, VOA routes, and observer frames all try to describe what a residual state means after transport.",
                    "The key missed connection is that Papers 15-16 need the lookup/invariant split from Paper 17 and the static-template guard from Paper 18 before physical or continuum language is evaluated.",
                    "Paper 19 should not be treated as an afterthought observer note; it is the selection rule that decides which face of the residual/tower/VOA object is being read.",
                ],
                "cross_population": [
                    "Back-populate Paper 15 with electron-hole-exciton and residue-carrier distinctions before any Higgs/mass reading is advanced.",
                    "Back-populate Paper 16 with Paper 17's bounded code tower and Paper 18's static-template guard.",
                    "Back-populate Paper 19 into Papers 15-18 as the observer-face selector for which invariant is being discussed.",
                ],
                "return_slots": [
                    "5P.15-19.R1: physical residue claims return to NP-12/NP-06 before calibration language is used.",
                    "5P.15-19.R2: lattice/VOA imports return to Paper 17/18 scope rows before being reused by applied papers.",
                    "5P.15-19.R3: observer-face choices return to Paper 03 representation transport and Paper 19 face selection.",
                ],
                "attachments": [
                    "SM_BRIDGE_SUPPLEMENT.md",
                    "LATTICE_FORGE_UNIFICATION_SUPPLEMENT.md",
                    "NP-12_Electron_Hole_Exciton_Accounting_For_Open_Math.md",
                ],
                "handoff": [
                    "Which mass/residue rows are symbolic carrier rows and which need empirical calibration?",
                    "Which Moonshine/VOA rows are finite seed, lookup, parity, or full identification burdens?",
                ],
            },
            {
                "id": "5P.20-24",
                "papers": "20-24",
                "focus": "synthesis ledger, applied reader, materials, protein, board automata",
                "top_inputs": ["20", "21", "22", "23", "24"],
                "reasoning": [
                    "This block is the first applied-forge group. Paper 20 aggregates the ledger; Paper 21 defines the applied reader; Papers 22-24 test materials, protein, and game/board domains.",
                    "The missed connection is that the applied papers are not just examples. They are tests of whether CAM/forge lookup surfaces can become domain-specific descriptor and candidate ledgers without pretending external validation is already done.",
                    "The repeated shape is internal descriptor closure versus external domain validation. This should become a standard applied-forge table across all four papers.",
                ],
                "cross_population": [
                    "Back-populate Paper 20 with applied-reader evidence demands from Papers 21-24.",
                    "Back-populate Paper 21 with domain adapter requirements from Papers 22-24.",
                    "Back-populate Papers 22-24 with an explicit internal/external split: descriptor generation, ranking, and lookup are internal; fabrication, wet-lab, native-structure, and game-theory validation are external.",
                ],
                "return_slots": [
                    "5P.20-24.R1: every applied forge row returns to Paper 20 with receipt and status-preservation fields.",
                    "5P.20-24.R2: every domain adapter returns to Paper 21 for common reader/codec obligations.",
                    "5P.20-24.R3: every external validation need returns to NP-07 rather than remaining scattered.",
                ],
                "attachments": [
                    "APPLIED_FORGES_WORKBOOK.md",
                    "METAFORGE_MATERIALS_SUPPLEMENT.md",
                    "SPECTRE_TILING_SUPPLEMENT.md",
                ],
                "handoff": [
                    "Which applied claims are already no-cost lookup/descriptor claims?",
                    "Which claims require external benchmark, fabrication, wet-lab, or game-theory evidence?",
                ],
            },
            {
                "id": "5P.25-29",
                "papers": "25-29",
                "focus": "energetic traversal, shear/plasma horizon, observer delay, game lattices, Monster ceiling",
                "top_inputs": ["25", "26", "27", "28", "29"],
                "reasoning": [
                    "This block mixes physical-energy language, plasma/shear language, observer-delay protocol, game-lattice search, and Monster/Moonshine ceiling claims.",
                    "The biggest missed connection is claim-scale separation. Papers 25-26 need calibration; Paper 27 needs protocol semantics; Paper 28 can close finite local-game surfaces; Paper 29 needs invariant/witness discipline.",
                    "This block should be the anti-overclaim training set: it contains many strong-sounding phrases that become useful once split into internal accounting, finite verification, observer protocol, external calibration, and large-invariant witness lanes.",
                ],
                "cross_population": [
                    "Back-populate Papers 25-26 with NP-06 and NP-12 calibration slots before any measured-energy or plasma statement is treated as settled.",
                    "Back-populate Paper 27 into Papers 25-26 and 28-29 as the observer/protocol guard.",
                    "Back-populate Paper 28's finite-game verification pattern into Paper 32's supervisor/minimality split.",
                    "Back-populate Paper 29 with the lookup-vs-invariant guard from Papers 08/17/21.",
                ],
                "return_slots": [
                    "5P.25-29.R1: physical measurements return to calibration protocols and units ledgers.",
                    "5P.25-29.R2: finite game/lattice results return to bounded verification lanes.",
                    "5P.25-29.R3: Monster-energy claims return to explicit witness functions and invariant definitions.",
                ],
                "attachments": [
                    "APPLIED_FORGES_WORKBOOK.md",
                    "NSIT_REASONED_CLOSURE_PASS.md",
                    "METAFORGE_MATERIALS_SUPPLEMENT.md",
                ],
                "handoff": [
                    "Which energy/plasma rows are internal accounting rows versus measured physics rows?",
                    "Which Paper 29 claims can import lookup surfaces and which still need invariant witnesses?",
                ],
            },
            {
                "id": "5P.30-32",
                "papers": "30-32",
                "focus": "corpus ribbon, retrospective LCR, supervisor cursor",
                "top_inputs": ["30", "31", "32"],
                "reasoning": [
                    "This block is the corpus-control tail. Paper 30 stores the corpus ribbon, Paper 31 reads the system retrospectively, and Paper 32 schedules/supervises next selection.",
                    "The missed connection is that the tail should not merely summarize. It must route every earlier obligation back to the start of the spine as a springboard: Paper 32 selects, Paper 31 reads, Paper 30 records, and Paper 00-04 re-admit.",
                    "This block is also where orbital data should become actionable: supplements, receipts, validators, CAM memories, and external formal papers need assigned lanes before scoring.",
                ],
                "cross_population": [
                    "Back-populate Paper 30 with the orbital audit as a corpus-routing table.",
                    "Back-populate Paper 31 with retrospective readout slots for every larger-window lane.",
                    "Back-populate Paper 32 with the larger-window queue as supervisor input rather than prose backlog.",
                ],
                "return_slots": [
                    "5P.30-32.R1: supervisor selections return to Paper 00 admission and Paper 06 obligation ledger.",
                    "5P.30-32.R2: retrospective readout returns to each paper's own supplement/cross-population section.",
                    "5P.30-32.R3: unnumbered orbital artifacts return to assigned spine lanes before NSIT scoring.",
                ],
                "attachments": [
                    "ORBITAL_DATA_CROSS_POPULATION_AUDIT.md",
                    "CRYSTAL_CAM_PROJECTOR_SUPPLEMENT.md",
                    "OBLIGATION_LEDGER_SUPPLEMENT.md",
                ],
                "handoff": [
                    "Which orbital artifacts remain unassigned to paper lanes?",
                    "Which supervisor queue items should become direct paper edits versus new papers?",
                ],
            },
        ],
    },
    "7P": {
        "title": "Internal Reasoning 7-Paper Window Supplement",
        "path": SUPP / "INTERNAL_REASONING_7P_WINDOW_SUPPLEMENT.md",
        "purpose": (
            "The seven-paper layer reads block-scale systems. It recombines the "
            "three-paper supplements and the five-paper windows into wider invariants "
            "and deferred-return lanes."
        ),
        "windows": [
            {
                "id": "7P.00-06",
                "papers": "00-06",
                "focus": "base kernel: grounding through causal ledger",
                "top_inputs": ["00-02", "03-05", "06"],
                "reasoning": [
                    "The base kernel is a proof-routing machine: contract, carrier, correction, representation, repair, transport, and ledger are one cycle.",
                    "Paper 06 should be read as the first memory surface for Papers 00-05, not merely a later obligation list.",
                    "A later claim should be able to return to this block and ask: what entered, how was it carried, what correction was generated, what representation changed, what repair fired, and what ledger row preserved the state?",
                ],
                "cross_population": [
                    "Add a base-kernel import note to Papers 00-06 naming this seven-paper cycle.",
                    "Move repeated obligation prose in later papers into Paper 06-compatible row shapes.",
                    "Use Paper 04 repair as the common format for rejected routes, negative receipts, and failed joins.",
                ],
                "deferred_return": [
                    "7P.00-06.R1: all later CAM/crystal adapters return to this base-kernel cycle.",
                    "7P.00-06.R2: all later validation tools should emit carrier/correction/repair/ledger fields.",
                ],
                "questions": [
                    "What is the minimal row schema every later paper must provide to be re-admitted to the base kernel?",
                    "Which legacy labels are just missing base-kernel fields?",
                ],
                "new_needs": ["NP-05", "NP-08", "RECEIPT_VERIFIER_CATALOG.md"],
            },
            {
                "id": "7P.07-13",
                "papers": "07-13",
                "focus": "presentation, lattice, temporal/receipt/admission/prediction, quark-face transport",
                "top_inputs": ["07-09", "10-12", "13"],
                "reasoning": [
                    "This block is the first full evidence pipeline from presentation bridge to lattice address to temporal window to receipt/admission to prediction and SM-facing transport.",
                    "The important shared invariant is scope discipline: lookup, finite prediction, algebraic transport, physical mapping, and unbounded prediction must be stored as different claim natures.",
                    "Paper 13 benefits from the entire block: it should import receipt/admission rules before presenting quark-face transport, while Paper 07-09 need the same discipline to avoid continuum or temporal overreach.",
                ],
                "cross_population": [
                    "Route all Paper 13 physics-facing claims through Paper 10/11 receipt/admission fields.",
                    "Route Paper 12 finite CA evidence back into Paper 07/09 presentation and temporal-window boundaries.",
                    "Route Paper 08 terminal lookup capability forward into Paper 13 only as symbolic/algebraic addressability unless calibrated data is attached.",
                ],
                "deferred_return": [
                    "7P.07-13.R1: standard physics correspondences return through NP-12 before promotion.",
                    "7P.07-13.R2: every lattice import returns through lookup/construction/invariant/physical-map split.",
                ],
                "questions": [
                    "Which prediction rows are finite bounded checks?",
                    "Which SM rows are representation hygiene rather than measured physics?",
                ],
                "new_needs": ["NP-01", "NP-02", "NP-12", "SM_BRIDGE_SUPPLEMENT.md"],
            },
            {
                "id": "7P.14-20",
                "papers": "14-20",
                "focus": "curvature, mass, continuum, lattice tower, VOA, observer selection, synthesis ledger",
                "top_inputs": ["14-16", "17-19", "20"],
                "reasoning": [
                    "This block is a residual-meaning stack: repair curvature, mass residue, continuum edge, code/lattice towers, VOA/Moonshine, observer-face selection, and aggregate synthesis all ask what a persistent residual means.",
                    "The shared invariant is that residual meaning depends on both a formal address and an observer/face protocol. Without Paper 19, the block risks treating a selected face as the whole object.",
                    "Paper 20 should aggregate not only statuses but the reasons a residual is still alive: calibration, invariant, observer, lookup receipt, or full theorem burden.",
                ],
                "cross_population": [
                    "Back-route Paper 20 synthesis rows into Papers 14-19 with residual-type fields.",
                    "Attach Paper 19 observer-face slots to Papers 14-18.",
                    "Use Paper 17/18 scope rows to prevent finite tower/seed evidence from becoming full Moonshine or physical claims.",
                ],
                "deferred_return": [
                    "7P.14-20.R1: every residual row returns to a residual-type classifier before NSIT scoring.",
                    "7P.14-20.R2: observer-face selections return to Paper 03 representation transport and Paper 19.",
                ],
                "questions": [
                    "Which residuals are symbolic, numeric, lattice-theoretic, VOA-theoretic, observer-selected, or empirical?",
                    "Which Paper 20 aggregation rows need exact receipt paths?",
                ],
                "new_needs": ["NP-01", "NP-02", "NP-06", "NP-12"],
            },
            {
                "id": "7P.21-27",
                "papers": "21-27",
                "focus": "applied reader through observer delay",
                "top_inputs": ["21-23", "24-26", "27"],
                "reasoning": [
                    "This block is the applied-forge proof of usefulness: reader, materials, protein, games, energy, plasma/shear, and observer-delay protocol.",
                    "The shared invariant is a two-surface model: internal forge addressability and descriptor generation on one side; external domain validation on the other.",
                    "Paper 27 matters because applied claims are observer/process dependent. The same candidate can be internally well-addressed while its empirical validation depends on protocol timing, measurement conditions, and shared-state assumptions.",
                ],
                "cross_population": [
                    "Attach the internal/external validation split to Papers 21-26.",
                    "Route all empirical or benchmark claims to NP-07 and all calibration claims to NP-06/NP-12.",
                    "Route observer-delay constraints from Paper 27 back into applied measurement protocols.",
                ],
                "deferred_return": [
                    "7P.21-27.R1: every applied result returns to Paper 21 reader/adapter contract.",
                    "7P.21-27.R2: every measured result returns to protocol, unit, and dataset slots.",
                ],
                "questions": [
                    "Which applied rows are already supported by internal lookup/descriptor receipts?",
                    "Which applied rows require domain-specific validation before any stronger paper claim?",
                ],
                "new_needs": ["NP-06", "NP-07", "APPLIED_FORGES_WORKBOOK.md"],
            },
            {
                "id": "7P.28-32",
                "papers": "28-32",
                "focus": "game lattices, Monster ceiling, corpus ribbon, retrospective readout, supervisor cursor",
                "top_inputs": ["28-29", "30-32"],
                "reasoning": [
                    "This block is the corpus-return machine. It combines finite game/lattice search, large-invariant ceiling claims, corpus ribbon storage, retrospective readout, and supervisor selection.",
                    "Paper 32 should use Paper 28's bounded-search discipline and Paper 29's invariant-witness burden as examples of how to schedule next work without flattening claim types.",
                    "Papers 30-32 should treat orbital data as active fuel: external papers, supplements, receipts, validators, and CAM memories become assigned return lanes back into Papers 00-29.",
                ],
                "cross_population": [
                    "Attach the orbital audit to Papers 30-32 as active queue data.",
                    "Back-route bounded-game search methods from Paper 28 into Paper 32 supervisor minimality/corridor language.",
                    "Back-route Paper 29 invariant-witness needs into NP-02/NP-09 and the lookup-vs-invariant split.",
                ],
                "deferred_return": [
                    "7P.28-32.R1: every supervisor queue item returns to the earliest paper able to own it.",
                    "7P.28-32.R2: unnumbered orbital data returns through a lane assignment before scoring.",
                ],
                "questions": [
                    "Which orbital artifacts are corpus-level background and which are paper-lane evidence?",
                    "Which tail obligations should become direct edits versus new papers?",
                ],
                "new_needs": ["NP-02", "NP-09", "NP-11", "ORBITAL_DATA_CROSS_POPULATION_AUDIT.md"],
            },
        ],
    },
    "9P": {
        "title": "Internal Reasoning 9-Paper Window Supplement",
        "path": SUPP / "INTERNAL_REASONING_9P_WINDOW_SUPPLEMENT.md",
        "purpose": (
            "The nine-paper layer is the architectural sweep. It turns local and "
            "block windows into long-range bridge candidates and return-to-start "
            "obligations for the supervisor and CAM/crystal playbook."
        ),
        "windows": [
            {
                "id": "9P.00-08",
                "papers": "00-08",
                "focus": "base formal kernel through lattice closure",
                "top_inputs": ["00-02", "03-05", "06-08"],
                "reasoning": [
                    "The first nine papers form the base-to-terminal arc: contract, carrier, correction, representation, repair, transport, ledger, bridge, and lattice closure.",
                    "The architectural insight is that Paper 08 is not a separate capstone; it is the first terminal-address layer for the entire base formal kernel.",
                    "The larger missing data is not only citations or receipts. It is the absence of a single import rule saying how later papers may call a terminal address without inheriting stronger invariant or physical claims.",
                ],
                "bridge_candidates": [
                    "CAM terminal-address schema for E8/Niemeier/Leech/Spectre-like endpoints.",
                    "A base-kernel-to-lattice receipt route: carrier -> correction -> repair -> ledger -> terminal address.",
                    "A reusable lookup/import guard phrase for every later paper.",
                ],
                "return_to_start": [
                    "9P.00-08.R1: every later lattice, tiling, or forge terminal returns to Paper 00-04 admission and Paper 06 ledger.",
                    "9P.00-08.R2: every lookup call returns to Paper 08 scope discipline before being used as evidence.",
                ],
                "cam_queries": [
                    "Find all artifacts with attachment keys `token:lattice`, `token:leech`, `token:e8`, `token:glue`, and route them to lookup/construction/invariant/physical-map slots.",
                    "Find all Paper 00-08 obligations lacking receipt paths and assign the nearest validator or supplement.",
                ],
                "handoff": [
                    "Does the CAM schema store terminal addresses with enough claim-nature metadata?",
                    "Which base-kernel fields are mandatory for a later paper to import Paper 08?",
                ],
            },
            {
                "id": "9P.09-17",
                "papers": "09-17",
                "focus": "temporal windows through E6/E8 tower",
                "top_inputs": ["09-11", "12-14", "15-17"],
                "reasoning": [
                    "This window is the temporal/receipt/physics bridge into code towers. It joins Hamiltonian windows, master receipts, admission gates, CA prediction, quark/curvature/mass/continuum language, and E6/E8 tower claims.",
                    "The architectural issue is mixed proof burden. Finite CA receipts, algebraic transport, standard physics correspondence, numerical continuum analysis, and exceptional-lattice tower claims need different lanes.",
                    "A lot of missing richness can be recovered by reattaching standard formalism: finite verification, standard electron-hole-exciton language, SU(2)/SU(3) representation hygiene, numerical analysis, and code/lattice lookup all already answer parts of the burden.",
                ],
                "bridge_candidates": [
                    "A standard-formalism reapplication table for Papers 09-17.",
                    "A receipt import map from Paper 10/11 into every physics-facing row.",
                    "A tower-scope table that separates E6/E7/E8 symbolic transport, lookup, invariant, and physical calibration.",
                ],
                "return_to_start": [
                    "9P.09-17.R1: every physics-facing claim returns to Paper 11 admission and NP-06/NP-12 calibration/correspondence.",
                    "9P.09-17.R2: every finite verification row returns to Paper 12 bounded-state evidence before unbounded language is used.",
                    "9P.09-17.R3: every tower row returns to Paper 08/17 lookup-vs-invariant discipline.",
                ],
                "cam_queries": [
                    "Find all rows mentioning mass, hole, excitation, energy, curvature, continuum, carrier, and bind them to standard-physics or calibration slots.",
                    "Find all receipt/admission references in Papers 09-17 and assign missing exact paths.",
                ],
                "handoff": [
                    "Which standard formalism entries can be cited immediately without claiming CQE invented them?",
                    "Which exceptional tower claims need new invariant receipts?",
                ],
            },
            {
                "id": "9P.18-26",
                "papers": "18-26",
                "focus": "VOA/Moonshine through energetic and plasma/applied physical bridges",
                "top_inputs": ["18-20", "21-23", "24-26"],
                "reasoning": [
                    "This window connects finite VOA/Moonshine seeds, observer selection, synthesis ledger, applied reader, materials, proteins, games, energy, and plasma/shear.",
                    "The common architectural form is projection into a domain: a high-structure symbolic substrate is read through an observer/adapter into an applied descriptor surface.",
                    "The main missing data is the lack of a uniform applied-evidence table. Internal descriptor/lookup claims, finite search claims, external benchmark claims, and measured physical claims should be separated and then cross-populated across Papers 21-26.",
                ],
                "bridge_candidates": [
                    "A domain adapter contract shared by MorphForge, MetaForge, FoldForge, KnightForge, energy maps, and plasma/shear maps.",
                    "A projection-readout table from Paper 18/19 structures into Paper 21 applied readers.",
                    "A validation ladder: internal descriptor -> benchmark -> external experiment -> calibrated physical claim.",
                ],
                "return_to_start": [
                    "9P.18-26.R1: every applied descriptor returns to Paper 21 reader/adapter contract.",
                    "9P.18-26.R2: every physical/material claim returns to NP-06/NP-07/NP-12 before stronger language.",
                    "9P.18-26.R3: every high-structure import returns to Paper 18/19 observer/static-template scope.",
                ],
                "cam_queries": [
                    "Find all applied-forge artifacts with descriptors, candidates, Pareto scores, PDB/material/plasma/game terms, and assign internal/external validation lanes.",
                    "Find all Paper 18-26 references to observer, face, projection, readout, and adapter, then link them to Paper 21.",
                ],
                "handoff": [
                    "Which applied rows can be strengthened by existing no-cost lookup/descriptor receipts?",
                    "Which applied rows should become NP-07 benchmark tables instead of remaining in the spine?",
                ],
            },
            {
                "id": "9P.27-32",
                "papers": "27-32",
                "focus": "observer delay through supervisor cursor",
                "top_inputs": ["27-29", "30-32"],
                "reasoning": [
                    "The final window is the return/control arc: observer delay, game lattice bounds, Monster ceiling, corpus ribbon, retrospective readout, and supervisor cursor.",
                    "The tail should operate like a scheduler over the whole corpus. It should not just state what remains; it should assign orbital data, select next edits, and send obligations back to the earliest responsible paper.",
                    "Paper 32 becomes much stronger when it imports Paper 27 protocol semantics, Paper 28 finite bounded-search discipline, Paper 29 witness/invariant burden, and Paper 30-31 corpus readout.",
                ],
                "bridge_candidates": [
                    "A supervisor queue keyed by paper, claim nature, attached orbital data, and next action.",
                    "A return-to-start protocol: selected item -> owning paper -> supplement/orbital evidence -> NSIT/grading.",
                    "A CAM/crystal query playbook that loads orbital artifacts and shines them through all indexed paper faces.",
                ],
                "return_to_start": [
                    "9P.27-32.R1: every tail obligation returns to Papers 00-06 for re-admission and ledger storage.",
                    "9P.27-32.R2: every unnumbered orbital artifact returns to a numbered lane or corpus-level background lane.",
                    "9P.27-32.R3: every supervisor/minimality row returns to bounded/unbounded split before scoring.",
                ],
                "cam_queries": [
                    "Find all unnumbered formal papers, supplements, receipts, validators, and CAM memories not lane-assigned to 00-32.",
                    "For each supervisor queue item, query upstream papers for earlier ownership before creating a new paper.",
                ],
                "handoff": [
                    "Which orbital artifacts should be auto-assigned by token match, and which need human/NSIT review?",
                    "Which tail claims are scheduling claims rather than mathematical claims?",
                ],
            },
        ],
    },
}


def bullet(lines: list[str], values: list[str]) -> None:
    for value in values:
        lines.append(f"- {value}")


def render_layer(layer_key: str, layer: dict) -> str:
    lines: list[str] = []
    lines.append(f"# {layer['title']}")
    lines.append("")
    lines.append("**Status:** active pyramid pass.")
    lines.append("**Method note:** this pass adds reasoning, cross-paper applications, and")
    lines.append("back-application slots only. NSIT and grading tools own validity labels,")
    lines.append("promotion decisions, and scores.")
    lines.append("")
    lines.append("## Pyramid Position")
    lines.append("")
    lines.append(
        "The `00-32` three-paper reasoning supplements are the fine-grain top "
        "of the pyramid. This layer stacks below them as a broader connected-state "
        "view. It is meant to push data both forward into later papers and backward "
        "to the earliest paper that can own the obligation."
    )
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(layer["purpose"])
    lines.append("")
    lines.append("## Window Map")
    lines.append("")
    lines.append("| Window | Papers | Focus | Three-paper inputs |")
    lines.append("|---|---|---|---|")
    for window in layer["windows"]:
        lines.append(
            f"| `{window['id']}` | {window['papers']} | {window['focus']} | "
            f"{', '.join(window['top_inputs'])} |"
        )
    lines.append("")
    lines.append("## Concurrent Window Reasoning")
    lines.append("")
    for window in layer["windows"]:
        lines.append(f"### {window['id']} - Papers {window['papers']}")
        lines.append("")
        lines.append(f"**Focus:** {window['focus']}")
        lines.append("")
        lines.append("#### Reasoning Additions")
        lines.append("")
        bullet(lines, window["reasoning"])
        lines.append("")
        lines.append("#### Cross-Population Moves")
        lines.append("")
        bullet(lines, window["cross_population"] if "cross_population" in window else window["bridge_candidates"])
        lines.append("")
        if "return_slots" in window:
            title = "Deferred Back-Application Slots"
            values = window["return_slots"]
        elif "deferred_return" in window:
            title = "Deferred Return Lanes"
            values = window["deferred_return"]
        else:
            title = "Return-To-Start Obligations"
            values = window["return_to_start"]
        lines.append(f"#### {title}")
        lines.append("")
        bullet(lines, values)
        lines.append("")
        if "attachments" in window:
            lines.append("#### Candidate Tool/Data Attachments")
            lines.append("")
            bullet(lines, [f"`{item}`" for item in window["attachments"]])
            lines.append("")
        if "new_needs" in window:
            lines.append("#### Candidate New-Paper Or Supplement Needs")
            lines.append("")
            bullet(lines, [f"`{item}`" for item in window["new_needs"]])
            lines.append("")
        if "cam_queries" in window:
            lines.append("#### Candidate CAM/Crystal Query Patterns")
            lines.append("")
            bullet(lines, window["cam_queries"])
            lines.append("")
        lines.append("#### NSIT / Grading Handoff Questions")
        lines.append("")
        bullet(lines, window["handoff"] if "handoff" in window else window["questions"])
        lines.append("")
    lines.append("## Layer Output")
    lines.append("")
    lines.append(
        f"This `{layer_key}` layer should be used as a queue for direct paper edits, "
        "orbital backlink insertion, and NSIT/grading handoff. It deliberately "
        "does not decide validity state."
    )
    lines.append("")
    return "\n".join(lines)


def render_index() -> str:
    lines: list[str] = []
    lines.append("# Internal Reasoning Pyramid Index")
    lines.append("")
    lines.append(
        "The pyramid stacks reasoning windows from local to architectural scale. "
        "The three-paper supplements remain the fine-grain layer; the 5/7/9-paper "
        "windows recombine them into broader connected states."
    )
    lines.append("")
    lines.append("| Layer | File | Window count | Job |")
    lines.append("|---|---|---:|---|")
    for key, layer in LAYERS.items():
        lines.append(
            f"| {key} | `{layer['path'].name}` | {len(layer['windows'])} | {layer['purpose']} |"
        )
    lines.append("")
    lines.append("## Reading Direction")
    lines.append("")
    lines.append("- Top-down: start from a numbered three-paper supplement, then read the 5P, 7P, and 9P windows that include it.")
    lines.append("- Bottom-up: start from a 9P architectural obligation, then return through the 7P and 5P layers to the earliest owning paper.")
    lines.append("- Sideways: use the orbital audit to attach supplements, receipts, validators, CAM memory, and external formal papers to the active window.")
    lines.append("")
    lines.append("## Kimi Window Crosswalk")
    lines.append("")
    lines.append(
        "Kimi's MannyAI paper-brain build supplies a second window lattice at "
        "`D:\\DockerContainers\\Manny Docker Starter\\mannyai\\brain\\window_summary.json`. "
        "This is not a replacement for the 3/5/7/9 reasoning pyramid; it is an "
        "orthogonal binary stacking layer that should be read concurrently."
    )
    lines.append("")
    lines.append("| Kimi layer | Count | Windows | Use with this pyramid |")
    lines.append("|---|---:|---|---|")
    lines.append("| size-2 | 16 | `00-01`, `02-03`, ..., `30-31` | Attach local node-pair evidence before three-paper reasoning is promoted into a broader lane. |")
    lines.append("| size-4 | 8 | `00-03`, `04-07`, ..., `28-31` | Compare against 5P windows to find one-paper-overhang obligations and missing neighbors. |")
    lines.append("| size-8 | 4 | `00-07`, `08-15`, `16-23`, `24-31` | Compare against 7P and 9P windows to find block-scale evidence already computed by Kimi. |")
    lines.append("| size-16 | 2 | `00-15`, `16-31` | Use as corpus-halves for receipt/admission versus applied/supervisor balance. |")
    lines.append("| size-32 | 1 | `00-31` | Use as whole-corpus paper-brain evidence, especially with Kimi standards reports. |")
    lines.append("")
    lines.append(
        "Kimi standards reports should enter as conformance/orbital evidence: "
        "`corpus_conformance_report.json` reports `192/192` PASS for canonical "
        "32-paper standards checks, `suite_resolution_report.json` resolves `188/188` "
        "items across `96` papers, and `glue_report.json` maps `140/142` obligations "
        "to candidate routes. These are not validity labels; they are strong routing "
        "and cross-population inputs for NSIT/grading."
    )
    lines.append("")
    lines.append("## Active Cross-Layer Themes")
    lines.append("")
    lines.append("- base-kernel admission and ledger preservation")
    lines.append("- lookup, construction, invariant, and physical-mapping split")
    lines.append("- standard formalism reapplication before residual scoring")
    lines.append("- internal forge descriptor claims versus external validation")
    lines.append("- finite bounded verification versus unbounded/minimality claims")
    lines.append("- observer/static-template/protocol separation")
    lines.append("- supervisor return lanes back to the start of the paper list")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    manifest = {"schema": "internal_reasoning_pyramid.v1", "layers": {}}
    for key, layer in LAYERS.items():
        layer["path"].write_text(render_layer(key, layer), encoding="utf-8")
        manifest["layers"][key] = {
            "file": str(layer["path"]),
            "window_count": len(layer["windows"]),
            "windows": [
                {
                    "id": window["id"],
                    "papers": window["papers"],
                    "focus": window["focus"],
                    "top_inputs": window["top_inputs"],
                }
                for window in layer["windows"]
            ],
        }
    index_path = SUPP / "INTERNAL_REASONING_PYRAMID_INDEX.md"
    index_path.write_text(render_index(), encoding="utf-8")
    json_path = SUPP / "INTERNAL_REASONING_PYRAMID_INDEX.json"
    json_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"wrote {index_path}")
    print(f"wrote {json_path}")
    for layer in LAYERS.values():
        print(f"wrote {layer['path']}")


if __name__ == "__main__":
    main()
