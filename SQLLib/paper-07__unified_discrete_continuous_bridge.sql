-- ============================================================
-- Paper 07 — Unified Discrete Continuous Bridge
-- Domain: Bridge Math / Piecewise-Linear Interpolation
-- Cross-references: Paper 06 (causal links), Paper 08 (lattice closure),
--                   Paper 33 (GR continuum), Paper 85 (Navier-Stokes)
-- ============================================================

-- Table: bridge_artifacts
-- Role: Bridge artifacts that map discrete lattice carriers to
--       continuous observables. Each artifact preserves sample identity.
CREATE TABLE IF NOT EXISTS bridge_artifacts (
    artifact_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_name   TEXT NOT NULL,
    discrete_source TEXT NOT NULL,         -- e.g., "lcr_state_3"
    continuous_target TEXT NOT NULL,       -- e.g., "Riemannian manifold M"
    interpolant_type TEXT NOT NULL CHECK (interpolant_type IN ('piecewise_linear','spline','kernel','bridge_limit')),
    sample_identity_preserved INTEGER NOT NULL DEFAULT 1 CHECK (sample_identity_preserved IN (0,1)),
    provenance_hash  TEXT NOT NULL,        -- content-addressed provenance
    calibration_required INTEGER NOT NULL DEFAULT 1 CHECK (calibration_required IN (0,1))
);

-- Table: sample_provenance
-- Role: Provenance tracking for each sample — trace to origin
CREATE TABLE IF NOT EXISTS sample_provenance (
    sample_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_id     INTEGER NOT NULL,
    origin_paper    INTEGER NOT NULL,
    origin_state    INTEGER,
    extraction_step INTEGER,
    provenance_chain TEXT,                 -- JSON array of derivation steps
    FOREIGN KEY (artifact_id) REFERENCES bridge_artifacts(artifact_id),
    FOREIGN KEY (origin_paper) REFERENCES papers(paper_num),
    FOREIGN KEY (origin_state) REFERENCES lcr_states(state_id)
);

-- Table: e8_roots
-- Role: The 240 roots of the E8 root system.
--       Included here per explicit schema pattern request for Paper 07 (E8).
CREATE TABLE IF NOT EXISTS e8_roots (
    root_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    root_vector     TEXT NOT NULL,         -- 8D integer vector as JSON
    root_norm       INTEGER NOT NULL DEFAULT 2,
    weyl_orbit      TEXT,                  -- orbit label under Weyl group
    height          INTEGER,
    simple_root     INTEGER NOT NULL DEFAULT 0 CHECK (simple_root IN (0,1)),
    dual_root_id    INTEGER,               -- self-dual for E8
    FOREIGN KEY (dual_root_id) REFERENCES e8_roots(root_id)
);

-- Table: signal_harmonization
-- Role: Signal harmonization table for E8 root system integration.
--       Maps signals across different E8 sublattices.
CREATE TABLE IF NOT EXISTS signal_harmonization (
    harmonization_id INTEGER PRIMARY KEY AUTOINCREMENT,
    root_id_1       INTEGER NOT NULL,
    root_id_2       INTEGER NOT NULL,
    correlation     REAL,                  -- harmonic correlation coefficient
    sublattice      TEXT CHECK (sublattice IN ('D8','E7','A8','E6','A4+A4','D5+D3','A7+A1','A5+A2+A1','A3+A3+2A1','6A1+A2')),
    FOREIGN KEY (root_id_1) REFERENCES e8_roots(root_id),
    FOREIGN KEY (root_id_2) REFERENCES e8_roots(root_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_bridge_interp ON bridge_artifacts(interpolant_type);
CREATE INDEX IF NOT EXISTS idx_prov_sample   ON sample_provenance(sample_id);
CREATE INDEX IF NOT EXISTS idx_e8_orbit      ON e8_roots(weyl_orbit);
CREATE INDEX IF NOT EXISTS idx_e8_height     ON e8_roots(height);

-- Seed data: E8 simple roots (8 vectors)
INSERT INTO e8_roots (root_vector, root_norm, weyl_orbit, height, simple_root) VALUES
('[1,-1,0,0,0,0,0,0]', 2, 'A7', 1, 1),
('[0,1,-1,0,0,0,0,0]', 2, 'A7', 1, 1),
('[0,0,1,-1,0,0,0,0]', 2, 'A7', 1, 1),
('[0,0,0,1,-1,0,0,0]', 2, 'A7', 1, 1),
('[0,0,0,0,1,-1,0,0]', 2, 'A7', 1, 1),
('[0,0,0,0,0,1,-1,0]', 2, 'A7', 1, 1),
('[0,0,0,0,0,0,1,-1]', 2, 'A7', 1, 1),
('[-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]', 2, 'A1', 1, 1);

-- Seed data: sample bridge artifacts
INSERT INTO bridge_artifacts (artifact_name, discrete_source, continuous_target, interpolant_type, sample_identity_preserved, provenance_hash, calibration_required) VALUES
('LCR-to-Manifold', 'lcr_carrier', 'Riemannian manifold M', 'piecewise_linear', 1, 'sha256:abc123', 1),
('Lattice-to-QFT',  'lattice_F4',  'continuum_QFT',         'bridge_limit',     1, 'sha256:def456', 1),
('Discrete-NS',     'rule30_grid', 'Navier-Stokes field',   'kernel',           1, 'sha256:ghi789', 1);

-- ============================================================
-- Harvested tables (from cqe_signal_harmonizer.py)
-- ============================================================

-- Table: signal_registry
-- Role: Registry of individual signals processed by the harmonizer.
CREATE TABLE IF NOT EXISTS signal_registry (
    signal_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    signal_name     TEXT NOT NULL,
    values_json     TEXT NOT NULL,         -- JSON array of raw signal values
    confidence      REAL NOT NULL DEFAULT 1.0,
    modality        TEXT NOT NULL DEFAULT 'generic',
    vector_8d       TEXT,                  -- JSON array of 8D projection
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Table: consensus_results
-- Role: Results of geometric harmonization operations.
CREATE TABLE IF NOT EXISTS consensus_results (
    result_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    consensus_vector TEXT NOT NULL,        -- JSON array of 8D consensus
    nearest_root_index INTEGER NOT NULL,
    root_distance   REAL NOT NULL,
    agreement_score REAL NOT NULL,
    stable          INTEGER NOT NULL DEFAULT 0 CHECK (stable IN (0,1)),
    avg_displacement REAL,
    max_displacement REAL,
    probes_run      INTEGER,
    energy          REAL NOT NULL,
    receipt_hash    TEXT NOT NULL,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Table: morsr_probe_results
-- Role: Per-signal MORSR stability probe results.
CREATE TABLE IF NOT EXISTS morsr_probe_results (
    probe_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    result_id       INTEGER NOT NULL,
    signal_name     TEXT NOT NULL,
    signal_distance REAL NOT NULL,
    signal_weight   REAL NOT NULL,
    FOREIGN KEY (result_id) REFERENCES consensus_results(result_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_signal_modality ON signal_registry(modality);
CREATE INDEX IF NOT EXISTS idx_consensus_root   ON consensus_results(nearest_root_index);
CREATE INDEX IF NOT EXISTS idx_consensus_receipt ON consensus_results(receipt_hash);
