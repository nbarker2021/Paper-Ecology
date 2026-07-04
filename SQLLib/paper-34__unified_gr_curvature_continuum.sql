-- ============================================================
-- Paper 34 — Unified Gr Curvature Continuum
-- Domain: GR Continuum / Curvature Translation
-- Cross-references: Paper 14 (repair curvature), Paper 15 (mass),
--                   Paper 65 (EFE), Paper 66 (BH entropy)
-- ============================================================

-- Table: gr_curvature_continuum
-- Role: Ricci scalar as repair curvature, continuum as bridge limit
CREATE TABLE IF NOT EXISTS gr_curvature_continuum (
    mapping_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    discrete_curvature REAL,               -- repair curvature K(v)
    ricci_scalar    REAL,                  -- continuum limit
    metric_tensor   TEXT,                  -- JSON matrix
    bridge_limit    INTEGER NOT NULL DEFAULT 1 CHECK (bridge_limit IN (0,1)),
    efe_status      TEXT NOT NULL DEFAULT 'deferred' CHECK (efe_status IN ('proven','deferred','open'))
);

-- Table: continuum_limit_params
-- Role: Parameters for taking the continuum limit
CREATE TABLE IF NOT EXISTS continuum_limit_params (
    param_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    lattice_spacing REAL,
    cutoff_scale    REAL,
    regulator       TEXT CHECK (regulator IN ('lattice','dimensional','zeta','none'))
);

-- Seed data: GR curvature mapping
INSERT INTO gr_curvature_continuum (discrete_curvature, ricci_scalar, bridge_limit, efe_status) VALUES
(0.0, 0.0, 1, 'deferred'),
(0.5, 0.5, 1, 'deferred'),
(1.0, 1.0, 1, 'deferred');
