import numpy as np

FALSE_ALARM_RATE_CASE = [
    {"obs": [False, False, False, False], "fct": [2, 0, 0, 0], "result": 25},
    {
        "obs": [False, False, False, False],
        "fct": [True, False, False, False],
        "result": 25,
    },
    {"obs": [0, 0, 0, 0], "fct": [2, 0, 0, 0], "result": 25},
    {"obs": [0, 0.5, 0, 0], "fct": [2.1, 0, 0, 0], "result": 33.33},
    {"obs": [1, 2, 3, 4], "fct": [0, 0, 0, 0], "result": np.nan},
    {"obs": [1, 2, 3, 4], "fct": [4, 3, 2, 1], "result": np.nan},
    {"obs": [1, 2, 3, 0], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": [1, 2, 3, 1], "fct": [2, 0, 0, 0], "result": np.nan},
    {"obs": np.array([1, 2, 3, 1]), "fct": [2, 0, 0, 0], "result": np.nan},
    {"obs": np.array([1, 2, 3, 1]), "fct": np.array([2, 0, 0, 0]), "result": np.nan},
    {"obs": [1, 2, 3, 1], "fct": np.array([2, 0, 0, 0]), "result": np.nan},
    {"obs": [0, 2, 0, 1], "fct": np.array([2, 0, 0, 0]), "result": 50},
]

FALSE_ALARM_RATIO_CASE = [
    {"obs": [False, False, False, False], "fct": [2, 0, 0, 0], "result": 100},
    {
        "obs": [False, False, False, False],
        "fct": [True, False, False, False],
        "result": 100,
    },
    {"obs": [0, 0, 0, 0], "fct": [2, 0, 0, 0], "result": 100},
    {"obs": [0, 0.5, 0, 0], "fct": [2.1, 0, 0, 0], "result": 100},
    {"obs": [1, 2, 3, 4], "fct": [0, 0, 0, 0], "result": np.nan},
    {"obs": [1, 2, 3, 4], "fct": [4, 3, 2, 1], "result": 0},
    {"obs": [1, 2, 3, 0], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": [1, 2, 3, 1], "fct": [2, 0, 0, 0], "result": 0},
    {"obs": np.array([1, 2, 3, 1]), "fct": [2, 0, 0, 0], "result": 0},
    {"obs": np.array([1, 2, 3, 1]), "fct": np.array([2, 0, 0, 0]), "result": 0},
    {"obs": [1, 2, 3, 1], "fct": np.array([2, 0, 0, 0]), "result": 0},
    {"obs": [1, 0, 0, 1], "fct": np.array([2, 0, 2, 0]), "result": 50},
]
