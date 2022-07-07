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
    np.random.seed(0)

    obs = np.sin(np.arange(100)) * 20 + np.random.random(100) * 5 * np.random.choice(
        [1, -1]
    )
    fcst = obs + np.random.random(100) * 5 * np.random.choice([1, -1])

    temp = TemperatureComparison(obs, fcst)
    temp.gather_all_factors()


def test_temp_obj():
    np.random.seed(0)

    obs = np.sin(np.arange(100)) * 20 + np.random.random(100) * 5 * np.random.choice(
        [1, -1]
    )
    fcst = obs + np.random.random(100) * 5 * np.random.choice([1, -1])

    temp = TemperatureComparison(obs, fcst)
    temp
    print(temp)
    assert (
        temp.__str__()
        == temp.__repr__()
        == """<Object:TemperatureComparison(degC)>
data:
    observation   forecast
0     -2.744068  -5.592160
1     13.253473   9.734786
2     15.172132  13.729749
3      0.097984  -2.068456
4    -17.254324 -21.034857
..          ...        ...
95    12.749277   7.898094
96    16.739190  13.336467
97     7.491617   7.065139
98   -15.612338 -15.894429
99   -20.007614 -22.446803

[100 rows x 2 columns]"""
    )
