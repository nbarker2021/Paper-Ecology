-- ============================================================
-- Paper 51 — Unified Mass And Yukawa 3 BSM Constraints
-- Domain: BSM Constraints / Flavor Symmetry
-- Cross-references: Paper 49-50 (mass/Yukawa), Paper 61-64 (BSM)
-- ============================================================

-- Table: bsm_constraints
-- Role: Beyond-the-Standard-Model constraints and open obligations
CREATE TABLE IF NOT EXISTS bsm_constraints (
    constraint_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    constraint_name TEXT NOT NULL,
    constraint_type TEXT CHECK (constraint_type IN ('flavor','CP','neutrino','dark_matter','dark_energy','inflation')),
    current_limit   REAL,                  -- experimental limit
    flcr_prediction REAL,                  -- FLCR structural prediction
    status          TEXT DEFAULT 'open' CHECK (status IN ('open','partial','closed'))
);

-- Table: flavor_symmetry_breaking
-- Role: Flavor symmetry breaking as D12 action
CREATE TABLE IF NOT EXISTS flavor_symmetry_breaking (
    breaking_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    symmetry_before TEXT NOT NULL,
    symmetry_after  TEXT NOT NULL,
    d12_element     TEXT,
    pattern         TEXT                   -- observed pattern description
);

-- Seed data: BSM constraints
INSERT INTO bsm_constraints (constraint_name, constraint_type, current_limit, flcr_prediction, status) VALUES
('Proton decay limit', 'flavor', 1.6e34, NULL, 'open'),
('Neutrinoless double beta', 'neutrino', 0.0, NULL, 'open'),
('Dark matter cross-section', 'dark_matter', 1e-46, NULL, 'open'),
('Flavor-changing neutral current', 'flavor', 1e-12, NULL, 'open');

-- Mapped claims extraction

-- Table: mapped_claims_51
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (51, 1, 'SpectreTile (center C), FCCTile (C shared), CrystalTile - C shared 64/64 - GLUON = C = GLUON(swap_LR) - LR swap invariant', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (51, 2, 'Gluon Invariant = Shared Center C — Tile Center Invariant', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (51, 3, 'Observer Physics (50-53)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (51, 4, 'Center C is invariant under all observer frames (64/64) = gluon invariant', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
