import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from regression_model.processing.errors import InvalidModelInputError


class LogTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, variables = None):

        if not isinstance(variables,list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, x: pd.DataFrame, y: pd.DataFrame = None) -> 'LogTransformer':

        return self

    def transform(self, x: pd.DataFrame) -> 'pd.DataFrame':
        x = x.copy()

        temp = x[self.variables]<0

        if temp.any(axis=None):
            neg_columns = [column for column in x[self.variables]
                           if x[column].min() <= 0]
            raise InvalidModelInputError(
                    f'Log transformation cannot happen'
                    f'in these columns{neg_columns} because they have negative values')

        for var in self.variables:
            x[var] = np.log(x[var])
        return x
