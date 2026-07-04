-- ============================================================
-- Paper 47 — Unified SU2 U1 VA Weak Interaction
-- Domain: Weak Interaction / V-A Structure
-- Cross-references: Paper 45-46 (electroweak), Paper 52 (PMNS)
-- ============================================================

-- Table: va_weak_interaction
-- Role: V-A as D4 sheet selection, weak force as boundary repair,
--       parity violation as Arf mismatch.
CREATE TABLE IF NOT EXISTS va_weak_interaction (
    interaction_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    process_name    TEXT NOT NULL,
    sheet_selected  INTEGER,               -- 0 or 1 (D4 sheet)
    parity_violation INTEGER NOT NULL DEFAULT 1 CHECK (parity_violation IN (0,1)),
    arf_mismatch    REAL,                  -- Arf invariant difference
    process_type    TEXT CHECK (process_type IN ('beta_decay','muon_decay','pion_decay','neutral_current'))
);

-- Seed data: weak interaction processes
INSERT INTO va_weak_interaction (process_name, sheet_selected, parity_violation, arf_mismatch, process_type) VALUES
('Neutron beta decay',     0, 1, 1.0, 'beta_decay'),
('Muon decay',             1, 1, 1.0, 'muon_decay'),
('Pion decay',             0, 1, 1.0, 'pion_decay'),
('Neutral current (Z0)',   NULL, 0, 0.0, 'neutral_current');

-- Mapped claims extraction

-- Table: mapped_claims_47
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (47, 1, '**FILE:** `paper_47.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (47, 2, '**TITLE:** Paper 47 — Electroweak Phase Diagram: Phase Transitions as Boundary Repair, Critical Points as Terminal Addresses, Phases as Lattice Regions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (47, 3, '**SUMMARY:** Electroweak phase diagram: phase transitions as boundary repair, critical points as terminal addresses, phases as lattice regions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
