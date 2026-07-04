-- ============================================================
-- Paper 74 — Unified Calibration Protocols 4 Between Sample Dynamics Dynamics
-- Domain: Meta-Tests / Cross-Validation
-- Cross-references: Paper 72 (between-sample), Paper 73 (closure)
-- ============================================================

-- Table: meta_tests
-- Role: Meta-tests that test the tests themselves
CREATE TABLE IF NOT EXISTS meta_tests (
    meta_test_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    target_test_id  INTEGER NOT NULL,
    meta_test_type  TEXT CHECK (meta_test_type IN ('cross_validation','bootstrap','jackknife','replication')),
    meta_test_result TEXT CHECK (meta_test_result IN ('pass','fail','inconclusive')),
    repair_of_test_process TEXT             -- boundary repair of test process
);

-- Table: cross_validation_results
-- Role: Cross-validation as meta-test procedure
CREATE TABLE IF NOT EXISTS cross_validation_results (
    cv_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    meta_test_id    INTEGER NOT NULL,
    fold_count      INTEGER,
    mean_score      REAL,
    std_score       REAL,
    FOREIGN KEY (meta_test_id) REFERENCES meta_tests(meta_test_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_meta_target ON meta_tests(target_test_id);
