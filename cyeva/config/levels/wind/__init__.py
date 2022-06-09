"""
This is the module to store wind speed level constants.

* GENERAL_WIND_SCALES: Wind speed levels thresholds.
"""

import numpy as np

GENERAL_WIND_SCALES = {
    0: {"min": 0, "max": 0.2},
    1: {"min": 0.2, "max": 1.5},
    2: {"min": 1.5, "max": 3.3},
    3: {"min": 3.3, "max": 5.4},
    4: {"min": 5.4, "max": 7.9},
    5: {"min": 7.9, "max": 10.7},
    6: {"min": 10.7, "max": 13.8},
    7: {"min": 13.8, "max": 17.1},
    8: {"min": 17.1, "max": 20.7},
    9: {"min": 20.7, "max": 24.4},
    10: {"min": 24.4, "max": 28.4},
    11: {"min": 28.4, "max": 32.6},
    12: {"min": 32.6, "max": 36.9},
    13: {"min": 36.9, "max": 41.4},
    14: {"min": 41.4, "max": 46.1},
    15: {"min": 46.1, "max": 50.9},
    16: {"min": 50.9, "max": 56.0},
    17: {"min": 56.0, "max": np.inf},
}
