from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    def find_elements(self):
        self._find_username = (By.ID, 'user-name')
        self._find_password = (By.ID, 'password')
        self._find_logbut = (By.ID, 'login-button')

    def fill_in_and_click(self):
        self.username = self._driver.find_element(*self._find_username).send_keys('standard_user')
        self.password = self._driver.find_element(*self._find_password).send_keys('secret_sauce')
        self.logbut = self._driver.find_element(*self._find_logbut).click()
