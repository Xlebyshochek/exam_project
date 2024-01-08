import time
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    email = "//input[@class='input-text email required']"
    sign_emails = "//*[@id='dwfrm_singleshipping_shippingAddress']/fieldset[1]/div[1]/div[2]/label"
    first_name = "//input[@class='input-text firstName required']"
    last_name = "//input[@class='input-text lastName required']"
    street_address = "//input[@class='input-text address1 required']"
    floor = "//input[@class='input-text address2']"
    zip_code = "//input[@class='input-text zip required']"
    state = "//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state-button']/span[1]"
    state_list = "//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state-menu']"
    city = "//input[@class='input-text required']"
    phone_number = "//input[@class='input-text phone required']"
    billing_btn = "//*[@id='dwfrm_singleshipping_shippingAddress']/fieldset[2]/div/button"

    # GETTERS

    def get_email(self):
        # Returns the clickable WebElement for the email input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_sign_emails(self):
        # Returns the clickable WebElement for the checkbox related to email sign-ups.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.sign_emails)))

    def get_first_name(self):
        # Returns the clickable WebElement for the first name input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        # Returns the clickable WebElement for the last name input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_street_address(self):
        # Returns the clickable WebElement for the street address input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.street_address)))

    def get_floor(self):
        # Returns the clickable WebElement for the floor input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.floor)))

    def get_zip_code(self):
        # Returns the clickable WebElement for the zip code input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_state(self):
        # Returns the clickable WebElement for the state dropdown.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.state)))

    def get_state_list(self):
        # Returns the clickable WebElement for the state dropdown list.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.state_list)))

    def get_city(self):
        # Returns the clickable WebElement for the city input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_phone_number(self):
        # Returns the clickable WebElement for the phone number input field.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_billing_btn(self):
        #  Returns the clickable WebElement for the billing button.
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.billing_btn)))

    # ACTIONS

    def input_email(self):
        # Clears existing content and inputs the email into the email field.
        email_field = self.get_email()
        email_field.clear()  # Clear existing content
        email_field.send_keys("xlebborodinskiy9600@gmail.com")
        print("Filled email field")

    def input_first_name(self):
        # Clears existing content and inputs the first name into the respective field.
        first_name_field = self.get_first_name()
        first_name_field.clear()
        first_name_field.send_keys("Gregory")
        print("Filled first name field")

    def input_last_name(self):
        # Clears existing content and inputs the last name into the respective field.
        last_name_field = self.get_last_name()
        last_name_field.clear()
        last_name_field.send_keys("Malkov")
        print("Filled last name field")

    def input_street_address(self):
        # Clears existing content and inputs the street address into the respective field.
        street_address_field = self.get_street_address()
        street_address_field.clear()
        street_address_field.send_keys("Broad Street")
        print("Filled street address field")

    def input_floor_(self):
        # Clears existing content and inputs the floor into the respective field.
        floor_field = self.get_floor()
        floor_field.clear()
        floor_field.send_keys("1")
        print("Filled floor field")

    def select_state(self):
        # Clicks on the state dropdown and selects a state from the list.
        ActionChains(self.driver).move_to_element(self.get_state()).click().perform()
        (ActionChains(self.driver).move_to_element(self.get_state_list()).send_keys(Keys.ARROW_DOWN).
         send_keys(Keys.ARROW_DOWN).click().perform())
        print("Selected state")

    def input_city_field(self):
        # Clears existing content and inputs the city into the respective field.
        city_field = self.get_city()
        city_field.clear()
        city_field.send_keys("Mooresville")
        print("Filled city field")

    def input_zip_code(self):
        # Clears existing content and inputs the zip code into the respective field.
        zip_code_field = self.get_zip_code()
        zip_code_field.clear()
        zip_code_field.send_keys("35649")
        print("Filled zip code field")

    def input_phone_number(self):
        # Clears existing content and inputs the phone number into the respective field.
        phone_number_field = self.get_phone_number()
        phone_number_field.clear()
        phone_number_field.send_keys("704-663-3800")
        print("Filled phone number field")

    def click_billing_btn(self):
        # Clicks on the continue to billing button.
        ActionChains(self.driver).move_to_element(self.get_billing_btn()).click().perform()
        print("Click continue to billing button")

    # METHODS

    def fill_info(self):
        # Calls the above actions to fill in the entire checkout information and proceed to billing.
        Logger.add_start_step(method="fill_info")
        self.input_email()
        self.input_first_name()
        self.input_last_name()
        self.input_street_address()
        self.input_floor_()
        self.select_state()
        self.input_city_field()
        self.input_zip_code()
        self.input_phone_number()
        self.click_billing_btn()
        print("Successfully filled info")
        time.sleep(10)
        self.driver.quit()
        Logger.add_end_step(self.driver.current_url, method="fill_info")
