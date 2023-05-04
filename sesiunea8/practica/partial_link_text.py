from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com")
time.sleep(2)

chrome.maximize_window()
time.sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT, "Authentication").click()
time.sleep(2)

# elements = chrome.find_elements(By.PARTIAL_LINK_TEXT, "Authentication")
# elements[1].click()
# time.sleep(3)
