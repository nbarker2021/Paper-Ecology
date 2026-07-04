-- ============================================================
-- Paper 64 — Unified BSM And Dark 4 Inflation
-- Domain: Inflation / Early Universe
-- Cross-references: Paper 63 (dark energy), Paper 67 (FLRW)
-- ============================================================

-- Table: inflation_models
-- Role: Inflation as boundary repair of initial singularity
CREATE TABLE IF NOT EXISTS inflation_models (
    model_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name      TEXT NOT NULL,
    inflaton_field  TEXT,
    repair_curvature REAL,                 -- inflaton as repair curvature
    e_fold_count    REAL,                  -- N
    scalar_spectral_index REAL,            -- n_s
    tensor_to_scalar_ratio REAL,           -- r
    status          TEXT DEFAULT 'open'
);

-- Seed data: inflation models
INSERT INTO inflation_models (model_name, inflaton_field, e_fold_count, scalar_spectral_index, tensor_to_scalar_ratio) VALUES
('Slow-roll',      'inflaton_scalar', 60, 0.965, 0.03),
('Starobinsky',    'R^2',             60, 0.960, 0.003);
