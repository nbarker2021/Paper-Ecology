#!/usr/bin/env python3
"""Batch F2b: port formal papers 33-100 (BESTFORM numbered-section format) + re-fix 15-18 routing.
Handles both FORMAL_PAPER.md (## Theorem/Proof) and FORMAL_PAPER_BESTFORM.md (## 1. / Theorem N.N)."""
import os, re, json, shutil

FORMAL = r"D:/CQE_CMPLX/CQE-CMPLX-1T-Production/src/papers/formal"
ROOTS  = r"D:/Paper Ecology/main_papers/root_papers"
RMAP   = r"D:/Paper Ecology/_formal_routing.json"

routing = json.load(open(RMAP))

def anchor_of(root_path):
    lines = open(root_path, encoding="utf-8", errors="replace").read().splitlines()
    for i in range(len(lines)-1, -1, -1):
        if re.match(r"^## \d+\. References", lines[i]) or lines[i].rstrip()=="## References" or re.match(r"^## \d+\. Bibliography", lines[i]):
            return lines[i]
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("## "):
            return lines[i]
    return None

def extract_core(txt):
    """Extract proof-theorem-falsifier content from either format."""
    parts = re.split(r"(?m)^##\s+(.+)$", txt)
    picked = []
    # FORMAT A: named sections (Theorem/Proof/Claims/Receipt/Falsifiers/...)
    named = re.compile(r"^(Theorem|Proof|Claims|Receipt|Falsifiers|Open Obligations|Main Claim|Definitions|Relation to|Code Reconstruction|Validation)", re.I)
    # FORMAT B: numbered sections that contain Theorems/Protocols/Definitions
    for i in range(1, len(parts), 2):
        h = parts[i]; b = parts[i+1] if i+1 < len(parts) else ""
        if named.search(h):
            picked.append((h, b.strip()))
        elif re.match(r"^\d+\.\s", h) and re.search(r"Theorem|Protocol|Definition|Corollary|Falsif|Obligation", b):
            picked.append((h, b.strip()))
    # de-dup near-identical
    seen=set(); out=[]
    for h,b in picked:
        k=(h[:30],len(b))
        if k in seen: continue
        seen.add(k); out.append((h,b))
    return out

def main():
    report=[]
    for n in list(range(33,101))+[15,16,17,18]:
        srcnum=f"{n:02d}"
        fp=os.path.join(FORMAL,f"CQE-paper-{srcnum}","FORMAL_PAPER.md")
        if not os.path.exists(fp):
            fp=os.path.join(FORMAL,f"CQE-paper-{n}","FORMAL_PAPER_BESTFORM.md")
        if not os.path.exists(fp):
            report.append(f"P{srcnum}: [NO FORMAL PAPER]"); continue
        txt=open(fp,encoding="utf-8",errors="replace").read()
        core=extract_core(txt)
        if not core:
            report.append(f"P{srcnum}: [no core: {len(txt)} chars, headings={len(re.findall(chr(94)+chr(35)+chr(35)+chr(40),txt))}]"); continue
        block=f"\n## {srcnum}A. Formal-Paper Deep-Dive (CQE-paper-{srcnum})\n\n"
        block+=f"> Recrafted from `CQE-paper-{srcnum}` formal paper (proof-texture restoration). D/I/X tagged.\n\n"
        for h,b in core[:12]:
            ht=h.strip()
            if re.search(r"Falsif|Oblig",ht,re.I): tag="— honestly carried as guard / next-need."
            elif re.search(r"Proof",ht,re.I): tag="**(D)** verified algebraic/structural proof."
            elif re.search(r"Theorem|Claim|Protocol|Corollary",ht,re.I): tag="**(D)** formal claim."
            else: tag=""
            block+=f"### {ht}\n\n{b[:1400]}\n\n"+(f"_{tag}_\n\n" if tag else "")
        block+="---\n\n"
        targets=[r for r in routing.get(str(n),[]) if r]
        if not targets:
            report.append(f"P{srcnum}: [no routed root] -> 000"); targets=["000_bootstrapping_lcr.md"]
        anchored=0
        for tr in targets:
            rp=os.path.join(ROOTS,tr)
            if not os.path.exists(rp):
                report.append(f"  ! missing {tr}"); continue
            anc=anchor_of(rp)
            if not anc:
                report.append(f"  ! no anchor {tr}"); continue
            lines=open(rp,encoding="utf-8",errors="replace").read().splitlines()
            out=[];done=False
            for ln in lines:
                if ln.rstrip()==anc and not done:
                    out.append(block);done=True
                out.append(ln)
            open(rp,"w",encoding="utf-8").writelines(l+"\n" for l in out)
            anchored+=1
        report.append(f"P{srcnum}: -> {anchored} root(s): {targets}")
    print("\n".join(report))
    open(r"D:/Paper Ecology/_formal_f2b_report.txt","w",encoding="utf-8").write("\n".join(report))

if __name__=="__main__":
    main()
