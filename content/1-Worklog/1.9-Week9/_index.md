---
title: "Implementing User Authentication (Cognito + SES) and Hosting Express Backend on AWS Lambda"
date: 2026-07-08
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives:

* Implement user authentication for Examora using Amazon Cognito and Amazon SES.
* Update the frontend for sign-up, OTP verification, sign-in, sign-out, and forgot password flows.
* Add Cognito identity information to user data in MongoDB.
* Update the backend to verify Cognito JWT and sync user profiles.
* Add a Lambda handler for the Express backend and protect APIs with API Gateway Authorizer.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Configure Cognito User Pool and App Client for Examora <br> - **Practice:** <br>&emsp; + Create the main user groups <br>&emsp; + Configure email-based sign-up and sign-in <br>&emsp; + Verify an email identity in Amazon SES | 15/06/2026 | 15/06/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html> <br>  <br> <https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html> |
| 3 | - Update user data to store Cognito identity information <br> - Add the required information for account synchronization and authorization <br> - Check the existing role logic to avoid breaking current business behavior | 16/06/2026 | 16/06/2026 |  <br> |
| 4 | - Update frontend authentication flows with Cognito <br> - **Practice:** <br>&emsp; + Update sign-up and email OTP verification <br>&emsp; + Update sign-in, sign-out, and forgot password flows <br>&emsp; + Store the token for authenticated API calls | 17/06/2026 | 18/06/2026 |  <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html> |
| 5 | - Update the backend to verify Cognito JWT and sync profiles to MongoDB <br> - **Practice:** <br>&emsp; + Read the token from the `Authorization` header <br>&emsp; + Sync user information after sign-in <br>&emsp; + Map Cognito Groups to system roles | 19/06/2026 | 19/06/2026 |  <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html> |
| 6 | - Add a Lambda handler for the Express backend and configure API Gateway Authorizer <br> - **Practice:** <br>&emsp; + Create an entry point for the Lambda Backend API <br>&emsp; + Configure required environment variables <br>&emsp; + Test `/health` and an authenticated API | 20/06/2026 | 20/06/2026 |   <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html> |

### Week 9 Results:

* Configured Cognito User Pool, App Client, user groups, and SES email identity for the authentication flow.

* Added Cognito identity information to user data while keeping the existing business authorization logic.

* Updated the frontend for sign-up, OTP verification, sign-in, sign-out, and forgot password flows.

* Verified Cognito JWT in the backend, synced user profiles, and mapped groups to system roles.

* Created a Lambda handler for the Express backend, configured API Gateway Authorizer, and tested an authenticated API.