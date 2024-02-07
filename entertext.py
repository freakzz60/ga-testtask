import time
import initwebdriver
from selenium.webdriver.common.by import By


def enter(classname, text):
    element = initwebdriver.driver.find_element(By.XPATH, classname)
    element.send_keys(text)
    time.sleep(2)
