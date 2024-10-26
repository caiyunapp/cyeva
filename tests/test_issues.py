import numpy as np

from cyeva import identify_direction


def test_iss33():
    from cyeva import WindComparison

    ws1 = np.array([1, 2])
    ws2 = np.array([2, 3])
    wd1 = np.array([357, 357])
    wd2 = np.array([3, 3])

    wc = WindComparison(ws1, ws2, wd1, wd2)
    assert np.isclose(wc.calc_rmse(kind="direction"), 6)


def test_iss36():
    assert (
        np.array([0, 2, 4, 6, 0]) == identify_direction([0, 90, 180, 270, 360])
    ).all()
    assert (
        np.array([0, 4, 8, 12, 0])
        == identify_direction([0, 90, 180, 270, 360], dnum=16)
    ).all()
