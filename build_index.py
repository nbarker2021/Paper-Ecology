import json, re, os, glob
from pathlib import Path

PAPER_DIR = Path(r"D:\Paper Ecology\PaperLib")
CODE_DIR = Path(r"D:\Paper Ecology\CodeLib")

def count_words(text):
    return len(text.split())

def extract_titles_and_headers(text):
    # Extract theorem/definition/corollary/claim names
    pattern = r'(?:Theorem|Definition|Corollary|Claim)\s+([0-9]+(?:\.[0-9]+)*(?:\.[0-9]+)?)'
    matches = re.findall(pattern, text)
    return sorted(set(matches))

def extract_cross_references(text):
    # Find "Paper \d+" or "paper-\d+" references
    pattern = r'Paper\s+(\d+)|paper-(\d+)'
    matches = re.findall(pattern, text)
    refs = set()
    for m in matches:
        num = m[0] if m[0] else m[1]
        if num:
            refs.add(int(num))
    return sorted(refs)

def count_claim_status(text):
    # Count D, I, X in claim ledger tables
    d_count = len(re.findall(r'\|\s*D\s*\|', text)) + len(re.findall(r'\|\s*D\s*\*?\s*\|', text))
    i_count = len(re.findall(r'\|\s*I\s*\|', text))
    x_count = len(re.findall(r'\|\s*X\s*\|', text))
    # Alternative: look for status column patterns
    return {"D": d_count, "I": i_count, "X": x_count}

def extract_open_obligations(text):
    # Find FLCR-XX-OBL-XXX patterns
    pattern = r'FLCR-\d+-OBL-\d+'
    matches = re.findall(pattern, text)
    return matches

def extract_keywords(text):
    # Extract from title and key terms
    title_match = re.search(r'Title[:\s]+(.+)', text, re.IGNORECASE)
    title = title_match.group(1) if title_match else ""
    
    # Common physics/math keywords
    keywords = []
    keyword_map = {
        "mass": "mass", "higgs": "Higgs", "yukawa": "Yukawa", "coupling": "coupling",
        "ckm": "CKM", "pmns": "PMNS", "neutrino": "neutrino", "mixing": "mixing",
        "gauge": "gauge", "symmetry": "symmetry", "lie": "Lie algebra",
        "gravity": "gravity", "einstein": "Einstein field equation", "curvature": "curvature",
        "boundary": "boundary repair", "repair": "boundary repair",
        "bridge": "bridge artifact", "calibration": "calibration",
        "plasma": "plasma", "energy": "energy", "lattice": "lattice",
        "code": "lattice code", "chain": "lattice code chain",
        "e6": "E6", "f4": "F4", "e8": "E8", "monster": "Monster VOA",
        "vo": "VOA", "automorphism": "automorphism", "universal": "universality",
        "receipt": "receipt", "carrier": "carrier", "ledger": "ledger",
        "niemeier": "Niemeier", "glue": "glue group", "d4": "D4",
        "freudenthal": "Freudenthal-Tits", "magic": "magic square",
        "triality": "triality", "octonion": "octonion", "jordan": "Jordan algebra",
        "state": "state machine", "automaton": "automaton", "machine": "state machine",
        "mckay": "McKay-Thompson", "moonshine": "moonshine",
        "between-sample": "between-sample dynamics", "closure": "closure stability",
        "sampling": "sampling", "meta-test": "meta-test", "cross-validation": "cross-validation",
        "measurement": "measurement", "protocol": "protocol", "standard": "standard",
        "traceability": "traceability", "error": "error propagation",
        "systematic": "systematic error", "uncertainty": "uncertainty",
        "sm": "Standard Model", "bsm": "BSM", "flcr": "FLCR",
        "unit": "natural unit", "kappa": "natural unit", "kappa": "natural unit"
    }
    
    text_lower = text.lower()
    for key, val in keyword_map.items():
        if key in text_lower and val not in keywords:
            keywords.append(val)
    
    # Limit to 5 most relevant
    return keywords[:5]

def extract_paper_number(filename):
    match = re.search(r'paper-(\d+)', filename)
    return int(match.group(1)) if match else None

def get_codelib_status(paper_num):
    # Check if corresponding Python file exists
    pattern = str(CODE_DIR / f"paper-{paper_num}__*.py")
    files = glob.glob(pattern)
    if files:
        return "EXISTS"
    return "MISSING"

def build_index():
    results = []
    
    for paper_num in range(51, 76):
        pattern = str(PAPER_DIR / f"paper-{paper_num}__*.md")
        files = glob.glob(pattern)
        if not files:
            print(f"WARNING: Paper {paper_num} not found")
            continue
        
        filepath = files[0]
        filename = os.path.basename(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        word_count = count_words(text)
        
        # Extract title from header
        title_match = re.search(r'Title[:\s]+(.+)', text, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else filename
        
        # Extract all theorem/definition/corollary/claim numbers
        named_items = extract_titles_and_headers(text)
        
        # Cross-references
        cross_refs = extract_cross_references(text)
        # Remove self-reference
        cross_refs = [r for r in cross_refs if r != paper_num]
        
        # Claim status counts
        claim_counts = count_claim_status(text)
        
        # Open obligations
        obligations = extract_open_obligations(text)
        
        # Keywords
        keywords = extract_keywords(text)
        
        # CodeLib status
        codelib_status = get_codelib_status(paper_num)
        
        results.append({
            "paper_number": paper_num,
            "title": title,
            "word_count": word_count,
            "keywords": keywords,
            "named_theorems_claims_definitions_corollaries": named_items,
            "cross_references_to_papers": cross_refs,
            "claim_status_counts": claim_counts,
            "open_obligations": obligations,
            "codelib_file_status": codelib_status
        })
    
    return results

if __name__ == "__main__":
    index = build_index()
    print(json.dumps(index, indent=2))
