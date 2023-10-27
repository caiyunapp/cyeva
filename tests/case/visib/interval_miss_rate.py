import numpy as np

INTERVAL_MISS_RATE_CASE = {
    "1h": {
        1: [
            {"obs": [0.5, 0, 0.5, 0], "fct": [0.6, 0.6, 0, 0], "result": 33.33},
            {"obs": [0.5, 0, 5, 0], "fct": [0.6, 6, 0, 0], "result": 0},
        ],
        2: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": 25},
            {"obs": [2.1, 2.4, 0, 2.2], "fct": [2.2, 0, 10, 0], "result": 50},
        ],
    }
}
