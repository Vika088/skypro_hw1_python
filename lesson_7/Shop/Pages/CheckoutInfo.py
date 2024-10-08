from selenium.webdriver.common.by import By

class CheckoutInfoPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')

    def fill_in_and_continue(self):
        self.first_name = self._driver.find_element(By.ID, 'first-name').send_keys('Vika')
        self.last_name = self._driver.find_element(By.ID, 'last-name').send_keys('Danilova')
        self.postal_code = self._driver.find_element(By.ID, 'postal-code').send_keys('170026')
        self.continuebut = self._driver.find_element(By.ID, 'continue').click()
