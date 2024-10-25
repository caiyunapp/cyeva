import numpy as np

from cyeva import WeatherCodeComparison

from .case.weather_code import ACCURACY_RATE_CASE, HK_CASE, HSS_CASE


def test_calc_weather_code_accuracy_ratio():
    for case in ACCURACY_RATE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        wc = WeatherCodeComparison(obs, fcst)

        _result = wc.calc_multiclass_accuracy_ratio()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_weather_code_hanssen_kuipers_score():
    for case in HK_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        wc = WeatherCodeComparison(obs, fcst)

        _result = wc.calc_multiclass_hanssen_kuipers_score()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_weather_code_heidke_skill_score():
    for case in HSS_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        wc = WeatherCodeComparison(obs, fcst)

        _result = wc.calc_multiclass_heidke_skill_score()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_gather_all_factors():
    for case in ACCURACY_RATE_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        wc = WeatherCodeComparison(obs, fcst)
        wc.gather_all_factors()
