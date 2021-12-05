from python.model.model_utils import (create_default_linear_regression_model,
                                        create_and_fit_default_model)
from python.data.data_utils import get_california_housing_prices_dataset

[X,y] = get_california_housing_prices_dataset()

def test_create_default_linear_regression_model():
    model = create_default_linear_regression_model()
    # ensure fitting works
    model.fit(X,y)
    #ensure predicting works and outputs 
    prediction = model.predict(X[0].reshape(1,-1))
    assert prediction is not None, "Prediction was not done successfully"

def test_create_and_fit_default_model():
    model = create_and_fit_default_model()
    prediction = model.predict(X[0].reshape(1,-1))
    assert prediction is not None, "Prediction was not done successfully"

# TODO: get_model_from_s3