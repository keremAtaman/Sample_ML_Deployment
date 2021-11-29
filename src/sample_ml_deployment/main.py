from .utils import (upload_file_to_bucket, 
                    retreive_environment_variable,
                    get_model_from_s3,
                    create_and_fit_default_model)
from .api import create_app
from .model import Model
import boto3
import logging

def main():
    # TODO: Ensure environment variables/secrets work as intended
    s3_client = None
    try:
        s3_client = boto3.client("s3")
    except Exception as e:
        logging.exception(e) 
        logging.info("s3 client could not be created")
    bucket_name:str = retreive_environment_variable("bucket_name")
    model_key:str = retreive_environment_variable("model_key")

    # try to get the model from s3. If fails, create a new model
    # TODO: check model loading from S3 bucket
    model_loaded_from_bucket:bool = False
    model:Model = get_model_from_s3(s3_client, bucket_name, model_key)
    # check if all required variables for bucket load are proper
    # failed to load a model, so create the default model
    if model is None:
        model = create_and_fit_default_model()

    # save model if it is not saved and we have the credentials
    # TODO: check model saving to S3 bucket
    local_model_filename = retreive_environment_variable("local_model_filename")
    s3_model_filename = retreive_environment_variable("s3_model_filename")
    if not model_loaded_from_bucket:
        try:
            model.save(local_model_filename)
            upload_file_to_bucket(
                    s3_client, local_model_filename, 
                    bucket_name, s3_model_filename)
        except Exception as e:
            logging.exception(e)
            logging.info("Failed to save the model")

    # Create the API
    return create_app(model.predict)

app = main()