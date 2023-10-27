from .wind_directions import (
    LEAST_ANGLE_DEFLECTION_CASE,
    LEAST_DIR_DEFLECTION_CASE,
    IDENTIFY_DIRECTION8_CASE,
    WIND_DIR_SCORE_CASE,
    WIND_DIR_ACCURACY_RATE,
)
from .wind_speed import (
    IDENTIFY_SPEED_LEVEL_GENERAL_CASE,
    IDENTIFY_SPEED_LEVEL_MAPPING_CASE,
    LEAST_LEV_DEFLECTION_CASE,
    WIND_LEVEL_ACCURACY_RATE_CASE,
    WIND_SPEED_SCORE_CASE,
    WIND_SPEED_ACCURACY_RATE_CASE,
    WIND_SPEED_MAE_CASE,
    WIND_SPEED_STRONGER_RATE_CASE,
    WIND_SPEED_WEAKER_RATE_CASE,
    WIND_SPEED_CHI_SQUARE_CASE,
    WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE,
    WIND_SPEED_LINREGRESS_CASE,
)

WIND_CONPOSITE_ACCURACY_RATE_CASE = [
    {
        "obs_spd": [1, 2, 3, 4],
        "fct_spd": [1, 2, 3, 4],
        "obs_dir": [10, 10, 20, 20],
        "fct_dir": [11, 9, 19, 21],
        "result": 100,
    },
    {
        "obs_spd": [1, 2, 3, 4],
        "fct_spd": [11, 21, 31, 41],
        "obs_dir": [10, 10, 20, 20],
        "fct_dir": [110, 90, 190, 210],
        "result": 0,
    },
    {
        "obs_spd": [1, 2, 3, 4],
        "fct_spd": [1, 21, 31, 41],
        "obs_dir": [10, 10, 20, 20],
        "fct_dir": [11, 90, 190, 210],
        "result": 25,
    },
]
