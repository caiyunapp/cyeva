import numpy as np

from cyeva.core.wind import (
    get_least_angle_deflection,
    get_least_lev_deflection,
    identify_direction8,
    calc_wind_dir_score,
    calc_wind_dir_accuracy_rate,
    identify_speed_level_single,
    calc_wind_level_accuracy_rate,
    calc_wind_speed_score,
    calc_wind_speed_accuracy_rate,
    calc_wind_speed_mae,
    calc_wind_speed_stronger_rate,
    calc_wind_speed_weaker_rate,
    calc_wind_speed_chi_square,
    calc_wind_speed_rss,
    calc_wind_speed_linregress,
    calc_wind_composite_accuracy_rate,
)

from .case.wind import (
    LEAST_ANGLE_DEFLECTION_CASE,
    LEAST_DIR_DEFLECTION_CASE,
    IDENTIFY_DIRECTION8_CASE,
    WIND_DIR_SCORE_CASE,
    WIND_DIR_ACCURACY_RATE,
    IDENTIFY_SPEED_LEVEL_GENERAL_CASE,
    IDENTIFY_SPEED_LEVEL_MAPPING_CASE,
    LEAST_LEV_DEFLECTION_CASE,
    WIND_LEVEL_ACCURACY_RATE_CASE,
    WIND_SPEED_SCORE_CASE,
    WIND_SPEED_ACCURACY_RATE_CASE,
    WIND_CONPOSITE_ACCURACY_RATE_CASE,
    WIND_SPEED_MAE_CASE,
    WIND_SPEED_STRONGER_RATE_CASE,
    WIND_SPEED_WEAKER_RATE_CASE,
    WIND_SPEED_CHI_SQUARE_CASE,
    WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE,
    WIND_SPEED_LINREGRESS_CASE,
)


def test_get_least_angle_deflection():
    for case in LEAST_ANGLE_DEFLECTION_CASE:
        angle1 = case["angle1"]
        angle2 = case["angle2"]
        result = case["result"]
        assert get_least_angle_deflection(angle1, angle2) == result


def test_get_least_lev_deflection():
    for case in LEAST_DIR_DEFLECTION_CASE:
        dir1 = case["dir1"]
        dir2 = case["dir2"]
        result = case["result"]
        assert get_least_lev_deflection(dir1, dir2) == result


def test_identify_direction8():
    for case in IDENTIFY_DIRECTION8_CASE:
        angle = case["angle"]
        result = case["result"]
        assert identify_direction8(angle) == result


def test_calc_wind_dir_score():
    for case in WIND_DIR_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_dir_score(obs, fct) == result


def test_calc_wind_dir_accuracy_rate():
    for case in WIND_DIR_ACCURACY_RATE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_dir_accuracy_rate(obs, fct) == result


def test_get_least_lev_deflection2():
    for case in LEAST_LEV_DEFLECTION_CASE:
        lev1 = case["lev1"]
        lev2 = case["lev2"]
        result = case["result"]
        assert get_least_lev_deflection(lev1, lev2, circle_num=14) == result


def test_identify_speed_level_single():
    for case in IDENTIFY_SPEED_LEVEL_GENERAL_CASE:
        wspd = case["wspd"]
        result = case["result"]
        assert identify_speed_level_single(wspd) == result

    for case in IDENTIFY_SPEED_LEVEL_MAPPING_CASE:
        wspd = case["wspd"]
        result = case["result"]
        assert identify_speed_level_single(wspd, kind="mapping") == result


def test_calc_wind_level_accuracy_rate():
    for case in WIND_LEVEL_ACCURACY_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_level_accuracy_rate(obs, fct) == result


def test_calc_wind_speed_accuracy_rate():
    for case in WIND_SPEED_ACCURACY_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_speed_accuracy_rate(obs, fct) == result


def test_calc_wind_speed_score():
    for case in WIND_SPEED_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_speed_score(obs, fct) == result


def test_calc_wind_speed_stronger_rate():
    for case in WIND_SPEED_STRONGER_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_speed_stronger_rate(obs, fct) == result


def test_calc_wind_speed_weaker_rate():
    for case in WIND_SPEED_WEAKER_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_speed_weaker_rate(obs, fct) == result


def test_calc_wind_speed_chi_square():
    for case in WIND_SPEED_CHI_SQUARE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_speed_chi_square(obs, fct) == result


def test_calc_wind_speed_rss():
    for case in WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]
        assert calc_wind_speed_rss(obs, fct) == result


def test_calc_wind_speed_linregress():
    for case in WIND_SPEED_LINREGRESS_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        slope, intercept, *_ = calc_wind_speed_linregress(obs, fct)

        assert slope == result["slope"]
        assert intercept == result["intercept"]


def test_calc_wind_composite_accuracy_rate():
    for case in WIND_CONPOSITE_ACCURACY_RATE_CASE:
        obs_spd = case["obs_spd"]
        fct_spd = case["fct_spd"]
        obs_dir = case["obs_dir"]
        fct_dir = case["fct_dir"]
        result = case["result"]
        assert (
            calc_wind_composite_accuracy_rate(obs_spd, fct_spd, obs_dir, fct_dir)
            == result
        )
