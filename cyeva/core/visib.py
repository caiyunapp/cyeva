import numpy as np
import pandas as pd

from cyeva.config.levels.visib import VISIB_LEVELS, SENS_VISIB_LEVELS
from cyeva.core.binarize import interval_level_binarize
from cyeva.utils import (
    fix_zero_division,
    result_round_digit,
    source_round_digit,
    drop_nan,
)
from .statistic import (
    calc_miss_rate,
    calc_false_alarm_rate,
    calc_ts_score,
    calc_bias_score,
    calc_mae,
    calc_threshold_accuracy_rate,
    calc_threshold_miss_rate,
    calc_threshold_false_alarm_rate,
    calc_threshold_bias_score,
    calc_threshold_ts_score,
    calc_threshold_mae,
)
from cyeva.core import Comparison


@result_round_digit(4)
@source_round_digit()
def calc_visib_interval_miss_rate(observation, forecast, kind, lev, *args, **kwargs):
    """分等级计算能见度漏报率

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：0-1km
                        * 2：1-5km
                        * 3：5-10km
                        * 4：>10km

    Returns:
        float: 相应等级的能见度漏报率（单位%）
    """
    observation, forecast = interval_level_binarize(
        observation, forecast, VISIB_LEVELS, kind, lev
    )
    return calc_miss_rate(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_visib_interval_false_alarm_rate(
    observation, forecast, kind, lev, *args, **kwargs
):
    """分等级计算能见度误报率（空报率）

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：0-1km
                        * 2：1-5km
                        * 3：5-10km
                        * 4：>10km

    Returns:
        float: 相应等级的能见度误报率（空报率）
    """
    observation, forecast = interval_level_binarize(
        observation, forecast, VISIB_LEVELS, kind, lev
    )
    return calc_false_alarm_rate(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_visib_interval_ts_score(observation, forecast, kind, lev, *args, **kwargs):
    """分等级计算能见度TS评分

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：0-1km
                        * 2：1-5km
                        * 3：5-10km
                        * 4：>10km

    Returns:
        float: 相应等级的能见度TS评分
    """
    observation, forecast = interval_level_binarize(
        observation, forecast, VISIB_LEVELS, kind, lev
    )
    return calc_ts_score(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_visib_interval_bias_score(observation, forecast, kind, lev, *args, **kwargs):
    """分等级计算能见度BIAS偏差

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：0-1km
                        * 2：1-5km
                        * 3：5-10km
                        * 4：>10km

    Returns:
        float: 相应等级的能见度BIAS偏差
    """
    observation, forecast = interval_level_binarize(
        observation, forecast, VISIB_LEVELS, kind, lev
    )
    return calc_bias_score(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_visib_mae(observation, forecast, *args, **kwargs):
    """计算能见度预报与观测之间的平均绝对误差

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表

    Returns:
        float: 能见度预报与观测之间的平均绝对误差（单位与原变量相同）
    """
    return calc_mae(observation, forecast)


@result_round_digit(4)
@source_round_digit()
def calc_visib_sensitive_ts_score(observation, forecast, lev, *args, **kwargs):
    """分等级计算赛事敏感能见度TS评分

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：≤1km
                        * 2：≤0.5km
                        * 3：≤0.1km

    Returns:
        float: 相应等级的赛事敏感能见度TS评分
    """
    threshold = SENS_VISIB_LEVELS[lev]["threshold"]
    compare = SENS_VISIB_LEVELS[lev]["compare"]
    return calc_threshold_ts_score(observation, forecast, threshold, compare)


@result_round_digit(4)
@source_round_digit()
def calc_visib_sensitive_false_alarm_rate(observation, forecast, lev, *args, **kwargs):
    """分等级计算赛事敏感能见度空报率

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：≤1km
                        * 2：≤0.5km
                        * 3：≤0.1km

    Returns:
        float: 相应等级的赛事敏感能见度空报率（%）
    """
    threshold = SENS_VISIB_LEVELS[lev]["threshold"]
    compare = SENS_VISIB_LEVELS[lev]["compare"]
    return calc_threshold_false_alarm_rate(observation, forecast, threshold, compare)


@result_round_digit(4)
@source_round_digit()
def calc_visib_sensitive_miss_rate(observation, forecast, lev, *args, **kwargs):
    """分等级计算赛事敏感能见度漏报率

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：≤1km
                        * 2：≤0.5km
                        * 3：≤0.1km

    Returns:
        float: 相应等级的赛事敏感能见度漏报率（%）
    """
    threshold = SENS_VISIB_LEVELS[lev]["threshold"]
    compare = SENS_VISIB_LEVELS[lev]["compare"]
    return calc_threshold_miss_rate(observation, forecast, threshold, compare)


@result_round_digit(4)
@source_round_digit()
def calc_visib_sensitive_bias_rate(observation, forecast, lev, *args, **kwargs):
    """分等级计算赛事敏感能见度BIAS偏差

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：≤1km
                        * 2：≤0.5km
                        * 3：≤0.1km

    Returns:
        float: 相应等级的赛事敏感能见度BIAS偏差
    """
    threshold = SENS_VISIB_LEVELS[lev]["threshold"]
    compare = SENS_VISIB_LEVELS[lev]["compare"]
    return calc_threshold_bias_score(observation, forecast, threshold, compare)


@result_round_digit(4)
@source_round_digit()
def calc_visib_sensitive_mae(observation, forecast, lev, *args, **kwargs):
    """分等级计算赛事敏感能见度MAE

    Args:
        observation (list | ndarray): 观测数据列表
        forecast (list | ndarray): 预报数据列表
        kind (str): 数据类型(1h/3h/24h)
        lev (int): 等级编号，可选项：
                        * 1：≤1km
                        * 2：≤0.5km
                        * 3：≤0.1km

    Returns:
        float: 相应等级的赛事敏感能见度MAE
    """
    threshold = SENS_VISIB_LEVELS[lev]["threshold"]
    compare = SENS_VISIB_LEVELS[lev]["compare"]
    return calc_threshold_mae(observation, forecast, threshold, compare)


class Visibility(Comparison):
    def __init__(self, fp, time_col_name, obs_col_name, fct_col_name, kind=None):
        super().__init__(fp, time_col_name, obs_col_name, fct_col_name, kind=kind)

    def __repr__(self):
        return super().__repr__().replace("Comparison", "Visibility")

    def __str__(self):
        return super().__str__().replace("Comparison", "Visibility")

    def gather_all_factors(self, kind=None):
        if not kind:
            kind = self.kind
        assert kind and (kind.lower() in ["1h", "3h", "24h"])

        LEVS = {1: ("分级", 1), 2: ("分级", 2), 3: ("分级", 3), 4: ("分级", 4)}
        LEVS_COMMENTS = {
            1: "能见度<=1000m",
            2: "1000m<能见度<=5000m",
            3: "5000m<能见度<=10000m",
            4: "能见度>10000m",
        }
        KINDS = {"1h": "01小时", "3h": "03小时", "24h": "24小时"}
        FUNCS = {
            # 元组含义：函数对象，单位，备注
            "TS评分": (calc_visib_interval_ts_score, None, None),
            "空报率": (calc_visib_interval_false_alarm_rate, "%", None),
            "漏报率": (calc_visib_interval_miss_rate, "%", None),
            "预报偏差": (calc_visib_interval_bias_score, None, None),
            "赛事敏感TS评分": (calc_visib_sensitive_ts_score, None, None),
            "赛事敏感空报率": (calc_visib_sensitive_false_alarm_rate, "%", None),
            "赛事敏感漏报率": (calc_visib_sensitive_miss_rate, "%", None),
            "赛事敏感预报偏差": (calc_visib_sensitive_bias_rate, None, None),
        }

        kind_desc = KINDS[kind]
        result = []
        for lev, (lev_kind, lev_desc) in LEVS.items():
            for func_desc, (func, units, comment) in FUNCS.items():
                try:
                    value = func(self.observation, self.forecast, kind=kind, lev=lev)
                except KeyError:
                    continue
                else:
                    result.append(
                        {
                            "要素": "能见度",
                            "时间类型": kind_desc,
                            "统计类型": lev_kind,
                            "级别": lev_desc,
                            "检验指标": func_desc,
                            "值": value,
                            "单位": units,
                            "备注": LEVS_COMMENTS[lev],
                        }
                    )

        df = pd.DataFrame(result)

        return df


if __name__ == "__main__":
    pass
