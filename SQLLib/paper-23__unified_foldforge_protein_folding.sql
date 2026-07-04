
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
-- Paper 23 — Unified Foldforge Protein Folding
-- Domain: Biophysics / Protein Folding
-- Cross-references: Paper 21 (forge systems), Paper 22 (materials)
-- ============================================================

-- Table: foldforge_proteins
-- Role: Protein descriptors and fold-facing kernel records
CREATE TABLE IF NOT EXISTS foldforge_proteins (
    protein_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    protein_name    TEXT NOT NULL,
    pdb_id          TEXT,
    sequence        TEXT,                  -- amino acid sequence
    fold_class      TEXT CHECK (fold_class IN ('alpha','beta','alpha+beta','irregular')),
    forge_id        INTEGER,
    fold_energy     REAL,                  -- predicted folding energy
    FOREIGN KEY (forge_id) REFERENCES forge_systems(forge_id)
);

-- Table: foldforge_facing
-- Role: Fold-facing kernel — orientation of fold relative to carrier
CREATE TABLE IF NOT EXISTS foldforge_facing (
    facing_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    protein_id      INTEGER NOT NULL,
    face_orientation TEXT,                 -- LCR face label
    facing_energy   REAL,
    stability_score REAL,
    FOREIGN KEY (protein_id) REFERENCES foldforge_proteins(protein_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_protein_name ON foldforge_proteins(protein_name);
CREATE INDEX IF NOT EXISTS idx_protein_fold ON foldforge_proteins(fold_class);

-- Added claims from mapped file report for paper-023
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (23, 23.12, 'Light-cone = recursive self-closure of tile substitution at depth 3 = void boundary', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (23, 23.13, 'Light-Cone Closure = Recursive Self-Closure — Tile Void Boundary', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (23, 23.14, 'Tier: Recursive Closure (20-23)', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (23, 23.15, 'SpectreTile, CrystalTile (343 void boundary), TarpitTile', 'D', '28_N_Dimensional_Game_Lattices.md');
