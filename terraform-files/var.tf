variable "aws_region" {
  description = "AWS region where resources will be provisioned"
  default     = "eu-north-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  default     = "ami-07a0715df72e58928"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
  default     = "t3.micro"
}
