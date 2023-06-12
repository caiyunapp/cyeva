import numpy as np

from cyeva.core.binarize import level_binarize


def test_level_binarize_0():
    fct = np.array([1.5, 2.4, 3.1, 6])
    obs = np.array([0, 2, 3, 4])

    obs_bin, fct_bin = level_binarize(
        obs, fct, lev_config={1: {"min": 0, "max": 2}}, lev_id=1
    )
    assert (obs_bin == np.array([False, True, False, False])).all()
    assert (fct_bin == np.array([True, False, False, False])).all()

    obs_bin, fct_bin = level_binarize(
        obs, fct, lev_config={1: {"min": 0, "max": 2}}, lev_id=1, include_zero=True
    )

    assert (obs_bin == np.array([True, True, False, False])).all()
    assert (fct_bin == np.array([True, False, False, False])).all()
