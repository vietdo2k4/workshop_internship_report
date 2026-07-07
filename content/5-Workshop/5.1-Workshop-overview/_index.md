---
title : "Introduction"
date : 2024-01-01 
weight : 1 
chapter : false
pre : " <b> 5.1. </b> "
---

### Resource Preparation

#### 1. Resource Scope

**Examora - Online Exam Platform** is deployed using a **Console-first, SAM-lite optional** approach. We will configure the primary resources on the **AWS Management Console** first to capture step-by-step screenshots for the workshop, helping users understand each installation and configuration step. Afterwards, we will use **AWS SAM-lite** to define a portion of the serverless resources using Infrastructure as Code (IaC).

Key services used in this workshop:

| Category | Service |
|---|---|
| **Authentication** | Amazon Cognito, Amazon SES |
| **Backend API** | AWS Lambda, Amazon API Gateway |
| **External Database** | MongoDB Atlas |
| **Secret/Config** | AWS Secrets Manager |
| **Async Grading** | Amazon SQS, AWS Lambda |
| **File Upload/Import** | Amazon S3, AWS Lambda |
| **Frontend Hosting** | Amazon S3, Amazon CloudFront |
| **Protection** | AWS WAF |
| **Monitoring** | Amazon CloudWatch Logs, AWS X-Ray |
| **Permission** | AWS IAM |

**Examora — Online Exam Platform on AWS** is deployed following a **Console-first, SAM-lite optional** approach. This means we will configure core resources on the **AWS Management Console** first for easy control and capturing visual step-by-step guides. Once the system is running stably, we will use **AWS SAM-lite** to define some serverless resources via Infrastructure as Code (IaC).