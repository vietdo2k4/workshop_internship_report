---
title: "Designing REST APIs with API Gateway, Writing Lambda Functions, and S3 Presigned URLs"
date: 2026-07-08
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Understand the role of API Gateway in creating backend endpoints.
* Write and test a simple Lambda function for request handling.
* Connect API Gateway with Lambda using Lambda proxy integration.
* Configure CORS for frontend-to-backend API calls.
* Practice uploading files to S3 using a presigned URL.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Review API Gateway HTTP API, route, method, and stage <br> - Check how API Gateway receives client requests and forwards them to a backend <br> - Note the difference between a public endpoint and an endpoint that needs protection | 25/05/2026 | 25/05/2026 | <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html> <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html> |
| 3 | - Create a simple Lambda function to handle requests <br> - **Practice:** <br>&emsp; + Create a Lambda function that returns a JSON response <br>&emsp; + Test the input event and output response <br>&emsp; + Configure a sample environment variable for Lambda | 26/05/2026 | 26/05/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html> |
| 4 | - Connect API Gateway with Lambda using Lambda proxy integration <br> - **Practice:** <br>&emsp; + Create a route that invokes the Lambda function <br>&emsp; + Test the API using a browser or Postman <br>&emsp; + Review the request/response format through API Gateway | 27/05/2026 | 27/05/2026 | <https://000079.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html> |
| 5 | - Review CORS when a frontend calls an API from another domain <br> - **Practice:** <br>&emsp; + Configure CORS for an HTTP API <br>&emsp; + Check allowed origin, method, and header settings <br>&emsp; + Record common errors when CORS is missing | 28/05/2026 | 28/05/2026 | <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html> |
| 6 | - Practice uploading a file to S3 using a presigned URL <br> - **Practice:** <br>&emsp; + Create a private bucket for upload testing <br>&emsp; + Generate a presigned URL for object upload <br>&emsp; + Upload a file using the presigned URL and check the object in the bucket | 29/05/2026 | 29/05/2026 | <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html> |

### Week 6 Results:

* Understood how API Gateway organizes HTTP APIs through routes, methods, and stages.

* Created a simple Lambda function and tested its input event, output response, and environment variable.

* Connected API Gateway with Lambda using Lambda proxy integration and tested the API with a browser/Postman.

* Configured CORS for an HTTP API and identified common frontend cross-origin request issues.

* Generated a presigned URL to upload files to S3 without directly granting AWS credentials to the uploader.