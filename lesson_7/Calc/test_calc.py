from lesson_7.Calc.MainPage import MainPage
from selenium import webdriver

def test_calc():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)

    main_page.delay()

    main_page.find_elements()
    main_page.click_elements()
    main_page.wait()
    main_page.result()

    expected_result = '15'

    assert expected_result in main_page.result()

