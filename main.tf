provider "aws" {
    profile = "default"
    region = "us-east-1"
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
    source = "./src/S3"
    #bucket name should be unique
    bucket_name = "Sample_ML_Deployment_Model"       
}