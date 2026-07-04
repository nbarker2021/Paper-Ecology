
-- Table: claims
-- Role: Claim ledger entries from mapped file reports
CREATE TABLE IF NOT EXISTS claims (
    claim_id        TEXT PRIMARY KEY,
    paper_num       INTEGER NOT NULL,
    claim_text      TEXT NOT NULL,
    tag             TEXT CHECK (tag IN ('D','I','X')),
    source_file     TEXT,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- ============================================================
-- Paper 33 — Unified Electroweak Higgs Mass Residue
-- Domain: Electroweak / Symmetry Breaking
-- Cross-references: Paper 15 (mass residue), Paper 31 (electroweak),
--                   Paper 45-48 (electroweak sector)
-- ============================================================

-- Table: electroweak_translation
-- Role: Electroweak translation tables: W/Z as D4 sheets,
--       Higgs as VOA weight 5, mass residue as VOA weight diff.
CREATE TABLE IF NOT EXISTS electroweak_translation (
    translation_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    particle_name   TEXT NOT NULL,
    d4_sheet        INTEGER,               -- 0 or 1
    voa_weight      INTEGER,
    mass_gev        REAL,
    symmetry_broken INTEGER NOT NULL DEFAULT 1 CHECK (symmetry_broken IN (0,1)),
    paper_ref       INTEGER DEFAULT 33
);

-- Table: electroweak_symmetry_breaking
-- Role: Symmetry breaking as boundary repair records
CREATE TABLE IF NOT EXISTS electroweak_symmetry_breaking (
    breaking_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    gauge_state     TEXT NOT NULL,         -- symmetric state
    broken_state    TEXT NOT NULL,         -- broken state
    repair_curvature REAL,                 -- Higgs field as repair curvature
    mass_residue    REAL                   -- particle mass as residue
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_ew_particle ON electroweak_translation(particle_name);

-- Seed data: electroweak particle translations
INSERT INTO electroweak_translation (particle_name, d4_sheet, voa_weight, mass_gev, symmetry_broken) VALUES
('W+', 0, 3, 80.38, 1),
('W-', 1, 3, 80.38, 1),
('Z0', NULL, 4, 91.19, 1),
('Photon', NULL, 0, 0.0, 0),
('Higgs', NULL, 5, 125.25, 1);

-- Added claims from mapped file report for paper-033
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.12, 'αₛ = 5κ/π (bare) → running αₛ(m_Z) = 0.1179', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.13, 'α_em⁻¹ = 137.035999...', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.14, 'G_N = κ³', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.15, 'sin²θ_W = 0.23122', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.16, 'All from κ = ln(φ)/16 per tile edge', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.17, 'Coupling Transport — Tile Coupling Constants from κ', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (33, 33.18, 'Tier: Energy/Mass (30-33)', 'I', '25_Energetic_Traversal_Maps.md');
