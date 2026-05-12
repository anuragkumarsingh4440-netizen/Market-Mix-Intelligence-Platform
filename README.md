# MarketMix Intelligence Platform

<p align="center">

AI-Powered Marketing Analytics & Revenue Prediction Platform

</p>

---

# Overview

MarketMix Intelligence Platform is an end-to-end enterprise-grade Machine Learning application designed to simulate real-world marketing analytics systems used by large-scale retail and e-commerce organizations.

The platform enables:

- Marketing campaign performance analysis
- Revenue prediction using ML models
- Real-time API inference
- Interactive business dashboards
- Experiment tracking with MLflow
- Containerized deployment using Docker
- CI/CD automation using GitHub Actions

---

# Business Problem

Modern marketing teams spend millions on campaigns across:

- Digital Ads
- Social Media
- Influencer Marketing
- Search Campaigns
- Email Campaigns

However, businesses often struggle to answer:

- Which campaigns generate maximum revenue?
- What marketing spend leads to better ROI?
- How can future revenue be predicted?
- Which metrics influence conversions most?

This platform solves these challenges using Machine Learning and MLOps engineering.

---

# Key Features

## Machine Learning Pipeline

- Automated data ingestion
- Data validation framework
- Data transformation pipeline
- Feature engineering
- Model training and evaluation
- Best model selection
- Model serialization

---

## MLOps Integration

- MLflow experiment tracking
- Metric logging
- Artifact tracking
- Model versioning
- Reproducible workflows

---

## Backend Engineering

- FastAPI production APIs
- Real-time prediction endpoints
- Swagger documentation
- Modular backend architecture

---

## Frontend Dashboard

- Streamlit interactive UI
- Business KPI visualization
- Real-time revenue prediction
- Executive-friendly analytics interface

---

## DevOps & Deployment

- Docker containerization
- Docker Compose orchestration
- CI/CD pipeline using GitHub Actions
- Production-ready deployment architecture

---

# Project Architecture

```text
                    ┌────────────────────┐
                    │   Business Users   │
                    └─────────┬──────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │ Streamlit Dashboard UI │
                 └─────────┬──────────────┘
                           │ HTTP Request
                           ▼
                ┌─────────────────────────┐
                │    FastAPI Backend      │
                └─────────┬───────────────┘
                          │
                          ▼
               ┌──────────────────────────┐
               │ Prediction Pipeline      │
               └─────────┬────────────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
 ┌────────────────┐         ┌──────────────────┐
 │ Preprocessor   │         │ Trained ML Model │
 └────────────────┘         └──────────────────┘
```

---

# Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| ML Framework | Scikit-learn |
| Backend | FastAPI |
| Frontend | Streamlit |
| Experiment Tracking | MLflow |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
| Data Handling | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Model Serialization | Joblib |

---

# Project Structure

```text
MarketMix-Intelligence-Platform/

│
├── artifacts/
├── config/
├── data/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── monitoring/
│   ├── visualization/
│   ├── utils/
│   ├── logger/
│   └── exception/
│
├── streamlit_app/
│   ├── components/
│   ├── pages/
│   └── Home.py
│
├── tests/
├── .github/
│   └── workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
└── README.md
```

---

# Machine Learning Workflow

## 1. Data Ingestion

- Reads marketing campaign dataset
- Splits train/test data
- Stores processed artifacts

---

## 2. Data Validation

- Schema validation
- Missing value checks
- Column verification
- Data consistency validation

---

## 3. Data Transformation

- Feature scaling
- Numerical preprocessing
- Pipeline serialization

---

## 4. Model Training

Models used:

- Linear Regression
- Random Forest Regressor

Evaluation Metrics:

- R² Score
- MAE
- RMSE

---

## 5. MLflow Tracking

Tracks:

- Parameters
- Metrics
- Models
- Experiments

---

# API Endpoints

## Health Check

```http
GET /
```

Response:

```json
{
  "message": "MarketMix Intelligence API Running"
}
```

---

## Revenue Prediction

```http
POST /predict
```

Parameters:

| Parameter | Type |
|---|---|
| spend | int |
| impressions | int |
| clicks | int |
| conversions | int |
| ctr | float |
| roas | float |

Example Response:

```json
{
  "predicted_revenue": 11433.26
}
```

---

# Running the Project Locally

## Clone Repository

```bash
git clone <repository_url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Backend

```bash
uvicorn src.api.app:app --reload
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running Frontend

```bash
streamlit run streamlit_app/Home.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Docker Deployment

## Build Docker Image

```bash
docker build -t marketmix-platform .
```

---

## Run Container

```bash
docker run -p 8000:8000 marketmix-platform
```

---

# Docker Compose Deployment

## Start Full Stack

```bash
docker compose up --build
```

---

# CI/CD Pipeline

GitHub Actions pipeline automatically performs:

- Dependency installation
- Python validation
- Docker build validation
- Deployment readiness checks

Workflow file:

```text
.github/workflows/ci_cd.yml
```

---

# Sample Business Use Cases

- Marketing Spend Optimization
- Revenue Forecasting
- Campaign Effectiveness Analysis
- ROI Prediction
- Performance Monitoring
- Executive Decision Support

---

# Future Enhancements

- Cloud deployment (AWS/Azure/GCP)
- Kubernetes orchestration
- Authentication & Authorization
- Drift detection
- Real-time monitoring dashboards
- LLM-powered analytics assistant
- Advanced forecasting models
- Automated retraining pipelines

---

# Engineering Highlights

This project demonstrates:

- Modular software engineering
- MLOps best practices
- Backend API development
- Full-stack ML deployment
- DevOps automation
- Enterprise architecture patterns

---

# Author

Anurag Kumar Singh

---

# License

This project is intended for educational, portfolio, and enterprise learning purposes.
