-- ============================================================
-- Paper 67 — Unified Cosmology 1 FLRW Derivation
-- Domain: FLRW Metric / Cosmological Model
-- Cross-references: Paper 65 (EFE), Paper 68 (dark energy),
--                   Paper 69-70 (cosmology)
-- ============================================================

-- Table: flrw_parameters
-- Role: FLRW metric derived from FLCR substrate.
--       Scale factor = carrier. Hubble parameter = carrier velocity.
CREATE TABLE IF NOT EXISTS flrw_parameters (
    param_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name      TEXT NOT NULL,
    scale_factor    REAL,                  -- a(t)
    hubble_param    REAL,                  -- H(t) in km/s/Mpc
    spatial_curvature REAL,                -- k
    repair_curvature  REAL,                -- k as repair curvature
    omega_matter    REAL,
    omega_radiation REAL,
    omega_lambda    REAL,
    redshift        REAL
);

-- Table: flrw_solutions
-- Role: Solutions for different curvature cases
CREATE TABLE IF NOT EXISTS flrw_solutions (
    solution_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    param_id        INTEGER NOT NULL,
    curvature_case  TEXT NOT NULL CHECK (curvature_case IN ('k=0','k>0','k<0')),
    solution_formula TEXT,
    scale_factor_at_t TEXT,                -- a(t) expression
    FOREIGN KEY (param_id) REFERENCES flrw_parameters(param_id)
);

-- Seed data: FLRW parameters (ΛCDM)
INSERT INTO flrw_parameters (model_name, hubble_param, spatial_curvature, omega_matter, omega_radiation, omega_lambda, redshift) VALUES
('ΛCDM today', 67.4, 0.0, 0.315, 9.0e-5, 0.684, 0.0),
('ΛCDM z=1',   67.4, 0.0, 0.315, 9.0e-5, 0.684, 1.0);
