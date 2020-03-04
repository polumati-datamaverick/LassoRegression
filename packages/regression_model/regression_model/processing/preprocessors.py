import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from regression_model.processing.errors import InvalidModelInputError

class CategoricalImputer(BaseEstimator, TransformerMixin):
    """ Categorical data missing value imputer"""

    def __init__(self, variables = None) -> None:

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X:pd.DataFrame, Y:pd.Series = None) -> 'CategoricalImputer':

        return self

    def transform(self, X:pd.DataFrame)-> pd.DataFrame:

        X = X.copy()
        for var in self.variables:
            X[var] = X[var].fillna('Missing')
        return(X)

class NumericalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, variables = None )-> None:

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self,  X:pd.DataFrame, Y: pd.Series = None) -> 'NumericalImputer':

        self.numerical_imputer_dict = {}
        for var in self.variables:
            self.numerical_imputer_dict[var] = X[var].mode()[0]
        return self

    def transform (self, X:pd.DataFrame) -> 'pd.DataFrame':

        X = X.copy()
        for var in self.variables:
            X[var] = X[var].fillna(self.numerical_imputer_dict[var])
        return(X)

class TemporalVariableEstimator(BaseEstimator,TransformerMixin):

    def __init__(self, variables = None, reference_variable = None)-> None:

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        self.reference_variable = reference_variable

    def fit(self, X:pd.DataFrame, Y:pd.Series=None) ->'TemporalVariableEstimator':

        return self

    def transform(self, X:pd.DataFrame) -> pd.DataFrame:

        X = X.copy()
        for var in self.variables:
            X[var] = X[var]-X[self.reference_variable]

        return X

class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, variables = None):

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
        self.non_rare_variables = {}
        self.tol = 0.05

    def fit(self,X:pd.DataFrame, Y: pd.Series = None) -> 'RareLabelCategoricalEncoder':

        X = X.copy()
        for var in self.variables:
            temp_var = X[var].value_counts()/len(X[var])
            mask = temp_var.values > self.tol
            self.non_rare_variables[var]= list(temp_var.index[mask])

        return self


    def transform(self, X:pd.DataFrame) -> pd.DataFrame:

        X = X.copy()

        for var in self.variables:
            X[var]= np.where(X[var].isin(self.non_rare_variables[var]),X[var],'Rare')
        return X


class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, variables = None):

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
        self.encoder_dict = {}

    def fit(self, X:pd.DataFrame, Y:pd.Series) -> 'CategoricalEncoder':

        X = X.copy()
        target = list(Y.index)[0]
        X[target] = Y[target]
        for var in self.variables:
            sorted_variables = list(X.groupby(var)[target].mean().sort_values().index)
            ordered_dict = {i:k for k,i in enumerate(sorted_variables,1)}
            self.encoder_dict[var]= ordered_dict
        return self

    def transform (self, X: pd.DataFrame) -> pd.DataFrame:

        X = X.copy()

        for var in self.variables:
            X[var] = X[var].map(self.encoder_dict[var])

        if X[self.variables].isnull().any(axis = None):
            null_columns = [index for index,value in X[self.variables].isnull().any().items() if value ]
            raise InvalidModelInputError(
                f'Categorical encoding has created nulls in these {null_columns} columns')

        return X

class DropUnnecessaryColumns(BaseEstimator, TransformerMixin):

    def __init__(self,  variables_to_drop= None):

        if not isinstance(variables_to_drop,list):
            self.variables = variables_to_drop
        else:
            self.variables = [variables_to_drop]

    def fit (self, X:pd.DataFrame, Y: pd.Series = None) -> 'DropUnnecessaryColumns':

        return self

    def transform(self, X:pd.DataFrame) ->'pd.DataFrame':

        X = X.copy()
        X.drop(columns = self.variables,inplace= True)

        return X
















