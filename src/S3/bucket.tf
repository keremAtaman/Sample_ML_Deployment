resource "aws_s3_bucket" "Sample_ML_Deployment_Model" {
    bucket = "${var.bucket_name}" 
    acl = "${var.acl_value}"   
}