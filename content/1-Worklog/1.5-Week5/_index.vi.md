---
title: "Nghiên cứu Amazon Cognito quản lý người dùng và Amazon SES gửi email xác thực"
date: 2026-07-08
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:

* Nắm vai trò của Amazon Cognito trong đăng ký, đăng nhập và quản lý người dùng.
* Cấu hình được User Pool, App Client và luồng xác thực cơ bản.
* Sử dụng Cognito Groups để phân loại người dùng theo nhóm quyền.
* Khảo sát Amazon SES cho luồng xác thực email và khôi phục mật khẩu.
* Hiểu cách JWT token được dùng để bảo vệ API.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Khảo sát Amazon Cognito User Pools <br> - Nắm luồng sign-up, confirm account, sign-in và token trả về sau đăng nhập <br> - Xem vai trò của App Client trong ứng dụng web | 18/05/2026 | 18/05/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html> <br>  |
| 3 | - Làm lab xác thực SPA bằng Amazon Cognito <br> - **Thực hành:** <br>&emsp; + Tạo/cấu hình Cognito User Pool <br>&emsp; + Cấu hình App Client cho ứng dụng web <br>&emsp; + Kiểm tra luồng đăng ký và đăng nhập người dùng | 19/05/2026 | 19/05/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html> |
| 4 | - Khảo sát Cognito Groups và thông tin nhóm trong token <br> - **Thực hành:** <br>&emsp; + Tạo một số group người dùng mẫu <br>&emsp; + Gán user vào group phù hợp <br>&emsp; + Kiểm tra thông tin group trong token sau đăng nhập | 20/05/2026 | 20/05/2026 | <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html> <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html> |
| 5 | - Khảo sát Amazon SES cho email xác thực và reset password <br> - **Thực hành:** <br>&emsp; + Tạo email identity trong SES <br>&emsp; + Verify email identity <br>&emsp; + Xem giới hạn gửi mail khi tài khoản còn trong SES sandbox | 21/05/2026 | 21/05/2026 | <https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html> <br> <https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html> <br> <https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html> |
| 6 | - Khảo sát cách bảo vệ API bằng Cognito/JWT Authorizer <br> - **Thực hành:** <br>&emsp; + Xem cách API Gateway dùng Cognito User Pool làm authorizer <br>&emsp; + Kiểm tra cách gửi token trong header `Authorization` <br>&emsp; + Phân biệt API public và API yêu cầu đăng nhập | 22/05/2026 | 22/05/2026 |  <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html> <br> <https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-accessing-resources-api-gateway-and-lambda.html> |

### Kết quả đạt được tuần 5:

* Nắm được vai trò của Cognito User Pool, App Client và luồng sign-up/sign-in trong ứng dụng web.

* Cấu hình được luồng xác thực SPA bằng Amazon Cognito và kiểm tra được đăng ký, đăng nhập người dùng.

* Tạo được Cognito Groups, gán user vào group và kiểm tra thông tin group trong token.

* Verify được email identity trong Amazon SES và hiểu giới hạn gửi mail khi tài khoản còn trong sandbox.

* Biết cách Cognito/JWT Authorizer bảo vệ API và cách client gửi token qua header `Authorization`.