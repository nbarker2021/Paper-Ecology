#!/usr/bin/env python3
"""FINAL consistency check across all Paper Ecology databases."""
import sqlite3
import os
from collections import defaultdict, Counter
from datetime import datetime

# Database paths
DATABASES = {
    'CrystalLib': r'D:\Paper Ecology\CrystalLib\crystal_lib.db',
    'SystemsLib': r'D:\Paper Ecology\SystemsLib\systems_lib.db',
    'TileLib': r'D:\Paper Ecology\TileLib\tile_lib.db',
    'ReForge_ForgeLib': r'D:\Paper Ecology\ReForge_ForgeLib\reforge_forge_lib.db',
    'PaperLib': r'D:\Paper Ecology\PaperLib\paper_lib.db',
    'CodeLib': r'D:\Paper Ecology\CodeLib\code_lib.db',
    'SQLLib': r'D:\Paper Ecology\SQLLib\sql_lib.db',
    'CMPLX-Standards': r'D:\Paper Ecology\CMPLX-Standards\cmplx_standards.db',
    'cqekernel': r'D:\Paper Ecology\cqekernel\cqekernel.db',
}

PAPERS = [f'paper-{i:02d}' for i in range(101)]

def connect(db_path):
    return sqlite3.connect(db_path)

def check_crystal_lib(conn):
    """CrystalLib checks."""
    c = conn.cursor()
    issues = []
    
    # 1. Papers present
    c.execute("SELECT paper_number FROM papers")
    found = {r[0] for r in c.fetchall()}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)} ({sorted(list(missing))[:5]}...)")
    
    # 2. D/I/X claims per paper
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[paper]:
            claim_counts[paper][status] = count
    
    for p in PAPERS:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # 3. Code stubs - CrystalLib has no code table with status, skip
    # 4. SQL stubs - CrystalLib has no SQL table with status, skip
    # 5. Grades - CrystalLib has no grade column, skip
    # 6. Receipts >= 1 per paper
    c.execute("SELECT paper_number, COUNT(*) FROM receipts GROUP BY paper_number")
    receipt_counts = {r[0]: r[1] for r in c.fetchall()}
    for p in PAPERS:
        if receipt_counts.get(p, 0) < 1:
            issues.append(f"{p}: receipts = {receipt_counts.get(p, 0)} (< 1)")
    
    # 7. CAM hashes unique
    c.execute("SELECT cam_hash FROM cam_hashes")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    if dupes:
        issues.append(f"CAM hash duplicates: {len(dupes)} (e.g., {list(dupes.items())[:2]})")
    
    # 8. B-family refs in all text fields
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    b_refs = []
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                for row in c.fetchall():
                    if row[0] and any(b in row[0] for b in ['B-family', 'B family', 'Bfamily']):
                        b_refs.append(f"{t}.{col}: {row[0][:80]}")
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {len(b_refs)} ({b_refs[0]})")
    
    return {
        'name': 'CrystalLib',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': sum(1 for i in issues if 'receipts = ' in i),
        'stub_count': 0,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': len(b_refs),
        'issues': issues
    }

def check_paper_lib(conn):
    c = conn.cursor()
    issues = []
    
    c.execute("SELECT paper_number FROM papers")
    found = {r[0] for r in c.fetchall()}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)}")
    
    # D/I/X claims via claims table
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[paper]:
            claim_counts[paper][status] = count
    
    for p in PAPERS:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # No code/sql stubs, grades, or receipts in this DB
    # CAM hashes
    c.execute("SELECT cam_hash FROM cam_hashes")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    if dupes:
        issues.append(f"CAM hash duplicates: {len(dupes)}")
    
    # B-family refs
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'PaperLib',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': 0,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_code_lib(conn):
    c = conn.cursor()
    issues = []
    
    # code_papers has paper_number as INTEGER
    c.execute("SELECT paper_number FROM code_papers")
    found_nums = {r[0] for r in c.fetchall()}
    found = {f'paper-{n:02d}' for n in found_nums}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)} (only {len(found)} papers have code)")
    
    # D/I/X claims via code_claims
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM code_claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[f'paper-{paper:02d}']:
            claim_counts[f'paper-{paper:02d}'][status] = count
    
    for p in found:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # Code stubs
    c.execute("SELECT COUNT(*) FROM code_files WHERE status = 'stub' OR status = 'placeholder'")
    stub_count = c.fetchone()[0]
    if stub_count > 0:
        issues.append(f"Code stubs: {stub_count}")
    
    # CAM hashes
    c.execute("SELECT cam_hash FROM cam_hashes")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    
    # B-family
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'CodeLib',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': stub_count,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_sql_lib(conn):
    c = conn.cursor()
    issues = []
    
    c.execute("SELECT paper_number FROM sql_papers")
    found_nums = {r[0] for r in c.fetchall()}
    found = {f'paper-{n:02d}' for n in found_nums}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)}")
    
    # D/I/X claims
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM sql_claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[f'paper-{paper:02d}']:
            claim_counts[f'paper-{paper:02d}'][status] = count
    
    for p in PAPERS:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # SQL stubs
    c.execute("SELECT COUNT(*) FROM sql_files WHERE status = 'stub' OR status = 'placeholder' OR status = 'empty'")
    sql_stub_count = c.fetchone()[0]
    if sql_stub_count > 0:
        issues.append(f"SQL stubs: {sql_stub_count}")
    
    # CAM hashes
    c.execute("SELECT cam_hash FROM cam_hashes")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    
    # B-family
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'SQLLib',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': 0,
        'sql_stub_count': sql_stub_count,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_cmplx_standards(conn):
    c = conn.cursor()
    issues = []
    
    c.execute("SELECT paper_number FROM standards_papers")
    found = {r[0] for r in c.fetchall()}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)} (only {len(found)} graded)")
    
    # Grades
    c.execute("SELECT paper_number, grade FROM standards_papers WHERE grade IS NULL OR grade = ''")
    empty_grades = c.fetchall()
    if empty_grades:
        issues.append(f"Empty grades: {len(empty_grades)}")
    
    # D/I/X not tracked directly in standards_papers, check grader_runs
    c.execute("SELECT paper_number, metrics_json FROM grader_runs")
    for paper, metrics in c.fetchall():
        if metrics:
            try:
                import json
                m = json.loads(metrics)
                for k in ['d_claims', 'i_claims', 'x_claims']:
                    if m.get(k, 0) == 0:
                        issues.append(f"{paper}: {k} = 0 in grader_runs")
            except:
                pass
    
    # CAM hashes
    c.execute("SELECT cam_hash FROM cam_hashes")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    
    # B-family
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'CMPLX-Standards',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': 0,
        'sql_stub_count': 0,
        'grade_empty': len(empty_grades),
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_cqekernel(conn):
    c = conn.cursor()
    issues = []
    
    c.execute("SELECT paper_number FROM kernel_papers")
    found = {r[0] for r in c.fetchall()}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)} (note: some papers may have multiple layer entries)")
    
    # D/I/X claims
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM kernel_claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[paper]:
            claim_counts[paper][status] = count
    
    for p in PAPERS:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # CAM hashes
    c.execute("SELECT cam_hash FROM cam_hashes")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    
    # B-family
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'cqekernel',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': 0,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_systems_lib(conn):
    c = conn.cursor()
    issues = []
    
    # SystemsLib doesn't have a per-paper table with all 101 papers
    c.execute("SELECT paper_number FROM systems")
    found = {r[0] for r in c.fetchall() if r[0]}
    # Also check paper_sources
    c.execute("SELECT paper_number FROM paper_sources")
    found2 = {r[0] for r in c.fetchall() if r[0]}
    
    issues.append(f"systems table: {len(found)} paper entries")
    issues.append(f"paper_sources table: {len(found2)} paper entries")
    
    # B-family
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'SystemsLib',
        'paper_count': len(found),
        'missing_papers': 101 - len(found),
        'claim_issues': 0,
        'receipt_issues': 0,
        'stub_count': 0,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': 0,
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_tile_lib(conn):
    c = conn.cursor()
    issues = []
    
    c.execute("SELECT paper_number FROM tile_papers")
    found = {r[0] for r in c.fetchall() if r[0]}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)} (only {len(found)} papers in tile_papers)")
    
    # D/I/X claims via tile_claims
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM tile_claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[paper]:
            claim_counts[paper][status] = count
    
    for p in found:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # Code stubs via tile_code
    c.execute("SELECT COUNT(*) FROM tile_code WHERE status = 'stub' OR status = 'placeholder'")
    stub_count = c.fetchone()[0]
    if stub_count > 0:
        issues.append(f"Code stubs: {stub_count}")
    
    # CAM hashes
    c.execute("SELECT cam_hash FROM tiles")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    
    # B-family
    b_refs = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                b_refs += len(c.fetchall())
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs}")
    
    return {
        'name': 'TileLib',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': stub_count,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

def check_reforge_forge_lib(conn):
    c = conn.cursor()
    issues = []
    
    c.execute("SELECT paper_number FROM forge_papers")
    found = {r[0] for r in c.fetchall() if r[0]}
    missing = set(PAPERS) - found
    if missing:
        issues.append(f"Missing papers: {len(missing)} (only {len(found)} papers in forge_papers)")
    
    # D/I/X claims via forge_claims
    c.execute("SELECT paper_number, claim_status, COUNT(*) FROM forge_claims GROUP BY paper_number, claim_status")
    claim_counts = defaultdict(lambda: {'D': 0, 'I': 0, 'X': 0})
    for paper, status, count in c.fetchall():
        if status in claim_counts[paper]:
            claim_counts[paper][status] = count
    
    for p in found:
        for prefix in ['D', 'I', 'X']:
            if claim_counts[p][prefix] == 0:
                issues.append(f"{p}: {prefix}_claims = 0")
    
    # CAM hashes
    c.execute("SELECT cam_hash FROM forge_docs")
    hashes = [r[0] for r in c.fetchall() if r[0]]
    dupes = {h: n for h, n in Counter(hashes).items() if n > 1}
    
    # B-family
    b_refs = 0
    b_ref_details = []
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        try:
            c.execute(f"PRAGMA table_info({t})")
            cols = [col[1] for col in c.fetchall() if col[2].upper() in ('TEXT', 'VARCHAR', 'CHAR')]
            for col in cols:
                c.execute(f"SELECT {col} FROM {t} WHERE {col} LIKE '%B-family%' OR {col} LIKE '%B family%' OR {col} LIKE '%Bfamily%'")
                for row in c.fetchall():
                    if row[0] and any(b in row[0] for b in ['B-family', 'B family', 'Bfamily']):
                        b_refs += 1
                        b_ref_details.append(f"{t}.{col}: {row[0][:100]}")
        except:
            pass
    if b_refs:
        issues.append(f"B-family refs: {b_refs} ({b_ref_details[0] if b_ref_details else 'N/A'})")
    
    return {
        'name': 'ReForge_ForgeLib',
        'paper_count': len(found),
        'missing_papers': len(missing),
        'claim_issues': sum(1 for i in issues if '_claims = 0' in i),
        'receipt_issues': 0,
        'stub_count': 0,
        'sql_stub_count': 0,
        'grade_empty': 0,
        'cam_duplicates': len(dupes),
        'b_family_refs': b_refs,
        'issues': issues
    }

CHECKERS = {
    'CrystalLib': check_crystal_lib,
    'PaperLib': check_paper_lib,
    'CodeLib': check_code_lib,
    'SQLLib': check_sql_lib,
    'CMPLX-Standards': check_cmplx_standards,
    'cqekernel': check_cqekernel,
    'SystemsLib': check_systems_lib,
    'TileLib': check_tile_lib,
    'ReForge_ForgeLib': check_reforge_forge_lib,
}

def main(ctx):
    results = []
    all_cam_hashes = []
    total_stubs = 0
    total_sql_stubs = 0
    total_b_family = 0
    total_missing_papers = 0
    total_claim_issues = 0
    total_receipt_issues = 0
    total_grade_empty = 0
    
    for db_name, db_path in DATABASES.items():
        if not os.path.exists(db_path):
            results.append({
                'name': db_name,
                'paper_count': 0,
                'missing_papers': 101,
                'claim_issues': 0,
                'receipt_issues': 0,
                'stub_count': 0,
                'sql_stub_count': 0,
                'grade_empty': 0,
                'cam_duplicates': 0,
                'b_family_refs': 0,
                'issues': [f"Database not found: {db_path}"]
            })
            continue
        
        conn = connect(db_path)
        checker = CHECKERS[db_name]
        result = checker(conn)
        conn.close()
        
        results.append(result)
        total_stubs += result['stub_count']
        total_sql_stubs += result['sql_stub_count']
        total_b_family += result['b_family_refs']
        total_missing_papers += result['missing_papers']
        total_claim_issues += result['claim_issues']
        total_receipt_issues += result['receipt_issues']
        total_grade_empty += result['grade_empty']
        
        # Collect CAM hashes for global duplicate check
        if os.path.exists(db_path):
            conn = connect(db_path)
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table'")
            for t in [r[0] for r in c.fetchall()]:
                try:
                    c.execute(f"PRAGMA table_info({t})")
                    cols = [col[1] for col in c.fetchall()]
                    if 'cam_hash' in cols:
                        c.execute(f"SELECT cam_hash FROM {t} WHERE cam_hash IS NOT NULL")
                        all_cam_hashes.extend([r[0] for r in c.fetchall() if r[0]])
                except:
                    pass
            conn.close()
    
    # Global CAM duplicate check
    global_counts = Counter(all_cam_hashes)
    global_dupes = {h: n for h, n in global_counts.items() if n > 1}
    
    # Write report
    report_path = r'D:\Paper Ecology\FINAL_CONSISTENCY_REPORT.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# FINAL CONSISTENCY REPORT\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## 1. PER-DATABASE STATUS\n\n")
        for r in results:
            f.write(f"### {r['name']}\n")
            f.write(f"- **Papers found**: {r['paper_count']}\n")
            f.write(f"- **Papers missing**: {r['missing_papers']}\n")
            f.write(f"- **D/I/X claim issues**: {r['claim_issues']}\n")
            f.write(f"- **Code stubs**: {r['stub_count']}\n")
            f.write(f"- **SQL stubs**: {r['sql_stub_count']}\n")
            f.write(f"- **Empty grades**: {r['grade_empty']}\n")
            f.write(f"- **Receipt issues**: {r['receipt_issues']}\n")
            f.write(f"- **CAM duplicates (local)**: {r['cam_duplicates']}\n")
            f.write(f"- **B-family refs**: {r['b_family_refs']}\n")
            if r['issues']:
                f.write(f"- **Issues**:\n")
                for issue in r['issues']:
                    f.write(f"  - {issue}\n")
            f.write("\n")
        
        f.write("## 2. CROSS-DATABASE COMPARISON\n\n")
        f.write("| Database | Papers | D/I/X Issues | Stubs | SQL Stubs | Grade Empty | Receipts | B-Family |\n")
        f.write("|----------|--------|-------------|-------|-----------|-------------|----------|----------|\n")
        for r in results:
            f.write(f"| {r['name']} | {r['paper_count']} | {r['claim_issues']} | {r['stub_count']} | {r['sql_stub_count']} | {r['grade_empty']} | {r['receipt_issues']} | {r['b_family_refs']} |\n")
        f.write("\n")
        
        f.write("## 3. REMAINING INCONSISTENCIES\n\n")
        any_issues = False
        for r in results:
            if r['missing_papers'] > 0 or r['claim_issues'] > 0 or r['stub_count'] > 0 or r['sql_stub_count'] > 0 or r['grade_empty'] > 0 or r['receipt_issues'] > 0 or r['b_family_refs'] > 0 or r['cam_duplicates'] > 0:
                any_issues = True
                f.write(f"### {r['name']}\n")
                for issue in r['issues']:
                    f.write(f"- {issue}\n")
                f.write("\n")
        
        if not any_issues:
            f.write("No inconsistencies found.\n\n")
        
        f.write("## 4. TOTAL STUBS REMAINING\n\n")
        f.write(f"- **Total code stubs**: {total_stubs}\n")
        f.write(f"- **Total SQL stubs**: {total_sql_stubs}\n")
        f.write(f"- **Total stubs**: {total_stubs + total_sql_stubs}\n\n")
        
        f.write("## 5. TOTAL B-FAMILY REFERENCES REMAINING\n\n")
        f.write(f"- **Total B-family references**: {total_b_family}\n\n")
        
        f.write("## 6. GLOBAL CAM HASH UNIQUENESS\n\n")
        f.write(f"- **Total CAM hashes collected**: {len(all_cam_hashes)}\n")
        f.write(f"- **Unique CAM hashes**: {len(global_counts)}\n")
        f.write(f"- **Duplicate CAM hashes**: {len(global_dupes)}\n")
        if global_dupes:
            f.write(f"- **Most frequent duplicate**: {global_dupes.most_common(1)[0] if hasattr(global_dupes, 'most_common') else list(global_dupes.items())[0]}\n")
        f.write("\n")
        
        f.write("## 7. SUMMARY\n\n")
        f.write(f"| Metric | Count | Target | Status |\n")
        f.write(f"|--------|-------|--------|--------|\n")
        f.write(f"| Total stubs | {total_stubs + total_sql_stubs} | 0 | {'PASS' if total_stubs + total_sql_stubs == 0 else 'FAIL'} |\n")
        f.write(f"| Total B-family refs | {total_b_family} | 0 | {'PASS' if total_b_family == 0 else 'FAIL'} |\n")
        f.write(f"| Total missing papers | {total_missing_papers} | 0 | {'PASS' if total_missing_papers == 0 else 'FAIL'} |\n")
        f.write(f"| Total claim issues | {total_claim_issues} | 0 | {'PASS' if total_claim_issues == 0 else 'FAIL'} |\n")
        f.write(f"| Total receipt issues | {total_receipt_issues} | 0 | {'PASS' if total_receipt_issues == 0 else 'FAIL'} |\n")
        f.write(f"| Total empty grades | {total_grade_empty} | 0 | {'PASS' if total_grade_empty == 0 else 'FAIL'} |\n")
        f.write(f"| Global CAM duplicates | {len(global_dupes)} | 0 | {'PASS' if len(global_dupes) == 0 else 'FAIL'} |\n")
        f.write("\n")
    
    return {
        "report_path": report_path,
        "total_stubs": total_stubs + total_sql_stubs,
        "total_b_family": total_b_family,
        "total_missing_papers": total_missing_papers,
        "total_claim_issues": total_claim_issues,
        "total_receipt_issues": total_receipt_issues,
        "total_grade_empty": total_grade_empty,
        "global_cam_dupes": len(global_dupes)
    }
