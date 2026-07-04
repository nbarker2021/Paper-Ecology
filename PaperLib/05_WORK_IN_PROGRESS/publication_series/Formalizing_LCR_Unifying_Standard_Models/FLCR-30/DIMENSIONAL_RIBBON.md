# Dimensional Ribbon Role - FLCR-30

**Ribbon slot:** `30`  
**Slot family:** `closure_lift`  
**Lift depth:** `3` / `third_lift_3x`  
**Order index:** `3`  
**Ten-window anchor:** `30`

## Dimensional Role

3x closure/lift of slots 21-29

## State-Bound Action

bind the preceding ten-slot ribbon into a replayable lift state

## Proof Form Required

aggregate receipt, replay, lockfile, and open-slot preservation

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `20` |
| Same family, next lift | `40` |
| Previous slot in window | `29` |
| Next slot in window | `31` |
| Closure/lift anchor | `30` |

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
