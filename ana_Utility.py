import pandas as pd
from excel_Utility import read_excel, df_viewer, add_col_ticketCounter
from output_Utility import df_to_csv


def get_record_resampling_month_data_at_year(df, resample_tar_col, sum_col):
    add_df = add_col_ticketCounter(df)
    return add_df.resample('M', on=resample_tar_col).sum()


def get_record_resampling_business_year_end_frequency(df, resample_tar_col, sum_col):
    add_df = add_col_ticketCounter(df)
    return add_df.resample('A', on=resample_tar_col).sum()

def sprit_YMD(df, dateColName):

    sprited = df.copy()
    print(sprited.index)

    # print(df[])

    y = lambda x: x[dateColName].year
    m = lambda x: x[dateColName].month
    d = lambda x: x[dateColName].day

    sprited["year"] = df.apply(y, axis=1)
    sprited["month"] = df.apply(m, axis=1)
    sprited["day"] = df.apply(d, axis=1)

    return sprited


def sprit_YMD_index(df):
    sprited = df.copy()
    sprited["y-m-d"] = sprited.index
    return sprit_YMD(sprited, "y-m-d")


if __name__ == '__main__':
    for df in read_excel("案件一覧_201705291850.xlsx"):
        resampling_data = get_record_resampling_business_year_end_frequency(
            df, "プロジェクト開始年月日", len(df.columns))
        YMD_splited = sprit_YMD_index(resampling_data)
        # print(YMD_splited)
        df_to_csv(YMD_splited, "プロジェクト開始年集計_年度推移.csv")
