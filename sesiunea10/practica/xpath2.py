import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')
time.sleep(1)

chrome.maximize_window()
time.sleep(1)


# 1. XPATH - Cautare dupa atribut-valoare pentru tag specific
el1 = chrome.find_element(By.XPATH, '//input[@id="first-name"]')
el1.send_keys("Ana")
time.sleep(2)

el1.clear()

# 2. XPATH - Cautare dupa atribut-valoare pentru orice element/indiferent de tag
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Cosmina")
time.sleep(2)

# 3. XPATH - Cautare dupa atribut-valoare navigand in jos, trecand prin
# fiecare element (practic cautam dupa copii)

# identificam elementul input job -> dupa placeholder,
# dar vrem sa ne asiguram, ca il indentificam sigur pe acela
# -> si atunci vedem a cui copil este

# incepem de la div cu o clasa mai unica de exemplu:
# div cu clasa form-group
# "//div[@class='form-group']//div/input[@placeholder='Enter your job title']"
# SAU
# "//div[@class='form-group']/div[3]/input"

chrome.find_element(
  By.XPATH,
  "//div[@class='form-group']/div[3]/input"
).send_keys("Tester")
time.sleep(2)

# 4. XPATH - navigare in jos - skip tags

# luam exemplul din curs

chrome.find_element(
    By.XPATH,
    '//form//input[@id="first-name"]'
)

# Daca vrem sa accesam al doilea element -> fratele primului
# putem scrie
# //div[@class='form-group']/div[1]/following-sibling::div"

chrome.quit()