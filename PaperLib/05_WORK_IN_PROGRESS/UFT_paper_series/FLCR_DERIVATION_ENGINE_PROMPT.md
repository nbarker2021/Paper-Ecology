## FLCR Paper Series — Autonomous Derivation Engine Prompt

**Objective:** Systematically derive, formalize, and deepen every paper in the FLCR 0-100 series (plus bridge papers 101-103), using each prior paper as a verified receipt carrier. Work in sequential passes (0→100, then 100→0, repeating), upgrading claims from (X) open → (I) interpretation → (D) data-backed, and closing the irreducible gaps.

**Workspace:** `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\`  
**Quick-access mirror:** `D:\CQE_CMPLX\papers\UFT0-100\` (must stay in sync after every change)

**Codebase:** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\` (192 files)  
**Kernel:** `D:\CQE_CMPLX\cqekernel\`

---

## 0. The Meta-Rule: Assume Nothing, Verify Everything

The user's earlier work is speculative, interpretive, and occasionally contains fabrications that were later corrected. **You must treat every claim as potentially unproven until you verify it against actual source files, standard mathematical references, or explicit computational proof.** When you encounter a claim:

- If you can find a file that supports it → tag **(D)** and cite `file:line`
- If it is a reasonable structural reading but not literally in the data → tag **(I)** and state the upstream reasoning
- If you stated it as fact but cannot verify it → tag **(X)** and correct it honestly

**Never fabricate:** Do not invent file paths, test results, mass values, success rates, or structural counts that do not exist in the source. If you cannot verify something, say so explicitly. The `HONEST-DISCLOSURE.md` file in the paper series documents past fabrications — read it before writing.

---

## 1. The Priority Framework: What to Derive

Use the following hierarchy. On each pass, work from the top down:

### Tier 1: Close the 10 Open (X) Obligations (Highest Priority)
These are gaps where no formula or construction exists. They must be explicitly addressed in the papers that claim them:

1. **Higgs potential from Albert algebra cubic norm** — Derive `V(φ) = μ²|φ|² + λ|φ|⁴` from `det(X)` on `J₃(𝕆)`. Papers 53-56.
2. **Yukawa couplings from octonion structure** — Derive `Y_ij = f(octonion constants f_abc)`. Papers 53-56.
3. **CKM matrix from octonion associator** — Derive `CKM = f(associator)`. Papers 50, 41-44.
4. **Einstein Field Equations from discrete repair** — Derive `G_μν = 8πG T_μν` from the boundary-repair axioms of Papers 3, 5, 15. Paper 65.
5. **Riemann Hypothesis from boundary repair** — Derive zero distribution of `ζ(s)` from the repair-curvature framework. Paper 86.
6. **Prime distribution from LCR carrier** — Derive `π(x)` from the Rule 30 / lattice structure. Paper 86.
7. **Γ72 glue vectors** — Explicitly construct the 9 glue vectors for `Hermitian E6×E6×E6` and verify evenness and unimodularity. Paper 91.
8. **Witness map `s → A(s)`** — Construct explicit map from D4 axis/sheet pairs to `Gr≥0(3,6)` matrices, verifying positivity and positroid encoding. Papers 4, 101, 80.
9. **Monster VOA states → Gr(3,8) positroid cells** — Prove or computationally verify that Monster VOA states correspond to positroid cells of the E8 tropical fan. Papers 27, 90.
10. **Neutrino masses from VOA extension** — The SM assigns neutrinos weight 0 (massless). Extend the VOA framework to account for observed neutrino oscillations. Papers 16, 49, 100.

### Tier 2: Upgrade (I) Interpretations to (D) (High Priority)
These are structural analogies that need explicit formulas, proofs, or computational verification to become theorems. Target 20 of the 38 (I) claims in `paper_103__formal_math_claims_registry.md`:

Key targets:
- The 3 trace-2 idempotents = 3 fermion generations (Papers 4, 41): Derive explicit quantum numbers from idempotents.
- The Higgs doublet as a point in `J₃(𝕆)` (Papers 53-56): Embed `SU(2)` doublet with gauge covariance.
- The positive Grassmannian ↔ Albert algebra correspondence (Papers 101, 102): Build explicit bridge formulas.
- Boundary repair = positroid boundary collapse (Papers 5, 101): Prove exact correspondence.
- The 2-category `ℒ` = chamber complex (Paper 80): Prove equivalence with `Gr≥0(2,4)` or `Gr≥0(3,6)` cell decomposition.
- The 24-cell = D4 associahedron (Paper 4): Prove combinatorial isomorphism.
- The Monster = Aut(E8 tropical fan) (Paper 27): Prove automorphism correspondence.

### Tier 3: Deepen Short Papers (Medium Priority)
Papers still below 200 lines or lacking structural depth:
- Papers 40, 58, 59, 61, 63, 64, 71, 73, 85, 90 (all 159-176 lines)
- Add VOA weight derivations, Grassmannian connections, or explicit computational receipts.

### Tier 4: Cross-Reference Validation (Ongoing)
- Ensure every paper cites `file:line` for (D) claims.
- Ensure every (I) claim cites the upstream FLCR doctrine and the standard math it interprets.
- Ensure every (X) claim has an explicit open obligation with: *Why not closed, Next binding action, Owner.*
- Update `PAPER_DEPENDENCY_MAP.md` as new connections are discovered.
- Update `HONEST-DISCLOSURE.md` if any new fabrications are found.

---

## 2. The Pass Structure: How to Work

### Pass 0: The Setup (Run Once)
Before touching any paper, read:
1. `HONEST-DISCLOSURE.md` — know the fabrication history
2. `PAPER_DEPENDENCY_MAP.md` — know the dependency graph
3. `paper_103__formal_math_claims_registry.md` — know the 120 claim statuses
4. `paper_102__albert_algebra_formalization_study.md` — know the Albert algebra obligations
5. `paper_101__positive_grassmannian_bridge.md` — know the Grassmannian framework

### Pass A: Forward Pass (0 → 100)
For each paper `n` from 0 to 100:

**Step 1: Read the paper.** Read it fully. Note its current line count, its (D)/(I)/(X) claims, and its open obligations.

**Step 2: Read the receipt carriers.** Read Papers 0 through `n-1` that are cited as receipts. Verify the claims they carry are still (D). If a prior paper has been corrected in a later pass, propagate the correction forward.

**Step 3: Ask critical questions.** For each theorem/claim in the paper, ask:
- Is this stated as fact? Can I find it in a source file?
- Is this a structural reading? Is it clearly labeled as interpretation?
- Is this a numerical claim? Can I recompute it?
- Does this paper rely on a prior paper that was later corrected? If so, update.
- Is there a Grassmannian interpretation of this claim? If so, add it (from Paper 101).
- Is there an Albert algebra interpretation of this claim? If so, add it (from Paper 102).

**Step 4: Derive new content.** Based on the priority framework (Tier 1 → 2 → 3 → 4):
- Add derivations, formulas, computational verifications, or explicit constructions.
- If you cannot derive something, add an honest open obligation with the standard format: *Why not closed, Next binding action, Owner.*
- If a claim was previously (X) and you now have a derivation, upgrade it to (I) or (D) and add the proof.

**Step 5: Add/audit Data vs. Interpretation disclosure.** At the end of the paper, ensure there is a section (or appendix) that tags every theorem as (D), (I), or (X) with justification.

**Step 6: Update the paper.** Write the enhanced version back to both directories. Maintain the existing naming convention: `paper_NN__<name>/paper_NN.md` in `active-rework`, and `paper_NN.md` flat in `UFT0-100`.

**Step 7: Update artifacts.** If any claim status changed, update `paper_103` (registry), `HONEST-DISCLOSURE.md` (if fabrication found), and `PAPER_DEPENDENCY_MAP.md` (if new dependencies found).

### Pass B: Reverse Pass (100 → 0)
After completing Pass A, work backward from Paper 100 to Paper 0. This pass focuses on:
- **Propagation:** Ensure later papers' corrections propagate backward to earlier papers that cite them.
- **Synthesis:** Papers 90-100 synthesize the whole series. In the reverse pass, ensure every synthesis claim has a receipt in an earlier paper.
- **Gap closure:** The 8-10 irreducible gaps are most visible in the capstone papers (80, 90, 91, 100). Use the reverse pass to add baseline derivations where they are missing.
- **Consistency:** Ensure all VOA constants (κ, SCALE, 25.05 GeV) are used identically across all papers.

### Pass C+: Subsequent Passes
Repeat Pass A and Pass B. On each subsequent pass:
- If a paper is fully derived (all claims are (D), all obligations closed), **extend it further** by adding deeper connections, alternative derivations, or connections to the Grassmannian/Albert algebra frameworks.
- If a paper still has (X) or (I) claims, **focus on upgrading them**.
- The series is never "done" — it deepens with each pass.

---

## 3. The Receipt Carrier Protocol

When Paper `n` uses Paper `m < n` as a receipt carrier, you must:

1. **Verify the receipt exists.** Check that the cited theorem/claim in Paper `m` is actually in the file and is tagged (D) or (I).
2. **Check for corrections.** If Paper `m` was corrected in a later pass (e.g., Paper 11's fabrications), ensure Paper `n` does not repeat the old (false) claim.
3. **Trace the chain.** If the claim in Paper `m` itself relies on Paper `k < m`, trace back to the original (D) source. Do not cite chains of (I) claims as if they were (D).
4. **Add cross-reference.** If Paper `n` makes a new claim that is supported by Paper `m`, add an explicit forward/backward citation: `Paper m, Theorem X.Y`.

---

## 4. The Computational Verification Protocol

For every claim that can be computed, you must actually compute it using the codebase:

1. **Use the forge runtime:** `powershell -NoProfile -ExecutionPolicy Bypass -File D:\CQE_CMPLX\tools\forge_runtime_env.ps1 <command>`
2. **Run Python scripts:** Use `PythonRun` or the local `.venv` Python to run lattice forge modules.
3. **Verify against data:** For Rule 30, use the 1M-bit data in `CMPLX-R30-main/DATA/wolfram-rule30-center/wolfram_rule30_center_1m.json`.
4. **Verify lattice claims:** Use `lattice_codes.py`, `enumerated_glue.py`, `ledger/roots.py`, `calibrate_units.py`.
5. **Document the result:** If a computation passes, add a receipt citation: `Verified by [script_name] at [timestamp]`. If it fails, add a falsifier and an honest correction.

**Never claim a computation was run unless you actually ran it in this session.**

---

## 5. The Honest Disclosure Protocol

Every paper must end with a **Data vs. Interpretation vs. Open** disclosure section. Use this exact format:

```markdown
## Data vs. Interpretation vs. Open

| Claim | Status | Evidence |
|-------|--------|----------|
| Theorem X.Y: [statement] | (D) | Backed by [file:line] or [standard reference] |
| Theorem X.Z: [statement] | (I) | Structural reading of [upstream paper/doctrine] |
| Theorem X.W: [statement] | (X) | Open obligation: [why not closed, next action, owner] |
```

If a paper does not have this section, add it.

If you find a **fabrication** (a claim stated as fact that is not in the data and the interpretation is wrong), you must:
1. Correct it in the paper immediately.
2. Add an entry to `HONEST-DISCLOSURE.md` documenting the false claim and the honest replacement.
3. Propagate the correction to all papers that cited the false claim.

---

## 6. The New Framework Integration Protocol

Two new frameworks have been added to the FLCR series:

### 6.1 The Positive Grassmannian (Paper 101)
Whenever a paper deals with:
- D4 codec / 8 LCR states → mention `Gr≥0(2,4)` or `Gr(3,6)` tropical D4
- E6 / 72 roots → mention `Gr(3,7)` tropical E6
- E8 / Monster / 196883 → mention `Gr(3,8)` tropical E8
- Boundary repair → mention positroid boundary collapse
- State transitions → mention cluster mutations / plabic moves
- The 2-category ℒ → mention chamber complex

### 6.2 The Albert Algebra (Paper 102)
Whenever a paper deals with:
- Fermion generations → mention trace-2 idempotents of `J₃(𝕆)`
- Higgs field → mention cubic norm `det(X)` and Freudenthal determinant
- Yukawa couplings → mention octonion structure constants `f_abc`
- CKM mixing → mention octonion associator
- Gauge groups → mention `F4 ⊃ SU(3)` and the Tits construction
- Exceptional Lie algebras → mention the magic square

---

## 7. The Todo List Protocol

Maintain a `TodoList` throughout the work. Update it after every substantive action. Use these categories:

- `pending` — not started
- `in_progress` — actively working on it right now
- `done` — completed and verified

Mark exactly one task as `in_progress` at any time. When a task is done, mark it `done` immediately.

Example tasks for a single paper:
- "Read Paper 53 and audit claims"
- "Verify Higgs mass formula computationally"
- "Derive Higgs potential from cubic norm (attempt)"
- "Add Grassmannian bridge section to Paper 53"
- "Update Data vs. Interpretation disclosure"
- "Sync to UFT0-100"

---

## 8. The Artifact Sync Protocol

After modifying any paper, you must:

1. **Write the enhanced paper** to `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\<paper_dir>\paper_NN.md`
2. **Copy it** to `D:\CQE_CMPLX\papers\UFT0-100\paper_NN.md`
3. **If the paper is a new bridge paper** (101, 102, 103, etc.), copy it to both directories.
4. **If claim statuses changed**, update `paper_103` (registry), `HONEST-DISCLOSURE.md` (if needed), and `PAPER_DEPENDENCY_MAP.md` (if new dependencies).
5. **Report the change** to the user: state what was added, what was corrected, and what remains open.

---

## 9. The User-Interaction Protocol

If you encounter any of the following, **stop and ask the user**:

- A claim that contradicts established mathematics (e.g., a physics mass value that is off by orders of magnitude, or a mathematical identity that is false)
- A claim that requires a new file or codebase modification that does not exist
- A situation where the user's prior work appears to be a fabrication (false claim stated as fact)
- A situation where you need more than 5 tool calls to make progress on a single paper (indicate you may need a subagent)
- A situation where you have completed a full pass (0→100 or 100→0) and need direction on the next pass

Do not silently continue if you are uncertain about the mathematical validity of a claim.

---

## 10. Summary of Deliverables

On each paper, the expected output is:

1. **Enhanced paper content** with new derivations, proofs, or constructions.
2. **Honest disclosure section** tagging all claims as (D), (I), or (X).
3. **Updated cross-references** to prior papers (receipt carriers) and forward references to later papers.
4. **Computational verification** where applicable (code runs, file citations).
5. **Synced files** in both `active-rework` and `UFT0-100` directories.
6. **Updated registry** (`paper_103`) if any claim statuses changed.

---

*This prompt is the operating instructions for the FLCR autonomous derivation engine. The goal is not to finish the papers, but to deepen them iteratively, with honesty about what is proven, what is interpreted, and what remains open.*
