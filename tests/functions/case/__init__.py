import numpy as np

RMSE_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 0},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 2.7386},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 2.1602,
    },
]

MAE_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 0},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 2.5},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 2,
    },
]

CHI_SQUARE_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 0},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 7.5},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 4.6667,
    },
]

MEAN_RESIDUAL_SUM_OF_SQUARE_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 0},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 1.875},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 1.5556,
    },
]

RESIDUAL_SUM_OF_SQUARE_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 0},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 30},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 14,
    },
]

LINREGRESS_ARGS_CASE = [
    {
        "obs": np.array([1, 2, 3, 0]),
        "fct": np.array([1, 2, 3, 0]),
        "result": (1.0, 0.0, 1.0, 0.0),
    },
    {
        "obs": np.array([1, 2, 0, 0]),
        "fct": np.array([0, 0, 3, 4]),
        "result": (-0.4118, 1.4706, -0.8866, 0.1134),
    },
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": (-0.5, 1.5, -0.866, 0.3333),
    },
]

BINARY_ACCURACY_RATIO_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 100.0},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 0},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 0,
    },
]

BIAS_CASE = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 1},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 1},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 0.5,
    },
]


DIFF_ACCURACY_RATIO = [
    {"obs": np.array([1, 2, 3, 0]), "fct": np.array([1, 2, 3, 0]), "result": 100},
    {"obs": np.array([1, 2, 0, 0]), "fct": np.array([0, 0, 3, 4]), "result": 25},
    {
        "obs": np.array([1, 2, 0, np.nan]),
        "fct": np.array([0, 0, 3, 4]),
        "result": 33.3333,
    },
]
