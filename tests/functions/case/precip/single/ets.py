import numpy as np

ETS_SCORE_CASE = [
    {"obs": [False, False, False, False], "fct": [2, 0, 0, 0], "result": 0},
    {
        "obs": [False, False, False, False],
        "fct": [True, False, False, False],
        "result": 0,
    },
    {"obs": [0, 0, 0, 0], "fct": [0, 0, 0, 0], "result": np.nan},
    {"obs": [0, 0, 0, 0], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": [1, 1, 1, 1], "fct": [1, 1, 1, 1], "result": np.nan},
    {"obs": [0, 0.5, 0, 0], "fct": [2.1, 0, 0, 0], "result": -0.14},
    {"obs": [1, 2, 3, 4], "fct": [0, 0, 0, 0], "result": 0},
    {"obs": [1, 2, 0, 0], "fct": [1, 2, 0, 0], "result": 1},
    {"obs": [1, 2, 3, 4], "fct": [4, 3, 2, 1], "result": np.nan},
    {"obs": [1, 2, 3, 0], "fct": [2, 0, 0, 0], "result": 0.11},
    {"obs": [1, 2, 3, 1], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": np.array([1, 2, 3, 1]), "fct": [2, 0, 0, 0], "result": 0},
    {"obs": np.array([1, 2, 3, 1]), "fct": np.array([2, 0, 0, 0]), "result": 0},
    {"obs": [1, 2, 3, 1], "fct": np.array([2, 0, 0, 0]), "result": 0},
]
