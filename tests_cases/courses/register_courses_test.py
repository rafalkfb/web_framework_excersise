import time

import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.login_page import LoginPage
import unittest
from utilities.checkteststatus import CheckTestStatus


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.courses_url = "https://courses.letskodeit.com/courses"
        self.log_page = LoginPage(self.driver)
        self.log_page.login("test@email.com", "abcabc")
        self.test_status = CheckTestStatus(self.driver)
        self.courses = RegisterCoursesPage(self.driver)

    def test_example(self):
        time.sleep(3)

        self.courses.enter_course_name("JavaScript")
        assert True