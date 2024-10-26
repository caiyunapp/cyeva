from collections import Counter
from functools import partial
from numbers import Number
from typing import List, Union

import numpy as np
import pandas as pd
from pint import Quantity, UnitRegistry

from ..config.directions import (
    DIRECTION8_CENTER_ANGLE,
    DIRECTION16_CENTER_ANGLE,
)
from ..config.levels.wind import (
    GENERAL_WIND_SCALES,
)
from ..core import Comparison
from ..utils import (
    assert_length,
    convert_to_ndarray,
    drop_nan,
    fix_zero_division,
    result_round_digit,
    source_round_digit,
)

UNITS = UnitRegistry()


def get_angle_relative_positions(
    angle1: Union[Number, np.ndarray], angle2: Union[Number, np.ndarray]
) -> Union[Number, np.ndarray]:
    """To identify the relative positions (less or greater) of angles

    Args:
        angle1 (Union[Number, np.ndarray]): One angle number or array in degree.
        angle2 (Union[Number, np.ndarray]): Another angle number or array in degree

    Returns:
        Union[Number, np.ndarray]: The number or array to indicate the relative postisons,
        -1 stands for first one less than second one, 0 stands for equal, 1 stands for first
        one greater than second one.
    """
    if isinstance(angle1, Number) and isinstance(angle2, Number):
        if angle1 == 180 or angle2 == 180:
            defl = 90
        else:
            defl = 180

        ag1 = (angle1 + defl) % 360
        ag2 = (angle2 + defl) % 360

        if ag1 - ag2 < 0:
            return -1
        elif ag1 - ag2 > 0:
            return 1
        else:
            return 0
    elif isinstance(angle1, np.ndarray) or isinstance(angle2, np.ndarray):
        if (
            (isinstance(angle1, np.ndarray) and 180 in angle1)
            or (isinstance(angle2, np.ndarray) and 180 in angle2)
            or (isinstance(angle1, Number) and angle1 == 180)
            or (isinstance(angle2, Number) and angle2 == 180)
        ):
            defl = 90
        else:
            defl = 180

        ag1 = (angle1 + defl) % 360
        ag2 = (angle2 + defl) % 360

        diff = ag1 - ag2
        relation_position_array = np.full(diff.shape, np.nan)

        relation_position_array[diff < 0] = -1
        relation_position_array[diff == 0] = 0
        relation_position_array[diff > 0] = 1

        return relation_position_array.astype(int)
    else:
        raise TypeError("parameter of 'angle1' and 'angle2' types are not supported.")


def get_least_angle_deflection(
    angle1: Union[Number, np.ndarray],
    angle2: Union[Number, np.ndarray],
    absolute: bool = True,
) -> Union[Number, np.ndarray]:
    """Calculate the least angle deflection between two angles.

    Args:
        angle1 (Union[Number, np.ndarray]): One angle(degree).
        angle2 (Union[Number, np.ndarray]): Another angle(degree).
        absolute (bool, optional): Whether to return the absolute value. Defaults to True.

    Returns:
        Union[Number, np.ndarray]: The least deflection between two angles.
    """

    if isinstance(angle1, Quantity):
        angle1 = angle1.magnitude

    if isinstance(angle2, Quantity):
        angle2 = angle2.magnitude

    diff = (angle2 - angle1 + 180) % 360 - 180
    if absolute:
        return np.abs(diff)
    else:
        return diff


def identify_direction(
    angle: Union[Number, np.ndarray], dnum: int = 8
) -> Union[int, np.ndarray]:
    """Identify 8 cardinal directions by angle.

    Args:
        angle (Number): The wind direction in degree.
        dnum (int): The wind directions number.

    Returns:
        Union[int, np.ndarray]: Direction ID of the cardinal direction.
    """
    if isinstance(angle, List):
        angle = np.array(angle)

    if isinstance(angle, Quantity):
        angle_magnitude = angle.magnitude

    if isinstance(angle, np.ndarray) or isinstance(angle, Number):
        angle_magnitude = angle

    if dnum == 8:
        DIRECTION_CENTER_ANGLE = DIRECTION8_CENTER_ANGLE
        threshold = 22.5
    elif dnum == 16:
        DIRECTION_CENTER_ANGLE = DIRECTION16_CENTER_ANGLE
        threshold = 11.25

    angle_magnitude %= 360

    if isinstance(angle, Number):
        for dir_id, center_angle in DIRECTION_CENTER_ANGLE.items():
            least_angle_deflection = get_least_angle_deflection(
                angle_magnitude, center_angle
            )
            if get_least_angle_deflection(angle_magnitude, center_angle) < threshold:
                break
            elif least_angle_deflection == threshold:
                rp = get_angle_relative_positions(angle_magnitude, center_angle)
                if rp > 0:
                    break

        return dir_id

    elif isinstance(angle, np.ndarray) or isinstance(angle, Quantity):
        dir_ids = np.full_like(angle_magnitude, -1)
        for dir_id, center_angle in DIRECTION_CENTER_ANGLE.items():
            least_angle_defl = get_least_angle_deflection(angle_magnitude, center_angle)
            dir_ids[least_angle_defl < threshold] = dir_id

            rp = get_angle_relative_positions(angle_magnitude, center_angle)

            dir_ids[(least_angle_defl == threshold) & (rp < 0)] = dir_id - 1
            dir_ids[(least_angle_defl == threshold) & (rp > 0)] = dir_id

            dir_ids[dir_ids < min(DIRECTION_CENTER_ANGLE)] = 7

        return dir_ids


def identify_wind_scale(speed: Union[Number, np.ndarray]) -> Union[int, np.ndarray]:
    """Identify wind scale by speed.

    Args:
        speed (Union[Number, np.ndarray]): Wind speed in m/s.

    Returns:
        Union[int, np.ndarray]: Wind scale.
    """
    if isinstance(speed, list):
        speed = np.array(speed)
    if isinstance(speed, np.ndarray) or isinstance(speed, Quantity):
        spd_levs = np.full_like(speed, np.nan)

    try:
        speed_magnitude = speed.magnitude
    except AttributeError:
        speed_magnitude = speed

    for lev, attr in GENERAL_WIND_SCALES.items():
        minimum = attr["min"]
        maximum = attr["max"]
        if isinstance(speed, Number):
            if lev == 0:
                if minimum <= speed <= maximum:
                    return lev
            else:
                if minimum < speed <= maximum:
                    return lev
        elif isinstance(speed, np.ndarray) or isinstance(speed, Quantity):
            if lev == 0:
                spd_levs[
                    (speed_magnitude >= minimum) & (speed_magnitude <= maximum)
                ] = lev
            else:
                spd_levs[(speed_magnitude > minimum) & (speed_magnitude <= maximum)] = (
                    lev
                )

    return spd_levs


def get_least_lev_diff(
    lev1: Union[int, np.ndarray],
    lev2: Union[int, np.ndarray],
) -> int:
    """Calculate least level difference.

    Args:
        lev1 (int): One level value.
        lev2 (int): Another level value.

    Returns:
        int: Least level difference.
    """
    return np.abs(lev1 - lev2)


@convert_to_ndarray
def get_least_dir_deflection(
    dir1: Union[int, np.ndarray], dir2: Union[int, np.ndarray], circle_num: int = 8
) -> Union[int, np.ndarray]:
    """Get least deflection from two directions.

    Args:
        dir1 (Union[int, np.ndarray]): One direction number(0-7 if circle_num is 8)
        dir2 (Union[int, np.ndarray]): Another direction number(0-7 if circle_num is 8)
        circle_num (int, optional): Circulation knot num. Defaults to 8.

    Returns:
        Union[int, np.ndarray]: The least deflection of directions.
    """
    if isinstance(dir1, Number) and isinstance(dir2, Number):
        deflection1 = abs(dir1 - dir2)
        deflection2 = circle_num - abs(dir1 - dir2)

        return int(deflection1) if deflection1 < deflection2 else int(deflection2)
    else:
        deflection1 = np.abs(dir1 - dir2)
        deflection2 = circle_num - np.abs(dir1 - dir2)

        index1 = np.where(deflection1 <= deflection2)
        index2 = np.where(deflection2 <= deflection1)

        deflection = np.full_like(deflection1, 0)

        deflection[index1] = deflection1[index1]
        deflection[index2] = deflection2[index2]

        return deflection


@assert_length
@source_round_digit(series_num=2)
@convert_to_ndarray
@drop_nan
def filter_wind_scales(
    observation,
    forecast,
    scale_min=None,
    scale_max=None,
    mode="and",
    return_index=False,
    *args,
    **kwargs,
):
    """Filter wind by wind scales.

    Args:
        observation (list | ndarray): Observation wind speed array.
        forecast (list | ndarray): Forecast wind speed array.
        scale_min (float | int, optional): The minimum wind scale to filter,
            if set to None it will be the minimum scale in default scales.
            Defaults to None.
        scale_max (float | int, optional): The maximum wind scale to filter,
            if set to None it will be the maximum scale in default scales.
            Defaults to None.
        mode (str, optional): Filter logic(and/or). Defaults to 'and'.
        return_index (boolean, optional): Whether return index, if it is False
            return values, otherwise return array's index. Defaults to False.

    Returns:
        tuple: (Observation wind speed array, Forecast wind speed array)
    """

    if not scale_min:
        scale_min = float(sorted(GENERAL_WIND_SCALES.keys())[0])
    if not scale_max:
        scale_max = float(sorted(GENERAL_WIND_SCALES.keys())[-1])

    obs_lev = identify_wind_scale(observation)
    fct_lev = identify_wind_scale(forecast)
    assert (obs_lev == obs_lev).all() and (fct_lev == fct_lev).all()

    if mode == "and":
        bools = ((obs_lev >= scale_min) & (obs_lev <= scale_max)) & (
            (fct_lev >= scale_min) & (fct_lev <= scale_max)
        )
        index = np.where(bools == True)  # noqa
    elif mode == "or":
        bools = ((obs_lev >= scale_min) & (obs_lev <= scale_max)) | (
            (fct_lev >= scale_min) & (fct_lev <= scale_max)
        )
        index = np.where(bools == True)  # noqa

    filtered_obs = observation[index]
    filtered_fct = forecast[index]

    if return_index:
        return index
    else:
        return filtered_obs, filtered_fct


class WindComparison(Comparison):
    # FIXME: 需要加最小扇形逻辑，Issue：#33
    def __init__(
        self,
        obs_spd: Union[np.ndarray, list] = None,
        fct_spd: Union[np.ndarray, list] = None,
        obs_dir: Union[np.ndarray, list] = None,
        fct_dir: Union[np.ndarray, list] = None,
        unit_spd: str = "m/s",
        unit_dir: str = "degree",
    ):
        if obs_spd is not None:
            self.obs_spd = (
                (obs_spd * UNITS.parse_expression(unit_spd)).to("m/s").magnitude
            )
        if obs_dir is not None:
            self.obs_dir = (
                (obs_dir * UNITS.parse_expression(unit_dir)).to("degree").magnitude
            )
        if fct_spd is not None:
            self.fct_spd = (
                (fct_spd * UNITS.parse_expression(unit_spd)).to("m/s").magnitude
            )
        if fct_dir is not None:
            self.fct_dir = (
                (fct_dir * UNITS.parse_expression(unit_dir)).to("degree").magnitude
            )

        self.df = pd.DataFrame(
            {
                "observation_speed": obs_spd,
                "forecast_speed": fct_spd,
                "observation_direction": obs_dir,
                "forecast_direction": fct_dir,
            }
        )

    def __repr__(self):
        text = "\n".join(["<Object:WindComparison>", "data:", self.df.__str__()])
        return text

    def __str__(self):
        text = "\n".join(["<Object:WindComparison>", "data:", self.df.__str__()])
        return text

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_rmse(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        kind: str = "speed",
        *args,
        **kwargs,
    ):
        "Root Mean Square Error"
        if observation is None:
            if kind == "speed":
                observation = self.obs_spd
            elif kind == "direction":
                observation = self.obs_dir
        if forecast is None:
            if kind == "speed":
                forecast = self.fct_spd
            elif kind == "direction":
                forecast = self.fct_dir

        if kind == "direction":
            forecast = get_least_angle_deflection(observation, forecast, absolute=False)
            observation = np.zeros_like(forecast)

        return super().calc_rmse(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_mae(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        kind: str = "speed",
        *args,
        **kwargs,
    ):
        """Mean Absolute Error"""
        if observation is None:
            if kind == "speed":
                observation = self.obs_spd
            elif kind == "direction":
                observation = self.obs_dir
        if forecast is None:
            if kind == "speed":
                forecast = self.fct_spd
            elif kind == "direction":
                forecast = self.fct_dir

        if kind == "direction":
            forecast = forecast = get_least_angle_deflection(
                observation, forecast, absolute=False
            )
            observation = np.zeros_like(forecast)

        return super().calc_mae(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_chi_square(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        kind: str = "speed",
        *args,
        **kwargs,
    ):
        """χ2"""
        if observation is None:
            if kind == "speed":
                observation = self.obs_spd
            elif kind == "direction":
                observation = self.obs_dir
        if forecast is None:
            if kind == "speed":
                forecast = self.fct_spd
            elif kind == "direction":
                forecast = self.fct_dir

        if kind == "direction":
            forecast = forecast = get_least_angle_deflection(
                observation, forecast, absolute=False
            )
            observation = np.zeros_like(forecast)

        return super().calc_chi_square(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_rss(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        kind: str = "speed",
        *args,
        **kwargs,
    ):
        """Residual Sum of Square"""
        if observation is None:
            if kind == "speed":
                observation = self.obs_spd
            elif kind == "direction":
                observation = self.obs_dir
        if forecast is None:
            if kind == "speed":
                forecast = self.fct_spd
            elif kind == "direction":
                forecast = self.fct_dir

        if kind == "direction":
            forecast = forecast = get_least_angle_deflection(
                observation, forecast, absolute=False
            )
            observation = np.zeros_like(forecast)

        return super().calc_rss(observation, forecast)

    def calc_linregress_args(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        *args,
        **kwargs,
    ):
        """linregress args, only for wind speed
        (slope, intercept, rvalue, pvalue, stderr)
        """
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        return super().calc_linregress_args(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_bias(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        kind: str = "speed",
        threshold: Number = 0,
        *args,
        **kwargs,
    ):
        """BIAS score"""
        if observation is None:
            if kind == "speed":
                observation = self.obs_spd
            elif kind == "direction":
                observation = self.obs_dir
        if forecast is None:
            if kind == "speed":
                forecast = self.fct_spd
            elif kind == "direction":
                forecast = self.fct_dir

        if kind == "direction":
            forecast = forecast = get_least_angle_deflection(
                observation, forecast, absolute=True
            )
            observation = np.zeros_like(forecast)

        return super().calc_bias(observation, forecast, threshold=threshold)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_binary_accuracy_ratio(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        threshold: Number = 0,
        *args,
        **kwargs,
    ) -> float:
        """Binary accuracy ratio, only for wind speed

        Args:
            threshold (Number, optional): The threshold to binarize array.
                                          Defaults to 0.

        Returns:
            float: The accuracy ratio.
        """
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        return super().calc_binary_accuracy_ratio(
            observation, forecast, threshold=threshold
        )

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_diff_accuracy_ratio(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        kind: str = "speed",
        limit: Number = 1,
        *args,
        **kwargs,
    ) -> float:
        """
        Calculate the accuracy ratio that
        two array's difference within a limit scope.

        Args:
            limit (Number, optional): The limit of difference.
                                      Defaults to 1.

        Returns:
            float: The accuracy ratio.
        """
        if observation is None:
            if kind == "speed":
                observation = self.obs_spd
            elif kind == "direction":
                observation = self.obs_dir
        if forecast is None:
            if kind == "speed":
                forecast = self.fct_spd
            elif kind == "direction":
                forecast = self.fct_dir

        if kind == "direction":
            forecast = forecast = get_least_angle_deflection(
                observation, forecast, absolute=False
            )
            observation = np.zeros_like(forecast)

        return super().calc_diff_accuracy_ratio(observation, forecast, limit=limit)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_dir_accuracy_ratio(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        mode="degree",
        threshold=22.5,
        *args,
        **kwargs,
    ) -> float:
        """Calculate wind direction accuracy ratio.

        Args:
            mode (str, optional): Wind direction mode. Options as follow:
                                  * degree: Calculate wind direction accuracy ratio from degree way.
                                  * drange8: Calculate wind direction accuracy ratio from 8 cardinal directions way.
                                  * drange16 Calculate wind direction accuracy ratio from 16 cardinal directions way.
                                  Defaults to "degree".
            threshold (float, optional): The degree threshold to check if wind
                                         is accurate, only useful when
                                         mode=="degree".
                                         Defaults to 22.5.

        Returns:
            float: The accuracy ratio (%).
        """
        if observation is None:
            observation = self.obs_dir
        if forecast is None:
            forecast = self.fct_dir
        if mode == "degree":
            angle_deflection = get_least_angle_deflection(observation, forecast)

            count_series = np.full_like(angle_deflection, 0).astype(float)
            count_series[angle_deflection <= threshold] = 1

            try:
                return np.sum(count_series) / len(count_series) * 100
            except TypeError:
                return np.sum(count_series) * 100

        elif mode == "drange8":
            obs_d8 = identify_direction(observation)
            fct_d8 = identify_direction(forecast)

            cross = obs_d8 == fct_d8
            try:
                total = len(cross)
            except TypeError:
                cross = [cross]
                total = 1
            counter = Counter(cross)
            correct = counter[True]

            return correct / total * 100

        elif mode == "drange16":
            obs_d16 = identify_direction(observation, dnum=16)
            fct_d16 = identify_direction(forecast, dnum=16)

            cross = obs_d16 == fct_d16
            try:
                total = len(cross)
            except TypeError:
                cross = [cross]
                total = 1
            counter = Counter(cross)
            correct = counter[True]

            return correct / total * 100

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_dir_score(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        dnum: int = 8,
        *args,
        **kwargs,
    ) -> float:
        """Calculate wind direction score.

        Args:
            observation (Union[Number, np.ndarray]): Observation wind direction value or ndarray in degree.
            forecast (Union[Number, np.ndarray]): Forecast wind direction value or ndarray in degree.
            dnum (int, optional): The wind directions number. Defaults to 8.

        Returns:
            float: The wind direction score
        """
        if observation is None:
            observation = self.obs_dir
        if forecast is None:
            forecast = self.fct_dir

        if dnum == 8:
            obs_d8 = identify_direction(observation)
            fct_d8 = identify_direction(forecast)

            dir_deflection = get_least_lev_diff(obs_d8, fct_d8)

            score_series = np.full_like(dir_deflection, 0).astype(float)
            score_series[np.isclose(dir_deflection, 1)] = 0.6
            score_series[dir_deflection < 1] = 1

        elif dnum == 16:
            obs_d16 = identify_direction(observation, dnum=16)
            fct_d16 = identify_direction(forecast, dnum=16)

            dir_deflection = get_least_lev_diff(obs_d16, fct_d16)

            score_series = np.full_like(dir_deflection, 0).astype(float)
            score_series[np.isclose(dir_deflection, 2)] = 0.6
            score_series[np.isclose(dir_deflection, 1)] = 0.8
            score_series[dir_deflection < 1] = 1

        try:
            return np.sum(score_series) / len(score_series)
        except TypeError:
            return np.sum(score_series)

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_wind_scale_accuracy_ratio(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        scale_min=None,
        scale_max=None,
        mode="strict",
    ):
        """Calculate wind scale accuracy ratio

        Args:
            observation (Union[Number, np.ndarray]): Observation wind speed value or ndarray in m/s.
            forecast (Union[Number, np.ndarray]): Forecast wind speed value or ndarray in m/s.
            scale_min (Number): The min wind scale to remain after filter.
            scale_max (Number): The max wind scale to remain after filter.
            mode (str): The mode to filter, Options are 'strict' and 'loose'.
                        If 'strict' it will use 'and' logic when filter observation and forecast.
                        If 'loose' it will use 'or' logic.

        Returns:
            float: Wind scale accuracy ratio (%)
        """
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        if mode == "strict":
            observation, forecast = filter_wind_scales(
                observation, forecast, scale_min=scale_min, scale_max=scale_max
            )
        elif mode == "loose":
            observation, forecast = filter_wind_scales(
                observation,
                forecast,
                scale_min=scale_min,
                scale_max=scale_max,
                mode="or",
            )

        obs_lev = identify_wind_scale(observation)
        fct_lev = identify_wind_scale(forecast)

        hits = np.count_nonzero(obs_lev == fct_lev)
        try:
            total = len(observation)
        except TypeError:
            total = 1

        return hits / total * 100

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_speed_accuracy_ratio(
        self,
        observation: Union[Number, np.ndarray] = None,
        forecast: Union[Number, np.ndarray] = None,
        limit: Number = 2,
    ):
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        return self.calc_diff_accuracy_ratio(
            observation, forecast, kind="speed", limit=limit
        )

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_wind_scale_stronger_ratio(
        self,
        observation: Union[Number, np.ndarray] = None,
        forecast: Union[Number, np.ndarray] = None,
    ):
        """Calculate wind scale stronger ratio.

        Args:
            observation (Union[Number, np.ndarray]): Observation wind speed value or ndarray in m/s.
            forecast (Union[Number, np.ndarray]): Forecast wind speed value or ndarray in m/s.

        Returns:
            float: Wind scale stronger ratio(%).
        """
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        obs_lev = identify_wind_scale(observation)
        fct_lev = identify_wind_scale(forecast)

        lev_defls = fct_lev - obs_lev

        stronger_series = np.full_like(lev_defls, False)
        stronger_series[lev_defls > 0] = True

        return Counter(stronger_series)[True] / len(stronger_series) * 100

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_wind_scale_weaker_ratio(
        self,
        observation: Union[Number, np.ndarray] = None,
        forecast: Union[Number, np.ndarray] = None,
    ):
        """Calculate wind scale weaker ratio.

        Args:
            observation (Union[Number, np.ndarray]): Observation wind speed value or ndarray in m/s.
            forecast (Union[Number, np.ndarray]): Forecast wind speed value or ndarray in m/s.

        Returns:
            float: Wind scale weaker ratio(%).
        """
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        obs_lev = identify_wind_scale(observation)
        fct_lev = identify_wind_scale(forecast)

        lev_defls = fct_lev - obs_lev

        stronger_series = np.full_like(lev_defls, False)
        stronger_series[lev_defls < 0] = True

        return Counter(stronger_series)[True] / len(stronger_series) * 100

    @result_round_digit(4)
    @source_round_digit()
    @fix_zero_division
    def calc_speed_score(
        self,
        observation: Union[Number, np.ndarray] = None,
        forecast: Union[Number, np.ndarray] = None,
    ):
        """Calculate wind speed score.

        Args:
            observation (Union[Number, np.ndarray]): Observation wind speed value or ndarray in m/s.
            forecast (Union[Number, np.ndarray]): Forecast wind speed value or ndarray in m/s.

        Returns:
            float: Wind speed score.
        """
        if observation is None:
            observation = self.obs_spd
        if forecast is None:
            forecast = self.fct_spd

        obs_lev = identify_wind_scale(observation)
        fct_lev = identify_wind_scale(forecast)

        lev_defls = get_least_lev_diff(obs_lev, fct_lev)
        score_series = np.full_like(lev_defls, 0).astype(float)

        score_series[np.isclose(lev_defls, 0)] = 1
        score_series[np.isclose(lev_defls, 1)] = 0.6
        score_series[np.isclose(lev_defls, 2)] = 0.4

        return sum(score_series) / len(score_series)

    def gather_all_factors(self):
        funcs = {
            # tuple: (function object, unit, comment)
            "direction_accuracy_ratio": (self.calc_dir_accuracy_ratio, "%", None),
            "direction_accuracy_ratio_8": (
                partial(self.calc_dir_accuracy_ratio, mode="drange8"),
                "%",
                None,
            ),
            "direction_score": (self.calc_dir_score, None, None),
            "speed_accuracy_ratio": (
                self.calc_speed_accuracy_ratio,
                "%",
                "≤2m/s",
            ),
            "wind_scale_stronger_ratio": (
                self.calc_wind_scale_stronger_ratio,
                "%",
                None,
            ),
            "wind_scale_weaker_ratio": (self.calc_wind_scale_weaker_ratio, "%", None),
            "speed_mae": (self.calc_mae, "m/s", None),
            "speed_score": (self.calc_speed_score, None, None),
            "rmse": (self.calc_rmse, "m/s", "RMSE"),
            "mae": (self.calc_mae, "m/s", "MAE"),
            "rss": (self.calc_rss, "(m/s) ** 2", None),
            "chi_square": (self.calc_chi_square, "(m/s) ** 2", None),
        }

        result = []

        for func_desc, (func, units, comment) in funcs.items():
            result.append(
                {
                    "element": "wind",
                    "interval": np.nan,
                    "kind": np.nan,
                    "level": np.nan,
                    "indicator": func_desc,
                    "value": func(),
                    "unit": units,
                    "comment": comment,
                }
            )

        slope, intercept, *_ = self.calc_linregress_args()
        if intercept > 0:
            formula = f"y = {slope} * x + {abs(intercept)}"
        else:
            formula = f"y = {slope} * x - {abs(intercept)}"
        result.append(
            {
                "element": "wind",
                "interval": np.nan,
                "kind": np.nan,
                "level": np.nan,
                "indicator": "equation_of_linear_regression",
                "value": formula,
                "unit": None,
                "comment": None,
            }
        )

        df = pd.DataFrame(result)

        return df


if __name__ == "__main__":
    pass
