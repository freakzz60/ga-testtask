import tablehandle
import openpyxl as oxl
import pandas as pd


def calcresult():
    df = pd.read_excel(tablehandle.filename)
    df['Результат'] = df['Курс USD/RUB'] / df['Курс JPY/RUB']
    df.to_excel(tablehandle.filename, index=False)


def formatting():
    wb = oxl.load_workbook(filename=tablehandle.filename)
    ws = wb.active
    column_letters = tuple(oxl.utils.get_column_letter(col_number + 1) for col_number in range(ws.max_column))
    for column_letter in column_letters:
        ws.column_dimensions[column_letter].auto_size = True
        ws.column_dimensions[column_letter].width += 2
    for row in (ws.iter_rows()):
        for c in row:
            c.number_format = '₽ #,##0.00'
    wb.save(tablehandle.filename)


def countrows():
    wb = oxl.load_workbook(filename=tablehandle.filename)
    ws = wb.active
    rowsnum = str(ws.max_row - 1)
    return rowsnum
