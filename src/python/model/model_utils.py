from sklearn.linear_model import LinearRegression
from python.model.model import Model
from pickle import load
from python.logger.logger import getLogger
from python.data.data_utils import get_california_housing_prices_dataset

_logger = getLogger()

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
        _logger.info("Model successfully loaded")
    #any other exception
    except Exception as e:
        _logger.exception(e) 
        _logger.info("Model could not be retrieved, creating new model")

    return model

def create_and_fit_default_model():
    [X,y] = get_california_housing_prices_dataset()

    model: Model = create_default_linear_regression_model()
    model.fit(X, y)
    return model