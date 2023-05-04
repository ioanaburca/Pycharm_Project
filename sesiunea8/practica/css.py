from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(2)

chrome.maximize_window()
time.sleep(2)

"""
CSS Selectors

Putem identifica un element dupa mai multi selectori CSS:

1. cautam dupa id: #
2. cautam dupa clasa: .
3. putem cauta in acelasi timp un element dupa tag + id
4. putem cauta in acelasi timp un element dupa tag + clasa
5. putem cauta dupa tag + atribut=valoare
6. putem cauta dupa tag + atribut=valoare PARTIALA

Resursa cu CSS Selectori: https://www.w3schools.com/cssref/css_selectors.php
"""

# CSS SELECTOR - CLASA - inputul pentru Last Name
# elements = chrome.find_elements(By.CSS_SELECTOR, '.form-control')
# elements[1].send_keys("Popa")
# time.sleep(3)

# ca sa stergem continutul unui element, ne folosim de metoda clear()
# elements[1].clear()
# time.sleep(2)

# CSS SELECTOR - ID - inputul pentru Last Name
# element = chrome.find_element(By.CSS_SELECTOR, '#last-name')
# element.send_keys("Popescu")
# time.sleep(3)

# CSS SELECTOR - TAG + ID - inputul pentru First Name
# element = chrome.find_element(By.CSS_SELECTOR, 'input#first-name')
# element.send_keys("ana")
# time.sleep(2)

# CSS SELECTOR - TAG + CLASA - inputul pentru Last Name
# elements = chrome.find_elements(By.CSS_SELECTOR, 'input.form-control')
# elements[1].send_keys("popa")
# time.sleep(2)

# CSS SELECTOR - TAG + pereche atribut=valoare - Job
# element = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your job title"]')
# element.send_keys("Tester")
# time.sleep(2)


# CSS SELECTOR - TAG + pereche atribut=valoare partiala -  Job
# element = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="job"]')
# element.send_keys("Tester")
# time.sleep(2)

# CSS SELECTOR - TAG + pereche atribut=valoare partiala + parinte => copil
element = chrome.find_element(By.CSS_SELECTOR, 'strong > label[for="last-name"]')
text_last_name = element.text

assert text_last_name == 'Last name'
time.sleep(2)

