window.BENCHMARK_DATA = {
  "lastUpdate": 1686621673805,
  "repoUrl": "https://github.com/caiyunapp/cyeva",
  "entries": {
    "cyeva Benchmark": [
      {
        "commit": {
          "author": {
            "name": "caiyunapp",
            "username": "caiyunapp"
          },
          "committer": {
            "name": "caiyunapp",
            "username": "caiyunapp"
          },
          "id": "3be5dd344193d9f5824102933fdcf26b2e0e9efe",
          "message": "tests: add test perf",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/43/commits/3be5dd344193d9f5824102933fdcf26b2e0e9efe"
        },
        "date": 1686621673239,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 39678.9005792443,
            "unit": "iter/sec",
            "range": "stddev: 0.000005364374814113715",
            "extra": "mean: 25.20231118810514 usec\nrounds: 4049"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 50.00946595841249,
            "unit": "iter/sec",
            "range": "stddev: 0.0008059049627991118",
            "extra": "mean: 19.99621433333427 msec\nrounds: 51"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.020983972371509,
            "unit": "iter/sec",
            "range": "stddev: 0.0010944600803583057",
            "extra": "mean: 199.1641489999978 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 41738.829731876256,
            "unit": "iter/sec",
            "range": "stddev: 0.0000052143014596714935",
            "extra": "mean: 23.95850593856714 usec\nrounds: 7746"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 64.57363176307896,
            "unit": "iter/sec",
            "range": "stddev: 0.0005900066995170291",
            "extra": "mean: 15.48619727118657 msec\nrounds: 59"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.016240836982795,
            "unit": "iter/sec",
            "range": "stddev: 0.0015196980736878407",
            "extra": "mean: 166.21675014285333 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2293.088556656665,
            "unit": "iter/sec",
            "range": "stddev: 0.000059371140183735345",
            "extra": "mean: 436.09305759128864 usec\nrounds: 1146"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.3315548649470452,
            "unit": "iter/sec",
            "range": "stddev: 0.006917115132973592",
            "extra": "mean: 300.16014759999905 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3215632091679045,
            "unit": "iter/sec",
            "range": "stddev: 0.0724270429935415",
            "extra": "mean: 3.109808496400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2111.1761069447957,
            "unit": "iter/sec",
            "range": "stddev: 0.000045411482219643376",
            "extra": "mean: 473.6696274225828 usec\nrounds: 1393"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.142764241129929,
            "unit": "iter/sec",
            "range": "stddev: 0.002967177356527168",
            "extra": "mean: 318.1912237999967 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3191777250910198,
            "unit": "iter/sec",
            "range": "stddev: 0.055992639790702514",
            "extra": "mean: 3.133050715600001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2027.602538735723,
            "unit": "iter/sec",
            "range": "stddev: 0.0000363406273704067",
            "extra": "mean: 493.1933063289282 usec\nrounds: 1185"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.1736787756749383,
            "unit": "iter/sec",
            "range": "stddev: 0.003914607042140578",
            "extra": "mean: 315.091750199997 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.3151602360164938,
            "unit": "iter/sec",
            "range": "stddev: 0.048589605912347004",
            "extra": "mean: 3.172989120200003 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}