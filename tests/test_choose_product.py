from selenium import webdriver
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options, service=service)


def test_buy_product(notification):

    # Creating an instance of the MainPage class to navigate to the products page.
    main_page = MainPage(driver)
    main_page.go_to_products_page()

    # Creating an instance of the ProductsPage class to filter and choose a product.
    products_page = ProductsPage(driver)
    products_page.filter_and_choose_product()

    # Creating an instance of the ProductPage class to navigate to the cart page.
    product_page = ProductPage(driver)
    product_page.go_to_cart_page()

    # Creating an instance of the CartPage class to navigate to the checkout page.
    cart_page = CartPage(driver)
    cart_page.go_to_checkout_page()

    # Creating an instance of the CheckoutPage class to fill in the checkout information.
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info()


