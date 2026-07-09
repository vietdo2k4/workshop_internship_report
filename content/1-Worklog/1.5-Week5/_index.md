---
title: "Exploring User Authentication with Amazon Cognito and Email Sending with Amazon SES"
date: 2026-07-08
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:

* Understand the role of Amazon Cognito in user sign-up, sign-in, and user management.
* Configure a User Pool, App Client, and basic authentication flow.
* Use Cognito Groups to classify users by permission groups.
* Review Amazon SES for email verification and password recovery flows.
* Understand how JWT tokens are used to protect APIs.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Review Amazon Cognito User Pools <br> - Understand the sign-up, account confirmation, sign-in, and token flow <br> - Identify the role of App Client in a web application | 18/05/2026 | 18/05/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html> <br>  |
| 3 | - Complete the SPA authentication lab with Amazon Cognito <br> - **Practice:** <br>&emsp; + Create/configure a Cognito User Pool <br>&emsp; + Configure an App Client for the web application <br>&emsp; + Test user sign-up and sign-in | 19/05/2026 | 19/05/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html> |
| 4 | - Review Cognito Groups and group information in tokens <br> - **Practice:** <br>&emsp; + Create sample user groups <br>&emsp; + Add users to the appropriate groups <br>&emsp; + Check group information in the token after sign-in | 20/05/2026 | 20/05/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html> <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html> |
| 5 | - Review Amazon SES for verification and password reset emails <br> - **Practice:** <br>&emsp; + Create an email identity in SES <br>&emsp; + Verify the email identity <br>&emsp; + Review sending limits while the account is still in the SES sandbox | 21/05/2026 | 21/05/2026 | <https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html> <br> <https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html> <br> <https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html> |
| 6 | - Review how to protect APIs using a Cognito/JWT Authorizer <br> - **Practice:** <br>&emsp; + Check how API Gateway uses a Cognito User Pool as an authorizer <br>&emsp; + Review how to send a token in the `Authorization` header <br>&emsp; + Distinguish between public APIs and authenticated APIs | 22/05/2026 | 22/05/2026 |  <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html> <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-accessing-resources-api-gateway-and-lambda.html> |

### Week 5 Results:

* Understood the role of Cognito User Pool, App Client, and the sign-up/sign-in flow in a web application.

* Configured SPA authentication with Amazon Cognito and tested user sign-up and sign-in.

* Created Cognito Groups, assigned users to groups, and checked group information in tokens.

* Verified an email identity in Amazon SES and understood sending limits while the account is still in the sandbox.

* Learned how a Cognito/JWT Authorizer protects APIs and how the client sends a token through the `Authorization` header.