# 🚀 CI/CD Pipeline with Jenkins, Docker & Kubernetes

## 📌 Project Overview

This project demonstrates a complete CI/CD pipeline implemented with Jenkins, where the application is deployed on Kubernetes, using:

- ✅ Jenkins (deployed via Helm using the official [jenkinsci/jenkins](https://artifacthub.io/packages/helm/jenkinsci/jenkins) chart)
- ✅ Docker
- ✅ Kubernetes (Minikube as a local cluster)
- ✅ GitHub
- ✅ Test Driven Development (TDD) with automated unit tests

The pipeline is automatically triggered by a GitHub push event and performs the following steps:
1. Runs unit tests
2. Builds a Docker image
3. Deploys the application to Kubernetes

---

## 🏗 Architecture
GitHub
↓
Jenkins (running inside Kubernetes)
↓
Dynamic Kubernetes Agent Pod
↓
Docker Build
↓
Kubernetes Deployment
↓
Flask Application running in cluster

---

## 📁 Project Structure

flask_hello_jenkins/
│
├── Jenkinsfile # CI/CD pipeline definition
│
├── flask_app/ # Application source code
│ ├── app.py
│ ├── test.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── kubernetes/
│ ├── deployment.yml
│ └── service.yml
│
└── jenkins_k8s/ # Jenkins Helm configuration
  └── values.yaml

---

## 🧱 Infrastructure

### 🔹 Jenkins Deployment

Jenkins is deployed in Kubernetes using Helm.

Configuration is stored in:

jenkins_k8s/values.yaml

This file customizes:
- Admin credentials
- Service type (NodePort)
- Installed plugins
- Kubernetes agent configuration

---

## 🔄 CI/CD Pipeline (Jenkinsfile)

The pipeline includes:

### 1️⃣ Test Stage
- Install Python dependencies
- Execute unit tests
- TDD workflow supported

### 2️⃣ Build Stage
- Build Docker image inside Kubernetes agent
- Image built inside Minikube Docker daemon

### 3️⃣ Deploy Stage
- Apply Kubernetes Deployment
- Apply Kubernetes Service
- Expose app via NodePort

---

## 🧪 Test Driven Development (TDD)

A feature branch strategy is used:

- `main` → stable branch
- `feature1` → new feature development

Workflow:
1. Write failing test
2. Push feature branch
3. Observe pipeline failure
4. Implement feature
5. Pipeline passes ✅

---

## ☸ Kubernetes Deployment

Deployment:
- 1 replica
- imagePullPolicy: IfNotPresent

Service:
- NodePort exposed on port `31000`

---

## 🔐 RBAC Configuration

Jenkins service account requires permissions:

```bash
kubectl create clusterrolebinding jenkins-admin \
  --clusterrole=cluster-admin \
  --serviceaccount=jenkins:jenkins

🚀 How to Run Locally

1️⃣ Start Minikube
minikube start
2️⃣ Install Jenkins
Bash

helm install jenkins jenkins/jenkins -f jenkins_k8s/values.yaml -n jenkins
3️⃣ Push Code
Bash

git push origin main
Pipeline runs automatically.

🎯 Skills Demonstrated

CI/CD pipeline design
Kubernetes-native Jenkins agents
Docker image build inside K8s
RBAC configuration
Branch-based development workflow
Infrastructure as Code (Helm)
Debugging Kubernetes workloads

📌 Future Improvements

Replace docker.sock with Kaniko
Add Helm chart for application
Use GitHub webhook instead of polling
Add image tagging with commit SHA
Implement staging and production environments

👤 Author

FANOMEZANTSOA Bien Aimé Louison
DevOps Engineer
GitHub: FANOMEZANTSOA-Bien-Aime-Louison
LinkedIn: in/fanomezantsoa-bien-aime-louison-b33749285