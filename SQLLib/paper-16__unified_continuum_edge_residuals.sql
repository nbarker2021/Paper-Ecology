-- ============================================================
-- Paper 16 — Unified Continuum Edge Residuals
-- Domain: Continuum Limits / Bridge Artifacts
-- Cross-references: Paper 07 (bridge), Paper 15 (mass residue),
--                   Paper 33 (GR continuum), Paper 85 (Navier-Stokes)
-- ============================================================

-- Table: continuum_edge_residuals
-- Role: Boundary between discrete and continuous descriptions.
--       Tracks finite, local, explicit bridge artifacts.
CREATE TABLE IF NOT EXISTS continuum_edge_residuals (
    residual_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    edge_name       TEXT NOT NULL,
    discrete_model  TEXT NOT NULL,
    continuum_model TEXT NOT NULL,
    bridge_artifact_id INTEGER,
    is_finite       INTEGER NOT NULL DEFAULT 1 CHECK (is_finite IN (0,1)),
    is_local        INTEGER NOT NULL DEFAULT 1 CHECK (is_local IN (0,1)),
    is_explicit     INTEGER NOT NULL DEFAULT 1 CHECK (is_explicit IN (0,1)),
    global_collapse_deferred INTEGER NOT NULL DEFAULT 1 CHECK (global_collapse_deferred IN (0,1)),
    residue_type    TEXT CHECK (residue_type IN ('none','mckay','o2_prime','bridge_limit','open'))
);

-- Table: bridge_artifact_registry
-- Role: Registry of all bridge artifacts across papers
CREATE TABLE IF NOT EXISTS bridge_artifact_registry (
    artifact_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    artifact_name   TEXT NOT NULL,
    source_paper    INTEGER NOT NULL,
    target_paper    INTEGER,
    artifact_type   TEXT CHECK (artifact_type IN ('piecewise_linear','spline','kernel','limit','extrapolation')),
    verification_status TEXT NOT NULL DEFAULT 'open',
    FOREIGN KEY (source_paper) REFERENCES papers(paper_num),
    FOREIGN KEY (target_paper) REFERENCES papers(paper_num)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_residual_edge ON continuum_edge_residuals(edge_name);
CREATE INDEX IF NOT EXISTS idx_artifact_source ON bridge_artifact_registry(source_paper);

-- Seed data: key continuum edge residuals
INSERT INTO continuum_edge_residuals (edge_name, discrete_model, continuum_model, is_finite, is_local, is_explicit, global_collapse_deferred, residue_type) VALUES
('LCR-to-Riemann', 'LCR lattice', 'Riemannian manifold', 1, 1, 1, 1, 'bridge_limit'),
('F4-to-QFT',      'F4 lattice',  'Quantum field theory', 1, 1, 1, 1, 'bridge_limit'),
('Rule30-to-NS',   'Rule 30 grid', 'Navier-Stokes fluid', 1, 1, 1, 1, 'open'),
('E8-to-GR',       'E8 root lattice', 'General relativity', 1, 1, 1, 1, 'mckay');
