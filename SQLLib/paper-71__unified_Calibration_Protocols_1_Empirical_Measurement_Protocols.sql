-- ============================================================
-- Paper 71 — Unified Calibration Protocols 1 Empirical Measurement
-- Domain: Calibration / Measurement Protocols
-- Cross-references: Paper 72-74 (calibration), Paper 15 (natural unit)
-- ============================================================

-- Table: empirical_measurement_protocols
-- Role: Calibration protocols with natural unit κ = 25.05 GeV as anchor
CREATE TABLE IF NOT EXISTS empirical_measurement_protocols (
    protocol_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    protocol_name   TEXT NOT NULL,
    measurement_type TEXT NOT NULL,
    anchor_unit     TEXT DEFAULT 'kappa',
    anchor_value_gev REAL DEFAULT 25.05,
    lattice_code_chain TEXT,               -- e.g., "1->3->7->8->24->72"
    protocol_status TEXT DEFAULT 'active'
);

-- Table: calibration_measurements
-- Role: Individual calibration measurements
CREATE TABLE IF NOT EXISTS calibration_measurements (
    measurement_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    protocol_id     INTEGER NOT NULL,
    measured_value  REAL,
    uncertainty     REAL,
    calibration_date DATETIME,
    FOREIGN KEY (protocol_id) REFERENCES empirical_measurement_protocols(protocol_id)
);

-- Seed data: calibration protocols
INSERT INTO empirical_measurement_protocols (protocol_name, measurement_type, lattice_code_chain) VALUES
('Higgs mass anchor', 'mass', '1->3->7->8->24->72'),
('VOA weight ladder', 'weight', '1->3->7->8'),
('CKM matrix element', 'mixing', '3->8->24->72');
