from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction
from regression_model import __version__ as model_version
from api.validation import validate_inputs

from api.config import get_logger
from api  import __version__ as api_version

_logger = get_logger(logger_name = __name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods = ['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

@prediction_app.route('/v1/predict/regression',methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.DEBUG(f'inputs:{json_data}')

        input_data, errors = validate_inputs(json_data)
        result = make_prediction(input_data = input_data)
        _logger.DEBUG(f'output:{result}')

        predictions = result.get('prediction').tolist()
        version = result.get('version')

        return(jsonify({'predictions':predictions,
                        'version':version,
                        'errors':errors}))



@prediction_app.route('/version', methods = ['GET'])
def version():

    if request.method == 'GET':

        return(jsonify({'modelversion':model_version,
                        'apiversion':api_version}))

