# Dimensional Ribbon Role - FLCR-28

**Ribbon slot:** `28`  
**Slot family:** `terminal_action`  
**Lift depth:** `2` / `second_lift_2x`  
**Order index:** `3`  
**Ten-window anchor:** `20`

## Dimensional Role

order-3 slot-8 action: land in a lattice, exceptional, game, or runtime terminal surface

## State-Bound Action

land in a lattice, exceptional, game, or runtime terminal surface

## Proof Form Required

terminal lookup, construction/invariant split, addressability proof

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `18` |
| Same family, next lift | `38` |
| Previous slot in window | `27` |
| Next slot in window | `29` |
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
