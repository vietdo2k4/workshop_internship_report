---
title: "Thiết kế sơ đồ kiến trúc AWS và thực hành tích hợp API Gateway với Lambda"
date: 2026-07-08
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:

* Hiểu vai trò của sơ đồ kiến trúc khi trình bày hệ thống trên AWS.
* Biết cách đọc và phác thảo sơ đồ AWS bằng các lớp cơ bản.
* Sử dụng được AWS Architecture Icons khi vẽ sơ đồ.
* Nắm các ý chính của AWS Well-Architected Framework.
* Thực hành một lab serverless ngắn để hiểu cách API Gateway kết nối với Lambda.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Xem cách vẽ AWS Architecture thông qua video hướng dẫn <br> - Nhận diện các lớp thường gặp: user/client, frontend, network, backend, database, storage <br> - Ghi lại cách trình bày luồng request bằng mũi tên trong sơ đồ | 04/05/2026 | 04/05/2026 | <https://www.youtube.com/watch?v=l8isyDe-GwY&list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i&index=2> <br> <https://aws.amazon.com/architecture/> |
| 3 | - Khảo sát AWS Architecture Center và một số kiến trúc tham khảo <br> - Tải bộ AWS Architecture Icons chính thức <br> - Thử dựng sơ đồ web đơn giản bằng draw.io/diagrams.net | 05/05/2026 | 05/05/2026 | <https://aws.amazon.com/architecture/> <br> <https://aws.amazon.com/architecture/icons/> |
| 4 | - Khảo sát AWS Well-Architected Framework và 6 pillar chính <br> - Đối chiếu các pillar với một hệ thống web đơn giản <br> - Làm thử một checklist ngắn từ AWS Well-Architected Labs | 06/05/2026 | 06/05/2026 | <https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html> <br> <https://aws.amazon.com/architecture/well-architected/> <br> <https://www.wellarchitectedlabs.com/> |
| 5 | - Thực hành lab serverless cơ bản với API Gateway và Lambda <br> - **Thực hành:** <br>&emsp; + Tạo Lambda function đơn giản <br>&emsp; + Tạo API endpoint gọi vào Lambda <br>&emsp; + Kiểm tra response và log trong CloudWatch | 07/05/2026 | 07/05/2026 | <https://aws.amazon.com/serverless-workshops/> <br> <https://docs.aws.amazon.com/serverless/latest/devguide/starter-apigw.html> |
| 6 | - Khảo sát vai trò của database trong sơ đồ kiến trúc AWS <br> - So sánh nhanh RDS và DynamoDB theo kiểu dữ liệu, cách mở rộng và tình huống sử dụng <br> - Bổ sung database layer vào sơ đồ web mẫu đã vẽ | 08/05/2026 | 08/05/2026 | <https://aws.amazon.com/rds/getting-started/> <br> <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html> |

### Kết quả đạt được tuần 3:

* Biết cách đọc sơ đồ AWS theo các lớp chính: client, frontend, network, backend, storage/database và monitoring.

* Dựng được một sơ đồ web đơn giản bằng AWS Architecture Icons.

* Nắm được 6 pillar của AWS Well-Architected Framework và hiểu vì sao kiến trúc không chỉ cần “chạy được”.

* Hoàn thành lab serverless cơ bản với API Gateway và Lambda, kiểm tra được response và log.

* Phân biệt được vai trò cơ bản của RDS và DynamoDB khi đặt database layer trong sơ đồ.

* Có nền tảng ban đầu để sang tuần 4 học cách viết workshop, trình bày báo cáo và mô tả kiến trúc rõ ràng hơn.