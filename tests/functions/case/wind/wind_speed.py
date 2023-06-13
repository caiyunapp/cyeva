import numpy as np

IDENTIFY_SPEED_LEVEL_GENERAL_CASE = [
    {"wspd": 0.1, "result": 0},
    {"wspd": 8.1, "result": 5},
    {"wspd": 38, "result": 13},
    {"wspd": [38, 8.1], "result": np.array([13, 5])},
]

IDENTIFY_SPEED_LEVEL_MAPPING_CASE = [
    {"wspd": 0.9, "result": {0, 1, 2}},
    {"wspd": 9.4, "result": {5, 6}},
    {"wspd": 35, "result": {12, 13}},
]

LEAST_LEV_DEFLECTION_CASE = [
    {"lev1": 0, "lev2": 1, "result": 1},
    {"lev1": 0, "lev2": 13, "result": 13},
    {"lev1": 1, "lev2": 13, "result": 12},
    {"lev1": 2, "lev2": 13, "result": 11},
    {"lev1": 2, "lev2": 12, "result": 10},
    {"lev1": 3, "lev2": 12, "result": 9},
]

WIND_SPEED_SCORE_CASE = [
    {"obs": [0.1, 0.1, 0.1, 0.1], "fct": [0.1, 0.4, 1.7, 3.5], "result": 0.5},
    {"obs": [0.1, 0.1, 0.1, 0.1], "fct": [0.0, 0.4, 1.7, 3.5], "result": 0.5},
    {"obs": [0.1, 0.1, 0.1, 0.1], "fct": [0.1, 0.1, 0.1, 0.1], "result": 1},
    {"obs": [38, 38, 38, 38], "fct": [0.1, 0.1, 0.1, 0.1], "result": 0},
]

WIND_LEVEL_ACCURACY_RATE_CASE = [
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.1, 8.1, 38, 0], "result": 25},
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.1, 8.1, 0, 0], "result": 25},
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.1, 0, 0, 0], "result": 0},
]

WIND_SPEED_ACCURACY_RATE_CASE = [
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.1, 8.1, 37, 0], "result": 75},
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.1, 8.1, 38, 0], "result": 50},
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.1, 7, 0, 0], "result": 25},
]

WIND_SPEED_MAE_CASE = [
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.9, 9.4, 35, 38], "result": 0},
    {"obs": [0.9, 9.4, 35, 38], "fct": [1.9, 10.4, 34, 37], "result": 1},
]

WIND_SPEED_STRONGER_RATE_CASE = [
    {"obs": [0.9, 9.4, 20, 20], "fct": [10, 20, 50, 50], "result": 100},
    {"obs": [0.9, 9.4, 20, 20], "fct": [1, 20, 50, 30], "result": 75},
    {"obs": [0.9, 9.4, 20, 20], "fct": [0.1, 7, 0, 0], "result": 0},
]

WIND_SPEED_WEAKER_RATE_CASE = [
    {"obs": [10, 20, 50, 50], "fct": [0.9, 9.4, 20, 20], "result": 100},
    {"obs": [10, 20, 50, 50], "fct": [10, 9.4, 20, 20], "result": 75},
    {"obs": [0.1, 7, 0, 0], "fct": [0.9, 9.4, 20, 20], "result": 0},
]

WIND_SPEED_CHI_SQUARE_CASE = [
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.9, 9.4, 35, 38], "result": 0},
    {"obs": [0.9, 9.4, 35, 38], "fct": [1.9, 10.4, 34, 37], "result": 1},
]

WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE = [
    {"obs": [0.9, 9.4, 35, 38], "fct": [0.9, 9.4, 35, 38], "result": 0},
    {"obs": [0.9, 9.4, 35, 38], "fct": [1.9, 10.4, 34, 37], "result": 4},
]

WIND_SPEED_LINREGRESS_CASE = [
    {"obs": [1, 2, 3, 4], "fct": [1, 2, 3, 4], "result": {"slope": 1, "intercept": 0}},
    {"obs": [1, 2, 3, 4], "fct": [4, 3, 2, 1], "result": {"slope": -1, "intercept": 5}},
]
