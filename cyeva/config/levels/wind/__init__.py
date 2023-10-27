import numpy as np

# 通用风速等级
GENERAL_WIND_SPEED_LEVELS = {
    0: {"min": 0, "max": 0.2},
    1: {"min": 0.2, "max": 1.5},
    2: {"min": 1.5, "max": 3.3},
    3: {"min": 3.3, "max": 5.4},
    4: {"min": 5.4, "max": 7.9},
    5: {"min": 7.9, "max": 10.7},
    6: {"min": 10.7, "max": 13.8},
    7: {"min": 13.8, "max": 17.1},
    8: {"min": 17.1, "max": 20.7},
    9: {"min": 20.7, "max": 24.4},
    10: {"min": 24.4, "max": 28.4},
    11: {"min": 28.4, "max": 32.6},
    12: {"min": 32.6, "max": 36.9},
    13: {"min": 36.9, "max": np.inf},
}

# 专门用于计算风速准确率的观测风速等级映射，不同等级的风速范围会有重叠
# OBS_WIND_SPEED_MAPPING_LEVELS_FOR_ACCURACY = {
#     0: {"min": 0, "max": 0.9},
#     1: {"min": 0.1, "max": 2.4},
#     2: {"min": 0.9, "max": 4.4},
#     3: {"min": 2.5, "max": 6.6},
#     4: {"min": 4.5, "max": 9.3},
#     5: {"min": 6.7, "max": 12.2},
#     6: {"min": 9.4, "max": 15.4},
#     7: {"min": 12.3, "max": 18.9},
#     8: {"min": 15.5, "max": 22.6},
#     9: {"min": 19, "max": 26.5},
#     10: {"min": 22.7, "max": 30.5},
#     11: {"min": 26.6, "max": 34.7},
#     12: {"min": 30.6, "max": 39.2},
#     13: {"min": 34.8, "max": np.inf},
# }

# EXCLUSIVE_LEVEL = []
# CROSS_LEVEL = []
# for n in range(1, max(OBS_WIND_SPEED_MAPPING_LEVELS_FOR_ACCURACY)):
#     pn = n - 1
#     ln = n + 1
#     previous_items = OBS_WIND_SPEED_MAPPING_LEVELS_FOR_ACCURACY[pn]
#     current_items = OBS_WIND_SPEED_MAPPING_LEVELS_FOR_ACCURACY[n]
#     latter_items = OBS_WIND_SPEED_MAPPING_LEVELS_FOR_ACCURACY[ln]
#     pmin = previous_items["min"]
#     pmax = previous_items["max"]
#     cmin = current_items["min"]
#     cmax = current_items["max"]
#     lmin = latter_items["min"]
#     lmax = latter_items["max"]
#     if pmax > cmin:
#         CROSS_LEVEL.append((pn, n, cmin, pmax))
#     if cmax > lmin:
#         CROSS_LEVEL.append((n, ln, lmin, cmax))
#     if n == 1:
#         EXCLUSIVE_LEVEL.append((pn, pmin, cmin))
#     if pmax < lmin:
#         EXCLUSIVE_LEVEL.append((n, pmax, lmin))
#     if n == max(OBS_WIND_SPEED_MAPPING_LEVELS_FOR_ACCURACY) - 1:
#         EXCLUSIVE_LEVEL.append((ln, cmax, lmax))

# EXCLUSIVE_LEVELS = np.array(sorted(set(EXCLUSIVE_LEVEL)))
# CROSS_LEVELS = np.array(sorted(set(CROSS_LEVEL)))

# CROSS_LEVELS_LEV = CROSS_LEVELS[:, 0:2]
# CROSS_LEVELS_MIN = CROSS_LEVELS[:, 2]
# CROSS_LEVELS_MAX = CROSS_LEVELS[:, 3]

# EXCLUSIVE_LEVELS_LEV = EXCLUSIVE_LEVELS[:, 0]
# EXCLUSIVE_LEVELS_MIN = EXCLUSIVE_LEVELS[:, 1]
# EXCLUSIVE_LEVELS_MAX = EXCLUSIVE_LEVELS[:, 1]
