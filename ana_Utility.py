import pandas as pd
from excel_Utility import read_excel, df_viewer, add_col_ticketCounter
from output_Utility import df_to_csv


def get_record_resampling_month_data_at_year(df, resample_tar_col, sum_col):
    add_df = add_col_ticketCounter(df)
    return add_df.resample('M', on=resample_tar_col).sum()


if __name__ == '__main__':
    for df in read_excel("ブック1.xlsx"):
        resampling_data = get_record_resampling_month_data_at_year(
            df, "作成日", len(df.columns))
        df_to_csv(resampling_data, "test.csv")
