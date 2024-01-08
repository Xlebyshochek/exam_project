from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class MainPage(Base):
    url = 'https://www.fila.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    close_promo_btn = ("//button[@class='ui-button ui-corner-all ui-widget ui-button-icon-only "
                       "ui-dialog-titlebar-close']")
    shoes_category = "//a[@aria-controls='subnav-shoes']"
    mens_shoes = "//*[@id='subnav-shoes']/div[1]/div[2]/p/a"
    check_word = "//div[@class='results-hits']"

    # GETTERS

    def get_close_promo_btn(self):
        #  Returns the WebElement for the close promo button after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.close_promo_btn)))

    def get_shoes_category(self):
        # Returns the WebElement for the shoes category link after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shoes_category)))

    def get_mens_shoes(self):
        # Returns the WebElement for the men's shoes link under the shoes category after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.mens_shoes)))

    def get_check_word(self):
        # Returns the WebElement for a specific element with class 'results-hits' after waiting for it to be clickable.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.check_word)))

    # ACTIONS

    def click_close_promo_btn(self):
        #  Clicks the close promo button to dismiss any promotional overlay.
        self.get_close_promo_btn().click()
        print("Click to close promo button")

    def move_to_shoes_category(self):
        # Moves the mouse pointer to the shoes category link using ActionChains.
        ActionChains(self.driver).move_to_element(self.get_shoes_category()).perform()
        print("Move to shoes category")

    def click_mens_shoes(self):
        #  Clicks the men's shoes link under the shoes category.
        self.get_mens_shoes().click()
        print("Click on men's shoes category")

    # METHODS

    def go_to_products_page(self):
        # Navigates to the products page
        Logger.add_start_step(method="go_to_products_page")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_close_promo_btn()
        self.move_to_shoes_category()
        self.click_mens_shoes()
        self.assert_url("https://www.fila.com/men-shoes")
        print("Successful navigation to product page")
        Logger.add_end_step(self.driver.current_url, method="go_to_products_page")
