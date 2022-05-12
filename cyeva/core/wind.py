from typing import List, Union
from numbers import Number
from collections import Counter

import numpy as np
import pandas as pd

from cyeva.utils import (
    convert_to_ndarray,
    fix_zero_division,
    result_round_digit,
    source_round_digit,
    assert_length,
    drop_nan,
)
from cyeva.config.directions.wind import (
    DIRECTION8_CENTER_ANGLE,
    DIRECTION16_CENTER_ANGLE,
)
from cyeva.config.levels.wind import (
    GENERAL_WIND_SPEED_LEVELS,
)
from .statistic import (
    # calc_differ_accuracy_rate,
    calc_mae,
    calc_rmse,
    calc_rss,
    calc_chi_square,
    calc_linregress,
)
from .binarize import threshold_binarize
from cyeva.core import Comparison


# @np.vectorize
def get_least_angle_deflection(
    angle1: Union[Number, np.ndarray], angle2: Union[Number, np.ndarray]
) -> Union[Number, np.ndarray]:
    """Calculate the least angle deflection between two angles.

    Args:
        angle1 (Union[Number, np.ndarray]): One angle(degree).
        angle2 (Union[Number, np.ndarray]): Another angle(degree).

    Returns:
        Union[Number, np.ndarray]: The least deflection between two angles.
    """

    angle1 %= 360
    angle2 %= 360

    deflection1 = abs(angle1 - angle2)
    deflection2 = 360 - abs(angle1 - angle2)

    if isinstance(angle1, Number) and isinstance(angle2, Number):
        return deflection1 if deflection1 < deflection2 else deflection2
    else:
        index1 = np.where(deflection1 <= deflection2)
        index2 = np.where(deflection2 <= deflection1)

        deflection = np.full_like(deflection1, 0)

        deflection[index1] = deflection1[index1]
        deflection[index2] = deflection2[index2]

        return deflection


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

    if dnum == 8:
        DIRECTION_CENTER_ANGLE = DIRECTION8_CENTER_ANGLE
        threshold = 22.5
    elif dnum == 16:
        DIRECTION_CENTER_ANGLE = DIRECTION16_CENTER_ANGLE
        threshold = 11.25

    angle %= 360

    if isinstance(angle, Number):
        for dir_id, center_angle in DIRECTION_CENTER_ANGLE.items():
            if get_least_angle_deflection(angle, center_angle) <= threshold:
                break

        return dir_id

    elif isinstance(angle, np.ndarray):
        dir_ids = np.full_like(angle, -1)
        for dir_id, center_angle in DIRECTION_CENTER_ANGLE.items():
            least_angle_defl = get_least_angle_deflection(angle, center_angle)
            dir_ids[least_angle_defl <= threshold] = dir_id

        return dir_ids


def identify_speed_level(speed: Union[Number, np.ndarray]) -> Union[int, np.ndarray]:
    """Identify wind level by speed.

    Args:
        speed (Union[Number, np.ndarray]): Wind speed in m/s.

    Returns:
        Union[int, np.ndarray]: Wind level.
    """
    if isinstance(speed, np.ndarray):
        spd_levs = np.full_like(speed, np.nan)
    for lev, attr in GENERAL_WIND_SPEED_LEVELS.items():
        minimum = attr["min"]
        maximum = attr["max"]
        if isinstance(speed, Number):
            if lev == 0:
                if minimum <= speed <= maximum:
                    return lev
            else:
                if minimum < speed <= maximum:
                    return lev
        elif isinstance(speed, np.ndarray):
            if lev == 0:
                spd_levs[(speed >= minimum) & (speed <= maximum)] = lev
            else:
                spd_levs[(speed > minimum) & (speed <= maximum)] = lev

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
@result_round_digit(4)
@fix_zero_division
def calc_wind_dir_score(
    observation: Union[Number, np.ndarray],
    forecast: Union[Number, np.ndarray],
    dnum: int = 8,
) -> float:
    """Calculate wind direction score.

    Args:
        observation (Union[Number, np.ndarray]): Observation wind direction value or ndarray in degree.
        forecast (Union[Number, np.ndarray]): Forecast wind direction value or ndarray in degree.
        dnum (int, optional): The wind directions number. Defaults to 8.

    Returns:
        float: The wind direction score
    """
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
@assert_length
@fix_zero_division
def calc_wind_dir_accuracy_ratio(
    observation: Union[Number, np.ndarray],
    forecast: Union[Number, np.ndarray],
    mode="degree",
    threshold=22.5,
) -> float:
    """Calculate wind direction accuracy ratio.

    Args:
        observation (Union[Number, np.ndarray]): Observation wind direction value or ndarray in degree.
        forecast (Union[Number, np.ndarray]): Forecast wind direction value or ndarray in degree.
        mode (str, optional): Wind direction mode. Options as follow:
                              * degree: Calculate wind direction accuracy ratio from degree way.
                              * drange8: Calculate wind direction accuracy ratio from 8 cardinal directions way.
                              * drange16 Calculate wind direction accuracy ratio from 16 cardinal directions way.
                              Defaults to "degree".
        threshold (float, optional): The degree threshold to check if wind is accurate, only useful when mode=='degree'.
                                     Defaults to 22.5.

    Returns:
        float: The accuracy ratio (%).
    """
    try:
        couples = zip(observation, forecast)
    except TypeError:
        couples = zip([observation], [forecast])

    if mode == "degree":
        angle_deflection = np.array(
            [get_least_angle_deflection(obs, fct) for obs, fct in couples]
        )

        count_series = np.full_like(angle_deflection, 0).astype(float)
        count_series[angle_deflection <= threshold] = 1

        return np.sum(count_series) / len(count_series) * 100

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
@assert_length
@fix_zero_division
@source_round_digit(digit_num=1)
@convert_to_ndarray
@drop_nan
def calc_wind_level_accuracy_rate(observation, forecast, mode="strict"):
    """计算风速等级准确率

    Args:
        observation (list | ndarray): 观测风速(m/s)
        forecast (list | ndarray): 预报风速(m/s)
        mode (str): 计算模式，可选选项包括：'strict', 'loose',
                    * 'loose'模式采用的观测等级划分为宽松模式，相邻风级之间会有风速重叠，此模式下计算出来的准确率会比较高。
                    * 'strict'模式采用的观测等级划分为严格模式，相邻风级之间界面清晰，此模式下计算出来的准确率会比较低。

    Returns:
        float: 风速等级准确率(%)
    """
    couples = zip(observation, forecast)
    hits = 0
    total = 0
    for obs, fct in couples:
        total += 1
        if mode == "loose":
            obs_lev = identify_speed_level(obs, kind="mapping")
        elif mode == "strict":
            obs_lev = identify_speed_level(obs, kind="general")

        fct_lev = identify_speed_level(fct, kind="general")

        if obs_lev & fct_lev:
            hits += 1

    return hits / total * 100


@result_round_digit(4)
@assert_length
@fix_zero_division
@source_round_digit(digit_num=1)
def calc_wind_speed_accuracy_rate(observation, forecast, limit=2):
    """计算风速准确率

    Args:
        observation (list | ndarray): 观测风速(m/s)
        forecast (list | ndarray): 预报风速(m/s)
        limit (int | float): 准确率阈值
                             预报与观测之间差值的绝对值低于limit的样本个数计入准确率计算

    Returns:
        float: 风速准确率(%)
    """
    return calc_differ_accuracy_rate(observation, forecast, limit=limit)


@result_round_digit(4)
@assert_length
@fix_zero_division
@source_round_digit(digit_num=1)
@convert_to_ndarray
@drop_nan
def calc_wind_speed_score(observation, forecast):
    """计算风速评分

    Args:
        observation (list | ndarray): 观测风速(m/s)
        forecast (list | ndarray): 预报风速(m/s)

    Returns:
        float: 风速评分
    """
    couples = zip(observation, forecast)

    lev_defls = []
    for obs, fct in couples:
        obs_lev = identify_speed_level_single(obs, kind="general").pop()
        fct_lev = identify_speed_level_single(fct, kind="general").pop()

        lev_defls.append(get_least_lev_diff(obs_lev, fct_lev, circle_num=None))

    score_series = np.full_like(lev_defls, 0).astype(np.float)
    score_series[np.isclose(lev_defls, 0)] = 1
    score_series[np.isclose(lev_defls, 1)] = 0.6
    score_series[np.isclose(lev_defls, 2)] = 0.4

    return sum(score_series) / len(score_series)


@result_round_digit(4)
@source_round_digit()
def calc_wind_speed_mae(observation, forecast):
    """计算预报风速与观测之间的平均绝对误差

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表

    Returns:
        float: 预报风速与观测之间的平均绝对误差（单位与原变量相同）
    """
    return calc_mae(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_wind_speed_rmse(observation, forecast):
    """计算预报风速与观测之间的均方根误差

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表

    Returns:
        float: 预报风速与观测之间的均方根误差（单位与原变量相同）
    """
    return calc_rmse(observation, forecast)


@result_round_digit(4)
@fix_zero_division
@convert_to_ndarray
@drop_nan
@source_round_digit()
@assert_length
def calc_wind_speed_stronger_rate(observation, forecast):
    """计算风速（等级）的偏强率

    Args:
        observation (list | ndarray): 观测的风速数据列表
        forecast (list | ndarray): 预报的风速数据列表

    Returns:
        float: 风速（等级）的偏强率(%)
    """
    couples = zip(observation, forecast)

    lev_defls = []
    for obs, fct in couples:
        obs_lev = identify_speed_level_single(obs, "general").pop()
        fct_lev = identify_speed_level_single(fct, "general").pop()

        lev_defls.append(fct_lev - obs_lev)

    lev_defls = np.array(lev_defls)
    stronger_series = np.full_like(lev_defls, False)
    stronger_series[lev_defls > 0] = True

    return Counter(stronger_series)[True] / len(stronger_series) * 100


@result_round_digit(4)
@fix_zero_division
@convert_to_ndarray
@drop_nan
@source_round_digit()
@assert_length
def calc_wind_speed_weaker_rate(observation, forecast):
    """计算风速（等级）的偏弱率

    Args:
        observation (list | ndarray): 观测的风速数据列表
        forecast (list | ndarray): 预报的风速数据列表

    Returns:
        float: 风速（等级）的偏弱率(%)
    """
    couples = zip(observation, forecast)

    lev_defls = []
    for obs, fct in couples:
        obs_lev = identify_speed_level_single(obs, "general").pop()
        fct_lev = identify_speed_level_single(fct, "general").pop()

        lev_defls.append(fct_lev - obs_lev)

    lev_defls = np.array(lev_defls)
    stronger_series = np.full_like(lev_defls, False)
    stronger_series[lev_defls < 0] = True

    return Counter(stronger_series)[True] / len(stronger_series) * 100


@result_round_digit(4)
@source_round_digit()
def calc_wind_speed_chi_square(observation, forecast):
    """计算预报风速与观测之间的χ2

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表

    Returns:
        float: 预报风速与观测之间的χ2（单位是原变量的平方）
    """
    return calc_chi_square(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_wind_speed_mean_rss(observation, forecast):
    """计算预报风速与观测之间的平均剩余平方和

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表

    Returns:
        float: 预报风速与观测之间的平均剩余平方和（单位是原变量的平方）
    """
    return calc_mean_rss(observation, forecast)


def calc_wind_speed_linregress(observation, forecast):
    """计算预报风速与观测之间的线性拟合参数

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表

    Returns:
        tuple: 预报风速与观测之间的线性拟合参数，参数包括（按顺序）：
               slope, intercept, r_value, p_value, std_err
    """
    return calc_linregress(observation, forecast)


@result_round_digit(4)
@assert_length
@fix_zero_division
@convert_to_ndarray
@drop_nan
def calc_wind_composite_accuracy_rate(
    observation_speed, forecast_speed, observation_direction, forecast_direction
):
    """计算风的综合准确率

    风向预报正确，且预报风力和实况风力在同一检验等级的样本个数除以样本总个数

    Args:
        observation_speed (list | ndarray): 观测风速(m/s)
        forecast_speed (list | ndarray): 预报风速(m/s)
        observation_direction (list | ndarray): 观测风向（°）
        forecast_direction (list | ndarray): 预报风向（°）

    Returns:
        float: 风综合准确率(%)
    """
    groups = zip(
        observation_speed, forecast_speed, observation_direction, forecast_direction
    )

    hits = 0
    total = 0
    for obs_spd, fct_spd, obs_dir, fct_dir in groups:
        total += 1
        angle_deflection = get_least_angle_deflection(obs_dir, fct_dir)
        obs_lev = identify_speed_level_single(obs_spd, kind="general")
        fct_lev = identify_speed_level_single(fct_spd, kind="mapping")

        if (obs_lev & fct_lev) and (angle_deflection <= 45):
            hits += 1

    return hits / total * 100


@assert_length
@source_round_digit(series_num=2)
@convert_to_ndarray
@drop_nan
def filter_wind_speed_levels(
    observation,
    forecast,
    lev_min=None,
    lev_max=None,
    mode="and",
    return_index=False,
    *args,
    **kwargs,
):
    """根据风速等级过滤风速数组

    Args:
        observation (list | ndarray): 观测风速数组
        forecast (list | ndarray): 预报风速数组
        lev_min (float | int, optional): 过滤最小风级，若为None则取预定义风级中的最小值. Defaults to None.
        lev_max (float | int, optional): 过滤最大风级，若为None则取预定义风级中的最大值. Defaults to None.
        mode (str, optional): 过滤逻辑(and/or). Defaults to 'and'.
        return_index (boolean, optional): 是否返回索引，若为False则返回观测和预报数组，否则返回原数组的过滤索引. Defaults to False.

    Returns:
        tuple: (观测风速数组, 预报风速数组)
    """

    if not lev_min:
        lev_min = float(sorted(GENERAL_WIND_SPEED_LEVELS.keys())[0])
    if not lev_max:
        lev_max = float(sorted(GENERAL_WIND_SPEED_LEVELS.keys())[-1])

    obs_lev = identify_speed_level_array(observation)
    fct_lev = identify_speed_level_array(forecast)
    assert (obs_lev == obs_lev).all() and (fct_lev == fct_lev).all()

    if mode == "and":
        index = ((obs_lev >= lev_min) & (obs_lev <= lev_max)) & (
            (fct_lev >= lev_min) & (fct_lev <= lev_max)
        )
    elif mode == "or":
        index = ((obs_lev >= lev_min) & (obs_lev <= lev_max)) | (
            (fct_lev >= lev_min) & (fct_lev <= lev_max)
        )

    filtered_obs = observation[index]
    filtered_fct = forecast[index]

    if return_index:
        return index
    else:
        return filtered_obs, filtered_fct


class Wind(Comparison):
    def __init__(
        self,
        fp,
        time_col_name,
        obs_spd_col_name,
        obs_dir_col_name,
        fct_spd_col_name,
        fct_dir_col_name,
        kind=None,
    ):
        self.obs_spd_col_name = obs_spd_col_name
        self.obs_dir_col_name = obs_dir_col_name
        self.fct_spd_col_name = fct_spd_col_name
        self.fct_dir_col_name = fct_dir_col_name
        self.df = pd.read_csv(
            fp,
            index_col=time_col_name,
            usecols=[
                time_col_name,
                obs_spd_col_name,
                obs_dir_col_name,
                fct_spd_col_name,
                fct_dir_col_name,
            ],
        ).rename(
            columns={
                obs_spd_col_name: "obs_spd",
                obs_dir_col_name: "obs_dir",
                fct_spd_col_name: "fct_spd",
                fct_dir_col_name: "fct_dir",
            }
        )
        self.obs_spd = self.df["obs_spd"].values
        self.obs_dir = self.df["obs_dir"].values
        self.fct_spd = self.df["fct_spd"].values
        self.fct_dir = self.df["fct_dir"].values
        self.fp = fp
        self.kind = kind

    def __repr__(self):
        return super().__repr__().replace("Comparison", "Wind")

    def __str__(self):
        return super().__str__().replace("Comparison", "Wind")

    def calc_dir_accuracy_rate(self, kind=None, *args, **kwargs):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        valid_index = (
            (self.obs_spd == self.obs_spd)
            & (self.fct_spd == self.fct_spd)
            & (self.fct_dir == self.fct_dir)
            & (self.obs_dir == self.obs_dir)
        )
        obs_spd = self.obs_spd[valid_index]
        fct_spd = self.fct_spd[valid_index]
        obs_dir = self.obs_dir[valid_index]
        fct_dir = self.fct_dir[valid_index]

        index = filter_wind_speed_levels(
            obs_spd, fct_spd, lev_min=3, mode="or", return_index=True
        )
        obs = obs_dir[index]
        fct = fct_dir[index]

        return calc_wind_dir_accuracy_rate(obs, fct)

    def calc_dirange8_accuracy_rate(self, kind=None, *args, **kwargs):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        valid_index = (
            (self.obs_spd == self.obs_spd)
            & (self.fct_spd == self.fct_spd)
            & (self.fct_dir == self.fct_dir)
            & (self.obs_dir == self.obs_dir)
        )
        obs_spd = self.obs_spd[valid_index]
        fct_spd = self.fct_spd[valid_index]
        obs_dir = self.obs_dir[valid_index]
        fct_dir = self.fct_dir[valid_index]

        index = filter_wind_speed_levels(
            obs_spd, fct_spd, lev_min=3, mode="or", return_index=True
        )
        obs = obs_dir[index]
        fct = fct_dir[index]

        return calc_wind_dir_accuracy_rate(obs, fct, mode="drange8")

    def calc_dir_score(self, kind=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        valid_index = (
            (self.obs_spd == self.obs_spd)
            & (self.fct_spd == self.fct_spd)
            & (self.fct_dir == self.fct_dir)
            & (self.obs_dir == self.obs_dir)
        )
        obs_spd = self.obs_spd[valid_index]
        fct_spd = self.fct_spd[valid_index]
        obs_dir = self.obs_dir[valid_index]
        fct_dir = self.fct_dir[valid_index]

        index = filter_wind_speed_levels(
            obs_spd, fct_spd, lev_min=3, mode="or", return_index=True
        )
        obs = obs_dir[index]
        fct = fct_dir[index]

        return calc_wind_dir_score(obs, fct)

    def calc_level_accuracy_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="and"
        )
        return calc_wind_level_accuracy_rate(obs, fct)

    def calc_level_accuracy_rate_strict(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="and"
        )
        return calc_wind_level_accuracy_rate(obs, fct, mode="strict")

    def calc_level_accuracy_rate_loose(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="and"
        )
        return calc_wind_level_accuracy_rate(obs, fct, mode="loose")

    def calc_speed_accuracy_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="and"
        )
        return calc_wind_speed_accuracy_rate(obs, fct)

    def calc_speed_stronger_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_stronger_rate(obs, fct)

    def calc_speed_weaker_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_weaker_rate(obs, fct)

    def calc_speed_score(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_score(obs, fct)

    def calc_speed_mae(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_mae(obs, fct)

    def calc_linregress_args(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_speed_linregress(self.obs_spd, self.fct_spd)

    def calc_composite_accuracy_rate(self, kind=None):
        """计算风预报综合准确率

        Args:
            kind (str, optional): 检验数据的统计类型(1h/3h/24h). Defaults to None.

        Returns:
            float: 风预报综合准确率
        """
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_composite_accuracy_rate(
            self.obs_spd, self.fct_spd, self.obs_dir, self.fct_dir
        )

    def calc_chi_square(self, kind="1h", *args, **kwargs):
        """计算χ2

        Args:
            kind (str, optional): 检验数据的统计类型(1h/3h/24h). Defaults to None.

        Returns:
            float: χ2
        """
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_speed_chi_square(self.obs_spd, self.fct_spd)

    def calc_mean_rss(self, kind="1h", *args, **kwargs):
        """计算平均剩余平方和

        Args:
            kind (str, optional): 检验数据的统计类型(1h/3h/24h). Defaults to None.

        Returns:
            float: 平均剩余平方和
        """
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_speed_mean_rss(self.obs_spd, self.fct_spd)

    def calc_mae(self, kind="1h", *args, **kwargs):
        """计算平均绝对误差

        Args:
            kind (str, optional): 检验数据的统计类型(1h/3h/24h). Defaults to None.

        Returns:
            float: 平均绝对误差
        """
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_speed_mae(self.obs_spd, self.fct_spd)

    def calc_rmse(self, kind="1h", *args, **kwargs):
        """计算均方根误差

        Args:
            kind (str, optional): 检验数据的统计类型(1h/3h/24h). Defaults to None.

        Returns:
            float: 均方根误差
        """
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_speed_rmse(self.obs_spd, self.fct_spd)

    def gather_all_factors(self, kind=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])
        SPD_LEVS = {
            "0": ("分级", "总体", {"lev_min": None, "lev_max": None}),
            "1": ("分级", "≤6", {"lev_max": 6}),
            "2": ("分级", "6~8", {"lev_min": 6, "lev_max": 8}),
            "3": ("分级", "≥8", {"lev_min": 8}),
        }
        SNES_LEVS = {
            "1": ("分级", "≥6", {"lev_min": 6}),
            "2": ("分级", "≥8", {"lev_min": 8}),
            "3": ("分级", "≥10", {"lev_min": 10}),
        }
        KINDS = {"1h": "01小时", "3h": "03小时", "24h": "24小时"}
        DIR_FUNCS = {
            # 元组含义：函数对象，单位，备注
            "风向预报准确率": (self.calc_dir_accuracy_rate, "%", "风级≥3"),
            "风向8方位预报准确率": (self.calc_dirange8_accuracy_rate, "%", "风级≥3"),
            "风向预报评分": (self.calc_dir_score, None, "风级≥3"),
        }
        SPD_FUNCS = {
            # 元组含义：函数对象，单位，备注
            "风速预报准确率": (self.calc_speed_accuracy_rate, "%", "预报实况差≤2m/s"),
            "风级预报准确率1": (self.calc_level_accuracy_rate_strict, "%", "严格模式"),
            "风级预报准确率2": (self.calc_level_accuracy_rate_loose, "%", "宽松模式"),
            "风速预报偏强率": (self.calc_speed_stronger_rate, "%", None),
            "风速预报偏弱率": (self.calc_speed_weaker_rate, "%", None),
            "风速预报评分": (self.calc_speed_score, None, None),
            "风速预报平均绝对误差": (self.calc_speed_mae, "m/s", None),
        }

        OTHER_FUNCS = {
            # 元组含义：函数对象，单位，备注
            "平均剩余平方和": (self.calc_mean_rss, "(m/s)^2", None),
            "卡方": (self.calc_chi_square, "(m/s)^2", None),
            "综合准确率": (self.calc_composite_accuracy_rate, "%", None),
        }

        kind_desc = KINDS[kind]

        result = []
        # 计算风向指标
        for func_desc, (func, units, comment) in DIR_FUNCS.items():
            value = func(kind=kind)
            result.append(
                {
                    "要素": "风",
                    "时间类型": kind_desc,
                    "统计类型": None,
                    "级别": None,
                    "检验指标": func_desc,
                    "值": value,
                    "单位": units,
                    "备注": comment,
                }
            )
        # 计算分级风速指标
        for func_desc, (func, units, comment) in SPD_FUNCS.items():
            for lev, (lev_kind, lev_val, kwargs) in SPD_LEVS.items():
                value = func(kind=kind, **kwargs)
                result.append(
                    {
                        "要素": "风",
                        "时间类型": kind_desc,
                        "统计类型": lev_kind,
                        "级别": lev_val,
                        "检验指标": func_desc,
                        "值": value,
                        "单位": units,
                        "备注": comment,
                    }
                )

        # 计算风速拟合度指标
        for func_desc, (func, units, comment) in OTHER_FUNCS.items():
            value = func(kind=kind)
            result.append(
                {
                    "要素": "风",
                    "时间类型": kind_desc,
                    "统计类型": None,
                    "级别": None,
                    "检验指标": func_desc,
                    "值": value,
                    "单位": units,
                    "备注": comment,
                }
            )

        slope, intercept, *_ = self.calc_linregress_args(kind=kind)
        if intercept > 0:
            formula = f"y = {slope} * x + {abs(intercept)}"
        else:
            formula = f"y = {slope} * x - {abs(intercept)}"
        result.append(
            {
                "要素": "风",
                "时间类型": kind_desc,
                "统计类型": None,
                "级别": None,
                "检验指标": "线性回归方程",
                "值": formula,
                "单位": None,
                "备注": None,
            }
        )

        df = pd.DataFrame(result)

        return df


class Gust(Comparison):
    def __init__(
        self, fp, time_col_name, obs_spd_col_name, fct_spd_col_name, kind=None
    ):
        self.obs_spd_col_name = obs_spd_col_name
        self.fct_spd_col_name = fct_spd_col_name
        self.df = pd.read_csv(
            fp,
            index_col=time_col_name,
            usecols=[time_col_name, obs_spd_col_name, fct_spd_col_name],
        ).rename(
            columns={
                obs_spd_col_name: "obs_spd",
                fct_spd_col_name: "fct_spd",
            }
        )
        self.obs_spd = self.df["obs_spd"].values
        self.fct_spd = self.df["fct_spd"].values
        self.fp = fp
        self.kind = kind

    def __repr__(self):
        return super().__repr__().replace("Comparison", "Wind")

    def __str__(self):
        return super().__str__().replace("Comparison", "Wind")

    def calc_dir_accuracy_rate(self, kind=None, *args, **kwargs):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=3, mode="or"
        )

        return calc_wind_dir_accuracy_rate(obs, fct)

    def calc_dir_score(self, kind=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=3, mode="or"
        )

        return calc_wind_dir_score(obs, fct)

    def calc_level_accuracy_rate_loose(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="and"
        )
        return calc_wind_level_accuracy_rate(obs, fct, mode="loose")

    def calc_level_accuracy_rate_strict(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="and"
        )
        return calc_wind_level_accuracy_rate(obs, fct, mode="strict")

    def calc_speed_accuracy_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_accuracy_rate(obs, fct)

    def calc_speed_stronger_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_stronger_rate(obs, fct)

    def calc_speed_weaker_rate(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_weaker_rate(obs, fct)

    def calc_speed_score(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_score(obs, fct)

    def calc_speed_mae(self, kind=None, lev_min=None, lev_max=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        obs, fct = filter_wind_speed_levels(
            self.obs_spd, self.fct_spd, lev_min=lev_min, lev_max=lev_max, mode="or"
        )
        return calc_wind_speed_mae(obs, fct)

    def calc_composite_accuracy_rate(self, kind=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        return calc_wind_composite_accuracy_rate(
            self.obs_spd, self.fct_spd, self.obs_dir, self.fct_dir
        )

    def gather_all_factors(self, kind=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])
        SPD_LEVS = {
            "0": ("分级", "总体", {"lev_min": None, "lev_max": None}),
            "1": ("分级", "≤6", {"lev_max": 6}),
            "2": ("分级", "6~8", {"lev_min": 6, "lev_max": 8}),
            "3": ("分级", "≥8", {"lev_min": 8}),
        }
        SNES_LEVS = {
            "1": ("分级", "≥6", {"lev_min": 6}),
            "2": ("分级", "≥8", {"lev_min": 8}),
            "3": ("分级", "≥10", {"lev_min": 10}),
        }
        KINDS = {"1h": "01小时", "3h": "03小时", "24h": "24小时"}
        SPD_FUNCS = {
            # 元组含义：函数对象，单位，备注
            "风速预报准确率": (self.calc_speed_accuracy_rate, "%", "预报实况差≤2m/s"),
            "风级预报准确率1": (self.calc_level_accuracy_rate_strict, "%", "严格模式"),
            "风级预报准确率2": (self.calc_level_accuracy_rate_loose, "%", "宽松模式"),
            "风速预报偏强率": (self.calc_speed_stronger_rate, "%", None),
            "风速预报偏弱率": (self.calc_speed_weaker_rate, "%", None),
            "风速预报评分": (self.calc_speed_score, None, None),
            "风速预报平均绝对误差": (self.calc_speed_mae, "m/s", None),
        }

        SENS_FUNCS = {
            # 元组含义：函数对象，单位，备注
            "赛事敏感风级预报准确率1": (self.calc_level_accuracy_rate_strict, "%", "严格模式"),
            "赛事敏感风级预报准确率2": (self.calc_level_accuracy_rate_loose, "%", "宽松模式"),
            "赛事敏感风速预报偏强率": (self.calc_speed_stronger_rate, "%", None),
            "赛事敏感风速预报偏弱率": (self.calc_speed_weaker_rate, "%", None),
            "赛事敏感风速预报评分": (self.calc_speed_score, None, None),
            "赛事敏感风速预报平均绝对误差": (self.calc_speed_mae, "m/s", None),
        }

        kind_desc = KINDS[kind]

        result = []
        # 计算分级风速指标
        for func_desc, (func, units, comment) in SPD_FUNCS.items():
            for lev, (lev_kind, lev_val, kwargs) in SPD_LEVS.items():
                value = func(kind=kind, **kwargs)
                result.append(
                    {
                        "要素": "阵风",
                        "时间类型": kind_desc,
                        "统计类型": lev_kind,
                        "级别": lev_val,
                        "检验指标": func_desc,
                        "值": value,
                        "单位": units,
                        "备注": comment,
                    }
                )
        # 计算赛事敏感风速指标
        for func_desc, (func, units, comment) in SENS_FUNCS.items():
            for lev, (lev_kind, lev_val, kwargs) in SNES_LEVS.items():
                value = func(kind=kind, **kwargs)
                result.append(
                    {
                        "要素": "阵风",
                        "时间类型": kind_desc,
                        "统计类型": lev_kind,
                        "级别": lev_val,
                        "检验指标": func_desc,
                        "值": value,
                        "单位": units,
                        "备注": comment,
                    }
                )

        df = pd.DataFrame(result)

        return df


if __name__ == "__main__":
    pass
