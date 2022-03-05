from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import custom_log
import logging


class NavigationPanel(SeleniumDriver):

    log = custom_log(logging.DEBUG)

    # Navigation panel
    NAVIGATION_USER_TRIANGLE = (By.XPATH, "//a[@class='dynamic-link']//span[@class='caret']")
    NAVIGATION_HOME = (By.LINK_TEXT, "HOME")
    NAVIGATION_ALL_COURSES = (By.LINK_TEXT, "ALL COURSES")
    NAVIGATION_SUPPORT = (By.LINK_TEXT, "SUPPORT")
    NAVIGATION_MY_COURSES = (By.LINK_TEXT, "MY COURSES")
    NAVIGATION_LOGOUT = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_all_courses(self):
        self.element_click(self.NAVIGATION_ALL_COURSES)

    def click_home(self):
        self.element_click(self.NAVIGATION_HOME)

    def click_support(self):
        self.element_click(self.NAVIGATION_SUPPORT)

    def click_my_courses(self):
        self.element_click(self.NAVIGATION_MY_COURSES)

    def click_logout(self):
        self.element_click(self.NAVIGATION_USER_TRIANGLE)
        self.element_click(self.NAVIGATION_LOGOUT)
