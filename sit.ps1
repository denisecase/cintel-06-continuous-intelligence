#Requires -Version 7.0

<#
============================================================
sit.ps1 (ALL-PY-SRC-REPOS)
============================================================
Updated: 2026-09-25

This is a PowerShell script for managing
the development environment of the project.

PowerShell (pwsh) is available for all major operating systems
and is a popular terminal for developers.

To get situated, run this script in your PowerShell terminal:

.\sit.ps1

#>

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ============================================================
# Precheck: pyproject.toml must use [dependency-groups], not the
# old [project.optional-dependencies]. With the old table, `uv sync`
# succeeds but does NOT install dev/docs, and later steps fail confusingly.
# ============================================================
if (Test-Path "pyproject.toml") {
    $pyproject = Get-Content "pyproject.toml" -Raw
    if ($pyproject -match '(?m)^\[project\.optional-dependencies\]') {
        Write-Host ""
        Write-Host "ERROR: pyproject.toml uses the old [project.optional-dependencies] table." -ForegroundColor Red
        Write-Host ""
        Write-Host "This repo has not been migrated. 'uv sync' would run but NOT install" -ForegroundColor Yellow
        Write-Host "the dev and docs dependencies, so linting, tests, and docs would fail." -ForegroundColor Yellow
        Write-Host ""
        Write-Host "FIX: open pyproject.toml and rename this one line:" -ForegroundColor Cyan
        Write-Host "    [project.optional-dependencies]   ->   [dependency-groups]" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Then run .\sit.ps1 again." -ForegroundColor Cyan
        Write-Host ""
        exit 1
    }
}

# set up or update Python environment
uvx pup-clean --delete
uv self update
uv python install
uv lock --upgrade
uv sync
uv audit

# set up and run git hooks
uv run prek install --force
uv run prek update
git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files

# run common chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

Write-Host "All commands executed successfully."
Write-Host "Run a Python module to verify .venv/ is working correctly."
