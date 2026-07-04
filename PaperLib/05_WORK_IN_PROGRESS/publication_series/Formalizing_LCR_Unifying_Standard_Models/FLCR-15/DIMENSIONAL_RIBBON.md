# Dimensional Ribbon Role - FLCR-15

**Ribbon slot:** `15`  
**Slot family:** `carrier_action`  
**Lift depth:** `1` / `first_lift_1x`  
**Order index:** `2`  
**Ten-window anchor:** `10`

## Dimensional Role

order-2 slot-5 action: carry the state or residue along an admissible path

## State-Bound Action

carry the state or residue along an admissible path

## Proof Form Required

path/transducer proof, noninterference, traversal ledger

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `05` |
| Same family, next lift | `25` |
| Previous slot in window | `14` |
| Next slot in window | `16` |
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
