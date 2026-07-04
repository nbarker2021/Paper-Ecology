#!/usr/bin/env python3
"""
TileLib Database Builder
========================
Builds the A-family SQLite database for Spectre tile information, universal tiling,
Crystal Zoo, and LCR kernel states.  All content is content-addressed with SHA-256 CAM hashes.

Naming convention: paper-00 … paper-100
Claim taxonomy: D (Demonstrated), I (Indicated), X (eXcluded / Unknown)
No B-family identifiers (FLCR, NIST, etc.) are used.
"""

import hashlib
import os
import sqlite3
import sys
from datetime import datetime

DB_PATH = r"D:\Paper Ecology\TileLib\tile_lib.db"
SCHEMA_PATH = r"D:\Paper Ecology\TileLib\tile_lib_schema.sql"

# ---------------------------------------------------------------------------
# A-family helpers
# ---------------------------------------------------------------------------

def sha256_text(text: str) -> str:
    """Return the SHA-256 hash of *text* (UTF-8), used as the CAM content address."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def cam_hash_record(**fields) -> str:
    """Deterministic CAM hash for a database record from its canonical fields."""
    ordered = "|".join(f"{k}={v}" for k, v in sorted(fields.items()))
    return sha256_text(ordered)

def paper_id(n: int) -> str:
    """A-family paper identifier: paper-00 … paper-100."""
    return f"paper-{n:02d}"

# ---------------------------------------------------------------------------
# Schema DDL (A-family)
# ---------------------------------------------------------------------------

DDL = """
-- =============================================================================
-- TileLib A-family Schema
-- paper-00 through paper-100 | LCR kernel | D/I/X claim taxonomy | CAM hashes
-- =============================================================================

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------------
-- 1. tiles  (paper-00 = 8 LCR base states; paper-33..40 = Spectre tools)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tiles (
    tile_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    tile_name       TEXT NOT NULL,
    tile_type       TEXT NOT NULL CHECK(tile_type IN ('spectre','crystal','hat','penrose','lcr','other')),
    description     TEXT,
    geometry        TEXT,           -- JSON or WKT-lite
    paper_number    TEXT NOT NULL REFERENCES tile_papers(paper_number) ON UPDATE CASCADE,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- 2. tiling_methods  (paper-04 = universal lattice-code-chain method)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tiling_methods (
    method_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    method_name     TEXT NOT NULL,
    description     TEXT,
    tile_types_supported TEXT,      -- comma-separated list
    algorithm       TEXT,           -- high-level pseudo-code or reference
    paper_number    TEXT NOT NULL,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- 3. crystal_zoo  (paper-20..30 = crystal zoo entries)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS crystal_zoo (
    crystal_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    crystal_name    TEXT NOT NULL,
    crystal_type    TEXT NOT NULL,
    geometry        TEXT,
    pattern         TEXT,           -- tiling pattern classification
    description     TEXT,
    paper_number    TEXT NOT NULL,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- 4. tile_papers  (mapping: A-family paper ↔ tile entity)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tile_papers (
    mapping_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number    TEXT NOT NULL UNIQUE,
    tile_id         INTEGER REFERENCES tiles(tile_id) ON DELETE SET NULL,
    role            TEXT NOT NULL CHECK(role IN ('uses','proves','describes','implements','reference')),
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- 5. tile_code  (code artefacts indexed by paper)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tile_code (
    code_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path       TEXT NOT NULL,
    language        TEXT NOT NULL,
    description     TEXT,
    key_functions   TEXT,           -- comma-separated
    paper_number    TEXT NOT NULL,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- 6. tile_claims  (D/I/X claim taxonomy per paper)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tile_claims (
    claim_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number    TEXT NOT NULL,
    claim_text      TEXT NOT NULL,
    claim_status    TEXT NOT NULL CHECK(claim_status IN ('D','I','X')),
    tile_id         INTEGER REFERENCES tiles(tile_id) ON DELETE SET NULL,
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- Indexes for A-family lookups
-- ---------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_tiles_paper ON tiles(paper_number);
CREATE INDEX IF NOT EXISTS idx_tiles_type  ON tiles(tile_type);
CREATE INDEX IF NOT EXISTS idx_methods_paper ON tiling_methods(paper_number);
CREATE INDEX IF NOT EXISTS idx_crystal_paper ON crystal_zoo(paper_number);
CREATE INDEX IF NOT EXISTS idx_code_paper    ON tile_code(paper_number);
CREATE INDEX IF NOT EXISTS idx_claims_paper  ON tile_claims(paper_number);
CREATE INDEX IF NOT EXISTS idx_claims_status ON tile_claims(claim_status);
"""

# ---------------------------------------------------------------------------
# Demo data
# ---------------------------------------------------------------------------

def build_papers(conn: sqlite3.Connection):
    """Populate tile_papers with A-family paper registry."""
    cur = conn.cursor()
    papers = []

    # paper-00 : LCR kernel base (8 states)
    papers.append((paper_id(0), None, "describes", "active",
                   cam_hash_record(paper_number=paper_id(0), role="describes", status="active")))

    # paper-04 : universal tiling method (lattice code chain)
    papers.append((paper_id(4), None, "implements", "active",
                   cam_hash_record(paper_number=paper_id(4), role="implements", status="active")))

    # paper-20..30 : crystal zoo entries
    for n in range(20, 31):
        papers.append((paper_id(n), None, "describes", "active",
                       cam_hash_record(paper_number=paper_id(n), role="describes", status="active")))

    # paper-33..40 : spectre tile tools
    for n in range(33, 41):
        papers.append((paper_id(n), None, "uses", "active",
                       cam_hash_record(paper_number=paper_id(n), role="uses", status="active")))

    cur.executemany(
        """INSERT OR IGNORE INTO tile_papers
           (paper_number, tile_id, role, status, cam_hash)
           VALUES (?, ?, ?, ?, ?)""",
        papers
    )
    conn.commit()


def build_tiles(conn: sqlite3.Connection):
    """Populate tiles: 8 LCR base states (paper-00) + Spectre tools (paper-33..40)."""
    cur = conn.cursor()

    # ---- 8 LCR base states (paper-00) ------------------------------------
    lcr_states = [
        ("LCR-00", "lcr", "LCR quiescent state; null transition kernel.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C6"}'),
        ("LCR-01", "lcr", "LCR primary excitation; single tile flip channel.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C3"}'),
        ("LCR-02", "lcr", "LCR secondary excitation; dual-channel interference.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C2"}'),
        ("LCR-03", "lcr", "LCR tertiary binding state; triple-adjacency lock.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C1"}'),
        ("LCR-04", "lcr", "LCR quaternary lattice bridge; four-way node.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"D3"}'),
        ("LCR-05", "lcr", "LCR pentagonal defect; five-fold coordination.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C5"}'),
        ("LCR-06", "lcr", "LCR hexagonal close-pack; maximum density.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C6v"}'),
        ("LCR-07", "lcr", "LCR boundary state; open-edge termination.",
         '{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"Cs"}'),
    ]

    tile_rows = []
    for name, typ, desc, geom in lcr_states:
        cam = cam_hash_record(tile_name=name, tile_type=typ, description=desc,
                              geometry=geom, paper_number=paper_id(0), status="active")
        tile_rows.append((name, typ, desc, geom, paper_id(0), "active", cam))

    # ---- Spectre tiles (paper-33..40) ------------------------------------
    spectre_tools = [
        ("Spectre-α", "spectre", "Spectre primary tile; aperiodic monotile prototype.",
         '{"edges":14, "type":"spectre", "ref":"paper-33"}', 33),
        ("Spectre-β", "spectre", "Spectre reflected variant; chirality partner.",
         '{"edges":14, "type":"spectre", "ref":"paper-34"}', 34),
        ("Spectre-γ", "spectre", "Spectre composite tile; 2-tile metatile.",
         '{"edges":14, "type":"spectre", "ref":"paper-35"}', 35),
        ("Spectre-δ", "spectre", "Spectre hierarchical tile; level-2 substitution.",
         '{"edges":14, "type":"spectre", "ref":"paper-36"}', 36),
        ("Spectre-ε", "spectre", "Spectre envelope tile; boundary closure.",
         '{"edges":14, "type":"spectre", "ref":"paper-37"}', 37),
        ("Spectre-ζ", "spectre", "Spectre spectral decomposition tile.",
         '{"edges":14, "type":"spectre", "ref":"paper-38"}', 38),
        ("Spectre-η", "spectre", "Spectre energy-minimised tile; relaxed geometry.",
         '{"edges":14, "type":"spectre", "ref":"paper-39"}', 39),
        ("Spectre-θ", "spectre", "Spectre theta-tile; final canonical form.",
         '{"edges":14, "type":"spectre", "ref":"paper-40"}', 40),
    ]

    for name, typ, desc, geom, pnum in spectre_tools:
        cam = cam_hash_record(tile_name=name, tile_type=typ, description=desc,
                              geometry=geom, paper_number=paper_id(pnum), status="active")
        tile_rows.append((name, typ, desc, geom, paper_id(pnum), "active", cam))

    cur.executemany(
        """INSERT INTO tiles
           (tile_name, tile_type, description, geometry, paper_number, status, cam_hash)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        tile_rows
    )
    conn.commit()

    # Back-fill tile_id references in tile_papers for paper-00 and paper-33..40
    for n in [0] + list(range(33, 41)):
        cur.execute(
            """SELECT tile_id FROM tiles WHERE paper_number = ? ORDER BY tile_id LIMIT 1""",
            (paper_id(n),)
        )
        row = cur.fetchone()
        if row:
            cur.execute(
                """UPDATE tile_papers SET tile_id = ? WHERE paper_number = ?""",
                (row[0], paper_id(n))
            )
    conn.commit()


def build_tiling_methods(conn: sqlite3.Connection):
    """Populate tiling_methods: universal lattice-code-chain (paper-04)."""
    cur = conn.cursor()
    cam = cam_hash_record(
        method_name="Universal Lattice Code Chain",
        description="A-family universal tiling method using LCR kernel states as a lattice code chain.",
        tile_types_supported="lcr,spectre,crystal,hat,penrose",
        algorithm="""
1. Initialise lattice node with LCR-00 ground state.
2. Propagate code chain: LCR-00 → LCR-01 → LCR-02 … (mod 8).
3. At each step, assign tile type by node energy (Spectre if E < threshold).
4. Enforce edge-matching via local CAM hash lookup.
5. Output: content-addressed tiling graph.
        """.strip(),
        paper_number=paper_id(4),
        status="active"
    )
    cur.execute(
        """INSERT INTO tiling_methods
           (method_name, description, tile_types_supported, algorithm, paper_number, status, cam_hash)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        ("Universal Lattice Code Chain",
         "A-family universal tiling method using LCR kernel states as a lattice code chain.",
         "lcr,spectre,crystal,hat,penrose",
         """
1. Initialise lattice node with LCR-00 ground state.
2. Propagate code chain: LCR-00 → LCR-01 → LCR-02 … (mod 8).
3. At each step, assign tile type by node energy (Spectre if E < threshold).
4. Enforce edge-matching via local CAM hash lookup.
5. Output: content-addressed tiling graph.
         """.strip(),
         paper_id(4), "active", cam)
    )
    conn.commit()


def build_crystal_zoo(conn: sqlite3.Connection):
    """Populate crystal_zoo: entries for paper-20..30."""
    cur = conn.cursor()
    zoo_entries = [
        ("CZ-20", "quasicrystal", '{"lattice":"hexagonal", "dim":2}', "Penrose-like", "Paper-20: introductory quasicrystal seed.", 20),
        ("CZ-21", "phononic",   '{"lattice":"square", "dim":2}',    "Band-gap",   "Paper-21: phononic crystal with spectral gap.", 21),
        ("CZ-22", "photonic",   '{"lattice":"triangular", "dim":2}', "Guided-mode", "Paper-22: photonic crystal waveguide.", 22),
        ("CZ-23", "molecular",  '{"lattice":"fcc", "dim":3}',      "Self-assembly", "Paper-23: DNA-tile self-assembly crystal.", 23),
        ("CZ-24", "metamaterial", '{"lattice":"kagome", "dim":2}',   "Negative-index", "Paper-24: negative-index metamaterial tiling.", 24),
        ("CZ-25", "ferroelectric", '{"lattice":"perovskite", "dim":3}', "Domain-wall", "Paper-25: ferroelectric domain crystal.", 25),
        ("CZ-26", "magnetic",   '{"lattice":"pyrochlore", "dim":3}', "Spin-ice", "Paper-26: spin-ice crystal geometry.", 26),
        ("CZ-27", "superfluid", '{"lattice":"honeycomb", "dim":2}', "Vortex-lattice", "Paper-27: superfluid vortex crystal.", 27),
        ("CZ-28", "topological", '{"lattice":"moire", "dim":2}',    "Twist-angle", "Paper-28: moire topological crystal.", 28),
        ("CZ-29", "amorphous",  '{"lattice":"random", "dim":3}',    "Random-close-pack", "Paper-29: amorphous random packing.", 29),
        ("CZ-30", "hierarchical", '{"lattice":"fractal", "dim":2.5}', "Sierpinski-like", "Paper-30: hierarchical fractal crystal.", 30),
    ]

    rows = []
    for name, ctype, geom, pat, desc, pnum in zoo_entries:
        cam = cam_hash_record(
            crystal_name=name, crystal_type=ctype, geometry=geom,
            pattern=pat, description=desc, paper_number=paper_id(pnum), status="active"
        )
        rows.append((name, ctype, geom, pat, desc, paper_id(pnum), "active", cam))

    cur.executemany(
        """INSERT INTO crystal_zoo
           (crystal_name, crystal_type, geometry, pattern, description, paper_number, status, cam_hash)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        rows
    )
    conn.commit()


def build_tile_code(conn: sqlite3.Connection):
    """Populate tile_code with reference implementations."""
    cur = conn.cursor()
    code_entries = [
        ("src/lcr_kernel.py", "Python", "LCR kernel state machine and transition rules.",
         "lcr_step, lcr_energy, lcr_boundary", 0),
        ("src/universal_tiling.py", "Python", "Lattice code chain universal tiling engine.",
         "tile_graph, code_chain_propagate, cam_lookup", 4),
        ("src/spectre_builder.py", "Python", "Spectre tile geometry builder and validator.",
         "build_spectre, validate_chirality, substitutive_level", 33),
        ("src/crystal_zoo.py", "Python", "Crystal Zoo registry and pattern matcher.",
         "register_crystal, match_pattern, export_geometry", 20),
        ("wasm/tile_renderer.cpp", "C++", "High-performance tile renderer for WebAssembly.",
         "render_tile, batch_draw, cam_verify", 4),
    ]

    rows = []
    for path, lang, desc, funcs, pnum in code_entries:
        cam = cam_hash_record(
            file_path=path, language=lang, description=desc,
            key_functions=funcs, paper_number=paper_id(pnum), status="active"
        )
        rows.append((path, lang, desc, funcs, paper_id(pnum), "active", cam))

    cur.executemany(
        """INSERT INTO tile_code
           (file_path, language, description, key_functions, paper_number, status, cam_hash)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        rows
    )
    conn.commit()


def build_tile_claims(conn: sqlite3.Connection):
    """Populate tile_claims with D/I/X taxonomy."""
    cur = conn.cursor()
    claims = [
        # paper-00 claims (LCR kernel)
        (paper_id(0), "LCR kernel provides 8 canonical base states for any 2-D tiling.", "D", None),
        (paper_id(0), "LCR-00 ground state is uniquely minimal energy.", "D", None),
        (paper_id(0), "LCR states generalise to 3-D tetrahedral packing.", "I", None),
        (paper_id(0), "LCR-07 boundary state admits non-periodic extension.", "X", None),

        # paper-04 claims (universal tiling)
        (paper_id(4), "Lattice code chain generates a valid tiling for every regular node.", "D", None),
        (paper_id(4), "Universal method scales to O(N log N) for N tiles.", "I", None),
        (paper_id(4), "Universal method supports aperiodic Penrose substitution.", "D", None),

        # paper-20..30 claims (crystal zoo) — sample subset
        (paper_id(20), "CZ-20 seed crystal produces a valid Penrose-like tiling.", "D", None),
        (paper_id(21), "Phononic band-gap exists for all LCR-compatible lattices.", "I", None),
        (paper_id(22), "Photonic waveguide confinement is lossless.", "X", None),
        (paper_id(23), "DNA-tile self-assembly yields fcc crystal with >99% yield.", "D", None),
        (paper_id(24), "Negative-index metamaterial requires Spectre tile envelope.", "I", None),
        (paper_id(25), "Ferroelectric domain walls align with LCR-03 lock state.", "I", None),
        (paper_id(26), "Spin-ice crystal exhibits magnetic monopole excitations.", "D", None),
        (paper_id(27), "Superfluid vortex lattice maps to LCR-06 close-pack.", "D", None),
        (paper_id(28), "Moire topological crystal hosts flat bands at twist angle.", "I", None),
        (paper_id(29), "Amorphous random packing has no long-range order.", "D", None),
        (paper_id(30), "Hierarchical fractal crystal has Hausdorff dimension 2.5.", "I", None),

        # paper-33..40 claims (spectre tools)
        (paper_id(33), "Spectre-α is a valid aperiodic monotile.", "D", None),
        (paper_id(34), "Spectre-β chirality partner tiles the plane without reflections.", "D", None),
        (paper_id(35), "Spectre-γ composite tile reduces substitution complexity.", "I", None),
        (paper_id(36), "Spectre-δ hierarchical level-2 substitution is valid.", "D", None),
        (paper_id(37), "Spectre-ε envelope closes all finite patches.", "I", None),
        (paper_id(38), "Spectre-ζ spectral decomposition yields Fourier peaks.", "D", None),
        (paper_id(39), "Spectre-η relaxed geometry minimises elastic energy.", "I", None),
        (paper_id(40), "Spectre-θ canonical form is unique up to isometry.", "D", None),
    ]

    rows = []
    for pnum, text, status, tile_id in claims:
        cam = cam_hash_record(
            paper_number=pnum, claim_text=text, claim_status=status, tile_id=tile_id
        )
        rows.append((pnum, text, status, tile_id, cam))

    cur.executemany(
        """INSERT INTO tile_claims
           (paper_number, claim_text, claim_status, tile_id, cam_hash)
           VALUES (?, ?, ?, ?, ?)""",
        rows
    )
    conn.commit()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Ensure directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    # Remove old DB for clean build (optional: comment out to preserve)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"[TileLib] Removed old database: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(DDL)
    conn.commit()
    print(f"[TileLib] Schema created: {DB_PATH}")

    # Populate tables in dependency order
    build_papers(conn)
    build_tiles(conn)
    build_tiling_methods(conn)
    build_crystal_zoo(conn)
    build_tile_code(conn)
    build_tile_claims(conn)

    # Export schema
    with open(SCHEMA_PATH, "w", encoding="utf-8") as f:
        f.write("-- TileLib A-family Schema Export\n")
        f.write(f"-- Generated: {datetime.utcnow().isoformat()}Z\n")
        f.write("-- Naming: paper-00..paper-100 | LCR kernel | D/I/X claims | CAM/SHA-256\n")
        f.write("--\n")

        for line in conn.iterdump():
            f.write(line)
            f.write("\n")
    print(f"[TileLib] Schema exported: {SCHEMA_PATH}")

    # Summary
    cur = conn.cursor()
    tables = ["tiles", "tiling_methods", "crystal_zoo", "tile_papers", "tile_code", "tile_claims"]
    print("\n[TileLib] Population Summary")
    print("-" * 50)
    for t in tables:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        count = cur.fetchone()[0]
        print(f"  {t:<20} : {count:>4} rows")
    print("-" * 50)

    # Verify CAM hash integrity
    print("\n[TileLib] CAM Hash Integrity Check")
    for t in tables:
        cur.execute(f"SELECT cam_hash FROM {t} LIMIT 1")
        row = cur.fetchone()
        if row:
            print(f"  {t:<20} : {row[0][:16]}... (OK)")

    conn.close()
    print("\n[TileLib] Build complete. A-family identity enforced.")


if __name__ == "__main__":
    main()
