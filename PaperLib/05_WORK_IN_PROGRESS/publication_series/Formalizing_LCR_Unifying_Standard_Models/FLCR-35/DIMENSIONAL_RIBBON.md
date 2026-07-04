# Dimensional Ribbon Role - FLCR-35

**Ribbon slot:** `35`  
**Slot family:** `carrier_action`  
**Lift depth:** `3` / `third_lift_3x`  
**Order index:** `4`  
**Ten-window anchor:** `30`

## Dimensional Role

order-4 slot-5 action: carry the state or residue along an admissible path

## State-Bound Action

carry the state or residue along an admissible path

## Proof Form Required

path/transducer proof, noninterference, traversal ledger

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `25` |
| Same family, next lift | `45` |
| Previous slot in window | `34` |
| Next slot in window | `36` |
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
