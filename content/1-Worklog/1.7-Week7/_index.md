---
title: "Studying Asynchronous Serverless Architectures, SQS Queue Triggers, and Finalizing Project Scope"
date: 2026-07-08
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:

* Understand asynchronous processing in serverless architecture.
* Practice the S3 ObjectCreated flow that invokes Lambda.
* Use SQS to separate background processing from the main request flow.
* Monitor Lambda with CloudWatch Logs and X-Ray.
* Finalize the project direction, scope, and high-level architecture for the final project.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Learn event-driven architecture with SNS and SQS <br> - Distinguish between message queue and publish/subscribe patterns <br> - Review how a queue separates the request sender from background processing | 01/06/2026 | 01/06/2026 | <https://000077.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html> |
| 3 | - Practice an S3 ObjectCreated trigger with Lambda <br> - **Practice:** <br>&emsp; + Create an S3 bucket for the lab <br>&emsp; + Configure an event notification when an object is uploaded <br>&emsp; + Check that Lambda is invoked after the file upload | 02/06/2026 | 02/06/2026 |  <br> <https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html> |
| 4 | - Practice processing messages with SQS and Lambda <br> - **Practice:** <br>&emsp; + Create a test SQS queue <br>&emsp; + Send a sample message to the queue <br>&emsp; + Configure Lambda to read and process messages from the queue | 03/06/2026 | 03/06/2026 | <https://000083.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html> |
| 5 | - Monitor Lambda with CloudWatch Logs and X-Ray <br> - **Practice:** <br>&emsp; + View Lambda logs in CloudWatch Logs <br>&emsp; + Enable X-Ray tracing for the Lambda function <br>&emsp; + Check errors and request processing time | 04/06/2026 | 04/06/2026 | <https://000140.awsstudygroup.com/>  <br> <https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-view.html> |
| 6 | - Plan and finalize the final project topic: Examora <br> - Finalize the Serverless architecture direction for the project <br> - Define the main feature groups: authentication, API/backend, file upload, Word import, asynchronous grading, and monitoring | 05/06/2026 | 05/06/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html> <br> <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html> |

### Week 7 Results:

* Understood the role of SQS and SNS in event-driven architecture.

* Configured an S3 ObjectCreated event to invoke Lambda after a file upload.

* Created an SQS queue, sent a sample message, and configured Lambda to process messages from the queue.

* Viewed Lambda logs in CloudWatch and enabled X-Ray tracing to monitor requests.

* Finalized Examora as the final project topic using the AWS Serverless direction.

* Defined the main Examora feature groups: authentication, API/backend, file upload, Word import, asynchronous grading, and monitoring.