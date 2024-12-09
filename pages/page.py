from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver, url, logger):
        self.driver = driver
        self.url = url
        self.logger = logger
        self.header = ""

    header_locator = (By.XPATH, '//h1')

    def check_page_url(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(self.url)
            )
            return True
        except TimeoutException:
            self.logger.error(f"TimeoutException during URL check. "
                              f"Expected URL is: {self.url}, actual URL is: {self.driver.current_url}")
            return False

    def check_page_header(self):
        try:
            header_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.header_locator)
            )
            if header_element.text == self.header:
                return True
            else:
                self.logger.error(f"AssertionError during header check. "
                                  f"Expected header is '{self.header}', actual header is '{header_element.text}'")
                return False
        except TimeoutException:
            self.logger.error("There is no header on the page")
            return False

    def check_page_is_opened(self):
        if self.check_page_url() & self.check_page_header():
            return True
        self.logger.error("Check page URL and header failed")
        return False
