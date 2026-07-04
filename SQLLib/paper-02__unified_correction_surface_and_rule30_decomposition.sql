-- ============================================================
-- Paper 02 — Unified Correction Surface And Rule30 Decomposition
-- Domain: Cellular Automata / ANF Decomposition
-- Cross-references: Paper 00 (axioms), Paper 81-83 (Wolfram problems)
-- ============================================================

-- Table: correction_surface
-- Role: The typed correction surface with firing set and residue tracking.
--       Each entry is a (state, fires, residue_type) triple.
CREATE TABLE IF NOT EXISTS correction_surface (
    surface_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    state_tuple     TEXT NOT NULL,         -- e.g., "(0,1,0)"
    left_input      INTEGER NOT NULL CHECK (left_input IN (0,1)),
    center_input    INTEGER NOT NULL CHECK (center_input IN (0,1)),
    right_input     INTEGER NOT NULL CHECK (right_input IN (0,1)),
    fires           INTEGER NOT NULL DEFAULT 0 CHECK (fires IN (0,1)),
    residue_type    TEXT NOT NULL CHECK (residue_type IN ('none','rule90','correction','open')),
    anf_term        TEXT,                  -- Algebraic Normal Form term
    arf_value       INTEGER,               -- Arf invariant contribution
    depth_verified  INTEGER DEFAULT 4096
);

-- Table: rule30_decomposition
-- Role: Rule 30 = Rule 90 + correction, with ANF equivalence proof
CREATE TABLE IF NOT EXISTS rule30_decomposition (
    decomposition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cell_index       INTEGER NOT NULL,
    generation       INTEGER NOT NULL,
    rule90_output    INTEGER NOT NULL CHECK (rule90_output IN (0,1)),
    correction_bit   INTEGER NOT NULL CHECK (correction_bit IN (0,1)),
    rule30_output    INTEGER NOT NULL CHECK (rule30_output IN (0,1)),
    lucas_carry      INTEGER,              -- Lucas bit formula value
    extraction_method TEXT CHECK (extraction_method IN ('simulation','lucas','cold_start'))
);

-- Table: cold_start_readout
-- Role: O(log N) extraction records for any bit without simulation
CREATE TABLE IF NOT EXISTS cold_start_readout (
    readout_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    bit_position     INTEGER NOT NULL,
    initial_condition TEXT NOT NULL,
    extracted_bit    INTEGER NOT NULL CHECK (extracted_bit IN (0,1)),
    computation_steps INTEGER NOT NULL,    -- should be O(log N)
    method           TEXT NOT NULL DEFAULT 'cold_start'
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_corr_state ON correction_surface(state_tuple);
CREATE INDEX IF NOT EXISTS idx_corr_fires ON correction_surface(fires, residue_type);
CREATE INDEX IF NOT EXISTS idx_r30_cell   ON rule30_decomposition(cell_index, generation);
CREATE INDEX IF NOT EXISTS idx_r30_method ON rule30_decomposition(extraction_method);

-- Seed data: correction surface firing set {(0,1,0),(1,1,0)}
INSERT INTO correction_surface (state_tuple, left_input, center_input, right_input, fires, residue_type, anf_term, arf_value) VALUES
('(0,0,0)', 0, 0, 0, 0, 'none',       '0',       0),
('(0,0,1)', 0, 0, 1, 0, 'none',       'R',       0),
('(0,1,0)', 0, 1, 0, 1, 'correction', 'C',       1),  -- fires
('(0,1,1)', 0, 1, 1, 0, 'none',       'C+R',     0),
('(1,0,0)', 1, 0, 0, 0, 'none',       'L',       0),
('(1,0,1)', 1, 0, 1, 0, 'none',       'L+R',     0),
('(1,1,0)', 1, 1, 0, 1, 'correction', 'L+C',     1),  -- fires
('(1,1,1)', 1, 1, 1, 0, 'none',       'L+C+R',   0);
