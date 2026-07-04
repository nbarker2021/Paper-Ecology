# Dimensional Ribbon Role - FLCR-20

**Ribbon slot:** `20`  
**Slot family:** `closure_lift`  
**Lift depth:** `2` / `second_lift_2x`  
**Order index:** `2`  
**Ten-window anchor:** `20`

## Dimensional Role

2x closure/lift of slots 11-19

## State-Bound Action

bind the preceding ten-slot ribbon into a replayable lift state

## Proof Form Required

aggregate receipt, replay, lockfile, and open-slot preservation

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `10` |
| Same family, next lift | `30` |
| Previous slot in window | `19` |
| Next slot in window | `21` |
| Closure/lift anchor | `20` |

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
