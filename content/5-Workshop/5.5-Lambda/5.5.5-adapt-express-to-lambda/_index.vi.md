---
title : "Điều chỉnh backend Express để chạy trên Lambda"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5.5.5. </b> "
---

Trong mô hình máy chủ truyền thống, một ứng dụng **Express** sẽ lắng nghe yêu cầu trực tiếp từ một cổng mạng cố định (Port):

$$\text{Express App} \longrightarrow \text{server.listen(PORT)}$$

Tuy nhiên, **AWS Lambda** hoạt động theo mô hình hướng sự kiện (event-driven). Thay vì chạy một máy chủ liên tục để lắng nghe cổng mạng, Lambda sẽ được kích hoạt bởi một sự kiện (**event**) từ **Amazon API Gateway** và gọi một hàm xử lý đặc biệt tên là **handler function**.

Để chạy ứng dụng Express hiện tại trên AWS Lambda mà không phải viết lại toàn bộ mã nguồn, chúng ta cần chuyển đổi sự kiện của API Gateway thành định dạng request mà Express hiểu được.

#### Giải pháp kiến trúc:

Để thực hiện điều này, chúng ta sử dụng thư viện `@vendia/serverless-express` hoặc `serverless-http`. Thư viện này hoạt động như một wrapper (lớp bọc) trung gian:

$$\text{API Gateway Event} \longrightarrow \text{Lambda Handler} \longrightarrow \text{serverless-http} \longrightarrow \text{Express App}$$

#### Cách thiết lập trong mã nguồn:

1. Cài đặt thư viện bọc trong project backend:
   ```bash
   npm install serverless-http
   ```

2. Tách file cấu hình ứng dụng Express (`app.js` hoặc `src/app.js`) ra khỏi file khởi chạy cổng mạng (`server.js` hoặc `src/server.js`). File `app.js` sẽ xuất đối tượng Express:
   ```javascript
   const express = require('express');
   const app = express();
   
   // Cấu hình Middleware, Routes, Business Logic...
   app.use(express.json());
   app.get('/health', (req, res) => {
       res.status(200).json({ status: 'OK', environment: process.env.NODE_ENV });
   });

   module.exports = app;
   ```

3. Tạo file handler cho Lambda (ví dụ: `src/lambda.js`):
   ```javascript
   const serverless = require('serverless-http');
   const app = require('./app');

   // Khởi tạo handler để AWS Lambda có thể gọi trực tiếp
   module.exports.handler = serverless(app);
   ```

Với kiến trúc này, toàn bộ mã nguồn Express backend (kết nối cơ sở dữ liệu, định tuyến router, middleware bảo mật xác thực JWT bằng Cognito) vẫn được giữ nguyên và chạy ổn định trên môi trường Serverless.
