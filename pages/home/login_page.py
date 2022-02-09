from base.selenium_driver import *
from base.basepage import BasePage


class LoginPage(BasePage):

    # overrides object from SeleniumDriver, so the name will indicate that the error comes from this class
    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"
    _element_to_verify_login = "//a[@class='dynamic-link']//span[@class='caret']"
    _incorrect_credentials = "//span[contains(text(), 'Your username or password is invalid. Please try again.')]"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='xpath')

    def enter_email(self, email):
        self.element_send_keys(email, locator=self._email_field, locator_type='id')

    def enter_password(self, password):
        self.element_send_keys(password, locator=self._password_field, locator_type='id')

    def click_login_button(self):
        self.element_click(locator=self._login_button, locator_type='xpath')

    def login(self, email, password):

        self.click_login_link()
        self.clear_login_fields()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_successful_login(self):
        result = self.is_element_present(locator=self._element_to_verify_login, locator_type="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self._incorrect_credentials, 'xpath')
        return result

    def clear_login_fields(self):
        self.get_element(locator=self._email_field, locator_type='id').clear()
        self.get_element(locator=self._password_field, locator_type='id').clear()

