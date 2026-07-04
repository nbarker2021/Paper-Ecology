-- ============================================================
-- Paper 12 — Unified Ca Prediction Surface
-- Domain: CA Enumeration / Bounded Prediction
-- Cross-references: Paper 02 (Rule 30), Paper 81-83 (Wolfram problems)
-- ============================================================

-- Table: ca_prediction_surface
-- Role: The set of all CA behaviors predictable by the FLCR substrate.
--       Tracks bounded CA enumeration results.
CREATE TABLE IF NOT EXISTS ca_prediction_surface (
    surface_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_number     INTEGER NOT NULL,      -- Wolfram code
    neighborhood_size INTEGER NOT NULL DEFAULT 3,
    state_count     INTEGER NOT NULL DEFAULT 2,
    n_depth         INTEGER NOT NULL,      -- enumeration depth
    predicted_count INTEGER NOT NULL,      -- number predicted
    total_count     INTEGER NOT NULL,      -- total possible
    closure_ratio   REAL,                  -- predicted / total
    tr_cl_id        TEXT,                  -- e.g., "TR-CL-06"
    coverage_status TEXT NOT NULL CHECK (coverage_status IN ('full','partial','residue'))
);

-- Table: tr_cl_closure
-- Role: TR-CL closure achievements (e.g., 64/256 at n=3)
CREATE TABLE IF NOT EXISTS tr_cl_closure (
    closure_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    tr_cl_code      TEXT NOT NULL,
    n_value         INTEGER NOT NULL,
    achieved        INTEGER NOT NULL,
    total           INTEGER NOT NULL,
    rule_scope      TEXT                   -- which rules covered
);

-- Table: peep_coverage
-- Role: PEEP-2026-018 Rule 30 coverage records
CREATE TABLE IF NOT EXISTS peep_coverage (
    peep_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    peep_code       TEXT NOT NULL,
    rule_number     INTEGER NOT NULL,
    coverage_depth  INTEGER NOT NULL,
    coverage_type   TEXT CHECK (coverage_type IN ('bounded','unbounded','residue'))
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_ca_rule   ON ca_prediction_surface(rule_number);
CREATE INDEX IF NOT EXISTS idx_ca_depth  ON ca_prediction_surface(n_depth);
CREATE INDEX IF NOT EXISTS idx_trcl_n    ON tr_cl_closure(n_value);

-- Seed data: TR-CL-06 closure
INSERT INTO tr_cl_closure (tr_cl_code, n_value, achieved, total, rule_scope) VALUES
('TR-CL-06', 3, 64, 256, 'elementary CA (2-state, 3-neighbor)');

-- Seed data: PEEP-2026-018 coverage
INSERT INTO peep_coverage (peep_code, rule_number, coverage_depth, coverage_type) VALUES
('PEEP-2026-018', 30, 4096, 'bounded');

-- Seed data: bounded CA enumeration (elementary CA at n=3)
INSERT INTO ca_prediction_surface (rule_number, neighborhood_size, state_count, n_depth, predicted_count, total_count, closure_ratio, tr_cl_id, coverage_status) VALUES
(0,   3, 2, 3, 256, 256, 1.0,   'TR-CL-06', 'full'),
(30,  3, 2, 3, 64,  256, 0.25,  'TR-CL-06', 'partial'),
(90,  3, 2, 3, 256, 256, 1.0,   'TR-CL-06', 'full'),
(110, 3, 2, 3, 128, 256, 0.5,   'TR-CL-06', 'partial'),
(184, 3, 2, 3, 256, 256, 1.0,   'TR-CL-06', 'full');

-- === BATCH GROUP 1 CLAIMS (paper-12) ===
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (12, '12.1', 'S3 = ⟨LR, LC, CR⟩ on tile boundary transpositions', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (12, '12.2', '7 non-identity S3 sequences = 7 child tiles', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (12, '12.3', 'S3 acts on off-diagonal tiles', 'D', '28_N_Dimensional_Game_Lattices.md');
