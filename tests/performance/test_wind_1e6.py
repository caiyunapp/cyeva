from numbers import Number
from typing import List

import numpy as np

from cyeva.core.wind import (
    get_least_angle_deflection,
    identify_direction,
    identify_wind_scale,
    get_least_lev_diff,
    get_least_dir_deflection,
    filter_wind_scales,
    WindComparison,
)


def test_get_least_angle_deflection_1e6(benchmark):
    angle1 = np.random.rand(int(1e6)) * 360
    angle2 = np.random.rand(int(1e6)) * 360

    def inner():
        get_least_angle_deflection(angle1, angle2)

    benchmark(inner)


def test_get_least_dir_deflection_1e6(benchmark):
    dir1 = np.random.randint(0, 8, (int(1e6),))
    dir2 = np.random.randint(0, 8, (int(1e6),))

    def inner():
        get_least_dir_deflection(dir1, dir2)

    benchmark(inner)


def test_identify_direction8_1e6(benchmark):
    angle = np.random.rand(int(1e6)) * 360

    def inner():
        identify_direction(angle, dnum=8)

    benchmark(inner)


def test_identify_direction16_1e6(benchmark):
    angle = np.random.rand(int(1e6)) * 360

    def inner():
        identify_direction(angle, dnum=16)

    benchmark(inner)


def test_identify_wind_scale_1e6(benchmark):
    wspd = np.random.rand(int(1e6)) * 50

    def inner():
        identify_wind_scale(wspd)

    benchmark(inner)


def test_calc_wind_dir_score_1e6(benchmark):
    obs_angle = np.random.rand(int(1e6)) * 360
    fct_angle = np.random.rand(int(1e6)) * 360
    wind_comparison = WindComparison(obs_dir=obs_angle, fct_dir=fct_angle)

    def inner():
        wind_comparison.calc_dir_score()

    benchmark(inner)


def test_get_least_lev_deflection_1e6(benchmark):
    lev1 = np.random.randint(0, 12, (int(1e6),))
    lev2 = np.random.randint(0, 12, (int(1e6),))

    def inner():
        get_least_lev_diff(lev1, lev2)

    benchmark(inner)


def test_calc_wind_dir_accuracy_ratio_1e6(benchmark):
    obs_angle = np.random.rand(int(1e6)) * 360
    fct_angle = np.random.rand(int(1e6)) * 360
    wind_comparison = WindComparison(obs_dir=obs_angle, fct_dir=fct_angle)

    def inner():
        wind_comparison.calc_dir_accuracy_ratio()

    benchmark(inner)


def test_calc_wind_scale_accuracy_ratio_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_wind_scale_accuracy_ratio()

    benchmark(inner)


def test_calc_wind_speed_accuracy_ratio_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_speed_accuracy_ratio()

    benchmark(inner)


def test_calc_wind_speed_score_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_speed_score()

    benchmark(inner)


def test_calc_wind_scale_stronger_ratio_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_wind_scale_stronger_ratio()

    benchmark(inner)


def test_calc_wind_scale_weaker_ratio_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_wind_scale_weaker_ratio()

    benchmark(inner)


def test_calc_wind_speed_chi_square_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_chi_square()

    benchmark(inner)


def test_calc_wind_speed_rss_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_rss()

    benchmark(inner)


def test_calc_wind_speed_mae_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_mae()

    benchmark(inner)


def test_calc_wind_speed_linregress_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50
    wind_comparison = WindComparison(obs_spd=obs_wspd, fct_spd=fct_wspd)

    def inner():
        wind_comparison.calc_linregress_args()

    benchmark(inner)


def test_filter_wind_scales_1e6(benchmark):
    obs_wspd = np.random.rand(int(1e6)) * 50
    fct_wspd = np.random.rand(int(1e6)) * 50

    def inner():
        filter_wind_scales(obs_wspd, fct_wspd, scale_min=3, scale_max=5)

    benchmark(inner)
