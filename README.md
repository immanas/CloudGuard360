# 🌩️ CloudGuard360

**CloudGuard360** is a real-time, cloud usage and billing monitoring dashboard built using AWS Lambda, API Gateway, and a modern React frontend. It helps you visualize AWS service usage, track daily billing trends, and prepare for cost optimization — all in one sleek dashboard.

> 🔒 Think of it as your personal AWS billing and usage control tower.


## ⚠️ Key Cloud Challenges Identified(problems)


| 🧠 **Category**             | 💥 **Problem / Challenge**                                                                         | 🚨 **Severity** |
|----------------------------|-----------------------------------------------------------------------------------------------------|-----------------|
| 🧾 Cloud Cost Visibility    | AWS bills are delayed and hard to interpret — overspending is realized too late                    | 🔴 Major        |
| 🛑 Usage Blind Spots        | No quick way to view what services (like EC2/S3) are running or how much they consume              | 🔴 Major        |
| 🖼️ UI Inaccessibility      | AWS Console dashboards are not beginner-friendly or customizable                                   | 🟠 Moderate     |
| 🔧 Complex Billing APIs     | Cost Explorer API is complex — requires pagination, auth, and JSON manipulation                   | 🟠 Moderate     |
| 🌐 CORS / API Access        | Frontend apps can’t access AWS APIs directly due to CORS and credential issues                    | 🟠 Moderate     |
| 🧪 Fake vs Real Data        | Many dashboards show dummy data which hurts trust                                                  | 🔴 Major        |
| 🗃️ Disjointed Interfaces   | Cost, usage, and security info are scattered across different AWS pages                            | 🔴 Major        |
| 📊 Lack of Visual Insights  | Raw AWS tables/JSON are hard to interpret                                                          | 🟠 Moderate     |
| 🔐 API Security Risks       | Exposing secrets or credentials in frontend is risky                                               | 🔴 Major        |
| 🧳 No Shareable View        | AWS Console can’t be customized or shared externally                                               | 🟠 Moderate     |


## 🔍 Problems Solved by CloudGuard360

| 🧠 **Category**             | ✅ **CloudGuard360’s Solution**                                                                                                  |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 🧾 Cloud Cost Visibility    | • Integrated AWS Cost Explorer in Lambda to **fetch daily billing data for last 60 days** <br>• Visualized trends in React using Recharts |
| 🛑 Usage Blind Spots        | • Added a **real-time usage table** showing EC2 vCPU, S3 GB, and CloudWatch alarm count (mocked) <br>• All usage pulled via a centralized Lambda |
| 🖼️ UI Inaccessibility      | • Built a **fully custom React dashboard** using Tailwind CSS <br>• Includes cards, tables, and charts with responsive layout              |
| 🔧 Complex Billing APIs     | • Wrapped complex AWS Cost Explorer logic inside Lambda <br>• Handled auth, pagination, and formatting — exposed via simple `/data` API   |
| 🌐 CORS / API Access        | • Configured API Gateway with **CORS headers** <br>• Enabled secure frontend-backend communication without exposing credentials            |
| 🧪 Fake vs Real Data        | • Dashboard shows **real billing data** directly from AWS Cost Explorer <br>• Usage stats shown with placeholder logic for expandability     |
| 🗃️ Disjointed Interfaces   | • Unified **billing + usage + infrastructure metrics** in a single-pane dashboard <br>• No need to log into AWS console for summaries      |
| 📊 Lack of Visual Insights  | • Used **Recharts** to display daily cost trends <br>• Made billing data easy to scan via tooltips, grids, and smooth line charts         |
| 🔐 API Security Risks       | • API uses **IAM-secured Lambda**, with no frontend secrets <br>• Follows secure architecture: Lambda → API Gateway → React               |
| 🧳 No Shareable View        | • Entire dashboard is **frontend-agnostic and portable** <br>• Can be deployed to GitHub Pages or any static hosting provider             |


## 🧰 Tech Stack Used


| 🔧 Area                  | 💡 What I Used (and Why)                                                                                  |
|--------------------------|------------------------------------------------------------------------------------------------------------|
| ☁️ **Cloud Platform**     | **AWS** — End-to-end architecture deployed on cloud-native services like Lambda, API Gateway, and S3       |
| 🌐 **Multi-Cloud Scope**  | **GCP Billing API (Integrated)** — Added GCP cost-fetching to make the dashboard cross-cloud compatible     |
| 🧠 **Serverless Compute** | **AWS Lambda (Python)** — Fetches billing data securely from AWS Cost Explorer and returns JSON API        |
| 🛠️ **DevOps & IaC**        | **Terraform** — Provisioned all AWS infra (Lambda, IAM, Gateway, roles, permissions) as code                |
| 📊 **Monitoring APIs**     | **AWS Cost Explorer + CloudWatch SDKs** — Pulled real-time cost + alarm usage data with automated handling |
| 🔐 **Security Controls**   | Scoped **IAM roles**, API **CORS policies**, and zero secrets in frontend for production-grade protection   |
| 📦 **Storage (Optional)**  | **Amazon S3** — Stores frontend app and optionally logs usage/output from Lambda                           |
| 🌐 **API Gateway (REST)**  | Acts as a secure, CORS-enabled public endpoint bridging frontend and Lambda                                |
| 💻 **Frontend Framework**  | **React + Tailwind CSS** — Clean, responsive UI showing billing data and usage summaries                   |
| 📈 **Charts & Graphs**     | **Recharts.js** — Visualizes trends and spikes in AWS/GCP cost over time in line charts                   |
| 🔄 **Data Pipeline Flow**  | React → Axios → API Gateway → Lambda → Cost Explorer/CloudWatch → JSON → Render in dashboard               |


## ⚙️ CloudGuard360 Architecture 


### 🧭 End-to-End Data Flow

- 🧑‍💻 **Frontend: React + Tailwind + Recharts**  
  Interactive dashboard that fetches real-time AWS billing, usage, and alarm metrics.
- 🌐 **API Gateway (REST)**  
  Exposes a secure `/data` endpoint, enabling frontend to query AWS Lambda seamlessly.
- 🧠 **AWS Lambda (Python)**  
  Acts as the core logic layer:
  - Queries **AWS Cost Explorer** for daily billing trends
  - Adds mock EC2/S3/CloudWatch usage for demo
  - Returns JSON data to frontend
- 💰 **AWS Cost Explorer SDK**  
  Provides actual billing data for EC2, S3, CloudWatch, etc., using `get_cost_and_usage()`.
- 📊 **CloudWatch (Optional)**  
  Can be used to count alarms and enhance security monitoring in future.
- 📦 **Amazon S3 (Optional)**  
  Used optionally to host the React frontend or store analytics snapshots.
- 🔐 **IAM + CORS Security**  
  Lambda runs under least-privilege IAM roles. CORS headers allow safe cross-origin requests from React app.

---

### 🛠️ DevOps & IaC Foundation

| 🔧 Component            | ✅ Implementation                                                                 |
|------------------------|------------------------------------------------------------------------------------|
| ☁️ Cloud Provider       | **AWS** — Primary cloud platform for compute, monitoring, and billing services    |
| 🧠 Compute Backend       | **AWS Lambda (Python)** — Serverless function fetching real-time cost + usage     |
| 🌐 API Management       | **API Gateway (REST)** — Secure endpoint between Lambda and React frontend        |
| 📦 Frontend Hosting     | **React + Tailwind** — Deployed locally or on S3/GitHub Pages                     |
| 📈 Data Visualization   | **Recharts.js** — Billing chart with cost trends and spikes                       |
| 🔐 IAM & CORS           | Scoped IAM roles + CORS headers to prevent credential leaks                       |
| ⚙️ Infrastructure as Code | **Terraform** — Provisions Lambda, API Gateway, IAM roles, and (optional) S3 bucket |


## Project Workflow 

