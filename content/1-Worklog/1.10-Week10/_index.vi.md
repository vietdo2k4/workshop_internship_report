---
title: "Xây dựng luồng tải tập tin lên S3 và quy trình nhập câu hỏi tự động từ file Word"
date: 2026-07-08
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu tuần 10:

* Triển khai luồng upload file cho Examora bằng S3 Upload Bucket và presigned URL.
* Cập nhật backend để tạo presigned URL theo loại file và quyền người dùng.
* Cập nhật frontend để upload avatar, ảnh lớp học, ảnh đề thi, ảnh câu hỏi và file Word.
* Xây dựng luồng import câu hỏi từ Word bằng S3 ObjectCreated event và Lambda.
* Bổ sung xử lý lỗi, log và secret config cho pipeline import Word.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Thiết kế S3 Upload Bucket cho file nghiệp vụ <br> - Quy ước prefix cho avatar, ảnh lớp học, ảnh đề thi, ảnh câu hỏi và file Word <br> - Cấu hình bucket private và xem lại CORS cho luồng upload từ frontend | 22/06/2026 | 22/06/2026 | <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html> |
| 3 | - Cập nhật backend để tạo presigned URL theo từng loại upload <br> - Kiểm tra JWT và role trước khi tạo URL <br> - Backend quyết định object key theo prefix và trả về presigned PUT URL cho frontend | 23/06/2026 | 23/06/2026 | <https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html> |
| 4 | - Cập nhật frontend cho luồng upload file bằng presigned URL <br> - Gọi API để lấy presigned URL và PUT file trực tiếp lên S3 <br> - Lưu lại object key khi cập nhật nghiệp vụ tương ứng | 24/06/2026 | 24/06/2026 | > |
| 5 | - Xây dựng pipeline import câu hỏi từ file Word <br> - Upload file Word vào prefix `imports/word/raw/` <br> - Cấu hình S3 ObjectCreated event gọi Lambda Import Word Processor và kiểm tra event payload | 25/06/2026 | 25/06/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html> <br> <https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html> |
| 6 | - Hoàn thiện xử lý import Word và ghi log lỗi <br> - Lambda đọc file Word từ S3 và lấy secret config cần thiết bằng Secrets Manager <br> - Ghi log kết quả import thành công hoặc thất bại để dễ kiểm tra lỗi | 26/06/2026 | 26/06/2026 | <https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html> <br> |

### Kết quả đạt được tuần 10:

* Thiết kế được S3 Upload Bucket private và quy ước prefix cho các loại file của Examora.

* Backend tạo được presigned URL theo loại upload, role người dùng và object key do hệ thống quy định.

* Frontend upload được file trực tiếp lên S3 bằng presigned URL và lưu lại object key cho nghiệp vụ.

* Cấu hình được S3 ObjectCreated event để kích hoạt Lambda Import Word Processor khi có file Word mới.

* Lambda Import Word Processor đọc được file từ S3, dùng secret config cần thiết và ghi log kết quả xử lý.