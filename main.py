import initwebdriver, clickelement, tablehandle, wordcase, tableops, mail, os

initwebdriver.driver.get('https://moex.ru')
clickelement.click("/html/body/div/div/div/div[2]/div/header/div[5]/div[3]/button") # Меню
clickelement.click("/html/body/div/div/div/div[2]/div/header/div[6]/div[2]/div/div/ul[1]/li[2]/a") # Срочный рынок
clickelement.click("/html/body/div[2]/div/div/div/div/div[1]/div/a[1]") # Принять EULA
clickelement.click("/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[14]/div/a") # Индикативные курсы
tablehandle.handle()
initwebdriver.driver.close()
mail.send('Тестовое задание', str(wordcase.correctcase('Добрый день. Высылаю Excel-файл, содержащий ' + tableops.countrows())), tablehandle.filename)
os.remove(tablehandle.filename)