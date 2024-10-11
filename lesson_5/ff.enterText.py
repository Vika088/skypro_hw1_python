from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com/inputs')

search_locator = 'input[type="number"]'

field = driver.find_element(By.CSS_SELECTOR, search_locator)
field.send_keys('1000')

sleep(4)

field.clear()
field.send_keys('999')

sleep(4)

driver.quit()
