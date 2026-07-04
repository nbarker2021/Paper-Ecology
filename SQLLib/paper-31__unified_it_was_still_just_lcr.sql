
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
-- Paper 31 — Unified It Was Still Just Lcr
-- Domain: LCR Core / Kernel Verification
-- Cross-references: Paper 01 (LCR kernel), Paper 32 (supervisor cursor)
-- ============================================================

-- Table: lcr_core_verification
-- Role: Verification that all higher structures reduce to LCR kernel
CREATE TABLE IF NOT EXISTS lcr_core_verification (
    verification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_num       INTEGER NOT NULL,
    reduction_path  TEXT NOT NULL,         -- e.g., "E8 → F4 → D4 → LCR"
    reduction_valid INTEGER NOT NULL DEFAULT 1 CHECK (reduction_valid IN (0,1)),
    depth_verified  INTEGER DEFAULT 4096,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- Table: lcr_invariant_checks
-- Role: Invariant checks that survive all reductions
CREATE TABLE IF NOT EXISTS lcr_invariant_checks (
    invariant_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    invariant_name  TEXT NOT NULL,
    invariant_value TEXT,
    checked_at_depth INTEGER DEFAULT 4096,
    status          TEXT NOT NULL DEFAULT 'verified'
);

-- Seed data: core verification paths
INSERT INTO lcr_core_verification (paper_num, reduction_path, reduction_valid, depth_verified) VALUES
(3,  'D4/J3(O) → LCR',          1, 4096),
(8,  'Leech → E8 → F4 → D4 → LCR', 1, 4096),
(17, 'E6-E8 tower → D4 → LCR',  1, 4096),
(29, 'Monster VOA → E8 → LCR',  1, 256);

-- Added claims from mapped file report for paper-031
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (31, 31.7, 'Z(q) = 2q⁰ + 6q⁵: 2 true vacua (weight 0) = fixed-point tiles (L=R), 6 excited (weight 5) = off-diagonal tiles', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (31, 31.8, 'Complete energy spectrum of all tile states', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (31, 31.9, 'Mass = bonded interactions × κ', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (31, 31.10, 'VOA Partition Z(q) = 2q⁰ + 6q⁵ — Tile State Energy Classification', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (31, 31.11, 'Tier: Energy/Mass (30-33)', 'I', '25_Energetic_Traversal_Maps.md');
