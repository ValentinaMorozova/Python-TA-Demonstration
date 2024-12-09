from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.page import Page


class ProductPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)

    add_to_cart_button = (By.CLASS_NAME, "add-to-cart-button")
    bar_notification = (By.ID, 'bar-notification')
    bar_success_text = "The product has been added to your shopping cart"

    def check_product_page_is_opened(self, product):
        self.header = product
        if super().check_page_header():
            return True
        self.logger.error("Check product page header failed")
        return False

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def check_success_bar_notification(self):
        try:
            bar = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.bar_notification)
            )
            if bar.get_attribute("class") != "bar-notification success":
                self.logger.error("There is no success notification bar")
                return False
            if bar.text.strip() != self.bar_success_text:
                self.logger.error(f"AssertionError during notification bar text check. "
                                  f"Expected text is '{self.bar_success_text}', actual text is '{bar.text}'")
                return False
            return True
        except TimeoutException:
            self.logger.error("There is no notification bar on the product page")
            return False
