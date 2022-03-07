import logging
import time
from traceback import print_stack
from configfiles.config_data import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException
from selenium.common.exceptions import TimeoutException
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

    def get_title(self):

        return self.driver.title

    def get_element(self, locator_tuple):

        by_type, locator = locator_tuple
        element = self.driver.find_element(by_type, locator)
        self.log.info("Element found with locator: " + str(locator_tuple))
        return element

    def get_element_list(self, locator_tuple):
        """
        Get elements
        :param locator_tuple:
        :return:
        """
        by_type, locator = locator_tuple
        element = self.driver.find_elements(by_type, locator)
        self.log.info("Element list found with locator: " + str(locator_tuple))
        return element

    def element_click(self, locator_tuple=None, element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locator_type
        :param locator_tuple
        :param element:
        :return:
        """
        if locator_tuple:
            element = self.get_element(locator_tuple)
        element.click()
        self.log.info("Clicked on element with locator: " + str(locator_tuple))

    def element_send_keys(self, data, locator_tuple=None, element=None):
        """
        Get text into an element
        Either provide element or a combination of locator and locator_type
        :param element:
        :param data:
        :param locator_tuple:
        :return:
        """
        if locator_tuple:
            element = self.get_element(locator_tuple)
        element.send_keys(data)
        self.log.info("Send text on element with locator: " + str(locator_tuple))

    def get_text(self, locator_tuple=None, element=None):
        """
        Get 'Text' of an element
        Either provide element or a combination of locator and locator_type
        :param locator_tuple:
        :param element:
        :return:
        """
        if locator_tuple:
            element = self.get_element(locator_tuple)
        text = element.text
        if len(text) == 0:
            text = element.get_attribute("innerText")
        if len(text) != 0:
            self.log.info("Getting text on element :: " + str(locator_tuple))
            self.log.info("The text is :: '" + text + "'")
            text = text.strip()
        return text

    def is_element_present(self, locator_tuple=None, element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        :param locator_tuple:
        :param element:
        :return:
        """
        try:
            if locator_tuple:
                element = self.get_element(locator_tuple)
            if element is not None:
                self.log.info("Element present with locator: " + str(locator_tuple))
                return True
        except (NoSuchElementException, TimeoutException, ElementNotVisibleException):
            self.log.error("Element not present with locator: " + str(locator_tuple))
            return False

    def is_element_displayed(self, locator_tuple=None, element=None):
        """
        Check if element is displayed, not only present
        Either provide element or a combination of locator and locatorType
        :param locator_tuple:
        :param element:
        :return:
        """
        displayed = False
        try:
            if locator_tuple:
                element = self.get_element(locator_tuple)
            if element is not None:
                displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + str(locator_tuple))
            else:
                self.log.warning("Element not displayed with locator: " + str(locator_tuple))
            return displayed
        except (NoSuchElementException, TimeoutException):
            self.log.error("Element not found with locator: " + str(locator_tuple))
            return False

    def element_present_check_by_list(self, locator_tuple):
        by_type, locator = locator_tuple
        elements = self.driver.find_elements(by_type, locator)
        if len(elements) > 0:
            self.log.info('Element found with locator' + str(locator_tuple))
            return True
        else:
            self.log.info('Element not found with locator' + str(locator_tuple))
            return False

    def verify_title_contains(self, title: str):

        if title in self.get_title():
            self.log.info("### Given title: " + title + "  contains in actual title: " + self.get_title())
            return True
        else:
            self.log.error("### Given title: " + title + "  does not contains in actual title: " + self.get_title())
            return False

    def verify_title_match(self, title: str):

        if title == self.get_title():
            self.log.info("### Given title: " + title + "   match with actual title: " + self.get_title())
            return True
        else:
            self.log.error("### Given title: " + title + "   does not match with actual title: " + self.get_title())
            return False

    def scroll_down(self, how_much=-1000):
        """
        Scroll down by default
        To scroll up provide positive value
        :param how_much:
        :return:
        """
        self.driver.execute_script("window.scrollBy(0, {0});".format(how_much))
        self.log.info("Scrolled on the page")

    def get_element_attribute_value(self, attribute, locator_tuple=None, element=None):
        """
        Get value of the attribute of element
        :param attribute:
        :param locator_tuple:
        :param element:
        :return:
        """
        if locator_tuple:
            element = self.get_element(locator_tuple)
        return element.get_attribute(attribute)

    def is_enabled(self, locator_tuple):
        """
        Check if element is enabled
        :param locator_tuple:
        :return:
        """
        element = self.get_element(locator_tuple)
        attribute_value = self.get_element_attribute_value(attribute="disabled", element=element)
        if attribute_value is not None:
            enabled = element.is_enabled()
        else:
            value = self.get_element_attribute_value(attribute="class", element=element)
            self.log.info("Attribute value From Application Web UI :: " + value)
            enabled = not ("disabled" in value)
        if enabled:
            self.log.info("Element :: '" + str(locator_tuple) + "' is enabled")
        else:
            self.log.info("Element :: '" + str(locator_tuple) + "' is not enabled")
        return enabled

    def switch_frame_by_index(self, locator_tuple):
        """
        Get iframe index using element locator inside iframe
        :param locator_tuple:
        :return:
        """
        result = False
        iframe_list = self.get_element_list((By.XPATH, "//iframe"))
        if len(iframe_list) == 0:
            self.log.warning("There are no iframes")
        for i in range(len(iframe_list)):
            self.driver.switch_to.frame(iframe_list[i])  # or i +1 ?
            result = self.is_element_present(locator_tuple)
            if result:
                self.log.info("iframe index is: " + str(iframe_list[i]))
                break
            self.driver.switch_to.default_content()
        return result

    def wait_for_element(self, locator_tuple, timeout=10, poll_frequency=0.5):

        self.driver.implicitly_wait(0)  # just in case you need to use this method, do not mix imp and exp ways
        self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be visible")
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                 ElementNotSelectableException, ])
        element = wait.until(ec.visibility_of_element_located(locator_tuple))
        self.log.info("Element appeared on the web page")

        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)  # set up to the default value
        return element
