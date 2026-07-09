-- CodeLib SQLite Schema
-- A-family naming (paper-00 through paper-100)
-- LCR kernel, D/I/X claims, CAM hashes

CREATE TABLE cam_hashes (
        cam_hash TEXT PRIMARY KEY,
        content_type TEXT,
        content_id TEXT,
        created_at TEXT
    );

CREATE TABLE code_claims (
        claim_id TEXT PRIMARY KEY,
        paper_number INTEGER,
        claim_text TEXT,
        claim_status TEXT CHECK(claim_status IN ('D', 'I', 'X')),
        code_file_id TEXT,
        evidence TEXT,
        cam_hash TEXT,
        FOREIGN KEY (code_file_id) REFERENCES code_files(code_id)
    );

CREATE TABLE code_files (
        code_id TEXT PRIMARY KEY,
        file_name TEXT NOT NULL,
        description TEXT,
        language TEXT,
        file_path TEXT,
        key_functions TEXT,
        paper_number INTEGER,
        status TEXT CHECK(status IN ('stub', 'real', 'verified')),
        verifier_type TEXT CHECK(verifier_type IN ('unit', 'integration', 'property')),
        cam_hash TEXT
    );

CREATE TABLE code_papers (
        mapping_id TEXT PRIMARY KEY,
        paper_number INTEGER,
        code_id TEXT,
        role TEXT CHECK(role IN ('verifier', 'implementation', 'spec')),
        status TEXT,
        cam_hash TEXT,
        FOREIGN KEY (code_id) REFERENCES code_files(code_id)
    );

CREATE TABLE code_sources (
        source_id TEXT PRIMARY KEY,
        code_id TEXT,
        source_type TEXT CHECK(source_type IN ('B_family_lattice_forge', 'B_family_forge', 'original')),
        original_path TEXT,
        stripped INTEGER,
        cam_hash TEXT,
        FOREIGN KEY (code_id) REFERENCES code_files(code_id)
    );
