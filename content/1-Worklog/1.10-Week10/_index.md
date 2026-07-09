---
title: "Building S3 Direct Upload Flow and Automating Question Import from Word Documents"
date: 2026-07-08
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Week 10 Objectives:

* Implement file upload for Examora using an S3 Upload Bucket and presigned URLs.
* Update the backend to generate presigned URLs based on upload type and user permission.
* Update the frontend to upload avatars, class images, exam images, question images, and Word files.
* Build the Word question import flow using S3 ObjectCreated events and Lambda.
* Add error handling, logs, and secret configuration for the Word import pipeline.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Design the S3 Upload Bucket for business files <br> - Define prefixes for avatars, class images, exam images, question images, and Word files <br> - Configure the bucket as private and review CORS for frontend upload | 22/06/2026 | 22/06/2026 | <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html> |
| 3 | - Update the backend to generate presigned URLs by upload type <br> - Check JWT and role before generating the URL <br> - Let the backend decide the object key by prefix and return a presigned PUT URL to the frontend | 23/06/2026 | 23/06/2026 | <https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html> |
| 4 | - Update the frontend file upload flow using presigned URLs <br> - Call the API to get a presigned URL and PUT the file directly to S3 <br> - Save the object key when updating the related business data | 24/06/2026 | 24/06/2026 | |
| 5 | - Build the Word question import pipeline <br> - Upload a Word file to the `imports/word/raw/` prefix <br> - Configure an S3 ObjectCreated event to invoke the Lambda Import Word Processor and check the event payload | 25/06/2026 | 25/06/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html> |
| 6 | - Complete Word import processing and error logging <br> - Let Lambda read the Word file from S3 and retrieve the required secret config with Secrets Manager <br> - Log successful or failed import results for easier troubleshooting | 26/06/2026 | 26/06/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html> <br>  |

### Week 10 Results:

* Designed a private S3 Upload Bucket and prefix structure for Examora file types.

* Generated presigned URLs in the backend based on upload type, user role, and system-defined object keys.

* Uploaded files directly from the frontend to S3 using presigned URLs and saved object keys for business data.

* Configured an S3 ObjectCreated event to invoke the Lambda Import Word Processor when a new Word file is uploaded.

* The Lambda Import Word Processor read files from S3, used the required secret configuration, and logged processing results.