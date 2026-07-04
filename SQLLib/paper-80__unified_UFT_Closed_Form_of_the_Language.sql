-- ============================================================
-- Paper 80 — Unified UFT Closed Form Of The Language
-- Domain: 2-Category ℒ / Capstone Foundation
-- Cross-references: ALL PAPERS (synthesizes entire series)
-- ============================================================

-- Table: category_l_objects
-- Role: 8 objects of 2-category ℒ = typed 5-tuples (L,C,R,Σ,∂)
CREATE TABLE IF NOT EXISTS category_l_objects (
    object_id       INTEGER PRIMARY KEY CHECK (object_id BETWEEN 1 AND 8),
    object_name     TEXT NOT NULL,
    tuple_form      TEXT NOT NULL,         -- e.g., "(L, C, R, Σ, ∂)"
    lcr_state_id    INTEGER,
    FOREIGN KEY (lcr_state_id) REFERENCES lcr_states(state_id)
);

-- Table: category_l_1morphisms
-- Role: 8 1-morphisms = admissible operations
CREATE TABLE IF NOT EXISTS category_l_1morphisms (
    morph_id        INTEGER PRIMARY KEY CHECK (morph_id BETWEEN 1 AND 8),
    morph_name      TEXT NOT NULL,
    op_symbol       TEXT,
    source_object   INTEGER NOT NULL,
    target_object   INTEGER NOT NULL,
    FOREIGN KEY (source_object) REFERENCES category_l_objects(object_id),
    FOREIGN KEY (target_object) REFERENCES category_l_objects(object_id)
);

-- Table: category_l_2morphisms
-- Role: 7 2-morphisms = claim-lane promotions
CREATE TABLE IF NOT EXISTS category_l_2morphisms (
    two_morph_id    INTEGER PRIMARY KEY CHECK (two_morph_id BETWEEN 1 AND 7),
    two_morph_name  TEXT NOT NULL,
    lane_promoted_from INTEGER,
    lane_promoted_to   INTEGER,
    FOREIGN KEY (lane_promoted_from) REFERENCES claim_lanes(lane_id),
    FOREIGN KEY (lane_promoted_to) REFERENCES claim_lanes(lane_id)
);

-- Table: generating_relations
-- Role: 26 generating relations of 2-category ℒ
CREATE TABLE IF NOT EXISTS generating_relations (
    relation_id     INTEGER PRIMARY KEY CHECK (relation_id BETWEEN 1 AND 26),
    relation_name   TEXT NOT NULL,
    relation_expr   TEXT NOT NULL,
    lhs_morph       INTEGER,
    rhs_morph       INTEGER
);

-- Seed data: 8 objects
INSERT INTO category_l_objects (object_id, object_name, tuple_form, lcr_state_id) VALUES
(1, 'Vacuum object', '(∅, ∅, ∅, ∅, ∅)', 0),
(2, 'L object',      '(L, ∅, ∅, Σ, ∂)', 1),
(3, 'C object',      '(∅, C, ∅, Σ, ∂)', 2),
(4, 'R object',      '(∅, ∅, R, Σ, ∂)', 3),
(5, 'LC object',     '(L, C, ∅, Σ, ∂)', 4),
(6, 'LR object',     '(L, ∅, R, Σ, ∂)', 5),
(7, 'CR object',     '(∅, C, R, Σ, ∂)', 6),
(8, 'LCR object',    '(L, C, R, Σ, ∂)', 7);

-- Seed data: 8 1-morphisms
INSERT INTO category_l_1morphisms (morph_id, morph_name, op_symbol, source_object, target_object) VALUES
(1, 'Lookup',   'λ', 1, 2),
(2, 'Repair',   'ρ', 2, 5),
(3, 'Fold',     'φ', 5, 8),
(4, 'Terminal', 'τ', 8, 1),
(5, 'Ledger',   'Λ', 3, 7),
(6, 'Window',   'ω', 4, 6),
(7, 'Bridge',   'β', 6, 3),
(8, 'Admit',    'α', 7, 8);

-- Seed data: 7 2-morphisms (claim-lane promotions)
INSERT INTO category_l_2morphisms (two_morph_id, two_morph_name, lane_promoted_from, lane_promoted_to) VALUES
(1, 'Structural → Physical',    1, 2),
(2, 'Physical → Mathematical',  2, 3),
(3, 'Mathematical → Computational', 3, 4),
(4, 'Computational → Empirical',    4, 5),
(5, 'Empirical → Governance',       5, 6),
(6, 'Governance → Residue',         6, 7),
(7, 'Residue → Closed',             7, 1);
