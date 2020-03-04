import pandas as pd
import numpy as np
from regression_model.config import config


def validate_input(inputdata: pd.DataFrame) -> pd.DataFrame:

    validated_data = inputdata.copy()
    # Validating numerical columns that do not have missing values in training
    # Should not have missing values at prediction
    if validated_data[config.NUMERICAL_NA_NOT_ALLOWED].isnull().any(axis=None):
        validated_data.dropna(axis=0, subset=config.NUMERICAL_NA_NOT_ALLOWED, inplace=True)

    # Validating categorical columns that do not have missing values in training
    # Should not have missing values at prediction
    if validated_data[config.CATEGORICAL_NA_NOT_ALLOWED].isnull().any(axis=None):
        validated_data.dropna(axis=0, subset=config.CATEGORICAL_NA_NOT_ALLOWED, inplace=True)

    # Validating numerical columns that do not have negative values in training
    # Should not have negative values at prediction

    if (validated_data[config.NUMERICALS_LOG_VARS]<=0).any(axis=None):
        for var in config.NUMERICALS_LOG_VARS:
            validated_data.loc[validated_data[var]<=0, var]=np.nan
        validated_data.dropna(axis=0, subset=config.NUMERICALS_LOG_VARS, inplace=True)

    return validated_data
