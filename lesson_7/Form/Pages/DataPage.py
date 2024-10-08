from selenium.webdriver.common.by import By

class DataPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def find_fields(self):
        self._first_name = (By.NAME, 'first-name')
        self._last_name = (By.NAME, 'last-name')
        self._address = (By.NAME, 'address')
        self._zip_code = (By.NAME, 'zip-code')
        self._city = (By.NAME, 'city')
        self._country = (By.NAME, 'country')
        self._email = (By.NAME, 'e-mail')
        self._phone = (By.NAME, 'phone')
        self._job_position = (By.NAME, 'job-position')
        self._company = (By.NAME, 'company')
        self._button = (By.TAG_NAME, 'button')

    def fill_in(self):
        self._driver.find_element(*self._first_name).send_keys('Иван')
        self._driver.find_element(*self._last_name).send_keys('Петров')
        self._driver.find_element(*self._address).send_keys('Ленина, 55-3')
        self._driver.find_element(*self._zip_code).send_keys('')
        self._driver.find_element(*self._city).send_keys('Москва')
        self._driver.find_element(*self._country).send_keys('Россия')
        self._driver.find_element(*self._email).send_keys('test@skypro.com')
        self._driver.find_element(*self._phone).send_keys('+7985899998787')
        self._driver.find_element(*self._job_position).send_keys('QA')
        self._driver.find_element(*self._company).send_keys('SkyPro')

    def click_button(self):
        self._driver.find_element(*self._button).click()


