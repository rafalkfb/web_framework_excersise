from selenium.webdriver.common.keys import Keys

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
    _all_courses = "//div[@id='course-list']//div[contains(@class, 'col-lg-4')]//a"  # list of elements
    _enroll_button = "//button[normalize-space()='Enroll in Course']"
    _cc_num = "//input[@name='cardnumber']"  # driver.switch_to.frame(0) ?
    _cc_exp = "//input[@name='exp-date']"  # driver.switch_to.frame(1)
    _cc_cvv = "//input[@name='cvc']"  # driver.switch_to.frame(2)
    _submit_enroll = "//button[contains(@class, 'sp-buy')]"  # driver.switch_to.default_content()
    _enroll_error_message = "//span[normalize-space()='Your card number is incorrect.']"

    def enter_course_name(self, name):
        """
        Go to the courses page, enter into search box any course
        Hit enter
        :param name:
        :return:
        """
        self.driver.get("https://courses.letskodeit.com/courses")

        self.element_send_keys(name + Keys.ENTER, self._search_box, 'xpath')
        time.sleep(2)

    def select_course_to_enroll(self, full_course_name):
        """
        Gets list of elements, search through them to find matching element
        Must be on courses list
        :param full_course_name:
        :return:
        """
        if not self.verify_title_match("All Courses"):
            self.driver.get("https://courses.letskodeit.com/courses")
            self.log.warning("Function select_course_to_enroll wasn't called in the proper page")
        list_of_courses = self.get_element_list(locator=self._all_courses)
        print("list of courses length ", len(list_of_courses))
        for course in list_of_courses:
            if full_course_name in self.get_text(element=course):
                self.element_click(element=course)

    def enter_card_num(self, num):
        """
        Enter numbers to the card number input box
        :param num:
        :return:
        """
        self.driver.switch_to.frame(0)
        self.element_send_keys(num, locator=self._cc_num)
        self.driver.switch_to.default_content()

    def enter_card_exp(self, exp):
        """
        Enter numbers to the card expiration input box
        :param exp:
        :return:
        """
        self.driver.switch_to.frame(1)
        self.element_send_keys(exp, locator=self._cc_exp)
        self.driver.switch_to.default_content()

    def enter_card_cvv(self, cvv):
        """
        Enter numbers to the card cvv input box
        :param cvv:
        :return:
        """
        self.driver.switch_to.frame(2)
        self.element_send_keys(cvv, locator=self._cc_cvv)
        self.driver.switch_to.default_content()

    def click_enroll_submit_button(self):
        """
        Click enroll button
        :return:
        """
        self.element_click(locator=self._enroll_button)

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

    def verify_enroll_failed(self):
        """
        Check if error message is displayed (not only present)
        Need to wait sometimes a little for it to show
        :return:
        """


