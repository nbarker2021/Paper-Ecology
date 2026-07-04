# SMD-08 - Renormalization, Effective Field Theory, And Running Parameters

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** formal paper source  
**Status:** expanded defining draft with IRL source registry; final equation/citation polishing pending.  
**Claim posture:** close what standard formalism and FLCR receipts can close; route remaining physical claims to calibration or falsifier lanes.

## Abstract

This paper defines **scale and renormalization sector** as an external Standard Model or standard-physics object before any LCR translation is attempted. It binds accepted formalism, IRL sources, FLCR claim lanes, and falsifier boundaries. The strongest current claim is: Any claim that changes by scale must carry its scale, scheme, matching rule, and allowed error or falsifier. The paper also identifies what can be treated as closed now and what remains data-bound, calibration-bound, or unresolved.

## Keywords

Standard Model definition; scale and renormalization sector; FLCR; claim lane; calibration; falsifier; closure bridge.

## 1. Contribution And Scope

- Defines **scale and renormalization sector** as an external target for later LCR translation.
- Imports IRL formalism by citation/source lane rather than by analogy.
- States which rows can be closed now using accepted formalism and FLCR-01..40 proof infrastructure.
- Routes unresolved or measured claims to explicit comparator, calibration, or falsifier rows.
- Routes this definition into: FLCR-31, FLCR-32, FLCR-33, FLCR-37, FLCR-39, FLCR-40.

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

- A running parameter depends on scale and scheme, e.g. g = g(mu).
- Effective field theories require a cutoff or matching scale and a domain of validity.
- Anomaly and consistency checks are separate closure rows from phenomenological fit.
- Units-bearing comparisons require constants, units, uncertainty, and convention fields.

## 5. Formal Claims

| Claim | Lane | Statement |
|---|---|---|
| Theorem 08.1 | `standard_theorem_citation_bound_result` | Any claim that changes by scale must carry its scale, scheme, matching rule, and allowed error or falsifier. |
| Proposition 08.2 | `normal_form_result` | This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named. |
| Protocol 08.3 | `falsifier_or_open_obligation` | Claims outside the closure rows remain obligations until their missing citation, receipt, normal-form, or calibration field is supplied. |

## 6. What This Paper Closes Now

These rows can be treated as closed for publication routing:

- Close scale-dependence as a definition when scale, scheme, and domain are stated.
- Close zero-cost lookup only as an internal retrieval claim, not as a substitute for renormalization context.

The closure rule is conservative: a closed external definition does not automatically close a measured LCR-to-physics identity. It closes the definition target and permits later papers to ask a precise translation question.

## 7. What Remains Open Or Calibration-Bound

- Running-coupling agreement remains open without scale/scheme/value/uncertainty.
- Cross-scale synthesis claims need matching rules.

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
| `FLCR-31` | Cite SMD-08, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-32` | Cite SMD-08, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-33` | Cite SMD-08, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-37` | Cite SMD-08, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-39` | Cite SMD-08, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-40` | Cite SMD-08, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |

## 10. Comparator And Falsifier Template

| Field | Required value |
|---|---|
| External object | `scale and renormalization sector` |
| External source | one or more rows from the IRL source registry |
| LCR object | named FLCR carrier/face/residue/window/receipt/normal form |
| Claim lane | one of the FLCR claim lanes |
| Closure route | citation, receipt, normal form, CAM/crystal reapplication, calibration, or obligation |
| Falsifier | missing source, failed comparator, incompatible mapping, or out-of-scope physical claim |

## Online Source Addendum

Scale and running-parameter claims now have explicit online calibration anchors. NIST/CODATA closes source availability for constants; PDG closes the evaluated-parameter review surface. Scale, scheme, and uncertainty fields are still required before any value is promoted.

| Source | Use |
|---|---|
| `IRL-PDG-2026` | Evaluated particle/parameter review target. |
| `IRL-NIST-ALPHA-2022` | Alpha inverse calibration row. |
| `IRL-CODATA-2022-WALLET` | Constants/units wallet card. |

## 11. Conclusion

SMD-08 makes **scale and renormalization sector** usable by the FLCR suite without blurring definition, analogy, proof, and calibration. It closes the rows that standard formalism or FLCR receipts can actually close, and it names the rows that still require data.

