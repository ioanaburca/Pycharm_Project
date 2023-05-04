# 1. Importam libraria webdriver din framework-ul selenium
from selenium import webdriver
# 8. Importam clasa By
from selenium.webdriver.common.by import By
# 5. importam modulul time
import time

# 2. Deschidem un browser Chrome
chrome = webdriver.Chrome()

# 3. Deschidem un site
chrome.get("https://the-internet.herokuapp.com/login")

# 4. Pentru a vedea ce se intampla, adaugam un delay
time.sleep(3)

# 6. De fiecare data cand lucram cu browser-ul, recomandarea
# este sa maximizam fereastra
# ca sa fim siguri ca avem acces la toate elementele
chrome.maximize_window()
time.sleep(3)

# 7. Identificam username-ul dupa id
el1 = chrome.find_element(By.ID, 'username')

# 9. Trimitem text/ completam inputul el1
el1.send_keys("cosminabacter")
time.sleep(2)

# 10. Identificam parola dupa id si o completam
el2 = chrome.find_element(By.ID, "password")
el2.send_keys("1234")
time.sleep(2)