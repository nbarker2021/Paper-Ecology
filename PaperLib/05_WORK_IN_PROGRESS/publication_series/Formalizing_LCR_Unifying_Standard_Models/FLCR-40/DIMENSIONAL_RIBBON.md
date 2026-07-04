# Dimensional Ribbon Role - FLCR-40

**Ribbon slot:** `40`  
**Slot family:** `closure_lift`  
**Lift depth:** `4` / `fourth_lift_4x`  
**Order index:** `4`  
**Ten-window anchor:** `40`

## Dimensional Role

4x closure/lift of slots 31-39

## State-Bound Action

bind the preceding ten-slot ribbon into a replayable lift state

## Proof Form Required

aggregate receipt, replay, lockfile, and open-slot preservation

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `30` |
| Same family, next lift | `50` |
| Previous slot in window | `39` |
| Next slot in window | `41` |
| Closure/lift anchor | `40` |

## C-Form Ports

| Port | Meaning |
|---|---|
| UP | same slot digit at next lift depth |
| DOWN | same slot digit at previous lift depth |
| SIDEWAYS | neighbor slot in same ten-window |
| WRAP | slot-0 closure for this ten-window |
| FOLD | slot-3 family representation/folding route |

## Rewrite Instruction

The formal paper must prove both its topical claim and this dimensional slot
role. The workbook should show how to build or replay the state-bound ribbon
operation for this slot.
