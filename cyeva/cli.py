import os
from glob import glob

import fire
import pandas as pd

from cyeva import Temperature, Precipitation, Wind, Gust, Visibility

KINDS = {"1h": "1hour", "3h": "3hour", "24h": "24hour"}


def parse_info(fp):
    subpath, filename = fp.split("/")[-2:]
    station_kind, init_hour, _ = subpath.split("_")
    step = filename.split(".")[0]

    return {"station_kind": station_kind, "init_hour": init_hour, "step": step}


def generate(base_dir=".", savefp="./result.csv"):
    """计算各项指标

    Args:
        base_dir (str, optional): 数据根目录. Defaults to '.'.
        savefp (str, optional): 结果保存路径. Defaults to './result.csv'.
    """
    result = []
    for kind, kdir in KINDS.items():
        fps = sorted(glob(os.path.join(base_dir, kdir, "*/*.csv")))

        for fp in fps:
            fp_info = parse_info(fp)
            print(f"正在处理温度: {fp} ")
            if kind != "24h":
                temp = Temperature(
                    fp,
                    time_col_name="bj_time",
                    obs_col_name="t2m_obs",
                    fct_col_name="t2m_predict",
                    kind=kind,
                )
                temp_df = temp.gather_all_factors()
                temp_df["数据源"] = [fp] * len(temp_df)
                temp_df["起报时次"] = [fp_info["init_hour"]] * len(temp_df)
                temp_df["站点类型"] = [fp_info["station_kind"]] * len(temp_df)
                temp_df["预报时效"] = [fp_info["step"]] * len(temp_df)
            else:
                temp = Temperature(
                    fp,
                    time_col_name="bj_time",
                    obs_col_name="tmax_obs",
                    fct_col_name="tmax_predict",
                    obs_col_name2="tmin_obs",
                    fct_col_name2="tmin_predict",
                    kind=kind,
                )
                temp_df = temp.gather_all_factors()
                temp_df["数据源"] = [fp] * len(temp_df)
                temp_df["起报时次"] = [fp_info["init_hour"]] * len(temp_df)
                temp_df["站点类型"] = [fp_info["station_kind"]] * len(temp_df)
                temp_df["预报时效"] = [fp_info["step"]] * len(temp_df)

            print(f"正在处理降水: {fp} ")
            precip = Precipitation(
                fp,
                time_col_name="bj_time",
                obs_col_name="rain_obs",
                fct_col_name="rain_predict",
                kind=kind,
            )
            precip_df = precip.gather_all_factors()
            precip_df["数据源"] = [fp] * len(precip_df)
            precip_df["起报时次"] = [fp_info["init_hour"]] * len(precip_df)
            precip_df["站点类型"] = [fp_info["station_kind"]] * len(precip_df)
            precip_df["预报时效"] = [fp_info["step"]] * len(precip_df)

            print(f"正在处理风: {fp} ")
            wind = Wind(
                fp,
                time_col_name="bj_time",
                obs_spd_col_name="w10m_obs",
                obs_dir_col_name="d10m_obs",
                fct_spd_col_name="w10m_predict",
                fct_dir_col_name="d10m_predict",
                kind=kind,
            )
            wind_df = wind.gather_all_factors()
            wind_df["数据源"] = [fp] * len(wind_df)
            wind_df["起报时次"] = [fp_info["init_hour"]] * len(wind_df)
            wind_df["站点类型"] = [fp_info["station_kind"]] * len(wind_df)
            wind_df["预报时效"] = [fp_info["step"]] * len(wind_df)

            print(f"正在处理阵风: {fp} ")
            gust = Gust(
                fp,
                time_col_name="bj_time",
                obs_spd_col_name="gust_obs",
                fct_spd_col_name="gust_predict",
                kind=kind,
            )
            gust_df = gust.gather_all_factors()
            gust_df["数据源"] = [fp] * len(gust_df)
            gust_df["起报时次"] = [fp_info["init_hour"]] * len(gust_df)
            gust_df["站点类型"] = [fp_info["station_kind"]] * len(gust_df)
            gust_df["预报时效"] = [fp_info["step"]] * len(gust_df)

            print(f"正在处理能见度: {fp} ")
            vis = Visibility(
                fp,
                time_col_name="bj_time",
                obs_col_name="vis_obs",
                fct_col_name="vis_predict",
                kind=kind,
            )
            vis_df = vis.gather_all_factors()
            vis_df["数据源"] = [fp] * len(vis_df)
            vis_df["起报时次"] = [fp_info["init_hour"]] * len(vis_df)
            vis_df["站点类型"] = [fp_info["station_kind"]] * len(vis_df)
            vis_df["预报时效"] = [fp_info["step"]] * len(vis_df)

            # if kind != '24h':
            #     result.append(
            #         pd.concat([temp_df, precip_df, wind_df, gust_df, vis_df]))
            # else:
            #     result.append(pd.concat([temp_df, precip_df, wind_df, gust_df, vis_df]))
            result.append(pd.concat([temp_df, precip_df, wind_df, gust_df, vis_df]))

    pd.concat(result).reset_index(drop=True).to_csv(savefp)


def cli():
    fire.Fire(generate)


if __name__ == "__main__":
    generate(
        "/Users/wentao.li/moji/lab/冬奥会/predict_bj_wog_merge_xiongjie_complete_2021-09-06-modify-precip/sample",
        "./result7.csv",
    )
