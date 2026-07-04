-- ============================================================
-- Paper 91 — Unified Niemeier Glue Leech Invariants Gamma72 Landing
-- Domain: Niemeier Glue / Γ72 / Leech
-- Cross-references: Paper 08 (lattice closure), Paper 17 (E6-E8),
--                   Paper 18 (moonshine)
-- ============================================================

-- Table: niemeier_glue
-- Role: Niemeier glue Γ72 unifies 72 E6 roots.
--       Leech lattice is closure of Niemeier glue.
CREATE TABLE IF NOT EXISTS niemeier_glue (
    glue_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    glue_name       TEXT NOT NULL,
    root_count      INTEGER,
    glue_group      TEXT,
    leech_closure   INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'open'
);

-- Table: gamma72_landing
-- Role: Γ72 landing process — 72 E6 roots glued into Leech
CREATE TABLE IF NOT EXISTS gamma72_landing (
    landing_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    e6_root_index   INTEGER,
    glue_vector     TEXT,                  -- glue vector
    leech_target    TEXT,                  -- target in Leech
    landed          INTEGER DEFAULT 0
);

-- Table: leech_invariants
-- Role: Invariants of the Leech lattice
CREATE TABLE IF NOT EXISTS leech_invariants (
    invariant_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    invariant_name  TEXT NOT NULL,
    invariant_value TEXT,
    description     TEXT
);

-- Seed data: Niemeier glue
INSERT INTO niemeier_glue (glue_name, root_count, glue_group, status) VALUES
('Gamma72', 72, 'E6^12', 'open');

-- Seed data: Leech invariants
INSERT INTO leech_invariants (invariant_name, invariant_value, description) VALUES
('kissing_number', '196560', 'Number of minimal vectors'),
('Aut(Leech)', 'Co_0', 'Conway group order ~8e18'),
('min_norm', '4', 'Minimum norm of non-zero vectors');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 91
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p91 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p91 (claim_ref, claim_text, status, source_file) VALUES
('91.1', 'The proof of the Γ72 landing is the NP-02 paper (Paper 91)', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p91 (claim_ref, claim_text, status, source_file) VALUES
('91.2', '*Next binding action:* Paper 91 must address the Γ72 landing through the magic square', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p91 (claim_ref, claim_text, status, source_file) VALUES
('91.3', 'Theorem 15.8 (The magic square is the tropical Grassmannian sequence). The magic square entries (R,O)=F4, (C,O)=E6, (H,O)=E7, (O,O)=E8 correspond to the tropical Grassmannian sequence:', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p91 (claim_ref, claim_text, status, source_file) VALUES
('91.4', 'Gr(3,7) ↔ E6 (exceptional, Paper 91)', 'I', 'mapped_file_claims_report.md');
