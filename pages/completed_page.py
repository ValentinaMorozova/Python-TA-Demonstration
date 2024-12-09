from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.page import Page


class CompletedPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)
        self.url += "checkout/completed"
        self.header = "Thank you"

    completed_message = (By.CLASS_NAME, "order-completed")
    completed_message_title = (By.CLASS_NAME, "title")
    completed_message_text = "Your order has been successfully processed!"

    def check_success_message(self):
        try:
            message = self.driver.find_element(*self.completed_message)
            message_title = message.find_element(*self.completed_message_title)
            if message_title.text == self.completed_message_text:
                return True
            else:
                self.logger.error(f"AssertionError during success message check. "
                                  f"Expected text is '{self.completed_message_text}', actual text is '{message_title.text}'")
                return False
        except NoSuchElementException:
            self.logger.error("No success message appeared on the completed page")
            return False
