-- ============================================================
-- Paper 88 — Unified P vs NP Complexity Of Lattice Codes And Finite Presentation
-- Domain: P vs NP / Clay Millennium
-- Cross-references: Paper 75 (F4 universality), Paper 08 (lattice closure)
-- ============================================================

-- Table: p_vs_np
-- Role: P vs NP from F4 universality and lattice code chain.
CREATE TABLE IF NOT EXISTS p_vs_np (
    pnp_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'P ≠ NP',
    p_definition    TEXT DEFAULT 'Polynomial time on FLCR lattice',
    np_definition   TEXT DEFAULT 'Verifiable in polynomial time on FLCR lattice',
    f4_universality_link INTEGER DEFAULT 1,
    structural_approach INTEGER DEFAULT 1,
    full_proof      INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_approach'
);

-- Table: complexity_classes
-- Role: Complexity classes on the FLCR lattice
CREATE TABLE IF NOT EXISTS complexity_classes (
    class_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name      TEXT NOT NULL,
    definition      TEXT,
    lattice_model   TEXT DEFAULT 'FLCR'
);

-- Seed data: complexity classes
INSERT INTO complexity_classes (class_name, definition) VALUES
('P',   'Decidable in polynomial time on FLCR lattice'),
('NP',  'Verifiable in polynomial time on FLCR lattice'),
('FP4', 'F4-encodable finite-state problems');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 88
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p88 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p88 (claim_ref, claim_text, status, source_file) VALUES
('88.1', 'Paper 88 maps P vs NP (Cook-Levin theorem, oracle separations, bounded)', 'D', 'mapped_file_claims_report.md');
