# SMD-10 - Electron Hole Exciton And Condensed Matter Correspondence

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** formal paper source  
**Status:** expanded defining draft with IRL source registry; final equation/citation polishing pending.  
**Claim posture:** close what standard formalism and FLCR receipts can close; route remaining physical claims to calibration or falsifier lanes.

## Abstract

This paper defines **electron-hole-exciton standard model** as an external Standard Model or standard-physics object before any LCR translation is attempted. It binds accepted formalism, IRL sources, FLCR claim lanes, and falsifier boundaries. The strongest current claim is: Electron-hole-exciton language can explain LCR vacancy/residue analogs only when material model, band structure, and parameter boundary are stated. The paper also identifies what can be treated as closed now and what remains data-bound, calibration-bound, or unresolved.

## Keywords

Standard Model definition; electron-hole-exciton standard model; FLCR; claim lane; calibration; falsifier; closure bridge.

## 1. Contribution And Scope

- Defines **electron-hole-exciton standard model** as an external target for later LCR translation.
- Imports IRL formalism by citation/source lane rather than by analogy.
- States which rows can be closed now using accepted formalism and FLCR-01..40 proof infrastructure.
- Routes unresolved or measured claims to explicit comparator, calibration, or falsifier rows.
- Routes this definition into: FLCR-34, FLCR-36, FLCR-40.

This paper is a definition surface. It does not replace FLCR-31..40; it gives those papers the external object they must cite before making Standard Model-facing translation claims.

## 2. IRL Source Registry

| Source | Description | Lane | URL |
|---|---|---|---|
| `IRL-EXCITON-SPRINGER` | Excitons reference entry, Springer Nature | `standard_theorem_citation_bound_result` | http`local evidence artifact`|
| `IRL-EXCITON-2D-REVIEW` | Excitons in two-dimensional materials, arXiv:1911.00087 | `standard_theorem_citation_bound_result` | http`local evidence artifact`|
| `IRL-NIST-CONSTANTS` | NIST Fundamental Physical Constants extensive listing | `external_calibration_result` | http`local evidence artifact`|

## 3. Definitions And Notation

- **External object.** The accepted physics object as used in the Standard Model or adjacent standard formalism.
- **LCR object.** The FLCR-native object to be mapped, usually a carrier, face, residue, window, receipt, or normal-form row.
- **Closure by formalism.** A row is closed because the external definition is standard and properly cited.
- **Closure by FLCR proof.** A row is closed because FLCR-01..40 supplies a receipt, finite enumeration, normal form, or standards result.
- **Closure by calibration.** A row is closed only after a dataset, value, unit, uncertainty, and comparator pass/fail criterion are attached.
- **Open obligation.** A row that lacks required lane fields. It is a next work item, not a rhetorical weakness.

## 4. Accepted Formalism

The formalism that this paper imports is:

- A hole is an unoccupied state in a filled band that behaves as a positive charge carrier in the effective theory.
- An exciton is an electron-hole bound state, often modeled with screened Coulomb interaction and effective masses.
- Reduced effective mass: 1/mu = 1/m_e^* + 1/m_h^*.
- Wannier-Mott/Frenkel distinctions depend on dielectric screening, effective mass, and localization scale.

## 5. Formal Claims

| Claim | Lane | Statement |
|---|---|---|
| Theorem 10.1 | `standard_theorem_citation_bound_result` | Electron-hole-exciton language can explain LCR vacancy/residue analogs only when material model, band structure, and parameter boundary are stated. |
| Proposition 10.2 | `normal_form_result` | This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named. |
| Protocol 10.3 | `falsifier_or_open_obligation` | Claims outside the closure rows remain obligations until their missing citation, receipt, normal-form, or calibration field is supplied. |

## 6. What This Paper Closes Now

These rows can be treated as closed for publication routing:

- Close the electron-hole-exciton vocabulary as a standard condensed-matter correspondence.
- Close LCR vacancy/residue analogy when it is explicitly declared as addressability/bookkeeping.

The closure rule is conservative: a closed external definition does not automatically close a measured LCR-to-physics identity. It closes the definition target and permits later papers to ask a precise translation question.

## 7. What Remains Open Or Calibration-Bound

- Material-specific exciton binding, recombination, and transport require material parameters and data.
- A hole analogy does not prove a particle-physics hole or absence ontology beyond the model.

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
| `FLCR-34` | Cite SMD-10, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-36` | Cite SMD-10, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-40` | Cite SMD-10, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |

## 10. Comparator And Falsifier Template

| Field | Required value |
|---|---|
| External object | `electron-hole-exciton standard model` |
| External source | one or more rows from the IRL source registry |
| LCR object | named FLCR carrier/face/residue/window/receipt/normal form |
| Claim lane | one of the FLCR claim lanes |
| Closure route | citation, receipt, normal form, CAM/crystal reapplication, calibration, or obligation |
| Falsifier | missing source, failed comparator, incompatible mapping, or out-of-scope physical claim |

## Online Source Addendum

The electron-hole-exciton definition surface now has online formalism and metrology anchors. These close source availability for the standard condensed-matter vocabulary and measurement lanes.

| Source | Use |
|---|---|
| `IRL-EXCITON-2D-REVIEW` | Electron-hole/exciton formalism, screening, and material-dependence. |
| `IRL-NIST-CARRIER-DYNAMICS` | Exciton/electron-hole separation, recombination, and free-carrier metrology. |
| `IRL-NIST-PV-EXCITON` | Heterojunction exciton separation into free electrons and holes. |

## 11. Conclusion

SMD-10 makes **electron-hole-exciton standard model** usable by the FLCR suite without blurring definition, analogy, proof, and calibration. It closes the rows that standard formalism or FLCR receipts can actually close, and it names the rows that still require data.

