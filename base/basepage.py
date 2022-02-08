"""
@package base

Base Page class implementation
It implements methods which are common to all pages throughout the application, but not generic to every web page

This class needs to be inherited by all the pages classes
This class should not be used to create objects by itself

Example:
    class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
# from traceback import print_stack
# from utilities.my_utilities import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        :param driver:
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        # self.util = Util()
