# Dimensional Ribbon Role - FLCR-10

**Ribbon slot:** `10`  
**Slot family:** `closure_lift`  
**Lift depth:** `1` / `first_lift_1x`  
**Order index:** `1`  
**Ten-window anchor:** `10`

## Dimensional Role

1x closure/lift of slots 01-09

## State-Bound Action

bind the preceding ten-slot ribbon into a replayable lift state

## Proof Form Required

aggregate receipt, replay, lockfile, and open-slot preservation

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `00` |
| Same family, next lift | `20` |
| Previous slot in window | `09` |
| Next slot in window | `11` |
| Closure/lift anchor | `10` |

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
