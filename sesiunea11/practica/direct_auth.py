import unittest

import time
from selenium import webdriver


class AuthenticationInFirefox(unittest.TestCase):

    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(3)

    def tearDown(self) -> None:
        self.firefox.quit()

    def test_auth(self):
        # daca intram pe link-ul dat, vedem o casuta in care sa introducem username si parola
        # in loc sa le introducem acolo, putem sa le introducem direct in link
        # https://admin:admin@the-internet.herokuapp.com/basic_auth

        username = 'admin'
        password = 'admin'

        self.firefox.get(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth")
        time.sleep(2)