# Dimensional Ribbon Role - FLCR-38

**Ribbon slot:** `38`  
**Slot family:** `terminal_action`  
**Lift depth:** `3` / `third_lift_3x`  
**Order index:** `4`  
**Ten-window anchor:** `30`

## Dimensional Role

order-4 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface

## State-Bound Action

land in a lattice, exceptional, game, or runtime terminal surface

## Proof Form Required

terminal lookup, construction/invariant split, addressability proof

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `28` |
| Same family, next lift | `48` |
| Previous slot in window | `37` |
| Next slot in window | `39` |
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
