import sqlite3, os, re
from collections import defaultdict

root = r"D:\Paper Ecology"

def normalize_paper_number(pn):
    if pn is None:
        return None
    if isinstance(pn, int):
        if 0 <= pn <= 100:
            return f'paper-{pn:02d}' if pn < 100 else f'paper-{pn}'
        return None
    s = str(pn).strip().lower()
    m = re.match(r'paper[-_]?(\d+)', s)
    if m:
        num = int(m.group(1))
        if 0 <= num <= 100:
            return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
    try:
        num = int(s)
        if 0 <= num <= 100:
            return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
    except ValueError:
        pass
    return None

# 1. Papers with D-claims in each lib
all_papers = {f'paper-{i:02d}' if i < 100 else f'paper-{i}' for i in range(101)}

d_claim_papers = defaultdict(set)

# PaperLib claims
conn = sqlite3.connect(os.path.join(root, 'PaperLib', 'paper_lib.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['PaperLib'].add(pn)
conn.close()

# CodeLib code_claims
conn = sqlite3.connect(os.path.join(root, 'CodeLib', 'code_lib.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM code_claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['CodeLib'].add(pn)
conn.close()

# SQLLib sql_claims
conn = sqlite3.connect(os.path.join(root, 'SQLLib', 'sql_lib.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM sql_claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['SQLLib'].add(pn)
conn.close()

# CMPLX-Standards - no direct claim table, but check grader_runs or contracts? 
# Actually CMPLX-Standards doesn't have claim_status D. We'll skip for D-claims.

# CrystalLib claims
conn = sqlite3.connect(os.path.join(root, 'CrystalLib', 'crystal_lib.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['CrystalLib'].add(pn)
conn.close()

# ReForge forge_claims
conn = sqlite3.connect(os.path.join(root, 'ReForge_ForgeLib', 'reforge_forge_lib.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM forge_claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['ReForge_ForgeLib'].add(pn)
conn.close()

# TileLib tile_claims
conn = sqlite3.connect(os.path.join(root, 'TileLib', 'tile_lib.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM tile_claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['TileLib'].add(pn)
conn.close()

# cqekernel kernel_claims
conn = sqlite3.connect(os.path.join(root, 'cqekernel', 'cqekernel.db'))
cur = conn.cursor()
for pn, status in cur.execute("SELECT paper_number, claim_status FROM kernel_claims").fetchall():
    pn = normalize_paper_number(pn)
    if pn and status and str(status).upper() == 'D':
        d_claim_papers['cqekernel'].add(pn)
conn.close()

# SystemsLib doesn't have claims table with D status

any_d = set()
for s in d_claim_papers.values():
    any_d |= s
no_d = sorted(all_papers - any_d)
print(f"Papers with NO D-claims in any Lib: {len(no_d)} — {no_d}")

# 2. Papers with no receipts in CrystalLib
conn = sqlite3.connect(os.path.join(root, 'CrystalLib', 'crystal_lib.db'))
cur = conn.cursor()
receipt_papers = set()
for pn, in cur.execute("SELECT DISTINCT paper_number FROM receipts WHERE paper_number IS NOT NULL").fetchall():
    pn = normalize_paper_number(pn)
    if pn:
        receipt_papers.add(pn)
conn.close()
no_receipts = sorted(all_papers - receipt_papers)
print(f"Papers with NO receipts in CrystalLib: {len(no_receipts)} — {no_receipts}")

# 3. Papers with empty CMPLX-Standards (no standards_papers entry)
conn = sqlite3.connect(os.path.join(root, 'CMPLX-Standards', 'cmplx_standards.db'))
cur = conn.cursor()
std_papers = set()
for pn, in cur.execute("SELECT DISTINCT paper_number FROM standards_papers WHERE paper_number IS NOT NULL").fetchall():
    pn = normalize_paper_number(pn)
    if pn:
        std_papers.add(pn)
conn.close()
no_std = sorted(all_papers - std_papers)
print(f"Papers with NO CMPLX-Standards entry: {len(no_std)} — {no_std}")

# 4. Papers with no code verifier in CodeLib
# Check code_files for verifier_type or status indicating a verifier
conn = sqlite3.connect(os.path.join(root, 'CodeLib', 'code_lib.db'))
cur = conn.cursor()
verifier_papers = set()
for pn, status, vtype in cur.execute("SELECT paper_number, status, verifier_type FROM code_files").fetchall():
    pn = normalize_paper_number(pn)
    if pn:
        s = (status or '').lower()
        v = (vtype or '').lower()
        if 'verifier' in s or 'verifier' in v or 'real' in s or s == 'active':
            verifier_papers.add(pn)
# Also check code_papers for role/status
for pn, role, status in cur.execute("SELECT paper_number, role, status FROM code_papers").fetchall():
    pn = normalize_paper_number(pn)
    if pn:
        r = (role or '').lower()
        s = (status or '').lower()
        if 'verifier' in r or 'verifier' in s or 'real' in s or s == 'active':
            verifier_papers.add(pn)
conn.close()
no_verifier = sorted(all_papers - verifier_papers)
print(f"Papers with NO code verifier: {len(no_verifier)} — {no_verifier}")

# Summary of D-claims per lib
print("\nD-claim coverage by lib:")
for lib, papers in sorted(d_claim_papers.items()):
    print(f"  {lib}: {len(papers)} papers")
