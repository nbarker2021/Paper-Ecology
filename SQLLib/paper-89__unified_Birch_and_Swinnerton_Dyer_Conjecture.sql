-- ============================================================
-- Paper 89 — Unified Birch And Swinnerton Dyer Conjecture
-- Domain: BSD / Clay Millennium
-- Cross-references: Paper 15 (VOA weights), Paper 18 (moonshine)
-- ============================================================

-- Table: bsd_conjecture
-- Role: BSD from VOA weights. L-function = generating function of VOA weights.
CREATE TABLE IF NOT EXISTS bsd_conjecture (
    bsd_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'rank(E(Q)) = order_{s=1} L(E,s)',
    elliptic_curve  TEXT,
    voa_weight_link INTEGER DEFAULT 1,
    l_function      TEXT,                  -- generating function
    rank            INTEGER,
    analytic_rank   INTEGER,
    structural_approach INTEGER DEFAULT 1,
    full_proof      INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_approach'
);

-- Table: l_function_coefficients
-- Role: Coefficients from VOA weights
CREATE TABLE IF NOT EXISTS l_function_coefficients (
    coeff_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    n               INTEGER NOT NULL,
    a_n             INTEGER,               -- L-function coefficient
    voa_weight_link INTEGER
);

-- Seed data
INSERT INTO bsd_conjecture (elliptic_curve, rank, analytic_rank, status) VALUES
('y^2 = x^3 - x', 0, 0, 'structural_approach');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 89
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p89 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p89 (claim_ref, claim_text, status, source_file) VALUES
('89.1', 'Paper 89 maps the BSD conjecture (rank 0 and 1 theorems, bounded)', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p89 (claim_ref, claim_text, status, source_file) VALUES
('89.2', 'C-89-01 | Birch and Swinnerton-Dyer conjecture is open | Paper 89, §2 | **(D)** | Number theory | Clay Mathematics Institute | —', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p89 (claim_ref, claim_text, status, source_file) VALUES
('89.3', 'C-89-02 | **BSD from VOA L-function** | Paper 89, §3 | **(I)** | Number theory | Structural analogy | Prove VOA L-function = elliptic curve L-function', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p89 (claim_ref, claim_text, status, source_file) VALUES
('89.4', 'C-89-03 | Yang-Mills mass gap is open | Paper 89, §4 | **(D)** | QFT | Clay Mathematics Institute | —', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p89 (claim_ref, claim_text, status, source_file) VALUES
('89.5', 'C-89-04 | **Mass gap from VOA weight gap** | Paper 89, §5 | **(I)** | QFT | Structural analogy | Prove mass gap = VOA weight gap', 'I', 'mapped_file_claims_report.md');
