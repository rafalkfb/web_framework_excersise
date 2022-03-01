from base.selenium_driver import *
from base.basepage import BasePage


class LoginPage(SeleniumDriver):

    # overrides object from SeleniumDriver, so the name will indicate that the error comes from this class
    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_link = (By.XPATH, "//a[@href='/login']")
    _email_field = (By.ID, "email")
    _password_field = (By.ID, "password")
    _login_button = (By.XPATH, "//input[@type='submit']")
    _element_to_verify_login = (By.XPATH, "//a[@class='dynamic-link']//span[@class='caret']")
    _incorrect_credentials = (By.XPATH, "//span[contains(text(), 'Your username or password is invalid')]")

    def click_login_link(self):
        self.element_click(self._login_link)

    def enter_email(self, email):
        self.element_send_keys(email, self._email_field)

    def enter_password(self, password):
        self.element_send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button)

    def login(self, email, password):

        self.click_login_link()
        self.clear_login_fields()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_successful_login(self):
        result = self.is_element_present(self._element_to_verify_login)
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self._incorrect_credentials)
        return result

    def clear_login_fields(self):
        self.get_element(self._email_field).clear()
        self.get_element(self._password_field).clear()

