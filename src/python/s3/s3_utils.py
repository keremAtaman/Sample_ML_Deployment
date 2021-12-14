import boto3
from python.logger.logger import getLogger

_logger = getLogger()

def upload_file_to_bucket(s3_client, local_filename:str, bucket_name:str, 
                    s3_filename:str) -> bool:
    """Uploads a local file to s3 bucket

    Args:
        s3_client ([type]): s3 client instance
        local_filename (str): filename of the local file
        bucket_name (str): name of the bucket to store the local file
        s3_filename (str): name of the local file as it will be saved in s3

    Returns:
        bool: True if successfully uploaded, False otherwise
    """
    # NOTE: Each Amazon S3 object has data, a key, and metadata. 
    # The object key (or key name) uniquely identifies the object in a bucket
    try:
        s3_client.upload_file(
            local_filename, bucket_name, s3_filename)
        return True
    except Exception as e:
        _logger.error(e)

    return False

def get_s3_client():
    # TODO: Ensure environment variables/secrets work as intended
    s3_client = None
    try:
        s3_client = boto3.client("s3")
    except Exception as e:
        _logger.exception(e) 
        _logger.info("s3 client could not be created")
    return s3_client