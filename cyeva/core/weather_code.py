from typing import Union

import numpy as np
import pandas as pd
from pint import UnitRegistry

from ..core import Comparison

UNITS = UnitRegistry()


class WeatherCodeComparison(Comparison):
    def __init__(
        self,
        observation: Union[np.ndarray, list],
        forecast: Union[np.ndarray, list],
    ):
        super().__init__(observation, forecast)
        self.df = pd.DataFrame(
            {
                "observation": self.observation,
                "forecast": self.forecast,
            }
        )

    def __repr__(self):
        return super().__repr__().replace("Comparison", "WeatherCodeComparison")

    def __str__(self):
        return super().__str__().replace("Comparison", "WeatherCodeComparison")

    def gather_all_factors(self):
        funcs = {
            # tuple: (function object, comment)
            "acc": (self.calc_multiclass_accuracy_ratio, "Accuracy"),
            "hss": (self.calc_multiclass_heidke_skill_score, "HSS"),
            "hk": (self.calc_multiclass_hanssen_kuipers_score, "HK"),
        }

        result = []
        for func_desc, (func, comment) in funcs.items():
            result.append(
                {
                    "element": "weather_code",
                    "indicator": func_desc,
                    "value": func(),
                    "comment": comment,
                }
            )

        df = pd.DataFrame(result)

        return df


if __name__ == "__main__":
    pass
