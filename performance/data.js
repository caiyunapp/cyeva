window.BENCHMARK_DATA = {
  "lastUpdate": 1709001084658,
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
          "id": "d334125ffe78b263c6a66c900694127e8f968ffb",
          "message": "tests: enlarge perf test",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/44/commits/d334125ffe78b263c6a66c900694127e8f968ffb"
        },
        "date": 1686652274963,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mae_1e3",
            "value": 43500.455296124,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035523380675114863",
            "extra": "mean: 22.988265138666318 usec\nrounds: 4145"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_mbe_1e3",
            "value": 46442.36756590454,
            "unit": "iter/sec",
            "range": "stddev: 0.000002855093262417859",
            "extra": "mean: 21.532063338091866 usec\nrounds: 10515"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2488.450716165196,
            "unit": "iter/sec",
            "range": "stddev: 0.000015625792518277976",
            "extra": "mean: 401.8564617349709 usec\nrounds: 1568"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2482.0079602132746,
            "unit": "iter/sec",
            "range": "stddev: 0.000016578412465464205",
            "extra": "mean: 402.8995942116445 usec\nrounds: 1693"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_ts_1e3",
            "value": 2478.7038682677357,
            "unit": "iter/sec",
            "range": "stddev: 0.000013839488485704964",
            "extra": "mean: 403.4366560693105 usec\nrounds: 1730"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_hit_ratio_1e3",
            "value": 3933.774252562953,
            "unit": "iter/sec",
            "range": "stddev: 0.000006280987400220282",
            "extra": "mean: 254.20879181068278 usec\nrounds: 3468"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_miss_ratio_1e3",
            "value": 4005.436953165937,
            "unit": "iter/sec",
            "range": "stddev: 0.000005836880341471407",
            "extra": "mean: 249.66065168235642 usec\nrounds: 3448"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_binary_accuracy_ratio_1e3",
            "value": 3955.3954343864816,
            "unit": "iter/sec",
            "range": "stddev: 0.0000063670337141035475",
            "extra": "mean: 252.8192229040961 usec\nrounds: 3423"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_ratio_1e3",
            "value": 3929.3355431800037,
            "unit": "iter/sec",
            "range": "stddev: 0.00000636348050906698",
            "extra": "mean: 254.49595459865 usec\nrounds: 3436"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_false_alarm_rate_1e3",
            "value": 3872.2150311940304,
            "unit": "iter/sec",
            "range": "stddev: 0.000006666873763340594",
            "extra": "mean: 258.2501209111937 usec\nrounds: 3424"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ts_1e3",
            "value": 3997.252333155812,
            "unit": "iter/sec",
            "range": "stddev: 0.0000065242366543666995",
            "extra": "mean: 250.17184722249067 usec\nrounds: 3240"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_ets_1e3",
            "value": 3959.269607495581,
            "unit": "iter/sec",
            "range": "stddev: 0.0000062526083564932835",
            "extra": "mean: 252.57183751943222 usec\nrounds: 3225"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_bias_score_1e3",
            "value": 3986.8898850727437,
            "unit": "iter/sec",
            "range": "stddev: 0.000007752202327541573",
            "extra": "mean: 250.82207656250688 usec\nrounds: 3200"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_diff_accuracy_ratio_1e3",
            "value": 5804.26418275637,
            "unit": "iter/sec",
            "range": "stddev: 0.00000877346677383634",
            "extra": "mean: 172.28712693175743 usec\nrounds: 3624"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rmse_1e3",
            "value": 41388.15691063166,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032981900979119872",
            "extra": "mean: 24.16150113084942 usec\nrounds: 9728"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_rss_1e3",
            "value": 44497.15187681807,
            "unit": "iter/sec",
            "range": "stddev: 0.000002917916489474802",
            "extra": "mean: 22.47334846887078 usec\nrounds: 10417"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_chi_square_1e3",
            "value": 43918.693687273284,
            "unit": "iter/sec",
            "range": "stddev: 0.000003275702903809482",
            "extra": "mean: 22.769347538444183 usec\nrounds: 10278"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_linregress_1e3",
            "value": 5331.917761632215,
            "unit": "iter/sec",
            "range": "stddev: 0.000024138348758519915",
            "extra": "mean: 187.54977940505188 usec\nrounds: 2117"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_accuracy_ratio_1e3",
            "value": 2513.3875450167898,
            "unit": "iter/sec",
            "range": "stddev: 0.000013847180351658237",
            "extra": "mean: 397.8694021869675 usec\nrounds: 1646"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_miss_ratio_1e3",
            "value": 2515.858956886654,
            "unit": "iter/sec",
            "range": "stddev: 0.00001482371615375577",
            "extra": "mean: 397.4785618497025 usec\nrounds: 1730"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_bias_score_1e3",
            "value": 2503.1763146324065,
            "unit": "iter/sec",
            "range": "stddev: 0.00001448762354584396",
            "extra": "mean: 399.49243453386174 usec\nrounds: 1749"
          },
          {
            "name": "tests/performance/test_statistic_1e3.py::test_calc_threshold_mae_1e3",
            "value": 9727.553594385632,
            "unit": "iter/sec",
            "range": "stddev: 0.000010123335641513443",
            "extra": "mean: 102.80077002887565 usec\nrounds: 3470"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mae_1e6",
            "value": 57.88049213707377,
            "unit": "iter/sec",
            "range": "stddev: 0.00038264819967971094",
            "extra": "mean: 17.276978185185076 msec\nrounds: 54"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_mbe_1e6",
            "value": 75.13252758303246,
            "unit": "iter/sec",
            "range": "stddev: 0.00030413800298104555",
            "extra": "mean: 13.309814432834747 msec\nrounds: 67"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.695625813014195,
            "unit": "iter/sec",
            "range": "stddev: 0.00034388549194132745",
            "extra": "mean: 270.5901653999945 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.6807914774700965,
            "unit": "iter/sec",
            "range": "stddev: 0.0016610810390034118",
            "extra": "mean: 271.68069859999946 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_ts_1e6",
            "value": 3.665497092561375,
            "unit": "iter/sec",
            "range": "stddev: 0.002643789242738144",
            "extra": "mean: 272.814293600004 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_hit_ratio_1e6",
            "value": 4.676363579172462,
            "unit": "iter/sec",
            "range": "stddev: 0.00025244355769835476",
            "extra": "mean: 213.84137120000446 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_miss_ratio_1e6",
            "value": 4.648994188433829,
            "unit": "iter/sec",
            "range": "stddev: 0.00028811450463321885",
            "extra": "mean: 215.1002903999938 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_binary_accuracy_ratio_1e6",
            "value": 4.651721672339005,
            "unit": "iter/sec",
            "range": "stddev: 0.0004032110617962698",
            "extra": "mean: 214.9741687999949 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_ratio_1e6",
            "value": 4.664657279713574,
            "unit": "iter/sec",
            "range": "stddev: 0.00023683176850573126",
            "extra": "mean: 214.37802180000745 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_false_alarm_rate_1e6",
            "value": 4.6644019819614195,
            "unit": "iter/sec",
            "range": "stddev: 0.0003664300364776997",
            "extra": "mean: 214.38975540000342 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ts_1e6",
            "value": 4.652559519361141,
            "unit": "iter/sec",
            "range": "stddev: 0.0005056489004308791",
            "extra": "mean: 214.93545559999916 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_ets_1e6",
            "value": 4.674784577184912,
            "unit": "iter/sec",
            "range": "stddev: 0.00023212472236312665",
            "extra": "mean: 213.91360039999654 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_bias_score_1e6",
            "value": 4.597614769227537,
            "unit": "iter/sec",
            "range": "stddev: 0.007594998425898947",
            "extra": "mean: 217.50408640000387 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_diff_accuracy_ratio_1e6",
            "value": 6.094406493820556,
            "unit": "iter/sec",
            "range": "stddev: 0.00034240221925740656",
            "extra": "mean: 164.0848868571457 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rmse_1e6",
            "value": 73.1465167257956,
            "unit": "iter/sec",
            "range": "stddev: 0.00027854689980279056",
            "extra": "mean: 13.671190984373194 msec\nrounds: 64"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_rss_1e6",
            "value": 72.97316119014958,
            "unit": "iter/sec",
            "range": "stddev: 0.0002929252554992224",
            "extra": "mean: 13.703668358209853 msec\nrounds: 67"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_chi_square_1e6",
            "value": 72.39920159025033,
            "unit": "iter/sec",
            "range": "stddev: 0.00030252261023030065",
            "extra": "mean: 13.812307014925223 msec\nrounds: 67"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_linregress_1e6",
            "value": 37.96883570711388,
            "unit": "iter/sec",
            "range": "stddev: 0.00093148668167758",
            "extra": "mean: 26.337389108105807 msec\nrounds: 37"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_accuracy_ratio_1e6",
            "value": 3.785623190262546,
            "unit": "iter/sec",
            "range": "stddev: 0.0014895534342103428",
            "extra": "mean: 264.1572997999958 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_miss_ratio_1e6",
            "value": 3.8028521668099478,
            "unit": "iter/sec",
            "range": "stddev: 0.00046772505144580665",
            "extra": "mean: 262.9605243999947 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_bias_score_1e6",
            "value": 3.8130400076351147,
            "unit": "iter/sec",
            "range": "stddev: 0.000250806101327382",
            "extra": "mean: 262.2579354000038 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_statistic_1e6.py::test_calc_threshold_mae_1e6",
            "value": 20.344852417617048,
            "unit": "iter/sec",
            "range": "stddev: 0.00028686956912229365",
            "extra": "mean: 49.15248238095246 msec\nrounds: 21"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_angle_deflection_1e3",
            "value": 50742.904709707625,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021049364857789824",
            "extra": "mean: 19.70718873349578 usec\nrounds: 21231"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_dir_deflection_1e3",
            "value": 34597.00467412818,
            "unit": "iter/sec",
            "range": "stddev: 0.0000033146366833757825",
            "extra": "mean: 28.904236347021257 usec\nrounds: 9833"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_direction8_1e3",
            "value": 1197.8912861910965,
            "unit": "iter/sec",
            "range": "stddev: 0.000017584446407239102",
            "extra": "mean: 834.800295759454 usec\nrounds: 967"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_direction16_1e3",
            "value": 626.3419888012327,
            "unit": "iter/sec",
            "range": "stddev: 0.00002702633576949051",
            "extra": "mean: 1.596571869489252 msec\nrounds: 567"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_identify_wind_scale_1e3",
            "value": 8123.927373102801,
            "unit": "iter/sec",
            "range": "stddev: 0.000003710854059747941",
            "extra": "mean: 123.09317329828201 usec\nrounds: 4951"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_dir_score_1e3",
            "value": 543.0559419764163,
            "unit": "iter/sec",
            "range": "stddev: 0.000028798326007778493",
            "extra": "mean: 1.8414309147609471 msec\nrounds: 481"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_get_least_lev_deflection_1e3",
            "value": 258655.54182625943,
            "unit": "iter/sec",
            "range": "stddev: 0.0000011800155246622645",
            "extra": "mean: 3.866145658196283 usec\nrounds: 63292"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_dir_accuracy_ratio_1e3",
            "value": 14812.833887436418,
            "unit": "iter/sec",
            "range": "stddev: 0.000006191251803781611",
            "extra": "mean: 67.50902680736569 usec\nrounds: 4924"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_accuracy_ratio_1e3",
            "value": 1568.967387123868,
            "unit": "iter/sec",
            "range": "stddev: 0.000016483915361212478",
            "extra": "mean: 637.3618777590635 usec\nrounds: 1178"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_accuracy_ratio_1e3",
            "value": 4257.383993822171,
            "unit": "iter/sec",
            "range": "stddev: 0.000008480920527778757",
            "extra": "mean: 234.88602424659976 usec\nrounds: 2722"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_score_1e3",
            "value": 1756.8362271339954,
            "unit": "iter/sec",
            "range": "stddev: 0.000018654597821833173",
            "extra": "mean: 569.2050201124007 usec\nrounds: 1243"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_stronger_ratio_1e3",
            "value": 2212.0173719829645,
            "unit": "iter/sec",
            "range": "stddev: 0.00000908724490808677",
            "extra": "mean: 452.0760156162559 usec\nrounds: 1793"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_scale_weaker_ratio_1e3",
            "value": 2206.0291353892208,
            "unit": "iter/sec",
            "range": "stddev: 0.000012145873439297842",
            "extra": "mean: 453.30316991645935 usec\nrounds: 1795"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_chi_square_1e3",
            "value": 13011.450276630645,
            "unit": "iter/sec",
            "range": "stddev: 0.000007063835831593783",
            "extra": "mean: 76.85538343070493 usec\nrounds: 4285"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_rss_1e3",
            "value": 13146.072898445409,
            "unit": "iter/sec",
            "range": "stddev: 0.00000657966163256637",
            "extra": "mean: 76.06834434321866 usec\nrounds: 5056"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_mae_1e3",
            "value": 13109.333644546554,
            "unit": "iter/sec",
            "range": "stddev: 0.000009694495991822818",
            "extra": "mean: 76.28152788803246 usec\nrounds: 5289"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_calc_wind_speed_linregress_1e3",
            "value": 5158.778905911987,
            "unit": "iter/sec",
            "range": "stddev: 0.000017359982439595308",
            "extra": "mean: 193.84432212320533 usec\nrounds: 565"
          },
          {
            "name": "tests/performance/test_wind_1e3.py::test_filter_wind_scales_1e3",
            "value": 2997.9378600101054,
            "unit": "iter/sec",
            "range": "stddev: 0.000010657705667088697",
            "extra": "mean: 333.5626176042986 usec\nrounds: 2045"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_angle_deflection_1e6",
            "value": 72.97364176653895,
            "unit": "iter/sec",
            "range": "stddev: 0.00026378693126672645",
            "extra": "mean: 13.70357811111102 msec\nrounds: 54"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_dir_deflection_1e6",
            "value": 34.51333169838813,
            "unit": "iter/sec",
            "range": "stddev: 0.00044876942716514956",
            "extra": "mean: 28.974310818178786 msec\nrounds: 33"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_direction8_1e6",
            "value": 2.211151086025168,
            "unit": "iter/sec",
            "range": "stddev: 0.0013047156203428174",
            "extra": "mean: 452.25313019999476 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_direction16_1e6",
            "value": 1.1657337340005554,
            "unit": "iter/sec",
            "range": "stddev: 0.0025060261256891455",
            "extra": "mean: 857.8288256000008 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_identify_wind_scale_1e6",
            "value": 22.343653070441807,
            "unit": "iter/sec",
            "range": "stddev: 0.0001094282186733289",
            "extra": "mean: 44.75543890908733 msec\nrounds: 22"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_dir_score_1e6",
            "value": 1.0916117441611894,
            "unit": "iter/sec",
            "range": "stddev: 0.0018291405596013127",
            "extra": "mean: 916.0766228 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_get_least_lev_deflection_1e6",
            "value": 553.9837722243317,
            "unit": "iter/sec",
            "range": "stddev: 0.00005880221146995026",
            "extra": "mean: 1.805107026844565 msec\nrounds: 149"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_dir_accuracy_ratio_1e6",
            "value": 52.612584081536525,
            "unit": "iter/sec",
            "range": "stddev: 0.00019685828435432278",
            "extra": "mean: 19.006859622219785 msec\nrounds: 45"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_accuracy_ratio_1e6",
            "value": 4.570126848879439,
            "unit": "iter/sec",
            "range": "stddev: 0.00048389696288618196",
            "extra": "mean: 218.8123072000053 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_accuracy_ratio_1e6",
            "value": 6.3079778465584955,
            "unit": "iter/sec",
            "range": "stddev: 0.0008398314525427266",
            "extra": "mean: 158.52940899999825 msec\nrounds: 7"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_score_1e6",
            "value": 5.094742541316362,
            "unit": "iter/sec",
            "range": "stddev: 0.00043561859523251066",
            "extra": "mean: 196.28077216667825 msec\nrounds: 6"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_stronger_ratio_1e6",
            "value": 4.171786338485425,
            "unit": "iter/sec",
            "range": "stddev: 0.0010495978001106704",
            "extra": "mean: 239.70546879997983 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_scale_weaker_ratio_1e6",
            "value": 4.183510515420635,
            "unit": "iter/sec",
            "range": "stddev: 0.00034271553566554746",
            "extra": "mean: 239.03370059999816 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_chi_square_1e6",
            "value": 98.61612732190474,
            "unit": "iter/sec",
            "range": "stddev: 0.00041436021709061633",
            "extra": "mean: 10.140329245902954 msec\nrounds: 61"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_rss_1e6",
            "value": 97.37976312317575,
            "unit": "iter/sec",
            "range": "stddev: 0.00039295705985562267",
            "extra": "mean: 10.26907406557458 msec\nrounds: 61"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_mae_1e6",
            "value": 55.69635430110375,
            "unit": "iter/sec",
            "range": "stddev: 0.00036660136277297283",
            "extra": "mean: 17.954496529410772 msec\nrounds: 51"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_calc_wind_speed_linregress_1e6",
            "value": 42.66072374345059,
            "unit": "iter/sec",
            "range": "stddev: 0.00037411154136130355",
            "extra": "mean: 23.44076499999659 msec\nrounds: 40"
          },
          {
            "name": "tests/performance/test_wind_1e6.py::test_filter_wind_scales_1e6",
            "value": 8.36782801526525,
            "unit": "iter/sec",
            "range": "stddev: 0.0003909552725721067",
            "extra": "mean: 119.5053242222141 msec\nrounds: 9"
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
          "id": "6b4d1d9c63ad1987dfb560b1d1a46fa766214250",
          "message": "Update PyPI Publish",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/45/commits/6b4d1d9c63ad1987dfb560b1d1a46fa766214250"
        },
        "date": 1692342264282,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 43662.03305640882,
            "unit": "iter/sec",
            "range": "stddev: 0.0000031702529096194955",
            "extra": "mean: 22.903193690226427 usec\nrounds: 4089"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 56.34524888157866,
            "unit": "iter/sec",
            "range": "stddev: 0.0008451344382122595",
            "extra": "mean: 17.74772531578855 msec\nrounds: 57"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.566952214975388,
            "unit": "iter/sec",
            "range": "stddev: 0.0013437843596763198",
            "extra": "mean: 179.63150416666926 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 46786.68732541132,
            "unit": "iter/sec",
            "range": "stddev: 0.000002997754517071674",
            "extra": "mean: 21.373601277747838 usec\nrounds: 8921"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 69.81213410724574,
            "unit": "iter/sec",
            "range": "stddev: 0.000408597048974228",
            "extra": "mean: 14.324157437499263 msec\nrounds: 64"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.587459846244601,
            "unit": "iter/sec",
            "range": "stddev: 0.0013416515127715751",
            "extra": "mean: 151.80358185713771 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2484.0155594122634,
            "unit": "iter/sec",
            "range": "stddev: 0.000021579241208437336",
            "extra": "mean: 402.57396786862614 usec\nrounds: 1276"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.5635262356440234,
            "unit": "iter/sec",
            "range": "stddev: 0.0003021027518959244",
            "extra": "mean: 280.6209170000045 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.357159564046807,
            "unit": "iter/sec",
            "range": "stddev: 0.007606531594378026",
            "extra": "mean: 2.799869024000003 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2481.0196392651496,
            "unit": "iter/sec",
            "range": "stddev: 0.000016251554889537087",
            "extra": "mean: 403.060090365181 usec\nrounds: 1505"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.5491294342895925,
            "unit": "iter/sec",
            "range": "stddev: 0.0009242424760242424",
            "extra": "mean: 281.75923659999285 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3567363038627365,
            "unit": "iter/sec",
            "range": "stddev: 0.001513109451272841",
            "extra": "mean: 2.803191010200004 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2499.5823529782433,
            "unit": "iter/sec",
            "range": "stddev: 0.000014648883773083423",
            "extra": "mean: 400.06683468880453 usec\nrounds: 1476"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.5437621519946556,
            "unit": "iter/sec",
            "range": "stddev: 0.0013333554245279627",
            "extra": "mean: 282.18598119999 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.35681824689112496,
            "unit": "iter/sec",
            "range": "stddev: 0.0038384750292179528",
            "extra": "mean: 2.8025472596000043 sec\nrounds: 5"
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
          "id": "7363bf002bc957a62691f8e512d929c2b5245dca",
          "message": "Update PyPI Publish",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/45/commits/7363bf002bc957a62691f8e512d929c2b5245dca"
        },
        "date": 1692348750221,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 44542.61470545926,
            "unit": "iter/sec",
            "range": "stddev: 0.000003636418190642806",
            "extra": "mean: 22.450410839430077 usec\nrounds: 4133"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 52.89335117475112,
            "unit": "iter/sec",
            "range": "stddev: 0.0003217097983853889",
            "extra": "mean: 18.905967910714544 msec\nrounds: 56"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.594363108543029,
            "unit": "iter/sec",
            "range": "stddev: 0.0009992606344476898",
            "extra": "mean: 178.75135750000246 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 47325.739739139106,
            "unit": "iter/sec",
            "range": "stddev: 0.000004635627470924901",
            "extra": "mean: 21.130150432133338 usec\nrounds: 8562"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 66.48645881373702,
            "unit": "iter/sec",
            "range": "stddev: 0.00020625346656110463",
            "extra": "mean: 15.040656666668285 msec\nrounds: 63"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.6544001545600056,
            "unit": "iter/sec",
            "range": "stddev: 0.0002554735298298652",
            "extra": "mean: 150.2765052857151 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2480.4234217478597,
            "unit": "iter/sec",
            "range": "stddev: 0.000019873571012047864",
            "extra": "mean: 403.1569736167619 usec\nrounds: 1175"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.5363004555273077,
            "unit": "iter/sec",
            "range": "stddev: 0.0006573304492363478",
            "extra": "mean: 282.78140180000264 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3556543473929015,
            "unit": "iter/sec",
            "range": "stddev: 0.0050554444392732194",
            "extra": "mean: 2.8117187581999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2482.9623998008574,
            "unit": "iter/sec",
            "range": "stddev: 0.00002619023488150316",
            "extra": "mean: 402.74472141833627 usec\nrounds: 1382"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.533566105210202,
            "unit": "iter/sec",
            "range": "stddev: 0.000426315300788855",
            "extra": "mean: 283.0002241999978 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.35549185720373216,
            "unit": "iter/sec",
            "range": "stddev: 0.0067636085761396125",
            "extra": "mean: 2.813003954199999 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2479.0491706878465,
            "unit": "iter/sec",
            "range": "stddev: 0.00002178186329990935",
            "extra": "mean: 403.3804620835884 usec\nrounds: 1411"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.526676069800728,
            "unit": "iter/sec",
            "range": "stddev: 0.0004798664944985324",
            "extra": "mean: 283.5531192000019 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.35463639463638796,
            "unit": "iter/sec",
            "range": "stddev: 0.002752826825412034",
            "extra": "mean: 2.819789551000002 sec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ringsaturn.me@gmail.com",
            "name": "ringsaturn",
            "username": "ringsaturn"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "e44c475f989eefc151859bdcc7e1396d9b7b29cb",
          "message": "Update PyPI Publish (#45)",
          "timestamp": "2023-08-18T16:52:50+08:00",
          "tree_id": "634c0e5c58c11c6ee31a8cf28253fb14a6b2e950",
          "url": "https://github.com/caiyunapp/cyeva/commit/e44c475f989eefc151859bdcc7e1396d9b7b29cb"
        },
        "date": 1692348896869,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 42444.03174544894,
            "unit": "iter/sec",
            "range": "stddev: 0.000005535284021315926",
            "extra": "mean: 23.56043850870093 usec\nrounds: 4586"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 52.35620141057029,
            "unit": "iter/sec",
            "range": "stddev: 0.0013497142320882652",
            "extra": "mean: 19.09993416363679 msec\nrounds: 55"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.180923348044917,
            "unit": "iter/sec",
            "range": "stddev: 0.0015041764972420948",
            "extra": "mean: 193.01578749999493 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 43918.03127234752,
            "unit": "iter/sec",
            "range": "stddev: 0.0000049977223068525554",
            "extra": "mean: 22.769690968129492 usec\nrounds: 8614"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 68.08216872821379,
            "unit": "iter/sec",
            "range": "stddev: 0.000741229507749282",
            "extra": "mean: 14.688133746033154 msec\nrounds: 63"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.209369737573003,
            "unit": "iter/sec",
            "range": "stddev: 0.0024474294955189853",
            "extra": "mean: 161.04694071428582 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2396.3426111190875,
            "unit": "iter/sec",
            "range": "stddev: 0.000060936543712258546",
            "extra": "mean: 417.3025991191643 usec\nrounds: 1135"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.219801693868996,
            "unit": "iter/sec",
            "range": "stddev: 0.008331736552760101",
            "extra": "mean: 310.5781334000028 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.33326576545458697,
            "unit": "iter/sec",
            "range": "stddev: 0.02085284956141823",
            "extra": "mean: 3.0006082342000013 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2237.585504093508,
            "unit": "iter/sec",
            "range": "stddev: 0.00005293754789421911",
            "extra": "mean: 446.91029601799306 usec\nrounds: 1331"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.375865124346961,
            "unit": "iter/sec",
            "range": "stddev: 0.0038284491352687964",
            "extra": "mean: 296.22036519999995 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3227444228181161,
            "unit": "iter/sec",
            "range": "stddev: 0.021138682451165867",
            "extra": "mean: 3.0984268953999985 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2159.4741490934225,
            "unit": "iter/sec",
            "range": "stddev: 0.00003544170231531535",
            "extra": "mean: 463.07569850734916 usec\nrounds: 1340"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.289213377595016,
            "unit": "iter/sec",
            "range": "stddev: 0.005814362426671839",
            "extra": "mean: 304.02405839999744 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.32640462926660946,
            "unit": "iter/sec",
            "range": "stddev: 0.08876189762502545",
            "extra": "mean: 3.06368203859999 sec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "blizhan@mail.nankai.edu.cn",
            "name": "blizhan",
            "username": "blizhan"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8cc46ae0ab40bcf3a064a4bf6109bf5d0b4023e2",
          "message": "feat: Add multiclass verification support (#46)\n\nLGTM",
          "timestamp": "2023-10-15T21:53:53-05:00",
          "tree_id": "efeb4dab341ab81f99de87019e116adc995349af",
          "url": "https://github.com/caiyunapp/cyeva/commit/8cc46ae0ab40bcf3a064a4bf6109bf5d0b4023e2"
        },
        "date": 1697424954489,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 43143.045140296956,
            "unit": "iter/sec",
            "range": "stddev: 0.0000043096481837178665",
            "extra": "mean: 23.178706944493555 usec\nrounds: 3600"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 51.62807632884352,
            "unit": "iter/sec",
            "range": "stddev: 0.00040167791913040197",
            "extra": "mean: 19.36930583333241 msec\nrounds: 54"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.703313207776463,
            "unit": "iter/sec",
            "range": "stddev: 0.0008058177500799374",
            "extra": "mean: 175.33667949999673 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 46190.99426655862,
            "unit": "iter/sec",
            "range": "stddev: 0.000004092872976777765",
            "extra": "mean: 21.64924171645252 usec\nrounds: 8390"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 63.29751792013911,
            "unit": "iter/sec",
            "range": "stddev: 0.00027308249446888295",
            "extra": "mean: 15.798407786884708 msec\nrounds: 61"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.77813416755359,
            "unit": "iter/sec",
            "range": "stddev: 0.00042201095151891217",
            "extra": "mean: 147.53322599999916 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2398.8039866324625,
            "unit": "iter/sec",
            "range": "stddev: 0.000021627648115375046",
            "extra": "mean: 416.8744114035929 usec\nrounds: 1140"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.4338864521795474,
            "unit": "iter/sec",
            "range": "stddev: 0.00031828674457886626",
            "extra": "mean: 291.2152203999881 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3445987381848672,
            "unit": "iter/sec",
            "range": "stddev: 0.0017141532370631672",
            "extra": "mean: 2.901925890000007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2420.6075229039443,
            "unit": "iter/sec",
            "range": "stddev: 0.000019997073207201774",
            "extra": "mean: 413.11942995216515 usec\nrounds: 1449"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.4245750911197157,
            "unit": "iter/sec",
            "range": "stddev: 0.00044484353795740524",
            "extra": "mean: 292.0070295999949 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3459093738072046,
            "unit": "iter/sec",
            "range": "stddev: 0.001573678439699578",
            "extra": "mean: 2.890930618599998 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2414.945606876926,
            "unit": "iter/sec",
            "range": "stddev: 0.000023019741651708754",
            "extra": "mean: 414.0880014656842 usec\nrounds: 1364"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.416573360048124,
            "unit": "iter/sec",
            "range": "stddev: 0.0005744564094797872",
            "extra": "mean: 292.6909200000068 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.34466329533998014,
            "unit": "iter/sec",
            "range": "stddev: 0.0039101522876201856",
            "extra": "mean: 2.9013823447999814 sec\nrounds: 5"
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
          "id": "3808eb9971c347c91a43481f22862d9be90777d7",
          "message": "refactor: use pyproject.toml for environment build",
          "timestamp": "2023-04-14T21:45:30Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/47/commits/3808eb9971c347c91a43481f22862d9be90777d7"
        },
        "date": 1697437982378,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 38913.0508321962,
            "unit": "iter/sec",
            "range": "stddev: 0.000004792388457420505",
            "extra": "mean: 25.698319165780028 usec\nrounds: 6235"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 56.057965169263376,
            "unit": "iter/sec",
            "range": "stddev: 0.00026873815401252824",
            "extra": "mean: 17.838678178570433 msec\nrounds: 56"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.685640218851701,
            "unit": "iter/sec",
            "range": "stddev: 0.0020995093111626667",
            "extra": "mean: 175.8816881666784 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 41362.804460395746,
            "unit": "iter/sec",
            "range": "stddev: 0.000005351304248417907",
            "extra": "mean: 24.17631040848511 usec\nrounds: 4333"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 68.8334047945943,
            "unit": "iter/sec",
            "range": "stddev: 0.00039570119997771655",
            "extra": "mean: 14.527829953844345 msec\nrounds: 65"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.756332509943726,
            "unit": "iter/sec",
            "range": "stddev: 0.000258205818430335",
            "extra": "mean: 148.00929328570436 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2154.2814142280326,
            "unit": "iter/sec",
            "range": "stddev: 0.0000230868042907998",
            "extra": "mean: 464.1919079816882 usec\nrounds: 1065"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.1281929093552634,
            "unit": "iter/sec",
            "range": "stddev: 0.00043443265015908564",
            "extra": "mean: 319.6733798000025 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.31068064119424904,
            "unit": "iter/sec",
            "range": "stddev: 0.00201254256612633",
            "extra": "mean: 3.218739333600007 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2154.984469245023,
            "unit": "iter/sec",
            "range": "stddev: 0.000024194581454850318",
            "extra": "mean: 464.0404672384205 usec\nrounds: 1282"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.128552933317306,
            "unit": "iter/sec",
            "range": "stddev: 0.00036931253177372277",
            "extra": "mean: 319.6365928000034 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.31067844472535544,
            "unit": "iter/sec",
            "range": "stddev: 0.0022608614214897163",
            "extra": "mean: 3.2187620898000033 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2152.0313945267276,
            "unit": "iter/sec",
            "range": "stddev: 0.000023595449312918072",
            "extra": "mean: 464.6772359098966 usec\nrounds: 1242"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.1277503501283035,
            "unit": "iter/sec",
            "range": "stddev: 0.0007059964036642188",
            "extra": "mean: 319.71861180000474 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.3103045055572992,
            "unit": "iter/sec",
            "range": "stddev: 0.006496741065955587",
            "extra": "mean: 3.2226409288000015 sec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "mountain@users.noreply.github.com",
            "name": "Mingli Yuan",
            "username": "mountain"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ecce3786923008a8723797298e8f5cc986f6e099",
          "message": "Create README.en.md - English version (#49)",
          "timestamp": "2023-10-26T21:29:33-05:00",
          "tree_id": "f3dac188deb61dcc93d7d49e737a0ad7f80b6b33",
          "url": "https://github.com/caiyunapp/cyeva/commit/ecce3786923008a8723797298e8f5cc986f6e099"
        },
        "date": 1698373902605,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 26206.339822755257,
            "unit": "iter/sec",
            "range": "stddev: 0.000018183293235421298",
            "extra": "mean: 38.15870536532113 usec\nrounds: 3187"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 48.98438014063787,
            "unit": "iter/sec",
            "range": "stddev: 0.002378626322104753",
            "extra": "mean: 20.41467090384576 msec\nrounds: 52"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 4.126922385342982,
            "unit": "iter/sec",
            "range": "stddev: 0.0026917998801863955",
            "extra": "mean: 242.31131739999796 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 27079.889879379494,
            "unit": "iter/sec",
            "range": "stddev: 0.000019264782508457134",
            "extra": "mean: 36.92777202766505 usec\nrounds: 7343"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 60.07135487928065,
            "unit": "iter/sec",
            "range": "stddev: 0.0014780796180025248",
            "extra": "mean: 16.646869410713297 msec\nrounds: 56"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 5.1286956813717195,
            "unit": "iter/sec",
            "range": "stddev: 0.00884482184481729",
            "extra": "mean: 194.98134850000307 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 1594.042544946338,
            "unit": "iter/sec",
            "range": "stddev: 0.00019933169036967762",
            "extra": "mean: 627.3358281247531 usec\nrounds: 960"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.3237638272863568,
            "unit": "iter/sec",
            "range": "stddev: 0.01099438538824015",
            "extra": "mean: 300.8637351999937 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3282108894420162,
            "unit": "iter/sec",
            "range": "stddev: 0.0949962412788875",
            "extra": "mean: 3.046821516799997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 1747.9344819220908,
            "unit": "iter/sec",
            "range": "stddev: 0.0000797120077376924",
            "extra": "mean: 572.1038233082767 usec\nrounds: 1064"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.4656326466477236,
            "unit": "iter/sec",
            "range": "stddev: 0.012265703051313992",
            "extra": "mean: 288.54760499999657 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3370412112162923,
            "unit": "iter/sec",
            "range": "stddev: 0.11754048306661463",
            "extra": "mean: 2.966996220999994 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 1659.9234629389516,
            "unit": "iter/sec",
            "range": "stddev: 0.00038151363622315754",
            "extra": "mean: 602.4374149332558 usec\nrounds: 1058"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.1828234537475852,
            "unit": "iter/sec",
            "range": "stddev: 0.02803512790946503",
            "extra": "mean: 314.18644940000036 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.35582691197994254,
            "unit": "iter/sec",
            "range": "stddev: 0.05557862966188",
            "extra": "mean: 2.810355165200008 sec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "mountain@users.noreply.github.com",
            "name": "Mingli Yuan",
            "username": "mountain"
          },
          "committer": {
            "email": "clarmylee92510@gmail.com",
            "name": "Clarmy Lee",
            "username": "Clarmy"
          },
          "distinct": true,
          "id": "9784bf406e1a92877f968e0044c5e23cb2e3c3f1",
          "message": "Create README.en.md - English version (#49)",
          "timestamp": "2023-10-27T13:05:02+08:00",
          "tree_id": "f3dac188deb61dcc93d7d49e737a0ad7f80b6b33",
          "url": "https://github.com/caiyunapp/cyeva/commit/9784bf406e1a92877f968e0044c5e23cb2e3c3f1"
        },
        "date": 1698383429116,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 43525.29428704881,
            "unit": "iter/sec",
            "range": "stddev: 0.0000047421307947953",
            "extra": "mean: 22.975146208202787 usec\nrounds: 3666"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 57.03196596067039,
            "unit": "iter/sec",
            "range": "stddev: 0.00037391715023236846",
            "extra": "mean: 17.534026456138765 msec\nrounds: 57"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.692098991206267,
            "unit": "iter/sec",
            "range": "stddev: 0.0013674943214100753",
            "extra": "mean: 175.68211683333365 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 46762.015550194235,
            "unit": "iter/sec",
            "range": "stddev: 0.000003722321798109181",
            "extra": "mean: 21.384878051858188 usec\nrounds: 8397"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 70.19741886005126,
            "unit": "iter/sec",
            "range": "stddev: 0.0003902256017020725",
            "extra": "mean: 14.245538030303438 msec\nrounds: 66"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.7489221375996165,
            "unit": "iter/sec",
            "range": "stddev: 0.00007946481113722675",
            "extra": "mean: 148.17180871428295 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2391.680758078971,
            "unit": "iter/sec",
            "range": "stddev: 0.000023349187145391844",
            "extra": "mean: 418.11600340975815 usec\nrounds: 1173"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.4245484365774326,
            "unit": "iter/sec",
            "range": "stddev: 0.00147588590749735",
            "extra": "mean: 292.0093024000039 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3468381520302679,
            "unit": "iter/sec",
            "range": "stddev: 0.0013448798853823501",
            "extra": "mean: 2.8831891594000068 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2401.398785148067,
            "unit": "iter/sec",
            "range": "stddev: 0.000021776360768488267",
            "extra": "mean: 416.42396347691226 usec\nrounds: 1369"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.4320858044185685,
            "unit": "iter/sec",
            "range": "stddev: 0.0005564447475896436",
            "extra": "mean: 291.36800679999624 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3461575561720119,
            "unit": "iter/sec",
            "range": "stddev: 0.0023724804005731655",
            "extra": "mean: 2.8888579265999965 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2363.9331949126226,
            "unit": "iter/sec",
            "range": "stddev: 0.000029612494746998517",
            "extra": "mean: 423.02379870636014 usec\nrounds: 1391"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.4298468078953777,
            "unit": "iter/sec",
            "range": "stddev: 0.0004934006413205091",
            "extra": "mean: 291.55821119999814 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.346985461559961,
            "unit": "iter/sec",
            "range": "stddev: 0.000858237967979106",
            "extra": "mean: 2.881965127600006 sec\nrounds: 5"
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
          "id": "a5d84ca0043e2196228b61eca97fbecffd347d32",
          "message": "fix: wrong ets algorithm",
          "timestamp": "2023-11-08T16:23:49Z",
          "url": "https://github.com/caiyunapp/cyeva/pull/50/commits/a5d84ca0043e2196228b61eca97fbecffd347d32"
        },
        "date": 1699607647460,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 44263.24648672297,
            "unit": "iter/sec",
            "range": "stddev: 0.000004375780867682709",
            "extra": "mean: 22.592106982029797 usec\nrounds: 3552"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 47.37973597900076,
            "unit": "iter/sec",
            "range": "stddev: 0.00042067370283653446",
            "extra": "mean: 21.10606949019748 msec\nrounds: 51"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.29186278743798,
            "unit": "iter/sec",
            "range": "stddev: 0.0012251572847940403",
            "extra": "mean: 188.9693743333325 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 47183.624094039464,
            "unit": "iter/sec",
            "range": "stddev: 0.0000043876970522344005",
            "extra": "mean: 21.193793804540046 usec\nrounds: 7231"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 63.30431389907553,
            "unit": "iter/sec",
            "range": "stddev: 0.00036762178548927193",
            "extra": "mean: 15.79671176271296 msec\nrounds: 59"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.312169640879267,
            "unit": "iter/sec",
            "range": "stddev: 0.0005772671990661369",
            "extra": "mean: 158.42413257142798 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2393.5656524130604,
            "unit": "iter/sec",
            "range": "stddev: 0.00002230227229223835",
            "extra": "mean: 417.7867438028513 usec\nrounds: 1089"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 3.3694171130506687,
            "unit": "iter/sec",
            "range": "stddev: 0.0010313659832834013",
            "extra": "mean: 296.7872383999975 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3410391567327214,
            "unit": "iter/sec",
            "range": "stddev: 0.0033773479900231222",
            "extra": "mean: 2.9322146159999987 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2399.018511798777,
            "unit": "iter/sec",
            "range": "stddev: 0.00002111106058421323",
            "extra": "mean: 416.83713363687343 usec\nrounds: 1317"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 3.372134588657398,
            "unit": "iter/sec",
            "range": "stddev: 0.0003817055166926946",
            "extra": "mean: 296.54806879999 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.34078177338248766,
            "unit": "iter/sec",
            "range": "stddev: 0.004486051011253093",
            "extra": "mean: 2.9344292392 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2411.091711492424,
            "unit": "iter/sec",
            "range": "stddev: 0.000022366337659371928",
            "extra": "mean: 414.74988082515426 usec\nrounds: 1309"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 3.369154832140242,
            "unit": "iter/sec",
            "range": "stddev: 0.0002729193055258266",
            "extra": "mean: 296.81034260000274 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.340374113025761,
            "unit": "iter/sec",
            "range": "stddev: 0.005736152405017751",
            "extra": "mean: 2.9379437558000063 sec\nrounds: 5"
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
          "id": "393588d195d420ce7d9720f3dc7cda97d156a424",
          "message": "fix: wrong ets algorithm (#50)\n\n修复 ETS 计算逻辑错误",
          "timestamp": "2023-11-10T03:33:11-06:00",
          "tree_id": "a20e952a379f75aba87700d48d192659c7b1d722",
          "url": "https://github.com/caiyunapp/cyeva/commit/393588d195d420ce7d9720f3dc7cda97d156a424"
        },
        "date": 1699608883276,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 56576.239140051315,
            "unit": "iter/sec",
            "range": "stddev: 0.000004971762718004055",
            "extra": "mean: 17.675264655265543 usec\nrounds: 4674"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 84.80864754949813,
            "unit": "iter/sec",
            "range": "stddev: 0.0005581095555622916",
            "extra": "mean: 11.791250407764789 msec\nrounds: 103"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 13.688703871150535,
            "unit": "iter/sec",
            "range": "stddev: 0.0009123333559398188",
            "extra": "mean: 73.05293542857173 msec\nrounds: 14"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 61775.92845647111,
            "unit": "iter/sec",
            "range": "stddev: 0.000003640359678577773",
            "extra": "mean: 16.187534934495165 usec\nrounds: 12366"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 103.25536838919331,
            "unit": "iter/sec",
            "range": "stddev: 0.0002098832390427287",
            "extra": "mean: 9.684726475729272 msec\nrounds: 103"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 16.27072032958471,
            "unit": "iter/sec",
            "range": "stddev: 0.0005999394513399411",
            "extra": "mean: 61.460093944440864 msec\nrounds: 18"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 3473.7979660270953,
            "unit": "iter/sec",
            "range": "stddev: 0.000021848354321616008",
            "extra": "mean: 287.86936079177843 usec\nrounds: 1566"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 5.369022668293496,
            "unit": "iter/sec",
            "range": "stddev: 0.002969421776102805",
            "extra": "mean: 186.25363716667684 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.5629895394188021,
            "unit": "iter/sec",
            "range": "stddev: 0.0188427509779315",
            "extra": "mean: 1.7762319368000021 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 3483.0047843694088,
            "unit": "iter/sec",
            "range": "stddev: 0.00001942986999679601",
            "extra": "mean: 287.1084198585297 usec\nrounds: 1984"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 5.42546794516358,
            "unit": "iter/sec",
            "range": "stddev: 0.0016766479224991728",
            "extra": "mean: 184.31589866666323 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.5646918642826614,
            "unit": "iter/sec",
            "range": "stddev: 0.015870846865998232",
            "extra": "mean: 1.7708772929999952 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 3452.375207987751,
            "unit": "iter/sec",
            "range": "stddev: 0.000040158946605157294",
            "extra": "mean: 289.6556543698677 usec\nrounds: 1762"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 5.373288047703622,
            "unit": "iter/sec",
            "range": "stddev: 0.0008534633094923954",
            "extra": "mean: 186.1057868333281 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.5634626976488564,
            "unit": "iter/sec",
            "range": "stddev: 0.014787791789274925",
            "extra": "mean: 1.7747403762000034 sec\nrounds: 5"
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
          "id": "82ba49ce83d3aee87f4d38eb42bb494d072b3c36",
          "message": "chore: bump version (#51)",
          "timestamp": "2023-11-10T03:35:35-06:00",
          "tree_id": "0ebd4581d8cee218d3a3f0309d79e13a2a9fc4a7",
          "url": "https://github.com/caiyunapp/cyeva/commit/82ba49ce83d3aee87f4d38eb42bb494d072b3c36"
        },
        "date": 1699609068972,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 38183.62929067124,
            "unit": "iter/sec",
            "range": "stddev: 0.000005117045113083957",
            "extra": "mean: 26.18923393550526 usec\nrounds: 3984"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 53.71341984923283,
            "unit": "iter/sec",
            "range": "stddev: 0.0003678736757751168",
            "extra": "mean: 18.617321384616375 msec\nrounds: 52"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 5.131097716566646,
            "unit": "iter/sec",
            "range": "stddev: 0.0011583521886235329",
            "extra": "mean: 194.89007133333777 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 41763.23680887233,
            "unit": "iter/sec",
            "range": "stddev: 0.000004210039669883166",
            "extra": "mean: 23.944504219738935 usec\nrounds: 9242"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 67.76745656825761,
            "unit": "iter/sec",
            "range": "stddev: 0.0001863074378211465",
            "extra": "mean: 14.756345459014934 msec\nrounds: 61"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 6.095633109513729,
            "unit": "iter/sec",
            "range": "stddev: 0.000905272481552953",
            "extra": "mean: 164.0518682857167 msec\nrounds: 7"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 2096.3034532845595,
            "unit": "iter/sec",
            "range": "stddev: 0.00002977425381650143",
            "extra": "mean: 477.0301734861745 usec\nrounds: 1222"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 2.986214105552687,
            "unit": "iter/sec",
            "range": "stddev: 0.002838331263593697",
            "extra": "mean: 334.8721707999971 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.3005193783856674,
            "unit": "iter/sec",
            "range": "stddev: 0.00942343188920839",
            "extra": "mean: 3.327572435999997 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 2085.608686694651,
            "unit": "iter/sec",
            "range": "stddev: 0.000032422100998991826",
            "extra": "mean: 479.47633052144437 usec\nrounds: 1304"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 2.9850292936268037,
            "unit": "iter/sec",
            "range": "stddev: 0.0020301974979131826",
            "extra": "mean: 335.0050875999955 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.3004229729781793,
            "unit": "iter/sec",
            "range": "stddev: 0.011658551694058217",
            "extra": "mean: 3.328640250400002 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 2104.081401349798,
            "unit": "iter/sec",
            "range": "stddev: 0.00003656169914995703",
            "extra": "mean: 475.26678357523906 usec\nrounds: 1303"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 2.965916212296347,
            "unit": "iter/sec",
            "range": "stddev: 0.00546422888850163",
            "extra": "mean: 337.1639414000015 msec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.299353789877206,
            "unit": "iter/sec",
            "range": "stddev: 0.01284640990519701",
            "extra": "mean: 3.3405289454000124 sec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ringsaturn.me@gmail.com",
            "name": "ringsaturn",
            "username": "ringsaturn"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "d1856acca8935d23b0e22836355df2f63130e67a",
          "message": "Update index.rst",
          "timestamp": "2024-01-05T10:35:03+08:00",
          "tree_id": "e6d322ceaa2e5737baffc0a303556a9a529339d6",
          "url": "https://github.com/caiyunapp/cyeva/commit/d1856acca8935d23b0e22836355df2f63130e67a"
        },
        "date": 1704422191851,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 56142.46025838501,
            "unit": "iter/sec",
            "range": "stddev: 0.000004591915408429507",
            "extra": "mean: 17.81183074980487 usec\nrounds: 4709"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 97.00944051212353,
            "unit": "iter/sec",
            "range": "stddev: 0.000274533900353787",
            "extra": "mean: 10.308275099009846 msec\nrounds: 101"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 14.001366687403738,
            "unit": "iter/sec",
            "range": "stddev: 0.0010176275724285459",
            "extra": "mean: 71.42159921428564 msec\nrounds: 14"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 61090.53853303401,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035883842936099966",
            "extra": "mean: 16.369146909046503 usec\nrounds: 12375"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 114.17900601913998,
            "unit": "iter/sec",
            "range": "stddev: 0.00015480392346074718",
            "extra": "mean: 8.758177486957356 msec\nrounds: 115"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 16.104337252584084,
            "unit": "iter/sec",
            "range": "stddev: 0.0028247540241598925",
            "extra": "mean: 62.09507316667384 msec\nrounds: 18"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 3370.1391067054096,
            "unit": "iter/sec",
            "range": "stddev: 0.000016650421480856057",
            "extra": "mean: 296.7236568990123 usec\nrounds: 1638"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 5.401220141031196,
            "unit": "iter/sec",
            "range": "stddev: 0.0005625487960899113",
            "extra": "mean: 185.14335166666265 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.557425029285683,
            "unit": "iter/sec",
            "range": "stddev: 0.00422383722486233",
            "extra": "mean: 1.7939632192000032 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 3180.1647663952654,
            "unit": "iter/sec",
            "range": "stddev: 0.00006210096671629518",
            "extra": "mean: 314.4491161486282 usec\nrounds: 1963"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 5.404271394518415,
            "unit": "iter/sec",
            "range": "stddev: 0.00024349180160203676",
            "extra": "mean: 185.03881966666333 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.5561510222530514,
            "unit": "iter/sec",
            "range": "stddev: 0.005750133817764998",
            "extra": "mean: 1.7980727536000018 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 3358.5173990517437,
            "unit": "iter/sec",
            "range": "stddev: 0.000015339865713838534",
            "extra": "mean: 297.7504300803514 usec\nrounds: 1988"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 5.4447698306451615,
            "unit": "iter/sec",
            "range": "stddev: 0.00020996590764088438",
            "extra": "mean: 183.66249283333028 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.5646747263810707,
            "unit": "iter/sec",
            "range": "stddev: 0.0037625158174476397",
            "extra": "mean: 1.7709310391999906 sec\nrounds: 5"
          }
        ]
      },
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
          "id": "5257b76acb87398a5ede74c04fc35b9280732d80",
          "message": "style: reformat",
          "timestamp": "2024-02-26T17:05:02+08:00",
          "tree_id": "9d20db7007bf72d2ef326bf04b76aa7906895fba",
          "url": "https://github.com/caiyunapp/cyeva/commit/5257b76acb87398a5ede74c04fc35b9280732d80"
        },
        "date": 1708938410399,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 57030.294379206236,
            "unit": "iter/sec",
            "range": "stddev: 0.000003927390868524417",
            "extra": "mean: 17.534540385690327 usec\nrounds: 7156"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 91.58724785319933,
            "unit": "iter/sec",
            "range": "stddev: 0.00015388714932736716",
            "extra": "mean: 10.91855060000111 msec\nrounds: 95"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 13.488258559079384,
            "unit": "iter/sec",
            "range": "stddev: 0.0014081745200818408",
            "extra": "mean: 74.13855507143045 msec\nrounds: 14"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 59901.29104122415,
            "unit": "iter/sec",
            "range": "stddev: 0.00000460701856857952",
            "extra": "mean: 16.694131004819223 usec\nrounds: 9763"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 104.75534023643046,
            "unit": "iter/sec",
            "range": "stddev: 0.0003597954082732152",
            "extra": "mean: 9.546052714286663 msec\nrounds: 105"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 15.852498729355506,
            "unit": "iter/sec",
            "range": "stddev: 0.0009803703836171126",
            "extra": "mean: 63.08153793749938 msec\nrounds: 16"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 3381.227747895351,
            "unit": "iter/sec",
            "range": "stddev: 0.000016126391651721516",
            "extra": "mean: 295.75056002141565 usec\nrounds: 1891"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 5.406326170940248,
            "unit": "iter/sec",
            "range": "stddev: 0.0008535440466841688",
            "extra": "mean: 184.96849216666553 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.563033036599991,
            "unit": "iter/sec",
            "range": "stddev: 0.01399921282778902",
            "extra": "mean: 1.7760947137999892 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 3386.637204312111,
            "unit": "iter/sec",
            "range": "stddev: 0.00001549430406553212",
            "extra": "mean: 295.2781593277035 usec\nrounds: 2021"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 5.4049246349243,
            "unit": "iter/sec",
            "range": "stddev: 0.00040315621477169175",
            "extra": "mean: 185.01645583333945 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.5601092952201073,
            "unit": "iter/sec",
            "range": "stddev: 0.018798474459754102",
            "extra": "mean: 1.7853658358000075 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 3402.1915385647067,
            "unit": "iter/sec",
            "range": "stddev: 0.000021803971862774737",
            "extra": "mean: 293.9281897167592 usec\nrounds: 1945"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 5.334335334882528,
            "unit": "iter/sec",
            "range": "stddev: 0.0016547396532316657",
            "extra": "mean: 187.46478000000386 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.5643683335092542,
            "unit": "iter/sec",
            "range": "stddev: 0.004477349629937354",
            "extra": "mean: 1.7718924691999973 sec\nrounds: 5"
          }
        ]
      },
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
          "id": "44ae90c1bd6c3986eed28f8b3e6f5110d27bbbf2",
          "message": "docs: fix links.",
          "timestamp": "2024-02-26T18:38:17+08:00",
          "tree_id": "bbab0ae4b211cb53a75b3175686c348eecdfa59a",
          "url": "https://github.com/caiyunapp/cyeva/commit/44ae90c1bd6c3986eed28f8b3e6f5110d27bbbf2"
        },
        "date": 1708943995399,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 54486.77191502338,
            "unit": "iter/sec",
            "range": "stddev: 0.000006269562298148672",
            "extra": "mean: 18.35307846021017 usec\nrounds: 4754"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 87.09724698585543,
            "unit": "iter/sec",
            "range": "stddev: 0.00019801439834036465",
            "extra": "mean: 11.481419156249562 msec\nrounds: 96"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 14.164160468768932,
            "unit": "iter/sec",
            "range": "stddev: 0.0010397654564933277",
            "extra": "mean: 70.60072513333466 msec\nrounds: 15"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 62166.75940328077,
            "unit": "iter/sec",
            "range": "stddev: 0.0000033594265746043025",
            "extra": "mean: 16.085766888907937 usec\nrounds: 12745"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 118.6484416158213,
            "unit": "iter/sec",
            "range": "stddev: 0.00028832069893146176",
            "extra": "mean: 8.42826072033848 msec\nrounds: 118"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 16.736500650907132,
            "unit": "iter/sec",
            "range": "stddev: 0.00033184047838104834",
            "extra": "mean: 59.74964664706055 msec\nrounds: 17"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 3387.531768227771,
            "unit": "iter/sec",
            "range": "stddev: 0.000016323472745852277",
            "extra": "mean: 295.20018362017083 usec\nrounds: 1917"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 5.450748314612745,
            "unit": "iter/sec",
            "range": "stddev: 0.0009775350822098284",
            "extra": "mean: 183.46104833333263 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.5656485297450173,
            "unit": "iter/sec",
            "range": "stddev: 0.006805234622483202",
            "extra": "mean: 1.7678822579999973 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 3397.4714878435407,
            "unit": "iter/sec",
            "range": "stddev: 0.00001725373782928938",
            "extra": "mean: 294.3365392698924 usec\nrounds: 1999"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 5.434872318549282,
            "unit": "iter/sec",
            "range": "stddev: 0.0010655130671122668",
            "extra": "mean: 183.9969628333288 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.5652128063717841,
            "unit": "iter/sec",
            "range": "stddev: 0.004811442812718525",
            "extra": "mean: 1.7692451210000057 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 3400.1779933653324,
            "unit": "iter/sec",
            "range": "stddev: 0.000014583141765056004",
            "extra": "mean: 294.1022505149056 usec\nrounds: 1944"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 5.444853387821018,
            "unit": "iter/sec",
            "range": "stddev: 0.0010916275089049487",
            "extra": "mean: 183.65967433334163 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.5632635517767317,
            "unit": "iter/sec",
            "range": "stddev: 0.01639188351688926",
            "extra": "mean: 1.7753678484000033 sec\nrounds: 5"
          }
        ]
      },
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
        "date": 1709001084395,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_perf.py::test_calc_mae_1e3",
            "value": 57587.9976199951,
            "unit": "iter/sec",
            "range": "stddev: 0.0000040759270960470995",
            "extra": "mean: 17.364729480588686 usec\nrounds: 5312"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e6",
            "value": 89.74855534996688,
            "unit": "iter/sec",
            "range": "stddev: 0.00020540609969950542",
            "extra": "mean: 11.142240631067372 msec\nrounds: 103"
          },
          {
            "name": "tests/test_perf.py::test_calc_mae_1e7",
            "value": 14.560373898753435,
            "unit": "iter/sec",
            "range": "stddev: 0.0006041846515697052",
            "extra": "mean: 68.67955499999994 msec\nrounds: 15"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e3",
            "value": 62716.669143654995,
            "unit": "iter/sec",
            "range": "stddev: 0.000003707748126223298",
            "extra": "mean: 15.944724323759297 usec\nrounds: 12794"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e6",
            "value": 105.64216667172296,
            "unit": "iter/sec",
            "range": "stddev: 0.0001769033370828507",
            "extra": "mean: 9.46591717592695 msec\nrounds: 108"
          },
          {
            "name": "tests/test_perf.py::test_calc_mbe_1e7",
            "value": 17.040438524551504,
            "unit": "iter/sec",
            "range": "stddev: 0.00036050248458736764",
            "extra": "mean: 58.68393577778067 msec\nrounds: 18"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e3",
            "value": 3401.1542001077755,
            "unit": "iter/sec",
            "range": "stddev: 0.00001712205480679414",
            "extra": "mean: 294.01783664154715 usec\nrounds: 1965"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e6",
            "value": 5.451776913368559,
            "unit": "iter/sec",
            "range": "stddev: 0.0005363205102487041",
            "extra": "mean: 183.42643433333686 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_hit_ratio_1e7",
            "value": 0.5655689579783852,
            "unit": "iter/sec",
            "range": "stddev: 0.003019846404275562",
            "extra": "mean: 1.7681309872000042 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e3",
            "value": 3381.3334779690094,
            "unit": "iter/sec",
            "range": "stddev: 0.000023425387006312824",
            "extra": "mean: 295.74131227087594 usec\nrounds: 1361"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e6",
            "value": 5.454211998898901,
            "unit": "iter/sec",
            "range": "stddev: 0.0009567208621416415",
            "extra": "mean: 183.34454183333548 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_false_alarm_ratio_1e7",
            "value": 0.5636625585009827,
            "unit": "iter/sec",
            "range": "stddev: 0.014010943632401553",
            "extra": "mean: 1.774111096999991 sec\nrounds: 5"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e3",
            "value": 3417.5870062350264,
            "unit": "iter/sec",
            "range": "stddev: 0.00001553206088942182",
            "extra": "mean: 292.60410873976457 usec\nrounds: 1968"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e6",
            "value": 5.456135288046324,
            "unit": "iter/sec",
            "range": "stddev: 0.000996806712324246",
            "extra": "mean: 183.27991283333253 msec\nrounds: 6"
          },
          {
            "name": "tests/test_perf.py::test_calc_threshold_ts_1e7",
            "value": 0.5672067005928937,
            "unit": "iter/sec",
            "range": "stddev: 0.004519495365987989",
            "extra": "mean: 1.7630257170000163 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}