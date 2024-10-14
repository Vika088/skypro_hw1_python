from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')

    def choose_cards(self):
        self.backpack = self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.tshort = self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.onesie = self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
