---
title: "Thiết kế kiến trúc tổng quan và lập kế hoạch triển khai dự án cuối kỳ Examora"
date: 2026-07-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

* Bắt đầu dự án cuối kỳ Examora theo hướng kiến trúc Serverless trên AWS.
* Vẽ sơ đồ kiến trúc tổng quan cho dự án.
* Xác định các chức năng chính cần có trong phiên bản MVP.
* Tham khảo thêm tài liệu và lab về luồng frontend gọi API Gateway.
* Chốt phạm vi và các dịch vụ AWS sử dụng trong dự án.
* Làm quen với hướng triển khai CI/CD cho ứng dụng serverless bằng AWS SAM.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Vẽ sơ bộ sơ đồ kiến trúc Serverless cho Examora <br> - Xác định các lớp chính: frontend, authentication, API/backend, database, storage, async processing và monitoring <br> - Thể hiện luồng request chính từ người dùng đến các dịch vụ AWS | 08/06/2026 | 08/06/2026 | <https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/web-application.html> <br>  |
| 3 | - Xác định các chức năng chính của Examora từ source code và yêu cầu nghiệp vụ có sẵn <br> - Gom nhóm chức năng theo module: tài khoản, lớp học, bài giảng/đề thi, upload file, làm bài và lịch sử thi <br> - Ghi lại các phần cần triển khai mới khi đưa hệ thống lên AWS | 09/06/2026 | 09/06/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/framework/requirements.html> |
| 4 | - Thực hành lab frontend gọi API Gateway để hiểu luồng tích hợp client và backend <br> - **Thực hành:** <br>&emsp; + Xem cách cấu hình API Gateway cho backend endpoint <br>&emsp; + Test API bằng Postman <br>&emsp; + Kiểm tra cách frontend gọi API endpoint | 10/06/2026 | 10/06/2026 | <https://000135.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html> |
| 5 | - Chốt phạm vi và các dịch vụ sử dụng trong dự án Examora <br> - Xác định các dịch vụ chính: Amplify Hosting, Cognito, SES, API Gateway, Lambda, MongoDB Atlas, S3, SQS, CloudWatch, X-Ray, Secrets Manager và IAM <br> | 11/06/2026 | 11/06/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html> |
| 6 | - Làm quen với CI/CD cho ứng dụng serverless bằng AWS SAM <br> - **Thực hành:** <br>&emsp; + Xem luồng `sam build`, `sam deploy` và deploy tự động bằng pipeline <br>&emsp; + Đọc cách `sam pipeline bootstrap` và `sam pipeline init` chuẩn bị cấu hình pipeline <br>&emsp; + Phác thảo pipeline đơn giản cho backend serverless | 12/06/2026 | 12/06/2026 | <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/deploying-cicd-overview.html> <br> <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd.html> <br> |

### Kết quả đạt được tuần 8:

* Vẽ được sơ đồ kiến trúc Serverless tổng quan cho Examora.

* Xác định được các module chính của dự án: tài khoản, lớp học, bài giảng/đề thi, upload file, làm bài và lịch sử thi.

* Hoàn thành lab tham khảo về luồng frontend gọi API Gateway và test API bằng Postman.

* Chốt được phạm vi MVP và các dịch vụ AWS sẽ sử dụng cho Examora.

* Nắm được hướng triển khai CI/CD cho ứng dụng serverless bằng AWS SAM và phác thảo được pipeline backend cơ bản.