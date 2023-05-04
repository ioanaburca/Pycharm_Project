from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

# XPATH relativ el input first-name
# //*[@id="first-name"]

# XPATH ABSOLUT el input first-name
# /html/body/div/form/div/div[1]/input