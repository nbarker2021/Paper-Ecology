# Obligation Reasoning Audit

This file is the non-mechanical pass over the springboard lanes. It records what the obligations force us to change in the papers, not only where they route.

## Category Counts

| Category | Count |
|----------|------:|
| `external_calibration` | 24 |
| `open_next_need` | 18 |
| `claim_guard` | 9 |
| `engineering_gap` | 6 |
| `partial_closure` | 6 |
| `closed_receipt` | 4 |
| `receipt_integrity` | 4 |
| `exceptional_lift` | 3 |
| `rule30_boundary` | 3 |
| `transport_scope` | 2 |
| `engineering_evidence` | 1 |

## Rewrite Decisions

### 10.1 from Paper 10

- Category: `closed_receipt`
- Lane: `09 -> 10`
- Row: | 10.1 | Fix T10 receipt path normalization (`ROOT` should be repo root) and regenerate `t10_master_receipt.json` | **Closed / CQE-10** |
- Decision: Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims.

### 10.2 from Paper 10

- Category: `transport_scope`
- Lane: `09 -> 10`
- Row: | 10.2 | Demonstrate or scope the `J3O_TO_G2_F4_T5A_ROUTE` transport row | Later paper / CQE-13 |
- Decision: Downgrade route language to demonstrated, bounded, registered, or open according to its witness surface.

### 10.3 from Paper 10

- Category: `partial_closure`
- Lane: `09 -> 10`
- Row: | 10.3 | Demonstrate or scope the `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` transport row | Later paper / CQE-17 |
- Decision: Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- Saved evidence: GLM-F2-SP002:partially_closed

### 10.4 from Paper 10

- Category: `rule30_boundary`
- Lane: `09 -> 10`
- Row: | 10.4 | Keep cold Rule 30 Problem 3 extraction as an explicit open obligation | Ongoing guard |
- Decision: Separate enumerated/readout architecture from cold-start Rule 30 closure; never phrase cached or accumulated access as a solved cold extractor.

### 11.1 from Paper 11

- Category: `closed_receipt`
- Lane: `09 -> 10 -> 11`
- Row: | 11.1 | Fix T10 trust-anchor path normalization in `verify_theory_admission_gate.py` and regenerate receipt | **Closed / CQE-11** |
- Decision: Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims.

### 11.2 from Paper 11

- Category: `closed_receipt`
- Lane: `09 -> 10 -> 11`
- Row: | 11.2 | Classify candidates above K=9 consistently as boundary (not admitted) | **closed by Theorem 11.1 / CQE-11** |
- Decision: Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims.

### 11.3 from Paper 11

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11`
- Row: | 11.3 | Pariah / Happy-Family encoding-invariance of the boundary | CQE-29 |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 12.1 from Paper 12

- Category: `engineering_evidence`
- Lane: `09 -> 10 -> 11 -> 12`
- Row: | 12.1 | Scope or replace `verify_p3_closure.py` so it does not overclaim cold Problem 3 closure | Engineering / CQE-12 |
- Decision: Accept this as an engineering or implementation witness, not as a full mathematical closure theorem.
- Saved evidence: GLM-F4-RULE30P3:engineering

### 12.2 from Paper 12

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12`
- Row: | 12.2 | Infinite non-periodicity proof or explicit horizon status | Later formal paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 12.3 from Paper 12

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12`
- Row: | 12.3 | EntropyForge extension obligations | Product / later paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 12.4 from Paper 12

- Category: `rule30_boundary`
- Lane: `09 -> 10 -> 11 -> 12`
- Row: | 12.4 | Keep spectral layer scoped as non-cold-start predictor | Ongoing guard |
- Decision: Separate enumerated/readout architecture from cold-start Rule 30 closure; never phrase cached or accumulated access as a solved cold extractor.

### 13.1 from Paper 13

- Category: `receipt_integrity`
- Lane: `09 -> 10 -> 11 -> 12 -> 13`
- Row: | 13.1 | Exact numeric CKM calibration (`ckm_calibration_receipt.json`) | External calibration / CQE-13 |
- Decision: Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout.

### 13.2 from Paper 13

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13`
- Row: | 13.2 | Physical quark / color-charge measurement bridge | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 13.3 from Paper 13

- Category: `partial_closure`
- Lane: `09 -> 10 -> 11 -> 12 -> 13`
- Row: | 13.3 | Unconditional cold-start G2/F4/T5A route | Later formal paper |
- Decision: Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- Saved evidence: GLM-F7-SM04:partially_closed

### 14.1 from Paper 14

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14`
- Row: | 14.1 | Physical GR curvature measurement bridge | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 14.2 from Paper 14

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14`
- Row: | 14.2 | Derivation of Einstein field equations from repair-score accounting | Later physics paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 14.3 from Paper 14

- Category: `rule30_boundary`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14`
- Row: | 14.3 | Keep oloid normal form scoped as not an nth-bit extractor | Ongoing guard |
- Decision: Separate enumerated/readout architecture from cold-start Rule 30 closure; never phrase cached or accumulated access as a solved cold extractor.

### 15.1 from Paper 15

- Category: `partial_closure`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15`
- Row: | 15.1 | Physical Higgs / QFT mass calibration | External calibration |
- Decision: Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- Saved evidence: GLM-F9-SM07:partially_closed

### 15.2 from Paper 15

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15`
- Row: | 15.2 | Keep internal substrate claim separate from measured particle mass derivation | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 16.1 from Paper 16

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16`
- Row: | 16.1 | Global continuum limit | Later physics paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 16.2 from Paper 16

- Category: `partial_closure`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16`
- Row: | 16.2 | Collapse of propagating correction sum from O(N) to O(log N) (McKay-Thompson parity O2′) | Cross-cutting / CQE-17 |
- Decision: Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- Saved evidence: GLM-F6-YM-EXT02:partially_closed

### 16.3 from Paper 16

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16`
- Row: | 16.3 | Power-of-ten windows as methodology, not completed limit | Documentation cleanup |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 17.1 from Paper 17

- Category: `partial_closure`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17`
- Row: | 17.1 | Completed Leech lattice construction | Later formal paper / PFC |
- Decision: Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- Saved evidence: GLM-F8-HODGE-EXT01:partially_closed

### 17.2 from Paper 17

- Category: `exceptional_lift`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17`
- Row: | 17.2 | Weyl-extractor construction | Tooling / later paper |
- Decision: Keep exceptional-lattice and Moonshine language as a structured lift unless the specific construction, table, or identification is present.

### 17.3 from Paper 17

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17`
- Row: | 17.3 | W(E8) lookup table O1 (full materialized table) | Partially closed by Paper 08 construction; full table remains open |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 18.1 from Paper 18

- Category: `partial_closure`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18`
- Row: | 18.1 | Full Moonshine identification | Later formal paper |
- Decision: Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- Saved evidence: GLM-F10-BSD-EXT01:partially_closed

### 18.2 from Paper 18

- Category: `exceptional_lift`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18`
- Row: | 18.2 | McKay-Thompson fingerprint O2′ | Cross-cutting |
- Decision: Keep exceptional-lattice and Moonshine language as a structured lift unless the specific construction, table, or identification is present.

### 18.3 from Paper 18

- Category: `transport_scope`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18`
- Row: | 18.3 | `correction_via_voa` route completion | Later formal paper |
- Decision: Downgrade route language to demonstrated, bounded, registered, or open according to its witness surface.

### 19.1 from Paper 19

- Category: `receipt_integrity`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19`
- Row: | 19.1 | Physical observer claims (out of scope unless new receipt) | External calibration |
- Decision: Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout.

### 19.2 from Paper 19

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19`
- Row: | 19.2 | SPINOR observation model | Later formal paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 19.3 from Paper 19

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19`
- Row: | 19.3 | Open-gap observer evidence | Later formal paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 20.1 from Paper 20

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20`
- Row: | 20.1 | Preserve `unknown` reachability as open (do not promote to solved) | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 20.2 from Paper 20

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20`
- Row: | 20.2 | Preserve forbidden rows (do not discard) | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 20.3 from Paper 20

- Category: `receipt_integrity`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20`
- Row: | 20.3 | Expose aggregate ledger tooling across all 32 papers | Engineering / CQE-06 |
- Decision: Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout.

### 21.1 from Paper 21

- Category: `exceptional_lift`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21`
- Row: | 21.1 | Missing Leech import | Tooling / CQE-17 |
- Decision: Keep exceptional-lattice and Moonshine language as a structured lift unless the specific construction, table, or identification is present.

### 21.2 from Paper 21

- Category: `engineering_gap`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21`
- Row: | 21.2 | Expanded morphism witnesses | Engineering |
- Decision: Route this into tooling or adapter work before using it as a premise in the paper's theorem.

### 21.3 from Paper 21

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21`
- Row: | 21.3 | TF1 measurement | Tooling |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 21.4 from Paper 21

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21`
- Row: | 21.4 | Keep open gaps as named failure records | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 22.1 from Paper 22

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22`
- Row: | 22.1 | Finite-element validation | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 22.2 from Paper 22

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22`
- Row: | 22.2 | Fabrication and load testing | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 22.3 from Paper 22

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22`
- Row: | 22.3 | Manufacturability constraints | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 22.4 from Paper 22

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22`
- Row: | 22.4 | Relative-density and Poisson-ratio measurement | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 23.1 from Paper 23

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`
- Row: | 23.1 | PDB validation | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 23.2 from Paper 23

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`
- Row: | 23.2 | Native structure prediction | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 23.3 from Paper 23

- Category: `engineering_gap`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`
- Row: | 23.3 | Depth-only winding extraction | Tooling |
- Decision: Route this into tooling or adapter work before using it as a premise in the paper's theorem.

### 23.4 from Paper 23

- Category: `engineering_gap`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`
- Row: | 23.4 | Biological encoding parser | Engineering |
- Decision: Route this into tooling or adapter work before using it as a premise in the paper's theorem.

### 23.5 from Paper 23

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23`
- Row: | 23.5 | Fold-rate and thermodynamic validation | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 24.1 from Paper 24

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`
- Row: | 24.1 | OEIS identity | External verification |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 24.2 from Paper 24

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`
- Row: | 24.2 | N-dimensional playability | Later applied paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 24.3 from Paper 24

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`
- Row: | 24.3 | Placement-class relation to `2+6` sector split | Later formal paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 24.4 from Paper 24

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24`
- Row: | 24.4 | Combinatorial-game expert review | Peer review |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 25.1 from Paper 25

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25`
- Row: | 25.1 | Physical unit calibration (joules conversion) | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 25.2 from Paper 25

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25`
- Row: | 25.2 | Absorption measurement | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 25.3 from Paper 25

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25`
- Row: | 25.3 | Calibrated variational principle for least-action/geodesic/thermo readings | Later physics paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 25.4 from Paper 25

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25`
- Row: | 25.4 | Keep NSL unification as a calibration-level research claim | Ongoing guard |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 26.1 from Paper 26

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`
- Row: | 26.1 | Measured Z-pinch witness | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 26.2 from Paper 26

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`
- Row: | 26.2 | Controlled plasma observable connected to carrier shear bit | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 26.3 from Paper 26

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`
- Row: | 26.3 | Friction and generation mechanisms | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 26.4 from Paper 26

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`
- Row: | 26.4 | Physical collapse calibration | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 27.1 from Paper 27

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27`
- Row: | 27.1 | Keep human latency unclaimed (anneal steps ≠ response time) | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 27.2 from Paper 27

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27`
- Row: | 27.2 | Keep shared reality as agreement on `C`, not physical simultaneity | Ongoing guard |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 27.3 from Paper 27

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27`
- Row: | 27.3 | Keep consciousness / collapse interpretive | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 27.4 from Paper 27

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27`
- Row: | 27.4 | Any future temporal Z4 period claim must overcome recorded counterexamples | Empirical guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 28.1 from Paper 28

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`
- Row: | 28.1 | General N-dimensional game solver | Later applied paper |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 28.2 from Paper 28

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`
- Row: | 28.2 | Non-code-tower dimensions (dimension 5 rejected) | Out of scope / documented |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 28.3 from Paper 28

- Category: `engineering_gap`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`
- Row: | 28.3 | Real game-piece geometry per piece type | Tooling |
- Decision: Route this into tooling or adapter work before using it as a premise in the paper's theorem.

### 28.4 from Paper 28

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`
- Row: | 28.4 | Complete game theory (strategy, termination, winning, fairness) | External / later paper |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 28.5 from Paper 28

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28`
- Row: | 28.5 | OEIS identity | External verification |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 29.1 from Paper 29

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29`
- Row: | 29.1 | Physical energy-bound witness function (units bridge) | External calibration |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 29.2 from Paper 29

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29`
- Row: | 29.2 | Pariah/Happy-Family encoding-invariance of the boundary | CQE-11 / CQE-29 |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 30.1 from Paper 30

- Category: `engineering_gap`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30`
- Row: | 30.1 | Package `cqe_engine.ribbon` module in production root | Engineering |
- Decision: Route this into tooling or adapter work before using it as a premise in the paper's theorem.

### 30.2 from Paper 30

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30`
- Row: | 30.2 | Reconcile legacy '31 beads' workbook language with `00-29` + Paper 31 readout | Documentation cleanup |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.

### 30.3 from Paper 30

- Category: `receipt_integrity`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30`
- Row: | 30.3 | Keep transport ledger open lifts visible in ribbon framing | Ongoing guard |
- Decision: Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout.

### 31.1 from Paper 31

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31`
- Row: | 31.1 | Preserve Paper 31 as downstream of Paper 30 | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 31.2 from Paper 31

- Category: `closed_receipt`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31`
- Row: | 31.2 | Ensure Paper 32 preserves readout status | **closed by Theorem 32 / CQE-32** |
- Decision: Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims.

### 31.3 from Paper 31

- Category: `claim_guard`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31`
- Row: | 31.3 | Do not promote retrospective readout to an upstream premise | Ongoing guard |
- Decision: Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim.

### 32.1 from Paper 32

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`
- Row: | 32.1 | Minimality for `n ≥ 6` without independent exclusion proofs | External / later paper |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 32.2 from Paper 32

- Category: `external_calibration`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`
- Row: | 32.2 | `n=8` corridor below `46205` | External / later paper |
- Decision: Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.

### 32.3 from Paper 32

- Category: `engineering_gap`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`
- Row: | 32.3 | Product selectors must preserve proof/open/readout status | Engineering |
- Decision: Route this into tooling or adapter work before using it as a premise in the paper's theorem.

### 32.4 from Paper 32

- Category: `open_next_need`
- Lane: `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`
- Row: | 32.4 | Reconcile companion variants (`CQE-paper-32.md` vs `32-obs.md`) and `lib-forge/papers_output` copy | Documentation cleanup |
- Decision: Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
