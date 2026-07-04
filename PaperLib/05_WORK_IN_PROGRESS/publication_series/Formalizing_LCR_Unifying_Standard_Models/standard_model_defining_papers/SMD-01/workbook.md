# SMD-01 Workbook - ﻿# Standard Model Definition Contract And Evidence Boundary

## Purpose

This workbook turns `SMD-01` into a concrete Standard Model definition and comparator exercise. It is not a blank checklist. It is the place where a reviewer can take a
Standard Model-facing claim and decide exactly what closes now, what is merely
defined by external formalism, what is closed by FLCR proof, what is
calibration-bound, and what remains a falsifier/open obligation.

## Formal Paper Digest

This paper defines **definition contract** as an external Standard Model or standard-physics object before any LCR translation is attempted. It binds accepted formalism, IRL sources, FLCR claim lanes, and falsifier boundaries. The strongest current claim is: A Standard Model claim can enter the FLCR series only when its field, symmetry, equation, parameter, source, and boundary are separately named. The paper also identifies what can be treated as closed now and what remains data-bound, calibration-bound, or unresolved.

## Claim Routing Table

| Claim | Lane | Statement | Workbook action |
|---|---|---|---|
| Theorem 01.1 | `standard_theorem_citation_bound_result` | A Standard Model claim can enter the FLCR series only when its field, symmetry, equation, parameter, source, and boundary are separately named. | Attach source/receipt/comparator and mark closure state. |
| Proposition 01.2 | `normal_form_result` | This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named. | Attach source/receipt/comparator and mark closure state. |

## IRL Source Rows To Use

| Source | Description | Workbook treatment |
|---|---|---|
| `IRL-PDG-2026` | Particle Data Group Review of Particle Physics 2026 | Use as external definition or calibration source. |
| `IRL-PDG-2024` | Review of Particle Physics 2024/2025, Phys. Rev. D 110, 030001 | Use as external definition or calibration source. |
| `IRL-CODATA-2022` | NIST CODATA Recommended Values of the Fundamental Physical Constants: 2022 | Use as external definition or calibration source. |

## Closure-Now Rows

| Row | Closure statement | How to use it |
|---|---|---|
| Closure row 1 | Close definition status when the external object, source, lane, and boundary are named. | Cite in destination paper only at stated scope. |
| Closure row 2 | Close citation-bound use when PDG or another accepted reference supplies the field/parameter/definition. | Cite in destination paper only at stated scope. |
| Closure row 3 | Close internal use when FLCR-01..40 supplies the receipt or normal-form dependency. | Cite in destination paper only at stated scope. |

## Open Or Calibration-Bound Rows

| Row | Obligation | Required next evidence |
|---|---|---|
| Obligation 1 | Measured agreement remains open until a calibration row names values, units, uncertainty, and comparator. | Route to calibration, comparator, or falsifier. |
| Obligation 2 | LCR identity claims remain open if only wording similarity is supplied. | Route to calibration, comparator, or falsifier. |

## Destination FLCR Routing

| Destination | Required use |
|---|---|
| FLCR-01 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-31 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-39 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-40 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-02 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-18 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-19 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |
| FLCR-30 | Cite `SMD-01` before using this Standard Model-facing object; attach lane, comparator, and boundary. |

## Comparator Exercise

For each destination FLCR claim, fill the row below. A row is allowed to close only
at the scope supported by its evidence lane.

| Field | Required value |
|---|---|
| Claim | Copy the exact sentence from the FLCR or SMD paper. |
| External object | Name the Standard Model or standard-physics object defined by `SMD-01`. |
| External evidence | Cite one IRL source row or mark as missing. |
| FLCR object | Name the carrier, face, residue, bridge, ledger, CAM/crystal route, normal form, or receipt being mapped. |
| Lane | Choose receipt-bound, citation-bound, CAM/crystal, normal-form, calibration, synthesis dependency, or falsifier/open obligation. |
| Comparator | State what would count as match, mismatch, partial correspondence, or out-of-scope. |
| Boundary | State what the row does not prove. |
| Falsifier | State what observation, failed derivation, or missing dependency blocks promotion. |
| Closure state | closed by standard formalism / closed by FLCR proof / CAM-crystal reapplied / calibration-bound / open obligation |

## Worked Closure Pattern

```text
claim -> SMD-01 definition -> destination FLCR dependency -> lane
      -> evidence object -> boundary -> falsifier -> closure state
```

Use the pattern aggressively: the goal is not to preserve uncertainty by habit,
but to close every row whose evidence object is already present and to name the
exact missing object for every row that remains open.

## CAM/Crystal Query Patterns

```text
SMD-01 source registry
SMD-01 destination FLCR-01 FLCR-31 FLCR-39 FLCR-40 FLCR-02 FLCR-18 FLCR-19 FLCR-30
SMD-01 closure rows
SMD-01 comparator falsifier boundary
SMD-01 CAM crystal reapplication evidence
```

## Analog Review Route

Use two ledgers side by side. The left ledger names the external Standard Model
object and citation. The right ledger names the LCR/FLCR object. A string or
token connects them only when the comparator row has a lane, evidence object,
boundary, and falsifier. If the string cannot be attached, the claim is not
discarded; it becomes an open channel with a named missing object.

## Completion Criteria

- Every claim has a lane and closure state.
- Every external object has a source row.
- Every FLCR mapping names the exact destination paper.
- Every calibration-bound claim has units, dataset, uncertainty, and comparator
  requirements named.
- Every large synthesis statement names its dependencies rather than relying on
  rhetorical force.
