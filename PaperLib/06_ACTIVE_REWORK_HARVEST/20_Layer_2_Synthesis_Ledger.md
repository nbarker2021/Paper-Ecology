# Paper 20 — Layer-2 Synthesis Ledger

**Status.** IPMC for the suite-level aggregation discipline: seed ledger verification, 24 registered terminal forms, reachability status preservation, transport obligations with open lifts, and contributions-registry validation. ECO for source-paper re-proving, unknown reachability closure, and open transport lift resolution.

---

## Abstract

Paper 20 defines the Layer-2 synthesis ledger: the suite-level accounting surface that aggregates solved, open, failed, forbidden, and transported rows without changing their source-paper status. The closed result is ledger behavior. The seed ledger verifies, the rank-24 terminal registry contains twenty-four forms, reachability distinguishes `yes_with_template_glue`, `no`, and `unknown`, the transport-obligation verifier returns `pass_with_open_lifts`, and the contributions registry admits rows only through a named validator.

The paper does not re-prove any source-paper claim. Aggregation is accounting, not automatic closure.

**Keywords:** synthesis ledger, aggregation, reachability, transport obligation, contributions registry, terminal forms.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 20.1 | The seeded morphism ledger verifies its internal invariants. | [D] | `layer2_synthesis_ledger_receipt.json`: 8/8 |
| 20.2 | The ledger contains a populated object/edge/terminal summary with twenty-four registered terminal forms. | [D] | Same receipt |
| 20.3 | Ledger reachability preserves status distinctions: `yes_with_template_glue`, `no`, and `unknown`. | [D] | Same receipt |
| 20.4 | The transport layer contains four rows, two demonstrated and two open lifts, with verdict `pass_with_open_lifts`. | [D] | Same receipt |
| 20.5 | The contributions registry accepts a durable row only after a named validator accepts it, and records rejected proposals. | [D] | Same receipt |
| 20.6 | The solution ledger is monotone cumulative, zero-drift, with no violations. | [D] | `solution_ledger_affirmed_receipt.json`: 5/5 |
| 20.7 | Source-paper claims are not re-proved by aggregation. | [X] | Explicit scope boundary |
| 20.8 | Unknown reachability rows remain obligations. | [X] | Explicit scope boundary |
| 20.9 | Forbidden rows remain recorded obstructions. | [X] | Explicit scope boundary |
| 20.10 | Open transport lifts remain open until their source verifiers close them. | [X] | Explicit scope boundary |

---

## 2. Definitions

**Ledger row.** A typed record carrying a source, target, status, classification, witness, and proof boundary.

**Synthesis ledger.** The suite-level collection of ledger rows.

**Transported row.** Useful but not closed; it carries its open boundary with the row.

**Forbidden row.** A retained obstruction, not discarded data.

**Unknown row.** An obligation to seed, refute, or prove a path.

---

## 3. Theorems and Proofs

### Theorem 20.1 — Seed Ledger Verification

The seeded morphism ledger verifies its internal invariants.

**Proof.** The verifier builds a fresh seed ledger and runs `Ledger.verify()`. The result is `status=pass`. The ledger summary contains populated object, vector, edge, terminal, discriminant, and obstruction tables with 61 objects, 12,578 exact vectors, 52 gram forms, 66 morphisms, 33 involutions, 4 convolutions, 66 admissibility edges, 24 terminal 24D forms, 29 glue requirements, 4 residue entries, and 970 root adjacency entries. ∎

### Theorem 20.2 — Terminal Form Count

The ledger contains twenty-four registered terminal forms.

**Proof.** The ledger summary reports `terminal_24d_forms = 24`. These correspond to the 23 rootful Niemeier lattices plus the 1 rootless Leech lattice, matching the Niemeier classification. ∎

### Theorem 20.3 — Reachability Status Preservation

Ledger reachability preserves three distinct status categories: `yes_with_template_glue`, `no`, and `unknown`.

**Proof.** The verifier checks three reachability cases:

1. `A1 → Niemeier:A1^24`: Returns `yes_with_template_glue` with a legal edge, glue templates, and discriminant profile.
2. `G2 → Niemeier:Leech`: Returns `no` with obstruction `"direct rootful terminal path into rootless Leech not seeded; requires quotient/lift/code route"`.
3. Unseeded source → `Niemeier:E8^3`: Returns `unknown` with note `"no seeded admissibility path found"`.

These are different ledger states and are not collapsed into one verdict. ∎

### Theorem 20.4 — Transport Obligations

The transport layer contains four rows, two demonstrated and two open lifts, with verdict `pass_with_open_lifts`.

**Proof.** The transport verifier reports four rows:

| ID | Classification | Status |
|----|---------------|--------|
| `LCR_TO_D4_AXIS_SHEET` | demonstrated | pass |
| `D4_TO_J3O_DIAGONAL_CARRIER` | demonstrated | pass |
| `J3O_TO_G2_F4_T5A_ROUTE` | bounded_local | pass (oracle-backed) |
| `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` | registered_landing_forms | registered_only |

The verdict is `pass_with_open_lifts`: `demonstrated_count = 2`, `open_lift_count = 2`, `all_lifts_demonstrated = false`. ∎

### Theorem 20.5 — Contributions Registry Validation

The contributions registry accepts a durable row only after a named validator accepts it, and records rejected proposals.

**Proof.** The registry probe registers a validator `classification_required`. A valid proposal with a `classification` field is accepted and can be looked up. A bare assertion without a `classification` field is rejected with rationale `"missing classification field"`. The probe records both outcomes: 1 accepted, 1 rejected. ∎

### Theorem 20.6 — Solution Ledger Affirmed

The solution ledger is monotone cumulative, zero-drift, with no violations.

**Proof.** The `verify_solution_ledger_affirmed` verifier checks: ledger audit valid, cumulative monotone non-positive, zero drift, all events recorded, and conservation no violations. All 5 checks pass. ∎

---

## 4. Verifiers and Receipts

### 4.1 Layer-2 Synthesis Ledger

`verify_layer2_synthesis_ledger.py` → `layer2_synthesis_ledger_receipt.json`

| Check | Result |
|-------|--------|
| `seed_ledger_verifies` | pass |
| `ledger_has_required_tables` | pass |
| `terminal_count_is_24` | pass |
| `reachability_yes_with_template_glue` | pass |
| `reachability_forbidden_is_no` | pass |
| `reachability_unknown_is_open` | pass |
| `transport_obligations_pass_with_open_lifts` | pass |
| `registry_accepts_only_validated_rows` | pass |

**Status:** `pass`, 8/8.

### 4.2 Solution Ledger Affirmed

`verify_solution_ledger_affirmed.py` → `solution_ledger_affirmed_receipt.json`

| Check | Result |
|-------|--------|
| `ledger_audit_valid` | pass |
| `cumulative_monotone_nonpos` | pass |
| `zero_drift` | pass |
| `all_events_recorded` | pass |
| `conservation_no_violations` | pass |

**Status:** `pass`, 5/5.

---

## 5. Hand Reconstruction

All claims can be reconstructed from the ledger definitions:

1. **20.1:** Build a ledger and run `verify()`; check that all internal invariants hold.
2. **20.2:** Count the terminal forms in the ledger summary.
3. **20.3:** Query three reachability cases and confirm the three distinct answers.
4. **20.4:** Count the transport rows and classify each by its proof boundary.
5. **20.5:** Register a validator, submit a valid proposal and an invalid proposal, confirm acceptance and rejection.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F20.1 | `Ledger.verify()` fails. | Verifier confirms `status=pass`. |
| F20.2 | `unknown` reachability is treated as solved. | The verifier returns `unknown` for unseeded sources. |
| F20.3 | A forbidden row is discarded. | Forbidden rows are retained as obstructions. |
| F20.4 | `pass_with_open_lifts` is promoted to `pass`. | The verdict explicitly preserves open lifts. |
| F20.5 | A contribution enters without validator acceptance. | The registry rejects bare assertions. |
| F20.6 | Aggregation re-proves a source-paper claim. | The ledger does not re-prove; it records status. |

---

## 7. Relation to Later Papers

- **Papers 17, 18, and 19** export verified rows and open residues. Paper 20 is the ledger that keeps those rows visible: solved where solved, open where open, forbidden where forbidden, and transported where transported.
- **Paper 21** may query the ledger for reachability and transport status, but must not promote aggregated rows beyond their source evidence.
- **Papers 22+** may attempt to close unknown reachability rows and open transport lifts, but must supply separate verifiers and receipts.

---

## 8. Open Obligations

1. **Source-paper claims are not re-proved by aggregation.** The ledger records status; it does not close claims by aggregation alone.
2. **Unknown reachability rows remain obligations.** Unseeded sources require future seeding, refutation, or proof.
3. **Forbidden rows remain recorded obstructions.** Direct paths into rootless Leech are retained as obstructions, not discarded.
4. **Open transport lifts remain open until their source verifiers close them.** The `J3O_TO_G2_F4_T5A_ROUTE` and `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` rows remain open until their source papers supply stronger theorems.

---

## 9. Bibliography

1. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and Leech lattice.
2. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. Finite group and lattice data.
3. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and Monster group.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
5. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
6. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
7. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and exceptional structures.
8. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.
10. F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977. Coding theory and self-dual codes.

---

## 10. Conclusion

Paper 20 closes the suite's aggregation discipline. It makes the corpus easier to audit by refusing to let aggregation become promotion. The seed ledger verifies, the terminal registry holds 24 forms, reachability preserves status distinctions, transport obligations remain visible with open lifts, and the contributions registry enforces validation before acceptance. The remaining work is closing the source-paper claims that the ledger faithfully records — not the ledger itself.
