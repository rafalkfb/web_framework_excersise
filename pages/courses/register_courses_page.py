from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_log
import logging
from pages.home.navigation_panel import NavigationPanel


class RegisterCoursesPage(SeleniumDriver):
    
    # overrides object from SeleniumDriver, so the name will indicate that the error comes from this class
    log = custom_log(log_level=logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigation_panel = NavigationPanel(driver)

    # locators
    search_box = (By.CSS_SELECTOR, "input#search")  # "//input[@id='search']"
    all_courses = (By.XPATH, "//h4[@class='dynamic-heading' and contains(text(), '{0}')]")
    enroll_button = (By.XPATH, "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']")
    credit_card_num_field = (By.XPATH, "//input[@name='cardnumber']")  # driver.switch_to.frame(0) ?
    credit_card_exp_field = (By.XPATH, "//input[@name='exp-date']")  # driver.switch_to.frame(1)
    credit_card_cvv_field = (By.XPATH, "//input[@name='cvc']")  # driver.switch_to.frame(2)
    submit_button = (By.XPATH, "//button[contains(@class, 'sp-buy')]")  # driver.switch_to.default_content()
    enroll_error_message = (By.XPATH, "//span[normalize-space()='Your card number is invalid.']")

    def enter_course_name(self, name):
        """
        Go to the courses page, enter into search box any course
        Hit enter
        :param name:
        :return:
        """
        self.navigation_panel.click_all_courses()
        self.element_send_keys(name + Keys.ENTER, self.search_box)

    def select_course_to_enroll(self, full_course_name):
        """
        Gets list of elements, search through them to find matching element
        Must be on courses list
        :param full_course_name:
        :return:
        """
        by_type, locator = self.all_courses
        locator = locator.format(full_course_name)
        locator_tuple = (by_type, locator)
        self.element_click(locator_tuple)

    def enter_card_num(self, num):
        """
        Enter numbers to the card number input box
        :param num:
        :return:
        """
        # self.switch_frame_by_index(locator=self.credit_card_num_field)
        self.driver.switch_to.frame(0)
        self.element_send_keys(num, self.credit_card_num_field)
        self.driver.switch_to.default_content()

    def enter_card_exp(self, exp):
        """
        Enter numbers to the card expiration input box
        :param exp:
        :return:
        """
        # self.switch_frame_by_index(locator=self.credit_card_exp_field)
        self.driver.switch_to.frame(1)
        self.element_send_keys(exp, self.credit_card_exp_field)
        self.driver.switch_to.default_content()

    def enter_card_cvv(self, cvv):
        """
        Enter numbers to the card cvv input box
        :param cvv:
        :return:
        """
        # self.switch_frame_by_index(locator=self.credit_card_cvv_field)
        self.driver.switch_to.frame(2)
        self.element_send_keys(cvv, self.credit_card_cvv_field)
        self.driver.switch_to.default_content()

    def click_enroll_submit_button(self):
        """
        Click enroll button
        :return:
        """
        self.element_click(self.enroll_button)

    def enter_credit_card_info(self, num, exp, cvv):
        """
        Entering all card info
        Calling three methods
        :param num:
        :param exp:
        :param cvv:
        :return:
        """
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)

    def enroll_course(self, num="", exp="", cvv=""):
        """
        Click on the enroll button
        Scroll down
        Enter credit card info
        Click Enroll in course button
        :param num:
        :param exp:
        :param cvv:
        :return:
        """
        self.click_enroll_submit_button()
        self.scroll_down()
        self.enter_credit_card_info(num, exp, cvv)
        # self.element_click(locator=self.submit_button)

    def verify_enroll_failed(self):
        """
        Check if error message is displayed (not only present)
        Need to wait sometimes a little for it to show
        :return:
        """
        # error_info = self.wait_for_element(Config.enroll_error_message)
        return self.is_element_displayed(self.enroll_error_message)
