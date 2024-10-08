from lesson_7.Shop.Pages.LoginPage import LoginPage
from lesson_7.Shop.Pages.InventoryPage import InventoryPage
from lesson_7.Shop.Pages.ShoppingCartPage import ShoppingCartPage
from lesson_7.Shop.Pages.CheckoutInfo import CheckoutInfoPage
from lesson_7.Shop.Pages.CheckoutOverview import CheckoutOverviewPage
from selenium import webdriver

def test_shopping():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.find_elements()
    login_page.fill_in_and_click()

    inventory_page = InventoryPage(driver)
    inventory_page.choose_cards()

    shopping_cart_page = ShoppingCartPage(driver)
    shopping_cart_page.checkout()

    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_in_and_continue()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.total_label()

    expected_price = '$58.29'

    assert expected_price in checkout_overview_page.total_label()

