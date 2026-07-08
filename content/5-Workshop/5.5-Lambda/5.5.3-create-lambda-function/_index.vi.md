---
title : "Tạo Lambda Function"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.5.3. </b> "
---

Trong bước này, chúng ta sẽ tạo Lambda function chính đóng vai trò xử lý toàn bộ backend Express của hệ thống Examora.

#### Các bước thực hiện:

1. Tạo Lambda Function:
   * Trên thanh tìm kiếm của AWS Console, nhập **Lambda** -> Chọn **Functions** ở menu trái -> Bấm **Create function**.
   * Chọn **Author from scratch** (Tạo mới từ đầu).
   * Cấu hình các thông tin cơ bản:
     * **Function name**: Nhập `examora-backend-api`.
     * **Runtime**: Chọn **Node.js 20.x** (hoặc phiên bản LTS mới nhất hỗ trợ).
     * **Architecture**: Chọn **x86_64**.
     * **Permissions**: Mở rộng phần **Change default execution role** -> Chọn **Use an existing role** -> Tìm và chọn IAM execution role đã tạo ở bước trước (`examora-lambda-backend-role`).
   * Bấm nút **Create function** ở góc dưới cùng và đợi hệ thống khởi tạo.

   ![Cấu hình tạo Function](/images/5-Workshop/5.5-Lambda/5.5.3-create-lambda-function/LamdaFuctions5.1.png)

   ![Chọn Execution Role](/images/5-Workshop/5.5-Lambda/5.5.3-create-lambda-function/LamdaFuctions5.2.png)

2. Cấu hình cấu hình chung (General Configuration):
   * Do backend Express cần kết nối cơ sở dữ liệu MongoDB Atlas và xử lý nhiều API nghiệp vụ phức tạp hơn các hàm tính toán đơn giản, chúng ta cần tăng các thông số cấu hình mặc định (bộ nhớ và thời gian chờ):
   * Tại tab **Configuration** (Cấu hình) -> Chọn mục **General configuration** -> Chọn **Edit**.
   * Cấu hình các thông số sau:
     * **Memory**: Tăng lên **512 MB** hoặc **1024 MB** (để tăng tốc độ xử lý và giảm cold start).
     * **Timeout**: Tăng lên **30 seconds** (mặc định là 3 giây, tăng lên để tránh lỗi timeout khi kết nối DB hoặc xử lý các truy vấn nặng).
   * Nhấn **Save** để áp dụng cấu hình mới.

   ![Cấu hình General Configuration](/images/5-Workshop/5.5-Lambda/5.5.3-create-lambda-function/LamdaFuctions5.3.png)
