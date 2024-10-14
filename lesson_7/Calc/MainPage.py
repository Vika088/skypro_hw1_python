from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def delay(self):
        self._find_delay = (By.ID, 'delay')
        self._clear_delay = self._driver.find_element(*self._find_delay).clear()
        self._send_delay = self._driver.find_element(*self._find_delay).send_keys('45')

    def find_elements(self):
        self.seven = (By.XPATH, "//span[normalize-space()='7']")
        self.plus = (By.XPATH, "//span[normalize-space()='+']")
        self.eight = (By.XPATH, "//span[normalize-space()='8']")
        self.equal = (By.XPATH, "//span[normalize-space()='=']")

    def click_elements(self):
        self.click_seven = self._driver.find_element(*self.seven).click()
        self.click_plus = self._driver.find_element(*self.plus).click()
        self.click_eight = self._driver.find_element(*self.eight).click()
        self.click_equal = self._driver.find_element(*self.equal).click()

    def wait(self):
        self._wait = WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((
            By.CLASS_NAME, 'screen'), '15'))

    def result(self):
        return self._driver.find_element(By.CLASS_NAME, 'screen').text
