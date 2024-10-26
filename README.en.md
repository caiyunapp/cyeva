# cyeva

[![Pytest](https://github.com/caiyunapp/cyeva/actions/workflows/pytest.yml/badge.svg)](https://github.com/caiyunapp/cyeva/actions/workflows/pytest.yml)
[![Pypi publish](https://github.com/caiyunapp/cyeva/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/caiyunapp/cyeva/actions/workflows/pypi-publish.yml)
[![Anaconda.org](https://anaconda.org/conda-forge/cyeva/badges/version.svg)](https://anaconda.org/conda-forge/cyeva)
[![Downloads](https://anaconda.org/conda-forge/cyeva/badges/downloads.svg)](https://anaconda.org/conda-forge/cyeva)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/cyeva/badges/platforms.svg)](https://anaconda.org/conda-forge/cyeva)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/cyeva/badges/latest_release_date.svg)](https://anaconda.org/conda-forge/cyeva)
[![Pypi](https://badge.fury.io/py/cyeva.svg)](https://badge.fury.io/py/cyeva)
[![Documentation Status](https://readthedocs.org/projects/cyeva/badge/?version=latest)](https://cyeva.readthedocs.io/zh_CN/latest/?badge=latest)
[![Download statistic](https://pepy.tech/badge/cyeva)](https://pepy.tech/project/cyeva)
[![codecov](https://codecov.io/gh/caiyunapp/cyeva/branch/main/graph/badge.svg?token=344FXDKAYD)](https://codecov.io/gh/caiyunapp/cyeva)
[![performance](https://img.shields.io/badge/performance-benchmark-yellow)](https://caiyunapp.github.io/cyeva/performance/)
[![style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Cyeva is a Python open-source tool library jointly developed by the Colorful Clouds Technology weather team and community contributors for quickly evaluating the accuracy of deterministic forecasts of meteorological elements.

Cyeva aims to make automated evaluation of the accuracy of deterministic meteorological forecasts straightforward. It integrates commonly used deterministic forecast accuracy evaluation metrics. Its internal algorithms widely use numpy's vector operations, thus having high computational efficiency for large data sets.

## Installation

### Install via pip

```bash
$ pip install cyeva
```

**Note: Since this project is currently in beta, it is not a stable version. It may undergo incompatible changes in future releases. Therefore, it's recommended to specify the version during installation, e.g., pip install cyeva==0.2.0.**

### Install from Source Code

First, choose the desired version on the [release page](https://github.com/caiyunapp/cyeva/releases), extract it, navigate to the project directory, and then execute:

```bash
$ python setup.py install
```

## Usage

Cyeva has specially designed objects to handle relevant indicators for temperature, wind, and precipitation.

### Temperature

For temperature, which is a continuous variable, we are usually interested in its RMSE (Root Mean Square Error), MAE (Mean Absolute Error), and other similar metrics. In cyeva, we can refer to the following examples to calculate these kinds of metrics.

```python
import numpy as np
from cyeva import TemperatureComparison

np.random.seed(0)  # Specify a random seed to ensure that the results obtained are consistent.

obs = np.sin(np.arange(100)) * 20 + np.random.random(100) * 5 * np.random.choice([1, -1])  # Simulate real temperature by overlaying a sine array with a random array.
fcst = obs + np.random.random(100) * 5 * np.random.choice([1, -1])  # Limit the forecast to within plus or minus 5°C of the observation; the results are better in such cases.

temp = TemperatureComparison(obs, fcst, unit='degC')

print('accuracy ration within 1 degC:', temp.calc_diff_accuracy_ratio(limit=1))       # 1-degree accuracy (deviation within 1°C)
print('accuracy ration within 2 degC:', temp.calc_diff_accuracy_ratio(limit=2))       # 2-degree accuracy (deviation within 2°C)
print('rss:', temp.calc_rss())                                                        # Residual Sum of Squares
print('rmse:', temp.calc_rmse())                                                      # Root Mean Square Error
print('mae:', temp.calc_mae())                                                        # Mean Absolute Error
print('chi square:', temp.calc_chi_square())                                          # Chi Square (χ2)
```

### Precipitation

One characteristic of precipitation is that it is not continuous, so when assessing its accuracy, in addition to common metrics, other metrics (such as TS scores) are usually introduced. Moreover, precipitation has clear levels, so it is necessary to make distinctions according to different levels. In cyeva, we can refer to the following examples to calculate metrics used for assessing precipitation.

```python
import numpy as np
from cyeva import PrecipitationComparison

np.random.seed(0)  # Specify a random seed to ensure that the results obtained are consistent.

obs = np.random.random(int(100)) * 50
fcst = np.random.random(int(100)) * 50

precip = PrecipitationComparison(obs, fcst, unit='mm')

print('rss:', precip.calc_rss())                                        # Residual Sum of Squares
print('rmse:', precip.calc_rmse())                                      # Root Mean Square Error
print('mae:', precip.calc_mae())                                        # Mean Absolute Error
print('chi square:', precip.calc_chi_square())                          # Chi Square (χ2)
print('accuracy ratio:', precip.calc_accuracy_ratio())                  # Accuracy(0 level)
print('binary accuracy ratio:', precip.calc_binary_accuracy_ratio())    # Binary accuracy(Binary classes between sunny or rainy weather)
print('false alarm ratio:', precip.calc_false_alarm_ratio())            # False alarm
print('miss ratio:', precip.calc_miss_ratio())                          # Missing

print('accuracy ratio:', precip.calc_accuracy_ratio(kind='3h', lev='3'))         # Accuracy (3-hours time interval/level 3/heavy rain)
for inv in ['1h', '3h', '12h', '24h']:                                           # Accuracy on different time intervals
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'accuracy ratio({inv}|{lev_str}):', precip.calc_accuracy_ratio(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'accuracy ratio({inv}|{levp_str}):', precip.calc_accuracy_ratio(kind=inv, lev=levp_str))

print('ts:', precip.calc_ts())              # TS score（1-hr time interval/binary classes/default）
for inv in ['1h', '3h', '12h', '24h']:      # TS score under different time intervals with different level criteria
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'ts({inv}|{lev_str}):', precip.calc_ts(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'ts({inv}|{levp_str}):', precip.calc_ts(kind=inv, lev=levp_str))
    
print('ets:', precip.calc_ets())            # ETS score（1-hr time interval/binary classes/ETS score/default）
for inv in ['1h', '3h', '12h', '24h']:      # ETS score under different time intervals with different level criteria
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'ets({inv}|{lev_str}):', precip.calc_ets(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'ets({inv}|{levp_str}):', precip.calc_ets(kind=inv, lev=levp_str))

print('bias:', precip.calc_bias_score())    # bias score（1-hr time interval/binary classes/bias score/default）
for inv in ['1h', '3h', '12h', '24h']:      # bias score under different time intervals with different level criteria
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'bias({inv}|{lev_str}):', precip.calc_bias_score(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'bias({inv}|{levp_str}):', precip.calc_bias_score(kind=inv, lev=levp_str))
```

### Wind

For wind, which is a vector element, we need to provide both speed and direction information. Therefore, the data array passed in when instantiating the object will differ from that of temperature and precipitation. There are also some metrics specifically designed for wind assessment, such as the rates of wind being stronger or weaker than the standard, etc. In cyeva, we can refer to the following examples to calculate metrics used for assessing wind.

```python
import numpy as np
from cyeva import WindComparison

np.random.seed(0)

obs_spd = np.random.random(100) * 10
obs_dir = np.random.random(100) * 360
fct_spd = np.random.random(100) * 10
fct_dir = np.random.random(100) * 360

wind = WindComparison(obs_spd, fct_spd, obs_dir, fct_dir)

print('difference accuracy ratio within 1 m/s:', wind.calc_diff_accuracy_ratio(limit=1))       # 1m/s accuracy (speed deviation within 1m/s)
print('difference accuracy ratio within 2 m/s:', wind.calc_diff_accuracy_ratio(limit=2))       # 2m/s accuracy (speed deviation within 2m/s)
print('wind speed rss:', wind.calc_rss())                                                      # Residual Sum of Squares（by speed/default）
print('wind direction rss:', wind.calc_rss(kind='direction'))                                  # Residual Sum of Squares（by direction）
print('wind speed rmse:', wind.calc_rmse())                                                    # Root Mean Square Error（by speed/default）
print('wind direction rmse:', wind.calc_rmse(kind='direction'))                                # Root Mean Square Error（by direction）
print('wind speed mae:', wind.calc_mae())                                                      # Mean Absolute Error（by speed/default）
print('wind direction mae:', wind.calc_mae(kind='direction'))                                  # Mean Absolute Error（by direction）
print('wind speed chi square:', wind.calc_chi_square())                                        # Chi Square(χ2)
print('wind direction chi square:', wind.calc_chi_square(kind='direction'))                    # Chi Square(χ2)（by direction）
print('wind direction score:', wind.calc_dir_score())                                          # Direction score
print('wind speed score:', wind.calc_speed_score())                                            # Speed score
print('wind scale accuracy ratio:', wind.calc_wind_scale_accuracy_ratio())                     # Wind scale accuracy
print('wind speed accuracy ratio within 2m/s:', wind.calc_speed_accuracy_ratio())              # Speed accuracy(2m/s deviation/default)
print('wind speed accuracy radio within 3m/s:', wind.calc_speed_accuracy_ratio(limit=3))       # Speed accuracy(3m/s deviation)
print('wind scale stronger ratio:', wind.calc_wind_scale_stronger_ratio())                     # The ratio with a stronger wind scale forecast
print('wind scale weaker ratio:', wind.calc_wind_scale_weaker_ratio())                         # The ratio with a weaker wind scale forecast
```

## Algorithm Explanation

For explanations, formulas, and other information about the various evaluation algorithms implemented in this project, please refer to the [metrics](https://cyeva.readthedocs.io/zh_CN/latest/content/indicator.html) section in the [cyeva documentation](https://cyeva.readthedocs.io/zh_CN/latest/index.html).
