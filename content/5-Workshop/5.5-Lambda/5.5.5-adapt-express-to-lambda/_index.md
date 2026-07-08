---
title : "Adjusting Express Backend to Run on Lambda"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5.5.5. </b> "
---

In a traditional server architecture, an **Express** application continuously listens for incoming HTTP requests on a specific TCP port:

$$\text{Express App} \longrightarrow \text{server.listen(PORT)}$$

However, **AWS Lambda** operates on an event-driven serverless model. Instead of running an active web server on a port, Lambda functions are triggered on-demand by events dispatched from services like **Amazon API Gateway**, invoking a designated entry point called the **handler function**.

To deploy and execute an existing Express app on AWS Lambda without refactoring the entire codebase, we need to translate the incoming API Gateway event structures into standard Express request objects.

#### Architectural Solution:

We can achieve this by using intermediate wrappers such as `@vendia/serverless-express` or `serverless-http`. The wrapper translates the API Gateway HTTP proxy event into standard Node.js request/response streams:

$$\text{API Gateway Event} \longrightarrow \text{Lambda Handler} \longrightarrow \text{serverless-http} \longrightarrow \text{Express App}$$

#### Code Implementation:

1. Install the wrapper library in your backend project:
   ```bash
   npm install serverless-http
   ```

2. Decouple the Express app definition (typically `src/app.js`) from the port listener (typically `src/server.js`). The `app.js` file should export the Express application instance rather than calling `.listen()`:
   ```javascript
   const express = require('express');
   const app = express();
   
   // Configure Middlewares, Routes, and Business Logic
   app.use(express.json());
   app.get('/health', (req, res) => {
       res.status(200).json({ status: 'OK', environment: process.env.NODE_ENV });
   });

   module.exports = app;
   ```

3. Create the Lambda entrypoint handler file (e.g., `src/lambda.js`):
   ```javascript
   const serverless = require('serverless-http');
   const app = require('./app');

   // Export the handler function for AWS Lambda invocation
   module.exports.handler = serverless(app);
   ```

By using this architecture, the entire Express backend codebase—including database connections, routing configurations, and Cognito JWT authentication middlewares—remains intact while taking full advantage of the serverless runtime.
