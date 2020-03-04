from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from regression_model.processing.preprocessors import (CategoricalImputer, NumericalImputer, TemporalVariableEstimator,
RareLabelCategoricalEncoder, CategoricalEncoder, DropUnnecessaryColumns)

from regression_model.processing.features import *
from regression_model.config.config import *
# Understand importing from subfolders

import logging

_logger = logging.getLogger(__name__)



price_pipe = Pipeline(
    [
        ('categorical_imputer',
         CategoricalImputer(variables = CATEGORICAL_VARS_WITH_NA)),
        ('numerical_imputer',
         NumericalImputer(variables = NUMERICAL_VARS_WITH_NA)),
        ('temporal_variables',
         TemporalVariableEstimator(variables = TEMPORAL_VARS,
                                   reference_variable = DROP_FEATURES)),
        ('rare_categorical_encoder',
         RareLabelCategoricalEncoder(variables = CATEGORICAL_VARS)),
        ('categorical_encoder',
         CategoricalEncoder(variables = CATEGORICAL_VARS)),
        ('logtransformer',
         LogTransformer(variables = NUMERICALS_LOG_VARS)),
        ('dropunnecessarycolumns',
         DropUnnecessaryColumns(variables_to_drop = DROP_FEATURES)),
        # # ('scaler',MinMaxScaler()),
        ('lassomodel',
         Lasso(alpha = 0.005, random_state = 0 ))

    ])

