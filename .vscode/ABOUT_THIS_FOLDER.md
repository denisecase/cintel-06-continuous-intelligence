# VS Code Configuration (`.vscode/`)

This folder contains **optional editor configuration files** for Visual Studio Code.
They are provided to support a consistent, professional development experience,
but **nothing in this folder is required to run the code**.

## Scope

You do not need to understand or edit these files.
They exist to:

- prevent common conflicts
- model professional project structure

## Important Note About JSON and Comments

**Standard JSON does NOT allow comments.**

However, **VS Code intentionally allows comments** in certain configuration files
inside the `.vscode/` folder as a documented exception.

This means:

- These files are valid **for VS Code only**
- They should **not** be reused as general-purpose JSON files
- Comments are used here deliberately for teaching and documentation

Do not copy these files into other tools or contexts that expect strict JSON.

## Files

- `extensions.json` Recommends VS Code extensions as **suggestions**,
- not requirements.
- VS Code may prompt you to install these when you open the project.

- `settings.json` (Optional) Editor preferences that
  apply only to this workspace,
  such as formatting behavior or linting integration.
