---
title: "Practicing with AWS Console/CLI, IAM Policies, and Foundation Services"
date: 2026-07-08
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:

* Use the AWS Management Console to access and check basic AWS services.
* Install, configure, and verify AWS CLI access from the terminal.
* Understand IAM Policy, IAM Role, and the principle of least privilege more clearly.
* Review Amazon S3 through bucket, object, key, and access control concepts.
* Understand the role of Amazon VPC and Amazon EC2 in AWS infrastructure.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Navigate the AWS Management Console <br> - Check how to select a Region before viewing or creating resources <br> - Open key areas such as Billing, IAM, S3, EC2, VPC, and CloudWatch | 27/04/2026 | 27/04/2026 | <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html> <br> <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Install the AWS CLI on the local computer <br> - **Practice:** <br>&emsp; + Configure the default profile using `aws configure` <br>&emsp; + Check the configuration with `aws configure list` <br>&emsp; + Verify account identity with `aws sts get-caller-identity` | 28/04/2026 | 28/04/2026 | <https://000011.awsstudygroup.com/vi/3-installcli/> <br> <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html> <br> <https://docs.aws.amazon.com/cli/latest/reference/configure/> |
| 4 | - Analyze the IAM Policy structure: `Effect`, `Action`, `Resource`, and `Condition` <br> - Distinguish between AWS managed policies, customer managed policies, and inline policies <br> - Review the role of IAM Role when granting permissions to users or AWS services | 29/04/2026 | 29/04/2026 | <https://000002.awsstudygroup.com/vi/1-introduction/1.2-iam-policy/> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html> <br> <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html> |
| 5 | - Review the main Amazon S3 concepts: bucket, object, key, and metadata <br> - Learn how S3 stores data using the object storage model <br> - **Practice:** <br>&emsp; + Create a test bucket <br>&emsp; + Upload an object and check its object key <br>&emsp; + Review Block Public Access | 30/04/2026 | 30/04/2026 | <https://000057.awsstudygroup.com/vi/1-introduce/> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html> <br> <https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html> |
| 6 | - Understand the role of VPC, subnet, route table, internet gateway, and security group <br> - Review how an EC2 instance runs inside a VPC <br> - Read the VPC/EC2 lab to identify public subnet, private subnet, and security group usage | 01/05/2026 | 01/05/2026 | <https://000003.awsstudygroup.com/vi/> <br> <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html> <br> <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html> |

### Week 2 Results:

* Used the AWS Management Console to access key services and check resources by Region.

* Installed the AWS CLI, configured the default profile, and verified the account identity using CLI commands.

* Read the basic IAM Policy structure and distinguished IAM User, Group, and Role.

* Created a test S3 bucket, uploaded an object, and understood how S3 manages data using bucket/object/key.

* Understood the role of VPC, subnet, security group, and how EC2 works inside an AWS network.

* Built stronger AWS operation skills before moving to architecture and more advanced services.