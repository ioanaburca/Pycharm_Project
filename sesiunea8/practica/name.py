from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()
chrome.get("http://www.seleniumframework.com/PracticeForm")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.NAME, 'country').send_keys("Romania")
time.sleep(2)