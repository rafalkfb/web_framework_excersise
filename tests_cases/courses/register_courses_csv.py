import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
from utilities.checkteststatus import CheckTestStatus
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
from pages.home.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("one_time_set_up")
@ddt
class RegisterCoursesCSVTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        # self.courses_url = "https://courses.letskodeit.com/courses"
        # self.log_page = LoginPage(self.driver)
        # self.log_page.login("test@email.com", "abcabc")
        self.test_status = CheckTestStatus(self.driver)
        self.courses = RegisterCoursesPage(self.driver)
        self.navigation_panel = NavigationPanel(self.driver)

    def setUp(self) -> None:
        yield
        # return to all page courses after each test
        self.navigation_panel.click_all_courses()

    @pytest.mark.run(order=1)
    @data(*get_csv_data("testdata.csv"))  # * means there could be multiple arguments
    @unpack
    def test_course_page_enter(self, course_name, credit_card_num, credit_card_exp, credit_card_cvv):
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(credit_card_num, credit_card_exp, credit_card_cvv)
        result = self.courses.verify_enroll_failed()
        self.test_status.mark_final("is error displayed", result, "error is not displayed")
