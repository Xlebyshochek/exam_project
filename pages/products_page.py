import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class ProductsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    cookies_btn = "//button[@class='tracking-consent-accept']"

    shoes_type_btn = "//*[@id='main']/div[3]/div/dl[1]/a[3]"

    shoes_color_btn = "//*[@id='main']/div[3]/div/dl[2]/dt"
    shoes_color = "//a[@id='swatch-black']"

    shoes_size_btn = "//*[@id='main']/div[3]/div/dl[4]/dt"
    shoes_size = "//a[@id='swatch-8']"

    shoes_price_btn = "//*[@id='main']/div[3]/div/dl[5]/dt"
    shoes_price = "//a[@title='$101 +']"

    shoes_gender_btn = "//*[@id='main']/div[3]/div/dl[6]/dt"
    shoes_gender = "//a[@title='Unisex']"

    sort_by = "//select[@id='grid-sort-header']"

    product_btn = "//*[@id='cf9d3b3e2bd8a6908e42055adb']/div[3]/a"

    # GETTERS

    def get_cookies_btn(self):
        # Returns the WebElement for the "Accept Cookies" button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cookies_btn)))

    def get_shoes_type_btn(self):
        # Returns the WebElement for the shoes type button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_type_btn)))

    def get_shoes_color_btn(self):
        #  Returns the WebElement for the shoes color button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_color_btn)))

    def get_shoes_color(self):
        # Returns the WebElement for a specific color option after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_color)))

    def get_shoes_size_btn(self):
        # Returns the WebElement for the shoes size button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_size_btn)))

    def get_shoes_size(self):
        # Returns the WebElement for a specific size option after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_size)))

    def get_shoes_price_btn(self):
        # Returns the WebElement for the shoes price button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_price_btn)))

    def get_shoes_price(self):
        # Returns the WebElement for a specific price option after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_price)))

    def get_shoes_gender_btn(self):
        # Returns the WebElement for the shoes gender button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_gender_btn)))

    def get_shoes_gender(self):
        # Returns the WebElement for a specific gender option after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_gender)))

    def get_sort_by(self):
        #  Returns the WebElement for the sort by dropdown after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.sort_by)))

    def get_product_btn(self):
        # Returns the WebElement for the first product button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_btn)))

    # ACTIONS

    def click_accept_cookies(self):
        #  Clicks the "Accept Cookies" button.
        self.get_cookies_btn().click()
        print("Click cookies button")

    def click_shoes_type_btn(self):
        # Clicks the shoes type button.
        self.get_shoes_type_btn().click()
        print("Click shoes type button")

    def choose_shoes_color(self):
        #  Clicks the shoes color button and selects a specific color.
        self.get_shoes_color_btn().click()
        self.get_shoes_color().click()
        print("Choose shoes color")

    def choose_shoes_size(self):
        # Chooses a specific size for the shoes using ActionChains.
        ActionChains(self.driver).move_to_element(self.get_shoes_size_btn()).click().perform()
        ActionChains(self.driver).move_to_element(self.get_shoes_size()).click().perform()
        print("Choose shoes size")

    def choose_shoes_price(self):
        # Chooses a specific price range for the shoes using ActionChains.
        ActionChains(self.driver).move_to_element(self.get_shoes_price_btn()).click().perform()
        ActionChains(self.driver).move_to_element(self.get_shoes_price()).click().perform()
        print("Choose shoes price")

    def choose_shoes_gender(self):
        # Chooses a specific gender for the shoes using ActionChains.
        ActionChains(self.driver).move_to_element(self.get_shoes_gender_btn()).click().perform()
        ActionChains(self.driver).move_to_element(self.get_shoes_gender()).click().perform()
        print("Choose shoes gender")

    def sort_by_price(self):
        #  Sorts the products by price using the sort by dropdown and Arrow Down key.
        ActionChains(self.driver).move_to_element(self.get_sort_by()).click().perform()
        ActionChains(self.driver).click(self.get_sort_by()).send_keys(Keys.ARROW_DOWN).click().perform()
        print("Sort product from low to high prices")

    def click_product_btn(self):
        # Scrolls to a specific position and clicks the first product button.
        self.driver.execute_script("window.scrollTo(0, 200)")
        self.get_product_btn().click()
        print("Click product button")

    # METHODS

    def filter_and_choose_product(self):
        # Scrolls to a specific position and clicks the first product button.
        Logger.add_start_step(method="filter_and_choose_product")
        self.get_current_url()
        self.click_accept_cookies()
        self.click_shoes_type_btn()
        self.choose_shoes_color()
        self.choose_shoes_size()
        self.choose_shoes_price()
        self.choose_shoes_gender()
        self.sort_by_price()
        self.click_product_btn()
        time.sleep(1)
        self.get_screenshot()
        self.assert_url(
            "https://www.fila.com/grant-hill-3/1BM01358.html?dwvar_1BM01358_color=001&fromList=Category%3A%20Sneakers%20%26%20Lifestyle&gridposition=1&cgid=men-sneakers")
        print("Successful product selection")
        Logger.add_end_step(self.driver.current_url, method="filter_and_choose_product")
