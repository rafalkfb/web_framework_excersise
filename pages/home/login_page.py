from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.home.navigation_panel import NavigationPanel
from utilities.custom_logger import custom_log
import logging


class LoginPage(SeleniumDriver):

    # overrides object from SeleniumDriver, so the name will indicate that the error comes from this class
    log = custom_log(logging.DEBUG)

    link_to_login_page = (By.XPATH, "//a[@href='/login']")
    page_email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    login_button = (By.XPATH, "//input[@type='submit']")
    incorrect_credentials_info = (By.XPATH, "//span[contains(text(), 'username or password is invalid')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_link(self):
        self.element_click(self.link_to_login_page)

    def enter_email(self, email):
        self.element_send_keys(email, self.page_email_field)

    def enter_password(self, password):
        self.element_send_keys(password, self.password_field)

    def click_login_button(self):
        self.element_click(self.login_button)

    def login(self, email, password):

        self.click_login_link()
        self.clear_login_fields()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_successful_login(self):
        result = self.is_element_present(NavigationPanel.NAVIGATION_USER_TRIANGLE)
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self.incorrect_credentials_info)
        return result

    def clear_login_fields(self):
        self.get_element(self.page_email_field).clear()
        self.get_element(self.password_field).clear()
