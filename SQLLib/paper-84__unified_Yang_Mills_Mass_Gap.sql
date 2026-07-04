-- ============================================================
-- Paper 84 — Unified Yang Mills Mass Gap
-- Domain: Yang-Mills Mass Gap / Clay Millennium
-- Cross-references: Paper 53 (Higgs mechanism), Paper 15 (mass residue)
-- ============================================================

-- Table: yang_mills_mass_gap
-- Role: Mass gap as VOA weight difference between vacuum and first excited state
CREATE TABLE IF NOT EXISTS yang_mills_mass_gap (
    gap_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    gauge_group     TEXT NOT NULL,
    vacuum_weight   INTEGER DEFAULT 0,
    first_excited_weight INTEGER,
    mass_gap_gev    REAL,
    proof_method    TEXT DEFAULT 'VOA weight assignment',
    structural_argument INTEGER DEFAULT 1,
    full_proof      INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_argument'
);

-- Seed data: Yang-Mills mass gap
INSERT INTO yang_mills_mass_gap (gauge_group, vacuum_weight, first_excited_weight, mass_gap_gev, status) VALUES
('SU(2)', 0, 1, 1.0, 'structural_argument'),
('SU(3)', 0, 1, 1.5, 'structural_argument');


-- ============================================================
-- NEW MAPPED CLAIMS: Paper 84
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p84 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p84 (claim_ref, claim_text, status, source_file) VALUES
('84.1', 'TITLE:** Paper 84 — Yang-Mills Mass Gap', 'I', 'UFT_CATALOG.md');
INSERT INTO mapped_claims_p84 (claim_ref, claim_text, status, source_file) VALUES
('84.2', '"title": "Paper 84 \u2014 Yang-Mills Mass Gap",', 'I', 'training_corpus_code_verifier_pairs.json');
INSERT INTO mapped_claims_p84 (claim_ref, claim_text, status, source_file) VALUES
('84.3', '"source_file": "D:\\PaperLib\\paper-84__unified_Yang-Mills_Mass_Gap.md"', 'I', 'training_corpus_code_verifier_pairs.json');
