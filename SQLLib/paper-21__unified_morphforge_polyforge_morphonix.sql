
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
-- Paper 21 — Unified Morphforge Polyforge Morphonix
-- Domain: Forge Systems / SK-Combinators
-- Cross-references: Paper 20 (synthesis), Paper 22 (metaforge),
--                   Paper 24 (knightforge)
-- ============================================================

-- Table: forge_systems
-- Role: Registry of all Forge systems and their capabilities
CREATE TABLE IF NOT EXISTS forge_systems (
    forge_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    forge_name      TEXT NOT NULL UNIQUE,
    forge_type      TEXT NOT NULL CHECK (forge_type IN ('MorphForge','MetaForge','FoldForge','KnightForge','PolyForge')),
    substrate       TEXT NOT NULL,         -- e.g., 'SK-combinators', 'materials lattice'
    combinator_set  TEXT,                  -- for MorphForge: S, K, I
    status          TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','deprecated','experimental'))
);

-- Table: morphforge_terms
-- Role: SK-combinator terms and their normal forms
CREATE TABLE IF NOT EXISTS morphforge_terms (
    term_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    term_expr       TEXT NOT NULL,
    normal_form     TEXT,
    term_size       INTEGER,
    reduction_steps INTEGER,
    forge_id        INTEGER NOT NULL,
    FOREIGN KEY (forge_id) REFERENCES forge_systems(forge_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_forge_type ON forge_systems(forge_type);
CREATE INDEX IF NOT EXISTS idx_morph_term ON morphforge_terms(term_expr);

-- Seed data: Forge systems
INSERT INTO forge_systems (forge_name, forge_type, substrate, combinator_set, status) VALUES
('MorphForge-Core',  'MorphForge',  'SK-combinators',     'S,K,I',    'active'),
('MetaForge-Mat',    'MetaForge',   'materials lattice',  NULL,       'active'),
('FoldForge-Prot',   'FoldForge',   'protein backbone',   NULL,       'active'),
('KnightForge-Chess','KnightForge', 'n-dim chess lattice',NULL,       'active'),
('PolyForge-Gen',    'PolyForge',   'polymer graph',      NULL,       'experimental');

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: historical_morphon
-- Role: Historical morphon visualization findings
CREATE TABLE IF NOT EXISTS historical_morphon (
    morphon_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL
);

INSERT INTO historical_morphon (claim_text, source_file, source_date) VALUES
('composed_morphon_v3.py (324.0 KB) contains E8 visualization, Leech integration, protein basins, drug interactions', 'historical_files_addressed.md', '2026-07-03'),
('9 protein structure basin classes: alpha-Helix Right, beta-Sheet Extended, Left-Handed Helix, beta-Turn Type I, beta-Turn Type II, Polyproline II, 3_10-Helix, pi-Helix, Transition/Suspended', 'historical_files_addressed.md', '2026-07-03'),
('9 drug interaction classes: Potentiation, Additive, Synergistic, Partial Antagonism, Competitive, Antagonistic, Paradoxical, Pharmacokinetic, Neutral/Suspended', 'historical_files_addressed.md', '2026-07-03');

CREATE INDEX IF NOT EXISTS idx_historical_morphon_source ON historical_morphon(source_file);

-- Added claims from mapped file report for paper-021
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (21, 21.16, 'Each spectre tile substitution produces 7 children via 7 S3 non-identity sequences', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (21, 21.17, '7 paths = 7 correction paths at chiral doublet', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (21, 21.18, '1+7+49+343 = 400 states at depth 3', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (21, 21.19, 'Each path = 1 child tile', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (21, 21.20, 'Depth 3 = void boundary = 343', 'D', '28_N_Dimensional_Game_Lattices.md');
