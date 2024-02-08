import initwebdriver
import browseractions
import wordcase
import mail
import os
import calculatedates
import tableops
import main


def makemagic():
    initwebdriver.driver.get('https://moex.ru')
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
    browseractions.entertext('//*[@id="fromDate"]', calculatedates.firstofprevmonth.strftime("%d%m%Y"))
    # Ввод начальной даты
    browseractions.click('(//*[@id="keysParams"])[2]')
    # Выбор конечной даты
    browseractions.entertext('//*[@id="tillDate"]', calculatedates.lastofprevmonth.strftime("%d%m%Y"))
    # Ввод конечной даты
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[4]/button')
    # Показать
    main.firsttable = browseractions.parsetable('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[1]'
                                                '/div[2]/div/div[2]/div[3]/table/tbody')
    # Украсть таблицу
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[1]/div[1]')
    # Список валют
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div[8]/div')
    # JPY/RUB
    browseractions.click('(//*[@id="keysParams"])[1]')
    # Выбор начальной даты
    browseractions.entertext('//*[@id="fromDate"]', calculatedates.firstofprevmonth.strftime("%d%m%Y"))
    # Ввод начальной даты
    browseractions.click('(//*[@id="keysParams"])[2]')
    # Выбор конечной даты
    browseractions.entertext('//*[@id="tillDate"]', calculatedates.lastofprevmonth.strftime("%d%m%Y"))
    # Ввод конечной даты
    browseractions.click('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/form/div[4]/button')
    # Показать
    main.secondtable = browseractions.parsetable('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[5]/div[1]'
                                                 '/div[2]/div/div[2]/div[3]/table/tbody')
    # Украсть таблицу
    initwebdriver.driver.close()
    # Закрыть браузер
    tableops.maketable()
    # Сгенерить таблицу
    mail.send('Тестовое задание', f"Добрый день. Высылаю Excel-файл, содержащий {tableops.countrows()} "
                                  f"{wordcase.correctcase()}", main.exportfilename)
    # Отправить письмо
    os.remove(main.exportfilename)
    # Убрать за собой


def cleanobsoletefiles():
    for deletecandidate in os.listdir("."):
        if deletecandidate.endswith("xlsx"):
            os.remove(deletecandidate)
