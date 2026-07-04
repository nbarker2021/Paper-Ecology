-- ============================================================
-- Paper 09 — Unified Hamiltonian Temporal Emergence
-- Domain: Temporal Structure / Windowed Readouts
-- Cross-references: Paper 08 (lattice closure), Paper 10 (receipt),
--                   Paper 27 (observer delay)
-- ============================================================

-- Table: temporal_windows
-- Role: Temporal windows for FLCR substrate readouts.
--       Window count = n − w + 1.
CREATE TABLE IF NOT EXISTS temporal_windows (
    window_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    window_size     INTEGER NOT NULL,      -- w
    sequence_length INTEGER NOT NULL,      -- n
    window_count    INTEGER NOT NULL,      -- n - w + 1
    is_admitted     INTEGER NOT NULL DEFAULT 0 CHECK (is_admitted IN (0,1)),
    component_count INTEGER DEFAULT 5      -- 5-component admitted window
);

-- Table: hamiltonian_readouts
-- Role: Bounded Hamiltonian readout records
CREATE TABLE IF NOT EXISTS hamiltonian_readouts (
    readout_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    window_id       INTEGER NOT NULL,
    timestamp       REAL NOT NULL,         -- continuous time coordinate
    energy_value    REAL,                  -- Hamiltonian value
    is_bounded      INTEGER NOT NULL DEFAULT 1 CHECK (is_bounded IN (0,1)),
    receipt_hash    TEXT,
    FOREIGN KEY (window_id) REFERENCES temporal_windows(window_id)
);

-- Table: forward_receipts
-- Role: Forward-directed receipts (causal arrow)
CREATE TABLE IF NOT EXISTS forward_receipts (
    receipt_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    readout_id      INTEGER NOT NULL,
    from_window     INTEGER NOT NULL,
    to_window       INTEGER NOT NULL,
    transport_row   TEXT CHECK (transport_row IN ('demonstrated','bounded_local','registered_landing_forms')),
    FOREIGN KEY (readout_id) REFERENCES hamiltonian_readouts(readout_id)
);

-- Table: backward_receipts
-- Role: Backward-directed receipts (retrospective)
CREATE TABLE IF NOT EXISTS backward_receipts (
    receipt_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    readout_id      INTEGER NOT NULL,
    from_window     INTEGER NOT NULL,
    to_window       INTEGER NOT NULL,
    retrospective_verdict TEXT,
    FOREIGN KEY (readout_id) REFERENCES hamiltonian_readouts(readout_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_temp_size  ON temporal_windows(window_size);
CREATE INDEX IF NOT EXISTS idx_ham_window ON hamiltonian_readouts(window_id);
CREATE INDEX IF NOT EXISTS idx_fwd_readout ON forward_receipts(readout_id);
