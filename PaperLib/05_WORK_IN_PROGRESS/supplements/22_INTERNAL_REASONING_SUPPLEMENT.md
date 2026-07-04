# Paper 22 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Core Reading

Paper 22 is a candidate-generation and materials-ledger paper. The reasoning
surface should borrow from materials informatics, multi-objective optimization,
uncertainty, simulation validation, and lab-test protocol design.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Pareto optimization | Partner selection can be framed as multi-objective scoring with component weights. |
| Candidate vs measured material | A generated material candidate is not a measured material property. |
| Error-wall ledger | Error walls are useful design constraints that can drive seam/interlayer proposals. |
| Simulation hierarchy | DFT, FEM, MD, fabrication, and load testing are different validation tiers. |
| Uncertainty bands | Candidate estimates should eventually carry uncertainty, source, and validation tier. |
| Exciton/material bridge | TMD/interlayer/exciton ideas belong here only when material stack and band alignment are named. |

## Possible Uses

1. Add a materials validation ladder: database candidate, simulation, prototype,
   lab test, manufacturing.
2. Attach uncertainty and units to every property estimate.
3. Use error-wall rows to propose experiments, not just prose mitigations.
4. Route electron-hole-exciton material cases to NP-12 when band models exist.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `22.BA.1` | MetaForge emits material candidates. | NP-07 and lab/simulation adapters. | Later validation may promote or reject candidates. | Candidate ledger and scoring provenance remain attached. | Simulation/lab receipt. |
| `22.BA.2` | Error walls become seam obligations. | Papers 04, 14, 26. | Later seam models may become physical interface tests. | Error-wall source counts remain auditable. | Interface validation receipt. |
| `22.BA.3` | Exciton/TMD bridge is material-specific. | NP-12 and NP-06. | Later band/alignment data may bind the bridge. | Material stack and equations must be named. | Band structure or optical data receipt. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What validation tier is each materials row at? | Prevents candidate estimates from becoming measurements. |
| Which properties need units and uncertainty? | Makes materials claims scientific. |
| Which error walls map to testable seam designs? | Turns obligations into experiments. |

