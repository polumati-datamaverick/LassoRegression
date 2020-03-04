import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset
from regression_model import config


def test_make_single_prediction():

    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    single_test_json = test_data[0:1]
    output = make_prediction(input_data=single_test_json)

    assert output is not None
    assert isinstance(output.get('prediction'), float)
    assert math.ceil(output.get('prediction')) == 112476


def test_make_multiple_predictions():

    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    original_data_length = len(test_data)
    multiple_test_json = test_data
    output = make_prediction(input_data=multiple_test_json)

    assert output is not None
    assert len(output.get('prediction')) == 1451
    assert len(output.get('prediction')) == original_data_length








