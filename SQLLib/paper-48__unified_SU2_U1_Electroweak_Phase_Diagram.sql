-- ============================================================
-- Paper 48 — Unified SU2 U1 Electroweak Phase Diagram
-- Domain: Phase Diagram / Lattice Regions
-- Cross-references: Paper 46-47 (electroweak), Paper 53 (Higgs mechanism)
-- ============================================================

-- Table: electroweak_phase_diagram
-- Role: Phase transitions as boundary repair, critical points as terminal addresses
CREATE TABLE IF NOT EXISTS electroweak_phase_diagram (
    phase_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    phase_name      TEXT NOT NULL,
    temperature_gev REAL,
    region_type     TEXT NOT NULL CHECK (region_type IN ('symmetric','broken','critical','crossover')),
    is_terminal     INTEGER DEFAULT 0 CHECK (is_terminal IN (0,1)),
    boundary_repair_id INTEGER
);

-- Table: phase_transitions
-- Role: Boundary repair at phase boundaries
CREATE TABLE IF NOT EXISTS phase_transitions (
    transition_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    from_phase      INTEGER NOT NULL,
    to_phase        INTEGER NOT NULL,
    transition_type TEXT CHECK (transition_type IN ('first_order','second_order','crossover')),
    critical_temp   REAL,
    FOREIGN KEY (from_phase) REFERENCES electroweak_phase_diagram(phase_id),
    FOREIGN KEY (to_phase) REFERENCES electroweak_phase_diagram(phase_id)
);

-- Seed data: phases
INSERT INTO electroweak_phase_diagram (phase_id, phase_name, temperature_gev, region_type, is_terminal) VALUES
(1, 'High-T symmetric',   1000.0, 'symmetric', 0),
(2, 'Electroweak broken',    0.0, 'broken',    0),
(3, 'Critical point',      159.5, 'critical',  1);

-- Mapped claims extraction

-- Table: mapped_claims_48
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (48, 1, '**FILE:** `paper_48.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (48, 2, '**TITLE:** Paper 48 — Mass Hierarchy and Yukawa: Mass Hierarchy as VOA Weight Ladder, Yukawa Couplings as D12 Action, Fermion Masses as Residue', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (48, 3, '**SUMMARY:** Mass hierarchy and Yukawa: mass hierarchy as VOA weight ladder, Yukawa couplings as D12 action, fermion masses as residue', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
