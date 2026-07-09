---
title: "Quản lý tài nguyên AWS bằng Resource Groups, thiết lập quyền IAM và giám sát chi phí"
date: 2026-07-08
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:

* Biết cách viết workshop và báo cáo thực tập theo cấu trúc rõ ràng.
* Thực hành quản lý tài nguyên AWS bằng Tags và Resource Groups.
* Kiểm soát quyền truy cập EC2 dựa trên Resource Tags.
* Sử dụng IAM Permission Boundary để giới hạn quyền tối đa của IAM user.
* Xem cách phân tích chi phí sử dụng AWS bằng Cost Explorer.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Xem hướng dẫn triển khai và viết workshop báo cáo thực tập <br> - Ghi lại cách chia nội dung thành mục tiêu, chuẩn bị, các bước thực hành và kết quả <br> - Xem cách trình bày nội dung song ngữ trong workshop | 11/05/2026 | 11/05/2026 | <https://www.youtube.com/watch?v=mXRqgMr_97U&list=PLahN4TLWtox2a3vElknwzU_urND8hLn1i&index=3> |
| 3 | - Làm lab quản lý tài nguyên bằng Tags và Resource Groups <br> - **Thực hành:** <br>&emsp; + Gắn tag cho một số tài nguyên mẫu <br>&emsp; + Lọc tài nguyên theo tag <br>&emsp; + Tạo Resource Group dựa trên tag | 12/05/2026 | 12/05/2026 | <https://000027.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html> <br> <https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html> |
| 4 | - Làm lab quản lý quyền truy cập EC2 bằng Resource Tags và IAM <br> - **Thực hành:** <br>&emsp; + Tạo IAM Policy có điều kiện theo tag <br>&emsp; + Gán quyền cho role/user phù hợp <br>&emsp; + Kiểm tra quyền truy cập EC2 theo tag | 13/05/2026 | 13/05/2026 | <https://000028.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html> |
| 5 | - Làm lab giới hạn quyền người dùng bằng IAM Permission Boundary <br> - **Thực hành:** <br>&emsp; + Tạo policy giới hạn quyền <br>&emsp; + Gán Permission Boundary cho IAM user <br>&emsp; + Kiểm tra quyền thực tế sau khi bị giới hạn | 14/05/2026 | 14/05/2026 | <https://000030.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html> |
| 6 | - Làm lab phân tích chi phí sử dụng AWS bằng Cost Explorer <br> - **Thực hành:** <br>&emsp; + Xem chi phí theo service <br>&emsp; + Lọc chi phí theo khoảng thời gian <br>&emsp; + Tạo báo cáo chi phí EC2 đơn giản | 15/05/2026 | 15/05/2026 | <https://000034.awsstudygroup.com/> <br> <https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html> |

### Kết quả đạt được tuần 4:

* Biết được cách viết workshop báo cáo thực tập theo cấu trúc mục tiêu, chuẩn bị, thực hành và kết quả.

* Sử dụng được Tags và Resource Groups để phân loại, lọc và gom nhóm tài nguyên AWS.

* Kiểm tra được cách IAM Policy dùng Resource Tags để kiểm soát quyền truy cập EC2.

* Áp dụng được IAM Permission Boundary để giới hạn quyền tối đa của IAM user.

* Sử dụng Cost Explorer để xem chi phí theo service, khoảng thời gian và tạo báo cáo chi phí EC2 đơn giản.