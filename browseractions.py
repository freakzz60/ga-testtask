import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()


def click(classname):
    element = driver.find_element(By.XPATH, classname)
    element.click()
    time.sleep(2)


def entertext(classname, text):
    element = driver.find_element(By.XPATH, classname)
    element.send_keys(text)
    time.sleep(2)


def parsetable(tablexpath):
    table = driver.find_element(By.XPATH, tablexpath)
    rows = table.find_elements(By.TAG_NAME, "tr")
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        data.append([cell.text for cell in cells])
    df = pd.DataFrame(data)
    df = df.drop(columns=[1, 2])
    df.columns = ['Дата', 'Курс', 'Время']
    return df
