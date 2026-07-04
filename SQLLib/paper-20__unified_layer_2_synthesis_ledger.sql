
-- Table: claims
-- Role: Claim ledger entries from mapped file reports
CREATE TABLE IF NOT EXISTS claims (
    claim_id        TEXT PRIMARY KEY,
    paper_num       INTEGER NOT NULL,
    claim_text      TEXT NOT NULL,
    tag             TEXT CHECK (tag IN ('D','I','X')),
    source_file     TEXT,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- ============================================================
-- Paper 20 — Unified Layer 2 Synthesis Ledger
-- Domain: Synthesis / Prediction Ledger
-- Cross-references: Paper 10 (receipt), Paper 19 (observer),
--                   Paper 78-79 (governance)
-- ============================================================

-- Table: synthesis_ledger
-- Role: Master synthesis ledger: 1,105+ obligation rows,
--       39 assemble/446 records.
CREATE TABLE IF NOT EXISTS synthesis_ledger (
    entry_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    obligation_id   INTEGER NOT NULL,
    paper_num       INTEGER NOT NULL,
    assembly_tag    TEXT,                  -- e.g., "assemble/39"
    record_type     TEXT CHECK (record_type IN ('prediction','theory_admission','obligation','receipt')),
    record_count    INTEGER DEFAULT 1,
    decade_tower    INTEGER CHECK (decade_tower BETWEEN 1 AND 10),
    family_id       INTEGER CHECK (family_id BETWEEN 1 AND 9),
    structural_consistency INTEGER NOT NULL DEFAULT 1 CHECK (structural_consistency IN (0,1)),
    explicit_unknown INTEGER NOT NULL DEFAULT 0 CHECK (explicit_unknown IN (0,1)),
    forbidden_reach INTEGER NOT NULL DEFAULT 0 CHECK (forbidden_reach IN (0,1)),
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- Table: ledger_statistics
-- Role: Aggregated statistics for the synthesis ledger
CREATE TABLE IF NOT EXISTS ledger_statistics (
    stat_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    total_obligations INTEGER NOT NULL,
    assemble_count    INTEGER NOT NULL,
    record_count      INTEGER NOT NULL,
    closed_count      INTEGER NOT NULL,
    open_count        INTEGER NOT NULL,
    staged_count      INTEGER NOT NULL,
    last_updated      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_synth_paper ON synthesis_ledger(paper_num);
CREATE INDEX IF NOT EXISTS idx_synth_tag   ON synthesis_ledger(assembly_tag);

-- Seed data: ledger statistics
INSERT INTO ledger_statistics (total_obligations, assemble_count, record_count, closed_count, open_count, staged_count) VALUES
(1105, 39, 446, 200, 800, 105);

-- Added claims from mapped file report for paper-020
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (20, 20.15, 'T.project(T) at depth 3 generates tile substitution tree: 1+7+49+343 = 400 tiles', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (20, 20.16, 'At depth 3, hyperpermutation reaches fixed point = void boundary', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (20, 20.17, 'T.project(T) = tile self-similarity at all scales', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (20, 20.18, 'Recursive Closure = T.project(T) — Tile Self-Substitution', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (20, 20.19, 'Tier: Recursive Closure (20-23)', 'I', '28_N_Dimensional_Game_Lattices.md');
