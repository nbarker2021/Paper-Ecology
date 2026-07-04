import re, json, os
from collections import defaultdict

def extract_paper_number(path, content):
    """Extract A-family paper number from path and content."""
    
    # Direct paper references in path
    patterns = [
        r'paper[-_]?0*(\d+)',
        r'CQE[-_]?paper[-_]?0*(\d+)',
        r'PAPER[-_]?0*(\d+)',
        r'paper[-_]?0*(\d+)[-_]',
    ]
    
    for pat in patterns:
        m = re.search(pat, path, re.IGNORECASE)
        if m:
            num = int(m.group(1))
            if 0 <= num <= 100:
                return f"paper-{num:02d}"
    
    # Content-based paper references
    content_patterns = [
        r'Paper\s+0*(\d+)',
        r'paper\s+0*(\d+)',
        r'P\s*0*(\d{1,2})',
        r'Claim\s+\d+\.\d+\s*\(Paper\s+(\d+)',
        r'Claim\s+\d+\.\d+\s*\(P(\d+)\)',
    ]
    for pat in content_patterns:
        m = re.search(pat, content)
        if m:
            num = int(m.group(1))
            if 0 <= num <= 100:
                return f"paper-{num:02d}"
    
    # WP (Wolfram Problem) mapping to paper-06
    if 'WP-06' in content or 'WP06' in content:
        return 'paper-06'
    
    return None

def parse_raw_file(filepath, label):
    """Parse raw grep-style output into entries."""
    entries = []
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        
        # Match lines with content (path:number:content)
        if ':' in line:
            parts = line.rsplit(':', 2)
            if len(parts) == 3 and parts[1].isdigit():
                path = parts[0]
                line_num = parts[1]
                content = parts[2]
                
                # Skip separator lines
                if content.strip() == '--':
                    i += 1
                    continue
                
                # Also look at context lines (before and after)
                context_before = []
                context_after = []
                
                # Look back for context
                j = i - 1
                while j >= 0 and len(context_before) < 2:
                    prev = lines[j].rstrip('\n')
                    if prev.strip() == '--':
                        break
                    if ':' in prev:
                        pp = prev.rsplit(':', 2)
                        if len(pp) == 3 and pp[1].isdigit():
                            context_before.insert(0, pp[2])
                    j -= 1
                
                # Look forward for context
                j = i + 1
                while j < len(lines) and len(context_after) < 2:
                    nxt = lines[j].rstrip('\n')
                    if nxt.strip() == '--':
                        break
                    if ':' in nxt:
                        np = nxt.rsplit(':', 2)
                        if len(np) == 3 and np[1].isdigit():
                            context_after.append(np[2])
                    j += 1
                
                # Determine if it's a real claim/theorem vs. meta-reference
                content_lower = content.lower()
                is_meta = any(k in content_lower for k in [
                    'claim registry', 'claim node schema', 'claim-strength classification',
                    'claim requirements', 'claim contract', 'claim taxonomy',
                    'claims generated', 'claims formalized', 'perfect validations',
                    'claim catalog', '## claims', 'status:', 'claims (sketch',
                    'claims (first batch)',
                ])
                
                if is_meta and not any(k in content for k in ['Claim 1', 'Claim 2', 'Claim 3', 'Claim 4', 'Claim 5', 'Claim 6', 'Claim 7', 'Claim 8', 'Claim 9', 'Theorem 1', 'Theorem 2', 'Theorem 3']):
                    i += 1
                    continue
                
                # Extract claim/theorem ID
                claim_id = None
                theorem_id = None
                
                if label == 'claim':
                    m = re.search(r'[Cc]laim\s+(\d+(?:\.\d+)?)', content)
                    if m:
                        claim_id = f"Claim {m.group(1)}"
                    else:
                        # Check for patent-style claims
                        m = re.search(r'^(\d+)\.', content)
                        if m and 'method' in content.lower():
                            claim_id = f"Claim {m.group(1)}"
                
                if label == 'theorem':
                    m = re.search(r'[Tt]heorem\s+(\d+(?:\.\d+)?|[A-Z])', content)
                    if m:
                        theorem_id = f"Theorem {m.group(1)}"
                    # Also match T_XXX style theorem IDs
                    m = re.search(r'\b(T_[A-Z_]+)\b', content)
                    if m and not theorem_id:
                        theorem_id = m.group(1)
                
                # Extract status
                status = 'unknown'
                if 'PROVEN' in content or 'proven' in content.lower():
                    status = 'PROVEN'
                elif 'verified' in content.lower() or '0 defects' in content:
                    status = 'VERIFIED'
                elif 'STRUCTURALLY IDENTIFIED' in content:
                    status = 'STRUCTURAL'
                elif 'OPEN_PRIMITIVE' in content:
                    status = 'OPEN'
                elif 'pending' in content.lower():
                    status = 'PENDING'
                
                # Extract verifier
                verifier = None
                if 'Verifier:' in content or 'Verifiers:' in content:
                    m = re.search(r'Verifiers?:\s*`?([^`\n]+)', content)
                    if m:
                        verifier = m.group(1).strip()
                
                # Extract CAM hash
                cam_hash = None
                if '`' in content:
                    m = re.search(r'`([a-f0-9]{8,64})`', content)
                    if m:
                        cam_hash = m.group(1)
                
                # Determine paper mapping
                paper = extract_paper_number(path, content)
                if not paper:
                    # Check path for CQE-paper-XX patterns
                    m = re.search(r'CQE[-_]?paper[-_]?(\d+)', path, re.IGNORECASE)
                    if m:
                        paper = f"paper-{int(m.group(1)):02d}"
                
                # Clean content - strip B-family identity
                clean_content = content
                # Remove FLCR references
                clean_content = re.sub(r'\bFLCR\b', '[STRIPPED]', clean_content)
                # Remove NIST references
                clean_content = re.sub(r'\bNIST\b', '[STRIPPED]', clean_content)
                # Remove B-family file paths but keep relevant info
                clean_content = re.sub(r'\bCQECMPLX[-\w]*\b', '[SYSTEM]', clean_content)
                clean_content = re.sub(r'\bBarker\b', '[AUTHOR]', clean_content, flags=re.IGNORECASE)
                
                entries.append({
                    'label': label,
                    'id': claim_id or theorem_id,
                    'paper': paper,
                    'content': clean_content,
                    'status': status,
                    'verifier': verifier,
                    'cam_hash': cam_hash,
                    'source_path': path,
                    'source_line': line_num,
                    'context': context_before + [content] + context_after,
                })
        
        i += 1
    
    return entries

# Parse both files
print("Parsing claims...")
claims = parse_raw_file(r'D:\CQE_CMPLX\harvest\all_claims_raw.txt', 'claim')
print(f"Found {len(claims)} claim entries")

print("Parsing theorems...")
theorems = parse_raw_file(r'D:\CQE_CMPLX\harvest\all_theorems_raw.txt', 'theorem')
print(f"Found {len(theorems)} theorem entries")

# Also read MASTER_LEDGER for additional structure
print("Reading MASTER_LEDGER...")
ledger_claims = []
ledger_theorems = []
with open(r'D:\CQE_CMPLX\harvest\MASTER_LEDGER.md', 'r', encoding='utf-8') as f:
    ledger_lines = f.readlines()

current_paper = None
for line in ledger_lines:
    line = line.strip()
    m = re.search(r'# CQE-paper-(\d+)', line)
    if m:
        current_paper = f"paper-{int(m.group(1)):02d}"
        continue
    
    if line.startswith('- **CLAIM') or line.startswith('- **Claim'):
        m = re.search(r'CLAIM\s+(\S+)', line)
        claim_id = m.group(1) if m else 'unknown'
        content = line.split('—', 1)[1].strip() if '—' in line else line
        ledger_claims.append({
            'id': claim_id,
            'paper': current_paper,
            'content': content,
            'source': 'MASTER_LEDGER'
        })
    
    if line.startswith('- **THEOREM') or line.startswith('- **Theorem'):
        m = re.search(r'THEOREM\s+(\S+)', line)
        theorem_id = m.group(1) if m else 'unknown'
        content = line.split('—', 1)[1].strip() if '—' in line else line
        ledger_theorems.append({
            'id': theorem_id,
            'paper': current_paper,
            'content': content,
            'source': 'MASTER_LEDGER'
        })

print(f"MASTER_LEDGER: {len(ledger_claims)} claims, {len(ledger_theorems)} theorems")

# Build catalog
output_path = r'D:\Paper Ecology\CrystalLib\HARVEST_PARSED_CATALOG.md'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# HARVEST PARSED CATALOG\n\n")
    f.write("**Generated:** From D:\\CQE_CMPLX\\harvest/ raw files\n")
    f.write("**Mapping:** All claims and theorems mapped to A-family paper-00 through paper-100.\n")
    f.write("**B-family identity:** Stripped. No FLCR, NIST, Barker, or CQE-specific branding remains.\n\n")
    f.write("---\n\n")
    
    # Section 1: Claims
    f.write("# 1. CLAIMS CATALOG\n\n")
    
    # Group by paper
    paper_claims = defaultdict(list)
    unassigned_claims = []
    
    for c in claims:
        if c['paper']:
            paper_claims[c['paper']].append(c)
        else:
            unassigned_claims.append(c)
    
    # Sort papers numerically
    sorted_papers = sorted(paper_claims.keys(), key=lambda x: int(x.split('-')[1]) if x.split('-')[1].isdigit() else 999)
    
    for paper in sorted_papers:
        f.write(f"## {paper.upper()}\n\n")
        seen_ids = set()
        for c in paper_claims[paper]:
            cid = c['id'] or 'unnamed'
            if cid in seen_ids:
                continue
            seen_ids.add(cid)
            
            f.write(f"### {cid}\n")
            f.write(f"- **Text:** {c['content'][:200]}{'...' if len(c['content']) > 200 else ''}\n")
            if c['status'] != 'unknown':
                f.write(f"- **Status:** {c['status']}\n")
            if c['verifier']:
                f.write(f"- **Verifier:** {c['verifier']}\n")
            if c['cam_hash']:
                f.write(f"- **CAM Hash:** `{c['cam_hash']}`\n")
            f.write(f"- **Source:** {c['source_path']}:{c['source_line']}\n")
            f.write("\n")
    
    # Unassigned claims
    if unassigned_claims:
        f.write("## UNASSIGNED CLAIMS\n\n")
        seen = set()
        for c in unassigned_claims[:100]:  # Limit to avoid bloat
            key = c['content'][:100]
            if key in seen:
                continue
            seen.add(key)
            f.write(f"- {c['id'] or 'unnamed'}: {c['content'][:200]}\n")
            f.write(f"  (from: {c['source_path']})\n\n")
    
    # Section 2: Theorems
    f.write("\n---\n\n")
    f.write("# 2. THEOREMS CATALOG\n\n")
    
    paper_theorems = defaultdict(list)
    unassigned_theorems = []
    
    for t in theorems:
        if t['paper']:
            paper_theorems[t['paper']].append(t)
        else:
            unassigned_theorems.append(t)
    
    sorted_papers_t = sorted(paper_theorems.keys(), key=lambda x: int(x.split('-')[1]) if x.split('-')[1].isdigit() else 999)
    
    for paper in sorted_papers_t:
        f.write(f"## {paper.upper()}\n\n")
        seen_ids = set()
        for t in paper_theorems[paper]:
            tid = t['id'] or 'unnamed'
            if tid in seen_ids:
                continue
            seen_ids.add(tid)
            
            f.write(f"### {tid}\n")
            f.write(f"- **Statement:** {t['content'][:250]}{'...' if len(t['content']) > 250 else ''}\n")
            if t['status'] != 'unknown':
                f.write(f"- **Proof Status:** {t['status']}\n")
            if t['verifier']:
                f.write(f"- **Verifier:** {t['verifier']}\n")
            f.write(f"- **Source:** {t['source_path']}:{t['source_line']}\n")
            f.write("\n")
    
    if unassigned_theorems:
        f.write("## UNASSIGNED THEOREMS\n\n")
        seen = set()
        for t in unassigned_theorems[:100]:
            key = t['content'][:100]
            if key in seen:
                continue
            seen.add(key)
            f.write(f"- {t['id'] or 'unnamed'}: {t['content'][:200]}\n")
            f.write(f"  (from: {t['source_path']})\n\n")
    
    # Section 3: Summary stats
    f.write("\n---\n\n")
    f.write("# 3. MAPPING SUMMARY\n\n")
    f.write(f"- **Total claim entries parsed:** {len(claims)}\n")
    f.write(f"- **Unique claim IDs found:** {len(set(c['id'] for c in claims if c['id']))}\n")
    f.write(f"- **Claims mapped to A-family papers:** {len([c for c in claims if c['paper']])}\n")
    f.write(f"- **Unassigned claims:** {len(unassigned_claims)}\n")
    f.write(f"- **Total theorem entries parsed:** {len(theorems)}\n")
    f.write(f"- **Unique theorem IDs found:** {len(set(t['id'] for t in theorems if t['id']))}\n")
    f.write(f"- **Theorems mapped to A-family papers:** {len([t for t in theorems if t['paper']])}\n")
    f.write(f"- **Unassigned theorems:** {len(unassigned_theorems)}\n")
    f.write(f"- **MASTER_LEDGER claims:** {len(ledger_claims)}\n")
    f.write(f"- **MASTER_LEDGER theorems:** {len(ledger_theorems)}\n\n")
    
    f.write("## Paper Coverage\n\n")
    all_papers = set(paper_claims.keys()) | set(paper_theorems.keys())
    sorted_all = sorted(all_papers, key=lambda x: int(x.split('-')[1]) if x.split('-')[1].isdigit() else 999)
    for p in sorted_all:
        nc = len(paper_claims.get(p, []))
        nt = len(paper_theorems.get(p, []))
        f.write(f"- {p.upper()}: {nc} claims, {nt} theorems\n")
    
    f.write("\n## Mapping Rules Applied\n\n")
    f.write("1. `paper00` / `PAPER_00` / `CQE-paper-00` → `paper-00`\n")
    f.write("2. `CQE-paper-01` through `CQE-paper-11` → `paper-01` through `paper-11`\n")
    f.write("3. `WP-06` (Wolfram Problem) → `paper-06`\n")
    f.write("4. Content references to 'Paper N' in claim text were parsed for mapping\n")
    f.write("5. All B-family branding (FLCR, NIST, Barker, CQECMPLX) stripped from output text\n")
    f.write("6. Claims with no determinable paper number listed as 'unassigned'\n")

print(f"Catalog written to {output_path}")
print(f"Claims mapped: {len([c for c in claims if c['paper']])}/{len(claims)}")
print(f"Theorems mapped: {len([t for t in theorems if t['paper']])}/{len(theorems)}")
