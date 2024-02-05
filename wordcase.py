import tableops


def correctcase():
    rowsnum = tableops.countrows()
    if rowsnum[-1] in ('0', '5', '6', '7', '8', '9') or rowsnum in ('11', '12', '13', '14'):
        return 'строк данных'
    elif rowsnum[-1] in ('2', '3', '4') and rowsnum not in ('12', '13', '14'):
        return 'строки данных'
    elif rowsnum[-1] in '1':
        return 'строку данных'
