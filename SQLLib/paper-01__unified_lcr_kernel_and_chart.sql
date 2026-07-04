-- ============================================================
-- Paper 01 — Unified LCR Kernel And Chart
-- Domain: Foundation Math / LCR Transport
-- Cross-references: Paper 00 (grounding), Paper 03 (triality),
--                   Paper 04 (boundary repair)
-- ============================================================

-- Table: lcr_states
-- Role: The 8 binary states of the LCR finite-state machine.
--       These are the objects of the 2-category ℒ.
CREATE TABLE IF NOT EXISTS lcr_states (
    state_id        INTEGER PRIMARY KEY,   -- 0..7
    state_name      TEXT NOT NULL UNIQUE,
    l_bit           INTEGER NOT NULL CHECK (l_bit IN (0,1)),
    c_bit           INTEGER NOT NULL CHECK (c_bit IN (0,1)),
    r_bit           INTEGER NOT NULL CHECK (r_bit IN (0,1)),
    shell_grade     INTEGER NOT NULL CHECK (shell_grade IN (0,1,2,3)),
    axis_class      INTEGER,               -- D4 axis class 0..3
    sheet           INTEGER CHECK (sheet IN (0,1)),
    reversal_pair   INTEGER,               -- state_id of reversal partner
    FOREIGN KEY (reversal_pair) REFERENCES lcr_states(state_id)
);

-- Table: shell_partitions
-- Role: Shell grading 1+3+3+1 = 8, tracks which states belong to each shell
CREATE TABLE IF NOT EXISTS shell_partitions (
    partition_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    shell_grade     INTEGER NOT NULL CHECK (shell_grade IN (0,1,2,3)),
    state_id        INTEGER NOT NULL,
    partition_size  INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (state_id) REFERENCES lcr_states(state_id)
);

-- Table: lcr_transitions
-- Role: All valid transitions between LCR states (1-morphisms)
CREATE TABLE IF NOT EXISTS lcr_transitions (
    transition_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    from_state      INTEGER NOT NULL,
    to_state        INTEGER NOT NULL,
    transition_type TEXT NOT NULL CHECK (transition_type IN ('lookup','repair','fold','terminal')),
    admissible      INTEGER NOT NULL DEFAULT 1 CHECK (admissible IN (0,1)),
    FOREIGN KEY (from_state) REFERENCES lcr_states(state_id),
    FOREIGN KEY (to_state)   REFERENCES lcr_states(state_id)
);

-- Table: chart_j3o_bijection
-- Role: Verification table for chart ↔ J₃(𝕆) bijection at depth 4096
CREATE TABLE IF NOT EXISTS chart_j3o_bijection (
    entry_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    state_id        INTEGER NOT NULL,
    j3o_matrix_entry TEXT NOT NULL,
    depth_verified  INTEGER NOT NULL DEFAULT 4096,
    verification_status TEXT NOT NULL DEFAULT 'verified',
    FOREIGN KEY (state_id) REFERENCES lcr_states(state_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_lcr_shell ON lcr_states(shell_grade);
CREATE INDEX IF NOT EXISTS idx_lcr_axis  ON lcr_states(axis_class);
CREATE INDEX IF NOT EXISTS idx_trans_from ON lcr_transitions(from_state);
CREATE INDEX IF NOT EXISTS idx_trans_type ON lcr_transitions(transition_type);

-- Seed data: 8 LCR states
INSERT INTO lcr_states (state_id, state_name, l_bit, c_bit, r_bit, shell_grade, axis_class, sheet, reversal_pair) VALUES
(0, '∅ (vacuum)',     0, 0, 0, 0, 0, 0, 0),
(1, 'L',              1, 0, 0, 1, 1, 0, 2),
(2, 'C',              0, 1, 0, 1, 1, 1, 1),
(3, 'R',              0, 0, 1, 1, 2, 0, 4),
(4, 'LC',             1, 1, 0, 2, 2, 1, 3),
(5, 'LR',             1, 0, 1, 2, 3, 0, 6),
(6, 'CR',             0, 1, 1, 2, 3, 1, 5),
(7, 'LCR',            1, 1, 1, 3, 0, NULL, 7);

-- Seed data: shell partitions
INSERT INTO shell_partitions (shell_grade, state_id, partition_size) VALUES
(0, 0, 1),
(1, 1, 1), (1, 2, 1), (1, 3, 1),
(2, 4, 1), (2, 5, 1), (2, 6, 1),
(3, 7, 1);

-- Seed data: key transitions (partial — admissible operations)
INSERT INTO lcr_transitions (from_state, to_state, transition_type, admissible) VALUES
(0, 1, 'lookup', 1), (0, 2, 'lookup', 1), (0, 3, 'lookup', 1),
(1, 4, 'repair', 1), (1, 5, 'repair', 1),
(2, 4, 'repair', 1), (2, 6, 'repair', 1),
(3, 5, 'repair', 1), (3, 6, 'repair', 1),
(4, 7, 'fold',   1), (5, 7, 'fold',   1), (6, 7, 'fold',   1),
(7, 0, 'terminal', 1);
