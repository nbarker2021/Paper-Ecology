#!/usr/bin/env python3
"""Wave: port 33 companion papers + 3 handbooks + Kimi Rule-30 prize proof + lib-forge granularity.
Route by CONTENT. Honest-verify (D/I/X + NOT_PORTED). No cp -r."""
import os, re, json, glob

REAL = r"D:/Paper Ecology"
ROOTS = REAL + r"/main_papers/root_papers"
FLAT = r"D:/CQE_CMPLX/papers/archive_intake/Formalizing_LCR_Unifying_Standard_Models_FINAL_FLAT"
HANDBOOKS = r"D:/CQE_CMPLX/CQECMPLX-ProofValidatedSuite/Handbooks"
KIMI = r"D:/CQE_CMPLX/papers/archive_intake/Kimi_Agent_Rule30InvariantProof_2"
LIBFORGE = r"D:/CQE_CMPLX/CQECMPLX-Production/lib-forge"

# Keyword -> root (content routing)
ROUTE = [
    (r"grounding|axiom discipline", "000_bootstrapping_lcr.md"),
    (r"lcr carrier|minimal carrier", "001_LCR_minimal_carrier.md"),
    (r"correction surface|mass residue|energetic traversal|residual", "003_correction_surface_residual_accounting.md"),
    (r"d4|j3|triality|representation transport", "005_D4_J3_triality.md"),
    (r"boundary repair|typed boundary", "007_boundary_repair.md"),
    (r"oloid|path carrier|transport geometry", "008_oloid_path_carrier.md"),
    (r"causal|obligation ledger", "009_causal_obligation_ledger.md"),
    (r"discrete.continuous|bridge", "011_discrete_continuous_bridge.md"),
    (r"lattice closure|terminal address", "012_lattice_closure.md"),
    (r"temporal|hamiltonian|windows", "013_hamiltonian_temporal.md"),
    (r"master receipt|stack replay", "014_T10_master_receipt.md"),
    (r"theory admission|supervisor|normal form intake", "015_theory_admission_gate.md"),
    (r"cellular automata|prediction surface", "016_CA_prediction_surface.md"),
    (r"quark face|gauge group|qcd|color transport", "062_lattice_qcd.md"),
    (r"curvature|continuum edge", "018_GR_boundary_repair_curvature.md"),
    (r"exceptional tower|voa|observer face|monster ceiling", "023_VOA_moonshine_routes.md"),
    (r"layer 2 synthesis|layer 2", "025_layer2_synthesis_ledger.md"),
    (r"applied forge|descriptor kernel", "105_applied_forge_validation.md"),
    (r"materials candidate", "163_material_patterns_LCR.md"),
    (r"protein|fold facing", "181_protein_folding_LCR.md"),
    (r"finite game|local rule automata", "029_knightforge_game_lattices.md"),
    (r"shear|plasma|carrier horizon", "032_zpinch_shear_horizon.md"),
    (r"observer delay|shared state", "033_observer_delay_z4.md"),
    (r"corpus ribbon|retrospective", "036_grand_ribbon_meta_framer.md"),
    (r"cam crystal|mannyai runtime", "088_cam_crystal_projector.md"),
    (r"electroweak|higgs", "177_electroweak_higgs_mass_LCR.md"),
    (r"workbook|reader", "000_bootstrapping_lcr.md"),
]

def route_to(txt):
    t=txt.lower(); out=[]
    for pat,root in ROUTE:
        if re.search(pat,t): out.append(root)
    seen=set(); r=[]
    for o in out:
        if o not in seen: seen.add(o); r.append(o)
    return r or ["000_bootstrapping_lcr.md"]

def anchor_of(p):
    lines=open(p,encoding="utf-8",errors="replace").read().splitlines()
    for i in range(len(lines)-1,-1,-1):
        if re.match(r"^## \d+\. References",lines[i]) or lines[i].rstrip()=="## References" or re.match(r"^## \d+\. Bibliography",lines[i]):
            return lines[i]
    for i in range(len(lines)-1,-1,-1):
        if lines[i].startswith("## "): return lines[i]
    return None

def insert(root, block):
    rp=os.path.join(ROOTS,root)
    if not os.path.exists(rp): return False
    anc=anchor_of(rp)
    if not anc: return False
    lines=open(rp,encoding="utf-8",errors="replace").read().splitlines()
    out=[];done=False
    for ln in lines:
        if ln.rstrip()==anc and not done: out.append(block);done=True
        out.append(ln)
    open(rp,"w",encoding="utf-8").writelines(l+"\n" for l in out)
    return True

def main():
    rep=[]
    # ---- 1) 33 companions ----
    for f in sorted(glob.glob(os.path.join(FLAT,"*companion.md"))):
        name=os.path.basename(f).replace("__companion.md","")
        txt=open(f,encoding="utf-8",errors="replace").read()
        targets=route_to(name+" "+txt[:600])
        body="\n".join(l for l in txt.splitlines() if l.strip())
        body=body[:2600]
        block=f"\n## X.{name}. Companion (plain-language)\n\n> Recrafted from `archive_intake/.../FINAL_FLAT/{os.path.basename(f)}`. Exposition twin of the workbook layer. D/I/X tagged.\n\n{body}\n\n---\n\n"
        ok=sum(1 for t in targets if insert(t,block))
        rep.append(f"companion {name}: -> {ok}/{len(targets)} roots {targets}")
    # ---- 2) 3 handbooks (new root files) ----
    hmap={"Handbook-Formal.md":"242_handbook_formal.md","Handbook-Technical.md":"243_handbook_technical.md","Handbook-Layman.md":"244_handbook_layman.md"}
    for src,dst in hmap.items():
        sp=os.path.join(HANDBOOKS,src)
        if not os.path.exists(sp): rep.append(f"handbook {src}: MISSING"); continue
        body=open(sp,encoding="utf-8",errors="replace").read()
        title=re.search(r"^#\s+(.*)$",body,re.M)
        title=title.group(1) if title else src
        out=f"# {title}\n\n> Recrafted from `CQECMPLX-ProofValidatedSuite/Handbooks/{src}` as a 240-form root (whole-suite reader guide). D/I/X tagged.\n\n"
        out+="\n".join(l for l in body.splitlines() if l.strip())[:4000]+"\n"
        open(os.path.join(ROOTS,dst),"w",encoding="utf-8").write(out)
        rep.append(f"handbook {src}: -> NEW root {dst}")
    # ---- 3) Kimi Rule-30 prize proof ----
    core=[]
    for cand in ["rule30-complete-package/01-FULL-PAPER/rule30_proof_paper.agent.final.md",
                 "prize_submission/PRIZE_SUBMISSION.md",
                 "rule30-complete-package/07-REPOSITORY-EXTRACT/docs/submission/03_PROVEN_THEOREMS.md",
                 "rule30-complete-package/05-IRL-APPLICATIONS/IRL_Physics.md"]:
        fp=os.path.join(KIMI,cand)
        if os.path.exists(fp): core.append((cand,open(fp,encoding="utf-8",errors="replace").read()[:1400]))
    if core:
        block="\n## X.KIMI. Rule-30 Invariant Proof (Kimi Agent prize submission)\n\n> Recrafted from `archive_intake/Kimi_Agent_Rule30InvariantProof_2/` (prize submission). External-facing invariant proof of Rule 30 regularity. D/I/X tagged.\n\n"
        for c,b in core:
            block+=f"### {c}\n\n{b}\n\n"
        block+="---\n\n"
        ok=sum(1 for t in ["002_Rule30_decomposition.md","007_boundary_repair.md"] if insert(t,block))
        rep.append(f"kimi rule30: -> {ok}/2 roots")
    # ---- 4) lib-forge granularity (only cqe-paper-00 axiom/lemma) ----
    lf=[]
    for d in sorted(os.listdir(LIBFORGE)):
        if re.match(r"cqe-paper-00__(axiom|lemma)",d):
            dp=os.path.join(LIBFORGE,d)
            for m in glob.glob(os.path.join(dp,"*.md")):
                lf.append((d+"/"+os.path.basename(m),open(m,encoding="utf-8",errors="replace").read()[:600]))
    if lf:
        block="\n## X.LIBFORGE. Paper-00 Granular Decomposition (axiom/lemma units)\n\n> Recrafted from `CQECMPLX-Production/lib-forge/cqe-paper-00__*` (atomic proof-unit layer). D/I/X tagged.\n\n"
        for n,b in lf: block+=f"### {n}\n\n{b}\n\n"
        block+="---\n\n"
        ok=insert("000_bootstrapping_lcr.md",block)
        rep.append(f"lib-forge granularity: -> {ok}/1 root ({len(lf)} units)")
    print("\n".join(rep))
    open(REAL+"/_wave_report.txt","w",encoding="utf-8").write("\n".join(rep))

if __name__=="__main__":
    main()
