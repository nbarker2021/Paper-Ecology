-- ============================================================
-- Paper 15 — Unified Qft Higgs Mass Residue
-- Domain: Higgs Mechanism / Mass Residue
-- Cross-references: Paper 16 (continuum edge), Paper 31 (electroweak),
--                   Paper 53-56 (Higgs and vacuum)
-- ============================================================

-- Table: voa_weight_assignments
-- Role: VOA weight assignments for Standard Model particles.
--       Natural unit κ = 25.05 GeV.
CREATE TABLE IF NOT EXISTS voa_weight_assignments (
    particle_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    particle_name   TEXT NOT NULL,
    voa_weight      INTEGER NOT NULL,
    mass_gev        REAL,
    mass_formula    TEXT,                  -- e.g., "5 * kappa"
    structural_derived INTEGER NOT NULL DEFAULT 1 CHECK (structural_derived IN (0,1)),
    numeric_calibrated INTEGER NOT NULL DEFAULT 0 CHECK (numeric_calibrated IN (0,1)),
    paper_source    INTEGER NOT NULL DEFAULT 15
);

-- Table: mass_residue
-- Role: Mass residue tracking — structural derivation vs numeric calibration
CREATE TABLE IF NOT EXISTS mass_residue (
    residue_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    particle_id     INTEGER NOT NULL,
    structural_mass REAL,
    calibrated_mass REAL,
    residue_delta   REAL,                  -- difference
    status          TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','resolved','open')),
    FOREIGN KEY (particle_id) REFERENCES voa_weight_assignments(particle_id)
);

-- Table: natural_units
-- Role: Natural unit definitions and calibration anchors
CREATE TABLE IF NOT EXISTS natural_units (
    unit_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_name       TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    value_gev       REAL,
    formula         TEXT,
    calibration_source TEXT
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_voa_weight  ON voa_weight_assignments(voa_weight);
CREATE INDEX IF NOT EXISTS idx_voa_particle ON voa_weight_assignments(particle_name);
CREATE INDEX IF NOT EXISTS idx_residue_status ON mass_residue(status);

-- Seed data: natural unit κ
INSERT INTO natural_units (unit_name, symbol, value_gev, formula, calibration_source) VALUES
('kappa', 'κ', 25.05, 'ln(φ)/16 * SCALE', 'Higgs mass anchor');

-- Seed data: key VOA weight assignments
INSERT INTO voa_weight_assignments (particle_name, voa_weight, mass_gev, mass_formula, structural_derived, numeric_calibrated) VALUES
('Higgs boson',     5, 125.25, '5 * κ',        1, 1),
('W boson',         3,  80.38, '3.2 * κ',      1, 0),
('Z boson',         4,  91.19, '3.6 * κ',      1, 0),
('Top quark',       7, 173.1,  '6.9 * κ',      1, 0),
('Charm quark',     5, 1.27,   '0.05 * κ',     1, 0),
('Bottom quark',    5, 4.18,   '0.17 * κ',     1, 0),
('Tau lepton',      3, 1.777,  '0.07 * κ',     1, 0),
('Muon',            2, 0.1057, '0.004 * κ',    1, 0),
('Electron',        1, 0.000511, '2e-5 * κ',   1, 0);
