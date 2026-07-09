---
title: "Xây dựng REST API với API Gateway, viết Lambda Function và tạo S3 Presigned URL"
date: 2026-07-08
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

* Nắm vai trò của API Gateway trong việc tạo endpoint cho backend.
* Viết và kiểm thử Lambda function xử lý request đơn giản.
* Kết nối API Gateway với Lambda bằng Lambda proxy integration.
* Cấu hình CORS cho API khi frontend gọi backend.
* Thực hành upload file lên S3 bằng presigned URL.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu tiếp về API Gateway HTTP API, route, method và stage <br> - Xem cách API Gateway nhận request từ client và chuyển đến backend <br> - Ghi lại sự khác nhau giữa public endpoint và endpoint cần cấu hình bảo vệ | 25/05/2026 | 25/05/2026 | <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html> <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html> |
| 3 | - Thực hành tạo Lambda function, xử lý request đơn giản <br> - **Thực hành:** <br>&emsp; + Tạo Lambda function trả về JSON response <br>&emsp; + Kiểm tra input event và output response <br>&emsp; + Cấu hình thử environment variable cho Lambda | 26/05/2026 | 26/05/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html> |
| 4 | - Kết nối API Gateway với Lambda bằng Lambda proxy integration <br> - **Thực hành:** <br>&emsp; + Tạo route gọi vào Lambda function <br>&emsp; + Kiểm tra API bằng browser hoặc Postman <br>&emsp; + Xem request/response format khi đi qua API Gateway | 27/05/2026 | 27/05/2026 | <https://000079.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html> |
| 5 | - Tìm hiểu về CORS khi frontend gọi API khác domain <br> - **Thực hành:** <br>&emsp; + Cấu hình CORS cho HTTP API <br>&emsp; + Kiểm tra allowed origin, method và header <br>&emsp; + Ghi lại lỗi thường gặp khi thiếu CORS | 28/05/2026 | 28/05/2026 | <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html> |
| 6 | - Thực hành upload file lên S3 bằng presigned URL <br> - **Thực hành:** <br>&emsp; + Tạo private bucket dùng cho upload thử nghiệm <br>&emsp; + Tạo presigned URL cho thao tác upload object <br>&emsp; + Upload file bằng presigned URL và kiểm tra object trong bucket | 29/05/2026 | 29/05/2026 | <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html> |

### Kết quả đạt được tuần 6:

* Nắm được cách API Gateway tổ chức HTTP API thông qua route, method và stage.

* Tạo được Lambda function đơn giản, kiểm tra input event, output response và environment variable.

* Kết nối được API Gateway với Lambda bằng Lambda proxy integration và kiểm thử API bằng browser/Postman.

* Cấu hình được CORS cho HTTP API và nhận biết lỗi khi frontend bị chặn bởi cross-origin request.

* Tạo được presigned URL để upload file lên S3 mà không cần cấp AWS credentials trực tiếp cho phía upload.