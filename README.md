# 🌩️ CloudGuard360

**CloudGuard360**  is a real-time, cloud usage and billing monitoring dashboard built using AWS Lambda, API Gateway, and a modern React frontend. It helps you visualize AWS service usage, track daily billing trends, forecast upcoming cloud costs using lightweight ML in Lambda, and prepare for cost optimization — all in one sleek dashboard.


> 🔒 Think of it as your personal AWS billing and usage control tower..

## ⚠️ Real-Life Cloud Problems (Problem Table): 

| 💥 Problem (Real-world) | ⚙️ Solution (What I built) | 🎯 Impact |
|------------------------|---------------------------|----------|
| Cloud costs are **visible too late** (billing delay, no real-time insight) | Built Lambda integration with AWS Cost Explorer to fetch and expose **near real-time cost data via API** | Enables early detection of overspending instead of end-of-month surprises |
| Cost + usage data is **fragmented across AWS services** | Unified billing + usage into a **single API layer + React dashboard** | Single-pane visibility → faster debugging and decision making |
| AWS Cost Explorer API is **complex (auth, pagination, formatting)** | Abstracted complexity inside Lambda and exposed a **clean `/data` endpoint** | Simplifies frontend consumption and reduces engineering overhead |
| No built-in way to **predict future costs** | Designed a pipeline to export usage data and integrate with **ML-based forecasting (SageMaker)** | Enables proactive cost planning instead of reactive control |
| Frontend cannot securely access AWS APIs (**CORS + credentials issue**) | Used API Gateway + Lambda with proper **CORS and IAM-based access** | Secure, production-safe frontend-backend communication |
| Raw AWS billing data is **hard to interpret (JSON/tables)** | Built visual layer using **Recharts (trend graphs, summaries)** | Improves readability and decision speed |
| Many dashboards rely on **mock or static data** | Integrated **real AWS billing data pipeline** | Builds trust and makes system production-relevant |
| No easy way to **share or customize AWS dashboards** | Built a **portable React dashboard** deployable anywhere | Enables external sharing and customization |

## 📁 Project Structure :
This repository is structured to separate serverless backend processing, infrastructure provisioning, and frontend visualization for a clear and scalable system design.
```
CloudGuard360/
│
├── aws/  # Backend + cloud logic (AWS services, Lambda, forecasting)
|
│   ├── Forecasting/  # ML-based cost prediction logic (historical data → forecast)
│   │   
│   ├── Terraform/  # Infrastructure as Code for AWS resources
│   │   
│   │   ├── main.tf        # Core infrastructure definitions  
│   │   ├── variables.tf   # Input variables  
│   │   ├── outputs.tf     # Output values  
│   │   └── provider.tf    # AWS provider configuration  
│   └── lambda/  # Serverless backend (data processing APIs)
│
│       ├── cloud_cost_monitor.py      # Fetches AWS billing data  
│       ├── cloud_cost_monitor.zip     # Deployment package  
│       ├── CloudGuard360-BillingAnalyzer.py   # Billing insights logic  
│       ├── CloudGuard360-EC2Analyzer.py       # EC2 usage analysis  
│       ├── CloudGuard360BillingHistory.py     # Historical billing data  
│       ├── cloudguard360-ai-data.py           # Data prep for forecasting  
│       └── index.js                           # API handler / integration layer  
│
├── cloudguard360-dashboard/  # Frontend React dashboard (UI + visualization)
│
│   ├── public/  
│   │   # Static assets  
│   │   ├── index.html        # Entry HTML  
│   │   ├── favicon.ico       # Icon  
│   │   ├── manifest.json     # PWA config  
│   │   └── robots.txt        # SEO config  
│   ├── src/  # Application source code  
│   │
│   │   ├── components/  # Reusable UI components  
│   │   │   ├── Header.js          # Top navigation  
│   │   │   ├── SummaryCard.js     # Cost summary cards  
│   │   │   ├── UsageTable.js      # Service usage table  
│   │   │   └── AnalyticsChart.js  # Cost trend charts  
│   │   ├── App.js        # Main app logic  
│   │   ├── index.js      # React entry point  
│   │   ├── App.css       # App styles  
│   │   └── index.css     # Global styles  
│   ├── package.json        # Dependencies and scripts  
│   ├── package-lock.json   # Dependency lock file  
│   ├── tailwind.config.js  # Tailwind CSS config  
│   └── postcss.config.js   # PostCSS config  
│
├── docs/  # Architecture diagrams, screenshots, and proof
│
│   ├── CloudGuard360.png     # Architecture diagram  
│   ├── Dashboard.png         # UI dashboard preview  
│   ├── charts.png            # Visualization charts  
│   ├── ai-forecasting.png    # ML forecasting output  
│   ├── Api-Gateway.png       # API Gateway flow  
│   ├── Lambda-function.png   # Lambda execution view  
│   ├── Cloud-Watch.png       # Monitoring logs  
│   ├── IAM-roles.png         # IAM permissions setup  
│   ├── S3-bucket.png         # Storage layer  
│   └── SNS-alert.png         # Alerting system  
│
├── README.md   # Project documentation (architecture, setup, flow)
├── License    # MIT license file
├── CloudGuard360.png  # Root-level architecture image (quick preview)
├── Dashboard.png  # Dashboard preview image  
├── ai-forecasting.png    # Forecasting output sample
└── charts.png  # Cost visualization sample  
```
## 🏗️ System Architecture (Single Source of Truth) :
![CloudGuard360 Architecture](CloudGuard360.png)

## 📈 Core Features :

| ✅ What This Project IS | ❌ What This Project is NOT |
|------------------------|---------------------------|
| Real-Time Cloud Cost Visibility — Fetches AWS billing data via Cost Explorer and exposes it through a serverless API | Not a delayed billing report system or end-of-month analysis tool |
| Unified Cost + Usage Dashboard — Combines billing insights and service-level usage into a single view | Not fragmented AWS console navigation across multiple services |
| Serverless Data Processing — Uses Lambda + API Gateway to securely process and deliver cost data | Not a backend requiring persistent servers or manual scaling |
| Cost Forecasting Capability — Uses historical data with ML (LSTM/SageMaker or Python models) to predict future costs | Not a static dashboard without predictive insights |
| Secure API Abstraction — Hides AWS complexity (auth, pagination, APIs) behind a clean backend layer | Not direct frontend calls to AWS APIs with exposed credentials |
| Multi-Cloud Ready Design — Integrates GCP billing API for cross-cloud cost visibility | Not limited to a single-cloud, AWS-only view |
| Visual Analytics Dashboard — React + Recharts for clear cost trends and spike detection | Not raw JSON or table-based unreadable billing data |
| Production-Oriented Architecture — Built with real AWS APIs, deployable infra, and real data pipelines | Not a mock/demo dashboard with fake or static data |

## 🧰 Tech Stack :

**☁️ Cloud**
AWS (Lambda, API Gateway, S3) — core serverless infrastructure  
GCP Billing API — extended for multi-cloud cost visibility  

**⚙️ Backend**
AWS Lambda (Python) — fetches and processes billing data  
API Gateway — secure, CORS-enabled API layer  

**📊 Data & Monitoring**
AWS Cost Explorer — billing data source  
CloudWatch — metrics, logs, and alarms  
SNS — alerting on abnormal cost spikes  

**🧠 Forecasting**
SageMaker (LSTM, Python) — cost prediction based on historical usage  

**🛠️ Infrastructure**
Terraform — infrastructure provisioning and IAM configuration  

**🔐 Security**
IAM roles (least privilege), no frontend secrets, controlled API access  

**💻 Frontend**
React + Tailwind CSS — responsive dashboard  
Recharts — cost visualization (trends, spikes)  

**🔄 Data Flow**
React → API Gateway → Lambda → AWS APIs → JSON → Dashboard
 
## 🧭 Request Lifecycle (End-to-End) :

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



### 🛠️ DevOps & Infrastructure as Code :

| 🔧 Component            | ✅ Implementation                                                                 |
|------------------------|------------------------------------------------------------------------------------|
| ☁️ Cloud Provider       | **AWS** — Primary cloud platform for compute, monitoring, and billing services    |
| 🧠 Compute Backend       | **AWS Lambda (Python)** — Serverless function fetching real-time cost + usage     |
| 🌐 API Management       | **API Gateway (REST)** — Secure endpoint between Lambda and React frontend        |
| 📦 Frontend Hosting     | **React + Tailwind** — Deployed locally or on S3/GitHub Pages                     |
| 📈 Data Visualization   | **Recharts.js** — Billing chart with cost trends and spikes                       |
| 🔐 IAM & CORS           | Scoped IAM roles + CORS headers to prevent credential leaks                       |
| ⚙️ Infrastructure as Code | **Terraform** — Provisions Lambda, API Gateway, IAM roles, and (optional) S3 bucket |

## 🛡️ Resilience & Security :

***Failure Handling***
- Event retries handled via EventBridge  
- Idempotent execution prevents duplicate remediation  
- Failures logged in CloudWatch for debugging and traceability  
- Graceful handling of partial failures (no cascading impact)

***Security***
- IAM roles follow least-privilege principle  
- No hardcoded credentials or secrets  
- Input validation before executing remediation actions  
- Strict separation of permissions (read vs write actions)

***Scalability***
- Lambda auto-scales with incoming event volume  
- DynamoDB supports high-throughput, low-latency logging  
- Event-driven design avoids bottlenecks and polling overhead  

## 🧠 Engineering Philosophy :

***Key Decisions***
- Event-driven > Scheduled scans → real-time enforcement  
- Serverless > Containers → reduced operational overhead  
- Deterministic rules > ML → predictable and auditable behavior  
- Decoupled components → better fault isolation and maintainability  
- Policy abstraction → rules separated from execution logic  

***Trade-offs***
- No predictive intelligence (intentionally avoided ML complexity)  
- Limited to predefined rule coverage  
- Strong dependency on correct IAM configuration  
- Event-driven model depends on event completeness  

***Limitations***
- Cannot detect unknown or zero-day misconfigurations  
- Limited visibility outside supported AWS services/events  
- No centralized UI/dashboard (backend-focused design)  
- Requires manual rule expansion for broader coverage  

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

### 🤝 Let’s Build CloudGuard360 Together!
Made with ☁️💙 by **Manas Gantait**
