-- ============================================================
-- Paper 61 — Unified BSM And Dark 1 Neutrino Masses And Mixing
-- Domain: Neutrino Physics / BSM
-- Cross-references: Paper 50 (PMNS), Paper 52 (seesaw)
-- ============================================================

-- Table: bsm_neutrino_masses
-- Role: Neutrino masses from VOA weight ladder
CREATE TABLE IF NOT EXISTS bsm_neutrino_masses (
    neutrino_id     INTEGER PRIMARY KEY,
    flavor          TEXT NOT NULL,
    voa_weight      INTEGER,
    mass_eV         REAL,
    mass_from_voa   REAL,
    mixing_angle    TEXT                   -- associated PMNS angle
);

-- Seed data: BSM neutrino masses
INSERT INTO bsm_neutrino_masses (neutrino_id, flavor, voa_weight, mass_eV, mixing_angle) VALUES
(1, 'electron', 1, 0.01,  'theta12'),
(2, 'muon',     2, 0.05,  'theta23'),
(3, 'tau',      2, 0.05,  'theta23');

-- Merged from paper-061__unified_claims.sql
-- paper-061 SQL Claim Ledger

CREATE TABLE IF NOT EXISTS claims_061 (
    claim_id TEXT PRIMARY KEY,
    claim_text TEXT,
    tag TEXT,
    source_file TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.1', 'Supervisor Cursor scans all 31 formal papers, 9 verifiers, 5 calibrations, 298 lib modules', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.2', 'Cursor coverage achieves 100% completeness across all corpus dimensions', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.3', 'Papers Scan: 31/31 PASS, all 31 formal papers indexed', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.4', 'Verifiers Scan: 9/9 PASS, 43 checks tracked, 0 defects', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.5', 'Calibrations Scan: 5/5 PASS, 5 calibration suites all PASS', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.6', 'Lib Scan: 298/298 PASS, 298 modules and 1665 functions indexed', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.7', 'Schema Scan: 18 tables, all constraints verified', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.8', 'Coverage Map overall = 1.0 (100% complete)', 'D', 'CQE-PAPER-061.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.9', 'SpectreTile IRL Alignment: 14 edges, aperiodic, chiral', 'X', 'PAPER-061-TILE-INTEGRATION.md');
INSERT INTO claims_061 (claim_id, claim_text, tag, source_file) VALUES ('61.10', 'Cursor = Tile Coverage Map, 100% coverage, Meta-observer on tiles', 'I', 'PAPER-061-TILE-INTEGRATION.md');
