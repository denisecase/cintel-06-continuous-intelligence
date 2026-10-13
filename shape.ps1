#Requires -Version 5.1

<#
============================================================
shape.ps1 (ALL-REPOS) - Show Project Shape
============================================================
Updated: 2026-10-11

WHAT: A PowerShell script that lists the files and directories
      currently present in a project.
      PowerShell scripts use the .ps1 file extension.

WHEN: Use when reviewing or sharing the current project structure.
      Running the script is optional.

WHY: Provide a concise, copyable view of the current project
     structure for communication and collaboration.

POWERSHELL: PowerShell is a command shell and scripting language.
            Windows includes Windows PowerShell 5.1.
            The newer PowerShell (pwsh) is free and cross-platform.
            Windows, macOS, and Linux users can install pwsh.

HOW: Open a PowerShell terminal in the project root and run:

     .\shape.ps1

TOOLS: PowerShell inspects the local file system.
       Git, Python, and other development tools are not required.

SKILLS: PowerShell, scripting, project structure,
        file-system navigation, and technical communication.

OBS: Lists files and directories whether or not Git tracks them.
OBS: Includes newly created files and empty directories.
OBS: Excludes common generated, cached, and build directories.
OBS: Collapsed directories are listed without their contents.
OBS: Does not modify project files or directories.

CUSTOM: Adjust excluded directory names when necessary.
CUSTOM: Adjust collapsed directory paths when necessary.
============================================================
#>

# === CONFIGURE EXCLUDED DIRECTORIES ===

# WHY: These directories contain generated, cached, downloaded, or temporary
#      content rather than authored project structure.
#
# NOTE: Entries are directory names, not path or .gitignore patterns.
# NOTE: Do not include leading or trailing slashes.
# NOTE: Each name is matched against every directory component in the project,
#       so "bin" excludes directories named bin at any depth.

$excludedDirectories = @(
    ".cache",
    ".eggs",
    ".git",
    ".ipynb_checkpoints",
    ".lake",
    ".mypy_cache",
    ".nox",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".tox",
    ".venv",
    ".vscode-test",
    "__pycache__",
    "bin",
    "build",
    "coverage",
    "dist",
    "htmlcov",
    "node_modules",
    "out",
    "site",
    "venv"
)


# === CONFIGURE COLLAPSED DIRECTORIES ===

# WHY: Some generated directories are useful to show as part of the project
#      structure but contain too many files to list individually.
#
# NOTE: Entries are paths relative to the project root.
# NOTE: Use forward slashes for cross-platform consistency.
# NOTE: The directory itself remains visible.
# NOTE: All files and subdirectories beneath it are omitted.
# NOTE: Unlike excluded directory names, these paths match only
#       their specified location in the project.
#
# CUSTOM: Add other generated asset directories when needed.

$collapsedDirectories = @(
    "docs/app/assets"
)


# === GET PROJECT SHAPE ===

$projectRoot = (Get-Location).Path

Get-ChildItem -Path $projectRoot -Recurse -Force |
    Where-Object {
        $relativePath = $_.FullName.Substring($projectRoot.Length).TrimStart('\', '/')

        $pathParts = $relativePath -split '[\\/]'

        $exclude = $false

        # WHY: Exclude generated directories and everything beneath them.
        foreach ($directory in $excludedDirectories) {
            if ($pathParts -contains $directory) {
                $exclude = $true
                break
            }
        }

        # WHY: Keep selected generated directories visible while hiding
        #      their contents from the project shape.
        if (-not $exclude) {
            $normalizedPath = $relativePath -replace '\\', '/'

            foreach ($directory in $collapsedDirectories) {
                if ($normalizedPath.StartsWith(
                    "$directory/",
                    [System.StringComparison]::OrdinalIgnoreCase
                )) {
                    $exclude = $true
                    break
                }
            }
        }

        -not $exclude
    } |
    ForEach-Object {
        $relativePath = $_.FullName.Substring($projectRoot.Length).TrimStart('\', '/')

        if ($_.PSIsContainer) {
            ".\$relativePath\"
        }
        else {
            ".\$relativePath"
        }
    } |
    Sort-Object -Unique
