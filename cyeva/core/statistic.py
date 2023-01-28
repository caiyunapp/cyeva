from typing import Union
from numbers import Number
from collections import Counter

import numpy as np
from scipy import stats

from ..utils import (
    convert_to_ndarray,
    fix_zero_division,
    assert_length,
    drop_nan,
)
from .binarize import threshold_binarize


@assert_length
@drop_nan
def calc_binary_quadrant_values(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate binary quadrant values

    Quadrant values includes:
        * hits
        * misses
        * false_alarms
        * correct_rejects

    Args:
        observation (ndarray): Binarized obervation data array
                               that consist of True and False
        forecast (ndarray): Binarized forecast data array
                            that consist of True and False

    Returns:
        tuple: (hits, misses, false_alarms, correct_rejects, total)
    """
    hits = Counter(observation & forecast)[True]
    misses = Counter((observation ^ forecast) & observation)[True]
    false_alarms = Counter((observation ^ forecast) & forecast)[True]
    correct_rejects = Counter(~observation & ~forecast)[True]
    total = hits + misses + false_alarms + correct_rejects

    assert len(observation) == total

    return hits, misses, false_alarms, correct_rejects, total


@assert_length
@fix_zero_division
@drop_nan
def calc_binary_accuracy_ratio(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate accuracy of binarized observation and forecast.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: The accuracy(%) of binarized forecast.
    """
    hits, _, _, correct_rejects, total = calc_binary_quadrant_values(
        observation, forecast
    )

    return ((hits + correct_rejects) / total) * 100


@assert_length
@fix_zero_division
@drop_nan
def calc_hit_ratio(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate hit ratio.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: Missing ratio(%)
    """
    hits, misses, _, correct_rejects, _ = calc_binary_quadrant_values(
        observation, forecast
    )

    return (hits / (hits + misses)) * 100


@assert_length
@fix_zero_division
@drop_nan
def calc_miss_ratio(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate missing ratio.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: Missing ratio(%)
    """
    hits, misses, _, correct_rejects, _ = calc_binary_quadrant_values(
        observation, forecast
    )

    return (misses / (hits + misses)) * 100


@assert_length
@fix_zero_division
@drop_nan
def calc_false_alarm_ratio(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate false alarm ratio, commonly known as FAR.

    Note that false alarm rate(POFD) is different from false alarm ratio(FAR).
    You can get more information about this from https://doi.org/10.1175/2009WAF2222300.1

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: False alarm ratio(%)
    """
    hits, _, false_alarms, _, _ = calc_binary_quadrant_values(observation, forecast)

    return (false_alarms / (hits + false_alarms)) * 100


@assert_length
@fix_zero_division
@drop_nan
def calc_false_alarm_rate(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate false alarm rate, commonly known as POFD.

    Note that false alarm rate(POFD) is different from false alarm ratio(FAR).
    You can get more information about this from https://doi.org/10.1175/2009WAF2222300.1

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: False alarm rate(%)
    """
    _, _, false_alarms, correct_rejects, _ = calc_binary_quadrant_values(
        observation, forecast
    )

    return (false_alarms / (correct_rejects + false_alarms)) * 100


@assert_length
@fix_zero_division
@drop_nan
def calc_ts(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate Threat score(TS)

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: Threat score(TS)
    """
    hits, misses, false_alarms, _, _ = calc_binary_quadrant_values(
        observation, forecast
    )

    return hits / (hits + false_alarms + misses)


@assert_length
@fix_zero_division
@drop_nan
def calc_ets(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate Equitable threat score(ETS)

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: Equitable threat score(ETS)
    """
    hits, misses, false_alarms, _, total = calc_binary_quadrant_values(
        observation, forecast
    )

    hits_ref = ((hits + misses) * (hits + false_alarms)) / total

    if hits - hits_ref == hits + false_alarms + misses - hits_ref:
        return 1.0
    return (hits - hits_ref) / (hits + false_alarms + misses - hits_ref)


@assert_length
@fix_zero_division
@drop_nan
def calc_bias_score(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate Bias score

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of True and False.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of True and False.

    Returns:
        float: Bias score
    """
    hits, misses, false_alarms, _, _ = calc_binary_quadrant_values(
        observation, forecast
    )

    return (hits + false_alarms) / (hits + misses)


@assert_length
@fix_zero_division
@convert_to_ndarray
@drop_nan
def calc_diff_accuracy_ratio(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    limit: Union[float, int] = 1,
) -> float:
    """Calculate the accuracy within a limited difference scope.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        limit (Union[float, int]): The limited(or tolerable) scope between
                                   observation and forecast. Default to 1.

    Returns:
        float: The difference accuracy(%).
    """

    diff = np.abs(observation - forecast)

    bins = np.full_like(diff, False)
    bins[diff <= limit] = True

    total = len(bins)
    counter = Counter(bins)

    return counter[True] / total * 100


@assert_length
@fix_zero_division
@convert_to_ndarray
@drop_nan
def calc_rmse(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate RMSE(root-mean-square error).

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

    Returns:
        float: The RMSE of forecast to observation.
    """
    return np.sqrt(np.sum((observation - forecast) ** 2) / len(observation))


@assert_length
@fix_zero_division
@convert_to_ndarray
@drop_nan
def calc_mae(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate MAE(mean absolute error).

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

    Returns:
        float: The MAE of forecast to observation.
    """
    return np.sum(np.abs(observation - forecast)) / len(observation)


@assert_length
@fix_zero_division
@convert_to_ndarray
@drop_nan
def calc_rss(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate the residual sum of square between forecast and observation.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

    Returns:
        float: The residual sum of square of forecast and observation.
    """
    return np.sum((observation - forecast) ** 2)


@assert_length
@fix_zero_division
@convert_to_ndarray
@drop_nan
def calc_chi_square(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate the χ2 between observation and forecast.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

    Returns:
        float: The chi square of forecast and observation.
    """
    return np.sum((observation - forecast) ** 2) / len(observation)


@assert_length
@convert_to_ndarray
@drop_nan
def calc_linregress(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> tuple:
    """Calculste the parameters of linear regression.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

    Returns:
        tuple: Aguments of linear regression as follow:
               slope, intercept, r_value, p_value
    """
    linreg_result = stats.linregress(forecast, observation)[:4]

    return tuple(round(p, 4) for p in linreg_result)


@assert_length
@drop_nan
def calc_threshold_accuracy_ratio(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate accuracy ratio of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter obervation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.
        compare (str, optional): The logical operator applying `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        float: The accuracy ratio of forecast filtered by threshold.
    """
    obs_bins, fct_bins = threshold_binarize(
        observation, forecast, threshold=threshold, compare=compare
    )

    return calc_binary_accuracy_ratio(obs_bins, fct_bins)


@assert_length
@drop_nan
def calc_threshold_miss_ratio(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate missing ratio of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter obervation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.
        compare (str, optional): The logical operator applying `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        float: The missing ratio of forecast filtered by threshold.
    """
    obs_bins, fct_bins = threshold_binarize(
        observation, forecast, threshold=threshold, compare=compare
    )

    return calc_miss_ratio(obs_bins, fct_bins)


@assert_length
@drop_nan
def calc_threshold_false_alarm_ratio(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate false alarm ratio of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter obervation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.
        compare (str, optional): The logical operator applying `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        float: The false alarm ratio of forecast filtered by threshold.
    """
    obs_bins, fct_bins = threshold_binarize(
        observation, forecast, threshold=threshold, compare=compare
    )

    return calc_false_alarm_ratio(obs_bins, fct_bins)


@assert_length
@drop_nan
def calc_threshold_bias_score(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate bias score of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter obervation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.
        compare (str, optional): The logical operator applying `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        float: The bias score of forecast filtered by threshold.
    """
    obs_bins, fct_bins = threshold_binarize(
        observation, forecast, threshold=threshold, compare=compare
    )

    return calc_bias_score(obs_bins, fct_bins)


@assert_length
@drop_nan
def calc_threshold_ts(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate Threat score(TS) of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter obervation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.
        compare (str, optional): The logical operator applying `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        float: The Threat score(TS) of forecast filtered by threshold.
    """
    obs_bins, fct_bins = threshold_binarize(
        observation, forecast, threshold=threshold, compare=compare
    )

    return calc_ts(obs_bins, fct_bins)


@assert_length
@drop_nan
def calc_threshold_mae(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate MAE(mean absolute error) of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter obervation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.
        compare (str, optional): The logical operator applying `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        float: The MAE(mean absolute error) of forecast filtered by threshold.
    """
    obs_bins = np.full_like(observation, False)
    fct_bins = np.full_like(forecast, False)

    exec(f"obs_index = observation {compare} {threshold}")
    exec(f"fct_index = forecast {compare} {threshold}")

    obs_bins[locals()["obs_index"]] = True
    fct_bins[locals()["fct_index"]] = True

    return calc_mae(obs_bins, fct_bins)
