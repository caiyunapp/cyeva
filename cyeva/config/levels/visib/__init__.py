import numpy as np

VISIB_LEVELS = {
    "1h": {
        1: {"min": 0, "max": 1000},
        2: {"min": 1000, "max": 5000},
        3: {"min": 5000, "max": 10000},
        4: {"min": 10000, "max": np.inf},
    },
    "3h": {
        1: {"min": 0, "max": 1000},
        2: {"min": 1000, "max": 5000},
        3: {"min": 5000, "max": 10000},
        4: {"min": 10000, "max": np.inf},
    },
    "24h": {
        1: {"min": 0, "max": 1000},
        2: {"min": 1000, "max": 5000},
        3: {"min": 5000, "max": 10000},
        4: {"min": 10000, "max": np.inf},
    },
}

SENS_VISIB_LEVELS = {
    1: {"compare": "<=", "threshold": 1000},
    2: {"compare": "<=", "threshold": 500},
    3: {"compare": "<=", "threshold": 100},
}
