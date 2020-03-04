import json

from regression_model.config.config import DATASET_DIR, TESTING_DATA_FILE
from regression_model.processing.data_management import load_dataset


def test_prediction_endpoint_validation_200(flask_test_client):

    data = load_dataset(TESTING_DATA_FILE)
    data_json = data.to_json(orient= 'records')
    response = flask_test_client('/v1/prediction/regression',
                                json = json.loads(data_json))

    assert response.status_code == 200

    response_json = json.loads(response.data)

    assert len(response_json.get('predictions')) + len(response_json.get('errors')) == len(data_json)
