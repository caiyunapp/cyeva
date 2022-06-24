使用
==========
下面我们将以示例的方式来介绍 cyeva 的主要功能的用法。

快速开始
----------
cyeva 为气温、风和降水编写了专门的对象用于处理对应要素的相关指标。

对于气温这种连续性变量，我们通常会比较关心它的 RMSE 、 MAE 等指标。在 cyeva 中我们可以参照以下的例子来计算此类指标：

.. code:: python

    import numpy as np
    from cyeva import TemperatureComparison

    np.random.seed(0)

    obs = np.random.random(100) * 20
    fcst = obs + np.random.random(100) * 5 * np.random.choice([1, -1])

    temp = TemperatureComparison(obs, fcst, unit='degC')

    print('accuracy ration within 1 degC:', temp.calc_diff_accuracy_ratio(limit=1))       # 1度准确率（偏差在1°C以内）
    print('accuracy ration within 2 degC:', temp.calc_diff_accuracy_ratio(limit=2))       # 2度准确率（偏差在2°C以内）
    print('rss:', temp.calc_rss())                                                        # 剩余平方和
    print('rmse:', temp.calc_rmse())                                                       # 均方根误差
    print('mae:', temp.calc_mae())                                                         # 平均绝对误差
    print('chi square:', temp.calc_chi_square())                                           # 卡方(χ2)

降水的一个特点是它不具有连续性，因此在对其进行准确性评估的时候，除了通用的指标以外，通常会引入一些其他的指标（例如 TS 评分）。此外，降水有明显的分级特点，还需要按照不同级别的做相应的区别，在 cyeva 中我们可以参照以下的例子来计算用于评估降水的指标：

.. code:: python

    import numpy as np
    from cyeva import PrecipitationComparison

    np.random.seed(0)

    obs = np.random.random(int(1E4)) * 50
    fcst = np.random.random(int(1E4)) * 50

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


对于风这种矢量要素，我们需要同时提供速度和方向信息，因此在实例化对象的时候传入的数据数组会和气温、降水不一样，同时也有一些专门针对于风评估的指标，例如风级偏强率偏弱率等，在 cyeva 中我们可以参照以下的例子来计算用于评估风的指标：

.. code:: python

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
    print('wind speed rss:', wind.calc_rss())                                                      # 剩余平方和（默认为风速）
    print('wind direction rss:', wind.calc_rss(kind='direction'))                                  # 剩余平方和（指定为风向）
    print('wind speed rmse:', wind.calc_rmse())                                                    # 均方根误差（默认为风速）
    print('wind direction rmse:', wind.calc_rmse(kind='direction'))                                # 均方根误差（指定为风向）
    print('wind speed mae: ', wind.calc_mae())                                                     # 平均绝对误差（默认为风速）
    print('wind direction mae:', wind.calc_mae(kind='direction'))                                  # 平均绝对误差（指定为风向）
    print('wind speed chi square:', wind.calc_chi_square())                                        # 卡方(χ2)
    print('wind direction chi square:', wind.calc_chi_square(kind='direction'))                    # 卡方(χ2)（指定为风向）
    print('wind direction score:', wind.calc_dir_score())                                          # 风向评分
    print('wind speed score:', wind.calc_speed_score())                                            # 风速评分
    print('wind scale accuracy ratio:', wind.calc_wind_scale_accuracy_ratio())                     # 风级准确率
    print('wind speed accuracy ratio within 2m/s:', wind.calc_speed_accuracy_ratio())              # 风速准确率(默认2m/s偏差以内)
    print('wind speed accuracy radio within 3m/s:', wind.calc_speed_accuracy_ratio(limit=3))       # 风速准确率(指定3m/s偏差以内)
    print('wind scale stronger ratio:', wind.calc_wind_scale_stronger_ratio())                     # 风级偏强率
    print('wind scale weaker ratio:', wind.calc_wind_scale_weaker_ratio())                         # 风级偏弱率