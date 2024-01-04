import re
import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # DEFINE METHODS

    def get_current_url(self):
        # Print the current URL of the web page.
        print("Current url " + self.driver.current_url)

    def assert_word(self, web_name, input_name):
        # Assert whether the product name on the web page matches the expected input name.
        if isinstance(web_name, str):
            assert web_name == input_name
            print("Product name match")
        else:
            name_value = web_name.text
            assert name_value == input_name
            print("Product name match")

    def assert_price(self, web_price, input_price):
        # Assert whether the product price on the web page matches the expected input price.
        if isinstance(web_price, str):
            assert web_price == input_price
            print("Product price match")
        else:
            price_value = web_price.text
            assert price_value == input_price
            print("Product price match")

    def assert_size(self, web_size, input_size):
        # Assert whether the product size on the web page matches the expected input size.
        if isinstance(web_size, str):
            assert web_size == input_size
            print("Product size match")
        else:
            size_value = web_size.text
            assert size_value == input_size
            print("Product size match")

    def assert_color(self, web_color, input_color):
        # Assert whether the product color on the web page matches the expected input color.
        if isinstance(web_color, str):
            assert web_color == input_color
            print("Product color match")
        else:
            size_value = web_color.text
            assert size_value == input_color
            print("Product color match")

    def assert_url(self, input_url):
        # Assert whether the current URL matches the provided input URL.
        assert self.driver.current_url == input_url
        print("Success check URL")

    def get_screenshot(self):
        # Capture a screenshot of the current web page and save it with a timestamped filename.
        now_time = datetime.datetime.today().strftime('%Y.%m.%d-%H:%M:%S')
        now_time = re.sub(r'[^\w\-_.]', '_', now_time)
        self.driver.save_screenshot(f'/Users/xlebb/PycharmProjects/exam_project/screenshots/{now_time}.png')
