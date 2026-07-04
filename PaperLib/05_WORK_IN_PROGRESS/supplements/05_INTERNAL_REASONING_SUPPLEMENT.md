# Paper 05 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Scope:** firm and speculative applications supplied from existing
mathematical, computational, and scientific knowledge.

---

## Core Reading

Paper 05 is a finite-state transducer/path-carrier theorem. It proves that a
typed constraint can travel along a deterministic legal path while carrying
metadata without changing the transition law.

## Firm Applications

| Application | Why it helps Paper 05 | How to use it |
|-------------|-----------------------|---------------|
| Deterministic finite automaton / transducer | The carrier has finite state, input bits, transition function, and output dyad. | Call it a finite-state transducer where payload is side-channel metadata. |
| Monoid action over bit strings | Repeated `roll(q,b)` actions define a deterministic action of input words on carrier states. | Use induction over input words as the formal proof skeleton. |
| Noninterference property | Payload attachment does not affect `roll`; this is a standard information-flow/security property. | State payload non-interference as a theorem: metadata cannot mutate the carrier transition. |
| Runtime input validation | Invalid bits and discontinuous jumps are rejected by the recognizer. | Treat rejection tests as negative verification, not incidental tests. |
| Phase-cycle bookkeeping | `sheet mod 2`, `phase mod 4`, and parity define a finite product-state space of size 16. | Clarify the exact carrier cardinality and cycle periods. |
| Path vs straight-line transport | Curved/rolling transport can be formalized without physical geometry: it is adjacency in the transition graph. | Keep path continuity as graph continuity unless physical oloid geometry is attached. |

## Speculative Applications

| Speculative route | Potential value | Guard |
|-------------------|-----------------|-------|
| Holonomy / Wilson-loop analogy | Accumulated parity or center payload may be compared to path-dependent phase. | Do not identify with gauge holonomy without a gauge group, connection, and observable. |
| Physical oloid rolling geometry | The carrier may later map to real oloid kinematics. | Requires geometric model, units, contact constraints, and measurement. |
| Cayley-Dickson transfer pedagogy | The theta-zero and conjugation receipts offer a compelling algebraic motion story. | Keep physical QCD/gluon identity scoped until calibrated. |
| Rule 30 prediction pipeline | A legal carrier is necessary infrastructure for prediction. | It does not solve unbounded future-bit extraction by itself. |

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `05.BA.1` | Rolling carrier is a 16-state finite transducer. | Papers 06, 07, 09, 12 and NP-01. | Later papers may use it as infrastructure for causal ledgers, interpolation, or prediction attempts. | It does not prove unbounded Rule 30 extraction by itself. | Prediction theorem or bounded extraction receipt. |
| `05.BA.2` | Oloid geometry is symbolic/finite-carrier only. | Papers 14, 15, 22, 26 and NP-06. | Later papers may attach physical geometry or calibration. | The finite rolling theorem remains separate from physical measurement. | Geometry model plus measured/calibrated receipt. |
| `05.BA.3` | E6/E7/E8 lift is routed out. | Papers 08, 17, 21, 29 and NP-02. | Later lattice receipts may refine the path carrier's exceptional-lift role. | Paper 05 does not itself close the lift. | Lattice/Leech/Gamma72 receipt. |

## Concrete Upgrades For Paper 05

1. Name the rolling carrier as a deterministic finite-state transducer.
2. State payload non-interference using standard noninterference language.
3. Add the exact state-space size: `2 x 4 x 2 = 16`.
4. Define "continuous" as graph-adjacent legal transition unless a physical
   geometry model is attached.
5. Route holonomy, oloid geometry, QCD/gluon, and mass language to NP-06/NP-12
   unless their equations and data exist.

## Suggested Insert

```text
The Paper 05 carrier is a deterministic finite-state transducer with 16 states.
Each input word acts on the carrier by repeated legal `roll` transitions, and
the head/tail dyad is the output readout. A Paper 04 repair row is side-channel
metadata: the verifier's payload noninterference check proves that attaching it
does not mutate the transition function. Thus Paper 05 closes graph-continuous
finite transport, not physical oloid kinematics or unbounded Rule 30
prediction.
```
