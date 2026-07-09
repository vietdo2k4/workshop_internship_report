---
title: "Architecture Design and MVP Scope Definition for Examora Serverless Project"
date: 2026-07-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:

* Start the final Examora project using a Serverless architecture on AWS.
* Draw the high-level architecture diagram for the project.
* Identify the main features required for the MVP version.
* Review additional documentation and labs about frontend-to-API Gateway integration.
* Finalize the project scope and AWS services used in Examora.
* Learn the CI/CD direction for serverless applications using AWS SAM.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Sketch the initial Serverless architecture diagram for Examora <br> - Identify the main layers: frontend, authentication, API/backend, database, storage, async processing, and monitoring <br> - Show the main request flow from users to AWS services | 08/06/2026 | 08/06/2026 | <https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/web-application.html> <br> |
| 3 | - Identify the main Examora features from the available source code and business requirements <br> - Group features by modules: account, classes, lessons/exams, file upload, taking exams, and exam history <br> - Note the parts that need to be built when deploying the system on AWS | 09/06/2026 | 09/06/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/framework/requirements.html> |
| 4 | - Practice a frontend-to-API Gateway integration lab to understand client/backend communication <br> - **Practice:** <br>&emsp; + Review how API Gateway is configured for backend endpoints <br>&emsp; + Test APIs using Postman <br>&emsp; + Check how the frontend calls API endpoints | 10/06/2026 | 10/06/2026 | <https://000135.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html> |
| 5 | - Finalize the scope and AWS services used in Examora <br> - Define the main services: Amplify Hosting, Cognito, SES, API Gateway, Lambda, MongoDB Atlas, S3, SQS, CloudWatch, X-Ray, Secrets Manager, and IAM <br> | 11/06/2026 | 11/06/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html> |
| 6 | - Learn CI/CD for serverless applications using AWS SAM <br> - **Practice:** <br>&emsp; + Review the `sam build`, `sam deploy`, and automated deployment flow <br>&emsp; + Read how `sam pipeline bootstrap` and `sam pipeline init` prepare pipeline configuration <br>&emsp; + Sketch a simple backend serverless pipeline | 12/06/2026 | 12/06/2026 | <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-cicd-overview.html> <br> <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd.html> <br> |

### Week 8 Results:

* Created a high-level Serverless architecture diagram for Examora.

* Identified the main project modules: account, classes, lessons/exams, file upload, taking exams, and exam history.

* Completed a reference lab about frontend-to-API Gateway integration and API testing with Postman.

* Finalized the MVP scope and AWS services used in Examora.

* Understood the CI/CD direction for serverless applications with AWS SAM and sketched a basic backend pipeline.