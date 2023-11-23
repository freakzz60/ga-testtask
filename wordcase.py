def correctcase(input):
    numatinput = str()
    for text in input:
        if text.isnumeric():
            numatinput += text
    if numatinput[-1] in ('0', '5', '6', '7', '8', '9') or numatinput in ('11', '12', '13', '14'):
        input += ' строк данных'
    elif numatinput[-1] in ('2', '3', '4') and numatinput not in ('12', '13', '14'):
        input += ' строки данных'
    elif numatinput[-1] in ('1'):
        input += ' строку данных'
    return(input)