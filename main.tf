provider "aws" {
    profile = "default"
    region = "us-east-2"
}

# Declaring the Provider Requirements
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

module "s3" {
    source = "./src/terraform/S3"
    #bucket name should be unique
    bucket_name = "kacorperation2-model-bucket"       
}