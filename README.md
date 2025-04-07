# 🧵 End-to-End Chest Cancer Classification using MLflow & DVC

An end-to-end pipeline for Chest Cancer Classification leveraging **MLflow** for experiment tracking and **DVC** for pipeline orchestration and data versioning. Deployment is powered by **AWS** and **GitHub Actions**.

---

## ✨ Project Overview

- **ML pipeline**: Data ingestion ➡️ Data transformation ➡️ Model training ➡️ Evaluation ➡️ Deployment
- **Tools Used**:
  - MLflow for experiment tracking
  - DVC for pipeline orchestration & data versioning
  - AWS EC2 & ECR for containerization and deployment
  - GitHub Actions for CI/CD

---

## ⚙️ Workflow Structure

### 1. **Configuration**
- Update `config.yaml` — Project configurations
- Update `secrets.yaml` *(optional)* — Secrets & credentials
- Update `params.yaml` — Hyperparameters
- Update the entity & configuration manager inside `src/config`

### 2. **Development**
- Update & implement components
- Update the pipeline
- Update `main.py` to run the workflow
- Update `dvc.yaml` for pipeline orchestration

### 3. **Pipeline Execution**
```bash
# Initialize DVC
dvc init

# Visualize pipeline DAG
dvc dag

# Reproduce pipeline
dvc repro
```

### 4. **Experiment Tracking (MLflow)**
```bash
# Run MLflow tracking server locally
mlflow ui

# Or export environment variables for remote tracking (Dagshub)
export MLFLOW_TRACKING_URI=https://dagshub.com/username/titleofyourrepisotory.git
export MLFLOW_TRACKING_USERNAME=username
export MLFLOW_TRACKING_PASSWORD=yourToken

# Run your training script
python script.py
```

> ✅ **Tip:** Use [Dagshub](https://dagshub.com) for a collaborative MLflow dashboard and DVC remote storage.

---

## 🧰 About MLflow & DVC

| MLflow | DVC |
| ------ | --- |
| Production-grade experiment tracker | Lightweight for POC and rapid experiments |
| Track experiments, logs, models, and metrics | Data versioning & pipeline orchestration |
| Easy integration with cloud dashboards | Visualize pipeline with `dvc dag` |

---

## ☁️ AWS CI/CD Deployment with GitHub Actions

### Pre-requisites
- AWS Console access
- IAM user with necessary policies:
  - `AmazonEC2ContainerRegistryFullAccess`
  - `AmazonEC2FullAccess`

### Steps

1. **Create AWS Resources**
   - **ECR Repository** for Docker images  
     Example: `566373416292.dkr.ecr.us-east-1.amazonaws.com/chest-cancer-classifier`
   - **EC2 Instance (Ubuntu)** to host your application

2. **Install Docker on EC2**
```bash
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

3. **Configure EC2 as Self-hosted GitHub Runner**
- Go to **GitHub > Settings > Actions > Runners > New self-hosted runner**
- Choose OS, and run setup commands in EC2

4. **Setup GitHub Secrets**
| Key | Value |
| --- | ----- |
| `AWS_ACCESS_KEY_ID` | *your AWS access key* |
| `AWS_SECRET_ACCESS_KEY` | *your AWS secret key* |
| `AWS_REGION` | `us-east-1` |
| `AWS_ECR_LOGIN_URI` | `566373416292.dkr.ecr.us-east-1.amazonaws.com` |
| `ECR_REPOSITORY_NAME` | `chest-cancer-classifier` |

5. **CI/CD Pipeline**
- Build Docker image
- Push to ECR
- Launch EC2 instance
- Pull Docker image from ECR
- Run the container in EC2

---

## 📒 Documentation & Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)
- [Dagshub](https://dagshub.com/)
- [AWS ECR Documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

---

## 🥈 Future Improvements

- ✅ Add unit & integration testing
- ✅ Add automated model registry & promotion to production
- ✅ Integrate monitoring with Grafana & Prometheus
- ✅ Add cloud storage for DVC (S3 / GCS)

---

*Happy coding! 🚀*
