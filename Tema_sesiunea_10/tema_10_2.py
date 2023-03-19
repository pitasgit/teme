import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


# from selenium.webdriver import ActionChains


class Keyboard(unittest.TestCase):
    KEY = (By.XPATH, "//div/li[9]/a")
    FULL_NAME = (By.ID, "name")
    BUTTON = (By.ID, "button")
    AD_ELEMENT = (By.LINK_TEXT, 'Entry Ad')
    KEYPRESS = (By.LINK_TEXT, "Key Presses")
    TARGET = (By.ID, "target")
    DIGEST = (By.XPATH, '//*[@id="content"]/ul/li[8]/a')
    USERNAME = 'admin'
    PASSWORD = 'admin'
    RESULT = (By.CSS_SELECTOR, "#content > div > p")

    def setUp(self):
        self.mozilla = webdriver.Firefox()
        self.mozilla.maximize_window()
        self.mozilla.implicitly_wait(3)

    def tearDown(self):
        self.mozilla.quit()

    def test_keys(self):
        self.mozilla.get("https://formy-project.herokuapp.com/")
        self.mozilla.find_element(*self.KEY).click()
        sleep(2)
        self.mozilla.find_element(*self.FULL_NAME).send_keys("Petre Ungureanu")
        sleep(2)
        self.mozilla.find_element(*self.BUTTON).click()

    def test_alert(self):
        self.mozilla.get('https://the-internet.herokuapp.com/')
        self.mozilla.find_element(*self.KEYPRESS).click()
        tasta_apasata = self.mozilla.find_element(*self.TARGET)
        tasta_apasata.send_keys(Keys.SHIFT)
        sleep(2)

    def test_auth_digest(self):
        self.mozilla.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/digest_auth')

        sleep(3)
        confirm_message = self.mozilla.find_element(*self.RESULT).text
        self.assertEqual(confirm_message, "Congratulations! You must have the proper credentials.")

    # def test_alerta(self):
    #     self.mozilla.get('https://the-internet.herokuapp.com/')
    #
    #     self.mozilla.find_element(*self.AD_ELEMENT).click()
    #     sleep(3)
    #     obj = self.mozilla.switch_to.alert
    #     sleep(2)
    #     obj.dismiss()
    #     oself.mozilla.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p').click()
    #     sleep(2)
