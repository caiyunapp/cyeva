import numpy as np

ACC_MISS_RATIO_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 1], "fct": [1.4, 10, 0, 0], "result": 50},
            {"obs": [1.1, 1.2, 1.3, 1], "fct": [0, 10, 0, 0], "result": 75},
        ],
        2: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": 0},
            {"obs": [2.1, 2.4, 0, 0], "fct": [2.2, 0, 10, 0], "result": 50},
            {"obs": [2.1, 2.4, 2.2, 0], "fct": [2.2, 0, 10, 0], "result": 33.33},
            {"obs": [2.1, 2.4, 2.2, 3], "fct": [2.2, 0, 10, 0], "result": 50},
            {"obs": [2.1, 2.4, 2.2, 3], "fct": [0, 0, 10, 0], "result": 75},
        ],
        3: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": np.nan},
            {"obs": [5.1, 1, 0, 0], "fct": [5.2, 0, 10, 0], "result": 0},
            {"obs": [5.1, 5.4, 0, 0], "fct": [5.2, 0, 10, 0], "result": 50},
            {"obs": [5.1, 5.4, 5.2, 0], "fct": [5.2, 0, 10, 0], "result": 33.33},
            {"obs": [5.1, 5.4, 5.2, 6], "fct": [5.2, 0, 10, 0], "result": 50},
            {"obs": [5.1, 5.4, 5.2, 6], "fct": [0, 0, 10, 0], "result": 75},
        ],
        4: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": np.nan},
            {"obs": [10.1, 1, 0, 0], "fct": [10.2, 0, 10, 0], "result": 0},
            {"obs": [10.1, 10.4, 0, 0], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 10.4, 10.2, 0], "fct": [10.2, 0, 10, 0], "result": 33.33},
            {"obs": [10.1, 10.4, 10.2, 11], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 10.4, 10.2, 11], "fct": [0, 0, 10, 0], "result": 75},
        ],
        5: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 20, 0], "result": np.nan},
            {"obs": [20.1, 1, 0, 0], "fct": [20.2, 0, 20, 0], "result": 0},
            {"obs": [20.1, 20.4, 0, 0], "fct": [20.2, 0, 20, 0], "result": 50},
            {"obs": [20.1, 20.4, 20.2, 0], "fct": [20.2, 0, 20, 0], "result": 33.33},
            {"obs": [20.1, 20.4, 20.2, 21], "fct": [20.2, 0, 20, 0], "result": 50},
            {"obs": [20.1, 20.4, 20.2, 21], "fct": [0, 0, 20, 0], "result": 75},
        ],
    },
    "3h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 1.], "fct": [1.4, 10, 0, 0], "result": 50},
            {"obs": [1.1, 1.2, 1.3, 1.], "fct": [0, 10, 0, 0], "result": 75},
        ],
        2: [
            {"obs": [3.1, 1, 0, 0], "fct": [3.2, 0, 10, 0], "result": 0},
            {"obs": [3.1, 3.4, 0, 0], "fct": [3.2, 0, 10, 0], "result": 50},
            {"obs": [3.1, 3.4, 3.2, 0], "fct": [3.2, 0, 10, 0], "result": 33.33},
            {"obs": [3.1, 3.4, 3.2, 3.], "fct": [3.2, 0, 10, 0], "result": 50},
            {"obs": [3.1, 3.4, 3.2, 3.], "fct": [0, 0, 10, 0], "result": 75},
        ],
        3: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": np.nan},
            {"obs": [10.1, 1, 0, 0], "fct": [10.2, 0, 10, 0], "result": 0},
            {"obs": [10.1, 10.4, 0, 0], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 10.4, 10.2, 0], "fct": [10.2, 0, 10, 0], "result": 33.33},
            {"obs": [10.1, 10.4, 10.2, 10.], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 10.4, 10.2, 10.], "fct": [0, 0, 10, 0], "result": 75},
        ],
        4: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 20, 0], "result": np.nan},
            {"obs": [20.1, 1, 0, 0], "fct": [20.2, 0, 20, 0], "result": 0},
            {"obs": [20.1, 20.4, 0, 0], "fct": [20.2, 0, 20, 0], "result": 50},
            {"obs": [20.1, 20.4, 20.2, 0], "fct": [20.2, 0, 20, 0], "result": 33.33},
            {"obs": [20.1, 20.4, 20.2, 20.1], "fct": [20.2, 0, 20, 0], "result": 50},
            {"obs": [20.1, 20.4, 20.2, 20.1], "fct": [0, 0, 20, 0], "result": 75},
        ],
        5: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 50, 0], "result": np.nan},
            {"obs": [50.1, 1, 0, 0], "fct": [50.2, 0, 50, 0], "result": 0},
            {"obs": [50.1, 50.4, 0, 0], "fct": [50.2, 0, 50, 0], "result": 50},
            {"obs": [50.1, 50.4, 50.2, 0], "fct": [50.2, 0, 50, 0], "result": 33.33},
            {"obs": [50.1, 50.4, 50.2, 50.], "fct": [50.2, 0, 50, 0], "result": 50},
            {"obs": [50.1, 50.4, 50.2, 50.], "fct": [0, 0, 50, 0], "result": 75},
        ],
        6: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 80, 0], "result": np.nan},
            {"obs": [70.1, 1, 0, 0], "fct": [70.2, 0, 80, 0], "result": 0},
            {"obs": [70.1, 70.4, 0, 0], "fct": [70.2, 0, 80, 0], "result": 50},
            {"obs": [70.1, 70.4, 70.2, 0], "fct": [70.2, 0, 80, 0], "result": 33.33},
            {"obs": [70.1, 70.4, 70.2, 71.], "fct": [70.2, 0, 80, 0], "result": 50},
            {"obs": [70.1, 70.4, 70.2, 71.], "fct": [0, 0, 80, 0], "result": 75},
        ],
    },
    "12h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 1.], "fct": [1.4, 10, 0, 0], "result": 50},
            {"obs": [1.1, 1.2, 1.3, 1.], "fct": [0, 10, 0, 0], "result": 75},
        ],
        2: [
            {"obs": [5.1, 1, 0, 0], "fct": [5.2, 0, 10, 0], "result": 0},
            {"obs": [5.1, 5.4, 0, 0], "fct": [5.2, 0, 10, 0], "result": 50},
            {"obs": [5.1, 5.4, 5.2, 0], "fct": [5.2, 0, 10, 0], "result": 33.33},
            {"obs": [5.1, 5.4, 5.2, 5.], "fct": [5.2, 0, 10, 0], "result": 50},
            {"obs": [5.1, 5.4, 5.2, 5.], "fct": [0, 0, 10, 0], "result": 75},
        ],
        3: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 15, 0], "result": np.nan},
            {"obs": [15.1, 1, 0, 0], "fct": [15.2, 0, 15, 0], "result": 0},
            {"obs": [15.1, 15.4, 0, 0], "fct": [15.2, 0, 15, 0], "result": 50},
            {"obs": [15.1, 15.4, 15.2, 0], "fct": [15.2, 0, 15, 0], "result": 33.33},
            {"obs": [15.1, 15.4, 15.2, 15.], "fct": [15.2, 0, 15, 0], "result": 50},
            {"obs": [15.1, 15.4, 15.2, 15.], "fct": [0, 0, 15, 0], "result": 75},
        ],
        4: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 30, 0], "result": np.nan},
            {"obs": [30.1, 1, 0, 0], "fct": [30.2, 0, 30, 0], "result": 0},
            {"obs": [30.1, 30.4, 0, 0], "fct": [30.2, 0, 30, 0], "result": 50},
            {"obs": [30.1, 30.4, 30.2, 0], "fct": [30.2, 0, 30, 0], "result": 33.33},
            {"obs": [30.1, 30.4, 30.2, 30.1], "fct": [30.2, 0, 30, 0], "result": 50},
            {"obs": [30.1, 30.4, 30.2, 30.1], "fct": [0, 0, 30, 0], "result": 75},
        ],
        5: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 100, 0], "result": np.nan},
            {"obs": [70.1, 1, 0, 0], "fct": [70.2, 0, 100, 0], "result": 0},
            {"obs": [70.1, 70.4, 0, 0], "fct": [70.2, 0, 100, 0], "result": 50},
            {"obs": [70.1, 70.4, 70.2, 0], "fct": [70.2, 0, 100, 0], "result": 33.33},
            {"obs": [70.1, 70.4, 70.2, 70.], "fct": [70.2, 0, 100, 0], "result": 50},
            {"obs": [70.1, 70.4, 70.2, 70.], "fct": [0, 0, 100, 0], "result": 75},
        ],
        6: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 260, 0], "result": np.nan},
            {"obs": [140.1, 1, 0, 0], "fct": [140.2, 0, 260, 0], "result": 0},
            {"obs": [140.1, 140.4, 0, 0], "fct": [140.2, 0, 260, 0], "result": 50},
            {"obs": [140.1, 140.4, 140.2, 0], "fct": [140.2, 0, 260, 0], "result": 33.33},
            {"obs": [140.1, 140.4, 140.2, 140.], "fct": [140.2, 0, 260, 0], "result": 50},
            {"obs": [140.1, 140.4, 140.2, 140.], "fct": [0, 0, 260, 0], "result": 75},
        ],
    },
    "24h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 6, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 0], "fct": [1.4, 10, 0, 0], "result": 33.33},
            {"obs": [1.1, 1.2, 1.3, 1.], "fct": [1.4, 10, 0, 0], "result": 50},
            {"obs": [1.1, 1.2, 1.3, 1.], "fct": [0, 10, 0, 0], "result": 75},
        ],
        2: [
            {"obs": [10.1, 1, 0, 0], "fct": [10.2, 0, 10, 0], "result": 0},
            {"obs": [10.1, 10.4, 0, 0], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 10.4, 10.2, 0], "fct": [10.2, 0, 10, 0], "result": 33.33},
            {"obs": [10.1, 10.4, 10.2, 10.], "fct": [10.2, 0, 10, 0], "result": 50},
            {"obs": [10.1, 10.4, 10.2, 10.], "fct": [0, 0, 10, 0], "result": 75},
        ],
        3: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 25, 0], "result": np.nan},
            {"obs": [25.1, 1, 0, 0], "fct": [25.2, 0, 25, 0], "result": 0},
            {"obs": [25.1, 25.4, 0, 0], "fct": [25.2, 0, 25, 0], "result": 50},
            {"obs": [25.1, 25.4, 25.2, 0], "fct": [25.2, 0, 25, 0], "result": 33.33},
            {"obs": [25.1, 25.4, 25.2, 25.], "fct": [25.2, 0, 25, 0], "result": 50},
            {"obs": [25.1, 25.4, 25.2, 25.], "fct": [0, 0, 25, 0], "result": 75},
        ],
        4: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 50, 0], "result": np.nan},
            {"obs": [50.1, 1, 0, 0], "fct": [50.2, 0, 50, 0], "result": 0},
            {"obs": [50.1, 50.4, 0, 0], "fct": [50.2, 0, 50, 0], "result": 50},
            {"obs": [50.1, 50.4, 50.2, 0], "fct": [50.2, 0, 50, 0], "result": 33.33},
            {"obs": [50.1, 50.4, 50.2, 50.1], "fct": [50.2, 0, 50, 0], "result": 50},
            {"obs": [50.1, 50.4, 50.2, 50.1], "fct": [0, 0, 50, 0], "result": 75},
        ],
        5: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 100, 0], "result": np.nan},
            {"obs": [100.1, 1, 0, 0], "fct": [100.2, 0, 100, 0], "result": 0},
            {"obs": [100.1, 100.4, 0, 0], "fct": [100.2, 0, 100, 0], "result": 50},
            {"obs": [100.1, 100.4, 100.2, 0], "fct": [100.2, 0, 100, 0], "result": 33.33},
            {"obs": [100.1, 100.4, 100.2, 100.], "fct": [100.2, 0, 100, 0], "result": 50},
            {"obs": [100.1, 100.4, 100.2, 100.], "fct": [0, 0, 100, 0], "result": 75},
        ],
        6: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 260, 0], "result": np.nan},
            {"obs": [250.1, 1, 0, 0], "fct": [250.2, 0, 260, 0], "result": 0},
            {"obs": [250.1, 250.4, 0, 0], "fct": [250.2, 0, 260, 0], "result": 50},
            {"obs": [250.1, 250.4, 250.2, 0], "fct": [250.2, 0, 260, 0], "result": 33.33},
            {"obs": [250.1, 250.4, 250.2, 250.], "fct": [250.2, 0, 260, 0], "result": 50},
            {"obs": [250.1, 250.4, 250.2, 250.], "fct": [0, 0, 260, 0], "result": 75},
        ],
    },
}
