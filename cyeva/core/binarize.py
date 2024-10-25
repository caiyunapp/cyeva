from numbers import Number
from typing import Union

import numpy as np

from ..utils import (
    assert_length,
    convert_to_ndarray,
    drop_nan,
    source_round_digit,
)


@source_round_digit(digit_num=2)
@convert_to_ndarray
@assert_length
@drop_nan
def threshold_binarize(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    threshold: Number = 0,
    compare: str = ">=",
) -> tuple:
    """Binarize observation and forecast array filtered by threshold.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.

        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

        threshold (Number): The threshold to filter observation and forecast.
                            This parameter should be used with `compare` parameter,
                            The `compare` parameter will control the logical operator.

        compare (str, optional): The logical operator applying to `threshold` parameter.
                                * '>' greater
                                * '<' less
                                * '>=' greater or equal
                                * '<=' less or equal
                                Defaults to '>='.

    Returns:
        tuple: Binarized array tuple of (observation, forecast).
    """

    obs_bins = np.full_like(observation, False)
    fct_bins = np.full_like(forecast, False)

    exec(f"obs_index = observation {compare} {threshold}")
    exec(f"fct_index = forecast {compare} {threshold}")

    obs_bins[locals()["obs_index"]] = True
    fct_bins[locals()["fct_index"]] = True

    obs_bins = obs_bins.astype(bool)
    fct_bins = fct_bins.astype(bool)

    return obs_bins, fct_bins


@source_round_digit(digit_num=2)
@convert_to_ndarray
@assert_length
@drop_nan
def level_binarize(
    observation: Union[list, np.ndarray],
    forecast: Union[list, np.ndarray],
    lev_config: dict,
    lev_id: int,
    include_zero=False,
) -> tuple:
    """Binarize observation and forecast array by level.

    Args:
        observation (Union[list, np.ndarray]): Binarized observation data array
                                               that consist of numbers.

        forecast (Union[list, np.ndarray]): Binarized forecast data array that
                                            consist of numbers.

        lev_config (dict): Level configurature dict,
                           you can find some samples from cyeva.config.levels,
                           the dict's structure like:

                            lev_config = {
                                1: {"min": 0, "max": 1000},
                                2: {"min": 1000, "max": 5000},
                                3: {"min": 5000, "max": 10000},
                                4: {"min": 10000, "max": np.inf},
                            }

                            lev_config's keys should be the level's id
                            and values should contain max and min values.

        lev_id (int): The selected level id to binarize,
                        namely, this id will be marked as True
                        and other level id will be marked as False.
                        `lev_id` must be in `lev_config`'s keys.

        include_zero (bool): A flag to indicate weather include zero when filtering.
                             Default to False.

    Returns:
        tuple: Binarized array tuple of (observation, forecast) according to level id.
    """
    lev_obs = np.full((len(observation),), np.nan)
    lev_fct = np.full((len(forecast),), np.nan)

    interval = lev_config[lev_id]

    if not set(["max", "min"]).issubset(set(interval.keys())):
        raise ValueError(
            "lev_config's each interval item " "should contains 'max' and 'min' keys."
        )

    minimum = interval["min"]
    maximum = interval["max"]

    if include_zero:
        index_obs = np.where((observation >= minimum) & (observation <= maximum))
        index_fct = np.where((forecast >= minimum) & (forecast <= maximum))
    else:
        if minimum > 0:
            index_obs = np.where((observation >= minimum) & (observation <= maximum))
            index_fct = np.where((forecast >= minimum) & (forecast <= maximum))
        else:
            index_obs = np.where((observation > minimum) & (observation <= maximum))
            index_fct = np.where((forecast > minimum) & (forecast <= maximum))

    lev_obs[index_obs] = lev_id
    lev_fct[index_fct] = lev_id

    lev_obs[~np.isclose(lev_obs, float(lev_id))] = 0
    lev_fct[~np.isclose(lev_fct, float(lev_id))] = 0

    lev_obs = lev_obs.astype(bool)
    lev_fct = lev_fct.astype(bool)

    return lev_obs, lev_fct
