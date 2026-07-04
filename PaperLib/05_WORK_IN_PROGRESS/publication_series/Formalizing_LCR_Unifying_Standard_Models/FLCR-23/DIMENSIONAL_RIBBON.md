# Dimensional Ribbon Role - FLCR-23

**Ribbon slot:** `23`  
**Slot family:** `fold_action`  
**Lift depth:** `2` / `second_lift_2x`  
**Order index:** `3`  
**Ten-window anchor:** `20`

## Dimensional Role

order-3 slot-3 action: fold the enumerated/residual state into a representation surface

## State-Bound Action

fold the enumerated/residual state into a representation surface

## Proof Form Required

coordinate atlas, folding map, face/slot transport

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `13` |
| Same family, next lift | `33` |
| Previous slot in window | `22` |
| Next slot in window | `24` |
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
