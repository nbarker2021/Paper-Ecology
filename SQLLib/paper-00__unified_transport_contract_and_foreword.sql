-- ============================================================
-- Paper 00 — Unified Transport Contract And Foreword
-- Domain: Grounding / Foundational Axioms
-- ============================================================

-- Table: theorems
-- Role: Registry of all formally stated theorems, axioms, and lemmas
--       that ground the 100-paper series.
CREATE TABLE IF NOT EXISTS theorems (
    theorem_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL UNIQUE,
    theorem_type    TEXT NOT NULL CHECK (theorem_type IN ('axiom','lemma','theorem','corollary','conjecture')),
    author          TEXT,
    year            INTEGER,
    citation        TEXT,
    role            TEXT NOT NULL, -- e.g., 'grounding', 'closure', 'bridge'
    statement       TEXT NOT NULL,
    proof_status    TEXT NOT NULL DEFAULT 'open' CHECK (proof_status IN ('proven','open','disproven','deferred')),
    paper_ref       INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (paper_ref) REFERENCES papers(paper_num)
);

-- Table: papers
-- Role: Master registry of all 101 papers in the series
CREATE TABLE IF NOT EXISTS papers (
    paper_num       INTEGER PRIMARY KEY,
    title           TEXT NOT NULL,
    domain          TEXT NOT NULL,
    band            TEXT NOT NULL CHECK (band IN ('A','B','Bp','C')),
    status          TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft','review','published','deprecated')),
    word_count      INTEGER,
    key_claims      INTEGER DEFAULT 0
);

-- Table: irreducible_gaps
-- Role: Tracks the 8 irreducible gaps identified in Paper 00
CREATE TABLE IF NOT EXISTS irreducible_gaps (
    gap_id          INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    description     TEXT NOT NULL,
    target_paper    INTEGER,
    status          TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open','closed','partial')),
    FOREIGN KEY (target_paper) REFERENCES papers(paper_num)
);

-- Table: claim_lanes
-- Role: The 7 claim lanes for classifying all claims
CREATE TABLE IF NOT EXISTS claim_lanes (
    lane_id         INTEGER PRIMARY KEY,
    lane_name       TEXT NOT NULL UNIQUE,
    description     TEXT NOT NULL,
    admissibility_criterion TEXT
);

-- Table: claim_types
-- Role: D/I/X classification for every claim
CREATE TABLE IF NOT EXISTS claim_types (
    type_code       TEXT PRIMARY KEY CHECK (type_code IN ('D','I','X')),
    type_name       TEXT NOT NULL,
    description     TEXT NOT NULL
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_theorems_type ON theorems(theorem_type);
CREATE INDEX IF NOT EXISTS idx_theorems_role  ON theorems(role);
CREATE INDEX IF NOT EXISTS idx_papers_band    ON papers(band);
CREATE INDEX IF NOT EXISTS idx_gaps_status    ON irreducible_gaps(status);

-- Seed data: 8 irreducible gaps
INSERT INTO irreducible_gaps (gap_id, name, description, target_paper, status) VALUES
(1, 'CKM Numerics', 'Exact derivation of CKM matrix elements from lattice action', 50, 'partial'),
(2, 'Particle VOA Weights', 'Complete VOA weight assignment for all SM particles', 16, 'partial'),
(3, 'Higgs Mass Derivation', 'Structural derivation of Higgs mass 125.25 GeV', 16, 'partial'),
(4, 'Gamma72 Landing', 'Explicit Niemeier glue construction for Gamma72', 91, 'open'),
(5, 'Full Moonshine Identification', 'Complete Monster VOA to SM particle identification', 18, 'partial'),
(6, 'Unbounded Rule 30 Non-Periodicity', 'Proof of non-periodicity for unbounded Rule 30', 81, 'open'),
(7, 'GR EFE Identity', 'Einstein Field Equation from repair curvature', 65, 'open'),
(8, 'Cosmogenesis', 'Origin of the Big Bang from FLCR substrate', 100, 'open');

-- Seed data: 7 claim lanes
INSERT INTO claim_lanes (lane_id, lane_name, description, admissibility_criterion) VALUES
(1, 'Structural', 'Claims about algebraic and lattice structure', 'Verifiable by computation'),
(2, 'Physical', 'Claims mapping structure to physics observables', 'Requires external calibration'),
(3, 'Mathematical', 'Claims about proved theorems and conjectures', 'Requires formal proof'),
(4, 'Computational', 'Claims about algorithms and complexity', 'Requires implementation and benchmark'),
(5, 'Empirical', 'Claims backed by measurement data', 'Requires reproducible experiment'),
(6, 'Governance', 'Claims about process and evidence standards', 'Requires audit trail'),
(7, 'Residue', 'Open obligations and deferred claims', 'Explicitly named as open');

-- Seed data: claim types
INSERT INTO claim_types (type_code, type_name, description) VALUES
('D', 'Data-backed', 'Claim supported by direct computation, measurement, or citation'),
('I', 'Interpretation', 'Claim that is a plausible inference from D-claims'),
('X', 'Fabrication/Open', 'Claim that is currently unsupported or openly speculative');

-- Seed data: master paper registry (partial — all 101 papers)
INSERT INTO papers (paper_num, title, domain, band) VALUES
(0,  'Unified Transport Contract And Foreword',               'Grounding',          'A'),
(1,  'Unified Lcr Kernel And Chart',                          'Foundation Math',    'A'),
(2,  'Unified Correction Surface And Rule30 Decomposition',   'Cellular Automata',  'A'),
(3,  'Unified D4 J3 Triality And Correction Surface',         'Exceptional Algebra','A'),
(4,  'Unified Boundary Repair',                               'Boundary Repair',    'A'),
(5,  'Unified Oloid Path Carrier',                            'Carrier Geometry',   'A'),
(6,  'Unified Causal Link And Obligation Ledger',             'Causal Structure',   'A'),
(7,  'Unified Discrete Continuous Bridge',                    'Bridge Math',        'A'),
(8,  'Unified Lattice Closure',                               'Lattice Theory',     'A'),
(9,  'Unified Hamiltonian Temporal Emergence',                'Temporal Structure', 'A'),
(10, 'Unified T10 Master Receipt',                            'Receipt Protocol',   'A'),
(11, 'Unified Theory Admission Gate',                         'Admission Logic',    'A'),
(12, 'Unified Ca Prediction Surface',                         'CA Enumeration',     'A'),
(13, 'Unified Quark Face Transport',                          'QCD Structure',      'A'),
(14, 'Unified Gr Boundary Repair Curvature',                  'GR Curvature',       'A'),
(15, 'Unified Qft Higgs Mass Residue',                        'Higgs Mechanism',    'A'),
(16, 'Unified Continuum Edge Residuals',                      'Continuum Limits',   'A'),
(17, 'Unified E6 E8 Error Correction Tower',                  'Exceptional Tower',  'A'),
(18, 'Unified Voa Moonshine Routes',                          'Moonshine VOA',      'A'),
(19, 'Unified Observer Face Selection',                       'Observer Theory',    'A'),
(20, 'Unified Layer 2 Synthesis Ledger',                      'Synthesis',          'B'),
(21, 'Unified Morphforge Polyforge Morphonix',                'Forge Systems',      'B'),
(22, 'Unified Metaforge Applied Materials',                   'Materials',          'B'),
(23, 'Unified Foldforge Protein Folding',                     'Biophysics',         'B'),
(24, 'Unified Knightforge N Dimensional Chess Automata',      'Game Theory',        'B'),
(25, 'Unified Energetic Traversal Maps',                      'Energy Landscapes',  'B'),
(26, 'Unified Z Pinch And Shear Horizon',                     'Plasma Physics',     'B'),
(27, 'Unified Observer Delay And Shared Reality',             'Multi-observer',     'B'),
(28, 'Unified N Dimensional Game Lattices',                   'Game Lattices',      'B'),
(29, 'Unified Monster Universal Energy Bound Hypotheses',     'Monster VOA',        'B'),
(30, 'Unified Grand Ribbon Meta Framer',                      'Meta-framing',       'B'),
(31, 'Unified It Was Still Just Lcr',                         'LCR Core',           'B'),
(32, 'Unified The Supervisor Cursor',                         'Cursor/Agent',       'B'),
(33, 'Unified Electroweak Higgs Mass Residue',                'Electroweak',        'B'),
(34, 'Unified Gr Curvature Continuum',                        'GR Continuum',       'B'),
(35, 'Unified Electron Hole Exciton Accounting',              'Semiconductors',     'B'),
(36, 'Unified Condensed Matter Metamaterials',                'Metamaterials',      'B'),
(37, 'Unified Plasma Energy Traversal',                       'Plasma Energy',      'B'),
(38, 'Unified Observer Computation Ai Runtime',               'AI Runtime',         'B'),
(39, 'Unified Falsifiers Comparators Standards',              'Standards',          'B'),
(40, 'Unified Grand Reconstruction Map',                      'Reconstruction',     'Bp'),
(41, 'Unified Su3 Generation 1',                              'SU3 Gen1',           'Bp'),
(42, 'Unified SU3 Generation 2 Strange Charm',                'SU3 Gen2',           'Bp'),
(43, 'Unified SU3 Generation 3 Bottom Top',                   'SU3 Gen3',           'Bp'),
(44, 'Unified SU3 Color Confinement',                         'Color Confinement',  'Bp'),
(45, 'Unified SU2 U1 Electroweak Gauge Bosons',               'Gauge Bosons',       'Bp'),
(46, 'Unified SU2 U1 Electroweak Symmetry Breaking',          'Symmetry Breaking',  'Bp'),
(47, 'Unified SU2 U1 VA Weak Interaction',                    'Weak Interaction',   'Bp'),
(48, 'Unified SU2 U1 Electroweak Phase Diagram',              'Phase Diagram',      'Bp'),
(49, 'Unified Mass And Yukawa 1 Mass Hierarchy',              'Mass Hierarchy',     'Bp'),
(50, 'Unified Mass And Yukawa 2 CKM PMNS',                    'CKM/PMNS',           'Bp'),
(51, 'Unified Mass And Yukawa 3 BSM Constraints',             'BSM Constraints',    'Bp'),
(52, 'Unified Mass And Yukawa 4 Neutrino Seesaw PMNS',        'Neutrino Seesaw',    'Bp'),
(53, 'Unified Higgs And Vacuum 1 Higgs Mechanism',            'Higgs Mechanism',    'Bp'),
(54, 'Unified Higgs And Vacuum 2 VOA Excited Weight 5',       'VOA Weight 5',       'Bp'),
(55, 'Unified Higgs And Vacuum 3 Vacuum Stability',           'Vacuum Stability',   'Bp'),
(56, 'Unified Higgs And Vacuum 4 Higgs Couplings',            'Higgs Couplings',    'Bp'),
(57, 'Unified QCD Phenomenology 1 Hadron Spectroscopy',       'Hadron Spectroscopy','Bp'),
(58, 'Unified QCD Phenomenology 2 Parton Distributions',      'Parton Distributions','Bp'),
(59, 'Unified QCD Phenomenology 3 Jets And Fragmentation',    'Jets/Fragmentation', 'Bp'),
(60, 'Unified QCD Phenomenology 4 Lattice QCD',               'Lattice QCD',        'Bp'),
(61, 'Unified BSM And Dark 1 Neutrino Masses And Mixing',     'Neutrino Mixing',    'Bp'),
(62, 'Unified BSM And Dark 2 Dark Matter Candidates',         'Dark Matter',        'Bp'),
(63, 'Unified BSM And Dark 3 Dark Energy',                    'Dark Energy',        'Bp'),
(64, 'Unified BSM And Dark 4 Inflation',                      'Inflation',          'Bp'),
(65, 'Unified GR Side 1 Einstein Field Equation',             'EFE',                'Bp'),
(66, 'Unified GR Side 2 Black Hole Entropy',                  'BH Entropy',         'Bp'),
(67, 'Unified Cosmology 1 FLRW Derivation',                   'FLRW',               'Bp'),
(68, 'Unified Cosmology 2 Cosmological Constant And Dark Energy','Dark Energy',     'Bp'),
(69, 'Unified Cosmology 3 Cosmic Microwave Background',       'CMB',                'Bp'),
(70, 'Unified Cosmology 4 Large Scale Structure',             'LSS',                'Bp'),
(71, 'Unified Calibration Protocols 1 Empirical Measurement', 'Calibration',        'Bp'),
(72, 'Unified Calibration Protocols 2 Between Sample Dynamics','Dynamics',           'Bp'),
(73, 'Unified Calibration Protocols 3 Closure Stability Sampling','Stability',       'Bp'),
(74, 'Unified Calibration Protocols 4 Between Sample Dynamics Dynamics','Meta-tests','Bp'),
(75, 'Unified Foundation Math Closure 1 F4 Universality',     'F4 Universality',    'C'),
(76, 'Unified Foundation Math Closure 2 Encoder Invariance',  'Encoder Invariance', 'C'),
(77, 'Unified Foundation Math Closure 3 Superpermutation Minimality','Superpermutation','C'),
(78, 'Unified Governance 1 Bibliography Taxonomy Governance', 'Governance',         'C'),
(79, 'Unified Governance 2 First Routing Implementation',     'Routing',            'C'),
(80, 'Unified UFT Closed Form Of The Language',               '2-Category L',       'C'),
(81, 'Unified Wolfram P1 Rule 30 Non Periodicity',            'Wolfram P1',         'C'),
(82, 'Unified Wolfram P2 Rule 30 Density 1 2',                'Wolfram P2',         'C'),
(83, 'Unified Wolfram P3 Rule 30 Sub O N Extraction',         'Wolfram P3',         'C'),
(84, 'Unified Yang Mills Mass Gap',                           'Yang-Mills',         'C'),
(85, 'Unified Navier Stokes Smoothness',                      'Navier-Stokes',      'C'),
(86, 'Unified Riemann Hypothesis Critical Line As Big Bang Crease','Riemann',       'C'),
(87, 'Unified Hodge Conjecture Algebraic Cycles And Boundary Repair Completion','Hodge','C'),
(88, 'Unified P vs NP Complexity Of Lattice Codes And Finite Presentation','P vs NP','C'),
(89, 'Unified Birch And Swinnerton Dyer Conjecture',          'BSD',                'C'),
(90, 'Unified McKay Thompson Parity And Rule 30 Correction Collapse','McKay-Thompson','C'),
(91, 'Unified Niemeier Glue Leech Invariants Gamma72 Landing','Niemeier/Leech',     'C'),
(92, 'Unified F4 Universality Theorem',                       'F4 Theorem',         'C'),
(93, 'Unified Cold Start Terminal Selection And Fingerprint Map','Cold Start',      'C'),
(94, 'Unified Encoder Invariance For Sporadic Boundary',      'Encoder Invariance', 'C'),
(95, 'Unified SPINOR Observation And Open Gap Observer Evidence','SPINOR',           'C'),
(96, 'Unified Superpermutation Minimality Bounds',            'Superpermutation',   'C'),
(97, 'Unified Electron Hole Exciton Accounting For Open Math','EHX Open Math',      'C'),
(98, 'Unified Reasoned Reapplication Of Standard Formalism',  'Reapplication',      'C'),
(99, 'Unified Applied Forge Validation',                      'Forge Validation',   'C'),
-- ============================================================
-- Paper 00 — Harvested from cryst_cam.py (2024-07-04)
-- ============================================================

-- Table: harvest_log
-- Role: Tracks harvested source files and their disposition
CREATE TABLE IF NOT EXISTS harvest_log (
    harvest_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file   TEXT NOT NULL,
    harvested_at  TEXT NOT NULL,
    disposition   TEXT NOT NULL CHECK (disposition IN ('canon','supplemental','discard')),
    claims_added  INTEGER DEFAULT 0,
    notes         TEXT
);

-- Table: theorem_registry
-- Role: Structured registry of theorem bindings per paper
CREATE TABLE IF NOT EXISTS theorem_registry (
    registry_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_ref     INTEGER NOT NULL,
    theorem_name  TEXT NOT NULL,
    role          TEXT NOT NULL,
    instantiated_by TEXT,
    FOREIGN KEY (paper_ref) REFERENCES papers(paper_num),
    FOREIGN KEY (theorem_name) REFERENCES theorems(name)
);

-- Seed data: Paper 00 established grounding theorems (8 theorems)
INSERT INTO theorems (name, theorem_type, author, year, citation, role, statement, proof_status, paper_ref) VALUES
('Lucas theorem', 'theorem', 'Lucas', 1878, 'Lucas 1878', 'origin', 'Over GF(2), C(m,n) mod 2 = 1 iff n is submask of m', 'proven', 0),
('Kummer theorem', 'theorem', 'Kummer', 1852, 'Kummer 1852', 'carries_correction', 'Carry structure -> Lucas-sparse skip-pad', 'proven', 0),
('Boole/De Morgan duality', 'theorem', 'Boole/De Morgan', 1847, 'Boole 1847, De Morgan 1860', 'idempotent_dual', 'AND and OR are idempotent and De Morgan dual', 'proven', 0),
('Steinhaus Three-Gap', 'theorem', 'Steinhaus', 1958, 'Steinhaus 1958', 'low_discrepancy', 'Optimal low-discrepancy golden-ratio sweep', 'proven', 0),
('Chinese Remainder Theorem', 'theorem', 'Sunzi/Gauss', NULL, 'CRT (Sunzi/Gauss)', 'digit_binding', 'Digit-binding closure 119 mod 153', 'proven', 0),
('Jordan/von Neumann/Wigner', 'theorem', 'Jordan/von Neumann/Wigner', 1934, 'JvNW 1934', 'idempotent_normal_form', 'J3(O) idempotent normal form, chart = diagonal', 'proven', 0),
('Conway/Sloane lattices', 'theorem', 'Conway/Sloane', 1988, 'Conway/Sloane 1988', 'high_dim_closure', 'E8/Leech lattice high-dimensional closure frames', 'proven', 0),
('Golay code', 'theorem', 'Golay', 1949, 'Golay 1949', 'error_correction', 'Error-correction tower Golay -> Leech', 'proven', 0),
('Conway/Norton Moonshine', 'theorem', 'Conway/Norton', 1979, 'Conway/Norton 1979', 'moonshine_layer', 'Monster VOA bounded execution, correction-parity', 'proven', 0);

-- Seed data: harvest log entry for cryst_cam.py
INSERT INTO harvest_log (source_file, harvested_at, disposition, claims_added, notes) VALUES
('D:/CodeLib/06_ACTIVE_REWORK_HARVEST/cryst_cam.py', '2024-07-04', 'canon', 3, 'Ported CrystKernel, TheoremRegistry, fracture_map, _genesis_root, _self_hash, verify_theorem_registry, verify_genesis_root_consistency, verify_self_hash_stability, verify_chain_integrity. Discarded file I/O, timing-dependent code, external tier, subprocess calls, visualization pipeline, OpsGuide, BBA structural address, forge/verifier discovery. 2774 lines -> ~200 unified.');


-- === BATCH GROUP 1 CLAIMS (paper-00) ===
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (0, '00.1', 'Σ = {0,1}³ defines exactly 8 tile states σ = (L,C,R)', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (0, '00.2', 'Correction Operator ∂ = C ∧ ¬R is the unique boundary operator with nilpotency ∂² = 0', 'D', 'mapped_file_claims_report.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (0, '00.3', 'Chiral doublet support Δ = {(0,1,0), (1,1,0)}', 'D', 'mapped_file_claims_report.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (0, '00.4', 'Gluon invariance Γ(σ) = C = Γ(swap_LR(σ)) verified for all 8 states (64/64 rows)', 'D', 'mapped_file_claims_report.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (0, '00.5', 'T5 idempotency M₃² = M₃ exact over ℚ with residual 2.5×10⁻¹⁶', 'D', 'mapped_file_claims_report.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (0, '00.6', 'Spectre Correction 4/4 PASS', 'D', 'mapped_file_claims_report.md');
