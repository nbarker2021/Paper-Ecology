# Dimensional Ribbon Role - FLCR-24

**Ribbon slot:** `24`  
**Slot family:** `boundary_action`  
**Lift depth:** `2` / `second_lift_2x`  
**Order index:** `3`  
**Ten-window anchor:** `20`

## Dimensional Role

order-3 slot-4 action: turn boundary failure into typed repair or curvature demand

## State-Bound Action

turn boundary failure into typed repair or curvature demand

## Proof Form Required

typed boundary row, route, falsifier, and next-state admissibility

## Ribbon Links

| Link | Slot |
|---|---|
| Same family, previous lift | `14` |
| Same family, next lift | `34` |
| Previous slot in window | `23` |
| Next slot in window | `25` |
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
