from typing import Tuple
from numpy import ndarray, array
from sklearn.datasets import fetch_california_housing
from pydantic import BaseModel
from logger.logger import getLogger

_logger = getLogger()

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