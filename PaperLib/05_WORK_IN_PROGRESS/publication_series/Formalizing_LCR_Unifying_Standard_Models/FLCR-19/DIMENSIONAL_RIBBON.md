# Dimensional Ribbon Role - FLCR-19

**Ribbon slot:** `19`  
**Slot family:** `window_action`  
**Lift depth:** `1` / `first_lift_1x`  
**Order index:** `2`  
**Ten-window anchor:** `10`

## Dimensional Role

order-2 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows

## State-Bound Action

read the ribbon through temporal, observer, meta, or synthesis windows

## Proof Form Required

window count, source-preserving readout, meta-ribbon proof

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `09` |
| Same family, next lift | `29` |
| Previous slot in window | `18` |
| Next slot in window | `20` |
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
