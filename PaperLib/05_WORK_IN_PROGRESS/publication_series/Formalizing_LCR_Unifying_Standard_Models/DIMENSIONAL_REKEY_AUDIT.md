# Dimensional Re-Key Audit

The dimensional ribbon must be keyed to the **original paper number**, not to
the new FLCR ordinal.

The previous FLCR ordinal overlay is still useful as a publication-routing
view, but it is not the proof-ribbon view. In the proof-ribbon view:

- original `01` is the base slot-1 / one-dimensional action;
- original `11` is slot-1 after the `10` lift;
- original `21` is the third-order slot-1 action;
- original `31` is the next slot-1 meta/readout action;
- `02/12/22/32/42/...` are the slot-2 residual family across lifts;
- `03/13/23/33/43/...` are the slot-3 fold family across lifts;
- `10/20/30/40/...` are ten-window closure/lift nodes.

The current 40-paper FLCR series is therefore a publication arrangement over a
deeper 80-slot ribbon. Some FLCR papers combine multiple original slots, and
some Standard Model translation papers are overlays rather than primary slot
owners. The next rewrite pass should use `ORIGINAL_80_DIMENSIONAL_RIBBON_MAP`
to decide dimensional role, then use `SERIES_MAP` to decide publication
packaging.
