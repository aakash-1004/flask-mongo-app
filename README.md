# Flask Mongo App — CI/CD Pipeline with GitHub Actions

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat&logo=amazonaws&logoColor=white)
![MongoDB Atlas](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=flat&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

A Flask web application with a MongoDB Atlas backend, containerized with Docker and deployed to AWS EC2 via a fully automated GitHub Actions CI/CD pipeline.

---

## 📌 What It Does

A user-facing login/submission page that:
- Accepts user input (name, email, message) via a web form
- Validates and stores submissions in MongoDB Atlas
- Serves a success page on completion
- Exposes a `/api` endpoint returning data from a local JSON file

---

## 🏗️ Architecture

```
User → Flask App (Gunicorn) → MongoDB Atlas
           ↑
     Docker Container
           ↑
       AWS EC2
           ↑
   GitHub Actions CI/CD
           ↑
      Git Push (main)
```

---

## 🔄 CI/CD Pipeline

Every push to `main` triggers the GitHub Actions pipeline:

```
Push to main
    ↓
Checkout code
    ↓
Login to Docker Hub
    ↓
Build Docker image
    ↓
Push to Docker Hub (aakash0908/flask-mongo-app:latest)
    ↓
SSH into AWS EC2
    ↓
Pull latest image + restart container
```

Zero manual intervention after push. All secrets managed via GitHub Secrets — no credentials hardcoded.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, Gunicorn |
| Database | MongoDB Atlas |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2 |
| Registry | Docker Hub |

---

## 🚀 Running Locally

```bash
# Clone the repo
git clone https://github.com/aakash-1004/flask-mongo-app.git
cd flask-mongo-app

# Build Docker image
docker build -t flask-mongo-app .

# Run container
docker run -d \
  -p 5000:5000 \
  -e MONGO_URI="your-mongodb-atlas-uri" \
  -e MONGO_DB="users_db" \
  -e MONGO_COLLECTION="submissions" \
  flask-mongo-app

# Access at http://localhost:5000
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `MONGO_URI` | MongoDB Atlas connection string |
| `MONGO_DB` | Database name |
| `MONGO_COLLECTION` | Collection name |

---

## 📁 Project Structure

```
flask-mongo-app/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container definition
├── .dockerignore       # Docker ignore rules
├── data.json           # Sample API data
├── templates/          # HTML templates
│   ├── index.html      # Submission form
│   └── success.html    # Success page
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Actions pipeline
```
