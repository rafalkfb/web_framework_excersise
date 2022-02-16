import time
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
from utilities.checkteststatus import CheckTestStatus


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        # self.courses_url = "https://courses.letskodeit.com/courses"
        # self.log_page = LoginPage(self.driver)
        # self.log_page.login("test@email.com", "abcabc")
        self.test_status = CheckTestStatus(self.driver)
        self.courses = RegisterCoursesPage(self.driver)

    @pytest.mark.run(order=1)
    def test_course_page_enter(self):
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_to_enroll("JavaScript for beginners")
        self.courses.enroll_course(5168284143633642, 1224, 324)
        time.sleep(2)

        result = self.courses.verify_enroll_failed()
        self.test_status.mark_final("is error displayed", result, "error is not displayed")
