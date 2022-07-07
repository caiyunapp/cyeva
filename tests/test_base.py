import numpy as np

from cyeva.core.base import Comparison
from .case import (
    RMSE_CASE,
    MAE_CASE,
    CHI_SQUARE_CASE,
    RESIDUAL_SUM_OF_SQUARE_CASE,
    LINREGRESS_ARGS_CASE,
    BINARY_ACCURACY_RATIO_CASE,
    BIAS_CASE,
    DIFF_ACCURACY_RATIO,
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
