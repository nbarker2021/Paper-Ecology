# Dimensional Ribbon Role - FLCR-26

**Ribbon slot:** `26`  
**Slot family:** `ledger_action`  
**Lift depth:** `2` / `second_lift_2x`  
**Order index:** `3`  
**Ten-window anchor:** `20`

## Dimensional Role

order-3 slot-6 action: bind the carried state into causal edges or observer buffers

## State-Bound Action

bind the carried state into causal edges or observer buffers

## Proof Form Required

graph ledger, typed edge proof, synchronization or threshold row

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `16` |
| Same family, next lift | `36` |
| Previous slot in window | `25` |
| Next slot in window | `27` |
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
