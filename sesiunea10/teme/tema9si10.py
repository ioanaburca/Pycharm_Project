"""
OBLIGATORIU - grad de dificultate: Usor spre Mediu


1. Implementează o clasă Login care să moștenească unittest.TestCase.

In metoda de setUp():
- seteaza driver-ul (instanta de browser)
- acceseaza site-ul 'https://the-internet.herokuapp.com/'
- click pe Form Authentication

In metoda de tearDown():
- quit la browser

● Test 1
- Verifică dacă noul url e corect

● Test 2
- Verifică dacă page title e corect (page title este tag-ul title din <head>)

● Test 3
- Verifică daca textul de pe elementul xpath=//h2 e corect

● Test 4
- Verifică dacă butonul de login este displayed

● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed

● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')

● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut

● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi

● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed

- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

OPTIONAL - grad de dificultate: Mediu spre greu: may need Google
● Test 12 - brute force password hacking
- Completează user tomsmith
- Găsește elementul //h4
- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
potențială parolă.
- Folosește o structură iterativă prin care să introduci rând pe rând
parolele și să apeși pe login.
- La final testul trebuie să îmi printeze fie
‘Nu am reușit să găsesc parola’
‘Parola secretă este [parola]’

"""

import unittest
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.implicitly_wait(5)

    def test_1_login_form(self):
        button = self.chrome.find_element(By.XPATH, "//*[@id='content']/ul/li[21]/a")
        button.click()
        current_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'

        assert current_url == expected_url

    def test_2_page_title(self):
        WebDriverWait(self.chrome, 10).until(EC.title_contains("The Internet"))
        title = self.chrome.title
        expected_title = 'The Internet'
        assert title == expected_title

    def test_3_element_xpath_is_corect(self):
        button = self.chrome.find_element(By.XPATH, "//*[@id='content']/ul/li[21]/a")
        button.click()

        element = self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/h2')
        expected_element_text = 'Login Page'
        assert element.text == expected_element_text

    def test_4_login_is_displayed(self):
        element = self.chrome.find_element(By.ID, 'login')
        assert element.is_displayed()

    def test_5_url(self):
        element_href = self.chrome.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')
        status_code = urllib.request.urlopen(element_href).getcode()
        assert status_code == 200

    def test_6_eroare_displayed(self):
        button = self.chrome.find_element(By.XPATH, "//*[@id='content']/ul/li[21]/a")
        button.click()
        button = self.chrome.find_element(By.CLASS_NAME, "fa-sign-in")
        button.click()
        error_element = self.chrome.find_element(By.CLASS_NAME, "error")
        if error_element:
            print(error_element.text)

    def test_7_error_mesage_is_correct(self):
        button = self.chrome.find_element(By.XPATH, "//*[@id='content']/ul/li[21]/a")
        button.click()
        utilizator = self.chrome.find_element(By.ID,"username")
        utilizator.send_keys('Ana')
        parola = self.chrome.find_element(By.ID, "password")
        parola.send_keys('12345')

        button = self.chrome.find_element(By.CLASS_NAME, "fa-sign-in")
        button.click()

        error_element = self.chrome.find_element(By.CLASS_NAME, "error")
        expected_message = 'Your username is invalid!'
        self.assertTrue(expected_message in error_element.text)

    def test_8_eroare_dispare(self):
        button = self.chrome.find_element(By.XPATH, "//*[@id='content']/ul/li[21]/a")
        button.click()
        button = self.chrome.find_element(By.CLASS_NAME, "fa-sign-in")
        button.click()
        error_element = self.chrome.find_element(By.CLASS_NAME, "error")
        error_element.click()
        self.assertFalse(error_element)

    def test_9_label_is_corect(self):
        lista = self.chrome.find_elements(By.XPATH, '//*[@id="login"]/div[1]/div/label', '//*[@id="password"]/div[2]/div/label')
        expected_lista = 'Login'
        expected_lista1 = 'Password'
        self.assertTrue(expected_lista in lista.text)
        self.assertTrue(expected_lista1 in lista.text)

    def test_10_valid_credentials_login(self):
        username = self.chrome.find_element(By.ID, 'username')
        username.send_keys('tomsmith')

        password = self.chrome.find_element(By.ID, 'password')
        password.send_keys('SuperSecretPassword!')

        login_btn = self.chrome.find_element(By.TAG_NAME, 'button')
        login_btn.click()

        self.assertIn('/secure', self.chrome.current_url)

        success_element = WebDriverWait(self.chrome, 4).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="flash success"]')))
        self.assertTrue(success_element.is_displayed())
        self.assertIn('secure area!', success_element.text)

    def test_11_logout_success(self):
        username = self.chrome.find_element(By.ID, 'username')
        username.send_keys('tomsmith')

        password = self.chrome.find_element(By.ID, 'password')
        password.send_keys('SuperSecretPassword!')

        login_btn = self.chrome.find_element(By.TAG_NAME, 'button')
        login_btn.click()

        logout_btn = self.chrome.find_element(By.LINK_TEXT, 'Logout')
        logout_btn.click()

        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, self.chrome.current_url)

    def tearDown(self):)
        self.chrome.quit()


