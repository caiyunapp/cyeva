import numpy as np

from cyeva.core.statistic import (
    calc_mae,
    calc_mbe,
    calc_threshold_hit_ratio,
    calc_threshold_false_alarm_ratio,
    calc_threshold_ts,
    calc_hit_ratio,
    calc_miss_ratio,
    calc_binary_accuracy_ratio,
    calc_false_alarm_ratio,
    calc_false_alarm_rate,
    calc_ts,
    calc_ets,
    calc_bias_score,
    calc_diff_accuracy_ratio,
    calc_rmse,
    calc_rss,
    calc_chi_square,
    calc_linregress,
    calc_threshold_accuracy_ratio,
    calc_threshold_miss_ratio,
    calc_threshold_bias_score,
    calc_threshold_mae,
)


def test_calc_mae_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_mae(obs, fct)

    benchmark(inner)


def test_calc_mbe_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_mbe(obs, fct)

    benchmark(inner)


def test_calc_threshold_hit_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_hit_ratio(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_false_alarm_ratio_1e7(benchmark):
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_false_alarm_ratio(obs, fct, 0.5)

    benchmark(inner)


def test_calc_threshold_ts_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_ts(obs, fct, 0.5)

    benchmark(inner)


def test_calc_hit_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_hit_ratio(obs, fct)

    benchmark(inner)


def test_calc_miss_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_miss_ratio(obs, fct)

    benchmark(inner)


def test_calc_binary_accuracy_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_binary_accuracy_ratio(obs, fct)

    benchmark(inner)


def test_calc_false_alarm_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_false_alarm_ratio(obs, fct)

    benchmark(inner)


def test_calc_false_alarm_rate_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_false_alarm_rate(obs, fct)

    benchmark(inner)


def test_calc_ts_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_ts(obs, fct)

    benchmark(inner)


def test_calc_ets_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_ets(obs, fct)

    benchmark(inner)


def test_calc_bias_score_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    obs[obs > 0.5] = True
    obs[obs <= 0.5] = False
    obs = obs.astype(bool)

    fct[fct > 0.5] = True
    fct[fct <= 0.5] = False
    fct = fct.astype(bool)

    def inner():
        calc_bias_score(obs, fct)

    benchmark(inner)


def test_calc_diff_accuracy_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_diff_accuracy_ratio(obs, fct, 0.3)

    benchmark(inner)


def test_calc_rmse_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_rmse(obs, fct)

    benchmark(inner)


def test_calc_rss_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_rss(obs, fct)

    benchmark(inner)


def test_calc_chi_square_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_chi_square(obs, fct)

    benchmark(inner)


def test_calc_linregress_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_linregress(obs, fct)

    benchmark(inner)


def test_calc_threshold_accuracy_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_accuracy_ratio(obs, fct, 0.7)

    benchmark(inner)


def test_calc_threshold_miss_ratio_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_miss_ratio(obs, fct, 0.7)

    benchmark(inner)


def test_calc_threshold_bias_score_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_bias_score(obs, fct, 0.7)

    benchmark(inner)


def test_calc_threshold_mae_1e7(benchmark):
    # thousand level
    obs = np.random.rand(int(1e7))
    fct = np.random.rand(int(1e7))

    def inner():
        calc_threshold_mae(obs, fct, 0.7)

    benchmark(inner)
