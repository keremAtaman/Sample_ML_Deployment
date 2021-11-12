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

# Granting the Bucket Access
resource "aws_s3_bucket_public_access_block" "publicaccess" {
  bucket = aws_s3_bucket.modelbucket.id
  block_public_acls = false
  block_public_policy = false
}

resource "aws_s3_bucket" "modelbucket" {
  bucket = "modelbucket"
  force_destroy = false
#   server_side_encryption_configuration {
#     rule {
#         apply_server_side_encryption_by_default {
#         kms_master_key_id = aws_kms_key.mykey.arn
#         sse_algorithm = "aws:kms"
#       }
#     }
#   }
  # Keeping multiple versions of an object in the same bucket
  versioning {
    enabled = true
  }
}