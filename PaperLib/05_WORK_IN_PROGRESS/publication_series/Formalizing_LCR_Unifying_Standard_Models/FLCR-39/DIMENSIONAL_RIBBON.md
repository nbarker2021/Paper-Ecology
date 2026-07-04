# Dimensional Ribbon Role - FLCR-39

**Ribbon slot:** `39`  
**Slot family:** `window_action`  
**Lift depth:** `3` / `third_lift_3x`  
**Order index:** `4`  
**Ten-window anchor:** `30`

## Dimensional Role

order-4 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows

## State-Bound Action

read the ribbon through temporal, observer, meta, or synthesis windows

## Proof Form Required

window count, source-preserving readout, meta-ribbon proof

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `29` |
| Same family, next lift | `49` |
| Previous slot in window | `38` |
| Next slot in window | `40` |
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
