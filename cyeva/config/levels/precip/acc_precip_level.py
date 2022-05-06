import numpy as np

ACC_PRECIP_LEVELS = {
    "1h": {
        1: {"min": 0.1, "max": np.inf, "text": "小雨"},
        2: {"min": 2, "max": np.inf, "text": "中雨"},
        3: {"min": 5, "max": np.inf, "text": "大雨"},
        4: {"min": 10, "max": np.inf, "text": "暴雨"},
        5: {"min": 20, "max": np.inf, "text": "大暴雨"},
    },
    "3h": {
        1: {"min": 0.1, "max": np.inf, "text": "小雨"},
        2: {"min": 3, "max": np.inf, "text": "中雨"},
        3: {"min": 10, "max": np.inf, "text": "大雨"},
        4: {"min": 20, "max": np.inf, "text": "暴雨"},
        5: {"min": 50, "max": np.inf, "text": "大暴雨"},
        6: {"min": 70, "max": np.inf, "text": "特大暴雨"},
    },
    "24h": {
        1: {"min": 0.1, "max": np.inf, "text": "小雨"},
        2: {"min": 10, "max": np.inf, "text": "中雨"},
        3: {"min": 25, "max": np.inf, "text": "大雨"},
        4: {"min": 50, "max": np.inf, "text": "暴雨"},
        5: {"min": 100, "max": np.inf, "text": "大暴雨"},
        6: {"min": 250, "max": np.inf, "text": "特大暴雨"},
    },
}
