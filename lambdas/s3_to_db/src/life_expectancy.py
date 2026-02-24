import datetime
from io import BytesIO

import pandas as pd
import pandera.pandas as pa
from pandera.typing import DataFrame

from src.schemas.life_expectancy_schema import LifeExpectancySchema


class LifeExpectancy:
    def __init__(self, response: bytes):
        self.response = response

    def parse(self):
        with BytesIO(self.response) as bytes_file:
            excel = pd.read_excel(
                bytes_file, sheet_name="1", header=5, engine="openpyxl"
            )

        return excel

    @pa.check_types
    def clean(self, excel: pd.DataFrame) -> DataFrame[LifeExpectancySchema]:
        data = excel.rename(columns=lambda x: x.replace(" ", "_").lower().strip())
        str_cols = [
            "period",
            "country",
            "area_type",
            "area_name",
            "sex",
            "age_group",
        ]
        data[str_cols] = data[str_cols].map(lambda x: x.strip())
        data["age_group"] = data["age_group"].map(
            lambda x: x.replace(" to ", "-")
            .replace("90+", "over_90")
            .replace("<1", "00-01")
        )

        data[["period_from", "period_to"]] = data.period.str.split("to", expand=True)
        data["extraction_date"] = datetime.datetime.now()
        data.drop(["sex_code", "age_code"], axis="columns", inplace=True)

        return data
