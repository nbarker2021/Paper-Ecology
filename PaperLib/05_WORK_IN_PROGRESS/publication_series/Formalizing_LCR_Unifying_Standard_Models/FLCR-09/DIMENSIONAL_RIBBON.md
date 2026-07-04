# Dimensional Ribbon Role - FLCR-09

**Ribbon slot:** `09`  
**Slot family:** `window_action`  
**Lift depth:** `0` / `base_0x`  
**Order index:** `1`  
**Ten-window anchor:** `00`

## Dimensional Role

order-1 slot-9 action: read the ribbon through temporal, observer, meta, or synthesis windows

## State-Bound Action

read the ribbon through temporal, observer, meta, or synthesis windows

## Proof Form Required

window count, source-preserving readout, meta-ribbon proof

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `None` |
| Same family, next lift | `19` |
| Previous slot in window | `08` |
| Next slot in window | `10` |
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
