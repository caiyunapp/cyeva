from typing import Union

import numpy as np
import pandas as pd
from pint import UnitRegistry

from ..core import Comparison

UNITS = UnitRegistry()


class TemperatureComparison(Comparison):
    def __init__(
        self,
        observation: Union[np.ndarray, list],
        forecast: Union[np.ndarray, list],
        unit: str = "degC",
        kind: str = None,
        lev: str = None,
    ):
        super().__init__(observation, forecast)
        self.kind = kind
        self.lev = lev
        self.observation = (
            (self.observation * UNITS.parse_expression(unit)).to("degC").magnitude
        )
        self.forecast = (
            (self.forecast * UNITS.parse_expression(unit)).to("degC").magnitude
        )
        self.df = pd.DataFrame(
            {
                "observation": self.observation,
                "forecast": self.forecast,
            }
        )

    def __repr__(self):
        return super().__repr__().replace("Comparison", "TemperatureComparison(degC)")

    def __str__(self):
        return super().__str__().replace("Comparison", "TemperatureComparison(degC)")

    def gather_all_factors(self):
        LEVS = {
            1: ("limit", "within 1 degC"),
            2: ("limit", "within 2 degC"),
        }
        funcs = {
            # tuple: (function object, unit, comment)
            "rmse": (self.calc_rmse, "degC", "RMSE"),
            "mae": (self.calc_mae, "degC", "MAE"),
            "rss": (
                self.calc_rss,
                "degC ** 2",
                None,
            ),
            "chi_square": (self.calc_chi_square, "degC ** 2", "χ2"),
        }

        result = []
        for func_desc, (func, units, comment) in funcs.items():
            result.append(
                {
                    "element": "temperature",
                    "interval": np.nan,
                    "kind": np.nan,
                    "level": np.nan,
                    "indicator": func_desc,
                    "value": func(),
                    "unit": units,
                    "comment": comment,
                }
            )

        for lev, (lev_kind, lev_desc) in LEVS.items():
            result.append(
                {
                    "element": "temperature",
                    "interval": np.nan,
                    "kind": lev_kind,
                    "level": lev_desc,
                    "indicator": "accuracy_ratio",
                    "value": self.calc_diff_accuracy_ratio(limit=lev),
                    "unit": "%",
                    "comment": np.nan,
                }
            )

        df = pd.DataFrame(result)

        return df


if __name__ == "__main__":
    pass
