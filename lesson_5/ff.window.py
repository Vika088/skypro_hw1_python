from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/entry_ad')

sleep(4)

search_locator = '.modal-footer'

button = driver.find_element(By.CSS_SELECTOR, search_locator)
button.click()

sleep(4)

driver.quit()
