from selenium import webdriver
from selenium.webdriver.common.by import By


def test_fill_form():
    driver = webdriver.Chrome()

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    driver.find_element(By.NAME, "first-name").send_keys('Иван')

    driver.find_element(By.TAG_NAME, 'button').click()
    assert driver.find_element(By.ID, 'first-name').value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
