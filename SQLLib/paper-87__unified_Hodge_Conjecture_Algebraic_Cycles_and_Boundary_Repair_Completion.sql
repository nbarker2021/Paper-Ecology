-- ============================================================
-- Paper 87 — Unified Hodge Conjecture Algebraic Cycles And Boundary Repair Completion
-- Domain: Hodge Conjecture / Clay Millennium
-- Cross-references: Paper 08 (lattice closure), Paper 17 (E6-E8)
-- ============================================================

-- Table: hodge_conjecture
-- Role: Hodge decomposition as lattice closure of differential forms.
--       Conjecture ↔ lattice closure is complete.
CREATE TABLE IF NOT EXISTS hodge_conjecture (
    hodge_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'Every Hodge class is a rational linear combination of algebraic cycle classes',
    dimension       INTEGER,
    hodge_decomposition TEXT,
    lattice_closure_complete INTEGER DEFAULT 0,
    structural_approach INTEGER DEFAULT 1,
    full_proof      INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_approach'
);

-- Table: algebraic_cycles
-- Role: Algebraic cycles as lattice elements
CREATE TABLE IF NOT EXISTS algebraic_cycles (
    cycle_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    cycle_name      TEXT NOT NULL,
    codimension     INTEGER,
    hodge_type      TEXT,
    is_rational     INTEGER DEFAULT 1
);

-- Seed data
INSERT INTO hodge_conjecture (dimension, status) VALUES
(2, 'structural_approach');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 87
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p87 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p87 (claim_ref, claim_text, status, source_file) VALUES
('87.1', 'Paper 87 maps the Hodge conjecture (Lefschetz (1,1) theorem, bounded)', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p87 (claim_ref, claim_text, status, source_file) VALUES
('87.2', 'C-87-01 | Hodge conjecture is open | Paper 87, §2 | **(D)** | Algebraic geometry | Clay Mathematics Institute | —', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p87 (claim_ref, claim_text, status, source_file) VALUES
('87.3', 'C-87-02 | **Hodge from tropical Grassmannian cohomology** | Paper 87, §3 | **(I)** | Algebraic geometry | Structural analogy | Prove tropical Hodge theorem', 'D', 'mapped_file_claims_report.md');
