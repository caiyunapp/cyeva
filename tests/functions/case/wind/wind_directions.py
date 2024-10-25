import numpy as np
from pint import Unit

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
    {"angle": 22.5, "result": 0},
    {"angle": 22.6, "result": 1},
    {"angle": 67.5, "result": 1},
    {"angle": 67.6, "result": 2},
    {"angle": 112.5, "result": 2},
    {"angle": 112.6, "result": 3},
    {"angle": 157.5, "result": 3},
    {"angle": 157.6, "result": 4},
    {"angle": 202.5, "result": 4},
    {"angle": 202.6, "result": 5},
    {"angle": 247.5, "result": 5},
    {"angle": 247.6, "result": 6},
    {"angle": 292.5, "result": 6},
    {"angle": 292.6, "result": 7},
    {"angle": 337.5, "result": 7},
    {"angle": 337.6, "result": 0},
    {
        "angle": np.array(
            [
                22.5,
                22.6,
                67.5,
                67.6,
                112.5,
                112.6,
                157.5,
                157.6,
                202.5,
                202.6,
                247.5,
                247.6,
                292.5,
                292.6,
                337.5,
                337.6,
                359,
                1,
            ]
        )
        * Unit("degree"),
        "result": np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 0]),
    },
]

IDENTIFY_DIRECTION16_CASE = [
    {"angle": 22, "result": 1},
    {"angle": 23, "result": 1},
    {"angle": 91, "result": 4},
    {"angle": 350, "result": 0},
    {"angle": 348.76, "result": 0},
    {"angle": 11.25, "result": 0},
    {"angle": 11.26, "result": 1},
    {"angle": 33.75, "result": 1},
    {"angle": 33.76, "result": 2},
    {"angle": 56.25, "result": 2},
    {"angle": 56.26, "result": 3},
    {"angle": 78.75, "result": 3},
    {"angle": 78.76, "result": 4},
    {"angle": 101.25, "result": 4},
    {"angle": 101.26, "result": 5},
    {"angle": 123.75, "result": 5},
    {"angle": 123.76, "result": 6},
    {"angle": 146.25, "result": 6},
    {"angle": 146.26, "result": 7},
    {"angle": 168.75, "result": 7},
    {"angle": 168.76, "result": 8},
    {"angle": 191.25, "result": 8},
    {"angle": 191.26, "result": 9},
    {"angle": 213.75, "result": 9},
    {"angle": 213.76, "result": 10},
    {"angle": 236.25, "result": 10},
    {"angle": 236.26, "result": 11},
    {"angle": 258.75, "result": 11},
    {"angle": 258.76, "result": 12},
    {"angle": 281.25, "result": 12},
    {"angle": 281.26, "result": 13},
    {"angle": 303.75, "result": 13},
    {"angle": 303.76, "result": 14},
    {"angle": 326.25, "result": 14},
    {"angle": 326.26, "result": 15},
    {"angle": 348.75, "result": 15},
    {
        "angle": np.array(
            [
                348.76,
                11.25,
                11.26,
                33.75,
                33.76,
                56.25,
                56.26,
                78.75,
                78.76,
                101.25,
                101.26,
                123.75,
                123.76,
                146.25,
                146.26,
                168.75,
                168.76,
                191.25,
                191.26,
                213.75,
                213.76,
                236.25,
                236.26,
                258.75,
                258.76,
                281.25,
                281.26,
                303.75,
                303.76,
                326.25,
                326.26,
                348.75,
            ]
        )
        * Unit("degree"),
        "result": np.array(
            [
                0,
                0,
                1,
                1,
                2,
                2,
                3,
                3,
                4,
                4,
                5,
                5,
                6,
                6,
                7,
                7,
                8,
                8,
                9,
                9,
                10,
                10,
                11,
                11,
                12,
                12,
                13,
                13,
                14,
                14,
                15,
                15,
            ]
        ),
    },
]

LEAST_DIR_DEFLECTION_CASE = [
    {"dir1": 0, "dir2": 1, "result": 1},
    {"dir1": 0, "dir2": 7, "result": 1},
    {"dir1": 1, "dir2": 7, "result": 2},
    {"dir1": 2, "dir2": 7, "result": 3},
    {"dir1": 2, "dir2": 6, "result": 4},
    {"dir1": 3, "dir2": 6, "result": 3},
    {"dir1": [3, 2], "dir2": [6, 6], "result": np.array([3, 4])},
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