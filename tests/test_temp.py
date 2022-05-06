import numpy as np

from cyeva import TemperatureComparison
from .case.temp import (
    ACCURACY_RATE_CASE,
    RMSE_CASE,
    MAE_CASE,
    RESIDUAL_SUM_OF_SQUARE_CASE,
    CHI_SQUARE_CASE,
    LINREGRESS_CASE,
)


def test_calc_temp_accuracy_ratio():
    for limit, cases in ACCURACY_RATE_CASE.items():
        for case in cases:
            obs = case["obs"]
            fcst = case["fct"]
            result = case["result"]

            temp = TemperatureComparison(obs, fcst)

            _result = temp.calc_diff_accuracy_ratio(limit=limit)

            if not np.isnan(result):
                assert _result == result
            else:
                assert np.isnan(_result)


def test_calc_temp_rmse():
    for case in RMSE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        temp = TemperatureComparison(obs, fcst)

        _result = temp.calc_rmse()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_temp_mae():
    for case in MAE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        temp = TemperatureComparison(obs, fcst)

        _result = temp.calc_mae()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_temp_rss():
    for case in RESIDUAL_SUM_OF_SQUARE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        temp = TemperatureComparison(obs, fcst)

        _result = temp.calc_rss()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_temp_chi_square():
    for case in CHI_SQUARE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        temp = TemperatureComparison(obs, fcst)

        _result = temp.calc_chi_square()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_temp_linregress():
    for case in LINREGRESS_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        temp = TemperatureComparison(obs, fcst)

        slope, intercept, *_ = temp.calc_linregress_args(obs, fcst)

        assert slope == result["slope"]
        assert intercept == result["intercept"]


def test_gather_all_factors():
    for _, cases in ACCURACY_RATE_CASE.items():
        for case in cases:
            obs = case["obs"]
            fcst = case["fct"]

            TemperatureComparison(obs, fcst)
