"""
Tema 8 - SELECTORS
"""

"""
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
"""

"""
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri

- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.

Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
"""

"""
Exerciții extra - Opțional
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
eet/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ID
# chrome = webdriver.Chrome()
# chrome.get("https://www.phptravels.net/")
#
# chrome.maximize_window()
#
# chrome.find_element(By.ID, "flights-tab").click()
# time.sleep(3)
#
# el1 = chrome.find_element(By.CLASS_NAME, "autocomplete-airport")
# el1.click()
# el1.send_keys('Fumicino')
# time.sleep(5)


# LINK TEXT
# chrome = webdriver.Chrome()
# chrome.get("https://formy-project.herokuapp.com/")
#
# chrome.maximize_window()
# time.sleep(3)
#
# chrome.find_element(By.CLASS_NAME, "navbar-brand").click()
# time.sleep(3)
#
# chrome.find_element(By.ID, "navbarDropdownMenuLink").click()
# time.sleep(3)

# chrome.find_element(By.CLASS_NAME, "dropdown-item").click()
# time.sleep(3)
#
# chrome.find_element(By.CLASS_NAME, "pac-target-input").send_keys('Str.rozelor')
# time.sleep(3)
#
# chrome.back()
# time.sleep(2)

# chrome.find_element(By.LINK_TEXT, "Buttons").click()
# time.sleep(2)

# PARTIAL LINK TEXT
# chrome = webdriver.Chrome()
# chrome.get("https://the-internet.herokuapp.com/")
#
# chrome.maximize_window()
# time.sleep(1)
#
# chrome.find_element(By.PARTIAL_LINK_TEXT, "Dynamic ").click()
# time.sleep(2)
# chrome.back()
#
# chrome.find_element(By.LINK_TEXT, "Context Menu").click()
# time.sleep(2)
#
# chrome.find_element(By.ID, "hot-spot").click()
# time.sleep(2)

# NAME
# chrome = webdriver.Chrome()
# chrome.get("https://www.phptravels.net/")
#
# chrome.maximize_window()
# time.sleep(3)
#
# chrome.find_element(By.ID, "flights-tab").click()
# time.sleep(2)
#
# el1 = chrome.find_element(By.CLASS_NAME, "autocomplete-airport")
# el1.click()
# el1.send_keys('Milan')
# time.sleep(2)


# TAG
# chrome = webdriver.Chrome()
# chrome.get("https://the-internet.herokuapp.com/login")
#
# chrome.maximize_window()
# time.sleep(1)
#
# tag = chrome.find_element(By.TAG_NAME, "input")
# tag.click()
# tag.send_keys('ana-maria')
# time.sleep(2)
#
# tag1 = chrome.find_element(By.ID, "password")
# tag1.click()
# tag1.send_keys('1234')
# time.sleep(2)

# CLASS NAME
# chrome = webdriver.Chrome()
# chrome.get("https://formy-project.herokuapp.com/form")
#
# chrome.maximize_window()
#
# el1 = chrome.find_element(By.CLASS_NAME, "form-control")
# el1.click()
# el1.send_keys('Ioana')
# time.sleep(3)

# CSS
# chrome = webdriver.Chrome()
# chrome.get("https://formy-project.herokuapp.com/form")
#
# chrome.maximize_window()
#
# el2 = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your job title"]')
# el2.send_keys('QA')
# time.sleep(2)
#
# el3 = chrome.find_element(By.CSS_SELECTOR, "input#first-name")
# el3.send_keys('Ioana')
# time.sleep(2)
#
# el4 = chrome.find_elements(By.CSS_SELECTOR, "input.form-control")
# el4[1].send_keys('Popescu')
# time.sleep(2)

'''
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
'''
# xpath
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

chrome.maximize_window()

# 3 exemple dupa atribut - valoare
# el1 = chrome.find_element(By.XPATH, '//input[@id="first-name"]')
# el1.send_keys('Ioana')
# time.sleep(2)
#
# el1.clear()
#
# el2 = chrome.find_element(By.XPATH, '//input[@class="form-control"]')
# el2.send_keys('Mada')
# time.sleep(2)
#
# el3 = chrome.find_element(By.XPATH, '//input[@placeholder="Enter your job title"]')
# el3.send_keys('Testare')
# time.sleep(2)
#
# el3.clear()
#
# 1 exemplu dupa *
# el4 = chrome.find_element(By.XPATH, '//*[@id="job-title"]')
# el4.send_keys('QA')
# time.sleep(2)


# 1 exemplu dupa textul de pe element
# el5 = chrome.find_element(By.XPATH, '//*[@id="select-menu"]')
# el5.click()
# time.sleep(2)
#
# el6 = chrome.find_element(By.XPATH, '//*[@id="select-menu"]/option[3]')
# el6.click()
# time.sleep(2)

# 1 exemplu dupa partial text
# nu stiu daca am inteles bine si daca am facut ok
# el7 = chrome.find_element(By.XPATH, '//*["Enter"]')
# el7.click()
# time.sleep(2)

# 1 exemplu cu (xpath)[1]
# el = chrome.find_element(By.XPATH, "//div[@class='form-group']/div[1]/input")
# el.click()
# el.send_keys('Ana')
# time.sleep(2)

# 1 cu SAU, folosind pipe | pe asta nu l-am inteles

# 1 exemplu pentru parent::
# el2 = chrome.find_element(By.XPATH, "//input[@type='text']/parent::*")
# el2.click()
# time.sleep(2)

# 1 exemplu cu fratele  de dupa
# el1 = chrome.find_element(By.XPATH, "//div[@class='form-group']/div[1]/following-sibling::div")
# el1.click()
# time.sleep(2)

chrome.find_element(By.XPATH, '/html/body/div/form/div/div[8]/a').click()
time.sleep(2)