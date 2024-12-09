from selenium.webdriver.common.by import By

from pages.page import Page


class LoginPage(Page):
    def __init__(self, driver, url, logger):
        super().__init__(driver, url, logger)
        self.url += "login"
        self.header = "Welcome, Please Sign In!"

    email_field = (By.ID, "Email")
    password_field = (By.ID, "Password")
    login_button = (By.CLASS_NAME, "login-button")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
