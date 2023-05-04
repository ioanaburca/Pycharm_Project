import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Alerts(unittest.TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/javascript_alerts')
        self.chrome.implicitly_wait(5)

    def test_js_alert(self):
        # identific butonul cu js alert
        button = self.chrome.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        button.click()

        js_alert = self.chrome.switch_to.alert
        js_alert.accept()

        expected = 'You successfully clicked an alert'

        js_alert_text = self.chrome.find_element(By.ID, 'result')
        actual = js_alert_text.text

        self.assertEqual(expected, actual)

    def test_js_confirm_accept(self):
        # identific butonul cu js confirm
        button = self.chrome.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        button.click()

        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()

        expected = 'You clicked: Ok'

        js_confirm_text = self.chrome.find_element(By.ID, 'result')
        actual = js_confirm_text.text

        self.assertEqual(expected, actual)

    def test_js_confirm_cancel(self):
        # identific butonul cu js confirm
        button = self.chrome.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
        button.click()

        js_confirm = self.chrome.switch_to.alert
        js_confirm.dismiss()

        expected = 'You clicked: Cancel'

        js_confirm_text = self.chrome.find_element(By.ID, 'result')
        actual = js_confirm_text.text

        self.assertEqual(expected, actual)

    def test_js_prompt_accept_no_text_inserted(self):
        # identific butonul cu js prompt
        button = self.chrome.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        button.click()

        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()

        expected = 'You entered:'

        js_confirm_text = self.chrome.find_element(By.ID, 'result')
        actual = js_confirm_text.text

        self.assertEqual(expected, actual)

    def test_js_prompt_accept_text_inserted(self):
        # identific butonul cu js prompt
        button = self.chrome.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        button.click()

        js_confirm = self.chrome.switch_to.alert

        js_confirm.send_keys("test")

        js_confirm.accept()

        expected = 'You entered: test'

        js_confirm_text = self.chrome.find_element(By.ID, 'result')
        actual = js_confirm_text.text

        self.assertEqual(expected, actual)

    def test_js_prompt_cancel_no_text_inserted(self):
        # identific butonul cu js prompt
        button = self.chrome.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
        button.click()

        js_confirm = self.chrome.switch_to.alert
        js_confirm.dismiss()

        expected = 'You entered: null'
