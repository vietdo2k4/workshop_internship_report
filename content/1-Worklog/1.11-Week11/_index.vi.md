---
title: "Thiết lập hàng đợi Amazon SQS và triển khai Lambda Grading Worker chấm thi bất đồng bộ"
date: 2026-07-08
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

* Tách logic chấm bài khỏi request nộp bài bằng Amazon SQS.
* Xây dựng Lambda Grading Worker để xử lý chấm bài bất đồng bộ.
* Tối ưu lại sơ đồ kiến trúc theo luồng submit bài và chấm điểm.
* Tìm hiểu Amplify Hosting và Route 53 để chuẩn bị triển khai frontend.
* Test lại các chức năng chính sau khi tích hợp các luồng serverless.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Phân tích logic chấm bài hiện tại trong backend <br> - Xác định phần cần tách khỏi request nộp bài <br> - Thiết kế payload gửi vào SQS chỉ gồm các ID cần thiết | 29/06/2026 | 29/06/2026 | <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html> |
| 3 | - Hoàn thiện luồng chấm bài bằng SQS và Lambda Worker <br> - Tối ưu lại sơ đồ kiến trúc theo luồng SQS grading <br> - Backend gửi grading job vào SQS, Lambda Worker nhận message và xử lý chấm điểm | 30/06/2026 | 30/06/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html> |
| 4 | - Tìm hiểu Amplify Hosting để chuẩn bị deploy frontend <br> - Xem cách kết nối custom domain với Amplify bằng Route 53 <br> - Ghi lại các cấu hình cần chuẩn bị: build output, environment variables, rewrite rule và domain | 01/07/2026 | 01/07/2026 | <https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html> <br> <https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html> <br> <https://docs.aws.amazon.com/amplify/latest/userguide/to-add-a-custom-domain-managed-by-amazon-route-53.html> |
| 5 | - Bổ sung xử lý lỗi cho luồng chấm bài bất đồng bộ <br> - Cấu hình visibility timeout phù hợp với thời gian chấm bài <br> - Ghi nhận trạng thái xử lý thành công/thất bại và thêm log để kiểm tra lỗi worker | 02/07/2026 | 02/07/2026 | <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html> |
| 6 | - Test lại các chức năng chính sau khi tích hợp <br> - Test đăng nhập và gọi API cần token <br> - Test upload/import Word, nộp bài và nhận kết quả sau khi worker chấm | 03/07/2026 | 03/07/2026 | <br> <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html> |

### Kết quả đạt được tuần 11:

* Xác định được phần logic chấm bài cần tách khỏi request nộp bài.

* Backend gửi được grading job vào SQS và Lambda Worker xử lý được message chấm bài.

* Tối ưu lại sơ đồ kiến trúc với luồng submit bài, SQS Grading Queue và Lambda Grading Worker.

* Nắm được cách Amplify Hosting kết hợp với Route 53 để chuẩn bị deploy frontend.

* Bổ sung được xử lý lỗi, trạng thái xử lý và log cho luồng chấm bài bất đồng bộ.

* Test lại được các chức năng chính: xác thực, upload/import Word, nộp bài và nhận kết quả.