---
title: "Decoupling Submission Flow with Amazon SQS and Async Lambda Grading Worker"
date: 2026-07-08
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Week 11 Objectives:

* Separate grading logic from the exam submission request using Amazon SQS.
* Build a Lambda Grading Worker for asynchronous grading.
* Optimize the architecture diagram based on the submission and grading flow.
* Study Amplify Hosting and Route 53 to prepare for frontend deployment.
* Test the main features after integrating serverless flows.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Analyze the current grading logic in the backend <br> - Identify the part that should be separated from the submission request <br> - Design the SQS payload using only the required IDs | 29/06/2026 | 29/06/2026 | <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html> |
| 3 | - Complete the grading flow with SQS and Lambda Worker <br> - Optimize the architecture diagram with the SQS grading flow <br> - Send a grading job from the backend to SQS, then let Lambda Worker receive the message and process grading | 30/06/2026 | 30/06/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html> |
| 4 | - Study Amplify Hosting to prepare frontend deployment <br> - Review how to connect a custom domain to Amplify using Route 53 <br> - Note the required settings: build output, environment variables, rewrite rule, and domain | 01/07/2026 | 01/07/2026 | <https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html> <br> <https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html> <br> <https://docs.aws.amazon.com/amplify/latest/userguide/to-add-a-custom-domain-managed-by-amazon-route-53.html> |
| 5 | - Add error handling for the asynchronous grading flow <br> - Configure a visibility timeout suitable for grading time <br> - Record successful/failed processing states and add logs to inspect worker errors | 02/07/2026 | 02/07/2026 | <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html> |
| 6 | - Test the main features after integration <br> - Test login and authenticated API calls <br> - Test Word upload/import, exam submission, and result after worker grading | 03/07/2026 | 03/07/2026 | <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html> |

### Week 11 Results:

* Identified the grading logic that should be separated from the exam submission request.

* Sent grading jobs from the backend to SQS and processed messages with Lambda Worker.

* Optimized the architecture diagram with the submission flow, SQS Grading Queue, and Lambda Grading Worker.

* Understood how Amplify Hosting works with Route 53 to prepare frontend deployment.

* Added error handling, processing states, and logs for the asynchronous grading flow.

* Tested the main features: authentication, Word upload/import, exam submission, and result retrieval.