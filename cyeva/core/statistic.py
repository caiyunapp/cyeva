from collections import Counter
from itertools import product
from numbers import Number
from typing import Union

import numpy as np
import pandas as pd
from scipy import stats

from ..utils import (
    assert_length,
    convert_to_ndarray,
    drop_nan,
    fix_zero_division,
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
        observation (ndarray): Binarized observation data array
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
@drop_nan
def calc_multiclass_confusion_matrix(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> pd.DataFrame:
    """Calculate multiclass confusion matrix

        confusion matrix
                            Observation
                            class 1     class 2      ...    class K
        Forecast    class 1 n(F_1,O_1)  n(F_1,O_2)          n(F_1,O_K)
                    class 2 n(F_2,O_1)  n(F_2,O_2)          n(F_2,O_K)
                    .
                    .
                    .
                    class K n(F_K,O_1)  n(F_K,O_2)          n(F_K,O_K)

        where n(Fi,Oj) denotes the number of forecasts in category i that had observations in category j and K is total class number

    Args:
        observation (Union[list, np.ndarray]): Multiclass observation data array
                                                that consist of class labels.
        forecast (Union[list, np.ndarray]): Multiclass forecast data array
                                        that consist of class labels.

    Returns:
        pd.DataFrame: confusion matrix
    """

    cates = np.unique(np.concatenate([np.unique(observation), np.unique(forecast)]))
    confusion_matrix_list = []
    for obs_cate_, fcst_cate_ in product(cates, cates):
        count_cate_ = Counter((observation == obs_cate_) & (forecast == fcst_cate_))[
            True
        ]
        confusion_matrix_list.append([obs_cate_, fcst_cate_, count_cate_])

    confusion_matrix = pd.DataFrame(
        np.array(confusion_matrix_list), columns=["observation", "forecast", "count"]
    )
    confusion_matrix = confusion_matrix.pivot_table(
        "count", index="forecast", columns="observation", aggfunc="sum"
    ).astype(int)

    assert len(observation) == np.sum(confusion_matrix.values)

    return confusion_matrix


@assert_length
@fix_zero_division
@drop_nan
def calc_multiclass_accuracy_ratio(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate accuracy of Multiclass observation and forecast.

       Accuracy = \frac {\sum\limits_{i=1}^{K} n(F_i,O_i)} {Total} * 100

    Args:
        observation (Union[list, np.ndarray]): Multiclass observation data array
                                                that consist of class labels.
        forecast (Union[list, np.ndarray]): Multiclass forecast data array
                                            that consist of class labels.

    Returns:
        float: The accuracy(%) of multiclass forecast. Perfect score 100.
    """

    confusion_matrix = calc_multiclass_confusion_matrix(observation, forecast)
    # compute the sum of hits of all categories
    all_hits = np.sum(confusion_matrix.values.diagonal())
    total = len(observation)

    return (all_hits / total) * 100


@assert_length
@fix_zero_division
@drop_nan
def calc_multiclass_heidke_skill_score(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """calculate the Heidke Skill Score (HSS), which measures the
    fraction of correct forecasts after eliminating those forecasts
    which would be correct due purely to random chance.

        HSS = \frac {\frac {1} {Total} \sum\limits_{i=1}^{K} n(F_i,O_i) -
            \frac {1} {Total^2} \sum\limits_{i=1}^{K} N(F_i)N(O_i) }
            {1 - \frac {1} {Total^2} \sum\limits_{i=1}^{K} N(F_i)*N(O_i)}

    Args:
        observation (Union[list, np.ndarray]): Multiclass observation data array
                                                that consist of class labels.
        forecast (Union[list, np.ndarray]): Multiclass forecast data array
                                            that consist of class labels.

    Returns:
        float: HSS score. Perfect score 1.
    """

    confusion_matrix = calc_multiclass_confusion_matrix(observation, forecast)
    total = len(observation)

    # compute HSS score
    acc_ = np.sum(confusion_matrix.values.diagonal()) / total
    reference_acc_ = np.sum(
        confusion_matrix.sum(axis=0).values * confusion_matrix.sum(axis=1).values
    ) / (total**2)
    perfect_acc_ = 1
    hss_score_ = (acc_ - reference_acc_) / (perfect_acc_ - reference_acc_)

    return hss_score_


@assert_length
@fix_zero_division
@drop_nan
def calc_multiclass_hanssen_kuipers_score(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """calculate the Hanssen and Kuipers Score (HSS), which is
    similar to the Heidke skill score (above), except that in
    the denominator the fraction of correct forecasts due to
    random chance is for an unbiased forecast.

        HK = \frac {\frac {1} {Total} \sum\limits_{i=1}^{K} n(F_i,O_i) -
            \frac {1} {Total^2} \sum\limits_{i=1}^{K} N(F_i)N(O_i) }
            {1 - \frac {1} {Total^2} \sum\limits_{i=1}^{K} N(O_i)^2}

    Args:
        observation (Union[list, np.ndarray]): Multiclass observation data array
                                                that consist of class labels.
        forecast (Union[list, np.ndarray]): Multiclass forecast data array
                                            that consist of class labels.

    Returns:
        float: HK score. Perfect score 1.
    """

    confusion_matrix = calc_multiclass_confusion_matrix(observation, forecast)
    total = len(observation)

    # compute HK score
    acc_ = np.sum(confusion_matrix.values.diagonal()) / total
    reference_acc_ = np.sum(
        confusion_matrix.sum(axis=0).values * confusion_matrix.sum(axis=1).values
    ) / (total**2)
    perfect_acc_ = 1
    unbias_reference_acc_ = np.sum(confusion_matrix.sum(axis=0).values ** 2) / (
        total**2
    )
    hk_score_ = (acc_ - reference_acc_) / (perfect_acc_ - unbias_reference_acc_)

    return hk_score_


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
def calc_mbe(
    observation: Union[list, np.ndarray], forecast: Union[list, np.ndarray]
) -> float:
    """Calculate MBE(mean bias error).

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

    Returns:
        float: The MBE of forecast to observation.
    """
    return np.sum(forecast - observation) / len(observation)


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
        tuple: Arguments of linear regression as follow:
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
        threshold (Number): The threshold to filter observation and forecast.
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
def calc_threshold_hit_ratio(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number,
    compare: str = ">=",
) -> float:
    """Calculate hit ratio of forecast filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.
        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.
        threshold (Number): The threshold to filter observation and forecast.
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

    return calc_hit_ratio(obs_bins, fct_bins)


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
        threshold (Number): The threshold to filter observation and forecast.
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
        threshold (Number): The threshold to filter observation and forecast.
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
        threshold (Number): The threshold to filter observation and forecast.
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
        threshold (Number): The threshold to filter observation and forecast.
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
        threshold (Number): The threshold to filter observation and forecast.
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
