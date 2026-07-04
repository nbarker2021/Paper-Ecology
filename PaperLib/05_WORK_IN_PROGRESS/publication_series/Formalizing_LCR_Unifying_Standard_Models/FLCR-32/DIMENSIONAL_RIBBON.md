# Dimensional Ribbon Role - FLCR-32

**Ribbon slot:** `32`  
**Slot family:** `residual_action`  
**Lift depth:** `3` / `third_lift_3x`  
**Order index:** `4`  
**Ten-window anchor:** `30`

## Dimensional Role

order-4 slot-2 action: mark the correction, residue, vacancy, or mismatch surface

## State-Bound Action

mark the correction, residue, vacancy, or mismatch surface

## Proof Form Required

truth table, residual accounting, bounded-vs-unbounded split

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `22` |
| Same family, next lift | `42` |
| Previous slot in window | `31` |
| Next slot in window | `33` |
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
