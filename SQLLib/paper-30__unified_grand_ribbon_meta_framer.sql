
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
-- Paper 30 — Unified Grand Ribbon Meta Framer
-- Domain: Meta-Framing / Ribbon Structure
-- Cross-references: Paper 29 (Monster ceiling), Paper 80 (2-category),
--                   Paper 100 (capstone)
-- ============================================================

-- Table: meta_framer_ribbons
-- Role: Grand ribbon meta-framer structures
CREATE TABLE IF NOT EXISTS meta_framer_ribbons (
    ribbon_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    ribbon_name     TEXT NOT NULL,
    frame_count     INTEGER,
    cross_link_paper INTEGER,
    ribbon_type     TEXT CHECK (ribbon_type IN ('corpus','synthesis','governance','capstone')),
    FOREIGN KEY (cross_link_paper) REFERENCES papers(paper_num)
);

-- Table: ribbon_segments
-- Role: Segments within each meta-framer ribbon
CREATE TABLE IF NOT EXISTS ribbon_segments (
    segment_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    ribbon_id       INTEGER NOT NULL,
    paper_num       INTEGER NOT NULL,
    segment_order   INTEGER NOT NULL,
    FOREIGN KEY (ribbon_id) REFERENCES meta_framer_ribbons(ribbon_id),
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_ribbon_type ON meta_framer_ribbons(ribbon_type);

-- Added claims from mapped file report for paper-030
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (30, 30.9, 'κ = ln(φ)/16 = energy per tile edge', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (30, 30.10, 'All tile energies quantized in κ', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (30, 30.11, 'Energy κ = ln(φ)/16 — Tile Edge Energy Quantum', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (30, 30.12, 'Tier: Energy/Mass (30-33)', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (30, 30.13, 'Paper 013 (Anneal Bound ≤3) → Paper 020 (Recursive Closure) → Paper 030 (κ = ln(φ)/16)', 'I', 'DISTRIBUTED_DERIVATION_NETWORK.md');
