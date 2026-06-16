
# 🚀 SVG App on Kubernetes

A full-stack microservices application deployed on Kubernetes using Helm, featuring a frontend UI, backend API, PostgreSQL database with persistence, Ingress routing, and monitoring with Grafana/Prometheus.

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

---

## ✨ Features

- 🖼️ SVG-based interactive UI
- 📊 Click tracking per image
- 🔄 REST API backend
- 💾 Persistent PostgreSQL storage
- 🌐 Custom domain (`http://myapp`)
- 📈 Monitoring with Grafana dashboards
- ⚙️ Helm-based deployment

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


** Database Setup (first run only)**

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

