import numpy as np

from cyeva.core.statistic import (
    calc_mae,
    calc_mbe,
    calc_threshold_hit_ratio,
    calc_threshold_false_alarm_ratio,
    calc_threshold_ts,
    calc_linregress,
)


def test_calc_mae():
    MAE_CASE = [
        {"obs": [1, 2, 3, 4, 5], "fct": [1, 2, 3, 4, 5], "result": 0.0},
        {"obs": [1, 2, 3, 4, 5], "fct": [3, 3, 3, 3, 3], "result": 1.2},
    ]
    for case in MAE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_mae(obs, fct)
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
        _result = calc_mbe(obs, fct)
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
        _result = calc_threshold_hit_ratio(obs, fct, threshold)
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
        _result = calc_threshold_false_alarm_ratio(obs, fct, threshold)
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
        _result = calc_threshold_ts(obs, fct, threshold)
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
        threshold = case["threshold"]
        result = case["result"]
        _, _, _result, _ = calc_linregress(obs, fct)
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)
