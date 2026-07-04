-- ============================================================
-- Paper 55 — Unified Higgs And Vacuum 3 Vacuum Stability
-- Domain: Vacuum Stability / Metastability
-- Cross-references: Paper 53 (Higgs mechanism), Paper 54 (VOA weight 5),
--                   Paper 56 (Higgs couplings)
-- ============================================================

-- Table: vacuum_stability
-- Role: Vacuum stability analysis. Stable if repair curvature positive.
CREATE TABLE IF NOT EXISTS vacuum_stability (
    analysis_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    vacuum_id       INTEGER NOT NULL,
    higgs_mass_gev  REAL NOT NULL,
    top_mass_gev    REAL NOT NULL,
    alpha_s         REAL,                  -- strong coupling
    stability_status TEXT NOT NULL CHECK (stability_status IN ('stable','metastable','unstable')),
    lifetime_years  REAL,                  -- if metastable
    repair_curvature REAL,
    FOREIGN KEY (vacuum_id) REFERENCES vacuum_states(vacuum_id)
);

-- Table: metastability_boundaries
-- Role: Boundary between stable and unstable vacua
CREATE TABLE IF NOT EXISTS metastability_boundaries (
    boundary_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    higgs_mass_gev  REAL,
    top_mass_gev    REAL,
    boundary_type   TEXT CHECK (boundary_type IN ('stability','metastability','instability'))
);

-- Seed data: vacuum stability (SM metastability region)
INSERT INTO vacuum_stability (vacuum_id, higgs_mass_gev, top_mass_gev, alpha_s, stability_status, lifetime_years, repair_curvature) VALUES
(1, 125.25, 173.1, 0.118, 'metastable', 1e100, 0.01);
