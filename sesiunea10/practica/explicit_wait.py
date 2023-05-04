import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome() # deschidem browserul
chrome.implicitly_wait(10)
chrome.get('https://the-internet.herokuapp.com/login')


# pentru explicit wait, trebuie sa ne folosim de clasa WebDriverWait
# pe aceasta, trebuie sa o importam, din selenium.webdriver.support.ui
# cream un obiect de tip clasa WebDriverWait, la care trebuie sa ii dam
# instanta de chrome si perioada de asteptare pentru element
username = WebDriverWait(chrome, 1).until(EC.presence_of_element_located((By.ID, "usernames")))
username.send_keys("tomsmith")
time.sleep(2)

# locator = (By.ID, "username")
# *locator = By.ID, username
# find_element(By.ID, username)

chrome.find_element(By.ID, "passwords").send_keys("SuperSecretPassword!")

chrome.find_element(By.CLASS_NAME, 'radius').click()
time.sleep(3)

chrome.quit()