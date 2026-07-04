# Paper 26 - Z-Pinch and Shear Horizon

**Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data.

**Method:** preserve the strongest representation of each source face; when
sources disagree, keep the disagreement as a named boundary or next-need.

---

## Source Faces

| Face | Path | Words / count | Contribution |
|------|------|---------------|--------------|
| Current rework | `D:\Paper Reworks\26_Z_Pinch_and_Shear_Horizon.md` | 445 words | Existing skeleton, current status, obligations. |
| Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-26\FORMAL_PAPER.md` | 1109 words | Main theorem, proof, receipt, falsifier spine. |
| Companion variant | `CQE-paper-26.25.md` | 197 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-26.50.md` | 209 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-26.75.md` | 163 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-26_UPGRADED.md` | 1025 words | Alternate toolkit/contract/bridge phrasing. |
| Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-26` | 2 files | Executable evidence surface. |
| Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-26` | 2 files | Receipt status and check counts. |
| Saved CAM nodes | `D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json` | 1 relevant nodes | Prior crystal evidence and obligation nodes. |
| Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant rows | Closure/partial-closure status updates. |

## Virtuous Synthesis

Paper 26 states the CQECMPLX Z-pinch/shear physics map at the carrier layer.
Its closed content is the Oloid/octonion carrier algebra and a ledger
definition of pinch/shear as an analog boundary event. This is a valid internal
pinch/shear model. Magnetic confinement, friction, plasma collapse, and
energy-generation claims require an external observable bridge.

This version treats the formal paper as the proof spine, the companion variants as interface contracts, and the CAM/GLM rows as status-bearing crystal data. The paper's open obligations are not deleted; they are the next work items required before stronger claims can be promoted.

## Companion Face Digest

- **Paper 26.25 - Z-Pinch and Shear Toolkit Supplement.** This supplement shows how to reproduce Paper 26's carrier and shear receipt.
The proof is in Paper 26 and its formal verifier; the physical Z-pinch reading
is not discharged here.
- **Paper 26.50 - Z-Pinch and Shear Claim Contract.** This contract defines the minimum fields required before a Paper 26 claim can
be promoted.
- **Paper 26.75 - Z-Pinch and Shear Next-State Precondition.** This supplement defines what Paper 26 exports to later papers.
- **Paper 26 - Z-Pinch and Shear Horizon (UPGRADED: Affirmative Carrier-Level Shear Diagnostic Physics Map).** (Affirmative)

## Receipt Surface

| Receipt | Summary |
|---------|---------|
| `pinch_driven_roll_receipt.json` | status=pass; checks=7/7 |
| `zpinch_shear_horizon_receipt.json` | status=pass_with_open_obligations |

## Open Obligations as Next Needs

| ID | Current row | CAM/GLM status |
|----|-------------|----------------|
| `26.1` | \| 26.1 \| Measured Z-pinch witness \| External calibration \| | carry as next need |
| `26.2` | \| 26.2 \| Controlled plasma observable connected to carrier shear bit \| External calibration \| | carry as next need |
| `26.3` | \| 26.3 \| Friction and generation mechanisms \| External calibration \| | carry as next need |
| `26.4` | \| 26.4 \| Physical collapse calibration \| External calibration \| | carry as next need |

## Obligation Springboard Lanes

Obligations return to the earliest paper they can affect, then rework upward through each paper in the lane before the local claim is promoted.

### Local Claim Pressure

- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.

### Local Lane Table

| Obligation | Return start | Upward lane | Rework instruction |
|------------|--------------|-------------|--------------------|
| `26.1` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26.2` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26.3` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26.4` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |

## Detailed Expansion Pass

### Paper-Level Thesis

Paper 26 functions as the suite's Z-pinch/shear-horizon physical-witness bridge. Its virtuous version should therefore make three layers visible at once: the formal claim that is actually proved, the receipt or verifier evidence that lets the claim be replayed, and the explicit boundary that prevents the reader from promoting an open lift into a closed theorem.

The companion variants are used as exposition and interface contracts. They may contribute terminology, examples, and downstream preconditions, but the canonical formal paper remains the proof spine.

### Claim Status Ledger

No explicit claim/theorem lines were extracted from the formal spine. Use the abstract, proof, receipts, and obligation table to reconstruct the claim ledger before publication.

### Evidence and Receipt Detail

The receipt surface should be discussed in prose, not only listed. Passing receipts make the paper replayable; failed, partial, or missing checks become local boundaries.
- `pinch_driven_roll_receipt.json`: status=pass; checks=7/7.
- `zpinch_shear_horizon_receipt.json`: status=pass_with_open_obligations.
Verifier files are the strongest executable surface. The paper should name the verifier next to any claim it supports.
- `verify_pinch_driven_roll.py` should be mapped to the claim or obligation it checks.
- `verify_zpinch_shear_horizon.py` should be mapped to the claim or obligation it checks.

### Obligation Workups

**26.1.** | 26.1 | Measured Z-pinch witness | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `Z-pinch/shear-horizon physical-witness bridge` boundary before this obligation can strengthen the source paper.

**26.2.** | 26.2 | Controlled plasma observable connected to carrier shear bit | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `Z-pinch/shear-horizon physical-witness bridge` boundary before this obligation can strengthen the source paper.

**26.3.** | 26.3 | Friction and generation mechanisms | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `Z-pinch/shear-horizon physical-witness bridge` boundary before this obligation can strengthen the source paper.

**26.4.** | 26.4 | Physical collapse calibration | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `Z-pinch/shear-horizon physical-witness bridge` boundary before this obligation can strengthen the source paper.

### Cross-Paper Inheritance

The springboard lane means this paper cannot be revised in isolation. The upstream papers in the lane must preserve the following inherited roles before the local claim can be strengthened:

- Paper 09: finite Hamiltonian-window substrate and receipt-preserving temporal readout.
- Paper 10: master receipt, replay boundary, and open-lift visibility layer.
- Paper 11: theory-admission gate and boundary classifier.
- Paper 12: cellular-automaton prediction surface and Rule 30 scope boundary.
- Paper 13: Standard-Model quark-face transport and calibration boundary.
- Paper 14: GR boundary-repair curvature map and physical-curvature guard.
- Paper 15: QFT/Higgs mass-residue carrier and measured-mass calibration guard.
- Paper 16: continuum-edge residual layer and finite-window-to-limit boundary.
- Paper 17: E6/E8 correction tower and exceptional-lattice lift surface.
- Paper 18: VOA/Moonshine representation route and identification guard.
- Paper 19: observer face-selection and physical-observer boundary.
- Paper 20: layer-2 synthesis ledger and reachability status surface.
- Paper 21: MorphForge/PolyForge/MorphoniX engineering bridge.
- Paper 22: MetaForge applied-materials calibration bridge.
- Paper 23: FoldForge protein-folding calibration bridge.
- Paper 24: KnightForge combinatorial-game surface.
- Paper 25: energetic traversal and unit-calibration bridge.
- Paper 26: Z-pinch/shear-horizon physical-witness bridge.

### Publication-Grade Rewrite Targets

For the next manual/editorial pass, expand the paper body around these targets:

1. Put the strongest closed theorem in the opening synthesis, then immediately state the largest thing it does not prove.
2. Move every calibration, physical-identification, and external-validation claim into a guarded paragraph with its required witness named.
3. Place verifier and receipt names beside the exact claims they support.
4. Preserve open lifts as first-class obligations rather than treating them as editorial TODOs.


## Canonical Formal Spine

## Abstract

Paper 26 states the CQECMPLX Z-pinch/shear physics map at the carrier layer.
Its closed content is the Oloid/octonion carrier algebra and a ledger
definition of pinch/shear as an analog boundary event. This is a valid internal
pinch/shear model. Magnetic confinement, friction, plasma collapse, and
energy-generation claims require an external observable bridge.

The formal receipt verifies that the integer Oloid carrier has period-4 rolling
closure, that the octonion carrier realizes the same period through
`e4^2 = -1` and `e4^4 = 1`, and that a fixed-generator comparison on a Rule 30
center-column tape exposes a reproducible shear analog. The pinch analog is
defined as ledger reclassification toward bounded residue or open lift. Any
plasma interpretation remains an explicitly named obligation.

## Closed Evidence

The receipt is generated by
`production/formal-papers/CQE-paper-26/verify_zpinch_shear_horizon.py`.
It imports the live package modules `oloid_rolling`, `oloid_octonionic`,
`rule30_nth_bit`, and `transport_obligations`.

The receipt status is `pass_with_open_obligations`. The integer rolling
verifier passes with `bit0_period_4 = true`, `bit1_period_4 = true`, invariant
sheet and phase fractions equal to `1.0` at `K = 6`, and a `K = 8` landing
table of `256` entries. The octonion verifier passes with
`e4_squared_is_minus_one = true`, `e4_fourth_is_one = true`, and
`non_associative_imaginary_units = true`.

The worked probe reads the first sixteen Rule 30 center-column bits:
`1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1`. The integer landing is `(0,0,1)` with
head-tail dyad `(0,1)`. The fixed-generator octonion comparison produces
seventeen trace rows including the initial state and reports eight nonzero
shear rows. The orient-information probe over all 256 eight-bit sequences has
`trivial_baseline_rate = 0.5`, so the carrier-level shear signal is closed as
an internal diagnostic and awaits external mapping before it is treated as a
measured plasma observable.

## Definitions

An Oloid carrier state is `(sheet, phase, parity)`. `sheet` is the visible
contact sheet, `phase` is the quarter-rotation phase modulo four, and `parity`
is the cumulative input-bit parity.

An octonion carrier state carries an actual octonion. A bit-0 quarter step is
right multiplication by `e4`; a bit-1 quarter step is right multiplication by
`e5`. The identity `e4^2 = -1` is the gauge inversion and `e4^4 = 1` is the
period-4 return.

The shear analog is the XOR divergence between two fixed-generator carrier
orient bits on the same tape. It is the internal shear observable of this
paper. A plasma observable requires a domain measurement map.

The pinch analog is a ledger reclassification. A demonstrated row is not
pinched. A bounded row carries residue. A registered or open lift is held as
open until a witness is supplied.

## Claims

1. The integer Oloid carrier closes as a finite period-4 rolling algebra.

2. The octonion carrier realizes the same quarter-period structure with live
octonion multiplication.

3. The orient bit and dominant basis index give replayable path-history
residue at the carrier layer.

4. A fixed-generator comparison on the same tape gives a reproducible shear
analog.

5. A pinch in this paper is a transport-ledger reclassification and the
internal CQECMPLX pinch event.

6. Physical Z-pinch, shear-layer, friction, or generation readings are valid
exploratory targets that require external measurement rows before promotion.

## Theorem 26

Paper 26 is valid as a CQE horizon kernel when it separates the closed carrier
algebra from the external physical measurement bridge: period, octonion
grounding, carrier residue, shear analog, and pinch reclassification are
claimed; a plasma or energy mechanism requires a measured observable,
calibration row, and falsifier.

## Proof

The integer verifier establishes the finite carrier. Four bit-0 rolls return
the carrier to its initial state, and four bit-1 rolls do the same. The
complement test preserves sheet and phase while carrying parity difference.
The `K = 8` table has exactly 256 entries, so every eight-bit input has a
replayable landing.

The octonion verifier establishes the algebraic grounding. `e4 * e4` is the
negative real unit, `e4^4` is the positive real unit, and four bit-0 octonion
rolls return to the initial state. The verifier also confirms
non-associativity for imaginary units, so the carrier is not merely a scalar
phase counter.

The shear probe then uses the first sixteen Rule 30 center bits as a common
tape. One fixed carrier uses the `e4` generator and the other uses the `e5`
generator. Their orient bits diverge on eight trace rows. This proves a
replayable carrier-level shear observable inside CQECMPLX. A plasma shear
observable is the external calibration target.

Finally, the transport rows are classified as demonstrated, bounded residue,
or registered/open lift. Thus the paper closes the carrier and ledger theorem
while preserving plasma, friction, and generation readings as external
measurement obligations.

## Worked Example

For the 16-bit Rule 30 center tape, the integer carrier lands at `(0,0,1)`.
The fixed-generator comparison emits one row per state in the trace, including
the initial row. At every row, the receipt records the input bit, the `e4`
orient bit, the `e5` orient bit, their XOR shear bit, and the dominant basis
index for each carrier.

The solved result is the trace itself. Eight rows have nonzero shear divergence.
That is enough to use the carrier as a diagnostic pinch/shear map. Calling it a
measured physical Z-pinch requires a controlled observable tied to the same
rows.

## Open Obligations

A measured Z-pinch witness is open. A controlled plasma observable must be
connected to the carrier shear bit before the internal pinch map becomes an
external plasma claim.

Friction and generation mechanisms remain external-measurement targets. Carrier
residue is closed as algebraic path history; mechanical energy output requires
its own witness.

Pinch as measured physical collapse requires calibration. In this paper, pinch
means reclassification toward residue or open lift, and that internal pinch
meaning is closed.

A bounded-external measurement row is required before the horizon reading can
leave candidate status.

## Tie to the Monster Ceiling (Paper 29)

The z-pinch/shear collapse boundary is the carrier-level face of the same
supercriticality limit that Paper 29 reads arithmetically. In Paper 29 the
ceiling is the top of the Monster prime tower: `196883 = 47 x 59 x 71`, the
product of the three largest supersingular primes, above which no prime divides
`|M|`. Here the same "nothing exceeds this" limit appears as the shear front
where the carrier pinches — the divergence boundary of two fixed-generator
carriers on a common tape. The two papers describe one supercriticality
ceiling from two sides: the prime-tower top (29) and the carrier-collapse front
(26). Both close the structural claim; both name the same single bridge — the
units map to a measured physical observable.

## Suite Role

Paper 26 exports a real carrier residue test and shear diagnostic for applied
physics exploration. Later papers can use the diagnostic shape directly; they
inherit only the external measurement obligation when they claim plasma,
friction, collapse, or generation.

## Rework Integration Notes

- Keep the claim-strength tags attached to each theorem or bridge.
- Import companion variant language only when it strengthens exposition without
  promoting an open bridge.
- Treat every obligation row as a routed next-need: verifier, witness, adapter,
  calibration, documentation pass, or explicit guard.
- If a CAM/GLM row proposes `partially_closed`, update the paper body and
  obligation audit together; do not silently mark it closed.
## Upward Rework Intake

Downstream obligations now spring back through this paper. Rework this paper's definitions, receipts, guards, and claim-strength language before carrying the lane upward.

### Reasoned Claim Pressure

- Receipt-closed items may strengthen replayability and audit language, but they do not close unrelated transport, physical, or cold-start mathematical obligations.
- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.
- Engineering and adapter gaps should be promoted to work items, not used as theorem premises.
- Guard obligations must appear next to the claims they constrain, so the reader cannot miss the boundary.

### Intake Category Counts

| Category | Count |
|----------|------:|
| `external_calibration` | 6 |
| `claim_guard` | 5 |
| `open_next_need` | 5 |
| `engineering_gap` | 3 |
| `closed_receipt` | 1 |
| `receipt_integrity` | 1 |

### Routed Lanes

| Source | Obligation | Full lane | Required local action |
|--------|------------|-----------|-----------------------|
| `27` | `27.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `27` | `27.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `27` | `27.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `27` | `27.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `28` | `28.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28` | `28.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28` | `28.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `28` | `28.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `28` | `28.5` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `29` | `29.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `29` | `29.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `30` | `30.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `30` | `30.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `30` | `30.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout. |
| `31` | `31.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `31` | `31.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims. |
| `31` | `31.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `32` | `32.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32` | `32.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32` | `32.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `32` | `32.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
