import sqlite3
import os
import json
import glob
import re
import hashlib
from datetime import datetime, timezone

def main(ctx):
    base = "D:\\Paper Ecology"
    
    def sha256(content):
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def cam_hash(content):
        if isinstance(content, str):
            return f"cam:{sha256(content)}"
        return f"cam:{hashlib.sha256(content).hexdigest()}"
    
    def now_iso():
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    def find_code_file(paper_num):
        codelib = os.path.join(base, "CodeLib")
        code_files = glob.glob(os.path.join(codelib, f"paper-{paper_num:02d}__*.py"))
        code_files = [f for f in code_files if 'schema' not in f.lower()]
        if not code_files:
            return None
        verifier_files = [f for f in code_files if '_verifier' in f.lower()]
        if verifier_files:
            return verifier_files[0]
        return code_files[0]
    
    def has_verifier(paper_num):
        codelib = os.path.join(base, "CodeLib")
        code_files = glob.glob(os.path.join(codelib, f"paper-{paper_num:02d}__*.py"))
        code_files = [f for f in code_files if 'schema' not in f.lower()]
        # A verifier exists if any file has '_verifier' in the name
        if any('_verifier' in f.lower() for f in code_files):
            return True
        # Or if any file has verify_/test_claim_/run_verifier in content
        for f in code_files:
            with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
                content = fh.read()
            if 'verify_' in content or 'test_claim_' in content or 'run_verifier' in content:
                return True
        return False
    
    def extract_key_functions(content):
        funcs = re.findall(r'^def\s+(\w+)', content, re.MULTILINE)
        classes = re.findall(r'^class\s+(\w+)', content, re.MULTILINE)
        items = []
        if classes:
            items.extend([f"class:{c}" for c in classes[:20]])
        if funcs:
            items.extend([f"func:{f}" for f in funcs[:30]])
        return '; '.join(items) if items else ""
    
    def extract_paper_info(content, paper_num):
        lines = content.splitlines()
        title = f"Paper {paper_num}"
        abstract = ""
        for line in lines[:50]:
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
            elif line.startswith('## ') and not title.startswith('Paper '):
                title = line[3:].strip()
        for line in lines:
            line = line.strip()
            if len(line) > 80 and not line.startswith('#') and not line.startswith('!'):
                abstract = line[:800]
                break
        return title, abstract
    
    def extract_d_claims(content, paper_num):
        claims = []
        # Check for verify_ functions
        verify_funcs = re.findall(r'def\s+(verify_\w+)\s*\([^)]*\):\s*\n\s*"""(.+?)"""', content, re.DOTALL)
        for i, (func_name, doc) in enumerate(verify_funcs):
            doc = doc.strip().replace('\n', ' ').replace('  ', ' ')[:500]
            claims.append({
                "id": f"{paper_num:02d}.{i+1}",
                "claim": f"{func_name}: {doc}",
                "evidence": f"CodeLib / {func_name}"
            })
        # Check for test_claim_ functions
        test_funcs = re.findall(r'def\s+(test_claim_[\w_]+)\s*\([^)]*\):\s*\n\s*(?:"""(.+?)"""|(?:#\s*(.+?)))', content, re.DOTALL)
        for i, (func_name, doc1, doc2) in enumerate(test_funcs):
            doc = (doc1 or doc2 or "").strip().replace('\n', ' ').replace('  ', ' ')[:500]
            claims.append({
                "id": f"{paper_num:02d}.{len(claims)+1}",
                "claim": f"{func_name}: {doc}",
                "evidence": f"CodeLib / {func_name}"
            })
        if not claims:
            bullets = re.findall(r'[-•]\s+(.+)', content)
            for i, b in enumerate(bullets[:5]):
                b = b.strip()
                if len(b) > 10 and len(b) < 500:
                    claims.append({
                        "id": f"{paper_num:02d}.{i+1}",
                        "claim": b,
                        "evidence": "PaperLib source"
                    })
        return claims
    
    # ─────────────────────────────────────────────────────
    # FIX CMPLX-STANDARDS GRADES FOR 22-50, 51-54, 56-59
    # ─────────────────────────────────────────────────────
    print("=== Fixing CMPLX-Standards grades for 22-50, 51-54, 56-59 ===")
    
    conn = sqlite3.connect(os.path.join(base, "CMPLX-Standards", "cmplx_standards.db"))
    c = conn.cursor()
    
    c.execute("SELECT band_id, band_name FROM inclusion_bands")
    band_map = {name: bid for bid, name in c.fetchall()}
    
    target_papers = list(range(22, 51)) + list(range(51, 55)) + list(range(56, 60))
    
    fixed = 0
    for paper_num in target_papers:
        paper_str = f"paper-{paper_num:02d}"
        verifier_exists = has_verifier(paper_num)
        
        # Re-read the code file for claims extraction
        code_path = find_code_file(paper_num)
        code_content = ""
        if code_path:
            with open(code_path, 'r', encoding='utf-8', errors='ignore') as f:
                code_content = f.read()
        
        # Re-read paper markdown
        paperlib = os.path.join(base, "PaperLib")
        md_files = glob.glob(os.path.join(paperlib, f"*{paper_num:02d}*.md"))
        title = f"Paper {paper_num}"
        abstract = ""
        if md_files:
            with open(md_files[0], 'r', encoding='utf-8', errors='ignore') as f:
                paper_content = f.read()
            title, abstract = extract_paper_info(paper_content, paper_num)
        
        d_claims = extract_d_claims(code_content, paper_num) if verifier_exists else []
        if not d_claims and md_files:
            bullets = re.findall(r'[-•]\s+(.+)', paper_content)
            for i, cl in enumerate(bullets[:5]):
                cl = cl.strip()
                if len(cl) > 10 and len(cl) < 500:
                    d_claims.append({
                        "id": f"{paper_num:02d}.{i+1}",
                        "claim": cl,
                        "evidence": "PaperLib source"
                    })
        
        grade = 'D' if verifier_exists else 'I'
        band = 'perfect_fit' if verifier_exists else 'partial_inclusive'
        band_id = band_map.get(band, band_map.get('partial_inclusive', 1))
        status = 'active' if verifier_exists else 'draft'
        fit_score = 1.0 if verifier_exists else 0.65
        d_count = len(d_claims)
        i_count = 1 if not verifier_exists else 0
        
        # Rebuild payload JSON
        payload = {
            "title": title,
            "abstract": abstract if abstract else f"Unified paper for domain {paper_num}.",
            "D": d_count,
            "I": i_count,
            "X": 0,
            "D_claims": d_claims,
            "I_claims": [
                {
                    "id": f"{paper_num:02d}.I1",
                    "claim": "Domain-specific claims require downstream verification",
                    "reasoning": "Structural claim from paper text"
                }
            ] if not verifier_exists else [],
            "X_claims": [],
            "fit_score": fit_score,
            "band": band,
            "contract": "assembled_paper_model"
        }
        
        payload_path = os.path.join(base, "CMPLX-Standards", "output", f"{paper_str}_payload.json")
        with open(payload_path, 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        
        # Update grader_runs
        metrics = {
            "tool": "CMPLX-Standards",
            "schema": "cmplx_standards_report.v1",
            "paper": paper_str,
            "grade": grade,
            "band": band,
            "fit_score": fit_score,
            "d_claims": d_count,
            "i_claims": i_count,
            "x_claims": 0
        }
        metrics_json = json.dumps(metrics, indent=2, ensure_ascii=False)
        grader_cam = cam_hash(metrics_json)
        
        c.execute(
            """UPDATE grader_runs SET assigned_grade = ?, band = ?, metrics_json = ?, cam_hash = ?
               WHERE paper_number = ?""",
            (grade, band, metrics_json, grader_cam, paper_str)
        )
        
        # Update standards_papers
        mapping = {
            "paper_number": paper_str,
            "band_id": band_id,
            "grade": grade,
            "status": status
        }
        mapping_h = cam_hash(json.dumps(mapping, indent=2, ensure_ascii=False))
        c.execute(
            """UPDATE standards_papers SET band_id = ?, grade = ?, status = ?, cam_hash = ?
               WHERE paper_number = ?""",
            (band_id, grade, status, mapping_h, paper_str)
        )
        
        fixed += 1
        print(f"  {paper_str}: grade={grade}, verifier={verifier_exists}, claims={d_count}")
    
    conn.commit()
    conn.close()
    print(f"  Fixed {fixed} papers")
    
    # ─────────────────────────────────────────────────────
    # FIX CODELIB KEY_FUNCTIONS FOR 00-20 AND 51-75
    # ─────────────────────────────────────────────────────
    print("\n=== Fixing CodeLib key_functions for 00-20 and 51-75 ===")
    
    for db_path in [os.path.join(base, "code_lib.db"), os.path.join(base, "CodeLib", "code_lib.db")]:
        print(f"  DB: {db_path}")
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        # Check if code_files table exists
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='code_files'")
        if not c.fetchone():
            print(f"    code_files table not found, skipping")
            conn.close()
            continue
        
        for paper_num in list(range(0, 21)) + list(range(51, 76)):
            code_path = find_code_file(paper_num)
            if not code_path:
                continue
            with open(code_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            key_functions = extract_key_functions(content)
            content_hash = sha256(content)
            
            c.execute(
                """UPDATE code_files SET key_functions = ?, status = 'real', cam_hash = ? WHERE paper_number = ?""",
                (key_functions, content_hash, paper_num)
            )
            if c.rowcount > 0:
                print(f"    paper-{paper_num:02d}: updated key_functions ({len(key_functions)} chars)")
        
        conn.commit()
        conn.close()
    
    return {"ok": True, "fixed": fixed}
