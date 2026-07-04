# Conversion Chain Recursive Closure Record

Date: 2026-06-30

## Chain Node

This record binds the current operator-defined conversion rule into the external-paper ingress chain. It is not a scientific source. It is a governance and reasoning source that defines how external papers, local data, MannyAI review lanes, and NIST/NSIT validators are converted into claim candidates before anything passes.

## Operator Rule

The system should not pass an external paper attachment merely because it has a plausible LCR placement or because the ingress schema validates. A pass requires iterative and recursive modeling until the local placement reaches the true closed form that fits the slot.

The recursive process must determine:

1. whether the selected publication is the best fit for the slot,
2. whether multiple external inclusions must be combined,
3. whether the slot needs a new rework,
4. whether one or more new papers are required to fill newly exposed needs,
5. whether the problem is new-paradigm territory where outside data is weaker than internal derivation,
6. whether the correct answer is to solve internally with zero outside data.

## Closure Outcomes

Each ingress record must eventually land in one of these outcomes:

| Outcome | Meaning | Promotion status |
|---|---|---|
| `best_fit_closed_form_candidate` | The paper appears to be the strongest external fit, but equation/variable extraction and local derivation still decide closure. | candidate only |
| `multi_inclusion_required` | One paper is insufficient; closure requires a bundle of papers, datasets, or standards. | bundle required |
| `slot_rework_required` | The existing FLCR placement is not the right container. The slot must be rewritten or rerouted. | no pass |
| `new_paper_required` | The review exposes a missing paper-sized derivation or bridge. | create paper |
| `internal_solve_only` | External data is not strong enough or is not the right evidence type. The claim must be solved internally. | internal derivation required |
| `reject_or_hold` | The paper is not useful enough for the slot after review. | no pass |

## Recursive Fit Model

Every attached paper should pass through this loop:

1. **Extract.** Pull the paper's actual variables, equations, datasets, methods, scope limits, and stated uncertainties.
2. **Place.** Attach those extracted objects to the proposed FLCR or Standard-extension slot.
3. **Compare.** Test whether the slot's local claim asks for exactly those objects or only resembles them.
4. **Recurse.** If mismatch remains, try adjacent slot, multi-paper bundle, or internal derivation route.
5. **Close or split.** Close only the matched subclaim. Split residues into rework, new paper, or internal-solve lanes.
6. **Validate.** Run MannyAI lane checks and NIST/NSIT validators after the reasoning step, not before it.

## Pass Rule

An ingress record may not pass as closed unless all of these are present:

1. `external_id`
2. `route`
3. `knowledge_weight`
4. `logic_bound`
5. `claim_ceiling`
6. `reasoning_note`
7. `recursive_fit_status`
8. `recursive_fit_rationale`
9. `closure_outcome`
10. `next_recursive_action`

The current 80-paper ingress is therefore valid as an intake seed, not as a closed claim set. Its next valid state is recursive fit review.

## Claim Language

Allowed before recursive closure:

- attached for review,
- plausible comparator,
- bounded support,
- topic extension,
- requires bundle,
- requires rework,
- requires new paper,
- requires internal solve.

Forbidden before recursive closure:

- closes the slot,
- proves the placement,
- confirms universality,
- establishes equivalence,
- validates the model.
