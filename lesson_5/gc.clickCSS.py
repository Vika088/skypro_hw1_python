from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://uitestingplayground.com/classattr')

search_locator_add = ".btn-primary"

button = driver.find_element(By.CSS_SELECTOR, search_locator_add)
button.click()

sleep(4)
