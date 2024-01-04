from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    product_name = "//a[@title='Grant Hill 3']"
    product_color = "//*[@id='cart-table']/tbody/tr/td[2]/div[1]/div[3]/div[2]/span[2]"
    product_size = "//*[@id='cart-table']/tbody/tr/td[2]/div[1]/div[3]/div[1]/span[2]"
    product_price = "//*[@id='cart-table']/tbody/tr/td[5]/span"
    checkout_btn = "//button[@class='button-fancy-large']"
    check_word = "//*[@id='primary']/h1"

    # GETTERS

    def get_product_name(self):
        #  Returns the clickable WebElement for the product name.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_color(self):
        # Returns the clickable WebElement for the product color.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_color)))

    def get_product_size(self):
        #  Returns the clickable WebElement for the product size.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_size)))

    def get_product_price(self):
        # Returns the clickable WebElement for the product price.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_checkout_btn(self):
        # Returns the clickable WebElement for the checkout button.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))

    def get_check_word(self):
        # Waits for the presence of a specific element.
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.check_word)))

    # ACTIONS
    def click_checkout_btn(self):
        # Clicks on the checkout button.
        self.get_checkout_btn().click()

    # METHODS

    def go_to_checkout_page(self):
        #  Navigates to the checkout page
        self.get_current_url()
        self.assert_word(self.get_product_name(), "Grant Hill 3")
        self.assert_color("blk/blk/blk", "blk/blk/blk")
        self.assert_size(self.get_product_size(), "8")
        self.assert_price(self.get_product_price(), '$118.00')
        self.click_checkout_btn()
        self.assert_word("Checkout", "Checkout")
        self.get_screenshot()
        print("Successful navigation to checkout page")
