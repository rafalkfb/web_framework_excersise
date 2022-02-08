import logging
import time
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import os


class SeleniumDriver:
    # put at this level to capture class name, if put in __init__ it would say that it comes from __init__ in logs
    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        """
        Takes screenshot of the current open web page
        :param result_message:
        :return: None
        """
        # preparation
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshots_directory_path = "../screenshots/"
        relative_file_name = screenshots_directory_path + file_name
        current_directory = os.path.dirname(__file__)  # gives current directory
        final_destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshots_directory_path)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(final_destination_file)
            self.log.info("Screenshot saved to the directory: " + destination_directory)
        except NotADirectoryError:  # verify exceptions, add some more?
            self.log.error("### Exception Occurred while taking screenshot")
            print_stack()

    def get_by_type(self, locator_type='id'):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_title(self):
        return self.driver.title

    def get_element(self, locator, locator_type='id'):

        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator + "    locator type: " + locator_type)
        except NoSuchElementException:
            self.log.info("Element not found with locator: " + locator + "    locator type:" + locator_type)
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + "    locator type: " + locator_type)
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.info("Cannot click on element with locator: " + locator + "    locator type:" + locator_type)
            print_stack()

    def element_send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Send text on element with locator: " + locator + "    locator type:" + locator_type)
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.info("Cannot send text on element with locator: " + locator + "    locator type: " + locator_type)
            print_stack()

    def is_element_present(self, locator, locator_type):

        try:
            self.get_element(locator, locator_type)
            self.log.info('Element found')
            return True
        except NoSuchElementException:
            self.log.info('Element not found')
            return False

    def element_present_check(self, locator, by_type):

        elements = self.driver.find_elements(by_type, locator)
        if len(elements) > 0:
            self.log.info('Element found')
            return True
        else:
            self.log.info('Element not found')
            return False

    def verify_title_contains(self, title: str):
        try:
            if title in self.get_title():
                return True
            else:
                self.log.error("### Given title: " + title + "  does not contains in actual title: " + self.get_title())
                return False
        except:
            self.log.error("### Failed to get page title")
            return False

    def verify_title_match(self, title: str):
        try:
            if title == self.get_title():
                return True
            else:
                self.log.error("### Given title: " + title + "   does not match with actual title: " + self.get_title())
                return False
        except:
            self.log.error("### Failed to get page title")
            return False

    # class ExplicitWaitType:

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.hw = SeleniumDriver(driver)

    def wait_for_element(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):

        element = None
        try:
            self.driver.implicitly_wait(0)  # just in case you need to use this method, do not mix imp and exp ways
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.visibility_of_element_located((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.info("Element not appeared on the web page")
            print_stack()
        self.driver.implicitly_wait(10)  # set up to the default value
        return element
