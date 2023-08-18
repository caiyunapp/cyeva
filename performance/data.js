window.BENCHMARK_DATA = {
  "lastUpdate": 1692342264534,
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
      }
    ]
  }
}