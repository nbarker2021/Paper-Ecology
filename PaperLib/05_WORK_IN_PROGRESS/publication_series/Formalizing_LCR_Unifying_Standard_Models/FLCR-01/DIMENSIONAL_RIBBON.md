# Dimensional Ribbon Role - FLCR-01

**Ribbon slot:** `01`  
**Slot family:** `enumeration_action`  
**Lift depth:** `0` / `base_0x`  
**Order index:** `1`  
**Ten-window anchor:** `00`

## Dimensional Role

order-1 slot-1 action: select or enumerate the active center/state

## State-Bound Action

select or enumerate the active center/state

## Proof Form Required

state enumeration, identity preservation, and post-lift replay

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `None` |
| Same family, next lift | `11` |
| Previous slot in window | `00` |
| Next slot in window | `02` |
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
