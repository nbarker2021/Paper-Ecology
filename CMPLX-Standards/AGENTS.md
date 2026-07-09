# CMPLX-Standards

CMPLX-Standards is the validator and normal-form grading surface. It should replace the older NIST/NSIT naming in active work while preserving provenance from those historical tools.

## Role

- Define paper-specific and generalized normal forms.
- Grade incoming data, papers, claims, receipts, and tool outputs against CMPLX models.
- Record how close a candidate is to acceptance, exclusion, partial fit, or rework.
- Keep validator outputs machine-readable and receipt-friendly.

## Operating Rules

- Prefer local files and SQLite for validation queues and reports.
- Do not silently promote a claim because a validator accepts its shape; preserve honesty labels and open obligations.
- Keep NIST/NSIT references as lineage/provenance, but use `CMPLX-Standards` for active naming.
- When a validator depends on Forge/Lattice/ReForge, use:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\CQE_CMPLX\tools\forge_runtime_env.ps1 lattice-forge status
```

## Expected Outputs

- Validator reports should include source path, source type, normal form, score/distance, accepted/excluded fields, blockers, and next required derivation.
- Prefer JSON/JSONL plus a concise Markdown summary for human review.
