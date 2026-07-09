---
title: "Tìm hiểu xử lý bất đồng bộ serverless, tích hợp SQS, CloudWatch và chốt đề tài thực tập"
date: 2026-07-08
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:

* Hiểu cách xử lý bất đồng bộ trong kiến trúc serverless.
* Thực hành luồng S3 ObjectCreated kích hoạt Lambda.
* Sử dụng SQS để tách tác vụ xử lý nền khỏi request chính.
* Theo dõi Lambda bằng CloudWatch Logs và X-Ray.
* Chốt hướng đề tài, phạm vi và kiến trúc tổng quan cho dự án cuối kỳ.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu kiến trúc event-driven với SNS và SQS <br> - Phân biệt message queue và publish/subscribe <br> - Xem cách queue giúp tách hệ thống gửi yêu cầu và hệ thống xử lý nền | 01/06/2026 | 01/06/2026 | <https://000077.awsstudygroup.com/vi/> <br> <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html> |
| 3 | - Thực hành S3 ObjectCreated trigger Lambda <br> - **Thực hành:** <br>&emsp; + Tạo S3 bucket dùng cho lab <br>&emsp; + Cấu hình event notification khi upload object <br>&emsp; + Kiểm tra Lambda được gọi sau khi file được upload | 02/06/2026 | 02/06/2026 |  <br> <https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html> |
| 4 | - Thực hành xử lý message bằng SQS và Lambda <br> - **Thực hành:** <br>&emsp; + Tạo SQS queue thử nghiệm <br>&emsp; + Gửi message mẫu vào queue <br>&emsp; + Cấu hình Lambda đọc và xử lý message từ queue | 03/06/2026 | 03/06/2026 | <https://000083.awsstudygroup.com/vi/> <br> <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html> |
| 5 | - Theo dõi Lambda bằng CloudWatch Logs và X-Ray <br> - **Thực hành:** <br>&emsp; + Xem log của Lambda trong CloudWatch Logs <br>&emsp; + Bật X-Ray tracing cho Lambda function <br>&emsp; + Kiểm tra lỗi và thời gian xử lý của request | 04/06/2026 | 04/06/2026 | <https://000140.awsstudygroup.com/vi/> <br> <br> <https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-view.html> |
| 6 | - Lên kế hoạch và chốt hướng dự án cuối kỳ: Examora <br> - Chốt kiến trúc Serverless cho dự án <br> - Xác định các nhóm chức năng chính: authentication, API/backend, upload file, import Word, chấm bài bất đồng bộ và monitoring | 05/06/2026 | 05/06/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html> <br> <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html> |

### Kết quả đạt được tuần 7:

* Hiểu được vai trò của SQS và SNS trong kiến trúc event-driven.

* Cấu hình được S3 ObjectCreated event để kích hoạt Lambda sau khi upload file.

* Tạo được SQS queue, gửi message mẫu và cấu hình Lambda xử lý message từ queue.

* Xem được Lambda logs trong CloudWatch và bật X-Ray tracing để theo dõi request.

* Chốt được đề tài cuối kỳ là Examora theo hướng AWS Serverless.

* Xác định được các nhóm chức năng chính cần triển khai trong Examora: authentication, API/backend, upload file, import Word, chấm bài bất đồng bộ và monitoring.