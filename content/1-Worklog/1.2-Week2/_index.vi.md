---
title: "Sử dụng AWS Management Console, cấu hình AWS CLI và tìm hiểu IAM, S3, EC2"
date: 2026-07-08
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:

* Sử dụng được AWS Management Console để truy cập và kiểm tra các dịch vụ cơ bản.
* Cài đặt, cấu hình AWS CLI và kiểm tra kết nối tài khoản từ terminal.
* Nắm rõ hơn IAM Policy, IAM Role và nguyên tắc cấp quyền tối thiểu.
* Khảo sát Amazon S3 thông qua các khái niệm bucket, object và quyền truy cập.
* Nắm vai trò của Amazon VPC và Amazon EC2 trong hạ tầng AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Thực hành điều hướng trên AWS Management Console <br> - Kiểm tra cách chọn Region trước khi xem hoặc tạo tài nguyên <br> - Mở các khu vực chính như Billing, IAM, S3, EC2, VPC và CloudWatch | 27/04/2026 | 27/04/2026 | <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html> <br> <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Cài đặt AWS CLI trên máy cá nhân <br> - **Thực hành:** <br>&emsp; + Cấu hình default profile bằng `aws configure` <br>&emsp; + Kiểm tra cấu hình bằng `aws configure list` <br>&emsp; + Xác nhận danh tính tài khoản bằng `aws sts get-caller-identity` | 28/04/2026 | 28/04/2026 | <https://000011.awsstudygroup.com/vi/3-installcli/> <br> <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html> <br> <https://docs.aws.amazon.com/cli/latest/reference/configure/> |
| 4 | - Phân tích cấu trúc IAM Policy gồm `Effect`, `Action`, `Resource`, `Condition` <br> - Phân biệt AWS managed policy, customer managed policy và inline policy <br> - Xem vai trò của IAM Role khi cấp quyền cho người dùng hoặc dịch vụ AWS | 29/04/2026 | 29/04/2026 | <https://000002.awsstudygroup.com/vi/1-introduction/1.2-iam-policy/> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html> |
| 5 | - Khảo sát các khái niệm chính của Amazon S3: bucket, object, key, metadata <br> - Xem cách S3 lưu trữ dữ liệu theo mô hình object storage <br> - **Thực hành:** <br>&emsp; + Tạo bucket thử nghiệm <br>&emsp; + Upload object và kiểm tra object key <br>&emsp; + Rà soát Block Public Access | 30/04/2026 | 30/04/2026 | <https://000057.awsstudygroup.com/vi/1-introduce/> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html> |
| 6 | - Nắm vai trò của VPC, subnet, route table, internet gateway và security group <br> - Xem cách EC2 instance được đặt trong VPC <br> - Đọc lab VPC/EC2 để nhận biết public subnet, private subnet và security group | 01/05/2026 | 01/05/2026 | <https://000003.awsstudygroup.com/vi/> <br> <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html> |

### Kết quả đạt được tuần 2:

* Sử dụng được AWS Management Console để truy cập các dịch vụ chính và kiểm tra tài nguyên theo Region.

* Cài đặt AWS CLI, cấu hình default profile và kiểm tra được danh tính tài khoản bằng lệnh CLI.

* Đọc được cấu trúc IAM Policy cơ bản và phân biệt được IAM User, Group, Role.

* Tạo thử S3 bucket, upload object và hiểu cách S3 quản lý dữ liệu bằng bucket/object/key.

* Nắm được vai trò của VPC, subnet, security group và cách EC2 hoạt động trong mạng AWS.

* Có nền tảng thao tác AWS tốt hơn trước khi chuyển sang phần kiến trúc và các dịch vụ chuyên sâu hơn.