def proof_like_rows():
    return [{"lane":"proof","claim":"correction_surface_monitor","status":"D"},
            {"lane":"proof","claim":"correction_surface_split","status":"D"}]
def obligation_like_rows():
    return [{"lane":"obligation","claim":"correction_surface_recompute","status":"open"}]
def falsifier(c):
    if c.get("residue",0.0)!=0.0 and c.get("closed",False): return ("REJECT","nonzero residue")
    if c.get("d4_projection_changed",False) and not c.get("new_receipt",False): return ("DEFER","needs receipt")
    return ("ACCEPT",None)
