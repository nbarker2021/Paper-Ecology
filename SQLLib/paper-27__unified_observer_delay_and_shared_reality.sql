-- ============================================================
-- Paper 27 — Unified Observer Delay And Shared Reality
-- Domain: Multi-Observer / Shared State
-- Cross-references: Paper 06 (causal links), Paper 19 (face selection),
--                   Paper 38 (AI runtime)
-- ============================================================

-- Table: observer_delay_records
-- Role: Observer delay measurements and protocols
CREATE TABLE IF NOT EXISTS observer_delay_records (
    record_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    observer_id_1   TEXT NOT NULL,
    observer_id_2   TEXT NOT NULL,
    delay_ms        REAL,                  -- measured delay
    protocol        TEXT CHECK (protocol IN ('sync','async','causal','shared_state')),
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (observer_id_1) REFERENCES observer_registry(observer_id),
    FOREIGN KEY (observer_id_2) REFERENCES observer_registry(observer_id)
);

-- Table: shared_reality_states
-- Role: Lattice closure of multiple observers
CREATE TABLE IF NOT EXISTS shared_reality_states (
    shared_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    observer_set    TEXT NOT NULL,         -- JSON array of observer_ids
    consensus_state INTEGER,               -- agreed LCR state
    closure_depth   INTEGER,
    FOREIGN KEY (consensus_state) REFERENCES lcr_states(state_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_delay_obs1 ON observer_delay_records(observer_id_1);
CREATE INDEX IF NOT EXISTS idx_delay_obs2 ON observer_delay_records(observer_id_2);
