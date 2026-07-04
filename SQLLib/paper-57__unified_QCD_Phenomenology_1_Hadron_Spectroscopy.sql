-- ============================================================
-- Paper 57 — Unified QCD Phenomenology 1 Hadron Spectroscopy
-- Domain: Hadron Spectroscopy / QCD Bound States
-- Cross-references: Paper 13 (quark faces), Paper 44 (confinement),
--                   Paper 58-60 (QCD phenomenology)
-- ============================================================

-- Table: hadron_spectroscopy
-- Role: Hadron spectrum from FLCR substrate. Masses = VOA weight sums.
CREATE TABLE IF NOT EXISTS hadron_spectroscopy (
    hadron_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    hadron_name     TEXT NOT NULL,
    hadron_type     TEXT NOT NULL CHECK (hadron_type IN ('meson','baryon','tetraquark','pentaquark')),
    quark_content   TEXT NOT NULL,         -- JSON array
    voa_weight_sum  INTEGER,
    mass_mev        REAL,
    mass_from_voa   REAL,                  -- predicted from VOA weights
    jpc             TEXT                   -- quantum numbers
);

-- Seed data: selected hadrons
INSERT INTO hadron_spectroscopy (hadron_name, hadron_type, quark_content, voa_weight_sum, mass_mev, jpc) VALUES
('pion+',   'meson',   '["up","anti-down"]',   2, 139.57,  '0-+'),
('pion0',   'meson',   '["up","anti-up"]',     2, 134.98,  '0-+'),
('proton',  'baryon',  '["up","up","down"]',   3, 938.27,  '1/2+'),
('neutron', 'baryon',  '["up","down","down"]', 3, 939.57,  '1/2+'),
('J/psi',   'meson',   '["charm","anti-charm"]',4, 3096.9, '1--');

-- Mapped claims extraction

-- Table: mapped_claims_57
CREATE TABLE IF NOT EXISTS mapped_claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_num INTEGER NOT NULL,
    claim_seq INTEGER NOT NULL,
    claim_text TEXT NOT NULL,
    claim_tag TEXT DEFAULT 'D',
    source_file TEXT,
    extraction_date TEXT
);

-- Mapped claims extraction
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (57, 1, '**FILE:** `paper_57.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (57, 2, '**TITLE:** Paper 57 — QCD Phenomenology 1: Hadron Spectroscopy', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (57, 3, '**SUMMARY:** QCD phenomenology 1: hadron spectroscopy', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
