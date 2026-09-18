# CSI2113 Practical Assessment – Containerized Web Application with CI/CD

This project is a simple Task Manager web application developed using Python Flask.

## Technologies

- Python Flask
- SQLite
- Git and GitHub
- Docker
- Docker Compose
- Docker Hub
- GitHub Actions

## Application

The application allows users to create and manage tasks.

It runs locally at:

http://localhost:5000

## Docker

The application is containerized using Docker.

A Dockerfile is used to build the application image, and Docker Compose is used to configure and run the application container.

## CI/CD Pipeline

GitHub Actions is used to automate the CI/CD process.

The workflow is:

Code Push
→ Run Tests
→ Build Docker Image
→ Push Image to Docker Hub
→ Deploy to Local Computer

The local deployment uses a Windows self-hosted GitHub Actions runner.

## Run the Application

Install the dependencies:

pip install -r requirements.txt

Run locally:

python app.py

Or run using Docker Compose:

docker compose up -d

Then open:

http://localhost:5000
