-- ============================================================
-- Paper 95 — Unified SPINOR Observation And Open Gap Observer Evidence
-- Domain: SPINOR / Observer Evidence
-- Cross-references: Paper 19 (observer), Paper 32 (cursor)
-- ============================================================

-- Table: spinor_observation
-- Role: SPINOR = observer of FLCR substrate. Supervisor cursor.
CREATE TABLE IF NOT EXISTS spinor_observation (
    observation_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    spinor_id       TEXT NOT NULL,
    observer_id     TEXT,
    observed_state  INTEGER,
    observation_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    buffer_protocol TEXT,
    recording_hash  TEXT
);

-- Table: observer_evidence_gaps
-- Role: Open gaps in observer evidence
CREATE TABLE IF NOT EXISTS observer_evidence_gaps (
    gap_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    gap_description TEXT NOT NULL,
    target_paper    INTEGER,
    spinor_relevant INTEGER DEFAULT 1,
    status          TEXT DEFAULT 'open'
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_spinor_obs ON spinor_observation(spinor_id);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 95
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p95 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p95 (claim_ref, claim_text, status, source_file) VALUES
('95.1', 'The translation is the foundation of the metamaterials physics (Paper 96) and the applied forge validation (Paper 95)', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p95 (claim_ref, claim_text, status, source_file) VALUES
('95.2', 'The VOA partition Z(q) = 2q⁰ + 6q⁵ corresponds to the ti', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p95 (claim_ref, claim_text, status, source_file) VALUES
('95.3', 'Papers 90–95: the McKay-Thompson mapping (Paper 90) is bounded empirical (CONJ); the Niemeier glue (Paper 91) is structural proposal (CONJ); the F4 universality (Paper 92) is open; the cold-start terminal (Paper 93) is bounded (O(log n)); the encoder invariance (Paper 94) is bounded (crystal structure); the SPINOR observation (Paper 95) is bounded (quantum gate simulation)', 'I', 'mapped_file_claims_report.md');
