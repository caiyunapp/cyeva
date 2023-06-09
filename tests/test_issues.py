import numpy as np
from cyeva import identify_direction


def test_iss36():
    assert (
        np.array([0, 2, 4, 6, 0]) == identify_direction([0, 90, 180, 270, 360])
    ).all()
    assert (
        np.array([0, 4, 8, 12, 0])
        == identify_direction([0, 90, 180, 270, 360], dnum=16)
    ).all()
