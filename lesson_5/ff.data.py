from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com/login')

username_field = '#username'

username = driver.find_element(By.CSS_SELECTOR, username_field)
username.send_keys('tomsmith')

password_field = '#password'

password = driver.find_element(By.CSS_SELECTOR, password_field)
password.send_keys('SuperSecretPassword!')

login_button = 'button.radius'
log_but = driver.find_element(By.CSS_SELECTOR, login_button)
log_but.click()

sleep(4)

driver.quit()
