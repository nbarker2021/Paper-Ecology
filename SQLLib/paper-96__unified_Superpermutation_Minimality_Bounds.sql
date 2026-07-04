-- ============================================================
-- Paper 96 — Unified Superpermutation Minimality Bounds
-- Domain: Superpermutation / Application Band
-- Cross-references: Paper 77 (superpermutation closure)
-- ============================================================

-- Table: superpermutation_bounds
-- Role: Minimal length superpermutation bounds. Σk! conjecture.
CREATE TABLE IF NOT EXISTS superpermutation_bounds (
    n               INTEGER PRIMARY KEY,
    minimal_length  INTEGER,
    lower_bound     INTEGER,
    upper_bound     INTEGER,
    formula_sum_k_fact INTEGER,
    best_known      INTEGER,
    status          TEXT
);

-- Seed data
INSERT INTO superpermutation_bounds (n, minimal_length, lower_bound, upper_bound, formula_sum_k_fact, best_known, status) VALUES
(1, 1, 1, 1, 1, 1, 'proven'),
(2, 3, 3, 3, 3, 3, 'proven'),
(3, 9, 9, 9, 9, 9, 'proven'),
(4, 33, 33, 33, 33, 33, 'proven'),
(5, 153, 153, 153, 153, 153, 'proven'),
(6, 872, 873, 1172, 873, 872, 'open'),
(7, 5906, 5913, 7880, 5913, 5906, 'open');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 96
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p96 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p96 (claim_ref, claim_text, status, source_file) VALUES
('96.1', 'The translation is the foundation of the metamaterials physics (Paper 96) and the applied forge validation (Paper 95)', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p96 (claim_ref, claim_text, status, source_file) VALUES
('96.2', '============================================================', 'I', 'mapped_file_claims_report.md');
