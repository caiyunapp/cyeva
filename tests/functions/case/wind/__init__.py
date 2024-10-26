import numpy as np

from .wind_directions import (
    IDENTIFY_DIRECTION8_CASE,
    IDENTIFY_DIRECTION16_CASE,
    LEAST_ANGLE_DEFLECTION_CASE,
    LEAST_DIR_DEFLECTION_CASE,
    WIND_DIR_ACCURACY_RATE,
    WIND_DIR_SCORE_CASE,
)
from .wind_speed import (
    IDENTIFY_SPEED_LEVEL_GENERAL_CASE,
    IDENTIFY_SPEED_LEVEL_MAPPING_CASE,
    LEAST_LEV_DEFLECTION_CASE,
    WIND_LEVEL_ACCURACY_RATE_CASE,
    WIND_SPEED_ACCURACY_RATE_CASE,
    WIND_SPEED_CHI_SQUARE_CASE,
    WIND_SPEED_LINREGRESS_CASE,
    WIND_SPEED_MAE_CASE,
    WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE,
    WIND_SPEED_SCORE_CASE,
    WIND_SPEED_STRONGER_RATE_CASE,
    WIND_SPEED_WEAKER_RATE_CASE,
)

FILTER_WIND_SCALES_CASE = [
    {
        "obs": np.array(
            [
                5.96475312,
                2.9787626,
                3.8667877,
                14.75895423,
                8.48229788,
                10.05979194,
                0.47507922,
                6.50696602,
                16.67486185,
                14.4919493,
            ]
        ),
        "fct": np.array(
            [
                16.238759,
                10.40696757,
                8.82104982,
                3.61639317,
                5.3269034,
                10.9892586,
                7.59016338,
                17.7476437,
                15.76840345,
                1.84942086,
            ]
        ),
        "arg_cases": [
            {
                "parameters": {"scale_min": 3, "scale_max": 5, "return_index": False},
                "result": (np.array([3.9, 8.5]), np.array([8.8, 5.3])),
            },
            {
                "parameters": {"scale_min": 3, "scale_max": 5, "return_index": True},
                "result": (np.array([2, 4]),),
            },
            {
                "parameters": {"scale_min": 4, "scale_max": 10, "return_index": False},
                "result": (
                    np.array([6.0, 10.1, 6.5, 16.7]),
                    np.array([16.2, 11.0, 17.7, 15.8]),
                ),
            },
            {
                "parameters": {"scale_min": 4, "scale_max": 10, "return_index": True},
                "result": (np.array([0, 5, 7, 8]),),
            },
            {
                "parameters": {
                    "scale_min": 5,
                    "scale_max": np.inf,
                    "return_index": False,
                },
                "result": (np.array([10.1, 16.7]), np.array([11.0, 15.8])),
            },
            {
                "parameters": {
                    "scale_min": 5,
                    "scale_max": np.inf,
                    "return_index": True,
                },
                "result": (np.array([5, 8]),),
            },
            {
                "parameters": {
                    "scale_min": 0,
                    "scale_max": 4,
                    "return_index": False,
                },
                "result": (np.array([0.5]), np.array([7.6])),
            },
            {
                "parameters": {
                    "scale_min": 0,
                    "scale_max": 4,
                    "return_index": True,
                },
                "result": (np.array([6]),),
            },
            {
                "parameters": {
                    "scale_min": 0,
                    "scale_max": 4,
                    "return_index": False,
                    "mode": "or",
                },
                "result": (
                    np.array([6.0, 3.0, 3.9, 14.8, 8.5, 0.5, 6.5, 14.5]),
                    np.array([16.2, 10.4, 8.8, 3.6, 5.3, 7.6, 17.7, 1.8]),
                ),
            },
            {
                "parameters": {
                    "scale_min": 0,
                    "scale_max": 4,
                    "return_index": True,
                    "mode": "or",
                },
                "result": (np.array([0, 1, 2, 3, 4, 6, 7, 9]),),
            },
            {
                "parameters": {
                    "scale_min": 8,
                    "return_index": False,
                    "mode": "or",
                },
                "result": (np.array([6.5]), np.array([17.7])),
            },
            {
                "parameters": {
                    "scale_min": 8,
                    "return_index": True,
                    "mode": "or",
                },
                "result": (np.array([7]),),
            },
            {
                "parameters": {
                    "scale_min": 6,
                    "mode": "or",
                },
                "result": (
                    np.array([6.0, 14.8, 10.1, 6.5, 16.7, 14.5]),
                    np.array([16.2, 3.6, 11.0, 17.7, 15.8, 1.8]),
                ),
            },
            {
                "parameters": {
                    "scale_min": 6,
                    "mode": "and",
                },
                "result": (np.array([16.7]), np.array([15.8])),
            },
        ],
    },
]


__all__ = [
    "IDENTIFY_DIRECTION8_CASE",
    "IDENTIFY_DIRECTION16_CASE",
    "LEAST_ANGLE_DEFLECTION_CASE",
    "LEAST_DIR_DEFLECTION_CASE",
    "WIND_DIR_ACCURACY_RATE",
    "WIND_DIR_SCORE_CASE",
    "IDENTIFY_SPEED_LEVEL_GENERAL_CASE",
    "IDENTIFY_SPEED_LEVEL_MAPPING_CASE",
    "LEAST_LEV_DEFLECTION_CASE",
    "WIND_LEVEL_ACCURACY_RATE_CASE",
    "WIND_SPEED_ACCURACY_RATE_CASE",
    "WIND_SPEED_CHI_SQUARE_CASE",
    "WIND_SPEED_LINREGRESS_CASE",
    "WIND_SPEED_MAE_CASE",
    "WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE",
    "WIND_SPEED_SCORE_CASE",
    "WIND_SPEED_STRONGER_RATE_CASE",
    "WIND_SPEED_WEAKER_RATE_CASE",
    "FILTER_WIND_SCALES_CASE",
]
