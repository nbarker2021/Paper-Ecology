-- CMPLX-Standards Schema Export (A-family)

-- Generated: 2026-07-04T19:49:13+00:00



CREATE TABLE cam_hashes (
            cam_hash    TEXT PRIMARY KEY,
            content_type TEXT,
            content_id   TEXT,
            created_at   TEXT
        );

CREATE TABLE contracts (
            contract_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            contract_name TEXT NOT NULL UNIQUE,
            description   TEXT,
            validation_rules TEXT,
            paper_number  TEXT NOT NULL UNIQUE,
            status        TEXT CHECK(status IN ('active','draft','deprecated')),
            band          TEXT,
            lcr_kernel    TEXT,
            cam_hash      TEXT NOT NULL
        );

CREATE TABLE grader_runs (
            run_id         INTEGER PRIMARY KEY AUTOINCREMENT,
            grader_version TEXT,
            run_date       TEXT,
            paper_number   TEXT NOT NULL,
            assigned_grade TEXT CHECK(assigned_grade IN ('D','I','X')),
            band           TEXT,
            metrics_json   TEXT,
            cam_hash       TEXT NOT NULL
        );

CREATE INDEX idx_cam_type        ON cam_hashes(content_type);

CREATE INDEX idx_contracts_paper ON contracts(paper_number);

CREATE INDEX idx_sources_contract ON standards_sources(contract_id);

CREATE INDEX idx_sp_band         ON standards_papers(band_id);

CREATE INDEX idx_sp_contract     ON standards_papers(contract_id);

CREATE INDEX idx_sp_paper        ON standards_papers(paper_number);

CREATE TABLE inclusion_bands (
            band_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            band_name    TEXT NOT NULL UNIQUE,
            description  TEXT,
            min_score    REAL,
            max_score    REAL,
            criteria     TEXT,
            cam_hash     TEXT NOT NULL
        );

CREATE TABLE sqlite_sequence(name,seq);

CREATE TABLE standards_papers (
            mapping_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_number TEXT NOT NULL,
            contract_id  INTEGER,
            band_id      INTEGER,
            grade        TEXT CHECK(grade IN ('D','I','X')),
            status       TEXT,
            cam_hash     TEXT NOT NULL,
            FOREIGN KEY (contract_id) REFERENCES contracts(contract_id),
            FOREIGN KEY (band_id)     REFERENCES inclusion_bands(band_id)
        );

CREATE TABLE standards_sources (
            source_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            contract_id  INTEGER,
            source_type  TEXT CHECK(source_type IN ('B_family','original')),
            original_path TEXT,
            stripped     TEXT,
            cam_hash     TEXT NOT NULL,
            FOREIGN KEY (contract_id) REFERENCES contracts(contract_id)
        );