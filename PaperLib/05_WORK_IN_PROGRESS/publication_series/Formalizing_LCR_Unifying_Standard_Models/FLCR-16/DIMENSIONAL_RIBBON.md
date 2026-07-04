# Dimensional Ribbon Role - FLCR-16

**Ribbon slot:** `16`  
**Slot family:** `ledger_action`  
**Lift depth:** `1` / `first_lift_1x`  
**Order index:** `2`  
**Ten-window anchor:** `10`

## Dimensional Role

order-2 slot-6 action: bind the carried state into causal edges or observer buffers

## State-Bound Action

bind the carried state into causal edges or observer buffers

## Proof Form Required

graph ledger, typed edge proof, synchronization or threshold row

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `06` |
| Same family, next lift | `26` |
| Previous slot in window | `15` |
| Next slot in window | `17` |
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
