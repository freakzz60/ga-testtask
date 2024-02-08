import browseractions
import mail
import os
import tableops
import datetime


def makemagic(filename):
    browseractions.driver.get('https://moex.ru')
    # Открыть moex
    browseractions.click("/html/body/div[1]/div/div/div[2]/div/header/div[4]/div[2]/button")
    # Меню
    browseractions.click("/html/body/div[1]/div/div/div[2]/div/header/div[5]/div[2]/div/div/ul/li[2]/a")
    # Срочный рынок
    browseractions.click("/html/body/div[2]/div/div/div/div/div[1]/div/a[1]")
    # Принять EULA
    browseractions.click("/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[16]/div/a/span")
    # Индикативные курсы
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[1]/div[1]')
    # Список валют
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div[17]/div')
    # USD/RUB
    browseractions.click('(//*[@id="keysParams"])[1]')
    # Выбор начальной даты
    today = datetime.date.today()
    # Получить текущую дату
    lastofprevmonth = (today.replace(day=1)) - datetime.timedelta(days=1)
    # Получить последний день предыдущего месяца
    firstofprevmonth = lastofprevmonth.replace(day=1)
    # Получить первый день предыдущего месяца
    browseractions.entertext('//*[@id="fromDate"]', firstofprevmonth.strftime("%d%m%Y"))
    # Ввод начальной даты
    browseractions.click('(//*[@id="keysParams"])[2]')
    # Выбор конечной даты
    browseractions.entertext('//*[@id="tillDate"]', lastofprevmonth.strftime("%d%m%Y"))
    # Ввод конечной даты
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[4]/button')
    # Показать
    firsttable = browseractions.parsetable('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[1]/'
                                           'div[2]/div/div[2]/div[3]/table/tbody')
    # Украсть таблицу
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[1]/div[1]')
    # Список валют
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div[8]/div')
    # JPY/RUB
    browseractions.click('(//*[@id="keysParams"])[1]')
    # Выбор начальной даты
    browseractions.entertext('//*[@id="fromDate"]', firstofprevmonth.strftime("%d%m%Y"))
    # Ввод начальной даты
    browseractions.click('(//*[@id="keysParams"])[2]')
    # Выбор конечной даты
    browseractions.entertext('//*[@id="tillDate"]', lastofprevmonth.strftime("%d%m%Y"))
    # Ввод конечной даты
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[4]/button')
    # Показать
    secondtable = browseractions.parsetable('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[1]'
                                            '/div[2]/div/div[2]/div[3]/table/tbody')
    # Украсть таблицу
    browseractions.driver.close()
    # Закрыть браузер
    tableops.maketable(filename, firsttable, secondtable)
    # Сгенерить таблицу
    rowsnum = str(tableops.countrows(filename))
    try:
        mail.send('Тестовое задание', f"Добрый день. Высылаю Excel-файл, содержащий {rowsnum} "
                                      f"{correctcase(rowsnum)}", filename)
    except Exception:
        print('Письмо не отправлено. Проверьте конфигурацию')
    os.remove(filename)
    # Убрать за собой


def cleanobsoletefiles():  # Удалить старые выгрузки, если остались
    for deletecandidate in os.listdir("."):
        if deletecandidate.endswith("xlsx"):
            os.remove(deletecandidate)


def correctcase(rowsnum):  # Подобрать склонение
    if rowsnum[-1] in ('0', '5', '6', '7', '8', '9') or rowsnum in ('11', '12', '13', '14'):
        return 'строк данных'
    elif rowsnum[-1] in ('2', '3', '4') and rowsnum not in ('12', '13', '14'):
        return 'строки данных'
    elif rowsnum[-1] in '1':
        return 'строку данных'
