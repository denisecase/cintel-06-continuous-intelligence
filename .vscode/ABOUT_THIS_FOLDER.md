# VS Code Configuration (`.vscode/`)

> OPTIONAL: Nothing in this folder is required to run a Python project.

This folder provides optional configuration for
Visual Studio Code (VS Code), a widely used code editor.

These files help establish a consistent development environment by
recommending useful extensions and configuring editor behavior.

## Professional Practice

WHY: Project-level editor configuration files
help contributors work with consistent tools and conventions
without requiring everyone to configure their editor manually.

## .vscode Files

Included:

- `extensions.json` - Recommends VS Code extensions.
  VS Code may offer to install them when the project is opened.
  Installation is optional.
- `settings.json` - Defines project-specific editor preferences,
  such as formatting, linting, and Python development settings.

Professional projects may also include:

- `launch.json` - Defines configurations for running and debugging applications.
- `tasks.json` - Defines repeatable development tasks, such as running tests or builds.

All files are optional.

## Special Case: JSON with Comments

**Standard JSON does not allow comments**,
but VS Code supports comments
in its configuration files (JSON with Comments, or JSONC).

These files are intended for VS Code and may not be valid in tools
expecting strict JSON.
