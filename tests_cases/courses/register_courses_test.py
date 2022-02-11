import time
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
from utilities.checkteststatus import CheckTestStatus


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.courses_url = "https://courses.letskodeit.com/courses"
        # self.log_page = LoginPage(self.driver)
        # self.log_page.login("test@email.com", "abcabc")
        self.test_status = CheckTestStatus(self.driver)
        self.courses = RegisterCoursesPage(self.driver)

    @pytest.mark.run(order=1)
    def test_course_page_enter(self):
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_to_enroll("JavaScript for beginners")
        result = self.courses.verify_title_match("JavaScript for beginners")
        self.test_status.mark_final("Check if entered course page successfully", result, "Course page didn't open")

    @pytest.mark.run(order=2)
    def test_buy(self):
        # self.courses.click_enroll_submit_button()
        # self.courses.scroll_down()
        self.courses.enroll_course(5168284143633642, 1224, 324)
        # self.courses.screen_shot("card info")
        time.sleep(1)
        res = self.courses.verify_enroll_failed()
        self.test_status.mark_final(test_name="is error displayed", result=res, result_message="error is not displayed")

