import numpy as np

INTERVAL_BIAS_SCORE_CASE = {
    "1h": {
        1: [
            {"obs": [0.5, 0, 0.5, 0], "fct": [0.6, 0.6, 0, 0], "result": 1},
            {"obs": [0.5, 0, 5, 0], "fct": [0.6, 6, 0, 0], "result": 1},
        ],
        2: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": 0.5},
            {"obs": [2.1, 2.4, 0, 0], "fct": [2.2, 0, 10, 0], "result": 0.5},
        ],
    }
}
