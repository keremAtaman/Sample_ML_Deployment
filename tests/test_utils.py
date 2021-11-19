#TODO: tests for utils
from sample_ml_deployment.utils import(
    get_california_housing_prices_dataset,
    create_default_linear_regression_model,
    retreive_environment_variable,
    create_and_fit_default_model
)
import os
import logging

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

def test_create_default_linear_regression_model():
    model = create_default_linear_regression_model()
    # ensure fitting works
    [X,y] = get_california_housing_prices_dataset()
    model.fit(X,y)
    #ensure predicting works and outputs 
    prediction = model.predict(X[0].reshape(1,-1))
    assert prediction is not None, "Prediction was not done successfully"

def test_retreive_existing_environment_variable():
    env_variable_name = 'env_var_to_create_and_get'
    expected_result = 'Afgsjgfigasf'
    #set environment variable
    os.environ[env_variable_name] = expected_result
    actual_result = retreive_environment_variable(env_variable_name)
    assert expected_result == actual_result
    #delete the variable after use
    os.environ.pop(env_variable_name)

def test_retrieve_unexisting_environment_variable():
    env_variable_name = 'Afgsjgfigasf'
    # if the variable somewhy exists, pop it
    try:
        os.environ.pop(env_variable_name)
    except KeyError:
        # the variable is not an env variable, continue
        pass
    except Exception as e:
        logging.exception(e)
    expected_result = None
    actual_result = retreive_environment_variable(env_variable_name)
    assert expected_result == actual_result

def test_create_and_fit_default_model():
    model = create_and_fit_default_model()
    [X,y] = get_california_housing_prices_dataset()
    prediction = model.predict(X[0].reshape(1,-1))
    assert prediction is not None, "Prediction was not done successfully"