import numpy as np
from sklearn.model_selection import train_test_split


from regression_model.pipeline import price_pipe
from regression_model.config.config import TRAINING_DATA_FILE, FEATURES, TARGET
from regression_model import __version__ as _version
import logging
from regression_model.processing.data_management import load_dataset, save_pipeline


_logger = logging.getLogger(__name__)


def run_training() :

    data = load_dataset(file_name= TRAINING_DATA_FILE)

    X_train, X_test , Y_train, Y_test = train_test_split(data[FEATURES],data[TARGET],
                                                        test_size = 0.2, random_state=0 )
    Y_train = np.log(Y_train)
    Y_test  = np.log(Y_test)
    price_pipe.fit(X_train[FEATURES], Y_train)
    _logger.info(f"saving model version:{_version}")
    save_pipeline(pipeline_to_save=price_pipe)


if __name__ == '__main__':
    run_training()
