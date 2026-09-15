# CSI2113 Practical Assessment – Containerized Web Application with CI/CD

A small Flask Task Manager demonstrating Git/GitHub, Docker, Docker Compose,
Docker Hub, and GitHub Actions CI/CD.

## Architecture

Developer -> Git -> GitHub -> GitHub Actions -> Tests -> Docker Build
-> Docker Hub -> self-hosted runner on local computer -> Docker Compose
-> Running Flask application

## Run locally

1. Install Python 3.12 and Docker.
2. Create a virtual environment:
   `python -m venv .venv`
3. Activate it and install:
   `pip install -r requirements.txt`
4. Run:
   `python app.py`
5. Open http://localhost:5000

## Run with Docker Compose

Create `.env` from `.env.example` and put your Docker Hub username in it.

Then:
`docker compose pull`
`docker compose up -d`

Open http://localhost:5000.

## CI/CD

The workflow has three jobs:

1. `test` – installs Python dependencies and runs pytest.
2. `docker` – logs into Docker Hub, builds the image, and pushes it.
3. `deploy-local` – runs on a self-hosted GitHub Actions runner installed
   on the local computer. It pulls the new image and restarts the Compose
   application.

Required GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

The local computer must have Docker, Docker Compose, and a configured
self-hosted GitHub Actions runner. Clone/copy this repository to:
`$HOME/csi2113-task-manager`

## Suggested meaningful commits

- `feat: create Flask task manager`
- `test: add API health and task tests`
- `build: add Dockerfile and compose configuration`
- `ci: add GitHub Actions test and Docker build`
- `ci: add Docker Hub push and local deployment`

## Viva demonstration

Show:
1. Working application.
2. Git log with meaningful commits.
3. GitHub repository.
4. Dockerfile.
5. Docker Compose file.
6. Docker Hub image/tag.
7. GitHub Actions successful run.
8. Local self-hosted runner.
9. Running container using `docker ps`.
10. Application at http://localhost:5000.
11. Make a small code change, commit/push it, and show the pipeline run.
