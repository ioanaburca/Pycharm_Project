from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()

chrome.implicitly_wait(10)

chrome.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

# identificare + setare username
el1 = chrome.find_element(By.ID, 'username')
el1.send_keys('tomsmith')
time.sleep(2)

# identificare + setare password
el2 = chrome.find_element(By.ID, 'password')
el2.send_keys('SuperSecretPassword!')
time.sleep(2)

# identificare buton login + declansare login
el3 = chrome.find_element(By.CLASS_NAME, 'radius')
el3.click()
time.sleep(2)
chrome.quit()