# ============================================================
# Dockerfile (Containerized Execution)
# ============================================================
# WHY-FILE: Package and run the continuous intelligence pipeline
#           in a reproducible container environment.
# REQ: uv-based project with pyproject.toml and uv.lock present.

# ============================================================
# BASE IMAGE
# ============================================================
# WHY: Use a minimal official Python image for consistency.
FROM python:3.14-slim

# ============================================================
# SET WORKING DIRECTORY
# ============================================================
# WHY: All commands run relative to /app inside the container.
WORKDIR /app

# ============================================================
# COPY PROJECT FILES
# ============================================================
# WHY: Bring all project code and configuration into container.
COPY . .

# ============================================================
# ASSEMBLE: INSTALL TOOLING
# ============================================================
# WHY: Install uv to manage Python and dependencies.
RUN pip install --no-cache-dir uv

# ============================================================
# ASSEMBLE: PREPARE PYTHON ENVIRONMENT
# ============================================================
# WHY: Ensure correct Python version and environment setup.
RUN uv python pin 3.14

# ============================================================
# ASSEMBLE: INSTALL DEPENDENCIES
# ============================================================
# WHY: Install all required dependencies including dev and docs.
RUN uv sync --extra dev --extra docs --upgrade

# ============================================================
# EXECUTE: RUN APPLICATION
# ============================================================
# WHY: Run the continuous intelligence pipeline module.
CMD ["uv", "run", "python", "-m", "cintel.continuous_intelligence"]
