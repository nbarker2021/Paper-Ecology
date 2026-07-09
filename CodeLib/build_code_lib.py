import os
import re
import hashlib
import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional


def sha256_hash(content: str) -> str:
    """Generate SHA-256 CAM hash."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def extract_paper_number(filename: str) -> int:
    """Extract paper number from filename like paper-00__... or paper-100__..."""
    match = re.match(r'paper-(\d+)__', filename)
    if match:
        return int(match.group(1))
    return -1


def determine_status(file_path: Path) -> Tuple[str, str]:
    """Determine status (stub/real/verified) and verifier_type from file content."""
    content = file_path.read_text(encoding='utf-8')
    lines = content.splitlines()
    line_count = len(lines)
    
    # Check for stub indicators
    has_not_implemented = 'NotImplementedError' in content
    has_todo = 'TODO:' in content or '# TODO' in content
    has_stub_imports = 'lattice_forge' in content or 'cqekernel' in content
    
    # Real code: substantial line count, has actual implementations, few TODOs
    # Stub: small files with NotImplementedError, many TODOs, mostly imports
    if line_count < 80 and has_not_implemented and has_todo:
        return 'stub', 'property'
    elif line_count < 80 and has_stub_imports and not any(k in content for k in ['class ', 'def ']) and not has_not_implemented:
        return 'stub', 'property'
    elif line_count >= 80 and has_stub_imports and has_not_implemented:
        # Some files have both real code and stub sections
        if content.count('def ') > 3 and 'class ' in content:
            return 'real', 'unit'
        else:
            return 'stub', 'property'
    elif line_count >= 80 and (content.count('def ') > 2 or 'class ' in content):
        if 'verify_' in content and not has_not_implemented:
            return 'verified', 'integration'
        return 'real', 'unit'
    else:
        return 'stub', 'property'


def extract_description(content: str) -> str:
    """Extract description from docstring or header comments."""
    lines = content.splitlines()
    description_parts = []
    in_docstring = False
    
    for line in lines[:30]:
        stripped = line.strip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            in_docstring = True
            stripped = stripped.lstrip('"').lstrip("'")
            if stripped.endswith('"""') or stripped.endswith("'''"):
                stripped = stripped.rstrip('"').rstrip("'")
                description_parts.append(stripped)
                break
            if stripped:
                description_parts.append(stripped)
            continue
        if in_docstring:
            if stripped.endswith('"""') or stripped.endswith("'''"):
                stripped = stripped.rstrip('"').rstrip("'")
                description_parts.append(stripped)
                break
            description_parts.append(stripped)
    
    if description_parts:
        desc = ' '.join(description_parts).strip()
        desc = re.sub(r'\s+', ' ', desc).strip()
        if desc and len(desc) > 10:
            return desc[:500]
    
    domain_match = re.search(r'Domain:\s*([^\n]+)', content)
    if domain_match:
        return domain_match.group(1).strip()[:500]
    
    paper_match = re.search(r'Paper\s+\d+\s+[—\-]\s*([^\n]+)', content)
    if paper_match:
        return paper_match.group(1).strip()[:500]
    
    return "No description extracted"


def extract_key_functions(content: str) -> str:
    """Extract function and class names from code."""
    class_pattern = re.compile(r'^class\s+(\w+)', re.MULTILINE)
    func_pattern = re.compile(r'^def\s+(\w+)', re.MULTILINE)
    
    classes = class_pattern.findall(content)
    funcs = func_pattern.findall(content)
    
    all_items = []
    if classes:
        all_items.extend([f"class:{c}" for c in classes[:20]])
    if funcs:
        all_items.extend([f"func:{f}" for f in funcs[:30]])
    
    return '; '.join(all_items) if all_items else ""


def extract_claims(content: str, paper_number: int) -> List[Dict[str, Any]]:
    """Extract D/I/X claims from content."""
    claims = []
    
    claim_section = re.search(r'Claims:?(.*?)(?=Verifiers:?|Recovered|# ---|# -|def |class |$)', content, re.DOTALL | re.IGNORECASE)
    if claim_section:
        claim_text = claim_section.group(1)
        bullet_claims = re.findall(r'[-•]\s+(.+)', claim_text)
        for i, claim in enumerate(bullet_claims):
            claim = claim.strip()
            if claim and len(claim) > 10:
                claims.append({
                    'claim_id': f'C-{paper_number:03d}-{i+1:03d}',
                    'claim_text': claim[:1000],
                    'claim_status': 'D' if 'verified' in claim.lower() or 'proven' in claim.lower() else 'I'
                })
    
    verifier_section = re.search(r'Verifiers:?(.*?)(?=# ---|# -|def |class |$)', content, re.DOTALL | re.IGNORECASE)
    if verifier_section and len(claims) < 5:
        verifier_text = verifier_section.group(1)
        numbered = re.findall(r'\d+\.\s+(.+)', verifier_text)
        for i, v in enumerate(numbered):
            v = v.strip()
            if v and len(v) > 10:
                claims.append({
                    'claim_id': f'C-{paper_number:03d}-{len(claims)+i+1:03d}',
                    'claim_text': f'Verifier: {v[:1000]}',
                    'claim_status': 'D'
                })
    
    if not claims:
        verify_funcs = re.findall(r'def\s+(verify_\w+)\s*\([^)]*\):\s*\n\s*"""(.+?)"""', content, re.DOTALL)
        for i, (func_name, doc) in enumerate(verify_funcs):
            doc = doc.strip().replace('\n', ' ').replace('  ', ' ')[:500]
            claims.append({
                'claim_id': f'C-{paper_number:03d}-{i+1:03d}',
                'claim_text': f'{func_name}: {doc}',
                'claim_status': 'D'
            })
    
    if not claims:
        if 'NotImplementedError' in content:
            claims.append({
                'claim_id': f'C-{paper_number:03d}-001',
                'claim_text': 'Stub verifier placeholders present; implementation pending.',
                'claim_status': 'X'
            })
        else:
            claims.append({
                'claim_id': f'C-{paper_number:03d}-001',
                'claim_text': 'Programmatic claims for this paper are implemented in attached code.',
                'claim_status': 'I'
            })
    
    return claims


def extract_b_family_sources(content: str, paper_number: int) -> List[Dict[str, Any]]:
    """Extract B-family source references from imports and comments."""
    sources = []
    
    b_family_modules = {
        'lattice_forge': 'B_family_lattice_forge',
        'cqekernel': 'B_family_forge',
        'runtime': 'B_family_forge',
    }
    
    for module, source_type in b_family_modules.items():
        pattern = re.compile(rf'from\s+{module}\.([\w.]+)')
        matches = pattern.findall(content)
        for match in set(matches):
            sources.append({
                'source_type': source_type,
                'original_path': f'{module}.{match}',
                'stripped': True
            })
    
    path_refs = re.findall(r'[D]:/([A-Za-z_]+)/', content)
    for ref in set(path_refs):
        if ref in ['CodeLib', 'CAMLib', 'SQLLib', 'CQE_CMPLX']:
            source_type_map = {'CodeLib': 'B_family_forge', 'CAMLib': 'B_family_lattice_forge', 'SQLLib': 'B_family_lattice_forge', 'CQE_CMPLX': 'B_family_forge'}
            sources.append({
                'source_type': source_type_map.get(ref, 'B_family_forge'),
                'original_path': f'D:/{ref}/',
                'stripped': True
            })
    
    seen = set()
    deduped = []
    for s in sources:
        key = (s['source_type'], s['original_path'])
        if key not in seen:
            seen.add(key)
            deduped.append(s)
    
    return deduped


def build_database():
    base_dir = Path('D:/Paper Ecology/CodeLib')
    db_path = base_dir / 'code_lib.db'
    
    if db_path.exists():
        db_path.unlink()
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    cursor.executescript('''
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
    
    CREATE TABLE code_papers (
        mapping_id TEXT PRIMARY KEY,
        paper_number INTEGER,
        code_id TEXT,
        role TEXT CHECK(role IN ('verifier', 'implementation', 'spec')),
        status TEXT,
        cam_hash TEXT,
        FOREIGN KEY (code_id) REFERENCES code_files(code_id)
    );
    
    CREATE TABLE cam_hashes (
        cam_hash TEXT PRIMARY KEY,
        content_type TEXT,
        content_id TEXT,
        created_at TEXT
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
    ''')
    
    paper_files = sorted(base_dir.glob('paper-*.py'))
    print(f"Found {len(paper_files)} paper files")
    
    for paper_path in paper_files:
        filename = paper_path.name
        paper_number = extract_paper_number(filename)
        if paper_number < 0:
            print(f"Could not extract paper number from {filename}")
            continue
        
        content = paper_path.read_text(encoding='utf-8')
        status, verifier_type = determine_status(paper_path)
        description = extract_description(content)
        key_functions = extract_key_functions(content)
        file_path_str = str(paper_path)
        
        content_hash = sha256_hash(content)
        code_id = f'A-P{paper_number:03d}-CODE'
        
        cursor.execute('''
            INSERT INTO code_files (code_id, file_name, description, language, file_path, key_functions, paper_number, status, verifier_type, cam_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (code_id, filename, description, 'python', file_path_str, key_functions, paper_number, status, verifier_type, content_hash))
        
        cursor.execute('''
            INSERT OR IGNORE INTO cam_hashes (cam_hash, content_type, content_id, created_at)
            VALUES (?, ?, ?, ?)
        ''', (content_hash, 'code_file', code_id, datetime.now().isoformat()))
        
        claims = extract_claims(content, paper_number)
        for claim in claims:
            claim_hash = sha256_hash(claim['claim_text'])
            cursor.execute('''
                INSERT INTO code_claims (claim_id, paper_number, claim_text, claim_status, code_file_id, evidence, cam_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (claim['claim_id'], paper_number, claim['claim_text'], claim['claim_status'], code_id, f"Evidence from {filename}", claim_hash))
            
            cursor.execute('''
                INSERT OR IGNORE INTO cam_hashes (cam_hash, content_type, content_id, created_at)
                VALUES (?, ?, ?, ?)
            ''', (claim_hash, 'claim', claim['claim_id'], datetime.now().isoformat()))
        
        mapping_id = f'MAP-P{paper_number:03d}-{code_id}'
        role = 'implementation' if status in ('real', 'verified') else 'spec'
        cursor.execute('''
            INSERT INTO code_papers (mapping_id, paper_number, code_id, role, status, cam_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (mapping_id, paper_number, code_id, role, status, content_hash))
        
        if status == 'stub':
            sources = extract_b_family_sources(content, paper_number)
            if not sources:
                sources.append({
                    'source_type': 'B_family_lattice_forge',
                    'original_path': f'lattice_forge.paper_{paper_number:02d}_stub',
                    'stripped': True
                })
            
            for i, source in enumerate(sources):
                source_id = f'SRC-P{paper_number:03d}-{i+1:03d}'
                source_hash = sha256_hash(source['original_path'])
                cursor.execute('''
                    INSERT INTO code_sources (source_id, code_id, source_type, original_path, stripped, cam_hash)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (source_id, code_id, source['source_type'], source['original_path'], int(source['stripped']), source_hash))
                
                cursor.execute('''
                    INSERT OR IGNORE INTO cam_hashes (cam_hash, content_type, content_id, created_at)
                    VALUES (?, ?, ?, ?)
                ''', (source_hash, 'source_reference', source_id, datetime.now().isoformat()))
        else:
            source_id = f'SRC-P{paper_number:03d}-001'
            source_hash = sha256_hash(file_path_str)
            cursor.execute('''
                INSERT INTO code_sources (source_id, code_id, source_type, original_path, stripped, cam_hash)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (source_id, code_id, 'original', file_path_str, 0, source_hash))
            
            cursor.execute('''
                INSERT OR IGNORE INTO cam_hashes (cam_hash, content_type, content_id, created_at)
                VALUES (?, ?, ?, ?)
            ''', (source_hash, 'source_reference', source_id, datetime.now().isoformat()))
    
    conn.commit()
    
    cursor.execute('SELECT COUNT(*) FROM code_files')
    print(f"code_files: {cursor.fetchone()[0]}")
    cursor.execute('SELECT COUNT(*) FROM code_claims')
    print(f"code_claims: {cursor.fetchone()[0]}")
    cursor.execute('SELECT COUNT(*) FROM code_papers')
    print(f"code_papers: {cursor.fetchone()[0]}")
    cursor.execute('SELECT COUNT(*) FROM cam_hashes')
    print(f"cam_hashes: {cursor.fetchone()[0]}")
    cursor.execute('SELECT COUNT(*) FROM code_sources')
    print(f"code_sources: {cursor.fetchone()[0]}")
    
    cursor.execute('SELECT status, COUNT(*) FROM code_files GROUP BY status')
    print("\nStatus distribution:")
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}")
    
    conn.close()
    print("\nDatabase built successfully.")
    
    return db_path


def export_schema(db_path: Path, schema_path: Path):
    """Export database schema to SQL file."""
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    schema_lines = []
    schema_lines.append("-- CodeLib SQLite Schema")
    schema_lines.append("-- A-family naming (paper-00 through paper-100)")
    schema_lines.append("-- LCR kernel, D/I/X claims, CAM hashes")
    schema_lines.append("")
    
    cursor.execute('''
        SELECT sql FROM sqlite_master 
        WHERE type='table' AND name IN ('code_files', 'code_claims', 'code_papers', 'cam_hashes', 'code_sources')
        ORDER BY name
    ''')
    
    for row in cursor.fetchall():
        if row[0]:
            schema_lines.append(row[0] + ";")
            schema_lines.append("")
    
    cursor.execute('''
        SELECT sql FROM sqlite_master 
        WHERE type='index' AND tbl_name IN ('code_files', 'code_claims', 'code_papers', 'cam_hashes', 'code_sources')
        AND sql IS NOT NULL
        ORDER BY name
    ''')
    
    for row in cursor.fetchall():
        if row[0]:
            schema_lines.append(row[0] + ";")
            schema_lines.append("")
    
    conn.close()
    
    schema_path.write_text('\n'.join(schema_lines), encoding='utf-8')
    print(f"Schema exported to {schema_path}")


def main(ctx):
    base_dir = Path('D:/Paper Ecology/CodeLib')
    db_path = build_database()
    schema_path = base_dir / 'code_lib_schema.sql'
    export_schema(db_path, schema_path)
    return {"db_path": str(db_path), "schema_path": str(schema_path)}


if __name__ == '__main__':
    class FakeCtx:
        pass
    main(FakeCtx())
