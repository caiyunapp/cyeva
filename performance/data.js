window.BENCHMARK_DATA = {
  "lastUpdate": 1686651486919,
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
          "id": "1ca04f4450f5fac132d094dd159f9dbef691944e",
          "message": "tests: enlarge perf test",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/44/commits/1ca04f4450f5fac132d094dd159f9dbef691944e"
        },
        "date": 1686651218807,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mae_1e3",
            "value": 40349.79579945891,
            "unit": "iter/sec",
            "range": "stddev: 0.000004613866197677493",
            "extra": "mean: 24.783272881232524 usec\nrounds: 3540"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mbe_1e3",
            "value": 45486.153346645544,
            "unit": "iter/sec",
            "range": "stddev: 0.000003483425427542086",
            "extra": "mean: 21.984712410809887 usec\nrounds: 9524"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2449.8255021716814,
            "unit": "iter/sec",
            "range": "stddev: 0.000022640190421463706",
            "extra": "mean: 408.19233823532994 usec\nrounds: 1428"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2481.1640029583027,
            "unit": "iter/sec",
            "range": "stddev: 0.000016236547687750595",
            "extra": "mean: 403.036638774259 usec\nrounds: 1697"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_ts_1e3",
            "value": 2479.608258754952,
            "unit": "iter/sec",
            "range": "stddev: 0.000017152681656076553",
            "extra": "mean: 403.2895101350061 usec\nrounds: 1480"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_hit_ratio_1e3",
            "value": 3941.713528969964,
            "unit": "iter/sec",
            "range": "stddev: 0.000005730608917856691",
            "extra": "mean: 253.69677239363378 usec\nrounds: 3405"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_miss_ratio_1e3",
            "value": 3987.6649500437356,
            "unit": "iter/sec",
            "range": "stddev: 0.000006468417399955842",
            "extra": "mean: 250.77332537404686 usec\nrounds: 3141"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_binary_accuracy_ratio_1e3",
            "value": 3942.7953629592334,
            "unit": "iter/sec",
            "range": "stddev: 0.000006154377258824823",
            "extra": "mean: 253.62716244280506 usec\nrounds: 3275"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_ratio_1e3",
            "value": 3931.548939244939,
            "unit": "iter/sec",
            "range": "stddev: 0.000005798559601400409",
            "extra": "mean: 254.35267764771908 usec\nrounds: 3248"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_rate_1e3",
            "value": 3919.474880991652,
            "unit": "iter/sec",
            "range": "stddev: 0.000006284025989155504",
            "extra": "mean: 255.13621859135216 usec\nrounds: 3152"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ts_1e3",
            "value": 3982.639139818085,
            "unit": "iter/sec",
            "range": "stddev: 0.0000063179206837964175",
            "extra": "mean: 251.08978365679323 usec\nrounds: 3194"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ets_1e3",
            "value": 3923.6413221024154,
            "unit": "iter/sec",
            "range": "stddev: 0.000006377665994904687",
            "extra": "mean: 254.86529422729373 usec\nrounds: 3222"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_bias_score_1e3",
            "value": 3983.056531872766,
            "unit": "iter/sec",
            "range": "stddev: 0.000005751429755264643",
            "extra": "mean: 251.0634714817409 usec\nrounds: 3226"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_diff_accuracy_ratio_1e3",
            "value": 5784.53583187668,
            "unit": "iter/sec",
            "range": "stddev: 0.000008929271960049589",
            "extra": "mean: 172.87471787957955 usec\nrounds: 3339"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rmse_1e3",
            "value": 39973.4578770881,
            "unit": "iter/sec",
            "range": "stddev: 0.000003901719736071557",
            "extra": "mean: 25.016599841695907 usec\nrounds: 7582"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rss_1e3",
            "value": 43890.00304509519,
            "unit": "iter/sec",
            "range": "stddev: 0.000003173138492444527",
            "extra": "mean: 22.784231729775474 usec\nrounds: 9209"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_chi_square_1e3",
            "value": 43324.264130817006,
            "unit": "iter/sec",
            "range": "stddev: 0.000003115628569170154",
            "extra": "mean: 23.08175384076955 usec\nrounds: 8397"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_linregress_1e3",
            "value": 5326.064200642145,
            "unit": "iter/sec",
            "range": "stddev: 0.000014338241934285897",
            "extra": "mean: 187.75590423401832 usec\nrounds: 1984"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_accuracy_ratio_1e3",
            "value": 2508.344962427538,
            "unit": "iter/sec",
            "range": "stddev: 0.00001611646891314209",
            "extra": "mean: 398.6692480416311 usec\nrounds: 1532"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_miss_ratio_1e3",
            "value": 2483.9811349871215,
            "unit": "iter/sec",
            "range": "stddev: 0.000020369024313294963",
            "extra": "mean: 402.57954696793 usec\nrounds: 1682"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_bias_score_1e3",
            "value": 2469.832680367745,
            "unit": "iter/sec",
            "range": "stddev: 0.000021871453772008946",
            "extra": "mean: 404.8857268546245 usec\nrounds: 1523"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_mae_1e3",
            "value": 9659.916853017286,
            "unit": "iter/sec",
            "range": "stddev: 0.000010143235653006199",
            "extra": "mean: 103.52055977455424 usec\nrounds: 3371"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mae_1e6",
            "value": 55.88642088281529,
            "unit": "iter/sec",
            "range": "stddev: 0.0004647426248088671",
            "extra": "mean: 17.893434294116577 msec\nrounds: 51"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mbe_1e6",
            "value": 69.30790626475192,
            "unit": "iter/sec",
            "range": "stddev: 0.00034715814820056236",
            "extra": "mean: 14.4283683333336 msec\nrounds: 63"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.645261393339586,
            "unit": "iter/sec",
            "range": "stddev: 0.0015837230448373636",
            "extra": "mean: 274.32874959999936 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.659654813423917,
            "unit": "iter/sec",
            "range": "stddev: 0.0007996101111319281",
            "extra": "mean: 273.2498147999962 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_ts_1e6",
            "value": 3.658099711008418,
            "unit": "iter/sec",
            "range": "stddev: 0.0006074482909139093",
            "extra": "mean: 273.36597660000166 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_hit_ratio_1e6",
            "value": 4.681071957838838,
            "unit": "iter/sec",
            "range": "stddev: 0.000434594696565034",
            "extra": "mean: 213.62628239999992 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_miss_ratio_1e6",
            "value": 4.681284509340998,
            "unit": "iter/sec",
            "range": "stddev: 0.00058467084866049",
            "extra": "mean: 213.6165828000003 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_binary_accuracy_ratio_1e6",
            "value": 4.645282679530886,
            "unit": "iter/sec",
            "range": "stddev: 0.000422081281674601",
            "extra": "mean: 215.27215220000073 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_ratio_1e6",
            "value": 4.662755902628498,
            "unit": "iter/sec",
            "range": "stddev: 0.00021457043039321618",
            "extra": "mean: 214.46544079999512 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_rate_1e6",
            "value": 4.691167698573776,
            "unit": "iter/sec",
            "range": "stddev: 0.0003276775089371101",
            "extra": "mean: 213.1665427999991 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ts_1e6",
            "value": 4.68391605625412,
            "unit": "iter/sec",
            "range": "stddev: 0.0001501602948026269",
            "extra": "mean: 213.4965674 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ets_1e6",
            "value": 4.570394811846485,
            "unit": "iter/sec",
            "range": "stddev: 0.0034133615232256236",
            "extra": "mean: 218.7994782000004 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_bias_score_1e6",
            "value": 4.6906503345777315,
            "unit": "iter/sec",
            "range": "stddev: 0.000385346260804281",
            "extra": "mean: 213.19005439999898 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_diff_accuracy_ratio_1e6",
            "value": 6.0989524983737775,
            "unit": "iter/sec",
            "range": "stddev: 0.0002351635306246403",
            "extra": "mean: 163.96258214285808 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rmse_1e6",
            "value": 66.41126678942452,
            "unit": "iter/sec",
            "range": "stddev: 0.0005812504576796759",
            "extra": "mean: 15.057685967213658 msec\nrounds: 61"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rss_1e6",
            "value": 67.4385806254232,
            "unit": "iter/sec",
            "range": "stddev: 0.0003851650192155422",
            "extra": "mean: 14.828307338707793 msec\nrounds: 62"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_chi_square_1e6",
            "value": 65.01240547537807,
            "unit": "iter/sec",
            "range": "stddev: 0.0005004099167986513",
            "extra": "mean: 15.3816797377037 msec\nrounds: 61"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_linregress_1e6",
            "value": 33.57825017319902,
            "unit": "iter/sec",
            "range": "stddev: 0.0010538588307100808",
            "extra": "mean: 29.78118260605983 msec\nrounds: 33"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_accuracy_ratio_1e6",
            "value": 3.770348944633604,
            "unit": "iter/sec",
            "range": "stddev: 0.0003414460314200884",
            "extra": "mean: 265.2274403999968 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_miss_ratio_1e6",
            "value": 3.7669113006097126,
            "unit": "iter/sec",
            "range": "stddev: 0.0008139650579533809",
            "extra": "mean: 265.46948419999694 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_bias_score_1e6",
            "value": 3.7700788632033344,
            "unit": "iter/sec",
            "range": "stddev: 0.0010689459119481285",
            "extra": "mean: 265.24644080000144 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_mae_1e6",
            "value": 19.231735884386282,
            "unit": "iter/sec",
            "range": "stddev: 0.00035889655601830284",
            "extra": "mean: 51.997386299999704 msec\nrounds: 20"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_mae_1e7",
            "value": 5.2268125339491185,
            "unit": "iter/sec",
            "range": "stddev: 0.00023771429595433703",
            "extra": "mean: 191.32119116666502 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_mbe_1e7",
            "value": 6.238347285276664,
            "unit": "iter/sec",
            "range": "stddev: 0.0001458195157931282",
            "extra": "mean: 160.2988667142873 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.36701202361315544,
            "unit": "iter/sec",
            "range": "stddev: 0.0011512958433529898",
            "extra": "mean: 2.724706373799998 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3666649335344138,
            "unit": "iter/sec",
            "range": "stddev: 0.002526418803495991",
            "extra": "mean: 2.7272856184000034 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_ts_1e7",
            "value": 0.366802170453043,
            "unit": "iter/sec",
            "range": "stddev: 0.0023491148211885952",
            "extra": "mean: 2.7262652201999913 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_hit_ratio_1e7",
            "value": 0.45762389317901037,
            "unit": "iter/sec",
            "range": "stddev: 0.0017127141705774501",
            "extra": "mean: 2.185200587000003 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_miss_ratio_1e7",
            "value": 0.45752116320689906,
            "unit": "iter/sec",
            "range": "stddev: 0.0016125224217810714",
            "extra": "mean: 2.1856912432000057 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_binary_accuracy_ratio_1e7",
            "value": 0.45465736225529996,
            "unit": "iter/sec",
            "range": "stddev: 0.011186447365522078",
            "extra": "mean: 2.199458500000003 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_false_alarm_ratio_1e7",
            "value": 0.4576990061485971,
            "unit": "iter/sec",
            "range": "stddev: 0.001394566597153271",
            "extra": "mean: 2.184841973800002 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_false_alarm_rate_1e7",
            "value": 0.45752954002712665,
            "unit": "iter/sec",
            "range": "stddev: 0.0018667856268918975",
            "extra": "mean: 2.185651225800001 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_ts_1e7",
            "value": 0.4575190579032807,
            "unit": "iter/sec",
            "range": "stddev: 0.0010709218996240203",
            "extra": "mean: 2.1857013008000195 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_ets_1e7",
            "value": 0.45575568900105523,
            "unit": "iter/sec",
            "range": "stddev: 0.014525385165844092",
            "extra": "mean: 2.1941580196000245 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_bias_score_1e7",
            "value": 0.4579154148952363,
            "unit": "iter/sec",
            "range": "stddev: 0.0013339022399615102",
            "extra": "mean: 2.1838094274000013 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_diff_accuracy_ratio_1e7",
            "value": 0.6051453118935205,
            "unit": "iter/sec",
            "range": "stddev: 0.005818155382370118",
            "extra": "mean: 1.6524956573999816 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_rmse_1e7",
            "value": 6.0138895108253045,
            "unit": "iter/sec",
            "range": "stddev: 0.0001825909366067419",
            "extra": "mean: 166.28173799999976 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_rss_1e7",
            "value": 6.004770592077925,
            "unit": "iter/sec",
            "range": "stddev: 0.00038659799822560685",
            "extra": "mean: 166.53425550000142 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_chi_square_1e7",
            "value": 6.0178734796953925,
            "unit": "iter/sec",
            "range": "stddev: 0.00026266460732389594",
            "extra": "mean: 166.17165571427353 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_linregress_1e7",
            "value": 3.2132168957526885,
            "unit": "iter/sec",
            "range": "stddev: 0.0003213226816512454",
            "extra": "mean: 311.2145966000071 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_accuracy_ratio_1e7",
            "value": 0.37066728741536525,
            "unit": "iter/sec",
            "range": "stddev: 0.0025680802514146716",
            "extra": "mean: 2.697837208599992 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_miss_ratio_1e7",
            "value": 0.3703149481574455,
            "unit": "iter/sec",
            "range": "stddev: 0.002922897817606761",
            "extra": "mean: 2.7004040884000005 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_bias_score_1e7",
            "value": 0.37042746520619285,
            "unit": "iter/sec",
            "range": "stddev: 0.001494928533001213",
            "extra": "mean: 2.699583842800007 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e7.py::test_calc_threshold_mae_1e7",
            "value": 2.0573895262494535,
            "unit": "iter/sec",
            "range": "stddev: 0.0005145417466003034",
            "extra": "mean: 486.05282920000263 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_angle_deflection_1e3",
            "value": 48265.99813093403,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028146104285273465",
            "extra": "mean: 20.718519013887185 usec\nrounds: 15699"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_dir_deflection_1e3",
            "value": 33624.956673239554,
            "unit": "iter/sec",
            "range": "stddev: 0.000004516060124161551",
            "extra": "mean: 29.739815272263257 usec\nrounds: 9311"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_direction8_1e3",
            "value": 1144.5302182304497,
            "unit": "iter/sec",
            "range": "stddev: 0.00005308575369738084",
            "extra": "mean: 873.7209241588162 usec\nrounds: 923"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_direction16_1e3",
            "value": 596.8285488030286,
            "unit": "iter/sec",
            "range": "stddev: 0.00010238761443352559",
            "extra": "mean: 1.6755230660556588 msec\nrounds: 545"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_wind_scale_1e3",
            "value": 7856.311959078236,
            "unit": "iter/sec",
            "range": "stddev: 0.000003953017945248871",
            "extra": "mean: 127.28618787145614 usec\nrounds: 5046"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_dir_score_1e3",
            "value": 525.9679970469386,
            "unit": "iter/sec",
            "range": "stddev: 0.00006131837566963972",
            "extra": "mean: 1.9012563608708641 msec\nrounds: 460"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_lev_deflection_1e3",
            "value": 252056.2616367912,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012760414805964226",
            "extra": "mean: 3.9673682117882993 usec\nrounds: 49018"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_dir_accuracy_ratio_1e3",
            "value": 14539.427650111147,
            "unit": "iter/sec",
            "range": "stddev: 0.000006615552934677963",
            "extra": "mean: 68.77849830576758 usec\nrounds: 4722"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_accuracy_ratio_1e3",
            "value": 1484.3593347686162,
            "unit": "iter/sec",
            "range": "stddev: 0.00003481642751321847",
            "extra": "mean: 673.6913202731206 usec\nrounds: 1174"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_accuracy_ratio_1e3",
            "value": 4059.476207626249,
            "unit": "iter/sec",
            "range": "stddev: 0.000020352777824964456",
            "extra": "mean: 246.33719939566862 usec\nrounds: 331"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_score_1e3",
            "value": 1701.4376785919542,
            "unit": "iter/sec",
            "range": "stddev: 0.00003029413178341051",
            "extra": "mean: 587.7382478255462 usec\nrounds: 1150"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_stronger_ratio_1e3",
            "value": 2169.08890661216,
            "unit": "iter/sec",
            "range": "stddev: 0.000013925283824940997",
            "extra": "mean: 461.0230576310827 usec\nrounds: 1874"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_weaker_ratio_1e3",
            "value": 2161.8473334744695,
            "unit": "iter/sec",
            "range": "stddev: 0.000013966587044223904",
            "extra": "mean: 462.5673536312224 usec\nrounds: 1790"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_chi_square_1e3",
            "value": 13004.142934109484,
            "unit": "iter/sec",
            "range": "stddev: 0.000006683799298919451",
            "extra": "mean: 76.89857033000071 usec\nrounds: 4941"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_rss_1e3",
            "value": 13110.618662511184,
            "unit": "iter/sec",
            "range": "stddev: 0.00000699185925436404",
            "extra": "mean: 76.27405126650689 usec\nrounds: 4857"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_mae_1e3",
            "value": 13088.23580489448,
            "unit": "iter/sec",
            "range": "stddev: 0.000006751233568780637",
            "extra": "mean: 76.40449140028787 usec\nrounds: 5291"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_linregress_1e3",
            "value": 5267.351294780864,
            "unit": "iter/sec",
            "range": "stddev: 0.000014126823701326695",
            "extra": "mean: 189.84873877518788 usec\nrounds: 2205"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_filter_wind_scales_1e3",
            "value": 2876.1084849377517,
            "unit": "iter/sec",
            "range": "stddev: 0.000015129107931561423",
            "extra": "mean: 347.6920308246451 usec\nrounds: 1687"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_angle_deflection_1e6",
            "value": 70.86022849771466,
            "unit": "iter/sec",
            "range": "stddev: 0.00028974600009516906",
            "extra": "mean: 14.112288673077753 msec\nrounds: 52"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_dir_deflection_1e6",
            "value": 31.22811117174749,
            "unit": "iter/sec",
            "range": "stddev: 0.0006390181287880168",
            "extra": "mean: 32.02242987096555 msec\nrounds: 31"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_direction8_1e6",
            "value": 2.131498113230527,
            "unit": "iter/sec",
            "range": "stddev: 0.001408969865205029",
            "extra": "mean: 469.1535937999902 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_direction16_1e6",
            "value": 1.1235409429350605,
            "unit": "iter/sec",
            "range": "stddev: 0.004153850076857536",
            "extra": "mean: 890.0432211999942 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_wind_scale_1e6",
            "value": 22.029335298261312,
            "unit": "iter/sec",
            "range": "stddev: 0.00043817102368763974",
            "extra": "mean: 45.39401604545581 msec\nrounds: 22"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_dir_score_1e6",
            "value": 1.0429245849401743,
            "unit": "iter/sec",
            "range": "stddev: 0.004527147430590525",
            "extra": "mean: 958.8421007999955 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_lev_deflection_1e6",
            "value": 453.6394479784032,
            "unit": "iter/sec",
            "range": "stddev: 0.00008410267347161962",
            "extra": "mean: 2.2043938296292254 msec\nrounds: 135"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_dir_accuracy_ratio_1e6",
            "value": 49.71022953461155,
            "unit": "iter/sec",
            "range": "stddev: 0.0004656689215275336",
            "extra": "mean: 20.116583837210687 msec\nrounds: 43"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_accuracy_ratio_1e6",
            "value": 4.435169362020176,
            "unit": "iter/sec",
            "range": "stddev: 0.0003240882936970548",
            "extra": "mean: 225.47053300000925 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_accuracy_ratio_1e6",
            "value": 6.177301827771594,
            "unit": "iter/sec",
            "range": "stddev: 0.0007723903471496758",
            "extra": "mean: 161.88297542856844 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_score_1e6",
            "value": 4.94356936334708,
            "unit": "iter/sec",
            "range": "stddev: 0.0014025473134196514",
            "extra": "mean: 202.28299160000915 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_stronger_ratio_1e6",
            "value": 4.134375451065647,
            "unit": "iter/sec",
            "range": "stddev: 0.0019977379790957653",
            "extra": "mean: 241.87450119999312 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_weaker_ratio_1e6",
            "value": 4.1565492171449305,
            "unit": "iter/sec",
            "range": "stddev: 0.0006852486092303095",
            "extra": "mean: 240.58418359999223 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_chi_square_1e6",
            "value": 88.30888941963588,
            "unit": "iter/sec",
            "range": "stddev: 0.0002382873760339818",
            "extra": "mean: 11.32388830356693 msec\nrounds: 56"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_rss_1e6",
            "value": 89.48671583125541,
            "unit": "iter/sec",
            "range": "stddev: 0.000541895425272154",
            "extra": "mean: 11.174843000001188 msec\nrounds: 56"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_mae_1e6",
            "value": 50.68058669515622,
            "unit": "iter/sec",
            "range": "stddev: 0.0005304002383730283",
            "extra": "mean: 19.731421145832446 msec\nrounds: 48"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_linregress_1e6",
            "value": 40.345057602821264,
            "unit": "iter/sec",
            "range": "stddev: 0.00039366066454477576",
            "extra": "mean: 24.786183473687036 msec\nrounds: 38"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_filter_wind_scales_1e6",
            "value": 8.189703960280301,
            "unit": "iter/sec",
            "range": "stddev: 0.0005705520047824653",
            "extra": "mean: 122.10453575000457 msec\nrounds: 8"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_get_least_angle_deflection_1e7",
            "value": 4.745920934111552,
            "unit": "iter/sec",
            "range": "stddev: 0.0006095208365380552",
            "extra": "mean: 210.7072607999953 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_get_least_dir_deflection_1e7",
            "value": 2.3567622855529198,
            "unit": "iter/sec",
            "range": "stddev: 0.0031401079091195176",
            "extra": "mean: 424.31093120000014 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_identify_direction8_1e7",
            "value": 0.17015031942901374,
            "unit": "iter/sec",
            "range": "stddev: 0.006179098126840696",
            "extra": "mean: 5.877156172000002 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_identify_direction16_1e7",
            "value": 0.08778724707185102,
            "unit": "iter/sec",
            "range": "stddev: 0.0053715709736806725",
            "extra": "mean: 11.391176205600027 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_identify_wind_scale_1e7",
            "value": 1.6095481263714941,
            "unit": "iter/sec",
            "range": "stddev: 0.0017024901883499492",
            "extra": "mean: 621.2923885999999 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_dir_score_1e7",
            "value": 0.08332257192876244,
            "unit": "iter/sec",
            "range": "stddev: 0.007807192615610311",
            "extra": "mean: 12.001549842399982 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_get_least_lev_deflection_1e7",
            "value": 13.595598844395527,
            "unit": "iter/sec",
            "range": "stddev: 0.0005153281756770148",
            "extra": "mean: 73.5532146428568 msec\nrounds: 14"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_dir_accuracy_ratio_1e7",
            "value": 3.1406262901395396,
            "unit": "iter/sec",
            "range": "stddev: 0.0007016363713579167",
            "extra": "mean: 318.4078294000301 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_scale_accuracy_ratio_1e7",
            "value": 0.34767321795699485,
            "unit": "iter/sec",
            "range": "stddev: 0.013681907639417729",
            "extra": "mean: 2.8762641133999978 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_speed_accuracy_ratio_1e7",
            "value": 0.6149412122694867,
            "unit": "iter/sec",
            "range": "stddev: 0.00582479482813967",
            "extra": "mean: 1.6261717055999951 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_speed_score_1e7",
            "value": 0.4187076080178415,
            "unit": "iter/sec",
            "range": "stddev: 0.013200407064101987",
            "extra": "mean: 2.3883014801999707 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_scale_stronger_ratio_1e7",
            "value": 0.3670236326699837,
            "unit": "iter/sec",
            "range": "stddev: 0.004077839024716686",
            "extra": "mean: 2.7246201906000125 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_scale_weaker_ratio_1e7",
            "value": 0.36541639854683194,
            "unit": "iter/sec",
            "range": "stddev: 0.0024074191447226844",
            "extra": "mean: 2.736604060399986 sec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_speed_chi_square_1e7",
            "value": 4.944464403764251,
            "unit": "iter/sec",
            "range": "stddev: 0.00112953245541821",
            "extra": "mean: 202.24637459998576 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_speed_rss_1e7",
            "value": 4.945874853165998,
            "unit": "iter/sec",
            "range": "stddev: 0.0010744737951636127",
            "extra": "mean: 202.18869859997994 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_speed_mae_1e7",
            "value": 4.423873933990167,
            "unit": "iter/sec",
            "range": "stddev: 0.0005585833500260433",
            "extra": "mean: 226.0462243999882 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_calc_wind_speed_linregress_1e7",
            "value": 3.305051048637899,
            "unit": "iter/sec",
            "range": "stddev: 0.0002971940528183305",
            "extra": "mean: 302.56718740006363 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e7.py::test_filter_wind_scales_1e7",
            "value": 0.6596266193389553,
            "unit": "iter/sec",
            "range": "stddev: 0.009114864125099159",
            "extra": "mean: 1.5160091643999294 sec\nrounds: 5"
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
          "id": "d334125ffe78b263c6a66c900694127e8f968ffb",
          "message": "tests: enlarge perf test",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/44/commits/d334125ffe78b263c6a66c900694127e8f968ffb"
        },
        "date": 1686651485999,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mae_1e3",
            "value": 24939.762089843545,
            "unit": "iter/sec",
            "range": "stddev: 0.000013493006234622828",
            "extra": "mean: 40.0966134479382 usec\nrounds: 3019"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mbe_1e3",
            "value": 26155.74285430341,
            "unit": "iter/sec",
            "range": "stddev: 0.000013282597039444614",
            "extra": "mean: 38.232521460787716 usec\nrounds: 6873"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_hit_ratio_1e3",
            "value": 1572.632222437564,
            "unit": "iter/sec",
            "range": "stddev: 0.00007440460728317019",
            "extra": "mean: 635.8765805078127 usec\nrounds: 944"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 1571.8921603648764,
            "unit": "iter/sec",
            "range": "stddev: 0.00032925187941476185",
            "extra": "mean: 636.1759573683951 usec\nrounds: 1079"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_ts_1e3",
            "value": 1622.8168988934449,
            "unit": "iter/sec",
            "range": "stddev: 0.00010471033777608163",
            "extra": "mean: 616.2124640690351 usec\nrounds: 1155"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_hit_ratio_1e3",
            "value": 3056.643759136437,
            "unit": "iter/sec",
            "range": "stddev: 0.00010044406583894919",
            "extra": "mean: 327.15621407007535 usec\nrounds: 2317"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_miss_ratio_1e3",
            "value": 3140.471292670365,
            "unit": "iter/sec",
            "range": "stddev: 0.00014462396895347188",
            "extra": "mean: 318.4235443686202 usec\nrounds: 2930"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_binary_accuracy_ratio_1e3",
            "value": 3290.425628236818,
            "unit": "iter/sec",
            "range": "stddev: 0.000057761836507594196",
            "extra": "mean: 303.9120505926318 usec\nrounds: 3123"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_ratio_1e3",
            "value": 3251.175519895094,
            "unit": "iter/sec",
            "range": "stddev: 0.00005814596167505215",
            "extra": "mean: 307.5810561074436 usec\nrounds: 2317"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_rate_1e3",
            "value": 3345.450764997672,
            "unit": "iter/sec",
            "range": "stddev: 0.000052562335753175285",
            "extra": "mean: 298.9133812587124 usec\nrounds: 2177"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ts_1e3",
            "value": 3252.0298211945246,
            "unit": "iter/sec",
            "range": "stddev: 0.00018476733714709498",
            "extra": "mean: 307.50025521988704 usec\nrounds: 3209"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ets_1e3",
            "value": 3293.650224364658,
            "unit": "iter/sec",
            "range": "stddev: 0.00006529430334034141",
            "extra": "mean: 303.6145103091203 usec\nrounds: 2716"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_bias_score_1e3",
            "value": 3431.31300723348,
            "unit": "iter/sec",
            "range": "stddev: 0.00009303386078693506",
            "extra": "mean: 291.43362843667154 usec\nrounds: 2328"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_diff_accuracy_ratio_1e3",
            "value": 3952.936182526365,
            "unit": "iter/sec",
            "range": "stddev: 0.000036619083193466665",
            "extra": "mean: 252.9765100738077 usec\nrounds: 2035"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rmse_1e3",
            "value": 23469.296287696667,
            "unit": "iter/sec",
            "range": "stddev: 0.00001584326769188878",
            "extra": "mean: 42.60886171198201 usec\nrounds: 5409"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rss_1e3",
            "value": 23973.832547511385,
            "unit": "iter/sec",
            "range": "stddev: 0.00002721499145394408",
            "extra": "mean: 41.712145858122526 usec\nrounds: 5855"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_chi_square_1e3",
            "value": 24313.495010116876,
            "unit": "iter/sec",
            "range": "stddev: 0.00002185760391074469",
            "extra": "mean: 41.12942214123879 usec\nrounds: 7154"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_linregress_1e3",
            "value": 3069.4275222005563,
            "unit": "iter/sec",
            "range": "stddev: 0.00005084905871700913",
            "extra": "mean: 325.79365134612226 usec\nrounds: 1523"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_accuracy_ratio_1e3",
            "value": 1636.8466152377339,
            "unit": "iter/sec",
            "range": "stddev: 0.00005689036470834496",
            "extra": "mean: 610.9307925927814 usec\nrounds: 1215"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_miss_ratio_1e3",
            "value": 1631.064101911527,
            "unit": "iter/sec",
            "range": "stddev: 0.00011801239946878668",
            "extra": "mean: 613.0966887371558 usec\nrounds: 1314"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_bias_score_1e3",
            "value": 1580.3387668508067,
            "unit": "iter/sec",
            "range": "stddev: 0.0002761956203739618",
            "extra": "mean: 632.7757193432222 usec\nrounds: 1158"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_mae_1e3",
            "value": 5456.594752631717,
            "unit": "iter/sec",
            "range": "stddev: 0.00003519421797487728",
            "extra": "mean: 183.26448001616757 usec\nrounds: 2502"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mae_1e6",
            "value": 45.235872577846955,
            "unit": "iter/sec",
            "range": "stddev: 0.001901479927476154",
            "extra": "mean: 22.106349297873894 msec\nrounds: 47"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mbe_1e6",
            "value": 63.459656760685085,
            "unit": "iter/sec",
            "range": "stddev: 0.0017010053774500291",
            "extra": "mean: 15.758042999998167 msec\nrounds: 56"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.262393221290789,
            "unit": "iter/sec",
            "range": "stddev: 0.011743301538015317",
            "extra": "mean: 306.5234422000003 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.32447286403618,
            "unit": "iter/sec",
            "range": "stddev: 0.005967877784978823",
            "extra": "mean: 300.79956759999504 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_ts_1e6",
            "value": 3.357651852125239,
            "unit": "iter/sec",
            "range": "stddev: 0.005625402314286218",
            "extra": "mean: 297.8271851999921 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_hit_ratio_1e6",
            "value": 4.2531477197515475,
            "unit": "iter/sec",
            "range": "stddev: 0.006203404909064664",
            "extra": "mean: 235.11997840000163 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_miss_ratio_1e6",
            "value": 4.184900109045776,
            "unit": "iter/sec",
            "range": "stddev: 0.011097232493224243",
            "extra": "mean: 238.95432959999994 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_binary_accuracy_ratio_1e6",
            "value": 4.02388421867426,
            "unit": "iter/sec",
            "range": "stddev: 0.003645180166907961",
            "extra": "mean: 248.51609679998887 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_ratio_1e6",
            "value": 4.079222601728366,
            "unit": "iter/sec",
            "range": "stddev: 0.004914029962203274",
            "extra": "mean: 245.1447488000042 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_rate_1e6",
            "value": 4.11126059517604,
            "unit": "iter/sec",
            "range": "stddev: 0.009770123950179569",
            "extra": "mean: 243.23439899999357 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ts_1e6",
            "value": 4.102414298382769,
            "unit": "iter/sec",
            "range": "stddev: 0.01068483674077234",
            "extra": "mean: 243.75890080000318 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ets_1e6",
            "value": 4.3872109571612095,
            "unit": "iter/sec",
            "range": "stddev: 0.008897198974047813",
            "extra": "mean: 227.93524399999683 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_bias_score_1e6",
            "value": 4.235741490484141,
            "unit": "iter/sec",
            "range": "stddev: 0.005517402033982387",
            "extra": "mean: 236.08617339999682 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_diff_accuracy_ratio_1e6",
            "value": 5.461460338569276,
            "unit": "iter/sec",
            "range": "stddev: 0.0034198715715002036",
            "extra": "mean: 183.1012106666634 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rmse_1e6",
            "value": 60.49497245728574,
            "unit": "iter/sec",
            "range": "stddev: 0.0014987240265239479",
            "extra": "mean: 16.530299285714683 msec\nrounds: 56"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rss_1e6",
            "value": 60.99781921084932,
            "unit": "iter/sec",
            "range": "stddev: 0.0015206324316092662",
            "extra": "mean: 16.394028719999483 msec\nrounds: 50"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_chi_square_1e6",
            "value": 58.373482945327616,
            "unit": "iter/sec",
            "range": "stddev: 0.001710307843744548",
            "extra": "mean: 17.131066188676733 msec\nrounds: 53"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_linregress_1e6",
            "value": 32.200158747176545,
            "unit": "iter/sec",
            "range": "stddev: 0.0017509992829252052",
            "extra": "mean: 31.055747515148024 msec\nrounds: 33"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_accuracy_ratio_1e6",
            "value": 3.48351282918146,
            "unit": "iter/sec",
            "range": "stddev: 0.004222976049614251",
            "extra": "mean: 287.0665471999928 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_miss_ratio_1e6",
            "value": 3.467490763651747,
            "unit": "iter/sec",
            "range": "stddev: 0.004306787526616718",
            "extra": "mean: 288.3929816000034 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_bias_score_1e6",
            "value": 3.3928086906410115,
            "unit": "iter/sec",
            "range": "stddev: 0.008372005990444732",
            "extra": "mean: 294.74105119999194 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_mae_1e6",
            "value": 18.04160372358495,
            "unit": "iter/sec",
            "range": "stddev: 0.0036197259573683385",
            "extra": "mean: 55.427445105267815 msec\nrounds: 19"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_angle_deflection_1e3",
            "value": 35260.20243936109,
            "unit": "iter/sec",
            "range": "stddev: 0.000009797641192301265",
            "extra": "mean: 28.360585896231164 usec\nrounds: 16421"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_dir_deflection_1e3",
            "value": 23534.889508344128,
            "unit": "iter/sec",
            "range": "stddev: 0.000016866126709345057",
            "extra": "mean: 42.49010812842173 usec\nrounds: 9091"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_direction8_1e3",
            "value": 815.8771565766491,
            "unit": "iter/sec",
            "range": "stddev: 0.00008783971768069239",
            "extra": "mean: 1.225674713330515 msec\nrounds: 600"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_direction16_1e3",
            "value": 422.49407131393616,
            "unit": "iter/sec",
            "range": "stddev: 0.00024050895525181603",
            "extra": "mean: 2.3668971185561216 msec\nrounds: 388"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_wind_scale_1e3",
            "value": 6655.848290594942,
            "unit": "iter/sec",
            "range": "stddev: 0.00003558146596921326",
            "extra": "mean: 150.24380910440095 usec\nrounds: 3515"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_dir_score_1e3",
            "value": 367.44381400768884,
            "unit": "iter/sec",
            "range": "stddev: 0.00033440107029366587",
            "extra": "mean: 2.721504518182132 msec\nrounds: 330"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_lev_deflection_1e3",
            "value": 201302.95313701843,
            "unit": "iter/sec",
            "range": "stddev: 0.000004847884403464895",
            "extra": "mean: 4.9676370088785635 usec\nrounds: 42552"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_dir_accuracy_ratio_1e3",
            "value": 8599.71409422395,
            "unit": "iter/sec",
            "range": "stddev: 0.00002202077540230181",
            "extra": "mean: 116.28293557708577 usec\nrounds: 3089"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_accuracy_ratio_1e3",
            "value": 1076.193982689798,
            "unit": "iter/sec",
            "range": "stddev: 0.00008345343309774124",
            "extra": "mean: 929.2005122539696 usec\nrounds: 816"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_accuracy_ratio_1e3",
            "value": 2613.204744201128,
            "unit": "iter/sec",
            "range": "stddev: 0.00012375566557331033",
            "extra": "mean: 382.67189060446384 usec\nrounds: 2267"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_score_1e3",
            "value": 1153.4326371574923,
            "unit": "iter/sec",
            "range": "stddev: 0.00011814755859145936",
            "extra": "mean: 866.9773749981532 usec\nrounds: 768"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_stronger_ratio_1e3",
            "value": 1554.9524572916464,
            "unit": "iter/sec",
            "range": "stddev: 0.00007516829180620765",
            "extra": "mean: 643.1064791149691 usec\nrounds: 1221"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_weaker_ratio_1e3",
            "value": 1524.5207907058316,
            "unit": "iter/sec",
            "range": "stddev: 0.00015332446383025544",
            "extra": "mean: 655.9438258214991 usec\nrounds: 1309"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_chi_square_1e3",
            "value": 7433.101608538442,
            "unit": "iter/sec",
            "range": "stddev: 0.00002289738720303622",
            "extra": "mean: 134.53334188937964 usec\nrounds: 4013"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_rss_1e3",
            "value": 7462.725249769198,
            "unit": "iter/sec",
            "range": "stddev: 0.000034935718085842406",
            "extra": "mean: 133.99930541874463 usec\nrounds: 3248"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_mae_1e3",
            "value": 7452.794599289151,
            "unit": "iter/sec",
            "range": "stddev: 0.0000299673942152651",
            "extra": "mean: 134.17785592741015 usec\nrounds: 3408"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_linregress_1e3",
            "value": 3067.9331288550256,
            "unit": "iter/sec",
            "range": "stddev: 0.00005753742223832167",
            "extra": "mean: 325.9523457648528 usec\nrounds: 1582"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_filter_wind_scales_1e3",
            "value": 2001.24325744896,
            "unit": "iter/sec",
            "range": "stddev: 0.00011166589036395773",
            "extra": "mean: 499.68937872886454 usec\nrounds: 1307"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_angle_deflection_1e6",
            "value": 65.8519458549713,
            "unit": "iter/sec",
            "range": "stddev: 0.0009324980335241644",
            "extra": "mean: 15.185580122451428 msec\nrounds: 49"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_dir_deflection_1e6",
            "value": 31.53759831763973,
            "unit": "iter/sec",
            "range": "stddev: 0.0020276605050542685",
            "extra": "mean: 31.708184939392677 msec\nrounds: 33"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_direction8_1e6",
            "value": 1.9911695770888702,
            "unit": "iter/sec",
            "range": "stddev: 0.018934053020311467",
            "extra": "mean: 502.21739600000313 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_direction16_1e6",
            "value": 1.0541831723464223,
            "unit": "iter/sec",
            "range": "stddev: 0.039465085585630236",
            "extra": "mean: 948.6017479999987 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_wind_scale_1e6",
            "value": 24.538305801798217,
            "unit": "iter/sec",
            "range": "stddev: 0.0018029497954691724",
            "extra": "mean: 40.75260973912543 msec\nrounds: 23"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_dir_score_1e6",
            "value": 1.0117044846561456,
            "unit": "iter/sec",
            "range": "stddev: 0.01732616105418712",
            "extra": "mean: 988.4309253999959 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_lev_deflection_1e6",
            "value": 522.0803418751732,
            "unit": "iter/sec",
            "range": "stddev: 0.0005657886156545577",
            "extra": "mean: 1.9154140077526514 msec\nrounds: 129"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_dir_accuracy_ratio_1e6",
            "value": 46.693271550284614,
            "unit": "iter/sec",
            "range": "stddev: 0.0016881390258368333",
            "extra": "mean: 21.416361861110683 msec\nrounds: 36"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_accuracy_ratio_1e6",
            "value": 4.652702982540059,
            "unit": "iter/sec",
            "range": "stddev: 0.00721881343724083",
            "extra": "mean: 214.92882820000432 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_accuracy_ratio_1e6",
            "value": 5.238343519614064,
            "unit": "iter/sec",
            "range": "stddev: 0.006871404809643698",
            "extra": "mean: 190.9000423999828 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_score_1e6",
            "value": 4.851394014838132,
            "unit": "iter/sec",
            "range": "stddev: 0.00544373141884639",
            "extra": "mean: 206.12632099999928 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_stronger_ratio_1e6",
            "value": 3.877868672934272,
            "unit": "iter/sec",
            "range": "stddev: 0.006938986625474218",
            "extra": "mean: 257.87361159998454 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_weaker_ratio_1e6",
            "value": 3.8314811096674664,
            "unit": "iter/sec",
            "range": "stddev: 0.00629552185358046",
            "extra": "mean: 260.9956753999995 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_chi_square_1e6",
            "value": 73.88653204434704,
            "unit": "iter/sec",
            "range": "stddev: 0.0014100011819370556",
            "extra": "mean: 13.534266290909356 msec\nrounds: 55"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_rss_1e6",
            "value": 75.46979131433227,
            "unit": "iter/sec",
            "range": "stddev: 0.0011344402539634007",
            "extra": "mean: 13.250334770835556 msec\nrounds: 48"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_mae_1e6",
            "value": 43.67177960205029,
            "unit": "iter/sec",
            "range": "stddev: 0.0018322312978093964",
            "extra": "mean: 22.898082219508456 msec\nrounds: 41"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_linregress_1e6",
            "value": 33.97290976909746,
            "unit": "iter/sec",
            "range": "stddev: 0.00204588083527208",
            "extra": "mean: 29.435217848475933 msec\nrounds: 33"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_filter_wind_scales_1e6",
            "value": 7.956639070065126,
            "unit": "iter/sec",
            "range": "stddev: 0.006335313942963444",
            "extra": "mean: 125.68120675000216 msec\nrounds: 8"
          }
        ]
      }
    ]
  }
}