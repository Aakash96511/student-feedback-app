# Student Feedback Web Application - DevOps Project

## Problem Statement

Develop a simple web-based student feedback application that allows a user to enter their name, course, and feedback. The application displays the submitted feedback on a webpage. Implement a basic CI/CD pipeline using GitHub Actions.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Git
- GitHub
- GitHub Actions
- Pytest
- Docker
- VS Code

## Project Structure

```text
student-feedback-app/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
├── app.py
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Run on Windows using VS Code

Open the project folder in VS Code.

### 1. Create a virtual environment

For Python 3.13:

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the application without activating the environment after installing dependencies into the environment:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe app.py
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Start the application

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Health check:

```text
http://127.0.0.1:5000/health
```

## Run Tests

```powershell
pytest
```

## Git and GitHub

Initialize Git:

```powershell
git init
git add .
git commit -m "Initial student feedback application"
```

Create a GitHub repository named:

```text
student-feedback-app
```

Then connect your local project to GitHub using the repository URL provided by GitHub:

```powershell
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## CI/CD

The GitHub Actions workflow is located at:

```text
.github/workflows/ci-cd.yml
```

Whenever code is pushed to the `main` branch, GitHub Actions:

1. Checks out the source code.
2. Sets up Python 3.13.
3. Installs dependencies.
4. Runs Pytest.
5. Builds the Docker image if tests pass.

## Docker

Build the image:

```powershell
docker build -t student-feedback-app .
```

Run it:

```powershell
docker run -p 5000:5000 student-feedback-app
```

Then open:

```text
http://127.0.0.1:5000
```

## DevOps Flow

```text
VS Code
   |
   v
Git
   |
   v
GitHub
   |
   v
GitHub Actions
   |
   +--> Install dependencies
   |
   +--> Run tests
   |
   +--> Build Docker image
   |
   v
Application ready for deployment
```

## Important Note

The application stores feedback in memory for this academic demonstration. Restarting the Flask application clears the submitted feedback. A database can be added as a future enhancement.
