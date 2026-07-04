# Dimensional Ribbon Role - FLCR-02

**Ribbon slot:** `02`  
**Slot family:** `residual_action`  
**Lift depth:** `0` / `base_0x`  
**Order index:** `1`  
**Ten-window anchor:** `00`

## Dimensional Role

order-1 slot-2 action: mark the correction, residue, vacancy, or mismatch surface

## State-Bound Action

mark the correction, residue, vacancy, or mismatch surface

## Proof Form Required

truth table, residual accounting, bounded-vs-unbounded split

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `None` |
| Same family, next lift | `12` |
| Previous slot in window | `01` |
| Next slot in window | `03` |
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
