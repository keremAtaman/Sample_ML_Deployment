from typing import Callable
from fastapi import FastAPI
from .utils import convert_base_model_to_nparray
import logging
from .california_data_instance import CaliforniaDataInstance

def create_app(prediction_function:Callable):
    
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
            logging.exception(e)
    
    return app