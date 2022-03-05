import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
from utilities.checkteststatus import CheckTestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class RegisterCoursesMultiplyTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        # self.courses_url = "https://courses.letskodeit.com/courses"
        # self.log_page = LoginPage(self.driver)
        # self.log_page.login("test@email.com", "abcabc")
        self.test_status = CheckTestStatus(self.driver)
        self.courses = RegisterCoursesPage(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", 5168284143633642, 1224, 324),
          ("Learn Python 3 from scratch", 5168284143633642, 1224, 324))
    @unpack
    def test_course_page_enter(self, course_name, credit_card_num, credit_card_exp, credit_card_cvv):
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(credit_card_num, credit_card_exp, credit_card_cvv)
        result = self.courses.verify_enroll_failed()
        self.test_status.mark_final("is error displayed", result, "error is not displayed")
        self.courses.element_click("ALL COURSES", 'linktext')
