from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

el1 = chrome.find_element(By.LINK_TEXT, "Form Authentication")
el1.click()
time.sleep(3)

chrome.back()
time.sleep(2)

el2 = chrome.find_element(By.LINK_TEXT, "Checkboxes")
el2.click()
time.sleep(2)