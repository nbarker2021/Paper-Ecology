-- ============================================================
-- Paper 68 — Unified Cosmology 2 Cosmological Constant And Dark Energy
-- Domain: Cosmological Constant / ΛCDM
-- Cross-references: Paper 63 (dark energy), Paper 67 (FLRW)
-- ============================================================

-- Table: cosmological_constant
-- Role: Cosmological constant as vacuum repair curvature.
--       Dark energy as boundary repair.
CREATE TABLE IF NOT EXISTS cosmological_constant (
    cc_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    lambda_value    REAL,                  -- Λ
    vacuum_energy_density REAL,            -- ρ_Λ
    repair_curvature REAL,
    model           TEXT DEFAULT 'ΛCDM',
    status          TEXT DEFAULT 'observed'
);

-- Table: dark_energy_evolution
-- Role: Evolution of dark energy with redshift
CREATE TABLE IF NOT EXISTS dark_energy_evolution (
    evolution_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    redshift        REAL NOT NULL,
    w_z             REAL,                  -- w(z)
    rho_de          REAL,                  -- energy density
    FOREIGN KEY (redshift) REFERENCES flrw_parameters(redshift)
);

-- Seed data: cosmological constant
INSERT INTO cosmological_constant (lambda_value, vacuum_energy_density, repair_curvature, model) VALUES
(1.1056e-52, 5.96e-27, 0.0, 'ΛCDM');
