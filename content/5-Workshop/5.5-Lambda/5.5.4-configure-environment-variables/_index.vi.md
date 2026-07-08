---
title : "Cấu hình Environment Variables và X-Ray Tracing"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.5.4. </b> "
---

Chúng ta cần cấu hình biến môi trường (**Environment Variables**) cho Lambda Function để backend nhận diện cấu hình xác thực từ Cognito, cấu hình CORS cho Frontend và biết tên secret để đọc URI từ Secrets Manager thay vì ghi cứng. Đồng thời, kích hoạt AWS X-Ray để theo dõi và chuẩn đoán cuộc gọi hệ thống.

#### Các bước thực hiện:

1. Cấu hình Environment Variables:
   * Chọn function `examora-backend-api` -> Chọn tab **Configuration** (Cấu hình) -> Mục **Environment variables** ở menu trái -> Bấm **Edit**.
   * Thêm các cặp Key/Value cấu hình cho dự án:
     * `NODE_ENV`: `production` hoặc `development` (môi trường ứng dụng).
     * `MONGO_SECRET_NAME`: `/examora/dev/mongodb` (Tên secret đã tạo ở AWS Secrets Manager chứa kết nối DB).
     * `COGNITO_USER_POOL_ID`: `<USER_POOL_ID_CỦA_BẠN>` (Lấy từ phần Cognito đã cấu hình ở bước trước).
     * `COGNITO_CLIENT_ID`: `<APP_CLIENT_ID_CỦA_BẠN>` (Lấy từ Cognito App Client).
     * `FRONTEND_URL`: URL trang web Frontend (ví dụ: `https://vietdo2k4.github.io` để cấu hình CORS bảo mật).
   * Bấm **Save** để lưu các biến môi trường.

   ![Cấu hình Environment Variables](/images/5-Workshop/5.5-Lambda/5.5.4-configure-environment-variables/LambdaEnv5.1.png)

2. Bật AWS X-Ray Tracing:
   * AWS X-Ray Tracing giúp theo dõi đường đi và đo lường thời gian xử lý của các request khi đi qua API Gateway, Lambda và kết nối tới database. Điều này giúp dễ dàng xác định các điểm nghẽn hiệu năng hoặc phát hiện lỗi.
   * Vẫn trong tab **Configuration** -> Chọn mục **Monitoring and operations tools** ở menu trái -> Bấm **Edit** ở góc phải.
   * Tại phần **CloudWatch Application Signals and AWS X-Ray** -> Tích chọn **Enable** cho mục **Lambda service traces**.
   * Nhấn **Save** để lưu cấu hình.

   ![Bật AWS X-Ray Tracing](/images/5-Workshop/5.5-Lambda/5.5.4-configure-environment-variables/LambdaXRay5.1.png)
