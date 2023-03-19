import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


class Authentication(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'
    AUTH_CONFIRM_MESSAGE = (By.XPATH, '//div[@class="example"]/p')

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self):
        self.chrome.quit()

    def test_basic_auth(self):
        # url-ul pe care il accesam in mod normal este https://the-internet.herokuapp.com/basic_auth
        # dar ne putem autentifica direct folosind sintaxa https://user:pass@the-internet.herokuapp.com/basic_auth
        # pe pagina asta ne-am autentifica cu https://admin:admin@the-internet.herokuapp.com/basic_auth

        self.chrome.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        # self.chrome.get(f'https://{self.USERNAME}:{self.PASSWORD}@the-internet.herokuapp.com/basic_auth')

        sleep(3)
        confirm_message = self.chrome.find_element(*self.AUTH_CONFIRM_MESSAGE).text
        self.assertEqual(confirm_message, "Congratulations! You must have the proper credentials.")
