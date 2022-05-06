import numpy as np

PRECIP_LEVELS = {
    "1h": {
        1: {"min": 0.1, "max": 1.9, "text": "小雨"},
        2: {"min": 2, "max": 4.9, "text": "中雨"},
        3: {"min": 5, "max": 9.9, "text": "大雨"},
        4: {"min": 10, "max": 19.9, "text": "暴雨"},
        5: {"min": 20, "max": np.inf, "text": "大暴雨"},
    },
    "3h": {
        1: {"min": 0.1, "max": 2.9, "text": "小雨"},
        2: {"min": 3, "max": 9.9, "text": "中雨"},
        3: {"min": 10, "max": 19.9, "text": "大雨"},
        4: {"min": 20, "max": 49.9, "text": "暴雨"},
        5: {"min": 50, "max": 69.9, "text": "大暴雨"},
        6: {"min": 70, "max": np.inf, "text": "特大暴雨"},
    },
    "24h": {
        1: {"min": 0.1, "max": 9.9, "text": "小雨"},
        2: {"min": 10, "max": 24.9, "text": "中雨"},
        3: {"min": 25, "max": 49.9, "text": "大雨"},
        4: {"min": 50, "max": 99.9, "text": "暴雨"},
        5: {"min": 100, "max": 249.9, "text": "大暴雨"},
        6: {"min": 250, "max": np.inf, "text": "特大暴雨"},
    },
}
