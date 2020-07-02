import pandas as pd
from resources.data.path import *

def get_sheet(sheet):
    data = pd.read_excel(EXCEL_PATH, sheet_name = sheet)
    return data

def get_value(sheet,row_name, col_name):
    data = pd.read_excel(EXCEL_PATH, sheet_name = sheet, index_col="TestCaseID")
    value = data.loc[row_name, col_name]
    return value

def write_to_excel(sheet, row_number, column_name, value_to_write):
    data = get_sheet(EXCEL_PATH, sheet)
    data.loc[row_number, column_name] = value_to_write
    write = pd.ExcelWriter(EXCEL_PATH)
    data.to_excel(write, sheet_name= sheet)
    write.save()