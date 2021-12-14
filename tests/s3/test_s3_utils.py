from python.s3.s3_utils import (get_s3_client)

# TODO: upload_file_to_bucket
# TODO: get_s3_client

def test_get_s3_client():
    assert get_s3_client() != None