from typing import Union
from numbers import Number

import numpy as np
import pandas as pd

from ..utils import result_round_digit, source_round_digit
from .binarize import threshold_binarize
from .statistic import (
    calc_diff_accuracy_ratio,
    calc_rmse,
    calc_mae,
    calc_rss,
    calc_chi_square,
    calc_linregress,
    calc_bias_score,
    calc_binary_accuracy_ratio,
)


class Comparison:
    """A base class of comparison between obervation & forecast"""

    def __init__(
        self, observation: Union[np.ndarray, list], forecast: Union[np.ndarray, list]
    ):

        self.df = pd.DataFrame({"observation": observation, "forecast": forecast})
        self.observation = self.df["observation"].values
        self.forecast = self.df["forecast"].values

    def __repr__(self):
        text = "\n".join(["<Object:Comparison>", "data:", self.df.__str__()])
        return text

    def __str__(self):
        text = "\n".join(["<Object:Comparison>", "data:", self.df.__str__()])
        return text

    @result_round_digit(4)
    @source_round_digit()
    def calc_rmse(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        *args,
        **kwargs
    ) -> float:
        "Root Mean Square Error"
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        return calc_rmse(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    def calc_mae(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        *args,
        **kwargs
    ) -> float:
        """Mean Absolute Error"""
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        return calc_mae(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    def calc_chi_square(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        *args,
        **kwargs
    ) -> float:
        """χ2"""
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        return calc_chi_square(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    def calc_rss(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        *args,
        **kwargs
    ) -> float:
        """Residual Sum of Square"""
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        return calc_rss(observation, forecast)

    def calc_linregress_args(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        *args,
        **kwargs
    ):
        """linregress args"""
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        return calc_linregress(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    def calc_bias(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        threshold: Number = 0,
        *args,
        **kwargs
    ) -> float:
        """BIAS score"""
        if observation is None:
            _observation = self.observation
        else:
            _observation = observation
        if forecast is None:
            _forecast = self.forecast
        else:
            _forecast = forecast

        observation, forecast = threshold_binarize(
            _observation, _forecast, threshold=threshold, compare=">"
        )
        return calc_bias_score(observation, forecast)

    @result_round_digit(4)
    @source_round_digit()
    def calc_binary_accuracy_ratio(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        threshold: Number = 0,
        *args,
        **kwargs
    ) -> float:
        """Binary accuracy ratio

        Args:
            threshold (Number, optional): The threshold to binarize array.
                                                     Defaults to 0.

        Returns:
            float: The accuracy ratio.
        """
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        binary_observation, binary_forecast = threshold_binarize(
            observation, forecast, threshold=threshold, compare=">"
        )
        return calc_binary_accuracy_ratio(binary_observation, binary_forecast)

    @result_round_digit(4)
    @source_round_digit()
    def calc_diff_accuracy_ratio(
        self,
        observation: Union[np.ndarray, list] = None,
        forecast: Union[np.ndarray, list] = None,
        limit: Number = 1,
        *args,
        **kwargs
    ) -> float:
        """
        Calculate the accuracy ratio that
        two array's difference within a limit scope.

        Args:
            limit (Number, optional): The limit of difference.
                                                 Defaults to 1.

        Returns:
            float: The accuracy ratio.
        """
        if observation is None:
            observation = self.observation
        if forecast is None:
            forecast = self.forecast

        return calc_diff_accuracy_ratio(observation, forecast, limit=limit)
