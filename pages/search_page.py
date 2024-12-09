from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.page import Page


class SearchPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)
        self.url += "search"
        self.header = "Search"

    search_results = (By.CLASS_NAME, "search-results")
    item_box = (By.CLASS_NAME, "item-box")
    advanced_search_block = (By.ID, "advanced-search-block")
    advanced_search_checkbox = (By.ID, "As")
    category_dropdown = (By.ID, "Cid")
    price_from_field = (By.ID, "Pf")
    price_to_field = (By.ID, "Pt")
    search_button = (By.CLASS_NAME, "search-button")
    product_title = (By.CLASS_NAME, "product-title")

    def open_advanced_search(self):
        block = self.driver.find_element(*self.advanced_search_block)
        if block.get_attribute('style') == "display: none;":
            self.driver.find_element(*self.advanced_search_checkbox).click()

    def check_advanced_search_is_opened(self):
        block = self.driver.find_element(*self.advanced_search_block)
        if block.get_attribute('style') == "display: block;":
            return True
        self.logger.error("Check advanced search failed")
        return False

    def select_category(self, category):
        dropdown = self.driver.find_element(*self.category_dropdown)
        Select(dropdown).select_by_visible_text(category)

    def set_price_range(self, price_from, price_to):
        self.driver.find_element(*self.price_from_field).send_keys(price_from)
        self.driver.find_element(*self.price_to_field).send_keys(price_to)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def check_number_of_products(self, expected_number):
        number_of_products = self.get_number_of_products()
        if number_of_products == int(expected_number):
            return True
        self.logger.error(f"Unexpected number of products on the search page. "
                          f"Expected number is {expected_number}, actual number is {number_of_products}")
        return False

    def get_number_of_products(self):
        try:
            search_results = self.driver.find_element(*self.search_results)
            products_number = search_results.find_elements(*self.item_box)
            return len(products_number)
        except NoSuchElementException:
            self.logger.error("There is no products on the search page")
            return 0

    def check_first_product_title(self, expected_title):
        title = self.get_first_product_title()
        if title == expected_title:
            return True
        self.logger.error(f"Unexpected title of the first product on the search page. "
                          f"Expected title is {expected_title}, actual title is {title}")
        return False

    def get_first_product_title(self):
        try:
            product = self.driver.find_elements(*self.item_box)[0]
            return product.find_element(*self.product_title).text
        except NoSuchElementException:
            self.logger.error("There is no products on the search page")
            return ""
