from pathlib import Path


ROOT = Path(r"D:\Paper Reworks\publication_series\Formalizing_LCR_Unifying_Standard_Models")


COMMON_INPUTS = [
    "NSIT_PAPER_EVIDENCE_INVENTORY.json",
    "NSIT_TOOL_CLOSURE_MATRIX.md",
    "CAM_CLAIM_100_SCORE_AUDIT.md",
    "ORBITAL_DATA_CROSS_POPULATION_AUDIT.md",
    "AGENT_CRYSTAL_WORK_HARVEST.md",
    "supplements/RECEIPT_VERIFIER_CATALOG.md",
    "supplements/OBLIGATION_LEDGER_SUPPLEMENT.md",
    "supplements/CRYSTAL_CAM_PROJECTOR_SUPPLEMENT.md",
]


PAPERS = [
    {
        "id": "FLCR-01",
        "legacy": "00",
        "source": "00_Established_Grounding_and_Axiom_Contract.md",
        "title": "Grounding Contract And Axiom Discipline",
        "score": "96",
        "class": "near publishable burden contract",
        "abstract": (
            "This paper installs the publication contract for the FLCR series. It treats "
            "LCR as a conservative extension discipline: imported mathematics remains "
            "external, new structure is admitted only through named bridges, and every "
            "strong claim must carry a lane, receipt, validator, boundary, and falsifier. "
            "The result is not merely editorial hygiene. It is the root type system for "
            "the corpus, separating finite internal proof, standard theorem import, "
            "CAM/crystal reapplication, normal-form promotion, external calibration, "
            "grand synthesis, and open falsifier lanes."
        ),
        "definitions": [
            ("Conservative extension contract", "A rule that later papers may add typed bridges without silently rewriting imported theorems or earlier receipts."),
            ("Claim lane", "A required type assigned to every proposition, theorem, empirical statement, synthesis claim, and obligation."),
            ("Receipt-bound statement", "A statement whose admissibility depends on a reproducible input-output-residue record and a named verifier."),
            ("Only-addition rule", "The local governance rule that new primitives or bridges must be declared as additions, not hidden reinterpretations of prior sources."),
            ("Deferred mapping slot", "A reserved place where later papers may attach stronger evidence while preserving the paper-local invariant."),
        ],
        "construction": [
            "Start from the legacy Paper 00 burden table and retain the rule that imported theorems are cited rather than reinvented.",
            "Promote the burden table into the FLCR claim-lane schema so every later claim has a type and a boundary.",
            "Treat exhaustive finite enumeration over declared finite domains as proof for that finite domain, while physical or interpretive claims require later calibration.",
            "Route corpus memory, CAM crystals, Kimi standards, and Claude scoring as evidence inputs, not as untyped authority.",
            "Install falsifier-first writing: every theorem row must identify how it can fail, what would demote it, and what evidence would promote it.",
        ],
        "claims": [
            ("normal_form_result", "The FLCR series begins with a typed claim grammar rather than prose-only status labels.", "CLAIM_LANE_SCHEMA.json; Paper 00 supplement; Kimi standards lane", "The grammar governs publication admission; it is not itself a theorem about physical systems."),
            ("receipt_bound_internal_result", "Finite internal statements may be closed by exhaustive verifier coverage when the domain is fully enumerated.", "Legacy Paper 00; receipt catalog; T3-T7 foundation references", "Only finite declared domains receive this proof status."),
            ("standard_theorem_citation_bound_result", "External mathematical results remain external theorem imports with citation and burden records.", "Paper 00 burden contract; SERIES_MAP routing", "Citation polish remains required before final arXiv package."),
            ("cam_crystal_reapplication_result", "CAM/crystal memory may reapply existing receipts and source routes across papers.", "PAPER_REWORKS_CRYSTAL_PROJECTION.json; AGENT_CRYSTAL_WORK_HARVEST.md", "CAM evidence must name address, source, and receipt or remain routing evidence."),
            ("falsifier_or_open_obligation", "A claim lacking lane, evidence, or boundary is inadmissible in the formal paper body.", "NSIT validity rebuild protocol; claim-lane schema", "Inadmissible does not mean false; it means not yet publication-typed."),
        ],
        "evidence": [
            "CAM 100 score: 96, system-composition closed with citation polish remaining.",
            "NSIT inventory records validators, receipts, formal artifacts, supplements, and memory/CAM artifacts as available evidence classes.",
            "The claim-lane schema supplies the new publication identity's root admission discipline.",
            "Internal supplement identifies conservative extension, proof-carrying code, finite model checking, and claim taxonomy as type system.",
        ],
        "limitations": [
            "This paper does not prove later physics claims; it defines the proof burden those claims must satisfy.",
            "The final citation table must be attached before publication-ready status.",
            "A receipt can close an internal finite claim without closing an external empirical interpretation.",
        ],
        "companion": [
            "Paper 1 is the rules of the game. It says the corpus can be ambitious, but it cannot be vague about why a claim is allowed.",
            "The important move is that open and closed are replaced by typed lanes. A claim can be internally receipt-bound, citation-bound, CAM-reapplied, normal-form bound, calibration-bound, synthesis-bound, or a falsifier.",
            "This lets later papers make stronger claims without collapsing every kind of evidence into the same bucket.",
        ],
        "workbook": [
            "Open CLAIM_LANE_SCHEMA.json and classify five claims from legacy Paper 00.",
            "For each claim, record evidence path, validator path, boundary, and falsifier.",
            "Check whether the claim is finite-domain, standard-theorem, CAM-route, calibration, or synthesis.",
            "Rewrite any unlabeled claim as a typed row before allowing it into formal.md.",
        ],
    },
    {
        "id": "FLCR-02",
        "legacy": "01",
        "source": "01_LCR_Chain_Carrier.md",
        "title": "The LCR Carrier",
        "score": "94",
        "class": "internally closed carrier theorem",
        "abstract": (
            "This paper defines the LCR carrier as the canonical radius-1 local readout: "
            "a left address, distinguished center, and right address over a finite state "
            "alphabet. The central result is a minimality and symmetry theorem. Fewer "
            "than three slots collapse either the center or one boundary address; with "
            "three binary slots the carrier has eight states, binomial shell profile "
            "1,3,3,1, a left-right reversal action, and a shell-2 doublet-plus-pivot "
            "interface. Later spinor, observer, and Standard Model translations are "
            "deferred; this paper closes the finite carrier semantics."
        ),
        "definitions": [
            ("LCR carrier", "A triple (L,C,R) whose center is distinguished and whose two boundary addresses remain address-distinct."),
            ("Radius-1 local readout", "The standard elementary cellular automaton neighborhood read around a center cell."),
            ("Shell grade", "The Hamming weight of a binary LCR state, producing the finite profile 1,3,3,1."),
            ("Reversal action", "The C2 action that swaps L and R while preserving C."),
            ("Shell-2 interface", "The grade-two stratum with one reversal-fixed pivot and one two-state chiral orbit."),
        ],
        "construction": [
            "Enumerate all binary triples in {0,1}^3.",
            "Grade each triple by shell weight and record the binomial count by grade.",
            "Apply left-right reversal and compute fixed points plus two-element orbits.",
            "Identify the shell-2 fixed pivot (1,0,1) and the boundary-distinct pair (1,1,0), (0,1,1).",
            "State minimality as an arity lower bound: center plus two address-distinct boundaries require three slots.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "The binary LCR carrier has exactly eight states with shell profile 1,3,3,1.", "verify_lcr_carrier; core.SHELL2_STATES; receipt catalog", "Only the declared binary carrier is closed here."),
            ("receipt_bound_internal_result", "Three slots are minimal for center plus two address-distinct boundaries.", "Paper 01 arity proof; internal supplement", "This is a data-structure lower bound, not a claim about all possible physical carriers."),
            ("receipt_bound_internal_result", "Left-right reversal is a C2 action on the carrier.", "Paper 01 verifier; shell-2 doublet receipt", "The physical spinor reading is deferred."),
            ("standard_theorem_citation_bound_result", "Radius-1 CA language supplies a standard external framing for LCR.", "Elementary cellular automata standard model; Paper 02 intake", "Standard CA language does not by itself add CQE claims."),
            ("falsifier_or_open_obligation", "Physical spinor or observer claims require later bridge evidence.", "NP-10 route; Papers 19 and 27", "No measured spinor transport is asserted in FLCR-02."),
        ],
        "evidence": [
            "CAM 100 score: 94, internally closed with physical spinor transport deferred.",
            "NSIT matrix lists shell-2 doublet and O8 double-cover closures as reusable support.",
            "Internal supplement supplies radius-1 CA, C2 action, binomial shell grading, and address/value separation.",
        ],
        "limitations": [
            "The shell-2 doublet is an interface type, not a particle claim.",
            "SU(2) or spinor language can be explanatory only until later bridge receipts attach.",
            "Carrier minimality depends on preserving center and boundary addresses as distinct roles.",
        ],
        "companion": [
            "Paper 2 says the whole system starts with a local window: left, center, right.",
            "The key insight is address separation. Even if two values match, the two sides are still different positions.",
            "That is why the carrier can later support repair, triality, observer, and lattice translations without losing provenance.",
        ],
        "workbook": [
            "List the eight binary triples in lexicographic order.",
            "Compute shell weight for each triple and verify the 1,3,3,1 profile.",
            "Apply L/R reversal and mark fixed states and two-state orbits.",
            "Highlight the shell-2 pivot and chiral pair.",
            "Record a receipt row with input set, operation, output orbits, and falsifier condition.",
        ],
    },
    {
        "id": "FLCR-03",
        "legacy": "02",
        "source": "02_Correction_Surface.md",
        "title": "Correction Surface And Residual Accounting",
        "score": "93",
        "class": "internally closed correction surface",
        "abstract": (
            "This paper turns the difference between a linear local carrier and the target "
            "Rule 30 update into a finite residual surface. In algebraic normal form over "
            "GF(2), Rule 30 is L xor C xor R xor C R, Rule 90 is L xor R, and the residual "
            "is C xor C R, equivalently C and not R. The correction surface is therefore a "
            "two-state firing set over the eight LCR states. It functions as a syndrome, "
            "innovation term, and typed obstruction for later repair, not as an untyped "
            "mystery field."
        ),
        "definitions": [
            ("Rule 30 local form", "The Boolean update L xor C xor R xor C R over GF(2)."),
            ("Rule 90 local form", "The linear Boolean update L xor R."),
            ("Correction residual", "The Boolean difference between Rule 30 and Rule 90, equal to C and not R."),
            ("Firing set", "The two LCR states satisfying C=1 and R=0."),
            ("Syndrome-like receipt", "A record that localizes mismatch without itself proving a downstream repair."),
        ],
        "construction": [
            "Write Rule 30 and Rule 90 in algebraic normal form over GF(2).",
            "Subtract them by xor to obtain C xor C R.",
            "Normalize C xor C R to C and not R over binary values.",
            "Enumerate all eight LCR states and select exactly the states with C=1, R=0.",
            "Pass the residual as typed obligation data to Paper 04 rather than promoting it to proof.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "The correction residual is exactly C and not R on the binary LCR carrier.", "rule90_linearization.py; correction surface receipt", "Only the radius-1 binary local rule is closed."),
            ("receipt_bound_internal_result", "The firing set has exactly two states.", "Exhaustive eight-state enumeration", "Any three-state variant is a failed import unless scoped to another domain."),
            ("normal_form_result", "Correction can be represented as residual, syndrome, innovation, or obstruction depending on downstream context.", "Internal supplement; NSIT reasoned closure", "These are explanatory normal forms, not external physics identities."),
            ("cam_crystal_reapplication_result", "Correction residuals become addressable CAM objects for later obligation routing.", "PAPER_REWORKS_CRYSTAL_PROJECTION.json; obligation supplements", "CAM addressability does not close McKay, VOA, or empirical claims."),
            ("falsifier_or_open_obligation", "Unbounded McKay or Moonshine parity promotion remains deferred.", "NP-01 route; Papers 09 and 18", "A bounded residual receipt is not an unbounded arithmetic theorem."),
        ],
        "evidence": [
            "CAM 100 score: 93, internally closed with McKay parity routed beyond paper-local scope.",
            "NSIT matrix closes Rule30 = Rule90 plus correction and Lucas decomposition as the verifiable core.",
            "Internal supplement supplies algebraic normal form, syndrome decoding analogy, and finite proof boundary.",
        ],
        "limitations": [
            "This paper does not solve unbounded Rule 30 prediction.",
            "Physical field language is deferred to calibrated bridge papers.",
            "Later corrections may aggregate the residual, but they cannot alter the local truth table without falsifying this paper.",
        ],
        "companion": [
            "Paper 3 says: do not call the mismatch a mystery. Compute it.",
            "When the simpler Rule 90 carrier misses Rule 30, the missing part is exactly C and not R.",
            "That exact residual becomes the thing later papers can repair, transport, ledger, and query.",
        ],
        "workbook": [
            "Make an eight-row truth table with L, C, R, Rule30, Rule90, and residual.",
            "Confirm residual is 1 only when C=1 and R=0.",
            "Record the two firing states and reject any extra firing state as a falsifier.",
            "Attach the row set to a CAM/crystal address for later Paper 04 repair.",
        ],
    },
    {
        "id": "FLCR-04",
        "legacy": "03",
        "source": "03_D4_J3_Triality_Surface.md",
        "title": "D4, J3(O), Triality, And Representation Transport",
        "score": "94",
        "class": "internally closed finite chart registration",
        "abstract": (
            "This paper registers the eight LCR states across multiple finite readouts: "
            "LCR triples, axis/sheet coordinates, diagonal J3(O)-style idempotents, and "
            "finite group-action bookkeeping. The central claim is chart registration, "
            "not unrestricted exceptional dynamics. The axis coordinate forms an "
            "antipodal quotient; the sheet bit lifts a complementary pair back to a "
            "specific state. Claims that survive every registered readout become stronger "
            "corpus objects because their address is preserved across representation."
        ),
        "definitions": [
            ("Finite coordinate atlas", "A set of lossless charts over the same eight-state carrier."),
            ("Axis/sheet codec", "An antipodal quotient by complement plus a sheet bit that restores the selected state."),
            ("Diagonal J3(O) carrier", "A diagonal idempotent presentation used without off-diagonal octonion multiplication."),
            ("Representation transport", "Movement of a state or claim through registered charts while preserving identity."),
            ("Chart-invariance rule", "A later paper may consume a transported claim only when its required charts agree or the dropped chart is declared."),
        ],
        "construction": [
            "Map each LCR state into complement-pair axis coordinates.",
            "Use the sheet bit to recover the original state from the quotient pair.",
            "Represent binary diagonal states as idempotent diagonal carriers.",
            "Track reversal, S3, D12, and block-tower actions as finite group actions on the registered state set.",
            "Export a representation-invariance rule to later papers.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "LCR, axis/sheet, and diagonal readings are registered over the same finite carrier.", "T1-T4 algebra foundation; chart/J3(O) isomorphism receipt", "The claim is diagonal/local unless a full off-diagonal receipt is attached."),
            ("receipt_bound_internal_result", "The axis/sheet codec is a lossless quotient-plus-lift for the eight states.", "D4 atlas and round-trip receipts", "Renaming the codec requires a migration receipt."),
            ("standard_theorem_citation_bound_result", "Group-action and idempotent language provide standard finite-algebra framing.", "Finite group action and idempotent algebra background", "Standard terms do not imply full exceptional Lie dynamics."),
            ("cam_crystal_reapplication_result", "Representation-invariant addresses are suitable CAM/crystal keys.", "crystal projector supplement; source routing matrix", "A key is not proof of all structure stored under it."),
            ("falsifier_or_open_obligation", "Full D4/F4/off-diagonal exceptional dynamics remain routed to later work.", "NP-04 route; Papers 17 and 18", "FLCR-04 closes registration, not the whole exceptional program."),
        ],
        "evidence": [
            "CAM 100 score: 94, internally closed with full D4/F4/off-diagonal theorem deferred.",
            "NSIT matrix records T1-T4 algebra foundation, T5-T7 closure, D12 idempotent chain, and block-tower receipts.",
            "Internal supplement supplies coordinate atlas, antipodal quotient, diagonal subalgebra guard, and representation invariance.",
        ],
        "limitations": [
            "J3(O) language is diagonal/local unless explicitly upgraded.",
            "Finite group-action receipts do not by themselves supply measured physics.",
            "Historical naming variants must be normalized by adapter receipts, not silently merged.",
        ],
        "companion": [
            "Paper 4 is the translation desk. It proves that the same finite object can be read in several coordinate languages.",
            "The reason this matters is practical: later papers can move between local carrier, lattice, algebra, and observer surfaces without losing the object.",
            "It is not claiming all exceptional geometry at once. It claims the registered finite bridge that later exceptional papers can build on.",
        ],
        "workbook": [
            "Choose an LCR state and write its complement pair.",
            "Drop to axis, then use the sheet bit to recover the original state.",
            "Write the same state as a diagonal binary idempotent.",
            "Record whether a proposed claim survives LCR, axis/sheet, and diagonal readings.",
            "Flag any dropped representation as an explicit obligation.",
        ],
    },
    {
        "id": "FLCR-05",
        "legacy": "04",
        "source": "04_Boundary_Repair.md",
        "title": "Typed Boundary Repair",
        "score": "93",
        "class": "internally closed typed repair constraint",
        "abstract": (
            "This paper converts failed joins into typed, replayable repair rows. A failure "
            "is not promoted into success; it becomes a proof obligation with state, "
            "coordinate, reason, route, source, target, and admissibility fields. Boundary "
            "repair is therefore a schema and state-machine discipline for the corpus. "
            "Its idempotence result says that already typed failures remain stable under "
            "repair normalization, while untyped failures are rejected."
        ),
        "definitions": [
            ("Boundary failure", "A failed join, mismatch, or transport attempt at a declared paper boundary."),
            ("Repair row", "A structured obligation record with enough fields to route and replay the failure."),
            ("Typed exception", "A failure promoted to an inspectable type rather than treated as a passed claim."),
            ("Next legal route", "A graph edge naming the verifier, paper, or adapter allowed to process the repair row."),
            ("Idempotent repair", "A repair normalization that leaves already typed repair rows unchanged."),
        ],
        "construction": [
            "Receive the Paper 03 registered state plus the Paper 02 correction residual.",
            "Reject untyped failure records as inadmissible.",
            "Normalize typed failures into repair rows with source, target, reason, route, and boundary.",
            "Check that repeated normalization returns the same row.",
            "Export the repair row to Paper 05 as payload and to Paper 06 as ledger edge.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "Two Paper 02 interaction states convert into typed boundary repair constraints while preserving Paper 03 coordinates.", "boundary_repair_receipt.json; verify_boundary_repair.py", "The constraints are not downstream proofs."),
            ("receipt_bound_internal_result", "Repair normalization is idempotent on already typed rows.", "Paper 04 verifier; repair schema checks", "Idempotence holds for declared row schema."),
            ("normal_form_result", "Boundary repair is equivalent to proof-obligation generation for the corpus workflow.", "Internal supplement; formal-methods analogy", "The analogy is structural unless encoded in a proof assistant."),
            ("cam_crystal_reapplication_result", "Repair rows are CAM-addressable obligations.", "OBLIGATION_LEDGER_SUPPLEMENT.md; crystal projector supplement", "Addressability does not close the obligation."),
            ("falsifier_or_open_obligation", "Untyped failure records must be rejected.", "Paper 04 falsifier; claim-lane schema", "A domain-specific extension must still preserve minimum replay fields."),
        ],
        "evidence": [
            "CAM 100 score: 93, internally closed with shared ledger population and examples remaining.",
            "Legacy paper records a 7/7 boundary repair receipt.",
            "Internal supplement supplies typed exception, proof obligation, Hoare pre/post condition, and state-machine routing language.",
        ],
        "limitations": [
            "A repair row is a constraint, not a proof.",
            "GR, oloid, dust, or material repair interpretations belong to later bridge papers.",
            "Domain-specific repair schemas may add fields but cannot remove replay essentials.",
        ],
        "companion": [
            "Paper 5 is where failure becomes useful.",
            "Instead of saying a boundary mismatch is closed, the system records exactly what failed and where it must go next.",
            "That is the difference between a vague open problem and a springboard: the obligation has shape, address, route, and replay data.",
        ],
        "workbook": [
            "Take one correction firing state from FLCR-03.",
            "Write a repair row with state, coordinate, reason, source paper, target paper, route, and falsifier.",
            "Run the row through repair normalization twice and confirm it does not change.",
            "Create one invalid row missing a route and mark why it must be rejected.",
        ],
    },
    {
        "id": "FLCR-06",
        "legacy": "05",
        "source": "05_Oloid_Path_Carrier.md",
        "title": "Oloid Path Carrier And Transport Geometry",
        "score": "91",
        "class": "system-composition closeable finite transport",
        "abstract": (
            "This paper defines a finite path carrier that transports typed repair payloads "
            "through legal graph-adjacent moves. The strongest formal reading is a "
            "deterministic finite-state transducer: repeated input bits act on a 16-state "
            "carrier, while payload metadata remains noninterfering side-channel data. "
            "The paper closes graph-continuous symbolic transport, not physical oloid "
            "rolling or unbounded prediction."
        ),
        "definitions": [
            ("Path carrier", "A finite transport object with legal adjacency, phase, sheet, parity, and head/tail readout."),
            ("Finite-state transducer", "A deterministic machine whose input word induces carrier transitions and output readouts."),
            ("Payload noninterference", "The property that attached metadata does not change the transition function."),
            ("Graph-continuous transport", "A path whose neighboring states are adjacent in the declared transition graph."),
            ("Physical geometry guard", "The rule that geometric or measured oloid claims require a later calibrated model."),
        ],
        "construction": [
            "Define carrier state as sheet mod 2, phase mod 4, and parity, giving 16 finite states.",
            "Define legal roll transitions and reject invalid bits or discontinuous jumps.",
            "Attach a Paper 04 repair row as payload.",
            "Verify that payload attachment does not alter the carrier transition.",
            "Export path receipts to Paper 07 and temporal windows to Paper 10.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "The path carrier is a deterministic finite-state transducer over the declared state space.", "oloid carrier family receipt; Paper 05 verifier", "Physical oloid geometry is not closed here."),
            ("receipt_bound_internal_result", "Repair payload is noninterfering metadata.", "payload noninterference checks", "Only declared payload fields are covered."),
            ("normal_form_result", "Continuity means graph adjacency unless a physical metric is attached.", "Internal supplement; Paper 07 bridge", "No smooth dynamics or force law is asserted."),
            ("cam_crystal_reapplication_result", "Path states and payloads are addressable as CAM carrier objects.", "MannyAI CAM/crystal routes; applied forge workbook", "CAM address does not prove real-world motion."),
            ("falsifier_or_open_obligation", "E6/E7/E8 lifts and physical oloid models remain routed.", "Papers 08, 17, 22, 26; NP-02/NP-06", "A later lattice receipt may strengthen the lift without changing this transport theorem."),
        ],
        "evidence": [
            "CAM 100 score: 91, system-composition closeable.",
            "NSIT matrix records oloid carrier family closure by batch tool unison.",
            "Internal supplement supplies transducer, monoid action, noninterference, and graph-continuity language.",
        ],
        "limitations": [
            "Graph-continuous transport is not measured physical kinematics.",
            "The carrier does not solve unbounded Rule 30 prediction.",
            "Holonomy, gauge, or gluon readings are deferred translation claims.",
        ],
        "companion": [
            "Paper 6 gives the obligation something to ride on.",
            "The repair row can move through a legal path without changing the path's rule.",
            "This is important because the system can carry context forward while preserving the clean finite machine underneath.",
        ],
        "workbook": [
            "Define a small state tuple: sheet, phase, parity, payload.",
            "Apply a short input word and record each legal roll.",
            "Repeat the run with an attached repair payload and confirm the carrier states match.",
            "Introduce an illegal jump and record the rejection receipt.",
        ],
    },
    {
        "id": "FLCR-07",
        "legacy": "06",
        "source": "06_Causal_Link_and_Obligation_Ledger.md",
        "title": "Causal Links And Obligation Ledgers",
        "score": "92",
        "class": "system-composition closeable ledger",
        "abstract": (
            "This paper turns the first six constructions into an auditable dependency "
            "graph. Claims, receipts, repair rows, failed extraction verdicts, and open "
            "obligations are represented as typed edges rather than prose annotations. "
            "The result is a corpus ledger: a build-like graph where proof-support edges, "
            "workflow edges, negative results, and future obligations remain distinct."
        ),
        "definitions": [
            ("Causal link", "A typed edge from one paper object to another with declared support relation."),
            ("Obligation edge", "A non-proof edge carrying required future work or unresolved residue."),
            ("Negative extraction verdict", "A failed tested route stored as reusable search-pruning knowledge."),
            ("Corpus lockfile", "A content-addressed manifest of paper ids, theorem ids, receipts, hashes, and dependency edges."),
            ("Proof-support edge", "An edge allowed to support a theorem only when its receipt and boundary are attached."),
        ],
        "construction": [
            "Collect outputs of FLCR-01 through FLCR-06 as typed graph nodes.",
            "Separate proof-support, repair, obligation, negative-result, and routing edges.",
            "Bind each edge to receipt metadata or declare it as a non-proof route.",
            "Store failed extraction routes as constraints against repeated unsupported claims.",
            "Prepare the graph for Paper 10 master-receipt composition.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "Typed causal edges can preserve claim support without collapsing obligations into proofs.", "Paper 06 ledger; obligation supplement", "Full 32-paper graph population remains later work."),
            ("normal_form_result", "The corpus can be treated as a build/provenance graph with typed dependencies.", "Internal supplement; NSIT standards", "A full lockfile must still be generated and validated."),
            ("cam_crystal_reapplication_result", "CAM queries can traverse from claim to receipts, obligations, and dependent papers.", "PAPER_REWORKS_CRYSTAL_PROJECTION.json; MannyAI routing", "A traversal is not a proof unless the edge is proof-typed."),
            ("receipt_bound_internal_result", "Negative extraction verdicts are admissible reusable evidence.", "Rule90/Lucas decomposition receipt; failed extraction records", "A later theorem may supersede a failed route only by changing the tested scope."),
            ("falsifier_or_open_obligation", "Every edge must declare whether it is proof support or workflow routing.", "Claim-lane schema; NSIT protocol", "Undeclared edges are inadmissible in formal claims."),
        ],
        "evidence": [
            "CAM 100 score: 92, system-composition closeable.",
            "NSIT matrix closes Rule90/Lucas correction core and identifies formal-methods closure for papers 00,06,10,20,30,32.",
            "Internal supplement supplies DAG, Merkle provenance, package-manager, negative-result, and triadic-keystone readings.",
        ],
        "limitations": [
            "A graph edge can route work without proving the downstream claim.",
            "The full corpus lockfile is still a build artifact to generate.",
            "Cycles in historical variants require typed reconciliation rather than deletion.",
        ],
        "companion": [
            "Paper 7 makes the papers talk to each other in a machine-readable way.",
            "A claim can point to a receipt, a repair row, an obligation, or a failed route, but those are not the same kind of edge.",
            "This is what lets obligations spring back to earlier papers without poisoning the proof graph.",
        ],
        "workbook": [
            "Draw nodes for FLCR-01 through FLCR-06.",
            "Add at least one proof edge, one repair edge, one obligation edge, and one negative-result edge.",
            "For each edge, write source, target, lane, receipt, and boundary.",
            "Run a manual query: what supports the correction residual, and what remains routed?",
        ],
    },
    {
        "id": "FLCR-08",
        "legacy": "07",
        "source": "07_Discrete_Continuous_Bridge.md",
        "title": "Discrete-Continuous Bridge Without Physical Overclaim",
        "score": "90",
        "class": "internally closed sample-preserving bridge",
        "abstract": (
            "This paper defines how finite receipt data can be presented continuously "
            "without pretending that presentation is physical dynamics. The core theorem "
            "is sample preservation: every indexed discrete sample is retained by the "
            "piecewise-linear bridge. A second bridge form treats continuous input as a "
            "quantized retraction into a discrete addressable lattice. The paper closes "
            "presentation and retraction, while reserving dynamics, sampling theory, and "
            "physical calibration for later papers."
        ),
        "definitions": [
            ("Sample-preserving bridge", "A continuous presentation whose indexed knots equal the source samples exactly."),
            ("Piecewise-linear interpolant", "A path composed of linear segments agreeing at shared endpoints."),
            ("Retraction", "A map that snaps an admitted object into a discrete representative and leaves it stable under reapplication."),
            ("Quantization budget", "A future-required norm, tolerance, and error accounting for numerical or physical bridge claims."),
            ("Presentation/dynamics split", "The rule that drawn continuity is not a law of motion unless a dynamics model is attached."),
        ],
        "construction": [
            "Take a finite indexed trace of receipt values.",
            "Construct the piecewise-linear path through the indexed samples.",
            "Verify exact sample preservation at every index and agreement at shared endpoints.",
            "Define continuous-to-discrete admission as a quantize-and-slot retraction.",
            "Export error-budget requirements to later continuum and physics-facing papers.",
        ],
        "claims": [
            ("standard_theorem_citation_bound_result", "Every finite numeric trace admits a sample-preserving piecewise-linear interpolant.", "Standard interpolation theorem; Paper 07 verifier", "Interpolation alone is not physical dynamics."),
            ("receipt_bound_internal_result", "The bridge preserves all indexed samples and segment endpoints.", "discrete_continuous_bridge receipt", "Between-sample behavior remains presentation-only."),
            ("receipt_bound_internal_result", "MDHG/SpeedLight-style retraction is idempotent after discrete admission.", "SpeedLight/MDHG receipts; crystal projection data", "Only declared admission surfaces are covered."),
            ("cam_crystal_reapplication_result", "Continuous-looking projections can preserve CAM address identity when receipts remain attached.", "Crystal CAM projector supplement; MannyAI spatial receipts", "A rendered field is not a measured physical field."),
            ("falsifier_or_open_obligation", "Any claim beyond sample preservation requires error norm, sampling model, or dynamics law.", "Internal supplement; NSIT questions", "Absent those, the claim stays in presentation lane."),
        ],
        "evidence": [
            "CAM 100 score: 90, internally closed with between-sample physics remaining.",
            "Internal supplement supplies interpolation-vs-evolution, retraction, quantization, aliasing, and cache semantics.",
            "MannyAI spatial/crystal receipts strengthen deterministic projection and round-trip preservation as bounded execution evidence.",
        ],
        "limitations": [
            "A continuous curve can hide aliasing or incompatible between-sample behavior.",
            "No physical clock, force, or dynamics is inferred here.",
            "Future numerical bridges must name norms, tolerances, and stability conditions.",
        ],
        "companion": [
            "Paper 8 is careful: it lets the system draw a line through points without pretending the line is reality.",
            "The continuous picture is useful because it preserves the samples and makes the data readable.",
            "But if a later paper wants real dynamics, it has to bring an equation, a sampling model, or measurements.",
        ],
        "workbook": [
            "Pick five receipt values and plot the piecewise-linear path through them.",
            "Verify each knot equals the original indexed sample.",
            "Create two different between-sample curves with the same samples to see why dynamics is not implied.",
            "Define a quantizer and show that applying it twice leaves the admitted representative fixed.",
        ],
    },
    {
        "id": "FLCR-09",
        "legacy": "08",
        "source": "08_Lattice_Closure.md",
        "title": "Lattice Closure And Terminal Addresses",
        "score": "91",
        "class": "system-composition closeable lattice lookup",
        "abstract": (
            "This paper lifts the local carrier into a code/lattice ladder while preserving "
            "the distinction between construction, lookup, invariant, and physical-mapping "
            "claims. The operational result is that lattice-forge surfaces can provide "
            "receipt-bound lookup addresses for E8, E8-cubed, Niemeier, Leech-facing, and "
            "Gamma72-facing routes. The paper can claim no-cost lookup capability where "
            "the library and receipt exist, while reserving full invariant proofs and "
            "empirical interpretations for later papers."
        ),
        "definitions": [
            ("Lattice ladder", "A staged route through code and lattice objects such as Fano/Hamming, E8, Golay, Leech, and Gamma72-facing surfaces."),
            ("Construction claim", "A claim that a mathematical object is generated by a declared construction."),
            ("Lookup claim", "A claim that an implemented library can retrieve or address the object without recomputing the full construction."),
            ("Glue claim", "A claim about discriminant forms or coset representatives used to combine lattice components."),
            ("Terminal address", "A stable CAM/lattice reference that later papers can import with its receipt and burden boundary."),
        ],
        "construction": [
            "Route binary code surfaces into lattice-facing addresses using standard code/lattice language.",
            "Separate E8, E8-cubed, Niemeier, Leech, and Gamma72 claims by burden type.",
            "Treat identity-glue closure as one case, not as proof of every nontrivial glue coset.",
            "Attach lookup receipts where lattice_forge already provides operational access.",
            "Export terminal addresses to Papers 10, 17, 21, 29, and 40 with explicit boundaries.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "The lattice code chain 1->3->7->8->24->72 is available as a verified internal route.", "lattice_code_chain_receipt.json; lattice_codes.py", "The route does not prove every invariant of every lattice."),
            ("receipt_bound_internal_result", "E8-cubed identity glue and Leech landing are bounded receipt-backed terminal cases.", "niemeier_leech_enumeration; o7_niemeier_e8cubed_glue receipt", "Identity glue is not nontrivial glue."),
            ("standard_theorem_citation_bound_result", "Hamming, Golay, Construction A, E8, Leech, and Niemeier language supply standard external framing.", "Paper 08 supplement; standard coding/lattice theory", "Formal citations must be attached before final publication."),
            ("cam_crystal_reapplication_result", "Terminal lattice addresses can be used as instant CAM/lattice lookups by dependent papers.", "lattice forge unification supplement; crystal projector", "Lookup is capability, not full mathematical classification."),
            ("falsifier_or_open_obligation", "Expanded Leech invariants and nontrivial glue representatives remain separate obligations.", "NP-02/NP-03 routes; CAM scorecard", "A dependent paper must state which invariant it imports."),
        ],
        "evidence": [
            "CAM 100 score: 91, system-composition closeable.",
            "NSIT matrix records E8 root enumeration, lattice code chain, Niemeier/Leech enumeration, exact E8^3 glue closure, and registry population.",
            "Internal supplement supplies Construction A ladder, Fano/Hamming, Golay/Leech, glue discipline, and lookup-vs-construction guard.",
        ],
        "limitations": [
            "No-cost lookup is a real library capability but not a proof of every associated invariant.",
            "Rootful E8-cubed and rootless Leech structures must not be conflated.",
            "Physical mappings require later calibrated data.",
        ],
        "companion": [
            "Paper 9 is where the system gets a lattice address book.",
            "The crucial distinction is simple: being able to look up or address Leech-related structure is already useful, but it is not the same as proving every Leech invariant inside this paper.",
            "That boundary is what lets later papers use the library honestly and aggressively.",
        ],
        "workbook": [
            "Build a table with rows: construction, lookup, invariant, physical mapping.",
            "Place E8 root enumeration, E8^3 glue, Leech lookup, and Gamma72 route into the right rows.",
            "For each terminal address, write the receipt or mark the missing requirement.",
            "Create a CAM query template for importing a lattice address into a later paper.",
        ],
    },
    {
        "id": "FLCR-10",
        "legacy": "09",
        "source": "09_Hamiltonian_Window_Emergence.md",
        "title": "Temporal Windows And Hamiltonian Readouts",
        "score": "84",
        "class": "bounded/system-closeable temporal window",
        "abstract": (
            "This paper turns the first nine FLCR objects into ordered windowed state. A "
            "Hamiltonian window is a contiguous sliding read over provenance-bearing "
            "centers; each emitted composite center preserves source indices, source "
            "centers, forward receipt, and backward receipt. The finite theorem is exact: "
            "a width w window over n centers emits n-w+1 composites. Kappa and McKay "
            "threshold language are ledgered as bounded readouts, while unbounded parity "
            "or physical time claims remain explicitly deferred."
        ),
        "definitions": [
            ("Hamiltonian window", "A contiguous width-w read over an ordered sequence of carried centers."),
            ("Composite center", "The emitted center produced from a window together with source provenance."),
            ("Forward receipt", "The source centers in source order."),
            ("Backward receipt", "The same source centers in reverse order, used as an audit inverse."),
            ("Kappa ledger scalar", "A monotone event-accounting scalar used before any physical energy calibration."),
            ("Threshold band", "A bounded event interval reserved for McKay-style candidate witnesses."),
        ],
        "construction": [
            "Order the carried centers from FLCR-01 through FLCR-09.",
            "For each width w, enumerate start indices 0 through n-w.",
            "Emit one composite center per start and attach source indices, forward receipt, and backward receipt.",
            "Verify that reversing the backward receipt recovers the forward source order.",
            "Separate ordinary scalar-window admissibility from McKay threshold promotion.",
        ],
        "claims": [
            ("receipt_bound_internal_result", "A width w Hamiltonian window over n centers emits exactly n-w+1 composites.", "09_Hamiltonian_Window_Emergence_VIRTUOUS.md; Paper 09 verifier", "Finite ordered sequences only."),
            ("receipt_bound_internal_result", "Forward and backward receipts preserve source provenance.", "Hamiltonian window receipts; virtuous rework", "Audit reversibility is not physical time reversal."),
            ("normal_form_result", "Sliding-window and time-series language provide the clean algorithmic normal form.", "Internal supplement; Paper 09 virtuous body", "No dynamics law is imported by the phrase time series."),
            ("cam_crystal_reapplication_result", "Window objects can become first-class CAM query objects with source indices attached.", "Kimi window lattice; CAM crystal routes", "A window object is admissible only if provenance survives."),
            ("falsifier_or_open_obligation", "Unbounded McKay/O2-prime correction collapse remains later-stage.", "CAM score 84; NP-01; Papers 18 and 29", "Bounded threshold candidates cannot be silently promoted to unbounded theorem."),
        ],
        "evidence": [
            "CAM 100 score: 84, bounded/system-closeable.",
            "Virtuous Paper 09 rework records finite Hamiltonian-window emergence, scalar sweep, kappa descent, and bounded McKay threshold stack.",
            "Internal supplement supplies sliding-window algorithms, provenance-preserving transforms, Lyapunov-style scalar, and audit-inverse language.",
        ],
        "limitations": [
            "Backward receipt is an audit inverse, not physical reversibility.",
            "Kappa is a ledger scalar here, not yet a calibrated energy unit.",
            "McKay threshold exactness is bounded to declared witnesses unless a later theorem closes the unbounded route.",
        ],
        "companion": [
            "Paper 10 is the first temporal paper in the new series.",
            "It does not say time has been solved. It says ordered source centers can be read through windows, and every emitted center can prove where it came from.",
            "That provenance is what makes the next master-receipt paper possible.",
        ],
        "workbook": [
            "Take n=6 ordered centers and compute window counts for widths 3, 5, and 7 where admissible.",
            "For one window, write source indices, forward receipt, backward receipt, and composite label.",
            "Reverse the backward receipt and check it matches the forward receipt.",
            "Mark whether a claim is ordinary window admissibility, kappa ledger, threshold candidate, or unbounded obligation.",
        ],
    },
]


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def definitions(items):
    return "\n".join(f"- **{term}.** {text}" for term, text in items)


def claim_table(rows):
    lines = ["| Lane | Claim | Evidence | Boundary |", "|------|-------|----------|----------|"]
    for lane, claim, evidence, boundary in rows:
        lines.append(f"| `{lane}` | {claim} | {evidence} | {boundary} |")
    return "\n".join(lines)


def write_formal(paper):
    return f"""# {paper['id']} - {paper['title']}

**Series:** Formalizing LCR, Unifying Standard Models  
**Artifact:** formal paper source  
**Rewrite status:** first-pass publication body for FLCR papers 01-10.  
**Legacy source:** `{paper['source']}`  
**Legacy paper:** `{paper['legacy']}`  
**Current CAM score:** {paper['score']}  
**Admission reading:** {paper['class']}  
**Claim posture:** strongest local claims are stated, but every strong claim is lane-bound.

## Abstract

{paper['abstract']}

## Keywords

LCR; CQECMPLX; receipt-bound formalization; CAM; crystal memory; normal form; claim lanes.

## 1. Role In The Series

{paper['id']} belongs to the LCR-native block of the FLCR series. Its job is to
make one layer of the substrate explicit before later papers are allowed to
translate the system into standard-model-facing language. The paper is therefore
written in native LCR terms first. Any physics, materials, observer, or Standard
Model reading is either absent or marked as deferred mapping.

The legacy source remains part of the evidence record, but the FLCR paper is
not a clipped mirror. It is a normalized publication paper: definitions precede
claims, claims name evidence and boundaries, and every later import is routed
through the manifest and workbook.

## 2. Inputs And Routing

Primary source:

- `D:/Paper Reworks/{paper['source']}`

Common cross-corpus inputs:

{bullets(COMMON_INPUTS)}

Paper-local supplement:

- `D:/Paper Reworks/supplements/{paper['legacy']}_INTERNAL_REASONING_SUPPLEMENT.md`

## 3. Definitions

{definitions(paper['definitions'])}

## 4. Construction

{bullets(paper['construction'])}

## 5. Claim Ledger

{claim_table(paper['claims'])}

## 6. Evidence Readout

{bullets(paper['evidence'])}

## 7. Proof And Verification Strategy

The verification strategy is intentionally layered.

1. **Finite enumeration layer.** When the paper names a finite carrier,
   truth table, graph, state set, or window count, the verifier must enumerate
   the declared domain completely. Exhaustive coverage closes only that domain.
2. **Receipt layer.** Every admitted result must name the receipt or validator
   that produced it, or be routed as a citation-bound theorem or obligation.
3. **CAM/crystal layer.** CAM memory may reapply and combine evidence, but the
   reapplication must preserve source address, claim lane, and boundary.
4. **Deferred mapping layer.** Any physical, Standard Model, observer, or
   materials interpretation waits for the FLCR-31..40 translation block unless
   the claim is explicitly scoped as analogy.

For this paper, the proof body should be completed by importing the exact
verifier rows from the legacy source and attaching them beneath the claim ledger
without changing the lane assignments above.

## 8. Limitations And Falsifiers

{bullets(paper['limitations'])}

General falsifier rule: if a claim cannot name its lane, evidence input,
boundary, and failure condition, it is not ready for the formal body. It may
remain in the workbook as a proposed route.

## 9. Dependency Export

This paper exports three objects to later FLCR papers:

- a normalized formal claim set;
- a companion explanation preserving the strongest claim and its boundary;
- a workbook procedure that can regenerate or inspect the paper-local evidence.

Downstream papers may cite this paper only through those exported objects or
through the receipts listed in `paper.yml`.

## 10. Publication Completion Tasks

- Attach exact verifier paths and content hashes for each evidence row.
- Add BibTeX-grade citations for external standard mathematics.
- Replace any remaining prose-only route with a claim-lane row.
- Regenerate `paper.tex` and final PDF with the publication toolchain.
"""


def write_companion(paper):
    return f"""# {paper['id']} Companion - {paper['title']}

**Purpose:** explain the formal result without weakening it.

## What This Paper Does

{bullets(paper['companion'])}

## The Strongest Claim

The strongest local claim is:

> {paper['claims'][0][1]}

Its lane is `{paper['claims'][0][0]}`. That matters because the paper is
allowed to be strong only where the evidence type supports that strength.

## What This Paper Does Not Do

{bullets(paper['limitations'])}

## Why It Matters Later

This paper gives later FLCR papers a reusable object: a claim, a boundary, and
a way to check the object again. Later papers are allowed to build upward from
that object, but they are not allowed to erase the boundary just because a later
interpretation is more exciting.

## How To Read The Formal Paper

Read the definitions first, then the claim ledger. The claim ledger is the real
center of the paper. The prose explains the construction, but the ledger says
what is admitted, what evidence supports it, and where the paper must stop.
"""


def write_workbook(paper):
    return f"""# {paper['id']} Workbook - {paper['title']}

**Purpose:** hands-on bridge from formal claims to receipts, CAM/crystals,
validators, and analog/digital checks.

## Workbook Goal

Rebuild the paper-local object in a small, inspectable form and attach a receipt
row that can be consumed by later FLCR papers.

## Exercise Sequence

{bullets(paper['workbook'])}

## CAM / Crystal Query Slots

Use these slots when the CAM/crystal projector is available:

| Slot | Query |
|------|-------|
| Source | `legacy:{paper['legacy']} source:{paper['source']}` |
| Claim lane | `publication:{paper['id']} lane:*` |
| Receipts | `publication:{paper['id']} receipt:*` |
| Obligations | `publication:{paper['id']} obligation:*` |
| Downstream uses | `depends_on:{paper['id']}` |

## Receipt Row Template

```yaml
publication_id: {paper['id']}
legacy_paper: "{paper['legacy']}"
claim:
lane:
input:
operation:
output:
validator:
receipt:
boundary:
falsifier:
downstream_exports:
```

## Analog Check

Write the paper-local object on paper as a table, graph, path, or window. Then
perform the operation by hand and compare the analog result to the digital or
formal receipt. The analog check is not a separate proof; it is a human-readable
replay of the same claim lane.
"""


def write_tex(paper):
    abstract = paper["abstract"].replace("&", "\\&").replace("_", "\\_")
    primary_claim = paper["claims"][0][1].replace("&", "\\&").replace("_", "\\_")
    primary_boundary = paper["claims"][0][3].replace("&", "\\&").replace("_", "\\_")
    return f"""\\documentclass[11pt]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{longtable}}
\\usepackage{{hyperref}}
\\title{{{paper['id']}: {paper['title']}}}
\\author{{Formalizing LCR, Unifying Standard Models}}
\\date{{First-pass FLCR rewrite}}
\\begin{{document}}
\\maketitle
\\begin{{abstract}}
{abstract}
\\end{{abstract}}
\\section*{{Status}}
This TeX file is generated from the enriched Markdown source. The Markdown
file remains canonical until the final publication build pass.
\\section*{{Primary Claim}}
{primary_claim}
\\section*{{Boundary}}
{primary_boundary}
\\end{{document}}
"""


def patch_manifest(text, paper):
    text = text.replace("status: blueprint_skeleton", "status: first_pass_publication_rewrite")
    if "rewrite_pass:" not in text:
        text += (
            "\nrewrite_pass:\n"
            "  stage: FLCR_01_10_first_publication_body\n"
            f"  cam_score: {paper['score']}\n"
            f"  admission_reading: \"{paper['class']}\"\n"
            "  body_status: richer first-pass body; final citations and exact receipt hashes pending\n"
        )
    return text


def main():
    for paper in PAPERS:
        paper_dir = ROOT / paper["id"]
        paper_dir.joinpath("formal.md").write_text(write_formal(paper), encoding="utf-8", newline="\n")
        paper_dir.joinpath("companion.md").write_text(write_companion(paper), encoding="utf-8", newline="\n")
        paper_dir.joinpath("workbook.md").write_text(write_workbook(paper), encoding="utf-8", newline="\n")
        paper_dir.joinpath("paper.tex").write_text(write_tex(paper), encoding="utf-8", newline="\n")
        manifest_path = paper_dir / "paper.yml"
        manifest_path.write_text(
            patch_manifest(manifest_path.read_text(encoding="utf-8"), paper),
            encoding="utf-8",
            newline="\n",
        )
    print(f"enriched={len(PAPERS)} papers")
    print(f"root={ROOT}")


if __name__ == "__main__":
    main()
