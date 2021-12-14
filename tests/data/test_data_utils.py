from python.logger.logger import getLogger
from python.data.data_utils import (get_california_housing_prices_dataset,
                                    convert_base_model_to_nparray)
from pydantic import BaseModel
from numpy import array

_logger = getLogger()

def test_get_california_housing_prices_dataset():
    num_expected_rows = 20640
    num_X_cols = 8
    test = get_california_housing_prices_dataset()

    #ensure X and y is acquired
    assert len(test) == 2
    #ensure # of expected rows is acquired
    assert len(test[0]) == num_expected_rows
    #ensure # of rows for X and y are equal
    assert len(test[0]) == len(test[1])
    #ensure # expected cols for X is acquired
    assert len(test[0][0]) == num_X_cols

def test_convert_base_model_to_nparray():
    class BaseModelTestClass(BaseModel):
        firstInput: float
        secondInput: float
    
    input_ = {'firstInput': 1.0, 'secondInput': 2.0}
    expected_output = array(list(input_.values()))

    baseModelTestClass = BaseModelTestClass(firstInput = 1.0, secondInput = 2.0)
    actual_output = convert_base_model_to_nparray(baseModelTestClass)

    assert expected_output.all() == actual_output.all()