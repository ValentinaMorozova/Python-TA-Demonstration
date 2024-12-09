from selenium.webdriver.common.by import By

from pages.page import Page


class CategoryPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)

    subcategory_items = (By.CLASS_NAME, "sub-category-item")
    product_titles = (By.CLASS_NAME, "product-title")

    def check_category_page_is_opened(self, category):
        self.url += category.lower()
        self.header = category
        if super().check_page_is_opened():
            return True
        self.logger.error("Category page is not opened")
        return False

    def open_subcategory(self, subcategory_name):
        subcategories = self.driver.find_elements(*self.subcategory_items)
        for subcategory in subcategories:
            if subcategory.text == subcategory_name:
                subcategory.click()
                break

    def open_product(self, product_name):
        products = self.driver.find_elements(*self.product_titles)
        for product in products:
            if product.text == product_name:
                product.click()
                break
