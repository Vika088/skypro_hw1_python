from selenium.webdriver.common.by import By


class CheckoutOverviewPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')

    def total_label(self):
        self.total_label = self._driver.find_element(By.CLASS_NAME, 'summary_total_label')
        self.total_price = self.total_label.text.strip().replace('Total: ', '')
        print(self.total_price)
        return self.total_price
