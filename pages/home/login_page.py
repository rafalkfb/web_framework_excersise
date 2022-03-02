from base.selenium_driver import *
from configfiles.config_data import Config


class LoginPage(SeleniumDriver):

    # overrides object from SeleniumDriver, so the name will indicate that the error comes from this class
    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_link(self):
        self.element_click(Config.LINK_TO_LOGIN_PAGE)

    def enter_email(self, email):
        self.element_send_keys(email, Config.LOGIN_PAGE_EMAIL_FIELD)

    def enter_password(self, password):
        self.element_send_keys(password, Config.LOGIN_PAGE_PASSWORD_FIELD)

    def click_login_button(self):
        self.element_click(Config.LOGIN_PAGE_LOGIN_BUTTON)

    def login(self, email, password):

        self.click_login_link()
        self.clear_login_fields()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_successful_login(self):
        result = self.is_element_present(Config.NAVIGATION_USER_TRIANGLE)
        return result

    def verify_login_failed(self):
        result = self.is_element_present(Config.LOGIN_PAGE_INCORRECT_CREDENTIALS_INFO)
        return result

    def clear_login_fields(self):
        self.get_element(Config.LOGIN_PAGE_EMAIL_FIELD).clear()
        self.get_element(Config.LOGIN_PAGE_PASSWORD_FIELD).clear()

