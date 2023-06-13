import numpy as np

TS_SCORE_CASE = [
    {"obs": [False, False, False, False], "fct": [2, 0, 0, 0], "result": 0},
    {
        "obs": [False, False, False, False],
        "fct": [True, False, False, False],
        "result": 0,
    },
    {"obs": [0, 0, 0, 0], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": [0, 0.5, 0, 0], "fct": [2.1, 0, 0, 0], "result": 0},
    {"obs": [1, 2, 3, 4], "fct": [0, 0, 0, 0], "result": 0},
    {"obs": [1, 2, 3, 4], "fct": [4, 3, 2, 1], "result": 1},
    {"obs": [1, 2, 3, 0], "fct": [2, 0, 0, 0], "result": 0.33},
    {"obs": [1, 2, 3, 1], "fct": [2, 0, 0, 0], "result": 0.25},
    {"obs": np.array([1, 2, 3, 1]), "fct": [2, 0, 0, 0], "result": 0.25},
    {"obs": np.array([1, 2, 3, 1]), "fct": np.array([2, 0, 0, 0]), "result": 0.25},
    {"obs": [1, 2, 3, 1], "fct": np.array([2, 0, 0, 0]), "result": 0.25},
]
