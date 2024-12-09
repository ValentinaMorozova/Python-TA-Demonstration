from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.page import Page


class CheckoutPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)
        self.url += "onepagecheckout"
        self.header = "Checkout"

    blocks = {
        "billing_address": (By.ID, 'opc-billing'),
        "shipping_address": (By.ID, 'opc-shipping'),
        "shipping_method": (By.ID, 'opc-shipping_method'),
        "payment_method": (By.ID, 'opc-payment_method'),
        "payment_info": (By.ID, 'opc-payment_info'),
        "confirm": (By.ID, 'opc-confirm_order')

    }
    block_buttons = {
        "billing_address": (By.CLASS_NAME, 'new-address-next-step-button'),
        "shipping_address": (By.CLASS_NAME, 'new-address-next-step-button'),
        "shipping_method": (By.CLASS_NAME, 'shipping-method-next-step-button'),
        "payment_method": (By.CLASS_NAME, 'payment-method-next-step-button'),
        "payment_info": (By.CLASS_NAME, 'payment-info-next-step-button'),
        "confirm": (By.CLASS_NAME, 'confirm-order-next-step-button')
    }

    def click_button_in_block(self, block):
        try:
            block_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.blocks[block])
            )
            button = WebDriverWait(block_element, 10).until(
                EC.element_to_be_clickable(self.block_buttons[block])
            )
            button.click()
        except TimeoutException:
            self.logger.error(f"Button in block '{block}' was not clicked")
            return False
