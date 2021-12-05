from python.main import (main, retreive_environment_variable)
import os

def test_retreive_existing_environment_variable():
    env_variable_name = 'env_var_to_create_and_get'
    expected_result = 'Afgsjgfigasf'
    #set environment variable
    os.environ[env_variable_name] = expected_result
    actual_result = retreive_environment_variable(env_variable_name)
    assert expected_result == actual_result
    #delete the variable after use
    os.environ.pop(env_variable_name)

def test_main():
    app = main()

# TODO: test_retreive_environment_variable
# TODO: test model_loaded_from_bucket
# TODO: test NOT model_loaded_from_bucket