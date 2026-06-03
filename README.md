# Exam CI Practical

This project demonstrates a basic Python CI/CD pipeline with GitHub Actions and Docker.

## What the workflow does

The workflow in [.github/workflows/ci.yml](.github/workflows/ci.yml) runs on:

- pushes to `main`
- version tags like `v1.0.0`
- pull requests
- manual runs from the GitHub Actions tab

It performs these steps:

1. Installs Python 3.11
2. Installs dependencies and `pytest`
3. Compiles the app with `python -m compileall app`
4. Runs automated tests with `python -m pytest`
5. Builds a Docker image
6. Pushes the image to GitHub Container Registry when the workflow is not a pull request

## Files to show

- [.github/workflows/ci.yml](.github/workflows/ci.yml)
- [app/server.py](app/server.py)
- [tests/test_server.py](tests/test_server.py)
- [Dockerfile](Dockerfile)
- [requirements.txt](requirements.txt)

## Commands already executed

- `c:/python314/python.exe -m compileall app`
- `c:/python314/python.exe -m pytest -q`
- `docker build -t exam-app:test .`
# EXAM
