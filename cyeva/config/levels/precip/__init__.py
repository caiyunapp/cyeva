"""
This is the module to store precipitation's level constants.

* PRECIP_LEVELS: Precipitation's levels thresholds for 1 hour, 3 hours and 24 hours.
* ACC_PRECIP_LEVELS: Accumulated precipitation's levels thresholds for 1 hour, 
                     3 hours and 24 hours.
"""

import numpy as np

PRECIP_LEVELS = {
    "1h": {
        1: {"min": 0.1, "max": 1.9, "text": "light_rain"},
        2: {"min": 2, "max": 4.9, "text": "moderate_rain"},
        3: {"min": 5, "max": 9.9, "text": "heavy_rain"},
        4: {"min": 10, "max": 19.9, "text": "violent_rain"},
        5: {"min": 20, "max": np.inf, "text": "severe_violent_rain"},
    },
    "3h": {
        1: {"min": 0.1, "max": 2.9, "text": "light_rain"},
        2: {"min": 3, "max": 9.9, "text": "moderate_rain"},
        3: {"min": 10, "max": 19.9, "text": "heavy_rain"},
        4: {"min": 20, "max": 49.9, "text": "violent_rain"},
        5: {"min": 50, "max": 69.9, "text": "severe_violent_rain"},
        6: {"min": 70, "max": np.inf, "text": "super_severe_violent_rain"},
    },
    "12h": {
        1: {"min": 0.1, "max": 4.9, "text": "light_rain"},
        2: {"min": 5, "max": 14.9, "text": "moderate_rain"},
        3: {"min": 15, "max": 29.9, "text": "heavy_rain"},
        4: {"min": 30, "max": 69.9, "text": "violent_rain"},
        5: {"min": 70, "max": 139.9, "text": "severe_violent_rain"},
        6: {"min": 140, "max": np.inf, "text": "super_severe_violent_rain"},
    },
    "24h": {
        1: {"min": 0.1, "max": 9.9, "text": "light_rain"},
        2: {"min": 10, "max": 24.9, "text": "moderate_rain"},
        3: {"min": 25, "max": 49.9, "text": "heavy_rain"},
        4: {"min": 50, "max": 99.9, "text": "violent_rain"},
        5: {"min": 100, "max": 249.9, "text": "severe_violent_rain"},
        6: {"min": 250, "max": np.inf, "text": "super_severe_violent_rain"},
    },
}

ACC_PRECIP_LEVELS = {
    "1h": {
        1: {"min": 0.1, "max": np.inf, "text": "light_rain"},
        2: {"min": 2, "max": np.inf, "text": "moderate_rain"},
        3: {"min": 5, "max": np.inf, "text": "heavy_rain"},
        4: {"min": 10, "max": np.inf, "text": "violent_rain"},
        5: {"min": 20, "max": np.inf, "text": "severe_violent_rain"},
    },
    "3h": {
        1: {"min": 0.1, "max": np.inf, "text": "light_rain"},
        2: {"min": 3, "max": np.inf, "text": "moderate_rain"},
        3: {"min": 10, "max": np.inf, "text": "heavy_rain"},
        4: {"min": 20, "max": np.inf, "text": "violent_rain"},
        5: {"min": 50, "max": np.inf, "text": "severe_violent_rain"},
        6: {"min": 70, "max": np.inf, "text": "super_severe_violent_rain"},
    },
    "12h": {
        1: {"min": 0.1, "max": np.inf, "text": "light_rain"},
        2: {"min": 5, "max": np.inf, "text": "moderate_rain"},
        3: {"min": 15, "max": np.inf, "text": "heavy_rain"},
        4: {"min": 30, "max": np.inf, "text": "violent_rain"},
        5: {"min": 70, "max": np.inf, "text": "severe_violent_rain"},
        6: {"min": 140, "max": np.inf, "text": "super_severe_violent_rain"},
    },
    "24h": {
        1: {"min": 0.1, "max": np.inf, "text": "light_rain"},
        2: {"min": 10, "max": np.inf, "text": "moderate_rain"},
        3: {"min": 25, "max": np.inf, "text": "heavy_rain"},
        4: {"min": 50, "max": np.inf, "text": "violent_rain"},
        5: {"min": 100, "max": np.inf, "text": "severe_violent_rain"},
        6: {"min": 250, "max": np.inf, "text": "super_severe_violent_rain"},
    },
}
