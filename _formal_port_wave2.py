#!/usr/bin/env python3
"""Wave 2: port the 66 CQE-paper-formal-* supplementary papers into 240-form roots.
Route by CONTENT (title/abstract keywords) to existing topical roots.
Honest-verify: tag D/I/X, carry NOT_PORTED flags verbatim, no cp -r.
"""
import os, re, json

FORMAL = r"D:/CQE_CMPLX/CQE-CMPLX-1T-Production/src/papers/formal"
ROOTS  = r"D:/Paper Ecology/main_papers/root_papers"

# Keyword -> root file map (content routing, never by paper number)
ROUTE = [
    (r"moonshine|monster|j-function|j\(tau|VOA", "023_VOA_moonshine_routes.md"),
    (r"superpermutation", "102_superpermutation_bounds.md"),
    (r"riemann", "095_mckay_thompson_parity.md"),  # honesty note lives near moonshine
    (r"barker|market engine|trade|asset|portfolio", "163_material_patterns_LCR.md"),  # applied/forge
    (r"covalent|chem|reaction graph|molecule", "163_material_patterns_LCR.md"),
    (r"spectre|aperiodic|monotile|tile", "033_observer_delay_z4.md"),  # correction geometry
    (r"oracle|observer map|prestate", "024_observer_face_selection.md"),
    (r"glossary|notation|reference", "000_bootstrapping_lcr.md"),
    (r"claim|formalization paper", "000_bootstrapping_lcr.md"),
    (r"digital root|centroid|hamming|annealing", "016_CA_prediction_surface.md"),
    (r"lattice forge|self-document", "012_lattice_closure.md"),
    (r"universal closed form|LCR closed", "000_bootstrapping_lcr.md"),
    (r"airlock|forgefactory|agent ledger|kernel|cross-walk", "000_bootstrapping_lcr.md"),
]

def route_to(title, abstract):
    txt = (title+" "+abstract).lower()
    hits = []
    for pat, root in ROUTE:
        if re.search(pat, txt, re.I):
            hits.append(root)
    # de-dup preserve order
    seen=set(); out=[]
    for h in hits:
        if h not in seen: seen.add(h); out.append(h)
    return out or ["000_bootstrapping_lcr.md"]

def anchor_of(root_path):
    lines = open(root_path, encoding="utf-8", errors="replace").read().splitlines()
    for i in range(len(lines)-1, -1, -1):
        if re.match(r"^## \d+\. References", lines[i]) or lines[i].rstrip()=="## References" or re.match(r"^## \d+\. Bibliography", lines[i]):
            return lines[i]
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("## "):
            return lines[i]
    return None

def extract(txt):
    parts = re.split(r"(?m)^##\s+(.+)$", txt)
    out=[]
    for i in range(1, len(parts), 2):
        h=parts[i]; b=parts[i+1] if i+1<len(parts) else ""
        out.append((h, b.strip()[:1200]))
    return out[:10]

def main():
    report=[]
    for d in sorted(os.listdir(FORMAL)):
        if not d.startswith("CQE-paper-formal-"): continue
        fp=os.path.join(FORMAL,d,"FORMAL_PAPER.md")
        if not os.path.exists(fp): continue
        txt=open(fp,encoding="utf-8",errors="replace").read()
        title=re.search(r"^#\s+(.*)$",txt,re.M)
        title=title.group(1).strip() if title else d
        am=re.search(r"\*\*Abstract\*\*\.\s*(.*?)(?=\n\n|\n##|\n\*\*)",txt,re.S)
        abstract=am.group(1).strip()[:400] if am else txt[:400]
        targets=route_to(title, abstract)
        block=f"\n## X.{d}. Formal-Supplement Deep-Dive\n\n"
        block+=f"> Recrafted from `CQE-paper-formal-*` series (`{d}`). {title}\n\n"
        # honesty flag if present
        if re.search(r"NOT_PORTED|not_ported|does NOT provide a path", txt, re.I):
            block+="_**HONEST FLAG: source explicitly NOT_PORTED — carried as honesty boundary, not a proof.**_\n\n"
        for h,b in extract(txt):
            block+=f"### {h.strip()}\n\n{b}\n\n"
        block+="---\n\n"
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
        report.append(f"{d}: -> {anchored} root(s): {targets}")
    print("\n".join(report))
    open(r"D:/Paper Ecology/_formal_wave2_report.txt","w",encoding="utf-8").write("\n".join(report))

if __name__=="__main__":
    main()
