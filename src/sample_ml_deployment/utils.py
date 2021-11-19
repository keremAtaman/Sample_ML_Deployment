import logging
from .model import Model
from numpy import ndarray, array
from typing import Callable, Tuple
from typing import Any
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
import os
from pickle import load



def get_california_housing_prices_dataset() -> Tuple[ndarray]:
    """Gets California housing prices dataset found in
    :link:`https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html`

    Returns:
        Tuple(ndarray): A tuple of form (ndarray, ndarray) where 
                        return[0] = input and return[1] = target (aka label)
    """
    return fetch_california_housing(return_X_y = True)

def convert_base_model_to_nparray(base_model: BaseModel)->ndarray:
    """Converts an object of type BaseModel into an ndarray

    Args:
        base_model (BaseModel): An instance of BaseModel which
                                all of the fields are in key,value format

    Returns:
        ndarray: base_model, turned into ndarray
    """
    return array(list(base_model.dict().values())).reshape(1,-1)

def create_default_linear_regression_model():
    model_ = LinearRegression()
    model = Model(
        model = model_,
        fit = model_.fit,
        predict = model_.predict
    )
    return model

def get_model_from_s3(s3_client, bucket_name:str, model_key:str)-> Model:
    """Loads the specified Model object from s3

    Args:
        s3_client ([type]): s3 client instance
        bucket_name (str): name of the bucket where model is stored
        model_key (str, optional): key (aka name) of model.

    Returns:
        Model: The model object if it is successfully retreived from s3. 
                Otherwise, this value is set to None 
    """
    model:Model = None
    try:
        model = load(s3_client.get_object(bucket_name, model_key))
        logging.info("Model successfully loaded")
    #any other exception
    except Exception as e:
        logging.exception(e) 
        logging.info("Model could not be retrieved, creating new model")

    return model

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
        logging.error(e)

    return False

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
        result = os.environ[env_var_name]
    except Exception as e:
        logging.exception(e) 
        logging.info(env_var_name + "does not exist as an environment variable")

    return result

def create_and_fit_default_model():
    [X,y] = get_california_housing_prices_dataset()

    model: Model = create_default_linear_regression_model()
    model.fit(X, y)
    return model