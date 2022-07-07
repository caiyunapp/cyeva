import numpy as np
import pytest

from cyeva import calc_diff_accuracy_ratio
from cyeva.errors import ArrayLengthNotEqualError


def test_length_not_equal_error():
    fct = np.array([1.5, 2.4, 3.1, 6])
    obs = np.array([1, 2, 3, 4, 5])

    with pytest.raises(ArrayLengthNotEqualError):
        calc_diff_accuracy_ratio(obs, fct)
