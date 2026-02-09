# 🌩️ CloudGuard360

**CloudGuard360**  is a real-time, cloud usage and billing monitoring dashboard built using AWS Lambda, API Gateway, and a modern React frontend. It helps you visualize AWS service usage, track daily billing trends, forecast upcoming cloud costs using lightweight ML in Lambda, and prepare for cost optimization — all in one sleek dashboard.


> 🔒 Think of it as your personal AWS billing and usage control tower..

## 🧠 One-Line Truth

**A serverless multi-cloud cost visibility and forecasting system that analyzes cloud spending and surfaces insights through a lightweight dashboard.**


## ⚠️ Real-Life Cloud Problems (Problem Table)  


| 🧠 **Category**             | 💥 **Problem / Challenge**                                                                         | 🚨 **Severity** |
|----------------------------|-----------------------------------------------------------------------------------------------------|-----------------|
| 🧾 Cloud Cost Visibility    | AWS bills are delayed and hard to interpret — overspending is realized too late                    | 🔴 Major        |
| 🛑 Usage Blind Spots        | No quick way to view what services (like EC2/S3) are running or how much they consume              | 🔴 Major        |
| 📈 Forecasting Blind Spot   | No built-in insights to **predict future costs** based on current usage trends                     | 🔴 Major     |
| 🧪 Fake vs Real Data        | Many dashboards show dummy data which hurts trust                                                  | 🔴 Major        |
| 🚨 No Alerting Mechanism    | No system to notify when **cost spikes unexpectedly** (e.g., >20% rise in daily spend)             | 🔴 Major        |
| 🗃️ Disjointed Interfaces   | Cost, usage, and security info are scattered across different AWS pages                            | 🔴 Major        |
| 🔐 API Security Risks       | Exposing secrets or credentials in frontend is risky                                               | 🔴 Major        |
| 🖼️ UI Inaccessibility      | AWS Console dashboards are not beginner-friendly or customizable                                   | 🟠 Moderate     |
| 🔧 Complex Billing APIs     | Cost Explorer API is complex — requires pagination, auth, and JSON manipulation                   | 🟠 Moderate     |
| 🌐 CORS / API Access        | Frontend apps can’t access AWS APIs directly due to CORS and credential issues                    | 🟠 Moderate     |
| 📊 Lack of Visual Insights  | Raw AWS tables/JSON are hard to interpret                                                          | 🟠 Moderate     |
| 🧳 No Shareable View        | AWS Console can’t be customized or shared externally                                               | 🟠 Moderate     |


## 🔍 Why CloudGuard360 (Problem → Solution → Impact)

| 🧠 **Category**             | ✅ **CloudGuard360’s Solution**                                                                                                  |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 🧾 Cloud Cost Visibility    | • Integrated AWS Cost Explorer in Lambda to **fetch daily billing data for last 60 days** <br>• Visualized trends in React using Recharts |
| 🛑 Usage Blind Spots        | • Added a **real-time usage table** showing EC2 vCPU, S3 GB, and CloudWatch alarm count (mocked) <br>• All usage pulled via a centralized Lambda |
| 🖼️ UI Inaccessibility      | • Built a **fully custom React dashboard** using Tailwind CSS <br>• Includes cards, tables, and charts with responsive layout              |
| 🔧 Complex Billing APIs     | • Wrapped complex AWS Cost Explorer logic inside Lambda <br>• Handled auth, pagination, and formatting — exposed via simple `/data` API   |
| 🌐 API Access               | • Configured API Gateway with **CORS headers** <br>• Enabled secure frontend-backend communication without exposing credentials            |
| 🧪 Fake vs Real Data        | • Dashboard shows **real billing data** directly from AWS Cost Explorer <br>• Usage stats shown with placeholder logic for expandability     |
| 🗃️ Disjointed Interfaces   | • Unified **billing + usage + infrastructure metrics** in a single-pane dashboard <br>• No need to log into AWS console for summaries      |
| 📈 Forecasting Blind Spot   | • Created forecasting-ready pipeline by exporting S3 usage to CSV <br>• Integrated with SageMaker for **cost prediction using LSTM**      |
| 📊 Lack of Visual Insights  | • Used **Recharts** to display daily cost trends <br>• Made billing data easy to scan via tooltips, grids, and smooth line charts         |
| 🔐 API Security Risks       | • API uses **IAM-secured Lambda**, with no frontend secrets <br>• Follows secure architecture: Lambda → API Gateway → React               |
| 🧳 No Shareable View        | • Entire dashboard is **frontend-agnostic and portable** <br>• Can be deployed to GitHub Pages or any static hosting provider             |


## 📌 What CloudGuard360 IS / IS NOT

### ✅ IS
- Cost visibility and usage analysis tool 💰
- Serverless multi-cloud monitoring system ☁️
- Basic cost forecasting engine 📈
- Lightweight insight dashboard 📊

### ❌ IS NOT
- A full FinOps platform
- A billing system replacement
- A production SaaS product
- Real-time, second-by-second cost tracker

---

## 🎯 Target Users & Use Cases

### 👥 Target Users
- Cloud engineers managing multi-cloud environments ☁️
- DevOps and SRE teams monitoring infrastructure costs ⚙️
- Startups needing simple cost visibility without full FinOps tools 💰
- Students and engineers learning cloud cost optimization 🧠

### 🧩 Use Cases
- Get a quick overview of AWS and GCP spending in one place
- Identify unusual cost spikes or inefficient resources
- Forecast short-term cloud expenses
- Demonstrate cost-aware, serverless architecture in real environments
- Provide a lightweight internal dashboard for cloud usage insights


## 🧰 Tech Stack Used


| 🔧 Area                  | 💡 What I Used (and Why)                                                                                  |
|--------------------------|------------------------------------------------------------------------------------------------------------|
| ☁️ **Cloud Platform**     | **AWS** — End-to-end architecture deployed on cloud-native services like Lambda, API Gateway, and S3       |
| 🌐 **Multi-Cloud Scope**  | **GCP Billing API (Integrated)** — Added GCP cost-fetching to make the dashboard cross-cloud compatible     |
| 🧠 **Serverless Compute** | **AWS Lambda (Python)** — Fetches billing data securely from AWS Cost Explorer and returns JSON API        |
| 🛠️ **DevOps & IaC**        | **Terraform** — Provisioned all AWS infra (Lambda, IAM, Gateway, roles, permissions) as code                |
🧪 **AI/ML Forecasting**  | **SageMaker + LSTM (Python)** — Trained an LSTM model to predict future AWS costs from past 60-day trends      |
| 📊 **Monitoring APIs**     | **AWS Cost Explorer + CloudWatch SDKs** — Pulled real-time cost + alarm usage data with automated handling |
| 🔐 **Security Controls**   | Scoped **IAM roles**, API **CORS policies**, and zero secrets in frontend for production-grade protection   |
| 📦 **Storage (Optional)**  | **Amazon S3** — Stores frontend app and optionally logs usage/output from Lambda                           |
| 🌐 **API Gateway (REST)**  | Acts as a secure, CORS-enabled public endpoint bridging frontend and Lambda                                |
| 💻 **Frontend Framework**  | **React + Tailwind CSS** — Clean, responsive UI showing billing data and usage summaries                   |
| 📈 **Charts & Graphs**     | **Recharts.js** — Visualizes trends and spikes in AWS/GCP cost over time in line charts                   |
| 📉 CloudWatch Monitoring     | • Configured **CloudWatch alarms** to track key AWS metrics (e.g., Lambda errors, usage patterns) <br>• Helps identify unusual behavior or misconfigurations in real-time |
| 📢 SNS Alerting Integration  | • Connected **SNS topic** to CloudWatch to send alerts on threshold breach (e.g., >20% daily cost increase) <br>• Delivers instant email notifications for proactive response |

| 🔄 **Data Pipeline Flow**  | React → Axios → API Gateway → Lambda → Cost Explorer/CloudWatch → JSON → Render in dashboard               |

## 🏗️ System Architecture (Single Source of Truth)
![CloudGuard360 Architecture](CloudGuard360.png)

 
## 🧭 Data Flow / Request Lifecycle (End-to-End)

This is how the entire pipeline flows — from cloud data collection to frontend insights :

### ☁️ Cloud + DevOps Backbone

- 🧠 **AWS Lambda (Python)**  
  Acts as the intelligent backend processor. It:
  - Authenticates securely using IAM roles
  - Calls **AWS Cost Explorer** to fetch **real-time billing data** for the last 60 days
  - Optionally adds usage metrics (e.g., EC2 instances, S3 storage, CloudWatch alarms)
  - Returns all data as structured JSON to the frontend 


- 🌐 **API  Gateway (REST)**
Used to expose a secure /data endpoint for frontend access, with CORS enabled and Lambda proxy integration.

- 🔐 **IAM Roles & Permissions**  
  Lambda runs with least-privilege IAM roles limited to Cost Explorer and CloudWatch APIs.


  ![IAM-ROLES](IAM-roles.png)



- 📦 **Amazon S3**  
  Used to:
  - Host the static React frontend (alternative to GitHub Pages)
  - Store CSV logs or forecasting results exported from Lambda or SageMaker  



- 📉 **Observability & Monitoring (Logs, Metrics, Alerts)**  
Used for Lambda error monitoring and cost-spike alerting via alarms.

![cloudwatch](Cloud-Watch.png)



- 📢 **SNS Notifications**  
  CloudWatch is integrated with **Amazon SNS** to trigger alerts (email/SMS) when:
  - Daily billing exceeds a threshold
  - Cost increases >20% from the previous day
  Useful for **real-time budget awareness** without logging into AWS.

***🤖 Cost Intelligence & Forecasting Strategy (ML included, one story)***

- ⚙️ **Serverless Python Forecasting** — Built in **VS Code** and deployed to **AWS Lambda** using **NumPy** and **Scikit-learn** to predict billing trends without SageMaker.
- 📆 **Flexible Triggers** — Runs on-demand via **API Gateway** or scheduled with **EventBridge** for auto-updated cost forecasts.
- 📊 **Output Ready** — Forecasted data is returned as JSON, and optionally stored in **S3** or **DynamoDB** for dashboards. 

 
  ![Forecasting](ai-forecasting.png)



***🌍 Multi-Cloud Ready (GCP Support)***

- 🌐 **GCP Billing API (Integrated)**  
  A separate Lambda or backend module fetches **daily cost data from GCP**.
  - Allows side-by-side visualization of AWS and GCP spending
  - Makes CloudGuard360 **multi-cloud compatible**
  - Useful for cost optimization across providers




***💻 Frontend & Visualization Layer***

- 🧑‍💻 **React + Tailwind CSS**  
  The UI is built with a clean, responsive design:
  - Mobile-ready layout using Tailwind grid and spacing
  - Custom components like `SummaryCard`, `UsageTable`, and `AnalyticsChart`  


  ![Visualization](Dashbord.png)



- 📈 **Recharts.js (Chart Library)**  
  Used to:
  - Plot daily AWS costs in a smooth, scrollable graph
  - Compare trends and spot cost spikes visually  


  ![Charts](charts.png)



- 🔄 **Data Pipeline**  
  Final flow:  
  `React App ⟶ Axios ⟶ API Gateway ⟶ Lambda ⟶ AWS SDK (Cost Explorer/CloudWatch) ⟶ JSON ⟶ UI Rendered`



### 🛠️ DevOps & Infrastructure as Code

| 🔧 Component            | ✅ Implementation                                                                 |
|------------------------|------------------------------------------------------------------------------------|
| ☁️ Cloud Provider       | **AWS** — Primary cloud platform for compute, monitoring, and billing services    |
| 🧠 Compute Backend       | **AWS Lambda (Python)** — Serverless function fetching real-time cost + usage     |
| 🌐 API Management       | **API Gateway (REST)** — Secure endpoint between Lambda and React frontend        |
| 📦 Frontend Hosting     | **React + Tailwind** — Deployed locally or on S3/GitHub Pages                     |
| 📈 Data Visualization   | **Recharts.js** — Billing chart with cost trends and spikes                       |
| 🔐 IAM & CORS           | Scoped IAM roles + CORS headers to prevent credential leaks                       |
| ⚙️ Infrastructure as Code | **Terraform** — Provisions Lambda, API Gateway, IAM roles, and (optional) S3 bucket |

## ⚙️ Design Rationale

- Used **Lambda over EC2** to avoid always-on infrastructure and reduce costs ☁️
- Chose **serverless over containers** for event-driven workloads ⚡
- Built a **custom React dashboard** to unify multi-cloud views 🖥️

Design focused on **simplicity, low cost, and cloud-native patterns**.


## ✨ Key Features

- Multi-cloud cost data collection (AWS + GCP) ☁️
- Serverless analysis using AWS Lambda ⚡
- Automated cost and usage insights 📊
- Basic forecasting of spending trends 📈
- Infrastructure as Code using Terraform 🏗️
- Lightweight React dashboard for visibility 🖥️
- Scheduled analysis using event-driven workflows ⏱️
- End-to-end system built and tested in real cloud environments 🧪


## 💰 Cost Awareness & Trade-offs

- Serverless keeps compute costs near zero at low usage ☁️
- Avoided always-on EC2 instances to reduce idle costs
- Cost Explorer APIs have rate limits and data delays
- Trade-off: lower cost but not real-time accuracy

---

## ⚠️ Explicit Limitations

- Forecast accuracy depends on limited historical data 📉
- AWS billing data may be delayed by 24–48 hours ⏱️
- Not real-time cost tracking
- Some usage metrics are simplified for demonstration


## 🎯 What This Project Demonstrates About Me

- Ability to design **serverless, multi-cloud systems** ☁️
- Practical understanding of **cloud cost behavior** 💰
- Experience with **IaC, automation, and dashboards** ⚙️
- Focus on **working, testable systems** over theoretical designs 🧪

## 🙌 Contributions Welcome!

**CloudGuard360** is a cloud-native, open-source DevOps project — and we’d love for you to contribute!  
Whether you're a Cloud Engineer, DevOps Developer, Data Scientist, or AWS enthusiast — your ideas are welcome.

### 💡 Feature Ideas You Can Work On

| 💡 Idea                        | 📋 Description                                                                                   |
|-------------------------------|--------------------------------------------------------------------------------------------------|                            
| 📈 GCP Forecast Integration    | Add **cost prediction logic for GCP** to match AWS’s forecasting capabilities                   |
| 🧑‍💼 IAM Role Breakdown        | Show costs broken down by **IAM users or roles** to highlight who’s driving usage              |
| 🌙 Dark Mode UI               | Add toggleable **dark mode** for the React + Tailwind dashboard                                |
| 🔐 Auth Layer (Optional)      | Add optional **user authentication** to limit dashboard access                                 |
| 🧪 Real-Time EC2 Fetching     | Replace placeholder data with **live EC2 instance count** via DescribeInstances API            |
| 📬 Weekly Email Reports       | Generate and send weekly cost reports using **SES or SNS**                                     |
| 📊 Region-Wise Cost Summary   | Break down AWS billing **by region** and display visual insights                              |
| 💾 CSV/JSON Export            | Add export button to download current cost/usage data in CSV or JSON                           |

### 🛠️ How to Contribute

- 🍴 Fork this repository  
- 📦 Create a new feature branch: `git checkout -b your-feature-name`  
- ✍️ Make your changes and test locally  
- 📬 Submit a pull request with a clear description of your enhancement  

---

### 🤝 Let’s Build CloudGuard360 Together!
Made with ☁️💙 by **Manas Gantait**


## 🏁 Final Note

CloudGuard360 is not a billing replacement or enterprise FinOps platform.  
It is a practical, working system that collects real cloud data, analyzes it, and surfaces useful insights using serverless architecture.

The goal of this project was to design a **cost-aware, event-driven, multi-cloud monitoring system**—and prove it with real infrastructure, real data, and real execution.

If you can deploy it, inspect the pipelines, and explain the trade-offs, you understand the system—not just the code.

