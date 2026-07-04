# SMD-01 - Standard Model Definition Contract And Evidence Boundary

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** formal paper source  
**Status:** expanded defining draft with IRL source registry; final equation/citation polishing pending.  
**Claim posture:** close what standard formalism and FLCR receipts can close; route remaining physical claims to calibration or falsifier lanes.

## Abstract

This paper defines **definition contract** as an external Standard Model or standard-physics object before any LCR translation is attempted. It binds accepted formalism, IRL sources, FLCR claim lanes, and falsifier boundaries. The strongest current claim is: A Standard Model claim can enter the FLCR series only when its field, symmetry, equation, parameter, source, and boundary are separately named. The paper also identifies what can be treated as closed now and what remains data-bound, calibration-bound, or unresolved.

## Keywords

Standard Model definition; definition contract; FLCR; claim lane; calibration; falsifier; closure bridge.

## 1. Contribution And Scope

- Defines **definition contract** as an external target for later LCR translation.
- Imports IRL formalism by citation/source lane rather than by analogy.
- States which rows can be closed now using accepted formalism and FLCR-01..40 proof infrastructure.
- Routes unresolved or measured claims to explicit comparator, calibration, or falsifier rows.
- Routes this definition into: FLCR-31, FLCR-39, FLCR-40.

This paper is a definition surface. It does not replace FLCR-31..40; it gives those papers the external object they must cite before making Standard Model-facing translation claims.

## 2. IRL Source Registry

| Source | Description | Lane | URL |
|---|---|---|---|
| `IRL-PDG-2026` | Particle Data Group Review of Particle Physics 2026 | `standard_theorem_citation_bound_result` | http`local evidence artifact`|
| `IRL-PDG-2024` | Review of Particle Physics 2024/2025, Phys. Rev. D 110, 030001 | `standard_theorem_citation_bound_result` | http`local evidence artifact`|
| `IRL-CODATA-2022` | NIST CODATA Recommended Values of the Fundamental Physical Constants: 2022 | `external_calibration_result` | http`local evidence artifact`|

## 3. Definitions And Notation

- **External object.** The accepted physics object as used in the Standard Model or adjacent standard formalism.
- **LCR object.** The FLCR-native object to be mapped, usually a carrier, face, residue, window, receipt, or normal-form row.
- **Closure by formalism.** A row is closed because the external definition is standard and properly cited.
- **Closure by FLCR proof.** A row is closed because FLCR-01..40 supplies a receipt, finite enumeration, normal form, or standards result.
- **Closure by calibration.** A row is closed only after a dataset, value, unit, uncertainty, and comparator pass/fail criterion are attached.
- **Open obligation.** A row that lacks required lane fields. It is a next work item, not a rhetorical weakness.

## 4. Accepted Formalism

The formalism that this paper imports is:

- External object O_ext must be named before any LCR object O_lcr is mapped to it.
- A mapping row has the form (O_ext, equation/source, O_lcr, lane, boundary, falsifier).
- A measured row additionally requires (dataset, units, uncertainty, version, pass/fail rule).

## 5. Formal Claims

| Claim | Lane | Statement |
|---|---|---|
| Theorem 01.1 | `standard_theorem_citation_bound_result` | A Standard Model claim can enter the FLCR series only when its field, symmetry, equation, parameter, source, and boundary are separately named. |
| Proposition 01.2 | `normal_form_result` | This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named. |
| Protocol 01.3 | `falsifier_or_open_obligation` | Claims outside the closure rows remain obligations until their missing citation, receipt, normal-form, or calibration field is supplied. |

## 6. What This Paper Closes Now

These rows can be treated as closed for publication routing:

- Close definition status when the external object, source, lane, and boundary are named.
- Close citation-bound use when PDG or another accepted reference supplies the field/parameter/definition.
- Close internal use when FLCR-01..40 supplies the receipt or normal-form dependency.

The closure rule is conservative: a closed external definition does not automatically close a measured LCR-to-physics identity. It closes the definition target and permits later papers to ask a precise translation question.

## 7. What Remains Open Or Calibration-Bound

- Measured agreement remains open until a calibration row names values, units, uncertainty, and comparator.
- LCR identity claims remain open if only wording similarity is supplied.

## 8. Bridge To FLCR-01..40

The first forty FLCR papers provide the internal side of the bridge:

- FLCR-01 supplies the claim-lane and conservative-extension discipline.
- FLCR-02 through FLCR-18 supply LCR carrier, correction, atlas, repair, path, ledger, window, receipt, admission, CA, face algebra, curvature, residue, continuum, and exceptional machinery.
- FLCR-19 through FLCR-30 supply synthesis, applied forge readers, energetic/plasma/observer/game/Monster/CAM/runtime/cursor evidence.
- FLCR-31 through FLCR-40 consume this SMD definition layer for Standard Model translation and synthesis.

This paper therefore stops treating the relevant object as unsolved when one of the allowed closure paths is present:

```text
standard formalism + citation
or FLCR receipt/normal form
or CAM/crystal reapplication
or external calibration pass
```

Rows not satisfying one of those paths stay as obligations, but obligations now have named owners and lane requirements.

## 9. Crosswalk To Destination Papers

| Destination | Required use |
|---|---|
| `FLCR-31` | Cite SMD-01, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-39` | Cite SMD-01, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-40` | Cite SMD-01, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |

## 10. Comparator And Falsifier Template

| Field | Required value |
|---|---|
| External object | `definition contract` |
| External source | one or more rows from the IRL source registry |
| LCR object | named FLCR carrier/face/residue/window/receipt/normal form |
| Claim lane | one of the FLCR claim lanes |
| Closure route | citation, receipt, normal form, CAM/crystal reapplication, calibration, or obligation |
| Falsifier | missing source, failed comparator, incompatible mapping, or out-of-scope physical claim |

## Online Source Addendum

This definition contract now includes the online-source application pass. PDG supplies the current Standard Model definition surface; NIST/CODATA supplies constants and numerical calibration targets. The source rows close definition and calibration availability, not LCR physical identity.

| Source | Use |
|---|---|
| `IRL-PDG-2026` | Current Standard Model review surface. |
| `IRL-NIST-ALPHA-2022` | Fine-structure alpha inverse calibration row. |
| `IRL-CODATA-2022-WALLET` | Compact constants/units table. |

## 11. Conclusion

SMD-01 makes **definition contract** usable by the FLCR suite without blurring definition, analogy, proof, and calibration. It closes the rows that standard formalism or FLCR receipts can actually close, and it names the rows that still require data.

