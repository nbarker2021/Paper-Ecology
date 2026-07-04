-- ============================================================
-- Paper 37 — Unified Plasma Energy Traversal
-- Domain: Plasma Physics / Energy-Carrier Identification
-- Cross-references: Paper 23 (shear/plasma), Paper 25 (energetic),
--                   Paper 26 (z-pinch), Paper 35 (plasma)
-- ============================================================

-- Table: plasma_energy_traversal
-- Role: Plasma as carrier, energy as curvature, traversal as path
CREATE TABLE IF NOT EXISTS plasma_energy_traversal (
    traversal_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    plasma_config_id INTEGER,
    carrier_path_id INTEGER,
    energy_density  REAL,
    curvature_k     REAL,
    traversal_length REAL,
    status          TEXT DEFAULT 'active'
);

-- Table: plasma_calibration
-- Role: Calibration of plasma physics to FLCR substrate
CREATE TABLE IF NOT EXISTS plasma_calibration (
    calibration_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    plasma_param    TEXT NOT NULL,
    flcr_equivalent TEXT NOT NULL,
    calibration_factor REAL,
    verified        INTEGER DEFAULT 0
);

-- Seed data: plasma calibration
INSERT INTO plasma_calibration (plasma_param, flcr_equivalent, calibration_factor, verified) VALUES
('plasma_frequency', 'carrier_frequency', 1.0, 0),
('magnetic_pressure', 'repair_curvature', 1.0, 0),
('Alfven_speed', 'carrier_velocity', 1.0, 0);
