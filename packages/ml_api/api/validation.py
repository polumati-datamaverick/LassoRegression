from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json

class InvalidInputError(Exception):

    """Invalid model input"""

SYNTAX_ERROR_FIELD_MAP ={
                        '1stFlrSF':'FirstFlrSF',
                        '2ndFlrSF':'SecondFlrSF',
                        '3SsnPorch':'ThreeSsnPortch'
                        }


class HouseDataRequestSchema(Schema):
    Alley = fields.Str(allow_none=True)
    BedroomAbvGr = fields.Integer()
    BldgType = fields.Str()
    BsmtCond = fields.Str()
    BsmtExposure = fields.Str(allow_none=True)
    BsmtFinSF1 = fields.Float()
    BsmtFinSF2 = fields.Float()
    BsmtFinType1 = fields.Str()
    BsmtFinType2 = fields.Str()
    BsmtFullBath = fields.Str()
    BsmtHalfBath = fields.Str()
    BsmtQual = fields.Str(allow_none=True)
    BsmtUnfSF = fields.Float()
    CentralAir = fields.Str()
    Condition1 = fields.Str()
    Condition2 = fields.Str()
    Electrical = fields.Str()
    EnclosedPorch = fields.Integer()
    ExterCond = fields.Str()
    ExterQual = fields.Str()
    Exterior1st = fields.Str()
    Exterior2nd = fields.Str()
    Fence = fields.Str(allow_none=True)
    FireplaceQu = fields.Str(allow_none=True)
    Fireplaces = fields.Integer()
    Foundation = fields.Str()
    FullBath = fields.Str()
    Functional = fields.Str()
    GarageArea = fields.Str()
    GarageCars = fields.Str()
    GarageCond = fields.Str()
    GarageFinish = fields.Str(allow_none=True)
    GarageQual = fields.Str()
    GarageType = fields.Str(allow_none=True)
    GarageYrBlt = fields.Float()
    GrLivArea = fields.Integer()
    HalfBath = fields.Integer()
    Heating = fields.Str()
    HeatingQC = fields.Str()
    HouseStyle = fields.Str()
    Id = fields.Integer()
    KitchenAbvGr = fields.Integer()
    KitchenQual = fields.Str()
    LandContour = fields.Str()
    LandSlope = fields.Str()
    LotArea = fields.Integer()
    LotConfig = fields.Str()
    LotFrontage = fields.Float(allow_none=True)
    LotShape = fields.Str()
    LowQualFinSF = fields.Str()
    MSSubClass = fields.Integer()
    MSZoning = fields.Str()
    MasVnrArea = fields.Float()
    MasVnrType = fields.Str(allow_none=True)
    MiscFeature = fields.Str(allow_none=True)
    MiscVal = fields.Integer()
    MoSold = fields.Integer()
    Neighborhood = fields.Str()
    OpenPorchSF = fields.Integer()
    OverallCond = fields.Integer()
    OverallQual = fields.Integer()
    PavedDrive = fields.Str()
    PoolArea = fields.Integer()
    PoolQC = fields.Str(allow_none=True)
    RoofMatl = fields.Str()
    RoofStyle = fields.Str()
    SaleCondition = fields.Str()
    SaleType = fields.Str()
    ScreenPorch = fields.Integer()
    Street = fields.Str()
    TotRmsAbvGrd = fields.Integer()
    TotalBsmtSF = fields.Str()
    Utilities = fields.Str()
    WoodDeckSF = fields.Integer()
    YearBuilt = fields.Integer()
    YearRemodAdd = fields.Integer()
    YrSold = fields.Integer()
    FirstFlrSF = fields.Integer()
    SecondFlrSF = fields.Integer()
    ThreeSsnPortch = fields.Integer()


def filter_error_rows(errors:dict, input_data:t.List[dict]) -> t.List[dict]:

    filtered_data = input_data.copy()
    for index in sorted(errors.keys(), reverse=True):
        del(filtered_data[index])
    return filtered_data


def validate_inputs(input_data:t.List[dict]) -> t.List[dict]:

    schema = HouseDataRequestSchema(strict=True, many=True)
    # correcting so that field names do-not have numeric values.
    for dict in input_data:
        for key, value in SYNTAX_ERROR_FIELD_MAP.items():

            dict[value] = dict[key]
            del(dict[key])
    # we do-not have any numeric values in columns now.
    error = None
    try:
        schema.load(input_data)
    except ValidationError as err:
        error = err
    # restoring back to original columns names
    for dict in input_data:
        for key, value in SYNTAX_ERROR_FIELD_MAP.items():

            dict[key] = dict[value]
            del(dict[value])
    if error:
        validated_inputs = filter_error_rows(errors=error, input_data=input_data)
    else:
        validated_inputs = input_data

    return validated_inputs, error





















