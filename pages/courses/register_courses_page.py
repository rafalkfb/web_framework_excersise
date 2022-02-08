from base.selenium_driver import *
from base.basepage import BasePage
from selenium import webdriver  # delete after tests

from pages.home.login_page import LoginPage


class RegisterCoursesPage(BasePage):
    
    # overrides object from SeleniumDriver, so the name will indicate that the error comes from this class
    log = cl.custom_log(log_level=logging.DEBUG)
    
    def __init__(self, driver):
        super(RegisterCoursesPage, self).__init__(driver)

    _search_box = "//input[@id='search']"
    _course = ""
    _all_courses = "//div[@id='course-list']//div[contains(@class, 'col-lg-4')]"  # list of elements
    _enroll_button = "//button[normalize-space()='Enroll in Bundle']"
    _cc_num = "//input[@name='cardnumber']"  # driver.switch_to.frame(0) ?
    _cc_exp = "//input[@name='exp-date']"  # driver.switch_to.frame(1)
    _cc_cvv = "//input[@name='cvc']"  # driver.switch_to.frame(2)
    _submit_enroll = "//button[contains(@class, 'sp-buy')]"  # driver.switch_to.default_content()
    _enroll_error_message = "//span[normalize-space()='Your card number is incorrect.']"

    def enter_course_name(self, name):
        """
        Go to the courses page, enter into search box any course
        :param name:
        :return:
        """
        self.driver.get("https://courses.letskodeit.com/courses")

        self.element_send_keys(name, self._search_box, 'xpath')
        time.sleep(2)

    def select_course_to_enroll(self, full_course_name):
        """

        :param full_course_name:
        :return:
        """

    def enter_card_num(self, num):
        """

        :param num:
        :return:
        """

    def enter_card_exp(self, exp):
        """

        :param exp:
        :return:
        """

    def enter_card_cvv(self, cvv):
        """

        :param cvv:
        :return:
        """

    def click_enroll_submit_button(self):
        """

        :return:
        """

    def enter_credit_card_info(self, num, exp, cvv):
        """
        Entering all card info
        Calling three methods
        :param num:
        :param exp:
        :param cvv:
        :return:
        """

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

    def verify_enroll_failed(self):
        """
        Check if error message is displayed (not only present)
        Need to wait sometimes a little for it to show
        :return:
        """


