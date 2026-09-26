# Alternative Execution: Containers in the Cloud (GitHub Actions)

> Optional Exploration (not required)

This project can be packaged and executed
in a Docker container without installing Docker locally.

Instead of running the pipeline on your machine,
you can use GitHub Actions to:

- build a container image from a Dockerfile
- run the project inside that container
- view logs from the execution

This approach avoids local setup issues and
provides a reproducible execution environment.

## Docker Containers

Containers package an application with its environment:

- Python version
- dependencies
- project files

It ensures the project runs the same way across systems.

In industry, containers are commonly used for deployment and scaling.
We illustrate them as an optional extension
to understand packaging and reproducibility.

## Requirements

Adding this option requires:

- a Dockerfile in the project root
- a GitHub Actions workflow file

No Docker installation is required on your local machine.
Docker Desktop is **not** recommended on many Windows machines.

## Step 1. Add a Dockerfile

Create a file named `Dockerfile` in the project root.

See the example file provided.

IMPORTANT: Adjust the final command when your custom project
entry point (the module name) differs.

## Step 2. Add a GitHub Actions Workflow

Create a file: `.github/workflows/deploy-docker.yml`

See the example file provided.

## Step 3. Run the Workflow

1. Push your changes to GitHub
2. Open the Actions tab
3. Select the workflow with the name e.g. `Docker Container and Quality Checks`
4. Look for:
   - Job 1 - Run Docker pre-commit
   - Job 2 - Build Docker image
   - Job 3 - Run project in container
5. Click to expand **Job 3 A3) Run project** to see the logs:

You should see:

```text
========================
Pipeline executed successfully!
========================
```

## Explore

As the workflow runs, note:

- how dependencies are installed inside the container
- how the pipeline runs without your local environment
- any errors during build or execution

These logs provide insight into how software
is packaged and executed in production systems.

## Share Your Results

If you experiment with containers, document:

- your operating system (if you also tried locally)
- any setup steps
- issues encountered
- performance observations
- link to your repository

## Reusability

This pattern is reusable across projects:

- Dockerfile defines execution environment
- GitHub Actions provides remote execution
- No local Docker installation is required (nice for Windows users)

---

[◄ Back to 🏠 Home](index.md)
