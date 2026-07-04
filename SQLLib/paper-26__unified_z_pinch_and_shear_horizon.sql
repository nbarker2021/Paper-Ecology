-- ============================================================
-- Paper 26 — Unified Z Pinch And Shear Horizon
-- Domain: Plasma Physics / Shear Boundaries
-- Cross-references: Paper 23 (plasma carrier), Paper 25 (energetic),
--                   Paper 35 (plasma energy), Paper 37 (plasma traversal)
-- ============================================================

-- Table: z_pinch_configurations
-- Role: Z-pinch plasma configurations as carrier states
CREATE TABLE IF NOT EXISTS z_pinch_configurations (
    config_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    config_name     TEXT NOT NULL,
    pinch_current   REAL,                  -- MA
    pinch_radius    REAL,                  -- m
    magnetic_field  REAL,                  -- T
    plasma_density  REAL,                  -- m^-3
    temperature_kev REAL,
    stability_status TEXT NOT NULL DEFAULT 'stable' CHECK (stability_status IN ('stable','unstable','shear_critical'))
);

-- Table: shear_horizons
-- Role: Shear bands and horizons as typed boundaries
CREATE TABLE IF NOT EXISTS shear_horizons (
    horizon_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    config_id       INTEGER NOT NULL,
    horizon_type    TEXT NOT NULL CHECK (horizon_type IN ('shear_band','plasma_horizon','carrier_horizon')),
    boundary_curvature REAL,               -- repair curvature at horizon
    entropy_density REAL,
    FOREIGN KEY (config_id) REFERENCES z_pinch_configurations(config_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_pinch_status ON z_pinch_configurations(stability_status);
CREATE INDEX IF NOT EXISTS idx_horizon_type ON shear_horizons(horizon_type);
