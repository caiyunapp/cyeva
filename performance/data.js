window.BENCHMARK_DATA = {
  "lastUpdate": 1686622028399,
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
      },
      {
        "commit": {
          "author": {
            "email": "clarmylee92510@gmail.com",
            "name": "Wentao Li",
            "username": "Clarmy"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "50fe03b7c0effe108480d5cf5775d91825a4a311",
          "message": "tests: add test perf (#43)",
          "timestamp": "2023-06-13T10:05:06+08:00",
          "tree_id": "812574a9dfca8bba6df61fa087bd2bc2a02fbcac",
          "url": "https://github.com/caiyunapp/cyeva/commit/50fe03b7c0effe108480d5cf5775d91825a4a311"
        },
        "date": 1686622028084,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 42270.67109986079,
            "unit": "iter/sec",
            "range": "stddev: 0.000004281380964849338",
            "extra": "mean: 23.65706467346087 usec\nrounds: 3278"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 51.81241610763764,
            "unit": "iter/sec",
            "range": "stddev: 0.0006087846296393899",
            "extra": "mean: 19.30039313207381 msec\nrounds: 53"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.172029457811129,
            "unit": "iter/sec",
            "range": "stddev: 0.0008532979549611077",
            "extra": "mean: 193.34769999999443 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 45238.58060854268,
            "unit": "iter/sec",
            "range": "stddev: 0.000003551075488998547",
            "extra": "mean: 22.105025987733217 usec\nrounds: 7542"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 67.0980164382638,
            "unit": "iter/sec",
            "range": "stddev: 0.0005091936231856643",
            "extra": "mean: 14.903570225806748 msec\nrounds: 62"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.21389243589204,
            "unit": "iter/sec",
            "range": "stddev: 0.0010414707448548753",
            "extra": "mean: 160.92972485714492 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2385.5281872166966,
            "unit": "iter/sec",
            "range": "stddev: 0.00002084223024543599",
            "extra": "mean: 419.1943760541958 usec\nrounds: 1186"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.4954087784722816,
            "unit": "iter/sec",
            "range": "stddev: 0.0005556137533052021",
            "extra": "mean: 286.0895715999959 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.348745810592343,
            "unit": "iter/sec",
            "range": "stddev: 0.003963907606760517",
            "extra": "mean: 2.867417957799995 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2366.97242323866,
            "unit": "iter/sec",
            "range": "stddev: 0.00002434137585621667",
            "extra": "mean: 422.4806297623564 usec\nrounds: 1391"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.4897309536783796,
            "unit": "iter/sec",
            "range": "stddev: 0.0009134558585799021",
            "extra": "mean: 286.5550419999977 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.34869496198214456,
            "unit": "iter/sec",
            "range": "stddev: 0.006321889393596833",
            "extra": "mean: 2.867836100400001 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2381.8789279457596,
            "unit": "iter/sec",
            "range": "stddev: 0.000020836959703328168",
            "extra": "mean: 419.83662068938384 usec\nrounds: 1450"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.4979535694865898,
            "unit": "iter/sec",
            "range": "stddev: 0.00026176799843440535",
            "extra": "mean: 285.88143899999636 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.3492030063868499,
            "unit": "iter/sec",
            "range": "stddev: 0.0034856303368215875",
            "extra": "mean: 2.8636637764 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}