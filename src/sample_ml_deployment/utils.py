import logging
from .model import Model
from numpy import ndarray, array
from typing import Callable, Tuple
from typing import Any
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from pickle import load
from pydantic import BaseModel


def get_california_housing_prices_dataset() -> Tuple[ndarray]:
    """Gets California housing prices dataset found in
    :link:`https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html`

    Returns:
        Tuple(ndarray): A tuple of form (ndarray, ndarray) where 
                        return[0] = input and return[1] = target (aka label)
    """
    return fetch_california_housing(return_X_y = True)

def convert_base_model_to_nparray(base_model: BaseModel):
    return array(list(base_model.dict().values())).reshape(1,-1)

def create_and_fit_linear_regression_model(X:ndarray, y:ndarray):
    model_ = LinearRegression()
    model = Model(
        model = model_,
        fit = model_.fit,
        predict = model_.predict
    )
    model.fit(X, y)    
    return model

def get_or_create_model(s3_client, bucket_name:str, model_key:str = None, 
                            get_dataset: Callable = get_california_housing_prices_dataset,
                            create_and_fit_model: Callable = create_and_fit_linear_regression_model
                            )-> Tuple[Model,bool]:
    # check if there is an existing model in S3 bucket - if not, 
    # create a model AND train it
    # TODO: check if the file is there
    model:Model = None
    model_successfully_loaded = False
    # check if we have s3 client etc. definitions
    try:
        model = load(s3_client.get_object(bucket_name, model_key))
        model_successfully_loaded = True
        logging.info("Model successfully loaded")
    #any other exception
    except Exception as e:
        logging.exception(e) 
        logging.info("Model could not be retrieved, creating new model")
        [X,y] = get_dataset()
        model = create_and_fit_model(X, y)

    return (model,model_successfully_loaded)

def upload_file_to_bucket(s3_client, local_filename:str, bucket_name:str, 
                    s3_filename:str) -> bool:
        # NOTE: Each Amazon S3 object has data, a key, and metadata. 
        # The object key (or key name) uniquely identifies the object in a bucket
        try:
            s3_client.upload_file(
                local_filename, bucket_name, s3_filename)
            return True
        except Exception as e:
            logging.error(e)

        return False