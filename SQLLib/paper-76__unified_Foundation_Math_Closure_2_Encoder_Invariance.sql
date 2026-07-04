-- ============================================================
-- Paper 76 — Unified Foundation Math Closure 2 Encoder Invariance
-- Domain: Encoder Invariance / Open Conjecture
-- Cross-references: Paper 03 (D4 codec), Paper 94 (encoder invariance)
-- ============================================================

-- Table: encoder_invariance
-- Role: Encoder invariance conjecture: admissibility independent of encoder.
--       D4 axis/sheet codec is canonical basis.
CREATE TABLE IF NOT EXISTS encoder_invariance (
    conjecture_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    conjecture_name TEXT NOT NULL DEFAULT 'Encoder Invariance',
    statement       TEXT NOT NULL,
    status          TEXT DEFAULT 'open',
    canonical_basis TEXT DEFAULT 'D4_axis_sheet'
);

-- Table: encoder_tests
-- Role: Tests of invariance under different encoders
CREATE TABLE IF NOT EXISTS encoder_tests (
    test_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    encoder_name    TEXT NOT NULL,
    encoder_type    TEXT,
    d4_equivariant  INTEGER DEFAULT 0,
    arf_invariant   INTEGER DEFAULT 1,
    admissibility_independent INTEGER DEFAULT 0
);

-- Seed data: encoder invariance
INSERT INTO encoder_invariance (statement, status) VALUES
('The FLCR substrate is invariant under the choice of encoder', 'open');

-- Seed data: encoder tests
INSERT INTO encoder_tests (encoder_name, encoder_type, d4_equivariant, arf_invariant) VALUES
('D4_axis_sheet',  'canonical', 1, 1),
('F4_maximal',     'alternative', 1, 1),
('E8_root',        'alternative', 0, 1);
