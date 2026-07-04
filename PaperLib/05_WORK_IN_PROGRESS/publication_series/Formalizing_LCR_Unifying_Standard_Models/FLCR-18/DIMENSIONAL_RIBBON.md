# Dimensional Ribbon Role - FLCR-18

**Ribbon slot:** `18`  
**Slot family:** `terminal_action`  
**Lift depth:** `1` / `first_lift_1x`  
**Order index:** `2`  
**Ten-window anchor:** `10`

## Dimensional Role

order-2 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface

## State-Bound Action

land in a lattice, exceptional, game, or runtime terminal surface

## Proof Form Required

terminal lookup, construction/invariant split, addressability proof

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `08` |
| Same family, next lift | `28` |
| Previous slot in window | `17` |
| Next slot in window | `19` |
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
