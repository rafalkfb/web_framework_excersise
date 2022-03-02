from base.selenium_driver import *
from configfiles.config_data import Config


class NavigationPanel(SeleniumDriver):

    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_all_courses(self):
        self.element_click(Config.NAVIGATION_ALL_COURSES)

    def click_home(self):
        self.element_click(Config.NAVIGATION_HOME)

    def click_support(self):
        self.element_click(Config.NAVIGATION_SUPPORT)

    def click_my_courses(self):
        self.element_click(Config.NAVIGATION_MY_COURSES)
