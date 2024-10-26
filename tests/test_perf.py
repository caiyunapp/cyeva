import numpy as np

from cyeva.core.statistic import (
    calc_mae,
    calc_mbe,
    calc_threshold_false_alarm_ratio,
    calc_threshold_hit_ratio,
    calc_threshold_ts,
)


def test_calc_mae_1e3(benchmark):
    # thousand level
    obs = np.random.rand(int(1e3))
    fct = np.random.rand(int(1e3))

    def inner():
        calc_mae(obs, fct)

    benchmark(inner)


def test_calc_mae_1e6(benchmark):
    # million level
    obs = np.random.rand(int(1e6))
    fct = np.random.rand(int(1e6))

    def inner():
        calc_mae(obs, fct)

    benchmark(inner)


def test_calc_mbe_1e3(benchmark):
    # thousand level
    obs = np.random.rand(int(1e3))
    fct = np.random.rand(int(1e3))

    def inner():
        calc_mbe(obs, fct)

    benchmark(inner)


def test_calc_mbe_1e6(benchmark):
    # million level
    obs = np.random.rand(int(1e6))
    fct = np.random.rand(int(1e6))

    def inner():
        calc_mbe(obs, fct)

    benchmark(inner)


def test_calc_threshold_hit_ratio_1e3(benchmark):
    # thousand level
    obs = np.random.rand(int(1e3))
    fct = np.random.rand(int(1e3))

    def inner():
        calc_threshold_hit_ratio(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_hit_ratio_1e6(benchmark):
    # million level
    obs = np.random.rand(int(1e6))
    fct = np.random.rand(int(1e6))

    def inner():
        calc_threshold_hit_ratio(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_false_alarm_ratio_1e3(benchmark):
    obs = np.random.rand(int(1e3))
    fct = np.random.rand(int(1e3))

    def inner():
        calc_threshold_false_alarm_ratio(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_false_alarm_ratio_1e6(benchmark):
    # million level
    obs = np.random.rand(int(1e6))
    fct = np.random.rand(int(1e6))

    def inner():
        calc_threshold_false_alarm_ratio(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_ts_1e3(benchmark):
    # thousand level
    obs = np.random.rand(int(1e3))
    fct = np.random.rand(int(1e3))

    def inner():
        calc_threshold_ts(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_ts_1e6(benchmark):
    # million level
    obs = np.random.rand(int(1e6))
    fct = np.random.rand(int(1e6))

    def inner():
        calc_threshold_ts(obs, fct, 0.5)

    benchmark(inner)
