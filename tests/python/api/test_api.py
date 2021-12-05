from python.api import api
from python.model.model_utils import create_and_fit_default_model
from fastapi.testclient import TestClient

model = create_and_fit_default_model()

client = TestClient(
    api.create_app(model.predict))

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_predict_california_data_instance():
    input = {
        "MedInc": 0.1,
        "HouseAge": 0.1,
        "AveRooms": 0.1,
        "AveBedrms": 0.1,
        "Population": 0.1,
        "AveOccup": 0.1,
        "Latitude": 0.1,
        "Longitude": 0.1
        }

    expected_response = {
        "prediction": -36.929494799979395
    }

    response = client.post(
        "/predict_california_data_instance",
        json = input
    )
    assert response.json() == expected_response

# test improper body (1 variable off)
def test_predict_improper_california_data_instance():
    input = {
        "MedInc": 0.1,
        "HouseAge": 0.1,
        "AveRooms": 0.1,
        "AveBedrms": 0.1,
        "Population": 0.1,
        "AveOccup": 0.1,
        "Latitude": 0.1
        }

    expected_response = 422

    response = client.post(
        "/predict_california_data_instance",
        json = input
    )
    assert response.status_code == expected_response