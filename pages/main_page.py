from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.page import Page


class MainPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)

    login_link = (By.CLASS_NAME, "ico-login")
    logout_link = (By.CLASS_NAME, "ico-logout")
    cart_link = (By.ID, 'topcartlink')
    cart_qty = (By.CLASS_NAME, 'cart-qty')
    search_field = (By.ID, "small-searchterms")
    search_button = (By.CLASS_NAME, "search-box-button")
    top_menu = (By.CLASS_NAME, "top-menu")
    list_items = (By.XPATH, "//li")

    log_out_text = "Log out"

    def navigate_to_main_page(self):
        self.driver.get(self.url)

    def check_page_is_opened(self):
        if super().check_page_url():
            return True
        self.logger.error("Main page is not opened")
        return False

    def click_login(self):
        self.driver.find_element(*self.login_link).click()

    def check_logged_in(self):
        try:
            logout = self.driver.find_element(*self.logout_link)
            if logout.text == self.log_out_text:
                return True
            else:
                self.logger.error(f"AssertionError during log in check. "
                                  f"Expected text for link is '{self.log_out_text}', actual text is '{logout.text}'")
                return False
        except NoSuchElementException:
            self.logger.error(f"There is no '{self.log_out_text}' link on the main page")
            return False

    def enter_search_term(self, search_text):
        self.driver.find_element(*self.search_field).send_keys(search_text)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def navigate_to_category_from_top_menu(self, category_name):
        top_menu = self.driver.find_element(*self.top_menu)
        categories_list = top_menu.find_elements(*self.list_items)
        for category in categories_list:
            if category.text == category_name.upper():
                category.click()
                break

    def check_shopping_cart_number_of_products(self, expected_number):
        number_of_products = self.get_shopping_cart_number_of_products()
        if number_of_products == expected_number:
            return True
        self.logger.error(f"Unexpected number of products in the shopping cart. "
                          f"Expected number is '{expected_number}', actual number is '{number_of_products}'")
        return False

    def get_shopping_cart_number_of_products(self):
        cart_link = self.driver.find_element(*self.cart_link)
        text_number_of_products = cart_link.find_element(*self.cart_qty).text
        return text_number_of_products[1:-1]

    def navigate_to_shopping_cart(self):
        self.driver.find_element(*self.cart_link).click()
