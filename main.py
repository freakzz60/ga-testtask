import initwebdriver
import clickelement
import tablehandle
import wordcase
import tableops
import mail
import os

initwebdriver.driver.get('https://moex.ru')
# Открыть moex
clickelement.click("/html/body/div[1]/div/div/div[2]/div/header/div[4]/div[2]/button")
# Меню
clickelement.click("/html/body/div[1]/div/div/div[2]/div/header/div[5]/div[2]/div/div/ul/li[2]/a")
# Срочный рынок
clickelement.click("/html/body/div[2]/div/div/div/div/div[1]/div/a[1]")
# Принять EULA
clickelement.click("/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[16]/div/a/span")
# Индикативные курсы
tablehandle.handle()
initwebdriver.driver.close()
print('Тестовое задание', f"Добрый день. Высылаю Excel-файл, содержащий {tableops.countrows()} {wordcase.correctcase()}"
      , tablehandle.filename)
mail.send('Тестовое задание', f"Добрый день. Высылаю Excel-файл, содержащий {tableops.countrows()} "
                              f"{wordcase.correctcase()}", tablehandle.filename)
os.remove(tablehandle.filename)
