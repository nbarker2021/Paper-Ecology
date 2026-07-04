# Dimensional Ribbon Role - FLCR-21

**Ribbon slot:** `21`  
**Slot family:** `enumeration_action`  
**Lift depth:** `2` / `second_lift_2x`  
**Order index:** `3`  
**Ten-window anchor:** `20`

## Dimensional Role

order-3 slot-1 action: select or enumerate the active center/state

## State-Bound Action

select or enumerate the active center/state

## Proof Form Required

state enumeration, identity preservation, and post-lift replay

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `11` |
| Same family, next lift | `31` |
| Previous slot in window | `20` |
| Next slot in window | `22` |
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
