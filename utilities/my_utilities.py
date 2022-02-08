"""
@package utilities

Helping class
All most commonly used utilities/methods should be implemented in this class

Example:
    name = self.util.get_unique_name()   # if created instance of this class
    name = util.get_unique_name()  # if method is static
"""
import logging
import random
import string
import time
import traceback
from utilities.custom_logger import custom_log


class Util:

    @staticmethod
    def sleep_and_log(sec, info=""):
        """
        Put the program to sleep, additionally it adds logs
        use simple sleep if you don't care about the logs
        :param info:
        :param sec:
        :return: None
        """
        log = custom_log(logging.INFO)
        try:
            log.info("Wait :: " + str(sec) + "seconds for " + info)
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()
            log.error("### Sleep was interrupted")

    @staticmethod
    def get_alpha_numeric(length, mode='letters'):
        """
        Get random string of characters
        :param length:
        :param mode: lower, upper, digits, mix; if other, then letter mix
        :return: random string
        """
        alpha_num = ''
        if mode == 'lower':
            case = string.ascii_lowercase
        elif mode == 'upper':
            case = string.ascii_uppercase
        elif mode == 'digits':
            case = string.digits
        elif mode == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        # need to refresh knowledge about these constructions
        return alpha_num.join(random.choice(case) for i in range(length))

    @staticmethod
    def get_unique_name_list(list_size=15, name_max_size=20):
        """
        Get a list of valid random names (upper and lower letters)
        :param list_size:
        :param name_max_size: each name will have random length starting from 1 to name_max_size
        :return: list with names
        """
        name_list = []
        for i in range(list_size + 1):
            name_list.append(Util.get_alpha_numeric(random.randint(1, name_max_size + 1)))
        return name_list

    @staticmethod
    def verify_list_match(expected_list, actual_list):
        """
        Verify two lists
        Not really necessary to use this function, I've just create it  to remember how to compare lists
        :param expected_list:
        :param actual_list:
        :return: boolean
        """
        # check if this has any logic
        return set(expected_list) == set(actual_list)

    @staticmethod
    def verify_list_contains(expected_list, actual_list):
        """
        Verify if actual_list contains expected_list
        expected_list length should be lower or same size as actual_list
        :param expected_list:
        :param actual_list:
        :return: boolean
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        return True
