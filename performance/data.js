window.BENCHMARK_DATA = {
  "lastUpdate": 1709001496281,
  "repoUrl": "https://github.com/caiyunapp/cyeva",
  "entries": {
    "cyeva Benchmark": [
      {
        "commit": {
          "author": {
            "email": "clarmylee92510@gmail.com",
            "name": "Clarmy Lee",
            "username": "Clarmy"
          },
          "committer": {
            "email": "clarmylee92510@gmail.com",
            "name": "Clarmy Lee",
            "username": "Clarmy"
          },
          "distinct": true,
          "id": "5b416b2ee5444ccfa168ad11c2af6dfb67ec61d3",
          "message": "docs: change license",
          "timestamp": "2024-02-27T10:29:38+08:00",
          "tree_id": "edb85da1803374593b8c0f801c67248f00814842",
          "url": "https://github.com/caiyunapp/cyeva/commit/5b416b2ee5444ccfa168ad11c2af6dfb67ec61d3"
        },
        "date": 1709001495564,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 56779.49828539296,
            "unit": "iter/sec",
            "range": "stddev: 0.000004951134733828353",
            "extra": "mean: 17.611990774798006 usec\nrounds: 4661"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 94.11796453908674,
            "unit": "iter/sec",
            "range": "stddev: 0.00029481170118857207",
            "extra": "mean: 10.624964159575558 msec\nrounds: 94"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 14.05883096363889,
            "unit": "iter/sec",
            "range": "stddev: 0.0008785312322964992",
            "extra": "mean: 71.12966949999995 msec\nrounds: 14"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 61016.066925212894,
            "unit": "iter/sec",
            "range": "stddev: 0.000004109333928170096",
            "extra": "mean: 16.38912585476372 usec\nrounds: 12578"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 112.68379102760093,
            "unit": "iter/sec",
            "range": "stddev: 0.00023945346367525188",
            "extra": "mean: 8.874390814159408 msec\nrounds: 113"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 16.333197945213954,
            "unit": "iter/sec",
            "range": "stddev: 0.0006827458867277203",
            "extra": "mean: 61.224997294116896 msec\nrounds: 17"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 3416.2806453795747,
            "unit": "iter/sec",
            "range": "stddev: 0.00001711010103816553",
            "extra": "mean: 292.7159984214038 usec\nrounds: 1900"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 5.431699322287265,
            "unit": "iter/sec",
            "range": "stddev: 0.0019415114983723138",
            "extra": "mean: 184.1044470000052 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.5639646780936386,
            "unit": "iter/sec",
            "range": "stddev: 0.005501592608887255",
            "extra": "mean: 1.7731606939999949 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 3191.6537343941736,
            "unit": "iter/sec",
            "range": "stddev: 0.00004712892622988397",
            "extra": "mean: 313.31719641880755 usec\nrounds: 1787"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 5.291470683784398,
            "unit": "iter/sec",
            "range": "stddev: 0.006545641705552633",
            "extra": "mean: 188.98337716666921 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.5614931261325371,
            "unit": "iter/sec",
            "range": "stddev: 0.010292093073297901",
            "extra": "mean: 1.7809657027999948 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 3406.457340369714,
            "unit": "iter/sec",
            "range": "stddev: 0.000017509212693949778",
            "extra": "mean: 293.5601124808058 usec\nrounds: 1947"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 5.434268774955604,
            "unit": "iter/sec",
            "range": "stddev: 0.00016228874368106442",
            "extra": "mean: 184.01739800000408 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.5618042191755486,
            "unit": "iter/sec",
            "range": "stddev: 0.008294398136217141",
            "extra": "mean: 1.779979512200009 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}