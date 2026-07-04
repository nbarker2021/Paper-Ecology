-- ============================================================
-- Paper 58 — Unified QCD Phenomenology 2 Parton Distributions
-- Domain: Parton Distributions / PDFs
-- Cross-references: Paper 57 (hadron spectroscopy), Paper 59 (jets)
-- ============================================================

-- Table: parton_distributions
-- Role: PDFs derived from FLCR substrate — structural, not fitted.
CREATE TABLE IF NOT EXISTS parton_distributions (
    pdf_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    hadron_name     TEXT NOT NULL,
    parton_type     TEXT NOT NULL CHECK (parton_type IN ('up','down','strange','charm','gluon','anti-up','anti-down')),
    x_min           REAL NOT NULL,
    x_max           REAL NOT NULL,
    q2_gev2         REAL NOT NULL,
    pdf_value       REAL,
    flcr_derived    INTEGER DEFAULT 1
);

-- Table: pdf_moments
-- Role: Moments of PDFs for sum rules
CREATE TABLE IF NOT EXISTS pdf_moments (
    moment_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    hadron_name     TEXT NOT NULL,
    moment_order    INTEGER NOT NULL,
    moment_value    REAL,
    sum_rule        TEXT                   -- e.g., 'momentum_sum_rule'
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_pdf_hadron ON parton_distributions(hadron_name);
CREATE INDEX IF NOT EXISTS idx_pdf_parton ON parton_distributions(parton_type);

-- Mapped claims extraction

-- Table: mapped_claims_58
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (58, 1, '**FILE:** `paper_58.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (58, 2, '**TITLE:** Paper 58 — QCD Phenomenology 2: Parton Distributions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (58, 3, '**SUMMARY:** QCD phenomenology 2: parton distributions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
