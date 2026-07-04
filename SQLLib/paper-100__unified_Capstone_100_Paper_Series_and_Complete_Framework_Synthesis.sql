-- ============================================================
-- Paper 100 — Unified Capstone 100 Paper Series And Complete Framework Synthesis
-- Domain: Capstone / Synthesis of All 100 Papers
-- Cross-references: ALL PAPERS 00-99
-- ============================================================

-- Table: capstone_synthesis
-- Role: Synthesis of 100-paper series. 2-category ℒ closed form.
--       8 irreducible gaps. Cosmological framework.
CREATE TABLE IF NOT EXISTS capstone_synthesis (
    synthesis_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    synthesis_name  TEXT NOT NULL,
    papers_count    INTEGER DEFAULT 100,
    category_l_form TEXT,                  -- closed form description
    gaps_count      INTEGER DEFAULT 8,
    cosmology_note  TEXT
);

-- Table: capstone_cross_references
-- Role: Cross-reference map from capstone to all papers
CREATE TABLE IF NOT EXISTS capstone_cross_references (
    xref_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_num       INTEGER NOT NULL,
    role_in_capstone TEXT,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- Table: cosmological_framework
-- Role: Big Bang = Higgs observing itself. Critical line = crease.
CREATE TABLE IF NOT EXISTS cosmological_framework (
    framework_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL,
    basis_paper     INTEGER,
    status          TEXT DEFAULT 'interpretation'
);

-- Seed data: capstone synthesis
INSERT INTO capstone_synthesis (synthesis_name, papers_count, category_l_form, gaps_count, cosmology_note) VALUES
('100-Paper UFT Synthesis', 100, '2-category ℒ with 8 objects, 8 1-morphisms, 7 2-morphisms, 26 generating relations', 8, 'Big Bang = Higgs self-observation');

-- Seed data: cosmological framework
INSERT INTO cosmological_framework (claim, basis_paper, status) VALUES
('Big Bang = Higgs field observing itself', 100, 'interpretation'),
('Critical line = crease of FLCR substrate', 86, 'structural_approach'),
('Primes = fold points of critical line', 86, 'structural_approach');

-- Seed data: cross-references to all papers
INSERT INTO capstone_cross_references (paper_num, role_in_capstone) VALUES
(0, 'grounding'), (1, 'foundation'), (2, 'foundation'), (3, 'foundation'),
(4, 'foundation'), (5, 'foundation'), (6, 'foundation'), (7, 'foundation'),
(8, 'foundation'), (9, 'foundation'), (10, 'foundation'), (11, 'foundation'),
(12, 'foundation'), (13, 'foundation'), (14, 'foundation'), (15, 'foundation'),
(16, 'foundation'), (17, 'foundation'), (18, 'foundation'), (19, 'foundation'),
(20, 'sm_translation'), (21, 'sm_translation'), (22, 'sm_translation'), (23, 'sm_translation'),
(24, 'sm_translation'), (25, 'sm_translation'), (26, 'sm_translation'), (27, 'sm_translation'),
(28, 'sm_translation'), (29, 'sm_translation'), (30, 'sm_translation'), (31, 'sm_translation'),
(32, 'sm_translation'), (33, 'sm_translation'), (34, 'sm_translation'), (35, 'sm_translation'),
(36, 'sm_translation'), (37, 'sm_translation'), (38, 'sm_translation'), (39, 'sm_translation'),
(40, 'sm_unification'), (41, 'sm_unification'), (42, 'sm_unification'), (43, 'sm_unification'),
(44, 'sm_unification'), (45, 'sm_unification'), (46, 'sm_unification'), (47, 'sm_unification'),
(48, 'sm_unification'), (49, 'sm_unification'), (50, 'sm_unification'), (51, 'sm_unification'),
(52, 'sm_unification'), (53, 'sm_unification'), (54, 'sm_unification'), (55, 'sm_unification'),
(56, 'sm_unification'), (57, 'sm_unification'), (58, 'sm_unification'), (59, 'sm_unification'),
(60, 'sm_unification'), (61, 'sm_unification'), (62, 'sm_unification'), (63, 'sm_unification'),
(64, 'sm_unification'), (65, 'sm_unification'), (66, 'sm_unification'), (67, 'sm_unification'),
(68, 'sm_unification'), (69, 'sm_unification'), (70, 'sm_unification'), (71, 'sm_unification'),
(72, 'sm_unification'), (73, 'sm_unification'), (74, 'sm_unification'), (75, 'sm_unification'),
(76, 'sm_unification'), (77, 'sm_unification'), (78, 'sm_unification'), (79, 'sm_unification'),
(80, 'applications'), (81, 'applications'), (82, 'applications'), (83, 'applications'),
(84, 'applications'), (85, 'applications'), (86, 'applications'), (87, 'applications'),
(88, 'applications'), (89, 'applications'), (90, 'applications'), (91, 'applications'),
(92, 'applications'), (93, 'applications'), (94, 'applications'), (95, 'applications'),
(96, 'applications'), (97, 'applications'), (98, 'applications'), (99, 'applications');

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: drive_inventory
-- Role: Unmapped file claims from project structure analysis
CREATE TABLE IF NOT EXISTS drive_inventory (
    claim_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    value       INTEGER,
    unit        TEXT,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL,
    tag         TEXT CHECK (tag IN ('D','I','X'))
);

INSERT INTO drive_inventory (claim_text, value, unit, source_file, source_date, tag) VALUES
('Total code files on D:\ drive', 207292, 'files', 'project_breakdown.md', '2026-07-03', 'D'),
('Active classification files', 115372, 'files', 'bipartite_review_part_a_historical.md', '2026-07-03', 'D'),
('Excluded historical files', 91920, 'files', 'bipartite_review_part_a_historical.md', '2026-07-03', 'D'),
('Merged active + historical files', 193259, 'files', 'file_by_file_merged_report.md', '2026-07-03', 'D'),
('CQE_CMPLX project files', 121809, 'files', 'project_breakdown.md', '2026-07-03', 'D'),
('CQE_CMPLX project size', 5905, 'MB', 'project_breakdown.md', '2026-07-03', 'D'),
('repo_harvest files', 68749, 'files', 'project_breakdown.md', '2026-07-03', 'D'),
('File classification categories', 88, 'categories', 'file_by_file_merged_report.md', '2026-07-03', 'D'),
('python_module classification count', 59941, 'files', 'file_by_file_merged_report.md', '2026-07-03', 'D'),
('HTTP endpoints passing tests', 13, 'endpoints', 'SERVER_TEST_REPORT.md', '2026-07-01', 'D'),
('Workspace units', 52, 'units', 'SERVER_TEST_REPORT.md', '2026-07-01', 'D'),
('Git repositories', 35, 'repos', 'SERVER_TEST_REPORT.md', '2026-07-01', 'D'),
('Source-of-truth units', 5, 'units', 'SERVER_TEST_REPORT.md', '2026-07-01', 'D'),
('Duplicate file groups', 37767, 'groups', 'deduplication_report.md', '2026-07-03', 'D'),
('Duplicate files', 146519, 'files', 'deduplication_report.md', '2026-07-03', 'D'),
('Estimated wasted space', 5, 'GB', 'deduplication_report.md', '2026-07-03', 'D');

-- Table: obligation_rows
-- Role: Open obligations tracked by the framework
CREATE TABLE IF NOT EXISTS obligation_rows (
    row_id      INTEGER PRIMARY KEY,
    count       INTEGER NOT NULL,
    phase       TEXT,
    source_file TEXT NOT NULL
);

INSERT INTO obligation_rows (row_id, count, phase, source_file) VALUES
(1, 1105, 'Phase 7', 'FORWARD_PLAN.md');

-- Indexes
CREATE INDEX IF NOT EXISTS idx_drive_inventory_tag ON drive_inventory(tag);
CREATE INDEX IF NOT EXISTS idx_drive_inventory_source ON drive_inventory(source_file);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 100
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p100 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p100 (claim_ref, claim_text, status, source_file) VALUES
('100.1', 'Title: Closed Clusters = Crystals — Tile Cluster Closure', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p100 (claim_ref, claim_text, status, source_file) VALUES
('100.2', 'CrystalTile (343-cluster), SpectreTile (343-cluster), IsingTile — 343 tiles = depth 3 cluster', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p100 (claim_ref, claim_text, status, source_file) VALUES
('100.3', 'Space group P1 (triclinic) for 343-tile crystal cluster', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p100 (claim_ref, claim_text, status, source_file) VALUES
('100.4', 'Ising: J = κ — Tc from κ for crystal tile thermodynamics', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p100 (claim_ref, claim_text, status, source_file) VALUES
('100.5', 'Tile Concept: Spectre closed cluster at depth 3 (343 tiles) = fully closed crystalline object', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p100 (claim_ref, claim_text, status, source_file) VALUES
('100.6', 'Void Boundary ∂ = 0 at depth 3 (references Paper 022, Paper 070)', 'D', 'mapped_file_claims_report.md');
