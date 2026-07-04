import os
import re
import hashlib
import sqlite3
import json

PAPERLIB = r"D:\PaperLib"

def get_paper_files():
    files = {}
    for f in os.listdir(PAPERLIB):
        if not f.endswith('.md') or not f.startswith('paper-'):
            continue
        m = re.match(r'paper-(\d{2,3})__', f)
        if m:
            num = int(m.group(1))
            files[num] = f
    return files

def extract_metadata(num, filename, content):
    title = f"Paper {num}"
    title_patterns = [
        r'^#\s+Paper\s+\d+\s+[-—]\s+(.+)$',
        r'^#\s+(.+)$',
        r'^##\s+Paper\s+\d+\s+[-—]\s+(.+)$',
    ]
    for pattern in title_patterns:
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            title = match.group(1).strip()
            break
    
    band = "Unknown"
    band_match = re.search(r'\*\*Band\*\*:\s*(.+)', content)
    if band_match:
        band = band_match.group(1).strip()
    
    theorem_count = len(re.findall(r'^#{1,4}\s+(Theorem|Corollary)\s+\d', content, re.MULTILINE))
    
    claim_d = 0
    claim_i = 0
    claim_x = 0
    
    ledger_match = re.search(r'##\s+Claim Ledger.*?(?=##\s|$)', content, re.DOTALL)
    if ledger_match:
        ledger_text = ledger_match.group(0)
        claim_d = len(re.findall(r'\bD\b', ledger_text))
        claim_i = len(re.findall(r'\bI\b', ledger_text))
        claim_x = len(re.findall(r'\bX\b', ledger_text))
    
    open_count = 0
    obl_match = re.search(r'##\s+Open Obligations.*?(?=##\s|$)', content, re.DOTALL)
    if obl_match:
        open_count = len(re.findall(r'^\d+\.', obl_match.group(0), re.MULTILINE))
    
    refs = sorted(set(int(r) for r in re.findall(r'Paper\s+(\d+)', content)))
    
    return {
        'title': title,
        'band': band,
        'theorem_count': theorem_count,
        'claim_d': claim_d,
        'claim_i': claim_i,
        'claim_x': claim_x,
        'open_count': open_count,
        'refs': refs,
        'content': content
    }

def build_database(papers):
    db_path = os.path.join(PAPERLIB, 'cmplx_unified.db')
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    conn.execute('PRAGMA journal_mode=WAL')
    
    conn.execute('''
        CREATE TABLE papers (
            id INTEGER PRIMARY KEY,
            canonical_id TEXT UNIQUE,
            title TEXT,
            slug TEXT,
            filename TEXT,
            band TEXT,
            content_hash TEXT,
            size_bytes INTEGER,
            theorem_count INTEGER,
            claim_d_count INTEGER,
            claim_i_count INTEGER,
            claim_x_count INTEGER,
            open_obligation_count INTEGER,
            full_text TEXT
        )
    ''')
    
    conn.execute('''
        CREATE TABLE cross_references (
            id INTEGER PRIMARY KEY,
            from_canonical_id TEXT,
            to_canonical_id TEXT,
            context TEXT
        )
    ''')
    
    conn.execute('''
        CREATE TABLE content_address (
            hash TEXT PRIMARY KEY,
            canonical_id TEXT,
            content_type TEXT
        )
    ''')
    
    has_fts5 = False
    try:
        conn.execute('CREATE VIRTUAL TABLE papers_fts USING fts5(canonical_id, title, full_text)')
        has_fts5 = True
    except Exception as e:
        print(f"FTS5 not available: {e}")
        conn.execute('CREATE TABLE papers_search (canonical_id TEXT, title TEXT, full_text TEXT)')
    
    for num in sorted(papers.keys()):
        meta = papers[num]
        filename = meta['filename']
        content = meta['content']
        size = os.path.getsize(os.path.join(PAPERLIB, filename))
        h = hashlib.sha256(content.encode('utf-8')).hexdigest()
        canonical_id = f"Paper {num}"
        
        conn.execute('''
            INSERT INTO papers (canonical_id, title, slug, filename, band, content_hash, size_bytes,
            theorem_count, claim_d_count, claim_i_count, claim_x_count, open_obligation_count, full_text)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            canonical_id, meta['title'], filename.replace('.md', ''), filename,
            meta['band'], h, size, meta['theorem_count'], meta['claim_d'],
            meta['claim_i'], meta['claim_x'], meta['open_count'], content
        ))
        
        conn.execute('INSERT INTO content_address VALUES (?, ?, ?)', (h, canonical_id, 'paper'))
        
        for ref in meta['refs']:
            if ref != num:
                conn.execute(
                    'INSERT INTO cross_references (from_canonical_id, to_canonical_id, context) VALUES (?, ?, ?)',
                    (canonical_id, f"Paper {ref}", f"Cross-reference from {canonical_id}")
                )
        
        if has_fts5:
            conn.execute('INSERT INTO papers_fts (canonical_id, title, full_text) VALUES (?, ?, ?)',
                       (canonical_id, meta['title'], content))
        else:
            conn.execute('INSERT INTO papers_search (canonical_id, title, full_text) VALUES (?, ?, ?)',
                       (canonical_id, meta['title'], content))
    
    conn.commit()
    conn.close()
    print(f"Database built: {db_path}")
    return db_path, has_fts5

def write_master_index(papers, has_fts5):
    index_path = os.path.join(PAPERLIB, 'MASTER_INDEX.md')
    
    total_theorems = sum(p['theorem_count'] for p in papers.values())
    total_d = sum(p['claim_d'] for p in papers.values())
    total_i = sum(p['claim_i'] for p in papers.values())
    total_x = sum(p['claim_x'] for p in papers.values())
    total_open = sum(p['open_count'] for p in papers.values())
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# CMPLX Unified Paper Suite — Master Index\n\n")
        f.write("**Content-Addressed Database** for the 101-paper unified CMPLX framework.\n\n")
        f.write(f"- **Total Papers:** 101 (Papers 0-100)\n")
        f.write(f"- **Total Size:** {sum(os.path.getsize(os.path.join(PAPERLIB, p['filename'])) for p in papers.values())/1024/1024:.2f} MB\n")
        f.write(f"- **Total Theorems:** {total_theorems}\n")
        f.write(f"- **Total Claims:** D={total_d}, I={total_i}, X={total_x}\n")
        f.write(f"- **Total Open Obligations:** {total_open}\n")
        f.write(f"- **Database:** `cmplx_unified.db` (SQLite with {'FTS5' if has_fts5 else 'basic text'} search)\n")
        f.write(f"- **Query Script:** `query_papers.py`\n")
        f.write(f"- **Cross-Reference Manifest:** `CROSS_REFERENCES.json`\n\n")
        
        bands = {}
        for num, meta in papers.items():
            b = meta['band']
            bands[b] = bands.get(b, 0) + 1
        
        f.write("## Band Breakdown\n\n")
        for band, count in sorted(bands.items(), key=lambda x: -x[1]):
            f.write(f"- {band}: {count} papers\n")
        
        f.write("\n## Paper Index\n\n")
        f.write("| Paper | Title | Band | Thm | D | I | X | Open |\n")
        f.write("|-------|-------|------|-----|---|---|---|------|\n")
        for num in sorted(papers.keys()):
            meta = papers[num]
            title_short = meta['title'][:45] + '...' if len(meta['title']) > 45 else meta['title']
            band_short = meta['band'][:15] + '...' if len(meta['band']) > 15 else meta['band']
            f.write(f"| [{num}]({meta['filename']}) | {title_short} | {band_short} | {meta['theorem_count']} | {meta['claim_d']} | {meta['claim_i']} | {meta['claim_x']} | {meta['open_count']} |\n")
        
        f.write("\n## Cross-Reference Hub Papers\n\n")
        f.write("Papers with the most outgoing references (hubs):\n\n")
        hub_papers = sorted(papers.items(), key=lambda x: -len(x[1]['refs']))[:10]
        for num, meta in hub_papers:
            f.write(f"- **Paper {num}** ({meta['title'][:40]}): {len(meta['refs'])} references\n")
        
        f.write("\n## Open Obligation Hotspots\n\n")
        open_hotspots = sorted(papers.items(), key=lambda x: -x[1]['open_count'])[:10]
        for num, meta in open_hotspots:
            if meta['open_count'] > 0:
                f.write(f"- **Paper {num}** ({meta['title'][:40]}): {meta['open_count']} open obligations\n")
        
        f.write("\n## Content Addressing\n\n")
        f.write("Each paper is content-addressed by SHA-256. The `content_address` table in `cmplx_unified.db` maps:\n")
        f.write("- `hash` -> `canonical_id`\n")
        f.write("- Content integrity is verifiable by recomputing the hash.\n")
        f.write("\nTo verify a paper:\n")
        f.write("```python\n")
        f.write("import hashlib\n")
        f.write("with open('paper-NN.md', 'r') as f:\n")
        f.write("    h = hashlib.sha256(f.read().encode()).hexdigest()\n")
        f.write("# Compare against cmplx_unified.db content_address table\n")
        f.write("```\n")
    
    print(f"Master index written: {index_path}")
    return index_path

def write_cross_ref_manifest(papers):
    manifest = {}
    for num in sorted(papers.keys()):
        meta = papers[num]
        canonical_id = f"Paper {num}"
        manifest[canonical_id] = {
            "title": meta['title'],
            "band": meta['band'],
            "references": [f"Paper {r}" for r in meta['refs']],
            "referenced_by": []
        }
    
    for num in sorted(papers.keys()):
        canonical_id = f"Paper {num}"
        for ref in papers[num]['refs']:
            if ref != num:
                target = f"Paper {ref}"
                if target in manifest and canonical_id not in manifest[target]['referenced_by']:
                    manifest[target]['referenced_by'].append(canonical_id)
    
    manifest_path = os.path.join(PAPERLIB, 'CROSS_REFERENCES.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"Cross-reference manifest written: {manifest_path}")
    return manifest_path

def main():
    print("=== Building CMPLX Content-Addressed Memory Database ===")
    
    files = get_paper_files()
    print(f"Found {len(files)} papers")
    
    papers = {}
    for num, filename in sorted(files.items()):
        path = os.path.join(PAPERLIB, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        meta = extract_metadata(num, filename, content)
        meta['filename'] = filename
        papers[num] = meta
    
    db_path, has_fts5 = build_database(papers)
    index_path = write_master_index(papers, has_fts5)
    manifest_path = write_cross_ref_manifest(papers)
    
    print("\n=== Testing Database ===")
    conn = sqlite3.connect(db_path)
    total = conn.execute('SELECT COUNT(*) FROM papers').fetchone()[0]
    total_refs = conn.execute('SELECT COUNT(*) FROM cross_references').fetchone()[0]
    total_hashes = conn.execute('SELECT COUNT(*) FROM content_address').fetchone()[0]
    conn.close()
    
    print(f"Database entries: {total}")
    print(f"Cross-references: {total_refs}")
    print(f"Content hashes: {total_hashes}")
    print(f"\nAll artifacts built successfully in {PAPERLIB}")

if __name__ == '__main__':
    main()
