# Paper 13 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** this supplement adds reasoning and possible uses only. NSIT and
the grading tools own validity labels, promotion decisions, and scores.

---

## Core Reading

Paper 13 is an algebraic transport paper with Standard Model-facing language.
Its useful reasoning should keep three surfaces separate: finite shell-2
transport, representation-theoretic analogy, and measured particle physics.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| SU(3) representation hygiene | Internal SU(3)-like transport and measured QCD color are different burdens; the paper can use group-action language while leaving measurement to data. |
| Weyl group as permutation structure | The finite `S3` action on three idempotent faces is a clean mathematical object and should be foregrounded. |
| Trace-2 idempotents as face basis | The shell-2 triple can be explained as a basis of faces rather than as literal particles. |
| CKM as calibration matrix | CKM comparison should be treated as external numerical calibration with uncertainty, source data, and units. |
| Gauge-language guard | Words like color, charge, gluon, weak parity, and quark should be attached to either algebraic role or physical role explicitly. |
| Bounded route vs cold route | Already-enumerated exceptional routing and unconditional cold routing are different solver tasks. |
| Tool literalization | `QuarkFaceForge` can act as a structural adapter that makes the algebraic object queryable by later papers. |

## Possible Uses

1. Create a two-column vocabulary table: algebraic face term vs physical SM
   term.
2. Attach exact group-action objects to CAM so later papers can query shell-2
   faces without invoking measured physics.
3. Treat CKM calibration as a data-binding task with versioned PDG inputs.
4. Route exceptional G2/F4/T5A work into a route-condition theorem rather than
   a Standard Model claim.
5. Use the finite face triple as an internal transport primitive for Papers 14
   and 15.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `13.BA.1` | Shell-2 transport gives a three-face algebraic surface. | Papers 14, 15, 19, 27. | Later papers may use the face triple for curvature, mass residue, or observer transport. | Algebraic face transport remains distinct from measured particle identity. | Cross-paper transport receipt. |
| `13.BA.2` | CKM is a calibration/data-binding lane. | NP-06 and external-data binders. | Later data may update numerical comparisons or uncertainty. | The data source and version must remain attached. | PDG/data receipt and calibration report. |
| `13.BA.3` | G2/F4/T5A route is route-condition work. | Papers 03, 10, 17 and NP-04. | Later route conditions may strengthen exceptional transport. | Already-enumerated route evidence is not identical to unconditional cold route. | Route theorem or cold-start verifier. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| Which terms are algebraic labels and which are physical labels? | Avoids hidden Standard Model promotion. |
| What external dataset and uncertainty model should CKM binding use? | Makes calibration reproducible. |
| Which route claims are bounded/enumerated versus unconditional/cold? | Separates tool reach from theorem reach. |
| Can QuarkFaceForge be an adapter standard for later papers? | Makes the structural object reusable. |

