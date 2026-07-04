-- ============================================================
-- Paper 46 — Unified SU2 U1 Electroweak Symmetry Breaking
-- Domain: Symmetry Breaking / Higgs Mechanism
-- Cross-references: Paper 45 (gauge bosons), Paper 53-56 (Higgs)
-- ============================================================

-- Table: electroweak_symmetry_breaking_events
-- Role: Symmetry breaking as boundary repair events
CREATE TABLE IF NOT EXISTS electroweak_symmetry_breaking_events (
    event_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    symmetry_before TEXT NOT NULL,         -- e.g., 'SU(2)xU(1)'
    symmetry_after  TEXT NOT NULL,         -- e.g., 'U(1)_EM'
    higgs_vev       REAL NOT NULL DEFAULT 246.0, -- GeV
    repair_curvature REAL,                 -- Higgs field as repair curvature
    temperature_gev REAL,                  -- critical temperature
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: mass_generation
-- Role: Particle masses as residue of symmetry breaking repair
CREATE TABLE IF NOT EXISTS mass_generation (
    generation_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id        INTEGER NOT NULL,
    particle_name   TEXT NOT NULL,
    generated_mass  REAL,
    yukawa_coupling REAL,
    FOREIGN KEY (event_id) REFERENCES electroweak_symmetry_breaking_events(event_id)
);

-- Seed data: symmetry breaking event
INSERT INTO electroweak_symmetry_breaking_events (symmetry_before, symmetry_after, higgs_vev, temperature_gev) VALUES
('SU(2)_L × U(1)_Y', 'U(1)_EM', 246.0, 159.5);

-- Table: mapped_claims_46
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (46, 1, '**FILE:** `paper_46.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (46, 2, '**TITLE:** Paper 46 — V-A Weak Interaction: V-A as D4 Sheet Selection, Weak Force as Boundary Repair, Parity Violation as Arf Mismatch', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (46, 3, '**SUMMARY:** V-A weak interaction: V-A as D4 sheet selection, weak force as boundary repair, parity violation as Arf mismatch', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
