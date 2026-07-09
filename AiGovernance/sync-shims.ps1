#Requires -Version 5.1
<#
.SYNOPSIS
  Wire AiGovernance rules to all local AI tool config folders.
  Edit rules ONLY under D:\Paper Ecology\AiGovernance\, then re-run this script.
#>
$ErrorActionPreference = 'Stop'
$GovRoot = 'D:\Paper Ecology\AiGovernance'
$CursorRules = Join-Path $GovRoot 'cursor-rules'
$MarkdownRules = Join-Path $GovRoot 'rules'
$Stub = Join-Path $GovRoot 'shims\GLOBAL_AGENTS.stub.md'

function Set-RulesJunction {
    param([string]$LinkPath, [string]$TargetPath)
    if (Test-Path $LinkPath) {
        $item = Get-Item $LinkPath -Force
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            Remove-Item $LinkPath -Force
        } else {
            Remove-Item $LinkPath -Recurse -Force
        }
    }
    $parent = Split-Path $LinkPath -Parent
    if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    cmd /c mklink /J `"$LinkPath`" `"$TargetPath`" | Out-Null
    Write-Host "JUNCTION: $LinkPath -> $TargetPath"
}

function Copy-Stub {
    param([string]$Dest)
    $dir = Split-Path $Dest -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    Copy-Item $Stub $Dest -Force
    Write-Host "STUB: $Dest"
}

# --- Global Cursor user rules (all workspaces) ---
Set-RulesJunction -LinkPath "$env:USERPROFILE\.cursor\rules" -TargetPath $CursorRules

# --- Global Grok rules ---
Set-RulesJunction -LinkPath "$env:USERPROFILE\.grok\rules" -TargetPath $MarkdownRules
Copy-Stub -Dest "$env:USERPROFILE\.grok\AGENTS.md"

# --- Global Claude ---
Copy-Stub -Dest "$env:USERPROFILE\.claude\CLAUDE.md"

# --- Global Codex / Hermes ---
Copy-Stub -Dest "$env:USERPROFILE\.codex\AGENTS.md"
Copy-Stub -Dest "$env:USERPROFILE\.hermes\AGENTS.md"

# --- Workspace Cursor rules ---
foreach ($ws in @('D:\Paper Ecology', 'D:\MannyAI', 'D:\CQE_CMPLX')) {
    if (Test-Path $ws) {
        Set-RulesJunction -LinkPath (Join-Path $ws '.cursor\rules') -TargetPath $CursorRules
    }
}

# --- Workspace AGENTS.md (Paper Ecology already has full file; others get pointer) ---
$pointer = @"
# AI governance pointer

**Read first:** ``D:\Paper Ecology\AiGovernance\AGENTS.md`` and ``D:\Paper Ecology\AiGovernance\ECOLOGY.json``

All five rules under ``D:\Paper Ecology\AiGovernance\rules\`` apply globally.
Regenerate shims: ``D:\Paper Ecology\AiGovernance\sync-shims.ps1``
"@
foreach ($pair in @(
    @{ Path = 'D:\MannyAI\AGENTS-GOVERNANCE.md'; Keep = $false },
    @{ Path = 'D:\CQE_CMPLX\AGENTS-GOVERNANCE.md'; Keep = $false }
)) {
    if (-not (Test-Path $pair.Path)) {
        Set-Content -Path $pair.Path -Value $pointer
        Write-Host "POINTER: $($pair.Path)"
    }
}

# Copy Codex governance skill (mirror of AiGovernance/SKILL.md)
$skillDir = Join-Path $env:USERPROFILE '.codex\skills\paper-ecology-governance'
if (-not (Test-Path $skillDir)) { New-Item -ItemType Directory -Path $skillDir -Force | Out-Null }
Copy-Item (Join-Path $GovRoot 'SKILL.md') (Join-Path $skillDir 'SKILL.md') -Force
$agentsDir = Join-Path $skillDir 'agents'
if (-not (Test-Path $agentsDir)) { New-Item -ItemType Directory -Path $agentsDir -Force | Out-Null }
@'
name: paper-ecology-governance
description: Global AI constitution for Paper Ecology / MannyAI / CQE_CMPLX
'@ | Set-Content (Join-Path $agentsDir 'openai.yaml')
Write-Host "CODEX SKILL: $skillDir"

Write-Host "`nDone. Constitution: $GovRoot"
