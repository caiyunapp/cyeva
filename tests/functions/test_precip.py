import numpy as np

from cyeva import (
    PrecipitationComparison,
    calc_precip_accumulate_indicators,
    calc_precip_interval_indicators,
    calc_precip_occur_indicators,
)

from .case import (
    BIAS_CASE,
    CHI_SQUARE_CASE,
    DIFF_ACCURACY_RATIO,
    LINREGRESS_ARGS_CASE,
    MAE_CASE,
    RESIDUAL_SUM_OF_SQUARE_CASE,
    RMSE_CASE,
)
from .case.precip.accumulate import (
    ACC_ACCURACY_RATE_CASE,
    ACC_BIAS_SCORE_CASE,
    ACC_ETS_SCORE_CASE,
    ACC_FALSE_ALARM_RATE_CASE,
    ACC_FALSE_ALARM_RATIO_CASE,
    ACC_HIT_RATIO_CASE,
    ACC_MISS_RATIO_CASE,
    ACC_TS_SCORE_CASE,
)
from .case.precip.interval import (
    LEV_ACCURACY_RATE_CASE,
    LEV_BIAS_SCORE_CASE,
    LEV_ETS_SCORE_CASE,
    LEV_FALSE_ALARM_RATIO_CASE,
    LEV_HIT_RATIO_CASE,
    LEV_MISS_RATE_CASE,
    LEV_TS_SCORE_CASE,
)
from .case.precip.single import (
    ACCURACY_RATE_CASE,
    BIAS_SCORE_CASE,
    ETS_SCORE_CASE,
    FALSE_ALARM_RATE_CASE,
    FALSE_ALARM_RATIO_CASE,
    HIT_RATIO_CASE,
    MISS_RATE_CASE,
    TS_SCORE_CASE,
)


def test_calc_accuracy_ratio():
    for case in ACCURACY_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="accuracy_ratio")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_hit_ratio():
    for case in HIT_RATIO_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="hit_ratio")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_miss_ratio():
    for case in MISS_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="miss_ratio")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_false_alarm_ratio():
    for case in FALSE_ALARM_RATIO_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="false_alarm_ratio")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_false_alarm_rate():
    for case in FALSE_ALARM_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="false_alarm_rate")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_ts():
    for case in TS_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="ts")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_ets():
    for case in ETS_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="ets")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_bias_score():
    for case in BIAS_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        _result = calc_precip_occur_indicators(obs, fct, indicator="bias_score")
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)


def test_calc_precip_interval_accuracy_ratio():
    for kind, levs in LEV_ACCURACY_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="accuracy_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_interval_miss_ratio():
    for kind, levs in LEV_MISS_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="miss_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_interval_false_alarm_ratio():
    for kind, levs in LEV_FALSE_ALARM_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="false_alarm_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_interval_bias_score():
    for kind, levs in LEV_BIAS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="bias_score"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_interval_hit_ratio():
    for kind, levs in LEV_HIT_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="hit_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_interval_ts():
    for kind, levs in LEV_TS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="ts"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_interval_ets():
    for kind, levs in LEV_ETS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_interval_indicators(
                    obs, fct, kind, lev, indicator="ets"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_accuracy_ratio():
    for kind, levs in ACC_ACCURACY_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="accuracy_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_hit_ratio():
    for kind, levs in ACC_HIT_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="hit_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_miss_ratio():
    for kind, levs in ACC_MISS_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="miss_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_false_alarm_ratio():
    for kind, levs in ACC_FALSE_ALARM_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="false_alarm_ratio"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_false_alarm_rate():
    for kind, levs in ACC_FALSE_ALARM_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="false_alarm_rate"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_bias_score():
    for kind, levs in ACC_BIAS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="bias_score"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_ts():
    for kind, levs in ACC_TS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="ts"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_calc_precip_accumulate_ets():
    for kind, levs in ACC_ETS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fct = case["fct"]
                result = case["result"]
                _result = calc_precip_accumulate_indicators(
                    obs, fct, kind, lev, indicator="ets"
                )
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_precipitation_object_each():
    for case in RMSE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_rmse()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in MAE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_mae()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in CHI_SQUARE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_chi_square()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in RESIDUAL_SUM_OF_SQUARE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_rss()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in LINREGRESS_ARGS_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_linregress_args()
        assert _result == result

    for case in BIAS_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_bias()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in DIFF_ACCURACY_RATIO:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_diff_accuracy_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in ACCURACY_RATE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_accuracy_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in ACCURACY_RATE_CASE:
        obs = np.array(case["obs"]) / 1000
        fcst = np.array(case["fct"]) / 1000
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst, unit="m")

        _result = precip.calc_accuracy_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in MISS_RATE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_miss_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in FALSE_ALARM_RATIO_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_false_alarm_ratio()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in TS_SCORE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_ts()
        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in ETS_SCORE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_ets()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for case in BIAS_SCORE_CASE:
        obs = case["obs"]
        fcst = case["fct"]
        result = case["result"]

        precip = PrecipitationComparison(obs, fcst)

        _result = precip.calc_bias_score()

        if not np.isnan(result):
            assert _result == result
        else:
            assert np.isnan(_result)

    for kind, levs in LEV_ACCURACY_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]

                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_accuracy_ratio(lev=str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in LEV_MISS_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]

                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_miss_ratio(lev=str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in LEV_FALSE_ALARM_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_false_alarm_ratio(lev=str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in LEV_BIAS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_bias_score(lev=str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in LEV_TS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_ts(lev=str(lev), kind=kind)
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in LEV_ETS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_ets(lev=str(lev), kind=kind)
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_ACCURACY_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]

                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_accuracy_ratio(lev="+" + str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_MISS_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]

                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_miss_ratio(lev="+" + str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_FALSE_ALARM_RATIO_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_false_alarm_ratio(lev="+" + str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_FALSE_ALARM_RATE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_false_alarm_rate(lev="+" + str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_BIAS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_bias_score(lev="+" + str(lev), kind=kind)

                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_TS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_ts(lev="+" + str(lev), kind=kind)
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)

    for kind, levs in ACC_ETS_SCORE_CASE.items():
        for lev, cases in levs.items():
            for case in cases:
                obs = case["obs"]
                fcst = case["fct"]
                result = case["result"]
                precip = PrecipitationComparison(obs, fcst)

                _result = precip.calc_ets(lev="+" + str(lev), kind=kind)
                if not np.isnan(result):
                    assert _result == result
                else:
                    assert np.isnan(_result)


def test_precipitation_object_all():
    for case in ACCURACY_RATE_CASE:
        obs = case["obs"]
        fcst = case["fct"]

        precip = PrecipitationComparison(obs, fcst)

        precip.gather_all_indicators(kind="1h")
        precip.gather_all_indicators(kind="3h")
        precip.gather_all_indicators(kind="24h")


if __name__ == "__main__":
    test_precipitation_object_all()
