from functools import partial
from numbers import Number
from typing import Union

import numpy as np
import pandas as pd
from pint import UnitRegistry

from ..config.levels.precip import ACC_PRECIP_LEVELS, PRECIP_LEVELS
from ..core import Comparison
from ..core.binarize import (
    level_binarize,
    threshold_binarize,
)
from ..utils import result_round_digit, source_round_digit
from .statistic import (
    calc_bias_score,
    calc_binary_accuracy_ratio,
    calc_ets,
    calc_false_alarm_rate,
    calc_false_alarm_ratio,
    calc_hit_ratio,
    calc_miss_ratio,
    calc_ts,
)

UNITS = UnitRegistry()


@result_round_digit(2)
@source_round_digit(2)
def calc_precip_occur_indicators(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number = 0.0001,
    indicator: str = "accuracy_ratio",
    *args,
    **kwargs,
):
    """Calculate binarized indicators of precipitation occurrence

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.

        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

        threshold (Number): The threshold to filter observation and forecast.
                            Values less than threshold will be dropped.
                            Default to 0.0001.

        indicator (str): Indicator name, Options:
                         * accuracy_ratio: binarized accuracy ratio
                         * miss_ratio: binarized missing ratio
                         * false_alarm_ratio: binarized false alarm ratio
                         * ts: binarized ts
                         * ets: binarized ets
                         * bias_score: binarized bias score

    Returns:
        float: Binarized indicators of precipitation occurrence(%)
    """
    observation, forecast = threshold_binarize(
        observation, forecast, threshold=threshold
    )
    indicator_funcs = {
        "accuracy_ratio": calc_binary_accuracy_ratio,
        "hit_ratio": calc_hit_ratio,
        "miss_ratio": calc_miss_ratio,
        "false_alarm_ratio": calc_false_alarm_ratio,
        "false_alarm_rate": calc_false_alarm_rate,
        "ts": calc_ts,
        "ets": calc_ets,
        "bias_score": calc_bias_score,
    }
    return indicator_funcs[indicator](observation, forecast)


@result_round_digit(2)
@source_round_digit(2)
def calc_precip_interval_indicators(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    kind: str,
    lev: int,
    indicator: str = "accuracy_ratio",
    *args,
    **kwargs,
) -> float:
    """Calculate indicators of specific level of precipitation.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.

        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

        kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.

        lev (int): Level ID, Options:
                   * 1: Light rain
                   * 2: Moderate rain
                   * 3: Heavy rain
                   * 4: Violent rain
                   * 5: Severe violent rain
                   * 6: Super severe violent rain(1h don't have this)

        indicator (str): Indicator name, Options:
                         * accuracy_ratio: binarized accuracy ratio
                         * miss_ratio: binarized missing ratio
                         * false_alarm_ratio: binarized false alarm ratio
                         * ts: binarized ts
                         * ets: binarized ets
                         * bias_score: binarized bias score

    Returns:
        float: The indicators in specific level
    """
    observation, forecast = level_binarize(
        observation, forecast, PRECIP_LEVELS[kind], lev
    )
    indicator_funcs = {
        "accuracy_ratio": calc_binary_accuracy_ratio,
        "hit_ratio": calc_hit_ratio,
        "miss_ratio": calc_miss_ratio,
        "false_alarm_ratio": calc_false_alarm_ratio,
        "false_alarm_rate": calc_false_alarm_rate,
        "ts": calc_ts,
        "ets": calc_ets,
        "bias_score": calc_bias_score,
    }

    return indicator_funcs[indicator](observation, forecast)


@result_round_digit(2)
@source_round_digit(2)
def calc_precip_accumulate_indicators(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    kind: str,
    lev: int,
    indicator: str = "accuracy_ratio",
    *args,
    **kwargs,
):
    """Calculate indicators of specific level of precipitation.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.

        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

        kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.

        lev (int): Level ID, Options:
                   * 1: Light rain
                   * 2: Moderate rain
                   * 3: Heavy rain
                   * 4: Violent rain
                   * 5: Severe violent rain
                   * 6: Super severe violent rain(1h don't have this)

        indicator (str): Indicator name, Options:
                         * accuracy_ratio: binarized accuracy ratio
                         * miss_ratio: binarized missing ratio
                         * false_alarm_ratio: binarized false alarm ratio
                         * ts: binarized ts
                         * ets: binarized ets
                         * bias_score: binarized bias score

    Returns:
        float: The indicators in specific level
    """
    observation, forecast = level_binarize(
        observation, forecast, ACC_PRECIP_LEVELS[kind], lev
    )

    indicator_funcs = {
        "accuracy_ratio": calc_binary_accuracy_ratio,
        "hit_ratio": calc_hit_ratio,
        "miss_ratio": calc_miss_ratio,
        "false_alarm_ratio": calc_false_alarm_ratio,
        "false_alarm_rate": calc_false_alarm_rate,
        "ts": calc_ts,
        "ets": calc_ets,
        "bias_score": calc_bias_score,
    }

    return indicator_funcs[indicator](observation, forecast)


class PrecipitationComparison(Comparison):
    """Comparison of Precipitation"""

    def __init__(
        self,
        observation: Union[np.ndarray, list],
        forecast: Union[np.ndarray, list],
        unit: str = "mm",
        kind: str = None,
        lev: str = None,
    ):
        super().__init__(observation, forecast)
        self.kind = kind
        self.unit = unit
        self.lev = lev
        self.observation = (
            (self.observation * UNITS.parse_expression(unit)).to("mm").magnitude
        )
        self.forecast = (
            (self.forecast * UNITS.parse_expression(unit)).to("mm").magnitude
        )
        self.df = pd.DataFrame(
            {
                "observation": self.observation,
                "forecast": self.forecast,
            }
        )

        self.lev_index = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "+1",
            "+2",
            "+3",
            "+4",
            "+5",
            "+6",
        ]

    def __repr__(self):
        return super().__repr__().replace("Comparison", "PrecipitationComparison(mm)")

    def __str__(self):
        return super().__str__().replace("Comparison", "PrecipitationComparison(mm)")

    @staticmethod
    def __make_func_choice(indicator="accuracy_ratio"):
        interval_choice = dict.fromkeys(
            ["1", "2", "3", "4", "5", "6"],
            partial(calc_precip_interval_indicators, indicator=indicator),
        )
        accumulate_choice = dict.fromkeys(
            ["+1", "+2", "+3", "+4", "+5", "+6"],
            partial(calc_precip_accumulate_indicators, indicator=indicator),
        )

        func_choice = {"0": partial(calc_precip_occur_indicators, indicator=indicator)}
        func_choice.update(interval_choice)
        func_choice.update(accumulate_choice)

        return func_choice

    def calc_accuracy_ratio(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation accuracy ratio.

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: Accuracy ratio of specific kind and level(%).
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="accuracy_ratio")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_hit_ratio(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation hit ratio.

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: Hit ratio of specific kind and level(%).
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="hit_ratio")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_miss_ratio(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation missing ratio.

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain
                       * "2": Moderate rain
                       * "3": Heavy rain
                       * "4": Violent rain
                       * "5": Severe violent rain
                       * "6": Super severe violent rain(1h don't have this)
                       * "+1": Accumulated to Light rain
                       * "+2": Accumulated to Moderate rain
                       * "+3": Accumulated to Heavy rain
                       * "+4": Accumulated to Violent rain
                       * "+5": Accumulated to Severe violent rain
                       * "+6": Accumulated to Super severe violent rain(1h don't have this)
                       Defaults to "0".

        Returns:
            float: Missing ratio of specific kind and level(%)
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="miss_ratio")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_false_alarm_ratio(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation false alarm ratio.

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: False alarm ratio of specific kind and level(%)
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="false_alarm_ratio")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_false_alarm_rate(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation false alarm rate.

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: False alarm ratio of specific kind and level(%)
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="false_alarm_rate")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_ts(self, kind: str = "1h", lev: str = "0"):
        """Calculste precipitation threat score(TS).

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: Threat score(TS) of specific kind and level.
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="ts")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_ets(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation equitable threat score(ETS).

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: Equitable threat score(ETS) of specific kind and level
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="ets")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def calc_bias_score(self, kind: str = None, lev: str = "0"):
        """Calculste precipitation equitable threat score(ETS).

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.
            lev (str): Level ID, Options:
                       * "0": Rain or shine.
                       * "1": Light rain.
                       * "2": Moderate rain.
                       * "3": Heavy rain.
                       * "4": Violent rain.
                       * "5": Severe violent rain.
                       * "6": Super severe violent rain(1h don't have this).
                       * "+1": Accumulated to Light rain.
                       * "+2": Accumulated to Moderate rain.
                       * "+3": Accumulated to Heavy rain.
                       * "+4": Accumulated to Violent rain.
                       * "+5": Accumulated to Severe violent rain.
                       * "+6": Accumulated to Super severe violent rain(1h don't have this).
                       Defaults to "0".

        Returns:
            float: Equitable threat score(ETS) of specific kind and level
        """
        if int(lev) > 0:
            if not kind:
                kind = self.kind
            assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])
            if not lev:
                lev = self.lev
            assert lev and (lev in self.lev_index)

            if kind == "1h" and lev in ["6", "+6"]:
                lev = lev.replace("6", "5")

            kind = kind.lower()
        else:
            kind = None

        func_choice = self.__make_func_choice(indicator="bias_score")

        return func_choice[lev](
            self.observation, self.forecast, kind=kind, lev=int(lev)
        )

    def gather_all_indicators(self, kind: str = None):
        """Calculate all indicators.

        Args:
            kind (str): Statistic kind. Options are '1h', '3h', '12h' and '24h'.

        Returns:
            pandas.core.frame.DataFrame: All indicators.
        """
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "12h", "24h"])

        LEVS = {
            "0": ("rain_or_shine", None),
            "1": ("level", 1),
            "2": ("level", 2),
            "3": ("level", 3),
            "4": ("level", 4),
            "5": ("level", 5),
            "6": ("level", 6),
            "+1": ("accumulative", 1),
            "+2": ("accumulative", 2),
            "+3": ("accumulative", 3),
            "+4": ("accumulative", 4),
            "+5": ("accumulative", 5),
            "+6": ("accumulative", 6),
        }
        KINDS = {"1h": "01_hour", "3h": "03_hours", "24h": "24_hours"}
        funcs = {
            # tuple: (function object, unit, comment)
            "bias_score": (self.calc_bias_score, None, "BIAS score"),
            "ts": (self.calc_ts, None, None),
            "ets": (self.calc_ets, None, None),
            "false_alarm_ratio": (self.calc_false_alarm_ratio, "%", None),
            "missing_ratio": (self.calc_miss_ratio, "%", None),
            "accuracy_ratio": (self.calc_accuracy_ratio, "%", None),
        }
        result = []
        kind_desc = KINDS[kind]

        for lev, (lev_kind, lev_desc) in LEVS.items():
            for func_desc, (func, units, comment) in funcs.items():
                result.append(
                    {
                        "element": "precipitation",
                        "interval": kind_desc,
                        "kind": lev_kind,
                        "level": lev_desc,
                        "indicator": func_desc,
                        "value": func(kind=kind, lev=lev),
                        "unit": units,
                        "comment": comment,
                    }
                )

        df = pd.DataFrame(result)

        return df


if __name__ == "__main__":
    temp = PrecipitationComparison(
        np.array([1, 2, 3, 4]), np.array([1, 2, 3, 9]), unit="m"
    )
    print(temp)
    # temp.gather_all_factors().to_csv("./test.csv")
