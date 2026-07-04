-- ============================================================
-- Paper 72 — Unified Calibration Protocols 2 Between Sample Dynamics
-- Domain: Between-Sample Dynamics / Error Propagation
-- Cross-references: Paper 07 (bridge), Paper 71 (calibration)
-- ============================================================

-- Table: between_sample_dynamics
-- Role: Between-sample dynamics tests validating bridge artifact
CREATE TABLE IF NOT EXISTS between_sample_dynamics (
    test_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    bridge_artifact_id INTEGER,
    sample_id_1     INTEGER NOT NULL,
    sample_id_2     INTEGER NOT NULL,
    dynamic_test    TEXT NOT NULL,
    test_result     TEXT CHECK (test_result IN ('pass','fail','inconclusive')),
    systematic_error REAL
);

-- Table: systematic_errors
-- Role: Systematic errors converted to typed obligation rows
CREATE TABLE IF NOT EXISTS systematic_errors (
    error_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    error_source    TEXT NOT NULL,
    error_magnitude REAL,
    obligation_row_id INTEGER,
    traceability_hash TEXT
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_bsd_test ON between_sample_dynamics(test_result);
