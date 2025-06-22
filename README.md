<<<<<<< HEAD
# Customer 360 Behavior Analytics Platform 🚀

A production-grade, enterprise-scale AWS Data Engineering project that integrates **real-time and batch processing** to build a **Customer 360 view** and compute **behavioral analytics** like retention, funnel progression, and churn risk.

## 🔧 Tech Stack
- AWS Glue (10+ PySpark Jobs)
- AWS Lambda, Kinesis
- Amazon S3, Athena, Redshift
- AWS Step Functions, SNS, CloudWatch

## 📊 Outputs
- `customer_360_curated`
- `product_usage_funnel`
- `retention_metrics`
- `churn_risk_scores`
- Dashboards in QuickSight / Redshift

## 📂 Structure
```
customer360-behavior-platform/
├── glue_jobs/           # PySpark Glue jobs
├── lambda/              # Streaming triggers
├── kinesis/             # Stream config
├── stepfunctions/       # State machine JSON
├── cloudformation/      # Infra templates
├── scripts/             # Athena & Redshift SQL
├── data/                # Sample input files
└── dashboards/          # Dashboard placeholder
```
=======
# customer360-behavior-platform
A real-time + batch Customer 360 behavioral analytics platform using AWS Glue, Athena, Redshift, and Step Functions
>>>>>>> e5a7ec68f01f0ddc1cfc5cb54094beec9365dee3
