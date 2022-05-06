import numpy as np

FRQ_PRECIP_LEVELS = {
    "1h": {
        1: {"min": 0.1, "max": 0.9},
        2: {"min": 1, "max": 1.9},
        3: {"min": 2, "max": 2.9},
        4: {"min": 3, "max": 4.9},
        5: {"min": 5, "max": np.inf},
    },
    "3h": {
        1: {"min": 0.1, "max": 0.9},
        2: {"min": 1, "max": 1.9},
        3: {"min": 2, "max": 2.9},
        4: {"min": 3, "max": 4.9},
        5: {"min": 5, "max": np.inf},
    },
    "24h": {
        1: {"min": 0.1, "max": 2.4},
        2: {"min": 2.5, "max": 4.9},
        3: {"min": 5, "max": 9.9},
        4: {"min": 10, "max": np.inf},
    },
}

OCR_FRQ_PRECIP_LEVELS = {
    "1h": {
        1: {"min": 0.1, "max": np.inf},
        2: {"min": 1, "max": np.inf},
        3: {"min": 2, "max": np.inf},
        4: {"min": 3, "max": np.inf},
        5: {"min": 5, "max": np.inf},
    },
    "3h": {
        1: {"min": 0.1, "max": np.inf},
        2: {"min": 1, "max": np.inf},
        3: {"min": 2, "max": np.inf},
        4: {"min": 3, "max": np.inf},
        5: {"min": 5, "max": np.inf},
    },
    "24h": {
        1: {"min": 0.1, "max": np.inf},
        2: {"min": 2.5, "max": np.inf},
        3: {"min": 5, "max": np.inf},
        4: {
            "min": 50,
            "max": np.inf,
        },
        5: {"min": 10, "max": np.inf},
    },
}
