from cyeva.core.visib import (
    calc_visib_interval_bias_score,
    calc_visib_interval_false_alarm_rate,
    calc_visib_interval_miss_rate,
    calc_visib_interval_ts_score,
    calc_visib_mae,
)

from .case.visib import (
    INTERVAL_BIAS_SCORE_CASE,
    INTERVAL_FALSE_ALARM_RATE_CASE,
    INTERVAL_MISS_RATE_CASE,
    INTERVAL_TS_SCORE_CASE,
    INTERVAL_MAE_CASE,
)


def test_calc_visib_interval_miss_rate():
    for kind, levs in INTERVAL_MISS_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                assert calc_visib_interval_miss_rate(obs, fct, kind, lev) == result


def test_calc_visib_interval_false_alarm_rate():
    for kind, levs in INTERVAL_FALSE_ALARM_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                assert (
                    calc_visib_interval_false_alarm_rate(obs, fct, kind, lev) == result
                )


def test_calc_visib_interval_bias_score():
    for kind, levs in INTERVAL_BIAS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                assert calc_visib_interval_bias_score(obs, fct, kind, lev) == result


def test_calc_visib_interval_ts_score():
    for kind, levs in INTERVAL_TS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                assert calc_visib_interval_ts_score(obs, fct, kind, lev) == result


def test_calc_visib_mae():
    for case in INTERVAL_MAE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_visib_mae(obs, fct) == result
