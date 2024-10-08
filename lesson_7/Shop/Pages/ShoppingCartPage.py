from selenium.webdriver.common.by import By

class ShoppingCartPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/cart.html')

    def checkout(self):
        self._checkout = self._driver.find_element(By.ID, 'checkout').click()