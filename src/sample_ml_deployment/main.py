from .utils import get_or_create_model, upload_file_to_bucket
from .api import create_app
from .model import Model
import boto3
import os

model: Model = None
model_is_retrieved: bool = None
s3_client = boto3.client("s3")
# [model, model_is_retrieved] = get_or_create_model(
#             s3_client, os.environ["bucket_name"], 
#             os.environ["model_key"])

[model, model_is_retrieved] = get_or_create_model(None, None)

# save model if it is not saved and we have the credentials
if not model_is_retrieved:
    pass
    # save the model
    # model.save(os.environ["local_model_filename"])
    # upload_file_to_bucket(
    #         s3_client, os.environ["local_model_filename"], 
    #         os.environ["bucket_name"], os.environ["s3_model_filename"])

# Create the API
app = create_app(model.predict)
