from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()
chrome.get("http://formy-project.herokuapp.com/form")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.TAG_NAME, 'input').send_keys('Andy')
time.sleep(3)

# cautam toate elementele cu tag-ul input
# si il accesam pe al doilea
elements = chrome.find_elements(By.TAG_NAME, 'input')
elements[1].send_keys('Popa')
time.sleep(3)