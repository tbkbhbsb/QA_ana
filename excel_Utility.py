import pandas as pd
import numpy as np

import dateutil.parser


def read_excel(filePath):
    df_list = []
    file = pd.ExcelFile(filePath)
    my_parser = lambda date: pd.datetime.strptime(date, "%Y/%m/%d %H:%M:%S")
    for sheet in file.sheet_names:
        df_list.append(file.parse(sheet))
    return df_list
# lambda date: pd.datetime.strptime(date, "%y%y%y%y/%m%m/%d%d %h%h:%m%m:%s%s")


def add_col_ticketCounter(df):
    add_df = df.copy()
    add_df["ticketCounter"] = np.ones(len(add_df.index))
    return add_df


def df_viewer(df):
    print(df)

if __name__ == '__main__':
    for df in read_excel("ブック1.xlsx"):
        df_viewer(df)
