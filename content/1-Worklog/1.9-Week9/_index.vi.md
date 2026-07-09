---
title: "Triển khai luồng xác thực người dùng Cognito và đưa Express Backend lên AWS Lambda"
date: 2026-07-08
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:

* Triển khai luồng xác thực người dùng cho Examora bằng Amazon Cognito và Amazon SES.
* Cập nhật frontend cho các chức năng đăng ký, xác thực OTP, đăng nhập, đăng xuất và quên mật khẩu.
* Bổ sung dữ liệu định danh từ Cognito vào thông tin người dùng trong MongoDB.
* Sửa backend để verify Cognito JWT và đồng bộ profile người dùng.
* Đưa Express backend vào Lambda handler và bảo vệ API bằng API Gateway Authorizer.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Cấu hình Cognito User Pool và App Client cho Examora <br> - **Thực hành:** <br>&emsp; + Tạo các group người dùng chính <br>&emsp; + Cấu hình đăng ký, đăng nhập bằng email <br>&emsp; + Verify email identity trong Amazon SES | 15/06/2026 | 15/06/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html> <br>  <br> <https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html> |
| 3 | - Cập nhật dữ liệu người dùng để lưu thông tin định danh từ Cognito <br> - Bổ sung thông tin cần thiết cho việc đồng bộ tài khoản và phân quyền <br> - Kiểm tra lại logic role hiện có để không ảnh hưởng nghiệp vụ cũ | 16/06/2026 | 16/06/2026 |  <br>  |
| 4 | - Sửa frontend cho các luồng xác thực bằng Cognito <br> - **Thực hành:** <br>&emsp; + Cập nhật đăng ký và xác thực OTP email <br>&emsp; + Cập nhật đăng nhập, đăng xuất và quên mật khẩu <br>&emsp; + Lưu token để gọi các API cần đăng nhập | 17/06/2026 | 18/06/2026 |   <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html> |
| 5 | - Sửa backend để verify Cognito JWT và đồng bộ profile vào MongoDB <br> - **Thực hành:** <br>&emsp; + Đọc token từ header `Authorization` <br>&emsp; + Đồng bộ thông tin người dùng sau khi đăng nhập <br>&emsp; + Mapping Cognito Groups sang role hệ thống | 19/06/2026 | 19/06/2026 |  <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html> |
| 6 | - Đưa Express backend vào Lambda handler và cấu hình API Gateway Authorizer <br> - **Thực hành:** <br>&emsp; + Tạo entry point cho Lambda Backend API <br>&emsp; + Cấu hình các biến môi trường cần thiết <br>&emsp; + Test `/health` và một API cần token | 20/06/2026 | 20/06/2026 |    <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html> |

### Kết quả đạt được tuần 9:

* Cấu hình được Cognito User Pool, App Client, nhóm người dùng và email identity trong SES cho luồng xác thực.

* Bổ sung được thông tin định danh từ Cognito vào dữ liệu người dùng mà vẫn giữ được phân quyền nghiệp vụ hiện có.

* Cập nhật được frontend cho các luồng đăng ký, xác thực OTP, đăng nhập, đăng xuất và quên mật khẩu.

* Backend verify được Cognito JWT, đồng bộ profile người dùng và mapping group sang role hệ thống.

* Tạo được Lambda handler cho Express backend, cấu hình API Gateway Authorizer và test được API cần token.