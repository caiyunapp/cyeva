window.BENCHMARK_DATA = {
  "lastUpdate": 1686568788928,
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
          "id": "d67341a9322e3297f07a8d598d44f11824b292e9",
          "message": "tests: add test perf",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/43/commits/d67341a9322e3297f07a8d598d44f11824b292e9"
        },
        "date": 1686568788627,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae",
            "value": 23501.994103412642,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036553943106708498",
            "extra": "mean: 42.54958092491366 usec\nrounds: 2076"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe",
            "value": 12660.334070329953,
            "unit": "iter/sec",
            "range": "stddev: 0.000004321718497048767",
            "extra": "mean: 78.98685725391275 usec\nrounds: 5142"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio",
            "value": 1516.1642913071144,
            "unit": "iter/sec",
            "range": "stddev: 0.0000183662361078141",
            "extra": "mean: 659.5591293987545 usec\nrounds: 881"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio",
            "value": 1519.2751545051592,
            "unit": "iter/sec",
            "range": "stddev: 0.00001765188027610993",
            "extra": "mean: 658.208618125996 usec\nrounds: 982"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts",
            "value": 1531.4242400864466,
            "unit": "iter/sec",
            "range": "stddev: 0.000017436335272235607",
            "extra": "mean: 652.9869214709253 usec\nrounds: 1006"
          }
        ]
      }
    ]
  }
}