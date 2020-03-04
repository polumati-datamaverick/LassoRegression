import pandas as pd
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline


from regression_model.config.config import DATASET_DIR, TRAINED_MODEL_DIR, PIPELINE_SAVE_FILE
from regression_model  import __version__ as _version

import logging

_logger = logging.getLogger(__name__)
# Experiment this package loading with relative paths


def load_dataset(*,file_name:str)->pd.DataFrame:

    _data = pd.read_csv(f'{DATASET_DIR}/{file_name}')
    # Why do we have to use f here
    return _data


def remove_old_pipelines(*, files_to_keep) -> None:

    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in [files_to_keep, '__init__.py']:
            model_file.unlink()


def save_pipeline(*, pipeline_to_save) -> None:

    save_file_name = f'{PIPELINE_SAVE_FILE}{_version}.pkl'
    save_path = TRAINED_MODEL_DIR/save_file_name
    remove_old_pipelines(files_to_keep = save_file_name)
    joblib.dump(pipeline_to_save, save_path)
    _logger.info(f'saved pipeline:{save_file_name}')


def load_pipeline(*,file_name:str)-> Pipeline:

    file_path = TRAINED_MODEL_DIR/file_name
    trained_model = joblib.load(filename = file_path)
    return trained_model

