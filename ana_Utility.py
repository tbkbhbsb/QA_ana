import pandas as pd
from excel_Utility import read_excel, df_viewer, add_col_ticketCounter
from output_Utility import df_to_csv


def get_record_resampling_month_data_at_year(df, resample_tar_col, sum_col):
    add_df = add_col_ticketCounter(df)
    return add_df.resample('M', on=resample_tar_col).sum()


def sprit_YMD(df, dateColName):

    sprited = df.copy()
    print(sprited.index)

    # print(df[])

    # y = lambda x: x[dateColName].year
    # m = lambda x: x[dateColName].month
    # d = lambda x: x[dateColName].day

    # df["year"] = df.apply(y, axis=1)
    # sprited["month"] = df.apply(m, axis=1)
    # sprited["day"] = df.apply(d, axis=1)

    return sprited


def sprit_YMD_index(df):
    sprited = df.copy()

    for index, time in enumerate(sprited.index):
        print(type(index))
        print(sprited[index])
        # sprited[index]["year"] = index.year
        # sprited[index]["month"] = index.month
        # sprited[index]["day"] = index.day

    print(sprited)

    return sprited


if __name__ == '__main__':
    for df in read_excel("ブック1.xlsx"):
        resampling_data = get_record_resampling_month_data_at_year(
            df, "作成日", len(df.columns))
        # print(resampling_data)
        sprit_YMD_index(resampling_data)
        # df_to_csv(resampling_data, "test.csv")
