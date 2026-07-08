---
title : "Create Lambda Function"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.5.3. </b> "
---

In this step, we will create the core Lambda function that will host and execute the Express backend of the Examora system.

#### Step-by-Step Instructions:

1. Create Lambda Function:
   * In the AWS Console search bar, search for **Lambda** -> select **Functions** in the left navigation pane -> click **Create function**.
   * Choose **Author from scratch**.
   * Configure the basic function details:
     * **Function name**: Enter `examora-backend-api`.
     * **Runtime**: Select **Node.js 20.x** (or the latest supported LTS version).
     * **Architecture**: Select **x86_64**.
     * **Permissions**: Expand **Change default execution role** -> choose **Use an existing role** -> search for and select the IAM execution role created in the previous step (e.g., `examora-lambda-backend-role`).
   * Click **Create function** and wait for the initialization to complete.

   ![Configure Function Parameters](/images/5-Workshop/5.5-Lambda/5.5.3-create-lambda-function/LamdaFuctions5.1.png)

   ![Select Execution Role](/images/5-Workshop/5.5-Lambda/5.5.3-create-lambda-function/LamdaFuctions5.2.png)

2. Adjust General Configuration Settings:
   * Since the Express backend connects to a MongoDB Atlas database and processes various API tasks, we must increase the default memory allocation and timeout duration to ensure stability:
   * Select the newly created function -> navigate to the **Configuration** tab -> choose **General configuration** -> click **Edit**.
   * Set the following parameters:
     * **Memory**: Increase to **512 MB** or **1024 MB** (to allocate more compute power and reduce cold start latency).
     * **Timeout**: Increase to **30 seconds** (the default is 3 seconds; increasing this prevents database connection timeouts or execution failures on long-running queries).
   * Click **Save** to apply the configuration.

   ![Adjust General Configuration](/images/5-Workshop/5.5-Lambda/5.5.3-create-lambda-function/LamdaFuctions5.3.png)
