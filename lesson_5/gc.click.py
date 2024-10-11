from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

search_locator_add = "button[onclick='addElement()']"

for x in range(5):
    button_add = driver.find_element(By.CSS_SELECTOR, search_locator_add)
    button_add.click()

sleep(4)

search_locator_delete = '.added-manually'

delete_buttons = driver.find_elements(By.CSS_SELECTOR, search_locator_delete)

print(len(delete_buttons))

driver.quit()
