from typing import Callable
from fastapi import FastAPI
from python.data.data_utils import convert_base_model_to_nparray
from python.data.california_data_instance import CaliforniaDataInstance
from python.logger.logger import getLogger

_logger = getLogger()


def create_app(prediction_function: Callable):

    app = FastAPI()

    @app.get("/")
    def root():
        return {"message": "Hello World"}

    @app.post("/predict_california_data_instance")
    def predict_california_data_instance(data_input: CaliforniaDataInstance):
        try:
            data = convert_base_model_to_nparray(data_input)
            prediction = prediction_function(data)
            return {
                "prediction": prediction[0]
            }
        except Exception as e:
            _logger.exception(e)

    return app
