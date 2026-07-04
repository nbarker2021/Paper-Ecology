-- ============================================================
-- Paper 40 — Unified Grand Reconstruction Map
-- Domain: Reconstruction / SM Mapping Bridge
-- Cross-references: Paper 38 (grand map), Paper 41-48 (SM sectors)
-- ============================================================

-- Table: reconstruction_map
-- Role: 8 irreducible gaps → 8 papers mapping
CREATE TABLE IF NOT EXISTS reconstruction_map (
    map_entry_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    gap_id          INTEGER NOT NULL,
    gap_name        TEXT NOT NULL,
    target_paper    INTEGER NOT NULL,
    sm_mapping_bridge TEXT,                -- bridge to SM
    reconstruction_status TEXT DEFAULT 'in_progress',
    FOREIGN KEY (gap_id) REFERENCES irreducible_gaps(gap_id),
    FOREIGN KEY (target_paper) REFERENCES papers(paper_num)
);

-- Table: sm_bridge_mappings
-- Role: SM mapping as bridge between FLCR substrate and physical reality
CREATE TABLE IF NOT EXISTS sm_bridge_mappings (
    bridge_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    sm_sector       TEXT NOT NULL,         -- e.g., 'QCD', 'Electroweak', 'Higgs'
    flcr_structure  TEXT NOT NULL,
    bridge_status   TEXT DEFAULT 'open'
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_recon_gap ON reconstruction_map(gap_id);
CREATE INDEX IF NOT EXISTS idx_sm_sector ON sm_bridge_mappings(sm_sector);

-- Seed data: reconstruction map
INSERT INTO reconstruction_map (gap_id, gap_name, target_paper, sm_mapping_bridge, reconstruction_status) VALUES
(1, 'CKM Numerics', 50, 'CKM matrix as D12 action', 'in_progress'),
(2, 'Particle VOA Weights', 16, 'VOA weight ladder', 'in_progress'),
(3, 'Higgs Mass Derivation', 53, 'Higgs as VOA weight 5', 'in_progress'),
(4, 'Gamma72 Landing', 91, 'Niemeier glue', 'open'),
(5, 'Full Moonshine ID', 18, 'Monster VOA routes', 'partial'),
(6, 'Rule 30 Non-Periodicity', 81, 'Lucas carry proof', 'open'),
(7, 'GR EFE Identity', 65, 'Repair curvature → EFE', 'open'),
(8, 'Cosmogenesis', 100, 'Big Bang = Higgs self-observation', 'open');

-- Mapped claims extraction

-- Table: mapped_claims_40
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (40, 1, 'TarpitTile (Knight CA), SpectreTile (tile cluster), KnightCATile - Knight CA = 8 states = 8 chart states - OEIS A033996 = Knight moves - Golden sweep = 7-fold substitution', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (40, 2, 'Tarpit Engine = Universal Tile Computer', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (40, 3, 'Tarpit Tile Computer (40-43)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (40, 4, 'Spectre tile cluster = universal tile computer', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
