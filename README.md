# cyeva
Python用于进行预报准确性检验的工具包

## 安装

由于项目尚未完成，为避免对包环境污染，建议clone之后以开发模式安装：
`$ python setup.py develop`

## 使用

### 降水
```python
import numpy as np
from cyeva import PrecipitationComparison

obs = np.array([1, 2, 3, 4])
fcst = np.array([0, 0, 0, 0])

precip = PrecipitationComparison(obs, fcst)

print(precip.calc_ts())                     # TS评分
print(precip.calc_ets())                    # ETS评分
print(precip.calc_bias_score())             # bias评分
print(precip.calc_rss())                    # 剩余平方和
print(precip.calc_rmse())                   # 均方根误差
print(precip.calc_mae())                    # 平均绝对误差
print(precip.calc_chi_square())             # 卡方(χ2)
print(precip.calc_accuracy_ratio())         # 准确率(0级)
print(precip.calc_accuracy_ratio(kind='1h', lev='1'))         # 准确率(1小时间隔1级/小雨)
print(precip.calc_accuracy_ratio(kind='3h', lev='1'))         # 准确率(3小时间隔1级/小雨)
print(precip.calc_accuracy_ratio(kind='3h', lev='3'))         # 准确率(3小时间隔3级/大雨)
print(precip.calc_accuracy_ratio(kind='3h', lev='+3'))        # 准确率(3小时间隔累计3级/大雨)
print(precip.calc_binary_accuracy_ratio())  # 准确率(二分/晴雨)
print(precip.calc_false_alarm_ratio())      # 空报率
print(precip.calc_miss_ratio())             # 漏报率
```

### 气温
```python
import numpy as np
from cyeva import TemperatureComparison

obs = np.array([1, 2, 3, 4])
fcst = np.array([0, 0, 0, 0])

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

obs_spd = np.random.random(100) * 10
obs_dir = np.random.random(100) * 360
fct_spd = np.random.random(100) * 10
fct_dir = np.random.random(100) * 360

wind = WindComparison(obs_spd, fct_spd, obs_dir, fct_dir)

print(wind.calc_diff_accuracy_ratio(limit=1))       # 1度准确率（偏差在1°C以内）
print(wind.calc_diff_accuracy_ratio(limit=2))       # 2度准确率（偏差在2°C以内）
print(wind.calc_rss())                              # 剩余平方和
print(wind.calc_rmse())                             # 均方根误差
print(wind.calc_mae())                              # 平均绝对误差
print(wind.calc_chi_square())                       # 卡方(χ2)
```