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
