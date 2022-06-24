# cyeva

[![Pytest](https://github.com/caiyunapp/cyeva/actions/workflows/pytest.yml/badge.svg)](https://github.com/caiyunapp/cyeva/actions/workflows/pytest.yml)
[![Pypi publish](https://github.com/caiyunapp/cyeva/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/caiyunapp/cyeva/actions/workflows/pypi-publish.yml)
[![Pypi](https://badge.fury.io/py/cyeva.svg)](https://badge.fury.io/py/cyeva)
[![Documentation Status](https://readthedocs.org/projects/cyeva/badge/?version=latest)](https://cyeva.readthedocs.io/zh_CN/latest/?badge=latest)
[![Line statistic](https://tokei.rs/b1/github/caiyunapp/cyeva?category=lines)](https://github.com/caiyunapp/cyeva)
[![Download statistic](https://pepy.tech/badge/cyeva)](https://pepy.tech/project/cyeva)

cyeva 是一个由彩云科技天气团队开发的用于对气象要素确定性预报准确率进行快速评测的 Python 开源工具库。

cyeva 将致力于让气象要素确定性预报准确率的自动化评估变得简单直接，将集成常用的确定性预报准确率评估指标，且内部算法广泛使用了 numpy 的向量运算实现，对于大数据量的计算也具有较高的计算效率。

## 安装

### 通过pip安装

```bash
$ pip install cyeva
```

**注意：由于本项目目前处于beta阶段，并非稳定版本，有可能在后续的发布版中出现不兼容性修改，因此在安装时建议指定版本号，例如 `pip install cyeva==0.1.0b0`**

### 通过源码安装

首先在[版本页面](https://github.com/caiyunapp/cyeva/releases)选择想要安装的版本，解压，进入项目目录然后执行：

```bash
$ python setup.py install
```

## 使用

### 降水
```python
import numpy as np
from cyeva import PrecipitationComparison

np.random.seed(0)

obs = np.random.random(int(1E4)) * 50
fcst = np.random.random(int(1E4)) * 50

precip = PrecipitationComparison(obs, fcst)

print(precip.calc_rss())                    # 剩余平方和
print(precip.calc_rmse())                   # 均方根误差
print(precip.calc_mae())                    # 平均绝对误差
print(precip.calc_chi_square())             # 卡方(χ2)
print(precip.calc_accuracy_ratio())         # 准确率(0级)
print(precip.calc_binary_accuracy_ratio())  # 准确率(二分/晴雨)
print(precip.calc_false_alarm_ratio())      # 空报率
print(precip.calc_miss_ratio())             # 漏报率

print(precip.calc_ts())                     # TS评分（默认为1h晴雨TS）
for inv in ['1h', '3h', '12h', '24h']:      # 不同间隔下的分级TS评分
    for lev in range(7):
        print(f'ts-{inv}-{lev}:', precip.calc_ts(kind=inv, lev=str(lev)))
    
print(precip.calc_ets())                    # ETS评分（默认为1h晴雨ETS）
for inv in ['1h', '3h', '12h', '24h']:      # 不同间隔下的分级ETS评分
    for lev in range(7):
        print(f'ets-{inv}-{lev}:', precip.calc_ets(kind=inv, lev=str(lev)))

print(precip.calc_bias_score())             # bias评分（默认为1h晴雨bias）
for inv in ['1h', '3h', '12h', '24h']:      # 不同间隔下的分级bias评分
    for lev in range(7):
        print(f'bias-{inv}-{lev}:', precip.calc_bias(kind=inv, lev=str(lev)))

print(precip.calc_accuracy_ratio(kind='3h', lev='3'))         # 准确率(3小时间隔3级/大雨)
for inv in ['1h', '3h', '12h', '24h']:                        # 不同间隔下的分级准确率
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'ts-{inv}- {lev_str}:', precip.calc_ts(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'ts-{inv}- {levp_str}:', precip.calc_ts(kind=inv, lev=levp_str))
```

### 气温
```python
import numpy as np
from cyeva import TemperatureComparison

np.random.seed(0)

obs = np.random.random(int(1E4)) * 50
fcst = np.random.random(int(1E4)) * 50

temp = TemperatureComparison(obs, fcst, unit='degC')

print(temp.calc_diff_accuracy_ratio(limit=1))       # 1度准确率（偏差在1°C以内）
print(temp.calc_diff_accuracy_ratio(limit=2))       # 2度准确率（偏差在2°C以内）
print(temp.calc_rss())                              # 剩余平方和
print(temp.calc_rmse())                             # 均方根误差
print(temp.calc_mae())                              # 平均绝对误差
print(temp.calc_chi_square())                       # 卡方(χ2)
```

### 风

```python
import numpy as np
from cyeva import WindComparison

np.random.seed(0)

obs_spd = np.random.random(int(1E4)) * 10
obs_dir = np.random.random(int(1E4)) * 360
fct_spd = np.random.random(int(1E4)) * 10
fct_dir = np.random.random(int(1E4)) * 360

wind = WindComparison(obs_spd, fct_spd, obs_dir, fct_dir)

print(wind.calc_diff_accuracy_ratio(limit=1))       # 1m/s准确率（风速偏差在1m/s以内）
print(wind.calc_diff_accuracy_ratio(limit=2))       # 2m/s准确率（风速偏差在2m/s以内）
print(wind.calc_rss())                              # 剩余平方和（默认风速）
print(wind.calc_rss(kind='direction'))              # 剩余平方和（指定风向）
print(wind.calc_rmse())                             # 均方根误差（默认风速）
print(wind.calc_rmse(kind='direction'))             # 均方根误差（指定风向）
print(wind.calc_mae())                              # 平均绝对误差（默认风速）
print(wind.calc_mae(kind='direction'))              # 平均绝对误差（指定风向）
print(wind.calc_chi_square())                       # 卡方(χ2)
print(wind.calc_chi_square(kind='direction'))       # 卡方(χ2)（指定风向）
print(wind.calc_dir_score())                        # 风向评分
print(wind.calc_speed_score())                      # 风速评分
print(wind.calc_wind_scale_accuracy_ratio())        # 风级准确率
print(wind.calc_speed_accuracy_ratio())             # 风速准确率(默认2m/s偏差以内)
print(wind.calc_speed_accuracy_ratio(limit=3))      # 风速准确率(指定3m/s偏差以内)
print(wind.calc_wind_scale_stronger_ratio())        # 风级偏强率
print(wind.calc_wind_scale_weaker_ratio())          # 风级偏弱率
```