# Dimensional Ribbon Map

This map is a **publication-ordinal overlay**: it overlays the FLCR publication
series onto an 80-slot state-bound ribbon. It is useful for publication
packaging, but it is not the proof-ribbon key.

For proof-role assignment, use `ORIGINAL_80_DIMENSIONAL_RIBBON_MAP.md`, where
the original paper number is the ribbon slot.

The key rule:

```text
ones digit = slot/action family
tens digit = lift depth / ribbon cycle
slot 0 = closure/lift node
```

| Slot | FLCR | Family | Lift | Dimensional Role | Proof Form |
|---|---|---|---:|---|---|
| 00 |  | closure_lift | 0 | 0x closure/lift of slots 00--1 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 01 | FLCR-01 - Grounding Contract And Axiom Discipline | enumeration_action | 0 | order-1 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 02 | FLCR-02 - The LCR Carrier | residual_action | 0 | order-1 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 03 | FLCR-03 - Correction Surface And Residual Accounting | fold_action | 0 | order-1 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 04 | FLCR-04 - D4, J3(O), Triality, And Representation Transport | boundary_action | 0 | order-1 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 05 | FLCR-05 - Typed Boundary Repair | carrier_action | 0 | order-1 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 06 | FLCR-06 - Oloid Path Carrier And Transport Geometry | ledger_action | 0 | order-1 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 07 | FLCR-07 - Causal Links And Obligation Ledgers | bridge_action | 0 | order-1 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 08 | FLCR-08 - Discrete-Continuous Bridge Without Physical Overclaim | terminal_action | 0 | order-1 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 09 | FLCR-09 - Lattice Closure And Terminal Addresses | window_action | 0 | order-1 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 10 | FLCR-10 - Temporal Windows And Hamiltonian Readouts | closure_lift | 1 | 1x closure/lift of slots 01-09 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 11 | FLCR-11 - Master Receipt And Stack Replay | enumeration_action | 1 | order-2 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 12 | FLCR-12 - Theory Admission Gates | residual_action | 1 | order-2 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 13 | FLCR-13 - Cellular Automata Prediction Surfaces | fold_action | 1 | order-2 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 14 | FLCR-14 - Quark-Face Algebra Before Standard-Model Translation | boundary_action | 1 | order-2 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 15 | FLCR-15 - Curvature As Boundary-Repair Demand | carrier_action | 1 | order-2 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 16 | FLCR-16 - Mass Residue And Carrier Accounting | ledger_action | 1 | order-2 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 17 | FLCR-17 - Continuum Edge Residuals | bridge_action | 1 | order-2 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 18 | FLCR-18 - Exceptional Towers, VOA Routes, And Observer Face Selection | terminal_action | 1 | order-2 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 19 | FLCR-19 - Layer-2 Synthesis Ledger | window_action | 1 | order-2 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 20 | FLCR-20 - Applied Forge Reader And Descriptor Kernel | closure_lift | 2 | 2x closure/lift of slots 11-19 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 21 | FLCR-21 - Materials Candidate Generation | enumeration_action | 2 | order-3 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 22 | FLCR-22 - Protein Descriptor And Fold-Facing Kernel | residual_action | 2 | order-3 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 23 | FLCR-23 - Finite Game Lattices And Local Rule Automata | fold_action | 2 | order-3 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 24 | FLCR-24 - Energetic Traversal Maps | boundary_action | 2 | order-3 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 25 | FLCR-25 - Shear, Plasma, And Carrier Horizons | carrier_action | 2 | order-3 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 26 | FLCR-26 - Observer Delay And Shared-State Protocols | ledger_action | 2 | order-3 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 27 | FLCR-27 - Monster Ceiling And Large-Invariant Boundaries | bridge_action | 2 | order-3 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 28 | FLCR-28 - CAM, Crystal Projectors, And MannyAI Runtime | terminal_action | 2 | order-3 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 29 | FLCR-29 - Corpus Ribbon And Retrospective LCR Readout | window_action | 2 | order-3 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 30 | FLCR-30 - Supervisor Cursor And Universal Normal-Form Intake | closure_lift | 3 | 3x closure/lift of slots 21-29 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 31 | FLCR-31 - Gauge Groups Translated Into LCR | enumeration_action | 3 | order-4 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 32 | FLCR-32 - QCD And Color Transport In LCR | residual_action | 3 | order-4 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 33 | FLCR-33 - Electroweak, Higgs, And Mass Residue Translation | fold_action | 3 | order-4 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 34 | FLCR-34 - Electron-Hole-Exciton Accounting | boundary_action | 3 | order-4 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 35 | FLCR-35 - GR, Curvature, And Continuum Translation | carrier_action | 3 | order-4 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 36 | FLCR-36 - Condensed Matter, Materials, And Metamaterials | ledger_action | 3 | order-4 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 37 | FLCR-37 - Plasma, Energy, And Traversal Calibration | bridge_action | 3 | order-4 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 38 | FLCR-38 - Observer, Computation, And AI Runtime Translation | terminal_action | 3 | order-4 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 39 | FLCR-39 - Falsifiers, Comparators, And Standards Of Evidence | window_action | 3 | order-4 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 40 | FLCR-40 - Grand Unification In LCR Normal Form | closure_lift | 4 | 4x closure/lift of slots 31-39 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 41 |  | enumeration_action | 4 | order-5 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 42 |  | residual_action | 4 | order-5 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 43 |  | fold_action | 4 | order-5 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 44 |  | boundary_action | 4 | order-5 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 45 |  | carrier_action | 4 | order-5 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 46 |  | ledger_action | 4 | order-5 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 47 |  | bridge_action | 4 | order-5 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 48 |  | terminal_action | 4 | order-5 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 49 |  | window_action | 4 | order-5 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 50 |  | closure_lift | 5 | 5x closure/lift of slots 41-49 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 51 |  | enumeration_action | 5 | order-6 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 52 |  | residual_action | 5 | order-6 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 53 |  | fold_action | 5 | order-6 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 54 |  | boundary_action | 5 | order-6 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 55 |  | carrier_action | 5 | order-6 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 56 |  | ledger_action | 5 | order-6 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 57 |  | bridge_action | 5 | order-6 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 58 |  | terminal_action | 5 | order-6 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 59 |  | window_action | 5 | order-6 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 60 |  | closure_lift | 6 | 6x closure/lift of slots 51-59 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 61 |  | enumeration_action | 6 | order-7 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 62 |  | residual_action | 6 | order-7 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 63 |  | fold_action | 6 | order-7 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 64 |  | boundary_action | 6 | order-7 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 65 |  | carrier_action | 6 | order-7 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 66 |  | ledger_action | 6 | order-7 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 67 |  | bridge_action | 6 | order-7 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 68 |  | terminal_action | 6 | order-7 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 69 |  | window_action | 6 | order-7 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
| 70 |  | closure_lift | 7 | 7x closure/lift of slots 61-69 | aggregate receipt, replay, lockfile, and open-slot preservation |
| 71 |  | enumeration_action | 7 | order-8 slot-1 action: select or enumerate the active center/state | state enumeration, identity preservation, and post-lift replay |
| 72 |  | residual_action | 7 | order-8 slot-2 action: mark the correction, residue, vacancy, or mismatch surface | truth table, residual accounting, bounded-vs-unbounded split |
| 73 |  | fold_action | 7 | order-8 slot-3 action: fold the enumerated/residual state into a representation surface | coordinate atlas, folding map, face/slot transport |
| 74 |  | boundary_action | 7 | order-8 slot-4 action: turn boundary failure into typed repair or curvature demand | typed boundary row, route, falsifier, and next-state admissibility |
| 75 |  | carrier_action | 7 | order-8 slot-5 action: carry the state or residue along an admissible path | path/transducer proof, noninterference, traversal ledger |
| 76 |  | ledger_action | 7 | order-8 slot-6 action: bind the carried state into causal edges or observer buffers | graph ledger, typed edge proof, synchronization or threshold row |
| 77 |  | bridge_action | 7 | order-8 slot-7 action: project between discrete, continuous, lattice, or external forms | sample preservation, lookup bridge, calibration boundary |
| 78 |  | terminal_action | 7 | order-8 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface | terminal lookup, construction/invariant split, addressability proof |
| 79 |  | window_action | 7 | order-8 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows | window count, source-preserving readout, meta-ribbon proof |
