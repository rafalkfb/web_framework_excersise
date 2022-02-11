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

    def get_by_type(self, locator_type='xpath'):
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
            self.log.error("Locator type " + locator_type + " not correct/supported")
        return False

    def get_title(self):
        return self.driver.title

    def get_element(self, locator, locator_type='xpath'):

        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator)
        except NoSuchElementException:
            self.log.error("Element not found with locator: " + locator)
        return element

    def get_element_list(self, locator, locator_type="xpath"):
        """
        Get elements
        :param locator:
        :param locator_type:
        :return:
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator)
        except NoSuchElementException:
            self.log.error("Element list not found with locator: " + locator)
        return element

    def element_click(self, locator="", locator_type="xpath", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locator_type
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:  # if locator is empty, means element should be already provided
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator)
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, TimeoutException):
            self.log.error("Cannot click on element with locator: " + locator)
            print_stack()

    def element_send_keys(self, data, locator="", locator_type="xpath", element=None):
        """
        Get text into an element
        Either provide element or a combination of locator and locator_type
        :param element:
        :param data:
        :param locator:
        :param locator_type:
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Send text on element with locator: " + locator)
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error("Cannot send text on element with locator: " + locator)
            print_stack()

    def get_text(self, locator="", locator_type="xpath", element=None, info=""):
        """
        Get 'Text' of an element
        Either provide element or a combination of locator and locator_type
        :param locator:
        :param locator_type:
        :param element:
        :param info:
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info + " locator: " + locator)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def is_element_present(self, locator="", locator_type="xpath", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator)
                return True
        except NoSuchElementException:
            self.log.error("Element not present with locator: " + locator)
            return False

    def is_element_displayed(self, locator="", locator_type="xpath", element=None):
        """
        Check if element is displayed, not only present
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator)
            else:
                self.log.warning("Element not displayed with locator: " + locator)
            return displayed
        except (NoSuchElementException, TimeoutException):
            self.log.error("Element not found with locator: " + locator)
            return False

    def element_present_check(self, locator, by_type):

        elements = self.driver.find_elements(by_type, locator)
        if len(elements) > 0:
            self.log.info('Element found with locator' + locator)
            return True
        else:
            self.log.info('Element not found with locator' + locator)
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

    def scroll_down(self, how_much=-1000):
        """
        Scroll down by default
        To scroll up provide positive value
        :param how_much:
        :return:
        """
        self.driver.execute_script("window.scrollBy(0, {0});".format(how_much))

    # class ExplicitWaitType:

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.hw = SeleniumDriver(driver)

    def wait_for_element(self, locator, locator_type='xpath', timeout=10, poll_frequency=0.5):

        element = None
        try:
            self.driver.implicitly_wait(0)  # just in case you need to use this method, do not mix imp and exp ways
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,])
            element = wait.until(ec.visibility_of_element_located((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, TimeoutException):
            self.log.info("Element not appeared on the web page")
            print_stack()
        self.driver.implicitly_wait(10)  # set up to the default value
        return element
