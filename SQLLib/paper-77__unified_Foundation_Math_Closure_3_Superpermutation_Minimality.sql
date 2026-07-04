-- ============================================================
-- Paper 77 — Unified Foundation Math Closure 3 Superpermutation Minimality
-- Domain: Superpermutation / Open Conjecture
-- Cross-references: Paper 96 (superpermutation bounds)
-- ============================================================

-- Table: superpermutation_minimality
-- Role: Minimal length superpermutation on n symbols = Σk! (k=1..n).
--       Open for n ≥ 6.
CREATE TABLE IF NOT EXISTS superpermutation_minimality (
    n               INTEGER PRIMARY KEY,
    minimal_length  INTEGER,
    formula         TEXT NOT NULL DEFAULT 'SUM(k!, k=1..n)',
    formula_value   INTEGER,
    best_known      INTEGER,
    status          TEXT CHECK (status IN ('proven','open','conjectured'))
);

-- Seed data: superpermutation lengths
INSERT INTO superpermutation_minimality (n, minimal_length, formula_value, best_known, status) VALUES
(1, 1,     1,     1,     'proven'),
(2, 3,     3,     3,     'proven'),
(3, 9,     9,     9,     'proven'),
(4, 33,    33,    33,    'proven'),
(5, 153,   153,   153,   'proven'),
(6, 872,   873,   872,   'open'),
(7, 5906,  5913,  5906,  'open'),
(8, 46205, 46233, 46205, 'open');
