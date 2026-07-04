-- ============================================================
-- Paper 75 — Unified Foundation Math Closure 1 F4 Universality
-- Domain: F4 Universality / Open Conjecture
-- Cross-references: Paper 03 (magic square), Paper 92 (F4 theorem)
-- ============================================================

-- Table: f4_universality
-- Role: F4 universality conjecture: lossless F4 encoding is universal.
--       Every finite-state machine on LCR carrier encodes in F4.
CREATE TABLE IF NOT EXISTS f4_universality (
    conjecture_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    conjecture_name TEXT NOT NULL DEFAULT 'F4 Universality',
    statement       TEXT NOT NULL,
    status          TEXT DEFAULT 'open' CHECK (status IN ('open','proven','disproven')),
    tested_machines INTEGER DEFAULT 0,
    encoding_algorithm TEXT
);

-- Table: f4_encoding_tests
-- Role: Tests of F4 encoding for various machines
CREATE TABLE IF NOT EXISTS f4_encoding_tests (
    test_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_name    TEXT NOT NULL,
    machine_states  INTEGER,
    f4_encoded      INTEGER DEFAULT 0 CHECK (f4_encoded IN (0,1)),
    encoding_size   INTEGER,
    notes           TEXT
);

-- Seed data: F4 universality conjecture
INSERT INTO f4_universality (statement, status, tested_machines, encoding_algorithm) VALUES
('Every finite-state machine on the LCR carrier can be encoded in F4', 'open', 100, 'magic_square_embedding');

-- Seed data: encoding tests
INSERT INTO f4_encoding_tests (machine_name, machine_states, f4_encoded, encoding_size) VALUES
('LCR carrier', 8, 1, 24),
('Rule 30 CA',  2, 1, 52),
('D4 automaton',24, 1, 48);
