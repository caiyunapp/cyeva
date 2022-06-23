# cyeva

cyeva 是一个由彩云科技天气团队开发的用于对气象要素确定性预报准确率进行快速评测的 Python 开源工具库。

cyeva 将致力于让气象要素确定性预报准确率的自动化评估变得简单直接，将集成常用的确定性预报准确率评估指标，且内部算法广泛使用了 numpy 的向量运算实现，对于大数据量的计算也具有较高的计算效率。

## 安装

### 通过pip安装

```bash
$ pip install cyeva
```

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

obs = np.random.random(int(1E6)) * 50
fcst = np.random.random(int(1E6)) * 50

precip = PrecipitationComparison(obs, fcst)

print(precip.calc_ts())                     # TS评分
for inv in ['1h', '3h', '24h']:
    for lev in range(7):
        print(f'ts-{inv}-{lev}:', precip.calc_ts(kind=inv, lev=str(lev)))
    
print(precip.calc_ets())                    # ETS评分
for inv in ['1h', '3h', '24h']:
    for lev in range(7):
        print(f'ets-{inv}-{lev}:', precip.calc_ets(kind=inv, lev=str(lev)))

print(precip.calc_bias_score())             # bias评分
for inv in ['1h', '3h', '24h']:
    for lev in range(7):
        print(f'bias-{inv}-{lev}:', precip.calc_bias(kind=inv, lev=str(lev)))

print(precip.calc_accuracy_ratio(kind='3h', lev='3'))         # 准确率(3小时间隔3级/大雨)
for inv in ['1h', '3h', '24h']:
    for lev in range(7):
        lev_str = str(lev)
        levp_str = f'+{lev_str}'
        print(f'ts-{inv}- {lev_str}:', precip.calc_ts(kind=inv, lev=lev_str))
        if lev > 0:
            print(f'ts-{inv}- {levp_str}:', precip.calc_ts(kind=inv, lev=levp_str))

print(precip.calc_rss())                    # 剩余平方和
print(precip.calc_rmse())                   # 均方根误差

print(precip.calc_mae())                    # 平均绝对误差
print(precip.calc_chi_square())             # 卡方(χ2)
print(precip.calc_accuracy_ratio())         # 准确率(0级)
print(precip.calc_accuracy_ratio(kind='1h', lev='1'))         # 准确率(1小时间隔1级/小雨)
print(precip.calc_accuracy_ratio(kind='3h', lev='1'))         # 准确率(3小时间隔1级/小雨)
print(precip.calc_accuracy_ratio(kind='3h', lev='3'))         # 准确率(3小时间隔3级/大雨)
for inv in ['1h', '3h', '24h']:
    for lev in range(7):
        print(f'{inv}-{lev}:', precip.calc_ts(kind=inv, lev=str(lev)))
print(precip.calc_accuracy_ratio(kind='3h', lev='+3'))        # 准确率(3小时间隔累计3级/大雨)
print(precip.calc_binary_accuracy_ratio())  # 准确率(二分/晴雨)
print(precip.calc_false_alarm_ratio())      # 空报率
print(precip.calc_miss_ratio())             # 漏报率
```

### 气温
```python
import numpy as np
from cyeva import TemperatureComparison

np.random.seed(0)

obs = np.random.random(int(1E7)) * 50
fcst = np.random.random(int(1E7)) * 50

temp = TemperatureComparison(obs, fcst, unit='degC')

print(temp.calc_diff_accuracy_ratio(limit=1))       # 1度准确率（偏差在1°C以内）
print(temp.calc_diff_accuracy_ratio(limit=2))       # 2度准确率（偏差在2°C以内）
print(temp.calc_rss())                              # 剩余平方和
print(temp.calc_rmse())                             # 均方根误差
print(temp.calc_mae())                              # 平均绝对误差
print(temp.calc_chi_square())                       # 卡方(χ2)
print(temp.gather_all_factors())                    # 全部要素
```

### 风

```python
import numpy as np
from cyeva import WindComparison

np.random.seed(0)

obs_spd = np.random.random(int(1E7)) * 10
obs_dir = np.random.random(int(1E7)) * 360
fct_spd = np.random.random(int(1E7)) * 10
fct_dir = np.random.random(int(1E7)) * 360

wind = WindComparison(obs_spd, fct_spd, obs_dir, fct_dir)

print(wind.calc_diff_accuracy_ratio(limit=1))       # 1度准确率（偏差在1°C以内）
print(wind.calc_diff_accuracy_ratio(limit=2))       # 2度准确率（偏差在2°C以内）
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