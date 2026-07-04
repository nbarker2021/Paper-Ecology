-- ============================================================
-- Paper 13 — Unified Quark Face Transport
-- Domain: QCD Structure / SU(3) Weyl Closure
-- Cross-references: Paper 03 (D4 codec), Paper 30 (QCD color),
--                   Paper 41-43 (SU3 generations)
-- ============================================================

-- Table: quark_faces
-- Role: 6 chart faces corresponding to the 6 faces of the LCR cube.
--       These map to the 6 quark flavors.
CREATE TABLE IF NOT EXISTS quark_faces (
    face_id         INTEGER PRIMARY KEY CHECK (face_id BETWEEN 1 AND 6),
    face_name       TEXT NOT NULL,
    quark_flavor    TEXT NOT NULL,
    axis_class      INTEGER NOT NULL,
    sheet           INTEGER,
    color_charge    TEXT CHECK (color_charge IN ('red','green','blue','anti-red','anti-green','anti-blue')),
    su3_rep         TEXT NOT NULL DEFAULT '3' CHECK (su3_rep IN ('3','3bar','8','1')),
    weyl_depth      INTEGER DEFAULT 3       -- exact closure at depth 3
);

-- Table: su3_weyl_closure
-- Role: Exact SU(3) Weyl closure verification at depth 3
CREATE TABLE IF NOT EXISTS su3_weyl_closure (
    closure_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    depth           INTEGER NOT NULL DEFAULT 3,
    weyl_element    TEXT NOT NULL,
    face_id         INTEGER NOT NULL,
    action_result   TEXT NOT NULL,
    verified        INTEGER NOT NULL DEFAULT 1 CHECK (verified IN (0,1)),
    FOREIGN KEY (face_id) REFERENCES quark_faces(face_id)
);

-- Table: trace_idempotents
-- Role: 3 trace-2 idempotents = 3 fermion generations
CREATE TABLE IF NOT EXISTS trace_idempotents (
    idempotent_id   INTEGER PRIMARY KEY CHECK (idempotent_id BETWEEN 1 AND 3),
    generation      INTEGER NOT NULL,
    trace_value     INTEGER NOT NULL DEFAULT 2,
    associated_face_ids TEXT,              -- JSON array of face_ids
    mass_scale_gev  REAL
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_face_axis  ON quark_faces(axis_class);
CREATE INDEX IF NOT EXISTS idx_face_color ON quark_faces(color_charge);
CREATE INDEX IF NOT EXISTS idx_su3_depth  ON su3_weyl_closure(depth);

-- Seed data: 6 quark faces
INSERT INTO quark_faces (face_id, face_name, quark_flavor, axis_class, sheet, color_charge, su3_rep, weyl_depth) VALUES
(1, 'Face L',  'up',      1, 0, 'red',        '3', 3),
(2, 'Face C',  'down',    1, 1, 'green',      '3', 3),
(3, 'Face R',  'strange', 2, 0, 'blue',       '3', 3),
(4, 'Face LC', 'charm',   2, 1, 'anti-red',   '3bar', 3),
(5, 'Face LR', 'bottom',  3, 0, 'anti-green', '3bar', 3),
(6, 'Face CR', 'top',     3, 1, 'anti-blue',  '3bar', 3);

-- Seed data: 3 trace-2 idempotents = generations
INSERT INTO trace_idempotents (idempotent_id, generation, trace_value, associated_face_ids, mass_scale_gev) VALUES
(1, 1, 2, '[1,2]',   2.2),
(2, 2, 2, '[3,4]', 127.5),
(3, 3, 2, '[5,6]', 173.1);

-- === BATCH GROUP 1 CLAIMS (paper-13) ===
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (13, '13.1', 'M₃² = M₃ (anneal operator idempotency)', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (13, '13.2', 'Depth 3 = void boundary = light-cone bound', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (13, '13.3', 'Tree state count: 1+7+49+343 = 400', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (13, '13.4', 'Anneal distance ≤ 3', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (13, '13.5', 'κ derivation chain: Paper 013 → Paper 020 → Paper 030', 'D', 'DISTRIBUTED_DERIVATION_NETWORK.md');
