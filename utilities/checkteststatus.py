"""
@package utilities

CheckTestStatus class implementation
It provides functionality to assert the result

If you want only one assert in test case, use mark_final (or skip this class)
if you want to check multiple asserts in one test case use mark methods and as last check use mark_final

Example:
    test_status = CheckTestStatus(driver)
    self.test_status.mark_final("Test Name", result, "Message")
"""
import logging
from traceback import print_stack

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class CheckTestStatus(SeleniumDriver):
    # overrides for naming
    log = cl.custom_log(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits CheckTestStatus class
        :param driver:
        """
        super(CheckTestStatus, self).__init__(driver)
        self.result_list = []

    def __set_result(self, result, result_message):
        """
        Set result to the list
        takes screenshots (method from SeleniumDriver class) on test failure
        :param result:
        :param result_message: message if something negative happens
        :return: None
        """
        try:
            if result:
                self.result_list.append("PASS")
                self.log.info("### VERIFICATION SUCCESSFUL :: ")
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + result_message)
                self.screen_shot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception Occurred !!! :: " + result_message)
            self.screen_shot(result_message)
            print_stack()

    # this method is simple right now and seems not necessary, will be improved later
    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        :param result:
        :param result_message:
        :return:
        """
        self.__set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        :param test_name:
        :param result:
        :param result_message:
        :return:
        """
        self.__set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(test_name + "### TEST FAILED")
            self.result_list.clear()
            assert False
        else:
            self.log.info(test_name + "### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True
