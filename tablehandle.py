import calculatedates
import clickelement
import entertext
import parsetable
import datetime
import tableops

filename = 'export ' + datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + '.xlsx'  # Сгенерить имя файла


def handle():
    clickelement.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[1]/div[1]')
    # Список валют
    clickelement.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div[17]/div')
    # USD/RUB
    clickelement.click('(//*[@id="keysParams"])[1]')
    # Выбор начальной даты
    entertext.enter('//*[@id="fromDate"]', calculatedates.firstofprevmonth.strftime("%d%m%Y"))
    # Ввод начальной даты
    clickelement.click('(//*[@id="keysParams"])[2]')
    # Выбор конечной даты
    entertext.enter('//*[@id="tillDate"]', calculatedates.lastofprevmonth.strftime("%d%m%Y"))
    # Ввод конечной даты
    clickelement.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[4]/button')
    # Показать
    first = parsetable.doparse('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[1]/div[2]/div/div[2]'
                               '/div[3]/table/tbody')
    # Украсть таблицу
    clickelement.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[1]/div[1]')
    # Список валют
    clickelement.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div[8]/div')
    # JPY/RUB
    clickelement.click('(//*[@id="keysParams"])[1]')
    # Выбор начальной даты
    entertext.enter('//*[@id="fromDate"]', calculatedates.firstofprevmonth.strftime("%d%m%Y"))
    # Ввод начальной даты
    clickelement.click('(//*[@id="keysParams"])[2]')
    # Выбор конечной даты
    entertext.enter('//*[@id="tillDate"]', calculatedates.lastofprevmonth.strftime("%d%m%Y"))
    # Ввод конечной даты
    clickelement.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[4]/button')
    # Показать
    second = parsetable.doparse('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[1]/div[2]/div/'
                                'div[2]/div[3]/table/tbody')
    # Украсть таблицу
    result = first.join(second, how='right', lsuffix=' USD/RUB', rsuffix=' JPY/RUB')
    # Объединить две таблицы
    result.to_excel(filename, index=False)
    # Записать файл без индексов
    tableops.calcresult()
    tableops.formatting()
