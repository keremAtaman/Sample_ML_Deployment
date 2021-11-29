resource "aws_s3_bucket" "model-bucket" {
    bucket = "${var.bucket_name}" 
    acl = "${var.acl_value}"   
}