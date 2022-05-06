import numpy as np

MISS_RATE_CASE = [
    {"obs": [False, False, False, False], "fct": [2, 0, 0, 0], "result": 0},
    {
        "obs": [False, False, False, False],
        "fct": [True, False, False, False],
        "result": 0,
    },
    {"obs": [0, 0, 0, 0], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": [0, 0.5, 0, 0], "fct": [2.1, 0, 0, 0], "result": 33.33},
    {"obs": [1, 2, 3, 4], "fct": [0, 0, 0, 0], "result": 100},
    {"obs": [1, 2, 3, 4], "fct": [4, 3, 2, 1], "result": 0},
    {"obs": [1, 2, 3, 0], "fct": [2, 0, 0, 0], "result": 50},
    {"obs": [1, 2, 3, 1], "fct": [2, 0, 0, 0], "result": 75},
    {"obs": np.array([1, 2, 3, 1]), "fct": [2, 0, 0, 0], "result": 75},
    {"obs": np.array([1, 2, 3, 1]), "fct": np.array([2, 0, 0, 0]), "result": 75},
    {"obs": [1, 2, 3, 1], "fct": np.array([2, 0, 0, 0]), "result": 75},
]
