-- ============================================================
-- Paper 98 — Unified Reasoned Reapplication Of Standard Formalism
-- Domain: Reapplication / Lattice Code Chain Mapping
-- Cross-references: ALL PAPERS (meta-reapplication)
-- ============================================================

-- Table: reasoned_reapplication
-- Role: FLCR substrate reapplied to new problems via lattice code chain
CREATE TABLE IF NOT EXISTS reasoned_reapplication (
    reapplication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    target_problem   TEXT NOT NULL,
    lattice_code_chain TEXT,
    magic_square_used INTEGER DEFAULT 1,
    mapping_valid    INTEGER DEFAULT 0,
    application_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: reapplication_registry
-- Role: Registry of all reapplications
CREATE TABLE IF NOT EXISTS reapplication_registry (
    registry_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    reapplication_id INTEGER NOT NULL,
    source_paper    INTEGER,
    target_domain   TEXT,
    result_status   TEXT DEFAULT 'open'
);

-- Seed data
INSERT INTO reasoned_reapplication (target_problem, lattice_code_chain, mapping_valid) VALUES
('Protein folding', '1->3->7->8->24->72', 1),
('Materials design', '1->3->7->8', 1),
('Game theory', '1->3', 1);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 98
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p98 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p98 (claim_ref, claim_text, status, source_file) VALUES
('98.1', 'The translation is the foundation of the plasma transport (Paper 25), the SPINOR observation (Paper 98), and the carrier threshold event', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p98 (claim_ref, claim_text, status, source_file) VALUES
('98.2', '19 | Reasoned reapplication as physical-science analog of scaffolded ATP | Paper 98 / NP-13 | §2 (reapplication validated by AI provers) | Supp F §4.1', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p98 (claim_ref, claim_text, status, source_file) VALUES
('98.3', '**P19** | **Add AI ATP citations to Paper 98 / NP-13**: Cite Aletheia, LEGO-Prover, Goedel-Prover-V2, DeepSeek-Prover-V2 as validation of reasoned reapplication | Paper 98 / NP-13 Author | 2026-07-15 | Feng et al', 'I', 'mapped_file_claims_report.md');
