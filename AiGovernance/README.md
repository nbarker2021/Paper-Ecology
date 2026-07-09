# AiGovernance

Single constitution for **all** local AI tools (Cursor, VS Code, Codex, Claude, Grok, Kimi,
Vibe, Hermes, …).

## Source of truth

| Artifact | Purpose |
|----------|---------|
| `ECOLOGY.json` | Machine-readable constitution + paths |
| `AGENTS.md` | Human/tool-readable constitution (also at `D:\Paper Ecology\AGENTS.md`) |
| `rules/*.md` | Universal rules (Grok, Claude, AGENTS.md scanners) |
| `cursor-rules/*.mdc` | Cursor rules (`alwaysApply: true`) |
| `SKILL.md` | Vibe / Codex-style skill wrapper |
| `SHIMS.json` | Where each tool reads from |

## Sync / repair

Run from PowerShell:

```powershell
& "D:\Paper Ecology\AiGovernance\sync-shims.ps1"
```

This recreates junctions from `cursor-rules/` → `~/.cursor/rules` and `rules/` → `~/.grok/rules`,
and copies AGENTS stubs to Codex/Claude/Hermes homes.

## Do not edit shims directly

Edit files **here**, then run `sync-shims.ps1`. Shims are junctions or generated stubs.
