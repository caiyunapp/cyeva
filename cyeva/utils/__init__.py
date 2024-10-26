from functools import wraps
from numbers import Number

import numpy as np
from pint import Quantity

from ..errors import ArrayLengthNotEqualError


def assert_length(func):
    """Check if array is empty"""

    @wraps(func)
    def wrapper(observation, forecast, *args, **kwargs):
        if isinstance(observation, Number) and isinstance(forecast, Number):
            return func(observation, forecast, *args, **kwargs)
        if (
            hasattr(observation, "__len__")
            and hasattr(forecast, "__len__")
            and len(observation) == len(forecast)
            and len(observation) > 0
        ):
            return func(observation, forecast, *args, **kwargs)
        else:
            raise ArrayLengthNotEqualError(
                f"The length of observation array is not equal to forecast array, "
                f"observation: {len(observation)}, forecast: {len(forecast)}"
            )

    return wrapper


def convert_to_ndarray(func):
    """Convert list array to numpy ndarray"""

    @wraps(func)
    def wrapper(observation, forecast, *args, **kwargs):
        if not isinstance(observation, np.ndarray) and not isinstance(
            observation, Number
        ):
            if isinstance(observation, Quantity):
                observation = np.array(observation.magnitude)
            else:
                observation = np.array(observation)

        if not isinstance(forecast, np.ndarray) and not isinstance(forecast, Number):
            if isinstance(forecast, Quantity):
                forecast = np.array(forecast.magnitude)
            else:
                forecast = np.array(forecast)

        return func(observation, forecast, *args, **kwargs)

    return wrapper


def fix_zero_division(func):
    """Check if there is zero division and fix it."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return np.nan

    return wrapper


def drop_nan(func):
    """Drop nan"""

    @wraps(func)
    def wrapper(observation, forecast, *args, **kwargs):
        if not isinstance(observation, np.ndarray):
            observation = np.array(observation)
        if not isinstance(forecast, np.ndarray):
            forecast = np.array(forecast)

        where_obs_nan = observation != observation
        where_fct_nan = forecast != forecast

        either_nan = where_obs_nan | where_fct_nan

        valid_obs = observation[~either_nan]
        valid_fct = forecast[~either_nan]

        return func(valid_obs, valid_fct, *args, **kwargs)

    return wrapper


def source_round_digit(series_num=2, digit_num=1):
    """A decorator to round source array's significant digit

    Args:
        digit_num (int, optional): The digit num to round.
                                   Defaults to 2.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args_list = list(args)
            series = args[:series_num]
            for i, series in enumerate(series):
                try:
                    args_list[i] = np.round(series, digit_num)
                except TypeError:
                    args_list[i] = series
            return func(*args_list, **kwargs)

        return wrapper

    return decorator


def result_round_digit(digit_num=2):
    """A decorator to round result array's significant digit

    Args:
        digit_num (int, optional): The digit num to round.
                                   Defaults to 2.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result:
                return round(result, digit_num)
            else:
                return result

        return wrapper

    return decorator
