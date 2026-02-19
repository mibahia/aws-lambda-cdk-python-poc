import pandera.pandas as pa
from pandera.typing.pandas import DateTime, Series


class LifeExpectancy(pa.DataFrameModel):
    period: Series[str] = pa.Field(nullable=False)
    country: Series[str] = pa.Field(nullable=False)
    area_type: Series[str] = pa.Field(nullable=False)
    area_code: Series[str] = pa.Field(str_length={"exact_value": 9}, nullable=False)
    area_name: Series[str] = pa.Field(nullable=False)
    sex: Series[str] = pa.Field(nullable=False)
    age_group: Series[str] = pa.Field(nullable=False)
    life_expectancy: Series[float] = pa.Field(nullable=False)
    lower_confidence_interval: Series[float] = pa.Field(nullable=False)
    upper_confidence_interval: Series[float] = pa.Field(nullable=False)
    period_from: Series[str] = pa.Field(nullable=False)
    period_to: Series[str] = pa.Field(nullable=False)
    extraction_date: Series[DateTime] = pa.Field(nullable=False)
