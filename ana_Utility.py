import pandas as pd
from excel_Utility import read_excel, df_viewer, add_col_ticketCounter


def get_resampling_month_data_at_year(df, resample_tar_col, sum_col):
    add_df = add_col_ticketCounter(df)
    # print(add_df)
    # input()
    return add_df.resample('M', on=resample_tar_col).sum()
    # return df.groupby(df[tar_col].dt.year, df[tar_col].dt.month).groups

if __name__ == '__main__':
    for df in read_excel("ブック1.xlsx"):
        df_viewer(get_resampling_month_data_at_year(
            df, "作成日", len(df.columns)))
