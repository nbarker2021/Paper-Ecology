-- ============================================================
-- Paper 97 — Unified Electron Hole Exciton Accounting For Open Math
-- Domain: EHX / Open Math Bookkeeping
-- Cross-references: Paper 35 (EHX accounting), Paper 87 (Hodge)
-- ============================================================

-- Table: ehx_open_math
-- Role: Bookkeeping of exceptional, Hodge, extended structures
CREATE TABLE IF NOT EXISTS ehx_open_math (
    entry_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    structure_type  TEXT NOT NULL CHECK (structure_type IN ('exceptional','hodge','extended')),
    structure_name  TEXT NOT NULL,
    accounting_status TEXT DEFAULT 'tracked',
    open_math_link  TEXT
);

-- Seed data: EHX structures
INSERT INTO ehx_open_math (structure_type, structure_name, accounting_status) VALUES
('exceptional', 'Monster VOA',     'tracked'),
('exceptional', 'Leech lattice',   'tracked'),
('hodge',       'Hodge decomposition', 'tracked'),
('extended',    '2-category L',    'tracked');


-- ============================================================
-- NEW MAPPED CLAIMS: Paper 97
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p97 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p97 (claim_ref, claim_text, status, source_file) VALUES
('97.1', 'Title: Unified Paper 97 — Electron-Hole-Exciton Accounting for Open Math (Deep Dive)', 'I', 'training_corpus_full.txt');
INSERT INTO mapped_claims_p97 (claim_ref, claim_text, status, source_file) VALUES
('97.2', 'TITLE:** Paper 97 — EHX Accounting', 'I', 'UFT_CATALOG.md');
