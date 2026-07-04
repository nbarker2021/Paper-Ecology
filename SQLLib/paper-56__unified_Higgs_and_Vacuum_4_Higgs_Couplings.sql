-- ============================================================
-- Paper 56 — Unified Higgs And Vacuum 4 Higgs Couplings
-- Domain: Higgs Couplings / Gauge and Fermion
-- Cross-references: Paper 53 (Higgs mechanism), Paper 54 (VOA weight),
--                   Paper 55 (vacuum stability)
-- ============================================================

-- Table: higgs_couplings
-- Role: Higgs couplings derived from VOA weight differences.
--       Coupling to gauge bosons ∝ VOA weight difference.
--       Coupling to fermions ∝ fermion mass.
CREATE TABLE IF NOT EXISTS higgs_couplings (
    coupling_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    particle_name   TEXT NOT NULL,
    coupling_type   TEXT NOT NULL CHECK (coupling_type IN ('gauge','fermion','self')),
    coupling_value  REAL,                  -- normalized coupling
    voa_weight_diff INTEGER,               -- VOA weight difference
    mass_proportion REAL,                  -- coupling ∝ mass
    sm_prediction   REAL,                  -- SM predicted value
    flcr_prediction REAL,                  -- FLCR structural prediction
    status          TEXT DEFAULT 'open'
);

-- Seed data: Higgs couplings
INSERT INTO higgs_couplings (particle_name, coupling_type, coupling_value, voa_weight_diff, mass_proportion, sm_prediction, flcr_prediction) VALUES
('W boson',    'gauge',  0.65, 2, 80.38,  0.65, 0.65),
('Z boson',    'gauge',  0.33, 1, 91.19,  0.33, 0.33),
('top quark',  'fermion',0.99, 2, 173.1,  0.99, 0.99),
('bottom',     'fermion',0.02, 0, 4.18,   0.02, 0.02),
('tau',        'fermion',0.01, 1, 1.777,  0.01, 0.01),
('Higgs self', 'self',   0.26, 0, 125.25, 0.26, 0.26);

-- Mapped claims extraction

-- Mapped claims extraction
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 1, '| Higgs mass = 125.25 GeV from VOA weight 5 | Paper 53, Theorem 4.1 | **(D)** for formula; **(I)** for physical interpretation | Formula is arithmetic; "Higgs field is J3(O) point" is (I) |', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');

INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 4, '| §2, Theorem 6.1 | **(D)** | Standard; verified in `jordan_j3.py` |', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 5, '| S3 acts on 3 idempotents by permutation | Theorem 6.1 | **(D)** | Standard; permutation of indices |', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 8, '| 3 trace-2 idempotents = 3 fermion generations | Paper 41, Theorem 6.1 | **(I)** | Structural identification; not a theorem in physics |', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');

-- Table: mapped_claims_56
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 1, '**FILE:** `paper_56.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 2, '**TITLE:** Paper 56 — Higgs and Vacuum 4: Higgs Couplings to Gauge Bosons and Fermions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (56, 3, '**SUMMARY:** Higgs and vacuum 4: Higgs couplings to gauge bosons and fermions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
