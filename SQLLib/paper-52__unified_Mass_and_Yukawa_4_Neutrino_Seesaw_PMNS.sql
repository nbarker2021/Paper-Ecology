-- ============================================================
-- Paper 52 — Unified Mass And Yukawa 4 Neutrino Seesaw PMNS
-- Domain: Neutrino Masses / Seesaw Mechanism
-- Cross-references: Paper 50 (PMNS), Paper 51 (BSM), Paper 61 (neutrino)
-- ============================================================

-- Table: neutrino_seesaw
-- Role: Seesaw mechanism as D12 action giving neutrinos small masses
CREATE TABLE IF NOT EXISTS neutrino_seesaw (
    seesaw_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    mechanism_type  TEXT NOT NULL CHECK (mechanism_type IN ('type_I','type_II','type_III','inverse')),
    light_neutrino  TEXT NOT NULL,
    heavy_partner   TEXT,
    mass_scale_gev  REAL,                  -- right-handed neutrino mass scale
    light_mass_ev   REAL,                  -- predicted light neutrino mass
    d12_action_index INTEGER,
    status          TEXT DEFAULT 'open'
);

-- Table: neutrino_mass_hierarchy
-- Role: Neutrino mass hierarchy from VOA weights
CREATE TABLE IF NOT EXISTS neutrino_mass_hierarchy (
    neutrino_id     INTEGER PRIMARY KEY,
    flavor          TEXT NOT NULL CHECK (flavor IN ('electron','muon','tau')),
    mass_squared_diff REAL,                -- eV^2
    hierarchy_type  TEXT CHECK (hierarchy_type IN ('normal','inverted','degenerate'))
);

-- Seed data: neutrino mass hierarchy (normal ordering)
INSERT INTO neutrino_mass_hierarchy (neutrino_id, flavor, mass_squared_diff, hierarchy_type) VALUES
(1, 'electron', 7.53e-5, 'normal'),
(2, 'muon',     2.51e-3, 'normal'),
(3, 'tau',      2.51e-3, 'normal');

-- Seed data: seesaw mechanism
INSERT INTO neutrino_seesaw (mechanism_type, light_neutrino, heavy_partner, mass_scale_gev, light_mass_ev, status) VALUES
('type_I', 'electron neutrino', 'right-handed nu_e', 1e12, 0.01, 'open'),
('type_I', 'muon neutrino',     'right-handed nu_mu', 1e12, 0.05, 'open'),
('type_I', 'tau neutrino',      'right-handed nu_tau', 1e12, 0.05, 'open');

-- Mapped claims extraction

-- Table: mapped_claims_52
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (52, 1, 'SpectreTile (center C), CrystalTile (bonded), TarpitTile - C invariant 64/64 - Gluon bond = C - Cluster cohesion = shared C', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (52, 2, 'Shared Center C = GLUON Invariant — Tile Center Bond', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (52, 3, 'Observer Physics (50-53)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (52, 4, 'Center C = unique invariant bond under LR swap across all tile states', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
