from selenium.webdriver.common.by import By

from pages.page import Page


class ShoppingCartPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)
        self.url += "cart"
        self.header = "Shopping cart"

    terms_of_service_checkbox = (By.ID, 'termsofservice')
    checkout_button = (By.ID, 'checkout')

    def agree_with_terms_of_service(self):
        self.driver.find_element(*self.terms_of_service_checkbox).click()

    def navigate_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
