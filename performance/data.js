window.BENCHMARK_DATA = {
  "lastUpdate": 1686646329430,
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
      },
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
          "id": "f603cb46fbbf5cc0afc4634b392d7f1b4808d14a",
          "message": "tests: enlarge perf test",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/44/commits/f603cb46fbbf5cc0afc4634b392d7f1b4808d14a"
        },
        "date": 1686646328706,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mae_1e3",
            "value": 43384.38472277664,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023498440022729823",
            "extra": "mean: 23.04976793816333 usec\nrounds: 5059"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mbe_1e3",
            "value": 45930.734117750835,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022433941627467843",
            "extra": "mean: 21.771914148734023 usec\nrounds: 11683"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2627.351990068246,
            "unit": "iter/sec",
            "range": "stddev: 0.00001109609103908995",
            "extra": "mean: 380.6113546186953 usec\nrounds: 1613"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2618.6988269099797,
            "unit": "iter/sec",
            "range": "stddev: 0.000015184172706260193",
            "extra": "mean: 381.8690372958936 usec\nrounds: 1716"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_ts_1e3",
            "value": 2638.2898402792234,
            "unit": "iter/sec",
            "range": "stddev: 0.00001233370608914376",
            "extra": "mean: 379.0334119977376 usec\nrounds: 1767"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_hit_ratio_1e3",
            "value": 3905.70116617784,
            "unit": "iter/sec",
            "range": "stddev: 0.000007346678673751192",
            "extra": "mean: 256.03597342768813 usec\nrounds: 3387"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_miss_ratio_1e3",
            "value": 4114.759104064849,
            "unit": "iter/sec",
            "range": "stddev: 0.000004498317616233619",
            "extra": "mean: 243.02759279689778 usec\nrounds: 3443"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_binary_accuracy_ratio_1e3",
            "value": 4075.399531450716,
            "unit": "iter/sec",
            "range": "stddev: 0.000004926958053358105",
            "extra": "mean: 245.37471535803775 usec\nrounds: 3464"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_ratio_1e3",
            "value": 4031.31805370728,
            "unit": "iter/sec",
            "range": "stddev: 0.000004956872545571263",
            "extra": "mean: 248.05782790578385 usec\nrounds: 3347"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_rate_1e3",
            "value": 4062.159375873447,
            "unit": "iter/sec",
            "range": "stddev: 0.000005862266089870328",
            "extra": "mean: 246.17448688481844 usec\nrounds: 3393"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ts_1e3",
            "value": 4118.00870590482,
            "unit": "iter/sec",
            "range": "stddev: 0.000005988706232711918",
            "extra": "mean: 242.83581493310064 usec\nrounds: 3442"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ets_1e3",
            "value": 4054.9183777482494,
            "unit": "iter/sec",
            "range": "stddev: 0.000004665277498370259",
            "extra": "mean: 246.61408858131279 usec\nrounds: 3398"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_bias_score_1e3",
            "value": 4091.6304009777064,
            "unit": "iter/sec",
            "range": "stddev: 0.000004881943754932938",
            "extra": "mean: 244.40135153973026 usec\nrounds: 3442"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_diff_accuracy_ratio_1e3",
            "value": 5988.7862215778605,
            "unit": "iter/sec",
            "range": "stddev: 0.00000401811523900278",
            "extra": "mean: 166.97874377231167 usec\nrounds: 3934"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rmse_1e3",
            "value": 40464.90250694836,
            "unit": "iter/sec",
            "range": "stddev: 0.000005403281466035895",
            "extra": "mean: 24.71277423263992 usec\nrounds: 10719"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rss_1e3",
            "value": 43815.35791621094,
            "unit": "iter/sec",
            "range": "stddev: 0.000002371093579494965",
            "extra": "mean: 22.823047615229388 usec\nrounds: 12286"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_chi_square_1e3",
            "value": 42602.96727478375,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023091400055220732",
            "extra": "mean: 23.472543439289726 usec\nrounds: 12270"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_linregress_1e3",
            "value": 5681.27544430978,
            "unit": "iter/sec",
            "range": "stddev: 0.000013004994985423515",
            "extra": "mean: 176.01681344311064 usec\nrounds: 2187"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_accuracy_ratio_1e3",
            "value": 2666.9534820485515,
            "unit": "iter/sec",
            "range": "stddev: 0.000011109518744971071",
            "extra": "mean: 374.9596709245471 usec\nrounds: 1644"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_miss_ratio_1e3",
            "value": 2676.98652357714,
            "unit": "iter/sec",
            "range": "stddev: 0.000011808059564164073",
            "extra": "mean: 373.55436465318616 usec\nrounds: 1788"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_bias_score_1e3",
            "value": 2666.652184264596,
            "unit": "iter/sec",
            "range": "stddev: 0.000011221469276664098",
            "extra": "mean: 375.00203659885176 usec\nrounds: 1776"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_mae_1e3",
            "value": 10088.291838105708,
            "unit": "iter/sec",
            "range": "stddev: 0.000006334991768390997",
            "extra": "mean: 99.12480884254151 usec\nrounds: 3845"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mae_1e6",
            "value": 67.43718481640065,
            "unit": "iter/sec",
            "range": "stddev: 0.0004454448401863898",
            "extra": "mean: 14.82861425373144 msec\nrounds: 67"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mbe_1e6",
            "value": 85.20167317879117,
            "unit": "iter/sec",
            "range": "stddev: 0.0004794937946896448",
            "extra": "mean: 11.736858710527356 msec\nrounds: 76"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.9465734264174057,
            "unit": "iter/sec",
            "range": "stddev: 0.0013658587955849755",
            "extra": "mean: 253.38436459999514 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.755935055333663,
            "unit": "iter/sec",
            "range": "stddev: 0.025474560261259736",
            "extra": "mean: 266.24528520000297 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_ts_1e6",
            "value": 4.000996075179775,
            "unit": "iter/sec",
            "range": "stddev: 0.0006839779692516682",
            "extra": "mean: 249.93776079999463 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_hit_ratio_1e6",
            "value": 5.039556922760096,
            "unit": "iter/sec",
            "range": "stddev: 0.0005875902442335071",
            "extra": "mean: 198.4301428333334 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_miss_ratio_1e6",
            "value": 5.040638090545106,
            "unit": "iter/sec",
            "range": "stddev: 0.0004412966158720078",
            "extra": "mean: 198.38758149999572 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_binary_accuracy_ratio_1e6",
            "value": 5.014505917587813,
            "unit": "iter/sec",
            "range": "stddev: 0.00014575426683475948",
            "extra": "mean: 199.42144180000128 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_ratio_1e6",
            "value": 5.040491061091352,
            "unit": "iter/sec",
            "range": "stddev: 0.00013204373226614806",
            "extra": "mean: 198.3933683999993 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_rate_1e6",
            "value": 5.030197212838871,
            "unit": "iter/sec",
            "range": "stddev: 0.0006605614459260603",
            "extra": "mean: 198.79936266666456 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ts_1e6",
            "value": 5.013041289054991,
            "unit": "iter/sec",
            "range": "stddev: 0.00021990435077449966",
            "extra": "mean: 199.47970549999403 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ets_1e6",
            "value": 5.031000231041087,
            "unit": "iter/sec",
            "range": "stddev: 0.0006126455208257325",
            "extra": "mean: 198.76763150000207 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_bias_score_1e6",
            "value": 5.045868598078522,
            "unit": "iter/sec",
            "range": "stddev: 0.0007384623830607255",
            "extra": "mean: 198.1819344999991 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_diff_accuracy_ratio_1e6",
            "value": 6.213005843830971,
            "unit": "iter/sec",
            "range": "stddev: 0.00015235248961481497",
            "extra": "mean: 160.9526894285673 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rmse_1e6",
            "value": 84.97136343335934,
            "unit": "iter/sec",
            "range": "stddev: 0.00036401936074218427",
            "extra": "mean: 11.76867075675762 msec\nrounds: 74"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rss_1e6",
            "value": 85.22023912682943,
            "unit": "iter/sec",
            "range": "stddev: 0.0004798550427637325",
            "extra": "mean: 11.73430173684147 msec\nrounds: 76"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_chi_square_1e6",
            "value": 85.47677913243037,
            "unit": "iter/sec",
            "range": "stddev: 0.0002827260498434756",
            "extra": "mean: 11.699083776316442 msec\nrounds: 76"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_linregress_1e6",
            "value": 42.74496242262858,
            "unit": "iter/sec",
            "range": "stddev: 0.0008726226306201396",
            "extra": "mean: 23.394569636365247 msec\nrounds: 44"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_accuracy_ratio_1e6",
            "value": 4.097233933198016,
            "unit": "iter/sec",
            "range": "stddev: 0.0010137194817245823",
            "extra": "mean: 244.0670990000001 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_miss_ratio_1e6",
            "value": 4.100019150451384,
            "unit": "iter/sec",
            "range": "stddev: 0.00214456853455361",
            "extra": "mean: 243.9012998000038 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_bias_score_1e6",
            "value": 4.123055956233673,
            "unit": "iter/sec",
            "range": "stddev: 0.0005370471005899959",
            "extra": "mean: 242.53854680000018 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_mae_1e6",
            "value": 22.78775968289362,
            "unit": "iter/sec",
            "range": "stddev: 0.0002839781285236275",
            "extra": "mean: 43.88320808695744 msec\nrounds: 23"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_mae_1e7",
            "value": 6.834470531625041,
            "unit": "iter/sec",
            "range": "stddev: 0.0005124826697534507",
            "extra": "mean: 146.31711342856997 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_mbe_1e7",
            "value": 8.03726023836914,
            "unit": "iter/sec",
            "range": "stddev: 0.002099362502649655",
            "extra": "mean: 124.42050777777386 msec\nrounds: 9"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.39738009812746683,
            "unit": "iter/sec",
            "range": "stddev: 0.09383397531543189",
            "extra": "mean: 2.516482342000006 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.40402804391653835,
            "unit": "iter/sec",
            "range": "stddev: 0.0029831184559528483",
            "extra": "mean: 2.4750757158 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_ts_1e7",
            "value": 0.40013910605541914,
            "unit": "iter/sec",
            "range": "stddev: 0.01921632493156385",
            "extra": "mean: 2.4991308893999986 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_hit_ratio_1e7",
            "value": 0.486938289604302,
            "unit": "iter/sec",
            "range": "stddev: 0.005373068761613352",
            "extra": "mean: 2.053648319200005 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_miss_ratio_1e7",
            "value": 0.4968367860051006,
            "unit": "iter/sec",
            "range": "stddev: 0.004869003216057075",
            "extra": "mean: 2.0127334130000065 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_binary_accuracy_ratio_1e7",
            "value": 0.4966580903198006,
            "unit": "iter/sec",
            "range": "stddev: 0.0016926769326100102",
            "extra": "mean: 2.0134575867999955 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_false_alarm_ratio_1e7",
            "value": 0.4927931874251299,
            "unit": "iter/sec",
            "range": "stddev: 0.006910971961983125",
            "extra": "mean: 2.029248831999996 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_false_alarm_rate_1e7",
            "value": 0.495035874162207,
            "unit": "iter/sec",
            "range": "stddev: 0.009565670289619443",
            "extra": "mean: 2.0200556205999987 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_ts_1e7",
            "value": 0.49669869549792545,
            "unit": "iter/sec",
            "range": "stddev: 0.0020219822120303944",
            "extra": "mean: 2.013292986399995 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_ets_1e7",
            "value": 0.4964958085964376,
            "unit": "iter/sec",
            "range": "stddev: 0.0019752720166736687",
            "extra": "mean: 2.014115693799988 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_bias_score_1e7",
            "value": 0.4968747773969926,
            "unit": "iter/sec",
            "range": "stddev: 0.0016757674972582813",
            "extra": "mean: 2.012579518000007 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_diff_accuracy_ratio_1e7",
            "value": 0.6198998736707396,
            "unit": "iter/sec",
            "range": "stddev: 0.000981726399575711",
            "extra": "mean: 1.613163742200004 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_rmse_1e7",
            "value": 7.608359670732616,
            "unit": "iter/sec",
            "range": "stddev: 0.0005731150708124074",
            "extra": "mean: 131.43437524999513 msec\nrounds: 8"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_rss_1e7",
            "value": 7.598170047607848,
            "unit": "iter/sec",
            "range": "stddev: 0.0011948046039518144",
            "extra": "mean: 131.61063700000142 msec\nrounds: 8"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_chi_square_1e7",
            "value": 7.633740621322407,
            "unit": "iter/sec",
            "range": "stddev: 0.0005226560390567747",
            "extra": "mean: 130.99737724999727 msec\nrounds: 8"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_linregress_1e7",
            "value": 4.083761776435456,
            "unit": "iter/sec",
            "range": "stddev: 0.0011399110833421396",
            "extra": "mean: 244.87226600001577 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_accuracy_ratio_1e7",
            "value": 0.40800940163008087,
            "unit": "iter/sec",
            "range": "stddev: 0.006073769257916011",
            "extra": "mean: 2.4509239149999873 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_miss_ratio_1e7",
            "value": 0.40671983530314276,
            "unit": "iter/sec",
            "range": "stddev: 0.022259505557944013",
            "extra": "mean: 2.458694937400003 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_bias_score_1e7",
            "value": 0.40744960700847443,
            "unit": "iter/sec",
            "range": "stddev: 0.0036012637309801696",
            "extra": "mean: 2.4542912370000183 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_mae_1e7",
            "value": 2.4602057161727373,
            "unit": "iter/sec",
            "range": "stddev: 0.002047064916558158",
            "extra": "mean: 406.47007420000136 msec\nrounds: 5"
          }
        ]
      }
    ]
  }
}