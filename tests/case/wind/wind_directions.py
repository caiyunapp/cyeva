import numpy as np

LEAST_ANGLE_DEFLECTION_CASE = [
    {"angle1": 2, "angle2": 358, "result": 4},
    {"angle1": 89, "angle2": 271, "result": 178},
    {"angle1": 91, "angle2": 269, "result": 178},
]

IDENTIFY_DIRECTION8_CASE = [
    {"angle": 22, "result": 0},
    {"angle": 23, "result": 1},
    {"angle": 91, "result": 2},
    {"angle": 350, "result": 0},
]

LEAST_DIR_DEFLECTION_CASE = [
    {"dir1": 0, "dir2": 1, "result": 1},
    {"dir1": 0, "dir2": 7, "result": 1},
    {"dir1": 1, "dir2": 7, "result": 2},
    {"dir1": 2, "dir2": 7, "result": 3},
    {"dir1": 2, "dir2": 6, "result": 4},
    {"dir1": 3, "dir2": 6, "result": 3},
]

WIND_DIR_SCORE_CASE = [
    {"obs": [0, 45, 90, 180], "fct": [0, 45, 90, 180], "result": 1},
    {"obs": [0, 45, 90, 180], "fct": [25, 45, 90, 180], "result": 0.9},
    {"obs": [22, 45, 90, 180], "fct": [25, 45, 90, 180], "result": 0.9},
    {"obs": [22, 45, 90, 180], "fct": [25, 80, 90, 180], "result": 0.8},
]

WIND_DIR_ACCURACY_RATE = [
    {"obs": [0, 45, 90, 180], "fct": [0, 45, 90, 180], "result": 100},
    {"obs": [0, 45, 45, 180], "fct": [25, 45, 90, 180], "result": 50},
    {"obs": [22, 45, 90, 0], "fct": [25, 45, 90, 180], "result": 75},
]
