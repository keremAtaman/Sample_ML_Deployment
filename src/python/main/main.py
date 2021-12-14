from python.model.model_utils import (create_and_fit_default_model,
                                get_model_from_s3)
from python.s3.s3_utils import (upload_file_to_bucket, get_s3_client)
from python.api.api import create_app
from python.model.model import Model
from typing import Any
from python.logger.logger import getLogger
import os

_logger = getLogger()

def retreive_environment_variable(env_var_name:str) ->Any:
    """Gets the environment variable with the name "env_var_name"
        If the environment variable does not exist, logs the exception and
        returns None

    Args:
        env_var_name (str): name of the environment variable to retreive

    Returns:
        Any: environment variable if it exists, None otherwise
    """
    result = None
    try:
        result = os.getenv(env_var_name)
    except Exception as e:
        _logger.exception(e) 
        _logger.info(env_var_name + "does not exist as an environment variable")

    return result

def main():
    s3_client = get_s3_client()
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
            _logger.exception(e)
            _logger.info("Failed to save the model")

    # Create the API
    return create_app(model.predict)

app = main()