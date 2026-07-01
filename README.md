
# 🚀 SVG App on Kubernetes

A full-stack microservices application deployed on Kubernetes using Helm, featuring a frontend UI, backend API, PostgreSQL database with persistence, Ingress routing, monitoring with Grafana/Prometheus, and automated CI/CD pipelines.

---

## 📦 Architecture

🌐 http://myapp
            │
       Ingress (Traefik)
            │
     ┌──────┴────────┐
     │               │

Frontend (nginx)      Grafana
│
▼
Backend (FastAPI)
│
▼
PostgreSQL (PVC)

---

## 🧰 Tech Stack

- ✅ Kubernetes
- ✅ Helm
- ✅ FastAPI (Python)
- ✅ PostgreSQL (Persistent Volume)
- ✅ Nginx (Frontend)
- ✅ Traefik (Ingress)
- ✅ Prometheus & Grafana (Monitoring)
- ✅ GitHub Actions (CI/CD)

---

## ✨ Features

- 🖼️ SVG-based interactive UI
- 📊 Click tracking per image
- 🔄 REST API backend
- 💾 Persistent PostgreSQL storage
- 🌐 Custom domain (`http://myapp`)
- 📈 Monitoring with Grafana dashboards
- ⚙️ Helm-based deployment
- 🚀 Automated CI/CD pipeline

---

## 🚀 Quick Start

### 1. Clone repo

git clone https://github.com/Vlad1slav1k/svg-app.git

cd svg-app

**2. Deploy application**

helm install my-app ./helm-app

**3. Configure local domain**
Edit /etc/hosts:
<INGRESS_IP> myapp grafana

Example:
172.18.0.2 myapp grafana


**4. Access applications**

http://myapp

http://grafana

**🔐 Grafana Login**   
kubectl get secret monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo


**** Database Setup (first run only)****

kubectl exec -it <postgres-pod> -- psql -U postgres -d appdb   

CREATE TABLE clicks (
    button_id INT PRIMARY KEY,
    count INT DEFAULT 0
);


Project Structure
.
├── backend/        # FastAPI service
├── frontend/       # Nginx + HTML/JS
├── helm-app/       # Helm chart
│   ├── templates/
│   └── values.yaml
└── README.md

Monitoring

Prometheus collects cluster + app metrics
Grafana provides dashboards
Accessible via http://grafana



# ⚙️ CI/CD Pipeline

The project includes a GitHub Actions pipeline:

### ✅ CI (Continuous Integration)
- Builds Docker images for backend and frontend  
- Tags images with commit SHA  
- Pushes images to GitHub Container Registry (GHCR)

### ✅ CD (Continuous Delivery)
- Updates Helm `values.yaml` with new image versions  
- Commits changes back to repository (GitOps-style)

### 🔄 Deployment
- Deployment is triggered locally via Helm:
  
```bash
helm upgrade --install my-app ./helm-app

