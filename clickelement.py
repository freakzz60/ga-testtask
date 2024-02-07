import time
import initwebdriver
from selenium.webdriver.common.by import By


def click(classname):
    element = initwebdriver.driver.find_element(By.XPATH, classname)
    element.click()
    time.sleep(2)
