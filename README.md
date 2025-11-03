# Flask CI/CD Pipeline with GitHub Actions and DockerHub

## Overview
This is a simple project that shows how to build a **CI/CD pipeline** using **GitHub Actions** and **DockerHub**.  

The app is a small Flask web service that runs inside a Docker container.  
Each time I push code to GitHub, the pipeline automatically:
1. Runs tests to make sure everything works.  
2. Builds a Docker image.  
3. Pushes the image to DockerHub if all tests pass.

This setup is a practical example of how DevOps automation works in real life.

---

## Tools 
- **Flask** – simple Python web framework  
- **Pytest** – for automated testing  
- **Docker** – to containerize the app  
- **GitHub Actions** – for CI/CD automation  
- **DockerHub** – to store built images  

---

## Project Structure

flask-ci-cd-pipeline/
│
├── app/
│ ├── app.py # Flask application
│ ├── requirements.txt # Dependencies
│ └── test_app.py # Unit tests
│
├── Dockerfile # Docker build instructions
└── .github/
└── workflows/
└── ci.yml # CI/CD pipeline



---

## How It Works
- Push code to GitHub.  
- GitHub Actions runs the tests automatically.  
- If tests pass, a Docker image is built and uploaded to DockerHub.  
- The image can then be deployed anywhere — like AWS or ECS.

---

## 💻 Run It Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/flask-ci-cd-pipeline.git
   cd flask-ci-cd-pipeline

2. Build the image:
```bash
docker build -t flask-ci-demo .
```
3. Run the container:
```bash
docker run -p 5000:5000 flask-ci-demo
```

4. Open your browser and visit:
   http://localhost:5000

What I Learned
How CI/CD works from start to finish.
How to automate testing and builds with GitHub Actions.
How to push Docker images to DockerHub.
The importance of using secrets and automation in DevOps pipelines.
