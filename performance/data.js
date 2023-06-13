window.BENCHMARK_DATA = {
  "lastUpdate": 1686646994579,
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
          "id": "f603cb46fbbf5cc0afc4634b392d7f1b4808d14a",
          "message": "tests: enlarge perf test",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/44/commits/f603cb46fbbf5cc0afc4634b392d7f1b4808d14a"
        },
        "date": 1686646994088,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mae_1e3",
            "value": 42815.02410508286,
            "unit": "iter/sec",
            "range": "stddev: 0.000004181059185851372",
            "extra": "mean: 23.356287212303197 usec\nrounds: 3910"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mbe_1e3",
            "value": 46068.01221646944,
            "unit": "iter/sec",
            "range": "stddev: 0.000003511634646756134",
            "extra": "mean: 21.707036008002476 usec\nrounds: 8026"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2424.759265354377,
            "unit": "iter/sec",
            "range": "stddev: 0.000022098868291117572",
            "extra": "mean: 412.4120749998869 usec\nrounds: 1480"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2422.84887442199,
            "unit": "iter/sec",
            "range": "stddev: 0.00002487622908561866",
            "extra": "mean: 412.73725759662426 usec\nrounds: 1448"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_ts_1e3",
            "value": 2444.864413911607,
            "unit": "iter/sec",
            "range": "stddev: 0.000022498138106183482",
            "extra": "mean: 409.02063701768725 usec\nrounds: 1529"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_hit_ratio_1e3",
            "value": 3959.7437278580805,
            "unit": "iter/sec",
            "range": "stddev: 0.000006491940351440103",
            "extra": "mean: 252.54159580193937 usec\nrounds: 3335"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_miss_ratio_1e3",
            "value": 4016.0974375102796,
            "unit": "iter/sec",
            "range": "stddev: 0.000006310064957591529",
            "extra": "mean: 248.99794279392165 usec\nrounds: 3164"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_binary_accuracy_ratio_1e3",
            "value": 3966.7854566997544,
            "unit": "iter/sec",
            "range": "stddev: 0.000006287777757093647",
            "extra": "mean: 252.09329088142056 usec\nrounds: 3290"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_ratio_1e3",
            "value": 3963.3867776448374,
            "unit": "iter/sec",
            "range": "stddev: 0.00000614654330321589",
            "extra": "mean: 252.3094656419654 usec\nrounds: 3318"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_rate_1e3",
            "value": 3954.5296588235965,
            "unit": "iter/sec",
            "range": "stddev: 0.00000845186222059462",
            "extra": "mean: 252.87457328047518 usec\nrounds: 3009"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ts_1e3",
            "value": 4011.6737266183154,
            "unit": "iter/sec",
            "range": "stddev: 0.000007521392990139875",
            "extra": "mean: 249.27251520102087 usec\nrounds: 3059"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ets_1e3",
            "value": 3960.908941885449,
            "unit": "iter/sec",
            "range": "stddev: 0.000007137205590245479",
            "extra": "mean: 252.4673035083674 usec\nrounds: 3107"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_bias_score_1e3",
            "value": 4008.1996625551333,
            "unit": "iter/sec",
            "range": "stddev: 0.000006570077167252056",
            "extra": "mean: 249.4885694797258 usec\nrounds: 3152"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_diff_accuracy_ratio_1e3",
            "value": 5730.473231162317,
            "unit": "iter/sec",
            "range": "stddev: 0.000010921000262349805",
            "extra": "mean: 174.5056576762281 usec\nrounds: 3374"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rmse_1e3",
            "value": 39875.24977039624,
            "unit": "iter/sec",
            "range": "stddev: 0.000004352836433953023",
            "extra": "mean: 25.07821282018425 usec\nrounds: 7457"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rss_1e3",
            "value": 43557.654751485185,
            "unit": "iter/sec",
            "range": "stddev: 0.000004021294762442724",
            "extra": "mean: 22.958077190000754 usec\nrounds: 8071"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_chi_square_1e3",
            "value": 42715.10128336934,
            "unit": "iter/sec",
            "range": "stddev: 0.000003632257909044438",
            "extra": "mean: 23.41092423885553 usec\nrounds: 8540"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_linregress_1e3",
            "value": 5170.662741604947,
            "unit": "iter/sec",
            "range": "stddev: 0.000019853184436566427",
            "extra": "mean: 193.39880591198744 usec\nrounds: 1793"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_accuracy_ratio_1e3",
            "value": 2381.8358407368246,
            "unit": "iter/sec",
            "range": "stddev: 0.00003164167115788254",
            "extra": "mean: 419.8442154983479 usec\nrounds: 1355"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_miss_ratio_1e3",
            "value": 2403.836763857807,
            "unit": "iter/sec",
            "range": "stddev: 0.000029763092331696497",
            "extra": "mean: 416.00162500017103 usec\nrounds: 1320"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_bias_score_1e3",
            "value": 2422.275358666975,
            "unit": "iter/sec",
            "range": "stddev: 0.000027197189604796223",
            "extra": "mean: 412.8349803097198 usec\nrounds: 1422"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_mae_1e3",
            "value": 9547.78329939943,
            "unit": "iter/sec",
            "range": "stddev: 0.000011502860531873216",
            "extra": "mean: 104.73635278912346 usec\nrounds: 2707"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mae_1e6",
            "value": 54.442525039677854,
            "unit": "iter/sec",
            "range": "stddev: 0.000617884946170184",
            "extra": "mean: 18.367994490909403 msec\nrounds: 55"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mbe_1e6",
            "value": 65.47872018267248,
            "unit": "iter/sec",
            "range": "stddev: 0.0004983449395601872",
            "extra": "mean: 15.272137225807114 msec\nrounds: 62"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.668481070746667,
            "unit": "iter/sec",
            "range": "stddev: 0.001446791311066942",
            "extra": "mean: 272.59238379999715 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.6801506035391642,
            "unit": "iter/sec",
            "range": "stddev: 0.0003854999855179542",
            "extra": "mean: 271.72801000000106 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_ts_1e6",
            "value": 3.6714417820313776,
            "unit": "iter/sec",
            "range": "stddev: 0.0006628966755039678",
            "extra": "mean: 272.3725607999995 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_hit_ratio_1e6",
            "value": 4.679405181790262,
            "unit": "iter/sec",
            "range": "stddev: 0.0003491979627306115",
            "extra": "mean: 213.702374799999 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_miss_ratio_1e6",
            "value": 4.678123661597552,
            "unit": "iter/sec",
            "range": "stddev: 0.00011306058613512251",
            "extra": "mean: 213.76091620000182 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_binary_accuracy_ratio_1e6",
            "value": 4.683511920810392,
            "unit": "iter/sec",
            "range": "stddev: 0.0003268930878340323",
            "extra": "mean: 213.51498979999803 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_ratio_1e6",
            "value": 4.6764977455103995,
            "unit": "iter/sec",
            "range": "stddev: 0.00030724251694723843",
            "extra": "mean: 213.83523620000346 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_rate_1e6",
            "value": 4.676829938185815,
            "unit": "iter/sec",
            "range": "stddev: 0.00022897317607408895",
            "extra": "mean: 213.82004760000086 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ts_1e6",
            "value": 4.681928246417588,
            "unit": "iter/sec",
            "range": "stddev: 0.00037365774641614054",
            "extra": "mean: 213.5872118000009 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ets_1e6",
            "value": 4.676198850496604,
            "unit": "iter/sec",
            "range": "stddev: 0.000423997926828209",
            "extra": "mean: 213.84890420000033 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_bias_score_1e6",
            "value": 4.676407478163296,
            "unit": "iter/sec",
            "range": "stddev: 0.00024531016552529713",
            "extra": "mean: 213.83936379999966 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_diff_accuracy_ratio_1e6",
            "value": 6.039331101523195,
            "unit": "iter/sec",
            "range": "stddev: 0.0020324291041268015",
            "extra": "mean: 165.581251166671 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rmse_1e6",
            "value": 59.70967973929876,
            "unit": "iter/sec",
            "range": "stddev: 0.001045848545595892",
            "extra": "mean: 16.747703293103346 msec\nrounds: 58"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rss_1e6",
            "value": 61.20091764784895,
            "unit": "iter/sec",
            "range": "stddev: 0.0003380544229063936",
            "extra": "mean: 16.339624280701408 msec\nrounds: 57"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_chi_square_1e6",
            "value": 61.832736029287055,
            "unit": "iter/sec",
            "range": "stddev: 0.00038557635889489725",
            "extra": "mean: 16.172662964911503 msec\nrounds: 57"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_linregress_1e6",
            "value": 34.85894779428503,
            "unit": "iter/sec",
            "range": "stddev: 0.0013052042505812544",
            "extra": "mean: 28.687039147060702 msec\nrounds: 34"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_accuracy_ratio_1e6",
            "value": 3.77394243899816,
            "unit": "iter/sec",
            "range": "stddev: 0.0008261768474595985",
            "extra": "mean: 264.97489459999883 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_miss_ratio_1e6",
            "value": 3.787388169041591,
            "unit": "iter/sec",
            "range": "stddev: 0.0004473736536423835",
            "extra": "mean: 264.0341985999953 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_bias_score_1e6",
            "value": 3.784350689335817,
            "unit": "iter/sec",
            "range": "stddev: 0.0001232429616860231",
            "extra": "mean: 264.24612360000594 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_mae_1e6",
            "value": 19.661323981720507,
            "unit": "iter/sec",
            "range": "stddev: 0.00032033385534586153",
            "extra": "mean: 50.86127470000079 msec\nrounds: 20"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_mae_1e7",
            "value": 5.441141829852222,
            "unit": "iter/sec",
            "range": "stddev: 0.000550581858285067",
            "extra": "mean: 183.7849538333316 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_mbe_1e7",
            "value": 6.477374753916615,
            "unit": "iter/sec",
            "range": "stddev: 0.00041270480275410967",
            "extra": "mean: 154.3835331428584 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.37199872905949755,
            "unit": "iter/sec",
            "range": "stddev: 0.0033082163957406058",
            "extra": "mean: 2.688181227199999 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3719837840132956,
            "unit": "iter/sec",
            "range": "stddev: 0.0038159366712572705",
            "extra": "mean: 2.688289229199995 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_ts_1e7",
            "value": 0.3719230477664269,
            "unit": "iter/sec",
            "range": "stddev: 0.0031647903283143755",
            "extra": "mean: 2.6887282356000015 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_hit_ratio_1e7",
            "value": 0.4604087010488268,
            "unit": "iter/sec",
            "range": "stddev: 0.0010391655652109402",
            "extra": "mean: 2.171983278600004 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_miss_ratio_1e7",
            "value": 0.46028733823730955,
            "unit": "iter/sec",
            "range": "stddev: 0.0011254064312846254",
            "extra": "mean: 2.172555959999994 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_binary_accuracy_ratio_1e7",
            "value": 0.4598109022202071,
            "unit": "iter/sec",
            "range": "stddev: 0.0018476836077540022",
            "extra": "mean: 2.1748070677999976 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_false_alarm_ratio_1e7",
            "value": 0.4606594530691571,
            "unit": "iter/sec",
            "range": "stddev: 0.002383804471675145",
            "extra": "mean: 2.170800996999998 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_false_alarm_rate_1e7",
            "value": 0.4605370266505951,
            "unit": "iter/sec",
            "range": "stddev: 0.0013599029062150536",
            "extra": "mean: 2.1713780697999994 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_ts_1e7",
            "value": 0.4597722708622691,
            "unit": "iter/sec",
            "range": "stddev: 0.004344348116986037",
            "extra": "mean: 2.1749898012000015 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_ets_1e7",
            "value": 0.4606577310571597,
            "unit": "iter/sec",
            "range": "stddev: 0.0009868718238371943",
            "extra": "mean: 2.1708091118000086 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_bias_score_1e7",
            "value": 0.46082532930772363,
            "unit": "iter/sec",
            "range": "stddev: 0.0010014961392867108",
            "extra": "mean: 2.1700196070000173 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_diff_accuracy_ratio_1e7",
            "value": 0.579220693569532,
            "unit": "iter/sec",
            "range": "stddev: 0.0033212771882336874",
            "extra": "mean: 1.7264576544000079 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_rmse_1e7",
            "value": 6.264976084111746,
            "unit": "iter/sec",
            "range": "stddev: 0.00034760045715832334",
            "extra": "mean: 159.61752871428254 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_rss_1e7",
            "value": 6.258257709582791,
            "unit": "iter/sec",
            "range": "stddev: 0.0002584854486384251",
            "extra": "mean: 159.78888157142788 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_chi_square_1e7",
            "value": 6.273962402284213,
            "unit": "iter/sec",
            "range": "stddev: 0.0003436051605797578",
            "extra": "mean: 159.38890542855688 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_linregress_1e7",
            "value": 3.3356256909431408,
            "unit": "iter/sec",
            "range": "stddev: 0.0010261542802704221",
            "extra": "mean: 299.79382960000294 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_accuracy_ratio_1e7",
            "value": 0.37414762732350765,
            "unit": "iter/sec",
            "range": "stddev: 0.006473596954906084",
            "extra": "mean: 2.6727417921999743 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_miss_ratio_1e7",
            "value": 0.3755400527898268,
            "unit": "iter/sec",
            "range": "stddev: 0.00262498607746705",
            "extra": "mean: 2.662831814000026 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_bias_score_1e7",
            "value": 0.37567597964607496,
            "unit": "iter/sec",
            "range": "stddev: 0.0006565845936141088",
            "extra": "mean: 2.661868349800011 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_mae_1e7",
            "value": 2.129091546176329,
            "unit": "iter/sec",
            "range": "stddev: 0.0008285290086811904",
            "extra": "mean: 469.6838901999854 msec\nrounds: 5"
          }
        ]
      }
    ]
  }
}