import numpy as np

from cyeva.core.base import Comparison

from .case import (
    BIAS_CASE,
    BINARY_ACCURACY_RATIO_CASE,
    CHI_SQUARE_CASE,
    DIFF_ACCURACY_RATIO,
    LINREGRESS_ARGS_CASE,
    MAE_CASE,
    RESIDUAL_SUM_OF_SQUARE_CASE,
    RMSE_CASE,
)


def test_comparison():
    for case in RMSE_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_rmse()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in MAE_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_mae()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in CHI_SQUARE_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_chi_square()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in RESIDUAL_SUM_OF_SQUARE_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_rss()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in LINREGRESS_ARGS_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_linregress_args()
        assert _result == result

    for case in BINARY_ACCURACY_RATIO_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_binary_accuracy_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in BIAS_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_bias()
        _result2 = cp.calc_bias(cp.observation, cp.forecast)
        if not np.isnan(result):
            assert _result == _result2 == result
        else:
            assert np.isnan(_result)

    for case in DIFF_ACCURACY_RATIO:
        obs = case["obs"]
        fcst = case["fct"]

        cp = Comparison(obs, fcst)

        result = case["result"]
        _result = cp.calc_diff_accuracy_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_mae():
    MAE_CASE = [
        {"obs": [1, 2, 3, 4, 5], "fct": [1, 2, 3, 4, 5], "result": 0.0},
        {"obs": [1, 2, 3, 4, 5], "fct": [3, 3, 3, 3, 3], "result": 1.2},
    ]
    for case in MAE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        cp = Comparison(obs, fct)
        _result = cp.calc_mae()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_mbe():
    MBE_CASE = [
        {"obs": [1, 2, 3, 4, 5], "fct": [1, 2, 3, 4, 5], "result": 0.0},
        {"obs": [1, 2, 3, 4, 5], "fct": [3, 3, 3, 3, 3], "result": 0.0},
        {"obs": [1, 2, 3, 4, 5], "fct": [1, 1, 1, 1, 1], "result": -2.0},
        {"obs": [1, 2, 3, 4, 5], "fct": [5, 5, 5, 5, 5], "result": 2.0},
    ]
    for case in MBE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        cp = Comparison(obs, fct)
        _result = cp.calc_mbe()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_threshold_hit_ratio():
    THRESHOLD_HIT_RATIO_CASE = [
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 1, 1, 1, 1],
            "threshold": 2,
            "result": 0.0,
        },
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 2, 1, 1, 1],
            "threshold": 2,
            "result": 25,
        },
        {"obs": [1, 2, 2, 2, 2], "fct": [1, 2, 2, 1, 1], "threshold": 2, "result": 50},
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 2, 2, 2, 1],
            "threshold": 2,
            "result": 75,
        },
        {"obs": [1, 2, 2, 2, 2], "fct": [1, 2, 2, 2, 2], "threshold": 2, "result": 100},
    ]
    for case in THRESHOLD_HIT_RATIO_CASE:
        obs = case["obs"]
        fct = case["fct"]
        threshold = case["threshold"]
        result = case["result"]
        cp = Comparison(obs, fct)
        _result = cp.calc_threshold_hit_ratio(threshold=threshold)
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_threshold_false_alarm_ratio():
    THRESHOLD_FAR_CASE = [
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 1, 1, 1, 1],
            "threshold": 2,
            "result": np.nan,
        },
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 2, 1, 1, 1],
            "threshold": 2,
            "result": 0,
        },
        {"obs": [1, 2, 1, 2, 2], "fct": [1, 2, 2, 1, 1], "threshold": 2, "result": 50},
        {
            "obs": [1, 2, 1, 1, 1],
            "fct": [1, 2, 2, 2, 2],
            "threshold": 2,
            "result": 75,
        },
        {"obs": [1, 1, 1, 1, 1], "fct": [1, 2, 2, 2, 2], "threshold": 2, "result": 100},
    ]
    for case in THRESHOLD_FAR_CASE:
        obs = case["obs"]
        fct = case["fct"]
        threshold = case["threshold"]
        result = case["result"]
        cp = Comparison(obs, fct)
        _result = cp.calc_threshold_false_alarm_ratio(threshold=threshold)
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_threshold_ts():
    THRESHOLD_TS_CASE = [
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 1, 1, 1, 1],
            "threshold": 2,
            "result": 0,
        },
        {
            "obs": [1, 2, 2, 2, 2],
            "fct": [1, 2, 1, 1, 1],
            "threshold": 2,
            "result": 0.25,
        },
        {"obs": [1, 2, 2, 2, 2], "fct": [2, 2, 1, 1, 1], "threshold": 2, "result": 0.2},
        {
            "obs": [1, 2, 1, 1, 1],
            "fct": [1, 2, 2, 2, 2],
            "threshold": 2,
            "result": 0.25,
        },
        {"obs": [1, 1, 1, 1, 1], "fct": [1, 2, 2, 2, 2], "threshold": 2, "result": 0},
    ]
    for case in THRESHOLD_TS_CASE:
        obs = case["obs"]
        fct = case["fct"]
        threshold = case["threshold"]
        result = case["result"]
        cp = Comparison(obs, fct)
        _result = cp.calc_threshold_ts(threshold=threshold)
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def calc_correlation_coefficient():
    THRESHOLD_TS_CASE = [
        {
            "obs": [1, 2, 3, 4, 5],
            "fct": [1, 2, 3, 4, 5],
            "result": 1,
        },
        {
            "obs": [1, 2, 3, 4, 5],
            "fct": [5, 4, 3, 2, 1],
            "result": -1,
        },
        {"obs": [1, 1, 1, 1, 1], "fct": [2, 2, 2, 2, 2], "result": 0},
    ]
    for case in THRESHOLD_TS_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        cp = Comparison(obs, fct)
        _, _, _result, _ = cp.calc_linregress()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)
