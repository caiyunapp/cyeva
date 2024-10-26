<h1 align="center" style="margin:1em;">
  <a href="./docs/source/_static/logo.png">
    <img src="./docs/source/_static/logo.png"
         alt="cyeva"></a>
</h1>

[![Pytest](https://github.com/caiyunapp/cyeva/actions/workflows/test.yml/badge.svg)](https://github.com/caiyunapp/cyeva/actions/workflows/test.yml)
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


cyeva 是一个由彩云科技天气团队和社区贡献者共同开发的用于对气象要素确定性预报准确率进行快速评测的 Python 开源工具库。

cyeva 将致力于让气象要素确定性预报准确率的自动化评估变得简单直接，将集成常用的确定性预报准确率评估指标，且内部算法广泛使用了 numpy 的向量运算实现，对于大数据量的计算也具有较高的计算效率。

## 安装

### 通过pip安装

```bash
$ pip install cyeva
```

**注意：由于本项目目前处于beta阶段，并非稳定版本，有可能在后续的发布版中出现不兼容性修改，因此在安装时建议指定版本号，例如 `pip install cyeva==0.2.0`**

### 通过源码安装

首先在[版本页面](https://github.com/caiyunapp/cyeva/releases)选择想要安装的版本，解压，进入项目目录然后执行：

```bash
$ python setup.py install
```

## 使用

cyeva 为气温、风和降水编写了专门的对象用于处理对应要素的相关指标。   

### 气温

对于气温这种连续性变量，我们通常会比较关心它的 RMSE 、 MAE 等指标。在 cyeva 中我们可以参照以下的例子来计算此类指标：

```python
import numpy as np
from cyeva import TemperatureComparison

np.random.seed(0)  # 指定随机种子以保证得到的结果都是一致的

obs = np.sin(np.arange(100)) * 20 + np.random.random(100) * 5 * np.random.choice([1, -1])  # sin数组叠加随机数组模拟真实气温
fcst = obs + np.random.random(100) * 5 * np.random.choice([1, -1])  # 限制预报在观测的正负5°C以内，这样的样例出来的效果更好一些

temp = TemperatureComparison(obs, fcst, unit='degC')

print('accuracy ration within 1 degC:', temp.calc_diff_accuracy_ratio(limit=1))       # 1度准确率（偏差在1°C以内）
print('accuracy ration within 2 degC:', temp.calc_diff_accuracy_ratio(limit=2))       # 2度准确率（偏差在2°C以内）
print('rss:', temp.calc_rss())                                                        # 剩余平方和
print('rmse:', temp.calc_rmse())                                                       # 均方根误差
print('mae:', temp.calc_mae())                                                         # 平均绝对误差
print('chi square:', temp.calc_chi_square())                                           # 卡方(χ2)
```

### 降水

降水的一个特点是它不具有连续性，因此在对其进行准确性评估的时候，除了通用的指标以外，通常会引入一些其他的指标（例如 TS 评分）。此外，降水有明显的分级特点，还需要按照不同级别的做相应的区别，在 cyeva 中我们可以参照以下的例子来计算用于评估降水的指标：

```python
import numpy as np
from cyeva import PrecipitationComparison

np.random.seed(0)  # 指定随机种子以保证得到的结果都是一致的

obs = np.random.random(int(100)) * 50
fcst = np.random.random(int(100)) * 50

precip = PrecipitationComparison(obs, fcst, unit='mm')

print('rss:', precip.calc_rss())                                        # 剩余平方和
print('rmse:', precip.calc_rmse())                                      # 均方根误差
print('mae:', precip.calc_mae())                                        # 平均绝对误差
print('chi square:', precip.calc_chi_square())                          # 卡方(χ2)
print('accuracy ratio:', precip.calc_accuracy_ratio())                  # 准确率(0级)
print('binary accuracy ratio:', precip.calc_binary_accuracy_ratio())    # 准确率(二分/晴雨)
print('false alarm ratio:', precip.calc_false_alarm_ratio())            # 空报率
print('miss ratio:', precip.calc_miss_ratio())                          # 漏报率

print('accuracy ratio:', precip.calc_accuracy_ratio(kind='3h', lev='3'))         # 准确率(3小时间隔3级/大雨)
for inv in ['1h', '3h', '12h', '24h']:                                           # 不同间隔下的准确率
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'accuracy ratio({inv}|{lev_str}):', precip.calc_accuracy_ratio(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'accuracy ratio({inv}|{levp_str}):', precip.calc_accuracy_ratio(kind=inv, lev=levp_str))

print('ts:', precip.calc_ts())              # TS评分（默认为1h晴雨TS）
for inv in ['1h', '3h', '12h', '24h']:      # 不同间隔下的分级TS评分
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'ts({inv}|{lev_str}):', precip.calc_ts(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'ts({inv}|{levp_str}):', precip.calc_ts(kind=inv, lev=levp_str))
    
print('ets:', precip.calc_ets())            # ETS评分（默认为1h晴雨ETS）
for inv in ['1h', '3h', '12h', '24h']:      # 不同间隔下的分级ETS评分
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'ets({inv}|{lev_str}):', precip.calc_ets(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'ets({inv}|{levp_str}):', precip.calc_ets(kind=inv, lev=levp_str))

print('bias:', precip.calc_bias_score())    # bias评分（默认为1h晴雨bias）
for inv in ['1h', '3h', '12h', '24h']:      # 不同间隔下的分级bias评分
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'bias({inv}|{lev_str}):', precip.calc_bias_score(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'bias({inv}|{levp_str}):', precip.calc_bias_score(kind=inv, lev=levp_str))
```


### 风

对于风这种矢量要素，我们需要同时提供速度和方向信息，因此在实例化对象的时候传入的数据数组会和气温、降水不一样，同时也有一些专门针对于风评估的指标，例如风级偏强率偏弱率等，在 cyeva 中我们可以参照以下的例子来计算用于评估风的指标：

```python
import numpy as np
from cyeva import WindComparison

np.random.seed(0)

obs_spd = np.random.random(100) * 10
obs_dir = np.random.random(100) * 360
fct_spd = np.random.random(100) * 10
fct_dir = np.random.random(100) * 360

wind = WindComparison(obs_spd, fct_spd, obs_dir, fct_dir)

print('difference accuracy ratio within 1 m/s:', wind.calc_diff_accuracy_ratio(limit=1))       # 1m/s准确率（风速偏差在1m/s以内）
print('difference accuracy ratio within 2 m/s:', wind.calc_diff_accuracy_ratio(limit=2))       # 2m/s准确率（风速偏差在2m/s以内）
print('wind speed rss:', wind.calc_rss())                                                      # 剩余平方和（默认风速）
print('wind direction rss:', wind.calc_rss(kind='direction'))                                  # 剩余平方和（指定风向）
print('wind speed rmse:', wind.calc_rmse())                                                    # 均方根误差（默认风速）
print('wind direction rmse:', wind.calc_rmse(kind='direction'))                                # 均方根误差（指定风向）
print('wind speed mae:', wind.calc_mae())                                                      # 平均绝对误差（默认风速）
print('wind direction mae:', wind.calc_mae(kind='direction'))                                  # 平均绝对误差（指定风向）
print('wind speed chi square:', wind.calc_chi_square())                                        # 卡方(χ2)
print('wind direction chi square:', wind.calc_chi_square(kind='direction'))                    # 卡方(χ2)（指定风向）
print('wind direction score:', wind.calc_dir_score())                                          # 风向评分
print('wind speed score:', wind.calc_speed_score())                                            # 风速评分
print('wind scale accuracy ratio:', wind.calc_wind_scale_accuracy_ratio())                     # 风级准确率
print('wind speed accuracy ratio within 2m/s:', wind.calc_speed_accuracy_ratio())              # 风速准确率(默认2m/s偏差以内)
print('wind speed accuracy radio within 3m/s:', wind.calc_speed_accuracy_ratio(limit=3))       # 风速准确率(指定3m/s偏差以内)
print('wind scale stronger ratio:', wind.calc_wind_scale_stronger_ratio())                     # 风级偏强率
print('wind scale weaker ratio:', wind.calc_wind_scale_weaker_ratio())                         # 风级偏弱率
```

## 算法解释

对于本项目所实现的各类测评算法及其解释、公式等信息，可以参考 [cyeva说明文档](https://cyeva.readthedocs.io/zh_CN/latest/index.html) 的 [算法指标](https://cyeva.readthedocs.io/zh_CN/latest/content/indicator.html) 部分。