from python.logger.logger import getLogger
from python.data.data_utils import get_california_housing_prices_dataset

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

# TODO: convert_base_model_to_nparray