-- ============================================================
-- Paper 69 — Unified Cosmology 3 Cosmic Microwave Background
-- Domain: CMB / Acoustic Peaks
-- Cross-references: Paper 67 (FLRW), Paper 68 (dark energy),
--                   Paper 70 (large-scale structure)
-- ============================================================

-- Table: cmb_anisotropies
-- Role: CMB anisotropies as boundary repair of photon-baryon fluid.
--       Acoustic peaks = repair modes.
CREATE TABLE IF NOT EXISTS cmb_anisotropies (
    anisotropy_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    multipole_l     INTEGER NOT NULL,      -- l
    cl_value        REAL,                  -- power spectrum D_l
    repair_mode     TEXT,                  -- which repair mode
    peak_order      INTEGER,               -- 1st, 2nd, 3rd peak
    FOREIGN KEY (multipole_l) REFERENCES cmb_power_spectrum(multipole_l)
);

-- Table: cmb_power_spectrum
-- Role: CMB power spectrum as receipt of repair
CREATE TABLE IF NOT EXISTS cmb_power_spectrum (
    multipole_l     INTEGER PRIMARY KEY,
    cl_theory       REAL,
    cl_observed     REAL,
    error_bar       REAL,
    receipt_hash    TEXT
);

-- Table: acoustic_peaks
-- Role: Acoustic peaks as repair modes
CREATE TABLE IF NOT EXISTS acoustic_peaks (
    peak_id         INTEGER PRIMARY KEY,
    peak_order      INTEGER NOT NULL,
    multipole_l     INTEGER NOT NULL,
    peak_amplitude  REAL,
    repair_curvature REAL
);

-- Seed data: acoustic peaks (Planck 2018 approximate)
INSERT INTO acoustic_peaks (peak_id, peak_order, multipole_l, peak_amplitude, repair_curvature) VALUES
(1, 1, 220, 5700.0, 1.0),
(2, 2, 537, 2200.0, 0.5),
(3, 3, 810, 1200.0, 0.3);
