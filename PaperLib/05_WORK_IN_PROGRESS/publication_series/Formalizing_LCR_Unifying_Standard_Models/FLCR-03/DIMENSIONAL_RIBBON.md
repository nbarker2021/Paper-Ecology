# Dimensional Ribbon Role - FLCR-03

**Ribbon slot:** `03`  
**Slot family:** `fold_action`  
**Lift depth:** `0` / `base_0x`  
**Order index:** `1`  
**Ten-window anchor:** `00`

## Dimensional Role

order-1 slot-3 action: fold the enumerated/residual state into a representation surface

## State-Bound Action

fold the enumerated/residual state into a representation surface

## Proof Form Required

coordinate atlas, folding map, face/slot transport

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `None` |
| Same family, next lift | `13` |
| Previous slot in window | `02` |
| Next slot in window | `04` |
| Closure/lift anchor | `00` |

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
