import numpy as np
import pytest

from cyeva import calc_diff_accuracy_ratio
from cyeva.core.binarize import level_binarize
from cyeva.errors import ArrayLengthNotEqualError


def test_length_not_equal_error():
    fct = np.array([1.5, 2.4, 3.1, 6])
    obs = np.array([1, 2, 3, 4, 5])

    with pytest.raises(ArrayLengthNotEqualError):
        calc_diff_accuracy_ratio(obs, fct)


def test_level_binarize_error():
    fct = np.array([1.5, 2.4, 3.1, 6])
    obs = np.array([1, 2, 3, 4])

    with pytest.raises(ValueError):
        level_binarize(obs, fct, lev_config={0: {}}, lev_id=0)