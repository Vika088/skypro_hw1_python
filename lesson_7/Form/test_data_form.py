from lesson_7.Form.Pages.DataPage import DataPage
from lesson_7.Form.Pages.DataFields import DataField
from selenium import webdriver

def test_ffa():
    driver = webdriver.Chrome()
    data_page = DataPage(driver)
    data_page.find_fields()
    data_page.fill_in()
    data_page.click_button()

    data_fields = DataField(driver)
    data_fields.find_filled_fields()
    data_fields.get_filled_zip_code()
    data_fields.get_filled_first_name()
    data_fields.get_filled_last_name()
    data_fields.get_filled_address()
    data_fields.get_filled_city()
    data_fields.get_filled_country()
    data_fields.get_filled_email()
    data_fields.get_filled_phone()
    data_fields.get_filled_job_position()
    data_fields.get_filled_company()

    red = "rgba(248, 215, 218, 1)"
    green = "rgba(209, 231, 221, 1)"

    assert red in data_fields.get_filled_zip_code()
    assert green in data_fields.get_filled_first_name()
    assert green in data_fields.get_filled_last_name()
    assert green in data_fields.get_filled_address()
    assert green in data_fields.get_filled_city()
    assert green in data_fields.get_filled_country()
    assert green in data_fields.get_filled_email()
    assert green in data_fields.get_filled_phone()
    assert green in data_fields.get_filled_job_position()
    assert green in data_fields.get_filled_company()



