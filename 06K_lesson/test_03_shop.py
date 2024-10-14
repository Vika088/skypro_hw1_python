from selenium import webdriver
from selenium.webdriver.common.by import By

def test_fill_form():
    driver = webdriver.Chrome()

    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')

    driver.find_element(By.ID, 'password').send_keys('secret_sauce')

    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys('Vika')
    driver.find_element(By.ID, 'last-name').send_keys('Danilova')
    driver.find_element(By.ID, 'postal-code').send_keys('170026')
    driver.find_element(By.ID, 'continue').click()
    total_label = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    total_price = total_label.strip().replace('Total: ', '')
    print(total_price)
    driver.quit()
    assert total_price == '$58.29'





