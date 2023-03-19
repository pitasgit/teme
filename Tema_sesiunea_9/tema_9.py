import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Login(unittest.TestCase):


    def setUp(self):
        base_url = 'https://the-internet.herokuapp.com/'
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.driver.maximize_window()
        form_auth= self.driver.find_element(By.LINK_TEXT, 'Form Authentication')
        form_auth.click()
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


    def test_1(self):

        actual_url = self.driver.current_url

        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual_url, expected, 'Noul URL nu este corect')

    def test_2(self):
        titlu=self.driver.title
        expected_title= "The Internet"
        self.assertEqual(titlu, expected_title, 'nu esti pe pagina corecta')

    def test_3(self):
        xpath_h2= self.driver.find_element(By.XPATH, '//h2').text
        expected_h2 = "Login Page"
        self.assertEqual(xpath_h2,expected_h2, "Elementul h2 nu este corect")
    def test_4(self):
        login_button= self.driver.find_element(By.XPATH, '//button')
        login_button.is_displayed()
    def test_5(self):
        es_href= self.driver.find_element(By.LINK_TEXT, 'Elemental Selenium').text
        expected_es= 'Elemental Selenium'
        self.assertEqual(es_href,expected_es,"Atributul nu este corect")
    def test_6(self):
        empty_login=self.driver.find_element(By.XPATH, "//button")
        empty_login.click()
        error_empty_login=self.driver.find_element(By.CSS_SELECTOR, 'div [class="flash error"]')
        error_empty_login.is_displayed()
    def test_7(self):
        user_insert=self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        user_insert.send_keys('petr')
        pass_insert=self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        pass_insert.send_keys('d21d2')
        sleep(2)
        login=self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login.click()
        sleep(2)
        actual= self.driver.find_element(By.XPATH, '//*[@id="flash-messages"]//following-sibling::div').text
        expected= "Your username is invalid!"
        self.assertTrue(expected in actual, "Error message text is incorrect")
    def test_8(self):
        login = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login.click()
        sleep(2)
        login = self.driver.find_element(By.XPATH, '//a[@class="close"]')
        login.click()
        sleep(2)
    def test_9(self):
        lista_label=self.driver.find_elements(By.XPATH, '//label')
        for label in lista_label:
            print(label.text)
        label_1=self.driver.find_element(By.XPATH, '//label[contains(text(), "Username")]').text
        expect_label_1 = "Username"
        self.assertEqual(label_1,expect_label_1,"nu gasesc username")
        label_2=self.driver.find_element(By.XPATH, '//label[contains(text(), "Password")]').text
        expected_label_2= "Password"
        self.assertEqual(label_2,expected_label_2, "nu gasesc Password")
    def test_10(self):
        user_insert = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        user_insert.send_keys('tomsmith')
        pass_insert = self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        pass_insert.send_keys('SuperSecretPassword!')
        sleep(2)
        login = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login.click()
        sleep(2)
        secure=self.driver.current_url.__contains__("/secure")
        print(secure)
        flash_suc=WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@class="flash success"]')))
        flash_suc.is_displayed()
        area_sec=self.driver.find_element(By.XPATH, '//div[contains(text(), "secure area!")]')
        assert area_sec
    def test_11(self):
        user_insert = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        user_insert.send_keys('tomsmith')
        pass_insert = self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        pass_insert.send_keys('SuperSecretPassword!')
        sleep(2)
        login = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login.click()
        logout= self.driver.find_element(By.LINK_TEXT, 'Logout')
        logout.click()
        sleep(2)
        actual_url = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual_url, expected, 'Noul URL nu este corect')

    def test_12(self):
        user_insert = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        user_insert.send_keys('tomsmith')
        elem_h4=self.driver.find_element(By.XPATH, "//h4")
        print(elem_h4)
# if __name__ == "__main__":
#     unittest.main
