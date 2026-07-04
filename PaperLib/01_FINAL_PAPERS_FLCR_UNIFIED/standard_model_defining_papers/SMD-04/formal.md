# SMD-04 - Fermion Fields, Generations, Flavor, And Mixing

**Series:** Formalizing LCR, Unifying Standard Models  
**Layer:** Standard Model defining papers  
**Artifact:** formal paper source  
**Status:** expanded defining draft with IRL source registry; final equation/citation polishing pending.  
**Claim posture:** close what standard formalism and FLCR receipts can close; route remaining physical claims to calibration or falsifier lanes.

## Abstract

This paper defines **fermion flavor sector** as an external Standard Model or standard-physics object before any LCR translation is attempted. It binds accepted formalism, IRL sources, FLCR claim lanes, and falsifier boundaries. The strongest current claim is: Flavor and generation claims must distinguish structural indexing from measured mixing angles, phases, and masses. The paper also identifies what can be treated as closed now and what remains data-bound, calibration-bound, or unresolved.

## Keywords

Standard Model definition; fermion flavor sector; FLCR; claim lane; calibration; falsifier; closure bridge.

## 1. Contribution And Scope

- Defines **fermion flavor sector** as an external target for later LCR translation.
- Imports IRL formalism by citation/source lane rather than by analogy.
- States which rows can be closed now using accepted formalism and FLCR-01..40 proof infrastructure.
- Routes unresolved or measured claims to explicit comparator, calibration, or falsifier rows.
- Routes this definition into: FLCR-31, FLCR-32, FLCR-33, FLCR-38, FLCR-40.

This paper is a definition surface. It does not replace FLCR-31..40; it gives those papers the external object they must cite before making Standard Model-facing translation claims.

## 2. IRL Source Registry

| Source | Description | Lane | URL |
|---|---|---|---|
| `IRL-PDG-2026` | Particle Data Group Review of Particle Physics 2026 | `standard_theorem_citation_bound_result` | http`local evidence artifact`|
| `IRL-PDG-2024` | Review of Particle Physics 2024/2025, Phys. Rev. D 110, 030001 | `standard_theorem_citation_bound_result` | http`local evidence artifact`|

## 3. Definitions And Notation

- **External object.** The accepted physics object as used in the Standard Model or adjacent standard formalism.
- **LCR object.** The FLCR-native object to be mapped, usually a carrier, face, residue, window, receipt, or normal-form row.
- **Closure by formalism.** A row is closed because the external definition is standard and properly cited.
- **Closure by FLCR proof.** A row is closed because FLCR-01..40 supplies a receipt, finite enumeration, normal form, or standards result.
- **Closure by calibration.** A row is closed only after a dataset, value, unit, uncertainty, and comparator pass/fail criterion are attached.
- **Open obligation.** A row that lacks required lane fields. It is a next work item, not a rhetorical weakness.

## 4. Accepted Formalism

The formalism that this paper imports is:

- Fermions are organized by chirality, gauge representation, and generation.
- Flavor and mass bases are related by unitary mixing matrices.
- Quark charged-current mixing is summarized by the CKM matrix.
- Lepton/neutrino mixing is summarized by the PMNS matrix when neutrino masses are admitted.

## 5. Formal Claims

| Claim | Lane | Statement |
|---|---|---|
| Theorem 04.1 | `standard_theorem_citation_bound_result` | Flavor and generation claims must distinguish structural indexing from measured mixing angles, phases, and masses. |
| Proposition 04.2 | `normal_form_result` | This definition can be consumed by an FLCR paper only after the external object, LCR mapping, boundary, and destination paper are named. |
| Protocol 04.3 | `falsifier_or_open_obligation` | Claims outside the closure rows remain obligations until their missing citation, receipt, normal-form, or calibration field is supplied. |

## 6. What This Paper Closes Now

These rows can be treated as closed for publication routing:

- Close generation indexing only as an indexing/representation statement.
- Close mixing formalism when a unitary matrix relation is stated and sourced.

The closure rule is conservative: a closed external definition does not automatically close a measured LCR-to-physics identity. It closes the definition target and permits later papers to ask a precise translation question.

## 7. What Remains Open Or Calibration-Bound

- Numerical CKM/PMNS agreement is open until values, uncertainties, dataset version, and comparator are attached.
- A threefold LCR structure is not automatically a physical generation structure.

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
| `FLCR-31` | Cite SMD-04, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-32` | Cite SMD-04, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-33` | Cite SMD-04, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-38` | Cite SMD-04, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |
| `FLCR-40` | Cite SMD-04, state the LCR mapping, assign a claim lane, and attach comparator/falsifier fields before promoting the claim. |

## 10. Comparator And Falsifier Template

| Field | Required value |
|---|---|
| External object | `fermion flavor sector` |
| External source | one or more rows from the IRL source registry |
| LCR object | named FLCR carrier/face/residue/window/receipt/normal form |
| Claim lane | one of the FLCR claim lanes |
| Closure route | citation, receipt, normal form, CAM/crystal reapplication, calibration, or obligation |
| Falsifier | missing source, failed comparator, incompatible mapping, or out-of-scope physical claim |

## 11. Conclusion

SMD-04 makes **fermion flavor sector** usable by the FLCR suite without blurring definition, analogy, proof, and calibration. It closes the rows that standard formalism or FLCR receipts can actually close, and it names the rows that still require data.
