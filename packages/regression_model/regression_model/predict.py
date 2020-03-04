import pandas as pd
import numpy as np

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config
from regression_model.processing.validation import validate_input
from regression_model import __version__  as _version

import logging

_logger = logging.getLogger(__name__)

pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
_price_pipe = load_pipeline(file_name = pipeline_file_name)

def make_prediction(*, input_data) ->dict:
    data = pd.DataFrame(input_data)
    data = validate_input(inputdata=data)
    prediction = _price_pipe.predict(data[config.FEATURES])
    output = np.exp(prediction)
    result = {'predictions':output, 'version':_version }

    _logger.info(f'making prediction with model version {_version}'
                 f'Inputs:{data}'
                 f'Prediction:{prediction}')
    return result


