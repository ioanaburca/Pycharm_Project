from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.CLASS_NAME, 'form-control').send_keys("Andy")
time.sleep(3)
