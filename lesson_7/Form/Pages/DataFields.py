from selenium.webdriver.common.by import By

class DataField:

    def __init__(self, driver):
        self._driver = driver

    def find_filled_fields(self):
        self.filled_zip_code = (By.ID, 'zip-code')
        self.filled_first_name = (By.ID, 'first-name')
        self.filled_last_name = (By.ID, 'last-name')
        self.filled_address = (By.ID, 'address')
        self.filled_city = (By.ID, 'city')
        self.filled_country = (By.ID, 'country')
        self.filled_email = (By.ID, 'e-mail')
        self.filled_phone = (By.ID, 'phone')
        self.filled_job_position = (By.ID, 'job-position')
        self.filled_company = (By.ID, 'company')

    def get_filled_zip_code(self):
        return self._driver.find_element(*self.filled_zip_code).value_of_css_property("background-color")

    def get_filled_first_name(self):
        return self._driver.find_element(*self.filled_first_name).value_of_css_property("background-color")

    def get_filled_last_name(self):
        return self._driver.find_element(*self.filled_last_name).value_of_css_property("background-color")

    def get_filled_address(self):
        return self._driver.find_element(*self.filled_address).value_of_css_property("background-color")

    def get_filled_city(self):
        return self._driver.find_element(*self.filled_city).value_of_css_property("background-color")

    def get_filled_country(self):
        return self._driver.find_element(*self.filled_country).value_of_css_property("background-color")

    def get_filled_email(self):
        return self._driver.find_element(*self.filled_email).value_of_css_property("background-color")

    def get_filled_phone(self):
        return self._driver.find_element(*self.filled_phone).value_of_css_property("background-color")

    def get_filled_job_position(self):
        return self._driver.find_element(*self.filled_job_position).value_of_css_property("background-color")

    def get_filled_company(self):
        return self._driver.find_element(*self.filled_company).value_of_css_property("background-color")