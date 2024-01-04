from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    size_btn = "//a[@title='8']"
    add_to_bag_btn = "//button[@id='add-to-cart']"
    bag_btn = "//button[@class='checkout']"

    # GETTERS

    def get_size_btn(self):
        # Returns the clickable WebElement for selecting a size.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.size_btn)))

    def get_add_to_bag_btn(self):
        # Returns the clickable WebElement for the "Add to Bag" button.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.add_to_bag_btn)))

    def get_view_bag_btn(self):
        #  Returns the clickable WebElement for the "Move to Bag" button.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.bag_btn)))

    # ACTIONS

    def click_size_btn(self):
        #  Clicks on the size button to choose a specific size.
        self.get_size_btn().click()
        print("Click on size button")

    def click_add_to_bag_btn(self):
        #  Clicks on the "Add to Bag" button after ensuring the size button is stale (no longer valid).
        WebDriverWait(self.driver, 15).until(EC.staleness_of(self.get_size_btn()))
        self.get_add_to_bag_btn().click()
        print("Click on add to bag button")

    def click_cart_btn(self):
        # Clicks on the "Move to Bag" button to proceed to the cart.
        self.get_view_bag_btn().click()
        print("Click on cart button")

    # METHODS

    def go_to_cart_page(self):
        #  Navigates to the cart page
        self.get_current_url()
        self.assert_word("001 BLACK / BLACK / BLACK", "001 BLACK / BLACK / BLACK")
        self.click_size_btn()
        self.click_add_to_bag_btn()
        self.click_cart_btn()
        self.assert_url("https://www.fila.com/shopping-cart")
        self.get_screenshot()
        print("Successful navigation to cart page")
